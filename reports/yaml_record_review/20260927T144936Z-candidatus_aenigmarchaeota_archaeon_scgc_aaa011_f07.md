# YAML Record Review: Candidatus Aenigmarchaeota archaeon SCGC AAA011-F07

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/candidatus_aenigmarchaeota_archaeon_scgc_aaa011_f07.yaml
- Started UTC: 2026-09-27T14:49:36Z
- Finished UTC: 2026-09-27T14:49:36Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/candidatus_aenigmarchaeota_archaeon_scgc_aaa011_f07.yaml` |
| Identifier | `NCBITaxon:1046938` |
| Label | `Candidatus Aenigmarchaeota archaeon SCGC AAA011-F07` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:1046937` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated GOLD- and NCBI-backed Candidatus Aenigmarchaeota
species record, with path pinned by `data/taxa/PATHS.tsv:17369`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/candidatus_aenigmarchaeota_archaeon_scgc_aaa011_f07.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/candidatus_aenigmarchaeota_archaeon_scgc_aaa011_f07.yaml data/taxa/archaea/candidate_division_dusel4_archaeon_scgc_aaa011_l21.yaml data/taxa/archaea/nanoarchaeota_archaeon_scgc_aaa011_l22.yaml data/taxa/archaea/thaumarchaeota_archaeon_scgc_aaa010_g21.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 54 YAML lines, 6 lineage entries, 2 exact NCBI synonyms, 2 source attestations, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1046938` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:224706`, 6 checked lineage entries with no missing rows or mismatches, 1 retained GOLD aggregate row, 1 native GOLD organism row, 1 native GOLD project, 1 native GOLD analysis, 0 NCBI merge rows, 0 NCBI type-material rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1046938` resolves to `Candidatus Aenigmarchaeota archaeon SCGC
AAA011-F07`, rank `SPECIES`, parent `NCBITaxon:1046937`, genetic code `11`,
source set `ncbitaxon|gold`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 6 committed NCBI rows, ending at
`NCBITaxon:1046937` unclassified Candidatus Aenigmatarchaeota. The bounded
scan found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the species-rank single-cell identity, direct
unclassified-Candidatus-Aenigmatarchaeota parent, genetic code, exact synonyms
`Aenigmarchaeota archaeon SCGC AAA011-F07` and `candidate division DUSEL2
archaeon SCGC AAA011-F07`, and 2026-09-13 snapshot date.

The retained GOLD aggregate and native GOLD organism/project/analysis rows
support the GOLD source attestation as side evidence. No normalized GOLD
strain, assembly, genome, or related-record row is filed under this taxon.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, retained GOLD, seed, path, and
generated YAML inputs, and found no omitted GTDB, LPSN, BacDive, strain,
type-material, StrainInfo, or culture-collection row.

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
Two exact NCBI synonyms were materialized.
No `taxonomy_mappings` section is expected.
No xref section is expected.
Native GOLD supplied one organism/project/analysis chain.
One retained GOLD aggregate row is filed on this target.
The GOLD organism stayed side-only.
No normalized genome assembly rows were present.
No normalized genome records were present.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Six NCBI lineage rows are expected.
The GOLD source attestation is expected without a strain block.
The 54-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
