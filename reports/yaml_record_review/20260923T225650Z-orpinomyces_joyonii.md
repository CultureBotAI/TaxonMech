# YAML Record Review

- Target: `data/taxa/eukaryota/orpinomyces_joyonii.yaml`
- Taxon: `NCBITaxon:48250` (`Orpinomyces joyonii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:48250`, label `Orpinomyces joyonii`.
- It is grounded exactly under `NCBITaxon:37163` (`Orpinomyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Orpinomyces`.

## Validation

- `just validate data/taxa/eukaryota/orpinomyces_joyonii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ordospora_colligata.yaml data/taxa/eukaryota/orpinomyces_intercalaris.yaml data/taxa/eukaryota/orpinomyces_joyonii.yaml data/taxa/eukaryota/orpinomyces_sp.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52747` contains the seeded identifier with reason `attested rule: Orpinomyces joyonii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6139` matches the YAML identity: parent `NCBITaxon:37163`, rank `SPECIES`, no exact or related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6139` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36789`, where `NCBITaxon:48250` has `organism_count` 6.
- Native GOLD has one exact current-taxid organism row, `Go0021047` / `Orpinomyces joyonii SG4`, linked to project `Gp0021047` and no analysis rows.

## Completeness

- Exact NCBI type-material, StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:48250`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD side inventories.

## Additional Notes

- None.
