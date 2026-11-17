# YAML Record Review: Hypoxylon fragiforme

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hypoxylon_fragiforme.yaml
- Started UTC: 2026-09-23T08:09:41Z
- Finished UTC: 2026-09-23T08:09:41Z
- Verdict: pass

## Target

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/hypoxylon_fragiforme.yaml`. It carries one exact NCBI synonym, two related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no generated local strains, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
| --- | --- |
| Prior report preflight | Passed; an exact `find` over ignored `reports/yaml_record_review` entries found no prior `*hypoxylon_fragiforme.md` report. |
| `just validate data/taxa/eukaryota/hypoxylon_fragiforme.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hypoxylon_argillaceum.yaml data/taxa/eukaryota/hypoxylon_cercidicola.yaml data/taxa/eukaryota/hypoxylon_crocopeplum.yaml data/taxa/eukaryota/hypoxylon_fragiforme.yaml` | Passed; strict closed-schema validation scanned 4 files and reported 0 errors. |
| `taxonmech_bounded_scan.py data/taxa/eukaryota/hypoxylon_fragiforme.yaml` | Passed; the bounded scan found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism row with two linked native GOLD projects and no linked native GOLD analyses, 27 exact direct StrainInfo rows carrying 33 deposit rows, two NCBI type-material rows, two NCBI merged-ID side rows but no retained retired old IDs, no exact BacDive rows, no maintained final strain rows, and no lineage mismatches. |
| `just verify-corpus` | Not rerun for this compact generated species record; the full generated corpus had already passed byte-for-byte reproduction from maintained inputs during this review sweep. |
| `just validate-history` | Not rerun for this compact generated species record; history records had already passed the full checkout gate during this review sweep. |
| `just validate-products` | Not applicable; this generated record has no `causal_graphs` or curator-added ontology grounding pairs to validate. |

## Identity and Grounding

The reviewed YAML identifies `NCBITaxon:63214` as `Hypoxylon fragiforme`, rank `SPECIES`, domain `EUKARYOTA`, parent `NCBITaxon:42308`, and genetic code `1`. The exact row in `data/raw/ncbitaxon_taxa.tsv` carries the same taxon ID, label, parent, rank, genetic code, and `taxonomy_snapshot: 2026-09-13`, so the primary identity fields and the NCBITAXON source attestation are reproduced correctly.

The root-first lineage has 16 ancestors ending in `Hypoxylon`; every YAML ancestor was checked against the NCBI lineage carried by the committed inventory and no label, rank, or identifier mismatches were found.

The `EXACT` grounding and `SEEDED` mapping status are appropriate for a generated record whose source identity is NCBI itself. The exact synonym `Sphaeria fragiformis` and the related synonyms `Hypoxylon fragiforme (Pers.) J. Kickx f., 1835` and `Sphaeria fragiformis Pers., 1794` are present in the exact and related NCBI synonym columns for this row.

## Evidence

| Claim | Evidence checked | Verdict |
| --- | --- | --- |
| NCBI identity, rank, lineage, genetic code, and synonyms | Exact `NCBITaxon:63214` row in `data/raw/ncbitaxon_taxa.tsv`; lineage cross-check against the committed NCBI-derived inventory | Supported exactly. |
| Scope inclusion | Exact row in `curation/seed_scope.tsv` with reason `attested rule: Hypoxylon fragiforme, 2 sources incl. NCBI` | Supported exactly. |
| GOLD source attestation | Exact retained `data/raw/gold_organisms.tsv` row for `NCBITaxon:63214` with `organism_count: 1` | Supported exactly; the YAML records one GOLD organism assertion. |
| Native GOLD side evidence | Exact native GOLD organism `Go0498779` for `Hypoxylon fragiforme CBS 206.31` and native projects `Gp0383017` and `Gp0383018` | Supported as same-taxon side evidence. No native GOLD analysis rows are linked by these project IDs, and the native GOLD rows do not create generated child strains without a BacDive-derived local strain to join through. |
| Omitted `replaces` | Exact scans of `data/raw/ncbi_merged_ids.tsv` and retained retired NCBI rows | Supported; side-inventory old IDs `NCBITaxon:557942` and `NCBITaxon:557943` map to this taxon, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry. |
| NCBI type-material side inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with `MUCL 51264` and `MUCL:51264` culture-from-epitype aliases. These side rows do not directly create generated `strains`. |
| Empty BacDive-derived and maintained final strain surfaces | Exact same-taxon scans of `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` | Supported; the absence of generated `strains`, genome links, and related records is consistent with the maintained final raw tables. |
| Empty StrainInfo overlay | Exact same-taxon scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported. Native StrainInfo has 27 exact records with 33 exact deposit rows for this taxon, but none overlays onto a generated BacDive-derived local strain. |
| Empty LPSN, GTDB, MediaDive, Madin et al., and BactoTraits surfaces | Exact bounded scans of the corresponding committed inventories | Supported; no same-taxon auxiliary rows are present for this record. |

## Completeness

The record is complete for the maintained generated surfaces currently present in the repository. One NCBI row, one scope row, and one retained GOLD aggregate row support the fields that are present. The NCBI type-material table has two exact rows for the target; these rows preserve `MUCL 51264` culture-from-epitype spelling variants but are not a generated `TaxonRecord` field by themselves.

The exact native StrainInfo and GOLD rows are side evidence only here: the current pipeline emits StrainInfo and GOLD genome or related-record links only after joining to a BacDive-derived local strain entry, and there is no such local strain for `NCBITaxon:63214`. The side NCBI merged-ID rows do not by themselves produce `replaces`; generation uses old IDs retained in `data/raw/ncbitaxon_taxa.tsv` with a `retired_into` value.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If a future source refresh adds BacDive, StrainInfo overlay, LPSN, GTDB, or retained retired-ID rows for `NCBITaxon:63214`, rerun `just seed-canary NCBITaxon:63214`, inspect `data/taxa/eukaryota/hypoxylon_fragiforme.yaml`, and rerun `just validate-strict data/taxa/eukaryota/hypoxylon_fragiforme.yaml`.

## Additional Notes

The retained GOLD aggregate count comes from `data/raw/gold_organisms.tsv`. The current native GOLD organism and project rows were inspected by exact taxon ID and organism GOLD ID to confirm that the aggregate is compatible with the native side snapshot.
