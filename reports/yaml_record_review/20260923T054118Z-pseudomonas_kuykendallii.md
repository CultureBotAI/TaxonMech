# YAML Record Review: Pseudomonas kuykendallii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_kuykendallii.yaml
- Started UTC: 2026-09-23T05:38:43Z
- Finished UTC: 2026-09-23T05:41:18Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1007099`
- Label: `Pseudomonas kuykendallii`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:286` (`Pseudomonas`)
- Maintained path: generated `data/taxa/bacteria/pseudomonas_kuykendallii.yaml`; fixes belong in `data/raw/gtdb_mappings.tsv` generation and GTDB synonym/xref projection in `src/taxonmech/seed.py`.

The record is a generated NCBI species for the ICNP name `Pseudomonas kuykendallii` with LPSN, BacDive, MediaDive, GOLD, BactoTraits, ATB, and StrainInfo evidence, plus a GTDB placeholder-genus mapping that is rendered too exactly.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/gordonia_caeni.yaml data/taxa/bacteria/deinococcus_daejeonensis.yaml data/taxa/bacteria/pseudomonas_kuykendallii.yaml data/taxa/bacteria/paenibacillus_elgii_b69.yaml` | Passed; closed-schema validation accepted all 4 files with zero errors. |
| `just validate data/taxa/bacteria/pseudomonas_kuykendallii.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI and ICNP identity is grounded. `data/raw/ncbitaxon_taxa.tsv:210809` has `NCBITaxon:1007099`, label `Pseudomonas kuykendallii`, rank `SPECIES`, parent `NCBITaxon:286`, genetic code `11`, and three related NCBI strain-name synonyms. `data/raw/lpsn_names.tsv:27161` has a legitimate, validly published, correct-name LPSN row for `Pseudomonas kuykendallii` linked to `NCBITaxon:1007099` with type strains DSM 25107, LMG 26364, and NRRL B-59562.

The GTDB mapping needs curation. `data/raw/gtdb_mappings.tsv:1071` maps the 10-genome `GTDB:s__Pseudomonas_O_kuykendallii` cluster to `NCBITaxon:1007099`, but the LPSN row has no GTDB species link. The GTDB suffixed genus `Pseudomonas_O` is also generated as the space-separated `Pseudomonas O kuykendallii` `EXACT_SYNONYM`, which makes a GTDB placeholder genus look like an exact synonym of the ICNP `Pseudomonas` species.

## Evidence

- `source_attestations` matches the local row counts: one NCBI name, one LPSN name, 10 GTDB genomes, one BacDive strain, one MediaDive medium, three GOLD organisms, and one BactoTraits trait assertion.
- `data/raw/bacdive_strains.tsv:13031` supports BacDive strain `13190`, designation `H2`, the three LPSN culture collection IDs, and the type-strain linkage.
- The assembly and genome blocks are supported by BV-BRC, GOLD, GTDB, NCBI Assembly, StrainInfo, and AllTheBacteria rows for `SAMN05216287`/`SRR4234991`.
- `data/straininfo/strain_links.tsv:12380-12382` supports the three generated StrainInfo deposit records for strain `376908`.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudomonas_kuykendallii.md'` included ignored reports and found no prior review for this stem.
- An exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, LPSN, GTDB, BacDive, culture-collection, strain assembly, strain genome, GOLD, MediaDive, BactoTraits, StrainInfo, and ATB rows supporting the generated fields and the GTDB placeholder-genus finding.
- No Madin row was found for `NCBITaxon:1007099`, so the absence of a Madin `source_attestations` entry is supported.

## Findings

### Major

- `data/raw/gtdb_mappings.tsv:1071` and `src/taxonmech/seed.py` render `GTDB:s__Pseudomonas_O_kuykendallii` as if it were an exact species synonym for the ICNP name `Pseudomonas kuykendallii`. The generated YAML should not turn the GTDB suffixed placeholder genus into `Pseudomonas O kuykendallii` as an `EXACT_SYNONYM`, and the unlinked GTDB xref needs an explicit curation decision before it can be treated as exact grounding.

## Recommended Edits

- Review the maintained GTDB mapping for `GTDB:s__Pseudomonas_O_kuykendallii` and downgrade or annotate it unless curated evidence confirms exact identity with `NCBITaxon:1007099`.
- Adjust `src/taxonmech/seed.py` so GTDB placeholder-genus labels are not normalized into plain-space `EXACT_SYNONYM` strings for ICNP names.
- Regenerate `data/taxa/bacteria/pseudomonas_kuykendallii.yaml` after the mapping or projection fix.

## Follow-up Checks

- Rerun `just validate-strict data/taxa/bacteria/pseudomonas_kuykendallii.yaml` and `just validate data/taxa/bacteria/pseudomonas_kuykendallii.yaml`.
- Re-run an exact `rg --no-ignore --hidden` for `NCBITaxon:1007099`, `GTDB:s__Pseudomonas_O_kuykendallii`, `SAMN05216287`, and `pseudomonas_kuykendallii` across `data/raw`, `data/atb`, and `data/straininfo`.
- Manually verify that the regenerated YAML preserves the ATB and StrainInfo genome evidence while removing or downgrading `Pseudomonas O kuykendallii`.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
