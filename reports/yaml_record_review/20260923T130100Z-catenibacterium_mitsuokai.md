# YAML Record Review: Catenibacterium mitsuokai

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/catenibacterium_mitsuokai.yaml
- Started UTC: 2026-09-23T12:58:54Z
- Finished UTC: 2026-09-23T13:01:00Z
- Verdict: pass

## Target

`data/taxa/bacteria/catenibacterium_mitsuokai.yaml` is the generated `TaxonRecord` for `NCBITaxon:100886`, label `Catenibacterium mitsuokai`, rank `SPECIES`, `taxon_domain: BACTERIA`, and parent `NCBITaxon:135858` `Catenibacterium`.

The full 1,263-line target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*catenibacterium_mitsuokai.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/coprobacillus_cateniformis.yaml data/taxa/bacteria/catenibacterium_mitsuokai.yaml data/taxa/bacteria/uncultured_aestuariimicrobium_sp.yaml data/taxa/bacteria/uncultured_telmatospirillum_sp.yaml` | Passed: 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate data/taxa/bacteria/catenibacterium_mitsuokai.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: no `causal_graphs` are present |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:17340` supports the NCBI identifier, label, `SPECIES` rank, `NCBITaxon:135858` parent, genetic code `11`, both authority synonyms, and the `ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal` source flags. `curation/seed_scope.tsv:13747` carries the matching five-source inclusion row.

`data/raw/lpsn_names.tsv:16060` supports `lpsn:774509`, the species name, the emended `Kageyama and Benno 2000 emend. Ricci et al. 2025` authority, correct-name status, type-strain designations `CCUG-48821`, `CIP-106738`, `DSM-15897`, and `JCM-10609`, and `INSDC:AB910738`. The LPSN synonym `lpsn:65825` is represented as the related synonym `Catenibacterium mitsuokai mitsuokai`.

## Evidence

`data/raw/gtdb_mappings.tsv:1109-1112` supports the four pooled `skos:broadMatch` entries under `taxonomy_mappings`; the 107-genome `GTDB:s__Catenibacterium_mitsuoka_A` row is correctly used as the GTDB source attestation and the other three GTDB species are retained as pooled context.

The BacDive strain count of eight is supported by six rows directly under `NCBITaxon:100886` plus two descendant rows: `bacdive:5366` under `NCBITaxon:451640` and `bacdive:176715` under `NCBITaxon:3035606`. The `bacdive:5366` type-strain block carries the expected NCBI Assembly, BV-BRC, GOLD, GTDB, AllTheBacteria, and StrainInfo evidence for `DSM-15897` / `JCM-10609`.

`data/raw/gold_organisms.tsv:204` supports the `GOLD` attestation count of 52 organisms filed directly under the species, and `data/raw/madin_taxa.tsv:399` supports the three direct `MADIN` trait assertions. Exact gitignore-independent searches of `data/raw/mediadive_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` found no direct same-taxon rows, so no direct MediaDive, BactoTraits, merged-id, or dropped-source block is missing.

## Completeness

The record reports `strain_count: 8`, lists all eight BacDive strain rows represented in the pinned BacDive inventory, and preserves the type strain's uncapped assembly, genome-record, ATB, StrainInfo, BioSample, BioProject, and GOLD organism/project context. The newer `Catenibacterium mitsuokai subsp. tridentinum` rows remain represented through their own descendant record rather than being flattened into the species nomenclature block.

No curator-added `evidence`, `definition`, `discussions`, or `causal_graphs` are present or required for the seeded identity.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. If a future source refresh changes `lpsn:774509`, the GTDB pooled mapping set, `bacdive:5366`, or the Ricci et al. subspecies rows, rerun `just seed-canary NCBITaxon:100886`, `just validate data/taxa/bacteria/catenibacterium_mitsuokai.yaml`, `just validate-strict data/taxa/bacteria/catenibacterium_mitsuokai.yaml`, and `just verify-corpus`.

## Additional Notes

Live NCBI, LPSN, GTDB, BacDive, and StrainInfo pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
