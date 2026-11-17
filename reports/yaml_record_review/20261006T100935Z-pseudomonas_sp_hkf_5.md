# YAML Record Review: Pseudomonas sp. HKF-5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_hkf_5.yaml`
- Started UTC: 2026-10-06T10:04:42Z
- Finished UTC: 2026-10-06T10:09:35Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1035057`, Pseudomonas sp. HKF-5. It asserts species rank, bacterial domain, parent `NCBITaxon:196821`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. No optional synonyms, nomenclature, taxonomy mappings, strain list, genome links, causal graph, evidence objects or discussions are asserted. This read-only review does not promote the record or append curation history.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_hkf_5.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_hkf_5.yaml --out /private/tmp/phkf5-validation.tsv`: exit 0, one file scanned, zero errors. Read the header-only diagnostic TSV.
- Structured comparisons verified the entire source lineage, identity, genetic code, unique PATHS/scope rows, sole attestation and inline event wording. Exact scans of type-material, merged-ID and dropped-record inventories found no target rows.
- An ignored-inclusive identifier/name/slug/designation search of `reports/yaml_record_review/` and `history/` found three contextual mentions in the HKF-2, HKF-3 and HKF-4 reports, not an earlier target-specific report or separate target history artifact. Those neighboring reports were inspected. The inline seed event is present and schema-valid.
- Not checked: full-corpus `just qc`, `just verify-corpus`, `just validate-all`, `just test`, `just validate-history`, site drift and publication gates. Focused checks do not certify whole-corpus reproduction or release readiness. No focused term/reference/history validator was invented. `just validate-products` is inapplicable without curator-added graph nodes.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:221868` and native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31294` agree with the target. The index is `data/taxa/PATHS.tsv:14349`; maintained scope is `curation/seed_scope.tsv:322160`. The pinned backbone supplies no target synonyms, retirement target or classified children.

Read the complete [NCBI EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035057&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035057) and [NCBI browser entry](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1035057&lvl=3&mode=node). They confirm the exact designation, species rank, bacterial domain, parent and genetic code 11. The complete stored chain agrees: root (`1`), cellular organisms (`131567`), Bacteria (`2`), Pseudomonadati (`3379134`), Pseudomonadota (`1224`), Gammaproteobacteria (`1236`), Pseudomonadales (`72274`), Pseudomonadaceae (`135621`), Pseudomonas (`286`) and unclassified Pseudomonas (`196821`). Datasets includes root; EFetch supplies the other ancestor labels/ranks. Exact grounding does not establish validly published species nomenclature or equivalence to another Pseudomonas species.

## Evidence

The sole NCBITAXON attestation correctly counts one imported `NAME` from snapshot `2026-09-13`. The `2026-09-13T17:54:04Z` `SEEDED_FROM_SOURCES` event agrees with the maintained scope reason. Source counts describe imported records, not biological abundance or global source absence.

