# YAML Record Review: Salmonella enterica subsp. enterica serovar Enteritidis str. 50-5646

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_enteritidis_str_50_5646.yaml
- Started UTC: 2026-10-03T03:17:42Z
- Finished UTC: 2026-10-03T03:17:42Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_enteritidis_str_50_5646.yaml` |
| Identifier | `NCBITaxon:1029986` |
| Label | `Salmonella enterica subsp. enterica serovar Enteritidis str. 50-5646` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:149539` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated Salmonella strain record, with path pinned by
`data/taxa/PATHS.tsv:12416`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_enteritidis_str_50_5646.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_typhimurium_str_sara13.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_pullorum_str_atcc_9120.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_kentucky_str_5349.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_tennessee_str_2691.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_tallahassee_str_0012.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_abony_str_0014.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_enteritidis_str_sarb17.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_enteritidis_str_6_0562_1.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_enteritidis_str_50_5646.yaml data/taxa/bacteria/bacterium_oc.yaml` | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 92 YAML lines, 12 lineage entries, 4 source attestations, 1 taxonomy mapping, 2 synonyms, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` source scan | Found `NCBITaxon:1029986` in the expected seed, NCBI, GOLD, MADIN, exact GTDB mapping, and legacy path rows; found no exact StrainInfo, ATB, BacDive, MediaDive, BactoTraits, or target-specific LPSN row. |
| Exact first-column NCBITaxon lineage scan | Found all 12 expected lineage IDs in `data/raw/ncbitaxon_taxa.tsv`; labels and ranks agree with the generated YAML. |
| Prior report probe | Found no existing `reports/yaml_record_review/*salmonella_enterica_subsp_enterica_serovar_enteritidis_str_50_5646.md` report, with ignored files included. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1029986` resolves to label `Salmonella enterica subsp. enterica
serovar Enteritidis str. 50-5646`, rank `STRAIN`, parent
`NCBITaxon:149539`, genetic code `11`, NCBI/GTDB/GOLD/MADIN source set, and
taxonomy snapshot `2026-09-13`.

The lineage is root-first and ends at `NCBITaxon:149539` Salmonella enterica
subsp. enterica serovar Enteritidis under subspecies `NCBITaxon:59201`.

## Evidence

`data/raw/ncbitaxon_taxa.tsv:220183` supports the record identifier, label,
rank, parent, genetic code, NCBI synonym, four retained source families, and
2026-09-13 snapshot date.

The exact GTDB closeMatch is at `data/raw/gtdb_mappings.tsv:1274`, the GOLD
organism row is `data/raw/gold_organisms.tsv:378`, the MADIN row is
`data/raw/madin_taxa.tsv:562`, the seed event is at
`curation/seed_scope.tsv:26068`, and the legacy generated page path is at
`curation/legacy_page_paths.tsv:710`.

## Completeness

No consequential required generated claim is absent for this record. The exact
source scan accounted for the expected NCBI, GTDB, GOLD, MADIN, seed, legacy
path, and generated YAML inputs and found no omitted exact strain inventory row.

The shared `GTDB:s__Salmonella_enterica` species key is expected; this record
uses its exact `NCBITaxon:1029986` closeMatch row.

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
The MADIN trait assertion is expected.
The GTDB exact synonym, taxonomy mapping, and xref are expected.
No `nomenclature`, strain, genome, or causal graph section is expected.
Twelve NCBI lineage rows are expected.
The ignored exact-ID and prior-report probes included gitignored files.
