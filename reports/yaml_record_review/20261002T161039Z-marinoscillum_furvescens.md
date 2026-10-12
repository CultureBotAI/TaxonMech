# YAML Record Review: Marinoscillum furvescens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/marinoscillum_furvescens.yaml
- Started UTC: 2026-10-02T16:10:39Z
- Finished UTC: 2026-10-02T16:10:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1026` |
| Label | `Marinoscillum furvescens` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:643701` |
| Parent label | `Marinoscillum` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `1` |
| Source attestations | `NCBITAXON`, `LPSN`, `GTDB`, `BACDIVE`, `GOLD`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/marinoscillum_furvescens.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/marinoscillum_furvescens.yaml` | Pass: the strict one-file batch scanned 1 file and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 749 lines, 11 lineage entries, 4 synonyms, 3 xrefs, 1 declared strain, 10 genome assemblies, 7 genome records, 1 nomenclature block, 1 GTDB mapping, and 6 source attestations. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: the simple NCBI-only helper stopped with `NCBI source mismatch`, as expected for a species row synthesized from `ncbitaxon`, `gtdb`, `lpsn`, `gold`, and `madin_etal`. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:1026` trace to maintained PATHS, seed scope, GOLD, LPSN, MADIN, NCBI type-material, GTDB mapping, StrainInfo/GOLD related-record, and generated YAML rows. |

## Identity and Lineage

- `data/taxa/PATHS.tsv` row 10815 maps `NCBITaxon:1026` to `marinoscillum_furvescens`.
- `curation/seed_scope.tsv` row 20755 keeps this taxon in scope with 5 non-NCBI source families plus NCBI.
- `data/raw/ncbitaxon_taxa.tsv` row 797 names `NCBITaxon:1026` as the species `Marinoscillum furvescens`, under `NCBITaxon:643701` / `Marinoscillum`.
- Direct first-column NCBI checks covered every lineage id in the 11-node root-first chain from `root` through `Marinoscillum`.

## Nomenclature and Mapping

- `data/raw/lpsn_names.tsv` row 25042 backs `lpsn:787863`, the current `Marinoscillum furvescens` LPSN name, the correct-name flags, the type strain designations, the three publications, and the `INSDC:AB078079` sequence accession.
- The record preserves the LPSN type strain designations `ATCC-23129`, `DSM-4134`, `IFO-15994`, `LMG-13023`, and `NBRC-15994` in `nomenclature`.
- `data/raw/gtdb_mappings.tsv` row 1195 maps `GTDB:s__Marinoscillum_luteum` to `NCBITaxon:1026` with `skos:closeMatch` and a genome count of 3, matching the GTDB source attestation.
- NCBI contributes `Microscilla furvescens` plus the quoted and recombination-form synonym strings; GTDB contributes the `Marinoscillum luteum` exact synonym and xref.

## Strain and Genome Evidence

- `data/raw/bacdive_strains.tsv` row 5363 backs the single declared BacDive strain, `kgmicrobe.strain:bacdive_5472` / `bacdive:5472`, filed as descendant strain taxon `NCBITaxon:1122208`.
- `data/raw/ncbitaxon_taxa.tsv` row 242468 confirms `NCBITaxon:1122208` is the NCBI strain `Marinoscillum furvescens DSM 4134` under `NCBITaxon:1026`.
- `data/raw/culture_collection_strains.tsv` rows 2699, 78398, and 141953 back the BacDive strain's ATCC 23129, DSM 4134, and NCMB 1419 culture collection ids.
- `data/raw/strain_assemblies.tsv` rows 132681-132689 cover the INSDC, BV-BRC, GOLD, GTDB, and NCBI Assembly assembly assertions for `GCA_003386095`, `GCA_003386095.1`, and `GCF_003386095.1`.
- `data/raw/strain_genome_records.tsv` rows 106412-106418 cover the GTDB, IMG/GOLD, BV-BRC, and BacDive genome records for `RS_GCF_003386095.1`, `2754412942`, and `1122208.3`.
- `data/straininfo/assemblies.tsv` row 10081 and `data/straininfo/strain_links.tsv` rows 92905-92906 back the `straininfo.strain:10156` genome evidence and the DSM 4134 and NCMB 1419 StrainInfo deposit related records.
- `data/atb/strain_links.tsv` row 4558 and `data/atb/genome_links.tsv` rows 19800-19804 back the AllTheBacteria assembly `atb.assembly:202505.SAMN08770194`, BioSample `SAMN08770194`, and shared-GTDB/IMG/NCBI/BV-BRC links.

## Related Records

- `data/raw/strain_related_records.tsv` rows 381923-381946 back all BioProject, BioSample, GOLD analysis, GOLD organism, and GOLD project related records for `kgmicrobe.strain:bacdive_5472`.
- GOLD organism ids `Go0620232` and `Go0620233` are intentionally related directly to `NCBITaxon:1026`, while `Go0013990`, `Gp0251905`, and `Ga0215637` are tied to descendant strain taxon `NCBITaxon:1122208`.
- The direct scans also confirmed BacDive, MediaDive, and BactoTraits source rows under the descendant strain taxon rather than unexpected duplicate top-level strain rows.

## Source Attestations

- The NCBI, LPSN, GTDB, BacDive, GOLD, and MADIN attestations all have matching exact source rows and appropriate units: names for NCBI/LPSN, genomes for GTDB, strains for BacDive, organisms for GOLD, and trait assertions for MADIN.
- GOLD's top-level assertion count is consistent with the 4 native GOLD organism rows recorded for `NCBITaxon:1026`; descendant GOLD project and analysis rows are represented under the BacDive strain evidence.
- The BacDive attestation correctly notes that its one strain is filed under one descendant NCBI taxon via `classified_as`.

## Completeness

- The record is complete for the maintained source inventories that currently mention `NCBITaxon:1026`, its descendant strain taxon `NCBITaxon:1122208`, and the linked strain/genome identifiers.
- LPSN type strain designations that are absent from BacDive remain represented in `nomenclature.type_strain_designations`; the `strains` list is limited to the single BacDive strain row.
- No causal graphs are present or expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/marinoscillum_furvescens.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/marinoscillum_furvescens.yaml`.
- Re-run `just verify-corpus`.
- Re-run the exact source scans after any refresh of `data/raw/`, `data/atb/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- The generated record has no top-level `causal_graphs` block.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, `data/atb/`, `data/straininfo/`, or the seeder, not in `data/taxa/bacteria/marinoscillum_furvescens.yaml` directly.
