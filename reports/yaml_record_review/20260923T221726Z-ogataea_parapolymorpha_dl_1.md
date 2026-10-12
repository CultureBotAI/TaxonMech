# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_parapolymorpha_dl_1.yaml`
- Taxon: `NCBITaxon:871575` (`Ogataea parapolymorpha DL-1`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:871575`, label `Ogataea parapolymorpha DL-1`.
- It is grounded exactly under `NCBITaxon:1005962` (`Ogataea parapolymorpha`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Ogataea parapolymorpha`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_parapolymorpha_dl_1.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_paraovalis.yaml data/taxa/eukaryota/ogataea_parapolymorpha_dl_1.yaml data/taxa/eukaryota/ogataea_philodendri.yaml data/taxa/eukaryota/ogataea_piceae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56808` contains the seeded identifier with reason `attested rule: Ogataea parapolymorpha DL-1, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:184956` matches the YAML identity: parent `NCBITaxon:1005962`, rank `STRAIN`, two exact synonyms, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:184956` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:43623`, where `NCBITaxon:871575` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0008917` / `Ogataea parapolymorpha DL-1`, linked to projects `Gp0008917` and `Gp0008949`; one native analysis row links through `Gp0008917`.

## Completeness

- The parent species `NCBITaxon:1005962` is reviewed separately; this record correctly scopes source attestations to the exact DL-1 strain taxon.
- Exact NCBI type-material, NCBI merged-ID, BacDive, StrainInfo, generated strain, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:871575`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD side inventories.

## Additional Notes

- None.
