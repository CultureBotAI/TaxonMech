# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_foenicola_nom_inval.yaml`
- Taxon: `NCBITaxon:2512244` (`Mucor foenicola (nom. inval.)`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2512244`, label `Mucor foenicola (nom. inval.)`.
- It is grounded exactly under `NCBITaxon:2621539` (`unclassified Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `unclassified Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_foenicola_nom_inval.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_exponens.yaml ... mucor_fragilis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62755` contains the seeded identifier with reason `attested rule: Mucor foenicola (nom. inval.), 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:528993` matches the YAML identity: parent `NCBITaxon:2621539`, rank `SPECIES`, exact synonym `Mucor foenicola Naumov, 1935`, and no related synonyms.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:528993` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:22878`, where `NCBITaxon:2512244` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0456303` / `Mucor foenicola NRRL A-10991`, linked to project `Gp0325313`; no native analysis row linked to that project.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:2512244` type-material rows.

## Completeness

- Exact StrainInfo direct and deposit rows were empty for `NCBITaxon:2512244`.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:2512244`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:2512244`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strain rows or an analysis row for the exact native GOLD project.

## Additional Notes

- The `nom. inval.` qualifier and `unclassified Mucor` parent are both present in NCBI and reproduced consistently by the generated record.
