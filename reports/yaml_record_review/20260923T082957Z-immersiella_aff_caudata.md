# YAML Record Review: Immersiella aff. caudata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/immersiella_aff_caudata.yaml
- Started UTC: 2026-09-23T08:29:57Z
- Finished UTC: 2026-09-23T08:29:57Z
- Verdict: pass

## Target

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/immersiella_aff_caudata.yaml`. It carries no synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no generated local strains, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
| --- | --- |
| Prior report preflight | Passed; an exact `find` over ignored `reports/yaml_record_review` entries found no prior `*immersiella_aff_caudata.md` report. |
| `just validate data/taxa/eukaryota/immersiella_aff_caudata.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/ilyonectria_sp.yaml data/taxa/eukaryota/imleria_badia.yaml data/taxa/eukaryota/imleria_badia_us_2013.yaml data/taxa/eukaryota/immersiella_aff_caudata.yaml` | Passed; strict closed-schema validation scanned 4 files and reported 0 errors. |
| `taxonmech_bounded_scan.py data/taxa/eukaryota/immersiella_aff_caudata.yaml` | Passed; the bounded scan found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism row with two linked native GOLD projects and no linked native GOLD analyses, no exact StrainInfo, NCBI type-material, NCBI merged-ID, or BacDive rows, no maintained final strain rows, and no lineage mismatches. |
| `just verify-corpus` | Not rerun for this compact generated species record; the full generated corpus had already passed byte-for-byte reproduction from maintained inputs during this review sweep. |
| `just validate-history` | Not rerun for this compact generated species record; history records had already passed the full checkout gate during this review sweep. |
| `just validate-products` | Not applicable; this generated record has no `causal_graphs` or curator-added ontology grounding pairs to validate. |

## Identity and Grounding

The reviewed YAML identifies `NCBITaxon:3127102` as `Immersiella aff. caudata`, rank `SPECIES`, domain `EUKARYOTA`, parent `NCBITaxon:260662`, and genetic code `1`. The exact row in `data/raw/ncbitaxon_taxa.tsv` carries the same taxon ID, label, parent, rank, genetic code, empty synonym columns, and `taxonomy_snapshot: 2026-09-13`, so the primary identity fields and the NCBITAXON source attestation are reproduced correctly.

The root-first lineage has 16 ancestors ending in `Immersiella`; every YAML ancestor was checked against the NCBI lineage carried by the committed inventory and no label, rank, or identifier mismatches were found.

The `EXACT` grounding and `SEEDED` mapping status are appropriate for a generated record whose source identity is NCBI itself. The empty exact, broad, and related NCBI synonym columns match the absence of `synonyms` in the YAML.

## Evidence

| Claim | Evidence checked | Verdict |
| --- | --- | --- |
| NCBI identity, rank, lineage, genetic code, and synonyms | Exact `NCBITaxon:3127102` row in `data/raw/ncbitaxon_taxa.tsv`; lineage cross-check against the committed NCBI-derived inventory | Supported exactly. |
| Scope inclusion | Exact row in `curation/seed_scope.tsv` with reason `attested rule: Immersiella aff. caudata, 2 sources incl. NCBI` | Supported exactly. |
| GOLD source attestation | Exact retained `data/raw/gold_organisms.tsv` row for `NCBITaxon:3127102` with `organism_count: 1` | Supported exactly; the YAML records one GOLD organism assertion. |
| Native GOLD side evidence | Exact native GOLD organism `Go0583346` filed under `ORGANISM NCBI TAX ID` 3127102 with projects `Gp0587287` and `Gp0587288` | Supported as same-NCBI-ID side evidence. The native GOLD organism row is named `Cercophora aff. Caudata PSN171`, but the row is filed under this target's NCBI taxon ID and does not create generated child strains without a BacDive-derived local strain to join through. |
| Empty BacDive-derived and maintained final strain surfaces | Exact same-taxon scans of `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` | Supported; the absence of generated `strains`, genome links, and related records is consistent with the maintained final raw tables. |
| Empty StrainInfo overlay | Exact same-taxon scans of native StrainInfo rows, `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no exact StrainInfo row names `NCBITaxon:3127102`. |
| Empty LPSN, GTDB, MediaDive, Madin et al., BactoTraits, NCBI type-material, and retired-ID surfaces | Exact bounded scans of the corresponding committed inventories | Supported; no same-taxon auxiliary rows are present for this record. |

## Completeness

The record is complete for the maintained generated surfaces currently present in the repository. One NCBI row, one scope row, and one retained GOLD aggregate row support the fields that are present. Exact scans of the maintained BacDive-derived strain tables, StrainInfo overlay tables, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, NCBI type-material, and NCBI merged-ID inventories found no same-taxon rows that should have produced additional generated YAML sections.

The exact native GOLD row is side evidence only here: the current pipeline emits GOLD genome or related-record links only after joining to a BacDive-derived local strain entry, and there is no such local strain for `NCBITaxon:3127102`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If a future source refresh adds BacDive, StrainInfo overlay, LPSN, GTDB, NCBI type-material, or retained retired-ID rows for `NCBITaxon:3127102`, rerun `just seed-canary NCBITaxon:3127102`, inspect `data/taxa/eukaryota/immersiella_aff_caudata.yaml`, and rerun `just validate-strict data/taxa/eukaryota/immersiella_aff_caudata.yaml`.

## Additional Notes

The retained GOLD aggregate count comes from `data/raw/gold_organisms.tsv`. The current native GOLD organism and project rows were inspected by exact taxon ID and organism GOLD ID to confirm that the aggregate is compatible with the native side snapshot.
