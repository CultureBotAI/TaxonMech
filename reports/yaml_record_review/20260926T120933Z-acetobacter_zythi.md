# YAML Record Review: Acetobacter zythi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacter_zythi.yaml
- Reviewed UTC: 2026-09-26T12:09:33Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | TaxonRecord |
| Identifier | NCBITaxon:2959295 |
| Label | Acetobacter zythi |
| Rank / domain | SPECIES / BACTERIA |
| Parent | NCBITaxon:434, Acetobacter |
| PATHS row | data/taxa/PATHS.tsv:400658 |
| Record status | Generated YAML; seeded from maintained inventories and curation/seed_scope.tsv |
| Scope row | curation/seed_scope.tsv:50069 |

## Validation

| Check | Result |
| --- | --- |
| Duplicate report preflight | Pass; ignored-file `find` over `reports/yaml_record_review` found no existing `*-acetobacter_zythi.md` report |
| `just validate data/taxa/bacteria/acetobacter_zythi.yaml` | Pass; no issues found |
| `just validate-strict data/taxa/bacteria/acetobacter_tropicalis_nbrc_101654.yaml data/taxa/bacteria/acetobacter_tropicalis_nric_0312.yaml data/taxa/bacteria/acetobacter_vaccinii.yaml data/taxa/bacteria/acetobacter_zythi.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |
| YAML summary helper | Pass; 103 lines, 9 lineage entries, 1 LPSN nomenclature row, 1 GTDB mapping, 1 GTDB exact synonym, 2 NCBI related synonyms, 2 xrefs, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records |
| Bounded source scan | Pass; exact NCBI, seed-scope, LPSN, GTDB, and NCBI type-material rows checked with no lineage mismatches and no BacDive, GOLD, StrainInfo, BactoTraits, MediaDive, Madin et al., or NCBI merged-ID rows for this species |
| Exact ignored-aware source scan | Pass; `rg --no-ignore --hidden` covered curation, raw, ATB, StrainInfo, and history paths and found the expected exact same-taxon rows |

## Identity and Grounding

- `NCBITaxon:2959295`, label `Acetobacter zythi`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, two NCBI related synonyms, and snapshot `2026-09-13` match `data/raw/ncbitaxon_taxa.tsv:579255`.
- `grounding_status: EXACT` is appropriate because the record identifier is the exact NCBI taxon ID used as the source identity.
- `mapping_status: SEEDED` is consistent with `curation/seed_scope.tsv:50069`.
- The bounded NCBI scan resolved all 9 root-first lineage entries and found no missing ancestors or label, rank, or parent mismatches.

## Evidence

- `data/raw/lpsn_names.tsv:10811` supports the single non-deprecated, legitimate, validly published, correct LPSN species name `lpsn:69673`, authority `Bongaerts et al. 2026`, type-strain identifier `kgmicrobe.strain:LMG-32666`, three publications, LPSN URL, and 16S accession `INSDC:ON876749`.
- `data/raw/gtdb_mappings.tsv:241280` supports the `skos:closeMatch` to `GTDB:s__Acetobacter_sp963921165`; `genome_count: 1` matches the GTDB source attestation and the GTDB exact synonym `Acetobacter sp963921165`.
- `data/raw/ncbitaxon_taxa.tsv:579255` supports the NCBI related synonyms `Acetobacter sp. LMG 32666` and `Acetobacter zythi Bongaerts et al. 2026`.
- Bounded raw scans found no exact BacDive, compact culture-collection, final strain-assembly, final strain-genome, final related-record, StrainInfo, GOLD, BactoTraits, MediaDive, Madin et al., or NCBI merged-ID row for `NCBITaxon:2959295`, matching the empty optional blocks in the YAML.

## Completeness

- The generated NCBI identity, LPSN nomenclature, GTDB close match, GTDB synonym, two NCBI synonyms, xrefs, and NCBI, LPSN, and GTDB source attestations are complete for the pinned local source rows.
- `strain_count: 0` is complete for the generated corpus because there is no exact `data/raw/bacdive_strains.tsv` row, no compact culture-collection strain row, no final StrainInfo overlay, and no final strain genome row for this taxon.
- NCBI has 10 exact type-material rows for this species; they agree with the LPSN `LMG-32666` type-strain identifier and do not imply generated local strain rows without a matching BacDive strain.
- No BacDive strain block, GOLD organism, MediaDive medium, BactoTraits row, Madin et al. row, NCBI merged-ID row, generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. Future changes should rerun the same exact source checks plus open and strict validation after any NCBI, LPSN, GTDB, BacDive, GOLD, or StrainInfo refresh.

## Additional Notes

- `GTDB:s__Acetobacter_sp963921165` appears as an exact GTDB synonym because the GTDB species identifier has not been latinized to `Acetobacter zythi` in the local GTDB snapshot.
- The generated YAML was left read-only; any future correction would belong in a maintained source inventory, seeder logic, or `curation/seed_scope.tsv`.
