---
name: review-open-issues
description: Sweep and triage the full open-issue queue for TaxonMech. Fetches every open issue, checks each against main, the corpus, the inventories and the docs, flags duplicates and already-fixed items, and assigns a priority tier (P0 silently wrong data, P1 real-but-schedulable, P2 process/doc, P3 backlog). Produces a short ranked report; only touches GitHub when asked. Use when asked to "review issues", "prioritize the backlog", "triage open issues", or after a review pass has filed a batch of new issues.
tools: Bash, Read
category: workflow
requires_database: false
requires_internet: true
version: 1.0.0
---

# Review & Prioritize Open Issues

Adapted from the `review-open-issues` skill in the sibling Mech repositories.
The method and the read-only default are unchanged; what a check consists of
is specific to this repository: a generated, gated corpus whose issues are
about mappings, identifiers, scope and pipeline gates.

## What makes this repo different

**1. Everything is on disk and checkable.** Records, inventories, pages and
the scope are all committed. "Cannot verify" is rarely honest; the honest
failure is *did not look*. Cite the file, the `just report` line, or the live
lookup that established a verdict.

**2. The dominant defect is a mapping, not a typo.** Every identifier came
from an inventory, so a wrong value is a wrong upstream mapping (LPSN name to
NCBI taxon, GTDB predicate) or a wrong seeder rule. Check by opening the
source page, and say whether the fix belongs in kg-microbe, the seeder or the
scope.

**3. Generated artifacts are gated, so drift is loud.** `pages/`, the README
block and the corpus are rebuilt by `just render`, `just docs-stats` and
`just seed-apply`; `just qc` fails on drift. Check `just qc` before believing
an issue about a stale page or count.

**4. Records are `SEEDED` until a human reads them.** An issue alleging a
wrong fact is a candidate for human review, not a second LLM pass.

## Workflow

### Step 1 — Fetch the full open-issue queue

```bash
queue_file="${TMPDIR:-/tmp}/taxonmech-open-issues.json"
gh issue list -R CultureBotAI/TaxonMech --state open --limit 5000 \
  --json number,title,body,labels,comments,createdAt,updatedAt > "$queue_file"
jq -r '.[] | [.number, .createdAt[:10], (.labels|map(.name)|join(",")), .title] | @tsv' "$queue_file"
jq length "$queue_file"
```

`--limit` caps silently; print `jq length` and say whether coverage was
complete.

### Step 2 — Establish the state of the tree

```bash
git fetch origin main && git status -sb | head -1
just report
just qc
```

If `just qc` fails on `main`, that is the first finding.

Classify each issue: **verifiable now**, **decision** (needs the owner),
**human review** (alleges a factual error in a SEEDED record), **upstream**
(belongs in kg-microbe or claw).

### Step 3 — Group and dedupe

Group by PR reference, module, or the same failure shape, and report a group
as one item.

### Step 4 — Check each issue against current reality

- **Already fixed on main?** `git log --oneline origin/main --perl-regexp --grep "#<N>\b"`.
- **Identifier claims** — resolve them at NCBI, LPSN, GTDB or BacDive.
- **Still reproducible?** Confirm the script, test or field still exists.
- **Title still true?** Re-derive counts with `just report`.

### Step 5 — Assign priority

- **P0 — silently wrong data.** A record whose identity, lineage or mapping
  is wrong and passes every gate.
- **P1 — real, schedulable.** A gate gap that would let a P0 through, a
  missing test with a known failure, a scope decision waiting on data.
- **P2 — process or doc.**
- **P3 — backlog.**
- **`decision`**, **`human-review`** and **`upstream`** are orthogonal labels.

### Step 6 — Present the report

Ranked list, P0 first, one line per issue or group. Separate **fixed in
code**, **needs a decision**, **needs a human reader**, **belongs upstream**
and **still open**. Recommend the top 2–3 to act on next with reasoning.
State the count reviewed and what `just qc` said on `main`.

### Step 7 — Act only when asked

Read-only by default. Closing, relabelling and retitling are writes; confirm
first, then one at a time with evidence in the comment. No @-mentions without
explicit per-mention authorization.
