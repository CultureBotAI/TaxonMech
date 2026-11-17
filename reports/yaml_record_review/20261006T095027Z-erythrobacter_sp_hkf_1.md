# YAML Record Review: Erythrobacter sp. HKF-1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/erythrobacter_sp_hkf_1.yaml`
- Started UTC: 2026-10-06T09:46:01Z
- Finished UTC: 2026-10-06T09:50:27Z
- Verdict: pass

## Target

Read the complete 57-line generated `TaxonRecord` for `NCBITaxon:1035053`, Erythrobacter sp. HKF-1. It asserts species rank, bacterial domain, parent `NCBITaxon:2633097`, eleven root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. No optional synonyms, nomenclature, mappings, strain list, genome links, causal graph, evidence objects or discussions are asserted. This is a read-only review, not a curation event or lifecycle promotion.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/erythrobacter_sp_hkf_1.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/erythrobacter_sp_hkf_1.yaml --out /private/tmp/ehkf1-validation.tsv`: exit 0, one file scanned, zero errors. Read the header-only diagnostic TSV.
- Structured comparisons verified the complete source lineage, identity, genetic code, unique PATHS/scope rows, sole attestation and inline event wording. Exact scans of type-material, merged-ID and dropped-record inventories found no target rows.
- An ignored-inclusive identifier/name/slug search of `reports/yaml_record_review/` and `history/` found no prior report or separate history artifact before this report was written. The inline seed event is present and schema-valid; no review history is appended.
- Not checked: full-corpus `just qc`, `just verify-corpus`, `just validate-all`, `just test`, `just validate-history`, site drift and publication gates. Focused checks do not certify whole-corpus reproduction or release readiness. No focused term/reference/history validator was invented. `just validate-products` is inapplicable without curator-added graph nodes.

## Identity and Grounding

The complete backbone at `data/raw/ncbitaxon_taxa.tsv:221864` and native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31290` agree with the target. The index is `data/taxa/PATHS.tsv:14345`; maintained scope is `curation/seed_scope.tsv:322156`. The pinned backbone supplies no target synonyms, retirement target or classified children.

Read the complete [NCBI EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035053&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035053). They confirm the exact designation, species rank, bacterial placement, parent and genetic code 11. The complete stored chain agrees: root (`1`), cellular organisms (`131567`), Bacteria (`2`), Pseudomonadati (`3379134`), Pseudomonadota (`1224`), Alphaproteobacteria (`28211`), Sphingomonadales (`204457`), Erythrobacteraceae (`335929`), Erythrobacter/Porphyrobacter group (`2800788`), Erythrobacter (`1041`) and unclassified Erythrobacter (`2633097`). Datasets includes root; EFetch supplies the remaining labels and ranks. Exact NCBI grounding does not establish validly published species nomenclature or equivalence to a named Erythrobacter species.

## Evidence

The sole NCBITAXON attestation correctly counts one imported `NAME` from snapshot `2026-09-13`. The `2026-09-13T17:54:04Z` `SEEDED_FROM_SOURCES` event agrees with the maintained scope reason. Source counts describe imported coverage, not biological abundance or global source absence.

