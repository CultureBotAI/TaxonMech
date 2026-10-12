# YAML Record Review: uncultured Treponema clone HsDiSp320

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_treponema_clone_hsdisp320.yaml`
- Started UTC: 2026-10-07T22:44:06Z
- Finished UTC: 2026-10-07T22:49:40Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:103616`, uncultured Treponema clone HsDiSp320, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read independently. It has ten ancestors, genetic code 11, exact grounding, seeded status, one NCBI name attestation and `strain_count: 0`. It asserts no synonyms, nomenclature, mappings, strains, evidence objects, graph, discussion or dataset.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/uncultured_treponema_clone_hsdisp320.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/uncultured_treponema_clone_hsdisp320.yaml --out /private/tmp/ths320-strict.tsv`: exit 0, one file, zero errors. The diagnostic TSV was read and contains only its header.
- Structured comparisons passed for backbone identity, all ten ancestors, sole attestation, unique path and scope reason. Exact pinned type-material, merged-ID and dropped-ID searches returned no target rows; the backbone has no target children.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. These bounded comparisons do not reproduce the corpus. No graph is asserted and the bounded search found no standalone target history record, so specialized graph/history checks had no target.

## Identity and Grounding

Live Taxonomy EFetch agrees on ID, label, species rank, genetic code 11 and parent `NCBITaxon:77353`, environmental samples. Datasets confirms all ten ancestor IDs including root. The chain continues through cellular organisms, Bacteria, Pseudomonadati, Spirochaetota, Spirochaetia, Treponematales, Treponemataceae and Treponema. EFetch's division is Environmental samples; the Bacteria ancestor establishes the domain. The carried parent label does not imply a cultured strain or formal species description. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103616), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103616).

Exact grounding identifies this NCBI node. HsDiSp320 is a sequence clone designation, not a demonstrated registered culture deposit. Grouping it with HsPySp4 in a published phylotype does not establish clone-identifier equivalence. Numeric matches to BacDive 103616, CIP 103616 and other identifiers do not denote this NCBI taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18518` matches all seeded identity fields, empty synonyms, sole source and 2026-09-13 snapshot. Its complete native scientific-name object is `data/catalog/ncbi_names-0000.jsonl.gz:38526`.
- `data/taxa/PATHS.tsv:14791` uniquely maps the ID and slug; `curation/seed_scope.tsv:144164` matches the date and one-source reason.
- Exact-taxonomy Nucleotide search returned [AB032008.1](https://www.ncbi.nlm.nih.gov/nuccore/AB032008.1), a 1,504-base partial 16S rRNA sequence explicitly identifying clone HsDiSp320 and taxon 103616. Complete non-sequence metadata identify an environmental sample from an isolated protist of the termite Hodotermopsis sjoestedti. The source has a clone qualifier, not a strain qualifier. No deposit, BioSample, BioProject, assembly or protein accession appears in those metadata. Submission was 29 August 1999 by Iida, Ohkuma and Kudo at RIKEN; creation was 29 February 2000 and update 16 December 2008. This marker is not a genome.
- GenBank explicitly cites PMID 11053732. Primary PubMed citation and full abstract confirm Iida, Ohkuma, Ohtoko and Kudo's 2000 paper and DOI `10.1111/j.1574-6941.2000.tb00750.x`. The abstract describes culture-independent analysis of protist fractions and cluster-specific hybridization; it does not report HsDiSp320-specific functional measurements. The original full-text and PDF routes failed during this review. No unseen table or probe result is treated as inspected evidence. [Primary study abstract](https://pubmed.ncbi.nlm.nih.gov/11053732/).
- The inspected 2003 follow-up's methods, results and discussion place HsDiSp320 and HsPySp4 in cluster I and describe them as representatives of a common phylotype from Dinenympha/Pyrsonympha in H. sjoestedti. Cluster I includes both attached and free-swimming populations. The study's phylotype-specific NkS probes concern other clones from N. koshunensis; they do not establish an HsDiSp320-specific assay result. Shared phylotype and cluster-level observations do not justify merging clone records or asserting metabolism, culture availability or an individually measured attachment phenotype. [Noda et al., 2003](https://journals.asm.org/doi/10.1128/AEM.69.1.625-633.2003).
- Exact-taxonomy Assembly search returned zero with phrase-not-found/no-items warnings. This is a bounded query, not proof that no genome exists under any identifier.
- The attestation counts one NCBI `NAME`, not a culture or genome. Seed event, inventory and scope reason agree. Timestamp `2026-09-13T17:54:04Z` matches the latest extracted-at value among the raw, ATB and StrainInfo manifests selected by `src/taxonmech/seed.py:139`.

## Completeness

Exact BacDive comparison and the lack of classified descendants support the inventory-specific zero strain count, not a biological claim of absolute uncultivability. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits comparisons returned no target rows. Optional slots are appropriately empty for this seeded identity record.

Resolution included ignored files in `data/taxa`, `reports`, `curation` and `history`, resolving one target. The source search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, covering digit-bounded 103616, HsDiSp320 label/slug variants and AB032008. All 40 candidate addresses were retained without truncation and all 28 JSON objects and 12 TSV rows were read completely. Five SOURCE.json files were parsed separately and history filenames checked independently.

Three candidates describe the target. The remaining 37 are numeric collisions in other culture/deposit identifiers, strain or isolate names, sequence/run accessions, assembly statistics or a checksum. No supported additional target culture/genome link, curation overlay or standalone history record was found in these bounded roots. No required representation was demonstrated missing. iModulonDB is not applicable: no gene, regulator, functional, transcriptomic or dataset claim is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found against the current YAML. Identity, lineage, source count and seeded provenance are supported. The YAML contains no unsupported phenotype, culture or genome assertion. Potential literature enrichment is optional and is not a missing required representation.

## Recommended Edits

None required. Preserve the generated YAML and seed event. Any future sequence or deposit enrichment belongs in maintained source/extractor inputs or a durable curator representation following `docs/CURATION.md`; identity and harmonization changes belong upstream or in `src/taxonmech/seed.py`, not in this generated record. Do not join by bare numbers or treat shared phylotype membership as clone synonymy.

## Follow-up Checks

Before adding protist-association or individual functional claims, inspect the original paper's methods, clone table and probe specificity, explicitly linking the asserted result to HsDiSp320/AB032008.1. Resolve any culture deposit independently through its own primary provenance. Regenerate future maintained-input changes through the documented pipeline and run focused schema/strict plus corpus/provenance gates.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the target YAML was byte-identical before report creation. Existing branches and worktrees were preserved.
- BacDive 103616 is Rhodococcus ST017752(HKI)/BI 11593, source taxon 194249, not NCBI taxon 103616. CIP 103616/VPI 9940 belongs to Lactobacillus gasseri, taxon 1596, BacDive 135315, StrainInfo SI-ID 69024/SI-DP 152087 and GOLD Go0238866.
- Other complete collision objects include Bacillus velezensis SRCM103616, uncultured Duncaniella MGBC103616, uncultured bacterium MarMAG_103616, Salmonella designations and Klebsiella accession CP103616. Rhizobium, Aerophototrophica and Pseudomonas matches concern numerical assembly statistics. StrainInfo SI-DP 103616 concerns Flavobacterium ATCC 25012; KY103616 concerns a separate fungal sequence. These source objects were disambiguated only, without reviewing another YAML or changing Eukaryota coverage.
- SOURCE.json's numeric match is a BacDive API batch request for BacDive 103616, not target evidence. The primary follow-up was read at the ASM publisher; PMC returned a browser check. The original OUP article and indexed PDF returned fetch errors. Search snippets and earlier review reports were used only as leads.
- No sequence alignment, culture-availability assessment, taxonomic reassignment or outreach was performed. Only this new report was written; no YAML, source inventory, history/lifecycle or GitHub state changed. Eukaryota remained untouched.

