# YAML Record Review: Acholeplasma sp. JGI_KR46_SmLR_5_H10

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_sp_jgi_kr46_smlr_5_h10.yaml
- Started UTC: 2026-09-26T19:27:32Z
- Finished UTC: 2026-09-26T19:27:32Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_sp_jgi_kr46_smlr_5_h10.yaml` |
| Identifier | `NCBITaxon:2738556` |
| Label | `Acholeplasma sp. JGI_KR46_SmLR_5_H10` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2644011` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:369157`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_sp_jgi_kr46_smlr_5_h10.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_sp_j294.yaml data/taxa/bacteria/acholeplasma_sp_jgi_kr46_smlr_5_h10.yaml data/taxa/bacteria/acholeplasma_sp_jgi_sa12_b04_030.yaml data/taxa/bacteria/acholeplasma_sp_jgi_sa12_b09_077.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected compact generated shape: 59 YAML lines, 10 lineage entries, 2 source attestations, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:549035`, 10 checked lineage entries with no missing rows or mismatches, 1 GOLD aggregate row, 1 native GOLD organism, 1 native GOLD project, 0 NCBI merge rows, and 0 LPSN, GTDB, BacDive, StrainInfo, Madin, MediaDive, BactoTraits, type-material, AllTheBacteria, normalized assembly, genome, or related-record rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:2738556` resolves in the committed NCBI inventory to label
`Acholeplasma sp. JGI_KR46_SmLR_5_H10`, rank `SPECIES`, parent
`NCBITaxon:2644011`, genetic code `11`, and taxonomy snapshot `2026-09-13`.
The record carries those same identity fields and correctly lands in the
`bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2644011` unclassified
Acholeplasma. There are no retained old identifiers for this target in the NCBI
merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:2738556`, source label `Acholeplasma sp. JGI_KR46_SmLR_5_H10`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The `GOLD` source attestation is supported by the aggregate row at
`data/raw/gold_organisms.tsv:25572`, native GOLD organism `Go0456363`, and
native GOLD project `Gp0325655`. No GOLD analysis or strain-normalized row is
present for this target, matching the YAML's compact shape.

The seed event is supported by `curation/seed_scope.tsv:63012`, which records
`NCBITaxon:2738556` as added on `2026-09-12` with reason `attested rule:
Acholeplasma sp. JGI_KR46_SmLR_5_H10, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated compact record.
The exact and bounded scans account for the expected NCBI, GOLD, and generated
YAML inputs, and found no NCBI merge, LPSN, GTDB, BacDive, StrainInfo, Madin,
MediaDive, BactoTraits, type-material, AllTheBacteria, normalized assembly,
normalized genome, or normalized related-record row that would require an
enriched YAML section.

An ignored-file-inclusive `find` under `reports/yaml_record_review` returned no
existing Markdown report for this stem before this report was written.

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

This was a read-only generated-record review. It did not append a curation
event, promote `mapping_status`, write a history record, or touch the seeded
YAML.
