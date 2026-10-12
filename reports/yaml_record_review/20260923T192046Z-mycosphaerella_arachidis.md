# YAML Record Review

- Target: `data/taxa/eukaryota/mycosphaerella_arachidis.yaml`
- Taxon: `NCBITaxon:143450` (`Mycosphaerella arachidis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:143450`, label `Mycosphaerella arachidis`.
- It is grounded exactly under `NCBITaxon:41254` (`Mycosphaerella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Mycosphaerella`.

## Validation

- `just validate data/taxa/eukaryota/mycosphaerella_arachidis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycogone_sp.yaml data/taxa/eukaryota/myconymphaea_yatsukahoi.yaml data/taxa/eukaryota/mycosarcoma_maydis.yaml data/taxa/eukaryota/mycosphaerella_arachidis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54019` contains the seeded identifier with reason `attested rule: Mycosphaerella arachidis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:29046` matches the YAML identity: parent `NCBITaxon:41254`, rank `SPECIES`, exact synonyms `Cercospora arachidicola` and `Passalora arachidicola`, and three related synonyms.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:29046` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:10357`, where `NCBITaxon:143450` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0144974` / `Mycosphaerella arachidis CALF-13A`, linked to project `Gp0150604` and one native analysis for `Mycosphaerella arachidis CALF-13A`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:143450`.
- Exact StrainInfo has 5 direct records and 5 deposit rows for `NCBITaxon:143450`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:143450`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found 2 side-inventory old IDs merged into `NCBITaxon:143450`: `NCBITaxon:143449` and `NCBITaxon:227732`.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows for those old IDs in `data/raw/ncbitaxon_taxa.tsv`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
