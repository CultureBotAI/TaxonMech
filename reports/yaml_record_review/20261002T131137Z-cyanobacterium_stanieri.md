# YAML Record Review: Cyanobacterium stanieri

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/cyanobacterium_stanieri.yaml
- Started UTC: 2026-10-02T13:11:37Z
- Finished UTC: 2026-10-02T13:11:37Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102235` |
| Label | `Cyanobacterium stanieri` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:102234` |
| Parent label | `Cyanobacterium` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `GOLD`, `MADIN`, `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/cyanobacterium_stanieri.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/cyanobacterium_stanieri.yaml data/taxa/bacteria/uncultured_bacterium_rbz_a.yaml data/taxa/bacteria/uncultured_bacterium_wekr_b.yaml data/taxa/bacteria/uncultured_bacterium_wekr_c.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 76 lines, 11 lineage entries, 2 NCBI synonyms, 0 xrefs, 0 taxonomy mappings, 0 declared strains, 0 genome assemblies, 3 source attestations, and no causal graphs. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper expects a simple exact NCBI source and is not applicable to this multi-source species record with NCBI type-material rows. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: exact source rows for `NCBITaxon:102235` trace to NCBI Taxonomy, NCBI type material, GOLD, MADIN, and seed-scope inputs represented in the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10555 maps `NCBITaxon:102235` to `cyanobacterium_stanieri`.
- `curation/seed_scope.tsv` row 31669 keeps this taxon in scope with an attested three-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17853 names `NCBITaxon:102235` as `Cyanobacterium stanieri` with parent `NCBITaxon:102234`.
- `data/raw/gold_organisms.tsv` row 321 and `data/raw/madin_taxa.tsv` row 494 provide direct aggregate source support for the GOLD and MADIN source attestations.

## Evidence

- The YAML identifier, species rank, label, parent taxon, lineage, and genetic code agree with the NCBI Taxonomy row and snapshot 2026-09-13.
- The two NCBI synonym rows in YAML lines 42-48 preserve both `Cyanobacterium stanieri` authored-name variants from the source row.
- The `GOLD` source attestation at YAML lines 58-63 preserves the exact direct aggregate count of 1 organism row.
- The `MADIN` source attestation at YAML lines 64-69 preserves the exact direct aggregate count of 3 trait assertions.

## Completeness

- `strain_count: 0` is consistent with the generated species record's absence of top-level `strains` and exact BacDive, culture-collection, ATB, or StrainInfo rows.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping row is currently present for `NCBITaxon:102235`.
- No top-level `xrefs`, `genomes`, or `causal_graphs` blocks are expected for this generated species record.
- The review accounts for the two NCBI type-material rows for PCC 7202; the current seeder does not materialize those rows as strain objects without a strain-source row.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/cyanobacterium_stanieri.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/cyanobacterium_stanieri.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct raw/curation exact-ID source scan after any refresh of NCBI Taxonomy, NCBI type material, GOLD, or MADIN source inventories.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10555 |
| `curation/seed_scope.tsv` | 31669 |
| `data/raw/ncbitaxon_taxa.tsv` | 17853 |
| `data/raw/gold_organisms.tsv` | 321 |
| `data/raw/madin_taxa.tsv` | 494 |
| `data/raw/ncbi_type_material.tsv` | 1301 and 1302 |
| `data/taxa/bacteria/cyanobacterium_stanieri.yaml` | 1, 42, and 51 |

- NCBI child-strain rows that name `NCBITaxon:102235` as their parent are descendant taxa, not direct source attestations for this generated species record.
- Future corrections belong in source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/cyanobacterium_stanieri.yaml` directly.
