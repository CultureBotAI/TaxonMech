# YAML Record Review

- Target: `data/taxa/eukaryota/oehlia_diaphana.yaml`
- Taxon: `NCBITaxon:118614` (`Oehlia diaphana`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:118614`, label `Oehlia diaphana`.
- It is grounded exactly under `NCBITaxon:2483397` (`Oehlia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Oehlia`.

## Validation

- `just validate data/taxa/eukaryota/oehlia_diaphana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/oculimacula_yallundae.yaml data/taxa/eukaryota/odontella_aurita.yaml data/taxa/eukaryota/oehlia_diaphana.yaml data/taxa/eukaryota/ogataea_allantospora.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53843` contains the seeded identifier with reason `attested rule: Oehlia diaphana, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:22192` matches the YAML identity: parent `NCBITaxon:2483397`, rank `SPECIES`, three exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:22192` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:4164`, where `NCBITaxon:118614` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0517194` / `Rhizophagus diaphanus SD1`, linked to project `Gp0441232`; one native analysis row links through `Gp0441232`.

## Completeness

- Exact StrainInfo side inventory found 2 direct records and 2 deposit groups, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:118614`.
- Exact NCBI type-material, NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:118614`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
