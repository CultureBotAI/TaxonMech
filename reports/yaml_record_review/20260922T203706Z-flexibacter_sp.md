# YAML Record Review: Flexibacter sp.
- Repository: TaxonMech
- Record: `data/taxa/bacteria/flexibacter_sp.yaml`
- Started UTC: 2026-09-22T20:33:22Z
- Finished UTC: 2026-09-22T20:37:08Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1005` / `flexibacter_sp`.
- The record is a generated `SPECIES`-rank `BACTERIA` record for `Flexibacter sp.` under `NCBITaxon:2628082` (`unclassified Flexibacter`).
- The record is seeded from the pinned `data/raw/`, `data/atb/`, and `data/straininfo/` inventories and has `grounding_status: EXACT` plus `mapping_status: SEEDED`.

## Validation
- `just validate data/taxa/bacteria/flexibacter_sp.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/flexibacter_sp.yaml data/taxa/bacteria/fimbriimonas_ginsengisoli.yaml data/taxa/bacteria/streptococcus_suis_ss12.yaml data/taxa/bacteria/streptococcus_suis_d9.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005`, `label: Flexibacter sp.`, `rank: SPECIES`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:2628082`, and `genetic_code: 11` match the exact pinned NCBI row in `data/raw/ncbitaxon_taxa.tsv`.
- The root-first lineage follows the local NCBI backbone through `Bacteria`, `Bacteroidota`, `Cytophagia`, `Cytophagales`, `Flexibacteraceae`, `Flexibacter`, and `unclassified Flexibacter`; no GTDB or LPSN placement is being merged into that lineage.
- No `nomenclature`, `taxonomy_mappings`, `synonyms`, or `xrefs` are emitted for this record, matching the absence of same-taxon LPSN and GTDB rows for `NCBITaxon:1005`.

## Evidence
- An exact-ID gitignore-independent `rg --no-ignore --hidden` search across `data/raw`, `data/atb`, and `data/straininfo` found the same `NCBITaxon:1005` source rows represented in `source_attestations`: one NCBITAXON name row, five BacDive strain rows, two MediaDive medium assertions, and one BactoTraits trait assertion.
- The five `strains` entries correspond to the five direct `data/raw/bacdive_strains.tsv` rows for `bacdive_3785`, `bacdive_3786`, `bacdive_3787`, `bacdive_145451`, and `bacdive_145453`.
- Genome assemblies, genome records, ATB BioSample links, GOLD organism/project records, and BV-BRC/PATRIC/IMG identifiers on the `ATCC-35103` and `ATCC-35208` strain entries preserve explicit strain and culture-collection evidence from `data/raw/strain_related_records.tsv` and `data/atb`.
- StrainInfo SI-ID/SI-DP related records on the same BacDive entries preserve their own `NCBITaxon:992` or `NCBITaxon:998` native classifications as related-record metadata; those source taxon IDs do not override the BacDive classification of the five strains under `NCBITaxon:1005`.

## Completeness
- `strain_count: 5` equals the five direct BacDive rows in the pinned inventory.
- The MediaDive and BactoTraits attestation counts agree with the exact same-taxon inventory rows.
- The record contains the available NCBI identity, BacDive strain, MediaDive count, BactoTraits count, ATB overlap, GOLD, BV-BRC, NCBI Assembly, and StrainInfo source evidence found locally for these strain IDs.

## Findings
- No findings.

## Recommended Edits
- None.

## Follow-up Checks
- None required for this record.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-flexibacter_sp.md'` returned no prior ignored report for this stem; `find` includes ignored reports.
- Live NCBI, BacDive, MediaDive, BactoTraits, and StrainInfo lookups were not used; the pinned rows in `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the local source of truth.
