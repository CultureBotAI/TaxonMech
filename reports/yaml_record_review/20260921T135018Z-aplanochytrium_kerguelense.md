# YAML Record Review: Aplanochytrium kerguelense

## Target

- File: `data/taxa/eukaryota/aplanochytrium_kerguelense.yaml`
- Identifier: `NCBITaxon:87111`
- Label: `Aplanochytrium kerguelense`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:87110` / `Aplanochytrium`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Sar` -> `Stramenopiles` -> `Bigyra` -> `Labyrinthulomycetes` -> `Thraustochytrida` -> `Thraustochytriidae` -> `Aplanochytrium`
- Existing review report: none found for `*aplanochytrium_kerguelense.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/aplanochytrium_kerguelense.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aplanochytrium_kerguelense.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:87111`, labelled `Aplanochytrium kerguelense` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:87111` is a `SPECIES` child of `NCBITaxon:87110` / `Aplanochytrium`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and one related synonym, `Aplanochytrium kerguelense Bahnweg & Sparrow, 1972`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aplanochytrium kerguelense, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:87111`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:87111`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and no duplicate review report. Ignored files were included. The identifier term was bounded so unrelated `NCBITaxon:871110` through `NCBITaxon:871119` prefix hits were excluded.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:87111`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:87111` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0002085`, `Aplanochytrium kerguelense PBS07`, strain `PBS07`, and no culture collection ID.
- GOLD organism `Go0002085` has two projects: `Gp0002085` with BioProject `PRJNA183061` and BioSample `SAMN00829126`, and `Gp0022360` with BioProject `PRJNA183064` and BioSample `SAMN06161157`.
- No native GOLD genome analysis row linked to `Go0002085`, `Gp0002085`, or `Gp0022360` was present in the local `data/gold/analyses.jsonl.gz` snapshot.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct or deposit-only strain rows for `87111`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `87111`.
- A `PBS07` token lookup found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:87111` in the local NCBI type-material snapshot.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: neither source has an exact NCBI match, and the GOLD `PBS07` token does not join to either local strain source.
- The absence of `nomenclature` is expected for this eukaryotic species because generated `nomenclature` entries currently come from LPSN only, and NCBI has no type-material rows for this taxon in the local raw snapshot.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aplanochytrium_kerguelense.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonym, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- If GOLD analysis linking changes, recheck whether organism `Go0002085` or projects `Gp0002085` and `Gp0022360` acquire analysis rows and whether those rows remain source evidence only or can join into strain-related records.
- Rerun `just validate data/taxa/eukaryota/aplanochytrium_kerguelense.yaml` and `just validate-strict data/taxa/eukaryota/aplanochytrium_kerguelense.yaml` after regenerating the taxon record.

## Additional Notes

- The broad string `NCBITaxon:87111` is a prefix of unrelated bacterial taxa `NCBITaxon:871110` through `NCBITaxon:871119`; future raw searches for this target should use a bounded identifier pattern.
