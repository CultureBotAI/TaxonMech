# YAML Record Review: Pseudoalteromonas sp. 1-Cc-6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_1_cc_6.yaml`
- Started UTC: 2026-10-07T09:48:20Z
- Finished UTC: 2026-10-07T09:50:27Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035761`, Pseudoalteromonas sp. 1-Cc-6, `SPECIES`, `BACTERIA`, parent `NCBITaxon:194690` (unclassified Pseudoalteromonas), ten root-first ancestors, code 11, `EXACT`, `SEEDED` and `strain_count: 0`. It contains one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graph are asserted. The laboratory strain-like label denotes a species-rank NCBI concept, not a registered deposit or formally named species. Generated YAML is read-only. Maintained source extraction and `src/taxonmech/seed.py` own future harmonization fixes; `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` own scope and slug decisions.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` with offline uv resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudoalteromonas_sp_1_cc_6.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudoalteromonas_sp_1_cc_6.yaml --out /private/tmp/pseudoCc6-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/pseudoCc6-strict.tsv` | Actual TSV inspected; header only. |
| Structured backbone, full lineage, seven inventories, scope/path and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target rows. |
| Live NCBI EFetch and Datasets | Identity, parent, rank, code and full ancestry agree. |
| Exact-taxid Assembly/nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete marker metadata read. |
| Related primary paper | Relevant pages/figures inspected; target-specific text search negative, nearby isolate evidence kept separate. |
| Entire target reread | Byte-identical to initial read. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. The bounded comparisons are not substitutes for full-corpus gates.

`just validate-products` was not run because no curator-added graph nodes are present and configured OAK targets exclude NCBI taxonomy. No YAML literature/internal evidence references require a separate citation check. The embedded seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target history artifact within the bounded scope below.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222165` agrees on ID, label, rank, parent, genetic code, empty synonyms and snapshot 2026-09-13. The complete native name row at `data/catalog/ncbi_names-0005.jsonl.gz:31649` confirms the scientific name. Unique path and scope rows are `data/taxa/PATHS.tsv:14665` and `curation/seed_scope.tsv:322431`.

Every ancestor's ID, label, rank and ordering agrees: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Alteromonadales, Pseudoalteromonadaceae, Pseudoalteromonas and unclassified Pseudoalteromonas. Live EFetch confirms the non-root chain, species rank, parent 194690, code 11 and no alternate names; Datasets includes root. The inspected lifecycle inventories contain no target type-material, merge or dropped entry. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035761&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035761)

The unclassified parent is a carried source node, not an assignment to infer. `EXACT` applies to the NCBI concept and does not imply a validly published binomial. Preserve the scientific label's case/hyphens and pinned lowercase filename. Other numbered isolates are not synonyms.

## Evidence

