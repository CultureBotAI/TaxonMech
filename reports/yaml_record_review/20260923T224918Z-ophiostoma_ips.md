# YAML Record Review

- Target: `data/taxa/eukaryota/ophiostoma_ips.yaml`
- Taxon: `NCBITaxon:5163` (`Ophiostoma ips`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:5163`, label `Ophiostoma ips`.
- It is grounded exactly under `NCBITaxon:5159` (`Ophiostoma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Ophiostoma`.

## Validation

- `just validate data/taxa/eukaryota/ophiostoma_ips.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ophiocordyceps_unilateralis.yaml data/taxa/eukaryota/ophiognomonia_clavigignenti_juglandacearum.yaml data/taxa/eukaryota/ophiosphaerella_herpotricha.yaml data/taxa/eukaryota/ophiostoma_ips.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:51949` contains the seeded identifier with reason `attested rule: Ophiostoma ips, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2271` matches the YAML identity: parent `NCBITaxon:5159`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2271` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37619`, where `NCBITaxon:5163` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0455119` / `Ophiostoma ips CBS 138721`, linked to project `Gp0323445` and one analysis row via that project.
- Exact StrainInfo side evidence has 41 direct `NCBITaxon:5163` records and 48 deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:5163`; the record correctly has `strain_count: 0`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old ID `NCBITaxon:221238` to `NCBITaxon:5163`, but no retained retired source row generated a YAML `replaces` entry.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD or StrainInfo side inventories.

## Additional Notes

- None.