Exact non-expanded searches for `txid1035057[Organism:noexp]` returned zero NCBI Assembly entries and one Nuccore entry, UID `371939999`. Read all metadata, references and features for [AB633203.1](https://www.ncbi.nlm.nih.gov/nuccore/AB633203.1), excluding bases. It is a 1,399-base 16S rRNA marker, partial at both ends, not a whole genome. Source qualifiers explicitly identify Pseudomonas sp. HKF-5, strain HKF-5 and `taxon:1035057`, with brackish-water isolation context in Lake Sanaru, Shizuoka, Japan. Created/updated 12 January 2012; direct submission 19 May 2011 by Hideyuki Tamegai and colleagues at Nihon University. No culture-collection, BioSample or assembly qualifier is present in the inspected source feature.

GenBank cites Fujimori et al., Limnology and Oceanography 57:154-162 (2012), without a DOI/PMID cross-reference. The inspected [primary publisher page](https://aslopubs.onlinelibrary.wiley.com/doi/10.4319/lo.2012.57.1.0154) verifies authors, title, journal coordinates and DOI `10.4319/lo.2012.57.1.0154`. Its abstract describes the Erythrobacter/Pseudomonas isolate study but names HKF-1 rather than HKF-5 individually. GenBank supplies the specific HKF-5 connection; it is not inferred from the abstract. The article's full experimental text and supplements were not audited.

The research team's [KAKEN project 23310010 results report](https://kaken.nii.ac.jp/ja/file/KAKENHI-PROJECT-23310010/23310010seika.pdf), dated 22 May 2014, was inspected as text and rendered pages 1, 3, 4 and 5 earlier in this review session. Its Lake Sanaru methods/results place HKF-2 through HKF-5 in Pseudomonas, separately from Erythrobacter HKF-1; its publication list supplies the same 2012 DOI. Culture-collection comparator strains are not stated to be deposits of HKF-5. Figure 1 concerns HKF-1, so neither its experimental values nor a deposit equivalence is transferred.

Inspected the bibliographic header and phylogenetic methods of [Tang et al. 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4462929/), DOI `10.1264/jsme2.ME14177`, PMID `25985930`. The methods distinguish Lake Bosten study clones from reference sequences. Read text on pages 6-8 of its [primary supplement](https://www.jstage.jst.go.jp/article/jsme2/30/2/30_ME14177/_supplement/_download/30_ME14177_1.pdf) and visually inspected page 7, panel B. That tree explicitly labels the Lake Sanaru HKF-5 reference with `AB633203`, separately from Pseudomonas peli R-20805 (`AM114534`) and clone Aug-B-12-093 (`JQ327522`). This is comparative phylogenetic context, not evidence that HKF-5 was isolated from Lake Bosten, that the clone is the same isolate, or that HKF-5 should be renamed P. peli. No phenotype or genotype is transferred between those nodes.

iModulonDB is inapplicable to the identity-only target, which asserts no genes, loci, regulators, pathways or transcriptomics claims. Finding external study context does not require adding an expression-module or mechanistic claim.

## Completeness

Exact target-ID scans found no entries in the imported BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits tables. The zero imported strain count is consistent with those inputs; it does not deny the existence of the experimental isolate.

The candidate search used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. It included ignored/compressed data, numeric taxon ID, designation, slug and HKF-5 separator variants, then expanded to `AB633203`. Only `SOURCE.json` provenance sidecars were excluded from this candidate-data search; unrelated directories and external unindexed sources are outside its exhaustive-search claim.

Both searches returned the same 22 rows. Every complete candidate was read with header-aware TSV or native JSON parsers; address reconciliation found no unread or extra rows. Three rows concern the target: backbone, native name and scope. The remaining 19 are unrelated number-substring matches, detailed below. No eligible missing culture deposit or whole-genome association was identified within these bounds. Optional nomenclature, mappings, genome and graph slots can remain empty.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage and imported provenance agree with inspected evidence. The additional study context does not establish a required missing representation or an error in the current claims.

## Recommended Edits

None required. Leave generated YAML, `SEEDED` status and history unchanged. Do not turn `AB633203.1` into a genome, or transfer comparator species identities, culture deposits or Lake Bosten clone provenance to HKF-5. Later taxonomy corrections belong upstream; verified scope changes belong in `curation/seed_scope.tsv`; import/harmonization defects belong in maintained extraction and `src/taxonmech/seed.py` with regression tests, not a manual generated-record patch.

## Follow-up Checks

No blocking follow-up. A later source refresh may recheck the exact taxon/designation and marker for an explicit deposit-to-sample-to-genome chain. Any proposed phenotype enrichment requires full experimental-text review and strain/condition-specific evidence. After actual curation, run the focused validators plus documented corpus reproduction, history, test and publication gates.

## Additional Notes

The J-STAGE supplement timed out through the web tool, including its screenshot route. A public PDF download succeeded; local PDFKit text extraction and page rendering allowed direct inspection. Poppler was unavailable. No search snippet was treated as evidence. No paid access, outbound messages or source mutations were used.

Full-row dispositions of nine unrelated strain/genome candidates:

| Source rows | Identity and exclusion |
| --- | --- |
| BV-BRC `0001:18240`; GenBank `0000:45616`; RefSeq `0000:38402`; GTDB `0000:7385`; GOLD projects `87481`; ATB `66037` | Six Staphylococcus haemolyticus CN1197 rows: taxon `1283`, sample `SAMEA1035057`, `GCA_001233565.1`/`GCF_001233565.1`, BV-BRC `1283.148`, GOLD `Gp0140539`/`Go0134656`, GenBank/GOLD project `PRJEB2705`, RefSeq/GTDB project `PRJNA224116`, ATB `ERR085229`/`ERZ3070501`. Sample-number substring only. |
| BV-BRC `0006:8508`; ATB `569527` | Mycobacterium tuberculosis `ERR1035057`, taxon `1773`, BV-BRC `1773.20493`, ATB sample `SAMEA3558590`/analysis `ERZ3501798`. Run-number substring only. |
| GenBank `0037:21038` | Bacteroides uniformis, taxon `820`, strain `RTP21198st1_A10_RTP21198_201120`, `GCA_040928685.1`, `SAMN41035057`, `PRJNA1093465`; no RefSeq partner, large multi-isolate project exclusion. Sample-number substring only. |

Abbreviated source names refer to the inspected `data/bvbrc/bvbrc-*.jsonl.gz`, `data/catalog/ncbi_*.jsonl.gz`, `data/catalog/gtdb_genomes-*.jsonl.gz`, `data/gold/projects.jsonl.gz` and `data/catalog/allthebacteria.tsv.xz` files. Both ATB rows have available FASTAs and passing assembly-pipeline, Sylph and HQ filters. Complete SeqKit sums and OSF/AWS location fields were inspected, not recomputed or downloaded; SeqKit sum is not MD5.

The other ten candidates are distinct GOLD community projects with empty organism GOLD fields, not HKF-5 strain-genome chains:

| `data/gold/projects.jsonl.gz` line | GOLD project | BioProject | BioSample | Inspected context |
| --- | --- | --- | --- | --- |
| 199259 | `Gp0297537` | `PRJNA502685` | `SAMN10350577` | Northeast subarctic Pacific, Canada; LP_J_2015_P26_10m |
| 199266 | `Gp0297544` | `PRJNA502691` | `SAMN10350579` | Saanich Inlet, British Columbia; SI112_135m |
| 199270 | `Gp0297548` | `PRJNA502695` | `SAMN10350578` | Separate Saanich Inlet sample; SI106_100 |
| 199272 | `Gp0297550` | `PRJNA502697` | `SAMN10350576` | Separate Saanich Inlet sample; SI106_135 |
| 199274 | `Gp0297552` | `PRJNA502699` | `SAMN10350575` | Separate Saanich Inlet sample; SI106_200 |
| 205699 | `Gp0306212` | `PRJNA502703` | `SAMN10350574` | Municipal landfill, Southern Ontario; leachate well 138R |
| 205701 | `Gp0306214` | `PRJNA502705` | `SAMN10350573` | Same landfill; methane capture system biofilm |
| 205714 | `Gp0306227` | `PRJNA502708` | `SAMN10350572` | Carex aquatilis rhizosphere, University of Washington, Seattle; 4-8-24 metaG |
| 205718 | `Gp0306231` | `PRJNA502710` | `SAMN10350571` | Separate Carex aquatilis rhizosphere sample; 4-12-25 metaG |
| 205729 | `Gp0306242` | `PRJNA502712` | `SAMN10350570` | Separate Carex aquatilis rhizosphere sample; 4-20-23 metaG |

These are review diagnostics only. No record, maintained input, generated product, curation history or completed Eukaryota review is changed.
