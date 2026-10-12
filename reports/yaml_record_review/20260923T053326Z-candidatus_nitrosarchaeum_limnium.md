# YAML Record Review: Candidatus Nitrosarchaeum limnium

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/candidatus_nitrosarchaeum_limnium.yaml
- Started UTC: 2026-09-23T05:32:40Z
- Finished UTC: 2026-09-23T05:33:26Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1007084`
- Label: `Candidatus Nitrosarchaeum limnium`
- Rank: `SPECIES`
- Domain: `ARCHAEA`
- Parent: `NCBITaxon:1007082` (`Nitrosarchaeum`)
- Maintained path: generated `data/taxa/archaea/candidatus_nitrosarchaeum_limnium.yaml`; fixes belong in `data/raw/`, `data/atb`, `data/straininfo`, `curation/seed_scope.tsv`, or `src/taxonmech/seed.py`, depending on source.

The record is a generated archaeal species record with direct NCBI, GOLD, and Madin attestations.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/archaea/candidatus_nitrosarchaeum_limnium.yaml data/taxa/bacteria/micrococcus_sp_kc5.yaml data/taxa/bacteria/brevibacterium_hankyongi.yaml data/taxa/bacteria/chitinophaga_sp_bs20.yaml` | Passed; closed-schema validation accepted all 4 files. |
| `just validate data/taxa/archaea/candidatus_nitrosarchaeum_limnium.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML agrees with the pinned NCBI inventory row in `data/raw/ncbitaxon_taxa.tsv:210795`: `NCBITaxon:1007084`, label `Candidatus Nitrosarchaeum limnium`, rank `SPECIES`, parent `NCBITaxon:1007082`, genetic code `11`, NCBI exact and related synonyms, source set `ncbitaxon|gold|madin_etal`, and snapshot date `2026-09-13`.

The lineage is carried from NCBI and is internally consistent from `root` through `Archaea`, `Thermoproteati`, `Nitrososphaerota`, `Nitrososphaeria`, `Nitrosopumilales`, `Nitrosopumilaceae`, and `Nitrosarchaeum`. `grounding_status: EXACT` is appropriate because the record is seeded directly from the same NCBI identifier.

## Evidence

- `source_attestations` correctly reflects one direct NCBI name row, three direct GOLD organism rows in `data/raw/gold_organisms.tsv:171`, and one direct Madin trait assertion in `data/raw/madin_taxa.tsv:367`.
- The four NCBI synonyms match the exact and related synonym columns in `data/raw/ncbitaxon_taxa.tsv:210795`, including `Candidatus Nitrosoarchaeum limnia` / `Nitrosoarchaeum limnia` alternates.
- Descendant strain rows for BG20 and SFB1 in `data/raw/ncbitaxon_taxa.tsv` are not gathered into this species record, matching the source-attestation note that records are filed directly under this taxon.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-candidatus_nitrosarchaeum_limnium.md'` included ignored reports and found no prior review for this stem.
- An anchored exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the direct PATHS, NCBI, GOLD, and Madin rows and two descendant NCBI strain rows whose labels include the species name.
- No ATB, BacDive, LPSN, or StrainInfo rows were found for `NCBITaxon:1007084`, so the absence of those evidence sections is supported.
- No GTDB species-cluster projection is attached to the species record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this passing direct-source record. If a future refresh links this taxon to GTDB, LPSN, BacDive, ATB, or StrainInfo, rerun `just validate-strict data/taxa/archaea/candidatus_nitrosarchaeum_limnium.yaml`, `just validate data/taxa/archaea/candidatus_nitrosarchaeum_limnium.yaml`, and a focused exact `rg --no-ignore --hidden` over the maintained source rows before reviewing the newly projected sections.

## Additional Notes

The live NCBI browser and source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 NCBI, GOLD, and Madin rows are the authority evidence used for this report.
