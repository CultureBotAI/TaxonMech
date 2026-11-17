# YAML Record Review: Chaetomium cochliodes

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/chaetomium_cochliodes.yaml
- Started UTC: 2026-09-22T08:32:00Z
- Finished UTC: 2026-09-22T08:32:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:904709 |
| label | Chaetomium cochliodes |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5149 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/chaetomium_cochliodes.yaml`. It carries one NCBI exact synonym, four NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 \( -name '*chaetocladium_jonesii.md' -o -name '*chaetomidium_leptoderma.md' -o -name '*chaetomium_cochliodes.md' -o -name '*chaetomium_fimeti.md' \) -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/chaetomium_cochliodes.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/chaetomium_cochliodes.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 190618 has `NCBITaxon:904709`, label `Chaetomium cochliodes`, rank `SPECIES`, direct parent `NCBITaxon:5149`, genetic code `1`, one exact synonym, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 56864 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Chaetomium` under family `Chaetomiaceae`.

The side-inventory merged-ID scan found `NCBITaxon:1131550` and `NCBITaxon:1795768` pointing into this taxon, but no retained retired row maps to this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 190618 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 56864 | Supported exactly: `attested rule: Chaetomium cochliodes, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 44142 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:904709`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has one exact organism row, `Go0373715` for `Chaetomium cochliodes CCM F-232`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact project `Gp0220883` joins to `Go0373715`. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; no native analysis row joins to `Gp0220883` in the local snapshot. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with two `culture from epitype` rows and two `epitype` rows on lines 271964-271967. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `904709`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:904709`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:904709`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; side-inventory old IDs `NCBITaxon:1131550` and `NCBITaxon:1795768` point into this taxon, but no retained retired rows exist for the generator to carry into `replaces`. |

The NCBI type-material inventory contributes `CBS 155.52` culture-from-epitype variants and `HMAS 244354` epitype variants. The native StrainInfo snapshot has 31 exact direct rows and 46 exact deposit links under `NCBITaxon:904709`, but none overlays onto a BacDive-derived local strain inventory entry.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Chaetomium` parent, one exact synonym, four related synonyms, and four type-material rows.
- The NCBI merged-ID side inventory has two old IDs that are not present as retained retired rows, so no `replaces` entry is generated.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, one joined project, and no joined analyses for this taxon.
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
- NCBI ranks `Chaetomium cochliodes` as `SPECIES`, and the generated record follows the source rank exactly.

