# YAML Record Review: Burkholderia sp. BSNF2(8)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsnf2_8.yaml`
- Started UTC: 2026-10-10T07:35:05Z
- Finished UTC: 2026-10-10T07:37:55Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037603`, Burkholderia sp. BSNF2(8). It is a species-ranked bacterial placeholder under `NCBITaxon:2613784`, with `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML must not be hand-edited.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsnf2_8.yaml`: passed.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsnf2_8.yaml --out /private/tmp/taxonmech-bsnf28-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured comparisons passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique index, scope reason, and seed-event wording. This is not corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222818` agrees on ID, label, rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Each root-first lineage label/rank matches its individual backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Full live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037603&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037603), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037603) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count; it does not assert zero assemblies. A strain qualifier on a marker is compatible with the species-ranked placeholder, not proof of formal nomenclature or a culture deposit.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32454` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15372` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323033` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event.

## Evidence

One NCBI `NAME` is counted, not a strain, genome, paper, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping sections match those inputs. Zero inventoried strains does not imply no biological isolate.

Exact Nucleotide search `txid1037603[Organism:exp]` returned one UID, 345019043. Complete [GenBank annotation JF779792.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779792.1) joins the exact organism, strain BSNF2(8), and taxon 1037603. It is a 450-base 16S rRNA fragment incomplete at both ends, annotated from non-fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `20a8510a516ac790f85b268f27cdadea24e1c9a5b37cc522cd6e94b7e459c376`. It is not a genome assembly. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. Complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1), freshly inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The cohort abstract does not establish individual BSNF2(8) assay results. Full text and isolate-specific results were not verified; no mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 19 non-target native rows were read completely:

- Four rows describe Shigella flexneri H103760371, not BSNF2(8): `data/bvbrc/bvbrc-0025.jsonl.gz:45389`, `data/gold/organisms.jsonl.gz:317724`, `data/gold/projects.jsonl.gz:230538`, and `data/gold/analyses.jsonl.gz:184859`. BV-BRC 623.790/taxid 623 carries GCA_900485835.1, UDTG00000000, SAMEA3710468, and PRJEB12097. GOLD Go0462885 is the strain organism; Gp0336161 explicitly links that organism and sample/project; Ga0319497 links Gp0336161 and GCA_900485835.1/UDTG00000000, with its direct organism and IMG fields empty. GOLD IDs are related source records, not genome identifiers. The numeric match is within strain H103760371; this explicit non-target chain supplies no target genome or deposit link.
- `data/catalog/gtdb_genomes-0005.jsonl.gz:23370` and `data/catalog/ncbi_genbank-0058.jsonl.gz:14042` describe freshwater MAG GCA_903896125.1, uncultured Actinomycetes bacterium/taxid 152507, isolate MJ120620A_bin-411, SAMEA6945781, PRJEB38681, CAITWP000000000.1. GTDB assigns PALSA-747 sp903897155. The match is total/ungapped length 1,037,603.
- `data/catalog/gtdb_genomes-0017.jsonl.gz:44319` and `data/catalog/ncbi_genbank-0035.jsonl.gz:48905` describe MAG GCA_038887315.1, Desulfurococcaceae archaeon/taxid 2184738, isolate SRBZ-1_201907_bins_9, SAMN36038145, PRJNA544494, JAWAKV000000000.1. GTDB assigns UBA285 sp038816475. Total length is 1,037,803, with the numeric match at ungapped length 1,037,603. PMID 38744885 is not a target citation.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41510` is Acinetobacter baumannii, taxid 470, AB29/isolate 10UC190075361, GCA_050715215.1, SAMN41037603, PRJNA514245, DBIYRF000000000.1. The numeric match is within BioSample; PMID 30286803 is not a target citation.
- Ten AllTheBacteria r0.2 rows match substrings within run accessions, as detailed below. Full native rows include available FASTA, passing assembly/Sylph/HQ filters, SeqKit sums, and download URLs. These do not override their unrelated organism/sample identities.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Scientific name | Sample | Run | ENA analysis |
| --- | --- | --- | --- | --- |
| 415736 | Enterobacter hormaechei | SAMEA13299053 | ERR10376030 | ERZ25187046 |
| 415738 | Enterobacter hormaechei | SAMEA13299055 | ERR10376032 | ERZ25187062 |
| 415739 | Enterobacter hormaechei | SAMEA13299056 | ERR10376031 | ERZ25187069 |
| 415740 | Enterobacter cloacae | SAMEA13299057 | ERR10376033 | ERZ25187082 |
| 415741 | Enterobacter cloacae | SAMEA13299058 | ERR10376034 | ERZ25187092 |
| 415742 | Enterobacter hormaechei | SAMEA13299059 | ERR10376039 | ERZ25187102 |
| 415743 | Klebsiella pneumoniae | SAMEA13299060 | ERR10376038 | ERZ25187111 |
| 415744 | Enterobacter hormaechei | SAMEA13299061 | ERR10376035 | ERZ25187120 |
| 415751 | Enterobacter hormaechei | SAMEA13299068 | ERR10376037 | ERZ25187188 |
| 417493 | Enterobacter kobei | SAMEA13410807 | ERR10376036 | ERZ25193719 |

Sylph names the E. hormaechei entries Enterobacter hormaechei_A; its other species labels agree with those rows' scientific names. None of the 19 non-target matches establishes an additional target attestation, synonym, deposit, or genome.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered ID, exact slug, organism/designation, and space/punctuation/hyphen variants, bounding the terminal designation number. The expanded pass added JF779792, soilbio.2011.07.010, and S003807171100280X. Both returned 22 lines: own backbone, scope, scientific name, and the 19 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact target YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism/designation web searches yielded taxonomy-tree leads; no snippets supported scientific claims.

Optional blanks do not establish missing required representation, and no causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the taxonomy/name-only assertions. Unavailable full text and unverified isolate assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve exact BSNF2(8)/JF779792 identity and explicitly non-fertilized context in later enrichment; keep partial markers outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the primary article and isolate-level table and inspect BSNF2(8)-specific conditions/results. Require an explicit deposit/genome source chain for future links. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Review-status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, and candidate native rows were inspected for this target. Shared HAL metadata and abstract were inspected earlier this turn. Previous attempts for the same study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried per isolate. No login, payment, or full-text reading occurred.

YAML SHA-256: `4ed987c2429d94c6fb1680c6f14cc58db7504639dc6a2dbdc34154bdaf9a6438`. Only this new report was written for the target. Maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and existing worktrees were unchanged.
