# YAML Record Review

- Target: `data/taxa/eukaryota/mrakia_frigida.yaml`
- Taxon: `NCBITaxon:29902` (`Mrakia frigida`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:29902`, label `Mrakia frigida`.
- It is grounded exactly under `NCBITaxon:29901` (`Mrakia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mrakia`.

## Validation

- `just validate data/taxa/eukaryota/mrakia_frigida.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mrakia_cryoconiti.yaml ... mrakia_psychrophila.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52225` contains the seeded identifier with reason `attested rule: Mrakia frigida, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:3299` matches the YAML identity: parent `NCBITaxon:29901`, rank `SPECIES`, exact synonyms `Cryptococcus curiosus` and `Leucosporidium frigidum`, and the three related synonyms represented in YAML.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:3299` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:29942`, where `NCBITaxon:29902` has `organism_count` 9.
- A complete native GOLD exact scan found nine current-taxid organism rows for `NCBITaxon:29902`, four linked projects, and two native analysis rows: `Mrakia frigida Nwmf-AP1` and `Mrakia frigida JCM 7857`.
- A complete exact `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found 17 type-material rows under `Leucosporidium frigidum`, spanning `ATCC 22029`, `CBS 5270`, `IFO 1920`, `IGC 3896`, `JCM 7857`, `MUCL 30339`, `NCYC 704`, and `NRRL Y-7103` aliases.

## Completeness

- Exact StrainInfo has 24 direct records and 85 deposit rows for `NCBITaxon:29902`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:29902`.
- `data/raw/ncbi_merged_ids.tsv` carries side-inventory old IDs `NCBITaxon:104672` and `NCBITaxon:162221` that merge into `NCBITaxon:29902`, but the bounded scan found no retained retired rows in `data/raw/ncbitaxon_taxa.tsv`; generated `replaces` omission is consistent with local retained-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- Five native GOLD organism rows retain the former `Leucosporidium frigidum` name while using the current `NCBITaxon:29902` taxon ID.
