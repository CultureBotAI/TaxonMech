# YAML Record Review: Burkholderia sp. BSNF3(20)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsnf3_20.yaml`
- Started UTC: 2026-10-10T07:46:13Z
- Finished UTC: 2026-10-10T07:50:40Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037605`, Burkholderia sp. BSNF3(20). It is a species-ranked bacterial placeholder under `NCBITaxon:2613784`, with `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML must not be hand-edited.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsnf3_20.yaml`: passed.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsnf3_20.yaml --out /private/tmp/taxonmech-bsnf320-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured comparisons passed for identity, full lineage labels/ranks, synonyms, code, attestation, unique index, scope reason, and seed-event wording. This is not corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222820` agrees on ID, label, rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Every root-first lineage label/rank agrees with its individual backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037605&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037605), and all 74 parsed [browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037605) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count; it does not assert zero assemblies. A strain qualifier on a marker is compatible with the species-ranked placeholder, not proof of formal nomenclature or culture deposition.

The full native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32456` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15374` uniquely resolves this ID/slug; `curation/seed_scope.tsv:323035` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, publication, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping sections match those inputs. Zero inventoried strains does not imply no biological isolate.

Exact Nucleotide search `txid1037605[Organism:exp]` returned one UID, 345019040. Complete [GenBank annotation JF779789.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779789.1) explicitly joins organism, strain BSNF3(20), and taxon 1037605. It contains a 450-base 16S rRNA fragment incomplete at both ends, annotated from non-fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `991d19d84ede064befa663b9a76ea19a047f60367010490c237f4dc24a100219`. It is not a genome assembly. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. Complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1), freshly inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The cohort abstract does not establish individual BSNF3(20) assays. Full text and isolate-specific results were not verified; no mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 16 non-target native rows were read completely:

- `data/bvbrc/bvbrc-0025.jsonl.gz:4712` is Klebsiella pneumoniae KP144, taxid 573, BV-BRC 573.95544, SAMN38194382, PRJNA1037605, with CP138841, CP138842, CP138843, and CP138844 but no assembly-accession field. `data/catalog/ncbi_genbank-0050.jsonl.gz:26303` separately names KP144 with the same sample/project and GCA_054693465.1/GCF_054693465.1. The numeric match is BioProject PRJNA1037605; no target identity or genome equivalence is inferred.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:12418` is Salmonella enterica serovar Ohio, taxid 117541/species 28901, strain 1037605, GCA_015710895.1, SAMN16972258, PRJNA248792, AAXMCO000000000.1.
- `data/catalog/ncbi_genbank-0019.jsonl.gz:19112` is Listeria monocytogenes, taxid 1639, isolate Lm-2014-11317, GCA_021037605.1, SAMEA9563554, PRJNA514245, DAFGCO000000000.1. The matching digits occur within the assembly accession.
- `data/catalog/ncbi_genbank-0037.jsonl.gz:25768` is Klebsiella pneumoniae, taxid 573, zj19012, GCA_041037605.1, SAMN37544742, PRJNA1021041, JAZCMU000000000.1. The matching digits again occur within an assembly accession.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:45975` is Acinetobacter baumannii, taxid 470, AB31/isolate 11MC180065516, GCA_050822025.1, SAMN41037605, PRJNA514245, DBJBAX000000000.1. The match is within BioSample. PMID 30286803 in this row and the Listeria row is not a target citation.
- Ten AllTheBacteria r0.2 rows match substrings in run accessions. Complete filter, SeqKit, FASTA, and download fields were read; all have available FASTA and passing assembly/Sylph/HQ filters, but their organism/sample identities are unrelated.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Scientific name | Sample | Run | ENA analysis |
| --- | --- | --- | --- | --- |
| 415733 | Enterobacter asburiae | SAMEA13299050 | ERR10376051 | ERZ25187015 |
| 415755 | Enterobacter hormaechei | SAMEA13299072 | ERR10376050 | ERZ25187230 |
| 992483 | Escherichia coli | SAMEA9849571 | ERR10376052 | ERZ25462707 |
| 992484 | Escherichia coli | SAMEA9849572 | ERR10376054 | ERZ25462712 |
| 992485 | Escherichia coli | SAMEA9849573 | ERR10376053 | ERZ25462720 |
| 992486 | Escherichia coli | SAMEA9849574 | ERR10376055 | ERZ25462723 |
| 992487 | Escherichia coli | SAMEA9849575 | ERR10376056 | ERZ25462729 |
| 992488 | Escherichia coli | SAMEA9849576 | ERR10376057 | ERZ25462738 |
| 992489 | Escherichia coli | SAMEA9849580 | ERR10376058 | ERZ25462744 |
| 992490 | Escherichia coli | SAMEA9849581 | ERR10376059 | ERZ25462749 |

Sylph calls the first two entries Enterobacter cloacae_M and Enterobacter hormaechei_A respectively; the other eight are Escherichia coli in both fields. None of the 16 non-target rows supports another target attestation, synonym, culture deposit, or genome.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered ID, exact slug, organism/designation, and space/punctuation/hyphen variants, bounding the terminal designation number. Expanded search added JF779789, soilbio.2011.07.010, and S003807171100280X. Both searches returned 19 lines: own backbone, scope, scientific name, and the 16 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact target YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism web search yielded taxonomy-tree leads; no snippets supported scientific claims.

Optional blanks do not establish missing required representation, and no causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Inspected pinned and live sources support the taxonomy/name-only assertions. Unavailable article full text and unverified isolate-level assays limit enrichment research without contradicting those assertions.

## Recommended Edits

None required. Preserve exact BSNF3(20)/JF779789 identity and non-fertilized context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the primary article and isolate-level table and inspect BSNF3(20)-specific conditions/results. Require an explicit source chain for future deposit/genome links. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Review-status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, and all candidate native rows were inspected for this target. Shared HAL metadata and abstract were inspected earlier this turn. Previous attempts for the same study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried per isolate. No login, payment, or full-text reading occurred.

YAML SHA-256: `64e8dd7d674955648a11b89149667ead53041e685bf344b4ebb87bc08b20a2b5`. Only this new report was written for the target. Maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and existing worktrees were unchanged.
