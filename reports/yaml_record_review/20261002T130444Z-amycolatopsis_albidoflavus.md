# YAML Record Review: Amycolatopsis albidoflavus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/amycolatopsis_albidoflavus.yaml
- Started UTC: 2026-10-02T13:04:44Z
- Finished UTC: 2026-10-02T13:04:44Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102226` |
| Label | `Amycolatopsis albidoflavus` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:1813` |
| Parent label | `Amycolatopsis` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `1` |
| Source attestations | `BACDIVE`, `BACTOTRAITS`, `GOLD`, `GTDB`, `LPSN`, `MADIN`, `MEDIADIVE`, `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/amycolatopsis_albidoflavus.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/uncultured_bacterium_env_os_ace8.yaml data/taxa/bacteria/pseudonocardia_sp_imsnu_22071.yaml data/taxa/bacteria/amycolatopsis_albidoflavus.yaml data/taxa/bacteria/pseudonocardia_kongjuensis.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 872 lines, 9 lineage entries, 1 LPSN nomenclature entry, 1 GTDB mapping, 6 synonyms, 1 xref, 1 BacDive strain, 8 source attestations, and no causal graphs. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper expects a simple exact NCBI source and is not applicable to this multi-source species rollup. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:102226` trace to NCBI Taxonomy, LPSN, GTDB, BacDive, MediaDive, GOLD, MADIN, BactoTraits, strain, assembly, related-record, and seed-scope inputs represented in the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10549 maps `NCBITaxon:102226` to `amycolatopsis_albidoflavus`.
- `curation/seed_scope.tsv` row 2030 keeps this taxon in scope with an attested eight-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17845 names `NCBITaxon:102226` as `Amycolatopsis albidoflavus` with parent `NCBITaxon:1813`.
- `data/raw/lpsn_names.tsv` row 15264 contributes the `lpsn:773196` misspelling entry, type-strain designations, publications, and `INSDC:AJ252832`; row 1102 contributes the corrected `lpsn:5931` synonym.
- `data/raw/gtdb_mappings.tsv` row 1192 contributes the `GTDB:s__Amycolatopsis_albidoflava` `skos:closeMatch` mapping with 7 genomes.

## Evidence

- The YAML identifier, species rank, label, parent taxon, lineage, and genetic code agree with the NCBI Taxonomy row and snapshot 2026-09-13.
- The LPSN block at YAML lines 36-61 preserves the Lee and Hah 2001 species name as a legitimate but inaccurate spelling and links it to the corrected `Amycolatopsis albidoflava` name.
- The synonym block at lines 68-88 preserves the GTDB, LPSN, and four NCBI synonyms for the corrected spelling, authority-bearing names, and `Pseudonocardia sp. IMSNU 22139`.
- The `bacdive:13244` strain is represented as G495-11, `is_type_strain: true`, with the JCM 11300 assembly, genome, BioProject, BioSample, GOLD, NCBI Assembly, BV-BRC, GTDB, and StrainInfo evidence nested under the strain.
- Direct MediaDive, GOLD, MADIN, and BactoTraits aggregate rows exist for `NCBITaxon:102226`, matching the corresponding source attestations at YAML lines 846-865.

## Completeness

- `strain_count: 1` matches the single BacDive strain materialized in the `strains` block.
- `taxonomy_mappings` contains only the GTDB species mapping because no other exact external taxonomy mapping row is present for `NCBITaxon:102226`.
- No top-level `genomes` or `causal_graphs` blocks are expected for this generated species record; assembly and related-record evidence is nested under the matched BacDive strain.
- The corrected LPSN spelling and GTDB mapping are retained as synonym and mapping evidence without changing the exact NCBI identifier under review.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/amycolatopsis_albidoflavus.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/amycolatopsis_albidoflavus.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct raw/curation exact-ID and `bacdive_13244` strain scans after any refresh of BacDive, LPSN, GTDB, GOLD, MediaDive, MADIN, BactoTraits, StrainInfo, or ATB source inventories.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10549 |
| `curation/seed_scope.tsv` | 2030 |
| `data/raw/ncbitaxon_taxa.tsv` | 17845 |
| `data/raw/lpsn_names.tsv` | 15264 and 1102 |
| `data/raw/gtdb_mappings.tsv` | 1192 |
| `data/raw/bacdive_strains.tsv` | 13084 |
| `data/raw/gold_organisms.tsv` | 317 |
| `data/raw/mediadive_taxa.tsv` | 75 |
| `data/raw/madin_taxa.tsv` | 491 |
| `data/raw/bactotraits_taxa.tsv` | 54 |
| `data/taxa/bacteria/amycolatopsis_albidoflavus.yaml` | 1, 36, 62, 93, and 822 |

- Future corrections belong in source extraction, matching, or the seeder, not in `data/taxa/bacteria/amycolatopsis_albidoflavus.yaml` directly.
