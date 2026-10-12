# YAML Record Review

- Target: `data/taxa/eukaryota/paragyromitra_infula.yaml`
- Taxon: `NCBITaxon:273506` (`Paragyromitra infula`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:273506`, label `Paragyromitra infula`.
- It is grounded exactly under `NCBITaxon:3135588` (`Paragyromitra`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Paragyromitra`.

## Validation

- `just validate data/taxa/eukaryota/paragyromitra_infula.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paraglomus_occultum.yaml data/taxa/eukaryota/paragyrodon_sphaerosporus.yaml data/taxa/eukaryota/paragyromitra_infula.yaml data/taxa/eukaryota/paralagenidium_karlingii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54930` contains the seeded identifier with reason `attested rule: Paragyromitra infula, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:56456` matches the YAML identity: parent `NCBITaxon:3135588`, rank `SPECIES`, two exact synonyms, four related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:56456` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:25502`, where `NCBITaxon:273506` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row and two project rows for strain `GyrinfSpk-SM18`; it found no analysis rows.
- Exact StrainInfo side evidence has three direct `NCBITaxon:273506` records and three deposits: `DSM 10402`, `DSM 10408`, and `UAMH 7349`.

## Completeness

- Exact NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:273506`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
