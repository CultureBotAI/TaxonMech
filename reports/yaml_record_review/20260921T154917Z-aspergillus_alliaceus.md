# YAML Record Review: Aspergillus alliaceus

## Target

- File: `data/taxa/eukaryota/aspergillus_alliaceus.yaml`
- Identifier: `NCBITaxon:209559`
- Label: `Aspergillus alliaceus`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2720871` / `Aspergillus subgen. Circumdati`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Eurotiomycetidae` -> `Eurotiales` -> `Aspergillaceae` -> `Aspergillus` -> `Aspergillus subgen. Circumdati`
- Existing review report: none found for `*aspergillus_alliaceus.md` under the ignored `reports/yaml_record_review/` tree. A no-ignore, hidden-file search over `reports/yaml_record_review/` for `aspergillus_alliaceus` also found no existing report body that mentioned this slug; ignored files were included.

## Validation

- `just validate data/taxa/eukaryota/aspergillus_alliaceus.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aspergillus_alliaceus.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:209559`, labelled `Aspergillus alliaceus` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:209559` is a `SPECIES` child of `NCBITaxon:2720871` / `Aspergillus subgen. Circumdati`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonyms `Aspergillus albertensis`, `Aspergillus burnettii`, `Petromyces albertensis`, and `Petromyces alliaceus`, plus six related authorship and provisional synonyms.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aspergillus alliaceus, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has three historical IDs, `NCBITaxon:2508778`, `NCBITaxon:36633`, and `NCBITaxon:41046`, all merged into the current `NCBITaxon:209559` identifier.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:209559`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:209559` with count `12`.
- Exact native GOLD inspection found 11 organism rows for the same taxon in the local `data/gold/organisms.jsonl.gz` snapshot. These rows cover `CBS 536.65`, `IBT 14317`, `QM 1885`, `NRRL 315`, `NBRC 7538`, `IMI 051982`, `IFO 7538`, `DSM 813`, `CMI 051982`, `ATCC 10060`, and `4656 (WB 315)`.
- Native GOLD has four project rows: two for `Go0108061` / `CBS 536.65` and two for `Go0108163` / `IBT 14317`, with BioProjects `PRJNA334014`, `PRJNA459589`, `PRJNA333895`, and `PRJNA459636`. The nine `Go06244xx` organism rows from the local native snapshot have no matching native project rows.
- No native GOLD genome analysis rows were linked to any exact `Aspergillus alliaceus` organism or project.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 51 direct strain rows and 1 deposit-only row for `209559`; all 52 rows are already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `209559`.
- Quoted exact JSON-string lookups for the visible NCBI type-material and native GOLD collection numbers found 0 BacDive rows. They found four StrainInfo rows by exact collection token, all already represented in the StrainInfo exclusion table.
- `data/raw/ncbi_type_material.tsv` has 24 rows for `NCBITaxon:209559`, covering type material for `Aspergillus albertensis`, `Aspergillus alliaceus`, and `Aspergillus burnettii`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, NCBITaxon and GOLD source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo rows are already excluded, and exact quoted collection-token lookups did not reveal an eligible local BacDive own deposit for the GOLD or NCBI type-material accessions.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aspergillus_alliaceus.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, aggregate GOLD source attestation, NCBI type-material inventory behavior, historical merge handling, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/aspergillus_alliaceus.yaml` and `just validate-strict data/taxa/eukaryota/aspergillus_alliaceus.yaml` after regenerating the taxon record.

## Additional Notes

- The aggregate GOLD count in `data/raw/gold_organisms.tsv` is 12 while this local native GOLD snapshot exposes 11 exact organism rows. The generated record only attests the transformed aggregate count, so this native-snapshot mismatch is useful provenance rather than a YAML defect.
- The exact StrainInfo rows are independently real source observations for `Aspergillus alliaceus` and its exact NCBI synonyms, but all 52 exact direct or deposit-only rows are intentionally filtered because none has an eligible matched local BacDive own deposit.
- The NCBI type-material rows are present in the local source inventory, but this generated eukaryotic record has no `nomenclature` block because TaxonMech currently generates `nomenclature` from LPSN rather than from NCBI `typematerial.dmp`.
