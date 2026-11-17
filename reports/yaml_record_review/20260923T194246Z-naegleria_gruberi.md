# YAML Record Review

- Target: `data/taxa/eukaryota/naegleria_gruberi.yaml`
- Taxon: `NCBITaxon:5762` (`Naegleria gruberi`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:5762`, label `Naegleria gruberi`.
- It is grounded exactly under `NCBITaxon:5761` (`Naegleria`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Naegleria`.

## Validation

- `just validate data/taxa/eukaryota/naegleria_gruberi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nadsonia_fulvescens_var_elongata_dsm_6958.yaml data/taxa/eukaryota/nadsonia_starkeyi_henricii.yaml data/taxa/eukaryota/naegleria_fowleri.yaml data/taxa/eukaryota/naegleria_gruberi.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52078` contains the seeded identifier with reason `attested rule: Naegleria gruberi, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2564` matches the YAML identity: parent `NCBITaxon:5761`, rank `SPECIES`, and no synonyms.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2564` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:39290`, where `NCBITaxon:5762` has `organism_count` 1.
- Native GOLD has two exact current-taxid organism rows, `Go0002409` / `Naegleria gruberi` and `Go0002410` / `Naegleria gruberi NEG-M`, linked to three projects and one native analysis for `Naegleria gruberi NEG-M`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:5762`.
- Exact StrainInfo side inventory has 7 direct rows and 7 deposit entries for `NCBITaxon:5762`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:5762`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- The YAML GOLD assertion count matches transformed `data/raw/gold_organisms.tsv`; the local native GOLD exact scan currently finds two organism rows for this taxon.
