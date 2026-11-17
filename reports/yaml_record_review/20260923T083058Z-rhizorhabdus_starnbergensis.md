# YAML Record Review: Rhizorhabdus starnbergensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/rhizorhabdus_starnbergensis.yaml
- Started UTC: 2026-09-23T08:28:42Z
- Finished UTC: 2026-09-23T08:30:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1007516 |
| label | Rhizorhabdus starnbergensis |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:1649486 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| strain_count | 1 |
| generated status | Generated from `data/raw/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: all 300 lines of `data/taxa/bacteria/rhizorhabdus_starnbergensis.yaml` were read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-rhizorhabdus_starnbergensis.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: exact `rg --no-ignore --hidden` checks found the NCBI, LPSN, BacDive, MediaDive, GOLD, Madin, BactoTraits, NCBI type-material, culture-collection, strain-related-record, and StrainInfo rows used by this generated record across `data/raw/`, `data/atb/`, and `data/straininfo/`. No AllTheBacteria row was found for this taxon. |
| `just validate data/taxa/bacteria/rhizorhabdus_starnbergensis.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/rhizorhabdus_starnbergensis.yaml data/taxa/bacteria/sphingomonas_sp_454.yaml data/taxa/bacteria/sphingomonas_sp_721.yaml data/taxa/bacteria/sphingopyxis_sp_1319.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The record denotes the pinned NCBI Taxonomy species `NCBITaxon:1007516`. Its label, `SPECIES` rank, parent `NCBITaxon:1649486`, and bacterial genetic code `11` match `data/raw/ncbitaxon_taxa.tsv:211021`.

The root-first lineage through `Pseudomonadati`, `Pseudomonadota`, `Alphaproteobacteria`, `Sphingomonadales`, `Rhizorhabdaceae`, and `Rhizorhabdus` is consistent with the corresponding pinned NCBI inventory rows.

LPSN `lpsn:11124` maps to the same NCBI taxon and confirms the current correct name, valid publication, legitimate status, type strain designations `DSM 25077` and `LMG 26763`, publications, and `INSDC:JN591314`. LPSN `lpsn:790567` supplies the old name `Sphingomonas starnbergensis` as a synonym, while the record's exact NCBI synonym and related NCBI synonyms mirror the raw NCBI synonym columns.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:211021` supports the NCBI identifier, label, rank, parent, genetic code, NCBI exact synonym `Sphingomonas starnbergensis`, and three NCBI related synonyms.
- `data/raw/lpsn_names.tsv:2293` supports the LPSN nomenclature block, the LPSN xref, the type strain designations, the three publication identifiers, and `INSDC:JN591314`.
- `data/raw/lpsn_names.tsv:27509` supports the LPSN related synonym `Sphingomonas starnbergensis`, its older authority string, and its link back to `lpsn:11124`.
- `data/raw/bacdive_strains.tsv:23085` supports the single BacDive strain `bacdive:23281`, its `382` designation, and its `DSM-25077` and `LMG-26763` culture-collection IDs.
- `data/raw/culture_collection_strains.tsv:73606` and `data/raw/culture_collection_strains.tsv:126514` support the DSM and LMG deposit identifiers attached to this NCBI taxon.
- `data/raw/strain_related_records.tsv:316630` through `data/raw/strain_related_records.tsv:316637` support the GOLD analysis, organism, and project related records attached to BacDive strain `kgmicrobe.strain:bacdive_23281`.
- `data/straininfo/strain_links.tsv:80880` and `data/straininfo/strain_links.tsv:80881` support the StrainInfo LMG and DSM deposit records and the two projected StrainInfo strain records.
- `data/raw/mediadive_taxa.tsv:53`, `data/raw/gold_organisms.tsv:184`, `data/raw/madin_taxa.tsv:378`, and `data/raw/bactotraits_taxa.tsv:38` match the MediaDive, GOLD, Madin, and BactoTraits source-attestation counts.

## Completeness

The record is complete for the available pinned evidence: it includes the NCBI/LPSN synonym and nomenclature surface, the LPSN-backed type-strain flag, the single BacDive strain with both LPSN type-strain deposits, all projected GOLD related records, both StrainInfo deposits, and the source-attestation counts from the available local inventories.

No GTDB taxonomy mapping is present, and the gitignore-independent search over `data/raw/`, `data/atb/`, and `data/straininfo/` found no GTDB or AllTheBacteria same-taxon row to project. The NCBI `typematerial.dmp` rows for `Sphingomonas starnbergensis` are present in `data/raw/ncbi_type_material.tsv`, but TaxonMech currently derives nomenclature and `is_type_strain` from LPSN, not from NCBI type material alone.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If upstream inventories for `NCBITaxon:1007516`, `lpsn:11124`, `lpsn:790567`, `bacdive:23281`, or `straininfo.strain:379147` change, rerun `just seed-canary NCBITaxon:1007516`, inspect `data/taxa/bacteria/rhizorhabdus_starnbergensis.yaml`, and rerun `just validate-strict data/taxa/bacteria/rhizorhabdus_starnbergensis.yaml`.

## Additional Notes

- External live NCBI, LPSN, BacDive, MediaDive, GOLD, and StrainInfo lookups were not used in this environment; the pinned `2026-09-13` local inventories are the reviewed source of truth.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
