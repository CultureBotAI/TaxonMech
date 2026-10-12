# YAML Record Review

- Target: `data/taxa/eukaryota/papiliotrema_odontotermitis.yaml`
- Taxon: `NCBITaxon:1857662` (`Papiliotrema odontotermitis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1857662`, label `Papiliotrema odontotermitis`.
- It is grounded exactly under `NCBITaxon:189450` (`Papiliotrema`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Papiliotrema`.

## Validation

- `just validate data/taxa/eukaryota/papiliotrema_odontotermitis.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/papiliotrema_odontotermitis.yaml data/taxa/eukaryota/papulosa_amerospora.yaml data/taxa/eukaryota/parabodo_caudatus.yaml data/taxa/eukaryota/paracercomonas_sp.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61372` contains the seeded identifier with reason `attested rule: Papiliotrema odontotermitis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:485651` matches the YAML identity: parent `NCBITaxon:189450`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:485651` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:16582`, where `NCBITaxon:1857662` has `organism_count` 3.
- The native GOLD exact current-taxid scan found three organism rows for strains `OO5`, `DSM 100791`, and `CBS 14181`; it found no linked project or analysis rows.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two holotype spellings for `NCBITaxon:1857662` on lines 65312-65313: `DSM 100791` and `DSM:100791`.
- Exact StrainInfo side evidence has one direct `NCBITaxon:1857662` record with one type-strain deposit, `DSM 100791`.

## Completeness

- Exact BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1857662`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
