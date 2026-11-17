# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_trehaloabstinens.yaml`
- Taxon: `NCBITaxon:169509` (`Ogataea trehaloabstinens`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:169509`, label `Ogataea trehaloabstinens`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_trehaloabstinens.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_thermomethanolica.yaml data/taxa/eukaryota/ogataea_trehaloabstinens.yaml data/taxa/eukaryota/ogataea_trehalophila.yaml data/taxa/eukaryota/ogataea_wickerhamii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54254` contains the seeded identifier with reason `attested rule: Ogataea trehaloabstinens, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:34591` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:34591` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:14628`, where `NCBITaxon:169509` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0517128` / `Ogataea trehaloabstinens NRRL Y-27595`, linked to project `Gp0441166` and one analysis row via that project.

## Completeness

- Exact NCBI type material has 10 duplicated spelling rows for `Pichia trehaloabstinens`, covering `CBS 9256`, `NCAIM Y.01537` / `NCAIM Y-1537`, and `NRRL Y-27595`.
- Exact StrainInfo side inventory found 3 direct records and 11 deposits, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:169509`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:169509`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
