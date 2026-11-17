# YAML Record Review: Flammispora bioteca

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/flammispora_bioteca.yaml
- Started UTC: 2026-09-23T01:43:10Z
- Finished UTC: 2026-09-23T01:43:10Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:295393` |
| Label | `Flammispora bioteca` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:295392` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/flammispora_bioteca.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/fimicolochytrium_jonesii.yaml data/taxa/eukaryota/fistulifera_pelliculosa.yaml data/taxa/eukaryota/fistulifera_solaris.yaml data/taxa/eukaryota/flammispora_bioteca.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, no current exact native GOLD organism/project/analysis rows, no exact StrainInfo rows, no NCBI type-material rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:295393`, `label: Flammispora bioteca`, `rank: SPECIES`, `parent_taxon: NCBITaxon:295392`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:60295`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Flammispora` genus; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:29417`, which records one retained direct organism for `NCBITaxon:295393`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:295393`. The YAML preserves NCBI's related synonym `Flammispora bioteca Pinruan, Sakay., K.D. Hyde & E.B.G. Jones, 2004`.

No NCBI merged-ID rows target `NCBITaxon:295393`, and no retained old IDs in `data/raw/ncbitaxon_taxa.tsv` retire into it, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies one organism assertion; the current native GOLD exact organism, project, and analysis catalogs do not contain exact rows for the target NCBI taxon.

No exact BacDive, NCBI type-material, StrainInfo, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive or StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI or GOLD inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/flammispora_bioteca.yaml` plus `just validate-strict data/taxa/eukaryota/flammispora_bioteca.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD exact catalogs are side evidence only and can differ from the retained aggregate used to generate source attestations.
