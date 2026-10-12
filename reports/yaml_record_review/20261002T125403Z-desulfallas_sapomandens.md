# YAML Record Review: Desulfallas sapomandens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/desulfallas_sapomandens.yaml
- Started UTC: 2026-10-02T12:54:03Z
- Finished UTC: 2026-10-02T12:54:03Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102170` |
| Label | `Desulfallas sapomandens` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:2282740` |
| Parent label | `Desulfallas` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `1` |
| Source attestations | `BACDIVE`, `BACTOTRAITS`, `GOLD`, `LPSN`, `MADIN`, `MEDIADIVE`, `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/desulfallas_sapomandens.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/pirellula_sp_ajl36.yaml data/taxa/bacteria/solobacterium_moorei.yaml data/taxa/bacteria/ehrlichia_sp_capl.yaml data/taxa/bacteria/desulfallas_sapomandens.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 277 lines, 9 lineage entries, 1 LPSN nomenclature entry, 4 synonyms, 1 xref, 1 BacDive strain, 7 source attestations, and no causal graphs. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper expects a simple exact NCBI source and stopped with `NCBI source mismatch` on this multi-source species rollup. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:102170` trace to NCBI Taxonomy, LPSN, BacDive, MediaDive, GOLD, MADIN, BactoTraits, strain, related-record, and seed-scope inputs represented in the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10534 maps `NCBITaxon:102170` to `desulfallas_sapomandens`.
- `curation/seed_scope.tsv` row 5893 keeps this taxon in scope with an attested seven-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17831 names `NCBITaxon:102170` as `Desulfallas sapomandens` with parent `NCBITaxon:2282740`.
- `data/raw/lpsn_names.tsv` row 33524 contributes `lpsn:798405`, the LPSN name details, type-strain designations, publications, `INSDC:AF168365`, and the `lpsn:775641` synonym.
- `data/raw/bacdive_strains.tsv` row 11648 contributes the single BacDive strain, `bacdive:11802`.

## Evidence

- The YAML identifier, species rank, label, parent taxon, lineage, and genetic code agree with the NCBI Taxonomy row and snapshot 2026-09-13.
- The LPSN block at YAML lines 36-56 preserves the exact species name, Watanabe et al. 2018 authority, correct-name status, two type-strain designations, three publications, and `INSDC:AF168365`.
- The synonym block preserves one LPSN synonym for `Desulfotomaculum sapomandens` and three NCBI synonyms for the current and former names.
- The single BacDive strain is `bacdive:11802`, designation `Pato`, with `kgmicrobe.strain:DSM-3223` and `kgmicrobe.strain:NBRC-112755` culture-collection ids and `is_type_strain: true`.
- The GOLD related records retain `gold:Go0028498` for DSM 3223 and `gold:Go0613617` for NBRC 112755, while StrainInfo related records retain DSM 3223 sequence, deposit, and strain evidence.
- Direct MediaDive, MADIN, and BactoTraits aggregate rows exist for `NCBITaxon:102170`, matching the `MEDIADIVE`, `MADIN`, and `BACTOTRAITS` source attestations at YAML lines 251-270.

## Completeness

- `strain_count: 1` matches the single BacDive strain materialized in the `strains` block.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping row is currently present for `NCBITaxon:102170`.
- No genome assemblies, top-level `genomes`, or `causal_graphs` blocks are expected for this generated species record; the current source evidence consists of nomenclature, strain, GOLD organism, StrainInfo, medium, and trait-assertion rows.
- The NCBI type-material rows for DSM 3223, NBRC 112755, and Pato are represented through the normalized BacDive/LPSN type-strain evidence rather than as separate duplicate strains.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/desulfallas_sapomandens.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/desulfallas_sapomandens.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct raw/curation exact-ID source scan after any refresh of BacDive, LPSN, GOLD, MediaDive, MADIN, BactoTraits, or StrainInfo source inventories.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10534 |
| `curation/seed_scope.tsv` | 5893 |
| `data/raw/ncbitaxon_taxa.tsv` | 17831 |
| `data/raw/lpsn_names.tsv` | 33524 |
| `data/raw/bacdive_strains.tsv` | 11648 |
| `data/raw/gold_organisms.tsv` | 315 |
| `data/raw/mediadive_taxa.tsv` | 73 |
| `data/raw/madin_taxa.tsv` | 489 |
| `data/raw/bactotraits_taxa.tsv` | 52 |
| `data/taxa/bacteria/desulfallas_sapomandens.yaml` | 1, 36, 77, and 233 |

- Future corrections belong in source extraction, matching, or the seeder, not in `data/taxa/bacteria/desulfallas_sapomandens.yaml` directly.
