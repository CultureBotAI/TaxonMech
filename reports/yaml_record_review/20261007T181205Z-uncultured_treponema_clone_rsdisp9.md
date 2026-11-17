# YAML Record Review: uncultured Treponema clone RsDiSp9

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_treponema_clone_rsdisp9.yaml`
- Started UTC: 2026-10-07T18:05:59Z
- Finished UTC: 2026-10-07T18:12:05Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:103610`, label uncultured Treponema clone RsDiSp9, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read. It carries ten ancestors, genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, zero inventoried strains and one NCBI name attestation. A species-rank environmental clone is not a formally named species, cultured isolate or genome assembly.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/uncultured_treponema_clone_rsdisp9.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/uncultured_treponema_clone_rsdisp9.yaml --out /private/tmp/rsd9-strict.tsv`: exit 0; one file, zero error rows; diagnostic file contains only the header.
- Full-row source comparison confirms the identifier, label, rank, parent, code, lineage, source attestation and scope/path entries. No children were found in the pinned backbone. These bounded manual comparisons are not a replacement for corpus reproduction.
- Ignored-inclusive status searches found no target type-material, merged-ID or dropped-ID row.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, render/docs/vendored checks and tests. No target causal graph or standalone history entry was found in the bounded searches, so graph term/label and standalone history validation have no target here. No substitute focused validator was invented.

## Identity and Grounding

Live NCBI Taxonomy EFetch and Datasets agree with the exact clone name, species rank, parent `NCBITaxon:77353` environmental samples and bacterial lineage. EFetch confirms genetic code 11. Datasets includes the root, while EFetch provides the other ancestor labels/ranks. All ten YAML ancestors match the complete pinned chain: root, cellular organisms, Bacteria, Pseudomonadati, Spirochaetota, Spirochaetia, Treponematales, Treponemataceae, Treponema and environmental samples. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103610), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103610).

The complete native name row contains only the scientific name. The record correctly does not invent a synonym, type strain, LPSN name or GTDB species equivalence. `EXACT` describes identity with the NCBI concept, not certainty about a named biological species.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18512` supplies the name, rank, parent, genetic code, empty synonym fields and sole NCBI attestation. `data/catalog/ncbi_names-0000.jsonl.gz:38520` independently preserves the native scientific-name row.
- `data/taxa/PATHS.tsv:14757` pins this slug to the identifier. `curation/seed_scope.tsv:144158` records the 2026-09-13 attested-rule inclusion, with one source.
- Exact-taxonomy NCBI Nucleotide search returned one sequence, UID 7209327. Its complete non-sequence metadata identify `AB032002.1`, a 1,507-base partial 16S rRNA gene, taxon 103610, clone RsDiSp9, an environmental sample and host Reticulitermes speratus. The source note says the PCR clone came from an isolated protist. The direct submission is dated 29 August 1999; the record was created 29 February 2000 and updated 16 December 2008. This corroborates clone identity, not a culture accession or assembled genome. [GenBank](https://www.ncbi.nlm.nih.gov/nuccore/AB032002.1).
- The sequence cites Iida, Ohkuma, Ohtoko and Kudo's 2000 study, `PMID:11053732`, `DOI:10.1111/j.1574-6941.2000.tb00750.x`. PubMed metadata/abstract and the publisher's abstract and methods were inspected. The study examined uncultivated protist-associated spirochetes with micromanipulation, SSU-rDNA amplification and in situ hybridization. Its cohort-level results do not establish that every phenotype or probe result applies to RsDiSp9; the exact clone-to-sequence link comes from GenBank. [PubMed](https://pubmed.ncbi.nlm.nih.gov/11053732/), [primary article](https://academic.oup.com/femsec/article/34/1/17/617207).
- Exact-taxonomy Assembly search returned zero items, with phrase-not-found/no-items warnings. This is the result of that query, not proof that no remotely related genome exists.
- The seed event matches the scope reason and source label. Its timestamp `2026-09-13T17:54:04Z` is the latest of the three source-manifest extraction timestamps, consistent with `src/taxonmech/seed.py:139`. `SEEDED` does not imply human review.

## Completeness

The zero strain count is supported by the empty exact-taxon BacDive inventory and lack of descendants. Exact source-row checks also found no target LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion in the pinned inventories. Optional nomenclature, mapping, strain, genome, trait and graph slots may remain empty. Record-level literature evidence is optional for this seeded record, whose NCBI provenance is explicit.

The gitignore-independent search used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It searched the digit-bounded taxon number and clone spelling, then expanded to AB032002, PMID 11053732 and the DOI suffix. All 45 resulting source rows/objects were read completely, with lossless common-field grouping. Five source manifests were parsed separately and history filenames checked independently. Within those roots, no target culture/genome association, additional curation overlay or standalone history record was found. These are bounded inventory findings, not a universal literature-absence claim.

The clone marker does not justify creating a BacDive strain entry or placing it in `genome_assemblies`. No gene-function, transcriptomic, MIC or mechanism claim is asserted, so iModulonDB is not applicable.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source scope, strain count and lifecycle provenance are supported.

## Recommended Edits

None required. Leave the generated YAML and seed event unchanged. Optional future marker/literature enrichment needs a maintained representation that survives seeding, not a direct YAML edit.

## Follow-up Checks

For any future culture or genome proposal, require an explicit link to RsDiSp9/AB032002.1, with the correct identifier namespace and source provenance. Shared Treponema membership or nearby 16S similarity alone is insufficient. Route source or harmonization fixes through the maintained extractor/seeder inputs, then rerun the documented schema/strict checks and full provenance/corpus gates.

## Additional Notes

- HEAD remained `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. Target bytes were unchanged. Existing worktrees were inspected and left untouched; the other session is closed.
- Numeric counterexamples included BacDive 103610 (Rhodococcus ST031436), CIP 103610 (Lactobacillus amylovorus), DSM 103610 (Glutamicibacter), StrainInfo deposit 103610 (Pseudomonas aeruginosa), E. coli sequence CP103610, unrelated MGBC/MarMAG/Salmonella/Listeria strain labels and genome assembly statistics. The AllTheBacteria matches were E. coli run DRR103610 and Mycobacterium sample SAMN11053732, not this taxon or its cited PMID.
- One row-reader invocation incorrectly treated the search summary as a filename and exited 1 after printing all real rows. The argument list was corrected and the reader rerun successfully; this was an inspection-script error, not a record finding.
- The original publisher page initially exposed its abstract and methods, but later in-page/full-text requests failed. A 2003 follow-up article appeared as a search lead and could not be opened; its similarity claims were not used as identity evidence. No sequence alignment or complete original-study result-table audit was performed.
- Only this new report was written for the target. No generated record, source snapshot, lifecycle/history or GitHub state was changed.
