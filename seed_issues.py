"""For club leads: create every weekly task in issues.json as a GitHub Issue.

Needs the GitHub CLI (https://cli.github.com) and `gh auth login`.

    python seed_issues.py OWNER/snapsnipe            # create labels + issues
    python seed_issues.py OWNER/snapsnipe --dry-run  # just print what would happen

Then on GitHub: Projects → New project → Board, and add the issues
(filter by label "week-3", "week-4", ... to drop them in one week at a time).
"""
import json
import subprocess
import sys
from pathlib import Path

COLORS = ["5319e7", "1d76db", "0e8a16", "fbca04", "d93f0b", "b60205"]


def gh(*args, dry):
    print("gh", " ".join(args[:4]), "...")
    if not dry:
        subprocess.run(["gh", *args], check=True)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    repo, dry = sys.argv[1], "--dry-run" in sys.argv
    weeks = json.loads(Path(__file__).with_name("issues.json").read_text())

    for i, week in enumerate(weeks):
        label = f"week-{week['week']}"
        gh("label", "create", label, "--repo", repo, "--force",
           "--color", COLORS[i % len(COLORS)],
           "--description", f"{week['date']} · {week['gm']}", dry=dry)
        for issue in week["issues"]:
            body = (f"**Week {week['week']} · {week['date']} · {week['gm']} ({week['speaker']})**\n"
                    f"Goal: {week['goal']}\n\n{issue['body']}")
            gh("issue", "create", "--repo", repo, "--title", f"[W{week['week']}] {issue['title']}",
               "--body", body, "--label", label, dry=dry)


if __name__ == "__main__":
    main()
