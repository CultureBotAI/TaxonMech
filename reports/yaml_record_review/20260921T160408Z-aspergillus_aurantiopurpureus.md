# YAML Record Review: Aspergillus aurantiopurpureus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_aurantiopurpureus.yaml
- Started UTC: 2026-09-21T16:03:33Z
- Finished UTC: 2026-09-21T16:04:08Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2663348 |
| label | Aspergillus aurantiopurpureus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_aurantiopurpureus.yaml`. It has two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_aurantiopurpureus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_aurantiopurpureus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_aurantiopurpureus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 541314 has `NCBITaxon:2663348`, label `Aspergillus aurantiopurpureus`, rank `SPECIES`, parent `NCBITaxon:2720870`, genetic code `1`, the two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 62926 keeps this identifier in scope through the attested-source rule, consistent with the generated `SEEDED` status and the `seed_from_sources` history event.

The YAML lineage matches the NCBI inventory parent chain exactly, from `root` through `Eukaryota`, `Fungi`, `Ascomycota`, `Eurotiales`, `Aspergillaceae`, `Aspergillus`, and `Aspergillus subgen. Nidulantes` to `Aspergillus aurantiopurpureus`.

`data/raw/ncbi_merged_ids.tsv` line 28785 maps old `NCBITaxon:1810884` to `NCBITaxon:2663348`. A scoped `rg --no-ignore --hidden` search for `NCBITaxon:1810884` across `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and `curation/seed_scope.tsv` found no retained retired taxon row or scoped/generated path, so the raw redirect alone does not require a generated `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 541314 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 62926 | Supported exactly: `attested rule: Aspergillus aurantiopurpureus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 24450 and native `data/gold/organisms.jsonl.gz` row 304884 | Supported exactly with one GOLD organism, `Go0446083`. |
| Empty BacDive strain surface | Exact scan of `data/bacdive/records.jsonl.gz` for taxon IDs `2663348` and `NCBITaxon:2663348` | Supported; no exact BacDive records were found. |
| Empty StrainInfo overlay | Exact scan of `data/straininfo/records.jsonl.gz` for strain and deposit taxon IDs `2663348` and `NCBITaxon:2663348` | Supported; no direct or deposit-only StrainInfo rows were found. |

No rows for `NCBITaxon:2663348` were found in `data/raw/ncbi_type_material.tsv`, so there were no NCBI type-material culture tokens to test against BacDive or StrainInfo.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and two related synonyms.
- The aggregate GOLD transform and native GOLD snapshot both support a single organism row for `Aspergillus aurantiopurpureus CBS 140608`.
- Native GOLD has three sequencing projects for `Go0446083`, but no analysis rows; without a BacDive strain join, these projects do not create TaxonMech strain related records or genome links.
- BacDive and StrainInfo do not supply exact records for this taxon.
- LPSN, GTDB, NCBI type-material, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The `data/raw/ncbi_type_material.tsv`, BacDive, and StrainInfo absence checks were exact source-specific scans of the committed TSV and gzip JSONL snapshots.
- The old-ID absence check for `NCBITaxon:1810884` included ignored files in the scoped search.
