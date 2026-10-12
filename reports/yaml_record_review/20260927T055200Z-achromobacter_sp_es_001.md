# YAML Record Review: Achromobacter sp. ES-001

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_sp_es_001.yaml
- Started UTC: 2026-09-27T05:52:00Z
- Finished UTC: 2026-09-27T05:52:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_sp_es_001.yaml` |
| Identifier | `NCBITaxon:2860286` |
| Label | `Achromobacter sp. ES-001` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2626865` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI and GTDB inputs. Its path is
pinned by `data/taxa/PATHS.tsv:386040`, and all reviewed fields are owned by
the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs rather
than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_sp_es_001.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_sp_ep_r_88.yaml data/taxa/bacteria/achromobacter_sp_ep_r_90.yaml data/taxa/bacteria/achromobacter_sp_ep_r_93.yaml data/taxa/bacteria/achromobacter_sp_es_001.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 73 YAML lines, 10 lineage entries, 2 source attestations, 1 `skos:closeMatch` GTDB mapping, 1 GTDB exact synonym, 1 GTDB xref, 0 nomenclature entries, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact ID-only local scan | Found this identifier in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no generated side-reference rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:565477`, 1 GTDB mapping row at `data/raw/gtdb_mappings.tsv:227497`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, MediaDive, MADIN, or BactoTraits rows, no normalized strain rows, no StrainInfo assembly or related rows, no direct StrainInfo or StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:2860286` resolves in the committed NCBI inventory to label
`Achromobacter sp. ES-001`, rank `SPECIES`, parent `NCBITaxon:2626865`,
genetic code `11`, source set `ncbitaxon|gtdb`, and taxonomy snapshot
`2026-09-13`. The generated record carries those same identity fields and
lands in `bacteria` through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2626865` unclassified
Achromobacter. The bounded scan found no NCBI merge row and no retained old-id
row that would change the active identifier.

## Evidence

The NCBI row supports the `NCBITAXON` name attestation and has no exact,
related, or broad synonyms to project. The generated GTDB `skos:closeMatch`
mapping to `GTDB:s__Achromobacter_spanius_B`, `GTDB` source attestation with
9 genomes, `GTDB:s__Achromobacter_spanius_B` xref, and exact synonym
`Achromobacter spanius B` are supported by `data/raw/gtdb_mappings.tsv:227497`.

The seed event is supported by `curation/seed_scope.tsv:107132`, which records
`NCBITaxon:2860286` as added on `2026-09-13` with reason `attested rule:
Achromobacter sp. ES-001, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for expected NCBI, GTDB, seed, path, and generated
YAML inputs, and found no omitted NCBI merge, NCBI type-material, LPSN, GOLD,
BacDive, MediaDive, MADIN, BactoTraits, StrainInfo, ATB, culture-collection,
normalized assembly, normalized genome, normalized related-record, or
StrainInfo exclusion row for this taxon.

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
