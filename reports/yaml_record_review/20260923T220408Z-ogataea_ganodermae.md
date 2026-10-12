# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_ganodermae.yaml`
- Taxon: `NCBITaxon:539824` (`Ogataea ganodermatis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:539824`, label `Ogataea ganodermatis`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_ganodermae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_degrootiae.yaml data/taxa/eukaryota/ogataea_dorogensis.yaml data/taxa/eukaryota/ogataea_ganodermae.yaml data/taxa/eukaryota/ogataea_glucozyma.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55937` contains the seeded identifier with reason `attested rule: Ogataea ganodermae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:124257` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:124257` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38267`, where `NCBITaxon:539824` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0704964` / `Ogataea ganodermae CBS 10646`, linked to project `Gp0830980`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material is limited to six `Ogataea ganodermatis` culture-from-holotype and holotype designations for `CBS 10646` and `CGMCC 2.3435`.
- `data/raw/ncbi_merged_ids.tsv:79998` maps side-inventory old ID `NCBITaxon:468358` into `NCBITaxon:539824`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
- Exact BacDive, StrainInfo, generated strain, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:539824`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or native GOLD side inventories.

## Additional Notes

- The YAML filename and seed-scope reason retain the `Ogataea ganodermae` synonym spelling while the current NCBI label is `Ogataea ganodermatis`.
