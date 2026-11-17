# YAML Record Review: Staphylococcus sp. CIFRI P-TSB-50-ZMA

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_cifri_p_tsb_50_zma.yaml`
- Started UTC: 2026-10-08T06:06:56Z
- Finished UTC: 2026-10-08T06:09:22Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1036326`, label `Staphylococcus sp. CIFRI P-TSB-50-ZMA`. The complete 54-line YAML was read before judgment. It has species rank, BACTERIA domain, parent `NCBITaxon:91994`, genetic code 11, `EXACT` grounding, `SEEDED` status, zero inventoried BacDive strains and one NCBITAXON name attestation. Its seed event is dated `2026-09-13T17:54:04Z`. No YAML, source or history was changed.

## Validation

Validation used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/staphylococcus_sp_cifri_p_tsb_50_zma.yaml` | Passed; no issues found. |
| `just validate-strict data/taxa/bacteria/staphylococcus_sp_cifri_p_tsb_50_zma.yaml --out /private/tmp/sp50-strict.tsv` | Passed; one file, zero ERROR rows; header-only TSV inspected. |
| Structured source comparison | Identity, parent, genetic code, all ten ancestors, synonym slots, source attestation, PATHS entry and scope-derived seed text agree with pinned inputs. |
| Type/lifecycle lookup | No exact target row in `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` or `dropped.tsv`. |
| Authority/reference checks | Live NCBI Taxonomy EFetch and Datasets checked; exact nucleotide metadata inspected. No record DOI, PMID, LPSN, GTDB, strain or graph link requires another authority check. |
| History | Embedded seed event checked. Ignored-inclusive content and filename searches found no target history artifact. No history was created; full `just validate-history` not run. |
| `just validate-products` | Not applicable: no curator-added graph nodes. |
| Full-corpus gates | Not run: `just verify-corpus`, provenance, render/site drift, documentation statistics, full tests, vendored checks or `just qc`. Focused comparisons do not establish corpus reproduction. |

## Identity and Grounding

The exact backbone row is `data/raw/ncbitaxon_taxa.tsv:222330`; its native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31874`. [Live NCBI Taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036326&retmode=xml) agrees with the ID, scientific name, species rank, parent 91994, Bacteria division, genetic code 11 and labeled ancestry. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036326) confirms the root-inclusive ancestor identifier order and rank.

All pinned ancestor IDs, labels, ranks and positions agree: root (1), cellular organisms (131567), Bacteria (2), Bacillati (1783272), Bacillota (1239), Bacilli (91061), Caryophanales (1385), Staphylococcaceae (90964), Staphylococcus (1279), and unclassified Staphylococcus (91994). The inspected pinned synonym slots and live OtherNames surface supply no alternate name. This is an isolate-designated NCBI species-rank concept, not a formal species epithet or registered culture deposit. `EXACT` denotes that concept match, not independent biological species identification.

The unique slug appears at `data/taxa/PATHS.tsv:14837`. `curation/seed_scope.tsv:322577` supplies the eligible scope and reason reproduced in the seed event. A complete pinned-backbone scan found no direct children.

## Evidence

The sole NCBITAXON attestation agrees with the source row: same ID and label, one `NAME`, snapshot `2026-09-13`. This count is not a strain, genome or phenotype count. No mapping predicate is needed because the record is the source concept.

Exact-taxon Nuccore search returned one UID, 334303330. [GenBank JF799892.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799892.1) is a 1,361-base partial 16S rRNA sequence. Its organism, strain `CIFRI P-TSB-50-ZMA` and `taxon:1036326` agree. Source qualifiers state marine water and `India: W.B.`. References name Behera, Sharma, Das, Chanda and Patra, an unpublished salt-tolerant-bacteria study and their 11 April 2011 direct submission. Creation and update dates are 5 June 2011. Complete top-level, source-feature and reference metadata were inspected; bases and non-source features were not audited. No culture deposit or assembly occurs in that inspected metadata. This marker supports source identity, not a genome or measured salt-tolerance threshold.

The related [Behera paper, DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), was inspected earlier in this same continuing session through publisher metadata/abstract and [author-uploaded primary text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis), including methods and complete Tables 1 and 2. Neither P-TSB-50-ZMA nor JF799892 appears in those tables. The nearby P-TSB-51-ZMA row concerns JF799893 and cannot support this isolate's identity, isolation provenance or phenotype. No quantitative growth or rendered-figure audit is claimed, and no other CIFRI isolate's results were transferred.

## Completeness

Complete raw BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin and BactoTraits taxon inventory scans found no exact target row. No pinned descendants were found. Zero inventoried strains and an empty BacDive listing agree with the source model; zero does not mean no biological isolate exists. No demonstrated omission requires optional synonyms, nomenclature, taxonomy mappings, xrefs, strain/genome links, definition, literature evidence, discussions or mechanisms.

Absence searches included ignored, hidden and compressed files through `rg --no-ignore --hidden -n -z -i`. Whole numeric ID, slug and flexible isolate spellings were searched across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All three matching rows, backbone, scope and native name, were read completely as parsed TSV/JSON objects. All five `SOURCE.json` files were parsed separately; history filenames were checked independently of ignore rules. Expanded accession and paper-DOI searches found only those same three rows. Ignored-independent filename search over records, reports and history found the target YAML and no previous report for its stem.

The exact-taxon Assembly query returned zero with a phrase-not-found warning, not proof of global genome absence. Full-designation, shortened-name and accession web searches established no further exact-target primary publication; the JF799892 search returned no results. This is a bounded literature check, not an exhaustive bibliography. iModulonDB is not applicable: the YAML asserts no gene, regulator, transcriptomic dataset or mechanism.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Bounded assembly and literature searches leave general enrichment uncertainty, not a demonstrated record defect.

## Recommended Edits

None required. Do not infer culture-medium performance or an isolation location from the strain designation, transfer the P-TSB-51-ZMA result, invent a deposit, count the marker as a genome, hand-edit generated YAML or promote review status from this report.

Future accepted taxonomy corrections belong upstream in NCBI, then through the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Demonstrated harmonization defects belong in `src/taxonmech/seed.py` with tests; scope decisions belong in `curation/seed_scope.tsv`. No such owner defect was established. Curation requires separate authorization.

## Follow-up Checks

No mandatory repair is outstanding. Later enrichment requires exact-isolate evidence, an explicit deposit/source chain for strain-genome links, and a marker-versus-genome distinction. After a separately authorized input or seeder correction, run the documented seed dry run and single-record canary, focused validators, then full reproduction, provenance, relevant tests, generated-product and QC gates. Human sign-off owns review-status promotion.

## Additional Notes

Baseline HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`. Initial and pre-report YAML SHA-256 agree: `7d6dc0e08b10d75f3081f95bf604b5a3c5033f0843376c3db1d6f0a2255ba031`.

The review skill, CLAUDE.md, justfile, curation skill/checklist, curation/harmonization/schema guides, history guide and relevant schema classes/enums were read earlier in this continuing unchanged-HEAD session. The read-only review contract overrides history scaffolding and GitHub mutation instructions. No paid research, source refresh, regeneration, outreach, GitHub mutation or Eukaryota review was performed; existing worktrees were preserved.
