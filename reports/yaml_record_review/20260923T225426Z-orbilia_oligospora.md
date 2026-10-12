# YAML Record Review

- Target: `data/taxa/eukaryota/orbilia_oligospora.yaml`
- Taxon: `NCBITaxon:2813651` (`Orbilia oligospora`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2813651`, label `Orbilia oligospora`.
- It is grounded exactly under `NCBITaxon:47022` (`Orbilia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Orbilia`.

## Validation

- `just validate data/taxa/eukaryota/orbilia_oligospora.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ophiostoma_triangulosporum.yaml data/taxa/eukaryota/ophiostoma_valdivianum.yaml data/taxa/eukaryota/orbilia_brochopaga.yaml data/taxa/eukaryota/orbilia_oligospora.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63279` contains the seeded identifier with reason `attested rule: Orbilia oligospora, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:558697` matches the YAML identity: parent `NCBITaxon:47022`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:558697` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:27064`, where `NCBITaxon:2813651` has `organism_count` 20.
- Native GOLD has 20 exact current-taxid organism rows, 20 linked projects, and 20 analysis rows linked through those projects, matching the aggregate GOLD organism count used by the YAML.
- Exact StrainInfo side evidence has nine direct `NCBITaxon:2813651` records and 10 deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:2813651`; the record correctly has `strain_count: 0`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old ID `NCBITaxon:13349` to `NCBITaxon:2813651`, but no retained retired source row generated a YAML `replaces` entry.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD or StrainInfo side inventories.

## Additional Notes

- None.
