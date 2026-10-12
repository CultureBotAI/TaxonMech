# YAML Record Review: Acetofilamentum sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetofilamentum_sp.yaml
- Started UTC: 2026-09-26T17:38:52Z
- Finished UTC: 2026-09-26T17:38:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetofilamentum_sp.yaml` |
| Identifier | `NCBITaxon:1872096` |
| Label | `Acetofilamentum sp.` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2636341` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:296618`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetofilamentum_sp.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacteroides_sp_miz14.yaml data/taxa/bacteria/acetofilamentum_rigidum.yaml data/taxa/bacteria/acetofilamentum_sp.yaml data/taxa/bacteria/acetohalobium_arabaticum.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected GTDB-pooled seeded shape: 145 YAML lines, 12 lineage entries, 11 `skos:broadMatch` taxonomy mappings, 1 `NCBITAXON`/`NAME` attestation, 1 `GTDB`/`GENOME` attestation, 0 strains, 0 xrefs, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, and `data/taxa/PATHS.tsv`; the ignored-file-inclusive scan found the 11 GTDB broadMatch rows at `data/raw/gtdb_mappings.tsv:70945` through `:70955`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:489180`, 11 matching GTDB mapping rows, 12 checked lineage entries with no missing rows or mismatches, and no LPSN, BacDive, StrainInfo, strain, NCBI type-material, NCBI merged, GOLD, MediaDive, Madin, or BactoTraits rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1872096` resolves in the committed NCBI inventory to label
`Acetofilamentum sp.`, rank `SPECIES`, parent `NCBITaxon:2636341`, genetic
code `11`, and taxonomy snapshot `2026-09-13`. The record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 12
stored taxa, from `NCBITaxon:1` root through `NCBITaxon:2636341` unclassified
Acetofilamentum. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The GTDB evidence is supported by 11 adjacent rows in
`data/raw/gtdb_mappings.tsv`, each of which maps a distinct placeholder GTDB
species to `NCBITaxon:1872096` with predicate `skos:broadMatch`. The mappings
cover 30 pooled genomes in total, and the first source attestation records the
largest component, `GTDB:s__DYMG01_sp020721655`, with 5 genomes.

The seed event is supported by `curation/seed_scope.tsv:80064`, which records
`NCBITaxon:1872096` as added on `2026-09-13` with reason `attested rule:
Acetofilamentum sp., 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated GTDB-pooled
record. The bounded scan found the expected GTDB broadMatch rows and no LPSN,
BacDive, StrainInfo, normalized strain, NCBI type-material, GOLD, MediaDive,
Madin, BactoTraits, or NCBI merge row for this target.

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
