# YAML Record Review: Paenimyroides anatoliense

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/paenimyroides_anatoliense.yaml
- Started UTC: 2026-10-02T08:45:06Z
- Finished UTC: 2026-10-02T08:45:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017018` |
| Label | `Paenimyroides anatoliense` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:3085669` |
| Parent label | `Paenimyroides` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `1` |
| Source attestations | `NCBITAXON`, `LPSN`, `BACDIVE`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/paenimyroides_anatoliense.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/capnocytophaga_gingivalis.yaml data/taxa/bacteria/enterobacter_sp_jdm_19.yaml data/taxa/bacteria/paenimyroides_anatoliense.yaml data/taxa/bacteria/escherichia_coli_c54_58_1b.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 215 lines, 11 lineage entries, 1 nomenclature record, 10 synonyms, 1 BacDive strain, and 4 source attestations. |
| `taxonmech_bounded_scan.py data/taxa/bacteria/paenimyroides_anatoliense.yaml` | Not applicable: the NCBI-only helper exited with `NCBI source mismatch` because the record intentionally combines NCBITaxon, LPSN, BacDive, and MADIN evidence. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*paenimyroides_anatoliense.md'` | Pass: no prior report existed for this stem. |
| Exact NCBI, LPSN, BacDive, MADIN, type-material, culture-collection, and StrainInfo scans | Pass: all inspected source rows agree with the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10183 maps `NCBITaxon:1017018` to `paenimyroides_anatoliense`.
- `curation/seed_scope.tsv` row 22134 keeps this species in scope with an attested four-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218518 names the same species, parent genus, rank, genetic code, exact synonyms, related synonyms, and source set `ncbitaxon|bacdive|lpsn|madin_etal`.
- `data/raw/lpsn_names.tsv` row 7241 backs the LPSN nomenclature block and marks the name as validly published and legitimate but deprecated as a synonym of a later correct name.
- The generated `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for the directly attested NCBI species.

## Evidence

- `source_attestations` accurately summarize the four asserted source families: NCBITaxon name, LPSN name, BacDive strain, and MADIN trait assertions.
- LPSN rows 1574, 7232, 7241, and 27772 support the LPSN synonym set for `Myroides anatoliensis`, `Paenimyroides anatoliensis`, `Paenimyroides anatoliense`, and `Flavobacterium anatoliense`.
- `data/raw/bacdive_strains.tsv` row 56140 supports strain `kgmicrobe.strain:bacdive_133830`, BacDive ID 133830, designation MK3, and the two LMG/NCCB culture-collection IDs.
- `data/straininfo/strain_links.tsv` rows 15338 and 15339 support the two StrainInfo deposits and the two mirrored `STRAININFO_STRAIN` related records.
- `data/raw/madin_taxa.tsv` row 459 supports the direct MADIN `TRAIT_ASSERTION` assertion count of 4.

## Completeness

- The single BacDive strain is represented as type material with both culture-collection identifiers.
- NCBI type-material rows 1099-1105 and culture-collection rows 126434 and 137742 support the type-strain placement asserted in the YAML.
- The maintained LPSN synonyms are represented, including the spelling variant `Paenimyroides anatoliensis`.
- No GTDB, GOLD, MediaDive, or BactoTraits attestation is maintained for this NCBI row, and none is asserted.
- No causal graph is expected for this generated taxon identity record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/paenimyroides_anatoliense.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/paenimyroides_anatoliense.yaml`.
- Re-run the LPSN, BacDive, MADIN, and StrainInfo source scans after any source refresh.

## Additional Notes

- The source scans used `--no-ignore --hidden`, so ignored files were included.
- The four `STRAININFO` related records intentionally use two deposits on one StrainInfo strain ID.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10183 |
| `curation/seed_scope.tsv` | 22134 |
| `data/raw/ncbitaxon_taxa.tsv` | 218518 |
| `data/raw/lpsn_names.tsv` | 1574, 7232, 7241, 27772 |
| `data/raw/bacdive_strains.tsv` | 56140 |
| `data/raw/madin_taxa.tsv` | 459 |
| `data/straininfo/strain_links.tsv` | 15338 and 15339 |
| `data/raw/ncbi_type_material.tsv` | 1099-1105 |
| `data/taxa/bacteria/paenimyroides_anatoliense.yaml` | 1, 188, 194, 200, and 205 |
