# YAML Record Review: Aspergillus galapagensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_galapagensis.yaml
- Started UTC: 2026-09-21T17:46:34Z
- Finished UTC: 2026-09-21T17:48:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1907209 |
| label | Aspergillus galapagensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_galapagensis.yaml`. It carries one NCBI exact synonym, four NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_galapagensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_galapagensis.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_galapagensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 492920 has `NCBITaxon:1907209`, label `Aspergillus galapagensis`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, exact synonym `Neosartorya galapagensis`, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 61526 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` lines 74908-74909 redirect old IDs `NCBITaxon:388759` and `NCBITaxon:388760` into `NCBITaxon:1907209`. Exact first-column scans of `data/raw/ncbitaxon_taxa.tsv` for both old IDs returned no retained retired rows, so the record has no `replaces` value to list.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 492920 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61526 | Supported exactly: `attested rule: Aspergillus galapagensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 17253 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1907209`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 69591-69596 | Supported exactly with six `typematerial.dmp` type-material designations for `CBS 117522`, `IBT 16756`, `KACC 41935`, and their colon-normalized variants under taxon name `Neosartorya galapagensis`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1907209` or the reviewed NCBI type-material designations. |
| Empty StrainInfo overlay | Exact taxon and exact quoted-designation scans of `data/straininfo/records.jsonl.gz`; exact scans of `data/straininfo/assemblies.tsv` and `data/straininfo/related_records.tsv.gz` | Supported; StrainInfo has no direct or deposit-taxonomy record for taxon ID `1907209`, and no assembly or related-record overlay rows for `NCBITaxon:1907209`. |

The local native GOLD snapshot has no organism row with `ORGANISM NCBI TAX ID` equal to `1907209`; consequently, it has no exact project rows and no analysis rows linked by `AP ORGANISM GOLD ID` or `AP PROJECT GOLD IDS`. Generated strain, assembly, genome, and related-record precursor tables likewise have no row for `NCBITaxon:1907209`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, the two old merged IDs, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot does not include an exact organism row for this NCBI taxon, so there are no native GOLD strain-level assertions to emit.
- BacDive and StrainInfo do not supply exact records for this taxon.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The old NCBI IDs merged into this current taxon do not become `replaces` values because they are absent from the retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
