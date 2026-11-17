# YAML Record Review: Burkholderia sp. MRhNF2(8)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf2_8.yaml`
- Started UTC: 2026-10-10T21:17:07Z
- Finished UTC: 2026-10-10T21:20:02Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF2(8), `NCBITaxon:1037636`. It has species rank, bacterial domain, parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf2_8.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf2_8.yaml --out /private/tmp/taxonmech-mrhnf28-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, complete lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They are not full-corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222851` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037636&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037636), and all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037636) lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes the NCBI placeholder, not nomenclatural standing or a deposit. The successful EFetch response was obtained after HTTP 400 failures; see Additional Notes.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32487` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15406` uniquely resolves ID/slug; `curation/seed_scope.tsv:323066` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037636[Organism:exp]` returned one UID, 345019076. Complete [GenBank annotation JF779825.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779825.1) explicitly joins organism, strain MRhNF2(8), and taxon 1037636. The 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `0d3b979bcff1c21f7958af051a6e8eeb050855d17a03b97344855ef6eca9d8ca`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), freshly read earlier this turn for MRhNF2(5)'s shared study, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate cohort compares mineral-amended and control forest plots; cohort-level results do not establish MRhNF2(8)-specific assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 12 non-target native matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7627` describes Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0018, GCA_010376365.1, PRJNA560345, SAMN12576322, and JAAGHT000000000.1. Assembly name ASM1037636v1 supplies the match. It is excluded from RefSeq as part of a large multi-isolate project.
- Eleven AllTheBacteria rows have dataset r0.2, available FASTA, and passing assembly/Sylph filters. The first ten rows below have scientific name/current and prior Sylph E. coli; row 1777103 has Salmonella enterica in all three fields. Row 992481 has HQ filter CHECKM2_MAX_CONTAM,MAX_CONTIG_NUM,MIN_N50 and false prior HQ membership. The other ten have passing HQ filters and true prior HQ membership. Complete SeqKit, filter, and download fields were inspected. Available FASTA was not conflated with passing quality.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992478 | SAMEA9849565 | ERR10376360 | ERZ25462668 |
| 992479 | SAMEA9849566 | ERR10376362 | ERZ25462674 |
| 992480 | SAMEA9849567 | ERR10376364 | ERZ25462681 |
| 992481 | SAMEA9849568 | ERR10376366 | ERZ25462688 |
| 992482 | SAMEA9849570 | ERR10376368 | ERZ25462697 |
| 992617 | SAMEA9849765 | ERR10376363 | ERZ25463615 |
| 992618 | SAMEA9849767 | ERR10376365 | ERZ25576441 |
| 992619 | SAMEA9849768 | ERR10376361 | ERZ25463627 |
| 992620 | SAMEA9849770 | ERR10376367 | ERZ25463630 |
| 992621 | SAMEA9849776 | ERR10376369 | ERZ25576447 |
| 1777103 | SAMN14055998 | SRR11037636 | ERZ25716008 |

These assembly-name/run-accession substrings do not establish target attestations, synonyms, deposits, or genomes. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779825, the DOI, and S003807171100280X. Both returned the same 15 lines: own backbone, scope, scientific name, and 12 unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism/16S web search returned NCBI taxonomy tree leads; the dedicated primary taxon page was independently inspected, and snippets were not treated as new evidence.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and successfully retrieved live sources support recorded taxonomy/name claims. Unchecked full text and isolate-specific assays constrain enrichment research without contradicting those claims. The resolved API retrieval failures are not record defects.

## Recommended Edits

None required. Preserve MRhNF2(8)/JF779825.1 identity and non-fertilized ectomycorrhizosphere context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Inspect the primary article and isolate-level table before adding MRhNF2(8)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Two initial EFetch requests terminated with HTTP 400. A later diagnostic request to the original URL returned HTTP 200 and complete TaxaSet XML, which was fully inspected; Datasets separately returned HTTP 200. A parameter-reordered EFetch request still returned HTTP 400 with an internal `CEFetchPApplication::proxy_stream()` error. No unresolved identity check remains from these retrieval failures.

Browser text, marker annotation, and native rows were inspected for this target. Shared HAL metadata/abstract were read earlier this turn. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `0bfa4751d7b4ba6e387bccffcfe18f7eb9776470d6023aad21dfb1357c331616`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged by this review.
