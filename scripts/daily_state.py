"""Exit 10 for a completed daily scan, 0 otherwise. Never accesses the network."""
import sys
from pathlib import Path

import yaml


def main():
    path = Path(__file__).resolve().parents[1] / 'data' / 'runs.yaml'
    runs = yaml.safe_load(path.read_text(encoding='utf-8'))['runs']
    return 10 if any(r.get('kind') == 'daily' and str(r.get('scan_date')) == sys.argv[1] for r in runs) else 0


if __name__ == '__main__':
    sys.exit(main())
