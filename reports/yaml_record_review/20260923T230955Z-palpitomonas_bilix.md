# YAML Record Review

- Target: `data/taxa/eukaryota/palpitomonas_bilix.yaml`
- Taxon: `NCBITaxon:652834` (`Palpitomonas bilix`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:652834`, label `Palpitomonas bilix`.
- It is grounded exactly under `NCBITaxon:759891` (`Palpitomonas`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries five lineage entries from `root` through `Palpitomonas`.

## Validation

- `just validate data/taxa/eukaryota/palpitomonas_bilix.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/palpitomonas_bilix.yaml data/taxa/eukaryota/panaeolus_cyanescens.yaml data/taxa/eukaryota/panaeolus_papilionaceus.yaml data/taxa/eukaryota/pandora_neoaphidis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56248` contains the seeded identifier with reason `attested rule: Palpitomonas bilix, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:150992` matches the YAML identity: parent `NCBITaxon:759891`, rank `SPECIES`, one exact synonym, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All five YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:150992` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40504`, where `NCBITaxon:652834` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0368773` / `Palpitomonas bilix NIES-2562`, and no linked project or analysis rows.

## Completeness

- Exact NCBI type-material, StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:652834`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD side inventories.

## Additional Notes

- None.
