# YAML Record Review: Burkholderia sp. MRhNF3(14)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf3_14.yaml`
- Started UTC: 2026-10-10T21:37:45Z
- Finished UTC: 2026-10-10T21:40:30Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF3(14), `NCBITaxon:1037640`. It carries species rank, bacterial domain, parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf3_14.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf3_14.yaml --out /private/tmp/taxonmech-mrhnf314-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured checks passed for identity, full lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording; these are not full-corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222855` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1 (no rank); cellular organisms 131567 (cellular root); Bacteria 2 (domain); Pseudomonadati 3379134 (kingdom); Pseudomonadota 1224 (phylum); Betaproteobacteria 28216 (class); Burkholderiales 80840 (order); Burkholderiaceae 119060 (family); Burkholderia 32008 (genus); unclassified Burkholderia 2613784 (no rank).

Complete live [EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037640&retmode=xml), [Datasets taxonomy JSON](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037640), and all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037640) lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes this NCBI placeholder, not nomenclatural standing or a deposit. Browser retrieval succeeded on retry after an initial HTTP 500.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32491` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15410` uniquely resolves ID/slug; `curation/seed_scope.tsv:323070` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037640[Organism:exp]` returned one UID, 345019070. Complete [GenBank annotation JF779819.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779819.1) explicitly joins organism, strain MRhNF3(14), and taxon 1037640. The 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `81e3195062c11ee14c80825c9f746aed87cad6f1503169b6a38351f841220264`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Freshly inspected [HAL metadata and complete abstract](https://hal.science/hal-02916138v1) confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate cohort compares mineral-amended and control forest plots. Cohort results do not establish MRhNF3(14)-specific assays; no weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 11 non-target native matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7629`: Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0003, GCA_010376405.1, PRJNA560345, SAMN12576320, JAAGHR000000000.1. Assembly name ASM1037640v1 supplies the match. RefSeq exclusion cites a large multi-isolate project.
- Ten AllTheBacteria rows match run-accession substrings. All have dataset r0.2, scientific name Escherichia coli, available FASTA, and passing assembly-pipeline filter. Nine have current/prior Sylph E. coli, passing Sylph/HQ filters, and true prior HQ membership. Row 993030 instead has current/prior Sylph unknown, `SYLPH_RESULTS_FAIL` for its Sylph filter, `CHECKM2_MAX_CONTAM,SYLPH_RESULTS_FAIL` for its HQ filter, and false prior HQ membership. Complete SeqKit and download fields were inspected without transferring source-specific quality or identity to this target.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992816 | SAMEA9850027 | ERR10376400 | ERZ25465217 |
| 992975 | SAMEA9850401 | ERR10376401 | ERZ25466356 |
| 992976 | SAMEA9850402 | ERR10376403 | ERZ25466366 |
| 992977 | SAMEA9850403 | ERR10376407 | ERZ25466372 |
| 992978 | SAMEA9850404 | ERR10376405 | ERZ25466381 |
| 992979 | SAMEA9850406 | ERR10376409 | ERZ25466388 |
| 993027 | SAMEA9850609 | ERR10376402 | ERZ25466674 |
| 993029 | SAMEA9850611 | ERR10376406 | ERZ25466682 |
| 993030 | SAMEA9850612 | ERR10376404 | ERZ25466688 |
| 993031 | SAMEA9850613 | ERR10376408 | ERZ25466691 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779819, the DOI, and S003807171100280X. Both returned the same 14 lines: own backbone, scope, scientific name, and 11 unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism/16S web search returned NCBI taxonomy tree leads; snippets were not treated as evidence, and the dedicated primary page was independently inspected.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and successfully retrieved live sources support recorded taxonomy/name claims. Unchecked full text and isolate-specific assays constrain enrichment research without contradicting those claims. The resolved browser error is not a record defect.

## Recommended Edits

None required. Preserve MRhNF3(14)/JF779819.1 identity and non-fertilized ectomycorrhizosphere context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Inspect the primary article and isolate-level table before adding MRhNF3(14)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Datasets and EFetch returned HTTP 200. The browser initially returned HTTP 500; its successful retry was read completely. Marker annotation, native rows, and HAL metadata/abstract were freshly inspected. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, contact, or full-text reading occurred.

YAML SHA-256: `295896a8c953471e2fb6548f76a85e41305fcb851b2362679d7ce7b4aecb0bfd`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged by this review.
