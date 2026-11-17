# YAML Record Review: Malawimonas californiana (nom. ined.)

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/malawimonas_californiana_nom_ined.yaml`
- Started UTC: 2026-09-23T14:34:00Z
- Finished UTC: 2026-09-23T14:37:12Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:221722`
- Label: `Malawimonas californiana (nom. ined.)`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/malawimonas_californiana_nom_ined.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/malawimonas_californiana_nom_ined.yaml data/taxa/eukaryota/malbranchea_aurantiaca.yaml data/taxa/eukaryota/malbranchea_cinnamomea.yaml data/taxa/eukaryota/mallocybe_terrigena.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/malawimonas_californiana_nom_ined.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:43682` contains `NCBITaxon:221722`, label `Malawimonas californiana (nom. ined.)`, rank `SPECIES`, parent `NCBITaxon:136088`, genetic code `1`, and exact synonym `Malawimonas californiana`, matching the record.
- All 8 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:54599` has exactly one scope row for `NCBITaxon:221722`; its rule names `Malawimonas californiana (nom. ined.)` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:21050` reports `organism_count=1` for `NCBITaxon:221722`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0002404` / `Malawimonas californiana`, and one linked project, `Gp0002404`; no native analysis rows are linked to that project or organism.
- The bounded scan found no exact NCBI type-material rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no exact StrainInfo direct, deposit, assembly, exclusion, or related-record rows for this taxon.
- The bounded scan and `rg --no-ignore --hidden` field-boundary search found no old merged IDs for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `malawimonas_californiana_nom_ined` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
