# YAML Record Review: Thalassobacillus sp. YIM 94206

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/thalassobacillus_sp_yim_94206.yaml`
- Started UTC: 2026-10-06T09:35:05Z
- Finished UTC: 2026-10-06T09:37:20Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord`, `NCBITaxon:1035050`, Thalassobacillus sp. YIM 94206. It asserts species rank, bacterial domain, parent `NCBITaxon:2621135`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero imported strains, one NCBI name attestation and one inline seed event. Optional synonyms, nomenclature, taxonomy mappings, strain listings, genome associations, evidence objects, causal graph and discussion are not asserted. This is an individual review, not a curation or lifecycle change.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/thalassobacillus_sp_yim_94206.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/thalassobacillus_sp_yim_94206.yaml --out /private/tmp/thbyim94206-validation.tsv`: exit 0, one file, zero errors; read the header-only diagnostic TSV.
- Structured comparisons verified the entire source lineage, identity, genetic code, unique PATHS/scope rows, name attestation and inline event wording. Exact scans of `ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Before writing this report, an identifier/name/slug search with `rg --no-ignore --hidden` found no prior report or separate history artifact in `reports/yaml_record_review/` and `history/`. The existing inline seed event is schema-valid. No new curation event is authorized.
- Not checked: full-corpus `just qc`, `just verify-corpus`, `just validate-all`, `just test`, `just validate-history`, site drift and publication gates. The focused checks are not proof of complete reproduction or release readiness. No focused term/reference/history validator was invented. `just validate-products` is inapplicable without curator-added graph nodes.

## Identity and Grounding

The backbone `data/raw/ncbitaxon_taxa.tsv:221861`, native scientific name `data/catalog/ncbi_names-0005.jsonl.gz:31287`, index `data/taxa/PATHS.tsv:14342` and scope `curation/seed_scope.tsv:322153` agree on this identity. The pinned backbone has no target synonyms, replacement or children.

Read complete live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035050&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035050). They confirm the name, species rank, bacterial placement, parent unclassified Thalassobacillus (`2621135`) and genetic code 11. All stored ancestors agree: root (`1`), cellular organisms (`131567`), Bacteria (`2`), Bacillati (`1783272`), Bacillota (`1239`), Bacilli (`91061`), Caryophanales (`1385`), Bacillaceae (`186817`), Thalassobacillus (`331971`) and unclassified Thalassobacillus (`2621135`). Datasets includes root; EFetch supplies the remaining ancestor labels and ranks. Exact identifier grounding does not imply valid publication of a formally named species.

## Evidence

The single NCBITAXON attestation correctly counts one imported `NAME` from the `2026-09-13` snapshot. The `2026-09-13T17:54:04Z` event matches the maintained scope reason and sole attesting source. Imported source counts do not measure biological abundance or prove strain absence.

Exact non-expanded NCBI searches for `txid1035050[Organism:noexp]` returned zero Assembly records and one Nuccore UID, `333798082`, with all returned IDs accounted for. Read the complete references, qualifiers and feature metadata, excluding sequence bases, for [JF792156.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792156.1). It is a 691-base partial 16S rRNA marker, partial at both ends, explicitly naming strain YIM 94206 and `taxon:1035050`. Its source supplies no culture-collection, BioSample or assembly cross-reference. It was created 28 May 2011, updated 26 August 2015, and submitted by C. Chen on 7 April 2011 from Yunnan Institute of Microbiology.

The accompanying Qijiaojing Lake study is marked unpublished, without a PMID or DOI. The marker supports its submitted identity only, not a whole genome, deposit equivalence, type status, enzyme phenotype or habitat assertion. None of these broader claims is asserted in the YAML. iModulonDB is inapplicable: this identity-only record contains no gene, regulator or transcriptomics claims.

## Completeness

Exact comparisons found no target entries in the imported BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventories. Together with the broader candidate inspection and lack of classified children, the zero imported strain count is consistent with source coverage. It does not imply that the sequenced isolate never existed.

The bounded candidate search used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. Terms included the taxon number, full designation, slug and separator variants of YIM 94206; a second search added `JF792156`. Compressed sources and ignored files were included. Only `SOURCE.json` provenance sidecars were excluded from this candidate-data search; unrelated directories and external unindexed sources are outside the claimed exhaustive scope.

Both searches returned the same 28 candidate rows. Every complete row was read with header-aware TSV or native JSON parsing, and address reconciliation found no unread or extra rows. Three are the target's backbone, native name and scope; 25 are unrelated substring hits detailed below. No supported missing culture deposit or eligible genome association was found. Optional nomenclature, mapping and mechanism fields may remain empty. A partial rRNA sequence is not a missing genome.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record's bounded assertions agree with maintained inputs and inspected primary authority. The search candidates do not justify new associations or changes to its identity.

## Recommended Edits

None required. Do not hand-edit generated YAML or promote `SEEDED` because of this report. A later verified source association should enter maintained acquisition/harmonization inputs and `src/taxonmech/seed.py` with a focused regression test; scope is owned by `curation/seed_scope.tsv`. Taxonomy classification changes belong upstream, not in a hand-edited lineage. Do not use numeric substrings or a marker alone to infer deposit/genome links.

## Follow-up Checks

No blocking follow-up. At a future refresh, recheck exact taxonomy and marker identity, requiring an explicit deposit-to-sequence chain before adding strain/genome associations. After an actual curation change, rerun the focused validators and the documented reproduction, history, tests and publication gates. The current report does not certify those skipped gates.

## Additional Notes

The NCBI taxonomy browser could not be opened by the web tool, but complete official EFetch and Datasets responses succeeded. The full-name web search supplied secondary taxonomy summaries only; the marker query returned no results. No search snippet or absence of web results was treated as biological or global literature evidence.

