# YAML Record Review: Hypomyces subglobosus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hypomyces_subglobosus.yaml
- Started UTC: 2026-09-23T08:10:39Z
- Finished UTC: 2026-09-23T08:10:39Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1924243` |
| Label | `Hypomyces subglobosus` |
| Rank | `SPECIES` |
| Parent Taxon | `NCBITaxon:5130` |
| Taxon Domain | `EUKARYOTA` |
| Grounding Status | `EXACT` |
| Mapping Status | `SEEDED` |
| Strain Count | `0` |

## Validation

- `just validate data/taxa/eukaryota/hypomyces_subglobosus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/hypomyces_subglobosus.yaml data/taxa/eukaryota/hypomyces_subiculosus.yaml data/taxa/eukaryota/hypomyces_tubariicola.yaml data/taxa/eukaryota/hypomyces_xyloboli.yaml` scanned the four-record batch and reported zero ERROR rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/hypomyces_subglobosus.yaml` completed and emitted the bounded source scan used below.

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1924243`, `label: Hypomyces subglobosus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5130`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:495695`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hypomyces`; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:17588`, which records one retained direct organism for `NCBITaxon:1924243`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs have no exact organism, project, or analysis rows for this taxon.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1924243`. The YAML's authorship-bearing `Hypomyces subglobosus` synonym is present in `data/raw/ncbitaxon_taxa.tsv:495695` as the only related synonym for the source row, and NCBI has no exact synonyms for this taxon.

The retained GOLD aggregate supplies one organism assertion, although the current native GOLD catalogs do not have exact `ORGANISM NCBI TAX ID: 1924243` rows or linked projects/analyses in the local snapshot.

NCBI carries four exact type-material rows for `Hypomyces subglobosus` at `data/raw/ncbi_type_material.tsv:71821` through `data/raw/ncbi_type_material.tsv:71824`, spanning CBS 543.86 culture-from-holotype and CBS H-33414 holotype spelling variants.

The scan found no exact side NCBI merged-ID rows, exact StrainInfo rows, exact BacDive rows, or maintained final strain-table rows. `strain_count: 0` is therefore consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, the NCBI related synonym for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hypomyces_subglobosus.yaml` plus `just validate-strict data/taxa/eukaryota/hypomyces_subglobosus.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hypomyces_subglobosus` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`, which can differ from the current native GOLD organism, project, and analysis rows. Native GOLD evidence creates generated child strains only after joining to BacDive-derived local strain inventory entries.
