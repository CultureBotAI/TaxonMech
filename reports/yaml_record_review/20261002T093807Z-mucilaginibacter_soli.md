# YAML Record Review: Mucilaginibacter soli

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/mucilaginibacter_soli.yaml
- Started UTC: 2026-10-02T09:38:07Z
- Finished UTC: 2026-10-02T09:38:07Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017095` |
| Label | `Mucilaginibacter soli` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:423349` |
| Parent label | `Mucilaginibacter` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `1` |
| Source attestations | `NCBITAXON`, `LPSN`, `BACDIVE`, `GOLD`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/mucilaginibacter_soli.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/mucilaginibacter_soli.yaml data/taxa/bacteria/colwellia_sp_bsw21760.yaml data/taxa/bacteria/flavobacterium_sp_bsw21750.yaml data/taxa/bacteria/flavobacterium_sp_bsw21751.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 139 lines, 11 lineage entries, 1 nomenclature row, 2 synonyms, 1 xref, 1 strain, and 5 source attestations. |
| `taxonmech_bounded_scan.py data/taxa/bacteria/mucilaginibacter_soli.yaml` | Not applicable: the NCBI-only helper exited with `NCBI source mismatch` on this five-source record, so the upstream rows were checked directly. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*mucilaginibacter_soli.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1017095)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to `PATHS.tsv`, `legacy_page_paths.tsv`, `seed_scope.tsv`, source rows, and this YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10253 maps `NCBITaxon:1017095` to `mucilaginibacter_soli`.
- `curation/seed_scope.tsv` row 14821 keeps this species in scope with 5 attested sources including NCBI.
- `data/raw/ncbitaxon_taxa.tsv` row 218588 names `NCBITaxon:1017095` as `Mucilaginibacter soli` and lists the NCBI synonyms in the YAML.
- The YAML identifier, label, rank, parent taxon, and genetic code agree with the raw NCBI row.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a direct NCBI Taxonomy species seed.

## Evidence

- `data/raw/lpsn_names.tsv` row 27009 supplies `lpsn:790018`, the Jiang et al. 2012 authority, the LPSN status flags, `kgmicrobe.strain:NRRL-B-59458`, two DOIs, `PMID:21890726`, and `INSDC:JF701183`.
- `data/raw/bacdive_strains.tsv` row 56048 supplies BacDive strain `133738`, designation `R9-65`, the matching LPSN id, and the CCTCC/NRRL culture-collection ids.
- `data/raw/ncbi_type_material.tsv` rows 1106-1113 contain CCTCC, NRRL, and R9-65 type-material spellings that agree with the type-strain evidence.
- `data/raw/strain_related_records.tsv` rows 86037-86038 attach `gold:Go0043805` to the BacDive strain by `ORGANISM CULTURE COLLECTION ID` and `ORGANISM STRAIN`.
- `data/raw/gold_organisms.tsv` row 292 counts 1 GOLD organism for the taxon, and `data/raw/madin_taxa.tsv` row 470 counts 6 MADIN trait assertions.

## Completeness

- The record materializes the expected LPSN nomenclature row, LPSN xref, NCBITaxon synonyms, BacDive type strain, GOLD related organism rows, and five source attestations.
- The two culture-collection ids, `kgmicrobe.strain:CCTCC-AB%202010331` and `kgmicrobe.strain:NRRL-B-59458`, agree with the culture-collection and type-material rows.
- `strain_count: 1` agrees with the single BacDive strain row for this exact taxon.
- No genome, genome assembly, taxonomy mapping, or causal graph block is asserted for this record.
- The legacy page path hit is historical routing metadata and does not imply additional YAML payload.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/mucilaginibacter_soli.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/mucilaginibacter_soli.yaml`.
- Re-check the LPSN, BacDive, GOLD, MADIN, culture-collection, strain-related, and NCBI type-material source rows after any source refresh.

## Additional Notes

- The source scans used `--no-ignore --hidden`, so ignored files were included.
- The 2026-09-13 curation event accurately reports a five-source seed from BACDIVE, GOLD, LPSN, MADIN, and NCBITAXON.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10253 |
| `curation/seed_scope.tsv` | 14821 |
| `data/raw/ncbitaxon_taxa.tsv` | 218588 |
| `data/raw/lpsn_names.tsv` | 27009 |
| `data/raw/bacdive_strains.tsv` | 56048 |
| `data/raw/gold_organisms.tsv` | 292 |
| `data/raw/madin_taxa.tsv` | 470 |
| `data/raw/ncbi_type_material.tsv` | 1106-1113 |
| `data/raw/culture_collection_strains.tsv` | 14548 and 146873 |
| `data/raw/strain_related_records.tsv` | 86037-86038 |
| `data/taxa/bacteria/mucilaginibacter_soli.yaml` | 1, 107, 113, 119, 124, and 129 |

- Source attestation units are internally consistent:

| Source | Assertion unit |
|---|---|
| `NCBITAXON` | `NAME` |
| `LPSN` | `NAME` |
| `BACDIVE` | `STRAIN` |
| `GOLD` | `ORGANISM` |
| `MADIN` | `TRAIT_ASSERTION` |

- The generated record has no top-level `taxonomy_mappings`, `genome_assemblies`, `genome_records`, or `causal_graphs` blocks.
- The review found no maintained upstream row that disagrees with the YAML payload.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/mucilaginibacter_soli.yaml` directly.
