# YAML Record Review: Salmonella enterica subsp. enterica serovar Agona str. SAR B1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sar_b1.yaml
- Started UTC: 2026-09-22T16:39:40Z
- Finished UTC: 2026-09-22T16:39:40Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sar_b1.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003190` / `Salmonella enterica subsp. enterica serovar Agona str. SAR B1`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003190`
- Label: `Salmonella enterica subsp. enterica serovar Agona str. SAR B1`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:58095` / `Salmonella enterica subsp. enterica serovar Agona`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sar_b1.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sar_b1.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sa_3.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sa_4.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sa_5.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sar_b1.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The pinned NCBI row maps `NCBITaxon:1003190` to the strain label `Salmonella enterica subsp. enterica serovar Agona str. SAR B1`, rank `STRAIN`, parent `NCBITaxon:58095`, exact synonym `Salmonella enterica subsp. enterica serovar Agona strain SAR B1`, source bundle `ncbitaxon|gold`, and snapshot date `2026-09-13`; the YAML carries those NCBI identity fields.
- The parent row maps `NCBITaxon:58095` to `Salmonella enterica subsp. enterica serovar Agona`, and the YAML lineage is root-first and reaches that parent through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Gammaproteobacteria`, `Enterobacterales`, `Enterobacteriaceae`, `Salmonella`, `Salmonella enterica`, and `Salmonella enterica subsp. enterica`.
- No GTDB mapping, GTDB synonym, or GTDB xref is projected for this strain, matching the absence of an exact `NCBITaxon:1003190` row from `data/raw/gtdb_mappings.tsv`.

## Evidence

- The NCBI source attestation and NCBI exact synonym are supported by the `NCBITaxon:1003190` row in `data/raw/ncbitaxon_taxa.tsv`.
- The same-taxon GOLD organism source attestation is supported by the `NCBITaxon:1003190` count row in `data/raw/gold_organisms.tsv`.

## Completeness

- The record correctly leaves GTDB mapping, causal-graph, and BacDive strain slots absent; no GTDB mapping, causal graph, or same-taxon BacDive strain was attested in the reviewed raw rows.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found the exact NCBI, GOLD, and PATHS rows and no LPSN, BacDive, StrainInfo, trait, medium, strain-genome, or GTDB evidence that would require additional same-strain blocks.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- Before this report was created, an exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-salmonella_enterica_subsp_enterica_serovar_agona_str_sar_b1.md'` probe found no prior review report for this stem; `find` includes ignored `reports/` files.
- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
