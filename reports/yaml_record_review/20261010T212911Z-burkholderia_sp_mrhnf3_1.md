# YAML Record Review: Burkholderia sp. MRhNF3(1)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf3_1.yaml`
- Started UTC: 2026-10-10T21:26:48Z
- Finished UTC: 2026-10-10T21:29:11Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF3(1), `NCBITaxon:1037638`. It has species rank, bacterial domain, parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf3_1.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf3_1.yaml --out /private/tmp/taxonmech-mrhnf31-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, complete lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They are not full-corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222853` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037638&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037638), and all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037638) lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes this NCBI placeholder, not nomenclatural standing or a deposit. Successful EFetch/browser responses were obtained after server-error retries.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32489` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15408` uniquely resolves ID/slug; `curation/seed_scope.tsv:323068` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037638[Organism:exp]` returned one UID, 345019069. Complete [GenBank annotation JF779818.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779818.1) explicitly joins organism, strain MRhNF3(1), and taxon 1037638. The 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `3079b036e906e35b6a6df49e6c7214fe7373d53cb6269e2879f0b099109f05d0`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), freshly read earlier this turn for MRhNF2(9)'s shared study, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate cohort compares mineral-amended and control forest plots; cohort-level results do not establish MRhNF3(1)-specific assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 14 non-target native matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7628`: Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0009, GCA_010376385.1, PRJNA560345, SAMN12576321, JAAGHS000000000.1. Assembly name ASM1037638v1 supplies the match.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:20406`: Salmonella enterica subsp. enterica serovar Montevideo, taxid 115981/species 28901, strain 1037638, GCA_015872805.1, PRJNA248792, SAMN16972256, AAXRPW000000000.1. Its numeric strain designation is not a target identity bridge. Both assemblies are excluded from RefSeq as part of a large multi-isolate project.
- Twelve AllTheBacteria rows have dataset r0.2, available FASTA, passing assembly/Sylph/HQ filters, and true prior HQ membership. The first ten rows below have scientific name/current and prior Sylph E. coli and match run-accession substrings. Row 2455715 has scientific name Enterococcus faecium and current/prior Sylph Enterococcus_B lactis. Row 2518589 has scientific name Mycobacterium tuberculosis variant bovis and current/prior Sylph Mycobacterium tuberculosis. These last two match SeqKit checksum substrings, not taxon IDs. Source-specific names were preserved without treating them as Burkholderia evidence. Complete SeqKit, filter, and download fields were inspected.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992594 | SAMEA9849706 | ERR10376380 | ERZ25576349 |
| 992595 | SAMEA9849707 | ERR10376384 | ERZ25576355 |
| 992596 | SAMEA9849708 | ERR10376382 | ERZ25576367 |
| 992767 | SAMEA9849970 | ERR10376383 | ERZ25464802 |
| 992768 | SAMEA9849971 | ERR10376381 | ERZ25464809 |
| 992769 | SAMEA9849972 | ERR10376385 | ERZ25464819 |
| 992770 | SAMEA9849973 | ERR10376387 | ERZ25464826 |
| 992771 | SAMEA9849974 | ERR10376389 | ERZ25464834 |
| 992809 | SAMEA9850017 | ERR10376386 | ERZ25465161 |
| 992810 | SAMEA9850018 | ERR10376388 | ERZ25465168 |
| 2455715 | SAMN31439984 | SRR22031646 | ERZ26236229 |
| 2518589 | SAMN32818926 | SRR23174354 | ERZ26264030 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779818, the DOI, and S003807171100280X. Both returned the same 17 lines: own backbone, scope, scientific name, and 14 unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism/16S web search returned NCBI taxonomy tree leads; the dedicated primary taxon page was independently inspected, and snippets were not treated as new evidence.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and successfully retrieved live sources support recorded taxonomy/name claims. Unchecked full text and isolate-specific assays constrain enrichment research without contradicting those claims. Resolved API/browser retrieval failures are not record defects.

## Recommended Edits

None required. Preserve MRhNF3(1)/JF779818.1 identity and non-fertilized ectomycorrhizosphere context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Inspect the primary article and isolate-level table before adding MRhNF3(1)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Initial EFetch and browser requests returned HTTP 400 and HTTP 500 respectively. The inspected EFetch error body reports an NCBI internal `CEFetchPApplication::proxy_stream()` server error. Retries succeeded: complete EFetch TaxaSet XML and all browser text were inspected. Datasets returned HTTP 200. No identity check remains unavailable from these retrieval errors.

Marker annotation and native rows were inspected for this target; shared HAL metadata/abstract were read earlier this turn. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `44624af22b76e3bde0ec987174d153ef0c285653b23ac6f91af4c9994975e66c`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged by this review.
