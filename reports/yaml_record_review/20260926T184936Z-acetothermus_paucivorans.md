# YAML Record Review: Acetothermus paucivorans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetothermus_paucivorans.yaml
- Started UTC: 2026-09-26T18:49:36Z
- Finished UTC: 2026-09-26T18:49:36Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetothermus_paucivorans.yaml` |
| Identifier | `NCBITaxon:1653171` |
| Label | `Acetothermus paucivorans` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:558421` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:237734`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetothermus_paucivorans.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetothermia_bacterium_uba7521.yaml data/taxa/bacteria/acetothermia_clone_opb14.yaml data/taxa/bacteria/acetothermia_clone_ops143a.yaml data/taxa/bacteria/acetothermus_paucivorans.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected LPSN/BacDive shape: 111 YAML lines, 11 lineage entries, 1 LPSN nomenclature entry, 1 LPSN xref, 1 related NCBITaxon synonym, 1 BacDive strain marked type, 1 culture collection ID, 1 related GOLD organism, 1 `NCBITAXON`/`NAME` attestation, 1 `LPSN`/`NAME` attestation, 1 `BACDIVE`/`STRAIN` attestation, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier or its LPSN/BacDive/strain/GOLD related IDs in the expected `curation/legacy_page_paths.tsv`, `curation/seed_scope.tsv`, `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/ncbi_type_material.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/raw/strain_related_records.tsv`, `data/taxa/PATHS.tsv`, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:432181`, 1 LPSN row, 1 BacDive JSON record, 1 normalized BacDive strain row, 1 normalized culture-collection row, 4 NCBI type-material alias rows, 11 checked lineage entries with no missing rows or mismatches, and no GTDB, StrainInfo, normalized GOLD aggregate, Madin, MediaDive, BactoTraits, strain assembly, or strain genome rows for this target. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1653171` resolves in the committed NCBI inventory to label
`Acetothermus paucivorans`, rank `SPECIES`, parent `NCBITaxon:558421`,
related synonym `Acetothermus paucivorans Dietrich et al. 1988`, genetic code
`11`, and taxonomy snapshot `2026-09-13`. The record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 11
stored taxa, from `NCBITaxon:1` root through `NCBITaxon:558421`
Acetothermus. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The LPSN nomenclature claim is supported by `data/raw/lpsn_names.tsv:14837`,
which maps `lpsn:772545` to `NCBITaxon:1653171`, flags
`Acetothermus paucivorans` as validly published, legitimate, and the correct
name, carries authority `Dietrich et al. 1988`, lists
`kgmicrobe.strain:DSM-20768` as the type strain, and carries the two
publications present in YAML.

The BacDive strain claim is supported by `data/raw/bacdive_strains.tsv:90266`,
which maps `kgmicrobe.strain:bacdive_168033` to `NCBITaxon:1653171`, strain
designation `TN`, `lpsn:772545`, and culture collection
`kgmicrobe.strain:DSM-20768`.

The related GOLD organism is supported by
`data/raw/strain_related_records.tsv:257316`, which links
`kgmicrobe.strain:bacdive_168033` to `gold:Go0027562` with matching culture
collection identifier `DSM 20768`.

The seed event is supported by `curation/seed_scope.tsv:30738`, which records
`NCBITaxon:1653171` as added on `2026-09-12` with reason `attested rule:
Acetothermus paucivorans, 3 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated LPSN/BacDive
record. The bounded scan found the expected LPSN, BacDive, culture-collection,
and type-material rows and no GTDB, StrainInfo, normalized GOLD aggregate,
Madin, MediaDive, BactoTraits, strain assembly, strain genome, or NCBI merge
row for this target.

The legacy page path for this identifier is already carried in
`curation/legacy_page_paths.tsv:26198`.

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
