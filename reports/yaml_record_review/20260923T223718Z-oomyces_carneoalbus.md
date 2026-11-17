# YAML Record Review

- Target: `data/taxa/eukaryota/oomyces_carneoalbus.yaml`
- Taxon: `NCBITaxon:1907525` (`Oomyces carneoalbus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1907525`, label `Oomyces carneoalbus`.
- It is grounded exactly under `NCBITaxon:1907524` (`Oomyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Oomyces`.

## Validation

- `just validate data/taxa/eukaryota/oomyces_carneoalbus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/onnia_scaura.yaml data/taxa/eukaryota/onygena_corvina.yaml data/taxa/eukaryota/oomyces_carneoalbus.yaml data/taxa/eukaryota/oosporidium_margaritiferum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61537` contains the seeded identifier with reason `attested rule: Oomyces carneoalbus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:493037` matches the YAML identity: parent `NCBITaxon:1907524`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:493037` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:17264`, where `NCBITaxon:1907525` has `organism_count` 1.
- The local exact native-GOLD scan found no current-taxid organism, project, or analysis rows for `NCBITaxon:1907525`, so the GOLD attestation rests on the transformed GOLD aggregate rather than matching rows in the local native JSONL snapshot.

## Completeness

- Exact StrainInfo, NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1907525`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if a refreshed local native GOLD snapshot materializes exact current-taxid rows for `NCBITaxon:1907525`.

## Additional Notes

- None.
