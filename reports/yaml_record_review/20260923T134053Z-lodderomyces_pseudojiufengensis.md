# YAML Record Review: Lodderomyces pseudojiufengensis

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lodderomyces_pseudojiufengensis.yaml`
- Started UTC: 2026-09-23T13:36:00Z
- Finished UTC: 2026-09-23T13:40:53Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:497109`
- Label: `Lodderomyces pseudojiufengensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lodderomyces_pseudojiufengensis.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lodderomyces_parapsilosis.yaml data/taxa/eukaryota/lodderomyces_parapsilosis_cab50_2638.yaml data/taxa/eukaryota/lodderomyces_parapsilosis_cdc317.yaml data/taxa/eukaryota/lodderomyces_pseudojiufengensis.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lodderomyces_pseudojiufengensis.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:112574` contains `NCBITaxon:497109`, label `Lodderomyces pseudojiufengensis`, rank `SPECIES`, and genetic code `12`, matching the record.
- All 13 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI exact synonym `Candida pseudojiufengensis` and related synonyms `Candida pseudojiufengensis F.Y. Bai & Z.H. Ji, 2009`, `Candida sp. AS 2.3693`, and `Lodderomyces pseudojiufengensis (F.Y. Bai & Z.H. Ji) Q.M. Wang, Boekhout, Yurkov, G. Peter & F.Y. Bai, 2026` match the YAML `synonyms`.
- `curation/seed_scope.tsv:55837` has exactly one scope row for `NCBITaxon:497109`; its rule names `Lodderomyces pseudojiufengensis` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:37231` reports `organism_count=1` for `NCBITaxon:497109`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0704970` / `Candida pseudojiufengensis CBS 10847`, and its direct project `Gp0830986`; no native analysis rows linked to that project.
- `data/raw/ncbi_type_material.tsv:224170-224182` contains 13 exact rows for `NCBITaxon:497109` under `Candida pseudojiufengensis`, including ATCC/CBS culture-from-holotype aliases and `CGMCC 2.3693` holotype aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found zero exact BacDive rows and no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lodderomyces_pseudojiufengensis` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- `data/raw/ncbi_merged_ids.tsv` has no old ID that now points to `NCBITaxon:497109`, and there are no retained old-ID rows in `data/raw/ncbitaxon_taxa.tsv`; the absence of `replaces` is expected.
