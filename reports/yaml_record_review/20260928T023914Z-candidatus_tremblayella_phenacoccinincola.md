# YAML Record Review: Candidatus Tremblayella phenacoccinincola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/candidatus_tremblayella_phenacoccinincola.yaml
- Started UTC: 2026-09-28T02:39:14Z
- Finished UTC: 2026-09-28T02:39:14Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/candidatus_tremblayella_phenacoccinincola.yaml` |
| Identifier | `NCBITaxon:1010676` |
| Label | `Candidatus Tremblayella phenacoccinincola` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:189384` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated multi-source Candidatus Tremblayella species record,
with path pinned by `data/taxa/PATHS.tsv:3811`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/candidatus_tremblayella_phenacoccinincola.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/candidatus_tremblayella_phenacoccinincola.yaml data/taxa/bacteria/bacillus_sp_nrs_1223.yaml data/taxa/bacteria/enterococcus_sp_alborz.yaml data/taxa/bacteria/pediococcus_sp_shahsavar.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 87 YAML lines, 8 lineage entries, 3 NCBI synonyms, 2 GTDB taxonomy mappings, 3 source attestations, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, 0 related rows, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1010676` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, generated target YAML rows, and one descendant NCBI strain row; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:212376`, 8 checked lineage rows, 2 GTDB broadMatch rows, 1 GOLD aggregate row, 2 native GOLD organisms, 2 native GOLD projects, 2 native GOLD analyses, 0 NCBI merge rows, no LPSN, BacDive, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1010676` resolves to `Candidatus Tremblayella phenacoccinincola`,
rank `SPECIES`, parent `NCBITaxon:189384`, genetic code `11`, source set
`ncbitaxon|gtdb|gold`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 8 committed NCBI rows, ending at
`NCBITaxon:189384` genus `Candidatus Tremblayella`; no NCBI merge row was retained.

## Evidence

The NCBI row supports the current species name, parent, genetic code, 2 exact
synonyms, 1 related synonym, three upstream source flags, and the snapshot date.

GTDB contributes broad mappings to `GTDB:s__Tremblaya_phenacola_C` and
`GTDB:s__Tremblaya_phenacola_D`, each with one genome.

GOLD contributes the target aggregate and native PPER and PSOL organism,
project, and analysis rows; no normalized genome or related row was retained.

## Completeness

No LPSN, BacDive, MediaDive, MADIN, BactoTraits, NCBI type-material,
StrainInfo, native `data/raw/gtdb_species.tsv`, definition, genome assembly,
genome record, related-record, or causal-graph row was filed.

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
No LPSN nomenclature or xref section is expected.
The two GTDB mappings are intentionally `skos:broadMatch`.
The GTDB source attestation points at one representative pooled species.
The GOLD source attestation preserves the aggregate organism count of 2.
Native GOLD rows cover PPER and PSOL organism/project/analysis triplets.
No BacDive row is filed under the exact NCBI species.
No StrainInfo row is filed under the exact NCBI species.
No normalized genome row is filed on this target.
No native GTDB species row is filed.
One NCBI child strain names this taxon as its parent.
The three synonyms all come from NCBITaxon.
The 87-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
