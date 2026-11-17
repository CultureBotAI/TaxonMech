# YAML Record Review: Burkholderia sp. BSNF3(7)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsnf3_7.yaml`
- Started UTC: 2026-10-10T08:01:28Z
- Finished UTC: 2026-10-10T08:10:14Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for Burkholderia sp. BSNF3(7), `NCBITaxon:1037607`. It is a species-ranked bacterial placeholder under `NCBITaxon:2613784`, with `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsnf3_7.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsnf3_7.yaml --out /private/tmp/taxonmech-bsnf37-20261010-validation.tsv --workers 1`: one file, zero errors; the inspected TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid history links.
- Structured comparisons passed for identity, full lineage labels/ranks, synonyms, code, source attestation, unique index entry, scope reason, and seed-event wording. These comparisons do not prove full corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222822` agrees on ID, label, species rank, parent, genetic code, and the 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Each root-first lineage label/rank matches its individual backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037607&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037607), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037607) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count; this is not a statement of zero assemblies. The species rank and exact grounding preserve NCBI's placeholder identity, not a claim of formal nomenclatural standing.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32458` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15376` uniquely resolves the ID/slug. `curation/seed_scope.tsv:323037` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. Lineage is carried from NCBI, not reconciled with another taxonomy.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, paper, or assay. Structured scans found no own rows in the pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping sections match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide search `txid1037607[Organism:exp]` returned one UID, 345019055. Complete [GenBank annotation JF779804.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779804.1) explicitly joins the organism, strain BSNF3(7), and taxon 1037607. It describes a 450-base partial 16S rRNA sequence, incomplete at both ends, from non-fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `2e25354f8801ad823eddd48cfea518e865039777d217a96a7bf55bb655c4772f`. This is not a genome assembly or a culture-deposit identifier. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. Freshly inspected complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1) confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The study concerns 80 isolates from beech ectomycorrhizosphere and bulk soil under control and calcium-amended conditions. Its cohort abstract does not establish individual BSNF3(7) assay results. No mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 11 non-target native search matches were read completely:

- `data/catalog/ncbi_genbank-0046.jsonl.gz:45979` describes Acinetobacter baumannii, taxid 470, strain AB34/isolate 14UC170047991, assembly GCA_050822105.1, BioSample SAMN41037607, BioProject PRJNA514245, and WGS DBJBAY000000000.1. The match is a BioSample substring, not the target taxonomy ID. PMID 30286803 is not a target citation.
- Ten AllTheBacteria rows are labeled Escherichia coli in the scientific-name and Sylph fields. They match run-accession substrings, not BSNF3(7). All have available FASTA and passing assembly/Sylph filters. Row 992494 fails HQ filters `CHECKM2_MAX_CONTAM,MAX_CONTIG_NUM`; the other nine have HQ PASS. Complete filter, SeqKit, dataset, and download fields were inspected.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992491 | SAMEA9849582 | ERR10376076 | ERZ25462757 |
| 992492 | SAMEA9849586 | ERR10376077 | ERZ25462763 |
| 992493 | SAMEA9849588 | ERR10376078 | ERZ25462769 |
| 992494 | SAMEA9849589 | ERR10376079 | ERZ25462775 |
| 992627 | SAMEA9849796 | ERR10376070 | ERZ25463687 |
| 992628 | SAMEA9849797 | ERR10376072 | ERZ25463691 |
| 992629 | SAMEA9849804 | ERR10376074 | ERZ25463704 |
| 992680 | SAMEA9849883 | ERR10376071 | ERZ25464067 |
| 992681 | SAMEA9849884 | ERR10376073 | ERZ25464077 |
| 992683 | SAMEA9849886 | ERR10376075 | ERZ25464094 |

None of these rows establishes an additional target attestation, synonym, deposit, or genome. Source sample, project, run, and assembly identifiers remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, and space/punctuation/hyphen variants, bounding the terminal designation number. Expanded search added JF779804, the study DOI, and S003807171100280X. Both searches returned 14 lines: own backbone, scope, scientific name, and the 11 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact target YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism/accession web searches supplied taxonomy-tree leads, not evidence for additional isolate-level claims.

The optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the taxonomy/name-only assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting the record.

## Recommended Edits

None required. Preserve exact BSNF3(7)/JF779804 identity and the explicitly non-fertilized context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the primary article and isolate-level table and inspect BSNF3(7)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, candidate native rows, and the shared study's requested HAL metadata/abstract were inspected. Previous attempts for the same study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried for this isolate. No login, payment, or full-text reading occurred.

YAML SHA-256: `5c877374457113d2ad8828a37b6c0f3887fb7e4236307fea3b2fb76b2ae98120`. This review writes only this new report within the repository. It does not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
