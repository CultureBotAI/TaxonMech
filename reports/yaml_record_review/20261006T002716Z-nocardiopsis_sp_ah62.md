# YAML Record Review: Nocardiopsis sp. AH62

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah62.yaml`
- Started UTC: 2026-10-06T00:25:05Z
- Finished UTC: 2026-10-06T00:27:16Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034882`, Nocardiopsis sp. AH62, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It carries ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, xrefs, literature evidence or causal graph are asserted.

`data/taxa/PATHS.tsv:14201` uniquely resolves this ID and stem; `curation/seed_scope.tsv:322034` supplies inclusion. This target received only a new review report. Records, inputs, scope, history and Eukaryota were untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah62.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah62.yaml --out /private/tmp/ah62-validation.tsv`, exit 0, one file, zero errors. The TSV was read and contains only its header.
- PASS: complete backbone row, reconstructed lineage, seven source inventories, PATHS, scope, attestation and seed-event text agree. No target children occur in the backbone.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, full marker and conflicting-accession metadata/references/features, relevant primary-paper text and Figure 3, and a full native BacDive candidate object.
- Unavailable: the BacDive candidate's live page could not be accessed by the web tool; its complete native snapshot was read instead. It concerns AH63, not an asserted AH62 culture link.
- Not applicable: graph-term, LPSN/GTDB mapping and iModulonDB checks. No corresponding graph, mapping, gene/regulator or expression-module assertion is present.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. These bounded checks do not prove corpus reproduction or publication readiness.

Required guidance, checklist, relevant schema classes and seeder behavior were fully read in the preceding turn at the same HEAD; the review skill was reread this turn. Guidance/schema/seeder/target diffs were empty. No history entry or human REVIEWED promotion was made under the read-only review contract.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034882&retmode=xml) confirms ID, exact label, species rank, bacterial division, parent and genetic code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034882) agrees and supplies all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies non-root ancestry; Datasets includes root explicitly.

The informal name does not assert validly published nomenclature. A marker's strain qualifier does not change this NCBI concept's species rank. `EXACT` grounds this taxon, not equivalence to N. xinjiangensis, AH63 or another organism called AH62.

## Evidence

| Assertion | Inspected support |
|---|---|
| Identity, parent, rank and code | Complete `data/raw/ncbitaxon_taxa.tsv:221731` and both NCBI authorities. |
| Lineage | Full reconstructed backbone chain and authority ancestry. |
| Scientific name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31134`; all backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | Source, ID, label, count, unit and snapshot note agree with the backbone. NAME is not a strain or genome count. |
| Inclusion and event | Scope line 322034 supplies 2026-09-13 and the exact one-source attested-rule reason; seed-event text agrees. |
| Seed timestamp | 2026-09-13T17:54:04Z is the maximum of the inspected raw 17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z extraction times on that date, following `src/taxonmech/seed.py:139`. |
| Zero strains | No BacDive inventory association under this taxon and no backbone children. This classification count does not mean AH62 was never cultivated. |

The exact `txid1034882[Organism:noexp]` query returned one Nuccore UID, 333497031. Complete [JF777527.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497031), references and features were read, excluding sequence bases. It is a 1,419-base 16S rRNA marker, partial at both ends. Source qualifiers identify AH62, taxon 1034882, Saharan soil, Algeria and collection year 2010, without a culture-collection qualifier.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. No DOI or PMID is supplied. This establishes submitted specimen context, not deposit or genome identity. The exact Assembly query returned zero items with phrase-not-found/no-items messages; absence under other classifications or indexing was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, groups AH62 with AH25 in cluster III within a pooled 99.4-99.8% similarity range to N. xinjiangensis, not an individual AH62 value. Figure 3 labels AH62 as JF777528, conflicting with NCBI. Its 1,529-1,544-base range also differs from 1,419 bases. Neither comparison establishes species equivalence; both external discrepancies remain unresolved.

Complete [JF777528.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=JF777528) identifies AH63, taxon 1034883, and a 1,411-base partial 16S marker. The conflicting figure accession must not be silently substituted for AH62's accession. These external details are not asserted by the YAML and do not establish a required missing field or record defect.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034882. Empty optional slots agree with the inputs; record-level literature evidence is optional for seeded records.

Bounded searches included ignored/hidden files and compressed native catalogs:

- `rg --no-ignore --hidden -n -z -i` searched ID, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All 13 matches were read in full as native JSON or header-aware TSV: three target backbone/name/scope rows and ten numeric substring matches.
- An AH62/AH-62/AH 62/AH_62 search across those ten roots returned 28 rows: three target rows, three rows for another NCBI concept, three GOLD objects and 19 genome objects. All were read in full; full-row addresses were reconciled against results. No BacDive inventory, native BacDive or StrainInfo row matched this alias screen.
- JF777527 or JF777528 returned one native BacDive row, read in full below. Only the latter accession matched. No local JF777527 match occurred in this bounded search; no global absence is claimed.
- Before writing, the ignored-inclusive ID/full-label/slug search of reports/history found AH62 mentioned as conflicting-accession context in the new AH57 report, not as its target. `find` found no prior exact-stem AH62 report.

