# YAML Record Review: Burkholderia sp. MRhNF3(22)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf3_22.yaml`
- Started UTC: 2026-10-10T21:44:24Z
- Finished UTC: 2026-10-10T21:46:50Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF3(22), `NCBITaxon:1037642`. It carries species rank, bacterial domain, parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf3_22.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf3_22.yaml --out /private/tmp/taxonmech-mrhnf322-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured checks passed for identity, full lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording; these are not full-corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222857` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1 (no rank); cellular organisms 131567 (cellular root); Bacteria 2 (domain); Pseudomonadati 3379134 (kingdom); Pseudomonadota 1224 (phylum); Betaproteobacteria 28216 (class); Burkholderiales 80840 (order); Burkholderiaceae 119060 (family); Burkholderia 32008 (genus); unclassified Burkholderia 2613784 (no rank).

Complete live [EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037642&retmode=xml), [Datasets taxonomy JSON](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037642), and all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037642) lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes this NCBI placeholder, not nomenclatural standing or a culture deposit. EFetch and browser responses succeeded after server-error retries.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32493` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15412` uniquely resolves ID/slug; `curation/seed_scope.tsv:323072` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037642[Organism:exp]` returned one UID, 345019072. Complete [GenBank annotation JF779821.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779821.1) explicitly joins organism, strain MRhNF3(22), and taxon 1037642. This marker has 326 bases, not the 450 found for neighboring isolates. Its 16S rRNA feature is partial at both ends and its source is annotated as non-fertilized ectomycorrhizosphere from a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `f2a6d776b494b6732b4286b19a2d8bd49460ed10c160d5b2f35f66cb97c7d55b`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), freshly read earlier this turn for MRhNF3(14)'s shared study, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate cohort compares mineral-amended and control forest plots. Cohort results do not establish MRhNF3(22)-specific assays; no weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All ten non-target native AllTheBacteria matches were read completely. They match run-accession substrings, not target taxon identifiers. All have dataset r0.2, scientific name Escherichia coli, available FASTA, passing assembly/Sylph/HQ filters, and true prior HQ membership. Nine have current/prior Sylph E. coli. Row 992781 instead has current/prior Sylph Salmonella enterica despite its scientific-name field E. coli; that source-level distinction was preserved without transferring either classification to this target. Complete SeqKit and download fields were inspected.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992779 | SAMEA9849982 | ERR10376421 | ERZ25464903 |
| 992780 | SAMEA9849983 | ERR10376423 | ERZ25464912 |
| 992781 | SAMEA9849984 | ERR10376425 | ERZ25464919 |
| 992782 | SAMEA9849986 | ERR10376427 | ERZ25464928 |
| 992783 | SAMEA9849987 | ERR10376429 | ERZ25464936 |
| 992818 | SAMEA9850029 | ERR10376420 | ERZ25465228 |
| 992819 | SAMEA9850030 | ERR10376422 | ERZ25465233 |
| 992820 | SAMEA9850032 | ERR10376424 | ERZ25465238 |
| 992821 | SAMEA9850033 | ERR10376426 | ERZ25465247 |
| 992822 | SAMEA9850035 | ERR10376428 | ERZ25465252 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779821, the DOI, and S003807171100280X. Both returned the same 13 lines: own backbone, scope, scientific name, and ten unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism/16S web search returned NCBI taxonomy tree leads; snippets were not treated as evidence, and the dedicated primary page was independently inspected.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and successfully retrieved live sources support recorded taxonomy/name claims. Unchecked full text and isolate-specific assays constrain enrichment research without contradicting those claims. Resolved retrieval errors are not record defects.

## Recommended Edits

None required. Preserve MRhNF3(22)/JF779821.1 identity, the 326-base marker length, and non-fertilized ectomycorrhizosphere context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Inspect the primary article and isolate-level table before adding MRhNF3(22)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Initial EFetch and browser requests returned HTTP 400 and HTTP 500 respectively. The inspected EFetch error body reports an NCBI internal `CEFetchPApplication::proxy_stream()` server error. Retries succeeded: complete EFetch TaxaSet XML and all browser text were inspected. Datasets returned HTTP 200 on both requests. No identity check remains unavailable from these retrieval errors.

Marker annotation and native rows were inspected for this target; shared HAL metadata/abstract were read earlier this turn. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, contact, or full-text reading occurred.

YAML SHA-256: `14852ac6ca282c1ff6aa1415b54d165efdf70492c1ae5a6cefa09e564ba3937b`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged by this review.
