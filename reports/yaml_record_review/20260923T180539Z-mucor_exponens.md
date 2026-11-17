# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_exponens.yaml`
- Taxon: `NCBITaxon:91643` (`Mucor exponens`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:91643`, label `Mucor exponens`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_exponens.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_exponens.yaml ... mucor_fragilis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53522` contains the seeded identifier with reason `attested rule: Mucor exponens, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:14833` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, exact `Zygorhynchus exponens` synonyms, and related synonym `Zygorhynchus exponens Burgeff, 1924`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:14833` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:44472`, where `NCBITaxon:91643` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0456198` / `Zygorhynchus exponens NRRL 1492` and `Go0470794` / `Zygorhynchus exponens var. smithii NRRL 2572`, linked to projects `Gp0325208` and `Gp0345282`; no native analysis row linked to those projects.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:91643` type-material rows.

## Completeness

- Exact StrainInfo has 14 direct records and 30 deposit rows for `NCBITaxon:91643`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:91643`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:1196574` and `NCBITaxon:1196575` into this current taxon.
- The bounded retained-row scan found no local retired-ID provenance, so the YAML's empty `replaces` list is consistent.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- Native GOLD uses synonym-bearing `Zygorhynchus exponens` names for both exact current-taxid organism rows.
