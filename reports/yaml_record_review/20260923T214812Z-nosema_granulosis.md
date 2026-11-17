# YAML Record Review

- Target: `data/taxa/eukaryota/nosema_granulosis.yaml`
- Taxon: `NCBITaxon:83296` (`Nosema granulosis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:83296`, label `Nosema granulosis`.
- It is grounded exactly under `NCBITaxon:27977` (`Nosema`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Nosema`.

## Validation

- `just validate data/taxa/eukaryota/nosema_granulosis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nitzschia_sigma.yaml data/taxa/eukaryota/niveomyces_insectorum_rcef_264.yaml data/taxa/eukaryota/norrisiella_sphaerica.yaml data/taxa/eukaryota/nosema_granulosis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53395` contains the seeded identifier with reason `attested rule: Nosema granulosis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:12706` matches the YAML identity: parent `NCBITaxon:27977`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:12706` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:43053`, where `NCBITaxon:83296` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0631312` / `Nosema granulosis Ou3-Ou53`, linked to project `Gp0644694` and one native analysis for that project.

## Completeness

- The bounded exact scan found no NCBI type-material rows, no exact StrainInfo rows, and no NCBI merged-ID side rows for `NCBITaxon:83296`; no retained retired old-ID rows were present either.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and checked auxiliary source rows were empty for `NCBITaxon:83296`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact native GOLD organism, project, and analysis rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD side inventories.

## Additional Notes

- None.
