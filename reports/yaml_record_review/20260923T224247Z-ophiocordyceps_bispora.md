# YAML Record Review

- Target: `data/taxa/eukaryota/ophiocordyceps_bispora.yaml`
- Taxon: `NCBITaxon:61658` (`Ophiocordyceps bispora`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:61658`, label `Ophiocordyceps bispora`.
- It is grounded exactly under `NCBITaxon:474995` (`Ophiocordyceps`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Ophiocordyceps`.

## Validation

- `just validate data/taxa/eukaryota/ophiocordyceps_bispora.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/ophioceras_dolichostomum.yaml data/taxa/eukaryota/ophiocordyceps_australis.yaml data/taxa/eukaryota/ophiocordyceps_bispora.yaml data/taxa/eukaryota/ophiocordyceps_camponoti_floridani.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53042` contains the seeded identifier with reason `attested rule: Ophiocordyceps bispora, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:7817` matches the YAML identity: parent `NCBITaxon:474995`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:7817` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:39899`, where `NCBITaxon:61658` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0384401` / `Ophiocordyceps bispora ERS1123077`, linked to project `Gp0235496` and one analysis row via that project.

## Completeness

- Exact StrainInfo, NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:61658`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD or other exact side inventories.

## Additional Notes

- None.
