# YAML Record Review: Burkholderia sp. BSNF2(4)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsnf2_4.yaml`
- Started UTC: 2026-10-10T07:32:00Z
- Finished UTC: 2026-10-10T07:34:05Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord` for `NCBITaxon:1037602`, Burkholderia sp. BSNF2(4). It is a species-ranked bacterial placeholder under `NCBITaxon:2613784`, with `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes; generated YAML must not be hand-edited.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsnf2_4.yaml`: passed.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsnf2_4.yaml --out /private/tmp/taxonmech-bsnf24-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured comparisons passed for identifier/label, full lineage labels/ranks, synonyms, code, attestation, unique ID/slug, scope reason, and seed-event wording. This is not corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222817` agrees on ID, exact label, rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Every root-first lineage label/rank agrees with its individual backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Full live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037602&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037602), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037602) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count; this is not a zero-assembly assertion. The marker's strain qualifier is compatible with the species-ranked placeholder, not proof of formal nomenclature or a culture deposit.

The full native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32453` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15371` uniquely resolves the target; `curation/seed_scope.tsv:323032` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, paper, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping sections match those inputs. Zero inventoried strains does not imply no biological isolate.

Exact Nucleotide search `txid1037602[Organism:exp]` returned one UID, 345019044. Complete [GenBank annotation JF779793.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779793.1) explicitly joins organism, strain BSNF2(4), and taxon 1037602. Its 450-base 16S rRNA fragment is incomplete at both ends and annotated from non-fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `a69e31bdbf49d315fa067c2bcb325f50d6f21e322cd2e049eb9ce0a8eb5ed8b0`. It is not a genome assembly. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. Complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1), freshly inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The abstract does not establish individual BSNF2(4) assays. Full text and isolate-specific results were not verified; no weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 11 non-target native rows were read completely:

- `data/bvbrc/bvbrc-0018.jsonl.gz:45805`, `data/catalog/gtdb_genomes-0012.jsonl.gz:4477`, and `data/catalog/ncbi_genbank-0031.jsonl.gz:44520` concern GCA_034197955.1, NCBI Buttiauxella sp. HR94/taxid 3094841, SAMN38194334, BV-BRC 3094841.3, CP139140. The match is BioProject PRJNA1037602. GTDB places this assembly in Pseudescherichia sp002298805; GenBank excludes it from RefSeq for unverified source organism. Those non-target classification details do not establish a link or conflict for BSNF2(4).
- `data/catalog/ncbi_genbank-0009.jsonl.gz:7611` is Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 14T0008, GCA_010376025.1, SAMN12576338, PRJNA560345, JAAGIJ000000000.1. The match is assembly name ASM1037602v1.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41490` is Acinetobacter baumannii, taxid 470, AB28/isolate 10UC190068996, GCA_050714815.1, SAMN41037602, PRJNA514245, DBIYQT000000000.1. The match is within BioSample; PMID 30286803 is not a target citation.
- Five AllTheBacteria r0.2 rows are Enterobacter hormaechei, Sylph species Enterobacter hormaechei_A, with matches inside run accessions. Complete filter, SeqKit, FASTA, and download fields were read. Their individual links are listed below.
- `data/catalog/allthebacteria.tsv.xz:1050131` is Salmonella enterica serovar Montevideo, Sylph species Salmonella enterica, sample SAMN02844326, run SRR1773005, ENA analysis ERZ4037611, dataset 661k. The match is inside SeqKit sum `seqkit.v0.1_DLS_k0_8c014f41037602bc411061c8d62b922e`, not a taxon identifier or MD5 assertion.

| AllTheBacteria physical row | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| `data/catalog/allthebacteria.tsv.xz:415731` | SAMEA13299048 | ERR10376025 | ERZ25186998 |
| `data/catalog/allthebacteria.tsv.xz:415732` | SAMEA13299049 | ERR10376026 | ERZ25187007 |
| `data/catalog/allthebacteria.tsv.xz:415734` | SAMEA13299051 | ERR10376027 | ERZ25187029 |
| `data/catalog/allthebacteria.tsv.xz:415735` | SAMEA13299052 | ERR10376028 | ERZ25187037 |
| `data/catalog/allthebacteria.tsv.xz:415737` | SAMEA13299054 | ERR10376029 | ERZ25187052 |

All six ATB rows have available FASTA and passing assembly/Sylph/HQ filters, but source identity remains unrelated. None of these 11 matches supports a target genome, deposit, synonym, or additional attestation.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered ID, exact slug, organism/designation, and punctuation/space/hyphen variants, bounding the final designation number. Expanded search added JF779793, soilbio.2011.07.010, and S003807171100280X. Both passes returned 14 lines: own backbone, scope, scientific name, and the 11 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact target YAML and no pre-existing report/history filename for it. Eukaryota contents were not opened. Exact organism/designation web searches yielded taxonomy-tree leads; no snippets supported scientific claims.

Optional blanks are not missing required representation, and no causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the recorded taxonomy/name assertions. Unavailable article full text and unverified isolate-level assays limit enrichment research without contradicting those assertions.

## Recommended Edits

None required. Preserve exact BSNF2(4)/JF779793 identity and non-fertilized context during later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the primary article and isolate-level table and verify BSNF2(4)-specific assay conditions/results. Require an explicit source chain for any deposit/genome association. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Review-status promotion requires separate human sign-off.

## Additional Notes

Full taxonomy responses, browser text, sequence annotation, and candidate native rows were inspected for this target. Shared HAL metadata and abstract were inspected earlier this turn. Previous access attempts for the same study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried per isolate. No login, payment, or full-text reading occurred.

YAML SHA-256: `07cbbb009ce91624106c29fbe1e322783f9375ab7b062a8486d557d8ac8cfcee`. Only this new report was written for the target. Maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and existing worktrees were unchanged.
