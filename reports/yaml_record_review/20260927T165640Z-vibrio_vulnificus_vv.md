# YAML Record Review: Vibrio vulnificus VV

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/vibrio_vulnificus_vv.yaml
- Started UTC: 2026-09-27T16:56:40Z
- Finished UTC: 2026-09-27T16:56:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/vibrio_vulnificus_vv.yaml` |
| Identifier | `NCBITaxon:1009845` |
| Label | `Vibrio vulnificus VV` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:672` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated Vibrio vulnificus strain record with NCBI and MADIN
support, with path pinned by `data/taxa/PATHS.tsv:3206`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/vibrio_vulnificus_vv.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/vibrio_vulnificus_vv.yaml data/taxa/bacteria/burkholderia_cepacia_gg4.yaml data/taxa/bacteria/comamonas_testosteroni_atcc_11996.yaml data/taxa/bacteria/xanthomonas_oryzae_x11_5a.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 66 YAML lines, 10 lineage entries, 2 source attestations, 2 synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009845` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211809`, 1 MADIN row at `data/raw/madin_taxa.tsv:405`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 GOLD aggregate rows, 1 native GOLD organism row, 1 native GOLD project row, no BacDive rows, no LPSN, GTDB, MediaDive, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009845` resolves to `Vibrio vulnificus VV`, rank `STRAIN`,
parent `NCBITaxon:672`, genetic code `11`, source set `ncbitaxon|madin_etal`,
and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:672` Vibrio vulnificus. The bounded scan found no NCBI merge row and
no retained old-id row.

## Evidence

The NCBI row supports the VV strain identity, direct Vibrio vulnificus parent,
two NCBI exact synonyms, genetic code, and source set. The seed event is
supported by `curation/seed_scope.tsv:57185`.

MADIN line 405 supports the one trait assertion. Native GOLD has side evidence
for `Go0011876` through project `Gp0011876`, but no GOLD aggregate, analysis,
assembly, genome, or strain row was retained for the generated YAML.

## Completeness

Native GOLD side rows exist for this exact NCBI taxon, but no GOLD aggregate or
normalized genome/strain row was retained.
No BacDive, LPSN, GTDB, MediaDive, BactoTraits, type-material, or StrainInfo
row was filed under this exact taxon.

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
Two NCBI exact synonyms are expected.
The MADIN trait assertion row is retained on this target.
No `taxonomy_mappings` section is expected.
No xref section is expected.
No retained GOLD aggregate row is filed on this target.
No normalized assembly row is filed on this target.
No normalized genome row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The 66-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
