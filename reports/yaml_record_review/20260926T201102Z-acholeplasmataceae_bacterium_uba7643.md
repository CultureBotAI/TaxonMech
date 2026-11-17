# YAML Record Review: Acholeplasmataceae bacterium UBA7643

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasmataceae_bacterium_uba7643.yaml
- Started UTC: 2026-09-26T20:11:02Z
- Finished UTC: 2026-09-26T20:11:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasmataceae_bacterium_uba7643.yaml` |
| Identifier | `NCBITaxon:1951333` |
| Label | `Acholeplasmataceae bacterium UBA7643` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1898208` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI and GTDB inputs. Its path is
pinned by `data/taxa/PATHS.tsv:310506`, and all reviewed fields are owned by
the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs rather
than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasmataceae_bacterium_uba7643.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasmataceae_bacterium_uba7643.yaml data/taxa/bacteria/acholeplasmatales_bacterium.yaml data/taxa/bacteria/acholeplasmatales_bacterium_canine_oral_taxon_172.yaml data/taxa/bacteria/acholeplasmatales_bacterium_canine_oral_taxon_256.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 70 YAML lines, 9 lineage entries, 2 source attestations, 0 nomenclature entries, 1 GTDB `skos:closeMatch` mapping, 1 GTDB exact synonym, 1 xref, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:502121`, 9 checked lineage entries with no missing rows or mismatches, 1 GTDB closeMatch row at `data/raw/gtdb_mappings.tsv:106787`, 0 NCBI merge rows, and 0 GOLD, LPSN, BacDive, StrainInfo, Madin, MediaDive, BactoTraits, type-material, normalized assembly, genome, or related-record rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1951333` resolves in the committed NCBI inventory to label
`Acholeplasmataceae bacterium UBA7643`, rank `SPECIES`, parent
`NCBITaxon:1898208`, genetic code `11`, source set `ncbitaxon|gtdb`, and
taxonomy snapshot `2026-09-13`. The generated record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:1898208` unclassified
Acholeplasmataceae. There are no retained old identifiers for this target in
the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:1951333`, source label `Acholeplasmataceae bacterium UBA7643`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The GTDB evidence is supported by one committed `skos:closeMatch` row:
`GTDB:s__UBA5409_sp002410615`, label `s__UBA5409_sp002410615`, parent
`GTDB:g__UBA5409`, and `genome_count: 25`. The YAML preserves this mapping,
copies the 25-genome count into the representative GTDB attestation, adds the
expected exact synonym `UBA5409 sp002410615`, and records the same GTDB ID as
an xref.

The seed event is supported by `curation/seed_scope.tsv:86106`, which records
`NCBITaxon:1951333` as added on `2026-09-13` with reason `attested rule:
Acholeplasmataceae bacterium UBA7643, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated NCBI and GTDB
record. The exact and bounded scans account for the expected NCBI, GTDB, and
generated YAML inputs, and found no NCBI merge, LPSN, GOLD, BacDive,
StrainInfo, Madin, MediaDive, BactoTraits, type-material, normalized assembly,
normalized genome, or normalized related-record row that would require an
enriched YAML section.

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
