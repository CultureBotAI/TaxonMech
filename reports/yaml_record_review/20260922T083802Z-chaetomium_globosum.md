# YAML Record Review: Chaetomium globosum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/chaetomium_globosum.yaml
- Started UTC: 2026-09-22T08:38:02Z
- Finished UTC: 2026-09-22T08:38:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:38033 |
| label | Chaetomium globosum |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5149 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/chaetomium_globosum.yaml`. It carries one NCBI exact synonym, four NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*chaetomium_globosum.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/chaetomium_globosum.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/chaetomium_globosum.yaml` exited successfully and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4325 has `NCBITaxon:38033`, label `Chaetomium globosum`, rank `SPECIES`, direct parent `NCBITaxon:5149`, genetic code `1`, one exact synonym, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52385 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Chaetomium` under family `Chaetomiaceae`.

The side-inventory merged-ID scan found `NCBITaxon:1087733` and `NCBITaxon:1671129` pointing into this taxon, but no retained retired rows map to this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4325 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52385 | Supported exactly: `attested rule: Chaetomium globosum, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 33876 | Supported exactly with eight aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:38033`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has eight exact organism rows, `Go0657843` through `Go0657850`, for the Y3904, Y3903, X1803, X1802H, X1802G, S3802, R1201, and 2NP9F rows on lines 484364-484371. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact projects `Gp0702111` through `Gp0702118` join one-to-one to the eight exact GOLD organism IDs on lines 527682-527689. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; eight exact analyses join through `AP PROJECT GOLD IDS` to projects `Gp0702111` through `Gp0702118`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with two CBS 160.62 `culture from neotype` rows on lines 199548-199549. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `38033`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:38033`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:38033`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; side-inventory old IDs `NCBITaxon:1087733` and `NCBITaxon:1671129` point into this taxon, but no retained retired row exists for the generator to carry into `replaces`. |

The native StrainInfo snapshot has 186 exact direct rows and 263 exact deposit links under `NCBITaxon:38033`, but none overlays onto a BacDive-derived local strain inventory entry.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Chaetomium` parent, one exact synonym, four related synonyms, and two type-material rows.
- The NCBI merged-ID side inventory has two old IDs that are not present as retained retired rows, so no `replaces` entry is generated.
- The aggregate GOLD transform supplies a taxon-level organism count of eight.
- The local native GOLD snapshot supplies eight exact organisms, eight joined projects, and eight joined analyses for this taxon.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Chaetomium globosum` as `SPECIES`, and the generated record follows the source rank exactly.
