# YAML Record Review: Pseudoalteromonas sp. 11-Cc-C1-10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_11_cc_c1_10.yaml`
- Started UTC: 2026-10-07T09:56:28Z
- Finished UTC: 2026-10-07T09:58:36Z
- Verdict: pass

## Target

Read the full generated `TaxonRecord`: `NCBITaxon:1035763`, Pseudoalteromonas sp. 11-Cc-C1-10, `SPECIES`, `BACTERIA`, parent `NCBITaxon:194690` (unclassified Pseudoalteromonas), ten root-first ancestors, code 11, `EXACT`, `SEEDED` and `strain_count: 0`. One NCBI name attestation and one seed event are present.

No synonyms, nomenclature, taxonomy mappings, deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graph are asserted. This strain-like scientific label identifies a species-rank NCBI concept, not a registered deposit or formal binomial. Generated YAML remains read-only. Maintained extraction inputs and `src/taxonmech/seed.py` own future harmonization fixes; `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` own scope and slug decisions.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudoalteromonas_sp_11_cc_c1_10.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudoalteromonas_sp_11_cc_c1_10.yaml --out /private/tmp/pseudo11CcC110-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/pseudo11CcC110-strict.tsv` | Actual TSV inspected; header only. |
| Structured backbone, full lineage, seven inventories, scope/path and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target rows. |
| Live NCBI EFetch and Datasets | Identity, rank, parent, code and ancestry agree. |
| Exact-taxid Assembly/nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete marker metadata read. |
| Related primary paper | Relevant complete pages and rendered Figure 8 checked; target-specific extracted-text search negative. |
| Entire target reread | Byte-identical to initial read. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. These bounded source checks do not prove full-corpus reproduction.

`just validate-products` was not run because no curator-added graph nodes are present and configured OAK targets exclude NCBI taxonomy. No YAML literature/internal evidence references require separate citation checking. The embedded seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target history artifact in the scope below.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222167` agrees on ID, label, rank, parent, code, empty synonyms and snapshot 2026-09-13. The complete native row at `data/catalog/ncbi_names-0005.jsonl.gz:31651` confirms the scientific name. Unique path and scope rows are `data/taxa/PATHS.tsv:14667` and `curation/seed_scope.tsv:322433`.

All ancestor IDs, labels, ranks and ordering agree: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Alteromonadales, Pseudoalteromonadaceae, Pseudoalteromonas and unclassified Pseudoalteromonas. EFetch confirms all non-root ancestry, species rank, parent 194690, genetic code 11 and no alternate names; Datasets includes root. No target retirement, merged or type-material entry was found in the inspected inventories. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035763&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035763)

The unclassified parent is carried NCBI placement. It does not authorize an inferred species assignment. Preserve the terminal 10 and the full designation; 11-Cc-C1-1 and 1-Cc-11 are different names. `EXACT` means NCBI concept agreement, not nomenclatural validity.

## Evidence

