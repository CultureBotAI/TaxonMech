# YAML Record Review

- Target: `data/taxa/eukaryota/ophiocordyceps_sinensis.yaml`
- Taxon: `NCBITaxon:72228` (`Ophiocordyceps sinensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:72228`, label `Ophiocordyceps sinensis`.
- It is grounded exactly under `NCBITaxon:474995` (`Ophiocordyceps`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Ophiocordyceps`.

## Validation

- `just validate data/taxa/eukaryota/ophiocordyceps_sinensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ophiocordyceps_camponoti_leonardi_nom_inval.yaml data/taxa/eukaryota/ophiocordyceps_camponoti_rufipedis.yaml data/taxa/eukaryota/ophiocordyceps_camponoti_saundersi_nom_inval.yaml data/taxa/eukaryota/ophiocordyceps_sinensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53241` contains the seeded identifier with reason `attested rule: Ophiocordyceps sinensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:10103` matches the YAML identity: parent `NCBITaxon:474995`, rank `SPECIES`, three exact synonyms, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:10103` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41983`, where `NCBITaxon:72228` has `organism_count` 5.
- Native GOLD has five exact current-taxid organism rows, six linked projects, and four analysis rows linked through those projects, matching the aggregate GOLD organism count used by the YAML.
- Exact StrainInfo side evidence has two direct `NCBITaxon:72228` records, `siID` 209187 and 232332, and four deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:72228`; the record correctly has `strain_count: 0`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:100490` and `NCBITaxon:1602209` to `NCBITaxon:72228`, but no retained retired source row generated a YAML `replaces` entry.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD or StrainInfo side inventories.

## Additional Notes

- None.
