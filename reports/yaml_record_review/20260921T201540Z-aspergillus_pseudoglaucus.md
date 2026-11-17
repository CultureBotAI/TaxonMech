# YAML Record Review: Aspergillus pseudoglaucus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_pseudoglaucus.yaml
- Started UTC: 2026-09-21T20:14:28Z
- Finished UTC: 2026-09-21T20:15:40Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1405805 |
| label | Aspergillus pseudoglaucus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720874 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_pseudoglaucus.yaml`. It carries nine NCBI exact synonyms, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_pseudoglaucus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_pseudoglaucus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_pseudoglaucus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 347031 has `NCBITaxon:1405805`, label `Aspergillus pseudoglaucus`, rank `SPECIES`, direct parent `NCBITaxon:2720874`, genetic code `1`, nine exact synonyms, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 60012 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Aspergillus`.

`data/raw/ncbi_merged_ids.tsv` redirects five old IDs, `NCBITaxon:1140384`, `NCBITaxon:1140385`, `NCBITaxon:41409`, `NCBITaxon:41410`, and `NCBITaxon:469278`, into `NCBITaxon:1405805`. None of those old IDs is retained in `data/raw/ncbitaxon_taxa.tsv` as a retired row pointing at this species, so the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 347031 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 60012 | Supported exactly: `attested rule: Aspergillus pseudoglaucus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 9649 | Supported exactly with eight aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:1405805`. |
| NCBI merged-ID handling | `data/raw/ncbi_merged_ids.tsv` lines 4962-4963, 76513-76514, and 80065; retained-old-ID scan of `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; all five source rows redirect old IDs into this species, with no retained retired rows. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 29038-29054 | Supported exactly with 17 designations for `Aspergillus glaber`, `Aspergillus pseudoglaucus`, `Eurotium fimicola`, `Eurotium glabrum`, and `Eurotium repens`. |
| Native GOLD evidence | Exact native GOLD organism and sequencing-project scans | Supported; seven exact organism rows exist under NCBI taxon `1405805`, and none joins to a native GOLD sequencing project. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1405805`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1405805`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1405805`. |

The native GOLD snapshot has seven exact organism rows, including `Go0630374` for `Eurotium glabrum ZT 8218`, `Go0630375` for `Eurotium glabrum PIL 619`, `Go0630376` for `Eurotium glabrum IMI 278373`, `Go0630377` for `Eurotium glabrum ETH 8218`, and `Go0630378` for `Eurotium glabrum DSM 1370` on lines 460929-460933. No native GOLD sequencing projects or genome analyses join to those organism IDs.

Native StrainInfo has 140 direct strain rows and 228 deposit-taxonomy hits under taxon `1405805`; the generated StrainInfo overlay files contain no rows for `NCBITaxon:1405805` because the overlay is limited to BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, nine exact synonyms, three related synonyms, merged-ID provenance, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of eight.
- The local native GOLD snapshot has seven exact organisms, no linked sequencing projects, and no matched BacDive-derived local strain identifier to join through.
- BacDive does not supply exact local strain records for this taxon, and the native StrainInfo records do not produce generated overlay rows.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
