# YAML Record Review: Burkholderia sp. MRhNF2(12)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf2_12.yaml`
- Started UTC: 2026-10-10T20:57:52Z
- Finished UTC: 2026-10-10T21:00:52Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for Burkholderia sp. MRhNF2(12), `NCBITaxon:1037631`. It records a species-ranked bacterial placeholder with parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf2_12.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf2_12.yaml --out /private/tmp/taxonmech-mrhnf212-20261010-validation.tsv --workers 1`: one file, zero errors; inspected output is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured source comparisons passed for identity, complete lineage, synonyms, code, name attestation, unique index row, scope reason, and seed-event wording. These are not full-corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. These full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222846` agrees on identity, rank, parent, code, and snapshot 2026-09-13. Exact/related/broad synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037631&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037631), and all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037631) lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes the NCBI placeholder, not nomenclatural standing or a deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32482` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15401` uniquely resolves ID/slug; `curation/seed_scope.tsv:323061` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The single source attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains agree with these inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037631[Organism:exp]` returned one UID, 345019064. Complete [GenBank annotation JF779813.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779813.1) explicitly joins organism, strain MRhNF2(12), and taxon 1037631. This 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `f7936266f598b7becfb6a32874a782d258e00532b1c2aae36223242e8c798f71`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Freshly read [HAL metadata and complete abstract](https://hal.science/hal-02916138v1) confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010), a study of 80 isolates comparing control and mineral-amended forest plots. Cohort-level results do not establish MRhNF2(12)-specific assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 12 non-target native matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7625`: Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0020, GCA_010376315.1, PRJNA560345, SAMN12576324, JAAGHV000000000.1. Assembly name ASM1037631v1 supplies the numeric match.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:12445`: Salmonella enterica subsp. enterica serovar Typhimurium, taxid 90371/species 28901, strain 1037631, GCA_015711435.1, PRJNA248792, SAMN16972233, AAXMEJ000000000.1. The numeric strain designation is not a target identity bridge. Both assemblies are excluded from RefSeq as part of a large multi-isolate project.
- Ten AllTheBacteria rows have scientific name/current and prior Sylph E. coli, dataset r0.2, available FASTA, passing assembly/Sylph/HQ filters, and true prior HQ membership. Their run-accession substrings supply the matches. Complete SeqKit, filter, and download fields were inspected.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992574 | SAMEA9849686 | ERR10376310 | ERZ25463314 |
| 992576 | SAMEA9849688 | ERR10376312 | ERZ25463323 |
| 992577 | SAMEA9849689 | ERR10376314 | ERZ25463330 |
| 992579 | SAMEA9849691 | ERR10376316 | ERZ25463342 |
| 992580 | SAMEA9849692 | ERR10376318 | ERZ25463352 |
| 992748 | SAMEA9849951 | ERR10376311 | ERZ25464657 |
| 992749 | SAMEA9849952 | ERR10376315 | ERZ25464663 |
| 992750 | SAMEA9849953 | ERR10376313 | ERZ25464672 |
| 992751 | SAMEA9849954 | ERR10376317 | ERZ25464678 |
| 992752 | SAMEA9849955 | ERR10376319 | ERZ25464685 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779813, the DOI, and S003807171100280X. Both searches returned the same 15 lines: own backbone, scope, scientific name, and 12 unrelated rows above. Ignored and compressed files were included; no additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. A combined exact organism/16S web search returned NCBI taxonomy tree leads; the dedicated primary taxon page was independently inspected, and snippets were not treated as new evidence.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support recorded taxonomy/name claims. Unchecked full text and isolate-specific assays constrain enrichment research without contradicting those claims.

## Recommended Edits

None required. Preserve MRhNF2(12)/JF779813.1 identity and non-fertilized ectomycorrhizosphere context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Inspect the primary article and isolate-level table before adding MRhNF2(12)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Taxonomy responses, full browser text, marker annotation, native rows, and requested HAL metadata/abstract were inspected. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `89d9baeae51e8c72458e303494b2095bc0c251cdea95e7511e74377279184f2b`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged.