The sole `NCBITAXON` attestation matches ID, label, count 1, unit `NAME` and snapshot note. It counts a source name, not laboratory isolates, deposits or genomes. Complete backbone scanning found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nucleotide search returned UID 333974689, `JF502832.1`: a 975-nt partial 16S rRNA record, partial at both ends, with strain 1-Cc-6 and explicit `taxon:1035761`. Source qualifiers give host Clathrina clathrus, France, November 2007, collectors/identifiers M. Roue and I. Domart-Coulon, and primers 27F/1385R. Submission was 6 March 2011; creation 30 May and update 3 June 2011. All metadata were read, excluding only sequence/translation/transcription payloads. They provide no culture-collection, assembly, BioSample, BioProject, DOI or PMID link. [GenBank JF502832.1](https://www.ncbi.nlm.nih.gov/nuccore/JF502832.1)

GenBank cites an unpublished glycerolipid study by Roue, Domart-Coulon, Jovet and Bourguet-Kondracki and the direct submission. This is submission context, not evidence that every associated isolate produces the referenced metabolites.

The related 2014 primary article DOI `10.6119/JMST-013-0718-2` was inspected from the authors' institutional repository, including the title page and relevant complete printed pages 39-40 and 44-47. Rendered species-affiliation text and Figures 8-9/captions were inspected. Its explicit compound work identifies strain 1-Cc-11; it does not establish those properties for 1-Cc-6. Case-insensitive searches of all 14 pages' extracted text found no JF502832, 1-Cc-6 or 1Cc-6, while finding 1-Cc-11 on PDF pages 5, 10, 11 and 12. The paper's broader isolate-group discussion does not independently resolve this target's membership, and shared genus, host, authors or submission title cannot transfer a phenotype or exact species assignment. This is a bounded attribution check, not exhaustive supplement or literature review. [Primary paper](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers17-06/010070108.pdf)

The only additional initial local candidate, `data/catalog/allthebacteria.tsv.xz:546918`, was read in full. It describes Staphylococcus aureus, SAMEA3322972, run ERR1035761 and analysis ERZ3253644. The digits match a run accession rather than this taxon's identity; no association is justified.

The embedded event agrees with the scope reason and NCBI-only source list. `src/taxonmech/seed.py:_seed_timestamp` takes the newest extraction time from the raw, ATB and StrainInfo manifests. Their times on 2026-09-13 are 17:50:44Z, 17:54:04Z and 17:29:00Z respectively, so the 17:54:04Z event is correct despite this target having no ATB link. A read-only review does not add an event or change status.

iModulonDB is not applicable: the record asserts no gene regulation, functional trait, pathway, stress response or expression module. The marker is taxonomic provenance; chemical findings about another isolate do not create target assertions.

## Completeness

No consequential gap was found. Zero BacDive strains is consistent with the source inventories and lack of descendants. It does not mean no laboratory strain was studied. Neither a partial marker nor an informal isolate name requires a genome link or a culture-deposit entry. Optional definition, literature and graph fields may remain empty.

Both local search stages included ignored/hidden files and compressed catalogs using `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed at each stage; history filenames were independently traversed.

The whole-digit taxid and label/slug search returned four rows: three target rows and the unrelated ATB run. The expanded JF502832 with optional .1 and bare 1-Cc-6 separator/case variants returned only the same three target rows. All matches were read. No marker-accession hit, matching metadata value or target history filename was found within these roots and terms, including ignored files.

The exact-taxid Assembly search returned zero with a phrase-not-found warning; it does not exclude assemblies under another classification. Web searches used exact label/accession and glycerolipid/designation terms. No target-specific experimental publication, deposit or assembly was verified beyond the GenBank metadata. Exhaustive literature retrieval, supplementary-material searches, sequence similarity searches and independent phylogenetic analysis were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML within the inspected scope. Identity, full lineage, source count, zero BacDive strains and seed history agree. Sparse optional enrichment is not a curation defect.

## Recommended Edits

None required. Do not merge neighboring isolate labels, infer a formal species, count JF502832.1 as a genome, create a deposit from the isolate designation, transfer 1-Cc-11 chemistry or promote `SEEDED` to `REVIEWED`.

Future exact-strain evidence should enter through maintained extraction inputs and a tested seeder workflow. Do not hand-edit generated records or pages.

## Follow-up Checks

On a controlled source refresh, repeat the NCBI identity/lineage and exact-taxid Assembly/nuccore queries and compare inventories. Any added association must name 1-Cc-6 or establish a verified deposit/accession chain; a shared host or similar isolate label is insufficient.

For changed maintained inputs, run `just seed`, an authorized `just seed-canary NCBITaxon:1035761`, inspect the entire emitted file, repeat focused schema/strict validation and run `just verify-corpus` plus `just qc`. These are future curation checks, not regeneration performed here.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The entire target was reread and remained byte-identical. The only repository write for this review is this new timestamped report. Strict-validation and PDF artifacts are temporary. No YAML, inventory, old report, status/history, generated page, worktree or GitHub item was changed.
