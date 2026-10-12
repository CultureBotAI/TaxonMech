# YAML Record Review: Arthrobotrys iridis

## Target

- File: `data/taxa/eukaryota/arthrobotrys_iridis.yaml`
- Identifier: `NCBITaxon:314119`
- Label: `Arthrobotrys iridis`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:13348` / `Arthrobotrys`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `Orbiliomycetes` -> `Orbiliales` -> `Orbiliaceae` -> `Arthrobotrys`
- Existing review report: none found for `*arthrobotrys_iridis.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/arthrobotrys_iridis.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/arthrobotrys_iridis.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:314119`, labelled `Arthrobotrys iridis` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:314119` is a `SPECIES` child of `NCBITaxon:13348` / `Arthrobotrys`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonyms `Dactylella iridis`, `Monacrosporium iridis`, and `Trinacrium iride`, plus two related synonyms with authorship.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Arthrobotrys iridis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has one retired identifier that now merges into `NCBITaxon:314119`: `NCBITaxon:467308`.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:314119`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/merged-ID/type-material rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:314119`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:314119` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0583384`, `Arthrobotrys iridis 316A_c6.1`, strain `316A_c6.1`, and no culture collection ID.
- GOLD organism `Go0583384` has two projects: `Gp0587347` with BioProject `PRJNA1340985` and BioSample `SAMN52640314`, and `Gp0749114` with no BioProject or BioSample accession in the native row.
- No native GOLD analysis rows link to organism `Go0583384` or to either project through `AP PROJECT GOLD IDS`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 3 direct strain rows for `314119`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `314119`.
- `data/raw/ncbi_type_material.tsv` has four type-material rows for `NCBITaxon:314119`, spelling two accessions with alternate punctuation: `CBS 686.94` / `CBS:686.94` and `IFO 32554` / `IFO:32554`.
- A `CBS 686.94` / `IFO 32554` / `316A_c6.1` token lookup found 0 BacDive rows and one StrainInfo row, `straininfo.strain:124872`; it is one of the excluded exact-NCBI StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, the three exact StrainInfo rows are all excluded, and neither the NCBI type-material tokens nor the native GOLD `316A_c6.1` token adds an eligible local strain.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/arthrobotrys_iridis.yaml`; it is generated and validates strictly.
- Preserve the NCBI exact and related synonyms, retained merged-ID context, type-material evidence, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/arthrobotrys_iridis.yaml` and `just validate-strict data/taxa/eukaryota/arthrobotrys_iridis.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD snapshot has one standard draft project and one transcriptome project for `Arthrobotrys iridis 316A_c6.1` but no matching genome analysis rows through either `AP ORGANISM GOLD ID` or `AP PROJECT GOLD IDS`.
