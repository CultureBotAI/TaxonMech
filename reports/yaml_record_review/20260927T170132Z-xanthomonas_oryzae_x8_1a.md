# YAML Record Review: Xanthomonas oryzae X8-1A

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/xanthomonas_oryzae_x8_1a.yaml
- Started UTC: 2026-09-27T17:01:32Z
- Finished UTC: 2026-09-27T17:01:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/xanthomonas_oryzae_x8_1a.yaml` |
| Identifier | `NCBITaxon:1009854` |
| Label | `Xanthomonas oryzae X8-1A` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:347` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated Xanthomonas oryzae strain record with NCBI, GTDB, and
MADIN support, with path pinned by `data/taxa/PATHS.tsv:3210`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/xanthomonas_oryzae_x8_1a.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/xanthomonas_oryzae_x8_1a.yaml data/taxa/bacteria/buchnera_aphidicola_str_usda_myzus_persicae.yaml data/taxa/bacteria/buchnera_aphidicola_str_w106_myzus_persicae.yaml data/taxa/bacteria/buchnera_aphidicola_str_g002_myzus_persicae.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 84 YAML lines, 10 lineage entries, 3 source attestations, 3 synonyms, 0 nomenclature entries, 1 taxonomy mapping, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009854` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, generated target YAML, and 1 GTDB mapping row; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211813`, 1 GTDB row, 1 MADIN row, 10 checked lineage entries with no mismatches, 0 NCBI merge rows, 0 GOLD aggregate rows, 1 native GOLD organism/project/analysis trio, no BacDive, LPSN, MediaDive, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009854` resolves to `Xanthomonas oryzae X8-1A`, rank `STRAIN`,
parent `NCBITaxon:347`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:347` Xanthomonas oryzae. The bounded scan found no NCBI merge row and
no retained old-id row.

## Evidence

The NCBI row supports the X8-1A strain identity, parent, genetic code, and two
NCBI exact synonyms. The seed event is supported by
`curation/seed_scope.tsv:36079`.

GTDB line 1134 supports the `s__Xanthomonas_oryzae` closeMatch, xref, and GTDB
exact synonym; MADIN line 409 supports 2 trait assertions. Native GOLD has side
evidence for `Go0011921` through project `Gp0011921` and analysis 12096.

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
Ten NCBI lineage rows are expected.
The 84-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
