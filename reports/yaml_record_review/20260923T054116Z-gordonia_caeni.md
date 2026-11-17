# YAML Record Review: Gordonia caeni

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/gordonia_caeni.yaml
- Started UTC: 2026-09-23T05:38:43Z
- Finished UTC: 2026-09-23T05:41:16Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1007097`
- Label: `Gordonia caeni`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2053` (`Gordonia`)
- Maintained path: generated `data/taxa/bacteria/gordonia_caeni.yaml`; fixes, if any, would belong in the source inventories or the generator, not by hand in the generated YAML.

The record is a generated NCBI species for `Gordonia caeni` with an LPSN correct-name row, one one-genome GTDB species cluster, a BacDive type strain, MediaDive/GOLD/Madin/BactoTraits source attestations, and StrainInfo deposit evidence.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/gordonia_caeni.yaml data/taxa/bacteria/deinococcus_daejeonensis.yaml data/taxa/bacteria/pseudomonas_kuykendallii.yaml data/taxa/bacteria/paenibacillus_elgii_b69.yaml` | Passed; closed-schema validation accepted all 4 files with zero errors. |
| `just validate data/taxa/bacteria/gordonia_caeni.yaml` | Passed. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI identity agrees with the pinned NCBI inventory row in `data/raw/ncbitaxon_taxa.tsv:210807`: `NCBITaxon:1007097`, label `Gordonia caeni`, rank `SPECIES`, parent `NCBITaxon:2053`, genetic code `11`, two related NCBI synonyms, the expected source set, and snapshot date `2026-09-13`.

The LPSN row in `data/raw/lpsn_names.tsv:27264` is a legitimate, validly published, correct-name species row for `Gordonia caeni`, maps to `NCBITaxon:1007097`, links `GTDB:s__Gordonia_caeni`, and supplies the DSM 45852, JCM 16923, and KCTC 19771 type-strain designations projected into `nomenclature`.

The GTDB projection is appropriately scoped. `data/raw/gtdb_mappings.tsv:1069` maps the one-genome `GTDB:s__Gordonia_caeni` species cluster to the NCBI species with `skos:closeMatch`, and the LPSN row independently links the same GTDB species to the same species name.

## Evidence

- `source_attestations` matches the local source rows: one NCBI name, one LPSN name, one GTDB genome, one BacDive strain, two MediaDive medium entries, five GOLD organisms, 19 Madin trait assertions, and 26 BactoTraits trait assertions.
- `data/raw/bacdive_strains.tsv:22959` supports BacDive strain `23155`, designations `MJ32, N2-9`, the three LPSN culture collection IDs, and the type-strain linkage.
- The generated assembly and genome blocks are supported by rows for BacDive, BV-BRC, GOLD, GTDB, and NCBI Assembly in `data/raw/strain_assemblies.tsv:108755-108763` and by BV-BRC, GOLD, and GTDB rows in `data/raw/strain_genome_records.tsv:87463-87467`.
- `data/raw/strain_related_records.tsv:314917-314940` and `data/straininfo/strain_links.tsv:80622` support the BioProject, BioSample, GOLD analysis/project/organism, and StrainInfo deposit/strain related records.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-gordonia_caeni.md'` included ignored reports and found no prior review for this stem.
- An exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, LPSN, GTDB, BacDive, culture-collection, strain assembly, strain genome, GOLD, MediaDive, Madin, BactoTraits, and StrainInfo rows supporting the generated fields.
- The record has no ATB genome block, and the exact ignored-file search did not find an ATB row for `NCBITaxon:1007097`; that absence is consistent with the YAML.

## Findings

No curation findings.

## Recommended Edits

No edits recommended.

## Follow-up Checks

- No follow-up is required for this record beyond normal regeneration QA.
- If the source inventories or generator change, rerun `just validate-strict data/taxa/bacteria/gordonia_caeni.yaml` and `just validate data/taxa/bacteria/gordonia_caeni.yaml`.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
