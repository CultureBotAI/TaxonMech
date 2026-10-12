# YAML Record Review: Burkholderia sp. MRhNF1(12)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf1_12.yaml`
- Started UTC: 2026-10-10T20:27:02Z
- Finished UTC: 2026-10-10T20:29:28Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF1(12), `NCBITaxon:1037625`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf1_12.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf1_12.yaml --out /private/tmp/taxonmech-mrhnf112-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They do not prove full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222840` agrees on ID, label, rank, parent, code, and snapshot 2026-09-13. Exact/related/broad synonym and retirement fields are empty. Every root-first lineage label/rank agrees with its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037625&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037625), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037625) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding identifies this NCBI placeholder, not formal nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32476` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15395` uniquely resolves ID/slug; `curation/seed_scope.tsv:323055` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The single attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037625[Organism:exp]` returned one UID, 345019058. Complete [GenBank annotation JF779807.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779807.1) explicitly joins organism, strain MRhNF1(12), and taxon 1037625. This 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `06811ffcfa3fc6cfb97d074ad151311493030defd5e068c21c7fbdf52caf3523`. It is not a genome assembly or deposit accession. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Requested [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), freshly inspected for this review, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The study compares soil compartments and calcium treatments using 80 isolates. Cohort-level findings do not establish individual MRhNF1(12) assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 14 non-target native matches were read completely:

- `data/catalog/ncbi_genbank-0019.jsonl.gz:19113` describes Listeria monocytogenes, taxid 1639, isolate Lm-2013-39163, GCA_021037625.1, PRJNA514245, SAMEA9563550, and DAFGCQ000000000.1. PMID 30286803 belongs to this unrelated row.
- `data/catalog/ncbi_genbank-0037.jsonl.gz:25769` describes Klebsiella pneumoniae, taxid 573, strain zj19001, GCA_041037625.1, PRJNA1021041, SAMN37544740, and JAZCMW000000000.1. The row has no annotation provider/name and zero reported gene counts, not evidence of biological gene absence. Both GenBank matches are assembly-accession substrings and both rows are excluded from RefSeq as part of a large multi-isolate project.
- Twelve AllTheBacteria rows match ten E. coli run-accession substrings and SeqKit hashes for Salmonella enterica and Clostridioides difficile. All are r0.2 with available FASTA and passing assembly filters. Row 992562 has unknown current/prior Sylph species and SYLPH_RESULTS_FAIL in Sylph/HQ fields; the other eleven have passing Sylph/HQ filters and species labels matching their scientific names. Available FASTA is preserved even for the failed-filter row.

Complete dataset, filter, SeqKit, and download fields were inspected for all twelve rows:

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992451 | SAMEA9849534 | ERR10376258 | ERZ25462511 |
| 992547 | SAMEA9849659 | ERR10376259 | ERZ25463133 |
| 992560 | SAMEA9849672 | ERR10376250 | ERZ25463229 |
| 992561 | SAMEA9849673 | ERR10376252 | ERZ25463234 |
| 992562 | SAMEA9849674 | ERR10376254 | ERZ25463240 |
| 992564 | SAMEA9849676 | ERR10376256 | ERZ25463253 |
| 992733 | SAMEA9849936 | ERR10376251 | ERZ25464535 |
| 992735 | SAMEA9849938 | ERR10376253 | ERZ25464549 |
| 992736 | SAMEA9849939 | ERR10376255 | ERZ25464559 |
| 992738 | SAMEA9849941 | ERR10376257 | ERZ25464577 |
| 1583865 | SAMN11419426 | SRR8898400 | ERZ25569144 |
| 1749987 | SAMN13621960 | SRR10727833 | ERZ25759067 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779807, the study DOI, and S003807171100280X. Both returned 17 lines: own backbone, scope, scientific name, and 14 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. A combined exact organism/accession web query returned no results; that limited query does not establish biological absence.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRhNF1(12)/JF779807 identity and its non-fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRhNF1(12)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, native candidate rows, and requested HAL metadata/abstract were inspected. Earlier reviews of the shared study encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `bcfcf849fda2f01fe03698ba30712345b9f9805a3a972f33a3582f931f17792e`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
