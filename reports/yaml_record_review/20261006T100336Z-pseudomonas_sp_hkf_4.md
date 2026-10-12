# YAML Record Review: Pseudomonas sp. HKF-4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_hkf_4.yaml`
- Started UTC: 2026-10-06T10:01:10Z
- Finished UTC: 2026-10-06T10:03:36Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1035056`, Pseudomonas sp. HKF-4. It asserts species rank, bacterial domain, parent `NCBITaxon:196821`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. No optional synonyms, nomenclature, taxonomy mappings, strain list, genome links, causal graph, evidence objects or discussions are asserted. This read-only review does not promote the record or append curation history.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_hkf_4.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_hkf_4.yaml --out /private/tmp/phkf4-validation.tsv`: exit 0, one file scanned, zero errors. Read the header-only diagnostic TSV.
- Structured comparisons verified the entire source lineage, identity, genetic code, unique PATHS/scope rows, sole attestation and inline event wording. Exact scans of type-material, merged-ID and dropped-record inventories found no target rows.
- An ignored-inclusive identifier/name/slug/designation search of `reports/yaml_record_review/` and `history/` found no prior report or separate history artifact before this report was written. The inline seed event is present and schema-valid.
- Not checked: full-corpus `just qc`, `just verify-corpus`, `just validate-all`, `just test`, `just validate-history`, site drift and publication gates. Focused checks do not certify whole-corpus reproduction or release readiness. No focused term/reference/history validator was invented. `just validate-products` is inapplicable without curator-added graph nodes.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:221867` and native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31293` agree with the target. The index is `data/taxa/PATHS.tsv:14348`; maintained scope is `curation/seed_scope.tsv:322159`. The pinned backbone supplies no target synonyms, retirement target or classified children.

Read the complete [NCBI EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035056&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035056). They confirm the exact designation, species rank, bacterial domain, parent and genetic code 11. The complete stored chain agrees: root (`1`), cellular organisms (`131567`), Bacteria (`2`), Pseudomonadati (`3379134`), Pseudomonadota (`1224`), Gammaproteobacteria (`1236`), Pseudomonadales (`72274`), Pseudomonadaceae (`135621`), Pseudomonas (`286`) and unclassified Pseudomonas (`196821`). Datasets includes root; EFetch supplies the other ancestor labels/ranks. Exact grounding does not establish validly published species nomenclature or equivalence to another Pseudomonas species.

## Evidence

The sole NCBITAXON attestation correctly counts one imported `NAME` from snapshot `2026-09-13`. The `2026-09-13T17:54:04Z` `SEEDED_FROM_SOURCES` event agrees with the maintained scope reason. Source counts describe imported records, not biological abundance or global source absence.

