# YAML Record Review: Staphylococcus sp. CIFRI P-TSB-53

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_cifri_p_tsb_53.yaml`
- Started UTC: 2026-10-08T06:11:57Z
- Finished UTC: 2026-10-08T06:16:19Z
- Verdict: pass with minor issues

## Target

One generated `TaxonRecord`, `NCBITaxon:1036327`, label `Staphylococcus sp. CIFRI P-TSB-53`. The entire 54-line YAML was read before judgment. It has species rank, BACTERIA domain, parent `NCBITaxon:91994`, genetic code 11, `EXACT` grounding, `SEEDED` status, zero inventoried BacDive strains and one NCBITAXON name attestation. Its seed event is dated `2026-09-13T17:54:04Z`. No record, source or history was edited. The minor issue concerns external source provenance, not an incorrect field asserted by the YAML.

## Validation

Validation used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/staphylococcus_sp_cifri_p_tsb_53.yaml` | Passed; no issues found. |
| `just validate-strict data/taxa/bacteria/staphylococcus_sp_cifri_p_tsb_53.yaml --out /private/tmp/sp53-strict.tsv` | Passed; one file, zero ERROR rows; header-only TSV inspected. |
| Structured pinned-source comparison | Identity, parent, genetic code, ten ancestors, synonym slots, attestation, PATHS entry and scope-derived seed text agree. |
| Type/lifecycle lookup | No exact target row in `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` or `dropped.tsv`. |
| Authority/reference checks | Live NCBI Taxonomy EFetch, Datasets and exact nucleotide metadata inspected. The matching publication's publisher metadata, methods and table text were checked. No record LPSN, GTDB, strain or graph reference requires another authority check. |
| History | Embedded seed event checked. Ignored-inclusive content and filename searches found no target history artifact. No history was created; full `just validate-history` not run. |
| `just validate-products` | Not applicable: no curator-added graph nodes. |
| Full-corpus gates | Not run: `just verify-corpus`, provenance, render/site drift, documentation statistics, full tests, vendored checks or `just qc`. Focused comparisons do not establish corpus reproduction. |

## Identity and Grounding

The exact backbone row is `data/raw/ncbitaxon_taxa.tsv:222331`; the complete native name object is `data/catalog/ncbi_names-0005.jsonl.gz:31875`. [Live NCBI Taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036327&retmode=xml) agrees with the identifier, scientific name, species rank, parent 91994, Bacteria division, genetic code 11 and labeled ancestry. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036327) confirms the root-inclusive ancestor identifier order and rank.

All pinned ancestor identifiers, labels, ranks and positions match: root (1), cellular organisms (131567), Bacteria (2), Bacillati (1783272), Bacillota (1239), Bacilli (91061), Caryophanales (1385), Staphylococcaceae (90964), Staphylococcus (1279), and unclassified Staphylococcus (91994). Inspected pinned synonym fields and the live OtherNames surface supply no alternate name. This is an isolate-designated species-rank NCBI concept, not a formal species epithet or registered culture deposit. `EXACT` denotes the concept match, not independent species identification.

The unique slug is at `data/taxa/PATHS.tsv:14838`; `curation/seed_scope.tsv:322578` supplies the eligible scope and reason reproduced in the seed event. A complete pinned-backbone scan found no direct children.

## Evidence

The sole NCBITAXON attestation is supported by the exact source row: same ID and label, one `NAME`, snapshot `2026-09-13`. It does not count strains, genomes or phenotypes. No mapping predicate is needed because the record is the source concept.

Exact-taxon Nuccore search returned UID 334303333. [GenBank JF799895.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799895.1) is a 1,430-base partial 16S rRNA sequence with matching organism, strain `CIFRI P-TSB-53` and `taxon:1036327`. Source qualifiers specify marine water and `India: W.B.`. References name Behera, Sharma, Das, Chanda and Patra, an unpublished salt-tolerant-bacteria study and their 11 April 2011 direct submission. Creation and update dates are 5 June 2011. Complete top-level, source-feature and reference metadata were read; sequence bases and non-source features were not audited. No culture deposit or assembly occurs in that inspected metadata. A marker is not a genome or a quantified salt-tolerance measurement.

