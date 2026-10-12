# YAML Record Review: Apophysomyces variabilis

## Target

- File: `data/taxa/eukaryota/apophysomyces_variabilis.yaml`
- Identifier: `NCBITaxon:760013`
- Label: `Apophysomyces variabilis`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:90268` / `Apophysomyces`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Fungi incertae sedis` -> `Mucoromycota` -> `Mucoromycotina` -> `Mucoromycetes` -> `Mucorales` -> `Mucorineae` -> `Mucoraceae` -> `Apophysomyces`
- Existing review report: none found for `*apophysomyces_variabilis.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/apophysomyces_variabilis.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/apophysomyces_variabilis.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:760013`, labelled `Apophysomyces variabilis` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:760013` is a `SPECIES` child of `NCBITaxon:90268` / `Apophysomyces`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and eight related synonyms, `Apophysomyces sp. CBS 658.93`, `Apophysomyces sp. GMCH 211/09`, `Apophysomyces sp. GMCH 480/07`, `Apophysomyces sp. IMI 338332`, `Apophysomyces sp. IMI 338333`, `Apophysomyces sp. UTHSC 03-3644`, `Apophysomyces sp. UTHSC 06-4222`, and `Apophysomyces variabilis E. Alvarez, Stchigel, Cano, Deanna A. Sutton & Guarro, 2010`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Apophysomyces variabilis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps seven old identifiers into this active target: `NCBITaxon:679941`, `NCBITaxon:679942`, `NCBITaxon:679943`, `NCBITaxon:679944`, `NCBITaxon:679945`, `NCBITaxon:679946`, and `NCBITaxon:679947`.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:760013`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material/merge rows, and no duplicate review report. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:760013`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:760013` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0455065`, `Apophysomyces variabilis NCCPF 102052`, strain `NCCPF 102052`, and no culture collection ID.
- GOLD organism `Go0455065` has one project, `Gp0323391`, with BioProject `PRJNA379216` and BioSample `SAMN06603527`.
- GOLD project `Gp0323391` is linked to genome analysis `Ga0655704` with GenBank assembly accession `GCA_002749535.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct or deposit-only strain rows for `760013`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `760013`.
- A `NCCPF 102052` / `CBS 658.93` / `FMR 10381` token lookup found 0 BacDive rows and one non-exact StrainInfo row: `CBS 658.93` appears in `straininfo.strain:172958`, which is grounded to `NCBITaxon:90269` / `Apophysomyces elegans`.
- `data/raw/ncbi_type_material.tsv` has four type-material rows for `NCBITaxon:760013`: duplicate punctuation variants of culture from holotype `CBS 658.93`, plus duplicate punctuation variants for type material `FMR 10381`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: neither source has an exact NCBI match, the GOLD `NCCPF 102052` token does not join to either local strain source, and the sole local strain-source hit for an NCBI type-material token is grounded to `Apophysomyces elegans`.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/apophysomyces_variabilis.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonyms, retired-ID merge evidence, type-material evidence, count-consistent one-organism GOLD source attestation, and empty exact BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- If the StrainInfo matching policy changes, keep `CBS 658.93` under `straininfo.strain:172958` out of `NCBITaxon:760013` unless its source taxon grounding changes from `Apophysomyces elegans` to `Apophysomyces variabilis`.
- Rerun `just validate data/taxa/eukaryota/apophysomyces_variabilis.yaml` and `just validate-strict data/taxa/eukaryota/apophysomyces_variabilis.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Apophysomyces variabilis NCCPF 102052` is project-linked through `AP PROJECT GOLD IDS = Gp0323391`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
