# YAML Record Review: Burkholderia sp. MRh3(24)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrh3_24.yaml`
- Started UTC: 2026-10-10T19:54:27Z
- Finished UTC: 2026-10-10T19:56:20Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for Burkholderia sp. MRh3(24), `NCBITaxon:1037617`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrh3_24.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrh3_24.yaml --out /private/tmp/taxonmech-mrh324-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured checks passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They do not prove full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222832` agrees on ID, label, rank, parent, code, and snapshot 2026-09-13. Exact/related/broad synonym and retirement fields are empty. Each root-first lineage label/rank matches its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037617&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037617), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037617) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding identifies this NCBI placeholder, not formal nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32468` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15387` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323047` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The single attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037617[Organism:exp]` returned one UID, 345019028. Complete [GenBank annotation JF779777.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779777.1) explicitly joins organism, strain MRh3(24), and taxon 1037617. This 450-base 16S rRNA marker is partial at both ends and annotated from fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `371093e4c6d20ae524f4d7e8e838161b5f826600302fa43ac740faa6caec63ad`. It is not a genome assembly or deposit accession. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1), inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Cohort-level findings do not establish individual MRh3(24) assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 13 non-target native search matches were read completely:

- `data/catalog/ncbi_genbank-0014.jsonl.gz:12340` describes E. coli, taxid 562, strain 1037617, GCA_015709005.1, SAMN16961268, PRJNA315192, and AAXMBY000000000.1. A numeric strain designation is not this NCBI taxonomy ID.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41466` describes Acinetobacter baumannii, taxid 470, strain AB5/isolate 10BC200004711, GCA_050714335.1, SAMN41037617, PRJNA514245, and DBIYQI000000000.1. The match is within BioSample; PMID 30286803 is not a target citation. Both GenBank rows are excluded from RefSeq as part of a large multi-isolate project.
- `data/gold/analyses.jsonl.gz:106453` describes Streptococcus pneumoniae sv. 07F 2245STDY5609060, GOLD analysis Ga0165775, project Gp0185488, IMG 8010376177, GCA_900051145.2, and unversioned FHGI00000000. Its organism GOLD ID field is blank. The numeric match is inside the IMG identifier; neither that substring nor the isolate-analysis type establishes a target organism/deposit/project chain. Ga/Gp are source analysis/project records, not genome identifiers. No target GOLD link was inferred.
- Ten AllTheBacteria rows match run-accession substrings. All have E. coli scientific and Sylph labels, r0.2 dataset, available FASTA, and passing assembly/Sylph/HQ filters. Their complete dataset, filter, SeqKit, and download fields were read.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992523 | SAMEA9849629 | ERR10376172 | ERZ25462960 |
| 992524 | SAMEA9849630 | ERR10376173 | ERZ25462965 |
| 992525 | SAMEA9849633 | ERR10376174 | ERZ25462972 |
| 992526 | SAMEA9849634 | ERR10376176 | ERZ25462975 |
| 992527 | SAMEA9849635 | ERR10376175 | ERZ25462981 |
| 992528 | SAMEA9849636 | ERR10376178 | ERZ25462985 |
| 992529 | SAMEA9849637 | ERR10376177 | ERZ25462994 |
| 992530 | SAMEA9849638 | ERR10376179 | ERZ25463000 |
| 992661 | SAMEA9849864 | ERR10376170 | ERZ25463894 |
| 992713 | SAMEA9849916 | ERR10376171 | ERZ25464359 |

None of the 13 unrelated rows establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779777, the study DOI, and S003807171100280X. Both returned 16 lines: own backbone, scope, scientific name, and 13 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. A combined exact organism/accession web query returned no results; that limited search is not evidence of biological absence.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRh3(24)/JF779777 identity and its fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRh3(24)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, and native candidate rows were inspected for this target. The shared study's requested HAL metadata/abstract were read earlier this turn. Earlier attempts for this study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `1f28ab2c7d7daa5064bd068a05f3ab0047d4dc15ec89c3c3432fb6d6918b2160`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
