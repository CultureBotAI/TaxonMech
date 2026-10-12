# YAML Record Review

- Target: `data/taxa/eukaryota/ordospora_colligata.yaml`
- Taxon: `NCBITaxon:174685` (`Ordospora colligata`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:174685`, label `Ordospora colligata`.
- It is grounded exactly under `NCBITaxon:174684` (`Ordospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Ordospora`.

## Validation

- `just validate data/taxa/eukaryota/ordospora_colligata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ordospora_colligata.yaml data/taxa/eukaryota/orpinomyces_intercalaris.yaml data/taxa/eukaryota/orpinomyces_joyonii.yaml data/taxa/eukaryota/orpinomyces_sp.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54282` contains the seeded identifier with reason `attested rule: Ordospora colligata, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:35426` matches the YAML identity: parent `NCBITaxon:174684`, rank `SPECIES`, no exact synonyms, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:35426` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:15183`, where `NCBITaxon:174685` has `organism_count` 3.
- Native GOLD has three exact current-taxid organism rows, three linked projects, and three analysis rows linked through those projects, matching the aggregate GOLD organism count used by the YAML.

## Completeness

- Exact NCBI type-material, StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:174685`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD side inventories.

## Additional Notes

- None.
