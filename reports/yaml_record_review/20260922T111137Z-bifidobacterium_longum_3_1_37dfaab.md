# YAML Record Review: Bifidobacterium longum 3_1_37DFAAB
## Target
- Path: `data/taxa/bacteria/bifidobacterium_longum_3_1_37dfaab.yaml`
- Identifier: `NCBITaxon:1000567`
- Label: `Bifidobacterium longum 3_1_37DFAAB`
- Domain: `BACTERIA`
- Rank: `STRAIN`

## Validation
- PASS: `just validate data/taxa/bacteria/bifidobacterium_longum_3_1_37dfaab.yaml`
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
  - `NCBITaxon:1000567	Bifidobacterium longum 3_1_37DFAAB	STRAIN	NCBITaxon:216816	11	...	ncbitaxon|madin_etal		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the NCBI and Madin source attestations.
- `mapping_status: SEEDED` accurately reflects a generated record that has not been manually curated beyond the source import.
- `parent_taxon: NCBITaxon:216816` is represented in the lineage as `Bifidobacterium longum`, and the lineage is internally coherent:
  - `Bacteria` -> `Bacillati` -> `Actinomycetota` -> `Actinomycetes` -> `Bifidobacteriales` -> `Bifidobacteriaceae` -> `Bifidobacterium` -> `Bifidobacterium longum`
- The two exact synonyms, `Bifidobacterium longum str. 3_1_37DFAAB` and `Bifidobacterium longum strain 3_1_37DFAAB`, match the NCBI exact-synonym field in `data/raw/ncbitaxon_taxa.tsv`.
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` contains one `NCBITAXON` name assertion for `NCBITaxon:1000567`, with `source_label: Bifidobacterium longum 3_1_37DFAAB` and `assertion_count: 1`.
- `source_attestations` also contains a `MADIN` trait assertion for `NCBITaxon:1000567`; the exact `data/raw/madin_taxa.tsv` row reports five direct trait assertions.
- An ignored-file-inclusive exact scan of `data/atb` and `data/straininfo` found no same-taxon ATB or StrainInfo auxiliary rows.
- An ignored-file-inclusive exact scan of GTDB raw inputs for `NCBITaxon:1000567` and `Bifidobacterium longum 3_1_37DFAAB` found no GTDB crosswalk evidence.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries the fields expected for an NCBI-and-Madin-seeded bacterial strain record.
- `strain_count: 0` is consistent with the absence of local BacDive, ATB, and StrainInfo same-taxon links.
- Exact synonyms from NCBI are preserved; no GTDB mapping, strain inventory, publications, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if a future BacDive, ATB, StrainInfo, GTDB, or Madin snapshot links additional same-taxon evidence to `NCBITaxon:1000567`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
