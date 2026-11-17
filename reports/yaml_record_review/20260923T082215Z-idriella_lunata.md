# YAML Record Review: Idriella lunata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/idriella_lunata.yaml
- Started UTC: 2026-09-23T08:22:15Z
- Finished UTC: 2026-09-23T08:22:15Z
- Verdict: pass

## Target

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/idriella_lunata.yaml`. It carries two related NCBI synonyms, no exact NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no generated local strains, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
| --- | --- |
| Prior report preflight | Passed; an exact `find` over ignored `reports/yaml_record_review` entries found no prior `*idriella_lunata.md` report. |
| `just validate data/taxa/eukaryota/idriella_lunata.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/ichthyophthirius_multifiliis.yaml data/taxa/eukaryota/ichthyophthirius_multifiliis_strain_g5.yaml data/taxa/eukaryota/ichthyosporea_sp_xgb_2017a.yaml data/taxa/eukaryota/idriella_lunata.yaml` | Passed; strict closed-schema validation scanned 4 files and reported 0 errors. |
| `taxonmech_bounded_scan.py data/taxa/eukaryota/idriella_lunata.yaml` | Passed; the bounded scan found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism row with two linked native GOLD projects and no linked native GOLD analyses, 17 exact direct StrainInfo rows carrying 22 deposit rows, two exact NCBI type-material rows, no NCBI merged-ID side rows, no exact BacDive rows, no maintained final strain rows, and no lineage mismatches. |
| `just verify-corpus` | Not rerun for this compact generated species record; the full generated corpus had already passed byte-for-byte reproduction from maintained inputs during this review sweep. |
| `just validate-history` | Not rerun for this compact generated species record; history records had already passed the full checkout gate during this review sweep. |
| `just validate-products` | Not applicable; this generated record has no `causal_graphs` or curator-added ontology grounding pairs to validate. |

## Identity and Grounding

The reviewed YAML identifies `NCBITaxon:1446843` as `Idriella lunata`, rank `SPECIES`, domain `EUKARYOTA`, parent `NCBITaxon:412494`, and genetic code `1`. The exact row in `data/raw/ncbitaxon_taxa.tsv` carries the same taxon ID, label, parent, rank, genetic code, and `taxonomy_snapshot: 2026-09-13`, so the primary identity fields and the NCBITAXON source attestation are reproduced correctly.

The root-first lineage has 16 ancestors ending in `Idriella`; every YAML ancestor was checked against the NCBI lineage carried by the committed inventory and no label, rank, or identifier mismatches were found.

The `EXACT` grounding and `SEEDED` mapping status are appropriate for a generated record whose source identity is NCBI itself. The related synonyms `Idriella lunata P.E. Nelson & S. Wilh., 1956` and `Idriella lunata P.E. Nelson & S. Wilhelm, 1956` are present in the related NCBI synonym column for this row, and the empty exact-synonym column matches the absence of exact synonyms in the YAML.

## Evidence

| Claim | Evidence checked | Verdict |
| --- | --- | --- |
| NCBI identity, rank, lineage, genetic code, and synonyms | Exact `NCBITaxon:1446843` row in `data/raw/ncbitaxon_taxa.tsv`; lineage cross-check against the committed NCBI-derived inventory | Supported exactly. |
| Scope inclusion | Exact row in `curation/seed_scope.tsv` with reason `attested rule: Idriella lunata, 2 sources incl. NCBI` | Supported exactly. |
| GOLD source attestation | Exact retained `data/raw/gold_organisms.tsv` row for `NCBITaxon:1446843` with `organism_count: 1` | Supported exactly; the YAML records one GOLD organism assertion. |
| Native GOLD side evidence | Exact native GOLD organism `Go0609082` for `Idriella lunata CBS 204.56` and native projects `Gp0620743` and `Gp0688259` | Supported as same-taxon side evidence. No native GOLD analysis rows are linked by these project IDs, and the native GOLD rows do not create generated child strains without a BacDive-derived local strain to join through. |
| NCBI type-material side inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with `CBS 204.56` and `CBS:204.56` type-material aliases. These side rows do not directly create generated `strains`. |
| Empty BacDive-derived and maintained final strain surfaces | Exact same-taxon scans of `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` | Supported; the absence of generated `strains`, genome links, and related records is consistent with the maintained final raw tables. |
| Empty StrainInfo overlay | Exact same-taxon scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported. Native StrainInfo has 17 exact records with 22 exact deposit rows for this taxon, but none overlays onto a generated BacDive-derived local strain. |
| Empty LPSN, GTDB, MediaDive, Madin et al., BactoTraits, and retired-ID surfaces | Exact bounded scans of the corresponding committed inventories | Supported; no same-taxon auxiliary rows are present for this record. |

## Completeness

The record is complete for the maintained generated surfaces currently present in the repository. One NCBI row, one scope row, and one retained GOLD aggregate row support the fields that are present. The NCBI type-material table has two exact rows for the target, but these rows are not a generated `TaxonRecord` field by themselves.

The exact native StrainInfo and GOLD rows are side evidence only here: the current pipeline emits StrainInfo and GOLD genome or related-record links only after joining to a BacDive-derived local strain entry, and there is no such local strain for `NCBITaxon:1446843`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If a future source refresh adds BacDive, StrainInfo overlay, LPSN, GTDB, or retained retired-ID rows for `NCBITaxon:1446843`, rerun `just seed-canary NCBITaxon:1446843`, inspect `data/taxa/eukaryota/idriella_lunata.yaml`, and rerun `just validate-strict data/taxa/eukaryota/idriella_lunata.yaml`.

## Additional Notes

The retained GOLD aggregate count comes from `data/raw/gold_organisms.tsv`. The current native GOLD organism and project rows were inspected by exact taxon ID and organism GOLD ID to confirm that the aggregate is compatible with the native side snapshot.
