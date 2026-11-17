# YAML Record Review

- Target: `data/taxa/eukaryota/obelidium_mucronatum.yaml`
- Taxon: `NCBITaxon:110081` (`Obelidium mucronatum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:110081`, label `Obelidium mucronatum`.
- It is grounded exactly under `NCBITaxon:110080` (`Obelidium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Obelidium`.

## Validation

- `just validate data/taxa/eukaryota/obelidium_mucronatum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/obelidium_mucronatum.yaml data/taxa/eukaryota/ochromonadaceae_sp_ccmp2298.yaml data/taxa/eukaryota/ochromonas_sp_ccmp1393.yaml data/taxa/eukaryota/octactis_speculum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53756` contains the seeded identifier with reason `attested rule: Obelidium mucronatum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:19752` matches the YAML identity: parent `NCBITaxon:110080`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:19752` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:1853`, where `NCBITaxon:110081` has `organism_count` 2.
- Native GOLD has one exact current-taxid organism row, `Go0110666` / `Obelidium mucronatum JEL802`, linked to projects `Gp0112136` and `Gp0112137`; one native analysis row links through `Gp0112136`.

## Completeness

- Exact NCBI merged-ID rows, NCBI type-material rows, BacDive rows, generated raw strain rows, exact StrainInfo rows, generated StrainInfo target rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:110081`; the record correctly has `strain_count: 0`.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs can differ from that generated aggregate and do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD side inventories.

## Additional Notes

- None.
