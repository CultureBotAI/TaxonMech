# YAML Record Review

- Target: `data/taxa/eukaryota/ophiostoma_triangulosporum.yaml`
- Taxon: `NCBITaxon:91039` (`Ophiostoma triangulosporum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:91039`, label `Ophiostoma triangulosporum`.
- It is grounded exactly under `NCBITaxon:5159` (`Ophiostoma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Ophiostoma`.

## Validation

- `just validate data/taxa/eukaryota/ophiostoma_triangulosporum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ophiostoma_triangulosporum.yaml data/taxa/eukaryota/ophiostoma_valdivianum.yaml data/taxa/eukaryota/orbilia_brochopaga.yaml data/taxa/eukaryota/orbilia_oligospora.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53507` contains the seeded identifier with reason `attested rule: Ophiostoma triangulosporum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:14760` matches the YAML identity: parent `NCBITaxon:5159`, rank `SPECIES`, no exact synonyms, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:14760` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:44332`, where `NCBITaxon:91039` has `organism_count` 4.
- Native GOLD has four exact current-taxid organism rows and no linked projects or analysis rows for `NCBITaxon:91039`.
- Exact StrainInfo side evidence has one direct `NCBITaxon:91039` record, `siID` 112839, and three deposits across that record.

## Completeness

- Exact NCBI type material has two isotype rows for `NCBITaxon:91039`, covering `CBS 138.77` and `CBS:138.77`.
- Exact BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:91039`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, native GOLD, or StrainInfo side inventories.

## Additional Notes

- None.
