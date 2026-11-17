# YAML Record Review: Burkholderia sp. MRh3(19)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrh3_19.yaml`
- Started UTC: 2026-10-10T19:40:47Z
- Finished UTC: 2026-10-10T19:43:01Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for Burkholderia sp. MRh3(19), `NCBITaxon:1037614`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrh3_19.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrh3_19.yaml --out /private/tmp/taxonmech-mrh319-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured checks passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They do not prove full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222829` agrees on ID, label, rank, parent, genetic code, and snapshot 2026-09-13. Exact/related/broad synonym and retirement fields are empty. Each root-first lineage label/rank matches its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037614&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037614), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037614) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding identifies this NCBI placeholder, not formal nomenclatural standing or a culture-deposit identity.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32465` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15384` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323044` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The single attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037614[Organism:exp]` returned one UID, 345019023. Complete [GenBank annotation JF779772.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779772.1) explicitly joins organism, strain MRh3(19), and taxon 1037614. This 450-base 16S rRNA marker is partial at both ends and annotated from fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `ee7bfabe8973f45aaf161854bc9ddc0bcb7587045517c23abb7a8a3d73fa8e00`. It is not a genome assembly or deposit accession. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1), inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Cohort-level findings do not establish individual MRh3(19) assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 21 non-target native search matches were read completely:

- Five `data/bvbrc/bvbrc-0024.jsonl.gz` rows describe Escherichia coli VCSW5, taxid 562, GCA_019890835.1, SAMN21037614, PRJNA758822, and CP082355/CP082356. Row 2680 is complete, BV-BRC 562.79113. Rows 3499, 4708, 6197, and 8476 are deprecated, respectively 562.80357, 562.85828, 562.87782, and 562.90635. All match the BioSample substring, not the target taxon ID.
- `data/catalog/gtdb_genomes-0010.jsonl.gz:14171`, `data/catalog/ncbi_genbank-0018.jsonl.gz:14155`, and `data/catalog/ncbi_refseq-0003.jsonl.gz:39811` also describe E. coli VCSW5, taxid 562, GCA_019890835.1/GCF_019890835.1, and SAMN21037614. GenBank/BV-BRC supply PRJNA758822, whereas GTDB/RefSeq supply PRJNA224116. These source project distinctions are preserved. GTDB reports soil/drain sediment in Hong Kong, not target collection metadata. The paired GenBank/RefSeq records report identical assemblies, but a shared BioSample alone does not equate every source assembly.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:12331` describes E. coli, taxid 562, strain 1037614, GCA_015708335.1, SAMN16961357, PRJNA315192, and AAXMBS000000000.1. A bare numeric strain designation is not this NCBI taxonomy identifier.
- `data/catalog/ncbi_genbank-0054.jsonl.gz:42186` describes Acinetobacter baumannii, taxid 470, strain AB41/isolate 10MC190005274, GCA_059223675.1, SAMN41037614, PRJNA514245, and DBPSPB000000000.1. Its match is within BioSample; PMID 30286803 is not a target citation. This row and the numeric E. coli strain row are excluded from RefSeq as part of a large multi-isolate project.
- Eleven AllTheBacteria rows have scientific name E. coli, r0.2 dataset, available FASTA, and passing assembly filters. Ten match run-accession substrings; row 2134589 instead matches SAMN21037614 and names SRR21680730/ERZ26004369. Ten rows have E. coli Sylph labels and passing Sylph/HQ filters. Row 992704 has unknown Sylph species, SYLPH_RESULTS_FAIL, and HQ failures CHECKM2_MAX_CONTAM,SYLPH_RESULTS_FAIL. Its available FASTA is preserved, not silently treated as unavailable.

Complete dataset, filter, SeqKit, and download fields were inspected for all 11 AllTheBacteria rows:

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992515 | SAMEA9849619 | ERR10376149 | ERZ25462907 |
| 992517 | SAMEA9849621 | ERR10376148 | ERZ25462916 |
| 992650 | SAMEA9849853 | ERR10376142 | ERZ25463855 |
| 992651 | SAMEA9849854 | ERR10376140 | ERZ25463862 |
| 992652 | SAMEA9849855 | ERR10376146 | ERZ25576521 |
| 992653 | SAMEA9849856 | ERR10376144 | ERZ25576531 |
| 992702 | SAMEA9849905 | ERR10376141 | ERZ25464261 |
| 992703 | SAMEA9849906 | ERR10376145 | ERZ25464268 |
| 992704 | SAMEA9849907 | ERR10376147 | ERZ25464276 |
| 992705 | SAMEA9849908 | ERR10376143 | ERZ25464285 |
| 2134589 | SAMN21037614 | SRR21680730 | ERZ26004369 |

None of the 21 unrelated rows establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, and assembly identifiers remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779772, the study DOI, and S003807171100280X. Both returned 24 lines: own backbone, scope, scientific name, and 21 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. A combined exact organism/accession web query returned no results; that limited query is not evidence of biological absence.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRh3(19)/JF779772 identity and the fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRh3(19)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input changes, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, and native candidate rows were inspected for this target. The shared study's requested HAL metadata/abstract were read earlier this turn. Earlier attempts for this study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `651579fc20d5f88ddea34a86cb0b05b0377973f1b5cd4bba829aa0ff626568b2`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
