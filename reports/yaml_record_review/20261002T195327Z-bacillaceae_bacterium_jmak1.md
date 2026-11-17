# YAML Record Review: Bacillaceae bacterium JMAK1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/bacillaceae_bacterium_jmak1.yaml
- Started UTC: 2026-10-02T19:53:27Z
- Finished UTC: 2026-10-02T19:53:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1028381` |
| Label | `Bacillaceae bacterium JMAK1` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:197483` |
| Parent label | `unclassified Bacillaceae` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `GTDB`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/bacillaceae_bacterium_jmak1.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/methylomonas_sp_m5.yaml data/taxa/bacteria/methylococcaceae_bacterium_m200.yaml data/taxa/bacteria/bacillaceae_bacterium_jmak1.yaml data/taxa/bacteria/algoriphagus_sp_ak10.yaml data/taxa/bacteria/streptomyces_sp_mds.yaml` | Pass: the strict five-file batch scanned 5 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 75 lines, 9 lineage entries, 1 synonym, 1 xref, 1 taxonomy mapping, 0 declared strains, 0 genome assemblies, and 3 source attestations. |
| Direct bounded-source fallback | Pass: found one seed row, one first-column NCBI Taxonomy row, one GTDB mapping row, one MADIN aggregate row, one legacy page row, all 9 first-column lineage rows, and no auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: ignored-file-inclusive source scans found `ncbitaxon_taxa.tsv`, `gtdb_mappings.tsv`, `madin_taxa.tsv`, `legacy_page_paths.tsv`, and `seed_scope.tsv` rows for `NCBITaxon:1028381`, with no exact `data/straininfo` or `data/atb` rows. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 11300 maps `NCBITaxon:1028381` to `bacillaceae_bacterium_jmak1`.
- `curation/seed_scope.tsv` row 36100 keeps this taxon in scope with an NCBI plus GTDB plus MADIN rule.
- `data/raw/ncbitaxon_taxa.tsv` row 219130 names `NCBITaxon:1028381` as `Bacillaceae bacterium JMAK1`, under `NCBITaxon:197483` / `unclassified Bacillaceae`.
- `data/raw/gtdb_mappings.tsv` row 1224 maps `GTDB:s__Geomicrobium_A_sp012970285` to `NCBITaxon:1028381` with `skos:closeMatch` and one genome.
- `data/raw/madin_taxa.tsv` row 520 contributes five trait assertions, and `curation/legacy_page_paths.tsv` row 658 records the generated page route.
- The generated YAML line 1 preserves the NCBI identifier; lines 36, 46, and 48 preserve the GTDB mapping, synonym, and xref; and lines 53, 59, and 65 preserve the three source IDs.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The GTDB `skos:closeMatch` row is reflected in both `taxonomy_mappings` and `xrefs`, and the GTDB species label is normalized into one exact synonym.
- The MADIN aggregate row is reflected as one source attestation with 5 `TRAIT_ASSERTION` assertions.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:197483` / `unclassified Bacillaceae`.

## Completeness

- The record is complete for the exact NCBI, GTDB, and MADIN rows currently present for this species taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- No explicit genome assemblies, genome records, related records, or causal graphs are expected for the current source set.
- The `GTDB` and `MADIN` source attestations are the only non-NCBI evidence currently linked to `NCBITaxon:1028381`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/bacillaceae_bacterium_jmak1.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/bacillaceae_bacterium_jmak1.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 11300, `curation/seed_scope.tsv` row 36100, `data/raw/ncbitaxon_taxa.tsv` row 219130, `data/raw/gtdb_mappings.tsv` row 1224, `data/raw/madin_taxa.tsv` row 520, `curation/legacy_page_paths.tsv` row 658, and YAML lines 1, 36, 46, 48, 53, 59, and 65.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/bacillaceae_bacterium_jmak1.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/bacillaceae_bacterium_jmak1.yaml` directly.
