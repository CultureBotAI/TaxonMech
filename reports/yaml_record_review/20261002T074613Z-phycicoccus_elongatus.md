# YAML Record Review: Phycicoccus elongatus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/phycicoccus_elongatus.yaml
- Started UTC: 2026-10-02T07:46:13Z
- Finished UTC: 2026-10-02T07:46:13Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:101689` |
| Label | `Phycicoccus elongatus` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:367298` / `Phycicoccus` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Primary nomenclature | `lpsn:798255` |
| GTDB mapping | `GTDB:s__Phycicoccus_A_elongatus` |
| BacDive strain | `kgmicrobe.strain:bacdive_6298` / `bacdive:6298` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/phycicoccus_elongatus.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/enterobacter_sp_12r.yaml data/taxa/bacteria/phycicoccus_elongatus.yaml data/taxa/bacteria/enterobacter_sp_28r.yaml data/taxa/bacteria/enterobacter_sp_59t.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 559 lines, 9 lineage entries, 1 nomenclature entry, 1 GTDB mapping, 5 synonyms, 2 xrefs, 1 strain, and 8 source attestations. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1016889\|101689\|1016890\|1016891)([^0-9]\|$)' data curation` | Pass: found the exact species row, the exact strain-child row, source aggregate rows, StrainInfo rows, GOLD rows, `PATHS.tsv`, `seed_scope.tsv`, and this YAML. |
| `rg --no-ignore --hidden -n 'NCBITaxon:101689([^0-9]\|$)' data/atb` | Pass: found no AllTheBacteria rows for the exact taxon. |
| Bounded NCBITaxon-only helper | Not applicable: `taxonmech_bounded_scan.py` exited with `NCBI source mismatch` because the raw NCBI row advertises `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, and that helper is intentionally limited to NCBITaxon-only records. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*phycicoccus_elongatus.md'` | Pass: no prior report existed for this stem. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` maps `NCBITaxon:101689` to `phycicoccus_elongatus`.
- `curation/seed_scope.tsv` row 2029 keeps the species in scope as an 8-source NCBI-backed seed.
- `data/raw/ncbitaxon_taxa.tsv` row 17643 names `NCBITaxon:101689` as `Phycicoccus elongatus`, a species under `NCBITaxon:367298`, with genetic code 11.
- The nine-entry `lineage` is root-first and stops at the NCBI parent genus `Phycicoccus`.
- `nomenclature[0]` maps LPSN `lpsn:798255` to the same species name, records `(Hanada et al. 2002) Nouioui et al. 2018`, and carries LPSN's correct-name, validly-published, and legitimate flags.
- `GTDB:s__Phycicoccus_A_elongatus` is kept as `skos:closeMatch`, which is conservative for GTDB's `Phycicoccus_A` split rather than overclaiming exact nomenclatural identity.

## Evidence

- The LPSN row at `data/raw/lpsn_names.tsv:33396` supports `lpsn:798255`, the three LPSN type-strain designations, synonym `Tetrasphaera elongata`, DOI and PMID publication references, and sequence accession `INSDC:AB030911`.
- The NCBI type-material rows 1067 through 1074 support the same type-material cluster for `DSM 14184`, `JCM 11141`, `NBRC 103079`, and `Lp2`.
- `data/raw/gtdb_mappings.tsv:1169` supports the close GTDB mapping and 24-genome count.
- `data/raw/bacdive_strains.tsv:6182` supports the BacDive `Lp2` strain, `bacdive:6298`, type-strain flag, and eight culture-collection identifiers.
- The BacDive and GOLD assembly/genome evidence stays under the BacDive strain: 2 `genome_assemblies`, 3 `genome_records`, and 22 `related_records`.
- The StrainInfo records all trace to `straininfo.strain:100994` and preserve their deposit IDs, deposit status, `DOI:10.60712/SI-ID100994.3`, match method, and BacDive cross-reference.
- The GOLD related records preserve `Go`, `Gp`, and `Ga` identifiers as typed related records rather than presenting them as genome identifiers.
- The child strain record `data/taxa/bacteria/phycicoccus_elongatus_lp2.yaml` represents `NCBITaxon:1193181`; the species record links to that NCBI strain only through strain-scoped assemblies and related records.

## Completeness

- All eight source attestation families in the raw NCBI row are reflected in `source_attestations`.
- The record has one BacDive strain, which matches the BacDive inventory for this species.
- The source aggregate rows for MediaDive, GOLD, MADIN, and BactoTraits are retained as source attestations; they do not require this generated TaxonRecord to inline media or trait assertions.
- No AllTheBacteria rows were found for the exact taxon in an ignored-inclusive `data/atb` scan.
- No causal graph is expected for this generated taxon-only record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/phycicoccus_elongatus.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/phycicoccus_elongatus.yaml`.
- Re-run exact source scans for `NCBITaxon:101689`, `lpsn:798255`, `GTDB:s__Phycicoccus_A_elongatus`, `bacdive:6298`, `gold:*`, and `straininfo.strain:100994` after any upstream refresh.
- Re-run `just verify-corpus` if this record is ever regenerated.

## Additional Notes

- The source scans used `--no-ignore --hidden`, so ignored files were included.
- The apparent `Phycicoccus` versus `Tetrasphaera` name split is explicitly represented as synonyms and LPSN nomenclature rather than silently normalized away.
- GOLD rows for `JCM 11141` and `DSM 14184` appear twice where the source matched both culture-collection and strain fields; retaining both rows preserves the evidence path.
- The public StrainInfo DOI is recorded as a provenance pointer for `straininfo.strain:100994`, not as a publication supporting a new species-level assertion.
- Future corrections belong in source inventories, source matching code, or the seeder; the generated YAML should not be edited directly.
