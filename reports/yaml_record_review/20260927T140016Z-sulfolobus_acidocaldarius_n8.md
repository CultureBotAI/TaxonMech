# YAML Record Review: Sulfolobus acidocaldarius N8

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/sulfolobus_acidocaldarius_n8.yaml
- Started UTC: 2026-09-27T14:00:16Z
- Finished UTC: 2026-09-27T14:00:16Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/sulfolobus_acidocaldarius_n8.yaml` |
| Identifier | `NCBITaxon:1028566` |
| Label | `Sulfolobus acidocaldarius N8` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2285` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Strain count | `1` |

The file is an NCBITaxon/GTDB/BacDive/MADIN strain record, with path pinned
by `data/taxa/PATHS.tsv:11332`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/sulfolobus_acidocaldarius_n8.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/nitrosopumilus_sp_sj.yaml data/taxa/archaea/sulfolobus_acidocaldarius_n8.yaml data/taxa/archaea/sulfolobus_acidocaldarius_ron12_i.yaml data/taxa/archaea/marine_group_ii_euryarchaeote_scgc_aaa288_c18.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 509 YAML lines, 10 lineage entries, 4 source attestations, 1 GTDB closeMatch mapping, 5 exact synonyms, 1 xref, 1 BacDive strain, 1 genome assembly, 2 genome records, 27 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1028566` in the expected seed, NCBI, GTDB mapping, `PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:219169`, 10 checked lineage entries with no mismatches, the 57-genome GTDB closeMatch row at `data/raw/gtdb_mappings.tsv:1229`, 1 MADIN row, 1 BacDive row, 3 culture-collection rows, 1 BacDive assembly row, 2 BacDive genome rows, 1 native GOLD organism, 1 native GOLD project, 1 native GOLD analysis, and no NCBI merge, type-material, LPSN, MediaDive, BactoTraits, or StrainInfo same-taxon rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1028566` resolves to `Sulfolobus acidocaldarius N8`, rank `STRAIN`,
parent `NCBITaxon:2285`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:2285` Sulfolobus acidocaldarius. The bounded scan found no NCBI
merge row and no retained old-id row.

## Evidence

The NCBI row supports the strain identity, parent species, genetic code, four
NCBI exact synonyms, source set, and snapshot date. The seed event is
supported by `curation/seed_scope.tsv:22135`.

The GTDB row supports the direct species-level closeMatch xref and GTDB exact
synonym. BacDive `165989` at `data/raw/bacdive_strains.tsv:88225` supports the
single strain and its IFO-15159, JCM-9063, and NBRC-15159 culture IDs.

The generated related-record block is culture-ID side evidence for that
BacDive strain: 18 GOLD organism rows in `data/raw/strain_related_records.tsv`
and 9 StrainInfo rows in `data/straininfo/related_records.tsv.gz`.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, BacDive, MADIN, seed, path,
culture-collection, assembly, genome, native GOLD side, and related rows.

The native same-strain GOLD rows do not create a retained aggregate GOLD
source attestation; the retained GOLD rows are species-side related records.

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
`strain_count: 1` matches the single exact BacDive row for this target.
`GTDB:s__Sulfolobus_acidocaldarius` has `skos:closeMatch` with 57 genomes.
No LPSN nomenclature is expected on this strain record.
No retained GOLD aggregate row is filed on this target.
No NCBI type-material row is filed on this strain target.
No same-taxon direct StrainInfo row is filed for this target.
No retained old identifier is generated for this target.
The 509-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
