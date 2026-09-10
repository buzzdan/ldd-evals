---
# cluster: ≥2 hunters converge on "Catalog.Find"; the report must render a
# 🔗 CLUSTER entry naming it (by the anchor or its last segment).
# members: CASE-E.nil-return
type: regex
pattern: '(?i:\bcluster\b)[^\n]*\b(Catalog\.Find|Find)\b'
match: contains
target: last_message
---