The [Behera publication, DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), has an exact accession match in [author-uploaded primary text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis). Table 2 pairs P-TSB-53 with JF799895 and the same length; its nearest-strain assignment is Staphylococcus hominis, with RDP S_ab 0.988 and SILVA alignment identity 99.93%. This is a published marker-based identification, not an NCBI synonym or authority-approved reclassification. Table 1 lists Puri water and Tryptone Soya Agar. The reported locality is not reconciled with the sequence submission's location qualifier. Methods and complete table text were inspected in this continuing session, with the target rows reopened during this review. Garbled growth symbols prevent a reliable quantitative salt-growth extraction; no rendered-figure audit is claimed.

The paper supports additional isolate context, while live NCBI retains its less-specific name. Both are preserved here without replacing the carried lineage, asserting a formal species mapping, transferring results from other isolates or treating sequence similarity as a genome/deposit link.

## Completeness

Complete raw BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin and BactoTraits taxon inventory scans found no exact target row. With no pinned descendants, zero inventoried BacDive strains and the empty listing agree with the source model. Zero does not mean no biological isolate exists. Optional record-level literature is not required for a seeded record; omission of this publication is not by itself a defect. No demonstrated missing synonym, nomenclature entry, taxonomy mapping, xref or strain/genome link was established.

Absence searches included ignored, hidden and compressed files via `rg --no-ignore --hidden -n -z -i`. Whole numeric ID, slug and flexible isolate spellings were searched across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All three matching rows, backbone, scope and native name, were read fully as parsed TSV/JSON objects. All five `SOURCE.json` files were parsed separately; history filenames were checked independently of ignore rules. Expanded accession and paper-DOI searches found only the same three rows. Ignored-independent filename search over records, reports and history found the target YAML and no previous report for its stem.

Exact-taxon Assembly search returned zero with a phrase-not-found warning, not proof of global genome absence. Full-name and accession web searches found the matching paper; they do not constitute an exhaustive bibliography. iModulonDB is not applicable: this YAML asserts no gene, regulator, transcriptomic dataset or mechanism.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**Minor M1: Exact-isolate locality provenance is unresolved.** The primary sequence and the accession-matched publication supply the differing location descriptions documented under Evidence. They should not be silently combined into a single locality claim. This is a non-blocking external-source inconsistency: the current YAML asserts neither location and its identity and lineage remain supported. Resolution belongs to the original source annotation/publication, not a generated-YAML patch. If later retained in TaxonMech, a provenance-aware discussion must use a maintained curation input supported through `src/taxonmech/seed.py` under `docs/CURATION.md`; no such discussion was inserted here.

No blocker or major finding was established. The publication's more-specific identification alone does not invalidate the NCBI placeholder.

## Recommended Edits

1. Before locality enrichment, reconcile M1 using an authoritative source correction or explicit isolate sampling documentation. Until then, preserve both source assertions and mark the locality unresolved; do not choose one silently. No immediate YAML edit is warranted.
2. Keep the NCBI name, lineage and source attestation as carried. Any accepted taxonomic revision belongs upstream in NCBI, then through the pinned workflow governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Seeder defects, if subsequently demonstrated, belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`.

Do not invent a registered deposit, infer a genome from the marker, add an unsupported hominis equivalence, hard-code an isolation location or promote mapping status from this report.

## Follow-up Checks

For M1, compare the exact accession/version and isolate label in any corrected source with the original table row, and retain dated provenance for the resolution. A source correction cannot be proved by schema validation alone. A later discussion/evidence integration must first have a maintained input path that survives regeneration. After a separately authorized input or seeder change, run the documented seed dry run, single-record canary and focused validators, followed by full reproduction, provenance, relevant tests, generated-product and QC gates. Human sign-off owns status promotion.

## Additional Notes

Baseline HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`. Initial and pre-report YAML SHA-256 agree: `726f3edb7e42a56c9253d5ab75aba035998408ac8c056d7e72bee90403179f4f`.

An independent check of the official Puri district page was attempted but not completed: web fetches timed out, Python's verified-TLS request failed certificate validation, and a system-curl retry failed with a connection reset. Search excerpts were not promoted to inspected primary evidence. M1 is limited to the unreconciled source descriptions, not a newly curated geographic assertion. No TLS verification was disabled.

The review skill, CLAUDE.md, justfile, curation skill/checklist, curation/harmonization/schema guides, history guide and relevant schema classes/enums were read earlier in this continuing unchanged-HEAD session. The read-only review contract overrides history scaffolding and GitHub mutation instructions. No paid research, source refresh, regeneration, outreach, GitHub mutation or Eukaryota review was performed; existing worktrees were preserved.
