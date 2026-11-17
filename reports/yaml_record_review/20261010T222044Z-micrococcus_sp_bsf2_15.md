# YAML Record Review: Micrococcus sp. BSF2(15)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/micrococcus_sp_bsf2_15.yaml`
- Started UTC: 2026-10-10T22:18:49Z
- Finished UTC: 2026-10-10T22:20:44Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Micrococcus sp. BSF2(15), `NCBITaxon:1037650`. Species rank, bacterial domain, parent `NCBITaxon:2620948`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event are recorded. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/micrococcus_sp_bsf2_15.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/micrococcus_sp_bsf2_15.yaml --out /private/tmp/taxonmech-micrococcusbsf215-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, full lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. These are not corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222865` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1 (no rank); cellular organisms 131567 (cellular root); Bacteria 2 (domain); Bacillati 1783272 (kingdom); Actinomycetota 201174 (phylum); Actinomycetes 1760 (class); Micrococcales 85006 (order); Micrococcaceae 1268 (family); Micrococcus 1269 (genus); unclassified Micrococcus 2620948 (no rank).

Complete live [EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037650&retmode=xml), [Datasets taxonomy JSON](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037650), and all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037650) lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes this NCBI placeholder, not nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32501` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15420` uniquely resolves ID/slug; `curation/seed_scope.tsv:323080` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037650[Organism:exp]` returned one UID, 345019011. Complete [GenBank annotation JF779760.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779760.1) explicitly joins organism, strain BSF2(15), and taxon 1037650. The 450-base 16S rRNA marker is partial at both ends and annotated from fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `ba50e3247a87c5d17056116da95f76430bb274e0c71c864834d9642876937a12`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Freshly inspected [HAL metadata and complete abstract](https://hal.science/hal-02916138v1) confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate study compares mineral-amended and control forest plots. Its cohort results do not establish BSF2(15)-specific weathering, iron-release, chitin-degradation, or plant-growth phenotypes. Full text and isolate-level assay tables were not inspected.

All 13 non-target native matches were read completely:

- `data/catalog/gtdb_genomes-0012.jsonl.gz:26748`: Brevundimonas sp. 1080, taxid/species 3156405, GCF_040545985.1 and recorded GenBank accession GCA_040545985.1, PRJNA224116, SAMN41528323, JBEPMW000000000.1. Contig N50 1037650 supplies the match, not a taxon join. GTDB assigns Brevundimonas sp016429195; representative and type-species-of-genus source flags are false. Those flags are not independent nomenclature conclusions.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:20368`: Salmonella Typhimurium, taxid 90371/species 28901, strain 1037650, GCA_015872025.1, PRJNA248792, SAMN16972264, AAXRPO000000000.1, assembly PDT000901573.1. The bare strain number is not this NCBI taxon ID.
- `data/catalog/ncbi_genbank-0017.jsonl.gz:19210`: Salmonella Enteritidis, taxid 149539/species 28901, strain FSIS32105020, GCA_018962735.1, PRJNA242847, SAMN19222417, ABAXNT000000000.1. Assembly name PDT001037650.1 supplies the match. Both Salmonella assemblies are excluded from RefSeq as parts of large multi-isolate projects.
- Ten AllTheBacteria rows have scientific name E. coli, dataset r0.2, available FASTA, and passing assembly filters. They match run-accession substrings. Eight pass HQ/Sylph, have true prior HQ membership, and current/prior Sylph E. coli. Row 992939 instead has current/prior Sylph unknown, `SYLPH_RESULTS_FAIL`, HQ `CHECKM2_MAX_CONTAM,MAX_CONTIG_NUM,MIN_N50,SYLPH_RESULTS_FAIL`, and false prior HQ membership. Row 993055 has current/prior Sylph E. coli and passing Sylph, but HQ `CHECKM2_MAX_CONTAM,MAX_CONTIG_NUM` and false prior HQ membership. Complete checksum, filter, and download fields were inspected; none was transferred to the target.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992935 | SAMEA9850290 | ERR10376507 | ERZ25576653 |
| 992936 | SAMEA9850291 | ERR10376505 | ERZ25576663 |
| 992937 | SAMEA9850292 | ERR10376503 | ERZ25576673 |
| 992938 | SAMEA9850293 | ERR10376501 | ERZ25576684 |
| 992939 | SAMEA9850294 | ERR10376509 | ERZ25466044 |
| 993053 | SAMEA9850635 | ERR10376502 | ERZ25466776 |
| 993054 | SAMEA9850636 | ERR10376500 | ERZ25466781 |
| 993055 | SAMEA9850637 | ERR10376506 | ERZ25466786 |
| 993056 | SAMEA9850638 | ERR10376504 | ERZ25466792 |
| 993057 | SAMEA9850639 | ERR10376508 | ERZ25466797 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779760, the DOI, and S003807171100280X. Both returned the same 16 lines: own backbone, scope, scientific name, and 13 unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism/16S web search returned taxonomy-tree and other terminology leads; snippets were not treated as target evidence. The dedicated NCBI primary page was independently inspected.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support recorded taxonomy/name claims. Unchecked full text and isolate-specific assays constrain enrichment research without contradicting those claims.

## Recommended Edits

None required. Preserve BSF2(15)/JF779760.1 identity and fertilized bulk-soil context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Inspect the primary article and isolate-level table before adding BSF2(15)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

All requested NCBI taxonomy/marker responses succeeded. HAL requested metadata and the complete abstract were freshly read for this target. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those routes were not retried. No login, payment, contact, or full-text reading occurred.

YAML SHA-256: `3f5f2f4b67d7e0016f46063dc37748a9d976fa5b8946458e3a6a05eab04c0ffe`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged by this review.
