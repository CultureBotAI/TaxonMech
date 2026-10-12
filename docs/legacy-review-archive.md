# Historical Review Archive

The Markdown files under `reports/yaml_record_review/` are historical
observations, preserved byte-for-byte in PR #115. They were produced under
earlier review instructions, not the current structured-review contract.
Importing them does not rerun their checks, validate their scientific claims,
resolve their findings, or promote any taxon to `REVIEWED`.

## Coverage Is Not A Verdict

At import, 23,883 distinct records have one report each, out of 625,960 indexed
taxon records. There are 602,077 records without an archived report.

| Domain | Records with an archived report | Indexed records |
| --- | ---: | ---: |
| Archaea | 555 | 14,013 |
| Bacteria | 17,085 | 605,695 |
| Eukaryota | 6,243 | 6,243 |
| Other | 0 | 9 |

Eukaryota therefore has complete **historical report-file coverage**, not a
guarantee of complete scientific assessment, passing verdicts, or resolution of
all findings. This publication does not re-review Eukaryota or any other record.

Older reports vary in layout and depth. Some record only pinned-source and
deterministic checks; others inspect live primary evidence. Some omit explicit
verdicts, timestamps, or sections. A filename timestamp is not evidence of the
actual review duration. A `pass` string is the original author's scoped verdict,
not a new assessment. Never infer a pass from missing metadata or `None found`.

## Inventory And Integrity

[The tab-separated inventory](legacy-review-inventory.tsv) records every report's
relative path, SHA-256, exact target ID and path, verbatim standard verdict/time
fields, and missing metadata/sections. Empty fields mean **not recorded in that
standard field**, not a negative result. The parser does not interpret free text
or normalize alternate verdicts such as `clean` or `fail`.

The imported inventory has 787 reports without a standard verdict field,
3,927 missing at least one standard metadata field, and 389 missing at least
one of the nine expected sections. Two further reports have nonstandard heading
layouts without missing a required section. These are format observations,
not retrospective scientific verdicts. In particular, the 22,402 original
`pass` fields do not establish 22,402 current scientific passes.

Target IDs come from `data/taxa/PATHS.tsv`; each report must mention its indexed
ID and an unambiguous same-slug target path that exists. These checks establish
an archive association, not scientific identity. They do not re-read taxon YAML
or verify old claims about source contents, commands, input hashes, or evidence.

```bash
uv run python scripts/legacy_review_inventory.py --check --base origin/main
uv run pytest -q tests/test_legacy_review_inventory.py
```

The checker enumerates hidden and ignored Markdown too, detects duplicate or
unmatched targets and inventory drift, and rejects changes/deletions to reports
already present in the specified base. The default base is `RECORD_REVIEW_BASE`
in CI and `HEAD` locally. Unknown bases fail. The normal test suite includes
the complete archive check; no new shared-contract exception is introduced.

`--write` regenerates only the derived inventory after deliberate inspection;
it still rejects rewrites of base reports. Do not use it to conceal historical
changes. Original extra final blank lines in 594 reports are intentionally
retained; the archive is not reformatted to silence blank-at-EOF warnings.

## Findings Remain Open

Reports with `needs curation`, `fail`, or other findings remain historical
observations requiring evidence-backed triage. For example, the
[Amylostereum chailletii report](../reports/yaml_record_review/20260921T123028Z-amylostereum_chailletii.md)
contains major findings. Its presence in this archive does not fix or close them.
Publication issues #116 and #117 concern archive clarity and integrity only;
resolving them does not dispose of scientific findings in individual reports.

For any new or successor review, follow the
[current native profile](record-review-profile.md) and
[structured-review contract](record-reviews.md). Save authoritative YAML and
derived Markdown under `reviews/structured/`, retaining original report links
as historical context. Do not invent missing timestamps, reviewer independence,
input hashes, issue dispositions, or claims of reassessment through automatic
conversion. A later clean review cannot silently retire an earlier finding.

The inventory is not a structured bundle and does not count toward structured
review coverage. Correct scientific records only through their maintained
owners and guarded regeneration, never by editing generated taxon YAML or
rewriting these historical reports.
