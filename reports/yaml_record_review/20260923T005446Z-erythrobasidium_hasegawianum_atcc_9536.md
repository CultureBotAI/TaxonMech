# YAML Record Review: Erythrobasidium hasegawianum ATCC 9536

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/erythrobasidium_hasegawianum_atcc_9536.yaml
- Started UTC: 2026-09-23T00:54:46Z
- Finished UTC: 2026-09-23T00:54:46Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1397323` |
| Label | `Erythrobasidium hasegawianum ATCC 9536` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5414` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/erythrobasidium_hasegawianum_atcc_9536.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/erysiphe_pisi.yaml data/taxa/eukaryota/erysiphe_pulchra.yaml data/taxa/eukaryota/erythrobasidium_hasegawianum.yaml data/taxa/eukaryota/erythrobasidium_hasegawianum_atcc_9536.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 10 organism assertions, nine exact native GOLD organism rows, two exact native GOLD project rows, no exact native GOLD analysis rows, no NCBI type-material rows, no NCBI merged-ID rows, no exact StrainInfo or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1397323`, `label: Erythrobasidium hasegawianum ATCC 9536`, `rank: STRAIN`, `parent_taxon: NCBITaxon:5414`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:343829`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the parent species `Erythrobasidium hasegawianum`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:9367`, which records 10 retained direct organisms for `NCBITaxon:1397323`; this agrees with `source_attestations[1].assertion_count: 10` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1397323`. NCBI supplies no exact, related, or broad synonyms and no old-ID side rows, so the absence of `synonyms` and `replaces` in the YAML is expected.

The current native GOLD catalogs contain nine exact organism rows for `NCBITaxon:1397323`, spanning `P36`, `NRRL Y-17193`, `NBRC 1058`, `IFO 1058`, `IAM 12911`, `DSM 7505`, `CCY 20-9-3`, `CCRC 21376`, and `CBS 8253`; only `Go0036642` for strain `P36` has current linked projects, `Gp0036641` and `Gp0036642`, and no native GOLD analysis rows are currently linked.

No exact StrainInfo, BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/erythrobasidium_hasegawianum_atcc_9536.yaml` plus `just validate-strict data/taxa/eukaryota/erythrobasidium_hasegawianum_atcc_9536.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD JSONL inputs have nine current organism rows for this taxon. The parent species keeps a separate direct-only GOLD assertion and intentionally does not roll up this strain record.
