# YAML Record Review: Paenibacillus elgii B69

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/paenibacillus_elgii_b69.yaml
- Started UTC: 2026-09-23T05:38:43Z
- Finished UTC: 2026-09-23T05:41:19Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1007103`
- Label: `Paenibacillus elgii B69`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:189691` (`Paenibacillus elgii`)
- Maintained path: generated `data/taxa/bacteria/paenibacillus_elgii_b69.yaml`; fixes belong in `data/raw/gtdb_mappings.tsv` generation and GTDB synonym/xref projection in `src/taxonmech/seed.py`.

The record is a generated NCBI strain for `Paenibacillus elgii B69` with NCBI, GTDB, and Madin evidence.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/gordonia_caeni.yaml data/taxa/bacteria/deinococcus_daejeonensis.yaml data/taxa/bacteria/pseudomonas_kuykendallii.yaml data/taxa/bacteria/paenibacillus_elgii_b69.yaml` | Passed; closed-schema validation accepted all 4 files with zero errors. |
| `just validate data/taxa/bacteria/paenibacillus_elgii_b69.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI identity is grounded: `data/raw/ncbitaxon_taxa.tsv:210810` has `NCBITaxon:1007103`, label `Paenibacillus elgii B69`, rank `STRAIN`, parent `NCBITaxon:189691`, two NCBI exact strain synonyms, source set `ncbitaxon|gtdb|madin_etal`, and snapshot date `2026-09-13`.

The lineage correctly places the strain under species `NCBITaxon:189691` / `Paenibacillus elgii`, which is independently supported by the LPSN row in `data/raw/lpsn_names.tsv:22587`.

The GTDB species projection is over-scoped. `data/raw/gtdb_mappings.tsv:1072` maps the eight-genome `GTDB:s__Paenibacillus_G_elgii` species cluster to the single `Paenibacillus elgii B69` NCBI strain with `skos:closeMatch`; the same GTDB species is broad-mapped to the NCBI species parent in `data/raw/gtdb_mappings.tsv:79106`, and the species parent has additional broad GTDB mappings for other `Paenibacillus_G` clusters.

## Evidence

- `source_attestations` correctly reflects one NCBI name, one GTDB mapping with eight genomes, and one Madin trait assertion.
- The two `EXACT_SYNONYM` values from NCBI are supported by the synonym column in `data/raw/ncbitaxon_taxa.tsv:210810`.
- No strain block is generated, which is consistent with the source inventories found for `NCBITaxon:1007103`: the pinned support for this strain is the NCBI taxon row, the GTDB mapping row, and the Madin row, not BacDive, GOLD, ATB, or StrainInfo rows for the B69 strain.
- The GTDB cluster supports, at most, a species-cluster relationship and does not justify projecting `Paenibacillus G elgii` as an exact synonym of the B69 strain.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-paenibacillus_elgii_b69.md'` included ignored reports and found no prior review for this stem.
- An exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS row, the B69 NCBI row, `data/raw/gtdb_mappings.tsv:1072`, and `data/raw/madin_taxa.tsv:371` for `NCBITaxon:1007103`.
- The same exact ignored-file search found LPSN, GOLD, StrainInfo, type-material, and additional GTDB rows for the parent species `NCBITaxon:189691`; those parent-species rows are not direct B69 strain evidence.

## Findings

### Major

- `data/raw/gtdb_mappings.tsv:1072` and `src/taxonmech/seed.py` project the multi-genome `GTDB:s__Paenibacillus_G_elgii` species cluster onto a single `Paenibacillus elgii B69` strain. The generated YAML consequently emits `Paenibacillus G elgii` as an `EXACT_SYNONYM` and `GTDB:s__Paenibacillus_G_elgii` as an exact-looking xref on a strain record, even though the GTDB cluster is broader than B69 and is already broad-mapped to the parent species.

## Recommended Edits

- Adjust the maintained GTDB mapping generation in `data/raw/gtdb_mappings.tsv` and the GTDB synonym/xref projection in `src/taxonmech/seed.py` so GTDB species clusters are not emitted as exact synonyms or exact-looking xrefs on NCBI strain records.
- Regenerate `data/taxa/bacteria/paenibacillus_elgii_b69.yaml` after the maintained input or generator fix.

## Follow-up Checks

- Rerun `just validate-strict data/taxa/bacteria/paenibacillus_elgii_b69.yaml` and `just validate data/taxa/bacteria/paenibacillus_elgii_b69.yaml`.
- Re-run an exact `rg --no-ignore --hidden` for `NCBITaxon:1007103`, `NCBITaxon:189691`, `GTDB:s__Paenibacillus_G_elgii`, and `paenibacillus_elgii_b69` across `data/raw`, `data/atb`, and `data/straininfo`.
- Manually verify that the regenerated strain YAML retains the NCBI and Madin evidence but no longer emits `Paenibacillus G elgii` as a GTDB exact synonym or `GTDB:s__Paenibacillus_G_elgii` as a strain xref.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
