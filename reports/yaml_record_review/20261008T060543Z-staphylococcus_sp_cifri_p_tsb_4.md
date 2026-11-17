# YAML Record Review: Staphylococcus sp. CIFRI P-TSB-4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_cifri_p_tsb_4.yaml`
- Started UTC: 2026-10-08T06:01:59Z
- Finished UTC: 2026-10-08T06:05:43Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1036325`, label `Staphylococcus sp. CIFRI P-TSB-4`. The entire 54-line YAML was read before judgment. It has species rank, BACTERIA domain, parent `NCBITaxon:91994`, genetic code 11, `EXACT` grounding, `SEEDED` status, zero inventoried BacDive strains and one NCBITAXON name attestation. Its seed event is dated `2026-09-13T17:54:04Z`. No record, source or history was edited.

## Validation

Validation used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/staphylococcus_sp_cifri_p_tsb_4.yaml` | Passed; no issues found. |
| `just validate-strict data/taxa/bacteria/staphylococcus_sp_cifri_p_tsb_4.yaml --out /private/tmp/sp4-strict.tsv` | Passed; one file, zero ERROR rows; header-only output inspected. |
| Structured pinned-source comparisons | Identity, parent, genetic code, all ten ancestors, synonym slots, attestation, PATHS entry and scope-derived seed text agree. |
| Type/lifecycle lookup | No exact target row in `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` or `dropped.tsv`. |
| Authority/reference checks | Live NCBI Taxonomy EFetch and Datasets inspected; exact nucleotide metadata and a confusable literature accession checked separately. No record DOI, PMID, LPSN, GTDB, strain or graph reference requires another authority check. |
| History | Embedded event checked. Ignored-inclusive content and filename searches found no target history artifact. No history was created; full `just validate-history` not run. |
| `just validate-products` | Not applicable: no curator-added graph nodes. |
| Full-corpus gates | Not run: `just verify-corpus`, provenance, render/site drift, documentation statistics, full tests, vendored checks or `just qc`. Focused comparisons do not establish corpus reproduction. |

## Identity and Grounding

