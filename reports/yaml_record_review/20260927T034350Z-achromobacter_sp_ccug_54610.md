# YAML Record Review: Achromobacter sp. CCUG 54610

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_sp_ccug_54610.yaml
- Started UTC: 2026-09-27T03:43:50Z
- Finished UTC: 2026-09-27T03:43:50Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_sp_ccug_54610.yaml` |
| Identifier | `NCBITaxon:1389638` |
| Label | `Achromobacter sp. CCUG 54610` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2626865` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI and BacDive inputs. Its path is
pinned by `data/taxa/PATHS.tsv:141555`, and all reviewed fields are owned by
the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs rather
than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_sp_ccug_54610.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_sp_ccug_44449.yaml data/taxa/bacteria/achromobacter_sp_ccug_54610.yaml data/taxa/bacteria/achromobacter_sp_ccug_56089.yaml data/taxa/bacteria/achromobacter_sp_cd8.yaml` | Passed strict validation with 4 files scanned, 0 files in error, and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 104 YAML lines, 10 lineage entries, 2 source attestations, 1 BacDive strain, 1 culture collection ID, 2 related records, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact ID-only local scan | Found this identifier in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no generated side-reference rows; found no prior ignored report for this identifier. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:340687`, 10 checked lineage entries with no missing rows or mismatches, 1 matching BacDive record, the BacDive row at `data/raw/bacdive_strains.tsv:76866`, the culture row at `data/raw/culture_collection_strains.tsv:31668`, 2 StrainInfo related rows in `data/straininfo/related_records.tsv.gz`, 0 NCBI merge rows, 0 NCBI type-material rows, and no GOLD, LPSN, GTDB, MediaDive, MADIN, BactoTraits, genome, or assembly rows for this taxon. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1389638` resolves in the committed NCBI inventory to label
`Achromobacter sp. CCUG 54610`, rank `SPECIES`, parent `NCBITaxon:2626865`,
genetic code `11`, source set `ncbitaxon|bacdive`, and taxonomy snapshot
`2026-09-13`. The generated record carries those same identity fields and
correctly lands in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2626865` unclassified
Achromobacter. The bounded scan found no NCBI merge row and no retained old-id
row that would change the active identifier.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation; BacDive record
`154621` and `data/raw/bacdive_strains.tsv:76866` support the BACDIVE strain
attestation for `kgmicrobe.strain:bacdive_154621` and culture ID
`kgmicrobe.strain:CCUG-54610`.

The two StrainInfo related records are backed by compressed rows
`data/straininfo/related_records.tsv.gz:121838` and `:121839`; both are matched
through `CCUG 54610` and keep StrainInfo's native `NCBITaxon:85698` taxon. The
seed event is supported by `curation/seed_scope.tsv:51430`, which records this
identifier as added on `2026-09-12` with 2 sources including NCBI.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, seed, path, BacDive,
culture-collection, StrainInfo related-record, and generated YAML inputs, and
found no omitted NCBI merge, NCBI type-material, LPSN, GTDB, GOLD, MediaDive,
MADIN, BactoTraits, normalized assembly, normalized genome, or strain exclusion
row for this taxon.

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

This was a read-only generated-record review; it did not append a curation
event, promote `mapping_status`, write history, or touch the seeded YAML.
