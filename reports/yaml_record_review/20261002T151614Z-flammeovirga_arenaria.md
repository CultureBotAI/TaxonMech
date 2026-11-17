# YAML Record Review: Flammeovirga arenaria

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/flammeovirga_arenaria.yaml
- Started UTC: 2026-10-02T15:16:14Z
- Finished UTC: 2026-10-02T15:16:14Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1025` |
| Label | `Flammeovirga arenaria` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:59739` |
| Parent label | `Flammeovirga` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Lineage entries | `11` |
| Nomenclature blocks | `1` |
| Synonyms | `3` NCBI Taxonomy synonyms |
| Xrefs | `1` |
| Declared strains | `1` |
| Culture collection IDs | `10` |
| Nested related records | `25` |
| Source attestations | `NCBITAXON`, `LPSN`, `BACDIVE`, `MEDIADIVE`, `GOLD`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/flammeovirga_arenaria.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/rhizosphere_soil_bacterium_rsc_ii_90.yaml data/taxa/bacteria/flammeovirga_arenaria.yaml` | Pass: the strict two-file batch scanned 2 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 550 lines, 11 lineage entries, 3 NCBI synonyms, 1 LPSN nomenclature block, 1 xref, 1 declared BacDive type strain, and 6 source attestations. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: the helper reported `NCBI source mismatch` on this complex multi-source rollup; exact direct source scans were used instead. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct exact-ID source scans | Pass: NCBI, LPSN, BacDive, MediaDive, GOLD, Madin, culture-collection, NCBI type-material, GOLD related-record, and StrainInfo source rows matched the generated YAML evidence. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10730 maps `NCBITaxon:1025` to `flammeovirga_arenaria`.
- `curation/seed_scope.tsv` row 9165 keeps this species in scope with six source families, including NCBI Taxonomy.
- `data/raw/ncbitaxon_taxa.tsv` row 796 grounds `NCBITaxon:1025` as the exact species `Flammeovirga arenaria`, with parent `NCBITaxon:59739`, genetic code `11`, and NCBI aliases for `Microscilla arenaria`.
- `curation/legacy_page_paths.tsv` row 625 preserves the legacy generated page path.
- The generated YAML line 1 preserves the NCBI identifier, line 42 starts LPSN nomenclature, line 66 starts NCBI synonyms, line 80 starts the BacDive strain block, and line 511 starts the six source attestations.

## Nomenclature

- `data/raw/lpsn_names.tsv` row 23359 carries `lpsn:785441`, the `(ex Lewin 1969) Takahashi et al. 2006` authority, legitimate/validly-published/correct-name flags, five LPSN type-strain designations, two DOI publications plus `PMID:16957105`, and the `INSDC:AB078078` sequence accession.
- The YAML preserves `lpsn:785441` both in the LPSN nomenclature block and as the sole top-level xref.
- The three NCBI Taxonomy synonyms in the YAML are the exact NCBI synonym set from `data/raw/ncbitaxon_taxa.tsv` row 796.

## Strain Evidence

- `data/raw/bacdive_strains.tsv` row 53459 provides the sole BacDive strain, `bacdive:131148`, which is marked as a type strain and carries ten culture-collection IDs.
- `data/raw/culture_collection_strains.tsv` has one exact row for each declared culture-collection ID: ATCC 23161, CIP 109101, DSM 28230, IAM 15329, IFO 15982 in both encoded and normalized forms, JCM 21777, LMG 13024, NBRC 15982, and NCIMB 1413.
- `data/raw/ncbi_type_material.tsv` rows 1303-1310 provide eight NCBI type-material spellings for CIP 109101, IFO 15982, JCM 21777, and NBRC 15982.
- `data/raw/strain_related_records.tsv` rows 53728-53735 provide eight GOLD organism links for Go0617427 through Go0617430, with culture-collection and organism-strain matches.
- `data/straininfo/strain_links.tsv` rows 11090-11097 provide eight exact StrainInfo deposit rows for `straininfo.strain:10155`; the generated strain block carries eight `STRAININFO_DEPOSIT` records, eight `STRAININFO_STRAIN` records, and one `NUCLEOTIDE_SEQUENCE` record for `INSDC:AB681015`.

## Source Attestations

- `NCBITAXON`, `LPSN`, and `BACDIVE` each contribute one assertion for the NCBI name, the LPSN name, and the BacDive strain, respectively.
- `MEDIADIVE` contributes two medium assertions through `data/raw/mediadive_taxa.tsv` row 77.
- `GOLD` contributes five organism assertions through `data/raw/gold_organisms.tsv` row 322.
- `MADIN` contributes two trait assertions through `data/raw/madin_taxa.tsv` row 495.

## Completeness

- The top-level taxonomy, genetic code, synonyms, LPSN nomenclature, xref, BacDive type strain, GOLD organism links, and StrainInfo nested records are all explained by exact source rows.
- `taxonomy_mappings`, top-level `related_records`, `genomes`, and `causal_graphs` are absent because the current exact source rows do not provide GTDB mappings, standalone genome records, or curated causal graphs for `NCBITaxon:1025`.
- The direct absence and source checks used `--no-ignore --hidden`, so ignored files were included.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/flammeovirga_arenaria.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/flammeovirga_arenaria.yaml`.
- Re-run exact direct scans after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.
- Re-run `just verify-corpus`.

## Additional Notes

- Reviewed row anchors: `data/taxa/PATHS.tsv` row 10730, `curation/seed_scope.tsv` row 9165, `data/raw/ncbitaxon_taxa.tsv` row 796, `data/raw/lpsn_names.tsv` row 23359, `data/raw/bacdive_strains.tsv` row 53459, and `data/straininfo/strain_links.tsv` rows 11090-11097.
- The generated record has no top-level `taxonomy_mappings`, `genomes`, or `causal_graphs` blocks.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, `data/straininfo/`, or the seeder, not in `data/taxa/bacteria/flammeovirga_arenaria.yaml` directly.
