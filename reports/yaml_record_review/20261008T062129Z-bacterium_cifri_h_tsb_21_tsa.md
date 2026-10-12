# YAML Record Review: bacterium CIFRI H-TSB-21-TSA

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_cifri_h_tsb_21_tsa.yaml`
- Started UTC: 2026-10-08T06:18:01Z
- Finished UTC: 2026-10-08T06:21:29Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1036328`, label `bacterium CIFRI H-TSB-21-TSA`. The entire 36-line YAML was read before judgment. It carries species rank, BACTERIA domain, parent `NCBITaxon:49928`, genetic code 11, `EXACT` grounding, `SEEDED` status, zero inventoried BacDive strains and one NCBITAXON name attestation. Its seed event is dated `2026-09-13T17:54:04Z`. No record, source or history was changed.

## Validation

Validation used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/bacterium_cifri_h_tsb_21_tsa.yaml` | Passed; no issues found. |
| `just validate-strict data/taxa/bacteria/bacterium_cifri_h_tsb_21_tsa.yaml --out /private/tmp/bh21-strict.tsv` | Passed; one file, zero ERROR rows; header-only TSV inspected. |
| Structured pinned-source comparison | Identity, parent, genetic code, all four ancestors, synonym slots, attestation, PATHS entry and scope-derived seed text agree. |
| Type/lifecycle lookup | No exact target row in `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` or `dropped.tsv`. |
| Authority/reference checks | Live NCBI Taxonomy EFetch and Datasets inspected; exact nucleotide metadata and a confusable literature accession checked separately. No record DOI, PMID, LPSN, GTDB, strain or graph reference requires another authority check. |
| History | Embedded seed event checked. Ignored-inclusive content and filename searches found no target history artifact. No history was created; full `just validate-history` not run. |
| `just validate-products` | Not applicable: no curator-added graph nodes. |
| Full-corpus gates | Not run: `just verify-corpus`, provenance, render/site drift, documentation statistics, full tests, vendored checks or `just qc`. Focused comparisons do not establish corpus reproduction. |

## Identity and Grounding

The exact backbone row is `data/raw/ncbitaxon_taxa.tsv:222332`; its native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31876`. [Live NCBI Taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036328&retmode=xml) agrees with the name, species rank, parent 49928, Bacteria division, genetic code 11 and labeled ancestry. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036328) confirms the root-inclusive ancestor order and rank.

All ancestor IDs, labels, ranks and positions match: root (1), cellular organisms (131567), Bacteria (2), and unclassified Bacteria (49928). The short lineage reflects the authority's unresolved classification, not omitted genus or phylum fields. Inspected pinned synonym fields and live OtherNames supply no alternate name. Species rank makes this isolate-designated NCBI concept eligible under the repository's scope rule; it is not a formal species epithet or registered culture deposit. `EXACT` denotes concept identity, not a resolved biological species identification.

The unique slug is at `data/taxa/PATHS.tsv:14839`; `curation/seed_scope.tsv:322579` supplies the eligible scope and reason reproduced in the seed event. A complete pinned-backbone scan found no direct children.

## Evidence

The NCBITAXON attestation agrees with the source row: same ID and label, one `NAME`, snapshot `2026-09-13`. This count is not a strain, genome or phenotype count. An absent mapping predicate is appropriate because the record is the source concept.

Exact-taxon Nuccore search returned one UID, 334303337. [GenBank JF799899.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799899.1) is a 1,438-base partial 16S rRNA sequence. Its organism, strain `CIFRI H-TSB-21-TSA` and `taxon:1036328` match. Source qualifiers state marine water and `India: W.B.`. References name Behera, Sharma, Das, Chanda and Patra, an unpublished salt-tolerant-bacteria study and their 11 April 2011 direct submission. Creation and update dates are 5 June 2011. Complete top-level, source-feature and reference metadata were inspected; bases and non-source features were not audited. No culture deposit or assembly occurs in that inspected metadata. This marker does not supply a genome or measured salt-tolerance threshold.

