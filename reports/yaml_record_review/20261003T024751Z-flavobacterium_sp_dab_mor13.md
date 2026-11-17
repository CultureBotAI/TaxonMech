# YAML Record Review: Flavobacterium sp. DAB_MOR13

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/flavobacterium_sp_dab_mor13.yaml
- Started UTC: 2026-10-03T02:47:51Z
- Finished UTC: 2026-10-03T02:47:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/flavobacterium_sp_dab_mor13.yaml` |
| Identifier | `NCBITaxon:1029906` |
| Label | `Flavobacterium sp. DAB_MOR13` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:196869` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only Flavobacterium placeholder, with path
pinned by `data/taxa/PATHS.tsv:12355`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/flavobacterium_sp_dab_mor13.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/brevundimonas_sp_dab_ata190.yaml data/taxa/bacteria/brevundimonas_sp_dab_mm90.yaml data/taxa/bacteria/brevundimonas_sp_dab_st86.yaml data/taxa/bacteria/chryseobacterium_sp_dab_38ecl.yaml data/taxa/bacteria/chryseobacterium_sp_dab_4ecl.yaml data/taxa/bacteria/flavobacterium_sp_dab_ata152.yaml data/taxa/bacteria/flavobacterium_sp_dab_ata170.yaml data/taxa/bacteria/flavobacterium_sp_dab_mor13.yaml data/taxa/bacteria/flavobacterium_sp_dab_mor16.yaml data/taxa/bacteria/flavobacterium_sp_dab_st4.yaml` | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 60 YAML lines, 12 lineage entries, 1 source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` source scan | Found `NCBITaxon:1029906` only in the expected seed and NCBI source rows under `curation/` and `data/raw/`; found no exact legacy, GTDB, GOLD, MADIN, StrainInfo, ATB, BacDive, LPSN, MediaDive, or BactoTraits row. |
| Exact first-column NCBITaxon lineage scan | Found all 12 expected lineage IDs in `data/raw/ncbitaxon_taxa.tsv`; labels and ranks agree with the generated YAML. |
| Prior report probe | Found no existing `reports/yaml_record_review/*flavobacterium_sp_dab_mor13.md` report, with ignored files included. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1029906` resolves to label `Flavobacterium sp. DAB_MOR13`, rank
`SPECIES`, parent `NCBITaxon:196869`, genetic code `11`, NCBI-only source set,
and taxonomy snapshot `2026-09-13`.

The lineage is root-first and ends at `NCBITaxon:196869` unclassified
Flavobacterium under genus `NCBITaxon:237`.

## Evidence

`data/raw/ncbitaxon_taxa.tsv:220122` supports the record identifier, label,
rank, parent, genetic code, empty synonym columns, single NCBITAXON source
attestation, and 2026-09-13 snapshot date.

The seed event is supported by `curation/seed_scope.tsv:320576`, whose
attested rule names `Flavobacterium sp. DAB_MOR13` with 1 source including
NCBI.

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
Twelve NCBI lineage rows are expected.
The ignored exact-ID and prior-report probes included gitignored files.
