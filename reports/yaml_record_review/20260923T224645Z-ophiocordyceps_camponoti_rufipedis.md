# YAML Record Review

- Target: `data/taxa/eukaryota/ophiocordyceps_camponoti_rufipedis.yaml`
- Taxon: `NCBITaxon:2004952` (`Ophiocordyceps camponoti-rufipedis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2004952`, label `Ophiocordyceps camponoti-rufipedis`.
- It is grounded exactly under `NCBITaxon:474995` (`Ophiocordyceps`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Ophiocordyceps`.

## Validation

- `just validate data/taxa/eukaryota/ophiocordyceps_camponoti_rufipedis.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/ophiocordyceps_camponoti_leonardi_nom_inval.yaml data/taxa/eukaryota/ophiocordyceps_camponoti_rufipedis.yaml data/taxa/eukaryota/ophiocordyceps_camponoti_saundersi_nom_inval.yaml data/taxa/eukaryota/ophiocordyceps_sinensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61839` contains the seeded identifier with reason `attested rule: Ophiocordyceps camponoti-rufipedis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:508880` matches the YAML identity: parent `NCBITaxon:474995`, rank `SPECIES`, no exact synonyms, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:508880` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:18500`, where `NCBITaxon:2004952` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0631293` / `Ophiocordyceps camponoti-rufipedis Map16`, linked to project `Gp0644675` and one analysis row via that project.

## Completeness

- Exact NCBI type-material, StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:2004952`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD side inventories.

## Additional Notes

- None.
