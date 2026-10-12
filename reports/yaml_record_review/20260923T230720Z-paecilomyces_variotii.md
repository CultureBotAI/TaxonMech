# YAML Record Review

- Target: `data/taxa/eukaryota/paecilomyces_variotii.yaml`
- Taxon: `NCBITaxon:264951` (`Paecilomyces variotii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:264951`, label `Paecilomyces variotii`.
- It is grounded exactly under `NCBITaxon:33202` (`Paecilomyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Paecilomyces`.

## Validation

- `just validate data/taxa/eukaryota/paecilomyces_variotii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paecilomyces_sp_m2902.yaml data/taxa/eukaryota/paecilomyces_sp_pk2413.yaml data/taxa/eukaryota/paecilomyces_sp_pl2402.yaml data/taxa/eukaryota/paecilomyces_variotii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54872` contains the seeded identifier with reason `attested rule: Paecilomyces variotii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:54231` matches the YAML identity: parent `NCBITaxon:33202`, rank `SPECIES`, four exact synonyms, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:54231` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:24269`, where `NCBITaxon:264951` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, three linked projects, and two analysis rows linked through those projects.
- Exact StrainInfo side evidence has 214 direct `NCBITaxon:264951` records and 302 deposits across those records.

## Completeness

- Exact NCBI type material has eight rows for `NCBITaxon:264951`, covering paired `CBS 101075`, `ATCC 90900`, `FRR 5219`, and `JCM 12815` designations.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old ID `NCBITaxon:45996` to `NCBITaxon:264951`, but no retained retired source row generated a YAML `replaces` entry.
- Exact BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:264951`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, native GOLD, or StrainInfo side inventories.

## Additional Notes

- None.
