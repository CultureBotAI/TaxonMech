# YAML Record Review: Stenotrophomonas sp. SBSA2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/stenotrophomonas_sp_sbsa2.yaml`
- Started UTC: 2026-10-06T11:56:31Z
- Finished UTC: 2026-10-06T11:58:45Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035109`, Stenotrophomonas sp. SBSA2. It retains SPECIES rank, BACTERIA domain, parent unclassified Stenotrophomonas (196198), ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME assertion and one inline seed event. It asserts no phenotype, host, culture deposit, genome association or causal graph.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/stenotrophomonas_sp_sbsa2.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/stenotrophomonas_sp_sbsa2.yaml --out /private/tmp/sbsa2-validation.tsv`: passed, one file and zero errors. Read the TSV; it contains only the header.
- Structured comparisons of the complete backbone row, ancestors, synonyms, seven other imported taxon tables, PATHS/scope, attestation and inline seed event passed.
- Exact-ID checks of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Read live NCBI Taxonomy XML/Datasets, exact non-expanded Assembly/Nuccore results and complete marker metadata.
- `just validate-products` is inapplicable: no curator-added graph nodes are present. Taxonomy identifiers were checked at their authority; no undocumented focused term/reference validator was invented.
- Ignored-inclusive history content and filename searches found no separate target artifact. Checked the inline event; no validator was run against a nonexistent separate history file.
- Full-corpus reproduction, validation, tests, history, provenance/site checks and `just qc` were not run. These focused checks do not certify the full corpus.

## Identity and Grounding

The backbone row at `data/raw/ncbitaxon_taxa.tsv:221888` agrees with the native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31324`. `data/taxa/PATHS.tsv:14374` resolves the slug, and `curation/seed_scope.tsv:322179` supports the one-source seeding rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035109&retmode=xml) confirms the name, rank, parent and genetic code. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035109) confirms all ten ancestor IDs: 1, 131567, 2, 3379134, 1224, 1236, 135614, 32033, 40323 and 196198.

The Lysobacterales / Lysobacteraceae chain is carried from NCBI, not reconciled with another classification. EXACT refers to this NCBI concept; SPECIES is its authority rank, not a claim that SBSA2 is a validly published binomial.

## Evidence

The attestation counts one NAME in the 2026-09-13 snapshot, not a culture, genome or experiment. The inline event at 2026-09-13T17:54:04Z agrees with source provenance and scope.

The exact Nuccore search returned [JN001927.1](https://www.ncbi.nlm.nih.gov/nuccore/JN001927.1), a 763-base partial 16S rRNA sequence. Read all metadata, references and feature qualifiers. The record explicitly identifies Stenotrophomonas sp. SBSA2, strain SBSA2 and taxon 1035109. Source qualifiers record India, collection date 2008-04-22 and Sandeep Bisht as collector and identifier. These are submitter annotations, not independent confirmation of collection details.

Pandey, Bisht and Shouche submitted the sequence on 2011-04-26. Its other reference is an unpublished plant-microbe/rhizoremediation study with no DOI or PMID. The study title and submitters' institutional address do not establish an isolation substrate, host, habitat or biodegradation phenotype for SBSA2. The partial marker is not a genome.

Bounded web searches for the exact organism, SBSA2 with the submitter names, and JN001927 did not yield an inspectable target-specific experimental publication. Search snippets and taxonomy mirrors were not counted as independent evidence. This is not an exhaustive literature-absence claim.

## Completeness

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the ID, full label, slug, Stenotrophomonas-associated variants and bounded SBSA2 tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.

The 204 initial matches were accounted for individually. Read 29 complete rows with lossless common-field factoring: five TSV, eleven GOLD and thirteen other native JSONL rows. For the remaining 175 GenBank metagenome rows in `data/catalog/ncbi_genbank-0066.jsonl.gz`, inspected every row's organism/taxon identity, assembly accession, sample and matching identifier fields, not every unrelated annotation field. The combined address set reconciles exactly with discovery.

All 175 metagenome rows match only `asm_name`, `isolate` and `ftp_path` through NOWI19-1 names containing SAMN10351090-93. They span 36 other recorded identities; none has target taxon ID 1035109 or a Stenotrophomonas organism name. A broad environmental taxon or shared numeric substring is not an SBSA2 association.

Expanded searches for JN001927 and sequence UID 333697167 found no rows in these roots, including ignored and compressed files. All five SOURCE.json files were separately discovered without ignore filtering and traversed completely for the initial identity pattern; none matched. History content and filenames contained no separate target artifact.

The backbone has no synonyms or direct children. Seven other imported taxon tables have no exact target row. Zero BacDive strains agrees with the pinned subtree; it does not deny the isolate's existence. No supported target deposit or genome association was found within the inspected catalogs. The exact Assembly query returned zero items with a phrases-not-found warning, not proof of global genome absence.

Optional phenotype and graph slots may remain empty. iModulonDB is inapplicable to this identity-only YAML, which names no functional gene, regulator or expression module.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the retained assertions. Optional sequence or phenotype enrichment is not a missing required representation.

## Recommended Edits

None required. Do not hand-edit the generated YAML, promote its status, append a review history event or convert a marker into a genome link.

Any later accepted enrichment belongs in maintained inventory handling and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`, with source-qualified identity tests. Do not join on bare strain labels or numeric substrings.

## Follow-up Checks

Before adding phenotype, host or habitat claims, require an inspected isolate-specific primary source. Before adding culture or genome links, require an explicit source chain for SBSA2. Run both focused validators for an accepted change, and corpus reproduction plus full QC before release.

## Additional Notes

Other excluded numeric collisions include Staphylococcus haemolyticus 2263-3461 (SAMEA1035109, paired GCA/GCF_001239225.1, BV-BRC 1283.199, GOLD Gp0140506, ATB ERZ3070569); Bifidobacterium bifidum RTP21002st1_A4_RTP21002_201210 (SAMN41035109, paired GCA/GCF_040927625.1, BV-BRC 1681.1553); Mycobacterium tuberculosis ERR1035109 (BV-BRC 1773.20606, ATB ERZ3502026); and Salmonella SRR11035109 / SAMN14051342 / ATB ERZ25717922. GOLD's SAMN10351090-99 rows describe unrelated community projects.

The three RefSeq metagenome candidates are Lentibacter algarum GCF_982995875.1 and GCF_983026285.1, and Thermus thermophilus GCF_983023285.1, not SBSA2. An initial scratch diagnostic assumed publication-field collisions and stopped on the first assembly-name match; the corrected full candidate check confirmed all 175 matching-field sets and completed successfully. This was not a schema or record-validation failure.

Only this new report was written in the repository for this individual review. No record, source, code, page, history or older report was changed. Eukaryotic reviews were not reopened.
