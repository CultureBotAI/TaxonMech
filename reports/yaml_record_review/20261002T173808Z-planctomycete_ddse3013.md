# YAML Record Review: planctomycete DDSe3013

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/planctomycete_ddse3013.yaml
- Started UTC: 2026-10-02T17:38:08Z
- Finished UTC: 2026-10-02T17:38:08Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1027572` |
| Label | `planctomycete DDSe3013` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:69476` |
| Parent label | `unclassified Planctomycetaceae` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/planctomycete_ddse3013.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/planctomycete_ddsw3010.yaml data/taxa/bacteria/planctomycete_ddse3011.yaml data/taxa/bacteria/planctomycete_ddse3012.yaml data/taxa/bacteria/planctomycete_ddse3013.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 54 lines, 10 lineage entries, 0 synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| Direct bounded-source fallback | Pass: found one seed row and one first-column NCBI Taxonomy row; confirmed all 10 first-column lineage rows; and found no GOLD aggregate or auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:1027572` trace only to PATHS, the seed row, the NCBI Taxonomy row, and the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 11023 maps `NCBITaxon:1027572` to `planctomycete_ddse3013`.
- `curation/seed_scope.tsv` row 319370 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218854 names `NCBITaxon:1027572` as `planctomycete DDSe3013`, under `NCBITaxon:69476` / `unclassified Planctomycetaceae`.
- The generated YAML line 1 preserves the NCBI identifier and line 43 preserves the sole NCBI source ID.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The NCBI row supplies no synonyms, matching the absence of a `synonyms` block.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:69476` / `unclassified Planctomycetaceae`.

## Completeness

- The record is complete for the exact NCBI row currently present for this species taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, exact GOLD, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no external taxonomy mapping is currently present for `NCBITaxon:1027572`.
- No external xrefs, genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/planctomycete_ddse3013.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/planctomycete_ddse3013.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 11023, `curation/seed_scope.tsv` row 319370, `data/raw/ncbitaxon_taxa.tsv` row 218854, and YAML lines 1 and 43.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/planctomycete_ddse3013.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/planctomycete_ddse3013.yaml` directly.
