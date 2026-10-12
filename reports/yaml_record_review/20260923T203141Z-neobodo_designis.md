# YAML Record Review

- Target: `data/taxa/eukaryota/neobodo_designis.yaml`
- Taxon: `NCBITaxon:312471` (`Neobodo designis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:312471`, label `Neobodo designis`.
- It is grounded exactly under `NCBITaxon:312470` (`Neobodo`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Neobodo`.

## Validation

- `just validate data/taxa/eukaryota/neobodo_designis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neoaidaea_tothii.yaml data/taxa/eukaryota/neobodo_designis.yaml data/taxa/eukaryota/neobodo_saliens.yaml data/taxa/eukaryota/neoboletus_brunneissimus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55144` contains the seeded identifier with reason `attested rule: Neobodo designis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:63919` matches the YAML identity: parent `NCBITaxon:312470`, rank `SPECIES`, three synonyms, and genetic code `1`.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:63919` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:31531`, where `NCBITaxon:312471` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0368751` / `Neobodo designis CCAP 1951/1`.
- No native GOLD project or analysis rows were found for `Go0368751`.

## Completeness

- Exact StrainInfo side inventory found two direct records, `SI-ID345626` and `SI-ID350839`, carrying deposits `CCAP 1951/1` and `ATCC 50090`.
- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:312471`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old ID `NCBITaxon:140237`; it was not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:312471`; the exact StrainInfo side inventory did not materialize local strain rows.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories, or if the side-inventory merged ID becomes a retained retired row.

## Additional Notes

- None.
