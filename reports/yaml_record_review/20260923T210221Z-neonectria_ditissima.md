# YAML Record Review

- Target: `data/taxa/eukaryota/neonectria_ditissima.yaml`
- Taxon: `NCBITaxon:78410` (`Neonectria ditissima`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:78410`, label `Neonectria ditissima`.
- It is grounded exactly under `NCBITaxon:140106` (`Neonectria`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neonectria`.

## Validation

- `just validate data/taxa/eukaryota/neonectria_ditissima.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/neonectria_ditissima.yaml data/taxa/eukaryota/neonectria_faginata.yaml data/taxa/eukaryota/neonectria_hederae.yaml data/taxa/eukaryota/neonectria_lugdunensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53324` contains the seeded identifier with reason `attested rule: Neonectria ditissima, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:11455` matches the YAML identity: parent `NCBITaxon:140106`, rank `SPECIES`, four synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:11455` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42737`, where `NCBITaxon:78410` has `organism_count` 4.
- Native GOLD has four exact current-taxid organism rows: `Go0119025` / `Neonectria ditissima R09/05`, `Go0139468` / `Neonectria ditissima RS324p`, `Go0139469` / `Neonectria ditissima RS305p`, and `Go0678572` / `Neonectria ditissima CBS 226.31`.
- Each native GOLD organism links to one project, and each of those projects has one native analysis row linked through `AP PROJECT GOLD IDS`.

## Completeness

- A structured exact scan found no rows for `NCBITaxon:78410` in `data/raw/ncbi_type_material.tsv`.
- Exact StrainInfo side inventory found 18 direct records and 20 exact deposit assertions, including sampled designations `MUCL 6128`, `IFO 5995`, `NBRC 5995`, `IMI 113922`, `IMI 113902`, and `IMI 113903`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:78410`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact StrainInfo side inventory did not materialize local strain rows; StrainInfo only joins through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
