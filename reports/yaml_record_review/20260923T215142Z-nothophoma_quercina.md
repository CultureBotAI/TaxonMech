# YAML Record Review

- Target: `data/taxa/eukaryota/nothophoma_quercina.yaml`
- Taxon: `NCBITaxon:749835` (`Nothophoma quercina`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:749835`, label `Nothophoma quercina`.
- It is grounded exactly under `NCBITaxon:1770230` (`Nothophoma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Nothophoma`.

## Validation

- `just validate data/taxa/eukaryota/nothophoma_quercina.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nothofagozyma_chilensis.yaml data/taxa/eukaryota/nothomitra_cinnamomea.yaml data/taxa/eukaryota/nothophoma_quercina.yaml data/taxa/eukaryota/obba_rivulosa.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56644` contains the seeded identifier with reason `attested rule: Nothophoma quercina, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:173369` matches the YAML identity: parent `NCBITaxon:1770230`, rank `SPECIES`, three exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:173369` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42289`, where `NCBITaxon:749835` has `organism_count` 1.
- Exact scans of the current native GOLD JSONL catalogs found no current exact organism, project, or analysis rows for `NCBITaxon:749835`.

## Completeness

- Exact StrainInfo side inventory found 2 direct records and 3 deposit entries: `CBS 633.92`, `ATCC 36786`, and `ATCC 38614`.
- `data/raw/ncbi_merged_ids.tsv:96069` maps side-inventory old ID `NCBITaxon:81445` into `NCBITaxon:749835`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
- Exact NCBI type-material, BacDive, generated raw strain rows, generated StrainInfo target rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:749835`; the record correctly has `strain_count: 0`.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs can differ from that generated aggregate and do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
