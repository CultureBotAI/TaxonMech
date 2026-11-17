# YAML Record Review: Candidatus Poribacteria bacterium WGA-4C

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/candidatus_poribacteria_bacterium_wga_4c.yaml
- Started UTC: 2026-10-02T17:09:49Z
- Finished UTC: 2026-10-02T17:09:49Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1027271` |
| Label | `Candidatus Poribacteria bacterium WGA-4C` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:2894089` |
| Parent label | `unclassified Candidatus Poribacteria` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/candidatus_poribacteria_bacterium_wga_4c.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/azalea_little_leaf_phytoplasma.yaml data/taxa/bacteria/candidatus_poribacteria_bacterium_wga_4c.yaml data/taxa/bacteria/bacterium_c37.yaml data/taxa/bacteria/enterobacter_sp_w001.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 50 lines, 7 lineage entries, 0 synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 2 source attestations. |
| Direct bounded-source fallback | Pass: found one seed row, one first-column NCBI Taxonomy row, and one GOLD aggregate row with 2 organism assertions; confirmed all 7 first-column lineage rows; and found no auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:1027271` trace only to PATHS, the seed row, the NCBI Taxonomy row, the GOLD aggregate row, the legacy page path row, and the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10947 maps `NCBITaxon:1027271` to `candidatus_poribacteria_bacterium_wga_4c`.
- `curation/seed_scope.tsv` row 57219 keeps this taxon in scope with an attested NCBI+GOLD rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218780 names `NCBITaxon:1027271` as `Candidatus Poribacteria bacterium WGA-4C`, under `NCBITaxon:2894089` / `unclassified Candidatus Poribacteria`.
- `data/raw/gold_organisms.tsv` row 331 preserves the exact same taxon with 2 GOLD organism assertions.
- The generated YAML line 1 preserves the NCBI identifier and lines 34 and 40 preserve the NCBI and GOLD source IDs.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy and GOLD source rows in the 2026-09-13 generated corpus.
- The NCBI row supplies no synonyms, matching the absence of a `synonyms` block.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:2894089` / `unclassified Candidatus Poribacteria`.

## Completeness

- The record is complete for the exact NCBI Taxonomy and GOLD aggregate rows currently present for this species taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no external taxonomy mapping is currently present for `NCBITaxon:1027271`.
- No external xrefs, genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/candidatus_poribacteria_bacterium_wga_4c.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/candidatus_poribacteria_bacterium_wga_4c.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 10947, `curation/seed_scope.tsv` row 57219, `data/raw/ncbitaxon_taxa.tsv` row 218780, `data/raw/gold_organisms.tsv` row 331, and YAML lines 1, 34, and 40.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/candidatus_poribacteria_bacterium_wga_4c.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/candidatus_poribacteria_bacterium_wga_4c.yaml` directly.
