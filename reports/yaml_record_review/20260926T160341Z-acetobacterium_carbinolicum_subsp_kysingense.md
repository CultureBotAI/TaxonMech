# YAML Record Review: Acetobacterium carbinolicum subsp. kysingense

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_carbinolicum_subsp_kysingense.yaml
- Started UTC: 2026-09-26T16:03:41Z
- Finished UTC: 2026-09-26T16:03:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_carbinolicum_subsp_kysingense.yaml` |
| Identifier | `NCBITaxon:346376` |
| Label | `Acetobacterium carbinolicum subsp. kysingense` |
| Class | `TaxonRecord` |
| Rank | `SUBSPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:52690` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:465741`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_carbinolicum_subsp_kysingense.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_bakii.yaml data/taxa/bacteria/acetobacterium_carbinolicum.yaml data/taxa/bacteria/acetobacterium_carbinolicum_subsp_kysingense.yaml data/taxa/bacteria/acetobacterium_fimetarium.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected subspecies shape: 10 lineage entries, 0 LPSN nomenclature rows, 0 GTDB taxonomy mappings, 1 BacDive strain, 2 culture collection identifiers, 4 genome assemblies, 2 genome records, 12 related records, 2 NCBITaxon synonyms, 0 xrefs, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier, exact label, and the `Acetobacterium halotolerans` synonym in the expected raw, overlay, seed, and legacy path rows across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:71505`, the target BacDive row, BactoTraits and MediaDive auxiliary rows, 10 checked lineage entries with no missing rows or mismatches, 1 side NCBI merged-ID row, and no same-taxon LPSN, GTDB, processed GOLD, StrainInfo, strain assembly/genome/related-record, Madin, or native GOLD rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:346376` resolves in the committed NCBI inventory to label
`Acetobacterium carbinolicum subsp. kysingense`, rank `SUBSPECIES`, parent
`NCBITaxon:52690`, genetic code `11`, one exact synonym, one related synonym,
and taxonomy snapshot `2026-09-13`. The record carries those same identity
fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through parent species
`NCBITaxon:52690` / `Acetobacterium carbinolicum`.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row, including
the `Acetobacterium halotolerans` exact synonym and `"Acetobacterium
carbinolicum subsp. kysingense" Paarup et al. 2006` related synonym.

`data/raw/bacdive_strains.tsv:23657` supports the BacDive 24007 strain,
designation `SyrA5`, and the ATCC BAA-990 and DSM 16427 culture-collection
identifiers. `data/raw/bactotraits_taxa.tsv:5838` and
`data/raw/mediadive_taxa.tsv:9166` support the auxiliary BactoTraits and
MediaDive source attestations.

The genome assembly, genome record, and related-record blocks are not
same-taxon rows keyed to `NCBITaxon:346376`; they are the GTDB, BV-BRC, and
NCBI Assembly rows for `kgmicrobe.strain:bacdive_24007` that carry parent
taxon `NCBITaxon:52690` and match DSM 16427. Keeping that parent species
`taxon_id` in each row preserves the upstream assignment.

The seed event is supported by `curation/seed_scope.tsv:21946`, which records
`NCBITaxon:346376` as added on `2026-09-12` with reason
`attested rule: Acetobacterium carbinolicum subsp. kysingense, 4 sources incl.
NCBI`.

## Completeness

No consequential required claim is absent for this generated subspecies record.
The bounded scan found no same-taxon LPSN, GTDB, processed GOLD, native GOLD,
Madin, StrainInfo, or strain overlay rows keyed to `NCBITaxon:346376`, so the
empty nomenclature, taxonomy mapping, direct same-taxon StrainInfo, and
same-taxon GOLD surfaces are consistent with the inspected sources.

`data/raw/ncbi_merged_ids.tsv:58548` maps old `NCBITaxon:295304` to
`NCBITaxon:346376`, but an exact ignored-aware scan found no retained retired
`NCBITaxon:295304` row in `data/raw/ncbitaxon_taxa.tsv`. Generated `replaces`
values come from retained retired rows, so the empty `replaces` surface is
consistent.

The exact ignored-aware source scan found no prior history or ignored review
report mentioning this target before this report was written; ignored files
under `reports/` were included.

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
