# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_griseocyanus.yaml`
- Taxon: `NCBITaxon:928730` (`Mucor griseocyanus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:928730`, label `Mucor griseocyanus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_griseocyanus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_griseocyanus.yaml ... mucor_hiemalis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56925` contains the seeded identifier with reason `attested rule: Mucor griseocyanus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:195496` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, exact synonym `Mucor circinelloides f. griseocyanus`, and two related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:195496` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:44598`, where `NCBITaxon:928730` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0527631` / `Mucor griseocyanus NRRL 1413` and `Go0535982` / `Mucor circinelloides f. griseocyanus NRRL 3622`, linked to two projects; no native analysis row linked to those projects.
- A complete scan of `data/raw/ncbi_type_material.tsv` found six culture-from-epitype aliases for `ATCC 22363`, `CBS 116.08`, and `NRRL A-7420`.

## Completeness

- Exact StrainInfo has 20 direct records and 28 deposit rows for `NCBITaxon:928730`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:928730`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:928730`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- One native GOLD row uses the current name and one uses exact synonym `Mucor circinelloides f. griseocyanus`.