The related [Behera paper, DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), was inspected in this continuing session through publisher metadata/abstract and [author-uploaded primary text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis), including methods and Tables 1 and 2. It lists the shorter H-TSB-21 designation with JF784016, not this target's accession. Neither H-TSB-21-TSA nor JF799899 appears in those tables. The paper cannot establish a genus, locality or phenotype for this target without a demonstrated identity bridge. No quantitative growth or rendered-figure audit is claimed.

[GenBank JF784016.1](https://www.ncbi.nlm.nih.gov/nuccore/JF784016.1) was read independently to resolve that near match. It names Staphylococcus haemolyticus, strain `CIFRI H-TSB21`, `taxon:1283`, and marine water from Haldia, India. Its partial 16S sequence is also 1,438 bases; the same five authors submitted it on 5 April 2011, and its creation/update date is 30 May 2011. These similarities do not establish that the cultures are identical. The inspected source metadata supplies no explicit link equating it to JF799899.1. No sequence alignment was performed, and even marker identity would not by itself prove culture identity. Do not silently resolve this unclassified bacterium as Staphylococcus.

## Completeness

Complete raw BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin and BactoTraits taxon inventory scans found no exact target row. With no pinned descendants, zero inventoried strains and an empty BacDive listing agree with the source model. Zero does not mean no biological isolate exists. No supported omission was established for synonyms, nomenclature, taxonomy mappings, xrefs or strain/genome links. Optional definition, literature evidence, discussions and mechanisms need not be invented.

Absence searches included ignored, hidden and compressed files through `rg --no-ignore --hidden -n -z -i`. Whole numeric ID, slug and flexible isolate spellings were searched across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All three matching rows, backbone, scope and native name, were read completely as parsed TSV/JSON objects. All five `SOURCE.json` files were parsed separately; history filenames were checked independently of ignore rules. Expanded searches for both accessions, the paper DOI and the shorter CIFRI H-TSB21 name found only those same three rows. Ignored-independent filename search over records, reports and history found the one YAML and no previous report for its stem.

Exact-taxon Assembly search returned zero with a phrase-not-found warning, not proof of global genome absence. Full-designation and accession web searches established no further exact-target primary publication; JF799899 returned no search results. This is not an exhaustive bibliography. iModulonDB is not applicable: the YAML asserts no gene, regulator, transcriptomic dataset or mechanism.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Unresolved classification and an unproven relationship to the shorter H-TSB21 name are enrichment limits, not demonstrated defects in the correctly carried NCBI concept.

## Recommended Edits

None required. Preserve the authority's short lineage and the complete isolate suffix. Do not substitute JF784016, infer Staphylococcus placement, transfer phenotype or Haldia context, invent a deposit, count a marker as a genome, hand-edit generated YAML or promote review status from this report.

Future accepted taxonomy corrections belong upstream in NCBI, then through the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Demonstrated harmonization defects belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. No such owner defect was established.

## Follow-up Checks

No mandatory repair is outstanding. Before enrichment from the H-TSB21 literature, obtain an explicit accession-to-isolate or culture-deposit chain resolving the two submissions. After a separately authorized input or seeder correction, run the documented seed dry run and single-record canary, focused validators, then full reproduction, provenance, relevant tests, generated-product and QC gates. Human sign-off owns status promotion.

## Additional Notes

Baseline HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`. Initial and pre-report YAML SHA-256 agree: `96f9247f220b884b42eda12fcd337e020f4e889cb8b0b61c9e1197b6bdef4131`.

The review skill, CLAUDE.md, justfile, curation skill/checklist, curation/harmonization/schema guides, history guide and relevant schema classes/enums were read earlier in this continuing unchanged-HEAD session. The read-only review contract overrides history scaffolding and GitHub mutation instructions. No paid research, source refresh, regeneration, outreach, GitHub mutation or Eukaryota review was performed; existing worktrees were preserved.
