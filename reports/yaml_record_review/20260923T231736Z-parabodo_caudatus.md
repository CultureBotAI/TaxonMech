# YAML Record Review

- Target: `data/taxa/eukaryota/parabodo_caudatus.yaml`
- Taxon: `NCBITaxon:351713` (`Parabodo caudatus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:351713`, label `Parabodo caudatus`.
- It is grounded exactly under `NCBITaxon:140243` (`Parabodo`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Parabodo`.

## Validation

- `just validate data/taxa/eukaryota/parabodo_caudatus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/papiliotrema_odontotermitis.yaml data/taxa/eukaryota/papulosa_amerospora.yaml data/taxa/eukaryota/parabodo_caudatus.yaml data/taxa/eukaryota/paracercomonas_sp.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55317` contains the seeded identifier with reason `attested rule: Parabodo caudatus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:72706` matches the YAML identity: parent `NCBITaxon:140243`, rank `SPECIES`, two exact synonyms, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:72706` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33031`, where `NCBITaxon:351713` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row and one project row for strain `ATCC 50361`; it found no analysis rows.
- Exact StrainInfo side evidence has three direct `NCBITaxon:351713` records and three deposits: `ATCC 30905`, `ATCC 30906`, and `ATCC 50361`.

## Completeness

- Exact NCBI type-material, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:351713`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains one old ID that now points at `NCBITaxon:351713`: `NCBITaxon:5713`; it is not retained as a retired taxon, so the YAML correctly has no `replaces` entry.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
