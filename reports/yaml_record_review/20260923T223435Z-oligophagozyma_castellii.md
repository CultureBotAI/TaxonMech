# YAML Record Review

- Target: `data/taxa/eukaryota/oligophagozyma_castellii.yaml`
- Taxon: `NCBITaxon:51914` (`Oligophagozyma castellii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:51914`, label `Oligophagozyma castellii`.
- It is grounded exactly under `NCBITaxon:3163254` (`Oligophagozyma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Oligophagozyma`.

## Validation

- `just validate data/taxa/eukaryota/oligophagozyma_castellii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/oligophagozyma_castellii.yaml data/taxa/eukaryota/oligophagozyma_castellii_cbs_4332.yaml data/taxa/eukaryota/olpidium_bornovanus.yaml data/taxa/eukaryota/olpidium_sp.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52841` contains the seeded identifier with reason `attested rule: Oligophagozyma castellii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6524` matches the YAML identity: parent `NCBITaxon:3163254`, rank `SPECIES`, three exact synonyms, four related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6524` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37682`, where `NCBITaxon:51914` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705256` / `Oligophagozyma castellii NRRL Y-17070`, linked to project `Gp0831291`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material has 16 duplicated spelling rows for `Torulopsis castellii`, covering `ATCC 22945`, `BCRC` / `CCRC 22269`, `CBS 4332`, `IFO 10270`, `JCM 9550`, `NRRL Y-17070`, and `UCD 60-67`.
- Exact StrainInfo side inventory found 2 direct records and 13 deposits, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:51914`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:51914`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
