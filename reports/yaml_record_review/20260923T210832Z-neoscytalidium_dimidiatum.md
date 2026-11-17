# YAML Record Review

- Target: `data/taxa/eukaryota/neoscytalidium_dimidiatum.yaml`
- Taxon: `NCBITaxon:108428` (`Neoscytalidium dimidiatum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:108428`, label `Neoscytalidium dimidiatum`.
- It is grounded exactly under `NCBITaxon:463684` (`Neoscytalidium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neoscytalidium`.

## Validation

- `just validate data/taxa/eukaryota/neoscytalidium_dimidiatum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neophaeococcomyces_sp.yaml data/taxa/eukaryota/neophaeosphaeria_agaves.yaml data/taxa/eukaryota/neopyrenochaeta_inflorescentiae.yaml data/taxa/eukaryota/neoscytalidium_dimidiatum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53729` contains the seeded identifier with reason `attested rule: Neoscytalidium dimidiatum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:19607` matches the YAML identity: parent `NCBITaxon:463684`, rank `SPECIES`, nine synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:19607` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:1551`, where `NCBITaxon:108428` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0452582` / `Neoscytalidium dimidiatum ERS1230299`, linked to native project `Gp0317009` and one project-linked native analysis.

## Completeness

- A structured exact scan found no rows for `NCBITaxon:108428` in `data/raw/ncbi_type_material.tsv`.
- Exact StrainInfo side inventory found 65 direct records and 78 exact deposit assertions, including sampled designations `IHEM 10366`, `IHEM 10364`, `IHEM 22788`, `IHEM 22963`, and `IHEM 26835`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:108428`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact StrainInfo side inventory did not materialize local strain rows; StrainInfo only joins through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
