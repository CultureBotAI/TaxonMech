# YAML Record Review: Burkholderia sp. MRhNF2(5)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf2_5.yaml`
- Started UTC: 2026-10-10T21:10:30Z
- Finished UTC: 2026-10-10T21:13:08Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF2(5), `NCBITaxon:1037634`. It has species rank, bacterial domain, parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf2_5.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf2_5.yaml --out /private/tmp/taxonmech-mrhnf25-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, complete lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They are not full-corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222849` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037634&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037634), and all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037634) lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes the NCBI placeholder, not nomenclatural standing or a deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32485` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15404` uniquely resolves ID/slug; `curation/seed_scope.tsv:323064` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037634[Organism:exp]` returned one UID, 345019063. Complete [GenBank annotation JF779812.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779812.1) explicitly joins organism, strain MRhNF2(5), and taxon 1037634. The 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `39d98777248121fd13c501c47312ce8fbcd3d6b4108ff5fb2e80692e59514f82`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Freshly read [HAL metadata and complete abstract](https://hal.science/hal-02916138v1) confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate cohort compares mineral-amended and control forest plots; cohort-level results do not establish MRhNF2(5)-specific assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All eleven non-target native AllTheBacteria rows were read completely. All have dataset r0.2, available FASTA, passing assembly/Sylph/HQ filters, and true prior HQ membership. The first ten rows below have scientific name/current and prior Sylph E. coli. Row 1716885 instead has Pseudomonas aeruginosa in all three fields. Complete SeqKit, filter, and download fields were inspected. These are run-accession substring matches, not target attestations, synonyms, deposits, or genomes.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992582 | SAMEA9849694 | ERR10376342 | ERZ25463363 |
| 992583 | SAMEA9849695 | ERR10376344 | ERZ25463367 |
| 992584 | SAMEA9849696 | ERR10376348 | ERZ25463373 |
| 992585 | SAMEA9849697 | ERR10376346 | ERZ25463379 |
| 992586 | SAMEA9849698 | ERR10376340 | ERZ25463385 |
| 992755 | SAMEA9849958 | ERR10376343 | ERZ25464708 |
| 992756 | SAMEA9849959 | ERR10376341 | ERZ25464716 |
| 992757 | SAMEA9849960 | ERR10376345 | ERZ25464724 |
| 992758 | SAMEA9849961 | ERR10376347 | ERZ25464732 |
| 992759 | SAMEA9849962 | ERR10376349 | ERZ25464740 |
| 1716885 | SAMN13164795 | SRR10376341 | ERZ25668576 |

The ERR/SRR prefix difference is significant. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779812, the DOI, and S003807171100280X. Both returned the same 14 lines: own backbone, scope, scientific name, and eleven unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism/16S web search returned NCBI taxonomy tree leads; the dedicated primary taxon page was independently inspected, and snippets were not treated as new evidence.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support recorded taxonomy/name claims. Unchecked full text and isolate-specific assays constrain enrichment research without contradicting those claims.

## Recommended Edits

None required. Preserve MRhNF2(5)/JF779812.1 identity and non-fertilized ectomycorrhizosphere context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Inspect the primary article and isolate-level table before adding MRhNF2(5)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Taxonomy responses, browser text, marker annotation, native rows, and requested HAL metadata/abstract were inspected for this target. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `396dc98da037635f2df95c565a3eb2119252df2bff817f863a653367474a10e6`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged by this review.
