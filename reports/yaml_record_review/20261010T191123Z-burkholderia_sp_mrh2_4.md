# YAML Record Review: Burkholderia sp. MRh2(4)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrh2_4.yaml`
- Started UTC: 2026-10-10T12:50:31Z
- Finished UTC: 2026-10-10T19:11:23Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for Burkholderia sp. MRh2(4), `NCBITaxon:1037610`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes; generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrh2_4.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrh2_4.yaml --out /private/tmp/taxonmech-mrh24-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured comparisons passed for identity, full lineage labels/ranks, synonyms, code, attestation, index uniqueness, scope reason, and seed-event wording. This is not full corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. These full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222825` agrees on ID, label, rank, parent, code, and the 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Each root-first lineage label/rank matches its individual backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037610&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037610), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037610) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count, not a statement of zero assemblies. Exact grounding preserves this NCBI placeholder identity, not formal nomenclatural standing or a culture-deposit identity.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32461` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15380` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323040` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. Lineage is carried from NCBI, not reconciled with another taxonomy.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping sections match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide search `txid1037610[Organism:exp]` returned one UID, 345019030. Complete [GenBank annotation JF779779.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779779.1) explicitly joins organism, strain MRh2(4), and taxon 1037610. It is a 450-base 16S rRNA fragment incomplete at both ends, annotated from fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `3ddc5caa0ccff77aae37ceb075a74a7feeff0d41f14cc9c3f0dd53396e9f593d`. This is not a genome assembly or deposit identifier. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Freshly inspected complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1) confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The abstract concerns 80 isolates from beech ectomycorrhizosphere and bulk soil under control and calcium-amended conditions. It does not establish individual MRh2(4) assay results. No mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 15 non-target native search matches were read completely:

- `data/bvbrc/bvbrc-0002.jsonl.gz:34133`, `data/catalog/gtdb_genomes-0000.jsonl.gz:46085`, and `data/catalog/ncbi_genbank-0031.jsonl.gz:25640` concern Enterococcus faecium AJ_C_05, taxid 1352, GCA_033802685.1, SAMN38194472, and PRJNA1037610. BV-BRC 1352.17523 retains CP138459/CP138458/CP138460. The match is the BioProject number, not the target taxon. GTDB assigns Enterococcus_B lactis while retaining the NCBI E. faecium name; GenBank excludes this non-target assembly from RefSeq for many frameshifted proteins. Neither distinction supplies evidence about MRh2(4).
- `data/catalog/ncbi_genbank-0014.jsonl.gz:12444` concerns Salmonella enterica subsp. enterica serovar Newport, taxid 108619/species 28901, GCA_015711415.1, SAMN16972270, PRJNA248792, and AAXMEG000000000.1. The matching strain designation is 1037610, not an NCBI taxonomy ID.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:45978` concerns Acinetobacter baumannii, taxid 470, strain AB38/isolate 14MC190004543, GCA_050822085.1, SAMN41037610, PRJNA514245, and DBJBAZ000000000.1. The match is within BioSample; PMID 30286803 is not a target citation.
- Ten AllTheBacteria rows have scientific name Escherichia coli, available FASTA, and passing assembly filter. Nine also have E. coli Sylph assignments and passing Sylph/HQ filters. Row 992691 has unknown Sylph species, `SYLPH_RESULTS_FAIL`, and HQ flags `CHECKM2_MAX_CONTAM,SYLPH_RESULTS_FAIL`. Full dataset, SeqKit, filter, and download fields were inspected. Each numeric match is within a run accession.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992499 | SAMEA9849600 | ERR10376100 | ERZ25462816 |
| 992500 | SAMEA9849601 | ERR10376101 | ERZ25462820 |
| 992501 | SAMEA9849603 | ERR10376103 | ERZ25462828 |
| 992502 | SAMEA9849604 | ERR10376102 | ERZ25462834 |
| 992503 | SAMEA9849605 | ERR10376104 | ERZ25462837 |
| 992504 | SAMEA9849607 | ERR10376105 | ERZ25462844 |
| 992505 | SAMEA9849608 | ERR10376106 | ERZ25462853 |
| 992507 | SAMEA9849611 | ERR10376107 | ERZ25462865 |
| 992638 | SAMEA9849841 | ERR10376108 | ERZ25463770 |
| 992691 | SAMEA9849894 | ERR10376109 | ERZ25464169 |

None establishes another target attestation, synonym, deposit, or genome. Sample, project, run, and assembly identifiers remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779779, the study DOI, and S003807171100280X. Both returned 18 lines: own backbone, scope, scientific name, and 15 unrelated rows described above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact target YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. The first web-search attempt failed to connect; a subsequent combined exact organism/accession query returned no results. This search result is not evidence that literature or other records do not exist. Primary NCBI and HAL source reads succeeded.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the taxonomy/name-only assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve exact MRh2(4)/JF779779 identity and the fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the primary article and isolate-level table and inspect MRh2(4)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, candidate native rows, and requested HAL metadata/abstract were inspected. Earlier attempts for the same study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried for this isolate. No login, payment, or full-text reading occurred.

YAML SHA-256: `67793ed93116774c6690f8b25e03ceb9b6aee1e729a3a133c3ed2d942f8f5b26`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
