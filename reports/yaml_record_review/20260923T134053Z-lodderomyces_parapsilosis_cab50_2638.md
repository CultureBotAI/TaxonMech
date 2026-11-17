# YAML Record Review: Lodderomyces parapsilosis CAB50-2638

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lodderomyces_parapsilosis_cab50_2638.yaml`
- Started UTC: 2026-09-23T13:36:00Z
- Finished UTC: 2026-09-23T13:40:53Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1231521`
- Label: `Lodderomyces parapsilosis CAB50-2638`
- Rank/domain: `STRAIN` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lodderomyces_parapsilosis_cab50_2638.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lodderomyces_parapsilosis.yaml data/taxa/eukaryota/lodderomyces_parapsilosis_cab50_2638.yaml data/taxa/eukaryota/lodderomyces_parapsilosis_cdc317.yaml data/taxa/eukaryota/lodderomyces_pseudojiufengensis.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lodderomyces_parapsilosis_cab50_2638.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:281265` contains `NCBITaxon:1231521`, label `Lodderomyces parapsilosis CAB50-2638`, rank `STRAIN`, and genetic code `12`, matching the record.
- All 14 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks, including the species parent `NCBITaxon:5480` / `Lodderomyces parapsilosis`.
- The NCBI row has no exact or related synonyms, consistent with the YAML's absent `synonyms` slot.
- `curation/seed_scope.tsv:58591` has exactly one scope row for `NCBITaxon:1231521`; its rule names `Lodderomyces parapsilosis CAB50-2638` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:5541` reports `organism_count=1` for `NCBITaxon:1231521`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0006199` / `Candida parapsilosis CAB50-2638`, and its direct project `Gp0006199`; no native analysis rows linked to that project.
- The bounded scan found no NCBI type-material, BacDive, StrainInfo, or generated strain rows for this exact strain taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this strain, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lodderomyces_parapsilosis_cab50_2638` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- `data/raw/ncbi_merged_ids.tsv` has no old ID that now points to `NCBITaxon:1231521`, and there are no retained old-ID rows in `data/raw/ncbitaxon_taxa.tsv`; the absence of `replaces` is expected.
