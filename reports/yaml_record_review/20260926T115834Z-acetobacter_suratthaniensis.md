# YAML Record Review: Acetobacter suratthaniensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacter_suratthaniensis.yaml
- Reviewed UTC: 2026-09-26T11:58:34Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | TaxonRecord |
| Identifier | NCBITaxon:1502841 |
| Label | Acetobacter suratthaniensis |
| Rank / domain | SPECIES / BACTERIA |
| Parent | NCBITaxon:434, Acetobacter |
| Record status | Generated YAML; seeded from maintained inventories and curation/seed_scope.tsv |
| PATHS row | data/taxa/PATHS.tsv:189339 |
| Raw NCBI row | data/raw/ncbitaxon_taxa.tsv:385928 |
| Scope row | curation/seed_scope.tsv:15816 |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/acetobacter_suratthaniensis.yaml` | Pass; no issues found |
| `just validate-strict data/taxa/bacteria/acetobacter_sp_zs_43.yaml data/taxa/bacteria/acetobacter_sp_zym8.yaml data/taxa/bacteria/acetobacter_sp_zym9.yaml data/taxa/bacteria/acetobacter_suratthaniensis.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |
| YAML summary helper | Pass; 128 lines, 9 lineage entries, 1 LPSN nomenclature row, 1 GTDB mapping, 5 synonyms, 2 xrefs, 1 BacDive strain, 0 genome assemblies, 0 genome records, and 0 related records |
| Bounded source scan | Pass; exact NCBI and seed-scope rows found, all 9 lineage entries checked, no lineage mismatches, 1 LPSN row, 1 GTDB row, 1 BacDive row, 2 culture-collection rows, 1 GOLD aggregate row, 11 NCBI type-material rows, 1 NCBI merged-ID side row, and no generated StrainInfo overlay rows |
| Exact ignored-aware source scan | Pass; `rg --no-ignore --hidden` found the expected exact NCBI, scope, LPSN, GTDB, GOLD, BacDive, culture-collection, type-material, and old-ID rows |

## Identity and Grounding

- `NCBITaxon:1502841`, label `Acetobacter suratthaniensis`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, and snapshot `2026-09-13` match the exact source row in `data/raw/ncbitaxon_taxa.tsv:385928`.
- `grounding_status: EXACT` is appropriate because the record identifier is the exact NCBI taxon ID used as the source identity.
- `mapping_status: SEEDED` is consistent with the single matching `curation/seed_scope.tsv:15816` row.
- The bounded NCBI scan resolved all 9 root-first lineage entries and found no missing ancestors or label, rank, or parent mismatches.

## Evidence

- The LPSN nomenclature assertion is supported by `data/raw/lpsn_names.tsv:31178`, which identifies `lpsn:794706` as a non-deprecated, legitimate, validly published correct-name row for `Acetobacter suratthaniensis`.
- The LPSN authority `Pitiwittayakul et al. 2016`, type strain `kgmicrobe.strain:NBRC-111399`, URL `https://lpsn.dsmz.de/species/acetobacter-suratthaniensis`, publications `DOI:10.1007/s13213-016-1200-z` and `DOI:10.1099/ijsem.0.001585`, and sequence accession `INSDC:AB937774` match the exact LPSN row.
- The GTDB `skos:closeMatch` to `GTDB:s__Acetobacter_suratthaniensis` is supported by `data/raw/gtdb_mappings.tsv:32669`, with `genome_count: 2` matching the GTDB `source_attestations` genome assertion count.
- The BacDive strain `kgmicrobe.strain:bacdive_167719` is supported by `data/raw/bacdive_strains.tsv:89952`: BacDive ID `167719`, designation `AI32`, target `NCBITaxon:1502841`, LPSN row `lpsn:794706`, culture IDs `kgmicrobe.strain:BCC-26087` and `kgmicrobe.strain:NBRC-111399`, and type-strain status all agree with the YAML.
- `data/raw/gold_organisms.tsv:11778` records 2 retained organisms for this NCBI taxon, matching the `GOLD` / `ORGANISM` source attestation.
- `data/raw/ncbi_merged_ids.tsv:18025` maps old ID `NCBITaxon:1502838` into `NCBITaxon:1502841`; no retained retired source row was present, so the record correctly has no generated `replaces` entry.
- The 11 exact NCBI type-material rows name culture-collection aliases for the type material but do not themselves create additional generated local strains beyond the exact BacDive and culture-collection rows.
- Native StrainInfo has one direct target row and one exact deposit hit in the local JSON snapshot, but `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1502841`; no StrainInfo assembly or related-record YAML entry is missing.

## Completeness

- The generated NCBI identity, LPSN nomenclature, GTDB mapping, NCBI/LPSN synonyms, xrefs, BacDive type strain, GOLD aggregate attestation, and seed history are complete for the pinned local rows.
- The five synonym entries match the NCBI and LPSN synonym inputs, including the NCBI exact synonym spelling `Acetobacter suratthanensis` and the LPSN related-name row for the same spelling.
- `strain_count: 1` is complete: the one exact BacDive row is present, its two culture-collection identifiers are represented, and no exact strain assembly, strain genome, or strain related-record rows exist for this taxon.
- No BactoTraits, Madin et al., MediaDive, ATB, curated definition, causal graph, generated genome, or generated related-record section is warranted by the checked source rows.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. If upstream LPSN, GTDB, BacDive, GOLD, NCBI type-material, or StrainInfo inventories change, regenerate the taxon records and rerun the same exact source, schema, and strict validation checks.

## Additional Notes

- Duplicate preflight used ignored-file `find` over `reports/yaml_record_review` and found no existing report for this stem before this file was written.
- Native GOLD and StrainInfo snapshot rows are exact side evidence; without generated final strain assembly, genome, or related-record rows, they do not imply additional child YAML entries.
- The generated YAML was left read-only; any future correction would belong in a maintained source inventory, seeder logic, or `curation/seed_scope.tsv`.
