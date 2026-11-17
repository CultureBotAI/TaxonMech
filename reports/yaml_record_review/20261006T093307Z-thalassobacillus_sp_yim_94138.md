# YAML Record Review: Thalassobacillus sp. YIM 94138

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/thalassobacillus_sp_yim_94138.yaml`
- Started UTC: 2026-10-06T09:31:36Z
- Finished UTC: 2026-10-06T09:33:07Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord` for `NCBITaxon:1035049`, Thalassobacillus sp. YIM 94138. Species rank, bacterial domain, parent `NCBITaxon:2621135`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status are asserted. There are zero imported strains, one NCBI name attestation and one inline seed event. No synonyms, nomenclature, taxonomy mappings, strain list, genome links, causal graph, evidence objects or discussion are asserted. This is an individual read-only review, not curation or a lifecycle promotion.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/thalassobacillus_sp_yim_94138.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/thalassobacillus_sp_yim_94138.yaml --out /private/tmp/thbyim94138-validation.tsv`: exit 0, one file scanned, zero errors; the diagnostic TSV contains only its header.
- Structured source comparisons verified the identity, full lineage, genetic code, unique PATHS/scope rows, attestation and complete inline event wording. Exact scans of the type-material, merged-ID and dropped-record inventories returned no target entries.
- Before writing this report, `rg --no-ignore --hidden` searched the identifier, full designation and slug in `reports/yaml_record_review/` and `history/`, finding no prior report or separate history artifact. The existing inline seed event passes schema validation; no review history or status change is made.
- Not checked: full-corpus `just qc`, `just verify-corpus`, `just validate-all`, `just test`, `just validate-history`, site drift and publication gates. The focused comparisons are not corpus reproduction or release certification. No focused term/reference/history validator was invented. `just validate-products` is inapplicable because no curator-added graph nodes exist in this target.

## Identity and Grounding

The complete backbone row `data/raw/ncbitaxon_taxa.tsv:221860` and scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31286` match the record. The unique index is `data/taxa/PATHS.tsv:14340`; maintained scope is `curation/seed_scope.tsv:322152`. No source synonyms, retirement target or child taxa were found in the pinned backbone for this identifier.

Read the full live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035049&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035049). Both agree on identifier, designation and species rank; EFetch confirms bacterial division, genetic code 11 and parent unclassified Thalassobacillus (`2621135`). The lineage agrees with all ten stored ancestors: root (`1`), cellular organisms (`131567`), Bacteria (`2`), Bacillati (`1783272`), Bacillota (`1239`), Bacilli (`91061`), Caryophanales (`1385`), Bacillaceae (`186817`), Thalassobacillus (`331971`) and unclassified Thalassobacillus (`2621135`). Datasets includes root; the remaining labels and ranks are supplied by EFetch. `EXACT` is correct NCBI identifier grounding, not a claim of validly published species nomenclature.

## Evidence

The sole NCBITAXON attestation correctly records one `NAME`, with source ID and label matching the `2026-09-13` snapshot. The `2026-09-13T17:54:04Z` `SEEDED_FROM_SOURCES` event matches the scope reason exactly. Counts describe imported source coverage, not the abundance or biological absence of strains.

The exact, non-expanded NCBI search `txid1035049[Organism:noexp]` returned zero Assembly entries and one Nuccore UID, `333798069`; all returned IDs were accounted for. Read complete metadata, references and features, excluding bases, for [JF792143.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792143.1). It is a 691-base partial 16S rRNA marker with both ends marked partial. Its source explicitly identifies YIM 94138 and `taxon:1035049`, without culture-collection, BioSample or assembly qualifiers. It was created 28 May 2011, updated 26 August 2015, and directly submitted by C. Chen on 7 April 2011 from Yunnan Institute of Microbiology.

