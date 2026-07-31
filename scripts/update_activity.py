"""
Refreshes the "Latest Activity" block inside README.md.

Fetches the authenticated user's most recent public GitHub events and
rewrites the content between the START_ACTIVITY / END_ACTIVITY markers.
Designed to run inside the update-readme.yml GitHub Action, but works
locally too if GH_USER / GH_TOKEN are exported.
"""

import os
import re
import sys
from datetime import datetime

import requests

USER = os.environ.get("GH_USER", "")
TOKEN = os.environ.get("GH_TOKEN", "")
README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")

START_MARK = "<!--START_ACTIVITY-->"
END_MARK = "<!--END_ACTIVITY-->"

EVENT_LABELS = {
    "PushEvent": "Pushed to",
    "PullRequestEvent": "Opened a pull request in",
    "IssuesEvent": "Opened an issue in",
    "CreateEvent": "Created a branch/tag in",
    "ReleaseEvent": "Published a release in",
    "WatchEvent": "Starred",
    "ForkEvent": "Forked",
}


def fetch_events():
    url = f"https://api.github.com/users/{USER}/events/public"
    headers = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    return resp.json()


def format_line(event):
    label = EVENT_LABELS.get(event["type"], event["type"])
    repo = event["repo"]["name"]
    when = datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ")
    return f"- **{label}** [`{repo}`](https://github.com/{repo}) &mdash; {when.strftime('%b %d, %Y')}"


def build_block(events, limit=5):
    lines = [format_line(e) for e in events[:limit]]
    if not lines:
        lines = ["- No recent public activity yet."]
    return "\n".join(lines)


def main():
    if not USER:
        print("GH_USER not set, skipping.")
        sys.exit(0)

    try:
        events = fetch_events()
        block = build_block(events)
    except Exception as exc:  # noqa: BLE001
        print(f"Could not fetch activity, leaving README untouched: {exc}")
        sys.exit(0)

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        re.escape(START_MARK) + r".*?" + re.escape(END_MARK), re.DOTALL
    )
    replacement = f"{START_MARK}\n{block}\n{END_MARK}"

    if not pattern.search(content):
        print("Markers not found in README.md, skipping.")
        sys.exit(0)

    new_content = pattern.sub(replacement, content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("README.md activity block updated.")


if __name__ == "__main__":
    main()
