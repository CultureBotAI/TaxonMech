# YAML Record Review: Magnusiomyces capitatus

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/magnusiomyces_capitatus.yaml`
- Started UTC: 2026-09-23T14:11:00Z
- Finished UTC: 2026-09-23T14:15:28Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1095183`
- Label: `Magnusiomyces capitatus`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/magnusiomyces_capitatus.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/magnaporthiopsis_incrustans.yaml data/taxa/eukaryota/magnaporthiopsis_rhizophila.yaml data/taxa/eukaryota/magnusiomyces_capitatus.yaml data/taxa/eukaryota/magnusiomyces_fungicola.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/magnusiomyces_capitatus.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:235506` contains `NCBITaxon:1095183`, label `Magnusiomyces capitatus`, rank `SPECIES`, parent `NCBITaxon:1095182`, genetic code `1`, 5 exact synonyms, and 6 related synonyms, matching the record.
- All 13 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:57611` has exactly one scope row for `NCBITaxon:1095183`; its rule names `Magnusiomyces capitatus` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:1755` reports `organism_count=1` for `NCBITaxon:1095183`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0705136` / `Magnusiomyces capitatus CBS 162.80`, and one linked project, `Gp0831159`; no native analysis rows are linked to that project or organism.
- The NCBI type-material inventory has 2 type-material rows for `Dipodascus capitatus` / `CBS 162.80`, including the normalized `CBS:162.80` variant. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 61 exact direct rows and 105 deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv` has 3 side-inventory old IDs, `NCBITaxon:1215383`, `NCBITaxon:40399`, and `NCBITaxon:43960`, that currently merge into `NCBITaxon:1095183`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `magnusiomyces_capitatus` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
