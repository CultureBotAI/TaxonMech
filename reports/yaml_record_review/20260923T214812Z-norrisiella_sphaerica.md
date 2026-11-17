# YAML Record Review

- Target: `data/taxa/eukaryota/norrisiella_sphaerica.yaml`
- Taxon: `NCBITaxon:552664` (`Norrisiella sphaerica`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:552664`, label `Norrisiella sphaerica`.
- It is grounded exactly under `NCBITaxon:552663` (`Norrisiella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 8 lineage entries from `root` through `Norrisiella`.

## Validation

- `just validate data/taxa/eukaryota/norrisiella_sphaerica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nitzschia_sigma.yaml data/taxa/eukaryota/niveomyces_insectorum_rcef_264.yaml data/taxa/eukaryota/norrisiella_sphaerica.yaml data/taxa/eukaryota/nosema_granulosis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55981` contains the seeded identifier with reason `attested rule: Norrisiella sphaerica, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:129381` matches the YAML identity: parent `NCBITaxon:552663`, rank `SPECIES`, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 8 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:129381` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38609`, where `NCBITaxon:552664` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0368756` / `Norrisiella sphaerica BC52`, with no native project or analysis rows linked to that organism.

## Completeness

- The bounded exact scan found no NCBI type-material rows, no exact StrainInfo rows, and no NCBI merged-ID side rows for `NCBITaxon:552664`; no retained retired old-ID rows were present either.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and checked auxiliary source rows were empty for `NCBITaxon:552664`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact native GOLD organism row did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD side inventories.

## Additional Notes

- None.
