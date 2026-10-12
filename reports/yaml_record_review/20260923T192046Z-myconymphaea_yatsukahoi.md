# YAML Record Review

- Target: `data/taxa/eukaryota/myconymphaea_yatsukahoi.yaml`
- Taxon: `NCBITaxon:417182` (`Myconymphaea yatsukahoi`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:417182`, label `Myconymphaea yatsukahoi`.
- It is grounded exactly under `NCBITaxon:417181` (`Myconymphaea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Myconymphaea`.

## Validation

- `just validate data/taxa/eukaryota/myconymphaea_yatsukahoi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycogone_sp.yaml data/taxa/eukaryota/myconymphaea_yatsukahoi.yaml data/taxa/eukaryota/mycosarcoma_maydis.yaml data/taxa/eukaryota/mycosphaerella_arachidis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55575` contains the seeded identifier with reason `attested rule: Myconymphaea yatsukahoi, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:91289` matches the YAML identity: parent `NCBITaxon:417181`, rank `SPECIES`, and related synonym `Myconymphaea yatsukahoi Kurihara, Degawa & Tokum., 2001`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:91289` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:34918`, where `NCBITaxon:417182` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0564613` / `Myconymphaea yatsukahoi NBRC 100467`, linked to projects `Gp0533786` and `Gp0533787` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 6 type-material rows for `NCBITaxon:417182`: 4 culture-from-holotype rows for `CBS 109376` and `NBRC 100467`, plus 2 holotype rows for `KPM NC0007581`.
- Exact StrainInfo has 1 direct record and 2 deposit rows for `NCBITaxon:417182`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:417182`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:417182`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.
