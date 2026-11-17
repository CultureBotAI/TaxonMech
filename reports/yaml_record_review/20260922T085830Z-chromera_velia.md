# YAML Record Review: Chromera velia

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/chromera_velia.yaml
- Started UTC: 2026-09-22T08:58:30Z
- Finished UTC: 2026-09-22T08:58:30Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:505693 |
| label | Chromera velia |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:505692 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic alveolate species at `data/taxa/eukaryota/chromera_velia.yaml`. It carries three NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*chromera_velia.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/chromera_velia.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/chromera_velia.yaml` exited successfully and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 114997 has `NCBITaxon:505693`, label `Chromera velia`, rank `SPECIES`, direct parent `NCBITaxon:505692`, genetic code `1`, three exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 55858 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Chromera` under family `Chromeraceae`.

The side-inventory merged-ID scan found `NCBITaxon:1169474`, `NCBITaxon:348534`, `NCBITaxon:465983`, and `NCBITaxon:467753` pointing into this taxon, but no retained retired rows map to this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 114997 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55858 | Supported exactly: `attested rule: Chromera velia, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 37419 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:505693`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has exact organism rows `Go0039297` for `Chromera velia` and `Go0101170` for `Chromera velia CCAP 1602/1`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact projects `Gp0039297` and `Gp0101170` join to the two exact GOLD organism IDs. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; exact analysis `Chromera velia CCAP 1602/1` joins to project `Gp0101170`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `505693`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:505693`. |
| Empty type-material and auxiliary source surfaces | Exact scans of `data/raw/ncbi_type_material.tsv` plus the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no type-material or auxiliary source row mentions `NCBITaxon:505693`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; four side-inventory old IDs point into this taxon, but no retained retired row exists for the generator to carry into `replaces`. |

The native StrainInfo snapshot has one exact direct row and two exact deposit links under `NCBITaxon:505693`, but none overlays onto a BacDive-derived local strain inventory entry.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Chromera` parent, three exact synonyms, and two related synonyms.
- The NCBI merged-ID side inventory has four old IDs that are not present as retained retired rows, so no `replaces` entry is generated.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot supplies two exact organisms, two joined projects, and one joined analysis for this taxon.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- Type-material, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Chromera velia` as `SPECIES`, and the generated record follows the source rank exactly.
