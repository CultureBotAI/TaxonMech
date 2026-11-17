# YAML Record Review: Pseudoalteromonas sp. 11-Cc-C1-1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_11_cc_c1_1.yaml`
- Started UTC: 2026-10-07T09:52:41Z
- Finished UTC: 2026-10-07T09:55:09Z
- Verdict: pass

## Target

Read the full generated `TaxonRecord`: `NCBITaxon:1035762`, Pseudoalteromonas sp. 11-Cc-C1-1, `SPECIES`, `BACTERIA`, parent `NCBITaxon:194690` (unclassified Pseudoalteromonas), ten root-first ancestors, code 11, `EXACT`, `SEEDED` and `strain_count: 0`. One NCBI name attestation and one seed event are present.

No synonyms, nomenclature, mappings, deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graph are asserted. The strain-like label denotes a species-rank NCBI concept, not a formal binomial or culture-collection deposit. Generated YAML remains read-only. Future source/harmonization changes belong to maintained extraction inputs and `src/taxonmech/seed.py`; scope/slug decisions belong to `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudoalteromonas_sp_11_cc_c1_1.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudoalteromonas_sp_11_cc_c1_1.yaml --out /private/tmp/pseudo11CcC11-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/pseudo11CcC11-strict.tsv` | Actual TSV inspected; header only. |
| Structured backbone, complete lineage, seven inventories, scope/path and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target rows. |
| Live NCBI EFetch and Datasets | Identity, rank, code, parent and ancestry agree. |
| Exact-taxid Assembly/nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata read. |
| Related primary paper | Relevant complete pages and rendered Figure 8 checked; attribution remains with another isolate. |
| Full target reread | Byte-identical to initial read. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded source checks do not prove corpus reproduction.

