# YAML Record Review

- Target: `data/taxa/eukaryota/parasitella_parasitica.yaml`
- Taxon: `NCBITaxon:35722` (`Parasitella parasitica`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:35722`, label `Parasitella parasitica`.
- It is grounded exactly under `NCBITaxon:35721` (`Parasitella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Parasitella`.

## Validation

- `just validate data/taxa/eukaryota/parasitella_parasitica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/parapyrenis_maritima.yaml data/taxa/eukaryota/parasitella_parasitica.yaml data/taxa/eukaryota/parastagonospora_nodorum.yaml data/taxa/eukaryota/parastagonospora_nodorum_sn4.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52295` contains the seeded identifier with reason `attested rule: Parasitella parasitica, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:3934` matches the YAML identity: parent `NCBITaxon:35721`, rank `SPECIES`, one exact synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:3934` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33120`, where `NCBITaxon:35722` has `organism_count` 5.
- The native GOLD exact current-taxid scan found five organism rows, seven project rows, and one analysis row for `NCBITaxon:35722`.
- Exact StrainInfo side evidence has seven direct `NCBITaxon:35722` records and 24 deposits across those records.

## Completeness

- BacDive, NCBI type material, retained retired old-ID, merged-ID side inventory, checked auxiliary source rows, and StrainInfo assembly rows were empty for `NCBITaxon:35722`.
- `data/straininfo/related_records.tsv.gz` contains two exact rows for `NCBITaxon:35722`, both linking `straininfo.strain:389485` / deposit `straininfo.deposit:179678` to `kgmicrobe.strain:bacdive_16067`; no BacDive strain rows were filed under the target taxon or its descendants, so the seed generator had no BacDive entries to decorate and `strain_count: 0` is consistent.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive rows under this taxon or its descendants.

## Additional Notes

- None.
