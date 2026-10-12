# YAML Record Review

- Target: `data/taxa/eukaryota/olpidium_bornovanus.yaml`
- Taxon: `NCBITaxon:278681` (`Olpidium bornovanus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:278681`, label `Olpidium bornovanus`.
- It is grounded exactly under `NCBITaxon:70188` (`Olpidium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Olpidium`.

## Validation

- `just validate data/taxa/eukaryota/olpidium_bornovanus.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/oligophagozyma_castellii.yaml data/taxa/eukaryota/oligophagozyma_castellii_cbs_4332.yaml data/taxa/eukaryota/olpidium_bornovanus.yaml data/taxa/eukaryota/olpidium_sp.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54939` contains the seeded identifier with reason `attested rule: Olpidium bornovanus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:56667` matches the YAML identity: parent `NCBITaxon:70188`, rank `SPECIES`, no synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:56667` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:26558`, where `NCBITaxon:278681` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0009557` / `Olpidium bornovanus S191`, linked to projects `Gp0009557` and `Gp0010016`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact StrainInfo, NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:278681`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD or other exact side inventories.

## Additional Notes

- None.
