# YAML Record Review: Beggiatoa alba

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/beggiatoa_alba.yaml
- Started UTC: 2026-10-02T12:56:22Z
- Finished UTC: 2026-10-02T12:56:22Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1022` |
| Label | `Beggiatoa alba` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:1021` |
| Parent label | `Beggiatoa` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `2` |
| Source attestations | `BACDIVE`, `BACTOTRAITS`, `GOLD`, `LPSN`, `MADIN`, `MEDIADIVE`, `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/beggiatoa_alba.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/beggiatoa_alba.yaml data/taxa/bacteria/helicobacter_sp_va.yaml data/taxa/bacteria/bacterium_i1.yaml data/taxa/bacteria/thermus_sp_env_os_ac7.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 386 lines, 9 lineage entries, 1 LPSN nomenclature entry, 6 synonyms, 2 xrefs, 2 BacDive strains, 7 source attestations, and no causal graphs. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper expects a simple exact NCBI source and stopped with `NCBI source mismatch` on this multi-source species rollup. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:1022` trace to NCBI Taxonomy, LPSN, BacDive, MediaDive, GOLD, MADIN, BactoTraits, strain, related-record, and seed-scope inputs represented in the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10535 maps `NCBITaxon:1022` to `beggiatoa_alba`.
- `curation/seed_scope.tsv` row 5181 keeps this taxon in scope with an attested seven-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 794 names `NCBITaxon:1022` as `Beggiatoa alba` with parent `NCBITaxon:1021`.
- `data/raw/lpsn_names.tsv` row 15751 contributes `lpsn:773996`, the LPSN name details, the ATCC 33555 type-strain designation, the species xrefs, and the `INSDC:AF110274` accession.
- `data/raw/bacdive_strains.tsv` rows 16890 and 91121 contribute the two generated BacDive strains.

## Evidence

- The YAML identifier, species rank, label, parent taxon, lineage, and genetic code agree with the NCBI Taxonomy row and snapshot 2026-09-13.
- The LPSN block at YAML lines 36-53 preserves the exact species name, Vaucher/Trevisan authority, lectotype/correct-name status, ATCC 33555 type-strain designation, publication, and `INSDC:AF110274`.
- The synonym block preserves all six NCBI synonyms: three related quoted or authority-bearing names and three exact unquoted names.
- The LSU B18LD strain from `bacdive:168888` is represented as the ATCC 33555 type strain and carries the GOLD assembly, organism, project, BioProject, BioSample, and StrainInfo evidence tied to descendant `NCBITaxon:395493`.
- The B15LD strain from `bacdive:17076` is represented with `kgmicrobe.strain:DSM-1416` and StrainInfo nucleotide, deposit, and strain related records.
- Direct MediaDive, GOLD, MADIN, and BactoTraits aggregate rows exist for `NCBITaxon:1022`, matching the corresponding source attestations at YAML lines 356-379.

## Completeness

- `strain_count: 2` matches the two BacDive strains materialized in the `strains` block.
- `taxonomy_mappings` is absent because no exact GTDB mapping row is currently present for `NCBITaxon:1022`; the GTDB species token is retained as an xref from LPSN.
- No top-level `genomes` or `causal_graphs` blocks are expected for this generated species record; assembly, genome, and related-record evidence is nested under the matched ATCC 33555 strain.
- The NCBI type-material rows for ATCC 33555 and B18LD are represented through the normalized LPSN/BacDive type-strain evidence rather than as separate duplicate strains.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/beggiatoa_alba.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/beggiatoa_alba.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct raw/curation exact-ID and Beggiatoa strain scans after any refresh of BacDive, LPSN, GOLD, MediaDive, MADIN, BactoTraits, or StrainInfo source inventories.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10535 |
| `curation/seed_scope.tsv` | 5181 |
| `data/raw/ncbitaxon_taxa.tsv` | 794 |
| `data/raw/lpsn_names.tsv` | 15751 |
| `data/raw/bacdive_strains.tsv` | 16890 and 91121 |
| `data/raw/gold_organisms.tsv` | 316 |
| `data/raw/mediadive_taxa.tsv` | 74 |
| `data/raw/madin_taxa.tsv` | 490 |
| `data/raw/bactotraits_taxa.tsv` | 53 |
| `data/taxa/bacteria/beggiatoa_alba.yaml` | 1, 36, 78, and 338 |

- Future corrections belong in source extraction, matching, or the seeder, not in `data/taxa/bacteria/beggiatoa_alba.yaml` directly.
