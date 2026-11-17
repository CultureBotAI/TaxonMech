# YAML Record Review

- Target: `data/taxa/eukaryota/parapyrenis_maritima.yaml`
- Taxon: `NCBITaxon:2081591` (`Parapyrenis maritima`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2081591`, label `Parapyrenis maritima`.
- It is grounded exactly under `NCBITaxon:2081589` (`Parapyrenis`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Parapyrenis`.

## Validation

- `just validate data/taxa/eukaryota/parapyrenis_maritima.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/parapyrenis_maritima.yaml data/taxa/eukaryota/parasitella_parasitica.yaml data/taxa/eukaryota/parastagonospora_nodorum.yaml data/taxa/eukaryota/parastagonospora_nodorum_sn4.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62282` contains the seeded identifier with reason `attested rule: Parapyrenis maritima, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:517668` matches the YAML identity: parent `NCBITaxon:2081589`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:517668` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:19918`, where `NCBITaxon:2081591` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, `Go0580373`, and two project rows for `NCBITaxon:2081591`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two holotype spellings, `CBS 538.93` and `CBS:538.93`, at lines 83313-83314.
- Exact StrainInfo side evidence has one direct `NCBITaxon:2081591` record, `siID` 172662 with DOI `10.60712/SI-ID172662.1`, and one non-type deposit, `CBS 538.93`.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:2081591`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
