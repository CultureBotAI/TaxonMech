# YAML Record Review: Buchnera aphidicola str. G002 (Myzus persicae)

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/buchnera_aphidicola_str_g002_myzus_persicae.yaml
- Started UTC: 2026-09-27T17:01:32Z
- Finished UTC: 2026-09-27T17:01:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/buchnera_aphidicola_str_g002_myzus_persicae.yaml` |
| Identifier | `NCBITaxon:1009858` |
| Label | `Buchnera aphidicola str. G002 (Myzus persicae)` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:98795` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated Buchnera aphidicola Myzus persicae strain record with
NCBI, GOLD, GTDB, and MADIN support, pinned by `data/taxa/PATHS.tsv:3213`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/buchnera_aphidicola_str_g002_myzus_persicae.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/xanthomonas_oryzae_x8_1a.yaml data/taxa/bacteria/buchnera_aphidicola_str_usda_myzus_persicae.yaml data/taxa/bacteria/buchnera_aphidicola_str_w106_myzus_persicae.yaml data/taxa/bacteria/buchnera_aphidicola_str_g002_myzus_persicae.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 89 YAML lines, 11 lineage entries, 4 source attestations, 2 synonyms, 0 nomenclature entries, 1 taxonomy mapping, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009858` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, generated target YAML, and 1 GTDB mapping row; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211816`, 1 GTDB row, 1 GOLD aggregate row, 1 MADIN row, 11 checked lineage entries with no mismatches, 0 NCBI merge rows, 1 native GOLD organism/project/analysis trio, no BacDive, LPSN, MediaDive, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009858` resolves to `Buchnera aphidicola str. G002 (Myzus persicae)`,
rank `STRAIN`, parent `NCBITaxon:98795`, genetic code `11`, source set
`ncbitaxon|gtdb|gold|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 11 committed NCBI rows, ending at
`NCBITaxon:98795` Buchnera aphidicola (Myzus persicae). The bounded scan found
no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the G002 strain identity, forma specialis parent, genetic
code, and NCBI exact synonym. The seed event is supported by
`curation/seed_scope.tsv:26043`.

GTDB line 1137 supports the `s__Buchnera_aphidicola_C` closeMatch and xref;
GOLD aggregate line 213 and MADIN line 412 support retained source attestations.
Native GOLD has `Go0011217`, project `Gp0011217`, and analysis line 14154.

## Completeness

The retained GOLD aggregate, GTDB, MADIN, NCBI synonym, and native GOLD rows are
consistent with the generated YAML. No BacDive, LPSN, MediaDive, BactoTraits,
normalized assembly, normalized genome, normalized strain, or StrainInfo row
was filed under this exact taxon.

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
The GTDB closeMatch and xref are expected.
Two exact synonyms are expected.
The GOLD aggregate row is retained on this target.
The MADIN trait assertion row is retained on this target.
No normalized assembly row is filed on this target.
No normalized genome row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
No exact StrainInfo row is filed on this target.
Eleven NCBI lineage rows are expected.
The 89-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
