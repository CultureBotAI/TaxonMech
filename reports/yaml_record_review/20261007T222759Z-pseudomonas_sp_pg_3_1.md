# YAML Record Review: Pseudomonas sp. PG-3-1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_pg_3_1.yaml`
- Started UTC: 2026-10-07T22:23:55Z
- Finished UTC: 2026-10-07T22:27:59Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1036156`, Pseudomonas sp. PG-3-1, rank `SPECIES`, domain `BACTERIA`. The entire target YAML was read independently. It has ten ancestors, genetic code 11, exact grounding, seeded status, one NCBI name attestation and `strain_count: 0`. It asserts no synonyms, nomenclature, mappings, strains, evidence objects, graph, discussion or dataset.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/pseudomonas_sp_pg_3_1.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/pseudomonas_sp_pg_3_1.yaml --out /private/tmp/ppg31-strict.tsv`: exit 0, one file, zero errors. The diagnostic TSV was read and contains only its header.
- Structured comparisons passed for backbone identity, ten ancestors, attestation, unique path and scope reason. Exact pinned type-material, merged-ID and dropped-ID searches returned no target rows; the backbone has no target descendants.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. Bounded comparisons do not reproduce the corpus. No graph is asserted and the bounded search found no standalone target history record, so specialized graph/history checks had no target.

## Identity and Grounding

Live Taxonomy EFetch agrees on ID, label, species rank, bacterial division, genetic code 11 and parent `NCBITaxon:196821`, unclassified Pseudomonas. Datasets confirms all ten ancestor IDs including root. Labels and ranks agree through cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae, Pseudomonas and the unclassified parent. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036156), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036156).

PG-3-1 is a source strain designation, not an identified registered culture deposit. Exact grounding identifies this NCBI node; species rank does not establish a formally published species name. Mycoplasmoides PG31 and longer labels containing PG31 are not supported aliases of this target.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:222284` matches all seeded identity fields, empty synonyms, sole source and 2026-09-13 snapshot. Its complete native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31802`.
- `data/taxa/PATHS.tsv:14787` uniquely maps the ID and slug; `curation/seed_scope.tsv:322538` matches the date and one-source reason.
- Exact-taxonomy Nucleotide search returned [JF820098.1](https://www.ncbi.nlm.nih.gov/nuccore/JF820098.1), a 1,429-base partial 16S rRNA sequence explicitly naming PG-3-1/taxon 1036156. Complete non-sequence metadata describe soil from Puguang gas field, China. Submission was 14 April 2011 by Zhang, Li, Yang, Wang and Yuan at China Agricultural University; creation and update were 7 June 2011. No culture deposit, BioSample, BioProject, assembly or protein accession appears in those metadata. The marker is not a genome.
- The accession's unpublished survey title and authors match the 2012 publication represented by PMID 22452226. Previously fetched primary citation/full-abstract XML was reread. This is bibliographic inference, not an explicit PMID link in GenBank. The abstract discusses Pseudomonas but does not name PG-3-1-specific results. [Primary survey abstract](https://pubmed.ncbi.nlm.nih.gov/22452226/).
- A secondary-review lead prompted inspection of the primary citation/full abstract for PMID 27324653, DOI `10.1007/s00248-016-0799-4`. That study reports butane/butanol interactions in a seven-strain consortium. Its abstract does not identify PG-3-1, and the available publisher preview does not supply strain-specific methods or results. This is an enrichment lead, not sufficient evidence here for a PG-3-1 phenotype, gene or quantitative performance claim. [Primary coculture study](https://pubmed.ncbi.nlm.nih.gov/27324653/).
- Exact-taxonomy Assembly search returned zero with phrase-not-found/no-items warnings; this does not establish genome absence under all identifiers.
- The attestation counts one NCBI `NAME`, not a culture or genome. Seed event, inventory and scope reason agree. Timestamp `2026-09-13T17:54:04Z` matches the latest extracted-at value among the raw, ATB and StrainInfo manifests, selected by `src/taxonmech/seed.py:139`.

## Completeness

The exact BacDive comparison and lack of classified descendants support the inventory-specific zero strain count, not a claim that this organism was never cultured. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits comparisons returned no target rows. Optional slots are appropriately empty for this seeded identity record.

Resolution searched ignored files in `data/taxa`, `reports`, `curation` and `history`. Identity, synonym and strain fields in the two Mycoplasmoides YAML candidates establish different taxon IDs; these were collision checks, not complete record reviews. The source search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, covering digit-bounded 1036156, PG-3-1 label/slug variants and JF820098. All 31 addresses were retained without truncation and all 27 JSON objects and four TSV rows were read completely. Five SOURCE.json files were parsed separately and history filenames checked independently.

Three candidates describe the target; 28 describe other organisms, projects or a coincidentally matching genome length. No supported additional target culture/genome link, curation overlay or standalone history record was found in these bounded roots. No required representation was demonstrated missing. iModulonDB was not applicable to the record: it asserts no gene, regulator, functional, transcriptomic or dataset claim. A gene mentioned in a candidate paper is not automatically a target gene.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source count and seeded provenance are supported. The YAML contains no unsupported phenotype or genome assertion.

## Recommended Edits

None required. Preserve the generated YAML and seed event. Optional sequence enrichment belongs in maintained source/extractor inputs or a durable curator representation. Phenotype and isolation-context curation should follow ownership rules in `docs/CURATION.md`, with direct strain-specific evidence. Do not join by bare strain designation or numeric coincidence.

## Follow-up Checks

Before adding a phenotype, inspect the primary survey and coculture study's full methods, strain tables and individual results with an explicit link to PG-3-1/JF820098.1. Separate consortium results from individual-strain measurements and establish which strain was used for any gene-expression experiment. Require direct source identity evidence before attaching a culture or genome. Regenerate future maintained-input changes through the documented pipeline and run focused schema/strict plus corpus/provenance gates.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the target YAML was byte-identical before report creation. Existing branches and worktrees were preserved.
- Ten candidates concern Mycoplasmoides gallisepticum or its ATCC 19610 strain, taxon IDs 2096 and 1267002. Complete BacDive 8604 and StrainInfo 37031 objects explicitly identify that separate organism and its deposits. Its PG31 genome is GCA/GCF_051052275.1, SAMN39617680 and BV-BRC 2096.490.
- Four candidates concern Serratia liquefaciens IPG31, taxon 614, GCA/GCF_028620915.1, SAMN32818142 and BV-BRC 614.163. Two concern Advenella incenata RIT-PG3_1, taxon 267800, GCA/GCF_054902015.1 and SAMN54913028.
- Eight GOLD rows describe Panicum virgatum FPG labels (Go0538922, Go0538930-32 and their projects), and three describe soil metagenome projects/analysis (Gp0574438, Gp0639856, Ga0547145). Their names do not identify the target. Reading source catalog rows did not modify or review Eukaryota YAMLs.
- GCA_965371795.1 is an uncultured archaeon, taxon 115547; the matching number 1036156 is its genome length, not its taxon ID.
- The first combined read of the two unrelated Mycoplasmoides YAMLs was truncated; a subsequent focused read established species identity and the PG31-bearing strain. No complete-read claim or verdict is made for those YAMLs. All target and source-candidate reads used for this verdict were complete.
- The 2016 publisher full-text route was inaccessible; a public ResearchGate publisher preview was inspected, not a full paper. No access restrictions were bypassed or authors contacted. The primary survey's full strain tables also remain uninspected. Search snippets and secondary-review assertions were not used as target claim evidence.
- Only this new report was written; no YAML, source inventory, history/lifecycle or GitHub state changed. Eukaryota remained untouched.
