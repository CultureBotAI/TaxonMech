# YAML Record Review: Burkholderia sp. MRhNF2(7)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf2_7.yaml`
- Started UTC: 2026-10-10T21:13:59Z
- Finished UTC: 2026-10-10T21:16:09Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF2(7), `NCBITaxon:1037635`. It has species rank, bacterial domain, parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf2_7.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf2_7.yaml --out /private/tmp/taxonmech-mrhnf27-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, complete lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They are not full-corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222850` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037635&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037635), and all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037635) lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes the NCBI placeholder, not nomenclatural standing or a deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32486` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15405` uniquely resolves ID/slug; `curation/seed_scope.tsv:323065` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037635[Organism:exp]` returned one UID, 345019067. Complete [GenBank annotation JF779816.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779816.1) explicitly joins organism, strain MRhNF2(7), and taxon 1037635. The 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `a5ab92eb99c8797775cc7bfe204d533c3ca6d7780ef423137301de6c4bd68c3a`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; partial-marker identity alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), freshly read earlier this turn for MRhNF2(5)'s shared study, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate cohort compares mineral-amended and control forest plots; cohort-level results do not establish MRhNF2(7)-specific assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 18 non-target native matches were read completely:

- Klebsiella pneumoniae P63, taxid 573, appears at `data/bvbrc/bvbrc-0024.jsonl.gz:28622`, `data/catalog/gtdb_genomes-0015.jsonl.gz:48264`, `data/catalog/ncbi_genbank-0009.jsonl.gz:40287`, and `data/catalog/ncbi_refseq-0002.jsonl.gz:42596`. These describe BV-BRC 573.30923, GCA_011037635.1/GCF_011037635.1, SAMN10592691, and SBCP00000000.1 (BV-BRC uses the unversioned WGS root). BV-BRC/GenBank give PRJNA510003, while GTDB's NCBI metadata and RefSeq give PRJNA224116. The source-specific project values were preserved. GTDB also records Brazil/blood and 693 contigs, not target collection metadata. The GenBank/RefSeq pair is marked identical; none links to MRhNF2(7).
- Klebsiella pneumoniae isolate 2002220, taxid 573, appears at `data/catalog/ncbi_genbank-0028.jsonl.gz:43570` as current GCA_031037635.3/ABLWLC000000000.3 and at `data/catalog/ncbi_genbank_historical-0001.jsonl.gz:21394` and `:21395` as replaced versions GCA_031037635.1/.2 with corresponding WGS versions .1/.2. All use PRJNA288601 and SAMN34589393 and are excluded from RefSeq as part of a large multi-isolate project. Historical versions are not distinct target genomes.
- `data/catalog/ncbi_genbank-0056.jsonl.gz:27409` describes Sellimonas intestinalis, taxid 1653434, isolate 1909_1909I_C_1, GCA_061037635.1, PRJNA1464738, SAMN60703973, and JCDDIQ000000000.1. It is excluded from RefSeq as derived from metagenome.
- Ten AllTheBacteria rows have scientific name/current and prior Sylph E. coli, dataset r0.2, available FASTA, passing assembly/Sylph/HQ filters, and true prior HQ membership. Complete SeqKit, filter, and download fields were inspected.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992475 | SAMEA9849561 | ERR10376354 | ERZ25462653 |
| 992476 | SAMEA9849563 | ERR10376356 | ERZ25462657 |
| 992477 | SAMEA9849564 | ERR10376358 | ERZ25462661 |
| 992587 | SAMEA9849699 | ERR10376352 | ERZ25463391 |
| 992588 | SAMEA9849700 | ERR10376350 | ERZ25463396 |
| 992614 | SAMEA9849753 | ERR10376355 | ERZ25463587 |
| 992615 | SAMEA9849756 | ERR10376357 | ERZ25463595 |
| 992616 | SAMEA9849760 | ERR10376359 | ERZ25463607 |
| 992760 | SAMEA9849963 | ERR10376351 | ERZ25464748 |
| 992761 | SAMEA9849964 | ERR10376353 | ERZ25464756 |

These assembly/run accession substrings do not establish target attestations, synonyms, deposits, or genomes. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779816, the DOI, and S003807171100280X. Both returned the same 21 lines: own backbone, scope, scientific name, and 18 unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism/16S web search returned NCBI taxonomy tree leads; the dedicated primary taxon page was independently inspected, and snippets were not treated as new evidence.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support recorded taxonomy/name claims. Unchecked full text and isolate-specific assays constrain enrichment research without contradicting those claims.

## Recommended Edits

None required. Preserve MRhNF2(7)/JF779816.1 identity and non-fertilized ectomycorrhizosphere context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Inspect the primary article and isolate-level table before adding MRhNF2(7)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Taxonomy responses, browser text, marker annotation, and native rows were inspected for this target. Shared HAL metadata/abstract were read earlier this turn. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `3c84431e232e70917566ecb48fd76d3341020eaab8336c87741b965cd2f87b87`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged by this review.
