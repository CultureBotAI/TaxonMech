# YAML Record Review: Hypholoma sublateritium FD-334 SS-4

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hypholoma_sublateritium_fd_334_ss_4.yaml
- Started UTC: 2026-09-23T07:47:24Z
- Finished UTC: 2026-09-23T07:47:24Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:945553` |
| Label | `Hypholoma sublateritium FD-334 SS-4` |
| Rank | `STRAIN` |
| Parent Taxon | `NCBITaxon:71945` |
| Taxon Domain | `EUKARYOTA` |
| Grounding Status | `EXACT` |
| Mapping Status | `SEEDED` |
| Strain Count | `0` |

## Validation

- `just validate data/taxa/eukaryota/hypholoma_sublateritium_fd_334_ss_4.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/hyphochytrium_catenoides.yaml data/taxa/eukaryota/hyphodiscus_hymeniophilus.yaml data/taxa/eukaryota/hypholoma_australianum.yaml data/taxa/eukaryota/hypholoma_sublateritium_fd_334_ss_4.yaml` scanned the four-record batch and reported zero ERROR rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/hypholoma_sublateritium_fd_334_ss_4.yaml` completed and emitted the bounded source scan used below.

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:945553`, `label: Hypholoma sublateritium FD-334 SS-4`, `rank: STRAIN`, `parent_taxon: NCBITaxon:71945`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:202278`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through species `Hypholoma sublateritium`; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:45007`, which records one retained direct organism for `NCBITaxon:945553`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs contain two exact organisms, three linked projects, and one linked analysis.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:945553`. The source NCBI row has no exact, broad, or related synonyms, and the generated record correspondingly has no `synonyms` block.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have exact `Go0009592` and `Go0010136` organisms for `NCBITaxon:945553`, linked `Gp0010136`, `Gp0332798`, and `Gp0332799` projects, and one native analysis linked by project ID `Gp0010136`.

The scan found no exact NCBI type-material rows, side NCBI merged-ID rows, exact BacDive rows, exact StrainInfo rows, or maintained final strain-table rows. `strain_count: 0` is therefore consistent with no generated local child-strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded exact NCBI strain identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage through the parent species, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hypholoma_sublateritium_fd_334_ss_4.yaml` plus `just validate-strict data/taxa/eukaryota/hypholoma_sublateritium_fd_334_ss_4.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hypholoma_sublateritium_fd_334_ss_4` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
