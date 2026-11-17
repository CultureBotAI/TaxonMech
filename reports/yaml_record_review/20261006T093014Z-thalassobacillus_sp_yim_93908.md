# YAML Record Review: Thalassobacillus sp. YIM 93908

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/thalassobacillus_sp_yim_93908.yaml`
- Started UTC: 2026-10-06T09:26:39Z
- Finished UTC: 2026-10-06T09:30:14Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1035048`, Thalassobacillus sp. YIM 93908. It carries species rank, bacterial domain, ten root-first ancestors, parent `NCBITaxon:2621135`, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero imported strains, one NCBI name attestation and one seed event. No optional synonyms, nomenclature, mappings, strain list, genome links, causal graph, evidence objects or discussions are asserted. This review does not change the record or its lifecycle status.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/thalassobacillus_sp_yim_93908.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/thalassobacillus_sp_yim_93908.yaml --out /private/tmp/thbyim93908-validation.tsv`: exit 0, one file scanned, zero errors; read the header-only diagnostic TSV.
- Read the complete target and source candidates. Structured comparisons verified the full source lineage, identity, genetic code, sole attestation, unique PATHS/scope entries and inline event wording. Exact type-material, merged-ID and dropped-record scans returned no target rows.
- An ignored-inclusive identifier/name/slug search of `reports/yaml_record_review/` and `history/` returned no prior report or separate history artifact. The inline seed event is present and schema-valid. No review event or status promotion is authorized.
- Not checked: full-corpus `just qc`, `just verify-corpus`, `just validate-all`, `just test`, `just validate-history`, site drift and other publication gates. This is a focused review, not a release certification or proof of whole-corpus reproduction. No focused term/reference/history validator was invented. `just validate-products` is inapplicable because there are no curator-added graph nodes.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:221859`, native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31285`, `data/taxa/PATHS.tsv:14339` and `curation/seed_scope.tsv:322151` agree on this identifier and designation. The backbone has no synonyms, replacement or child rows for the target.

Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035048&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035048) were read in full. They confirm species rank, bacterial placement, genetic code 11 and parent unclassified Thalassobacillus (`2621135`). The complete chain agrees: root (`1`), cellular organisms (`131567`), Bacteria (`2`), Bacillati (`1783272`), Bacillota (`1239`), Bacilli (`91061`), Caryophanales (`1385`), Bacillaceae (`186817`), Thalassobacillus (`331971`), unclassified Thalassobacillus (`2621135`). Datasets supplies root; EFetch supplies the named/ranked remaining ancestors. `EXACT` denotes the matching NCBI identifier, not formal nomenclatural recognition of a named species.

## Evidence

The NCBI attestation correctly counts one imported `NAME` from snapshot `2026-09-13`. The `2026-09-13T17:54:04Z` seed event matches the maintained scope reason and lists only NCBITAXON as an attesting source. Source counts are imported coverage, not biological abundance or evidence of absence.

An exact, non-expanded NCBI search, `txid1035048[Organism:noexp]`, returned zero Assembly records and one Nuccore record, UID `333798038`. All returned IDs were accounted for. Read its complete GenBank metadata, references and features, excluding sequence bases: [JF792112.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792112.1) is a 660-base partial 16S rRNA sequence with both ends marked partial, explicitly naming strain YIM 93908 and `taxon:1035048`. Creation is 28 May 2011; update is 26 August 2015. C. Chen submitted it on 7 April 2011 from Yunnan Institute of Microbiology. The accompanying Qijiaojing Lake study is listed as unpublished, without PMID or DOI. There is no culture-collection, BioSample or assembly cross-reference in its source qualifiers.

This supports the identity of the submitted marker only. It does not establish a whole-genome assembly, deposit equivalence, type status, enzyme phenotype or a habitat assertion for the generated record. No such claim is made in the YAML. iModulonDB is not applicable to this identity-only record; there are no gene, regulatory or transcriptomic claims to evaluate.

## Completeness

Exact structured comparisons found no target entries in the imported BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventories. Together with the broader searches below and lack of classified children, the zero imported strain count is consistent with the available source evidence. It does not imply that the sequenced isolate never existed or that no future source can connect it to a deposit.

The gitignore-independent search used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. It included compressed data, the numeric taxon ID, full name, slug and separator variants of YIM 93908, then expanded to `JF792112`. Only `SOURCE.json` provenance sidecars were excluded from this candidate-data search; unrelated repository directories and external unindexed sources were not claimed to have been exhaustively searched.

Both searches returned the same 28 candidate rows, all read completely with header-aware TSV or native JSON parsers. Address reconciliation found no unread or extra rows. Three rows concern the target: backbone, native scientific name and scope. The other 25 are unrelated substring matches, resolved individually below. No supported missing deposit or eligible genome linkage was identified. Optional nomenclature, mapping and mechanism fields may remain empty; the marker is not a missing genome.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record's bounded identity and provenance claims agree with its maintained inventories and the inspected primary authority. The evidence does not justify transferring any unrelated source candidate into this record.

## Recommended Edits

None required. Do not hand-edit this generated YAML, attach a genome inferred from a partial rRNA marker, or promote `SEEDED` as a consequence of this report. A later verified identity/deposit change belongs in the maintained source acquisition or harmonization inputs and `src/taxonmech/seed.py` with a focused regression test; a scope change belongs in `curation/seed_scope.tsv`. NCBI classification changes belong upstream, not in a hand-curated lineage.

## Follow-up Checks

No blocking follow-up. On a future source refresh, recheck the exact taxonomy and marker, requiring an explicit source chain before adding a culture deposit or genome. Then rerun the two focused validators and, for any actual curation/release change, the documented corpus reproduction, history, test and publication gates. Do not manufacture missing nomenclature or phenotype claims from the unpublished study title.

## Additional Notes

The direct NCBI taxonomy browser page failed in the web tool; both official structured taxonomy endpoints succeeded. Web queries for the full designation and marker yielded no additional usable primary evidence. Secondary taxonomy summaries and unrelated search results were not used to establish a finding. This bounded search is not proof of global literature absence.

Complete-row dispositions for the 25 unrelated candidates:

| Source rows | Inspected identity and exclusion |
| --- | --- |
| `data/bvbrc/bvbrc-0001.jsonl.gz:18442`; `data/catalog/ncbi_genbank-0000.jsonl.gz:45821`; `data/catalog/ncbi_refseq-0000.jsonl.gz:38603`; `data/catalog/gtdb_genomes-0014.jsonl.gz:23886`; `data/gold/projects.jsonl.gz:87397`; `data/catalog/allthebacteria.tsv.xz:66028` | Six records concern Staphylococcus haemolyticus 51-30, taxon 1283, sample `SAMEA1035048`, explicit paired assemblies `GCA_001237685.1`/`GCF_001237685.1`, BV-BRC `1283.186`, GOLD `Gp0140455`/`Go0134572`, and ATB run `ERR085194`/analysis `ERZ3070488`. GenBank/BV-BRC/GOLD retain study `PRJEB2705`; RefSeq/GTDB use umbrella `PRJNA224116`. The numeric match is inside a sample ID, not the target taxon. |
| `data/bvbrc/bvbrc-0027.jsonl.gz:21484`; `data/catalog/ncbi_genbank-0037.jsonl.gz:21047`; `data/catalog/ncbi_refseq-0006.jsonl.gz:20157`; `data/catalog/gtdb_genomes-0010.jsonl.gz:11697` | Four records concern Bacteroides thetaiotaomicron, taxon 818, strain `RTP21198st1_F9_RTP21198_201120`, sample `SAMN41035048`, paired `GCA_040928865.1`/`GCF_040928865.1`, BV-BRC `818.3298`. GenBank/BV-BRC use `PRJNA1093465`; RefSeq/GTDB retain `PRJNA224116`. No YIM designation or target taxon. |
| `data/bvbrc/bvbrc-0006.jsonl.gz:8495`; `data/catalog/allthebacteria.tsv.xz:569518` | Mycobacterium tuberculosis run/designation `ERR1035048`, BV-BRC `1773.20481`, ATB sample `SAMEA3558581`, analysis `ERZ3501758`; not the target isolate. |
| `data/catalog/ncbi_genbank-0009.jsonl.gz:6360` | Campylobacter jejuni, taxon 197, strain `PNUSAC013754`, `GCA_010350485.1`, sample `SAMN13391873`, project `PRJNA239251`. No RefSeq partner; exclusion is the source's large multi-isolate project designation. Assembly-number substring only. |
| `data/catalog/allthebacteria.tsv.xz:1611071` | Klebsiella pneumoniae, `SRR10350483`, `SAMN11919597`, `ERZ25758474`; run-number substring only. |
| `data/catalog/allthebacteria.tsv.xz:1611073` | Klebsiella pneumoniae, `SRR10350484`, `SAMN11927580`, `ERZ25758476`; distinct complete source row, also unrelated. |

All four ATB candidates retain available FASTA flags and passing pipeline, HQ and Sylph filters. Those properties cannot override their unrelated identities. Their full rows include SeqKit sums and supplied OSF/AWS locations; these were inspected, not downloaded or recomputed. SeqKit sum is not MD5, and no cross-source genome equivalence was inferred from a shared sample alone.

The remaining ten candidates are separate GOLD plant/fungal metatranscriptome project rows. Each has an empty GOLD organism field, and its full title identifies Pinaceae seedlings inoculated with Suillus ectomycorrhiza. Sample-number substrings do not connect any project to this bacterial record:

| `data/gold/projects.jsonl.gz` line | GOLD project | BioProject | BioSample | Source locality and title suffix |
| --- | --- | --- | --- | --- |
| 228179 | `Gp0333784` | `PRJNA502025` | `SAMN10350489` | Pennsylvania, United States; Same/Llari_rep2 |
| 228180 | `Gp0333785` | `PRJNA502026` | `SAMN10350488` | Pennsylvania, United States; Same/Llari_rep3 |
| 228183 | `Gp0333788` | `PRJNA502029` | `SAMN10350487` | Pennsylvania, United States; Same/Pmen_rep3 |
| 228184 | `Gp0333789` | `PRJNA502030` | `SAMN10350486` | Pennsylvania, United States; Same/Pmari_rep1 |
| 228186 | `Gp0333791` | `PRJNA502032` | `SAMN10350485` | Pennsylvania, United States; Same/Pmari_rep3 |
| 228188 | `Gp0333793` | `PRJNA502034` | `SAMN10350484` | North Carolina, United States; Scot/Psyl_rep2 |
| 228220 | `Gp0333825` | `PRJNA502066` | `SAMN10350482` | Minnesota, United States; Sgre/Pmari_rep1 |
| 228244 | `Gp0333849` | `PRJNA502211` | `SAMN10350481` | Occitanie, France; Sbov/Prad_rep1 |
| 228262 | `Gp0333867` | `PRJNA502229` | `SAMN10350480` | Minnesota, United States; Scav/Pstro_rep1 |
| 228295 | `Gp0333900` | `PRJNA501955` | `SAMN10350483` | Minnesota, United States; Sgla/Psyl_rep1 |

These are review diagnostics, not new curated associations. Only this new report is written; records, source inputs, history, generated pages and Eukaryota remain untouched.
