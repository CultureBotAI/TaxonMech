# YAML Record Review: Armillaria novae-zelandiae

## Target

- File: `data/taxa/eukaryota/armillaria_novae_zelandiae.yaml`
- Identifier: `NCBITaxon:153914`
- Label: `Armillaria novae-zelandiae`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:47424` / `Armillaria`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Agaricomycetes` -> `Agaricomycetidae` -> `Agaricales` -> `Marasmiineae` -> `Physalacriaceae` -> `Armillaria`
- Existing review report: none found for `*armillaria_novae_zelandiae.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/armillaria_novae_zelandiae.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/armillaria_novae_zelandiae.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:153914`, labelled `Armillaria novae-zelandiae` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:153914` is a `SPECIES` child of `NCBITaxon:47424` / `Armillaria`.
- The generated NCBI synonym block matches the raw NCBI row: it has 5 exact synonyms and 3 related synonyms, including the strain-like `CMW3951`, `CMW4143`, and `FM-2024l` exact synonyms.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Armillaria novae-zelandiae, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has four retired identifiers that now merge into `NCBITaxon:153914`: `NCBITaxon:188189`, `NCBITaxon:188191`, `NCBITaxon:3122163`, and `NCBITaxon:595674`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:153914`.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:153914`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/merged-ID rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:153914`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:153914` with count `1`.
- Exact native GOLD inspection found two organism rows for the same taxon: `Go0459840`, `Armillaria novae-zelandiae 2840`, strain `2840`; and `Go0530053`, `Armillaria novae-zelandiae`, strain `ICMP 16352`.
- The two native GOLD organisms have three projects: `Gp0326881` with BioProject `PRJNA677793` and BioSample `SAMN16773852`, `Gp0326883` with BioProject `PRJNA677795` and BioSample `SAMN16773632`, and `Gp0484103` with BioProject `PRJNA676626` and BioSample `SAMN16772404`.
- No native GOLD analysis rows link to either exact organism or to any of the three projects through `AP PROJECT GOLD IDS`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 18 direct strain rows for `153914`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `153914`.
- Exact `CMW 3951` / `CMW 4143` / `FM-2024l` token lookups found 0 BacDive rows and 0 StrainInfo rows.
- An `ICMP 16352` token lookup found one StrainInfo row, `straininfo.strain:304803`; it is one of the excluded exact-NCBI StrainInfo rows and does not imply a missing generated strain.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, the 18 exact StrainInfo rows are all excluded because they have no eligible own deposit, and neither the NCBI `CMW` / `FM` synonym tokens nor the native GOLD `ICMP 16352` token adds an eligible local strain.
- The absence of `nomenclature` is consistent with the local source inventory: `data/raw/ncbi_type_material.tsv` has no row for this identifier, and generated `nomenclature` entries currently come from LPSN only.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/armillaria_novae_zelandiae.yaml`; it is generated and validates strictly.
- Preserve the NCBI exact and related synonyms, retained merged-ID context, count-consistent aggregate GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/armillaria_novae_zelandiae.yaml` and `just validate-strict data/taxa/eukaryota/armillaria_novae_zelandiae.yaml` after regenerating the taxon record.

## Additional Notes

- The generated GOLD assertion count is backed by `data/raw/gold_organisms.tsv`, which is an aggregate transformed KG-Microbe GOLD count. The local native GOLD snapshot currently has two inspectable organisms for `NCBITaxon:153914`, three projects, and no matching analysis rows.
