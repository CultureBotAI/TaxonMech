# YAML Record Review: Aplosporella prunicola

## Target

- File: `data/taxa/eukaryota/aplosporella_prunicola.yaml`
- Identifier: `NCBITaxon:462254`
- Label: `Aplosporella prunicola`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:462253` / `Aplosporella`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `dothideomyceta` -> `Dothideomycetes` -> `Dothideomycetes incertae sedis` -> `Botryosphaeriales` -> `Aplosporellaceae` -> `Aplosporella`
- Existing review report: none found for `*aplosporella_prunicola.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/aplosporella_prunicola.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aplosporella_prunicola.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:462254`, labelled `Aplosporella prunicola` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:462254` is a `SPECIES` child of `NCBITaxon:462253` / `Aplosporella`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and two related synonyms, `Aplosporella prunicola Damm & Crous, 2007` and `Aplosporella sp. UD-2007`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aplosporella prunicola, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:462254`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:462254`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material rows, and no duplicate review report. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:462254`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:462254` with count `2`.
- Exact native GOLD inspection found two organism rows for the same taxon: `Go0019342` / `Aplosporella prunicola CBS 121167`, and `Go0677964` / `Aplosporella prunicola Aplpr1`.
- GOLD organism `Go0019342` has two projects: `Gp0019342` with BioProject `PRJNA459547` and BioSample `SAMN09074088`, and `Gp0019419` with BioProject `PRJNA196034` and BioSample `SAMN02745735`.
- GOLD organism `Go0677964` has one project, `Gp0779805`, with BioProject `PRJNA777748` and BioSample `SAMN22899345`.
- GOLD project `Gp0019419` is linked to genome analysis `Ga0226698`, which has IMG taxon `2761201861` and an empty `AP GENBANK` list. GOLD project `Gp0779805` is linked to genome analysis `Ga0663289` with GenBank assembly accession `GCA_023079245.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 3 direct strain rows for `462254`, 0 deposit-only rows, and 0 missing exclusions; all 3 direct IDs are excluded locally as `no_eligible_own_deposit_match`.
- A `CBS 121167` / `Aplpr1` token lookup found 0 BacDive rows and 0 StrainInfo rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `462254`.
- `data/raw/ncbi_type_material.tsv` has eight type-material rows for `NCBITaxon:462254`: duplicate punctuation variants of culture from holotype `CBS 121167`, `STE-U 6327`, and `STEU 6326`, plus duplicate punctuation variants for holotype `CBS H-19848`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: BacDive has no exact NCBI match, all exact StrainInfo matches are explicitly excluded, and the GOLD culture tokens do not join to either local strain source.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aplosporella_prunicola.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonyms, type-material evidence, count-consistent two-organism GOLD source attestation, and StrainInfo exclusion behavior when regenerating the record.

## Follow-up Checks

- If the StrainInfo exclusion policy for `no_eligible_own_deposit_match` changes, re-evaluate the 3 excluded StrainInfo rows for `NCBITaxon:462254` and check whether any should contribute to `strain_count`.
- If GOLD analysis linking changes, recheck whether project `Gp0019342` acquires an analysis and whether `Ga0226698` acquires a GenBank assembly accession.
- Rerun `just validate data/taxa/eukaryota/aplosporella_prunicola.yaml` and `just validate-strict data/taxa/eukaryota/aplosporella_prunicola.yaml` after regenerating the taxon record.

## Additional Notes

- Both native GOLD analysis rows are project-linked through `AP PROJECT GOLD IDS`; neither uses `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
