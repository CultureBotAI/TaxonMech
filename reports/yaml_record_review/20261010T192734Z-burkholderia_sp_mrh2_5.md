# YAML Record Review: Burkholderia sp. MRh2(5)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrh2_5.yaml`
- Started UTC: 2026-10-10T19:24:08Z
- Finished UTC: 2026-10-10T19:27:34Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for Burkholderia sp. MRh2(5), `NCBITaxon:1037611`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes; generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrh2_5.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrh2_5.yaml --out /private/tmp/taxonmech-mrh25-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured comparisons passed for identity, full lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. This is not full corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222826` agrees on ID, label, rank, parent, code, and the 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Each root-first lineage label/rank matches its individual backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037611&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037611), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037611) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding preserves this NCBI placeholder identity, not formal nomenclatural standing or a culture-deposit identity.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32462` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15381` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323041` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping sections match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide search `txid1037611[Organism:exp]` returned one UID, 345019022. Complete [GenBank annotation JF779771.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779771.1) explicitly joins organism, strain MRh2(5), and taxon 1037611. This is a 450-base 16S rRNA fragment incomplete at both ends, annotated from fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `26c09493bc54ddae1cbb29d1e83a75f6915d981be4c446b770a5974af1251b76`. It is not a genome assembly or deposit identifier. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz and colleagues' 2011 study, Soil Biology and Biochemistry 43(11):2275-2282. Complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1), inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Cohort-level results do not establish individual MRh2(5) assays. No mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 12 non-target native search matches were read completely:

- `data/catalog/ncbi_genbank-0046.jsonl.gz:41512` describes Acinetobacter baumannii, taxid 470, strain AB39/isolate 10RC170001217, GCA_050715255.1, SAMN41037611, PRJNA514245, and DBIYRH000000000.1. The numeric match is within BioSample, not the target taxonomy ID; PMID 30286803 is not a target citation.
- Ten AllTheBacteria rows match run-accession substrings and have scientific name Escherichia coli. Eight have matching E. coli Sylph labels; rows 992640 and 992693 instead have Hafnia paralvei Sylph assignments. All ten have available FASTA and passing assembly/Sylph/HQ filters. These retained label differences do not supply evidence for Burkholderia MRh2(5).
- A further AllTheBacteria row, 1891740, is labeled Salmonella enterica subsp. enterica serovar Javiana, with Sylph species Salmonella enterica. It has available FASTA and passing filters. The match is checksum substring `1037611` in `seqkit.v0.1_DLS_k0_6b064c17e4bb103761101ae274579f54`, not a taxonomy identifier or MD5 assertion.

Complete dataset, SeqKit, filter, and download fields were inspected for all 11 AllTheBacteria rows:

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992639 | SAMEA9849842 | ERR10376110 | ERZ25463782 |
| 992640 | SAMEA9849843 | ERR10376112 | ERZ25463793 |
| 992641 | SAMEA9849844 | ERR10376114 | ERZ25463803 |
| 992642 | SAMEA9849845 | ERR10376116 | ERZ25463811 |
| 992643 | SAMEA9849846 | ERR10376118 | ERZ25463820 |
| 992690 | SAMEA9849893 | ERR10376111 | ERZ25464160 |
| 992692 | SAMEA9849895 | ERR10376115 | ERZ25464178 |
| 992693 | SAMEA9849896 | ERR10376113 | ERZ25464186 |
| 992694 | SAMEA9849897 | ERR10376117 | ERZ25464193 |
| 992695 | SAMEA9849898 | ERR10376119 | ERZ25464200 |
| 1891740 | SAMN15858802 | SRR12478290 | ERZ25804025 |

None of the 12 non-target rows establishes another target attestation, synonym, deposit, or genome. Sample, project, run, and assembly identifiers remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779771, the study DOI, and S003807171100280X. Both returned 15 lines: own backbone, scope, scientific name, and 12 unrelated rows described above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism/accession web searches yielded taxonomy-tree leads, not evidence for additional isolate-level claims.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the taxonomy/name-only assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve exact MRh2(5)/JF779771 identity and the fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the primary article and isolate-level table and inspect MRh2(5)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, and candidate native rows were inspected for this target. The shared study's requested HAL metadata and abstract were read earlier this turn. Earlier attempts for the study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried for this isolate. No login, payment, or full-text reading occurred.

YAML SHA-256: `162a5a2b911365c2232951b1acb4ef06d7c91a2df3ea755b52a5b5d1b68fcc52`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
