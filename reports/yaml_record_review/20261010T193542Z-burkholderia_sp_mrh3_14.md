# YAML Record Review: Burkholderia sp. MRh3(14)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrh3_14.yaml`
- Started UTC: 2026-10-10T19:32:38Z
- Finished UTC: 2026-10-10T19:35:42Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord`, Burkholderia sp. MRh3(14), `NCBITaxon:1037612`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes; generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrh3_14.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrh3_14.yaml --out /private/tmp/taxonmech-mrh314-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. These bounded checks do not prove corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222827` agrees on ID, label, rank, parent, code, and the 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Every root-first lineage label/rank matches its backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037612&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037612), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037612) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count, which is not a zero count. Exact grounding preserves this NCBI placeholder identity, not formal nomenclatural standing or a culture-deposit identity.

The complete native name row at `data/catalog/ncbi_names-0005.jsonl.gz:32463` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15382` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323042` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The single attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037612[Organism:exp]` returned one UID, 345019031. Complete [GenBank annotation JF779780.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779780.1) explicitly joins organism, strain MRh3(14), and taxon 1037612. This 450-base 16S rRNA fragment is partial at both ends and annotated from fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `ddad1a3b0443dec526661597b1c0c5874ae3c3d34a6849860faefa10faaeab57`. It is not a genome assembly or deposit accession. Country, collection date, coordinates, and deposit qualifiers are absent from this annotation. The 5 April 2011 submission and INRA Champenoux address do not establish collection metadata.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1) were read during this review and confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The abstract describes an 80-isolate cohort and calcium-amendment comparisons, not an individual MRh3(14) assay result. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 16 non-target native search matches were read completely:

- `data/bvbrc/bvbrc-0001.jsonl.gz:9840` and `data/catalog/ncbi_genbank-0047.jsonl.gz:810` concern Staphylococcus aureus F88, taxid 1280, BioProject PRJNA1037612 and BioSample SAMN38194530. They identify BV-BRC 1280.63074, GCA_050916375.1/GCF_050916375.1, and CP139159/CP139160. The matching project number is not the target taxonomy ID.
- `data/catalog/gtdb_genomes-0002.jsonl.gz:16252` concerns Chlamydia trachomatis, taxid 813, R32100extract, GCF_001398215.1/GCA_001398215.1, PRJNA224116, and SAMEA1398303. The numeric match is contig N50, not taxon identity.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:7615` concerns Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0117, GCA_010376125.1, PRJNA560345, SAMN12576335, and JAAGIG000000000.1. Its assembly name ASM1037612v1 supplies the match; its exclusion from RefSeq is a large multi-isolate project flag.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41464` concerns Acinetobacter baumannii, taxid 470, strain AB4/isolate 10BC200000005, GCA_050714295.1, SAMN41037612, PRJNA514245, and DBIYQG000000000.1. The numeric match is in BioSample; PMID 30286803 is not a target citation.
- `data/catalog/ncbi_genbank-0054.jsonl.gz:19347` concerns Chlamydiales bacterium, taxid 2047757, isolate BJG_B_C30_databinning_comebin_bin406, GCA_058752955.1, SAMN60664191, PRJNA1467875, and JBZLOH000000000.1. Genome length supplies the numeric match. It is flagged as metagenome-derived, fragmented, and genus undefined.
- Ten AllTheBacteria rows match run-accession substrings. All have scientific name Escherichia coli. Nine have available FASTA, r0.2 dataset, and passing assembly/Sylph/HQ filters. Row 992508 has Sylph species Salmonella enterica, and row 992696 has Hafnia paralvei; seven other available rows have E. coli Sylph labels. Row 992511 is rejected with ASM_LEN, no FASTA, and no ENA analysis. These source-label differences and rejection are preserved, not evidence for MRh3(14).

Complete dataset, filter, SeqKit, and download fields were inspected for all ten AllTheBacteria rows:

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992506 | SAMEA9849610 | ERR10376126 | ERZ25462860 |
| 992508 | SAMEA9849612 | ERR10376124 | ERZ25462877 |
| 992509 | SAMEA9849613 | ERR10376125 | ERZ25462884 |
| 992510 | SAMEA9849614 | ERR10376127 | ERZ25462889 |
| 992511 | SAMEA9849615 | ERR10376129 | None |
| 992512 | SAMEA9849616 | ERR10376128 | ERZ25462894 |
| 992644 | SAMEA9849847 | ERR10376122 | ERZ25576483 |
| 992645 | SAMEA9849848 | ERR10376120 | ERZ25576495 |
| 992696 | SAMEA9849899 | ERR10376123 | ERZ25464208 |
| 992697 | SAMEA9849900 | ERR10376121 | ERZ25464221 |

None of the 16 unrelated rows establishes a target attestation, synonym, deposit, or genome. Project, sample, run, and assembly identifiers remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779780, the study DOI, and S003807171100280X. Both returned 19 lines: own backbone, scope, scientific name, and 16 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism/accession web searches yielded taxonomy-tree leads, not evidence for additional isolate-specific claims.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRh3(14)/JF779780 identity and the fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRh3(14)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, requested HAL metadata/abstract, and native candidate rows were inspected for this target. Earlier attempts for this study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `ad98abaeb5840cd78951cc6b8fe078ca9deff402a32db7dc017bc99ac4493ead`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
