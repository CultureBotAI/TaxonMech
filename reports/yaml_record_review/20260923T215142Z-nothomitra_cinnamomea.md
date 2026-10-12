# YAML Record Review

- Target: `data/taxa/eukaryota/nothomitra_cinnamomea.yaml`
- Taxon: `NCBITaxon:1167255` (`Nothomitra cinnamomea`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1167255`, label `Nothomitra cinnamomea`.
- It is grounded exactly under `NCBITaxon:1167256` (`Nothomitra`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Nothomitra`.

## Validation

- `just validate data/taxa/eukaryota/nothomitra_cinnamomea.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nothofagozyma_chilensis.yaml data/taxa/eukaryota/nothomitra_cinnamomea.yaml data/taxa/eukaryota/nothophoma_quercina.yaml data/taxa/eukaryota/obba_rivulosa.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58090` contains the seeded identifier with reason `attested rule: Nothomitra cinnamomea, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:257803` matches the YAML identity: parent `NCBITaxon:1167256`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:257803` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:3558`, where `NCBITaxon:1167255` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0677501` / `Nothomitra cinnamomea HN9HV3GS65`, linked to project `Gp0779319` and one native analysis for that project.

## Completeness

- The bounded exact scan found no NCBI type-material rows, no exact StrainInfo rows, and no NCBI merged-ID side rows for `NCBITaxon:1167255`; no retained retired old-ID rows were present either.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and checked auxiliary source rows were empty for `NCBITaxon:1167255`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact native GOLD organism, project, and analysis rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD side inventories.

## Additional Notes

- None.
