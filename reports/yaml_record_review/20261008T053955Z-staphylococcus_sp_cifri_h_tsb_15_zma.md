# YAML Record Review: Staphylococcus sp. CIFRI H-TSB-15-ZMA

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_cifri_h_tsb_15_zma.yaml`
- Started UTC: 2026-10-08T05:36:17Z
- Finished UTC: 2026-10-08T05:39:55Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1036321`, label `Staphylococcus sp. CIFRI H-TSB-15-ZMA`. All 54 YAML lines were read before judgment. The record carries species rank, BACTERIA domain, parent `NCBITaxon:91994`, genetic code 11, `EXACT` grounding, `SEEDED` status, zero inventoried BacDive strains, one NCBITAXON name attestation, and a single seed event dated `2026-09-13T17:54:04Z`. No record, source, history, status or generated page was changed.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` where applicable.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/staphylococcus_sp_cifri_h_tsb_15_zma.yaml` | Passed; no issues found. |
| `just validate-strict data/taxa/bacteria/staphylococcus_sp_cifri_h_tsb_15_zma.yaml --out /private/tmp/sh15-strict.tsv` | Passed; one file, zero ERROR rows. Header-only TSV read. |
| Structured source comparison | Exact identity, parent, genetic code, all ten lineage entries, synonyms, source attestation, PATHS entry and scope-derived seed text agree. |
| Type/lifecycle lookup | No exact target entry in `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` or `dropped.tsv`. |
| Authority/reference checks | Live NCBI Taxonomy EFetch and Datasets checked; the exact nucleotide record's source and reference metadata inspected. No record DOI, PMID, LPSN, GTDB, graph or strain link requires a further authority check. |
| History | Embedded seed event checked. Ignored-inclusive content and filename searches found no target history artifact. No history was written; full `just validate-history` not run. |
| `just validate-products` | Not applicable: no curator-added graph nodes. |
| Full-corpus gates | Not run: `just verify-corpus`, provenance, render/site drift, documentation statistics, full tests, vendored checks or `just qc`. These focused results do not prove complete corpus reproduction. |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222325` gives the exact record ID, label, species rank, parent 91994 and code 11. `data/catalog/ncbi_names-0005.jsonl.gz:31869` supplies its scientific name. The live [NCBI Taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036321&retmode=xml) agrees with those fields and the labeled ancestry. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036321) agrees with the species rank and root-inclusive identifier order.

All ten pinned ancestors were individually compared: root (1), cellular organisms (131567), Bacteria (2), Bacillati (1783272), Bacillota (1239), Bacilli (91061), Caryophanales (1385), Staphylococcaceae (90964), Staphylococcus (1279), and unclassified Staphylococcus (91994). IDs, labels, ranks and order agree. No alternative name occurs in the inspected pinned synonym fields or live OtherNames surface. The target is an isolate-designated NCBI species-rank concept, not a formal species epithet, another CIFRI isolate or a registered culture deposit. Exact grounding to that concept does not independently resolve biological species identification.

The unique identifier-to-slug entry is `data/taxa/PATHS.tsv:14832`; the scope row is `curation/seed_scope.tsv:322572`. Its reason matches the seed event. A complete pinned-backbone scan found no direct children. Species rank satisfies the repository scope rule despite the unclassified parent.

## Evidence

The sole NCBITAXON attestation matches the raw row: the same ID and label, one `NAME`, and snapshot `2026-09-13`. No mapping predicate is needed when the record is that source concept. This count is not a phenotype, strain count or genome count.

Exact-taxon Nuccore search returned one UID, 334303342. [GenBank JF799904.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799904.1) is a 1,436-base partial 16S rRNA sequence with matching organism, strain `CIFRI H-TSB-15-ZMA`, and `taxon:1036321`. Source qualifiers state marine water and `India: W.B.`. References name Behera, Sharma, Das, Chanda and Patra, an unpublished salt-tolerant-bacteria study and their 11 April 2011 direct submission. Creation/update dates are 5 June 2011. Complete top-level, source-feature and reference metadata were read; bases and non-source features were not examined. No culture deposit or assembly occurs in that inspected source metadata. The marker supports source identity, not a whole genome, a quantitative salt phenotype or a new species name.

The related [Behera paper, DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), has verified publisher metadata/abstract and an [author-uploaded primary text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis), inspected during this review session. It appeared online in 2014 and in volume 85, pages 957-964 (2015). Its methods and all Table 1 and Table 2 rows were read. Neither H-TSB-15-ZMA nor JF799904 occurs in those tables. Other Haldia or CIFRI designations are not substitutes for this target, so their identification, place, medium and salt results are not transferred. No rendered-figure or quantitative-growth audit is claimed. The paper is a rejected near-match, not direct target evidence.

## Completeness

Complete raw BacDive, LPSN, GTDB mapping, GOLD organism, MediaDive, Madin and BactoTraits taxon inventories contain no exact target row. No pinned descendants provide another route for BacDive inheritance. Thus `strain_count: 0` and the empty strain list accurately describe the local inventory, not the absence of a biological isolate. Empty synonyms, nomenclature, mappings, xrefs and strain/genome links have no demonstrated supported omission. Optional definitions, record-level literature, discussions and mechanisms need not be invented.

Ignored and hidden files were included in `rg --no-ignore --hidden -n -z -i` searches for the numeric ID, slug and flexible isolate-name variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 17 candidate rows were read as complete parsed JSON or TSV objects. Three concern the target. Fourteen are unrelated numeric collisions: ten plant GOLD project sample IDs, an E. coli sample, one metagenome's length in NCBI and GTDB, and an ATB row for the unrelated E. coli sample. None is an exact isolate/deposit link. All five `SOURCE.json` files were parsed separately; history filenames were also searched independently of ignore rules. Expanded searches for JF799904, the paper DOI and isolate-name variants found only the same three target rows. An ignored-inclusive filename search over `data/taxa`, reports and history found only the one target YAML and no existing report for its stem.

The exact-taxon Assembly query returned zero with a phrase-not-found warning, not proof that no genome exists globally. Exact/shortened designation and accession web searches did not establish another exact-isolate primary paper; broad literature completeness remains unproved. iModulonDB was not applicable because the record contains no gene, regulator, transcriptomic dataset or mechanism claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Bounded negative searches and unaudited broader literature are limitations, not evidence of a record defect.

## Recommended Edits

None required. Do not infer culture deposits from the designation, count the 16S sequence as a genome, transfer another CIFRI isolate's claims, hand-edit the generated YAML, or promote its mapping status based on this report.

Future accepted taxonomy corrections belong upstream in NCBI, then through the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. A demonstrated harmonization error belongs in `src/taxonmech/seed.py` with tests; scope decisions belong in `curation/seed_scope.tsv`. No such owner defect was established here, and any curation requires separate authorization.

## Follow-up Checks

No mandatory repair is outstanding. Later strain/genome enrichment requires an explicit exact-isolate/deposit/source chain and correct marker-versus-genome typing. After a separately authorized upstream or seeder correction, run the documented seed dry run, single-record canary, focused validators and full reproduction, provenance, relevant test, generated-product and QC gates. A human curator owns review-status promotion.

## Additional Notes

Baseline HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`. Initial and pre-report YAML SHA-256 agree: `ca2eb39477af9534c1202248911b69e30d781fcfdcea374a19a7ec9e2d5e7542`.

The review skill, CLAUDE.md, justfile, curation skill/checklist, curation/harmonization/schema guides, history guide and relevant schema classes were read during this unchanged-HEAD session. The review skill's read-only contract overrides history scaffolding. This is an individual review, not an inferred verdict from neighboring records. No paid research, source refresh, record regeneration, outreach, GitHub mutation or Eukaryota review occurred; existing worktrees were preserved.
