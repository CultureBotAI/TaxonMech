# YAML Record Review: Acetobacter sp. P5B1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacter_sp_p5b1.yaml
- Started UTC: 2026-09-26T11:06:38Z
- Finished UTC: 2026-09-26T11:08:16Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | TaxonRecord |
| Identifier | NCBITaxon:2762620 |
| Label | Acetobacter sp. P5B1 |
| Rank / domain | SPECIES / BACTERIA |
| Parent | NCBITaxon:2628570, unclassified Acetobacter |
| GTDB mapping | GTDB:s__Acetobacter_cerevisiae, skos:closeMatch, 10 genomes |
| Record status | Generated YAML; seeded from maintained inventories and curation/seed_scope.tsv |
| Raw NCBI row | data/raw/ncbitaxon_taxa.tsv:551971 |
| Raw GTDB row | data/raw/gtdb_mappings.tsv:214412 |
| Scope row | curation/seed_scope.tsv:101669 |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/acetobacter_sp_p5b1.yaml` | Pass; no issues found |
| `just validate-strict data/taxa/bacteria/acetobacter_sp_p1h12_c.yaml data/taxa/bacteria/acetobacter_sp_p5b1.yaml data/taxa/bacteria/acetobacter_sp_pa2_2.yaml data/taxa/bacteria/acetobacter_sp_pg_2009.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |
| YAML summary helper | Pass; 73 lines, 10 lineage entries, 1 NCBITAXON/NAME attestation, 1 GTDB/GENOME attestation, 1 GTDB mapping, 1 GTDB exact synonym, 0 strains |
| Bounded source scan | Pass; exact NCBI, GTDB, and seed-scope rows found; no lineage mismatches, no merged IDs, no exact strain source rows |
| Exact ignored-aware source scan | Pass; `rg --no-ignore --hidden` across raw, catalog, BacDive, GOLD, ATB, StrainInfo, curation, and history paths found the exact NCBI/scope/GTDB rows and same-label GTDB species rows on neighboring Acetobacter taxa |

## Identity and Grounding

- `NCBITaxon:2762620`, label `Acetobacter sp. P5B1`, rank `SPECIES`, parent `NCBITaxon:2628570`, genetic code `11`, source list `ncbitaxon|gtdb`, and snapshot `2026-09-13` match `data/raw/ncbitaxon_taxa.tsv:551971`.
- `grounding_status: EXACT` is appropriate because the record identifier is the exact NCBI taxon ID used as the source identity.
- The GTDB mapping to `GTDB:s__Acetobacter_cerevisiae` is exactly supported by `data/raw/gtdb_mappings.tsv:214412`, including `skos:closeMatch` and `genome_count: 10`.
- The GTDB exact synonym and `xrefs` entry mirror that mapping row without broadening the NCBI identity to the named Acetobacter cerevisiae species record.
- `mapping_status: SEEDED` is consistent with the single matching `curation/seed_scope.tsv:101669` row.
- The bounded NCBI scan resolved all 10 root-first lineage entries and found no missing ancestors or label/rank mismatches.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact NCBI row, and the `GTDB` source attestation is supported by the exact GTDB mapping row.
- The NCBI raw row has blank synonym fields and no retirement target, matching the absence of NCBI-derived synonyms and retained old IDs.
- Native GOLD contains one organism, one project, and one analysis row for NCBI taxon `2762620`; there is no projected `data/raw/gold_organisms.tsv` hit and no raw strain, assembly, genome, or related-record hit, so those source rows do not require a strain/genome block in this generated YAML.
- The bounded scan found no exact rows for this target in LPSN, Madin, BactoTraits, MediaDive, BacDive, StrainInfo, strain genome, strain assembly, strain related-record, or NCBI type-material inventories.

## Completeness

- `strain_count: 0` is complete for the committed strain inventories: exact BacDive, StrainInfo, aggregate GOLD, strain assembly, strain genome, and related-record scans all returned zero rows for `NCBITaxon:2762620`.
- No nomenclature, BacDive strains, StrainInfo deposits, genome links, related records, definitions, or causal graphs are warranted by the scanned exact rows.
- The ignored-aware exact scan included history and report paths and did not reveal a prior review report for this stem before this file was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. Future GTDB or GOLD projection changes should re-run the exact NCBI, GTDB, native GOLD, strain-source, schema, and strict validation checks before changing maintained inputs.

## Additional Notes

- Duplicate preflight used `find reports/yaml_record_review -maxdepth 1 -name '*-acetobacter_sp_p5b1.md' -print`, which includes ignored report files, and found no existing report for this stem before this file was written.
- The generated YAML was left read-only; any future correction would belong in a maintained source inventory, seeder logic, or `curation/seed_scope.tsv`.
