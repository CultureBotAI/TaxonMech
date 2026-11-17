# YAML Record Review: Lodderomyces parapsilosis

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lodderomyces_parapsilosis.yaml`
- Started UTC: 2026-09-23T13:36:00Z
- Finished UTC: 2026-09-23T13:40:53Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:5480`
- Label: `Lodderomyces parapsilosis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lodderomyces_parapsilosis.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lodderomyces_parapsilosis.yaml data/taxa/eukaryota/lodderomyces_parapsilosis_cab50_2638.yaml data/taxa/eukaryota/lodderomyces_parapsilosis_cdc317.yaml data/taxa/eukaryota/lodderomyces_pseudojiufengensis.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lodderomyces_parapsilosis.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2430` contains `NCBITaxon:5480`, label `Lodderomyces parapsilosis`, rank `SPECIES`, and genetic code `12`, matching the record.
- All 13 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI exact synonyms match the seeded exact synonyms: `Candida parapsilosis (Ashford) Langeron & Talice`, `Monilia parapsilosis`, `Mycocandida parapsilosis`, and `Mycotorula parapsilopsis`.
- NCBI related synonyms match the seeded related synonyms: `Lodderomyces parapsilosis (Ashford) Q.M. Wang, Boekhout, Yurkov, G. Peter & F.Y. Bai, 2026` and `Monilia parapsilosis Ashford, 1928`.
- `curation/seed_scope.tsv:52007` has exactly one scope row for `NCBITaxon:5480`; its rule names `Lodderomyces parapsilosis` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:38491` reports `organism_count=23` for `NCBITaxon:5480`, matching the YAML `GOLD` attestation.
- Exact native GOLD expansion found 23 organism rows in `data/gold/organisms.jsonl.gz`, 23 direct projects in `data/gold/projects.jsonl.gz`, and 20 linked analyses in `data/gold/analyses.jsonl.gz` through exact `AP PROJECT GOLD IDS`.
- `data/raw/ncbi_type_material.tsv:232863-232890` contains 28 exact rows for `NCBITaxon:5480` under `Monilia parapsilosis`, spanning culture-from-holotype aliases such as `ATCC 22019`, `DSM 5784`, `JCM 1785`, `NRRL Y-12969`, and holotype aliases for `CBS 604`.
- `data/straininfo/records.jsonl.gz` contains 331 exact StrainInfo strain records and 397 exact deposit records for NCBI taxon `5480`, but none joined into `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv` for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found zero exact BacDive rows, zero generated strain assembly rows, and zero generated StrainInfo assembly or exclusion rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lodderomyces_parapsilosis` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.
- If a future StrainInfo projection is added for the direct `Lodderomyces parapsilosis` rows, rerun `just seed`, a `just seed-canary NCBITaxon:5480`, `just validate data/taxa/eukaryota/lodderomyces_parapsilosis.yaml`, `just validate-strict data/taxa/eukaryota/lodderomyces_parapsilosis.yaml`, and `just verify-corpus`.

## Additional Notes

- `data/raw/ncbi_merged_ids.tsv` has one exact side-inventory row, `NCBITaxon:1114983 -> NCBITaxon:5480`, but the retired ID is absent from retained `data/raw/ncbitaxon_taxa.tsv` rows, so the generated YAML correctly has no `replaces` value.
- `data/straininfo/related_records.tsv.gz` has two rows for `straininfo.strain:90079` / `straininfo.deposit:485298` attached to `kgmicrobe.strain:bacdive_134588` with `NCBITaxon:5480`; those rows do not create a direct generated strain for this record.
