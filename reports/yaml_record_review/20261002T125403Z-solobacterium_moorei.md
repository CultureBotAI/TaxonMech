# YAML Record Review: Solobacterium moorei

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/solobacterium_moorei.yaml
- Started UTC: 2026-10-02T12:54:03Z
- Finished UTC: 2026-10-02T12:54:03Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102148` |
| Label | `Solobacterium moorei` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:123375` |
| Parent label | `Solobacterium` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `5` |
| Source attestations | `BACDIVE`, `GOLD`, `GTDB`, `LPSN`, `MADIN`, `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/solobacterium_moorei.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/pirellula_sp_ajl36.yaml data/taxa/bacteria/solobacterium_moorei.yaml data/taxa/bacteria/ehrlichia_sp_capl.yaml data/taxa/bacteria/desulfallas_sapomandens.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 1233 lines, 9 lineage entries, 1 LPSN nomenclature entry, 1 GTDB mapping, 2 synonyms, 2 xrefs, 5 BacDive strains, 6 source attestations, and no causal graphs. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper expects a simple exact NCBI source and stopped with `NCBI source mismatch` on this multi-source species rollup. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:102148` trace to NCBI Taxonomy, LPSN, GTDB, BacDive, GOLD, MADIN, strain, assembly, related-record, and seed-scope inputs represented in the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10532 maps `NCBITaxon:102148` to `solobacterium_moorei`.
- `curation/seed_scope.tsv` row 8685 keeps this taxon in scope with an attested six-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17829 names `NCBITaxon:102148` as `Solobacterium moorei` with parent `NCBITaxon:123375`.
- `data/raw/lpsn_names.tsv` row 22920 contributes `lpsn:784913`, the LPSN name details, type-strain designations, publications, and the `INSDC:AB031056` accession.
- `data/raw/gtdb_mappings.tsv` row 1191 contributes the `GTDB:s__Bulleidia_moorei` `skos:closeMatch` mapping with 15 genomes.

## Evidence

- The YAML identifier, species rank, label, parent taxon, lineage, and genetic code agree with the NCBI Taxonomy row and snapshot 2026-09-13.
- The LPSN block at YAML lines 36-57 preserves the exact species name, Kageyama and Benno 2000 authority, correct-name status, three type-strain designations, three publications, and `INSDC:AB031056`.
- The GTDB mapping at lines 58-63 preserves `GTDB:s__Bulleidia_moorei`, `skos:closeMatch`, and `genome_count: 15`; the paired `Bulleidia moorei` synonym and GTDB xref are present at lines 64-74.
- The BacDive strain block includes five strains: the RCA59-74 type strain from `bacdive:5375`, plus `bacdive:150232`, `bacdive:155834`, `bacdive:161013`, and `bacdive:161014`.
- The RCA59-74 type strain is classified under descendant `NCBITaxon:1123263`, and the record retains genome, BioProject, BioSample, GOLD organism, GOLD project, GOLD analysis, and StrainInfo related evidence for that descendant row.
- Direct GOLD and MADIN aggregate rows exist for `NCBITaxon:102148`, matching the `GOLD` and `MADIN` source attestations at YAML lines 1215-1226.

## Completeness

- `strain_count: 5` matches the five BacDive strains materialized in the `strains` block.
- `taxonomy_mappings` contains only the GTDB species mapping because no other exact external taxonomy mapping row is present for `NCBITaxon:102148`.
- MEDIADIVE and BACTOTRAITS source attestations are absent at this species level; those source memberships are attached to the generated `NCBITaxon:1123263` descendant strain record instead.
- No top-level `genomes` or `causal_graphs` blocks are expected for this generated species record; assembly and related-record evidence is nested under matched BacDive strains.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/solobacterium_moorei.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/solobacterium_moorei.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct raw/curation exact-ID and `bacdive_5375` descendant scans after any refresh of BacDive, GTDB, GOLD, StrainInfo, or ATB source inventories.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10532 |
| `curation/seed_scope.tsv` | 8685 |
| `data/raw/ncbitaxon_taxa.tsv` | 17829 |
| `data/raw/lpsn_names.tsv` | 22920 |
| `data/raw/gtdb_mappings.tsv` | 1191 |
| `data/raw/gold_organisms.tsv` | 314 |
| `data/raw/madin_taxa.tsv` | 488 |
| `data/raw/bacdive_strains.tsv` | 5266, 72492, 78075, 83250, 83251 |
| `data/taxa/bacteria/solobacterium_moorei.yaml` | 1, 58, 77, and 1190 |

- Future corrections belong in source extraction, matching, or the seeder, not in `data/taxa/bacteria/solobacterium_moorei.yaml` directly.
