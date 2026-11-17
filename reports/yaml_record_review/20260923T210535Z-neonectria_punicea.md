# YAML Record Review

- Target: `data/taxa/eukaryota/neonectria_punicea.yaml`
- Taxon: `NCBITaxon:979145` (`Neonectria punicea`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:979145`, label `Neonectria punicea`.
- It is grounded exactly under `NCBITaxon:140106` (`Neonectria`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neonectria`.

## Validation

- `just validate data/taxa/eukaryota/neonectria_punicea.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neonectria_punicea.yaml data/taxa/eukaryota/neonectria_sp_b_13.yaml data/taxa/eukaryota/neonothopanus_nambi.yaml data/taxa/eukaryota/neopestalotiopsis_clavispora.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57033` contains the seeded identifier with reason `attested rule: Neonectria punicea, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:204166` matches the YAML identity: parent `NCBITaxon:140106`, rank `SPECIES`, six synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:204166` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45168`, where `NCBITaxon:979145` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0517401` / `Neonectria punicea CBS 119724`, linked to native project `Gp0441454` and one project-linked native analysis.

## Completeness

- A structured exact scan found no rows for `NCBITaxon:979145` in `data/raw/ncbi_type_material.tsv`.
- Exact StrainInfo side inventory found 7 direct records and 10 exact deposit assertions, including sampled designations `KCTC 16047`, `CBS 131.25`, `DSM 62810`, `CBS 150.29`, `CBS 152.29`, and `CBS 242.29`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old ID `NCBITaxon:78411` into `NCBITaxon:979145`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` points to the target, so the generated record correctly omits `replaces`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and checked auxiliary source rows were empty for `NCBITaxon:979145`; the record correctly has `strain_count: 0`.
- The exact StrainInfo side inventory did not materialize local strain rows; StrainInfo only joins through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
