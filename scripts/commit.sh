#!/usr/bin/env bash
# Commit only the given paths, retrying if another process holds the git index lock.
# Usage: scripts/commit.sh "commit subject" path [path ...]
set -euo pipefail
cd "$(dirname "$0")/.."

subject="$1"
shift

msg="$subject

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01BpmvtUycaEsNxR45eZcGc3"

for attempt in $(seq 1 20); do
  if git add -- "$@" 2>/dev/null && git commit -q -m "$msg" --only -- "$@" 2>/tmp/commit_err.$$; then
    git log --oneline -1
    exit 0
  fi
  if grep -q "nothing to commit\|no changes added" /tmp/commit_err.$$ 2>/dev/null; then
    echo "nothing to commit"
    exit 0
  fi
  sleep $((RANDOM % 3 + 1))
done
echo "commit failed after retries:" >&2
cat /tmp/commit_err.$$ >&2
exit 1
