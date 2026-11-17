# YAML Record Review: Salmonella enterica subsp. enterica serovar Paratyphi B str. SPB7

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_paratyphi_b_str_spb7.yaml
- Started UTC: 2026-10-02T08:41:28Z
- Finished UTC: 2026-10-02T08:41:28Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1016998` |
| Label | `Salmonella enterica subsp. enterica serovar Paratyphi B str. SPB7` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:57045` |
| Parent label | `Salmonella enterica subsp. enterica serovar Paratyphi B` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `GTDB`, `GOLD`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_paratyphi_b_str_spb7.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/moraxella_sp_5484.yaml data/taxa/bacteria/moraxella_sp_623.yaml data/taxa/bacteria/polycladomyces_subterraneus.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_paratyphi_b_str_spb7.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 98 lines, 12 lineage entries, 1 taxonomy mapping, 4 synonyms, 1 xref, 0 strains, and 4 source attestations. |
| `taxonmech_bounded_scan.py data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_paratyphi_b_str_spb7.yaml` | Not applicable: the NCBI-only helper exited with `NCBI source mismatch` because the record intentionally combines NCBITaxon, GTDB, GOLD, and MADIN evidence. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*salmonella_enterica_subsp_enterica_serovar_paratyphi_b_str_spb7.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1016998)([^0-9]\|$)' data curation` plus source-specific row scans | Pass: the checked NCBI, GTDB, GOLD, and MADIN rows agree with the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10180 maps `NCBITaxon:1016998` to `salmonella_enterica_subsp_enterica_serovar_paratyphi_b_str_spb7`.
- `curation/seed_scope.tsv` row 26047 keeps this strain in scope with an attested four-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218516 names the same strain, parent serovar, rank, genetic code, three NCBI exact synonyms, and source set `ncbitaxon|gtdb|gold|madin_etal`.
- `data/raw/gtdb_mappings.tsv` row 1172 maps the strain to `GTDB:s__Salmonella_enterica` with `skos:closeMatch` and 21,527 GTDB genomes.
- The generated `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for the directly attested NCBI strain.

## Evidence

- `source_attestations` accurately summarize the four asserted source families: NCBITaxon name, GTDB genomes, GOLD organism, and MADIN trait assertions.
- The GTDB species row at `data/raw/gtdb_species.tsv` row 163163 supports the `s__Salmonella_enterica` label, genus, and 21,527 genome count used by the mapping and source attestation.
- `data/raw/gold_organisms.tsv` row 290 supports the direct GOLD `ORGANISM` assertion count of 1.
- `data/raw/madin_taxa.tsv` row 457 supports the direct MADIN `TRAIT_ASSERTION` assertion count of 7.
- The three NCBITaxon synonyms in the YAML exactly match the synonym field in `data/raw/ncbitaxon_taxa.tsv` row 218516.
- The NCBI lineage is root-first and ends at `NCBITaxon:57045`, the immediate Paratyphi B parent named by the YAML.

## Completeness

- The record is complete for a strain-level seed with count-only GOLD and MADIN attestations.
- `strain_count: 0` is appropriate because no BacDive or StrainInfo strain row is maintained for this exact NCBI taxon.
- The GTDB mapping is represented once in `taxonomy_mappings`, once in `xrefs`, once as a GTDB synonym, and once as a `GTDB` source attestation.
- `data/raw/ncbi_merged_ids.tsv` row 49683 records old `NCBITaxon:272994` as merged into this taxon, but does not require a separate generated xref or strain block.
- No causal graph is expected for this generated taxon identity record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_paratyphi_b_str_spb7.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_paratyphi_b_str_spb7.yaml`.
- Re-run the source-specific raw-row scans after any refresh of `data/raw/` or `curation/seed_scope.tsv`.

## Additional Notes

- The source scans used `--no-ignore --hidden`, so ignored files were included.
- GOLD and MADIN are direct count-style attestations here; they do not create strain, genome, synonym, or causal graph blocks.
- The broad GTDB species has many NCBI close matches; this review checked the exact raw row for `NCBITaxon:1016998`.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10180 |
| `curation/seed_scope.tsv` | 26047 |
| `data/raw/ncbitaxon_taxa.tsv` | 218516 |
| `data/raw/gtdb_species.tsv` | 163163 |
| `data/raw/gtdb_mappings.tsv` | 1172 |
| `data/raw/gold_organisms.tsv` | 290 |
| `data/raw/madin_taxa.tsv` | 457 |
| `data/raw/ncbi_merged_ids.tsv` | 49683 |
| `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_paratyphi_b_str_spb7.yaml` | 1, 71, 77, 83, and 88 |
