# YAML Record Review: Burkholderia sp. MRhNF1(9)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf1_9.yaml`
- Started UTC: 2026-10-10T20:44:48Z
- Finished UTC: 2026-10-10T20:47:52Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF1(9), `NCBITaxon:1037629`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf1_9.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf1_9.yaml --out /private/tmp/taxonmech-mrhnf19-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They do not prove full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222844` agrees on ID, label, rank, parent, code, and snapshot 2026-09-13. Exact/related/broad synonym and retirement fields are empty. Every root-first lineage label/rank agrees with its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037629&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037629), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037629) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding identifies this NCBI placeholder, not formal nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32480` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15399` uniquely resolves ID/slug; `curation/seed_scope.tsv:323059` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The single attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037629[Organism:exp]` returned one UID, 345019074. Complete [GenBank annotation JF779823.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779823.1) explicitly joins organism, strain MRhNF1(9), and taxon 1037629. This 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `a5ab92eb99c8797775cc7bfe204d533c3ca6d7780ef423137301de6c4bd68c3a`. It is not a genome assembly or deposit accession. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. Partial-marker sequence identity alone would not establish identity between separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Requested [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), inspected earlier this turn for the shared study, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Cohort-level findings do not establish individual MRhNF1(9) assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 12 non-target native matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7624` describes Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0021, GCA_010376295.1, PRJNA560345, SAMN12576325, and JAAGHW000000000.1. Its assembly name ASM1037629v1 supplies the match.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:12410` describes Salmonella enterica subsp. enterica serovar Typhimurium, taxid 90371/species 28901, strain 1037629, GCA_015710735.1, PRJNA248792, SAMN16972261, and AAXMCL000000000.1. Its numeric strain designation equal to the target taxid is not an identity bridge. Both rows are excluded from RefSeq as part of a large multi-isolate project.
- Ten AllTheBacteria rows match run-accession substrings. All have scientific name E. coli, r0.2 dataset, available FASTA, and passing assembly filters. Seven have current/prior Sylph E. coli and passing Sylph/HQ filters. Rows 992462, 992464, and 992602 have unknown current/prior Sylph and SYLPH_RESULTS_FAIL. Row 992464 additionally has CHECKM2_MAX_CONTAM in its HQ filter; all three have false prior HQ membership. Available FASTA was not conflated with passing quality. Complete SeqKit, filter, and download fields were inspected.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992459 | SAMEA9849543 | ERR10376290 | ERZ25462565 |
| 992460 | SAMEA9849545 | ERR10376292 | ERZ25462570 |
| 992461 | SAMEA9849546 | ERR10376294 | ERZ25462576 |
| 992462 | SAMEA9849547 | ERR10376296 | ERZ25462580 |
| 992464 | SAMEA9849549 | ERR10376298 | ERZ25462589 |
| 992555 | SAMEA9849667 | ERR10376291 | ERZ25463193 |
| 992599 | SAMEA9849711 | ERR10376295 | ERZ25576386 |
| 992600 | SAMEA9849712 | ERR10376293 | ERZ25576396 |
| 992601 | SAMEA9849713 | ERR10376299 | ERZ25576405 |
| 992602 | SAMEA9849714 | ERR10376297 | ERZ25576414 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779823, the study DOI, and S003807171100280X. Both returned 15 lines: own backbone, scope, scientific name, and 12 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. A combined exact organism/16S web query returned no results; that limited query does not establish biological absence.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRhNF1(9)/JF779823 identity and its non-fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRhNF1(9)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, and native candidate rows were inspected for this target. The shared study's requested HAL metadata/abstract were read earlier this turn. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `d855128326ce8110fafeb7324aee66ec56264b60fce70a10f8e0b7be7b944976`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
