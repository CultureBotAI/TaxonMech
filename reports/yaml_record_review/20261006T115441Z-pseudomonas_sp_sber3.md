# YAML Record Review: Pseudomonas sp. SBER3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_sber3.yaml`
- Started UTC: 2026-10-06T11:50:31Z
- Finished UTC: 2026-10-06T11:54:41Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035108`, Pseudomonas sp. SBER3. It retains SPECIES rank, BACTERIA domain, parent unclassified Pseudomonas (196821), ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME assertion and one inline seed event. It asserts no host, biodegradation phenotype, genome association or causal graph.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_sber3.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_sber3.yaml --out /private/tmp/sber3-validation.tsv`: passed, one file and zero errors. Read the diagnostic TSV; it contains only the header.
- Complete structured comparisons of the backbone, ancestors, synonyms, seven other imported taxon tables, PATHS/scope, attestation and inline seed event passed.
- Exact-ID checks of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Read live NCBI Taxonomy XML/Datasets, exact non-expanded Assembly/Nuccore results, complete marker metadata and the candidate paper's Crossref registration.
- `just validate-products` is inapplicable: no curator-added graph nodes are present. Taxonomy identifiers were checked at their authority; no undocumented focused reference or term validator was invented.
- Ignored-inclusive history content and filename searches found no separate target artifact. The inline event was checked; no validator was run against a nonexistent separate history file.
- Full-corpus reproduction, validation, tests, history, provenance/site checks and `just qc` were not run. Focused validation is not corpus-level certification.

## Identity and Grounding

The backbone row at `data/raw/ncbitaxon_taxa.tsv:221887` agrees with the native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31323`. `data/taxa/PATHS.tsv:14373` resolves the slug, and `curation/seed_scope.tsv:322178` supports the one-source seeding rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035108&retmode=xml) confirms the name, rank, parent and genetic code. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035108) confirms all ten ancestor IDs: 1, 131567, 2, 3379134, 1224, 1236, 72274, 135621, 286 and 196821.

Lineage is correctly carried from NCBI, not reconciled with an alternative classification. EXACT refers to this NCBI concept; SPECIES is the authority rank, not evidence of a validly published species binomial.

## Evidence

The attestation counts one NAME in the 2026-09-13 snapshot, not a culture, genome or experiment. The inline event at 2026-09-13T17:54:04Z agrees with source provenance and scope.

The exact Nuccore search returned [JN001928.1](https://www.ncbi.nlm.nih.gov/nuccore/JN001928.1), a 1,515-base partial 16S rRNA sequence. Read all metadata, references and feature qualifiers. It explicitly identifies Pseudomonas sp. SBER3, strain SBER3 and taxon 1035108. Its source qualifiers record India, collection date 2008-04-22 and Sandeep Bisht as collector and identifier. These are submitter annotations, not independent verification of those collection details.

Pandey, Bisht and Shouche submitted the marker on 2011-04-26. Its other reference is an unpublished plant-microbe/rhizoremediation study, without a DOI or PMID. The marker does not itself establish a host, endophytic lifestyle, PAH degradation or a complete genome.

An external name-collision lead remains unresolved. The inspected [Crossref registration](https://api.crossref.org/works/10.1016/j.ejsobi.2013.10.009) confirms a Bisht, Pandey and colleagues paper in European Journal of Soil Biology 60 (2014), pages 67-76, [DOI:10.1016/j.ejsobi.2013.10.009](https://doi.org/10.1016/j.ejsobi.2013.10.009). Its registered title concerns endophytic Bacillus sp. SBER3 and PAH biodegradation, whereas the inspected NCBI sources call this taxon Pseudomonas. Shared author names and the SBER3 label make this worth checking but do not prove organism identity.

Publisher access returned 403 or an internal error; the full paper, isolate-identification methods and accession statement were not inspected. Search excerpts are leads only. No explicit JN001928 identity bridge was established in the inspected metadata. The paper's organism cannot currently be declared equivalent to, or conclusively distinct from, the reviewed isolate. Do not transfer its habitat or functional claims, and do not change the NCBI lineage based on this unresolved lead.

## Completeness

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the ID, full label, slug, Pseudomonas-associated variants and bounded SBER3 tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.

All 27 initial candidate rows were read completely with lossless common-field factoring: five TSV rows, eleven GOLD rows and eleven other native JSONL rows. The parsed address set reconciles exactly with discovery. Expanded searches for JN001928, sequence UID 333697168 and the candidate paper's DOI found no additional rows in these roots, including ignored and compressed files.

All five SOURCE.json files were discovered without ignore filtering and traversed completely for the initial identity pattern; none matched. History content and filename checks found no separate target artifact.

The backbone has no synonyms or direct children. Seven other imported taxon tables have no exact target row. Zero BacDive strains agrees with the pinned subtree; it does not mean the isolate does not exist. No supported target culture-deposit or genome association was found in the inspected catalogs. The exact Assembly query returned zero items with a phrases-not-found warning, not proof of global genome absence.

Optional phenotype and graph slots may remain empty. iModulonDB is inapplicable to this identity-only YAML, which names no functional gene, regulator or expression module. The marker belongs outside genome counts.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the retained assertions. The unverified Bacillus-paper relationship is a follow-up limitation, not an established error in this NCBI-backed record.

## Recommended Edits

None required. Do not hand-edit the generated YAML, promote its status or append a review history event.

If later primary evidence resolves a classification conflict, route the source correction to NCBI or upstream kg-microbe and refresh the maintained inventory through `src/taxonmech/extract.py` and `src/taxonmech/seed.py`. Any accepted optional association needs source-qualified identity handling and tests, not a bare-strain-label join.

## Follow-up Checks

Before attaching the candidate paper, inspect its full isolate-identification and accession statements and compare them with JN001928.1. Preserve any confirmed classification disagreement explicitly; do not silently choose the convenient genus.

Before adding deposits or genomes, require an explicit source chain for this isolate. Run both focused validators for any accepted change, and corpus reproduction plus full QC before release.

## Additional Notes

Excluded numeric collisions include Staphylococcus haemolyticus 25-57 (SAMEA1035108, paired GCA/GCF_001229885.1, BV-BRC 1283.120, GOLD Gp0140469, ATB ERZ3070572); Bifidobacterium bifidum 2201st1_E8_2201SCRN_220225 (SAMN41035108, paired GCA/GCF_040927685.1, BV-BRC 1681.1556); Mycobacterium tuberculosis ERR1035108 (BV-BRC 1773.20602, ATB ERZ3502015); Campylobacter jejuni 839952 (GCA_010351085.1); and Salmonella SRR11035108 / SAMN14051349 / ATB ERZ25717962. GOLD's SAMN10351080-89 rows describe unrelated community projects. Their numeric overlap is not an identity join.

Only this new report was written in the repository for this individual review. No record, source, page, code, history or older report was changed. Eukaryotic reviews were not reopened.
