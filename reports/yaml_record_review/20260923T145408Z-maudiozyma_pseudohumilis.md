# YAML Record Review: Maudiozyma pseudohumilis

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/maudiozyma_pseudohumilis.yaml`
- Started UTC: 2026-09-23T14:54:08Z
- Finished UTC: 2026-09-23T14:54:08Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:640839`
- Label: `Maudiozyma pseudohumilis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/maudiozyma_pseudohumilis.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/maudiozyma_pseudohumilis.yaml data/taxa/eukaryota/maudiozyma_saulgeensis.yaml data/taxa/eukaryota/maudiozyma_serrabonitensis.yaml data/taxa/eukaryota/maudiozyma_turicensis.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/maudiozyma_pseudohumilis.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:147798` contains `NCBITaxon:640839`, label `Maudiozyma pseudohumilis`, rank `SPECIES`, parent `NCBITaxon:3162980`, genetic code `1`, 2 exact synonyms, and 4 related synonyms, matching the record.
- All 13 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:56203` has exactly one scope row for `NCBITaxon:640839`; its rule names `Maudiozyma pseudohumilis` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:40200` reports `organism_count=1` for `NCBITaxon:640839`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0704993` / `Maudiozyma pseudohumilis CBS 11404`, with one linked project and no linked analyses.
- The NCBI type-material inventory has 4 culture-from-holotype rows for `AS 2.3956` and `CGMCC 2.3956` variants, plus 6 type-material rows for `CBS 11404`, `CLIB 1974`, and `XZ-281` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:640839`.
- `data/raw/ncbi_merged_ids.tsv` has no side-inventory rows that currently merge into `NCBITaxon:640839`, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `maudiozyma_pseudohumilis` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The committed GOLD aggregate row and the current local native GOLD JSONL exact scan both report one organism row for `NCBITaxon:640839`.
