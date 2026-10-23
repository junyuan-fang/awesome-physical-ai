# Scheduled daily curation agent for awesome-physical-ai.
#
# Runs from a durable clone (not the session worktree, whose .git file is
# Windows-only and unreadable from WSL):
#   - WSL Ubuntu provides Python and runs fetch / apply / validate.
#   - Windows git commits and pushes (the clone is a normal repository).
#   - Claude Code headless fills the review stub when it is still unfilled.
#
# Logs: pipeline/logs/daily-YYYY-MM-DD.log
# Register (once):
#   schtasks /Create /SC DAILY /ST 08:00 /TN "awesome-physical-ai daily" ^
#     /TR "powershell.exe -NoProfile -ExecutionPolicy Bypass -File <this file>"
#
param(
    [string]$Day = (Get-Date).ToString("yyyy-MM-dd"),
    [switch]$Preflight
)

$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent $PSScriptRoot
Set-Location $repo
$wslRepo = "/mnt/" + $repo.Substring(0, 1).ToLower() + ($repo.Substring(2) -replace '\\', '/')
$logDir = Join-Path $repo "pipeline\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$log = Join-Path $logDir "daily-$Day.log"

function Log($m) { $m | Tee-Object -FilePath $log -Append }

Log "=== daily run $Day ($repo) ==="

if ($Preflight) {
    Log "preflight: repo=$repo wsl=$wslRepo"
    wsl -d Ubuntu -- bash -lc "cd $wslRepo && python3 --version && python3 scripts/validate.py" *>> $log
    if ($LASTEXITCODE -ne 0) { Log "preflight failed"; exit $LASTEXITCODE }
    Log ("git status: " + ((git -C $repo status --short) -join "; "))
    Log "preflight OK"
    exit 0
}

# Sync the branch: master once the v2 scripts are merged there, otherwise feat/curation-v2.
git -C $repo fetch origin --prune *>> $log
git -C $repo cat-file -e "origin/master:scripts/fetch_candidates.py" 2>$null
$branch = if ($LASTEXITCODE -eq 0) { "master" } else { "feat/curation-v2" }
Log "branch: $branch"
git -C $repo checkout $branch *>> $log
git -C $repo pull --rebase --autostash origin $branch *>> $log
if ($LASTEXITCODE -ne 0) { Log "pull failed"; exit $LASTEXITCODE }

# 1. Fetch candidates and write the review stub (Python lives in WSL).
wsl -d Ubuntu -- bash -lc "cd $wslRepo && bash scripts/run_daily.sh fetch $Day" *>> $log
if ($LASTEXITCODE -ne 0) { Log "fetch failed"; exit $LASTEXITCODE }

$review = Join-Path $repo "pipeline\reviews\$Day.yaml"
if (Select-String -Path $review -Pattern "triage: null" -Quiet) {
    Log "review stub unfilled — invoking agent"
    $prompt = @"
You are the daily reviewer for the awesome-physical-ai repository at $repo.
The review stub is $review. Read docs/METHODOLOGY.md and docs/REVIEWER_GUIDE.md,
then fill every item in the stub: triage for all; for includes also scores C/E/O/T
(1-5 with a one-line Chinese rationale each), evidence_read, one_liner, summary
(~300-400 Chinese characters), tags, affiliations, venue, open, uses, new_resources.
Use pipeline/cache/papers/<arxiv_id>.md as the primary source; open arXiv/project/repo
pages only when a score hinges on a fact the cache lacks. Do not change category/route/
contribution already set on the stub. Keep every item and its arxiv_id. Do not ask questions.
If you need to run Python, use `wsl -d Ubuntu -- bash -lc '...'`; the Windows python3 is a
Microsoft Store stub.
"@
    & "C:\Users\Administrator\.local\bin\claude.exe" -p $prompt --add-dir $repo --allowedTools "Read,Write,Edit,Glob,Grep,Bash(wsl *),Bash(git *)" --output-format text *>> $log
    if ($LASTEXITCODE -ne 0) { Log "agent failed"; exit $LASTEXITCODE }
}
if (Select-String -Path $review -Pattern "triage: null" -Quiet) { Log "review still unfilled"; exit 2 }

# 2. Apply, recheck, render, validate (WSL).
wsl -d Ubuntu -- bash -lc "cd $wslRepo && bash scripts/run_daily.sh apply $Day" *>> $log
if ($LASTEXITCODE -ne 0) { Log "apply failed"; exit $LASTEXITCODE }

# 3. Commit and push (Windows git; never force-push).
git -C $repo add data digests docs README.md pipeline/reviews topics
if ((git -C $repo status --porcelain).Length -gt 0) {
    git -C $repo -c user.name="junyuan-fang" -c user.email="fangjunyuan1@gmail.com" commit -m "chore: daily scan $Day"
    if ($LASTEXITCODE -ne 0) { Log "commit failed"; exit $LASTEXITCODE }
    git -C $repo push origin "HEAD:$branch"
    if ($LASTEXITCODE -ne 0) { Log "push failed"; exit $LASTEXITCODE }
} else {
    Log "no changes to commit"
}

Log "=== done $Day ==="
exit 0
