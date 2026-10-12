# YAML Record Review: Burkholderia sp. MRh3(28)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrh3_28.yaml`
- Started UTC: 2026-10-10T19:58:33Z
- Finished UTC: 2026-10-10T20:00:46Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord`, Burkholderia sp. MRh3(28), `NCBITaxon:1037618`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrh3_28.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrh3_28.yaml --out /private/tmp/taxonmech-mrh328-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured checks passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They do not prove full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222833` agrees on ID, label, rank, parent, code, and snapshot 2026-09-13. Exact/related/broad synonym and retirement fields are empty. Each root-first lineage label/rank matches its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037618&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037618), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037618) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding identifies this NCBI placeholder, not formal nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32469` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15388` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323048` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The single attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037618[Organism:exp]` returned one UID, 345019027. Complete [GenBank annotation JF779776.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779776.1) explicitly joins organism, strain MRh3(28), and taxon 1037618. This 450-base 16S rRNA fragment is partial at both ends and annotated from fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `bc91aca77504d13e855cb6c506e059ff778f17bede39b5c8180eac1f3789c72b`. It is not a genome assembly or deposit accession. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1) were read during this review and confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Its 80-isolate cohort and calcium-amendment comparisons do not establish individual MRh3(28) assay results. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 14 non-target native search matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7618` describes Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0063, GCA_010376185.1, PRJNA560345, SAMN12576331, and JAAGIC000000000.1. Its assembly name ASM1037618v1 supplies the match.
- `data/catalog/ncbi_genbank-0018.jsonl.gz:9878` describes Campylobacter jejuni, taxid 197, strain FSIS22132613, GCA_019803525.1, PRJNA287430, SAMN21037618, and ABCEBN000000000.1. Its match is within BioSample.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41604` describes Acinetobacter baumannii, taxid 470, strain AB6/isolate 10UC190066122, GCA_050717095.1, SAMN41037618, PRJNA514245, and DBIYUI000000000.1. The match is within BioSample; PMID 30286803 is not a target citation. All three GenBank rows are excluded from RefSeq as part of a large multi-isolate project.
- Ten AllTheBacteria rows match run-accession substrings and have E. coli scientific and Sylph labels. Row 2134590 instead matches SAMN21037618, scientific name Campylobacter jejuni, Sylph species Campylobacter_D jejuni, SRR15667914, and ERZ26004372. All 11 rows are r0.2, have available FASTA, and pass assembly/Sylph/HQ filters. Shared BioSample with a non-target GenBank row does not establish sequence identity or any link to MRh3(28).

Complete dataset, filter, SeqKit, and download fields were inspected for all 11 AllTheBacteria rows:

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992662 | SAMEA9849865 | ERR10376180 | ERZ25463909 |
| 992663 | SAMEA9849866 | ERR10376182 | ERZ25463917 |
| 992664 | SAMEA9849867 | ERR10376184 | ERZ25463923 |
| 992665 | SAMEA9849868 | ERR10376186 | ERZ25463932 |
| 992666 | SAMEA9849869 | ERR10376188 | ERZ25463942 |
| 992711 | SAMEA9849914 | ERR10376181 | ERZ25464341 |
| 992715 | SAMEA9849918 | ERR10376185 | ERZ25464378 |
| 992716 | SAMEA9849919 | ERR10376183 | ERZ25464386 |
| 992717 | SAMEA9849920 | ERR10376187 | ERZ25464395 |
| 992718 | SAMEA9849921 | ERR10376189 | ERZ25464402 |
| 2134590 | SAMN21037618 | SRR15667914 | ERZ26004372 |

None of the 14 unrelated rows establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779776, the study DOI, and S003807171100280X. Both returned 17 lines: own backbone, scope, scientific name, and 14 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. A combined exact organism/accession web query returned no results; that limited search is not evidence of biological absence.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRh3(28)/JF779776 identity and its fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRh3(28)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, requested HAL metadata/abstract, and native candidate rows were inspected for this target. Earlier attempts for this study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `3b58d0582e4c02afdcb5ea919ad569e71c1d2a5266d0d8bbcb8022e57b3a87ad`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
