# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_ctenidius.yaml`
- Taxon: `NCBITaxon:101144` (`Mucor ctenidius`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:101144`, label `Mucor ctenidius`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_ctenidius.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_circinelloides.yaml ... mucor_durus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53655` contains the seeded identifier with reason `attested rule: Mucor ctenidius, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:17456` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, exact synonyms `Backusella ctenidia` and `Thamnidium ctenidium`, and three related basionym or authority-bearing synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:17456` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:266`, where `NCBITaxon:101144` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0470778` / `Mucor ctenidius NRRL 2929` and `Go0527538` / `Backusella ctenidia NRRL 6239`, linked to four projects; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:935-936` has the `CBS 293.66` and `CBS:293.66` culture-from-isotype aliases under synonym `Thamnidium ctenidium`.

## Completeness

- Exact StrainInfo has two direct records and ten deposit rows for `NCBITaxon:101144`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:101144`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:101144`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- One native GOLD organism row uses current-name `Mucor ctenidius`; the other uses exact synonym `Backusella ctenidia`.
