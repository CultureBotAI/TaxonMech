# YAML Record Review: Hysterangium clathroides

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hysterangium_clathroides.yaml
- Started UTC: 2026-09-23T08:19:17Z
- Finished UTC: 2026-09-23T08:19:17Z
- Verdict: pass

## Target

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/hysterangium_clathroides.yaml`. It carries one related NCBI synonym, no exact NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no generated local strains, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
| --- | --- |
| Prior report preflight | Passed; an exact `find` over ignored `reports/yaml_record_review` entries found no prior `*hysterangium_clathroides.md` report. |
| `just validate data/taxa/eukaryota/hysterangium_clathroides.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hypsizygus_marmoreus.yaml data/taxa/eukaryota/hysterangium_clathroides.yaml data/taxa/eukaryota/hysterangium_stoloniferum.yaml data/taxa/eukaryota/ichthyophonus_hoferi.yaml` | Passed; strict closed-schema validation exited successfully. |
| `taxonmech_bounded_scan.py data/taxa/eukaryota/hysterangium_clathroides.yaml` | Passed; the bounded scan found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, no exact current native GOLD organism rows, no exact native GOLD projects or analyses, no exact StrainInfo rows, no NCBI type-material rows, no NCBI merged-ID side rows, no exact BacDive rows, no maintained final strain rows, and no lineage mismatches. |
| `just verify-corpus` | Not rerun for this compact generated species record; the full generated corpus had already passed byte-for-byte reproduction from maintained inputs during this review sweep. |
| `just validate-history` | Not rerun for this compact generated species record; history records had already passed the full checkout gate during this review sweep. |
| `just validate-products` | Not applicable; this generated record has no `causal_graphs` or curator-added ontology grounding pairs to validate. |

## Identity and Grounding

The reviewed YAML identifies `NCBITaxon:112995` as `Hysterangium clathroides`, rank `SPECIES`, domain `EUKARYOTA`, parent `NCBITaxon:112993`, and genetic code `1`. The exact row in `data/raw/ncbitaxon_taxa.tsv` carries the same taxon ID, label, parent, rank, genetic code, and `taxonomy_snapshot: 2026-09-13`, so the primary identity fields and the NCBITAXON source attestation are reproduced correctly.

The root-first lineage has 13 ancestors ending in `Hysterangium`; every YAML ancestor was checked against the NCBI lineage carried by the committed inventory and no label, rank, or identifier mismatches were found.

The `EXACT` grounding and `SEEDED` mapping status are appropriate for a generated record whose source identity is NCBI itself. The related synonym `Hysterangium clathroides Vittad., 1831` is present in the related NCBI synonym column for this row, and the empty exact-synonym column matches the absence of exact synonyms in the YAML.

## Evidence

| Claim | Evidence checked | Verdict |
| --- | --- | --- |
| NCBI identity, rank, lineage, genetic code, and synonyms | Exact `NCBITaxon:112995` row in `data/raw/ncbitaxon_taxa.tsv`; lineage cross-check against the committed NCBI-derived inventory | Supported exactly. |
| Scope inclusion | Exact row in `curation/seed_scope.tsv` with reason `attested rule: Hysterangium clathroides, 2 sources incl. NCBI` | Supported exactly. |
| GOLD source attestation | Exact retained `data/raw/gold_organisms.tsv` row for `NCBITaxon:112995` with `organism_count: 2` | Supported exactly; the YAML records two GOLD organism assertions. |
| Current native GOLD side evidence | Exact current native GOLD scans by NCBI taxon ID | Supported; no current native GOLD organism, project, or analysis rows are present for this taxon, but the retained GOLD aggregate row remains the maintained source for the generated attestation. |
| Empty BacDive-derived and maintained final strain surfaces | Exact same-taxon scans of `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` | Supported; the absence of generated `strains`, genome links, and related records is consistent with the maintained final raw tables. |
| Empty StrainInfo overlay | Exact same-taxon scans of native StrainInfo rows, `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no exact StrainInfo row names `NCBITaxon:112995`. |
| Empty LPSN, GTDB, MediaDive, Madin et al., BactoTraits, NCBI type-material, and retired-ID surfaces | Exact bounded scans of the corresponding committed inventories | Supported; no same-taxon auxiliary rows are present for this record. |

## Completeness

The record is complete for the maintained generated surfaces currently present in the repository. One NCBI row, one scope row, and one retained GOLD aggregate row support the fields that are present. Exact scans of the maintained BacDive-derived strain tables, StrainInfo overlay tables, current native GOLD snapshot, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, NCBI type-material, and NCBI merged-ID inventories found no same-taxon rows that should have produced additional generated YAML sections.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If a future source refresh adds BacDive, StrainInfo overlay, LPSN, GTDB, NCBI type-material, or retained retired-ID rows for `NCBITaxon:112995`, rerun `just seed-canary NCBITaxon:112995`, inspect `data/taxa/eukaryota/hysterangium_clathroides.yaml`, and rerun `just validate-strict data/taxa/eukaryota/hysterangium_clathroides.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; in this case no exact organism row was present in the current native GOLD snapshot, and no generated child strains exist without BacDive-derived local strain inventory entries.
