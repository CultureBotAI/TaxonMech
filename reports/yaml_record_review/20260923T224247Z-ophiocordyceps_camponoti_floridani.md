# YAML Record Review

- Target: `data/taxa/eukaryota/ophiocordyceps_camponoti_floridani.yaml`
- Taxon: `NCBITaxon:2030778` (`Ophiocordyceps camponoti-floridani`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2030778`, label `Ophiocordyceps camponoti-floridani`.
- It is grounded exactly under `NCBITaxon:474995` (`Ophiocordyceps`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Ophiocordyceps`.

## Validation

- `just validate data/taxa/eukaryota/ophiocordyceps_camponoti_floridani.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ophioceras_dolichostomum.yaml data/taxa/eukaryota/ophiocordyceps_australis.yaml data/taxa/eukaryota/ophiocordyceps_bispora.yaml data/taxa/eukaryota/ophiocordyceps_camponoti_floridani.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62093` contains the seeded identifier with reason `attested rule: Ophiocordyceps camponoti-floridani, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:512287` matches the YAML identity: parent `NCBITaxon:474995`, rank `SPECIES`, no exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:512287` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:19147`, where `NCBITaxon:2030778` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0631361` / `Ophiocordyceps camponoti-floridani EC05`, linked to project `Gp0644762` and one analysis row via that project.

## Completeness

- Exact NCBI type material has one `INPA:274575` holotype row for `Ophiocordyceps camponoti-floridani`.
- Exact StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:2030778`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or native GOLD side inventories.

## Additional Notes

- None.
