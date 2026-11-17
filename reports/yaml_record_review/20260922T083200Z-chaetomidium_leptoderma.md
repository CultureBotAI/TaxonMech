# YAML Record Review: Chaetomidium leptoderma

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/chaetomidium_leptoderma.yaml
- Started UTC: 2026-09-22T08:32:00Z
- Finished UTC: 2026-09-22T08:32:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:669021 |
| label | Chaetomidium leptoderma |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:223383 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/chaetomidium_leptoderma.yaml`. It carries two NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 \( -name '*chaetocladium_jonesii.md' -o -name '*chaetomidium_leptoderma.md' -o -name '*chaetomium_cochliodes.md' -o -name '*chaetomium_fimeti.md' \) -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/chaetomidium_leptoderma.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/chaetomidium_leptoderma.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 155006 has `NCBITaxon:669021`, label `Chaetomidium leptoderma`, rank `SPECIES`, direct parent `NCBITaxon:223383`, genetic code `1`, two exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 56323 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Chaetomidium` under family `Chaetomiaceae`.

The side-inventory merged-ID scan found `NCBITaxon:95316` pointing into this taxon, but no retained retired row maps to this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 155006 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 56323 | Supported exactly: `attested rule: Chaetomidium leptoderma, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 40867 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:669021`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has one exact organism row, `Go0382590` for `Chaetomidium leptoderma CBS 538.74`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact project `Gp0223620` joins to `Go0382590`. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; no native analysis row joins to `Gp0223620` in the local snapshot. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with four `type material` rows on lines 249188-249191. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `669021`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:669021`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:669021`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; side-inventory old ID `NCBITaxon:95316` points into this taxon, but no retained retired row exists for the generator to carry into `replaces`. |

The NCBI type-material inventory contributes CBS 538.74 and IMI 054770 spelling variants under the source taxon name `Thielavia leptoderma`. The native StrainInfo snapshot has one exact direct row and two exact deposit links under `NCBITaxon:669021`, but none overlays onto a BacDive-derived local strain inventory entry.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Chaetomidium` parent, two exact synonyms, two related synonyms, and four type-material rows.
- The NCBI merged-ID side inventory has one old ID that is not present as a retained retired row, so no `replaces` entry is generated.
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
- NCBI ranks `Chaetomidium leptoderma` as `SPECIES`, and the generated record follows the source rank exactly.

