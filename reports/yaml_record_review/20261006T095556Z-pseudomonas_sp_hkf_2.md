# YAML Record Review: Pseudomonas sp. HKF-2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_hkf_2.yaml`
- Started UTC: 2026-10-06T09:52:48Z
- Finished UTC: 2026-10-06T09:55:56Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1035054`, Pseudomonas sp. HKF-2. It asserts species rank, bacterial domain, parent `NCBITaxon:196821`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. No optional synonyms, nomenclature, taxonomy mappings, strain list, genome links, causal graph, evidence objects or discussions are asserted. This read-only review does not promote the record or append curation history.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_hkf_2.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_hkf_2.yaml --out /private/tmp/phkf2-validation.tsv`: exit 0, one file scanned, zero errors. Read the header-only diagnostic TSV.
- Structured comparisons verified the entire source lineage, identity, genetic code, unique PATHS/scope rows, sole attestation and inline event wording. Exact scans of type-material, merged-ID and dropped-record inventories found no target rows.
- An ignored-inclusive identifier/name/slug/designation search of `reports/yaml_record_review/` and `history/` found no prior report or separate history artifact before this report was written. The inline seed event is present and schema-valid.
- Not checked: full-corpus `just qc`, `just verify-corpus`, `just validate-all`, `just test`, `just validate-history`, site drift and publication gates. Focused checks do not certify whole-corpus reproduction or release readiness. No focused term/reference/history validator was invented. `just validate-products` is inapplicable without curator-added graph nodes.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:221865` and native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31291` agree with the target. The index is `data/taxa/PATHS.tsv:14346`; maintained scope is `curation/seed_scope.tsv:322157`. The pinned backbone supplies no target synonyms, retirement target or classified children.

Read the complete [NCBI EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035054&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035054). These confirm the exact designation, species rank, bacterial domain, parent and genetic code 11. The complete stored chain agrees: root (`1`), cellular organisms (`131567`), Bacteria (`2`), Pseudomonadati (`3379134`), Pseudomonadota (`1224`), Gammaproteobacteria (`1236`), Pseudomonadales (`72274`), Pseudomonadaceae (`135621`), Pseudomonas (`286`) and unclassified Pseudomonas (`196821`). Datasets includes root; EFetch supplies the other ancestor labels/ranks. Exact grounding to this NCBI node does not establish validly published species nomenclature or equivalence to another Pseudomonas species.

## Evidence

The sole NCBITAXON attestation correctly counts one imported `NAME` from snapshot `2026-09-13`. The `2026-09-13T17:54:04Z` `SEEDED_FROM_SOURCES` event agrees with the maintained scope reason. These counts describe imported records, not biological abundance or global source absence.

