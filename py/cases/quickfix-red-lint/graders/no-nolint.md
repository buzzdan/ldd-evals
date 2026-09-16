---
# hard limit: never add a suppression — not even for escalations; ruff's noqa
# and mypy's type: ignore alike
type: regex
pattern: '# noqa|# type: ignore'
match: count:0
target: files
---
