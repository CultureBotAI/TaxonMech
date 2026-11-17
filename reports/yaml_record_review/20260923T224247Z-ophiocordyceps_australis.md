# YAML Record Review

- Target: `data/taxa/eukaryota/ophiocordyceps_australis.yaml`
- Taxon: `NCBITaxon:1399860` (`Ophiocordyceps australis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1399860`, label `Ophiocordyceps australis`.
- It is grounded exactly under `NCBITaxon:474995` (`Ophiocordyceps`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Ophiocordyceps`.

## Validation

- `just validate data/taxa/eukaryota/ophiocordyceps_australis.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/ophioceras_dolichostomum.yaml data/taxa/eukaryota/ophiocordyceps_australis.yaml data/taxa/eukaryota/ophiocordyceps_bispora.yaml data/taxa/eukaryota/ophiocordyceps_camponoti_floridani.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59999` contains the seeded identifier with reason `attested rule: Ophiocordyceps australis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:344893` matches the YAML identity: parent `NCBITaxon:474995`, rank `SPECIES`, three exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:344893` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:9570`, where `NCBITaxon:1399860` has `organism_count` 2.
- Native GOLD has 2 exact current-taxid organism rows, `Go0631291` / `Ophiocordyceps australis 1348a` and `Go0631292` / `Ophiocordyceps australis Map64`, with 2 linked projects and 2 linked analyses.

## Completeness

- Exact StrainInfo, NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1399860`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD or other exact side inventories.

## Additional Notes

- None.
