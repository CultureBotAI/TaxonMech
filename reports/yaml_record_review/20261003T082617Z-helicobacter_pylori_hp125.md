# YAML Record Review: Helicobacter pylori HP125

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_hp125.yaml`
- Started UTC: 2026-10-03T08:25:46Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T08:26:17Z
- Verdict: pass with minor issues

## Target

The entire generated `TaxonRecord` was read. It represents `NCBITaxon:103170`,
Helicobacter pylori HP125, not the parent species or another HP-numbered taxon.
It declares rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:210`, `EXACT`
grounding and `SEEDED` mapping status. It has ten root-first lineage entries,
genetic code 11, zero attached BacDive strains, one NCBI name attestation and
one 2026-09-13 seeding event. The target is at `data/taxa/PATHS.tsv:13120`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_hp125.yaml`: passed,
  no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_hp125.yaml`:
  passed, one file scanned and zero errors.
- Structured YAML/TSV checks confirmed the target label, stored rank, parent
  and genetic code, and every ID, label, rank and parent link in the ten-entry
  lineage against `data/raw/ncbitaxon_taxa.tsv`. A complete inventory scan
  found zero direct children, ruling out missed descendant strain aggregation
  within this snapshot.
- `just verify-corpus` was not rerun: the documented recipe is full-corpus-only.
  Focused inventory agreement is not a new full-corpus reproduction pass.
- `just validate-products` was not run because this record has no causal
  graph. `just validate-history` was not run because the bounded target search
  found no separate history artifact. The embedded event was inspected and
  covered by strict validation; no history artifact was created.
- Full catalog hash/census and rendered-site checks were not rerun. No source
  inventories, generated record or page were changed.

## Identity and Grounding

The inspected [NCBI HP125 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103170&lvl=&mode=node)
agrees on taxon ID, scientific name, code 11 and displayed lineage through
Helicobacter pylori. NCBI's species tree separately lists HP125, HP112 and
HP131. Ancestor IDs and ranks also agree with the committed inventory.

The accessible browser reports `no rank`; the pinned inventory and YAML
report `STRAIN`. The conflict is retained as a minor finding rather than
silently choosing one source representation. Identity and immediate-parent
placement are unaffected. An unranked taxon directly below a species is still
in scope under the repository rules.

## Evidence

| Assertion | Inspected support |
| --- | --- |
| Identity, stored rank, parent and code | `data/raw/ncbitaxon_taxa.tsv:18337` supplies NCBITaxon:103170, the HP125 label, STRAIN, parent 210, code 11 and snapshot 2026-09-13. The browser-rank discrepancy is explicitly qualified above. |
| Scientific name | `data/catalog/ncbi_names-0000.jsonl.gz:38350` contains the exact scientific-name assertion. |
| Attestation | The taxonomy inventory has `attested_by=ncbitaxon`; the YAML carries one `NAME` assertion for this taxon, not a phenotype or genome assertion. |
| Inclusion and history | `curation/seed_scope.tsv:143998` supplies the 2026-09-13 inclusion and one-source rationale retained by the embedded seeding event. It does not record human review approval. |

The YAML has no literature citation, LPSN name, GTDB mapping, BacDive deposit,
assembly accession or causal edge requiring further claim-level verification.
Parent-species and sibling-strain evidence was not copied into this record.

## Completeness

Identifier, exact label and slug were searched with `rg --no-ignore --hidden`
in TSV/YAML/Markdown files under `data/raw/`, `data/atb/`, `data/straininfo/`,
`curation/`, `history/` and `reports/yaml_record_review/`. Only the taxonomy
and scope rows matched; no previous target report or separate history artifact
was found.

Ignored-file-inclusive `rg -z` searches also covered JSONL.GZ, TSV.GZ and
TSV.XZ files under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`
and `data/straininfo/`. Queries included the ID, exact label, slug, numeric
taxonomy-field forms and standalone designation HP125. Only the NCBI
scientific-name row matched. These are bounded source-surface checks, not a
claim that no external source or biological genome exists.

The zero attached-strain count and omitted optional source fields are
consistent with the maintained evidence. No definition, phenotype assertion,
causal graph or species-level nomenclature needs to be invented for HP125.

## Findings

- **Blocker:** None found.
- **Major:** None found.
- **Minor (1): Unresolved NCBI rank discrepancy.** The browser says `no rank`,
  while the pinned taxonomy inventory and YAML say `STRAIN`.
  `src/taxonmech/ncbi_taxdump.py:load_taxdump` directly normalizes the source
  rank's case and spaces; it does not infer strain rank from the name.
  The original archive pinned by `conf/ncbi_taxdump.yaml` is unavailable in
  this checkout, so the source-version-versus-importer cause was not resolved.
  Ownership lies with the pinned NCBI input/configuration and importer, not
  the generated YAML. The same pattern was independently observed for HP112;
  this does not by itself prove a corpus-wide importer defect.

## Recommended Edits

No immediate YAML edit is justified. Inspect the original, hash-verified
`nodes.dmp` row for 103170 and compare a dated current NCBI source. If the
pinned source says `strain`, preserve reproducibility until an authorized
refresh. If it says `no rank`, correct the extraction/inventory integration
owning that discrepancy, with a regression test, before regeneration. Keep
the current label, parent and evidence scope unless new exact-target evidence
supports a change.

## Follow-up Checks

1. Recover the archive configured in `conf/ncbi_taxdump.yaml` with SHA256
   `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`
   and inspect its exact rank field for this taxon.
2. For a separately authorized correction, test the changed import path,
   including relevant `tests/test_ncbi_taxdump.py` coverage, re-extract and
   use `just seed-canary NCBITaxon:103170`.
3. Repeat both target validators and run the full `just verify-corpus` after
   regeneration; do not replace the pinned source merely to match a browser
   page without recording a proper source refresh.

## Additional Notes

The live page was reached from NCBI's species-tree link. Earlier in this same
review session, an ignored-file-inclusive repository filename search for
taxdump/nodes artifacts found the configuration, importer, test and bytecode
but no archive or `nodes.dmp`; the configured `data/source_snapshots/` directory
was unavailable. No claim is made about copies outside the repository.

iModulonDB is not applicable to this taxonomy-only record. No paid research,
external messages, GitHub mutations, history additions or review-status
promotion were performed.
