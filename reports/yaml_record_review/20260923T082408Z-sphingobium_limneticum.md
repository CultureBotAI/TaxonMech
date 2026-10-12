# YAML Record Review: Sphingobium limneticum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/sphingobium_limneticum.yaml
- Started UTC: 2026-09-23T08:22:06Z
- Finished UTC: 2026-09-23T08:24:08Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1007511 |
| label | Sphingobium limneticum |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:165695 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| strain_count | 3 |
| generated status | Generated from `data/raw/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: all 1,437 lines of `data/taxa/bacteria/sphingobium_limneticum.yaml` were read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-sphingobium_limneticum.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: exact `rg --no-ignore --hidden` checks found the NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD, Madin, BactoTraits, NCBI type-material, culture-collection, strain-genome, strain-related-record, and StrainInfo rows used by this generated record. No AllTheBacteria row was found for this taxon. |
| `just validate data/taxa/bacteria/sphingobium_limneticum.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_enrichment_culture_clone_1.yaml data/taxa/bacteria/pseudomonas_sp_enrichment_culture_clone_2.yaml data/taxa/bacteria/sphingobium_sp_300.yaml data/taxa/bacteria/sphingobium_limneticum.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The record denotes the pinned NCBI Taxonomy species `NCBITaxon:1007511`. Its label, `SPECIES` rank, parent `NCBITaxon:165695`, and bacterial genetic code `11` match `data/raw/ncbitaxon_taxa.tsv:211016`.

The NCBI lineage through `Pseudomonadati`, `Pseudomonadota`, `Alphaproteobacteria`, `Sphingomonadales`, `Sphingobiaceae`, and `Sphingobium` is consistent with the corresponding pinned NCBI inventory rows.

LPSN `lpsn:790549` maps to the same NCBI taxon and confirms the correct name, valid publication, legitimate status, type strain designations `DSM 25076` and `LMG 26659`, publications, and `INSDC:JN591313`. GTDB species `GTDB:s__Sphingobium_limneticum` maps to the same species with `skos:closeMatch` and a genome count of 8.

## Evidence

- `data/raw/lpsn_names.tsv:27491` supports the LPSN nomenclature block, the two LPSN related synonyms, type strain designations, publication identifiers, and the 16S sequence accession.
- `data/raw/gtdb_mappings.tsv:1085` supports the close GTDB species mapping and `genome_count: 8`.
- `data/raw/bacdive_strains.tsv:23076`, `data/raw/bacdive_strains.tsv:63447`, and `data/raw/bacdive_strains.tsv:63448` support the three BacDive strain records and their deposit IDs.
- `data/raw/strain_assemblies.tsv` and `data/raw/strain_genome_records.tsv` support the BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and IMG genome identifiers projected under the three strains.
- `data/raw/strain_related_records.tsv` supports the BioProject, BioSample, GOLD analysis, GOLD organism, and GOLD project related records attached to those strain-genome links.
- `data/straininfo/assemblies.tsv:7973` and `data/straininfo/related_records.tsv.gz` rows 194272-194276 support the StrainInfo genome assembly, 16S rRNA sequence, DSM/LMG deposit records, and StrainInfo strain records for `straininfo.strain:401030`.
- `data/raw/mediadive_taxa.tsv:52`, `data/raw/gold_organisms.tsv:183`, `data/raw/madin_taxa.tsv:377`, and `data/raw/bactotraits_taxa.tsv:37` match the MediaDive, GOLD, Madin, and BactoTraits source-attestation counts.
- The seeded scope text matches `curation/seed_scope.tsv:1009`: the taxon was in scope by the attested rule with eight sources including NCBI.

## Completeness

The record is complete for the available pinned evidence: it includes the NCBI/LPSN synonym and nomenclature surface, a species-level GTDB close match, all three BacDive strains, the type-strain flag on strain 301 through LPSN, all projected assembly/genome/related records for the three eligible genome-bearing deposits, and the StrainInfo records for DSM 25076 and LMG 26659.

The NCBI `typematerial.dmp` rows for `Sphingobium algicola`, `Sphingobium limneticum`, and `Sphingobium paulinellae` are present in `data/raw/ncbi_type_material.tsv`, but TaxonMech currently derives nomenclature and `is_type_strain` from LPSN, not from NCBI type material alone; the omissions are therefore expected.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If upstream inventories for `NCBITaxon:1007511`, `lpsn:790549`, `GTDB:s__Sphingobium_limneticum`, or `straininfo.strain:401030` change, rerun `just seed-canary NCBITaxon:1007511`, inspect `data/taxa/bacteria/sphingobium_limneticum.yaml`, and rerun `just validate-strict data/taxa/bacteria/sphingobium_limneticum.yaml`.

## Additional Notes

- External live NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD, and StrainInfo lookups were not used in this environment; the pinned `2026-09-13` local inventories are the reviewed source of truth.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