`just validate-products` was not run because this record has no curator-added graph nodes, and the configured OAK targets exclude NCBI taxonomy. No YAML literature/internal evidence references require separate citation validation. The embedded seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target history artifact within the bounded scope below.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222166` agrees on ID, label, rank, parent, genetic code, empty synonyms and snapshot 2026-09-13. The complete native row at `data/catalog/ncbi_names-0005.jsonl.gz:31650` confirms the scientific name. Unique path/scope rows are `data/taxa/PATHS.tsv:14666` and `curation/seed_scope.tsv:322432`.

The full chain agrees in ancestor IDs, labels, ranks and ordering: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Alteromonadales, Pseudoalteromonadaceae, Pseudoalteromonas and unclassified Pseudoalteromonas. EFetch independently confirms all non-root ancestors, rank species, parent 194690, code 11 and no alternate names; Datasets includes root. No target lifecycle replacement or type-material row was found in the inspected inventories. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035762&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035762)

The unclassified parent is carried NCBI placement, not a species assignment to infer. Preserve all parts of the label: 11-Cc-C1-1 is not 11-Cc-C1-10 or 1-Cc-11. `EXACT` describes NCBI grounding, not nomenclatural validity.

## Evidence

The sole `NCBITAXON` attestation matches ID, label, count 1, unit `NAME` and snapshot note. It counts a name, not isolates, deposits or genomes. The complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore search returned UID 333974697, `JF502840.1`: an 858-nt partial 16S rRNA record, partial at both ends, with strain 11-Cc-C1-1 and explicit `taxon:1035762`. Source qualifiers name host Clathrina clathrus, France, November 2009, collectors/identifiers M. Roue and I. Domart-Coulon, and primers 27F/1492R. Submission was 6 March 2011; creation 30 May and update 3 June 2011. All metadata were read except nucleotide/translation/transcription payloads. They supply no culture-collection, assembly, BioSample, BioProject, DOI or PMID link. [GenBank JF502840.1](https://www.ncbi.nlm.nih.gov/nuccore/JF502840.1)

The unpublished GenBank reference by Roue, Domart-Coulon, Jovet and Bourguet-Kondracki concerns glycerolipids from C. clathrus and associated Pseudoalteromonas. The reference title is submission context, not direct experimental evidence for this isolate. Its collection date and primer pair must not be copied from neighboring submissions with different metadata.

The related 2014 primary article DOI `10.6119/JMST-013-0718-2` was inspected from the authors' institutional repository. Complete printed pages 40, 45 and 46 were read, and rendered Figure 8 and its caption were checked. Those methods/results identify 1-Cc-11, a November 2007 isolate, for the compound work. A case-insensitive search of all 14 pages' extracted text found no JF502840, 11-Cc-C1-1 or 11Cc-C1-1; 1-Cc-11 occurs on PDF pages 5, 10, 11 and 12. Shared host, genus, authors or reference title does not transfer chemistry, species affiliation or ecological interpretation to this target. The search is bounded to the article text, not all supplementary material or literature. [Primary paper](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers17-06/010070108.pdf)

The only extra initial local hit, `data/catalog/allthebacteria.tsv.xz:547454`, was read fully. It describes Staphylococcus aureus, SAMEA3339738, ERR1035762 and ERZ3254316. The digits occur in a sequencing-run accession, not a taxonomy field. The row cannot supply a target genome association.

The embedded event agrees with the scope reason and NCBI-only source list. `src/taxonmech/seed.py:_seed_timestamp` chooses the latest extraction time among raw, ATB and StrainInfo manifests: 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z respectively. The resulting 17:54:04Z seed timestamp is correct without a target ATB association. No status promotion or new event is warranted for a read-only review.

iModulonDB is not applicable: no regulator, functional gene, pathway, stress-response or transcriptomic claim is asserted. Taxonomic 16S metadata and neighboring-isolate chemistry do not create an expression-module question.

## Completeness

No consequential gap was found. `strain_count: 0` counts BacDive records in this source subtree, not every laboratory strain. A partial marker is not a genome, and an informal designation is not a deposit. Optional literature, definitions and causal graphs are not required for seeded records.

Both local search stages included ignored/hidden files and compressed catalogs with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed at each stage, and history filenames independently traversed.

The first whole-digit taxid/label/slug search returned four rows: three target rows and the unrelated ATB run. The expanded JF502840 with optional .1 and bare 11-Cc-C1-1 separator/case variants returned only the same three target rows. Every match was inspected. No marker-accession hit, matching metadata value or target history filename was found in these bounded roots/terms, including ignored files.

The exact-taxid Assembly search returned zero with a phrase-not-found warning, not proof against assemblies under another classification. Web searches used exact label/accession and glycerolipid/designation terms; no additional target-specific publication or deposit/assembly was verified. Exhaustive literature and supplement retrieval, sequence similarity searches and independent phylogenetic analysis were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML within the inspected scope. Identity, full lineage, attestation, strain count and seed history agree. Sparse optional enrichment is not a defect.

## Recommended Edits

None required. Preserve the full label, NCBI placement and `SEEDED` status. Do not infer a formal species, merge similar designations, count JF502840.1 as a genome, create a deposit from the label or transfer neighboring-isolate phenotypes.

Any future exact-strain association must enter through maintained extraction inputs and the tested seeder workflow, not a manual edit to generated YAML or pages.

## Follow-up Checks

On a controlled source refresh, repeat exact NCBI identity/lineage and Assembly/nuccore queries and compare updated inventories. Additional associations need this exact designation or a verified deposit/accession chain.

If maintained inputs change, run `just seed`, an authorized `just seed-canary NCBITaxon:1035762`, inspect the whole emitted file, repeat focused schema/strict checks and run `just verify-corpus` plus `just qc`. These are future curation checks, not regeneration performed here.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The entire target was reread and remained byte-identical. This timestamped report is the only repository write for this review. Validation/PDF artifacts are temporary. No YAML, source inventory, old report, status/history, generated page, worktree or GitHub item was changed.