Exact non-expanded searches for `txid1035054[Organism:noexp]` returned zero NCBI Assembly entries and one Nuccore entry, UID `371939996`. Read all metadata, references and features for [AB633200.1](https://www.ncbi.nlm.nih.gov/nuccore/AB633200.1), excluding bases. It is a 1,399-base 16S rRNA marker, partial at both ends, not a whole genome. Source qualifiers explicitly identify Pseudomonas sp. HKF-2, strain HKF-2 and `taxon:1035054`, with brackish-water isolation context in Lake Sanaru, Shizuoka, Japan. Created/updated 12 January 2012; direct submission 19 May 2011 by Hideyuki Tamegai and colleagues at Nihon University. No culture-collection, BioSample or assembly qualifier is present in the inspected source feature.

GenBank cites Fujimori et al., Limnology and Oceanography 57:154-162 (2012), without a DOI/PMID cross-reference. The inspected [primary publisher page](https://aslopubs.onlinelibrary.wiley.com/doi/10.4319/lo.2012.57.1.0154) verifies the authors, title, journal coordinates and DOI `10.4319/lo.2012.57.1.0154`. Its abstract describes the Erythrobacter/Pseudomonas isolate study but names HKF-1, not HKF-2 individually. The specific HKF-2 connection is supplied by GenBank, not inferred from that abstract. The article's full experimental text and supplements were not audited.

Also read the research team's [KAKEN project 23310010 results report](https://kaken.nii.ac.jp/ja/file/KAKENHI-PROJECT-23310010/23310010seika.pdf), dated 22 May 2014. Text and rendered pages 1, 3, 4 and 5 were inspected. Its Lake Sanaru methods/results distinguish HKF-2 through HKF-5 as Pseudomonas from Erythrobacter HKF-1, and its publication list includes the same 2012 DOI. It separately mentions culture-collection comparator strains; this is not a deposit equivalence for HKF-2. Figure 1 concerns HKF-1, so its values must not be transferred to HKF-2. This corroborates designation/provenance only; no new phenotype, rate or mechanism is added to the YAML.

iModulonDB is inapplicable to this identity-only record, which asserts no genes, loci, regulators, pathways or transcriptomics claims. This is not negative evidence about expression-module coverage.

## Completeness

Exact target-ID scans found no entries in the imported BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits tables. The zero imported strain count is consistent with those inputs; it does not deny the existence of the experimental isolate.

The candidate search used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. It included ignored/compressed data, numeric taxon ID, designation, slug and HKF-2 separator variants, then expanded to `AB633200`. Only `SOURCE.json` provenance sidecars were excluded from this candidate-data search; unrelated directories and external unindexed sources are outside its exhaustive-search claim.

Both searches returned the same 28 rows. Every complete candidate was read with header-aware TSV or native JSON parsers; address reconciliation found no unread or extra rows. Three rows concern the target: backbone, native name and scope. The 25 remaining hits concern different organisms or number substrings, detailed below. The Penicillium HKF2 designation is a different organism, not a conflicting Pseudomonas placement. No eligible missing deposit or genome association was identified within the inspected bounds. Optional nomenclature, mappings, genome and graph slots can remain empty.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage and imported provenance agree with inspected evidence. No actual claim is unsupported or over-scoped.

## Recommended Edits

None required. Leave generated YAML, `SEEDED` status and history unchanged. Do not convert `AB633200.1` into a whole-genome link, transfer HKF-1 experimental values, or import Penicillium HKF2 resources. Later taxonomy corrections belong upstream; verified scope changes belong in `curation/seed_scope.tsv`; import/harmonization defects belong in maintained extraction and `src/taxonmech/seed.py` with regression tests, not a manual generated-record patch.

## Follow-up Checks

No blocking follow-up. A later source refresh may recheck the exact taxon/designation and marker for an explicit deposit-to-sample-to-genome chain. Any proposed phenotype enrichment requires full experimental-text review and strain/condition-specific evidence. After actual curation, run the focused validators plus documented corpus reproduction, history, test and publication gates.

## Additional Notes

The NCBI browser did not load through the web tool; official EFetch and Datasets succeeded. KAKEN web text extraction omitted much Japanese text, and web screenshots timed out. A public PDF download succeeded; local PDFKit extraction/rendering supplied legible pages for the relevant methods/results and publication reference. Poppler was not available. PDFKit logged a generic CoreGraphics warning but produced all requested pages, which were visually inspected. No paid access or outbound contact was used.

Full-row dispositions of the fifteen unrelated strain/genome candidates:

| Source rows | Identity and exclusion |
| --- | --- |
| BV-BRC `0001:18885`; GenBank `0000:45252`; RefSeq `0000:38051`; GTDB `0003:24444`; GOLD projects `87458`; ATB `66034` | Six Staphylococcus haemolyticus JCSC_1435 rows: taxon `1283`, sample `SAMEA1035054`, `GCA_001226285.1`/`GCF_001226285.1`, BV-BRC `1283.91`, GOLD `Gp0140516`/`Go0134633`, project `PRJEB2705`, ATB `ERR085220`/`ERZ3070497`. Sample-number substring only. |
| BV-BRC `0006:8503`; ATB `569524` | Mycobacterium tuberculosis `ERR1035054`, BV-BRC `1773.20489`, ATB sample `SAMEA3558587`/analysis `ERZ3501782`. Run-number substring only. |
| ATB `2428168` | Different Mycobacterium tuberculosis run `SRR21685240`, sample `SAMN30986588`, analysis `ERZ26210932`; matched digits inside the SeqKit sum, not taxon identity. |
| GenBank `0037:21043` | Bacteroides uniformis, taxon `820`, strain `RTP21002st1_B5_RTP21002_201210`, `GCA_040928775.1`, `SAMN41035054`, `PRJNA1093465`; no RefSeq partner, large multi-isolate project exclusion. |
| GenBank `0009:6363` | Campylobacter jejuni FSIS11926427, taxon `197`, `GCA_010350545.1`, `SAMN13447803`, `PRJNA292668`; no RefSeq partner, large multi-isolate project exclusion. Assembly-number substring only. |
| GenBank `0061:4055` | Uncultured Eubacteriales bacterium, taxon `172733`, isolate `MGBC157726`, `GCA_949041515.1`, `SAMEA112427931`, `PRJEB59335`; matched ungapped size `1035054`. Fragmented metagenome/genus-undefined exclusion, no RefSeq partner. |
| GOLD organism `279932`, project `156398`, analysis `131960` | Penicillium sp. HKF2, taxon `887910`, `Go0384526`/`Gp0235633`/`Ga0213298`, project `PRJNA371405`, sample `SAMN06298664`, `GCA_002000375.1`, WGS `MUXA00000000`. Empty culture-collection field. A fungal organism with a similar designation, not this bacterial isolate; no Eukaryota review was reopened. |

These abbreviated source names refer to the inspected `data/bvbrc/bvbrc-*.jsonl.gz`, `data/catalog/ncbi_*.jsonl.gz`, `data/catalog/gtdb_genomes-*.jsonl.gz`, `data/gold/*.jsonl.gz` and `data/catalog/allthebacteria.tsv.xz` files. All three ATB rows have available FASTAs and passing assembly-pipeline filters. The `ERR1035054` row fails Sylph/HQ filters; the other two pass. Full SeqKit sums and OSF/AWS location fields were inspected, not recomputed or downloaded; SeqKit sum is not MD5.

The other ten candidates are distinct GOLD community/fungal projects with empty organism GOLD fields, not HKF-2 strain-genome chains:

| `data/gold/projects.jsonl.gz` line | GOLD project | BioProject | BioSample | Inspected context |
| --- | --- | --- | --- | --- |
| 205795 | `Gp0306339` | `PRJNA502734` | `SAMN10350547` | Sakinaw Lake saline-water community, British Columbia; sak_2013_06_06_60m |
| 205885 | `Gp0306429` | `PRJNA502738` | `SAMN10350546` | Enriched fungal community from goat fecal pellet, Isla Vista, California; alfalfa Gen0 Rep1, penicillin/streptomycin |
| 206805 | `Gp0307449` | `PRJNA502742` | `SAMN10350549` | Sakinaw Lake saline-water community; sak_2010_1_5_50m |
| 206807 | `Gp0307451` | `PRJNA502744` | `SAMN10350548` | Separate Sakinaw Lake sample; sak_2010_1_5_80m |
| 223276 | `Gp0326549` | `PRJNA502280` | `SAMN10350545` | Pisolithus thermaeus 72 free-living mycelial community, Australia; 72_FLM_1 |
| 223277 | `Gp0326550` | `PRJNA502281` | `SAMN10350544` | Separate Pisolithus thermaeus project; 72_FLM_2 |
| 223280 | `Gp0326553` | `PRJNA502284` | `SAMN10350543` | Pisolithus thermaeus 72/Eucalyptus grandis ectomycorrhiza, Australia; 72_ECM_2 |
| 223281 | `Gp0326554` | `PRJNA502285` | `SAMN10350542` | Separate ectomycorrhiza project; 72_ECM_3 |
| 223283 | `Gp0326556` | `PRJNA502287` | `SAMN10350541` | Pisolithus croceorhizus 76C free-living mycelial community, Australia; 76C_FLM_2 |
| 223284 | `Gp0326557` | `PRJNA502288` | `SAMN10350540` | Separate Pisolithus croceorhizus project; 76C_FLM_3 |

These are review diagnostics only. No record, maintained input, generated product, curation history or completed Eukaryota review is changed.
