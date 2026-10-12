# YAML Record Review: Lundqvistomyces karachiensis

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lundqvistomyces_karachiensis.yaml`
- Started UTC: 2026-09-23T13:56:00Z
- Finished UTC: 2026-09-23T13:58:43Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:330530`
- Label: `Lundqvistomyces karachiensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lundqvistomyces_karachiensis.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lulworthia_fucicola.yaml data/taxa/eukaryota/lunasporangiospora_selenospora.yaml data/taxa/eukaryota/lundqvistomyces_karachiensis.yaml data/taxa/eukaryota/lycoperdon_perlatum.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lundqvistomyces_karachiensis.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:67555` contains `NCBITaxon:330530`, label `Lundqvistomyces karachiensis`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI exact synonyms `Strattonia karachiensis` and `Zopfiella karachiensis` plus all four NCBI related synonyms match the YAML `synonyms`.
- `curation/seed_scope.tsv:55249` has exactly one scope row for `NCBITaxon:330530`; its rule names `Lundqvistomyces karachiensis` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:32292` reports `organism_count=1` for `NCBITaxon:330530`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0651414` / `Lundqvistomyces karachiensis IMI 340453`, and two direct projects, `Gp0688318` and `Gp0699270`; no native analysis rows linked to those projects.
- `data/straininfo/records.jsonl.gz` contains 10 exact StrainInfo strain records and 12 exact deposit records for NCBI taxon `330530`, but none joined into generated BacDive, strain assembly, strain genome, or strain related-record rows for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no NCBI type-material rows and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lundqvistomyces_karachiensis` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- `data/raw/ncbi_merged_ids.tsv` has one exact side-inventory row, `NCBITaxon:2587419 -> NCBITaxon:330530`, but the retired ID is absent from retained `data/raw/ncbitaxon_taxa.tsv` rows, so the generated YAML correctly has no `replaces` value.
