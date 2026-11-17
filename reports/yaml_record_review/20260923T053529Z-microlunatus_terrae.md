# YAML Record Review: Microlunatus terrae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/microlunatus_terrae.yaml
- Started UTC: 2026-09-23T05:34:42Z
- Finished UTC: 2026-09-23T05:35:29Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1007092`
- Label: `Microlunatus terrae`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:29404` (`Microlunatus`)
- Maintained path: generated `data/taxa/bacteria/microlunatus_terrae.yaml`; fixes belong in `data/raw/bacdive_strains.tsv`, `data/raw/mediadive_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, `data/straininfo/strain_links.tsv`, genome inputs in `data/raw/`, or `src/taxonmech/seed.py`, depending on source.

The record is a generated species record with NCBI, BacDive, MediaDive, GOLD, BV-BRC, BactoTraits, and StrainInfo support.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/compostibacter_hankyongensis.yaml data/taxa/bacteria/conexibacter_sp_bs10.yaml data/taxa/bacteria/dyella_sp_bs13.yaml data/taxa/bacteria/microlunatus_terrae.yaml` | Passed; closed-schema validation accepted all 4 files. |
| `just validate data/taxa/bacteria/microlunatus_terrae.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML agrees with the pinned NCBI inventory row in `data/raw/ncbitaxon_taxa.tsv:210802`: `NCBITaxon:1007092`, label `Microlunatus terrae`, rank `SPECIES`, parent `NCBITaxon:29404`, genetic code `11`, NCBI related synonyms, source set `ncbitaxon|bacdive|mediadive|gold|bactotraits`, and snapshot date `2026-09-13`.

The lineage is carried from NCBI and is internally consistent from `root` through `Bacteria`, `Bacillati`, `Actinomycetota`, `Actinomycetes`, `Propionibacteriales`, `Propionibacteriaceae`, and `Microlunatus`. `grounding_status: EXACT` is appropriate because the record is seeded directly from the NCBI species identifier.

## Evidence

- The NCBI related synonyms `"Microlunatus terrae" Lee and Kim 2012` and `Microlunatus sp. BS06` match the related-synonym column in `data/raw/ncbitaxon_taxa.tsv:210802`.
- `data/raw/bacdive_strains.tsv:12474` supports one BacDive strain, ID `12631`, designation `BS6`, and collection IDs `CCARM 9244`, `DSM 26486`, `JCM 17661`, `KCTC 19858`, and `KEMC 9004-079`; the five culture-collection rows all point at `NCBITaxon:1007092`.
- `data/raw/strain_genome_records.tsv:9095-9100` supports the generated BacDive, GOLD, and BV-BRC genome records for DSM 26486.
- `data/raw/strain_related_records.tsv:34779-34796` supports the BioProject, BioSample, GOLD analysis, GOLD organism, and GOLD project related records.
- `data/straininfo/strain_links.tsv:7828` links the BacDive strain to StrainInfo strain `406977`, deposit `914316`, and DOI `10.60712/SI-ID406977.2`.
- `data/raw/mediadive_taxa.tsv:47`, `data/raw/gold_organisms.tsv:173`, and `data/raw/bactotraits_taxa.tsv:33` support the MediaDive, GOLD, and BactoTraits source-attestation counts.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-microlunatus_terrae.md'` included ignored reports and found no prior review for this stem.
- An anchored exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, NCBI type-material, BacDive, culture-collection, MediaDive, GOLD, BactoTraits, strain genome, strain related-record, and StrainInfo rows supporting the generated fields.
- `strain_count: 1` is complete for the inspected rows: the single BacDive strain row, its five collection IDs, and its DSM 26486 StrainInfo link are represented under one generated strain.
- No LPSN, GTDB, ATB, sample, causal-graph, or quality sections are required by the local sources currently attached to this record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this passing source-rich record. If a future refresh changes the BacDive, MediaDive, GOLD, BV-BRC, BactoTraits, or StrainInfo rows, rerun `just validate-strict data/taxa/bacteria/microlunatus_terrae.yaml`, `just validate data/taxa/bacteria/microlunatus_terrae.yaml`, and a focused exact `rg --no-ignore --hidden` over the maintained source rows before reviewing the newly projected sections.

## Additional Notes

- The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
- `data/raw/ncbi_type_material.tsv` also extracts NCBI `typematerial.dmp` rows for `Microlunatus terrae`; the reviewed record correctly derives strain details from BacDive and StrainInfo rather than from NCBI type-material rows alone.
