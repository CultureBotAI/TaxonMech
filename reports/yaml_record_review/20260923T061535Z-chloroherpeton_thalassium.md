# YAML Record Review: Chloroherpeton thalassium

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/chloroherpeton_thalassium.yaml
- Started UTC: 2026-09-23T06:15:35Z
- Finished UTC: 2026-09-23T06:15:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | NCBITaxon:100716 |
| Label | Chloroherpeton thalassium |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:100715, Chloroherpeton |
| Maintained path | data/taxa/bacteria/chloroherpeton_thalassium.yaml |
| Generation status | Generated from `data/raw/`, `data/straininfo/`, and the committed catalog overlays by `seed_from_sources` |

The whole YAML record was read. It contains NCBI identity, LPSN nomenclature, two pooled GTDB broad matches, one BacDive type-strain row for GB-78 / ATCC 35110, strain-level assemblies and genome records from BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo, StrainInfo nucleotide and deposit records, five top-level source attestations, and one 2026-09-13 `SEEDED_FROM_SOURCES` curation-history event.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1c10.yaml data/taxa/bacteria/pseudomonas_sp_wr1d02.yaml data/taxa/bacteria/chloroherpeton_thalassium.yaml data/taxa/bacteria/pseudomonas_sp_wr1d06.yaml` | Passed for the four-record batch. |
| `just validate data/taxa/bacteria/chloroherpeton_thalassium.yaml` | Passed; LinkML reported `No issues found`. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-chloroherpeton_thalassium.md'` | No prior report found. The `find` search included ignored files under `reports/yaml_record_review`. |
| Boundary-aware `rg --no-ignore --hidden` for `NCBITaxon:100716`, `lpsn:783637`, `GTDB:s__GWF2-33-9_sp020720105`, `GTDB:s__GWF2-33-9_sp020722095`, `bacdive:168002`, `straininfo.strain:100591`, and `straininfo.deposit:302239` | Found the expected PATHS, NCBI, LPSN, GTDB, BacDive, Madin, strain assembly, strain genome, strain related-record, and StrainInfo rows. |
| `rg --no-ignore --hidden --search-zip ... data/straininfo/related_records.tsv.gz` | Found the emitted StrainInfo rows for INSDC:AM049310, INSDC:AM050088, `straininfo.deposit:302239`, and `straininfo.strain:100591`. |
| `just verify-corpus` | Skipped for this read-only review; earlier full-corpus verification over 625,960 records was clean and no generated YAML was edited. |
| `just validate-history` | Skipped because this review does not create a `history/` decision. |
| `just validate-products` | Not applicable because this record has no `causal_graphs`. |

## Identity and Grounding

The record denotes the NCBI species `Chloroherpeton thalassium`. `data/raw/ncbitaxon_taxa.tsv` carries `NCBITaxon:100716`, the same label, rank `SPECIES`, parent genus `NCBITaxon:100715`, genetic code `11`, and source set `ncbitaxon|gtdb|lpsn|madin_etal`. The generated lineage stays within the bacterial Chlorobiota branch and terminates at `Chloroherpeton`.

The LPSN row `lpsn:783637` maps the same species name to `NCBITaxon:100716`, marks it validly published, legitimate, and the correct name, and provides ATCC 35110 as the type-strain designation. The two GTDB mappings are intentionally represented as `skos:broadMatch` pooled placeholder clusters rather than exact synonyms; no GTDB placeholder label is promoted into `synonyms`.

Live NCBI, LPSN, GTDB, BacDive, and StrainInfo lookups were unavailable, so the local pinned inventory rows are the reviewed sources of truth.

## Evidence

- The LPSN nomenclature block, authority string, status flags, DOI/PMID accessions, INSDC:AF170103 sequence accession, `lpsn:783637` xref, and ATCC 35110 type-strain designation are all present in `data/raw/lpsn_names.tsv`.
- The GTDB broad matches are supported by `data/raw/gtdb_mappings.tsv`, with two genomes for `GTDB:s__GWF2-33-9_sp020720105` and one genome for `GTDB:s__GWF2-33-9_sp020722095`, matching `data/raw/gtdb_species.tsv`.
- The BacDive strain source row `bacdive:168002` classifies GB-78 / ATCC 35110 as descendant `NCBITaxon:517418` under LPSN name `lpsn:783637`; the record keeps that child classification in `classified_as`.
- The assembly, IMG, PATRIC, GOLD, BioProject, and BioSample rows all trace to `kgmicrobe.strain:bacdive_168002` in the maintained `data/raw/strain_*` overlays, with ATCC 35110 matched through the source culture-collection or strain fields.
- StrainInfo genome, nucleotide, SI-DP, and SI-ID records all trace to `straininfo.strain:100591` and `straininfo.deposit:302239`, with deposit designation ATCC 35110 and `source_bacdive_id` `bacdive:168002`.

## Completeness

The record carries the consequential source-backed pieces available in the committed inventories: one BacDive strain, one linked StrainInfo strain/deposit, LPSN nomenclature and type-strain support, two broad GTDB species clusters, and the genome and project/sample records attached to the ATCC 35110 strain. The GTDB mappings are broad and are not represented as exact GTDB synonyms, which avoids equivalence inflation for pooled placeholder species.

No ATB rows were found for this NCBI species in the gitignore-independent source search, so the absence of `atb_evidence` is appropriate.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Run `just validate-strict data/taxa/bacteria/chloroherpeton_thalassium.yaml` after any seed refresh touching LPSN, GTDB, BacDive, StrainInfo, or strain genome overlays.
- Run `just verify-corpus` after any future curation change to `data/raw/lpsn_names.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/bacdive_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, or `data/straininfo/*`.

## Additional Notes

`data/raw/ncbi_type_material.tsv` also lists NCBI type-material strings for ATCC 35110 and GB-78, but TaxonMech currently derives `nomenclature` and `is_type_strain` from LPSN rather than NCBI `typematerial.dmp`; the LPSN-backed type-strain assertion is already sufficient here.
