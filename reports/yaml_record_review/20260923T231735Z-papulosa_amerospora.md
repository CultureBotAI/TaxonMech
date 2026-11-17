# YAML Record Review

- Target: `data/taxa/eukaryota/papulosa_amerospora.yaml`
- Taxon: `NCBITaxon:101488` (`Papulosa amerospora`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:101488`, label `Papulosa amerospora`.
- It is grounded exactly under `NCBITaxon:101487` (`Papulosa`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Papulosa`.

## Validation

- `just validate data/taxa/eukaryota/papulosa_amerospora.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/papiliotrema_odontotermitis.yaml data/taxa/eukaryota/papulosa_amerospora.yaml data/taxa/eukaryota/parabodo_caudatus.yaml data/taxa/eukaryota/paracercomonas_sp.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53660` contains the seeded identifier with reason `attested rule: Papulosa amerospora, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:17575` matches the YAML identity: parent `NCBITaxon:101487`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:17575` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:278`, where `NCBITaxon:101488` has `organism_count` 1.
- The native GOLD exact current-taxid scan found no local organism, project, or analysis rows for `NCBITaxon:101488`.

## Completeness

- Exact NCBI type-material, StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:101488`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future source refreshes add non-GOLD evidence for this species.

## Additional Notes

- None.
