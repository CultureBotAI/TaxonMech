# YAML Record Review: Pseudoalteromonas sp. 2-Cc-10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_2_cc_10.yaml`
- Started UTC: 2026-10-07T10:19:00Z
- Finished UTC: 2026-10-07T10:21:11Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord`: `NCBITaxon:1035768`, Pseudoalteromonas sp. 2-Cc-10, `SPECIES`, `BACTERIA`, parent `NCBITaxon:194690`, ten root-first lineage entries, genetic code 11, `EXACT`, `SEEDED`, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, strains/deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graph are asserted. The informal strain-like designation identifies a species-rank NCBI concept, not a formal binomial or registered deposit. Generated YAML is read-only. Maintained extraction inputs and `src/taxonmech/seed.py` own future harmonization fixes; scope and slug changes belong to `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudoalteromonas_sp_2_cc_10.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudoalteromonas_sp_2_cc_10.yaml --out /private/tmp/pseudo2Cc10-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/pseudo2Cc10-strict.tsv` | Actual TSV inspected; header only. |
| Full backbone/lineage, seven inventory, path/scope and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target rows. |
| Live NCBI EFetch and Datasets | Identity, parent, rank, code and full ancestry agree. |
| Exact-taxid Assembly/nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete marker metadata read. |
| Related primary paper | Previously inspected primary pages/Figure 8 reused; new target-specific search of all 14 pages completed. |
| Entire target reread | Byte-identical to initial read. |

Not checked: full-corpus `just verify-corpus`, `just qc`, schema-all, tests, provenance hashing, generated-page drift, documentation statistics and vendored gates. The focused comparisons do not substitute for these gates.

`just validate-products` was not run: no curator-added graph nodes exist and OAK excludes NCBI taxonomy. There are no YAML literature/internal evidence references needing citation validation. The embedded seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target artifact in the bounded history scope below.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222172` agrees on identifier, label, species rank, parent, code, empty synonyms and snapshot 2026-09-13. The complete native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31656`. Unique path and scope rows are `data/taxa/PATHS.tsv:14672` and `curation/seed_scope.tsv:322438`.

Every ancestor ID, label, rank and position agrees: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Alteromonadales, Pseudoalteromonadaceae, Pseudoalteromonas and unclassified Pseudoalteromonas. Live EFetch confirms non-root ancestry, parent 194690, species rank, code 11 and no alternate names; Datasets includes root. Inspected lifecycle inventories contain no target retirement, merge or type-material row. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035768&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035768)

The unclassified parent is carried NCBI placement, not a formal-species assignment. `EXACT` refers to the source concept, not nomenclatural validity. The full designation and pinned slug distinguish this isolate from similar numbered names.

## Evidence

The sole `NCBITAXON` attestation agrees on ID, label, count 1, unit `NAME` and snapshot. It counts a taxonomic name, not strains or genomes. Full backbone scanning found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore search returned UID 333974687, `JF502830.1`: a 1,087-nt partial 16S rRNA sequence, partial at both ends, with strain 2-Cc-10 and explicit `taxon:1035768`. Source qualifiers list host Clathrina clathrus, France, collectors/identifiers M. Roue and I. Domart-Coulon, and primers 27F/1385R. No collection-date qualifier is supplied. Submission was 6 March 2011, creation 30 May and update 3 June 2011. All metadata were inspected except nucleotide/translation/transcription payloads; they contain no culture-collection, assembly, BioSample, BioProject, DOI or PMID link. [GenBank JF502830.1](https://www.ncbi.nlm.nih.gov/nuccore/JF502830.1)

GenBank lists an unpublished glycerolipid study by Roue, Domart-Coulon, Jovet and Bourguet-Kondracki and a direct submission naming Coulon and Roue. The shared study title is not experimental chemistry evidence for every associated isolate. Do not transfer another accession's collection date or 1492R primer to this record.

The related 2014 primary article, DOI `10.6119/JMST-013-0718-2`, was previously inspected in this ongoing review: title page, complete printed pages 40, 45 and 46, and rendered Figure 8/caption. Those methods/results attribute the pure-culture chemistry to 1-Cc-11. New case-insensitive searches for this target across all 14 pages' extracted text found no JF502830, 2-Cc-10 or 2Cc-10; 1-Cc-11 occurs on PDF pages 5, 10, 11 and 12. Shared host, genus and authors do not transfer chemical, ecological or formal-species claims to the target. This is a bounded attribution check, not exhaustive supplementary-material or literature coverage. [Primary paper](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers17-06/010070108.pdf)

The extra initial catalog hit at `data/catalog/allthebacteria.tsv.xz:546930` was read fully: Staphylococcus aureus, SAMEA3322984, ERR1035768 and ERZ3253649. The matching digits are in a sequencing-run accession, not a taxonomy field; the row supplies no target genome association.

The seed event matches the scope reason and NCBI-only source list. Inspected, unchanged `src/taxonmech/seed.py:_seed_timestamp` selects the latest raw/ATB/StrainInfo manifest extraction time. Their checked times are 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z respectively. The event's 17:54:04Z time is consistent without a target ATB link. No review event or status promotion was made.

iModulonDB is not applicable: the YAML asserts no gene, regulator, functional pathway, stress response or transcriptomic module. A taxonomic marker and neighboring-isolate chemistry do not supply target expression evidence.

## Completeness

No consequential gap was found. `strain_count: 0` counts BacDive records in this source subtree, not every named laboratory isolate. Partial 16S is not a genome, and a bare strain designation is not a deposit. Optional definitions, literature and graphs may remain empty. A missing collection date in the external marker metadata is not an unsupported assertion in the YAML.

Both local searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored/hidden files and compressed catalogs. All five excluded `SOURCE.json` files were separately parsed at each stage; history filenames were independently traversed.

The initial whole-digit taxid and label/slug search returned four rows: three target rows and the unrelated ATB run. Expanded JF502830 with optional .1 and bare 2-Cc-10 case/separator searches returned only the three target rows. All matches were inspected. No marker-accession hit, matching metadata value or target history filename was found within these bounded roots/terms, including ignored files. An ignored-independent report-filename search found no existing review for this stem before creation.

Exact-taxid Assembly search returned zero with a phrase-not-found warning; this does not exclude assemblies classified elsewhere. Exact-label/accession and designation/glycerolipid web searches supplied no additional verified target-specific publication, deposit or assembly. Exhaustive literature/supplement retrieval, sequence similarity and independent phylogenetic analysis were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, full lineage, attestation, zero BacDive count and seed event agree. Sparse optional enrichment is not itself a defect.

## Recommended Edits

None required. Preserve the full label, NCBI placement and `SEEDED` status. Do not merge similar designations, infer a formal species, count JF502830.1 as a genome, mint a deposit from the designation, invent a collection date or transfer chemistry from 1-Cc-11.

Future exact-strain associations should enter maintained extraction inputs and the tested seeder, not manual generated-YAML or page edits.

## Follow-up Checks

On an authorized source refresh, repeat exact NCBI identity/lineage and Assembly/nuccore queries and compare updated inventories. New associations need the exact designation or a verified explicit deposit/accession chain.

If maintained inputs change, run `just seed`, an authorized `just seed-canary NCBITaxon:1035768`, inspect the full emitted YAML, repeat focused schema/strict validation and run `just verify-corpus` plus `just qc`. These are future curation checks, not regeneration performed here.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Review guidance and relevant schema/seeder files remain unchanged from their prior complete inspection. The full target reread was byte-identical. This timestamped report is the only repository write for this review. No YAML, inventory, previous report, history/status, generated page, worktree or GitHub item was changed. Strict-output and primary-PDF artifacts are temporary.
