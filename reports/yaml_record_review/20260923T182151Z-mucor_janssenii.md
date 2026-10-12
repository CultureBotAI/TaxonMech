# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_janssenii.yaml`
- Taxon: `NCBITaxon:201730` (`Mucor janssenii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:201730`, label `Mucor janssenii`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_janssenii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_intermedius.yaml ... mucor_laxorrhizus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54458` contains the seeded identifier with reason `attested rule: Mucor janssenii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:39809` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, five exact synonyms, and six related synonyms across `Circinella`, `Circinomucor`, and `Mucor` names.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:39809` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:18773`, where `NCBITaxon:201730` has `organism_count` 3.
- Native GOLD has three exact current-taxid organism rows, `Go0470800`, `Go0470951`, and `Go0535944`, linked to three projects; no native analysis row linked to those projects.
- A complete `grep` scan of `data/raw/ncbi_type_material.tsv` found ten `NCBITaxon:201730` type-material rows for the current-name neotype cultures plus the `Mucor kurssanovii` and `Mucor tenellus` holotype cultures.

## Completeness

- Exact StrainInfo has 24 direct records and 46 deposit rows for `NCBITaxon:201730`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:201730`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:1392548` and `NCBITaxon:2572685` into this current taxon.
- The bounded retained-row scan found no local retired-ID provenance, so the YAML's empty `replaces` list is consistent.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- Two native GOLD organism rows use exact synonym `Mucor circinelloides f. janssenii`; one uses the current name `Mucor janssenii`.