Exact non-expanded searches for `txid1035056[Organism:noexp]` returned zero NCBI Assembly entries and one Nuccore entry, UID `371939998`. Read all metadata, references and features for [AB633202.1](https://www.ncbi.nlm.nih.gov/nuccore/AB633202.1), excluding bases. It is a 1,392-base 16S rRNA marker, partial at both ends, not a whole genome. Source qualifiers explicitly identify Pseudomonas sp. HKF-4, strain HKF-4 and `taxon:1035056`, with brackish-water isolation context in Lake Sanaru, Shizuoka, Japan. Created/updated 12 January 2012; direct submission 19 May 2011 by Hideyuki Tamegai and colleagues at Nihon University. No culture-collection, BioSample or assembly qualifier is present in the inspected source feature.

GenBank cites Fujimori et al., Limnology and Oceanography 57:154-162 (2012), without a DOI/PMID cross-reference. The inspected [primary publisher page](https://aslopubs.onlinelibrary.wiley.com/doi/10.4319/lo.2012.57.1.0154) verifies authors, title, journal coordinates and DOI `10.4319/lo.2012.57.1.0154`. Its abstract describes the Erythrobacter/Pseudomonas isolate study but names HKF-1 rather than HKF-4 individually. GenBank supplies the specific HKF-4 connection; it is not inferred from the abstract. The article's full experimental text and supplements were not audited.

The research team's [KAKEN project 23310010 results report](https://kaken.nii.ac.jp/ja/file/KAKENHI-PROJECT-23310010/23310010seika.pdf), dated 22 May 2014, was inspected as text and rendered pages 1, 3, 4 and 5 earlier in this review session. Its Lake Sanaru methods/results place HKF-2 through HKF-5 in Pseudomonas, separately from Erythrobacter HKF-1; its publication list supplies the same 2012 DOI. Its culture-collection comparator strains are not stated to be deposits of HKF-4, and Figure 1 concerns HKF-1. Neither a deposit equivalence nor HKF-1 experimental values are transferred.

Read the complete one-page [J-STAGE conference abstract PR0004](https://www.jstage.jst.go.jp/article/geochemproc/72/0/72_7/_pdf/-char/en) by S. Hashimoto, Y. Okuda and H. Yamashita, in text and as a rendered page. It explicitly distinguishes Pseudomonas HKF-4 from Phaeobacter gallaeciensis JCM 21319 and the diatom CCMP358 in brominated-methane experiments. It supplies designation-level study context but no HKF-4 deposit, BioSample, nucleotide or assembly accession. JCM 21319 belongs to the comparator, not HKF-4. Quantitative rates and broader environmental extrapolations were not added to the record. This conference abstract is not a substitute for reviewing the inaccessible full journal article.

iModulonDB is inapplicable to the identity-only target, which asserts no genes, loci, regulators, pathways or transcriptomics claims. Finding external phenotype literature does not require adding an expression-module or mechanistic claim.

## Completeness

Exact target-ID scans found no entries in the imported BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits tables. The zero imported strain count is consistent with those inputs; it does not deny the existence of the experimental isolate.

The candidate search used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. It included ignored/compressed data, numeric taxon ID, designation, slug and HKF-4 separator variants, then expanded to `AB633202`. Only `SOURCE.json` provenance sidecars were excluded from this candidate-data search; unrelated directories and external unindexed sources are outside its exhaustive-search claim.

Both searches returned the same 27 rows. Every complete candidate was read with header-aware TSV or native JSON parsers; address reconciliation found no unread or extra rows. Three rows concern the target: backbone, native name and scope. The remaining 24 are unrelated designation or number-substring matches, detailed below. Penicillium HKF42 is not HKF-4; its organism identity and complete designation exclude it. No eligible missing culture deposit or whole-genome association was identified within these bounds. Optional nomenclature, mappings, genome and graph slots can remain empty.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage and imported provenance agree with inspected evidence. The additional study context does not establish a required missing representation or an error in the current claims.

## Recommended Edits

None required. Leave generated YAML, `SEEDED` status and history unchanged. Do not turn `AB633202.1` into a genome, import Penicillium HKF42 resources, or assign the comparator's JCM 21319 deposit to HKF-4. Later taxonomy corrections belong upstream; verified scope changes belong in `curation/seed_scope.tsv`; import/harmonization defects belong in maintained extraction and `src/taxonmech/seed.py` with regression tests, not a manual generated-record patch.

## Follow-up Checks

No blocking follow-up. A later source refresh may recheck the exact taxon/designation and marker for an explicit deposit-to-sample-to-genome chain. Any proposed phenotype enrichment requires full experimental-text review and strain/condition-specific evidence. After actual curation, run the focused validators plus documented corpus reproduction, history, test and publication gates.

## Additional Notes

The NCBI browser did not load through the web tool; official EFetch and Datasets succeeded. The ScienceDirect journal lead `S030442032400094X` returned inaccessible/403 results on abstract and article paths, so search snippets were not used as evidence. J-STAGE web requests timed out, but a public PDF download succeeded and local PDFKit rendering allowed inspection of the complete conference abstract. Poppler was unavailable. No paid access, outbound messages or source mutations were used.

Full-row dispositions of fourteen unrelated strain/genome candidates:

| Source rows | Identity and exclusion |
| --- | --- |
| BV-BRC `0001:18927`; GenBank `0000:45298`; RefSeq `0000:38096`; GTDB `0002:40041`; GOLD projects `87434`; ATB `66036` | Six Staphylococcus haemolyticus 95671 rows: taxon `1283`, sample `SAMEA1035056`, `GCA_001227205.1`/`GCF_001227205.1`, BV-BRC `1283.98`, GOLD `Gp0140492`/`Go0134609`, project `PRJEB2705`, ATB `ERR085231`/`ERZ3070495`. Sample-number substring only. |
| BV-BRC `0006:8509`; ATB `569526` | Mycobacterium tuberculosis `ERR1035056`, BV-BRC `1773.20494`, ATB sample `SAMEA3558589`/analysis `ERZ3501797`. Run-number substring only. |
| ATB `107805` | Escherichia coli run `ERR3062006`, sample `SAMEA104370105`, analysis `ERZ25099922`; matched digits inside the SeqKit sum, not taxon identity. |
| GenBank `0037:21039` | Bacteroides uniformis, taxon `820`, strain `RTP21002st2_G1_RTP21002_201210`, `GCA_040928705.1`, `SAMN41035056`, `PRJNA1093465`; no RefSeq partner, large multi-isolate project exclusion. |
| GenBank `0009:6364` | Campylobacter jejuni PNUSAC013610, taxon `197`, `GCA_010350565.1`, `SAMN13347990`, `PRJNA239251`; no RefSeq partner, large multi-isolate project exclusion. Assembly-number substring only. |
| GOLD organism `279616`, project `156065`, analysis `131489` | Penicillium chrysogenum HKF42, taxon `5076`, `Go0384210`/`Gp0235300`/`Ga0212774`, project `PRJNA369334`, sample `SAMN06284326`, `GCA_002080375.1`, WGS `MWKT00000000`. Empty culture-collection field. Different organism and designation; no Eukaryota review was reopened. |

Abbreviated source names refer to the inspected `data/bvbrc/bvbrc-*.jsonl.gz`, `data/catalog/ncbi_*.jsonl.gz`, `data/catalog/gtdb_genomes-*.jsonl.gz`, `data/gold/*.jsonl.gz` and `data/catalog/allthebacteria.tsv.xz` files. All three ATB rows have available FASTAs and passing assembly-pipeline, Sylph and HQ filters. Complete SeqKit sums and OSF/AWS location fields were inspected, not recomputed or downloaded; SeqKit sum is not MD5.

The other ten candidates are distinct GOLD community projects with empty organism GOLD fields, not HKF-4 strain-genome chains:

| `data/gold/projects.jsonl.gz` line | GOLD project | BioProject | BioSample | Inspected context |
| --- | --- | --- | --- | --- |
| 205731 | `Gp0306244` | `PRJNA502713` | `SAMN10350569` | Carex aquatilis rhizosphere, University of Washington, Seattle; 4-21-19 metaG |
| 205739 | `Gp0306252` | `PRJNA502716` | `SAMN10350568` | Plant litter, Maridalen valley, Oslo, Norway; NLE2 |
| 205740 | `Gp0306253` | `PRJNA502717` | `SAMN10350567` | Separate Maridalen plant-litter sample; NLE4 |
| 205742 | `Gp0306255` | `PRJNA502719` | `SAMN10350566` | Separate Maridalen plant-litter sample; NLE6 |
| 205743 | `Gp0306256` | `PRJNA502720` | `SAMN10350565` | Maridalen soil community; NSE1 |
| 205745 | `Gp0306258` | `PRJNA502722` | `SAMN10350564` | Separate Maridalen soil sample; NSE4 |
| 205746 | `Gp0306259` | `PRJNA502723` | `SAMN10350563` | Separate Maridalen soil sample; NSE5 |
| 205749 | `Gp0306262` | `PRJNA502726` | `SAMN10350562` | Maridalen rhizosphere community; NZE2 |
| 205750 | `Gp0306263` | `PRJNA502727` | `SAMN10350561` | Separate Maridalen rhizosphere sample; NZE4 |
| 205752 | `Gp0306265` | `PRJNA502729` | `SAMN10350560` | Separate Maridalen rhizosphere sample; NZA6 |

These are review diagnostics only. No record, maintained input, generated product, curation history or completed Eukaryota review is changed.
