# YAML Record Review: Candidatus Phytoplasma australasiaticum subsp. ipomoeae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/candidatus_phytoplasma_australasiaticum_subsp_ipomoeae.yaml
- Started UTC: 2026-10-01T08:03:52Z
- Finished UTC: 2026-10-01T08:03:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/candidatus_phytoplasma_australasiaticum_subsp_ipomoeae.yaml` |
| Identifier | `NCBITaxon:101513` |
| Label | `Candidatus Phytoplasma australasiaticum subsp. ipomoeae` |
| Class | `TaxonRecord` |
| Rank | `SUBSPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2754999` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon, GTDB, and GOLD subspecies record, with path
pinned by `data/taxa/PATHS.tsv:8367`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/candidatus_phytoplasma_australasiaticum_subsp_ipomoeae.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict <4 exact YAML paths>` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 91 YAML lines, 11 lineage entries, 1 GTDB closeMatch, 1 GTDB xref, 4 synonyms, 3 source attestations, 0 nomenclature entries, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Exact local scans | Found `NCBITaxon:101513` in the expected seed, NCBI, GOLD aggregate, GTDB mapping, NCBI type-material, YAML, legacy page, and `data/taxa/PATHS.tsv` rows; the ignored-file-inclusive report probe found no prior report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:17579`, 11 checked lineage entries with no missing rows or mismatches, 1 GTDB mapping row with 130 genomes, 1 GOLD aggregate row with 1 organism, 2 NCBI type-material rows, 0 NCBI merge rows, no BacDive rows, no auxiliary rows, and no StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:101513` resolves to `Candidatus Phytoplasma australasiaticum subsp. ipomoeae`,
rank `SUBSPECIES`, parent `NCBITaxon:2754999`, genetic code `11`, source set
`ncbitaxon|gtdb|gold`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 11 committed NCBI rows, ending at
`NCBITaxon:2754999` Candidatus Phytoplasma australasiaticum. The bounded scan
found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the subspecies identity, species parent, bacterial
genetic code, three NCBI synonyms, NCBITAXON source attestation, and
2026-09-13 snapshot date.

The exact `data/raw/gtdb_mappings.tsv:1163` row supports the
`GTDB:s__Phytoplasma_australasiaticum` `skos:closeMatch`, 130-genome GTDB
source attestation, GTDB xref, and GTDB-derived synonym. The exact
`data/raw/gold_organisms.tsv:281` row supports the retained 1-organism GOLD
attestation.

## Completeness

Two exact NCBI type-material rows name `isolate o7C` and `personal::o7C`.
Those rows are side evidence and do not imply generated `StrainEntry` rows, so
`strain_count: 0` is expected.

No MADIN, BacDive, LPSN, MediaDive, BactoTraits, culture-collection,
normalized assembly, normalized genome, or exact-target related-record row is
filed for this exact NCBI taxon.

An ignored-file-inclusive `rg --no-ignore --hidden` check returned no existing
Markdown report for this stem before this report was written.

## Findings

No findings.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.

## Follow-up Checks

No follow-up needed.

## Additional Notes

This was a read-only generated-record review; it did not append history or touch YAML.
The GTDB synonym is backed by the exact closeMatch row.
The GOLD source attestation is aggregate-only and has assertion count 1.
No native GOLD organism, project, or analysis row is filed.
No NCBI merge row complicates identity.
Eleven NCBI lineage rows are expected.
The 91-line YAML shape omits BacDive and StrainInfo sections.
The record has no MADIN row.
The legacy page path is present and matches the generated stem.
The exact report probe included gitignored files.
