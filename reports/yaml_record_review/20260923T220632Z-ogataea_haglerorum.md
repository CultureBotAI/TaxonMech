# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_haglerorum.yaml`
- Taxon: `NCBITaxon:1937702` (`Ogataea haglerorum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1937702`, label `Ogataea haglerorum`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_haglerorum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_haglerorum.yaml data/taxa/eukaryota/ogataea_henricii.yaml data/taxa/eukaryota/ogataea_kodamae.yaml data/taxa/eukaryota/ogataea_krabiensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61679` contains the seeded identifier with reason `attested rule: Ogataea haglerorum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:497543` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:497543` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:17807`, where `NCBITaxon:1937702` has `organism_count` 23.
- Native GOLD has 23 exact current-taxid organism rows, 23 linked project rows, and 22 linked analysis rows for `NCBITaxon:1937702`.

## Completeness

- Exact NCBI type material is limited to eight `Ogataea haglerorum` culture-from-holotype, holotype, and isotype designations for `CBS 14645`, `UCDFST 17-101`, `VKPM Y-2583`, and `UCD-FST 81-530.1`.
- Exact NCBI merged-ID, BacDive, StrainInfo, generated strain, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1937702`; the record correctly has `strain_count: 0`.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or native GOLD side inventories.

## Additional Notes

- None.
