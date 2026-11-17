# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_annulatum.yaml`
- Taxon: `NCBITaxon:1295614` (`Penicillium annulatum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1295614`, label `Penicillium annulatum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_annulatum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/penicillium_annulatum.yaml data/taxa/eukaryota/penicillium_antarcticum.yaml data/taxa/eukaryota/penicillium_anthracinoglaciei.yaml data/taxa/eukaryota/penicillium_aotearoae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58975` contains the seeded identifier with reason `attested rule: Penicillium annulatum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:304948` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:304948` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:6958`, where `NCBITaxon:1295614` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:1295614`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found four culture-from-holotype spellings centered on `CBS 135126` and `DTO 180-G7`, two holotype spellings centered on `CBS H-21333`, and five type-material spellings centered on `CV 37`.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, exact StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:1295614`.
- With no BacDive or StrainInfo exact matches, there were no generated rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
