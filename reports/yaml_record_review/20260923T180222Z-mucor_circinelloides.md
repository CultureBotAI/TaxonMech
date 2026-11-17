# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_circinelloides.yaml`
- Taxon: `NCBITaxon:36080` (`Mucor circinelloides`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:36080`, label `Mucor circinelloides`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_circinelloides.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_circinelloides.yaml ... mucor_durus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52329` contains the seeded identifier with reason `attested rule: Mucor circinelloides, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4066` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, seven exact synonyms, and three related synonyms for `Circinomucor`, `Rhizomucor regularior`, and `Rhizomucor variabilis var. regularior` names.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4066` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33278`, where `NCBITaxon:36080` has `organism_count` 42.
- Exact native GOLD expansion found 42 current-taxid organism rows, 148 rows for projects linked to those organisms, and 14 native analysis rows linked through `AP PROJECT GOLD IDS`.
- A complete scan of `data/raw/ncbi_type_material.tsv` found seven `NCBITaxon:36080` type-material rows: the `CBS 195.68` neotype-culture aliases plus `CBS 384.95`, `CBS:384.95`, `AS Rm 7`, `AS:Rm:7`, and `Rm-7` aliases under synonym `Rhizomucor regularior`.

## Completeness

- Exact StrainInfo has 190 direct records and 243 deposit rows for `NCBITaxon:36080`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:36080`.
- `data/raw/ncbi_merged_ids.tsv` maps four side-inventory old IDs into this current taxon: `NCBITaxon:101506`, `NCBITaxon:1618004`, `NCBITaxon:342806`, and `NCBITaxon:70416`.
- The bounded retained-row scan found no local retired-ID provenance, so the YAML's empty `replaces` list is consistent.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- Native GOLD analysis rows for this taxon are linked through `AP PROJECT GOLD IDS`; the sampled analysis rows left `AP ORGANISM GOLD ID` empty.
