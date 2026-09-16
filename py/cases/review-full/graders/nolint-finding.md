---
# pre-commit-review step 1: every # noqa / # type: ignore directive in scope is its own finding
type: regex
pattern: 'noqa|type: ignore'
match: contains
target: last_message
---
