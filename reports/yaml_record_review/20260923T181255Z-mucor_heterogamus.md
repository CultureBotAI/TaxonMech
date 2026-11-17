# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_heterogamus.yaml`
- Taxon: `NCBITaxon:101122` (`Mucor heterogamus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:101122`, label `Mucor heterogamus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_heterogamus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_griseocyanus.yaml ... mucor_hiemalis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53643` contains the seeded identifier with reason `attested rule: Mucor heterogamus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:17436` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, exact `Mucor heterogamus` and `Zygorhynchus heterogamus` variety synonyms, and related synonym `Mucor heterogamus Vuill., 1887`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:17436` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:254`, where `NCBITaxon:101122` has `organism_count` 3.
- Native GOLD has three exact current-taxid organism rows, `Go0118600`, `Go0470921`, and `Go0527664`, linked to four projects; no native analysis row linked to those projects.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:101122` type-material rows.

## Completeness

- Exact StrainInfo has 15 direct records and 20 deposit rows for `NCBITaxon:101122`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:101122`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old ID `NCBITaxon:1385673` into this current taxon.
- The bounded retained-row scan found no local retired-ID provenance, so the YAML's empty `replaces` list is consistent.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- Native GOLD contains one current-name organism row and two `Zygorhynchus heterogamus` synonym-bearing organism rows.
