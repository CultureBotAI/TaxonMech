# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_plasmaticus.yaml`
- Taxon: `NCBITaxon:1196545` (`Mucor plasmaticus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1196545`, label `Mucor plasmaticus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_plasmaticus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_philippovii_nom_inval.yaml ... mucor_plumbeus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58296` contains the seeded identifier with reason `attested rule: Mucor plasmaticus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:269152` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor plasmaticus Tiegh., 1875`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:269152` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:4744`, where `NCBITaxon:1196545` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0470953` / `Mucor plasmaticus NRRL 2708` and `Go0535962` / `Mucor plasmaticus NRRL 2711`, linked to two native projects and no native analyses.

## Completeness

- Exact StrainInfo has 8 direct records and 19 deposit rows for `NCBITaxon:1196545`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:1196545`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1196545`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
