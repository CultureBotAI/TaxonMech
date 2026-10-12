# YAML Record Review: Burkholderia sp. MRh3(23)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrh3_23.yaml`
- Started UTC: 2026-10-10T19:48:54Z
- Finished UTC: 2026-10-10T19:50:56Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for Burkholderia sp. MRh3(23), `NCBITaxon:1037616`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrh3_23.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrh3_23.yaml --out /private/tmp/taxonmech-mrh323-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured checks passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They do not prove full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222831` agrees on ID, label, rank, parent, code, and snapshot 2026-09-13. Exact/related/broad synonym and retirement fields are empty. Each root-first lineage label/rank matches its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037616&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037616), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037616) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding identifies this NCBI placeholder, not formal nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32467` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15386` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323046` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The single attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037616[Organism:exp]` returned one UID, 345019029. Complete [GenBank annotation JF779778.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779778.1) explicitly joins organism, strain MRh3(23), and taxon 1037616. This 450-base 16S rRNA marker is partial at both ends and annotated from fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `98fffe1be3a085b981ad16ca2782189ee2a333816de209c7e88bcda800606f9d`. It is not a genome assembly or deposit accession. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1), inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Cohort-level findings do not establish individual MRh3(23) assay results. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 15 non-target native search matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7617` describes Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0064, GCA_010376165.1, PRJNA560345, SAMN12576332, and JAAGID000000000.1. Its assembly name ASM1037616v1 supplies the match.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41465` describes Acinetobacter baumannii, taxid 470, strain AB43/isolate 10RC180006903, GCA_050714315.1, SAMN41037616, PRJNA514245, and DBIYQF000000000.1. Its match is within BioSample; PMID 30286803 is not a target citation. Both GenBank rows are excluded from RefSeq as part of a large multi-isolate project.
- Ten AllTheBacteria rows match run-accession substrings and have E. coli scientific and Sylph labels, r0.2 dataset, available FASTA, and passing assembly/Sylph/HQ filters.
- Three further AllTheBacteria rows match SeqKit checksum substrings, not taxonomy IDs. Row 485854 is Campylobacter jejuni, Sylph Campylobacter_D jejuni, dataset 661k, checksum `seqkit.v0.1_DLS_k0_32bbc22ae1037616aabba62bc2fdb74f`. Row 812688 is Streptococcus pneumoniae in both name fields, r0.2, checksum `seqkit.v0.1_DLS_k0_ce5103761652cc6136f1aabbbd6b24a0`. Row 1740970 is Salmonella enterica subsp. enterica, Sylph Salmonella enterica, r0.2, checksum `seqkit.v0.1_DLS_k0_573210376165ff2e4c3ff53bdd7d0a83`. All three have available FASTA and passing filters. SeqKit sums are not asserted as MD5.

Complete dataset, filter, SeqKit, and download fields were inspected for all 13 AllTheBacteria rows:

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 485854 | SAMEA2246978 | ERR448851 | ERZ3173204 |
| 812688 | SAMEA6500189 | ERR5637072 | ERZ25338634 |
| 992655 | SAMEA9849858 | ERR10376160 | ERZ25576538 |
| 992657 | SAMEA9849860 | ERR10376162 | ERZ25576558 |
| 992658 | SAMEA9849861 | ERR10376164 | ERZ25576567 |
| 992659 | SAMEA9849862 | ERR10376166 | ERZ25576582 |
| 992660 | SAMEA9849863 | ERR10376168 | ERZ25463889 |
| 992708 | SAMEA9849911 | ERR10376161 | ERZ25464314 |
| 992709 | SAMEA9849912 | ERR10376163 | ERZ25464322 |
| 992710 | SAMEA9849913 | ERR10376165 | ERZ25464332 |
| 992712 | SAMEA9849915 | ERR10376169 | ERZ25464349 |
| 992714 | SAMEA9849917 | ERR10376167 | ERZ25464368 |
| 1740970 | SAMN13493549 | SRR10593981 | ERZ25690011 |

None of the 15 unrelated rows establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779778, the study DOI, and S003807171100280X. Both returned 18 lines: own backbone, scope, scientific name, and 15 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. A combined exact organism/accession web query returned no results; that limited search is not evidence of biological absence.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRh3(23)/JF779778 identity and its fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRh3(23)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, and native candidate rows were inspected for this target. The shared study's requested HAL metadata/abstract were read earlier this turn. Earlier attempts for this study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `f5902db84eebfc9c91f8cd892b78ed59e19cb35517e21117358d45346f0706c2`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
