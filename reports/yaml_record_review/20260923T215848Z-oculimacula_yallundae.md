# YAML Record Review

- Target: `data/taxa/eukaryota/oculimacula_yallundae.yaml`
- Taxon: `NCBITaxon:86028` (`Oculimacula yallundae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:86028`, label `Oculimacula yallundae`.
- It is grounded exactly under `NCBITaxon:228665` (`Oculimacula`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Oculimacula`.

## Validation

- `just validate data/taxa/eukaryota/oculimacula_yallundae.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/oculimacula_yallundae.yaml data/taxa/eukaryota/odontella_aurita.yaml data/taxa/eukaryota/oehlia_diaphana.yaml data/taxa/eukaryota/ogataea_allantospora.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53433` contains the seeded identifier with reason `attested rule: Oculimacula yallundae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:13302` matches the YAML identity: parent `NCBITaxon:228665`, rank `SPECIES`, six exact synonyms, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:13302` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:43354`, where `NCBITaxon:86028` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0021140` / `Pseudocercosporella herpotrichoides CBS 494.80`, linked to project `Gp0021140`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material is limited to four `Tapesia yallundae` designations: `CBS 110665`, `CBS:110665`, `K(M)233697`, and `K(M):233697`.
- Exact StrainInfo side inventory found 29 direct records and 30 deposit groups, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:86028`.
- `data/raw/ncbi_merged_ids.tsv:24890` maps side-inventory old ID `NCBITaxon:170078` into `NCBITaxon:86028`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
- Exact BacDive and checked auxiliary source rows were empty for `NCBITaxon:86028`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
