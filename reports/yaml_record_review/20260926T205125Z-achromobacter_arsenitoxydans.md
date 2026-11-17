# YAML Record Review: Achromobacter arsenitoxydans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_arsenitoxydans.yaml
- Started UTC: 2026-09-26T20:51:25Z
- Finished UTC: 2026-09-26T20:51:25Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_arsenitoxydans.yaml` |
| Identifier | `NCBITaxon:1147684` |
| Label | `Achromobacter arsenitoxydans` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI and MADIN inputs. Its path is
pinned by `data/taxa/PATHS.tsv:45395`, and all reviewed fields are owned by
the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs rather
than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_arsenitoxydans.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_arsenitoxydans.yaml data/taxa/bacteria/achromobacter_arsenitoxydans_sy8.yaml data/taxa/bacteria/achromobacter_cholinophagum.yaml data/taxa/bacteria/achromobacter_clevelandea.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 61 YAML lines, 9 lineage entries, 2 source attestations, 1 NCBI related synonym, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, NCBI, MADIN, `data/taxa/PATHS.tsv`, legacy path, and generated YAML rows; found no extra `data/atb` or generated YAML hits; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:250976`, 9 checked lineage entries with no missing rows or mismatches, 1 MADIN row, 0 NCBI merge rows, 0 GOLD aggregate rows, 0 native GOLD rows, and no GTDB, LPSN, BacDive, MediaDive, BactoTraits, type-material, normalized strain, StrainInfo assembly, StrainInfo related, direct StrainInfo, or StrainInfo deposit rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1147684` resolves in the committed NCBI inventory to label
`Achromobacter arsenitoxydans`, rank `SPECIES`, parent `NCBITaxon:222`,
genetic code `11`, source set `ncbitaxon|madin_etal`, and taxonomy snapshot
`2026-09-13`. The generated record carries those same identity fields and
correctly lands in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. The
bounded scan found no NCBI merge row and no retained old-id row that would
change the active identifier.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation and the related
synonym `"Achromobacter arsenitoxydans" Li et al. 2012`. The MADIN row supports
the `MADIN` source attestation with 2 trait assertions filed directly under
this taxon.

The seed event is supported by `curation/seed_scope.tsv:57992`, which records
`NCBITaxon:1147684` as added on `2026-09-12` with reason `attested rule:
Achromobacter arsenitoxydans, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, MADIN, seed, path, and
generated YAML inputs, and found no omitted GTDB, LPSN, BacDive, MediaDive,
GOLD, BactoTraits, StrainInfo, ATB, culture-collection, type-material,
normalized assembly, normalized genome, or normalized related-record row for
this taxon.

The exact scan also found an old `curation/legacy_page_paths.tsv` entry for the
same taxon. That row only records the historical HTML path and does not imply
an omitted `TaxonRecord` field.

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
