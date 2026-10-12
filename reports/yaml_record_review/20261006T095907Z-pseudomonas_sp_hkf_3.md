# YAML Record Review: Pseudomonas sp. HKF-3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_hkf_3.yaml`
- Started UTC: 2026-10-06T09:57:05Z
- Finished UTC: 2026-10-06T09:59:07Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1035055`, Pseudomonas sp. HKF-3. It asserts species rank, bacterial domain, parent `NCBITaxon:196821`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. No optional synonyms, nomenclature, taxonomy mappings, strain list, genome links, causal graph, evidence objects or discussions are asserted. This read-only review does not promote the record or append curation history.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_hkf_3.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_hkf_3.yaml --out /private/tmp/phkf3-validation.tsv`: exit 0, one file scanned, zero errors. Read the header-only diagnostic TSV.
- Structured comparisons verified the entire source lineage, identity, genetic code, unique PATHS/scope rows, sole attestation and inline event wording. Exact scans of type-material, merged-ID and dropped-record inventories found no target rows.
- An ignored-inclusive identifier/name/slug/designation search of `reports/yaml_record_review/` and `history/` found no prior report or separate history artifact before this report was written. The inline seed event is present and schema-valid.
- Not checked: full-corpus `just qc`, `just verify-corpus`, `just validate-all`, `just test`, `just validate-history`, site drift and publication gates. Focused checks do not certify whole-corpus reproduction or release readiness. No focused term/reference/history validator was invented. `just validate-products` is inapplicable without curator-added graph nodes.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:221866` and native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31292` agree with the target. The index is `data/taxa/PATHS.tsv:14347`; maintained scope is `curation/seed_scope.tsv:322158`. The pinned backbone supplies no target synonyms, retirement target or classified children.

Read the complete [NCBI EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035055&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035055). They confirm the exact designation, species rank, bacterial domain, parent and genetic code 11. The complete stored chain agrees: root (`1`), cellular organisms (`131567`), Bacteria (`2`), Pseudomonadati (`3379134`), Pseudomonadota (`1224`), Gammaproteobacteria (`1236`), Pseudomonadales (`72274`), Pseudomonadaceae (`135621`), Pseudomonas (`286`) and unclassified Pseudomonas (`196821`). Datasets includes root; EFetch supplies the other ancestor labels/ranks. Exact grounding to this NCBI node does not establish validly published species nomenclature or equivalence to another Pseudomonas species.

## Evidence

The sole NCBITAXON attestation correctly counts one imported `NAME` from snapshot `2026-09-13`. The `2026-09-13T17:54:04Z` `SEEDED_FROM_SOURCES` event agrees with the maintained scope reason. These counts describe imported records, not biological abundance or global source absence.

