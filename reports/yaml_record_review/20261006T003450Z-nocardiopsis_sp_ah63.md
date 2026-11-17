# YAML Record Review: Nocardiopsis sp. AH63

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah63.yaml`
- Started UTC: 2026-10-06T00:30:04Z
- Finished UTC: 2026-10-06T00:34:50Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034883`, Nocardiopsis sp. AH63, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It asserts ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero classified BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, xrefs, literature evidence or causal graph are asserted.

`data/taxa/PATHS.tsv:14202` uniquely resolves this ID and stem; `curation/seed_scope.tsv:322035` supplies inclusion. Only this new report was written. Records, inputs, scope, history and Eukaryota were untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah63.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah63.yaml --out /private/tmp/ah63-validation.tsv`, exit 0, one file, zero errors. The TSV was read and contains only its header.
- PASS: complete backbone row, reconstructed lineage, seven inventories, PATHS, scope, source attestation and seed-event text agree. No target children occur in the backbone.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, full target and conflicting-accession metadata/references/features, primary-paper text and Figure 3, full native culture objects, and live BacDive/DSMZ pages.
- Access limitation resolved: web-tool fetches of BacDive and DSMZ failed; direct public HTML reads then succeeded, and their complete visible text was read. No account or external write was used.
- Not applicable: graph-term, LPSN/GTDB mapping and iModulonDB checks. No corresponding graph, mapping, gene/regulator or expression-module assertion is present.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. These bounded checks do not prove corpus reproduction or publication readiness.

Required guidance, schema and seeder behavior were fully read in preceding reviews at the same HEAD. The review skill, checklist, strain-count schema and relevant BacDive/seeder implementation were reread for this target. Guidance/schema/seeder/target diffs were empty. No history entry or human REVIEWED promotion was made.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034883&retmode=xml) confirms exact ID, name, species rank, bacterial division, parent and code 11. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034883) agrees and supplies all ten ancestor IDs, including root.

The root-first chain matches the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies non-root ancestry; Datasets includes root explicitly.

The informal name does not assert validly published nomenclature. A sequence's strain qualifier does not change the NCBI concept's rank. `EXACT` grounds this taxon, not equivalence to N. litoralis, AH65 or another organism called AH63.

## Evidence

| Assertion | Inspected support |
|---|---|
| Identity, parent, rank and code | Complete `data/raw/ncbitaxon_taxa.tsv:221732` and both NCBI authorities. |
| Lineage | Full reconstructed backbone chain and authority ancestry. |
| Scientific name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31135`; backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | Source, ID, label, unit, count and snapshot note agree with the backbone. NAME is not a strain or genome count. |
| Inclusion and event | Scope line 322035 supplies 2026-09-13 and the exact one-source attested-rule reason; seed-event text agrees. |
| Seed timestamp | 2026-09-13T17:54:04Z is the maximum of raw 17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z extraction times on that date, following `src/taxonmech/seed.py:139`. |
| Zero classified strains | No BacDive inventory association under this taxon and no backbone children. This is a source-classification count, not evidence that AH63 lacks a deposited culture. |

Exact `txid1034883[Organism:noexp]` queries returned zero Assembly items with phrase-not-found/no-items messages and one Nuccore UID, 333497032. Complete [JF777528.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497032), references and features were read, excluding bases. It is a 1,411-base partial 16S marker with AH63, taxon 1034883, Saharan soil, Algeria and collection year 2010, but no culture-collection qualifier. References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished study and direct submission on 2011-03-07; no DOI or PMID is supplied. A marker is not a genome, and the Assembly query does not exclude records filed under other classifications.

The complete native culture chain was inspected:

