# YAML Record Review: Morchella anatolica

- Record: `data/taxa/eukaryota/morchella_anatolica.yaml`
- Reviewed: `2026-09-23T17:05:55Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1582322`
- Label: `Morchella anatolica`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:3367357` (`Morchella sect. Rufobrunnea`)

## Validation

- `just validate data/taxa/eukaryota/morchella_anatolica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_anatolica.yaml data/taxa/eukaryota/morchella_angusticeps.yaml data/taxa/eukaryota/morchella_arbutiphila.yaml data/taxa/eukaryota/morchella_brunnea.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:408390` has the same identifier, label, species rank, `NCBITaxon:3367357` parent, genetic code `1`, related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Morchella anatolica Isiloglu, Spooner, Alli & Solak, 2010` and `Morchella lanceolata Clowez & Illescas, 2012` as related synonyms from NCBI.
- The YAML lineage contains the expected 14 entries from `root` through `Morchella sect. Rufobrunnea`.

## Evidence

- `curation/seed_scope.tsv:60526` includes `NCBITaxon:1582322` with reason `attested rule: Morchella anatolica, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:12778` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0568259` for `Morchella anatolica PhC 233`, two linked project rows, and no linked native analyses.
- A complete `rg --no-ignore --hidden` scan found one NCBI type-material row at `data/raw/ncbi_type_material.tsv:44268`, covering `K(M) 157099`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has no exact direct or deposit rows for `NCBITaxon:1582322`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found old ID `NCBITaxon:1612333` merging into `NCBITaxon:1582322`, while a complete exact scan found that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1582322`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
