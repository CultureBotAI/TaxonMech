# YAML Record Review: Methyloversatilis universalis FAM5
## Target
- Path: `data/taxa/bacteria/methyloversatilis_universalis_fam5.yaml`
- Identifier: `NCBITaxon:1000565`
- Label: `Methyloversatilis universalis FAM5`
- Domain: `BACTERIA`
- Rank: `STRAIN`

## Validation
- PASS: `just validate data/taxa/bacteria/methyloversatilis_universalis_fam5.yaml`
- PASS: `just validate-strict data/taxa/bacteria/methyloversatilis_universalis_fam5.yaml data/taxa/bacteria/halosaccharopolyspora_lacisalsi.yaml data/taxa/bacteria/bifidobacterium_longum_3_1_37dfaab.yaml data/taxa/bacteria/megasphaera_lornae.yaml`
  - `files scanned: 4`
  - `files with ERROR: 0`
  - `total ERROR rows: 0`
- SKIPPED: `just validate-history`
  - This was a read-only review of a generated record and did not add a `history/` decision.
- SKIPPED: `just verify-corpus`
  - The record was unchanged; full-corpus verification was not rerun for this four-record review batch.
- NOT APPLICABLE: `just validate-products`
  - The record has no `causal_graphs`.

## Identity and Grounding
- `identifier`, `label`, `rank`, `parent_taxon`, and `genetic_code` match the pinned NCBI source row in `data/raw/ncbitaxon_taxa.tsv`:
  - `NCBITaxon:1000565	Methyloversatilis universalis FAM5	STRAIN	NCBITaxon:378211	11	...	ncbitaxon|gtdb|gold|madin_etal		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the NCBI, GTDB, GOLD, and Madin source attestations.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:378211` is represented in the lineage as `Methyloversatilis universalis`, and the lineage is internally coherent:
  - `Bacteria` -> `Pseudomonadati` -> `Pseudomonadota` -> `Betaproteobacteria` -> `Nitrosomonadales` -> `Sterolibacteriaceae` -> `Methyloversatilis` -> `Methyloversatilis universalis`
- The GTDB mapping is internally linked through `taxonomy_mappings`, `xrefs`, and `source_attestations`, and exact raw rows in `data/raw/gtdb_species.tsv` and `data/raw/gtdb_mappings.tsv` confirm `GTDB:s__Methyloversatilis_universalis` with six genomes.
- The two NCBI exact synonyms and one GTDB exact synonym match the pinned source rows:
  - `Methyloversatilis universalis`
  - `Methyloversatilis universalis str. FAM5`
  - `Methyloversatilis universalis strain FAM5`
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` covers the four expected source groups: `NCBITAXON` name count 1, `GTDB` genome count 6, `GOLD` organism count 1, and `MADIN` trait assertion count 3.
- Exact rows in `data/raw/gold_organisms.tsv` and `data/raw/madin_taxa.tsv` match the same-taxon GOLD and Madin counts.
- The exact BacDive strain for FAM5 is keyed to parent species `NCBITaxon:378211`, not the strain taxon `NCBITaxon:1000565`; `strain_count: 0` is therefore consistent with the absence of a direct same-taxon BacDive or StrainInfo row.
- An ignored-file-inclusive exact scan of `data/atb` found no same-taxon ATB auxiliary rows.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries the fields expected for an NCBI/GTDB/GOLD/Madin-seeded bacterial strain record.
- Exact synonyms from NCBI and GTDB are preserved; no direct same-taxon BacDive strain inventory, publications, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if a future BacDive, ATB, StrainInfo, GTDB, GOLD, or Madin snapshot links additional direct same-taxon evidence to `NCBITaxon:1000565`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
