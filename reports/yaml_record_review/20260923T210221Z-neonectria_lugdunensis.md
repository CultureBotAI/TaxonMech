# YAML Record Review

- Target: `data/taxa/eukaryota/neonectria_lugdunensis.yaml`
- Taxon: `NCBITaxon:57155` (`Neonectria lugdunensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:57155`, label `Neonectria lugdunensis`.
- It is grounded exactly under `NCBITaxon:140106` (`Neonectria`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neonectria`.

## Validation

- `just validate data/taxa/eukaryota/neonectria_lugdunensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neonectria_ditissima.yaml data/taxa/eukaryota/neonectria_faginata.yaml data/taxa/eukaryota/neonectria_hederae.yaml data/taxa/eukaryota/neonectria_lugdunensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52978` contains the seeded identifier with reason `attested rule: Neonectria lugdunensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:7267` matches the YAML identity: parent `NCBITaxon:140106`, rank `SPECIES`, four synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:7267` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:39155`, where `NCBITaxon:57155` has `organism_count` 1.
- The retained GOLD aggregate supports the generated source attestation; a direct exact scan of the current local native GOLD organism, project, and analysis JSONL snapshots found no rows for current NCBI taxid `57155`.

## Completeness

- The NCBI type-material inventory contains two exact `culture from type material` rows for `NCBITaxon:57155`, both for `Heliscus lugdunensis` with `CBS 250.58` spelling variants.
- Exact StrainInfo side inventory found 19 direct records and 21 exact deposit assertions, including sampled designations `MUCL 28006`, `MUCL 28013`, `MUCL 39530`, `MUCL 28051`, and `MUCL 39531`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old ID `NCBITaxon:575478` into `NCBITaxon:57155`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` points to the target, so the generated record correctly omits `replaces`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and checked auxiliary source rows were empty for `NCBITaxon:57155`; the record correctly has `strain_count: 0`.
- The exact StrainInfo side inventory did not materialize local strain rows; StrainInfo only joins through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, NCBI type-material, or native GOLD side inventories.

## Additional Notes

- `data/raw/gold_organisms.tsv` is a transformed aggregate inventory and can differ from exact current-taxid native GOLD JSONL scans. This record asserts only the retained aggregate organism count.
