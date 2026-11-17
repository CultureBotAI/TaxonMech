# YAML Record Review

- Target: `data/taxa/eukaryota/ophiocordyceps_camponoti_leonardi_nom_inval.yaml`
- Taxon: `NCBITaxon:2039875` (`Ophiocordyceps camponoti-leonardi (nom. inval.)`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2039875`, label `Ophiocordyceps camponoti-leonardi (nom. inval.)`.
- It is grounded exactly under `NCBITaxon:2610867` (`unclassified Ophiocordyceps`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `unclassified Ophiocordyceps`.

## Validation

- `just validate data/taxa/eukaryota/ophiocordyceps_camponoti_leonardi_nom_inval.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ophiocordyceps_camponoti_leonardi_nom_inval.yaml data/taxa/eukaryota/ophiocordyceps_camponoti_rufipedis.yaml data/taxa/eukaryota/ophiocordyceps_camponoti_saundersi_nom_inval.yaml data/taxa/eukaryota/ophiocordyceps_sinensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62141` contains the seeded identifier with reason `attested rule: Ophiocordyceps camponoti-leonardi (nom. inval.), 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:513112` matches the YAML identity: parent `NCBITaxon:2610867`, rank `SPECIES`, exact synonym `Ophiocordyceps camponoti-leonardi`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:513112` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:19318`, where `NCBITaxon:2039875` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0631756` / `Ophiocordyceps camponoti-leonardi BCC 80369`, linked to project `Gp0645358` and one analysis row via that project.

## Completeness

- Exact NCBI type-material, StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:2039875`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD side inventories.

## Additional Notes

- None.
