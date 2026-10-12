# YAML Record Review

- Target: `data/taxa/eukaryota/nitzschia_fonticola.yaml`
- Taxon: `NCBITaxon:303406` (`Nitzschia fonticola`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:303406`, label `Nitzschia fonticola`.
- It is grounded exactly under `NCBITaxon:2857` (`Nitzschia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Nitzschia`.

## Validation

- `just validate data/taxa/eukaryota/nitzschia_fonticola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nitzschia_fonticola.yaml data/taxa/eukaryota/nitzschia_inconspicua.yaml data/taxa/eukaryota/nitzschia_palea.yaml data/taxa/eukaryota/nitzschia_pellucida.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55092` contains the seeded identifier with reason `attested rule: Nitzschia fonticola, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:62119` matches the YAML identity: parent `NCBITaxon:2857`, rank `SPECIES`, exact synonym `Nitzschia palea var. fonticola`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:62119` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:30380`, where `NCBITaxon:303406` has `organism_count` 1.
- Exact scans of the current native GOLD JSONL catalogs found no current exact organism, project, or analysis rows for `NCBITaxon:303406`.

## Completeness

- Exact StrainInfo side inventory found 4 direct records and 4 deposit entries: `DCG 0012`, `DCG 0213`, `DCG 0010`, and `DCG 0280`.
- Exact NCBI type-material, BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:303406`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs can differ from that generated aggregate and do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
