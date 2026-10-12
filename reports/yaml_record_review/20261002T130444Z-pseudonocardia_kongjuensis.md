# YAML Record Review: Pseudonocardia kongjuensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudonocardia_kongjuensis.yaml
- Started UTC: 2026-10-02T13:04:44Z
- Finished UTC: 2026-10-02T13:04:44Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102227` |
| Label | `Pseudonocardia kongjuensis` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:1847` |
| Parent label | `Pseudonocardia` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `2` |
| Source attestations | `BACDIVE`, `BACTOTRAITS`, `GOLD`, `GTDB`, `LPSN`, `MADIN`, `MEDIADIVE`, `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/pseudonocardia_kongjuensis.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/uncultured_bacterium_env_os_ace8.yaml data/taxa/bacteria/pseudonocardia_sp_imsnu_22071.yaml data/taxa/bacteria/amycolatopsis_albidoflavus.yaml data/taxa/bacteria/pseudonocardia_kongjuensis.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 814 lines, 9 lineage entries, 1 LPSN nomenclature entry, 1 GTDB mapping, 2 synonyms, 2 xrefs, 2 BacDive strains, 8 source attestations, and no causal graphs. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper expects a simple exact NCBI source and is not applicable to this multi-source species rollup. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:102227` trace to NCBI Taxonomy, LPSN, GTDB, BacDive, MediaDive, GOLD, MADIN, BactoTraits, strain, assembly, related-record, and seed-scope inputs represented in the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10550 maps `NCBITaxon:102227` to `pseudonocardia_kongjuensis`.
- `curation/seed_scope.tsv` row 1218 keeps this taxon in scope with an attested eight-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17846 names `NCBITaxon:102227` as `Pseudonocardia kongjuensis` with parent `NCBITaxon:1847`.
- `data/raw/lpsn_names.tsv` row 19393 contributes `lpsn:780179`, the LPSN name details, type-strain designations, publications, the GTDB xref, and `INSDC:AJ252833`.
- `data/raw/gtdb_mappings.tsv` row 1193 contributes the `GTDB:s__Pseudonocardia_kongjuensis` `skos:closeMatch` mapping with 2 genomes.

## Evidence

- The YAML identifier, species rank, label, parent taxon, lineage, and genetic code agree with the NCBI Taxonomy row and snapshot 2026-09-13.
- The LPSN block at YAML lines 36-58 preserves the exact species name, Lee et al. 2001 authority, correct-name status, four type-strain designations, three publications, and `INSDC:AJ252833`.
- The GTDB mapping at lines 59-65 preserves `GTDB:s__Pseudonocardia_kongjuensis`, `skos:closeMatch`, and `genome_count: 2`.
- The `bacdive:13383` strain is represented as LM 157, `is_type_strain: true`, with the JCM 11896 assembly, genome, BioProject, BioSample, GOLD, NCBI Assembly, BV-BRC, GTDB, and StrainInfo evidence nested under the strain.
- The additional `bacdive:156989` strain is represented with the `kgmicrobe.strain:CCUG-68249%20Q` culture-collection id.
- Direct MediaDive, GOLD, MADIN, and BactoTraits aggregate rows exist for `NCBITaxon:102227`, matching the corresponding source attestations at YAML lines 788-807.

## Completeness

- `strain_count: 2` matches the two BacDive strains materialized in the `strains` block.
- `taxonomy_mappings` contains only the GTDB species mapping because no other exact external taxonomy mapping row is present for `NCBITaxon:102227`.
- No top-level `genomes` or `causal_graphs` blocks are expected for this generated species record; assembly and related-record evidence is nested under matched BacDive strains.
- The generated record retains both NCBI related synonyms, `Pseudonocardia kongjuensis Lee et al. 2001` and `soil bacterium LM 157`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/pseudonocardia_kongjuensis.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/pseudonocardia_kongjuensis.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct raw/curation exact-ID and BacDive strain scans after any refresh of BacDive, LPSN, GTDB, GOLD, MediaDive, MADIN, BactoTraits, StrainInfo, or ATB source inventories.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10550 |
| `curation/seed_scope.tsv` | 1218 |
| `data/raw/ncbitaxon_taxa.tsv` | 17846 |
| `data/raw/lpsn_names.tsv` | 19393 |
| `data/raw/gtdb_mappings.tsv` | 1193 |
| `data/raw/bacdive_strains.tsv` | 13220 and 79229 |
| `data/raw/gold_organisms.tsv` | 318 |
| `data/raw/mediadive_taxa.tsv` | 76 |
| `data/raw/madin_taxa.tsv` | 492 |
| `data/raw/bactotraits_taxa.tsv` | 55 |
| `data/taxa/bacteria/pseudonocardia_kongjuensis.yaml` | 1, 36, 59, 78, and 764 |

- Future corrections belong in source extraction, matching, or the seeder, not in `data/taxa/bacteria/pseudonocardia_kongjuensis.yaml` directly.
