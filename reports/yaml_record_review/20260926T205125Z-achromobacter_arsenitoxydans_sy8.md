# YAML Record Review: Achromobacter arsenitoxydans SY8

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_arsenitoxydans_sy8.yaml
- Started UTC: 2026-09-26T20:51:25Z
- Finished UTC: 2026-09-26T20:51:25Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_arsenitoxydans_sy8.yaml` |
| Identifier | `NCBITaxon:477184` |
| Label | `Achromobacter arsenitoxydans SY8` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1147684` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, and MADIN inputs. Its
path is pinned by `data/taxa/PATHS.tsv:514572`, and all reviewed fields are
owned by the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs
rather than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_arsenitoxydans_sy8.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_arsenitoxydans.yaml data/taxa/bacteria/achromobacter_arsenitoxydans_sy8.yaml data/taxa/bacteria/achromobacter_cholinophagum.yaml data/taxa/bacteria/achromobacter_clevelandea.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 90 YAML lines, 10 lineage entries, 3 source attestations, 1 GTDB `skos:closeMatch` mapping, 5 exact synonyms, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, NCBI, GTDB, MADIN, NCBI merge, `data/taxa/PATHS.tsv`, legacy path, and generated YAML rows; found no extra `data/atb` or generated YAML hits; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:106553`, 10 checked lineage entries with no missing rows or mismatches, 1 GTDB closeMatch row, 1 MADIN row, 2 NCBI merge rows, 1 native GOLD organism/project/analysis, 0 GOLD aggregate rows, and no LPSN, BacDive, MediaDive, BactoTraits, type-material, normalized assembly, normalized genome, normalized related-record, StrainInfo assembly, StrainInfo related, direct StrainInfo, or StrainInfo deposit rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:477184` resolves in the committed NCBI inventory to label
`Achromobacter arsenitoxydans SY8`, rank `STRAIN`, parent
`NCBITaxon:1147684`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, and taxonomy snapshot `2026-09-13`. The generated
record carries those same identity fields and correctly lands in the `bacteria`
path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10
stored taxa, from `NCBITaxon:1` root through `NCBITaxon:1147684`
Achromobacter arsenitoxydans. Two NCBI merge rows retire
`NCBITaxon:1094977` and `NCBITaxon:437225` into this identifier, and the
bounded scan found no retained raw `ncbitaxon_taxa.tsv` row for either old ID.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation and the four NCBI
exact synonyms. The GTDB evidence is the single
`GTDB:s__Achromobacter_arsenitoxydans` closeMatch row with `genome_count: 1`;
that row also supports the GTDB exact synonym and xref. The MADIN row supports
5 trait assertions filed directly under the strain taxon.

The seed event is supported by `curation/seed_scope.tsv:32899`, which records
`NCBITaxon:477184` as added on `2026-09-12` with reason `attested rule:
Achromobacter arsenitoxydans SY8, 3 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, GTDB, MADIN, seed, path, merge,
and generated YAML inputs, and found no omitted LPSN, BacDive, MediaDive, GOLD
aggregate, BactoTraits, StrainInfo, ATB, culture-collection, type-material,
normalized assembly, normalized genome, or normalized related-record row for
this taxon.

The native GOLD exact hits have no matching `data/raw/gold_organisms.tsv`
aggregate row, so they do not contribute a seeded GOLD attestation or YAML
section in this generated record.

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
