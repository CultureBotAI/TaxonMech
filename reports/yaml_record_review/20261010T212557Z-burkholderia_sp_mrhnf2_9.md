# YAML Record Review: Burkholderia sp. MRhNF2(9)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf2_9.yaml`
- Started UTC: 2026-10-10T21:22:38Z
- Finished UTC: 2026-10-10T21:25:57Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF2(9), `NCBITaxon:1037637`. It has species rank, bacterial domain, parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf2_9.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf2_9.yaml --out /private/tmp/taxonmech-mrhnf29-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, complete lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They are not full-corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Unavailable: EFetch taxonomy XML cross-check, HTTP 400 on both attempts. Live Datasets and Taxonomy Browser checks succeeded independently.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222852` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037637) confirms ID, organism name, species rank, and the full lineage ID list including root. Datasets omits assembly count rather than reporting zero. All 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037637) lines were read after a successful retry, confirming name, rank, code 11, and lineage labels. The parent ID is supported by the pinned row and the final Datasets ancestor; individual ancestor ranks were verified against pinned rows, not an unavailable live EFetch response. Exact grounding denotes this NCBI placeholder, not nomenclatural standing or a deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32488` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15407` uniquely resolves ID/slug; `curation/seed_scope.tsv:323067` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037637[Organism:exp]` returned one UID, 345019066. Complete [GenBank annotation JF779815.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779815.1) explicitly joins organism, strain MRhNF2(9), and taxon 1037637. The 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `6a28918a003a2a88e78690ad9032b07fadf7513c9bc856fadc2efc166d8578a0`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Freshly read [HAL metadata and complete abstract](https://hal.science/hal-02916138v1) confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate cohort compares mineral-amended and control forest plots; cohort-level results do not establish MRhNF2(9)-specific assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All ten non-target native AllTheBacteria rows were read completely. All have scientific name/current and prior Sylph E. coli, dataset r0.2, available FASTA, passing assembly/Sylph/HQ filters, and true prior HQ membership. Complete SeqKit, filter, and download fields were inspected. These run-accession substrings do not establish target attestations, synonyms, deposits, or genomes.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992589 | SAMEA9849701 | ERR10376370 | ERZ25463400 |
| 992590 | SAMEA9849702 | ERR10376372 | ERZ25463406 |
| 992591 | SAMEA9849703 | ERR10376376 | ERZ25463410 |
| 992592 | SAMEA9849704 | ERR10376374 | ERZ25576338 |
| 992593 | SAMEA9849705 | ERR10376378 | ERZ25576344 |
| 992762 | SAMEA9849965 | ERR10376371 | ERZ25464764 |
| 992763 | SAMEA9849966 | ERR10376373 | ERZ25464772 |
| 992764 | SAMEA9849967 | ERR10376375 | ERZ25464781 |
| 992765 | SAMEA9849968 | ERR10376379 | ERZ25464789 |
| 992766 | SAMEA9849969 | ERR10376377 | ERZ25464793 |

Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779815, the DOI, and S003807171100280X. Both returned the same 13 lines: own backbone, scope, scientific name, and ten unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism/16S web search returned NCBI taxonomy tree leads; the dedicated primary taxon page was independently inspected, and snippets were not treated as new evidence.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned sources, live Datasets, and the successfully retrieved browser page support recorded taxonomy/name claims. EFetch unavailability and unchecked full text/isolate assays are explicit review limitations, not evidence of a record defect.

## Recommended Edits

None required. Preserve MRhNF2(9)/JF779815.1 identity and non-fertilized ectomycorrhizosphere context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Retry the supplementary EFetch taxonomy XML cross-check after the NCBI service recovers. Inspect the primary article and isolate-level table before adding MRhNF2(9)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

EFetch returned HTTP 400 twice; the inspected second error body reports `CEFetchPApplication::proxy_stream()` and an NCBI internal server error. The first browser attempt returned HTTP 500; its retry succeeded and all text was inspected. Datasets returned HTTP 200. No successful EFetch XML response is claimed.

Marker annotation, native rows, and requested HAL metadata/abstract were inspected for this target. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `4feab4b46daae36e9e1371004b41aceb5f313b9f7bb26604caf36040e1f0b674`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged by this review.
