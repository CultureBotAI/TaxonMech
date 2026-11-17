# YAML Record Review: Hypoxylon trugodes

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hypoxylon_trugodes.yaml
- Started UTC: 2026-09-23T08:15:34Z
- Finished UTC: 2026-09-23T08:15:34Z
- Verdict: pass

## Target

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/hypoxylon_trugodes.yaml`. It carries one related NCBI synonym, no exact NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no generated local strains, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
| --- | --- |
| Prior report preflight | Passed; an exact `find` over ignored `reports/yaml_record_review` entries found no prior `*hypoxylon_trugodes.md` report. |
| `just validate data/taxa/eukaryota/hypoxylon_trugodes.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hypoxylon_rubiginosum.yaml data/taxa/eukaryota/hypoxylon_sp_kab_2019a.yaml data/taxa/eukaryota/hypoxylon_trugodes.yaml data/taxa/eukaryota/hypoxylon_vinosopulvinatum.yaml` | Passed; strict closed-schema validation exited successfully. |
| `taxonmech_bounded_scan.py data/taxa/eukaryota/hypoxylon_trugodes.yaml` plus `rg -n '^NCBITaxon:326681[[:space:]]' data/raw/ncbi_type_material.tsv` | Passed; the bounded scan found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism row with two linked native GOLD projects and no linked native GOLD analyses, four exact direct StrainInfo rows carrying six deposit rows, 13 exact NCBI type-material rows, one NCBI merged-ID side row but no retained retired old ID, no exact BacDive rows, no maintained final strain rows, and no lineage mismatches. The anchored `rg` recovered all 13 NCBI type-material rows. |
| `just verify-corpus` | Not rerun for this compact generated species record; the full generated corpus had already passed byte-for-byte reproduction from maintained inputs during this review sweep. |
| `just validate-history` | Not rerun for this compact generated species record; history records had already passed the full checkout gate during this review sweep. |
| `just validate-products` | Not applicable; this generated record has no `causal_graphs` or curator-added ontology grounding pairs to validate. |

## Identity and Grounding

The reviewed YAML identifies `NCBITaxon:326681` as `Hypoxylon trugodes`, rank `SPECIES`, domain `EUKARYOTA`, parent `NCBITaxon:42308`, and genetic code `1`. The exact row in `data/raw/ncbitaxon_taxa.tsv` carries the same taxon ID, label, parent, rank, genetic code, and `taxonomy_snapshot: 2026-09-13`, so the primary identity fields and the NCBITAXON source attestation are reproduced correctly.

The root-first lineage has 16 ancestors ending in `Hypoxylon`; every YAML ancestor was checked against the NCBI lineage carried by the committed inventory and no label, rank, or identifier mismatches were found.

The `EXACT` grounding and `SEEDED` mapping status are appropriate for a generated record whose source identity is NCBI itself. The related synonym `Hypoxylon trugodes Berk. & Broome, 1873` is present in the related NCBI synonym column for this row, and the empty exact-synonym column matches the absence of exact synonyms in the YAML.

## Evidence

| Claim | Evidence checked | Verdict |
| --- | --- | --- |
| NCBI identity, rank, lineage, genetic code, and synonyms | Exact `NCBITaxon:326681` row in `data/raw/ncbitaxon_taxa.tsv`; lineage cross-check against the committed NCBI-derived inventory | Supported exactly. |
| Scope inclusion | Exact row in `curation/seed_scope.tsv` with reason `attested rule: Hypoxylon trugodes, 2 sources incl. NCBI` | Supported exactly. |
| GOLD source attestation | Exact retained `data/raw/gold_organisms.tsv` row for `NCBITaxon:326681` with `organism_count: 1` | Supported exactly; the YAML records one GOLD organism assertion. |
| Native GOLD side evidence | Exact native GOLD organism `Go0498786` for `Hypoxylon trugodes CBS 135444` and native projects `Gp0383030` and `Gp0383031` | Supported as same-taxon side evidence. No native GOLD analysis rows are linked by these project IDs, and the native GOLD rows do not create generated child strains without a BacDive-derived local strain to join through. |
| Omitted `replaces` | Exact scans of `data/raw/ncbi_merged_ids.tsv` and retained retired NCBI rows | Supported; side-inventory old ID `NCBITaxon:1381688` maps to this taxon, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry. |
| NCBI type-material side inventory | Exact anchored scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with 13 rows covering `CBS 135444`, `MUCL 54794`, `JF13028` and LIP `JF13028` epitype variants, and holotype `K(M) 181784`. These side rows do not directly create generated `strains`. |
| Empty BacDive-derived and maintained final strain surfaces | Exact same-taxon scans of `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` | Supported; the absence of generated `strains`, genome links, and related records is consistent with the maintained final raw tables. |
| Empty StrainInfo overlay | Exact same-taxon scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported. Native StrainInfo has four exact records with six exact deposit rows for this taxon, but none overlays onto a generated BacDive-derived local strain. |
| Empty LPSN, GTDB, MediaDive, Madin et al., and BactoTraits surfaces | Exact bounded scans of the corresponding committed inventories | Supported; no same-taxon auxiliary rows are present for this record. |

## Completeness

The record is complete for the maintained generated surfaces currently present in the repository. One NCBI row, one scope row, and one retained GOLD aggregate row support the fields that are present. The NCBI type-material table has 13 exact rows for the target, but these rows are not a generated `TaxonRecord` field by themselves.

The exact native StrainInfo and GOLD rows are side evidence only here: the current pipeline emits StrainInfo and GOLD genome or related-record links only after joining to a BacDive-derived local strain entry, and there is no such local strain for `NCBITaxon:326681`. The side NCBI merged-ID row does not by itself produce `replaces`; generation uses old IDs retained in `data/raw/ncbitaxon_taxa.tsv` with a `retired_into` value.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If a future source refresh adds BacDive, StrainInfo overlay, LPSN, GTDB, or retained retired-ID rows for `NCBITaxon:326681`, rerun `just seed-canary NCBITaxon:326681`, inspect `data/taxa/eukaryota/hypoxylon_trugodes.yaml`, and rerun `just validate-strict data/taxa/eukaryota/hypoxylon_trugodes.yaml`.

## Additional Notes

The retained GOLD aggregate count comes from `data/raw/gold_organisms.tsv`. The current native GOLD organism and project rows were inspected by exact taxon ID and organism GOLD ID to confirm that the aggregate is compatible with the native side snapshot.
