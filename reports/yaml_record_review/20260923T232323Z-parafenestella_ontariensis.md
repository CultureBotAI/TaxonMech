# YAML Record Review

- Target: `data/taxa/eukaryota/parafenestella_ontariensis.yaml`
- Taxon: `NCBITaxon:2911076` (`Parafenestella ontariensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2911076`, label `Parafenestella ontariensis`.
- It is grounded exactly under `NCBITaxon:2065319` (`Parafenestella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Parafenestella`.

## Validation

- `just validate data/taxa/eukaryota/parafenestella_ontariensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paracorniculantispora_psalliotae.yaml data/taxa/eukaryota/paraeutypella_vitis.yaml data/taxa/eukaryota/parafenestella_ontariensis.yaml data/taxa/eukaryota/paraglomus_brasilianum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63372` contains the seeded identifier with reason `attested rule: Parafenestella ontariensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:570672` matches the YAML identity: parent `NCBITaxon:2065319`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:570672` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:28491`, where `NCBITaxon:2911076` has `organism_count` 2.
- The native GOLD exact current-taxid scan found one organism row, one project row, and one analysis row for strain `EI-6`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 13 type-material spellings for `NCBITaxon:2911076` on lines 139944-139956, spanning culture-from-holotype `BILAS 51517`/`EI-6`, holotype `BILAS 51516`, and isotype `DAOM 984987` spellings.

## Completeness

- Exact StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:2911076`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future source refreshes add local strain evidence for this species.

## Additional Notes

- None.
