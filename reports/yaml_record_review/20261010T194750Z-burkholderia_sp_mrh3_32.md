# YAML Record Review: Burkholderia sp. MRh3(32)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrh3_32.yaml`
- Started UTC: 2026-10-10T19:45:32Z
- Finished UTC: 2026-10-10T19:47:50Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord`, Burkholderia sp. MRh3(32), `NCBITaxon:1037615`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrh3_32.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrh3_32.yaml --out /private/tmp/taxonmech-mrh332-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They do not prove full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222830` agrees on ID, label, rank, parent, code, and the 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Each root-first lineage label/rank matches its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037615&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037615), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037615) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding identifies this NCBI placeholder, not formal nomenclatural standing or a culture-deposit identity.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32466` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15385` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323045` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The single attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037615[Organism:exp]` returned one UID, 345019024. Complete [GenBank annotation JF779773.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779773.1) explicitly joins organism, strain MRh3(32), and taxon 1037615. This 450-base 16S rRNA fragment is partial at both ends and annotated from fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `35dde56853e6fa20500f6d2b78016acf9b689e9ac541c7a1178111a46e7bb643`. It is not a genome assembly or deposit accession. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1) were read during this review and confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Its 80-isolate cohort and calcium-amendment comparisons do not establish individual MRh3(32) assay results. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 20 non-target native search matches were read completely:

- Klebsiella pneumoniae P36, taxid 573, occurs in `data/bvbrc/bvbrc-0024.jsonl.gz:28629`, `data/catalog/gtdb_genomes-0012.jsonl.gz:35873`, `data/catalog/ncbi_genbank-0009.jsonl.gz:40286`, and `data/catalog/ncbi_refseq-0002.jsonl.gz:42595`. These rows identify BV-BRC 573.30930, GCA_011037615.1/GCF_011037615.1, and SAMN10592687. GenBank/BV-BRC give PRJNA510003; GTDB/RefSeq give PRJNA224116. BV-BRC supplies unversioned SBCT00000000 while the other rows supply SBCT00000000.1. The match is within assembly accessions, not taxonomy ID; GTDB's Brazil/blood metadata do not concern MRh3(32).
- `data/catalog/ncbi_genbank-0014.jsonl.gz:12292` describes Shigella sonnei, taxid 624, strain 1037615, GCA_015707555.1, SAMN16961324, PRJNA315192, and AAXMBI000000000.1. A numeric strain name is not this NCBI taxonomy ID.
- `data/catalog/ncbi_genbank-0028.jsonl.gz:43569` describes K. pneumoniae isolate 2002224, taxid 573, GCA_031037615.3, SAMN34589397, PRJNA288601, and ABLWLD000000000.3. Historical rows `data/catalog/ncbi_genbank_historical-0001.jsonl.gz:21392` and `:21393` preserve replaced GCA_031037615.1 and .2, paired with ABLWLD000000000.1 and .2; their non-live dates are 2024-03-05 and 2025-08-11. Versions are not interchangeable. The numeric match is in assembly accessions.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41523` describes Acinetobacter baumannii, taxid 470, strain AB42/isolate 10MC200000267, GCA_050715475.1, SAMN41037615, PRJNA514245, and DBIYRN000000000.1. The match is within BioSample; PMID 30286803 is not a target citation.
- `data/catalog/ncbi_genbank-0056.jsonl.gz:27408` describes metagenome-derived Massilioclostridium sp., taxid 1935928, isolate 1909_1909I_C_20, GCA_061037615.1, SAMN60703975, PRJNA1464738, and JCDDIO000000000.1. Again the match is in assembly accession, not target identity.
- Ten AllTheBacteria rows match run-accession substrings. All have scientific and Sylph species E. coli, r0.2 dataset, available FASTA, and passing assembly/Sylph/HQ filters. Their full dataset, filter, SeqKit, and download fields were read.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992516 | SAMEA9849620 | ERR10376150 | ERZ25462909 |
| 992518 | SAMEA9849622 | ERR10376151 | ERZ25462924 |
| 992519 | SAMEA9849624 | ERR10376152 | ERZ25462937 |
| 992520 | SAMEA9849626 | ERR10376154 | ERZ25462944 |
| 992521 | SAMEA9849627 | ERR10376153 | ERZ25462950 |
| 992522 | SAMEA9849628 | ERR10376155 | ERZ25462955 |
| 992654 | SAMEA9849857 | ERR10376156 | ERZ25463873 |
| 992656 | SAMEA9849859 | ERR10376158 | ERZ25576549 |
| 992706 | SAMEA9849909 | ERR10376157 | ERZ25464294 |
| 992707 | SAMEA9849910 | ERR10376159 | ERZ25464305 |

None of the 20 unrelated rows establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779773, the study DOI, and S003807171100280X. Both returned 23 lines: own backbone, scope, scientific name, and 20 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. A combined exact organism/accession web query returned no results; that limited search is not evidence of biological absence.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live evidence supports the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRh3(32)/JF779773 identity and its fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRh3(32)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, requested HAL metadata/abstract, and native candidate rows were inspected for this target. Earlier attempts for this study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `bcd7c209ba034e241e1efbe324be3a7afcddc0e5453f332d0745eb3ac5f51c38`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
