# YAML Record Review: Anaplasma marginale str. Washington Okanogan
## Target
- Path: `data/taxa/bacteria/anaplasma_marginale_str_washington_okanogan.yaml`
- Identifier: `NCBITaxon:1000937`
- Label: `Anaplasma marginale str. Washington Okanogan`
- Domain: `BACTERIA`
- Rank: `STRAIN`

## Validation
- PASS: `just validate data/taxa/bacteria/anaplasma_marginale_str_washington_okanogan.yaml`
- PASS: `just validate-strict data/taxa/bacteria/anaplasma_marginale_str_florida_relapse.yaml data/taxa/bacteria/anaplasma_marginale_str_okeechobee.yaml data/taxa/bacteria/anaplasma_marginale_str_washington_okanogan.yaml data/taxa/bacteria/anaplasma_marginale_str_oklahoma.yaml`
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
- `identifier`, `label`, `rank`, `parent_taxon`, `genetic_code`, the NCBI synonym, and the source list match the pinned NCBI source row in `data/raw/ncbitaxon_taxa.tsv`:
  - `NCBITaxon:1000937	Anaplasma marginale str. Washington Okanogan	STRAIN	NCBITaxon:770	11	Anaplasma marginale strain Washington Okanogan	...	ncbitaxon|gold|madin_etal`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the source attestation.
- `parent_taxon: NCBITaxon:770` is represented in the lineage as `Anaplasma marginale`, and the Rickettsiales lineage is internally coherent:
  - `Bacteria` -> `Pseudomonadati` -> `Pseudomonadota` -> `Alphaproteobacteria` -> `Rickettsiales` -> `Anaplasmataceae` -> `Anaplasma` -> `Anaplasma marginale`
- The absence of a `taxonomy_mappings` block and `xrefs` is consistent with the NCBI source row's provenance list and with an ignored-file-inclusive exact `data/raw/gtdb_mappings.tsv` scan for `NCBITaxon:1000937`, which found no GTDB crosswalk evidence.

## Evidence
- `source_attestations` contains the three expected source rows from `curation/seed_scope.tsv`: NCBI name count 1, GOLD organism count 1, and MADIN trait-assertion count 3.
- Exact keyed scans of `data/raw/gold_organisms.tsv` and `data/raw/madin_taxa.tsv` found the same assertion counts represented in the YAML.
- An ignored-file-inclusive exact scan of `data/atb`, `data/straininfo`, and GTDB raw inputs found no same-taxon auxiliary strain or GTDB rows for `NCBITaxon:1000937`.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries the expected NCBI, GOLD, and MADIN seed evidence for this `Anaplasma marginale` strain.
- `strain_count: 0` is consistent with the absence of local ATB and StrainInfo same-taxon links.
- No GTDB mapping, strain inventory, publications, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if a future ATB, StrainInfo, or GTDB snapshot links culture inventory or genome rows to `NCBITaxon:1000937`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
