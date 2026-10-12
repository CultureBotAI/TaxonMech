# YAML Record Review: Arthromyces matolae

## Target

- File: `data/taxa/eukaryota/arthromyces_matolae.yaml`
- Identifier: `NCBITaxon:530044`
- Label: `Arthromyces matolae`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:5450` / `Arthromyces`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Agaricomycetes` -> `Agaricomycetidae` -> `Agaricales` -> `Tricholomatineae` -> `Lyophyllaceae` -> `Arthromyces`
- Existing review report: none found for `*arthromyces_matolae.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/arthromyces_matolae.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/arthromyces_matolae.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:530044`, labelled `Arthromyces matolae` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:530044` is a `SPECIES` child of `NCBITaxon:5450` / `Arthromyces`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and one related synonym, `Arthromyces matolae T. J. Baroni, Lodge & Lindner, 2007`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Arthromyces matolae, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:530044`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:530044`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:530044`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:530044` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0632102`, `Arthromyces matolae D32`.
- GOLD organism `Go0632102` has one project, `Gp0645923`, with BioProject `PRJNA417766` and BioSample `SAMN14543191`.
- GOLD project `Gp0645923` is linked to genome analysis `Ga0553226` with GenBank assembly accession `GCA_018855395.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `530044`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `530044`.
- `data/raw/ncbi_type_material.tsv` has two holotype rows for `NCBITaxon:530044`, spelling the same specimen as `NYBG:collector:T. J. Baroni:9820` and `T. J. Baroni 9820 (NYBG)`.
- Exact `Arthromyces matolae` lookups found 0 BacDive rows and 0 StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive and StrainInfo have no exact NCBI match, and the native GOLD row has only bare strain `D32` with no eligible local BacDive or StrainInfo strain evidence.
- The NCBI holotype rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/arthromyces_matolae.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonym, holotype evidence, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/arthromyces_matolae.yaml` and `just validate-strict data/taxa/eukaryota/arthromyces_matolae.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Arthromyces matolae D32` is project-linked through `AP PROJECT GOLD IDS = Gp0645923`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
