# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_moelleri.yaml`
- Taxon: `NCBITaxon:1302847` (`Mucor moelleri`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1302847`, label `Mucor moelleri`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_moelleri.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_mephitis.yaml ... mucor_mucedo.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59297` contains the seeded identifier with reason `attested rule: Mucor moelleri, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:307838` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, exact synonym `Zygorhynchus moelleri`, and two related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:307838` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:7417`, where `NCBITaxon:1302847` has `organism_count` 4.
- Native GOLD has four exact current-taxid organism rows for `NRRL 1498`, `NRRL 1497`, `NRRL 1625`, and `NRRL 3138`; those organism rows link to four native GOLD projects and no native analyses.
- `data/raw/ncbi_type_material.tsv:20932-20940` has nine aliases: `CBS 406.58` and `CBS:406.58` as cultures from neotype material, plus `ATCC 16388`, `ATCC:16388`, `CBS 444.65`, `CBS:444.65`, `VKM F-1366`, `VKM:F-1366`, and `VKM:F:1366` as type-material aliases.

## Completeness

- Exact StrainInfo has 48 direct records and 62 deposit rows for `NCBITaxon:1302847`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:1302847`.
- `data/raw/ncbi_merged_ids.tsv:23632` and `data/raw/ncbi_merged_ids.tsv:63972` contain side-inventory old IDs `NCBITaxon:1664330` and `NCBITaxon:311242` merged into `NCBITaxon:1302847`; the record has no `replaces` entries because no retained retired-ID rows were present in the local NCBI taxon inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
