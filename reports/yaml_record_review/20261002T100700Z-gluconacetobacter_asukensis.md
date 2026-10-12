# YAML Record Review: Gluconacetobacter asukensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/gluconacetobacter_asukensis.yaml
- Started UTC: 2026-10-02T10:07:00Z
- Finished UTC: 2026-10-02T10:07:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017181` |
| Label | `Gluconacetobacter asukensis` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:89583` |
| Parent label | `Gluconacetobacter` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `4` |
| Type strain | `kgmicrobe.strain:bacdive_133744` |
| Source attestations | `NCBITAXON`, `LPSN`, `GTDB`, `BACDIVE`, `GOLD`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/gluconacetobacter_asukensis.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/gluconacetobacter_tumulicola.yaml data/taxa/bacteria/spirosoma_sp_hdk211.yaml data/taxa/bacteria/gluconacetobacter_asukensis.yaml data/taxa/bacteria/bacillus_sp_ku7.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: 625960 records were expected, 625960 were found on disk, and 0 were missing, extra, or differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 1047 lines, 9 lineage entries, 1 LPSN nomenclature entry, 1 GTDB taxonomy mapping, 2 NCBI synonyms, 2 xrefs, 4 BacDive strains, and 6 source attestations. |
| Exact report lookup | Pass: `rg --no-ignore --hidden --files reports/yaml_record_review -g '*gluconacetobacter_asukensis.md'` found no prior report for this stem. |
| Direct source probes | Pass: ignored-inclusive exact-ID and source-ID scans found matching rows in NCBI Taxonomy, LPSN, GTDB, BacDive, GOLD, MADIN, AllTheBacteria, StrainInfo, and strain crosswalk raw inventories. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10267 maps `NCBITaxon:1017181` to `gluconacetobacter_asukensis`.
- `curation/seed_scope.tsv` row 8700 keeps this taxon in scope as `Gluconacetobacter asukensis` with 6 sources including NCBI.
- `data/raw/ncbitaxon_taxa.tsv` row 218601 names the exact NCBI taxon as `Gluconacetobacter asukensis`, `SPECIES`, parent `NCBITaxon:89583`, and genetic code `11`.
- The 9 YAML lineage entries match raw NCBI rows for root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Acetobacterales, Acetobacteraceae, and Gluconacetobacter.
- `grounding_status: EXACT` and `mapping_status: SEEDED` match a direct seeded NCBI Taxonomy record backed by additional curated source rows.

## Evidence

- The `NCBITAXON` attestation agrees with `data/raw/ncbitaxon_taxa.tsv` row 218601 and its 2026-09-13 snapshot.
- The LPSN nomenclature block agrees with `data/raw/lpsn_names.tsv` row 27073: `lpsn:790084`, `Gluconacetobacter asukensis`, species rank, `Tazato et al. 2012`, a validly published legitimate correct-name status, type strain `kgmicrobe.strain:JCM-17772`, publications `PMID:22038998`, `DOI:10.1099/ijs.0.034595-0`, `DOI:10.1099/ijs.0.047837-0`, and sequence accession `INSDC:AB627120`.
- The GTDB mapping agrees with `data/raw/gtdb_species.tsv` row 70486 and `data/raw/gtdb_mappings.tsv` row 1176: `GTDB:s__Gluconacetobacter_asukensis` maps to `NCBITaxon:1017181` with `skos:closeMatch` and 2 genomes.
- The 2 NCBI synonyms in YAML are exactly the alternative-name pipe list on the raw NCBI row.
- `data/raw/bacdive_strains.tsv` rows 56054 and 84635 through 84637 account for all 4 BacDive strains and for the 4 culture-collection IDs on the type strain.
- `data/raw/culture_collection_strains.tsv` rows 10445, 103287, 104052 through 104054, 126750, and 140744 ground the BCRC, JCM, LMG, and NCIMB strain aliases to `NCBITaxon:1017181`.
- `data/raw/strain_assemblies.tsv` rows 31862 through 31878 and `data/raw/strain_genome_records.tsv` rows 25144 through 25152 support the type-strain INSDC, BV-BRC, GOLD, GTDB, and NCBI Assembly genome assertions for `LMG 27724` and `JCM 17772`.
- `data/atb/genome_links.tsv` rows 4740 through 4744 connect `atb.assembly:202505.SAMN14650886` and `biosample:SAMN14650886` to the `LMG 27724` type-strain evidence.
- `data/raw/strain_related_records.tsv` rows 86147 through 86184 back the BioProject, BioSample, GOLD analysis, GOLD organism, and GOLD project related-record blocks.
- `data/straininfo/assemblies.tsv` row 2519 and `data/straininfo/strain_links.tsv` rows 15274 through 15276 back `straininfo.strain:380878` and the JCM, LMG, and NCIMB deposit records.
- `data/raw/gold_organisms.tsv` row 294 and `data/raw/madin_taxa.tsv` row 472 agree with the GOLD organism count 3 and MADIN assertion count 9 in `source_attestations`.

## Completeness

- The generated YAML is complete for the maintained raw rows reviewed here: it carries NCBI identity and synonyms, LPSN nomenclature, GTDB mapping, GOLD and MADIN taxon attestations, all 4 BacDive strains, genome records, related records, AllTheBacteria sample links, and StrainInfo cross-links.
- `strain_count: 4` agrees with the 4 BacDive rows for `NCBITaxon:1017181`.
- The record has no `causal_graphs` block; none is expected from the seeded taxon, strain, genome, project, and trait-count inputs.
- `just verify-corpus` reproduced this generated record from maintained inputs, so future edits belong in `data/raw/`, `data/atb/`, `data/straininfo/`, `curation/seed_scope.tsv`, or the seeder rather than in this YAML directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/gluconacetobacter_asukensis.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/gluconacetobacter_asukensis.yaml`.
- Re-run `just verify-corpus`.
- Re-run ignored-inclusive exact source probes after any refresh of `data/raw/`, `data/atb/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence and uniqueness checks used `--no-ignore --hidden`, so ignored files were included.
- The review read the full 1047-line YAML and checked the generated sections for lineage, nomenclature, taxonomy mapping, NCBI synonyms, xrefs, 4 nested strains, source attestations, and curation history.
- The source scan intentionally treated `data/straininfo/` and `data/atb/` as maintained inventories because the curation history lists those alongside `data/raw/`.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10267 |
| `curation/seed_scope.tsv` | 8700 |
| `data/raw/ncbitaxon_taxa.tsv` | 218601 |
| `data/raw/lpsn_names.tsv` | 27073 |
| `data/raw/gtdb_mappings.tsv` | 1176 |
| `data/raw/bacdive_strains.tsv` | 56054, 84635-84637 |
| `data/raw/strain_assemblies.tsv` | 31862-31878 |
| `data/raw/strain_related_records.tsv` | 86147-86184 |
| `data/straininfo/strain_links.tsv` | 15274-15276 |
| `data/taxa/bacteria/gluconacetobacter_asukensis.yaml` | 1 and 1007 |

