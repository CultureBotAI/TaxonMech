# YAML Record Review: Pseudoalteromonas sp. 11-Cc-C5-2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_11_cc_c5_2.yaml`
- Started UTC: 2026-10-07T10:10:37Z
- Finished UTC: 2026-10-07T10:13:47Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord`: `NCBITaxon:1035766`, Pseudoalteromonas sp. 11-Cc-C5-2, `SPECIES`, `BACTERIA`, parent `NCBITaxon:194690`, ten root-first lineage entries, code 11, `EXACT`, `SEEDED`, `strain_count: 0`, one NCBI attestation and one seed event.

The record asserts no synonyms, nomenclature, taxonomy mappings, strains/deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graph. The informal designation identifies a species-rank NCBI concept, not a formal binomial or registered culture deposit. Future source/harmonization fixes belong to maintained extraction inputs and `src/taxonmech/seed.py`; scope and slug ownership is `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudoalteromonas_sp_11_cc_c5_2.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudoalteromonas_sp_11_cc_c5_2.yaml --out /private/tmp/pseudo11CcC52-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/pseudo11CcC52-strict.tsv` | Actual TSV inspected; header only. |
| Full backbone/lineage, seven inventory, path/scope and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target rows. |
| Live NCBI EFetch and Datasets | Identity, parent, rank, code and complete ancestry agree. |
| Exact-taxid Assembly/nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete marker metadata read. |
| Related primary paper | Previously inspected primary pages/Figure 8 reused; new target-specific search of all 14 pages' text completed. |
| Complete target reread | Byte-identical to initial read. |

Not checked: full-corpus `just verify-corpus`, `just qc`, schema-all, tests, provenance hashing, generated-page drift, documentation statistics or vendored gates. Focused source comparisons are not substitutes for those checks.

`just validate-products` was not run: no curator-added graph nodes are asserted and OAK excludes NCBI taxonomy. There are no YAML literature/internal evidence references needing citation validation. The embedded seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target artifact in the bounded history scope below.

## Identity and Grounding

The full source row at `data/raw/ncbitaxon_taxa.tsv:222170` agrees on identifier, label, species rank, parent, genetic code, empty synonyms and snapshot 2026-09-13. The complete native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31654`. Unique path and scope rows are `data/taxa/PATHS.tsv:14670` and `curation/seed_scope.tsv:322436`.

All ancestor IDs, labels, ranks and ordering agree: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Alteromonadales, Pseudoalteromonadaceae, Pseudoalteromonas and unclassified Pseudoalteromonas. Live EFetch confirms the full non-root chain, rank, code, parent 194690 and no alternate names; Datasets includes root. Inspected lifecycle inventories contain no target retirement, merge or type-material row. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035766&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035766)

`EXACT` means the identifier denotes the source concept, not a validly published species name. The unclassified parent is carried NCBI placement; no alternative formal species should be inferred. The full isolate designation and pinned slug distinguish this record from neighboring numbered isolates.

## Evidence

The sole `NCBITAXON` attestation matches the identifier, label, count 1, unit `NAME` and snapshot. The count is a source-name count, not a deposit or genome count. Full backbone scanning found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore search returned UID 333974695, `JF502838.1`: 1,326 nt of partial 16S rRNA, partial at both ends, with strain 11-Cc-C5-2 and explicit `taxon:1035766`. The source lists host Clathrina clathrus, France, November 2009, collectors/identifiers M. Roue and I. Domart-Coulon, and primers 27F/1492R. Submission was 6 March 2011, creation 30 May and update 3 June 2011. Complete metadata, excluding nucleotide/translation/transcription payloads, contain no culture-collection, assembly, BioSample, BioProject, DOI or PMID link. [GenBank JF502838.1](https://www.ncbi.nlm.nih.gov/nuccore/JF502838.1)

The GenBank references are direct submission and an unpublished glycerolipid study by Roue, Domart-Coulon, Jovet and Bourguet-Kondracki. A shared submission title is not experimental chemical evidence for every associated isolate.

The related primary article DOI `10.6119/JMST-013-0718-2` was already inspected in this review session: title page, complete printed pages 40, 45 and 46, and the rendered Figure 8/caption. Those methods and results attribute the pure-culture chemistry to 1-Cc-11. A new search for this target across all 14 pages' extracted text found no JF502838, 11-Cc-C5-2 or 11Cc-C5-2; 1-Cc-11 occurs on PDF pages 5, 10, 11 and 12. Shared genus, host and authorship do not transfer those results or a formal-species identification. This is a bounded attribution check, not exhaustive supplementary-material or literature coverage. [Primary paper](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers17-06/010070108.pdf)

The extra initial catalog hit was read fully at `data/catalog/allthebacteria.tsv.xz:546926`: Staphylococcus aureus, SAMEA3322980, ERR1035766 and ERZ3253656. The taxid digits occur in a run accession, not a taxonomy field; this does not establish a target genome link.

The seed event matches the scope reason and NCBI-only attestation. Inspected `src/taxonmech/seed.py:_seed_timestamp` uses the latest manifest extraction time among raw, ATB and StrainInfo: 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z respectively. The event's 17:54:04Z time is therefore consistent without a target ATB association. This review does not change status or append history.

iModulonDB is not applicable: the YAML asserts no gene, regulator, functional pathway, stress response or transcriptomic module. Neither a taxonomic marker nor another isolate's chemistry supplies target expression evidence.

## Completeness

No consequential gap was found. `strain_count: 0` counts BacDive records in the taxonomic subtree, not every named laboratory isolate. A partial 16S accession is not a genome, and a bare isolate designation is not a culture deposit. Optional literature, definition and graph slots may remain empty.

Both search stages used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored/hidden files and compressed catalogs. All five excluded `SOURCE.json` files were separately parsed at each stage, and history filenames were independently traversed.

The initial whole-digit taxid and label/slug search returned four rows: three target rows and the unrelated ATB run. Expanded JF502838 with optional .1 and bare 11-Cc-C5-2 case/separator searches returned only the three target rows. All matches were inspected. No marker-accession hit, matching metadata value or target history filename was found within these bounded roots/terms, including ignored files. An ignored-independent report-filename search found no existing review for this stem before creation.

The exact-taxid Assembly query returned zero with a phrase-not-found warning; this does not exclude assemblies classified elsewhere. Exact label/accession and designation/glycerolipid web searches supplied no additional verified target-specific publication, deposit or assembly. Exhaustive literature/supplement retrieval, sequence similarity and independent phylogenetic analysis were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, attestation, zero BacDive count and seed event agree. Sparse optional enrichment is not itself a defect.

## Recommended Edits

None required. Preserve the full label, unclassified NCBI placement and `SEEDED` status. Do not merge similar designations, infer a formal species, count JF502838.1 as a genome, mint a deposit from the strain name or transfer chemistry from 1-Cc-11.

Future exact-strain associations belong in maintained extraction inputs and the tested seeder, not hand-edited generated YAML or pages.

## Follow-up Checks

On a controlled source refresh, repeat exact NCBI identity/lineage and Assembly/nuccore queries and compare inventories. Further associations need the exact designation or an explicit verified deposit/accession chain.

If maintained inputs change, run `just seed`, an authorized `just seed-canary NCBITaxon:1035766`, read the full emitted YAML, repeat focused schema/strict validation and run `just verify-corpus` plus `just qc`. These are future curation checks, not regeneration performed here.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The entire target remained byte-identical on reread. This new timestamped report is the only repository write for this review. No YAML, inventories, previous reports, history/status, generated pages, worktrees or GitHub items were changed. Strict output and primary-PDF artifacts are temporary.
