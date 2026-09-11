---
# cluster: ≥2 hunters converge on "Job.Kind"; the report must render a
# 🔗 CLUSTER entry naming it (by the anchor or its last segment).
# members: R11.Q1.job-kind-if
type: regex
pattern: '(?i:\bcluster\b)[^\n]*\b(Job\.Kind|Kind)\b'
match: contains
target: last_message
---
