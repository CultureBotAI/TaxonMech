# YAML Record Review: Acholeplasma brassicae 0502

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_brassicae_0502.yaml
- Started UTC: 2026-09-26T18:59:00Z
- Finished UTC: 2026-09-26T18:59:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_brassicae_0502.yaml` |
| Identifier | `NCBITaxon:1318465` |
| Label | `Acholeplasma brassicae 0502` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:61635` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:112192`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_brassicae_0502.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_brassicae.yaml data/taxa/bacteria/acholeplasma_brassicae_0502.yaml data/taxa/bacteria/acholeplasma_equifetale.yaml data/taxa/bacteria/acholeplasma_equifetale_atcc_29724.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected enriched generated shape: 280 YAML lines, 10 lineage entries, 4 source attestations, 0 nomenclature entries, 0 taxonomy mappings, 2 synonyms, 0 xrefs, 1 BacDive strain, 1 GOLD genome assembly, 1 GOLD genome record, 10 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, Madin, BacDive, GOLD, strain-normalization, and generated YAML rows, and found the `NCBITaxon:61635` species evidence that supplies the StrainInfo related records; found no unexpected duplicate generated record. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:313816`, 10 checked lineage entries with no missing rows or mismatches, 1 BacDive strain row, 1 culture-collection row, 1 GOLD assembly row, 1 GOLD genome row, 4 GOLD related rows, 1 GOLD organism/project/analysis set, 1 Madin row, 0 NCBI merge rows, 0 type-material rows for the strain taxon, and 0 LPSN, GTDB, StrainInfo, BactoTraits, or MediaDive direct target rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1318465` resolves in the committed NCBI inventory to label
`Acholeplasma brassicae 0502`, rank `STRAIN`, parent `NCBITaxon:61635`,
genetic code `11`, and taxonomy snapshot `2026-09-13`. The record carries
those same identity fields and correctly lands in the `bacteria` path bucket
through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:61635` Acholeplasma
brassicae. There are no retained old identifiers for this target in the NCBI
merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:1318465`, source label `Acholeplasma brassicae 0502`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

BacDive `167887`, GOLD organism `Go0003951`, GOLD project `Gp0003951`, GOLD
analysis `Ga0048255`, and the normalized `ATCC-49388` culture collection row
support the single `0502` strain block, its `GCA_000967915.1` assembly, its IMG
genome record, and its 4 GOLD related records. The 6 StrainInfo related records
are supported by species-scoped StrainInfo rows for `ATCC 49388`, which
matches the normalized strain identifier in this child record.

The seed event is supported by `curation/seed_scope.tsv:22499`, which records
`NCBITaxon:1318465` as added on `2026-09-12` with reason `attested rule:
Acholeplasma brassicae 0502, 4 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated enriched record.
The exact and bounded scans account for the expected NCBI, BacDive, GOLD,
Madin, strain-normalization, and inherited species StrainInfo inputs, and found
no NCBI merge, LPSN nomenclature, GTDB mapping, type-material, BactoTraits,
MediaDive, or direct StrainInfo target row that would require another YAML
section.

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
