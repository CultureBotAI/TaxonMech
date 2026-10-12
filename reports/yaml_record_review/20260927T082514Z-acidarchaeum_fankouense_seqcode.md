# YAML Record Review: Acidarchaeum fankouense (SeqCode)

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidarchaeum_fankouense_seqcode.yaml
- Started UTC: 2026-09-27T08:25:14Z
- Finished UTC: 2026-09-27T08:25:14Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidarchaeum_fankouense_seqcode.yaml` |
| Identifier | `NCBITaxon:3693715` |
| Label | `Acidarchaeum fankouense (SeqCode)` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:3693714` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI input only, with path
pinned by `data/taxa/PATHS.tsv:477123` and fields owned by generated inputs.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidarchaeum_fankouense_seqcode.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidarchaeum_fankouense_seqcode.yaml data/taxa/archaea/acidianus_ambivalens.yaml data/taxa/archaea/acidianus_brierleyi.yaml data/taxa/archaea/acidianus_convivator.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 64 YAML lines, 9 lineage entries, 1 NCBI source attestation, 4 NCBI synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact ID-only local scan | Found this identifier in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or generated side-reference rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:642420`, 9 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 6 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, no normalized strain rows, no StrainInfo assembly or related rows, no direct StrainInfo or StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history.

## Identity and Grounding

`NCBITaxon:3693715` resolves to label `Acidarchaeum fankouense (SeqCode)`,
rank `SPECIES`, parent `NCBITaxon:3693714`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`. The generated record carries
those same fields and lands in `archaea` through `taxon_domain: ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:3693714` Acidarchaeum
(SeqCode). The bounded scan found no NCBI merge row and no retained old-id row
that would change the active identifier.

## Evidence

The NCBI row supports two exact synonyms, `Acidarchaeum fankouense` and
`Candidatus Acidarchaeum fankouense`, plus two quoted Chang et al. 2026 related
synonyms. The generated record correctly contains no LPSN nomenclature, GTDB
mapping, provider xref, BacDive strain, genome assembly, genome record, or
related-record sections.

The NCBI type-material table has 6 exact rows: `GCA_977012245` as SeqCode type
material and `CDRNDM000000000` plus `FK_Bin2` as Candidatus reference material,
with `personal::` aliases for the two accessions. These rows are side evidence
only; no BacDive or final normalized strain row is filed under this taxon.

The seed event is supported by `curation/seed_scope.tsv:618236`, which records
`NCBITaxon:3693715` as added on `2026-09-13` with reason `attested rule:
Acidarchaeum fankouense (SeqCode), 1 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, seed, path, type-material,
and generated YAML inputs, and found no omitted NCBI merge, LPSN, GTDB, GOLD,
BacDive, MediaDive, MADIN, BactoTraits, StrainInfo, ATB, culture-collection,
normalized assembly, normalized genome, normalized related-record, or
StrainInfo exclusion row for this taxon.

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

This was a read-only generated-record review. It did not append curation
history, promote `mapping_status`, or touch the seeded YAML.
