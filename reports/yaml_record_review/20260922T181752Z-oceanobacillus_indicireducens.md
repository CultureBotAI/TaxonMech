# YAML Record Review: Oceanobacillus indicireducens

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/oceanobacillus_indicireducens.yaml`
- Started UTC: 2026-09-22T18:16:34Z
- Finished UTC: 2026-09-22T18:17:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004261` |
| Label | `Oceanobacillus indicireducens` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:182709` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated bacterial species record with one listed BacDive strain, `bacdive:23737` / A21.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/oceanobacillus_indicireducens.yaml` | Pass; `linkml-validate` exited 0. |
| `just validate-strict data/taxa/bacteria/oceanobacillus_indicireducens.yaml data/taxa/bacteria/bacillus_sp_mra1.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_monolepta_hieroglyphica.yaml data/taxa/bacteria/mesorhizobium_sp_ccbau_831015.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004261` is the pinned NCBI species row for `Oceanobacillus indicireducens`, parented by `NCBITaxon:182709` with genetic code `11`. LPSN row `lpsn:790639` is the correct species name and lists `DSM-28042` and `JCM-17251`, which are BacDive deposits on the A21 strain and support `is_type_strain: true`.

`GTDB:s__Oceanobacillus_indicireducens` maps to this species with `skos:closeMatch` and genome count `5`; LPSN links that GTDB species to the same name.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and related synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004261`, label `Oceanobacillus indicireducens`, rank `SPECIES`, parent `NCBITaxon:182709`, genetic code `11`, and the two NCBI related synonyms in the YAML. |
| LPSN correct-name nomenclature | `data/raw/lpsn_names.tsv` row `lpsn:790639` carries the `Oceanobacillus indicireducens` species name, correct-name status, DOI/PMID and INSDC support, and DSM/JCM type-strain designations. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Oceanobacillus_indicireducens` to `NCBITaxon:1004261` as `skos:closeMatch` with count `5`. |
| Direct source counts | Exact rows support `MEDIADIVE` count `3`, `GOLD` count `3`, `MADIN` count `15`, and `BACTOTRAITS` count `27`. |
| BacDive strain | `data/raw/bacdive_strains.tsv` has `bacdive:23737`, designation `A21`, exact taxon `NCBITaxon:1004261`, LPSN id `lpsn:790639`, and the BCRC/DSM/JCM/NCIMB culture-collection deposits present in the YAML. |
| Genome and related records | `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, and `data/straininfo/strain_links.tsv` support the NCBI, GTDB, GOLD, IMG, BV-BRC/PATRIC, BioProject, BioSample, StrainInfo deposit, and StrainInfo strain rows for `bacdive:23737`. |

## Completeness

The record has the exact NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD, Madin, and BactoTraits source coverage found by gitignore-independent searches for `NCBITaxon:1004261`, `lpsn:790639`, `GTDB:s__Oceanobacillus_indicireducens`, and `bacdive:23737`. `strain_count: 1` matches the single BacDive row filed under this species.

The three GOLD organism related records for NCIMB 14685, JCM 17251, and DSM 28042 are preserved through exact culture-deposit matches; the JCM 17251 GOLD chain additionally supplies the assembly, IMG genome, BioProject, BioSample, analysis, and project records.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused validators and an exact `rg --no-ignore --hidden` scan for `NCBITaxon:1004261`, `bacdive:23737`, `straininfo.strain:398524`, `lpsn:790639`, and `GTDB:s__Oceanobacillus_indicireducens` after any source refresh that changes this species or the A21 strain.

## Additional Notes

The StrainInfo SI-DP and SI-ID rows in the YAML are derived from `data/straininfo/strain_links.tsv`; no extra sequence rows for `straininfo.strain:398524` were present in compressed `data/straininfo/related_records.tsv.gz`.
