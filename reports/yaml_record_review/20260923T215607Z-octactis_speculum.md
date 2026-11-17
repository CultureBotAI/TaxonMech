# YAML Record Review

- Target: `data/taxa/eukaryota/octactis_speculum.yaml`
- Taxon: `NCBITaxon:3111310` (`Octactis speculum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:3111310`, label `Octactis speculum`.
- It is grounded exactly under `NCBITaxon:3095340` (`Octactis`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Octactis`.

## Validation

- `just validate data/taxa/eukaryota/octactis_speculum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/obelidium_mucronatum.yaml data/taxa/eukaryota/ochromonadaceae_sp_ccmp2298.yaml data/taxa/eukaryota/ochromonas_sp_ccmp1393.yaml data/taxa/eukaryota/octactis_speculum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63556` contains the seeded identifier with reason `attested rule: Octactis speculum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:600102` matches the YAML identity: parent `NCBITaxon:3095340`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:600102` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:31393`, where `NCBITaxon:3111310` has `organism_count` 1.
- The local exact current-taxid native-GOLD scan found no organism, project, or analysis rows for `NCBITaxon:3111310`; the YAML has only the retained GOLD aggregate attestation.

## Completeness

- `data/raw/ncbi_merged_ids.tsv:72214` maps side-inventory old ID `NCBITaxon:35687` into `NCBITaxon:3111310`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
- Exact NCBI type-material, BacDive, generated raw strain rows, exact StrainInfo, generated StrainInfo target rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:3111310`; the record correctly has `strain_count: 0`.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs can differ from that generated aggregate and do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD side inventories.

## Additional Notes

- None.
