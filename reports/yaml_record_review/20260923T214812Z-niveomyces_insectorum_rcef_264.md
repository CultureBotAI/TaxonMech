# YAML Record Review

- Target: `data/taxa/eukaryota/niveomyces_insectorum_rcef_264.yaml`
- Taxon: `NCBITaxon:1081102` (`Niveomyces insectorum RCEF 264`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:1081102`, label `Niveomyces insectorum RCEF 264`.
- It is grounded exactly under `NCBITaxon:150359` (`Niveomyces insectorum`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Niveomyces insectorum`.

## Validation

- `just validate data/taxa/eukaryota/niveomyces_insectorum_rcef_264.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nitzschia_sigma.yaml data/taxa/eukaryota/niveomyces_insectorum_rcef_264.yaml data/taxa/eukaryota/norrisiella_sphaerica.yaml data/taxa/eukaryota/nosema_granulosis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57555` contains the seeded identifier with reason `attested rule: Niveomyces insectorum RCEF 264, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:232194` matches the YAML identity: parent `NCBITaxon:150359`, rank `STRAIN`, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:232194` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:1510`, where `NCBITaxon:1081102` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0039314` / `Sporothrix insectorum RCEF 264`, linked to project `Gp0039314` and one native analysis for that project.

## Completeness

- The bounded exact scan found no NCBI type-material rows, no exact StrainInfo rows, and no NCBI merged-ID side rows for `NCBITaxon:1081102`; no retained retired old-ID rows were present either.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and checked auxiliary source rows were empty for `NCBITaxon:1081102`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact native GOLD organism, project, and analysis rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD side inventories.

## Additional Notes

- None.
