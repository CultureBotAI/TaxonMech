# Curation history

Append-only provenance for curation sessions. **One record per change** — per
target for hand curation, per *migration* for a bulk edit. Written once and
**never edited afterwards**; corrections go in a new record that references the
old one in its `details`.

```
history/<kind-dir>/<slug>/<TIMESTAMP>-<actor>-<shortid>.yaml
```

The schema (`src/taxonmech/schema/history.yaml`) and the scaffolder's
contract are vendored from culturebotai-claw; the conventions below are this
repository's.

## Why this exists

Per-record `curation_history` says what changed inside one record. It cannot
say that a source mapping was re-read at the source, that a gate was adopted
and what it found, or that a review deliberately changed nothing. Git says a
commit happened; it does not say which model, using which tool, changed what,
why, and under which issue.

## Writing a record

Do not hand-write the filename or timestamp — scaffold it:

```bash
just new-history --kind record --slug escherichia_coli \
  --target-root data/taxa/bacteria \
  --event REVIEW --outcome no_change \
  --sections nomenclature,strains \
  --summary "Checked the LPSN correct name and type strain against LPSN" \
  --model claude-fable-5 --agent-tool claude-code \
  --issue https://github.com/CultureBotAI/TaxonMech/issues/1 \
  --details "What was done, what evidence was used, how it was validated."
```

Omit `--details` and you get a TODO placeholder — `just validate-history`
**fails** while it is still there. The command prints the record path as its
final stdout line.

`--kind record` and `--kind schema` derive the target path from `--slug` plus
`--target-root`. Every other kind should pass an explicit `--path`.

Then validate and stage:

```bash
just validate-history history/records/escherichia_coli/<file>.yaml
git add history/
```

## The vocabulary

`event`: `CREATE` · `EDIT` · `REVIEW` · `AUDIT` · `GENERAL`

`outcome`: `changed` · `no_change` · `needs_followup` · `blocked`

`kind`: `record` · `schema` · `mapping` · `report` · `infrastructure` · `other`
(`other` requires an explicit `--path`).

## One record per CHANGE, not per file

| what happened | `--kind` | target |
|---|---|---|
| one taxon, curated | `record` | that taxon's YAML |
| a re-seed, re-extraction or bulk edit | `infrastructure` | the script that made it |
| a schema change | `schema` | the schema file |
| the scope grew or shrank | `other` | `curation/seed_scope.tsv` |
| a research note | `other` | the note under `research/` |

## What is checked

`just validate-history` (inside `just qc`) validates every record against the
vendored schema and checks that its links resolve. Records are append-only by
convention, not by a gate; a corrected record is a new record that names the
old one.
