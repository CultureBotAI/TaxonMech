# YAML Record Review: Burkholderia sp. MRhNF1(8)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf1_8.yaml`
- Started UTC: 2026-10-10T20:40:11Z
- Finished UTC: 2026-10-10T20:43:50Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF1(8), `NCBITaxon:1037628`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf1_8.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf1_8.yaml --out /private/tmp/taxonmech-mrhnf18-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They do not prove full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222843` agrees on ID, label, rank, parent, code, and snapshot 2026-09-13. Exact/related/broad synonym and retirement fields are empty. Every root-first lineage label/rank agrees with its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037628&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037628), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037628) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding identifies this NCBI placeholder, not formal nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32479` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15398` uniquely resolves ID/slug; `curation/seed_scope.tsv:323058` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The single attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037628[Organism:exp]` returned one UID, 345019057. Complete [GenBank annotation JF779806.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779806.1) explicitly joins organism, strain MRhNF1(8), and taxon 1037628. This 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `0c29a8f7af824a890dbe9655079747d91658d38a49aa2975aaef6fea49f235e6`. It is not a genome assembly or deposit accession. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Requested [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), freshly inspected for this review, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Cohort-level findings from 80 isolates do not establish individual MRhNF1(8) assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 13 non-target native matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7623` describes Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0036, GCA_010376285.1, PRJNA560345, SAMN12576326, and JAAGHX000000000.1. Its assembly name ASM1037628v1 supplies the match.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:19421` describes Salmonella enterica subsp. enterica serovar Enteritidis, taxid 149539/species 28901, strain 1037628, GCA_015853005.1, PRJNA248792, SAMN17004512, and AAXQPM000000000.1. The numeric strain designation equal to the target taxid is not an identity bridge. Both rows are excluded from RefSeq as part of a large multi-isolate project.
- `data/catalog/ncbi_genbank-0066.jsonl.gz:27411` describes uncultured bacterium, taxid 77133, isolate BERT20-1_SAMN15783171_MAG_00000005, GCA_982666505.1, PRJEB72921, SAMEA122232388, and CEXJFM000000000.1. Its ungapped size 1037628 supplies the numeric match; total size is 1037898, with 436 contigs and 427 scaffolds. The SAMN accession inside its label is not substituted for its SAMEA BioSample. This scaffold-level MAG is excluded from RefSeq for metagenomic origin, fragmentation, and undefined genus. Absent annotation provider/name and zero gene counts do not establish biological gene absence.
- Ten AllTheBacteria rows match run-accession substrings. Each has scientific/current/prior Sylph name E. coli, r0.2 dataset, available FASTA, and passing assembly/Sylph/HQ filters. Complete SeqKit, filter, and download fields were inspected.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992568 | SAMEA9849680 | ERR10376280 | ERZ25463282 |
| 992569 | SAMEA9849681 | ERR10376282 | ERZ25463287 |
| 992570 | SAMEA9849682 | ERR10376284 | ERZ25463295 |
| 992571 | SAMEA9849683 | ERR10376286 | ERZ25463301 |
| 992572 | SAMEA9849684 | ERR10376288 | ERZ25463307 |
| 992741 | SAMEA9849944 | ERR10376281 | ERZ25464602 |
| 992742 | SAMEA9849945 | ERR10376285 | ERZ25464610 |
| 992743 | SAMEA9849946 | ERR10376283 | ERZ25464619 |
| 992744 | SAMEA9849947 | ERR10376287 | ERZ25464624 |
| 992745 | SAMEA9849948 | ERR10376289 | ERZ25464631 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779806, the study DOI, and S003807171100280X. Both returned 16 lines: own backbone, scope, scientific name, and 13 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. A combined exact organism/16S web query returned no results; that limited query does not establish biological absence.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRhNF1(8)/JF779806 identity and its non-fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRhNF1(8)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, native candidate rows, and requested HAL metadata/abstract were inspected. Earlier reviews of the shared study encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `395f1ffca4ae231b4e99eb34fe97c8a7a9ce37924535b02bd79041fd8554e8e0`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
