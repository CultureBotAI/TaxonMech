# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_mattraensis.yaml`
- Taxon: `NCBITaxon:1185379` (`Ogataea mattraensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1185379`, label `Ogataea mattraensis`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_mattraensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_maris.yaml data/taxa/eukaryota/ogataea_mattraensis.yaml data/taxa/eukaryota/ogataea_methanolica.yaml data/taxa/eukaryota/ogataea_minuta.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58239` contains the seeded identifier with reason `attested rule: Ogataea mattraensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:265114` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:265114` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:4090`, where `NCBITaxon:1185379` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705020` / `Candida mattraensis CBS 12097`, linked to project `Gp0831040`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material is limited to 10 `Ogataea mattraensis` culture-from-holotype and holotype rows for `CBS 12097` and `BCC 42668`, including `BCC<THA>` variants.
- `data/raw/ncbi_merged_ids.tsv:99442` maps side-inventory old ID `NCBITaxon:936270` into `NCBITaxon:1185379`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
- Exact BacDive, StrainInfo, generated strain, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1185379`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or native GOLD side inventories.

## Additional Notes

- None.
