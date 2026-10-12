# YAML Record Review

- Target: `data/taxa/eukaryota/mrakia_cryoconiti.yaml`
- Taxon: `NCBITaxon:752005` (`Mrakia cryoconiti`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:752005`, label `Mrakia cryoconiti`.
- It is grounded exactly under `NCBITaxon:29901` (`Mrakia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mrakia`.

## Validation

- `just validate data/taxa/eukaryota/mrakia_cryoconiti.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mrakia_cryoconiti.yaml ... mrakia_psychrophila.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56651` contains the seeded identifier with reason `attested rule: Mrakia cryoconiti, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:173448` matches the YAML identity: parent `NCBITaxon:29901`, rank `SPECIES`, exact synonym `Mrakiella cryoconiti`, and both related synonyms represented in YAML.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:173448` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42314`, where `NCBITaxon:752005` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0608487` / `Mrakiella cryoconiti A 15` and `Go0608488` / `Mrakiella cryoconiti DSM 21094`; no native project rows were linked to those organism IDs.
- `data/raw/ncbi_type_material.tsv:262060-262063` has `CBS 10834` culture-from-holotype aliases and `A15` holotype aliases under the `Mrakiella cryoconiti` name.

## Completeness

- Exact StrainInfo has one direct record and one deposit row for `NCBITaxon:752005`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:752005`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:752005`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The local native GOLD organism evidence is present, but the current native exact scan found no project rows for the two exact organism IDs.
