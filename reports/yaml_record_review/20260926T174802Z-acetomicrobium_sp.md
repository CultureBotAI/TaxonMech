# YAML Record Review: Acetomicrobium sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetomicrobium_sp.yaml
- Started UTC: 2026-09-26T17:48:02Z
- Finished UTC: 2026-09-26T17:48:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetomicrobium_sp.yaml` |
| Identifier | `NCBITaxon:1872099` |
| Label | `Acetomicrobium sp.` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2627317` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:296620`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetomicrobium_sp.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetomicrobium_hydrogeniformans_atcc_baa_1850.yaml data/taxa/bacteria/acetomicrobium_mobile.yaml data/taxa/bacteria/acetomicrobium_mobile_dsm_13181.yaml data/taxa/bacteria/acetomicrobium_sp.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected GTDB-pooled seeded shape: 87 YAML lines, 10 lineage entries, 3 `skos:broadMatch` taxonomy mappings, 1 exact NCBI synonym, 1 `NCBITAXON`/`NAME` attestation, 1 `GTDB`/`GENOME` attestation, 0 strains, 0 xrefs, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/raw/ncbi_merged_ids.tsv`, `data/raw/gtdb_mappings.tsv`, and `data/taxa/PATHS.tsv`; the ignored-file-inclusive scan found the 3 GTDB broadMatch rows at `data/raw/gtdb_mappings.tsv:70956` through `:70958`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:489182`, 3 matching GTDB mapping rows, 1 NCBI merge row retaining old ID `NCBITaxon:1872509`, 10 checked lineage entries with no missing rows or mismatches, and no LPSN, BacDive, StrainInfo, strain, NCBI type-material, GOLD, MediaDive, Madin, or BactoTraits rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1872099` resolves in the committed NCBI inventory to label
`Acetomicrobium sp.`, rank `SPECIES`, parent `NCBITaxon:2627317`, exact synonym
`Anaerobaculum sp.`, genetic code `11`, and taxonomy snapshot `2026-09-13`.
The record carries those same identity fields and correctly lands in the
`bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10
stored taxa, from `NCBITaxon:1` root through `NCBITaxon:2627317` unclassified
Acetomicrobium. The raw NCBI merge input also records retained old ID
`NCBITaxon:1872509` as merged into this target.

## Evidence

The GTDB evidence is supported by 3 adjacent rows in
`data/raw/gtdb_mappings.tsv`, each of which maps a distinct placeholder GTDB
species to `NCBITaxon:1872099` with predicate `skos:broadMatch`. The mappings
cover 33 pooled genomes in total, and the source attestation correctly records
the largest component, `GTDB:s__Acetomicrobium_sp012518015`, with 24 genomes.

The seed event is supported by `curation/seed_scope.tsv:80065`, which records
`NCBITaxon:1872099` as added on `2026-09-13` with reason `attested rule:
Acetomicrobium sp., 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated GTDB-pooled
record. The bounded scan found the expected GTDB broadMatch and NCBI merge rows
and no LPSN, BacDive, StrainInfo, normalized strain, NCBI type-material, GOLD,
MediaDive, Madin, or BactoTraits row for this target.

An ignored-file-inclusive `find` under `reports/yaml_record_review` returned no
existing Markdown report for this stem before this report was written.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

This was a read-only generated-record review. It did not append a curation
event, promote `mapping_status`, write a history record, or touch the seeded
YAML.
