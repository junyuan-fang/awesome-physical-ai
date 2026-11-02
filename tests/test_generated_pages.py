"""Keep the generated navigation compact, complete, and locally navigable."""
from collections import Counter
import re
import sys
import unittest
from urllib.parse import unquote, urlsplit
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import generate_readme as generator


class GeneratedPagesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = generator.render_all()
        cls.papers = generator.load('papers.yaml', 'papers')

    def test_homepage_has_a_fixed_reading_budget(self):
        for path in ('README.md', 'README.zh-CN.md'):
            with self.subTest(path=path):
                home = self.pages[path]
                self.assertLessEqual(len(home.splitlines()), 130)
                self.assertLessEqual(len(home.encode('utf-8')), 12000)
                self.assertLessEqual(len(re.findall(r'^- \*\*\[', home, re.M)), generator.HOME_PICKS)
                self.assertNotIn('<details', home)

    def test_homepages_share_picks_language_switch_and_star_history(self):
        en, zh = self.pages['README.md'], self.pages['README.zh-CN.md']
        self.assertIn('[简体中文](README.zh-CN.md)', en)
        self.assertIn('[English](README.md)', zh)
        self.assertEqual(re.findall(r'docs/papers/[\d.]+\.md', en), re.findall(r'docs/papers/[\d.]+\.md', zh))
        for page in (en, zh):
            self.assertIn('![Star History Chart](https://api.star-history.com/svg?repos=junyuan-fang/awesome-physical-ai&type=Date)', page)
            self.assertIn(f'**{generator.compute_total(generator.SCORE_EXAMPLE)}/100', page)

    def test_every_paper_has_one_detail_page_and_one_catalog_entry(self):
        expected = {str(p['arxiv_id']) for p in self.papers}
        details = {Path(path).stem for path in self.pages if path.startswith('docs/papers/')}
        self.assertEqual(details, expected)
        appearances = Counter()
        for path, content in self.pages.items():
            if not path.startswith('docs/catalog/'):
                continue
            entries = re.findall(r'^\d+\. \*\*\[.*?\]\(../papers/(\d{4}\.\d{4,5})\.md\)', content, re.M)
            self.assertLessEqual(len(entries), generator.PAGE_SIZE, path)
            appearances.update(entries)
        self.assertEqual(appearances, Counter({aid: 1 for aid in expected}))

    def test_local_links_and_explicit_anchors_resolve(self):
        for relative, content in self.pages.items():
            source = generator.ROOT / relative
            for raw in re.findall(r'\]\(([^\s)]+)\)', content):
                url = urlsplit(raw)
                if url.scheme or url.netloc:
                    continue
                target = (source.parent / unquote(url.path)).resolve() if url.path else source
                self.assertTrue(target.exists(), f'{relative}: {raw}')
                if url.fragment and target.suffix == '.md':
                    text = target.read_text(encoding='utf-8')
                    self.assertIn(f'id="{unquote(url.fragment)}"', text, f'{relative}: {raw}')

    def test_details_preserve_full_reviews(self):
        for paper in self.papers:
            text = self.pages[f"docs/papers/{paper['arxiv_id']}.md"]
            if paper.get('summary'):
                self.assertIn(paper['summary'], text)
            self.assertIn(str(paper.get('authors', '')), text)
            for affiliation in paper.get('affiliations') or []:
                self.assertIn(affiliation, text)
            self.assertNotIn('**- 权重', text)

    def test_identical_data_produces_identical_pages(self):
        self.assertEqual(self.pages, generator.render_all())


if __name__ == '__main__':
    unittest.main()
