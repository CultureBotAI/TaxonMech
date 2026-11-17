# YAML Record Review

- Target: `data/taxa/eukaryota/neonectria_faginata.yaml`
- Taxon: `NCBITaxon:992199` (`Neonectria faginata`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:992199`, label `Neonectria faginata`.
- It is grounded exactly under `NCBITaxon:140106` (`Neonectria`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neonectria`.

## Validation

- `just validate data/taxa/eukaryota/neonectria_faginata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neonectria_ditissima.yaml data/taxa/eukaryota/neonectria_faginata.yaml data/taxa/eukaryota/neonectria_hederae.yaml data/taxa/eukaryota/neonectria_lugdunensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57113` contains the seeded identifier with reason `attested rule: Neonectria faginata, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:206855` matches the YAML identity: parent `NCBITaxon:140106`, rank `SPECIES`, three synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:206855` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45424`, where `NCBITaxon:992199` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0678573` / `Neonectria faginata A.R. 4307` and `Go0678574` / `Neonectria faginata N1A`; they link to native projects `Gp0780533` and `Gp0780534`, each with one project-linked native analysis.

## Completeness

- The NCBI type-material inventory contains four exact isotype rows for `NCBITaxon:992199`, all for `Nectria coccinea var. faginata` with `MICH 14670` spelling variants.
- Exact StrainInfo side inventory found 8 direct records and 13 exact deposit assertions, including sampled designations `ATCC 38282`, `ATCC 38283`, `IMI 105738`, `IMI 113901`, and `IMI 268212`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old ID `NCBITaxon:397354` into `NCBITaxon:992199`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` points to the target, so the generated record correctly omits `replaces`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and checked auxiliary source rows were empty for `NCBITaxon:992199`; the record correctly has `strain_count: 0`.
- The exact StrainInfo side inventory did not materialize local strain rows; StrainInfo only joins through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
