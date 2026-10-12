# YAML Record Review: Arthrocatena tenebrosa

## Target

- File: `data/taxa/eukaryota/arthrocatena_tenebrosa.yaml`
- Identifier: `NCBITaxon:702019`
- Label: `Arthrocatena tenebrosa`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:1487856` / `Arthrocatena`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `dothideomyceta` -> `Dothideomycetes` -> `Dothideomycetidae` -> `Arthrocatenales` -> `Arthrocatenaceae` -> `Arthrocatena`
- Existing review report: none found for `*arthrocatena_tenebrosa.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/arthrocatena_tenebrosa.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/arthrocatena_tenebrosa.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:702019`, labelled `Arthrocatena tenebrosa` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:702019` is a `SPECIES` child of `NCBITaxon:1487856` / `Arthrocatena`.
- The generated NCBI synonym block matches the raw NCBI row: it has one exact synonym, `Arthrocatena tenebrio`, and three related synonyms, including `Dothideomycetes sp. CCFEE 5413`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Arthrocatena tenebrosa, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:702019`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:702019`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:702019`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:702019` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon, using an exact synonym in the organism name: `Go0583372`, `Arthrocatena tenebrio CCFEE 5413`, strain and culture collection ID `CCFEE 5413`.
- GOLD organism `Go0583372` has two projects, `Gp0587335` and `Gp0891534`; neither native project row has a BioProject or BioSample accession.
- No native GOLD analysis rows link to organism `Go0583372` or to either project through `AP PROJECT GOLD IDS`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct or deposit-only strain rows for `702019`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `702019`.
- `data/raw/ncbi_type_material.tsv` has four type-material rows for `NCBITaxon:702019`, spelling two accessions with alternate punctuation: `CCFEE 5413` / `CCFEE:5413` as a culture from holotype and `CBS 136100` / `CBS:136100` as the holotype.
- Exact `CCFEE 5413` / `CBS 136100` token lookups found 0 BacDive rows and 0 StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive and StrainInfo have no exact NCBI matches, and neither the NCBI type-material tokens nor the native GOLD `CCFEE 5413` token adds an eligible local strain.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/arthrocatena_tenebrosa.yaml`; it is generated and validates strictly.
- Preserve the NCBI exact and related synonyms, type-material evidence, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/arthrocatena_tenebrosa.yaml` and `just validate-strict data/taxa/eukaryota/arthrocatena_tenebrosa.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD snapshot has one standard draft project and one transcriptome project for `Arthrocatena tenebrio CCFEE 5413` but no matching genome analysis rows through either `AP ORGANISM GOLD ID` or `AP PROJECT GOLD IDS`.
