# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_populi_albae.yaml`
- Taxon: `NCBITaxon:550978` (`Ogataea populi-albae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:550978`, label `Ogataea populi-albae`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_populi_albae.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/ogataea_polymorpha.yaml data/taxa/eukaryota/ogataea_populi_albae.yaml data/taxa/eukaryota/ogataea_rishiriensis.yaml data/taxa/eukaryota/ogataea_salicorniae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55975` contains the seeded identifier with reason `attested rule: Ogataea populi-albae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:128592` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, one exact synonym, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:128592` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38548`, where `NCBITaxon:550978` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0517165` / `Ogataea populi-albae NRRL Y-48632`, linked to projects `Gp0441203` and `Gp0780273` and two analysis rows via those projects.

## Completeness

- Exact NCBI type material has 6 duplicated spelling rows for `Ogataea populi-albae`, covering `CBS 11363`, `NCAIM Y.01853`, and `NRRL Y-48632`.
- Exact StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:550978`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or native GOLD side inventories.

## Additional Notes

- None.