The sole `NCBITAXON` attestation matches identifier, label, count 1, unit `NAME` and snapshot note. The unit counts a source name, not deposits, isolates or genomes. Complete backbone scanning found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore search returned UID 333974696, `JF502839.1`: a 906-nt partial 16S rRNA record, partial at both ends, with strain 11-Cc-C1-10 and explicit `taxon:1035763`. Source qualifiers give host Clathrina clathrus, France, November 2009, collectors/identifiers M. Roue and I. Domart-Coulon, and primers 27F/1492R. Submission was 6 March 2011; creation 30 May and update 3 June 2011. All metadata were read except nucleotide/translation/transcription payloads. No culture-collection, assembly, BioSample, BioProject, DOI or PMID link is supplied in these metadata. [GenBank JF502839.1](https://www.ncbi.nlm.nih.gov/nuccore/JF502839.1)

The unpublished GenBank reference by Roue, Domart-Coulon, Jovet and Bourguet-Kondracki concerns glycerolipids from C. clathrus and associated Pseudoalteromonas. Its title is submission context, not proof that this isolate produces the metabolites. The marker is distinct from neighboring isolate accessions even when collection metadata overlap.

The related 2014 primary article DOI `10.6119/JMST-013-0718-2` was inspected from the authors' institutional repository. Complete printed pages 40, 45 and 46 were read; rendered Figure 8 and its caption were checked. The compound work explicitly names strain 1-Cc-11, not 11-Cc-C1-10. A case-insensitive search of all 14 pages' extracted text found no JF502839, 11-Cc-C1-10 or 11Cc-C1-10, while finding 1-Cc-11 on PDF pages 5, 10, 11 and 12. Shared genus, host, authorship or submission title cannot transfer the chemistry, ecological interpretation or species affiliation. This is a bounded attribution check, not an exhaustive literature or supplement review. [Primary paper](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers17-06/010070108.pdf)

The extra initial local hit, `data/catalog/allthebacteria.tsv.xz:546921`, was read in full. It describes Staphylococcus aureus, SAMEA3322975, ERR1035763 and ERZ3253645. The target's digits occur in a sequencing-run accession, not taxonomic identity, so no association is warranted.

The embedded event matches the scope reason and NCBI-only source list. `src/taxonmech/seed.py:_seed_timestamp` chooses the newest extraction time across raw, ATB and StrainInfo manifests. Their times on 2026-09-13 are 17:50:44Z, 17:54:04Z and 17:29:00Z, respectively; the 17:54:04Z seed event is correct without a target ATB link. This review does not promote status or append an event.

iModulonDB is not applicable: no gene-regulatory, pathway, stress-response or transcriptomic claim is asserted. A taxonomic marker and a neighboring isolate's chemical study do not create an expression-module assertion.

## Completeness

No consequential gap was found. `strain_count: 0` measures BacDive source records classified in this subtree, not every laboratory strain. The marker is not a genome and the informal designation is not a culture deposit. Optional definition, literature and graph fields may remain empty.

Both local search stages included ignored/hidden files and compressed catalogs using `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed at each stage; history filenames were independently traversed.

The initial whole-digit taxid/label/slug search returned four rows: three target rows and the unrelated ATB run. The expanded JF502839 with optional .1 and bare 11-Cc-C1-10 separator/case variants returned only the same three target rows. Every matched row was read. No marker-accession hit, matching metadata value or target history filename was found within those roots/terms, including ignored files.

Exact-taxid Assembly search returned zero with a phrase-not-found warning, not proof of no assembly under other classifications. Web searches used exact label/accession and glycerolipid/designation terms. No additional target-specific experimental publication or deposit/assembly was verified. Exhaustive literature/supplement retrieval, sequence similarity searches and independent phylogenetic reanalysis were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML within the inspected scope. Identity, full lineage, attestation, zero BacDive count and seed history agree. Sparse optional enrichment is not a defect.

## Recommended Edits

None required. Retain the exact label, NCBI placement and `SEEDED` status. Do not merge similar isolate labels, infer a formal species, count JF502839.1 as a genome, create a deposit from the designation or transfer neighboring-isolate phenotypes.

Future exact-strain evidence should enter through maintained source extraction inputs and the tested seeder workflow, not manual edits to generated YAML or pages.

## Follow-up Checks

On a controlled source refresh, repeat exact NCBI identity/lineage and Assembly/nuccore queries and compare inventories. Accept new associations only with the exact designation or a verified deposit/accession chain.

If maintained inputs change, run `just seed`, an authorized `just seed-canary NCBITaxon:1035763`, inspect the whole emitted record, repeat focused schema/strict validation and run `just verify-corpus` plus `just qc`. These are future curation checks, not regeneration performed here.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The full target was reread and remained byte-identical. This timestamped report is the only repository write for this review; strict-output and PDF artifacts are temporary. No YAML, inventory, old report, status/history, generated page, worktree or GitHub item was changed.