Exact non-expanded searches for `txid1035055[Organism:noexp]` returned zero NCBI Assembly entries and one Nuccore entry, UID `371939997`. Read all metadata, references and features for [AB633201.1](https://www.ncbi.nlm.nih.gov/nuccore/AB633201.1), excluding bases. It is a 1,392-base 16S rRNA marker, partial at both ends, not a whole genome. Source qualifiers explicitly identify Pseudomonas sp. HKF-3, strain HKF-3 and `taxon:1035055`, with brackish-water isolation context in Lake Sanaru, Shizuoka, Japan. Created/updated 12 January 2012; direct submission 19 May 2011 by Hideyuki Tamegai and colleagues at Nihon University. No culture-collection, BioSample or assembly qualifier is present in the inspected source feature.

GenBank cites Fujimori et al., Limnology and Oceanography 57:154-162 (2012), without a DOI/PMID cross-reference. The [primary publisher page](https://aslopubs.onlinelibrary.wiley.com/doi/10.4319/lo.2012.57.1.0154), inspected during this review session, verifies authors, title, journal coordinates and DOI `10.4319/lo.2012.57.1.0154`. The abstract describes the Erythrobacter/Pseudomonas isolate study but names HKF-1 rather than HKF-3 individually. GenBank supplies the specific HKF-3 connection; it is not inferred from the abstract. The article's full experimental text and supplements were not audited.

The research team's [KAKEN project 23310010 results report](https://kaken.nii.ac.jp/ja/file/KAKENHI-PROJECT-23310010/23310010seika.pdf), dated 22 May 2014, was inspected as text and rendered pages 1, 3, 4 and 5 during this session. Its Lake Sanaru methods/results place HKF-2 through HKF-5 in Pseudomonas, separately from Erythrobacter HKF-1; the publication list supplies the same 2012 DOI. Its culture-collection comparator strains are not stated to be deposits of HKF-3, and Figure 1 concerns HKF-1. No deposit equivalence or HKF-1 production value is transferred.

A later [primary research article on Cuatro Cienegas methylotrophs](https://medcraveonline.com/JMEN/diversity-of-cultivated-methylotrophs-from-theextremely-oligotrophic-system-in-the-cuatrocienegas-basin-mexico-an-unexplored-ecologicalguildnbsp.html), DOI `10.15406/jmen.2022.10.00375`, was inspected at its bibliographic header, methods and phylogenetic-results sections. It reports 97.13% sequence identity between its isolate A24 and HKF-3. HKF-3 is a sequence comparator, not the Mexican isolate A24. That study does not establish A24/HKF-3 identity, a new HKF-3 deposit or HKF-3 methylotrophy. This distinction prevents evidence transfer; the YAML currently makes none of those claims.

iModulonDB is inapplicable to this identity-only record, which asserts no genes, loci, regulators, pathways or transcriptomics claims. Finding a comparator-based gene/trait study does not justify adding expression-module or phenotype assertions to HKF-3.

## Completeness

Exact target-ID scans found no entries in the imported BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits tables. The zero imported strain count is consistent with those inputs; it does not deny the existence of the experimental isolate.

The candidate search used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. It included ignored/compressed data, numeric taxon ID, designation, slug and HKF-3 separator variants, then expanded to `AB633201`. Only `SOURCE.json` provenance sidecars were excluded from this candidate-data search; unrelated directories and external unindexed sources are outside its exhaustive-search claim.

Both searches returned the same 29 rows. Every complete candidate was read with header-aware TSV or native JSON parsers; address reconciliation found no unread or extra rows. Three rows concern the target: backbone, native name and scope. The other 26 are unrelated number-substring matches, detailed below. No eligible missing culture deposit or genome association was identified within these bounds. Optional nomenclature, mappings, genome and graph slots can remain empty. A marker-sequence neighbor in another experiment is not a strain synonym.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage and imported provenance agree with inspected evidence. The comparator-study scope caution is not a defect in this record, which makes no corresponding phenotype or synonym claim.

## Recommended Edits

None required. Leave generated YAML, `SEEDED` status and history unchanged. Do not treat `AB633201.1` as a whole genome, merge A24 with HKF-3, or attach evidence from HKF-1 to HKF-3. Later taxonomy corrections belong upstream; verified scope changes belong in `curation/seed_scope.tsv`; import/harmonization defects belong in maintained extraction and `src/taxonmech/seed.py` with regression tests, not a manual generated-record patch.

## Follow-up Checks

No blocking follow-up. A later source refresh may recheck the exact taxon/designation and marker for an explicit deposit-to-sample-to-genome chain. Any proposed phenotype enrichment requires full experimental-text review and strain/condition-specific evidence, not nearest-neighbor assignment. After actual curation, run the focused validators plus documented corpus reproduction, history, test and publication gates.

## Additional Notes

The NCBI browser did not load through the web tool; official EFetch and Datasets succeeded. The KAKEN PDF was downloaded publicly and visually inspected through local PDFKit after incomplete web extraction and screenshot timeouts; Poppler was unavailable. A separate 2016 Food Science/ScienceEngine PDF search lead could not be inspected reliably: subsequent page and screenshot requests returned 403. Its search snippets were not used as evidence, and that lead remains unverified. No paid access, messages or source mutations were used.

Full-row dispositions of sixteen unrelated strain/genome candidates:

| Source rows | Identity and exclusion |
| --- | --- |
| BV-BRC `0001:18190`; GenBank `0000:45568`; RefSeq `0000:38356`; GTDB `0009:8096`; GOLD projects `87455`; ATB `66035` | Six Staphylococcus haemolyticus 51-39 rows: taxon `1283`, sample `SAMEA1035055`, `GCA_001232605.1`/`GCF_001232605.1`, BV-BRC `1283.140`, GOLD `Gp0140513`/`Go0134630`, project `PRJEB2705`, ATB `ERR085201`/`ERZ3070496`. Sample-number substring only. |
| BV-BRC `0006:8507`; ATB `569525` | Mycobacterium tuberculosis `ERR1035055`, BV-BRC `1773.20492`, ATB sample `SAMEA3558588`/analysis `ERZ3501779`. Run-number substring only. |
| ATB `988940` | Chlamydia trachomatis run `ERR6491827`, sample `SAMEA9664119`, analysis `ERZ25456656`; matched digits inside the SeqKit sum, not taxon identity. |
| GOLD organisms `125650` | Shigella boydii EDBN 201035055, taxon `621`, `Go0187422`, empty culture-collection field. Different organism and full designation. |
| GenBank `0056:27279` | Blautia fusiformis, taxon `2881264`, isolate `1755_1755K_C_7`, `GCA_061035055.1`, `SAMN60702902`, `PRJNA1464738`; metagenome-derived, no RefSeq partner. Assembly-number substring only. |
| Historical GenBank `0001:21177/21178`; current GenBank `0028:43441` | Klebsiella pneumoniae, taxon `573`, isolate `1923636`, `GCA_031035055.1/.2/.3`, sample `SAMN34998356`, project `PRJNA288601`. Versions 1 and 2 are replaced; version 3 is latest in the snapshot. All have large multi-isolate project exclusion and no RefSeq partner. These are versions of an unrelated assembly, not three HKF-3 genomes. |
| GenBank `0037:25641` | Different Klebsiella pneumoniae strain `zj02057`, `GCA_041035055.1`, `SAMN37542647`, `PRJNA1021041`; large multi-isolate project exclusion, no RefSeq partner. |
| GenBank `0037:21037` | Bacteroides uniformis, taxon `820`, strain `RTP21002st2_E4_RTP21002_201210`, `GCA_040928665.1`, `SAMN41035055`, `PRJNA1093465`; large multi-isolate project exclusion, no RefSeq partner. |

Abbreviated source names refer to the inspected `data/bvbrc/bvbrc-*.jsonl.gz`, `data/catalog/ncbi_*.jsonl.gz`, `data/catalog/gtdb_genomes-*.jsonl.gz`, `data/gold/*.jsonl.gz` and `data/catalog/allthebacteria.tsv.xz` files. All three ATB rows have available FASTAs and passing assembly-pipeline filters. The Chlamydia row fails Sylph/HQ filters; the other two pass. Complete SeqKit sums and OSF/AWS location fields were inspected, not recomputed or downloaded; SeqKit sum is not MD5.

The other ten candidates are distinct GOLD community/fungal projects with empty organism GOLD fields, not HKF-3 strain-genome chains:

| `data/gold/projects.jsonl.gz` line | GOLD project | BioProject | BioSample | Inspected context |
| --- | --- | --- | --- | --- |
| 199258 | `Gp0297536` | `PRJNA502684` | `SAMN10350559` | Northeast subarctic Pacific marine community, Canada; LP_J_2011_P26_2000m |
| 199261 | `Gp0297539` | `PRJNA502687` | `SAMN10350558` | Separate northeast Pacific community; LP_J_2015_P26_1000m |
| 199265 | `Gp0297543` | `PRJNA502690` | `SAMN10350557` | Saanich Inlet marine community, British Columbia; SI112_120m |
| 199269 | `Gp0297547` | `PRJNA502694` | `SAMN10350556` | Separate Saanich Inlet sample; SI106_10 |
| 199273 | `Gp0297551` | `PRJNA502698` | `SAMN10350555` | Separate Saanich Inlet sample; SI106_150 |
| 205792 | `Gp0306336` | `PRJNA502731` | `SAMN10350554` | Sakinaw Lake saline-water community, British Columbia; sak_2011_5_24_36m |
| 205793 | `Gp0306337` | `PRJNA502732` | `SAMN10350553` | Separate Sakinaw Lake sample; sak_2011_5_24_80m |
| 205794 | `Gp0306338` | `PRJNA502733` | `SAMN10350552` | Separate Sakinaw Lake sample; sak_2013_06_06_50m |
| 205883 | `Gp0306427` | `PRJNA502736` | `SAMN10350551` | Plant-litter microbial community, East Loma Ridge, Irvine, California; P2 T30 |
| 205887 | `Gp0306431` | `PRJNA502740` | `SAMN10350550` | Enriched fungal community from goat fecal pellet, Isla Vista, California; bagasse Gen10 Rep2, chloramphenicol |

These are review diagnostics only. No record, maintained input, generated product, curation history or completed Eukaryota review is changed.
