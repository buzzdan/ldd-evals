---
# cluster: ≥2 hunters converge on "Catalog.find"; the report must render a
# 🔗 CLUSTER entry naming it (by the anchor or its last segment).
# members: CASE-E.nil-return
type: regex
pattern: '(?i:\bcluster\b)[^\n]*\b(Catalog\.find|find)\b|(?i:\bclusters?\b)[^\n]*(?:\n[^\n]*){0,8}?\n[ \t]*(?:[-*•]|[0-9]+[.)])[ \t]*\**\x60?(Catalog\.find|find)\b'
match: contains
target: last_message
---
