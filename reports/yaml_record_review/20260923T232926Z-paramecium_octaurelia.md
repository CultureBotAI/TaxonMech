# YAML Record Review

- Target: `data/taxa/eukaryota/paramecium_octaurelia.yaml`
- Taxon: `NCBITaxon:43137` (`Paramecium octaurelia`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:43137`, label `Paramecium octaurelia`.
- It is grounded exactly under `NCBITaxon:5884` (`Paramecium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `6`.
- The YAML carries 11 lineage entries from `root` through `Paramecium`.

## Validation

- `just validate data/taxa/eukaryota/paramecium_octaurelia.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/paramecium_biaurelia.yaml data/taxa/eukaryota/paramecium_caudatum.yaml data/taxa/eukaryota/paramecium_octaurelia.yaml data/taxa/eukaryota/paramecium_pentaurelia.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52536` contains the seeded identifier with reason `attested rule: Paramecium octaurelia, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:5203` matches the YAML identity: parent `NCBITaxon:5884`, rank `SPECIES`, one exact synonym, one related synonym, genetic code `6`, and the 2026-09-13 taxonomy snapshot.
- All 11 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:5203` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:35314`, where `NCBITaxon:43137` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, one project row, and one analysis row for `GCA_905182995.1`.
- Exact StrainInfo side evidence has nine direct `NCBITaxon:43137` records and nine deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:43137`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains one old ID that now points at `NCBITaxon:43137`: `NCBITaxon:42406`; it is not retained as a retired taxon, so the YAML correctly has no `replaces` entry.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
