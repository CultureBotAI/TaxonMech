# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_plumbeus.yaml`
- Taxon: `NCBITaxon:97098` (`Mucor plumbeus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:97098`, label `Mucor plumbeus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_plumbeus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_philippovii_nom_inval.yaml ... mucor_plumbeus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53575` contains the seeded identifier with reason `attested rule: Mucor plumbeus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:16380` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor plumbeus Bonord., 1864`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:16380` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45136`, where `NCBITaxon:97098` has `organism_count` 7.
- Native GOLD has six exact current-taxid organism rows for `JES 114`, `NRRL 2353`, `NRRL 1159`, `NRRL 2357`, `NRRL 2630`, and `CBS 226.32`; those organism rows link to six native GOLD projects and one native analysis through project ID `Gp0645221`.

## Completeness

- Exact StrainInfo has 118 direct records and 140 deposit rows for `NCBITaxon:97098`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:97098`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:97098`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The transformed GOLD aggregate count is 7, while the local native GOLD exact current-taxid scan recovered 6 organism rows.
