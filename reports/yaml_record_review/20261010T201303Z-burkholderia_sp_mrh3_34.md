# YAML Record Review: Burkholderia sp. MRh3(34)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrh3_34.yaml`
- Started UTC: 2026-10-10T20:08:58Z
- Finished UTC: 2026-10-10T20:13:03Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord`, Burkholderia sp. MRh3(34), `NCBITaxon:1037621`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained source inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrh3_34.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrh3_34.yaml --out /private/tmp/taxonmech-mrh334-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, full lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. These checks do not prove full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222836` agrees on ID, label, rank, parent, code, and snapshot 2026-09-13. Exact/related/broad synonym and retirement fields are empty. Each root-first lineage label/rank matches its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037621&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037621), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037621) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding identifies this NCBI placeholder, not formal nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32472` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15391` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323051` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The single attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037621[Organism:exp]` returned one UID, 345019021. Complete [GenBank annotation JF779770.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779770.1) explicitly joins organism, strain MRh3(34), and taxon 1037621. This 450-base 16S rRNA marker is partial at both ends and annotated from fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `26498cf6651b9f9d9ec11d1b479ff740459865b5176589439cf6bd1649b9543d`. It is not a genome assembly or deposit accession. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Requested [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), freshly inspected for this review, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Its 80-isolate study compares soil compartments and calcium-amendment treatments. Cohort-level findings do not establish individual MRh3(34) assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 16 non-target native search matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7620` describes Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0060, GCA_010376215.1, PRJNA560345, SAMN12576330, and JAAGIB000000000.1. Its assembly name ASM1037621v1 supplies the match.
- `data/catalog/ncbi_genbank-0018.jsonl.gz:9880` describes Campylobacter coli, taxid 195, strain FSIS22132614, GCA_019803565.1, PRJNA287430, SAMN21037621, and ABCEBH000000000.1. Its match is within BioSample.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41467` describes Acinetobacter baumannii, taxid 470, strain AB9/isolate 10RC170000667, GCA_050714355.1, SAMN41037621, PRJNA514245, and DBIYQJ000000000.1. Its match is within BioSample; PMID 30286803 is not a target citation. All three GenBank rows are excluded from RefSeq as part of a large multi-isolate project.
- Thirteen AllTheBacteria rows match numeric substrings: ten E. coli run accessions, the Campylobacter BioSample, and SeqKit hashes for Salmonella enterica and Klebsiella pneumoniae. All report available FASTA and passing assembly, Sylph, and HQ filters. Twelve are r0.2; the Klebsiella row is Incr_release.202505 with prior Sylph/HQ membership fields NA. Current Sylph agrees with scientific name except that Campylobacter is labeled Campylobacter_D coli. These unrelated source classifications do not supply a target link.

Complete dataset, filter, SeqKit, and download fields were inspected for all thirteen AllTheBacteria rows:

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 796380 | SAMEA6146537 | ERR3638366 | ERZ25321611 |
| 992670 | SAMEA9849873 | ERR10376212 | ERZ25463980 |
| 992671 | SAMEA9849874 | ERR10376210 | ERZ25463988 |
| 992672 | SAMEA9849875 | ERR10376214 | ERZ25463995 |
| 992673 | SAMEA9849876 | ERR10376216 | ERZ25464003 |
| 992674 | SAMEA9849877 | ERR10376218 | ERZ25464014 |
| 992721 | SAMEA9849924 | ERR10376211 | ERZ25464428 |
| 992722 | SAMEA9849925 | ERR10376215 | ERZ25464438 |
| 992723 | SAMEA9849926 | ERR10376213 | ERZ25464446 |
| 992725 | SAMEA9849928 | ERR10376217 | ERZ25464462 |
| 992727 | SAMEA9849930 | ERR10376219 | ERZ25464482 |
| 2134591 | SAMN21037621 | SRR15667913 | ERZ26004378 |
| 3180628 | SAMN46491108 | SRR32189748 | ERZ27196849 |

None of the 16 unrelated rows establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779770, the study DOI, and S003807171100280X. Both returned 19 lines: own backbone, scope, scientific name, and 16 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism web query returned NCBI genus/family tree listings; these were leads, not independent evidence. It was not an exhaustive literature search.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRh3(34)/JF779770 identity and its fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRh3(34)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, and native candidate rows were inspected for this target. The shared study's requested HAL metadata/abstract were freshly read. Earlier reviews of this study encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `6d17241b25f1df03a25e2ff8add00ee8083954b8826699ae3ca0075077d499ca`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
