# YAML Record Review

- Target: `data/taxa/eukaryota/odontella_aurita.yaml`
- Taxon: `NCBITaxon:265563` (`Odontella aurita`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:265563`, label `Odontella aurita`.
- It is grounded exactly under `NCBITaxon:2838` (`Odontella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Odontella`.

## Validation

- `just validate data/taxa/eukaryota/odontella_aurita.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/oculimacula_yallundae.yaml data/taxa/eukaryota/odontella_aurita.yaml data/taxa/eukaryota/oehlia_diaphana.yaml data/taxa/eukaryota/ogataea_allantospora.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54885` contains the seeded identifier with reason `attested rule: Odontella aurita, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:54361` matches the YAML identity: parent `NCBITaxon:2838`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:54361` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:24376`, where `NCBITaxon:265563` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0368760` / `Odontella aurita 1302-5`; the local exact native-GOLD scan found no linked project or analysis rows.

## Completeness

- Exact StrainInfo side inventory found 6 direct records and 6 deposit groups, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:265563`.
- Exact NCBI type-material, NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:265563`; the record correctly has `strain_count: 0`.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs can differ from that generated aggregate and do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