- `data/raw/bacdive_strains.tsv:53353`: `kgmicrobe.strain:bacdive_131042`, AH63, DSM 45471, classified under taxon 310350.
- `data/bacdive/records.jsonl.gz:53352`: BacDive 131042, DOI 10.13145/bacdive131042.20260601.11, AH63, non-type, DSM 45471 and StrainInfo 400847. General classification is taxon 310350 at species matching level; the 16S object explicitly identifies JF777528, AH63, taxon 1034883 and 1,411 bases. No Genome sequences object is present.
- `data/straininfo/records.jsonl.gz:298736`: SI-ID 400847, DOI 10.60712/SI-ID400847.2, published online, BacDive 131042 and its own available DSM 45471 deposit SI-DP 907735. Both strain and deposit use genus taxon 2013, not 1034883; no sequence entry is supplied. Deposit provenance, statuses and archived version metadata were read in full.
- `data/straininfo/strain_links.tsv:10886` and `related_records.tsv.gz:27847-27848`: the exact own-deposit match connects DSM 45471, SI-DP 907735, SI-ID 400847 and BacDive 131042. Typed StrainInfo deposit/strain records are not genomes.
- `data/raw/culture_collection_strains.tsv:81472`: DSM 45471 is classified under taxon 310350.

The [live BacDive record](https://bacdive.dsmz.de/strain/131042) corroborates the culture, general taxon 310350 and distinct sequence taxon 1034883. The [DSMZ catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-45471) explicitly connects DSM 45471, AH63, Algerian Saharan soil and JF777528. This is positive deposit-to-marker evidence, stronger than a designation-only match. DSMZ gives sampling year 2003, conflicting with GenBank's 2010; the discrepancy remains unresolved. Peripheral catalogue widget text was not treated as authoritative identity evidence.

`strain_count` is defined by `src/taxonmech/schema/taxonmech.yaml:213` as BacDive records classified under the taxon/subtree. `src/taxonmech/bacdive_v2.py:55` deliberately uses General taxonomy, not 16S taxonomy; `src/taxonmech/seed.py:487` consumes those classifications. Its genome adapter reads Genome sequences, not 16S entries. Thus the observed zero is faithful to current classification semantics despite the positive marker association. Silently replacing General taxonomy with sequence taxonomy would change the model, not repair an established count error.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, reports 98.4% AH63 similarity to N. litoralis, not species equivalence. Figure 3 labels AH63 as JF777529, whereas NCBI, BacDive and DSMZ link AH63 to JF777528. Its reported sequence-length range of 1,529-1,544 bases also differs from 1,411. Full [JF777529.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=JF777529) identifies AH65, taxon 1034884, and a 1,418-base partial 16S marker. Do not silently substitute that accession or decide which source contains a typo. Neither accession, length nor sampling date is asserted by this YAML.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034883. Empty optional slots agree with the inputs. The culture/marker association above is retained as an enrichment lead, not discarded or misrepresented as absent.

Bounded searches included ignored/hidden files and compressed catalogs:

- `rg --no-ignore --hidden -n -z -i` searched ID, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All 12 matches were read fully: three target backbone/name/scope rows, one BacDive sequence object and eight numeric substring matches.
- An AH63/AH-63/AH 63/AH_63 screen across those roots returned 12 rows: three target, three culture, three other-NCBI-concept and three genome rows. All were read fully as native JSON or header-aware TSV, with address reconciliation.
- DSM 45471, BacDive 131042 and typed StrainInfo 400847/907735 identifier variants returned the seven full culture-chain rows above, without a genome match in this bounded search.
- JF777528/JF777529 returned one native BacDive row, matching only JF777528. No local JF777529 row occurred within these bounds; no global absence is claimed.
- Before writing, ignored-inclusive ID/full-label/slug searches in reports/history found only two AH63 mentions in the preceding AH62 report, not a target review. `find` found no prior exact-stem AH63 report.

No required missing representation was established under the current schema and classification contract. Optional literature/marker enrichment would benefit from resolving the external conflicts and preserving distinct taxonomic assignments. No exhaustive external culture/genome census or all-alias search is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's assertions. The review preserves three unresolved source issues without silently resolving them: culture/general versus marker taxonomy, DSMZ versus GenBank sampling year, and paper versus accession-authority identifiers/lengths. They constrain future enrichment but do not invalidate the current count or other asserted fields.

## Recommended Edits

None required on current evidence. Do not hand-edit generated YAML, set the count to one solely from marker taxonomy, treat 16S as a genome, transfer AH65's accession, infer N. litoralis equivalence or promote lifecycle to REVIEWED.

A future source-classification correction belongs in the upstream source and maintained extraction logic, particularly `src/taxonmech/bacdive_v2.py:55`, with regression coverage; `src/taxonmech/seed.py` owns generated taxon publication. A new sequence-supported association needs an explicit schema and persistence policy that preserves General and sequence taxonomies separately. `curation/seed_scope.tsv` owns inclusion, not specimen identity. Optional literature enrichment also needs a supported maintained mechanism rather than direct generated-YAML edits.

## Follow-up Checks

- Resolve the paper accession/length and DSMZ/GenBank sampling-year conflicts before copying those details. No author, depositor or source curator was contacted.
- Retain the explicit DSM 45471/AH63/JF777528 link and source versions when evaluating enrichment; seek authoritative classification clarification rather than assuming a marker taxon overrides culture taxonomy.
- Any proposed adapter change needs a regression case with different General and 16S taxon IDs and a check that markers never become genome entries. Validate an authorized canary, then run `just verify-corpus` and `just qc`; those gates did not run here.
- Reconcile reports against actual YAML files independently of ignore rules. A review report does not confer human REVIEWED status.

## Additional Notes

Other designation matches were read and kept separate:

- Burkholderia sp. AH63, taxon 861703: scope line 285675, backbone line 181212, names shard 0004 line 34896, parent 2613784.
- N. gonorrhoeae ah63, taxon 485: GCA_046241935.1, SAMEA114004407, GenBank shard 0042 line 32144.
- K. pneumoniae AH63, taxon 573: GCA/GCF_057664845.1, SAMN54997892, GenBank shard 0053 line 16193 and RefSeq shard 0008 line 44155.

All eight numeric substring matches were also read in full:

- M. tuberculosis ERR1034883, taxon 1773: BV-BRC shard 0006 line 6354, genome 1773.18539.
- Candidatus Nanopelagicaceae bacterium HER22_SLD_2000_bin_14, taxon 2518609: GCA_963925575.1, SAMEA115135993, GenBank shard 0062 line 43687 and GTDB shard 0009 line 43474. Its size/ungapped length is 1034883, not its taxon. GTDB calls it Planktophila sp963925575.
- Myxococcota bacterium MYXO-3, taxon 2818507: GCA_048499615.1, SAMN31034883, GenBank shard 0044 line 36999 and GTDB shard 0011 line 6091. GTDB calls it CAADGG01 sp900696485.
- Staphylococcus borealis 1710348831, taxon 2742203: GCA_057415325.1, SAMN55936710, GenBank shard 0053 line 4023.
- ATB row 65890 supplies S. dysgalactiae subsp. equisimilis/SAMEA1034883/ERR084986/ERZ3070268; row 569353 supplies M. tuberculosis/SAMEA3558416/ERR1034883/ERZ3501058. Samples, runs and analysis IDs do not establish target identity.

Catalog shards are under `data/catalog/`, BV-BRC shards under `data/bvbrc/`, and ATB rows in `data/catalog/allthebacteria.tsv.xz`. Candidate objects and the AH65 marker were identity checks, not separate record reviews.

Primary-paper text and Figure 3 were inspected, including the cached page-6 rendering of the [open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf). No new PDF/image was written to the repository; phenotype and antimicrobial claims were not exhaustively curated.

Review performed on `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, the sole listed worktree. No record, history, scope, lifecycle, GitHub item or external source was changed.