`data/bacdive/records.jsonl.gz:53352` supplies BacDive 131042, DOI 10.13145/bacdive131042.20260601.11, Nocardiopsis sp. AH63, DSM 45471, non-type, and a StrainInfo 400847 reference. Its general classification is taxon 310350, while its sequence object explicitly gives JF777528, AH63, taxon 1034883 and 1,411 bases. General classification, strain identity and sequence classification were kept separate. This is not evidence connecting DSM 45471 or JF777528 to AH62. The [live BacDive page](https://bacdive.dsmz.de/strain/131042) was inaccessible, so no claim of live corroboration is made.

Other same-designation objects concern Bacillus, E. coli, Aeromonas and Klebsiella, detailed below. No inspected source establishes a consequential missing target strain-to-genome relationship. No name-based join, exhaustive external census or all-alias search is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's assertions. Identity, lineage, provenance and source-classification count are supported. External accession and length discrepancies remain explicit; the AH63 culture evidence was not transferred to this target.

## Recommended Edits

None required on current evidence. Do not hand-edit generated YAML, transfer another AH62's genome evidence, attach the AH63 deposit via the conflicting figure, infer N. xinjiangensis equivalence or promote lifecycle to REVIEWED.

Resolve conflicting literature identifiers before enrichment. A verified target identity/link correction belongs in maintained extraction/source inputs or `src/taxonmech/seed.py`, with regression coverage and controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature enrichment needs a supported persistent curation mechanism rather than direct YAML edits.

## Follow-up Checks

- Obtain authoritative clarification of the figure accession and sequence-length discrepancy before reusing those details. No author or depositor contact was made.
- Require explicit target/deposit/sequence provenance for a future link; preserve accession versions and entity types. Live BacDive access remains unverified for the non-target candidate.
- After an authorized upstream/seeder change, inspect and validate a canary, then run `just verify-corpus` and `just qc`; neither gate ran here.
- Reconcile reports against actual YAML files independently of ignore rules. A report does not confer human REVIEWED status.

## Additional Notes

All same-designation objects were inspected and kept separate:

- Bacillus sp. AH62, taxon 861685: scope line 285658, backbone line 181195, `ncbi_names-0004.jsonl.gz:34879`, parent 185979 rather than Nocardiopsis.
- E. coli AH62, taxon 562: GCA/GCF_013371745.1, SAMN15229443, BV-BRC 562.61703 and GTDB RS_GCF_013371745.1. Full objects occur in BV-BRC shard 0023 line 45575, GenBank 0012 line 1999, RefSeq 0003 line 474 and GTDB 0015 line 28585. The native source context includes China: anhui and chaohu, not the Algerian Nocardiopsis submission.
- Seven further E. coli AH62 assemblies in GenBank shard 0019: GCA_021469105.1/SAMN22045351 (line 39985), GCA_021469265.1/SAMN22046027 (39993), GCA_021469285.1/SAMN22047683 (39994), GCA_021472365.1/SAMN22045413 (40148), GCA_021472485.1/SAMN22045444 (40154), GCA_021472605.1/SAMN22045467 (40160), and GCA_021472685.1/SAMN22045481 (40164). Neither shared designation nor species was used to infer specimen/genome equivalence.
- GOLD Go0699909, Gp0816140 and Ga0667233, at organism/project/analysis lines 522102/602687/447384, explicitly connect E. coli AH62/SAMN22047683 to GCA_021469285.1. This source chain does not concern the Nocardiopsis target; Go/Gp/Ga remain organism/project references rather than genome identifiers.
- Aeromonas dhakensis RYU-Ah62, taxon 196024: GCA/GCF_033096545.1, SAMD00613431, BV-BRC 196024.215 and GTDB RS_GCF_033096545.1. Full objects occur in BV-BRC shard 0009 line 19083, GenBank 0030 line 40942, RefSeq 0005 line 24404 and GTDB 0003 line 16990.
- Separate A. dhakensis AH62: GCA/GCF_056434765.1, SAMN56607722, GenBank shard 0052 line 8453 and RefSeq 0008 line 30852. No same-strain identity with RYU-Ah62 was inferred.
- K. pneumoniae AH62, taxon 573: GCA/GCF_057664865.1, SAMN54997891, GenBank shard 0053 line 16194 and RefSeq 0008 line 44156.

The ten numeric substring matches were also read in full:

- M. tuberculosis ERR1034882, taxon 1773: BV-BRC shard 0006 line 6343, genome 1773.18529.
- Uncultured Candidatus Peribacteria bacterium, taxon 2501586: GCA_964637495.1, SAMEA117373355, GenBank shard 0063 line 38238 and GTDB 0016 line 26971. Its ungapped length is 1034882; that number is not target taxonomy. GTDB calls it CAZWWJ01 sp964637495.
- Phycisphaerales bacterium PLAN-4, taxon 2052180: GCA_048499635.1, SAMN31034882, GenBank shard 0044 line 37000 and GTDB 0012 line 49654. GTDB calls it UBA5793 sp011525805.
- C. jejuni 19CA08GT13-UCD-C1, taxon 197: GCA_010348825.1, SAMN13474040, GenBank shard 0009 line 6279.
- Streptomyces sp. NPDC026183, taxon 3684478: GCA/GCF_055568095.1, SAMN55300076, GenBank shard 0051 line 17224 and RefSeq 0008 line 23265. The match is a substring of genome size 11034882, not target taxonomy.
- ATB row 65889 supplies S. dysgalactiae subsp. equisimilis/SAMEA1034882/ERR085051/ERZ3070264; row 569352 supplies M. tuberculosis/SAMEA3558415/ERR1034882/ERZ3501062. Samples, runs and analysis identifiers do not establish target identity.

Catalog shards are under `data/catalog/`, BV-BRC shards under `data/bvbrc/`, GOLD rows in the respective `data/gold/` native files, and ATB rows in `data/catalog/allthebacteria.tsv.xz`. Candidate objects and the AH63 marker were identity leads, not separate taxon reviews.

Relevant primary-paper text and Figure 3 were inspected this turn, including the cached page-6 rendering of the [open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf). No new PDF or image was written in the repository. Phenotype and antimicrobial claims were not exhaustively curated.

Review performed on `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, GitHub item or external source was changed.