The exact backbone row is `data/raw/ncbitaxon_taxa.tsv:222329`; the complete native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31873`. [Live NCBI Taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036325&retmode=xml) agrees with the ID, scientific name, species rank, parent 91994, Bacteria division, genetic code 11 and labeled ancestry. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036325) confirms the root-inclusive ancestor identifier order and rank.

All pinned ancestor IDs, labels, ranks and positions agree: root (1), cellular organisms (131567), Bacteria (2), Bacillati (1783272), Bacillota (1239), Bacilli (91061), Caryophanales (1385), Staphylococcaceae (90964), Staphylococcus (1279), and unclassified Staphylococcus (91994). Inspected pinned synonym fields and live OtherNames supply no alternate name. This is an isolate-designated species-rank NCBI concept, not a formal species epithet or registered culture deposit. `EXACT` refers to that concept match, not independent biological species identification.

The unique slug appears at `data/taxa/PATHS.tsv:14836`; `curation/seed_scope.tsv:322576` supplies the eligible scope and reason reproduced in the seed event. A complete pinned-backbone scan found no direct children.

## Evidence

The NCBITAXON attestation matches the source row: same ID and label, one `NAME`, snapshot `2026-09-13`. Its count is not a strain, genome or phenotype count. An absent mapping predicate is appropriate because this record is the source concept.

Exact-taxon Nuccore search returned one UID, 334303321. [GenBank JF799883.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799883.1) is a 1,340-base partial 16S rRNA sequence. Organism, strain `CIFRI P-TSB-4` and `taxon:1036325` match. Source qualifiers state marine water and `India: W.B.`. References identify Behera, Sharma, Das, Chanda and Patra, an unpublished salt-tolerant-bacteria study and their 11 April 2011 direct submission. Creation and update dates are 5 June 2011. Complete top-level, source-feature and reference metadata were inspected; sequence bases and non-source features were not audited. No culture deposit or assembly occurs in that inspected metadata. A marker sequence is not a genome or a measured salt-tolerance threshold.

The [Behera paper, DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), was checked through publisher metadata/abstract and [author-uploaded primary text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis), including methods and Tables 1 and 2. Its P-TSB-4 row refers to JF784022, 1,442 bases, and a nearest-strain identification of Staphylococcus haemolyticus; Table 1 places it in Puri water. JF799883 is not listed. The similar designation alone does not establish equivalence. Growth-symbol extraction is garbled; no quantitative phenotype or rendered-figure audit is claimed.

[GenBank JF784022.1](https://www.ncbi.nlm.nih.gov/nuccore/JF784022.1) independently confirms a different accession, 1,442-base length, strain `CIFRI P-TSB4`, organism Staphylococcus haemolyticus and `taxon:1283`. It specifies marine water from Puri, India, and a 5 April 2011 submission by overlapping authors with Jana also named. Its creation/update date is 30 May 2011. Those source differences are retained, not silently reconciled. The inspected metadata supplies no explicit same-isolate bridge to JF799883.1. Neither synonymization nor reclassification of this record is justified from name similarity. Search leads involving JF784022 in other papers were not treated as evidence about taxon 1036325.

## Completeness

Complete raw BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin and BactoTraits taxon inventory scans found no exact target row. No pinned descendants were found. Zero inventoried strains and an empty BacDive listing therefore agree with the source model; zero does not mean no biological isolate exists. No demonstrated omission requires populating optional synonyms, nomenclature, mappings, strain/genome links, definition, citations, discussions or mechanisms.

Absence searches included ignored, hidden and compressed files with `rg --no-ignore --hidden -n -z -i`. Whole numeric ID, slug and flexible isolate spellings were searched over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All three matching rows, backbone, scope and native name, were read in full as parsed TSV/JSON objects. All five `SOURCE.json` files were parsed separately; history filenames were checked independently of ignore rules. Expanded searches for both accessions and the paper DOI found only those same three rows. Ignored-independent filename search across records, reports and history found the one target YAML and no previous report for its stem.

Exact-taxon Assembly search returned zero with a phrase-not-found warning; this is not proof of global genome absence. Full-name and accession web searches found no additional verified exact-target publication; the JF799883 query returned no results, not an exhaustive bibliography. iModulonDB is not applicable: this YAML asserts no gene, regulator, transcriptomic dataset or mechanism.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The unresolved relationship between the two similarly named sequence submissions limits future enrichment but does not demonstrate an error in this correctly grounded NCBI record.

## Recommended Edits

None required. Do not substitute JF784022 for JF799883, assign Staphylococcus haemolyticus, transfer Puri provenance or salt-growth results, invent a culture deposit, count a marker as a genome, or promote review status based on this report.

Any future accepted taxonomy correction belongs upstream in NCBI, followed through `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. A demonstrated harmonization defect belongs in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. No maintained-owner defect was established, and no generated YAML should be patched by hand.

## Follow-up Checks

No mandatory repair is outstanding. Before literature enrichment, obtain an explicit accession-to-isolate or culture-deposit chain resolving the JF799883/JF784022 ambiguity. Similar designations, overlapping authors and sequence similarity alone do not establish culture identity. After any separately authorized input or seeder correction, run the documented seed dry run and single-record canary, focused validators, then full reproduction, provenance, relevant tests, generated-product and QC gates. Human sign-off owns status promotion.

## Additional Notes

Baseline HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`. Initial and pre-report YAML SHA-256 agree: `b9f91224292c48735f32b26098b60afccdb5c5baf7a83e834ff2d19b2e040a02`.

The review skill was read in the preceding continuing-session coverage check. CLAUDE.md, justfile, curation skill/checklist, curation/harmonization/schema guides, history guide and relevant schema classes/enums were read for this review at unchanged HEAD. The review-only contract overrides history scaffolding and GitHub mutation instructions. No paid research, source refresh, regeneration, outreach, GitHub mutation or Eukaryota review was performed; existing worktrees were preserved.
