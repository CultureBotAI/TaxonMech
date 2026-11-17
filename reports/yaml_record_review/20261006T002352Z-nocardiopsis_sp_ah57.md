# YAML Record Review: Nocardiopsis sp. AH57

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah57.yaml`
- Started UTC: 2026-10-06T00:21:28Z
- Finished UTC: 2026-10-06T00:23:52Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034881`, Nocardiopsis sp. AH57, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It carries ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, xrefs, literature evidence or causal graph are asserted.

`data/taxa/PATHS.tsv:14200` uniquely resolves the ID and stem; `curation/seed_scope.tsv:322033` supplies inclusion. Only this new report was written for the target. Records, inputs, scope, history and Eukaryota were untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah57.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah57.yaml --out /private/tmp/ah57-validation.tsv`, exit 0, one file, zero errors. The output TSV was read and contains only its header.
- PASS: full backbone row, reconstructed lineage, seven source inventories, PATHS, scope, attestation and seed-event text agree. No children occur under the target in the backbone.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, full marker metadata/references/features, relevant primary-paper text and Figure 3, and full sequence metadata for the conflicting accession and ambiguous alias.
- Not applicable: graph-term, LPSN/GTDB mapping and iModulonDB checks. No corresponding graph, mapping, gene/regulator or expression-module assertion is present.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. These bounded checks do not establish corpus reproduction or publication readiness.

Required guidance, checklist, relevant schema classes and seeder behavior were fully read in the preceding turn at the same HEAD. The review skill was reread here, and guidance/schema/seeder/target diffs were empty. No history entry or human REVIEWED promotion was made under the read-only review contract.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034881&retmode=xml) confirms ID, exact label, species rank, bacterial division, parent and genetic code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034881) agrees and supplies all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies non-root ancestry; Datasets includes root explicitly.

The informal name does not assert validly published nomenclature. A marker's strain qualifier does not change this NCBI concept's species rank. `EXACT` grounds this taxon, not equivalence to N. xinjiangensis or another organism called AH57.

## Evidence

| Assertion | Inspected support |
|---|---|
| Identity, parent, rank and code | Complete `data/raw/ncbitaxon_taxa.tsv:221730` and both NCBI authorities. |
| Lineage | Full reconstructed backbone chain and authority ancestry. |
| Name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31133`; all backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | Source, ID, label, count, unit and snapshot note agree with the backbone. NAME is not a strain or genome count. |
| Inclusion and event | Scope line 322033 supplies 2026-09-13 and the exact one-source attested-rule reason; seed-event text agrees. |
| Seed timestamp | Raw, ATB and StrainInfo extraction times were read: 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. The maximum is the recorded 17:54:04Z, following `src/taxonmech/seed.py:139`. |
| Zero strains | No BacDive inventory association under this taxon and no backbone children. This classification count does not mean AH57 was never cultivated. |

The exact `txid1034881[Organism:noexp]` query returned one Nuccore UID, 333497030. Complete [JF777526.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497030), references and features were read, excluding sequence bases. It is a 1,419-base 16S rRNA marker, partial at both ends. Source qualifiers identify AH57, taxon 1034881, Saharan soil, Algeria and collection year 2010, without a culture-collection qualifier.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. No DOI or PMID is supplied. This establishes submitted specimen context, not deposit or genome identity. The exact Assembly query returned zero items with phrase-not-found/no-items messages; absence under other classifications or indexing was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, includes AH57 in cluster I and reports a pooled 99.4-99.8% similarity range to N. xinjiangensis, not an individual AH57 value. Figure 3 labels AH57 as JF777527, conflicting with NCBI. The paper's 1,529-1,544-base sequence range also differs from 1,419 bases. Neither comparison establishes species equivalence; both external discrepancies remain unresolved.

Complete [JF777527.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=JF777527) identifies Nocardiopsis sp. AH62, taxon 1034882, a separate 1,419-base partial 16S marker. Thus the figure's accession must not be silently substituted for AH57's NCBI accession. The conflicting paper details are not YAML assertions, so they do not establish a defect in this generated record.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034881. Empty optional slots agree with the inputs. Record-level literature evidence is optional for seeded records.

Bounded searches included ignored/hidden files and compressed native catalogs:

- `rg --no-ignore --hidden -n -z -i` searched ID, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All 15 matches were read in full as native JSON or header-aware TSV: three target backbone/name/scope rows and 12 numeric substring matches.
- An AH57/AH-57/AH 57/AH_57 search across those ten roots returned 11 rows: three target rows, six rows for two other NCBI concepts and two Klebsiella assembly objects. All were read in full, with full-row addresses reconciled against results. No BacDive inventory, native BacDive or StrainInfo row matched this alias screen.
- JF777526 or JF777527 returned no matches across the ten roots. This bounded local absence does not establish a required missing genome link or global absence of sequence evidence.
- Before writing, ignored-inclusive ID/full-label/slug searches of reports/history returned no hits; `find` found no prior exact-stem report.

No inspected source establishes a consequential missing target strain-to-genome relationship. Name-only matches below supply no target identity chain. No exhaustive external census or all-alias search is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's assertions. Identity, lineage, provenance and source-classification count are supported. External accession and length discrepancies remain explicit, without promoting unasserted claims into record defects.

## Recommended Edits

None required on current evidence. Do not hand-edit generated YAML, transfer another AH57's culture/genome evidence, infer N. xinjiangensis equivalence or promote lifecycle to REVIEWED.

Resolve conflicting literature identifiers before enrichment. A verified target identity/link correction belongs in maintained extraction/source inputs or `src/taxonmech/seed.py`, with regression coverage and controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature enrichment needs a supported persistent curation mechanism rather than a direct YAML edit.

## Follow-up Checks

- Obtain authoritative clarification of the figure accession and sequence-length discrepancy before reusing those details; do not select a convenient interpretation. No author or depositor contact was made.
- Require explicit deposit-to-target/sequence provenance for a future strain or genome link, preserving supplied accession versions and entity types.
- After an authorized upstream/seeder change, inspect and validate a canary, then run `just verify-corpus` and `just qc`; neither ran here.
- Reconcile report coverage against actual YAML files independently of ignore rules. A report does not confer human REVIEWED status.

## Additional Notes

Other AH57 aliases were inspected and not joined:

- Bacterium AH57, taxon 124433: scope line 148450, backbone line 23716 and `ncbi_names-0000.jsonl.gz:45207`. An exact NCBI query returned one Nuccore UID, 11544611. Complete [AJ289964.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=11544611) identifies a 1,426-base 16S sequence from Germany: Lake Fuchskuhle, submitted on 2000-04-07. Its source context differs from the Algerian Nocardiopsis submission. No specimen equivalence was inferred. Its cited publication was not separately reviewed, and no findings about that paper are asserted.
- Burkholderiales bacterium AH57, taxon 861724: scope line 285696, backbone line 181233 and `ncbi_names-0004.jsonl.gz:34917`, under parent taxon 80841 rather than Nocardiopsis.
- K. pneumoniae AH57, taxon 573: GCA/GCF_057665105.1, SAMN54997878, GenBank shard 0053 line 16205 and RefSeq 0008 line 44167. These are another organism's assembly assertions.

The 12 numeric substring matches were read in full:

- E. coli PNUSAE018416, taxon 562: BV-BRC 562.36510, SAMN10348811, GCA_003759785.1/.2. BV-BRC shard 0023 line 36366, GenBank historical 0000 line 10507 and current 0002 line 48315 preserve replaced .1 and current .2.
- E. coli PNUSAE018415: BV-BRC 562.36594, SAMN10348815, GCA_003767145.1, BV-BRC 0023 line 36441 and GenBank 0002 line 48678.
- M. tuberculosis ERR1034881, taxon 1773: BV-BRC shard 0006 line 6345, genome 1773.18530.
- Rhodocyclaceae bacterium PROT-11, taxon 1898103: GCA_048499595.1, SAMN31034881, GenBank shard 0044 line 36998 and GTDB 0009 line 48594. GTDB calls it Desulfobacillus sp011526165.
- ATB row 65888 supplies S. dysgalactiae subsp. equisimilis/SAMEA1034881/ERR085020/ERZ3070265; row 569351 supplies M. tuberculosis/SAMEA3558414/ERR1034881/ERZ3501046. Rows 1502178/1502179 supply E. coli samples SAMN10348811/SAMN10348815, runs SRR8136832/SRR8136831 and analyses ERZ9092402/ERZ9092403. Samples, runs and analyses were not promoted to target taxonomy or genome equivalence.

Catalog shards are under `data/catalog/`, BV-BRC shards under `data/bvbrc/`, and ATB rows in `data/catalog/allthebacteria.tsv.xz`. Candidate objects and the AH62 marker were identity leads, not separate taxon reviews.

Relevant primary-paper text and Figure 3 were inspected this turn, including the cached page-6 rendering of the [open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf). No new PDF or image was written in the repository. Phenotype and antimicrobial claims were not exhaustively curated.

Review performed on `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, GitHub item or external source was changed.
