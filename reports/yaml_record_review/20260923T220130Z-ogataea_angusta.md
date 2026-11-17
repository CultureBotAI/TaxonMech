# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_angusta.yaml`
- Taxon: `NCBITaxon:870730` (`Ogataea angusta`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:870730`, label `Ogataea angusta`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_angusta.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/ogataea_angusta.yaml data/taxa/eukaryota/ogataea_arabinofermentans.yaml data/taxa/eukaryota/ogataea_chonburiensis.yaml data/taxa/eukaryota/ogataea_corticis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56807` contains the seeded identifier with reason `attested rule: Ogataea angusta, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:184559` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, two exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:184559` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:43608`, where `NCBITaxon:870730` has `organism_count` 13.
- Native GOLD has 14 exact current-taxid organism rows, 14 linked project rows, and 10 linked analysis rows for `NCBITaxon:870730`.

## Completeness

- Exact NCBI type material is limited to five `Hansenula angusta` culture-from-type-material designations for `CBS 7073` and `NRRL Y-2214`.
- Exact StrainInfo side inventory found 105 direct records and 172 deposit groups, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:870730`.
- `data/raw/ncbi_merged_ids.tsv:81723` maps side-inventory old ID `NCBITaxon:4905` into `NCBITaxon:870730`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
- Exact BacDive and checked auxiliary source rows were empty for `NCBITaxon:870730`; the record correctly has `strain_count: 0`.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs can differ from that generated aggregate and do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