Complete-row dispositions of 15 unrelated bacterial source candidates:

| Source rows | Inspected identity and exclusion |
| --- | --- |
| `data/bvbrc/bvbrc-0001.jsonl.gz:18530`; `data/catalog/ncbi_genbank-0000.jsonl.gz:45870`; `data/catalog/ncbi_refseq-0000.jsonl.gz:38649`; `data/catalog/gtdb_genomes-0014.jsonl.gz:31718`; `data/gold/projects.jsonl.gz:87453`; `data/catalog/allthebacteria.tsv.xz:66030` | Six rows concern Staphylococcus haemolyticus 97208, taxon 1283, sample `SAMEA1035050`, explicitly paired `GCA_001238665.1`/`GCF_001238665.1`, BV-BRC `1283.195`, GOLD `Gp0140511`/`Go0134628`, and ATB `ERR085290`/`ERZ3070483`. GenBank/BV-BRC/GOLD retain study `PRJEB2705`; RefSeq/GTDB use umbrella `PRJNA224116`. The match is a sample ID, not this taxon. |
| `data/catalog/ncbi_genbank-0037.jsonl.gz:21045`; `data/bvbrc/bvbrc-0027.jsonl.gz:21482`; `data/catalog/ncbi_refseq-0006.jsonl.gz:20155`; `data/catalog/gtdb_genomes-0001.jsonl.gz:13719` | Four rows concern Bacteroides thetaiotaomicron, taxon 818, strain `RTP21277st1_D5_RTP21277_210401`, sample `SAMN41035050`, paired `GCA_040928825.1`/`GCF_040928825.1`, BV-BRC `818.3296`. GenBank/BV-BRC carry `PRJNA1093465`; RefSeq/GTDB retain `PRJNA224116`. No target/YIM match. |
| `data/bvbrc/bvbrc-0006.jsonl.gz:8497`; `data/catalog/allthebacteria.tsv.xz:569520` | Mycobacterium tuberculosis run/designation `ERR1035050`, BV-BRC `1773.20483`, ATB sample `SAMEA3558583` and analysis `ERZ3501757`. Run-number substring only. |
| `data/catalog/ncbi_genbank-0009.jsonl.gz:6361` | Campylobacter jejuni 279504, taxon 197, `GCA_010350505.1`, `SAMN13326926`, `PRJNA505131`. No RefSeq partner; the source excludes it as a large multi-isolate project. Assembly-number substring only. |
| `data/catalog/ncbi_genbank-0042.jsonl.gz:41461` | Legionella pneumophila serogroup 1, taxon 66976/species 446, strain `CNR-L_210350504`, `GCA_046490015.1`, `SAMN38117038`, `PRJNA1036154`. No RefSeq partner, large multi-isolate project exclusion. Strain-number substring only. |
| `data/catalog/allthebacteria.tsv.xz:1813125` | Salmonella enterica, sample `SAMN14486361`, run `SRR11449236`, analysis `ERZ25742371`. The numeric match is inside the SeqKit sum `seqkit.v0.1_DLS_k0_85a3ffe559a861b0110350507d1718c7`, not a taxon or deposit. |

All three ATB rows retain available FASTAs and passing pipeline, HQ and Sylph filters. Their complete checksum and download-location fields were inspected, not downloaded or recomputed. SeqKit sum is not MD5. Availability cannot override an unrelated identity; shared samples alone were not used to infer genome equivalence.

The remaining ten candidates are distinct GOLD plant/fungal metatranscriptome projects at Duke University, North Carolina, United States. All have empty GOLD organism IDs; their sample numbers contain the search digits but establish no association to this bacterium. Every full row was read:

| `data/gold/projects.jsonl.gz` line | GOLD project | BioProject | BioSample | Source title context/suffix |
| --- | --- | --- | --- | --- |
| 226819 | `Gp0331579` | `PRJNA502121` | `SAMN10350509` | Pinus contorta roots inoculated with Suillus; DOB170(NC)xP.contorta(WY)_rep1 |
| 226821 | `Gp0331581` | `PRJNA502123` | `SAMN10350508` | Pinus contorta/Suillus; DOB170(NC)xP.contorta(WY)_rep3 |
| 226822 | `Gp0331582` | `PRJNA502124` | `SAMN10350507` | Pinus taeda/Suillus; DOB170(NC)xP.taeda(GA)_rep1 |
| 226828 | `Gp0331588` | `PRJNA502130` | `SAMN10350506` | Pinus banksiana/Suillus; DOB147(NC)xP.bank(MN)_rep1 |
| 226831 | `Gp0331591` | `PRJNA502133` | `SAMN10350505` | Pinus contorta/Suillus; DOB147(NC)xP.contorta(CO)_rep1 |
| 226835 | `Gp0331595` | `PRJNA502137` | `SAMN10350504` | Pinus contorta/Suillus; DOB147(NC)xP.contorta(CA)_rep2 |
| 226840 | `Gp0331600` | `PRJNA502142` | `SAMN10350503` | Pinus taeda/Suillus; DOB147(NC)xP.taeda(GA)_rep1 |
| 226841 | `Gp0331601` | `PRJNA502143` | `SAMN10350502` | Pinus taeda/Suillus; DOB147(NC)xP.taeda(GA)_rep2 |
| 226843 | `Gp0331603` | `PRJNA502145` | `SAMN10350501` | Pinus taeda/Suillus; DOB147(NC)xP.taeda(LA)_rep1 |
| 226848 | `Gp0331608` | `PRJNA502150` | `SAMN10350500` | Pinus banksiana roots; Pbank(MN)_control_rep3 |

These exclusions are review diagnostics, not new curated associations. Only this report is written; records, sources, curation history, generated products and completed Eukaryota reviews remain untouched.