The linked Qijiaojing Lake study is marked unpublished and supplies no DOI or PMID. Its title is not evidence of an enzyme phenotype, culture recipe or habitat claim for this record. The marker supports its submitted identity but does not supply a whole genome, culture-deposit equivalence or type status. The YAML makes none of those additional claims. iModulonDB is inapplicable to this identity-only target, which asserts no gene, regulatory or transcriptomic relationships.

## Completeness

Exact inventory comparisons found no target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. The broader candidate search and lack of classified children are consistent with the record's zero imported strains. This is not a claim that the isolate never existed or that future sources cannot connect it to a deposit.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. Terms included the numeric identifier, full name, slug and separator variants of YIM 94138; a second search added `JF792143`. Compressed catalogs were searched. Only `SOURCE.json` provenance sidecars were excluded from these candidate-data searches; no claim of exhaustive coverage of unrelated repository directories or external unindexed sources is made.

Both searches yielded the same 26 rows. Every row was read in full through header-aware TSV or native JSON parsers; address reconciliation found no unread or extra rows. Three target rows are the backbone, native name and scope. The 23 unrelated rows are individually accounted for below. No supported missing culture deposit or eligible genome link was identified. The partial marker is not a missing genome, and optional nomenclature, mapping and mechanism fields need not be fabricated.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The bounded identity and provenance claims agree with inspected primary authority and maintained source data. No unrelated search candidate supplies a defensible new association to this target.

## Recommended Edits

None required. Leave generated YAML, `SEEDED` status and history unchanged. A future verified identity or deposit association should be handled in maintained source acquisition/harmonization inputs and `src/taxonmech/seed.py`, with a focused regression test. Scope belongs in `curation/seed_scope.tsv`; taxonomy classification corrections belong at the upstream authority. Do not infer genome links from a shared numerical substring or a partial rRNA accession.

## Follow-up Checks

No blocking follow-up. At a future source refresh, recheck the exact NCBI identity and marker, requiring explicit deposit-to-sequence evidence before adding a strain or genome. Rerun the two focused validators after any resulting curation change, followed by documented corpus reproduction, history, tests and publication gates as appropriate. This review does not substitute for those gates.

## Additional Notes

The web tool could not open the NCBI taxonomy browser page; complete official XML and Datasets responses succeeded. The full-designation web query returned secondary taxonomy summaries, not additional primary evidence, and the exact marker query returned no results. Neither snippets nor search absence are used to infer global biological or literature absence.

Disposition of 13 unrelated bacterial genome/source candidates:

| Full rows inspected | Identity and reason for exclusion |
| --- | --- |
| `data/bvbrc/bvbrc-0001.jsonl.gz:18541`; `data/catalog/ncbi_genbank-0000.jsonl.gz:45917`; `data/catalog/ncbi_refseq-0000.jsonl.gz:38695`; `data/catalog/gtdb_genomes-0009.jsonl.gz:5357`; `data/gold/projects.jsonl.gz:87373`; `data/catalog/allthebacteria.tsv.xz:66029` | Six rows concern Staphylococcus haemolyticus 51-43, taxon 1283, sample `SAMEA1035049`, explicit paired assemblies `GCA_001239605.1`/`GCF_001239605.1`, BV-BRC `1283.203`, GOLD `Gp0140431`/`Go0134548`, and ATB run `ERR085204`/analysis `ERZ3070484`. GenBank/BV-BRC/GOLD carry study `PRJEB2705`; RefSeq/GTDB retain umbrella project `PRJNA224116`. Sample-number match only. |
| `data/bvbrc/bvbrc-0027.jsonl.gz:21483`; `data/catalog/ncbi_genbank-0037.jsonl.gz:21046`; `data/catalog/ncbi_refseq-0006.jsonl.gz:20156`; `data/catalog/gtdb_genomes-0017.jsonl.gz:23116` | Four rows concern Bacteroides thetaiotaomicron, taxon 818, strain `RTP21198st1_G6_RTP21198_201120`, sample `SAMN41035049`, paired `GCA_040928845.1`/`GCF_040928845.1`, BV-BRC `818.3297`. GenBank/BV-BRC use `PRJNA1093465`; RefSeq/GTDB retain `PRJNA224116`. Not the target taxon or YIM designation. |
| `data/bvbrc/bvbrc-0006.jsonl.gz:8498`; `data/catalog/allthebacteria.tsv.xz:569519` | Two rows concern Mycobacterium tuberculosis run/designation `ERR1035049`, BV-BRC `1773.20484`, ATB sample `SAMEA3558582` and analysis `ERZ3501764`; run-number match only. |
| `data/catalog/ncbi_genbank-0040.jsonl.gz:38929` | Steroidobacteraceae bacterium, taxon `2689616`, isolate `ME2018-10-05_3300044616_group8_bin38`, assembly `GCA_044369535.1`, sample `SAMN43900521`, project `PRJNA1158976`. Here `1035049` is the genome size, not an identifier. The row has no RefSeq partner, with source exclusions for metagenome origin, fragmentation and undefined genus. Its unrelated PMID `38370794` is not evidence for YIM 94138 and was not used as such. |