Exact non-expanded searches for `txid1035053[Organism:noexp]` returned zero NCBI Assembly entries and one Nuccore entry, UID `371939995`. Read all metadata, references and features for [AB633199.1](https://www.ncbi.nlm.nih.gov/nuccore/AB633199.1), excluding sequence bases. It is a 1,345-base 16S rRNA sequence, partial at both ends, not a genome. Source qualifiers explicitly name Erythrobacter sp. HKF-1, strain HKF-1 and `taxon:1035053`, with brackish-water isolation context in Lake Sanaru, Shizuoka, Japan. It was created and updated on 12 January 2012; the direct submission was 19 May 2011 by Hideyuki Tamegai and colleagues at Nihon University. Its source feature has no culture-collection, BioSample or assembly identifier.

The GenBank reference identifies a Fujimori et al. 2012 paper in Limnology and Oceanography 57:154-162, without a DOI/PMID cross-reference. The inspected [primary publisher page](https://aslopubs.onlinelibrary.wiley.com/doi/10.4319/lo.2012.57.1.0154) verifies the authors, title, journal coordinates and DOI `10.4319/lo.2012.57.1.0154`. Its abstract explicitly identifies HKF-1 as an Erythrobacter isolate studied for methyl-halide production. This supports isolate/literature identity, not a deposit or whole-genome association. The HTML exposed the abstract, not full experimental text; no production rate, phenotype or mechanism is added to the YAML.

The target asserts no genes, loci, regulatory relationships, pathways or transcriptomics claims. iModulonDB is therefore inapplicable to this identity-only review; this is not negative evidence about expression-module coverage.

## Completeness

Exact target-ID scans found no entries in the imported BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits tables. The zero imported strain count is consistent with the inspected inputs; it does not mean the experimental isolate does not exist.

The broader candidate search used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. It included ignored and compressed data, numeric taxon ID, full designation, slug and separator variants of HKF-1, then expanded to `AB633199`. Only `SOURCE.json` provenance sidecars were excluded from this candidate-data search; unrelated directories and external unindexed resources are outside its exhaustive-search claim.

Both searches returned the same 64 candidate rows. Every complete candidate was read using header-aware TSV or native JSON parsers, and address reconciliation found no unread or extra rows. Three concern this target: backbone, native name and scope. The remaining 61 are unrelated designation or numeric-substring matches, detailed below. In particular, ZFHKF-1 and GHKF11 are not HKF-1: their complete names and taxon/source chains identify different organisms. Their culture deposits, type-material annotations and genomes must not be transferred to this Erythrobacter record.

No eligible missing deposit or whole-genome association was identified within these bounds. Optional nomenclature, taxonomy mappings, genome fields, phenotypes and graph slots can remain empty. The marker sequence and primary article do not require inventing a named-species equivalence, deposit, genome or causal graph.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The bounded identity and imported-provenance claims agree with inspected evidence. The distinct ZFHKF-1/GHKF11 source identities are search exclusions, not an unresolved conflict about HKF-1.

## Recommended Edits

None required. Leave generated YAML, `SEEDED` status and curation history unchanged. Do not treat `AB633199.1` as a whole genome or import deposits/genomes from similarly spelled designations. A later verified taxonomy correction belongs upstream; scope changes belong in `curation/seed_scope.tsv`; an import or harmonization defect belongs in maintained source processing and `src/taxonmech/seed.py` with a regression test, not in a hand-edited generated record.

## Follow-up Checks

No blocking follow-up. A later source refresh may recheck the exact taxon/designation and marker for an explicit deposit-to-sample-to-genome chain. Any future phenotype enrichment should first inspect the relevant full experimental text and preserve strain/condition scope. After an actual curation change, run the focused validators and documented corpus reproduction, history, test and publication gates.

## Additional Notes

The NCBI taxonomy browser did not load through the web tool, but official taxonomy XML and Datasets succeeded. The 2012 publisher page supplied bibliographic information and an abstract; its full text and supplements were not audited. A ScienceDirect 2017 search lead (`S0304420317300932`) could not be opened through either abstract or article paths, so snippets were not used as evidence and that lead remains unverified. No paid access, messages or source mutations were used.

Disposition of the 61 unrelated candidates, all read in full:

| Candidate group | Rows | Inspected identity and exclusion |
| --- | --- | --- |
| Fictibacillus macauensis ZFHKF-1 | 22 | Taxon `1196324`, parent/species `245160`, old name Bacillus macauensis ZFHKF-1. BacDive `1245`, StrainInfo `289967`, deposits DSM 17262/JCM 13285/CIP 109160/NCIMB 14300, marker `AY373018`, assembly `GCA_000269865.1` paired with `GCF_000269865.1`, sample `SAMN02471793`, BV-BRC `1196324.3`, IMG `2524023182`, GOLD `Go0035254`/`Gp0035254`/`Ga0012808`. Different complete designation and genus. |
| Rhizobium sp. GHKF11 | 10 | Taxon `1805001`, sample `SAMN04500979`, project `PRJNA312606`, `GCA_001644925.1`, BV-BRC `1805001.3`, GOLD `Go0144798`/`Gp0150426`/`Ga0133081`, IMG `2744054783`. Historical RefSeq `GCF_001644925.1` is suppressed with unverified-source-organism exclusion. GTDB classifies its genome as Agrobacterium pusense. None identifies Erythrobacter HKF-1. |
| Staphylococcus haemolyticus 113101 | 6 | Taxon `1283`, sample `SAMEA1035053`, `GCA_001229185.1` paired with `GCF_001229185.1`, BV-BRC `1283.116`, GOLD `Gp0140413`/`Go0134530`, project `PRJEB2705`; ATB `ERR085269`/`ERZ3070490`. Sample-number substring only. |
| Mycobacterium tuberculosis | 2 | Run/designation `ERR1035053`, BV-BRC `1773.20488`, ATB sample `SAMEA3558586` and analysis `ERZ3501780`. Run-number substring only. |
| Nonomuraea sp. NPDC049419 | 3 | Taxon `3155772`, `GCA_040676995.1`/`GCF_040676995.1`, sample `SAMN41498124`; matched genome size `10350532`. GTDB calls the genome Nonomuraea salmonea. No relationship to HKF-1. |
| Bacteroides uniformis | 1 | Taxon `820`, strain `2201st1_B11_2201SCRN_220225`, `GCA_040928765.1`, sample `SAMN41035053`, project `PRJNA1093465`; no RefSeq partner and large multi-isolate project exclusion. Sample-number substring only. |
| Actinomycetota bacterium | 1 | Taxon `2900548`, isolate `NASQAN2011_332_B_bin.53`, `GCA_041170325.1`, sample `SAMN37153852`, project `PRJNA946291`; matched genome size `1035053`. Metagenome/genus-undefined exclusion, no RefSeq partner. |
| Sutterella sp. | 1 | Taxon `1981025`, isolate `UBA11837`, `GCA_003503795.1`, `SAMN08018967`, `PRJNA417962`; matched ungapped size `1035053`. Fragmented metagenome, no RefSeq partner. |
| Gammaproteobacteria bacterium | 1 | Taxon `1913989`, isolate `TARA_SAMEA2621295_MAG_00000027`, `GCA_983658495.1`, `SAMEA122618307`, `PRJEB103742`; matched genome size `1035053`. Fragmented metagenome/genus-undefined exclusion, no RefSeq partner. |
| Neisseria gonorrhoeae ATB | 3 | Runs `SRR10350533`, `SRR10350532`, `SRR10350531`; respective samples `SAMN12676038`, `SAMN12676039`, `SAMN12676040` and analyses `ERZ25635943`, `ERZ25635954`, `ERZ25635961`. Run-number substrings only. |
| Vibrio cholerae O1 biovar El Tor ATB | 1 | Run `SRR10350534`, sample `SAMN13118260`, analysis `ERZ25664729`. Run-number substring only. |
| GOLD community/plant/fungal projects | 10 | Distinct metatranscriptome samples detailed below, with empty organism GOLD fields. No HKF-1 strain-genome chain. |

The 22 ZFHKF-1 rows comprise legacy page 9483; scope 39886; backbone 269112; imported BacDive 1242; type-material 94807/94808; strain assemblies 10067/10068; strain-genome records 7764-7766; native BacDive 1241 and StrainInfo 225701; BV-BRC `0000:27996`; GOLD organism 30024, project 23823 and analysis 6967; native names `0006:37547/37548`; GenBank `0000:5853`; RefSeq `0000:4974`; GTDB `0013:9176`. StrainInfo's three displayed deposits have source-specific Bacillus/Fictibacillus names, not Erythrobacter; these native differences were not collapsed into the reviewed identity. The ten GHKF11 rows comprise scope 78723; backbone 471250; BV-BRC `0006:45384`; GOLD organism 83649, project 95474 and analysis 79091; native name `0011:8118`; GenBank `0001:13802`; historical RefSeq `0000:12453`; GTDB `0003:36193`. Counts are row dispositions, not numbers of distinct genomes.

All six inspected ATB rows retain available FASTAs and passing assembly-pipeline filters. The Staphylococcus row has failed Sylph/HQ filters; the other five have passing filters. Complete SeqKit sums and OSF/AWS location fields were inspected, not recomputed or downloaded. SeqKit sum is not MD5. Source-specific quality states do not justify attaching any of these assemblies to HKF-1.

| `data/gold/projects.jsonl.gz` line | GOLD project | BioProject | BioSample | Inspected context |
| --- | --- | --- | --- | --- |
| 196090 | `Gp0293454` | `PRJNA502360` | `SAMN10350530` | St. Lawrence River freshwater community, New York; Law_Law_RepA_8d |
| 223285 | `Gp0326558` | `PRJNA502289` | `SAMN10350539` | Pisolithus croceorhizus 76C/Eucalyptus grandis ectomycorrhiza, Australia; 76C_ECM_1 |
| 223287 | `Gp0326560` | `PRJNA502291` | `SAMN10350538` | Separate project in the same fungal/plant context; 76C_ECM_3 |
| 226702 | `Gp0331462` | `PRJNA502292` | `SAMN10350534` | Pinus banksiana/Suillus, Duke University, North Carolina; S112(MN)xP.bank(MN)_rep1 |
| 226703 | `Gp0331463` | `PRJNA502293` | `SAMN10350533` | Separate Pinus banksiana/Suillus project; S112(MN)xP.bank(MN)_rep2 |
| 226706 | `Gp0331466` | `PRJNA502296` | `SAMN10350532` | Pinus contorta/Suillus, Duke University; S112(MN)xP.contorta(CO)_rep2 |
| 226708 | `Gp0331468` | `PRJNA502298` | `SAMN10350531` | Separate Pinus contorta/Suillus project; S112(MN)xP.contorta(CA)_rep1 |
| 228106 | `Gp0333711` | `PRJNA502247` | `SAMN10350537` | Pinaceae seedling/Suillus ectomycorrhiza, Michigan; A217 |
| 228108 | `Gp0333713` | `PRJNA502249` | `SAMN10350536` | Separate Pinaceae/Suillus project, Michigan; A219 |
| 228110 | `Gp0333715` | `PRJNA502251` | `SAMN10350535` | Separate Pinaceae/Suillus project, Michigan; A221 |

These are review diagnostics only. No record, maintained input, generated product, curation history or completed Eukaryota review is changed.
