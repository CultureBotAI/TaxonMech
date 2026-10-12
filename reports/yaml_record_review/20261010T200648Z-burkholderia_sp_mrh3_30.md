# YAML Record Review: Burkholderia sp. MRh3(30)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrh3_30.yaml`
- Started UTC: 2026-10-10T20:04:42Z
- Finished UTC: 2026-10-10T20:06:48Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord`, Burkholderia sp. MRh3(30), `NCBITaxon:1037620`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrh3_30.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrh3_30.yaml --out /private/tmp/taxonmech-mrh330-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured checks passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They do not prove full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222835` agrees on ID, label, rank, parent, code, and snapshot 2026-09-13. Exact/related/broad synonym and retirement fields are empty. Each root-first lineage label/rank matches its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037620&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037620), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037620) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding identifies this NCBI placeholder, not formal nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32471` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15390` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323050` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The single attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037620[Organism:exp]` returned one UID, 345019035. Complete [GenBank annotation JF779784.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779784.1) explicitly joins organism, strain MRh3(30), and taxon 1037620. This 450-base 16S rRNA marker is partial at both ends and annotated from fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `a56f8d6113e0b549a74156d6e736000d0cf7ee90008ecef407083ea4e5fc34b8`. It is not a genome assembly or deposit accession. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1), inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Cohort-level findings do not establish individual MRh3(30) assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 12 non-target native search matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7619` describes Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0054, GCA_010376205.1, PRJNA560345, SAMN12576329, and JAAGIA000000000.1. Its assembly name ASM1037620v1 supplies the match.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:45977` describes Acinetobacter baumannii, taxid 470, strain AB8/isolate 10MC200000567, GCA_050822065.1, SAMN41037620, PRJNA514245, and DBJBBA000000000.1. Its match is within BioSample; PMID 30286803 is not a target citation. Both GenBank rows are excluded from RefSeq as part of a large multi-isolate project.
- Ten AllTheBacteria rows match run-accession substrings and have scientific name E. coli, r0.2 dataset, available FASTA, and passing assembly filters. Nine have E. coli Sylph labels and passing Sylph/HQ filters. Row 992441 instead has unknown current/prior Sylph species and SYLPH_RESULTS_FAIL in both Sylph and HQ fields. Its available FASTA is preserved, not treated as missing; none of these statuses supplies a target link.

Complete dataset, filter, SeqKit, and download fields were inspected for all ten AllTheBacteria rows:

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992438 | SAMEA9849519 | ERR10376200 | ERZ25462398 |
| 992439 | SAMEA9849520 | ERR10376202 | ERZ25462403 |
| 992440 | SAMEA9849522 | ERR10376206 | ERZ25462414 |
| 992441 | SAMEA9849523 | ERR10376204 | ERZ25462418 |
| 992442 | SAMEA9849524 | ERR10376208 | ERZ25462427 |
| 992533 | SAMEA9849641 | ERR10376201 | ERZ25463018 |
| 992535 | SAMEA9849644 | ERR10376203 | ERZ25463036 |
| 992536 | SAMEA9849646 | ERR10376205 | ERZ25463049 |
| 992537 | SAMEA9849647 | ERR10376207 | ERZ25463055 |
| 992538 | SAMEA9849648 | ERR10376209 | ERZ25463061 |

None of the 12 unrelated rows establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779784, the study DOI, and S003807171100280X. Both returned 15 lines: own backbone, scope, scientific name, and 12 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. A combined exact organism/accession web query returned no results; that limited search is not evidence of biological absence.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRh3(30)/JF779784 identity and its fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRh3(30)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, and native candidate rows were inspected for this target. The shared study's requested HAL metadata/abstract were read earlier this turn. Earlier attempts for this study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `aa684e5f57144f71123f55a3364d250eaca6d0f0ea444c24de2592a6e901dc36`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
