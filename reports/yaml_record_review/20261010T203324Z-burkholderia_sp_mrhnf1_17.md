# YAML Record Review: Burkholderia sp. MRhNF1(17)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf1_17.yaml`
- Started UTC: 2026-10-10T20:30:24Z
- Finished UTC: 2026-10-10T20:33:24Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF1(17), `NCBITaxon:1037626`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf1_17.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf1_17.yaml --out /private/tmp/taxonmech-mrhnf117-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They do not prove full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222841` agrees on ID, label, rank, parent, code, and snapshot 2026-09-13. Exact/related/broad synonym and retirement fields are empty. Every root-first lineage label/rank agrees with its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037626&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037626), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037626) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding identifies this NCBI placeholder, not formal nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32477` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15396` uniquely resolves ID/slug; `curation/seed_scope.tsv:323056` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The single attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037626[Organism:exp]` returned one UID, 345019065. Complete [GenBank annotation JF779814.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779814.1) explicitly joins organism, strain MRhNF1(17), and taxon 1037626. This 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `7be3fd7f173e70603c01056998cc989bd76ff24db60c17605d7aa6ff4923a816`. It is not a genome assembly or deposit accession. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Requested [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), inspected earlier this turn for the shared study, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Cohort-level findings do not establish individual MRhNF1(17) assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 15 non-target native matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7622` describes Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0040, GCA_010376265.1, PRJNA560345, SAMN12576327, and JAAGHY000000000.1. Its assembly name ASM1037626v1 supplies the match.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:20454` describes Salmonella enterica subsp. enterica serovar Agona, taxid 58095/species 28901, strain 1037626, GCA_015873765.1, PRJNA248792, SAMN16972230, and AAXRQJ000000000.1. Its bare numeric strain designation is not a target identity bridge. Both rows are excluded from RefSeq as part of a large multi-isolate project.
- `data/catalog/ncbi_genbank-0034.jsonl.gz:10459` and `data/catalog/gtdb_genomes-0016.jsonl.gz:36646` describe Streptomyces sp., taxid 1931, metagenomic isolate SMAG_U7264, GCA_036569285.1, PRJNA983538, SAMN37955078, and DATCQX000000000.1. Their 10376268-base total/ungapped length supplies the match. GenBank reports failed MAG annotation completeness and metagenomic origin as RefSeq exclusion reasons; PMID 37951952 is not a target citation. GTDB makes GB_GCA_036569285.1 representative of Streptomyces sp036569285 and places it in Streptomycetales, while its NCBI lineage uses Kitasatosporales. Those unrelated source classifications remain distinct.
- Eleven AllTheBacteria rows match ten E. coli run-accession substrings and a Staphylococcus hominis SeqKit hash. All are r0.2 with available FASTA, passing assembly filters, and true prior HQ membership. The ten E. coli rows have matching scientific/current/prior Sylph labels and passing Sylph/HQ filters. Row 2356443 retains scientific/prior Sylph Staphylococcus hominis but has unknown current Sylph and SYLPH_RESULTS_FAIL in current Sylph/HQ fields. Prior membership was not substituted for current quality.

Complete dataset, filter, SeqKit, and download fields were inspected for all eleven rows:

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992452 | SAMEA9849535 | ERR10376260 | ERZ25462519 |
| 992453 | SAMEA9849536 | ERR10376264 | ERZ25462522 |
| 992454 | SAMEA9849537 | ERR10376262 | ERZ25462526 |
| 992455 | SAMEA9849538 | ERR10376266 | ERZ25462537 |
| 992457 | SAMEA9849541 | ERR10376268 | ERZ25462554 |
| 992548 | SAMEA9849660 | ERR10376265 | ERZ25463145 |
| 992549 | SAMEA9849661 | ERR10376261 | ERZ25463151 |
| 992550 | SAMEA9849662 | ERR10376263 | ERZ25463157 |
| 992551 | SAMEA9849663 | ERR10376267 | ERZ25463163 |
| 992553 | SAMEA9849665 | ERR10376269 | ERZ25463181 |
| 2356443 | SAMN29515238 | SRR19995433 | ERZ26600149 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779814, the study DOI, and S003807171100280X. Both returned 18 lines: own backbone, scope, scientific name, and 15 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. A combined exact organism/16S web query returned no results; that limited query does not establish biological absence.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRhNF1(17)/JF779814 identity and its non-fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRhNF1(17)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, and native candidate rows were inspected for this target. The shared study's requested HAL metadata/abstract were read earlier this turn. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `05bd49c9850ad4ff3ff83c11dab0c51d468d1405243f4f0070ab2496629ae3c3`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
