# YAML Record Review: Pseudoalteromonas sp. 11-Cc-C1-9

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_11_cc_c1_9.yaml`
- Started UTC: 2026-10-07T10:00:55Z
- Finished UTC: 2026-10-07T10:03:06Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035764`, Pseudoalteromonas sp. 11-Cc-C1-9, `SPECIES`, `BACTERIA`, parent `NCBITaxon:194690` (unclassified Pseudoalteromonas), ten root-first ancestors, genetic code 11, `EXACT`, `SEEDED` and `strain_count: 0`. There is one NCBI name attestation and one seed event.

No synonyms, nomenclature, mappings, deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graph are asserted. The strain-like label denotes a species-rank NCBI concept, not a culture deposit or formal binomial. Generated YAML is read-only. Future source/harmonization fixes belong to maintained extraction inputs and `src/taxonmech/seed.py`; scope/slug changes belong to `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudoalteromonas_sp_11_cc_c1_9.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudoalteromonas_sp_11_cc_c1_9.yaml --out /private/tmp/pseudo11CcC19-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/pseudo11CcC19-strict.tsv` | Actual TSV inspected; header only. |
| Structured backbone, full lineage, seven inventories, scope/path and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target rows. |
| Live NCBI EFetch and Datasets | Identity, rank, parent, code and full ancestry agree. |
| Exact-taxid Assembly/nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete marker metadata read. |
| Related primary paper | Previously inspected primary text/figure reused for attribution; new target-specific search of all 14 pages performed. |
| Entire target reread | Byte-identical to initial read. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. These bounded source comparisons are not substitutes for full-corpus gates.

`just validate-products` was not run because no curator-added graph nodes are present and the configured OAK targets exclude NCBI taxonomy. No YAML literature/internal evidence references require separate citation validation. The embedded seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target history artifact within the bounded scope below.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222168` agrees on ID, label, rank, parent, genetic code, empty synonyms and snapshot 2026-09-13. The complete native row at `data/catalog/ncbi_names-0005.jsonl.gz:31652` confirms the scientific name. Unique path and scope rows are `data/taxa/PATHS.tsv:14668` and `curation/seed_scope.tsv:322434`.

All ancestor IDs, labels, ranks and ordering agree: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Alteromonadales, Pseudoalteromonadaceae, Pseudoalteromonas and unclassified Pseudoalteromonas. Live EFetch confirms all non-root ancestry, species rank, parent 194690, code 11 and no alternate names; Datasets includes root. The inspected lifecycle inventories contain no target retirement, merge or type-material row. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035764&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035764)

The unclassified parent is carried NCBI placement, not an inferred species assignment. `EXACT` refers to the source concept, not nomenclatural validity. Preserve the full designation and pinned lowercase slug; adjacent numbered isolates are not synonyms.

## Evidence

The sole `NCBITAXON` attestation matches ID, label, count 1, unit `NAME` and snapshot note. It counts a source name, not deposits or genomes. Full backbone scanning found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore search returned UID 333974692, `JF502835.1`: a 1,320-nt partial 16S rRNA record, partial at both ends, with strain 11-Cc-C1-9 and explicit `taxon:1035764`. Source qualifiers name host Clathrina clathrus, France, November 2009, collectors/identifiers M. Roue and I. Domart-Coulon, and primers 27F/1492R. Submission was 6 March 2011; creation 30 May and update 3 June 2011. All metadata were read except nucleotide/translation/transcription payloads. They supply no culture-collection, assembly, BioSample, BioProject, DOI or PMID link. [GenBank JF502835.1](https://www.ncbi.nlm.nih.gov/nuccore/JF502835.1)

GenBank lists an unpublished glycerolipid study by Roue, Domart-Coulon, Jovet and Bourguet-Kondracki, plus direct submission. The study title is submission context, not experimental proof for this isolate. Shared collection metadata do not make neighboring marker accessions equivalent.

The related 2014 primary article DOI `10.6119/JMST-013-0718-2` is available in an institutional repository. Its previously inspected complete printed pages 40, 45 and 46 and rendered Figure 8/caption attribute the compound work to 1-Cc-11. For this review, a new case-insensitive search of all 14 pages' extracted text found no JF502835, 11-Cc-C1-9 or 11Cc-C1-9; 1-Cc-11 occurs on PDF pages 5, 10, 11 and 12. Shared genus, host, authorship or submission title does not transfer chemical, ecological or species-identification claims to the target. This is a bounded attribution check, not exhaustive supplementary-material or literature coverage. [Primary paper](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers17-06/010070108.pdf)

The extra initial local hit, `data/catalog/allthebacteria.tsv.xz:546923`, was read fully. It describes Staphylococcus aureus, SAMEA3322977, ERR1035764 and ERZ3253651. The target digits occur in a sequencing-run accession, not taxonomic identity, so the row supplies no target genome association.

The embedded event agrees with the scope reason and NCBI-only source list. `src/taxonmech/seed.py:_seed_timestamp` selects the latest extraction time among raw, ATB and StrainInfo manifests: respectively 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. The 17:54:04Z timestamp is correct without a target ATB link. This read-only review does not append an event or promote status.

iModulonDB is not applicable: the YAML asserts no functional gene, regulator, pathway, stress response or transcriptomic module. A taxonomic marker and another isolate's chemical study do not create a target expression claim.

## Completeness

No consequential gap was found. `strain_count: 0` counts BacDive records classified in this subtree, not every laboratory strain. A partial marker is not a genome, and an informal designation is not a culture deposit. Optional definition, literature and graph fields can remain empty.

Both local search stages included ignored/hidden files and compressed catalogs using `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed at each stage; history filenames were independently traversed.

The initial whole-digit taxid/label/slug search returned four rows: three target rows and the unrelated ATB run. The expanded JF502835 with optional .1 and bare 11-Cc-C1-9 separator/case variants returned only the same three target rows. Every matched row was inspected. No marker-accession hit, matching metadata value or target history filename was found within these bounded roots/terms, including ignored files.

The exact-taxid Assembly search returned zero with a phrase-not-found warning, not proof that no assembly exists under another classification. Web searches used exact label/accession and glycerolipid/designation terms; no additional target-specific publication or deposit/assembly was verified. Exhaustive literature/supplement retrieval, sequence similarity searches and independent phylogenetic reanalysis were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML within the inspected scope. Identity, full lineage, attestation, zero BacDive count and seed event agree. Sparse optional enrichment is not a defect.

## Recommended Edits

None required. Preserve the full label, NCBI placement and `SEEDED` status. Do not infer a formal species, merge similar isolate names, count JF502835.1 as a genome, create a deposit from the designation or transfer neighboring-isolate phenotypes.

Any future exact-strain association should enter through maintained extraction inputs and the tested seeder workflow, not manual edits to generated YAML or pages.

## Follow-up Checks

On a controlled source refresh, repeat exact NCBI identity/lineage and Assembly/nuccore queries and compare updated inventories. Additional associations require the exact designation or a verified deposit/accession chain.

If maintained inputs change, run `just seed`, an authorized `just seed-canary NCBITaxon:1035764`, inspect the entire emitted record, repeat focused schema/strict validation and run `just verify-corpus` plus `just qc`. These are future curation checks, not regeneration performed here.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The full target was reread and remained byte-identical. This timestamped report is the only repository write for this review. Strict-output and primary-PDF artifacts are temporary. No YAML, inventory, old report, status/history, generated page, worktree or GitHub item was changed.
