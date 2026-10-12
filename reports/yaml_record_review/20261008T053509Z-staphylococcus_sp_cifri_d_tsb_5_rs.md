# YAML Record Review: Staphylococcus sp. CIFRI D-TSB-5-RS

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_cifri_d_tsb_5_rs.yaml`
- Started UTC: 2026-10-08T05:31:58Z
- Finished UTC: 2026-10-08T05:35:09Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1036320`, label `Staphylococcus sp. CIFRI D-TSB-5-RS`. The entire 54-line YAML was read before judgment. It carries `SPECIES`, `BACTERIA`, parent `NCBITaxon:91994`, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero inventoried BacDive strains, and one NCBITAXON name attestation. Its single seed event is dated `2026-09-13T17:54:04Z`. No record, source, history, status, or generated page was changed.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` where applicable.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/staphylococcus_sp_cifri_d_tsb_5_rs.yaml` | Passed; no issues found. |
| `just validate-strict data/taxa/bacteria/staphylococcus_sp_cifri_d_tsb_5_rs.yaml --out /private/tmp/sd5-strict.tsv` | Passed; one file, zero ERROR rows; header-only TSV inspected. |
| Structured inventory comparison | Identity, all ten ancestors, direct parent, genetic code, synonyms, attestation, PATHS entry and scope-derived seed text agree. |
| Lifecycle/type-material lookup | No exact target row in `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` or `dropped.tsv`. |
| Term/reference verification | Live NCBI Taxonomy EFetch and Datasets inspected; nucleotide accession and source qualifiers inspected separately. No record DOI, PMID, LPSN, GTDB, graph or strain reference requires another authority check. |
| History | Embedded seed event inspected. Ignored-inclusive history content and filename searches returned no target history artifact. No history was created; full `just validate-history` not run. |
| `just validate-products` | Not applicable: no curator-added causal graph. |
| Full-corpus gates | Not run: `just verify-corpus`, provenance, render/site drift, documentation statistics, full tests, vendored checks and `just qc`. Focused comparisons are not a claim of full reproduction or corpus health. |

## Identity and Grounding

The pinned `data/raw/ncbitaxon_taxa.tsv:222324` and scientific-name object `data/catalog/ncbi_names-0005.jsonl.gz:31868` identify this exact taxon. The live [NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036320&retmode=xml) agrees with the label, species rank, parent 91994, Bacteria division and genetic code 11. Its labeled ancestors agree with the YAML; [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036320) also returns the full root-inclusive identifier order.

The checked chain is root (1), cellular organisms (131567), Bacteria (2), Bacillati (1783272), Bacillota (1239), Bacilli (91061), Caryophanales (1385), Staphylococcaceae (90964), Staphylococcus (1279), and unclassified Staphylococcus (91994). IDs, labels, ranks and ordering match the pinned backbone. No alternative name is supplied by the inspected pinned name fields or live OtherNames surface. This is an isolate-designated species-rank NCBI concept, not a formally established species epithet or a culture-deposit identifier. `EXACT` denotes grounding to that concept; it is not independent species identification.

`data/taxa/PATHS.tsv:14831` resolves the identifier uniquely to this filename. `curation/seed_scope.tsv:322571` supplies its eligible species-level scope and the reason reproduced in the seed event. No direct children were found in the complete pinned backbone scan.

## Evidence

The NCBITAXON attestation is supported by the exact backbone row: one `NAME`, the same source ID and label, snapshot `2026-09-13`. It is neither a phenotype claim nor a genome count. Its missing mapping predicate is appropriate because the record is the source taxon itself.

The exact-taxon Nuccore query returned one UID, 334303314. The inspected [GenBank record JF799876.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799876.1) is a 1,446-base partial 16S rRNA sequence. Organism, strain `CIFRI D-TSB-5-RS` and `taxon:1036320` match. Source qualifiers give marine water and `India: W.B.`. The references name Behera, Sharma, Das, Chanda and Patra, an unpublished salt-tolerant-bacteria study and their 11 April 2011 direct submission. Creation and update dates are 5 June 2011. Complete top-level, source-feature and reference metadata were read; bases and non-source features were not audited. No culture deposit or assembly is supplied in that inspected source metadata. This marker supports source identity, not a whole genome or a measured salt-tolerance threshold.

The related Behera paper, [DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), was published online in 2014 and in volume 85, pages 957-964 (2015). Publisher metadata/abstract and the [author-uploaded primary text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis) were inspected, including methods and all rows of Tables 1 and 2. Those tables do not list D-TSB-5-RS or JF799876. They include other CIFRI isolates, which cannot supply this record's identification, locality, media or salt phenotype. No quantitative growth result was extracted; rendered figures were not visually audited. This is a rejected near-match, not evidence that the isolate lacks published research everywhere.

## Completeness

No exact target row was found in the complete local raw BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin or BactoTraits taxon inventories. With no pinned descendants, the empty BacDive listing and `strain_count: 0` agree with the local source model. Zero is an inventory count, not an assertion that no biological isolate exists. Empty synonyms, nomenclature, mappings, xrefs and strain/genome links have no demonstrated supported omission. Optional definitions, literature evidence, discussions and mechanisms need not be invented for this seeded record.

Absence checks included ignored and hidden files: `rg --no-ignore --hidden -n -z -i` searched identifier, slug and flexible isolate-name spellings across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 40 candidate rows were inspected as complete parsed JSON or TSV objects. Three concern this target; the other 37 are numeric substring collisions in unrelated sample/assembly identifiers. They do not justify a strain or genome join. All five `SOURCE.json` files were parsed separately, and ignored-independent history filenames were searched. An expanded search for JF799876, the paper DOI and isolate-name variants found only the same three target rows. Filename search over `data/taxa`, reports and history found the one target YAML and no earlier report for this stem.

The live exact-taxon Assembly search returned zero with a phrase-not-found warning; this is bounded query evidence, not a global proof of genome absence. Bounded web searches for the exact designation, shortened spelling and sequence accession did not establish another exact-isolate primary publication. iModulonDB was not applicable: this record has no gene, regulator, expression dataset or mechanistic claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record. The limited assembly query and unverified broader literature coverage remain explicit review limits, not fabricated defects.

## Recommended Edits

None required. Do not add another CIFRI isolate's literature identification, infer a culture deposit from this strain designation, or count the 16S marker as a genome. Do not hand-edit this generated YAML or promote its status from this report.

Future accepted NCBI corrections belong upstream, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`; harmonization fixes belong in `src/taxonmech/seed.py` with tests, and scope decisions in `curation/seed_scope.tsv`. Such changes require a separately authorized curation workflow. This review demonstrates no defect in those owners.

## Follow-up Checks

No mandatory repair is outstanding. For later enrichment, verify an explicit exact-isolate/deposit/source chain and preserve accession version and marker type. For an authorized input or seeder correction, use the documented dry-run seed, single-record canary and focused validators, then full `just verify-corpus`, relevant tests, provenance, generated-product and QC gates before publication. A human curator owns any review-status promotion.

## Additional Notes

Review baseline: HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`. YAML SHA-256 before review and before report creation: `90a747e119ba56e0835fbae5642963cd63ebc31923164cd274e5ce35307366e5`.

The skill, CLAUDE.md, justfile, curation skill/checklist, curation/harmonization/schema guides, history guidance and relevant schema classes were read. The review skill's read-only contract takes precedence over the curation skill's history-scaffolding step. No paid research, source refresh, outbound communication, GitHub mutation, record regeneration or Eukaryota review was performed. Existing worktrees were preserved.
