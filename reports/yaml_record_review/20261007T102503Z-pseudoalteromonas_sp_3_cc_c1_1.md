# YAML Record Review: Pseudoalteromonas sp. 3-Cc-C1-1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_3_cc_c1_1.yaml`
- Started UTC: 2026-10-07T10:23:02Z
- Finished UTC: 2026-10-07T10:25:03Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035769`, Pseudoalteromonas sp. 3-Cc-C1-1, `SPECIES`, `BACTERIA`, parent `NCBITaxon:194690`, ten root-first ancestors, code 11, `EXACT`, `SEEDED`, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, mappings, strains/deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graph are asserted. The designation identifies a species-rank NCBI concept, not a registered deposit or formal binomial. Generated YAML is read-only. Maintained extraction inputs and `src/taxonmech/seed.py` own future source/harmonization fixes; `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` own scope and slug changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudoalteromonas_sp_3_cc_c1_1.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudoalteromonas_sp_3_cc_c1_1.yaml --out /private/tmp/pseudo3CcC11-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/pseudo3CcC11-strict.tsv` | Actual TSV inspected; header only. |
| Full backbone/lineage, seven inventory, scope/path and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target rows. |
| Live NCBI EFetch and Datasets | Identity, parent, rank, code and complete ancestry agree. |
| Exact-taxid Assembly/nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete marker metadata read. |
| Related primary paper | Previously inspected primary text/Figure 8 reused; new target-specific text search across all 14 pages completed. |
| Entire target reread | Byte-identical to initial read. |

Not checked: full-corpus `just verify-corpus`, `just qc`, schema-all, tests, provenance hashing, generated-page drift, documentation statistics and vendored gates. Focused comparisons are not substitutes for these gates.

`just validate-products` was not run: no curator-added graph nodes exist and OAK excludes NCBI taxonomy. There are no YAML literature/internal evidence references needing citation validation. The embedded seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target history artifact within the bounded scope below.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222173` agrees on identifier, label, rank, parent, code, empty synonyms and snapshot 2026-09-13. The full native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31657`. Unique path and scope rows are `data/taxa/PATHS.tsv:14673` and `curation/seed_scope.tsv:322439`.

All ancestor IDs, labels, ranks and ordering agree: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Alteromonadales, Pseudoalteromonadaceae, Pseudoalteromonas and unclassified Pseudoalteromonas. Live EFetch confirms non-root ancestry, parent 194690, species rank, code 11 and no alternate names; Datasets includes root. Inspected lifecycle inventories contain no target retirement, merge or type-material row. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035769&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035769)

The unclassified parent is carried NCBI placement. `EXACT` refers to that source concept, not nomenclatural validity. Preserve the full designation and pinned slug; similarly numbered isolates are not synonyms.

## Evidence

The sole `NCBITAXON` attestation agrees on identifier, label, count 1, unit `NAME` and snapshot. It counts a name, not deposits or genomes. Full backbone scanning found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore search returned UID 333974688, `JF502831.1`: a 705-nt partial 16S rRNA sequence, partial at both ends, with strain 3-Cc-C1-1 and explicit `taxon:1035769`. Source qualifiers list host Clathrina clathrus, France, June 2008, collectors/identifiers M. Roue and I. Domart-Coulon, and primers 27F/1385R. Submission was 6 March 2011; creation 30 May and update 3 June 2011. Complete metadata were read except nucleotide/translation/transcription payloads. They supply no culture-collection, assembly, BioSample, BioProject, DOI or PMID link. [GenBank JF502831.1](https://www.ncbi.nlm.nih.gov/nuccore/JF502831.1)

GenBank lists direct submission and an unpublished glycerolipid study by Roue, Domart-Coulon, Jovet and Bourguet-Kondracki. The shared title is submission context, not experimental chemical evidence for every isolate. Preserve this marker's length, date and primer pair rather than importing neighboring accessions' metadata.

The related 2014 primary article, DOI `10.6119/JMST-013-0718-2`, was previously inspected during this ongoing review: title page, complete printed pages 40, 45 and 46, and rendered Figure 8/caption. Those methods/results attribute the pure-culture chemistry to 1-Cc-11. New case-insensitive searches of all 14 pages' extracted text found no JF502831, 3-Cc-C1-1 or 3Cc-C1-1; 1-Cc-11 occurs on PDF pages 5, 10, 11 and 12. Shared host, genus and authorship do not transfer chemical, ecological or formal-species claims. This is a bounded attribution check, not exhaustive supplementary-material or literature coverage. [Primary paper](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers17-06/010070108.pdf)

The extra initial catalog hit at `data/catalog/allthebacteria.tsv.xz:546932` was read in full: Staphylococcus aureus, SAMEA3322986, ERR1035769 and ERZ3253664. The matching digits occur in a sequencing-run accession, not a taxonomy field; the row supplies no target genome association.

The event matches the scope reason and NCBI-only source list. Inspected, unchanged `src/taxonmech/seed.py:_seed_timestamp` selects the latest extraction time among raw, ATB and StrainInfo manifests. Freshly checked times are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z respectively. The event's 17:54:04Z time is consistent without a target ATB link. No review event or status promotion was made.

iModulonDB is not applicable: no gene, regulator, functional pathway, stress response or transcriptomic module is asserted. A taxonomic marker and another isolate's chemistry do not establish target expression evidence.

## Completeness

No consequential gap was found. `strain_count: 0` counts BacDive records in the source subtree, not all laboratory isolates. Partial 16S is not a genome, and a bare designation is not a culture deposit. Optional definitions, literature and graphs may remain empty.

Both local searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored/hidden files and compressed catalogs. All five excluded `SOURCE.json` files were separately parsed at each stage; history filenames were independently traversed.

Initial whole-digit taxid and label/slug searches returned four rows: three target rows and the unrelated ATB run. Expanded JF502831 with optional .1 and bare 3-Cc-C1-1 case/separator searches returned only the same three target rows. Every matched row was inspected. No marker-accession hit, matching metadata value or target history filename was found within these bounded roots/terms, including ignored files. An ignored-independent report-filename search found no existing review for this stem before creation.

Exact-taxid Assembly search returned zero with a phrase-not-found warning; this does not exclude assemblies classified elsewhere. Exact-label/accession and designation/glycerolipid web searches supplied no additional verified target-specific publication, deposit or assembly. Exhaustive literature/supplement retrieval, sequence similarity and independent phylogenetic analysis were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, complete lineage, attestation, zero BacDive count and seed event agree. Sparse optional enrichment is not a defect.

## Recommended Edits

None required. Preserve the full label, NCBI placement and `SEEDED` status. Do not merge similar designations, infer a formal species, count JF502831.1 as a genome, mint a deposit from the label or transfer chemistry from 1-Cc-11.

Future exact-strain associations should enter maintained extraction inputs and the tested seeder, not hand-edited generated YAML or pages.

## Follow-up Checks

On an authorized source refresh, repeat exact NCBI identity/lineage and Assembly/nuccore queries and compare updated inventories. New associations require the exact designation or an explicit verified deposit/accession chain.

If maintained inputs change, run `just seed`, an authorized `just seed-canary NCBITaxon:1035769`, inspect the full emitted YAML, repeat focused schema/strict validation and run `just verify-corpus` plus `just qc`. These are future curation checks, not regeneration performed here.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Relevant guidance, schema and seeder files remain unchanged from prior full inspection. The entire target reread was byte-identical. This new timestamped report is the only repository write for this review. No YAML, inventories, previous reports, history/status, generated pages, worktrees or GitHub items were changed. Strict-output and primary-PDF artifacts are temporary.
