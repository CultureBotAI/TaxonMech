# YAML Record Review: Burkholderia cepacia GG4

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/burkholderia_cepacia_gg4.yaml
- Started UTC: 2026-09-27T16:56:40Z
- Finished UTC: 2026-09-27T16:56:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/burkholderia_cepacia_gg4.yaml` |
| Identifier | `NCBITaxon:1009846` |
| Label | `Burkholderia cepacia GG4` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:292` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated Burkholderia cepacia strain record with NCBI, GTDB,
and MADIN support, with path pinned by `data/taxa/PATHS.tsv:3207`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/burkholderia_cepacia_gg4.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/vibrio_vulnificus_vv.yaml data/taxa/bacteria/burkholderia_cepacia_gg4.yaml data/taxa/bacteria/comamonas_testosteroni_atcc_11996.yaml data/taxa/bacteria/xanthomonas_oryzae_x11_5a.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 87 YAML lines, 11 lineage entries, 3 source attestations, 3 synonyms, 0 nomenclature entries, 1 taxonomy mapping, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009846` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, generated target YAML, and 1 GTDB mapping row; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211810`, 1 GTDB row, 1 MADIN row, 11 checked lineage entries with no mismatches, 0 NCBI merge rows, 0 GOLD aggregate rows, 1 native GOLD organism/project/analysis trio, no BacDive, LPSN, MediaDive, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009846` resolves to `Burkholderia cepacia GG4`, rank `STRAIN`,
parent `NCBITaxon:292`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 11 committed NCBI rows, ending at
`NCBITaxon:292` Burkholderia cepacia. The bounded scan found no NCBI merge row
and no retained old-id row.

## Evidence

The NCBI row supports the GG4 strain identity, parent, genetic code, and two
NCBI exact synonyms. The seed event is supported by
`curation/seed_scope.tsv:36078`.

GTDB line 1132 supports the `s__Burkholderia_cepacia_D` closeMatch, xref, and
GTDB exact synonym; MADIN line 406 supports 5 trait assertions. Native GOLD has
side evidence for `Go0011118` through project `Gp0011118` and analysis 6607.

## Completeness

Native GOLD side rows exist for this exact NCBI taxon, but no GOLD aggregate or
normalized genome/strain row was retained.
No BacDive, LPSN, MediaDive, BactoTraits, type-material, or StrainInfo row was
filed under this exact taxon.

An ignored-file-inclusive `rg --no-ignore --hidden` check returned no existing
Markdown report for this stem before this report was written.

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

This was a read-only generated-record review; it did not append history, promote `mapping_status`, or touch YAML.
`strain_count: 0` is expected without an exact BacDive or normalized strain row.
One GTDB closeMatch and xref are expected.
Three exact synonyms are expected.
The MADIN trait assertion row is retained on this target.
Native GOLD side rows do not currently materialize on the generated target.
No retained GOLD aggregate row is filed on this target.
No normalized assembly row is filed on this target.
No normalized genome row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Eleven NCBI lineage rows are expected.
The 87-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
