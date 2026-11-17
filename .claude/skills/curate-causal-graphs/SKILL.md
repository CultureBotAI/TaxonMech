---
name: curate-causal-graphs
description: Assess and curate TaxonMech causal graphs only through verified native
  maintained inputs and gates; report prerequisite gaps without changing generated
  or unsupported fields.
---

# TaxonMech causal graphs

Read [native contract](../../../docs/CURATION.md),
[the schema](../../../src/taxonmech/schema/taxonmech.yaml), current `CLAUDE.md`,
`justfile`, native validators and tests before deciding whether writes are
supported. `TaxonRecord.causal_graphs` supports GENE_OR_PROTEIN nodes with `grounding`,
`xrefs` and `description`; no typed `protein_examples` field exists. Exact
protein references must preserve organism/strain, source and role scope without
collapsing a family or complex to an instance. Generated `data/taxa` records
must reproduce from maintained inputs; never hand-edit them.

## Verify prerequisites before applying

At the 2026-10-19 local checkout inspection, the curation guide marks curator
graph overlays as future work; current inspected seeder/justfile expose no
maintained graph-overlay route. Schema support alone does not make graph writes
reproducible.

These are current-checkout observations, not permanent assertions about published
main. Search hidden/ignored source and existing branches for the required route;
when reporting current published capability, pin and inspect the published
revision. If another session has implemented it, read its writer, validator,
provenance and canary tests and prove reproduction before using it. Do not
silently cherry-pick, switch or overwrite the active session's checkout.

While prerequisites are absent, complete the useful source-grounded inventory,
claim review and proposed native graph/protein candidate table, with exact IDs,
source locators, source scope and unresolved representation requirements. Save
an honest blocked/partial assessment using the native record-review contract.
Keep the curation goal blocked rather than marking unsupported writes complete.
A separately authorized prerequisite implementation must add maintained inputs,
a validated writer, semantic checks, history, derived-output handling and a
round-trip/canary test before corpus application. Merely adding this skill does
not supply that implementation. Preserve generated records and native status.

After verified prerequisites land, follow the current native contract and
`curate-yaml-record`, run its focused and full gates, and record evidence that
new assertions survive regeneration. Use actual documented commands, not the
names of planned recipes.
## Scope and completion

For one target, read the whole maintained record and its generated projection or
components. For a corpus goal, first freeze an inventory of record IDs, paths,
input hashes and applicable graph/protein elements; resume that ledger after an
interruption. Include hidden and ignored inputs when establishing absence.
Classify each target as checked, changed, evidence-limited, excluded, not
applicable or blocked, with reasons and inspected sources. A sample, a provider
report and a validator pass do not establish whole-corpus scientific completion.

Use [curate-yaml-record](../curate-yaml-record/SKILL.md) for the local evidence,
write, history and status contract; this adapter does not replace its managed
method. Record actual agent identity. Preserve scientific status rules and
unrelated edits. Use inspected primary evidence for mechanistic claims and exact
active identifiers for instances; never infer causality from association or
coverage from an empty query. A quotation is source text; interpretation belongs
in the native notes/explanation field.

Save final scientific assessments through
[review-yaml-record](../review-yaml-record/SKILL.md),
[record reviews](../../../docs/record-reviews.md), and the
[local profile](../../../docs/record-review-profile.md), including their native
persistence exceptions. Keep coverage/checkpoint accounting even when a clean
review should not produce a bundle. Unavailable prerequisites remain blocked;
a skipped target is not a completed enrichment. This skill authorizes no paid
provider call by itself.

After a completed goal, follow the user's authorized commit, push/PR,
adversarial review, issue/fix, merge and branch-cleanup sequence under the current
repository guidance. Carry forward existing authorization without asking again.
Use fresh required checks and native merge-queue rules. Verify actual merge and
landed content before deleting that feature branch or starting the next goal.
Only genuine review findings become issues; a no-diff goal needs a documented
no-op receipt rather than an artificial commit.
