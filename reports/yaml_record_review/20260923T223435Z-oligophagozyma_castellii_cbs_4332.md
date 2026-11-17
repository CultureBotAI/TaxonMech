# YAML Record Review

- Target: `data/taxa/eukaryota/oligophagozyma_castellii_cbs_4332.yaml`
- Taxon: `NCBITaxon:1279086` (`Oligophagozyma castellii CBS 4332`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:1279086`, label `Oligophagozyma castellii CBS 4332`.
- It is grounded exactly under `NCBITaxon:51914` (`Oligophagozyma castellii`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Oligophagozyma castellii`.

## Validation

- `just validate data/taxa/eukaryota/oligophagozyma_castellii_cbs_4332.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/oligophagozyma_castellii.yaml data/taxa/eukaryota/oligophagozyma_castellii_cbs_4332.yaml data/taxa/eukaryota/olpidium_bornovanus.yaml data/taxa/eukaryota/olpidium_sp.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58873` contains the seeded identifier with reason `attested rule: Oligophagozyma castellii CBS 4332, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:298698` matches the YAML identity: parent `NCBITaxon:51914`, rank `STRAIN`, two exact synonyms, no related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:298698` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:6507`, where `NCBITaxon:1279086` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0041973` / `Candida castellii CBS 4332`, linked to project `Gp0041973` and one analysis row via that project.

## Completeness

- Exact StrainInfo, NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1279086`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this strain taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD or other exact side inventories.

## Additional Notes

- None.
