# YAML Record Review: Sphingomonadaceae bacterium DAB_ATA163

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/sphingomonadaceae_bacterium_dab_ata163.yaml
- Started UTC: 2026-10-03T03:06:59Z
- Finished UTC: 2026-10-03T03:06:59Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/sphingomonadaceae_bacterium_dab_ata163.yaml` |
| Identifier | `NCBITaxon:1029945` |
| Label | `Sphingomonadaceae bacterium DAB_ATA163` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:122612` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only Sphingomonadaceae placeholder, with path
pinned by `data/taxa/PATHS.tsv:12394`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/sphingomonadaceae_bacterium_dab_ata163.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/polaromonas_sp_dab_ata123.yaml data/taxa/bacteria/polaromonas_sp_dab_ata159.yaml data/taxa/bacteria/polaromonas_sp_dab_ata189.yaml data/taxa/bacteria/pseudomonas_sp_dab_ata12.yaml data/taxa/bacteria/pseudomonas_sp_dab_mor33.yaml data/taxa/bacteria/rhodococcus_sp_dab_ata20.yaml data/taxa/bacteria/sphingomonadaceae_bacterium_dab_ata163.yaml data/taxa/bacteria/sphingomonas_sp_dab_ata120.yaml data/taxa/bacteria/sphingomonas_sp_dab_ata129.yaml data/taxa/bacteria/sphingomonas_sp_dab_ata95.yaml` | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 51 YAML lines, 9 lineage entries, 1 source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` source scan | Found `NCBITaxon:1029945` only in the expected seed and NCBI source rows under `curation/` and `data/raw/`; found no exact legacy, GTDB, GOLD, MADIN, StrainInfo, ATB, BacDive, LPSN, MediaDive, or BactoTraits row. |
| Exact first-column NCBITaxon lineage scan | Found all 9 expected lineage IDs in `data/raw/ncbitaxon_taxa.tsv`; labels and ranks agree with the generated YAML. |
| Prior report probe | Found no existing `reports/yaml_record_review/*sphingomonadaceae_bacterium_dab_ata163.md` report, with ignored files included. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1029945` resolves to label `Sphingomonadaceae bacterium
DAB_ATA163`, rank `SPECIES`, parent `NCBITaxon:122612`, genetic code `11`,
NCBI-only source set, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and ends at `NCBITaxon:122612` unclassified
Sphingomonadaceae under family `NCBITaxon:41297`; no genus row is asserted.

## Evidence

`data/raw/ncbitaxon_taxa.tsv:220161` supports the record identifier, label,
rank, parent, genetic code, empty synonym columns, single NCBITAXON source
attestation, and 2026-09-13 snapshot date.

The seed event is supported by `curation/seed_scope.tsv:320615`, whose
attested rule names `Sphingomonadaceae bacterium DAB_ATA163` with 1 source
including NCBI.

## Completeness

No consequential required generated claim is absent for this record. The exact
source scan accounted for the expected NCBI, seed, path, and generated YAML
inputs and found no omitted auxiliary source rows.

`strain_count: 0` is consistent with the absence of exact BacDive,
type-material, GOLD, StrainInfo, and strain inventory rows.

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

This was a read-only generated-record review; it did not append history,
promote `mapping_status`, or touch YAML.
No `synonyms` section is expected.
No `nomenclature` section is expected.
No `taxonomy_mappings` section is expected.
No xref, strain, genome, or causal graph section is expected.
Nine NCBI lineage rows are expected for this family-level placeholder.
The ignored exact-ID and prior-report probes included gitignored files.
