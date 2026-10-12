# YAML Record Review: Burkholderia sp. MRhNF3(11)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf3_11.yaml`
- Started UTC: 2026-10-10T21:31:24Z
- Finished UTC: 2026-10-10T21:35:33Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF3(11), `NCBITaxon:1037639`. It carries species rank, bacterial domain, parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained source inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf3_11.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf3_11.yaml --out /private/tmp/taxonmech-mrhnf311-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, complete lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. These are not full-corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222854` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. The complete root-first ancestor chain agrees with each ancestor's own backbone row: root 1 (no rank); cellular organisms 131567 (cellular root); Bacteria 2 (domain); Pseudomonadati 3379134 (kingdom); Pseudomonadota 1224 (phylum); Betaproteobacteria 28216 (class); Burkholderiales 80840 (order); Burkholderiaceae 119060 (family); Burkholderia 32008 (genus); unclassified Burkholderia 2613784 (no rank).

Complete live [EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037639&retmode=xml) and [Datasets taxonomy JSON](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037639) returned HTTP 200 and support recorded identity and lineage. EFetch verifies parent, ancestor labels/ranks, and code 11; it omits root while Datasets includes it. Datasets omits assembly count, not an assertion of zero assemblies. Exact grounding denotes this NCBI placeholder, not nomenclatural standing or a culture deposit.

The [Taxonomy Browser page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037639) returned HTTP 500 on both attempts. Its text was not read; this supplementary check remains unavailable, distinct from the successful authority API checks.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32490` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15409` uniquely resolves ID/slug; `curation/seed_scope.tsv:323069` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match these inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037639[Organism:exp]` returned one UID, 345019062. Complete [GenBank annotation JF779811.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779811.1) explicitly joins organism, strain MRhNF3(11), and taxon 1037639. The 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `4a95c4081576b8bd96f7d28664012f64118d84e9d0969acb4385859161828531`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Freshly retrieved [HAL metadata and complete abstract](https://hal.science/hal-02916138v1) confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate cohort compares mineral-amended and control forest plots; cohort results do not establish MRhNF3(11)-specific assays. No mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 12 non-target native matches were read completely:

- `data/catalog/ncbi_genbank-0014.jsonl.gz:20443`: Salmonella enterica subsp. enterica serovar Enteritidis, taxid 149539/species 28901, strain 1037639, GCA_015873545.1, PRJNA248792, SAMN16972249, AAXRPU000000000.1. The numeric strain designation is not a target identity bridge. RefSeq exclusion cites a large multi-isolate project.
- `data/catalog/ncbi_genbank-0065.jsonl.gz:39607`: uncultured bacterium, taxid/species 77133, isolate CTOTU24005, GCA_980324135.1, PRJEB97459, SAMEA121578099, CEKFAG000000000.1. Genome size 1037639 supplies the match; this is not its taxon ID. RefSeq exclusion cites metagenome derivation and undefined genus.
- Ten complete AllTheBacteria rows match run-accession substrings. All have dataset r0.2, scientific name Escherichia coli, available FASTA, and passing assembly-pipeline filter. Nine have current/prior Sylph E. coli, passing Sylph/HQ filters, and true prior HQ membership. Row 992774 instead has current/prior Sylph unknown, `SYLPH_RESULTS_FAIL` for Sylph/HQ filters, and false prior HQ membership. Complete SeqKit, filter, and download fields were inspected; these source distinctions were preserved.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992772 | SAMEA9849975 | ERR10376391 | ERZ25464842 |
| 992773 | SAMEA9849976 | ERR10376395 | ERZ25464849 |
| 992774 | SAMEA9849977 | ERR10376393 | ERZ25464855 |
| 992775 | SAMEA9849978 | ERR10376397 | ERZ25464867 |
| 992776 | SAMEA9849979 | ERR10376399 | ERZ25464874 |
| 992811 | SAMEA9850019 | ERR10376392 | ERZ25465175 |
| 992812 | SAMEA9850020 | ERR10376390 | ERZ25465180 |
| 992813 | SAMEA9850021 | ERR10376394 | ERZ25465193 |
| 992814 | SAMEA9850023 | ERR10376396 | ERZ25465201 |
| 992815 | SAMEA9850024 | ERR10376398 | ERZ25465214 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779811, the DOI, and S003807171100280X. Both returned the same 15 lines: own backbone, scope, scientific name, and 12 unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism/16S web search returned NCBI taxonomy tree leads; snippets were not treated as new evidence.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned sources and successfully retrieved authority APIs support recorded taxonomy/name claims. The unavailable browser rendering, unchecked article full text, and unverified isolate-specific assays limit additional checks and enrichment research without contradicting those claims.

## Recommended Edits

None required. Preserve MRhNF3(11)/JF779811.1 identity and non-fertilized ectomycorrhizosphere context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Retry the supplementary browser page when available. Inspect the primary article and isolate-level table before adding MRhNF3(11)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Both browser attempts failed with HTTP 500. Complete EFetch XML and Datasets JSON succeeded, so taxonomy was checked independently of that unavailable rendering. Marker annotation, native rows, and HAL metadata/abstract were freshly inspected for this target. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed full-text routes were not retried. No login, payment, contact, or full-text reading occurred.

YAML SHA-256: `23d48ae441504c26e1d690451ed31322849436efa27590d2bdef5fdf93623d89`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged by this review.
