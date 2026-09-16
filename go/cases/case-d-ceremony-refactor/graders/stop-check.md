---
type: regex
pattern: 'Stop check\W*\n\W*1\W{1,6}gates\b[^\n]*\n\W*2\W{1,6}re-run\b[^\n]*\n\W*3\W{1,6}nouns?\b[^\n]*\n\W*4\W{1,6}critic\b[^\n]*\n\W*5\W{1,6}STOP\b[^\n]*\n\W*6\W{1,6}commit\b'
flags: i
match: contains
target: last_message
---
The refactoring skill's exit is its `Stop check` block: six lines, each opening with
the step number and keyword (`1 gates`, `2 re-run`, `3 nouns`, `4 critic`, `5 STOP`,
`6 commit`), copied verbatim into the message that ends the turn whichever path
invoked the skill — standalone, the workflow's ship summary or quickfix's. The pattern
reads those six openings in order and tolerates markdown around them (`1.`, `**gates**`,
an em dash); it fails a prose account of the steps, a block missing a line, and a run
that never rendered the block at all. Checked against the go-2.11.0-c78b55f traces:
case-e's final message passes, the other six refactor runs fail.
