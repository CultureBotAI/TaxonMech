# YAML Record Review: Kazachstania bromeliacearum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/kazachstania_bromeliacearum.yaml`
- Started UTC: 2026-09-23T04:06:18Z
- Finished UTC: 2026-09-23T04:06:18Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1006466`
- Label: `Kazachstania bromeliacearum`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:71245` / `Kazachstania`
- PATHS row: `data/taxa/PATHS.tsv:2030` maps the identifier to `kazachstania_bromeliacearum`.

## Validation

- `just validate-strict data/taxa/bacteria/pseudomonas_sp_r171a.yaml data/taxa/eukaryota/kazachstania_bromeliacearum.yaml data/taxa/bacteria/pseudomonas_sp_lm.yaml data/taxa/bacteria/gamma_proteobacterium_ge01.yaml` scanned all four files with zero errors.
- `just validate data/taxa/eukaryota/kazachstania_bromeliacearum.yaml` returned `No issues found`.

## Identity and Grounding

The record is grounded exactly to `NCBITaxon:1006466` and preserves the seeded NCBI label, species rank, eukaryotic domain, genetic code `1`, and direct parent genus `NCBITaxon:71245`.

The YAML lineage follows the same fungal genus branch implied by the pinned NCBI parent: root -> cellular organisms -> Eukaryota -> Opisthokonta -> Fungi -> Dikarya -> Ascomycota -> saccharomyceta -> Saccharomycotina -> Saccharomycetes -> Saccharomycetales -> Saccharomycetaceae -> Kazachstania.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210691` is the local pinned NCBI taxon row for `NCBITaxon:1006466`, with label `Kazachstania bromeliacearum`, rank `SPECIES`, parent `NCBITaxon:71245`, genetic code `1`, three NCBI related synonyms, GOLD support, and snapshot date `2026-09-13`.
- `data/raw/gold_organisms.tsv:163` contributes one GOLD organism assertion for `NCBITaxon:1006466`; the YAML reflects this as a `GOLD` source attestation with `assertion_count: 1` and `assertion_unit: ORGANISM`.
- `data/raw/ncbi_type_material.tsv:497` through `data/raw/ncbi_type_material.tsv:506` list ten NCBI type-material designations for this species. Those rows are local supporting context; they are not projected into `nomenclature` or `strains` without an LPSN/BacDive source row.
- Exact same-taxon searches over `data/raw`, `data/atb`, and `data/straininfo` found no ATB, StrainInfo, BacDive, GTDB, LPSN, or other auxiliary rows for this identifier, label, related synonym, or slug beyond the NCBI, GOLD, and NCBI type-material rows listed above.

## Completeness

The YAML captures all currently projected local evidence: exact NCBI identity, three NCBI related synonyms, and the single GOLD organism count. There are no local LPSN, BacDive, GTDB, ATB, or StrainInfo rows that would justify adding nomenclature entries, classified strains, taxonomy mappings, genome links, or deprecation metadata.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

No follow-up required for this record.

## Additional Notes

- Exact `find` checks against `reports/yaml_record_review` found no prior report for `kazachstania_bromeliacearum`; `find` includes ignored report files.
- Live NCBI/source lookups were not required; this review treats the pinned local source inventories as the source of truth.
