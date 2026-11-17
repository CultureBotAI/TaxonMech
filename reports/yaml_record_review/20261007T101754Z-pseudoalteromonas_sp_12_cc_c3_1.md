# YAML Record Review: Pseudoalteromonas sp. 12-Cc-C3-1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_12_cc_c3_1.yaml`
- Started UTC: 2026-10-07T10:15:49Z
- Finished UTC: 2026-10-07T10:17:54Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read: `NCBITaxon:1035767`, Pseudoalteromonas sp. 12-Cc-C3-1, `SPECIES`, `BACTERIA`, parent `NCBITaxon:194690`, ten root-first ancestors, code 11, `EXACT`, `SEEDED`, `strain_count: 0`, one NCBI name attestation and one seed event.

The YAML asserts no synonyms, nomenclature, mappings, strains/deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graph. The strain-like designation denotes a species-rank source concept, not a registered deposit or formal binomial. Generated YAML is read-only. Maintained extraction inputs and `src/taxonmech/seed.py` own future source/harmonization fixes; `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` own scope and slug changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudoalteromonas_sp_12_cc_c3_1.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudoalteromonas_sp_12_cc_c3_1.yaml --out /private/tmp/pseudo12CcC31-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/pseudo12CcC31-strict.tsv` | Actual TSV inspected; header only. |
| Complete backbone/lineage, seven inventory, scope/path and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target rows. |
| Live NCBI EFetch and Datasets | Identity, parent, rank, code and full ancestry agree. |
| Exact-taxid Assembly/nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete marker metadata read. |
| Related primary paper | Previously inspected primary text/Figure 8 reused; new target-term search over all 14 pages completed. |
| Complete target reread | Byte-identical to initial read. |

Not checked: full-corpus `just verify-corpus`, `just qc`, schema-all, tests, provenance hashing, generated-page drift, documentation statistics and vendored gates. These focused checks are not substitutes for corpus-wide gates.

`just validate-products` was not run because no curator-added graph nodes exist and OAK excludes NCBI taxonomy. There are no YAML literature/internal evidence references needing citation validation. The embedded seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target history artifact within the bounded scope below.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222171` agrees on identifier, label, rank, parent, code, empty synonyms and snapshot 2026-09-13. The complete native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31655`. Unique path and scope rows are `data/taxa/PATHS.tsv:14671` and `curation/seed_scope.tsv:322437`.

All ancestor IDs, labels, ranks and ordering agree: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Alteromonadales, Pseudoalteromonadaceae, Pseudoalteromonas and unclassified Pseudoalteromonas. Live EFetch confirms non-root ancestry, species rank, parent 194690, code 11 and no alternate names; Datasets includes root. Inspected lifecycle inventories contain no target retirement, merge or type-material row. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035767&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035767)

The unclassified parent is carried source placement. `EXACT` means identity with that NCBI concept, not nomenclatural validity. Preserve the full designation and pinned slug; nearby numbered isolates are not synonyms.

## Evidence

The sole `NCBITAXON` attestation agrees on ID, label, count 1, unit `NAME` and snapshot. It counts a name, not deposits or genomes. Full backbone scanning found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nucleotide search returned UID 333974694, `JF502837.1`: a 1,344-nt partial 16S rRNA sequence, partial at both ends, with strain 12-Cc-C3-1 and explicit `taxon:1035767`. Source qualifiers list host Clathrina clathrus, France, March 2010, collectors/identifiers M. Roue and I. Domart-Coulon, and primers 27F/1492R. Submission was 6 March 2011; creation 30 May and update 3 June 2011. All metadata were inspected except nucleotide/translation/transcription payloads. They supply no culture-collection, assembly, BioSample, BioProject, DOI or PMID link. [GenBank JF502837.1](https://www.ncbi.nlm.nih.gov/nuccore/JF502837.1)

The GenBank references are direct submission and an unpublished glycerolipid study by Roue, Domart-Coulon, Jovet and Bourguet-Kondracki. That shared study title is submission context, not experimental chemistry evidence for every isolate. Preserve this accession's March 2010 collection date rather than transferring neighboring isolates' dates.

The related 2014 primary paper, DOI `10.6119/JMST-013-0718-2`, has already been inspected in this ongoing review: title page, complete printed pages 40, 45 and 46, and rendered Figure 8/caption. Those methods/results attribute the pure-culture chemical work to 1-Cc-11. For this target, new case-insensitive searches of all 14 pages' extracted text found no JF502837, 12-Cc-C3-1 or 12Cc-C3-1; 1-Cc-11 occurs on PDF pages 5, 10, 11 and 12. Shared host, genus and authors do not transfer that strain's chemistry, ecology or formal-species assignment. This is a bounded attribution check, not exhaustive supplementary-material or literature coverage. [Primary paper](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers17-06/010070108.pdf)

The extra initial local hit at `data/catalog/allthebacteria.tsv.xz:547455` was read fully: Staphylococcus aureus, SAMEA3339739, ERR1035767 and ERZ3254318. The target digits occur in a sequencing-run accession, not a taxonomy field. This is not target genome evidence.

The seed event agrees with the scope reason and NCBI-only source list. The inspected, unchanged `src/taxonmech/seed.py:_seed_timestamp` chooses the latest manifest extraction time among raw, ATB and StrainInfo. Their freshly checked times are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z respectively. The 17:54:04Z event is consistent without a target ATB association. No review event or status promotion was made.

iModulonDB is not applicable: no gene, regulator, functional pathway, stress response or transcriptomic module is asserted. A taxonomic marker and another isolate's chemistry do not create target expression evidence.

## Completeness

No consequential gap was found. `strain_count: 0` counts BacDive records in the source subtree, not every laboratory isolate. Partial 16S is not a genome; a strain designation is not a registered deposit. Optional definitions, literature and graphs can remain empty.

Both local searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored/hidden files and compressed catalogs. All five excluded `SOURCE.json` files were separately parsed at each stage; history filenames were independently traversed.

The initial whole-digit taxid and label/slug search returned four rows: three target rows and the unrelated ATB run. Expanded JF502837 with optional .1 and bare 12-Cc-C3-1 case/separator searches returned only those three target rows. Every matched row was inspected. No marker-accession hit, matching metadata value or target history filename was found within those bounded roots/terms, including ignored files. An ignored-independent report-filename search found no existing report for this stem before creation.

The exact-taxid Assembly query returned zero with a phrase-not-found warning; this does not exclude assemblies classified elsewhere. Exact-label/accession and designation/glycerolipid web searches supplied no additional verified target-specific publication, deposit or assembly. Exhaustive literature/supplement retrieval, sequence similarity and independent phylogenetic analysis were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, complete lineage, attestation, zero BacDive count and seed event agree. Sparse optional enrichment is not a defect.

## Recommended Edits

None required. Preserve the full designation, NCBI placement and `SEEDED` status. Do not merge neighboring labels, infer a formal species, promote JF502837.1 to a genome, create a deposit from the designation or transfer chemistry from 1-Cc-11.

Future exact-strain associations should enter maintained extraction inputs and the tested seeder, not hand-edited generated YAML or pages.

## Follow-up Checks

On an authorized source refresh, repeat exact NCBI identity/lineage and Assembly/nuccore searches and compare updated inventories. New associations need the exact designation or an explicit verified deposit/accession chain.

If maintained inputs change, run `just seed`, an authorized `just seed-canary NCBITaxon:1035767`, inspect the entire emitted YAML, repeat focused schema/strict checks and run `just verify-corpus` plus `just qc`. These are future curation checks, not regeneration performed here.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Review guidance and relevant schema/seeder files remain unchanged from their prior complete inspection. The full target reread was byte-identical. This new timestamped report is the only repository write for this review. No YAML, inventory, previous report, history/status, generated page, worktree or GitHub item was changed. Strict-output and primary-PDF artifacts are temporary.
