# YAML Record Review

- Target: `data/taxa/eukaryota/neonectria_hederae.yaml`
- Taxon: `NCBITaxon:78402` (`Neonectria hederae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:78402`, label `Neonectria hederae`.
- It is grounded exactly under `NCBITaxon:140106` (`Neonectria`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neonectria`.

## Validation

- `just validate data/taxa/eukaryota/neonectria_hederae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neonectria_ditissima.yaml data/taxa/eukaryota/neonectria_faginata.yaml data/taxa/eukaryota/neonectria_hederae.yaml data/taxa/eukaryota/neonectria_lugdunensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53323` contains the seeded identifier with reason `attested rule: Neonectria hederae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:11454` matches the YAML identity: parent `NCBITaxon:140106`, rank `SPECIES`, five synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:11454` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42736`, where `NCBITaxon:78402` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0517402` / `Neonectria hederae CBS 714.97`, linked to native project `Gp0441455` and one project-linked native analysis.

## Completeness

- A structured exact scan found no rows for `NCBITaxon:78402` in `data/raw/ncbi_type_material.tsv`.
- Exact StrainInfo side inventory found 3 direct records and 5 exact deposit assertions, including `CBS 146.84`, `IMI 281224`, `CBS 714.97`, `IMI 058770a`, and type-designated `ATCC 16543`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:78402`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact StrainInfo side inventory did not materialize local strain rows; StrainInfo only joins through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
