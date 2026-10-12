# YAML Record Review: Acidianus tengchongensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidianus_tengchongensis.yaml
- Started UTC: 2026-09-27T08:46:57Z
- Finished UTC: 2026-09-27T08:46:57Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidianus_tengchongensis.yaml` |
| Identifier | `NCBITaxon:146920` |
| Label | `Acidianus tengchongensis` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:12914` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBI and GOLD backed species record, with path pinned by
`data/taxa/PATHS.tsv:177573` and fields owned by generated inputs.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidianus_tengchongensis.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidianus_sp_syk_eso_2.yaml data/taxa/archaea/acidianus_sulfidivorans.yaml data/taxa/archaea/acidianus_sulfidivorans_jp7.yaml data/taxa/archaea/acidianus_tengchongensis.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 75 YAML lines, 9 lineage entries, 6 NCBI synonyms, 2 source attestations, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:146920` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:29877`, 9 checked lineage entries with no missing rows or mismatches, 1 GOLD aggregate row with 5 organism assertions, 1 NCBI merge row from old `NCBITaxon:119975`, 2 NCBI type-material rows, 1 direct StrainInfo hit with 1 deposit, and 0 BacDive, native GOLD, LPSN, GTDB, MediaDive, MADIN, BactoTraits, normalized strain, normalized genome, normalized related-record, or StrainInfo exclusion rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:146920` resolves to label `Acidianus tengchongensis`, rank
`SPECIES`, parent `NCBITaxon:12914`, genetic code `11`, source set
`ncbitaxon|gold`, and taxonomy snapshot `2026-09-13`. The generated record
carries those same NCBI-owned fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through genus `NCBITaxon:12914` Acidianus. The
bounded scan found old `NCBITaxon:119975` merged here.

## Evidence

The generated synonyms mirror NCBI: exact synonyms
`Acidianus tengchongenses` and `Sulfosphaerellus thermoacidophilum`, plus the
four related strings with quoted He et al. citations and `Acidianus sp. S5`.

The GOLD aggregate at `data/raw/gold_taxa.tsv:11298` contributes 5 organism
assertions and is represented by the generated GOLD source attestation.

StrainInfo has one direct side row for CGMCC 1.3347 and NCBI lists S5 type
material strings, but no retained BacDive, culture-collection, StrainInfo
related, assembly, genome, or related-record row is available to seed a strain.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GOLD, NCBI merge, type-material,
StrainInfo side evidence, seed, path, and YAML inputs, and found no omitted
LPSN, GTDB, BacDive, MediaDive, MADIN, BactoTraits, normalized strain,
normalized genome, normalized related-record, or StrainInfo exclusion row.

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

This was a read-only generated-record review; it did not append history, promote `mapping_status`, or touch YAML.
The retained GOLD aggregate has no exact native GOLD organism in the local
snapshot, which is why there are no native GOLD project or analysis rows.
The NCBI old ID is merge-only and is not retained as an emitted synonym.
`strain_count: 0` is expected because no final strain table row names this
taxon.
The retained StrainInfo row remains side evidence only.
No seeder, scope, or kg-microbe edit is indicated by this read-only review.
The report therefore has no follow-up curation item.
