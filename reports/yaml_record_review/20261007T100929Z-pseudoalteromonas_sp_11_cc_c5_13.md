# YAML Record Review: Pseudoalteromonas sp. 11-Cc-C5-13

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_11_cc_c5_13.yaml`
- Started UTC: 2026-10-07T10:06:36Z
- Finished UTC: 2026-10-07T10:09:29Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read: `NCBITaxon:1035765`, Pseudoalteromonas sp. 11-Cc-C5-13, `SPECIES`, `BACTERIA`, parent `NCBITaxon:194690`, ten root-first ancestors, genetic code 11, `EXACT`, `SEEDED`, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, mappings, deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graph are asserted. This species-rank source concept has a strain-like designation, not a formal binomial or culture-deposit identifier. Generated YAML is read-only; future source/harmonization fixes belong to maintained extraction inputs and `src/taxonmech/seed.py`, while scope/slug changes belong to `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudoalteromonas_sp_11_cc_c5_13.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudoalteromonas_sp_11_cc_c5_13.yaml --out /private/tmp/pseudo11CcC513-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/pseudo11CcC513-strict.tsv` | Actual TSV inspected; header only. |
| Structured backbone, full lineage, seven inventories, path/scope and attestation checks | Bounded comparisons passed. |
| Exact type-material, merged-ID and dropped-record scans | No target rows. |
| Live NCBI EFetch and Datasets | Identity, parent, rank, code and full ancestry agree. |
| Exact-taxid Assembly/nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete marker metadata inspected. |
| Related primary paper | Title page and printed pages 40, 45 and 46 read; rendered Figure 8/caption inspected; target terms searched across all 14 pages. |
| Full target reread | Byte-identical to initial read. |

Not checked: full-corpus `just verify-corpus`, `just qc`, schema-all, tests, provenance hashing, generated-page drift, documentation statistics and vendored gates. The focused comparisons are not substitutes for those checks.

`just validate-products` was not run: no curator-added graph nodes exist, and OAK targets exclude NCBI taxonomy. No YAML literature or internal evidence references require citation validation. The embedded seed event was checked. `just validate-history` was not run because the ignored-independent content and filename searches found no target history artifact within the bounded scope below.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222169` agrees on identifier, label, species rank, parent, code, empty synonyms and snapshot 2026-09-13. The complete native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31653`. Unique lockfile and scope rows are `data/taxa/PATHS.tsv:14669` and `curation/seed_scope.tsv:322435`.

All ancestor IDs, labels, ranks and ordering match the source: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Alteromonadales, Pseudoalteromonadaceae, Pseudoalteromonas and unclassified Pseudoalteromonas. EFetch confirms the non-root ancestry, parent 194690, species rank, code 11 and no alternate names; Datasets includes root. Inspected lifecycle inventories contain no target retirement, merge or type-material row. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035765&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035765)

The unclassified placement is carried NCBI lineage, not an inferred assignment to a formal species. `EXACT` describes identity with that source concept, not nomenclatural validity. Preserve the complete designation and pinned slug; nearby numbered isolates are distinct.

## Evidence

The `NCBITAXON` attestation matches the backbone ID, label, count 1, unit `NAME` and snapshot. It counts a taxonomic name, not a strain deposit or genome. Complete backbone scanning found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

The exact-taxid nucleotide result is UID 333974693, `JF502836.1`: a 1,232-nt partial 16S rRNA sequence, partial at both ends, with strain 11-Cc-C5-13 and explicit `taxon:1035765`. Source qualifiers specify Clathrina clathrus, France, November 2009, collectors/identifiers M. Roue and I. Domart-Coulon, and primers 27F/1492R. Submission was 6 March 2011, creation 30 May and update 3 June 2011. All metadata were inspected except nucleotide/translation/transcription payloads. They contain no culture-collection, BioSample, BioProject, assembly, DOI or PMID link. [GenBank JF502836.1](https://www.ncbi.nlm.nih.gov/nuccore/JF502836.1)

GenBank supplies a direct submission and an unpublished glycerolipid-study reference by Roue, Domart-Coulon, Jovet and Bourguet-Kondracki. Its title concerns sponge-associated Pseudoalteromonas but does not establish experimentally measured chemistry for every submitted isolate.

The related 2014 primary article, DOI `10.6119/JMST-013-0718-2`, was checked in the institutional-repository PDF. Its title page confirms identity; complete printed pages 40, 45 and 46 and the rendered Figure 8/caption attribute the pure-culture chemistry to 1-Cc-11. Case-insensitive searches of all 14 pages' extracted text found no JF502836, 11-Cc-C5-13 or 11Cc-C5-13; 1-Cc-11 occurs on PDF pages 5, 10, 11 and 12. This supports an attribution boundary, not a phenotype or species assignment for the target. Supplementary material and the entire literature were not exhaustively audited. [Primary paper](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers17-06/010070108.pdf)

The additional initial local hit at `data/catalog/allthebacteria.tsv.xz:546924` was read in full: Staphylococcus aureus, SAMEA3322978, ERR1035765 and ERZ3253648. Target digits occur in a sequencing-run accession, not a taxonomic identity. This is not a target genome association.

The embedded event agrees with the scope reason and NCBI-only attestation. `src/taxonmech/seed.py:_seed_timestamp` selects the latest extraction time among raw, ATB and StrainInfo manifests: respectively 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. The event time 17:54:04Z is correct without implying a target ATB link. No review event or status promotion was made.

iModulonDB is not applicable: this taxonomy-only YAML asserts no gene, regulator, functional pathway, stress response or transcriptomic module. A marker and another isolate's chemistry do not establish target expression evidence.

## Completeness

No consequential gap was found. `strain_count: 0` means no BacDive records in the source subtree, not no laboratory isolates. A partial marker is not a genome; the designation is not a deposit. Optional literature, definitions and graphs may remain empty.

Both local searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored/hidden files and compressed catalogs. The five excluded `SOURCE.json` files were separately parsed in full at each stage; history filenames were independently traversed.

The initial whole-digit taxid and label/slug search found four rows: three target rows and the unrelated ATB run. Expanded searches for JF502836 with optional .1 and bare 11-Cc-C5-13 case/separator variants found only those same three target rows. Every matching row was inspected. No target marker-accession hit, metadata value or history filename was found within those bounded roots/terms, including ignored files. A report-filename search including ignored files confirmed no existing review for this stem before creation.

Exact-taxid Assembly search returned zero with a phrase-not-found warning; this does not exclude assemblies classified elsewhere. Exact-label/accession and designation/glycerolipid web searches supplied no additional verified target publication, deposit or assembly. Sequence similarity, independent phylogeny and exhaustive literature/supplement searches were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. The source identity, complete lineage, attestation, BacDive count and seed event agree. Sparse optional enrichment is not a defect.

## Recommended Edits

None required. Keep the full designation, NCBI placement and `SEEDED` status. Do not infer a formal species, merge neighboring isolates, count JF502836.1 as a genome, create a deposit from a bare designation or transfer chemistry from 1-Cc-11.

Future exact-strain associations should enter maintained extraction inputs and the tested seeder, not manual generated-YAML or page edits.

## Follow-up Checks

On an authorized source refresh, repeat exact NCBI identity/lineage and Assembly/nuccore queries and compare updated inventories. New associations require the exact designation or a verified deposit/accession chain.

If maintained inputs change, run `just seed`, an authorized `just seed-canary NCBITaxon:1035765`, inspect the entire emitted YAML, repeat focused schema/strict validation and run `just verify-corpus` plus `just qc`. These are future curation checks, not regeneration performed here.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The entire YAML remained byte-identical on reread. This timestamped report is the sole repository write for this review. No inventories, YAML, previous reports, history/status, generated pages, worktrees or GitHub items were changed. Strict-output and primary-PDF artifacts are temporary.
