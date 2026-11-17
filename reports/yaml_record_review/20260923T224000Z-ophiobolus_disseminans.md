# YAML Record Review

- Target: `data/taxa/eukaryota/ophiobolus_disseminans.yaml`
- Taxon: `NCBITaxon:1469910` (`Ophiobolus disseminans`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1469910`, label `Ophiobolus disseminans`.
- It is grounded exactly under `NCBITaxon:45294` (`Ophiobolus`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Ophiobolus`.

## Validation

- `just validate data/taxa/eukaryota/ophiobolus_disseminans.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/opeltia_flavorubescens.yaml data/taxa/eukaryota/operculomyces_laminatus.yaml data/taxa/eukaryota/ophidiomyces_ophidiicola.yaml data/taxa/eukaryota/ophiobolus_disseminans.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60232` contains the seeded identifier with reason `attested rule: Ophiobolus disseminans, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:375372` matches the YAML identity: parent `NCBITaxon:45294`, rank `SPECIES`, no exact synonyms, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:375372` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:11313`, where `NCBITaxon:1469910` has `organism_count` 2.
- Native GOLD has one exact current-taxid organism row, `Go0036265` / `Ophiobolus disseminans CBS 113818`, linked to projects `Gp0036265` and `Gp0036266` and one analysis row via `Gp0036265`.

## Completeness

- Exact NCBI type material has 8 culture-from-epitype rows for `KUMCC 17-0162` and `MFLUCC 17-1787`, plus 4 `MFLU 15-2257` epitype spellings.
- Exact StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1469910`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or native GOLD side inventories.

## Additional Notes

- None.
