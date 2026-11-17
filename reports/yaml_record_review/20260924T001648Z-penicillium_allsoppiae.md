# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_allsoppiae.yaml`
- Taxon: `NCBITaxon:2795747` (`Penicillium allsoppiae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2795747`, label `Penicillium allsoppiae`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_allsoppiae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_allii.yaml data/taxa/eukaryota/penicillium_allsoppiae.yaml data/taxa/eukaryota/penicillium_americanum.yaml data/taxa/eukaryota/penicillium_angulare.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63254` contains the seeded identifier with reason `attested rule: Penicillium allsoppiae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:556151` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, five related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:556151` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:26713`, where `NCBITaxon:2795747` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:2795747`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 12 culture-from-holotype spellings centered on `CBS 138943`, `CV 931`, `DAOM 241348`, and `DTO 182-D5`, plus two holotype spellings centered on `CBS H-22036`.
- Exact StrainInfo side evidence has one direct `NCBITaxon:2795747` record, `siID` 146295 with DOI `10.60712/SI-ID146295.2`, and one deposit.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:2795747`.
- Four merged-ID side rows map old IDs `NCBITaxon:1297651`, `NCBITaxon:1651869`, `NCBITaxon:1651870`, and `NCBITaxon:3080661` to current `NCBITaxon:2795747`; the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
