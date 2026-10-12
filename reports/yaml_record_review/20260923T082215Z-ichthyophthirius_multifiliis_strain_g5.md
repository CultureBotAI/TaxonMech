# YAML Record Review: Ichthyophthirius multifiliis strain G5

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/ichthyophthirius_multifiliis_strain_g5.yaml
- Started UTC: 2026-09-23T08:22:15Z
- Finished UTC: 2026-09-23T08:22:15Z
- Verdict: pass

## Target

The target record is a generated eukaryotic strain record at `data/taxa/eukaryota/ichthyophthirius_multifiliis_strain_g5.yaml`. It carries no synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no generated local child strains, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
| --- | --- |
| Prior report preflight | Passed; an exact `find` over ignored `reports/yaml_record_review` entries found no prior `*ichthyophthirius_multifiliis_strain_g5.md` report. |
| `just validate data/taxa/eukaryota/ichthyophthirius_multifiliis_strain_g5.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/ichthyophthirius_multifiliis.yaml data/taxa/eukaryota/ichthyophthirius_multifiliis_strain_g5.yaml data/taxa/eukaryota/ichthyosporea_sp_xgb_2017a.yaml data/taxa/eukaryota/idriella_lunata.yaml` | Passed; strict closed-schema validation scanned 4 files and reported 0 errors. |
| `taxonmech_bounded_scan.py data/taxa/eukaryota/ichthyophthirius_multifiliis_strain_g5.yaml` | Passed; the bounded scan found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism row with one linked native GOLD project and one linked native GOLD analysis, no exact StrainInfo, NCBI type-material, NCBI merged-ID, or BacDive rows, no maintained final strain rows, and no lineage mismatches. |
| `just verify-corpus` | Not rerun for this compact generated strain record; the full generated corpus had already passed byte-for-byte reproduction from maintained inputs during this review sweep. |
| `just validate-history` | Not rerun for this compact generated strain record; history records had already passed the full checkout gate during this review sweep. |
| `just validate-products` | Not applicable; this generated record has no `causal_graphs` or curator-added ontology grounding pairs to validate. |

## Identity and Grounding

The reviewed YAML identifies `NCBITaxon:857967` as `Ichthyophthirius multifiliis strain G5`, rank `STRAIN`, domain `EUKARYOTA`, parent `NCBITaxon:5932`, and genetic code `6`. The exact row in `data/raw/ncbitaxon_taxa.tsv` carries the same taxon ID, label, parent, rank, genetic code, empty synonym columns, and `taxonomy_snapshot: 2026-09-13`, so the primary identity fields and the NCBITAXON source attestation are reproduced correctly.

The root-first lineage has 12 ancestors ending in species parent `Ichthyophthirius multifiliis`; every YAML ancestor was checked against the NCBI lineage carried by the committed inventory and no label, rank, or identifier mismatches were found.

The `EXACT` grounding and `SEEDED` mapping status are appropriate for a generated record whose source identity is NCBI itself. The empty exact, broad, and related NCBI synonym columns match the absence of `synonyms` in the YAML.

## Evidence

| Claim | Evidence checked | Verdict |
| --- | --- | --- |
| NCBI identity, rank, lineage, genetic code, and synonyms | Exact `NCBITaxon:857967` row in `data/raw/ncbitaxon_taxa.tsv`; lineage cross-check against the committed NCBI-derived inventory | Supported exactly. |
| Scope inclusion | Exact row in `curation/seed_scope.tsv` with reason `attested rule: Ichthyophthirius multifiliis strain G5, 2 sources incl. NCBI` | Supported exactly. |
| GOLD source attestation | Exact retained `data/raw/gold_organisms.tsv` row for `NCBITaxon:857967` with `organism_count: 1` | Supported exactly; the YAML records one GOLD organism assertion. |
| Native GOLD side evidence | Exact native GOLD organism `Go0008258`, project `Gp0008258`, and one native analysis row linked by project ID | Supported as same-taxon side evidence. The native GOLD rows do not create generated child strains without a BacDive-derived local strain to join through. |
| Empty BacDive-derived and maintained final strain surfaces | Exact same-taxon scans of `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` | Supported; the absence of generated child strains, genome links, and related records is consistent with the maintained final raw tables. |
| Empty StrainInfo overlay | Exact same-taxon scans of native StrainInfo rows, `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no exact StrainInfo row names `NCBITaxon:857967`. |
| Empty LPSN, GTDB, MediaDive, Madin et al., BactoTraits, NCBI type-material, and retired-ID surfaces | Exact bounded scans of the corresponding committed inventories | Supported; no same-taxon auxiliary rows are present for this record. |

## Completeness

The record is complete for the maintained generated surfaces currently present in the repository. One NCBI row, one scope row, and one retained GOLD aggregate row support the fields that are present. Exact scans of the maintained BacDive-derived strain tables, StrainInfo overlay tables, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, NCBI type-material, and NCBI merged-ID inventories found no same-taxon rows that should have produced additional generated YAML sections.

The exact native GOLD row is side evidence only here: the current pipeline emits GOLD genome or related-record links only after joining to a BacDive-derived local strain entry, and there is no such local strain for `NCBITaxon:857967`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If a future source refresh adds BacDive, StrainInfo overlay, LPSN, GTDB, NCBI type-material, or retained retired-ID rows for `NCBITaxon:857967`, rerun `just seed-canary NCBITaxon:857967`, inspect `data/taxa/eukaryota/ichthyophthirius_multifiliis_strain_g5.yaml`, and rerun `just validate-strict data/taxa/eukaryota/ichthyophthirius_multifiliis_strain_g5.yaml`.

## Additional Notes

The retained GOLD aggregate count comes from `data/raw/gold_organisms.tsv`. The current native GOLD organism, project, and analysis rows were inspected by exact taxon ID and by linked project ID to confirm that the aggregate is compatible with the native side snapshot.
