# YAML Record Review: Staphylococcus sp. CIFRI H-TSB-20-ZMA

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_cifri_h_tsb_20_zma.yaml`
- Started UTC: 2026-10-08T05:42:54Z
- Finished UTC: 2026-10-08T05:45:55Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1036322`, label `Staphylococcus sp. CIFRI H-TSB-20-ZMA`. The full 54-line YAML was read before judgment. Its populated fields are species rank, BACTERIA domain, parent `NCBITaxon:91994`, genetic code 11, `EXACT` grounding, `SEEDED` status, zero inventoried BacDive strains, one NCBITAXON name attestation and one seed event dated `2026-09-13T17:54:04Z`. This review changed none of those fields.

## Validation

Validation used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/staphylococcus_sp_cifri_h_tsb_20_zma.yaml` | Passed; no issues found. |
| `just validate-strict data/taxa/bacteria/staphylococcus_sp_cifri_h_tsb_20_zma.yaml --out /private/tmp/sh20-strict.tsv` | Passed; one file, zero ERROR rows. Header-only TSV inspected. |
| Structured source comparison | Identity, all ten ancestors, parent, genetic code, synonyms, attestation, PATHS entry and scope-derived seed text agree with pinned inputs. |
| Lifecycle/type-material lookup | No exact target row in `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` or `dropped.tsv`. |
| Authority/reference checks | Live NCBI Taxonomy EFetch and Datasets inspected; exact nucleotide source/reference metadata inspected separately. No record DOI, PMID, LPSN, GTDB, graph or strain link requires another authority check. |
| History | Embedded seed event checked. Ignored-inclusive history content and filename searches found no target artifact. No history was created; full `just validate-history` was not run. |
| `just validate-products` | Not applicable: no curator-added graph nodes. |
| Full-corpus gates | Not run: `just verify-corpus`, provenance, render/site drift, documentation statistics, full tests, vendored checks and `just qc`. Focused source comparison is not proof of corpus-wide reproduction. |

## Identity and Grounding

The target's row is `data/raw/ncbitaxon_taxa.tsv:222326`; its scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31870`. Both identify this exact taxon. The live [NCBI Taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036322&retmode=xml) agrees with the label, species rank, parent 91994, Bacteria division and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036322) confirms the species rank and root-inclusive identifier chain.

The checked ancestors are root (1), cellular organisms (131567), Bacteria (2), Bacillati (1783272), Bacillota (1239), Bacilli (91061), Caryophanales (1385), Staphylococcaceae (90964), Staphylococcus (1279), and unclassified Staphylococcus (91994). Every pinned label, ID, rank and position agrees with the YAML; the live labeled ancestry agrees as well. No synonym or OtherNames entry was supplied by the inspected source surfaces. This is an isolate-designated species-rank NCBI concept, not a formal species epithet or a culture-deposit accession. `EXACT` describes the ID-to-concept match, not independent biological species identification.

`data/taxa/PATHS.tsv:14833` uniquely fixes its slug. `curation/seed_scope.tsv:322573` supplies the species-level scope and exact reason reproduced in the seed event. The complete pinned-backbone scan found no direct children.

## Evidence

The NCBITAXON attestation is supported by the exact backbone row: same source ID and label, one `NAME`, snapshot `2026-09-13`. Absence of a mapping predicate is appropriate because the record is that source concept. This is not a genome, phenotype or biological strain count.

Exact-taxon Nuccore search returned UID 334303345. [GenBank JF799907.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799907.1) is a 1,444-base partial 16S rRNA sequence. Its organism, strain `CIFRI H-TSB-20-ZMA`, and `taxon:1036322` match this record. Source qualifiers state marine water and `India: W.B.`. References name Behera, Sharma, Das, Chanda and Patra, an unpublished salt-tolerant-bacteria study and their 11 April 2011 direct submission. Creation and update dates are 5 June 2011. Complete top-level, source-feature and reference metadata were inspected; sequence bases and non-source features were not audited. The inspected source metadata provides no culture deposit or assembly. A partial 16S marker does not supply a genome or quantitative salt-tolerance evidence.

The related [Behera publication, DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), was checked against its publisher metadata/abstract and [author-uploaded primary text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis), read earlier in this continuing review session. The methods and complete Tables 1 and 2 were inspected, not just search snippets. Those tables do not list H-TSB-20-ZMA or JF799907. They cannot supply this isolate's identification, medium, locality or measured salt phenotype merely because other CIFRI isolates are present. No figure-visual or quantitative-growth audit is claimed. This rejected near-match does not establish global absence of exact-isolate literature.

## Completeness

Complete local raw BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin and BactoTraits taxon inventory scans found no exact target row. With no pinned descendants, the empty BacDive listing and `strain_count: 0` match the local model; zero does not mean no isolate exists. No supported omission was established for synonyms, nomenclature, taxonomy mappings, xrefs or strain/genome links. Optional definition, literature evidence, discussions and mechanisms need not be invented for a seeded identity record.

Ignored and hidden files were included: `rg --no-ignore --hidden -n -z -i` searched numeric ID, slug and flexible isolate-name spellings across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 19 candidate rows were read as complete parsed JSON or TSV objects. Three concern this target. Sixteen are unrelated numeric substring matches: ten plant/fungal GOLD project sample IDs, one Campylobacter assembly accession, three Enterobacter assembly rows, one Enterobacter BV-BRC row and an ATB row for that unrelated sample. These are not target strain/genome evidence. All five `SOURCE.json` files were parsed separately, and history filenames were searched independently of ignore rules. Expanded searches for JF799907, the paper DOI and name variants found only the same three target rows. An ignored-inclusive filename search over records, reports and history found the single target YAML and no prior report for its stem.

The exact-taxon Assembly search returned zero with a phrase-not-found warning, not a proof of worldwide genome absence. Exact designation, shortened spelling and accession web searches established no further exact-isolate primary publication. iModulonDB was not applicable: this YAML has no gene, regulator, transcriptomic dataset or mechanism claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Bounded query limitations and unproved broader literature coverage are retained as limitations rather than invented record defects.

## Recommended Edits

None required. Do not transfer neighboring CIFRI results, infer a registered deposit from this name, count the 16S marker as a genome, hand-edit the generated YAML or promote its status from this report.

Future accepted NCBI corrections belong upstream, then through the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Demonstrated harmonization errors belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. No owner defect was demonstrated here. Curation would require separate authorization.

## Follow-up Checks

No mandatory repair is outstanding. Later enrichment requires an explicit exact-isolate/deposit/source chain and correct marker-versus-genome typing. After a separately authorized input or seeder correction, use the documented seed dry run, single-record canary and focused validators, then full reproduction, provenance, relevant tests, generated-product and QC gates. Human review is required for status promotion.

## Additional Notes

Baseline HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`. Initial and pre-report YAML SHA-256 agree: `c9f74f8dd676bebbe70330a30569ff6f87e6763a965da727f7b733b2256f8d85`.

The review skill was reread; CLAUDE.md, justfile, the curation skill/checklist, curation/harmonization/schema guides, history guide and relevant schema classes were read earlier in this continuing unchanged-HEAD session. The review contract overrides history scaffolding. No YAML/source/history edit, source refresh, record regeneration, paid research, outreach, GitHub mutation or Eukaryota review was performed. Existing worktrees were preserved.
