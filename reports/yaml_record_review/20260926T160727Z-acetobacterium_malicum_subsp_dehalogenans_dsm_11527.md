# YAML Record Review: Acetobacterium malicum subsp. dehalogenans DSM 11527

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_malicum_subsp_dehalogenans_dsm_11527.yaml
- Started UTC: 2026-09-26T16:07:27Z
- Finished UTC: 2026-09-26T16:07:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_malicum_subsp_dehalogenans_dsm_11527.yaml` |
| Identifier | `NCBITaxon:1068975` |
| Label | `Acetobacterium malicum subsp. dehalogenans DSM 11527` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:82116` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:21796`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_malicum_subsp_dehalogenans_dsm_11527.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_malicum.yaml data/taxa/bacteria/acetobacterium_malicum_subsp_dehalogenans.yaml data/taxa/bacteria/acetobacterium_malicum_subsp_dehalogenans_dsm_11527.yaml data/taxa/bacteria/acetobacterium_paludosum.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected strain shape: 11 lineage entries, 0 LPSN nomenclature rows, 1 `skos:closeMatch` GTDB mapping, 1 BacDive strain, 14 genome assemblies, 10 genome records, 32 related records, 2 exact synonyms, 1 xref, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier, exact label, and `GTDB:s__Acetobacterium_malicum` in the expected raw, overlay, seed, and legacy path rows across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:228711`, the GTDB mapping row at `data/raw/gtdb_mappings.tsv:2397`, the target BacDive row, processed GOLD, Madin, strain assembly/genome/related-record rows, 11 checked lineage entries with no missing rows or mismatches, and no same-taxon LPSN, BactoTraits, MediaDive, StrainInfo, NCBI merged, or NCBI type-material rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1068975` resolves in the committed NCBI inventory to label
`Acetobacterium malicum subsp. dehalogenans DSM 11527`, rank `STRAIN`, parent
`NCBITaxon:82116`, genetic code `11`, one exact synonym, and taxonomy snapshot
`2026-09-13`. The record carries those same identity fields and correctly lands
in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 11 stored
taxa, from `NCBITaxon:1` root through parent subspecies `NCBITaxon:82116`.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row, including
`Acetobacterium dehalogenans DSM 11527` as an exact synonym.

`data/raw/gtdb_species.tsv:3348` and `data/raw/gtdb_mappings.tsv:2397` support
the GTDB xref and `skos:closeMatch` mapping to the shared
`GTDB:s__Acetobacterium_malicum` species.

`data/raw/bacdive_strains.tsv:5301` supports the BacDive 5410 strain,
designation `MC`, DSM 11527 and NBRC 117038 culture-collection IDs, and one
medium assertion. The processed strain rows at `data/raw/strain_assemblies.tsv`
132169-132181, `data/raw/strain_genome_records.tsv`, and
`data/raw/strain_related_records.tsv` support the 14 assembly, 10 genome, and
32 related-record entries generated from BacDive, BV-BRC, GOLD, GTDB, and NCBI
Assembly sources.

The processed GOLD and Madin attestations are supported by
`data/raw/gold_organisms.tsv:1153` and `data/raw/madin_taxa.tsv:1312`. The seed
event is supported by `curation/seed_scope.tsv:14859`.

## Completeness

No consequential required claim is absent for this generated strain record. The
bounded scan found one native GOLD organism, one native GOLD project, one native
GOLD analysis, 13 exact raw strain assembly rows, 10 exact raw strain genome
rows, and 30 exact raw strain related-record rows for `NCBITaxon:1068975`.

No exact same-taxon LPSN, BactoTraits, MediaDive, StrainInfo, NCBI merged-ID,
or NCBI type-material rows were present for the strain identifier, so the empty
sections for those evidence types are consistent with the inspected inputs.

The exact ignored-aware history/report scan found no prior history or ignored
review report mentioning this target before this report was written; ignored
files under `reports/` were included.

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
