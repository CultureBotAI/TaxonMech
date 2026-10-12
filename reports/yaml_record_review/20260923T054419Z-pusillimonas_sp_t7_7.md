# YAML Record Review: Pusillimonas sp. T7-7

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pusillimonas_sp_t7_7.yaml
- Started UTC: 2026-09-23T05:42:45Z
- Finished UTC: 2026-09-23T05:44:19Z
- Verdict: pass with minor issues

## Target

- Identifier: `NCBITaxon:1007105`
- Label: `Pusillimonas sp. T7-7`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2640016` (`unclassified Pusillimonas`)
- Maintained path: generated `data/taxa/bacteria/pusillimonas_sp_t7_7.yaml`; fixes, if any, belong in source normalization and GTDB synonym display logic.

The record is a compact generated NCBI placeholder species attested directly by NCBI, a one-genome GTDB species cluster, and two Madin trait assertions.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/sphingomonas_sp_s17.yaml data/taxa/bacteria/pusillimonas_sp_t7_7.yaml data/taxa/bacteria/alpha_proteobacterium_scgc_aaa076_c03.yaml data/taxa/bacteria/alpha_proteobacterium_scgc_aaa076_e06.yaml` | Passed; closed-schema validation accepted all 4 files with zero errors. |
| `just validate data/taxa/bacteria/pusillimonas_sp_t7_7.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI side is grounded to the pinned NCBI row in `data/raw/ncbitaxon_taxa.tsv:210812`: `NCBITaxon:1007105`, label `Pusillimonas sp. T7-7`, rank `SPECIES`, parent `NCBITaxon:2640016`, genetic code `11`, sources `ncbitaxon|gtdb|madin_etal`, and snapshot date `2026-09-13`.

The GTDB mapping is at the same placeholder-species granularity: `data/raw/gtdb_mappings.tsv:1074` maps the one-genome `GTDB:s__Pusillimonas_C_sp000209655` cluster to `NCBITaxon:1007105` as `skos:closeMatch`. The `sp000209655` suffix also matches the observed `GCA_000209655` BacDive assembly accession for the T7-7 genome, so the single GTDB genome is consistent with this NCBI placeholder.

## Evidence

- `source_attestations` correctly reflects one NCBI name row, one GTDB mapping row with one genome, and two Madin trait assertions for `NCBITaxon:1007105`.
- The exact ignored-file search found no LPSN, MediaDive, GOLD, BactoTraits, ATB, or StrainInfo rows keyed directly to `NCBITaxon:1007105`.
- BacDive-derived assembly/genome rows for `GCA_000209655` exist under `data/raw/strain_assemblies.tsv:27739` and `data/raw/strain_genome_records.tsv:22162-22163`, but their `kgmicrobe.strain:bacdive_133037` root row in `data/raw/bacdive_strains.tsv:55348` is keyed to `NCBITaxon:1979962`, not to `NCBITaxon:1007105`; the generated YAML therefore does not treat that BacDive strain as a direct T7-7 strain.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pusillimonas_sp_t7_7.md'` included ignored reports and found no prior review for this stem.
- An exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, GTDB, Madin, and BacDive-derived assembly/genome rows needed to review the generated fields.

## Findings

### Minor

- The GTDB `Pusillimonas_C` placeholder genus is displayed as `Pusillimonas C sp000209655` and marked as an `EXACT_SYNONYM`. That does not currently change the record scope because the GTDB cluster contains one genome and matches the T7-7 assembly accession, but the suffix should not be made to look like an ICNP species name if these GTDB display synonyms are consumed downstream.
- BacDive strain `133037` and assembly `GCA_000209655` are split across NCBITaxon IDs in the local raw tables: the assembly rows point to `NCBITaxon:1007105`, while the BacDive strain and StrainInfo deposit rows point at broader Pusillimonas taxa. That should be normalized or documented so the omission of a strain block on this record remains intentional.

## Recommended Edits

- Prefer preserving the GTDB canonical label `s__Pusillimonas_C_sp000209655` as an xref label or related synonym rather than normalizing `Pusillimonas_C` into an exact-looking space-separated species synonym.
- Audit the BacDive `133037` source normalization for the T7-7 genome and decide whether the `GCA_000209655` assembly belongs on this NCBI placeholder record, the broader `NCBITaxon:1979962` record, or both with explicit provenance.

## Follow-up Checks

- Rerun `just validate-strict data/taxa/bacteria/pusillimonas_sp_t7_7.yaml` and `just validate data/taxa/bacteria/pusillimonas_sp_t7_7.yaml`.
- Re-run an exact `rg --no-ignore --hidden` for `NCBITaxon:1007105`, `NCBITaxon:1979962`, `bacdive_133037`, `GCA_000209655`, and `pusillimonas_sp_t7_7` across `data/raw`, `data/atb`, and `data/straininfo`.
- Verify that regenerated YAML still keeps the one-genome GTDB mapping at species-placeholder scope and handles the BacDive assembly deliberately.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
