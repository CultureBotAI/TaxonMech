# YAML Record Review: Fusarium vanettenii 77-13-4

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_vanettenii_77_13_4.yaml
- Started UTC: 2026-09-23T03:55:01Z
- Finished UTC: 2026-09-23T03:55:01Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:660122` |
| Label | `Fusarium vanettenii 77-13-4` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2747968` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_vanettenii_77_13_4.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_udum.yaml data/taxa/eukaryota/fusarium_vanettenii.yaml data/taxa/eukaryota/fusarium_vanettenii_77_13_4.yaml data/taxa/eukaryota/fusarium_venenatum.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI strain row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and one linked native analysis row, no exact NCBI type-material, StrainInfo, BacDive, or NCBI merged-ID rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:660122`, `label: Fusarium vanettenii 77-13-4`, `rank: STRAIN`, `parent_taxon: NCBITaxon:2747968`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:152814`, which carries the same label, parent, rank, code, exact synonym, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through parent species `Fusarium vanettenii`; the bounded scan checked all 18 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:40656`, which records one retained direct organism for `NCBITaxon:660122`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism, `Go0017718` for strain `MPVI 77-13-4`, with one linked project, `Gp0017718`, and one analysis row linked through `AP PROJECT GOLD IDS`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:660122`. The YAML preserves exact synonym `Nectria haematococca mpVI 77-13-4` and correctly has no related-synonym entries because the related-synonym field is empty upstream.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have the exact organism `Fusarium haematococca MPVI 77-13-4`, one matching project, and one native GOLD analysis for `Fusarium haematococca MPVI 77-13-4`.

The NCBI type-material table and StrainInfo inventories have no exact rows for the target.

No side `data/raw/ncbi_merged_ids.tsv` row maps an old ID into `NCBITaxon:660122`, and no retained row in `data/raw/ncbitaxon_taxa.tsv` carries a retired ID for this target, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded strain identity, NCBI and GOLD source attestations, one exact synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_vanettenii_77_13_4.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_vanettenii_77_13_4.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_vanettenii_77_13_4` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from direct rows in `data/raw/gold_organisms.tsv`; this strain-level record is counted under `NCBITaxon:660122`, not under the parent species aggregate for `NCBITaxon:2747968`.
