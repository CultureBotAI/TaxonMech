# YAML Record Review: Staphylococcus sp. CIFRI H-TSB-8-RS

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_cifri_h_tsb_8_rs.yaml`
- Started UTC: 2026-10-08T05:55:11Z
- Finished UTC: 2026-10-08T05:58:15Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1036324`, label `Staphylococcus sp. CIFRI H-TSB-8-RS`. The complete 54-line YAML was read before judgment. It carries species rank, BACTERIA domain, parent `NCBITaxon:91994`, genetic code 11, `EXACT` grounding, `SEEDED` status, zero inventoried BacDive strains and one NCBITAXON name attestation. Its one seed event is dated `2026-09-13T17:54:04Z`. No YAML, source or history was changed.

## Validation

Validation used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/staphylococcus_sp_cifri_h_tsb_8_rs.yaml` | Passed; no issues found. |
| `just validate-strict data/taxa/bacteria/staphylococcus_sp_cifri_h_tsb_8_rs.yaml --out /private/tmp/sh8-strict.tsv` | Passed; one file, zero ERROR rows; header-only TSV inspected. |
| Structured source comparison | Identity, parent, genetic code, all ten ancestors, synonyms, source attestation, PATHS entry and scope-derived seed text match pinned inputs. |
| Type/lifecycle lookup | No exact target row in `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` or `dropped.tsv`. |
| Authority/reference checks | Live NCBI Taxonomy EFetch and Datasets checked; exact nucleotide source/reference metadata inspected. No record DOI, PMID, LPSN, GTDB, graph or strain link needs another authority check. |
| History | Embedded seed event checked. Ignored-inclusive content and filename searches found no target history artifact. No history was created; full `just validate-history` not run. |
| `just validate-products` | Not applicable: no curator-added graph nodes. |
| Full-corpus gates | Not run: `just verify-corpus`, provenance, render/site drift, documentation statistics, full tests, vendored checks or `just qc`. Focused comparisons do not prove corpus reproduction. |

## Identity and Grounding

The exact backbone row is `data/raw/ncbitaxon_taxa.tsv:222328`; the scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31872`. [Live NCBI Taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036324&retmode=xml) agrees with the name, species rank, parent 91994, Bacteria division, genetic code 11 and labeled ancestry. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036324) confirms the root-inclusive ancestor identifier order and rank.

All pinned lineage entries match in ID, label, rank and position: root (1), cellular organisms (131567), Bacteria (2), Bacillati (1783272), Bacillota (1239), Bacilli (91061), Caryophanales (1385), Staphylococcaceae (90964), Staphylococcus (1279), and unclassified Staphylococcus (91994). No alternate name was supplied in the inspected pinned synonym fields or live OtherNames surface. This is an isolate-designated NCBI species-rank concept, not a formal species epithet or registered culture deposit. Exact grounding denotes the concept match, not independent biological species identification.

The unique slug entry is `data/taxa/PATHS.tsv:14835`. `curation/seed_scope.tsv:322575` supplies the eligible species-level scope and the reason reproduced in the seed event. A complete pinned-backbone scan found no direct children.

## Evidence

The sole NCBITAXON attestation is supported by the exact backbone row: same ID and label, one `NAME`, snapshot `2026-09-13`. No mapping predicate is necessary because this record is the source concept. The count is not a genome or phenotype claim.

Exact-taxon Nuccore search returned UID 334303336. [GenBank JF799898.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799898.1) is a 1,327-base partial 16S rRNA sequence. Its organism, strain `CIFRI H-TSB-8-RS` and `taxon:1036324` agree. Source qualifiers state marine water and `India: W.B.`. References name Behera, Sharma, Das, Chanda and Patra, an unpublished salt-tolerant-bacteria study and their 11 April 2011 direct submission. Creation and update dates are 5 June 2011. Complete top-level, source-feature and reference metadata were inspected; bases and non-source features were not audited. No culture deposit or assembly appears in that inspected source metadata. This marker supports source identity, not a genome or measured salt-tolerance threshold.

The related [Behera publication, DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), was previously inspected in this continuing session through publisher metadata/abstract and [author-uploaded primary text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis). Complete Tables 1 and 2 do not list H-TSB-8-RS or JF799898. The shorter H-TSB-8 designation in those tables concerns a different accession, JF267327, and cannot supply this target's identification or phenotype. No quantitative growth or rendered-figure audit is claimed. Other CIFRI isolate results were not transferred.

## Completeness

Complete raw BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin and BactoTraits taxon inventory scans found no exact target row. With no pinned descendants, zero inventoried strains and the empty BacDive listing agree with the source model. Zero does not mean no biological isolate exists. No supported omission was established for synonyms, nomenclature, mappings, xrefs or strain/genome links. Optional definition, literature evidence, discussions and mechanisms need not be invented.

Absence searches included ignored, hidden and compressed files using `rg --no-ignore --hidden -n -z -i`. The whole numeric identifier, slug and flexible isolate-name spellings were searched across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Identifier word boundaries excluded unrelated longer numeric identifiers. All three matching rows, backbone, scope and native name, were read in full as parsed TSV/JSON objects. All five `SOURCE.json` files were parsed separately; history filenames were searched independently of ignore rules. An expanded accession, paper-DOI and name search found only the same three rows. Filename search over records, reports and history found the one YAML and no prior report for its stem.

The exact-taxon Assembly query returned zero with a phrase-not-found warning, not proof of global genome absence. Web searches for the full designation and JF799898 established no further exact-isolate primary publication; this is not an exhaustive bibliography. iModulonDB was not applicable: the YAML asserts no gene, regulator, transcriptomic dataset or mechanism.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Limited assembly queries and broader literature uncertainty are review limits, not demonstrated record defects.

## Recommended Edits

None required. Do not equate H-TSB-8-RS with the shorter H-TSB-8 designation, invent a deposit, count the 16S marker as a genome, hand-edit the generated YAML or promote its status from this report.

Future accepted taxonomy corrections belong upstream in NCBI, then through the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Demonstrated harmonization defects belong in `src/taxonmech/seed.py` with tests; scope decisions belong in `curation/seed_scope.tsv`. No such owner defect was established here. Curation requires separate authorization.

## Follow-up Checks

No mandatory repair is outstanding. Later enrichment requires an explicit exact-isolate/deposit/source chain and marker-versus-genome distinction. After a separately authorized input or seeder correction, run the documented seed dry run, single-record canary, focused validators, then full reproduction, provenance, relevant tests, generated-product and QC gates. Human sign-off owns review-status promotion.

## Additional Notes

Baseline HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`. Initial and pre-report YAML SHA-256 agree: `9d549a3b66676a5d734a73b9f0dce9513f5932bf680747880b4eda6435a615eb`.

The review skill, CLAUDE.md, justfile, curation skill/checklist, curation/harmonization/schema guides, history guide and relevant schema classes were read earlier in this continuing unchanged-HEAD session. The read-only review contract overrides history scaffolding. No paid research, source refresh, regeneration, outreach, GitHub mutation or Eukaryota review was performed. Existing worktrees were preserved; no mapping-status promotion occurred.
