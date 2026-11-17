# YAML Record Review

- Target: `data/taxa/eukaryota/operculomyces_laminatus.yaml`
- Taxon: `NCBITaxon:382552` (`Operculomyces laminatus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:382552`, label `Operculomyces laminatus`.
- It is grounded exactly under `NCBITaxon:1397667` (`Operculomyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Operculomyces`.

## Validation

- `just validate data/taxa/eukaryota/operculomyces_laminatus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/opeltia_flavorubescens.yaml data/taxa/eukaryota/operculomyces_laminatus.yaml data/taxa/eukaryota/ophidiomyces_ophidiicola.yaml data/taxa/eukaryota/ophiobolus_disseminans.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55446` contains the seeded identifier with reason `attested rule: Operculomyces laminatus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:80395` matches the YAML identity: parent `NCBITaxon:1397667`, rank `SPECIES`, no exact synonyms, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:80395` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33930`, where `NCBITaxon:382552` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0111715` / `Operculomyces laminatus JEL223`, linked to projects `Gp0113828` and `Gp0113829`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material has 2 `JEL 223` culture-from-holotype rows for `Operculomyces laminatus`.
- Exact NCBI merged-ID side inventory maps old `NCBITaxon:388811` to `NCBITaxon:382552`, while exact StrainInfo, BacDive, retained retired old-ID, and checked auxiliary source rows were empty.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:382552`; the record correctly has no `replaces` entry and `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, native GOLD, or NCBI merged-ID side inventories.

## Additional Notes

- None.
