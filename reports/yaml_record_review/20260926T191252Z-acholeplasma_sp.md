# YAML Record Review: Acholeplasma sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_sp.yaml
- Started UTC: 2026-09-26T19:12:52Z
- Finished UTC: 2026-09-26T19:12:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_sp.yaml` |
| Identifier | `NCBITaxon:33015` |
| Label | `Acholeplasma sp.` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2644011` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:441302`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_sp.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_palmae.yaml data/taxa/bacteria/acholeplasma_pleciae.yaml data/taxa/bacteria/acholeplasma_sp.yaml data/taxa/bacteria/acholeplasma_sp_assh51.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected enriched generated shape: 243 YAML lines, 10 lineage entries, 3 source attestations, 0 nomenclature entries, 11 GTDB `skos:broadMatch` mappings, 1 NCBI exact synonym, 0 xrefs, 2 BacDive strains, 4 culture collection IDs, 0 genome assemblies, 0 genome records, 4 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, GTDB, BacDive, culture-collection, and generated YAML rows, and used an exact compressed StrainInfo scan to confirm the four genus-scoped related records; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:3474`, 10 checked lineage entries with no missing rows or mismatches, 11 GTDB `skos:broadMatch` rows, 2 exact BacDive hits, 4 normalized culture-collection rows, 0 NCBI merge rows, and 0 LPSN, Madin, MediaDive, BactoTraits, GOLD, AllTheBacteria, target-scoped StrainInfo, assembly, or genome rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:33015` resolves in the committed NCBI inventory to label
`Acholeplasma sp.`, rank `SPECIES`, parent `NCBITaxon:2644011`, genetic code
`11`, and taxonomy snapshot `2026-09-13`. The record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2644011` unclassified
Acholeplasma. There are no retained old identifiers for this target in the NCBI
merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:33015`, source label `Acholeplasma sp.`, `assertion_count: 1`,
`assertion_unit: NAME`, and the 2026-09-13 snapshot note all match.

The taxonomy mappings are exactly the 11 committed GTDB `skos:broadMatch` rows
for this unclassified species target, ranging from the 12-genome
`GTDB:s__Faecisoma_sp000432255` row to several 1-genome rows. The single
NCBI exact synonym, `Sapromyces sp.`, is carried from the NCBI row.

BacDive rows `174853` and `174854` provide the M4Ah and Holly strain payloads,
and the 4 normalized culture collection rows cover `DSM-112561`,
`DSM-116280`, `UQM%2041475`, and `VKM-B-3485`. The only related records are
four genus-scoped StrainInfo deposit/strain rows for `straininfo.strain:281834`
and `straininfo.strain:283039`, linked back through `bacdive_174853` and
`bacdive_174854`.

The seed event is supported by `curation/seed_scope.tsv:51150`, which records
`NCBITaxon:33015` as added on `2026-09-12` with reason `attested rule:
Acholeplasma sp., 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated enriched record.
The exact and bounded scans account for the expected NCBI, GTDB, BacDive,
StrainInfo, and strain-normalization inputs, and found no NCBI merge, LPSN,
Madin, MediaDive, BactoTraits, GOLD, AllTheBacteria, assembly, genome, or
target-scoped StrainInfo row that would require another YAML section.

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
