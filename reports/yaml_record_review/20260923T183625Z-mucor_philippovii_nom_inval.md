# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_philippovii_nom_inval.yaml`
- Taxon: `NCBITaxon:2045276` (`Mucor philippovii (nom. inval.)`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2045276`, label `Mucor philippovii (nom. inval.)`.
- It is grounded exactly under `NCBITaxon:2621539` (`unclassified Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `unclassified Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_philippovii_nom_inval.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_philippovii_nom_inval.yaml ... mucor_plumbeus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62172` contains the seeded identifier with reason `attested rule: Mucor philippovii (nom. inval.), 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:513568` matches the YAML identity: parent `NCBITaxon:2621539`, rank `SPECIES`, exact synonym `Mucor philippovii`, and related synonym `Mucor philippovii Naumov, 1935`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:513568` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:19440`, where `NCBITaxon:2045276` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0402581` / `Mucor philippovi NRRL 3036`, linked to project `Gp0290206`; no native analysis row linked to that project.

## Completeness

- The bounded scan found no exact type-material, BacDive, StrainInfo, generated raw strain, generated StrainInfo, or auxiliary source rows for `NCBITaxon:2045276`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:2045276`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if additional StrainInfo, BacDive, or generated strain evidence is added for this taxon.

## Additional Notes

- None.
