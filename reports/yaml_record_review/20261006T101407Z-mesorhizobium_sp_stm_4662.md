# YAML Record Review: Mesorhizobium sp. STM 4662

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/mesorhizobium_sp_stm_4662.yaml`
- Started UTC: 2026-10-06T10:11:34Z
- Finished UTC: 2026-10-06T10:14:07Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1035059`, Mesorhizobium sp. STM 4662. It asserts species rank, bacterial domain, parent `NCBITaxon:325217`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. No optional synonyms, nomenclature, taxonomy mappings, strain list, genome links, causal graph, evidence objects or discussions are asserted. This review does not promote the record or append curation history.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/mesorhizobium_sp_stm_4662.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/mesorhizobium_sp_stm_4662.yaml --out /private/tmp/mstm4662-validation.tsv`: exit 0, one file scanned, zero errors. Read the header-only diagnostic TSV.
- Structured comparisons verified the complete source lineage, identity, genetic code, unique PATHS/scope rows, attestation and inline event wording. Exact scans of type-material, merged-ID and dropped-record inventories found no target rows.
- An ignored-inclusive identifier/name/slug/designation search of `reports/yaml_record_review/` and `history/` found no prior target report or separate history artifact before this report was written. The inline seed event is present and schema-valid.
- Not checked: full-corpus `just qc`, `just verify-corpus`, `just validate-all`, `just test`, `just validate-history`, site drift and publication gates. Focused checks do not certify whole-corpus reproduction or release readiness. No focused term/reference/history validator was invented. `just validate-products` is inapplicable without curator-added graph nodes.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:221869` and native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31295` agree with the target. The index is `data/taxa/PATHS.tsv:14350`; maintained scope is `curation/seed_scope.tsv:322161`. The pinned backbone supplies no target synonyms, retirement target or classified children.

Read complete [NCBI EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035059&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035059). They confirm the designation, species rank, bacterial domain, parent and genetic code 11. The stored chain agrees: root (`1`), cellular organisms (`131567`), Bacteria (`2`), Pseudomonadati (`3379134`), Pseudomonadota (`1224`), Alphaproteobacteria (`28211`), Hyphomicrobiales (`356`), Phyllobacteriaceae (`69277`), Mesorhizobium (`68287`) and unclassified Mesorhizobium (`325217`). Datasets includes root; EFetch supplies the other ancestor labels/ranks. `EXACT` identifies this NCBI taxon; it does not claim validly published species nomenclature or equivalence to Aminobacter anthyllidis.

## Evidence

The sole NCBITAXON attestation correctly counts one imported `NAME` from snapshot `2026-09-13`. The `2026-09-13T17:54:04Z` `SEEDED_FROM_SOURCES` event matches the maintained scope reason. Counts describe imported records, not biological abundance or worldwide source coverage.

Exact non-expanded searches for `txid1035059[Organism:noexp]` returned zero NCBI Assembly entries and five Nuccore entries. Read all five records' metadata, references and features, excluding sequence bases and protein translations. All source features identify Mesorhizobium sp. STM 4662, strain STM 4662 and `taxon:1035059`; none supplies a culture-collection, BioSample or assembly qualifier. These are partial marker/gene sequences, not whole genomes:

| Accession | Sequence | Length | Source country | Source context |
| --- | --- | --- | --- | --- |
| [FR869635.1](https://www.ncbi.nlm.nih.gov/nuccore/FR869635.1) | 16S rRNA | 1,385 bp | France | Anthyllis vulneraria host; host growing on Zn-Pb mine soil |
| [FR869669.1](https://www.ncbi.nlm.nih.gov/nuccore/FR869669.1) | dnaK | 677 bp | France | Same explicit host and isolation context |
| [FR869657.1](https://www.ncbi.nlm.nih.gov/nuccore/FR869657.1) | atpD | 481 bp | Germany | Same explicit host and isolation context |
| [HE599786.1](https://www.ncbi.nlm.nih.gov/nuccore/HE599786.1) | recA | 516 bp | France | Anthyllis vulneraria as isolation source |
| [FR869682.1](https://www.ncbi.nlm.nih.gov/nuccore/FR869682.1) | nodA | 557 bp | France | Anthyllis vulneraria host; host growing on Zn-Pb mine soil |

The four protein-coding entries cite Maynaud et al., Systematic and Applied Microbiology 35(2):65-72 (2012), DOI `10.1016/j.syapm.2011.11.002`, PMID `22221859`. Read the complete [PubMed bibliographic record and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22221859&retmode=xml), verifying the DOI, PMID, authors and study identity. Its proposed Aminobacter anthyllidis type is STM4645, with LMG26462 and CFBP7437 equivalences, not STM4662. The inspected abstract does not describe STM4662 individually; the gene records provide that specific study connection. Full strain tables and experimental text were not accessible, so no target phenotype, type deposit or species reassignment is inferred from the abstract.

The 16S entry still cites an unpublished manuscript by the same authors rather than the published article, without a DOI/PMID cross-reference. Its direct submission is dated 17 May 2011, creation 17 July 2013 and update 26 October 2015. The dnaK, atpD and nodA entries were submitted 17 May 2011; recA was submitted 26 September 2011, all through LSTM/INRA in Montpellier. The four coding entries were created 15 February 2012; dnaK and atpD were updated 26 October 2015, while recA and nodA retain the 2012 update date.

Preserved source conflict: atpD reports Germany, whereas the other four entries report France. Shared strain labels and taxon identifiers do not justify silently choosing a country or correcting a source. The present YAML asserts neither geography nor sequence-specific isolation metadata, so this conflict does not contradict an existing record claim. It remains unresolved for future enrichment. Coding-feature product names, protein cross-references and PCR primers were inspected as source metadata, not promoted to curated functional or resistance assertions.

iModulonDB is inapplicable to the identity-only YAML, which asserts no genes, loci, regulators, pathways or transcriptomics claims. Genes discovered during completeness research do not create an expression-module claim in the record.

## Completeness

Exact target-ID scans found no entries in the imported BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits tables. Zero imported strains is consistent with those inputs and does not deny the existence of the isolate.

Candidate discovery used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. It included ignored/compressed data, numeric taxon ID, label, slug and STM4662 separator variants, then expanded to all five nucleotide accessions. Only `SOURCE.json` provenance sidecars were excluded; unrelated directories and external unindexed sources are outside this exhaustive-search claim.

Both searches returned the same 26 rows. Every complete row was read with native JSON or header-aware TSV parsers; address reconciliation found no unread or extra candidates. Three rows concern the target: backbone, native name and scope. The other 23 are unrelated number-substring matches detailed below. No eligible missing culture-deposit or whole-genome association was identified within these bounds. Optional nomenclature, mapping, genome and graph slots can remain empty.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current record. Identity, lineage and imported provenance agree with inspected evidence. The external country conflict is documented above, but the record makes no conflicting geography claim; absence of optional geographic enrichment is not a required-field defect.

## Recommended Edits

None required. Leave generated YAML, `SEEDED` status and history unchanged. Do not count the five gene/marker accessions as genomes, assign the Aminobacter type deposits to STM4662, or select a country by majority vote. Any later resolution of the source-country disagreement belongs with authoritative INSDC source metadata and supporting strain-specific literature; this review does not authorize contacting submitters.

Later taxonomy corrections belong upstream; verified scope changes belong in `curation/seed_scope.tsv`; import/harmonization defects belong in maintained extraction and `src/taxonmech/seed.py` with regression tests, not a manual generated-record patch.

## Follow-up Checks

No blocking follow-up for the existing YAML. Before geographic or phenotype enrichment, obtain the primary strain table and reconcile the atpD country qualifier without conflating the target with other study isolates. A later refresh may check for an explicit deposit-to-sample-to-genome chain. After actual curation, run focused validators and documented corpus reproduction, history, tests and publication gates.

## Additional Notes

The NCBI browser failed through the web tool; official taxonomy XML and Datasets succeeded. PubMed's web page returned a browser challenge, but the official public API supplied its complete abstract and bibliographic record. ScienceDirect article/abstract routes were inaccessible; HAL returned an access-denied page, and the ResearchGate author-upload PDF link returned 404. The ResearchGate landing page's supplementary-sequence listing was not substituted for the primary article's strain table. Search snippets were leads only. No paid access, contacts or source mutations were used.

Full-row dispositions of thirteen unrelated strain/genome candidates:

| Source rows | Identity and exclusion |
| --- | --- |
| BV-BRC `0001:18014`; GenBank `0000:45380`; RefSeq `0000:38174`; GTDB `0003:26171`; GOLD projects `87469`; ATB `66039` | Six Staphylococcus haemolyticus W59 rows: taxon `1283`, `SAMEA1035059`, `GCA_001228845.1`/`GCF_001228845.1`, BV-BRC `1283.113`, GOLD `Gp0140527`/`Go0134644`, GenBank/GOLD project `PRJEB2705`, RefSeq/GTDB project `PRJNA224116`, ATB `ERR085252`/`ERZ3070502`. Sample-number substring only. |
| BV-BRC `0006:8512`; ATB `569529` | Mycobacterium tuberculosis `ERR1035059`, taxon `1773`, BV-BRC `1773.20497`, ATB `SAMEA3558592`/`ERZ3501802`. Run-number substring only. |
| GenBank `0037:21036` | Bacteroides uniformis, taxon `820`, strain `RTP21198st1_A4_RTP21198_201120`, `GCA_040928645.1`, `SAMN41035059`, `PRJNA1093465`; no RefSeq partner, large multi-isolate project exclusion. |
| GTDB `0014:37287`; GenBank `0011:47783`; RefSeq `0002:48667` | Kibdelosporangium persicum 4NS15, taxon `2698649`, `GCA_013280595.1`/`GCF_013280595.1`, `SAMN13056085`, GenBank project `PRJNA578297`, RefSeq/GTDB project `PRJNA224116`; type-material assembly with 10,350,595 total bases. Matched length digits, not target identity. |
| GenBank `0064:47232` | Uncultured bacterium, taxon `77133`, MAG `MarMAG_046729`, `GCA_977311165.1`, `SAMEA120697810`, `PRJEB104710`; 1,035,059 total bases, metagenome/genus-undefined RefSeq exclusion. Matched length, not taxon ID. |

Abbreviated source names refer to inspected `data/bvbrc/bvbrc-*.jsonl.gz`, `data/catalog/ncbi_*.jsonl.gz`, `data/catalog/gtdb_genomes-*.jsonl.gz`, `data/gold/projects.jsonl.gz` and `data/catalog/allthebacteria.tsv.xz` files. Both ATB rows have available FASTAs and passing assembly-pipeline, Sylph and HQ filters. Complete SeqKit sums and provided OSF/AWS locations were inspected, not recomputed or downloaded; SeqKit sum is not MD5.

The remaining ten GOLD candidates have empty organism GOLD fields and community-level contexts, not target strain-genome chains:

| `data/gold/projects.jsonl.gz` line | GOLD project | BioProject | BioSample | Inspected context |
| --- | --- | --- | --- | --- |
| 196249 | `Gp0293613` | `PRJNA502371` | `SAMN10350597` | Jervis Inlet, British Columbia; JV7_2_27 |
| 196251 | `Gp0293615` | `PRJNA502372` | `SAMN10350596` | Amundsen Gulf, Northwest Territories; Cases_109_6 |
| 196872 | `Gp0294605` | `PRJNA502383` | `SAMN10350595` | St. Lawrence River metatranscriptome; Law_Law_RepB_8h |
| 196879 | `Gp0294612` | `PRJNA502385` | `SAMN10350594` | Separate St. Lawrence River experiment; Law_Miss_RepC_8d |
| 196880 | `Gp0294613` | `PRJNA502386` | `SAMN10350593` | Separate St. Lawrence River experiment; Law_Yuk_RepA_8d |
| 196883 | `Gp0294616` | `PRJNA502387` | `SAMN10350592` | Separate St. Lawrence River experiment; Law_Atlam_RepC_8d |
| 196891 | `Gp0294624` | `PRJNA502390` | `SAMN10350591` | Altamaha River, Georgia, metatranscriptome; Atl_Miss_RepB_8h |
| 196905 | `Gp0294638` | `PRJNA502392` | `SAMN10350590` | Mississippi River, Louisiana, metatranscriptome; Miss_Cont_RepB_0h |
| 198043 | `Gp0296284` | `PRJNA502663` | `SAMN10350599` | Enriched soil aggregate, Iowa State University; MC6-MC0761-MT |
| 198046 | `Gp0296288` | `PRJNA502666` | `SAMN10350598` | Separate enriched-soil metatranscriptome; MC6-MC0765-MT |

These are review diagnostics only. No record, maintained input, generated product, curation history or completed Eukaryota review is changed.