Both ATB candidates retain available FASTAs and passing pipeline, HQ and Sylph filters. Full source rows include SeqKit sums and supplied OSF/AWS locations; no sequence was downloaded or checksum recomputed. These unrelated candidates are excluded by identity, not availability. SeqKit sum is not MD5, and shared sample evidence alone does not imply genome equivalence.

The remaining ten candidates are distinct GOLD environmental or plant/fungal community projects, each with an empty organism GOLD ID. Read each complete row rather than transferring a generic project association:

| `data/gold/projects.jsonl.gz` line | GOLD project | BioProject | BioSample | Inspected project context |
| --- | --- | --- | --- | --- |
| 196948 | `Gp0294684` | `PRJNA502606` | `SAMN10350494` | Mediterranean deep-brine-pool seawater viral communities; Kryos LI F3 |
| 198025 | `Gp0296266` | `PRJNA502645` | `SAMN10350496` | Enriched soil aggregate metatranscriptome, Iowa State University, Ames; MC6-MC0513-MT |
| 198037 | `Gp0296278` | `PRJNA502657` | `SAMN10350497` | Separate enriched soil aggregate metatranscriptome, Iowa State University, Ames; MC6-MC0690-MT |
| 205702 | `Gp0306215` | `PRJNA502706` | `SAMN10350495` | Municipal-landfill groundwater community, Southern Ontario; Pumphouse #1 |
| 226851 | `Gp0331611` | `PRJNA502153` | `SAMN10350499` | Pinus contorta root metatranscriptome, Duke University, North Carolina; Pcontorta(CO)_control_rep3 |
| 226853 | `Gp0331613` | `PRJNA502155` | `SAMN10350498` | Separate Pinus contorta root metatranscriptome, Duke University, North Carolina; Pcontorta(CA)_control_rep2 |
| 228170 | `Gp0333775` | `PRJNA502016` | `SAMN10350493` | Pinaceae seedling/Suillus ectomycorrhiza metatranscriptome, Pennsylvania; Same/Psyl_rep2 |
| 228171 | `Gp0333776` | `PRJNA502017` | `SAMN10350492` | Separate Pinaceae/Suillus metatranscriptome, Pennsylvania; Same/Psyl_rep3 |
| 228174 | `Gp0333779` | `PRJNA502020` | `SAMN10350491` | Separate Pinaceae/Suillus metatranscriptome, Pennsylvania; Same/Pstro_rep3 |
| 228176 | `Gp0333781` | `PRJNA502022` | `SAMN10350490` | Separate Pinaceae/Suillus metatranscriptome, Pennsylvania; Same/Prad_rep2 |

These are sample-number substring hits, not target-specific strain/genome chains. Source dispositions are review diagnostics only. This report does not alter records, source inventories, curation history, generated pages or the completed Eukaryota reviews.
