#!/usr/bin/env bash
# quickfix-clean-tree postcheck: the scaffold is untouched — no commit, no dirty file.
set -uo pipefail
. "$(dirname "$(readlink -f "$0")")/../postcheck/lib.sh"

assert_eq "no commit after the scaffold base" "$(commits_since_base)" 0
assert_eq "working tree clean (nothing edited)" "$(git -C "$EVAL_DIR" status --porcelain | grep -c .)" 0
finish
