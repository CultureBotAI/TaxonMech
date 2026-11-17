# YAML Record Review: Mesorhizobium sp. STM 4664

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/mesorhizobium_sp_stm_4664.yaml`
- Started UTC: 2026-10-06T10:15:29Z
- Finished UTC: 2026-10-06T10:22:17Z
- Verdict: pass with minor issues

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1035060`, Mesorhizobium sp. STM 4664. It asserts species rank, bacterial domain, parent `NCBITaxon:325217`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. It asserts no synonyms, nomenclature, taxonomy mappings, strain list, genomes, causal graph, evidence objects or discussion. This report does not change generated YAML, review status or either history surface.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/mesorhizobium_sp_stm_4664.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/mesorhizobium_sp_stm_4664.yaml --out /private/tmp/mstm4664-validation.tsv`: exit 0, one file scanned, zero errors. Read the header-only diagnostic TSV.
- Structured comparisons checked every ancestor, identity, genetic code, unique PATHS/scope rows, imported attestation and inline event. Exact type-material and dropped-record scans found no target rows. The merged-ID inventory contains the historical redirect described below.
- Ignored-inclusive identifier/name/slug/designation searches of reports and `history/` found no prior target report or separate history artifact before this report. A separate search for historical ID `1665331` also found none there. The inline seed event is present and schema-valid.
- Not checked: full-corpus `just qc`, `just verify-corpus`, `just validate-all`, `just test`, `just validate-history`, site drift and publication gates. Focused checks do not certify whole-corpus reproduction or release readiness. No focused term/reference/history validator was invented. `just validate-products` is inapplicable without curator-added graph nodes.
- Not checked: hash and contents of the configured historical primary taxdump. Opening its configured local path failed with FileNotFoundError; the subsequent repository-wide filename inventory included ignored files and found no taxdump archive or `.dmp` files. This is not a machine-wide absence claim.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:221870` and scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31296` agree with the target. Its index row is `data/taxa/PATHS.tsv:14352`; maintained scope is `curation/seed_scope.tsv:322162`. The pinned backbone has no target synonyms, classified children or retirement destination.

Read complete [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035060&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035060). They confirm the label, species rank, bacterial domain, parent and genetic code. The lineage agrees: root (`1`), cellular organisms (`131567`), Bacteria (`2`), Pseudomonadati (`3379134`), Pseudomonadota (`1224`), Alphaproteobacteria (`28211`), Hyphomicrobiales (`356`), Phyllobacteriaceae (`69277`), Mesorhizobium (`68287`) and unclassified Mesorhizobium (`325217`). Datasets includes root; XML supplies the other ancestor labels and ranks. `EXACT` means identity with this NCBI taxon, not validly published species nomenclature.

`data/raw/ncbi_merged_ids.tsv:23664` maps historical `NCBITaxon:1665331` to the current identifier. Both [EFetch for the historical ID](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1665331&retmode=xml) and [Datasets for that ID](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1665331) resolve to `1035060`; EFetch also retains `1665331` in AkaTaxIds. An ignored-inclusive identity search across `data/taxa/` found only this YAML's identifier/label, not a separate old-ID or same-designation record. The current target is not retired and does not need a duplicate record.

Live NCBI additionally classifies `Mesorhizobium sp. STM4664` as a misspelling. That alias is absent from the pinned backbone and candidate native-name rows. This limited source discrepancy is the minor finding below; it does not invalidate the current identifier.

## Evidence

The NCBITAXON attestation correctly counts one imported `NAME` for snapshot `2026-09-13`. The `2026-09-13T17:54:04Z` `SEEDED_FROM_SOURCES` event matches the maintained scope reason. Counts describe imported evidence, not biological abundance or universal coverage.

Exact non-expanded NCBI searches for `txid1035060[Organism:noexp]` returned no Assembly hits and six Nuccore entries. Assembly reported no matching items; this is a bounded query result, not proof that no genome exists anywhere. Read all six entries' complete metadata, references and features, excluding sequence bases and protein translations. Every source feature identifies this organism and `taxon:1035060`; none supplies a culture-collection, BioSample or assembly qualifier. These partial marker/gene sequences are not whole genomes:

| Accession | Sequence | Length | Source country | Source context |
| --- | --- | --- | --- | --- |
| [FR869636.1](https://www.ncbi.nlm.nih.gov/nuccore/FR869636.1) | 16S rRNA | 1,381 bp | France | Anthyllis vulneraria host growing on Zn-Pb mine soil |
| [FR869670.1](https://www.ncbi.nlm.nih.gov/nuccore/FR869670.1) | dnaK | 682 bp | France | Same explicit host and mine-soil context |
| [FR869658.1](https://www.ncbi.nlm.nih.gov/nuccore/FR869658.1) | atpD | 488 bp | Germany | Same explicit host and mine-soil context |
| [KP749918.1](https://www.ncbi.nlm.nih.gov/nuccore/KP749918.1) | 16S rRNA | 1,164 bp | France: Languedoc Roussillon | Anthyllis vulneraria host; collected 7 July 2006 |
| [HE599787.1](https://www.ncbi.nlm.nih.gov/nuccore/HE599787.1) | recA | 516 bp | France | Anthyllis vulneraria as isolation source |
| [FR869683.1](https://www.ncbi.nlm.nih.gov/nuccore/FR869683.1) | nodA | 576 bp | France | Anthyllis vulneraria host growing on Zn-Pb mine soil |

The four coding sequences cite Maynaud et al., Systematic and Applied Microbiology 35(2):65-72 (2012), DOI `10.1016/j.syapm.2011.11.002`, PMID `22221859`. The inspected complete [PubMed bibliographic record and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22221859&retmode=xml) verify that study and identify the Aminobacter anthyllidis type as STM4645, equivalent to LMG26462 and CFBP7437, not STM4664. The abstract does not individually characterize the target; the sequence entries provide its specific study connection. No target phenotype, type deposit or species reassignment is inferred from that abstract.

FR869636 retains an unpublished manuscript reference by the Maynaud group. Its submission is dated 17 May 2011, creation 17 July 2013 and update 26 October 2015. The dnaK, atpD and nodA entries were submitted 17 May 2011; recA was submitted 26 September 2011, through LSTM/INRA in Montpellier. Coding entries were created 15 February 2012; dnaK/atpD were updated 26 October 2015, while recA/nodA retain the 2012 date.

KP749918 retains a separate unpublished reference by Mohamad, Brunel and Cleyet-Marel, submitted 5 February 2015 and created/updated 20 June 2015. It names strain `STM4664`, collector Celine Vidal and identifier Geraldine Maynaud. Its Sanger/BioEdit assembly-method comment describes the marker sequence, not a genome assembly.

Preserved conflict: atpD reports Germany while the other five entries report France. The record makes no geography claim, so this is not an existing YAML contradiction. Resolve the discrepancy from strain-specific primary evidence before geographic enrichment; neither shared labels nor a majority of entries determines the correct country. Inspected protein annotations and primers were not promoted to curated functional or resistance assertions.

iModulonDB is inapplicable to the identity-only YAML, which asserts no gene, locus, regulator, pathway or transcriptomics claims. Genes discovered during completeness research do not create an expression-module assertion in the record.

## Completeness

Exact target-ID scans found no rows in the imported BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits tables. Zero imported strains is consistent with these inputs; it does not deny the isolate's existence.

Candidate discovery used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. It included ignored/compressed data, identifier, label, slug and STM4664 separator variants, then expanded to the historical taxon ID and all six nucleotide accessions. Only `SOURCE.json` provenance sidecars were excluded; other directories and external unindexed sources are outside this exhaustive-search claim.

The expanded search returned 60 candidate rows. Every complete row was read with native JSON or header-aware TSV parsers; reconciliation found exactly 60 read addresses, no unread candidates and no extra addresses. Four are target rows: backbone, scientific name, scope and merged ID. The other 56 are unrelated number-substring matches summarized below. No eligible missing culture-deposit or whole-genome association was identified within these bounds. Optional nomenclature, genome and graph slots can remain empty.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

1. Minor: unresolved name-source completeness/provenance discrepancy. Live NCBI retains the misspelling `Mesorhizobium sp. STM4664`, but the pinned native names, backbone synonym columns and generated YAML do not. `src/taxonmech/ncbi_taxdump.py` maps non-scientific name classes other than synonym/equivalent name to `RELATED_SYNONYM`, including misspellings; this is not an intentional exact-synonym mapping. `docs/SOURCE_COVERAGE.md` promises retention of original NCBI name classes for the named snapshot. However, the historical archive configured by `conf/ncbi_taxdump.yaml` is not locally available, so this review cannot distinguish a historical extraction omission from later source drift. The finding is a non-blocking provenance gap, not a proven seeder defect or wrong taxon identity. Maintained owners: `conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py` and its integration in `src/taxonmech/extract.py`; the derived backbone and YAML are not hand-edit targets.

## Recommended Edits

No immediate generated-record edit is warranted. First recover the exact configured `2026-09-13` archive and verify SHA-256 `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`. Inspect its names and merged rows for both taxon IDs. A current mutable FTP download cannot prove the historical pin.

If the verified archive contains the missing alias, fix the responsible maintained extraction path with a regression test in `tests/test_ncbi_taxdump.py`, then regenerate through documented extraction/seeding. If the alias was added later, retain the old snapshot interpretation and include it in a separately authorized source refresh. Preserve the source name class and related-synonym scope; do not silently promote the spelling variant to exact synonymy.

Leave the current identifier, `SEEDED` status and history unchanged. Do not count marker sequences as genomes, attach STM4645's type deposits to this taxon, or resolve the country conflict by majority vote. Any future geography assertion requires reconciled authoritative metadata or primary strain-specific evidence; this review authorizes no contacts.

## Follow-up Checks

Verify the pinned archive hash, exact name classes and old-to-current redirect before deciding whether extraction needs correction. For a demonstrated importer defect, run focused importer tests, re-extract under the documented workflow, canary-seed `NCBITaxon:1035060`, inspect its synonym provenance and rerun both focused record validators. Actual curation must also pass documented corpus reproduction, history, tests and publication gates.

Before optional phenotype/geography enrichment, inspect the relevant primary strain tables and reconcile the atpD country qualifier. A later genome enrichment requires an explicit eligible deposit-to-sample-to-genome chain, not taxon/name co-occurrence. No blocker was found for the current identity record.

## Additional Notes

The Maynaud article's primary abstract was inspected, but full experimental text and strain tables were inaccessible through the attempted publisher/HAL/author-upload routes. A related [Mohamad et al. study](https://pmc.ncbi.nlm.nih.gov/articles/PMC5203628/) was inspected through its header, abstract and initial results only; further PMC access encountered a browser challenge and the Europe PMC XML request returned HTTP 500. Its supplementary strain/accession tables were not inspected, so it does not establish target-specific phenotype or genome evidence here. A Greek thesis search lead was not verified at the matching passage and was not used as evidence. Search snippets were never substituted for primary text.

Dispositions of all 56 unrelated candidates:

| Candidate group | Rows | Identity and exclusion |
| --- | --- | --- |
| BV-BRC `0001:17988`, GenBank `0000:45347`, RefSeq `0000:38142`, GTDB `0004:23876`, GOLD projects `87420`, ATB `66040` | 6 | Staphylococcus haemolyticus 135665, taxon `1283`, BV-BRC `1283.108`, `GCA_001228185.1`/`GCF_001228185.1`, `SAMEA1035060`, GOLD `Gp0140478`/`Go0134595`, ATB `ERR085261`/`ERZ3070500`. Sample-number substring, not target identity. |
| BV-BRC `0006:8510`, ATB `569530` | 2 | Mycobacterium tuberculosis, taxon `1773`, BV-BRC `1773.20495`, run `ERR1035060`, `SAMEA3558593`, `ERZ3501812`. Run-number substring. |
| GenBank `0037:21034` | 1 | Bacteroides uniformis, taxon `820`, `RTP21198st1_H4_RTP21198_201120`, `GCA_040928605.1`, `SAMN41035060`, `PRJNA1093465`; no RefSeq partner, large multi-isolate project exclusion. |
| GenBank `0009:6366` | 1 | Campylobacter jejuni, taxon `197`, FSIS11926163, `GCA_010350605.1`, `SAMN13340350`, `PRJNA287430`; no RefSeq partner, large multi-isolate project exclusion. |
| ATB `1440068` | 1 | Salmonella, `SRR7473097`, `SAMN09604656`, `ERZ8975209`; matched digits within its SeqKit sum. |
| GOLD projects `196962`, `198028`, `198030`, `198032`, `198033`, `198035`, `198036`, `198038`, `198040`, `198042` | 10 | One Monterey Bay metatranscriptome (`Gp0294699`, `PRJNA502609`, `SAMN10350604`) and nine Iowa soil-aggregate metatranscriptomes. The latter are `Gp0296269`, `Gp0296271`, `Gp0296273`, `Gp0296274`, `Gp0296276`, `Gp0296277`, `Gp0296279`, `Gp0296281`, `Gp0296283`, with matching sample-number prefixes. All have empty organism GOLD fields, not target strain-genome chains. |
| BacDive `2349`, GOLD analyses `366065`, BV-BRC `0019:49019`, GenBank `0015:8593`, RefSeq `0003:19240`, GTDB `0015:26428`, StrainInfo `237976`, plus 23 derived rows listed below | 30 | Halochromatium roseum DSM18859/JA134, taxon `391920`, assembly name `ASM1665331v1`, `GCA_016653315.1`/`GCF_016653315.1`, `SAMN07156354`. Historical-target-ID digits match an unrelated assembly name. GTDB calls this Lamprobacter roseus; neither name denotes STM4664. |
| GenBank `0027:15233` | 1 | Escherichia coli, taxon `562`, `GCA_029337735.1`, assembly `PDT001665331.1`, isolate 2023BB-00010, `SAMN33845279`, `PRJNA288601`; no RefSeq partner, large-project exclusion. |
| GenBank `0034:13981`, GTDB `0001:31330` | 2 | Erysipelotrichaceae bacterium, taxon `2049044`, `GCA_036647475.1`, CGS6M1-bin11, `SAMN37014018`, `PRJNA1005433`, GTDB JAVXTH01 sp036642795; MAG length 1,665,331 bases supplied the match. |
| ATB `819408` | 1 | Neisseria gonorrhoeae, `ERR3895160`, `SAMEA6534517`, `ERZ25338016`; SeqKit substring. Available FASTA and pipeline PASS, but Sylph/HQ `SYLPH_RESULTS_FAIL`. |
| ATB `2945139` | 1 | Mycobacterium tuberculosis, `SRR29274230`, `SAMN41665331`, `ERZ26801447`; sample-number substring. Available FASTA with passing filters. |

The 23 derived Halochromatium rows are `data/atb/strain_links.tsv:3763`; `data/straininfo/assemblies.tsv:8282`; `data/raw/strain_assemblies.tsv:114189` through `114197`; `data/atb/genome_links.tsv:16345`, `16347`, `16348`; `data/raw/strain_related_records.tsv:329307`, `329308`, `329313`, `329318`, `329319`, `329320`; and `data/raw/strain_genome_records.tsv:91719`, `91720`, `91723`. Complete nested sample/genome evidence was read, not inferred from shared grouping.

That unrelated strain has BacDive `2441`, BV-BRC `391920.5`, IMG `2993868656`, GOLD analysis `Ga0559589`/project `Gp0653976` and StrainInfo `SI-ID:309535.3` (DOI `10.60712/SI-ID309535.3`). StrainInfo explicitly attaches gene `FN257161` and unversioned genome `GCA_016653315` to DSM18859 deposit `SI-DP:721033`; its other deposits are ATCCBAA1363, JCM14151 and CIP109733. These are not STM4664 deposits. The GOLD analysis's organism field is empty; the inspected derived chain is not represented as a fully verified primary GOLD organism chain. ATB genome links retain explicit BioSample evidence; shared BioSample is not genome equivalence.

Abbreviated source names refer to the inspected compressed catalogs in `data/bvbrc/`, `data/catalog/`, `data/gold/`, `data/bacdive/` and `data/straininfo/`. All five ATB candidate rows were read completely. Except for the explicitly noted Neisseria Sylph/HQ failure, their available FASTAs and inspected filters pass. SeqKit sums and download locations were inspected, not recomputed or downloaded; SeqKit sum is not MD5. No source, record, generated product, curation history or completed Eukaryota review was modified.
