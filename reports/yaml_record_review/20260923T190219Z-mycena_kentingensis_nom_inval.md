# YAML Record Review

- Target: `data/taxa/eukaryota/mycena_kentingensis_nom_inval.yaml`
- Taxon: `NCBITaxon:1325293` (`Mycena kentingensis (nom. inval.)`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1325293`, label `Mycena kentingensis (nom. inval.)`.
- It is grounded exactly under `NCBITaxon:2631581` (`unclassified Mycena`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `unclassified Mycena`.

## Validation

- `just validate data/taxa/eukaryota/mycena_kentingensis_nom_inval.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycena_haematopus.yaml data/taxa/eukaryota/mycena_kentingensis_nom_inval.yaml data/taxa/eukaryota/mycena_latifolia.yaml data/taxa/eukaryota/mycena_leptocephala.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59470` contains the seeded identifier with reason `attested rule: Mycena kentingensis (nom. inval.), 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:316162` matches the YAML identity: parent `NCBITaxon:2631581`, rank `SPECIES`, one exact synonym, and two related synonyms.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:316162` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:7924`, where `NCBITaxon:1325293` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0632078` / `Mycena kentingensis 111111Pingtung`, linked to native project `Gp0645899` and one native analysis for the same project.

## Completeness

- Exact StrainInfo has 0 direct records and 0 deposit rows for `NCBITaxon:1325293`, and no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:1325293`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1325293`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
