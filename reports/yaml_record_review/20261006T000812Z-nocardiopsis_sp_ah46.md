# YAML Record Review: Nocardiopsis sp. AH46

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah46.yaml`
- Started UTC: 2026-10-06T00:05:54Z
- Finished UTC: 2026-10-06T00:08:12Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034878`, Nocardiopsis sp. AH46, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It carries ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, xrefs, literature evidence or causal graph are asserted.

`data/taxa/PATHS.tsv:14197` uniquely resolves the identifier and stem; `curation/seed_scope.tsv:322030` supplies inclusion. Only this new report was written for this target. Records, inputs, scope, history and Eukaryota were untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah46.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah46.yaml --out /private/tmp/ah46-validation.tsv`, exit 0, one file, zero errors. The TSV was read and contains only its header.
- PASS: complete backbone row, reconstructed lineage, seven source inventories, PATHS, scope, attestation and seed-event text agree. The backbone supplies no children of this target.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, complete marker metadata/references/features, relevant primary-paper text and Figure 3, candidate BacDive and DSMZ pages.
- Not applicable: LPSN/GTDB mapping validation, graph-term validation and iModulonDB. No corresponding mapping, graph, gene/regulator or expression-module assertion is present.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. These bounded checks do not prove corpus reproduction or publication readiness.

Required guidance, relevant schema classes, validators and seed-timestamp behavior were read earlier in this sequence. The review skill was reread this turn. HEAD remained unchanged; guidance/schema/seeder/target diffs were empty. No history entry or lifecycle promotion was made under the read-only review contract.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034878&retmode=xml) confirms ID, exact label, species rank, bacterial division, parent 2649073 and genetic code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034878) agrees and supplies all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies non-root ancestry; Datasets includes root explicitly.

This informal label does not assert validly published nomenclature. The submitted marker's strain qualifier does not change the NCBI concept's species rank. `EXACT` identifies this taxon, not equivalence to N. xinjiangensis or DSM 45467.

## Evidence

| Assertion | Inspected support |
|---|---|
| Identity, rank, parent and code | Complete `data/raw/ncbitaxon_taxa.tsv:221727` row and both NCBI authorities. |
| Lineage | Full reconstructed backbone chain and authority ancestry. |
| Scientific name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31130`; all three backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | Backbone attests only ncbitaxon; source, ID, label, count, unit and snapshot note agree. NAME is not a strain or genome count. |
| Scope and event | Scope line 322030 gives date 2026-09-13 and the exact one-source attested-rule reason; event text agrees. |
| Seed timestamp | 2026-09-13T17:54:04Z is the maximum of the previously inspected raw, ATB and StrainInfo extraction times, following `src/taxonmech/seed.py:139`. |
| Zero strains | No BacDive inventory strain is classified under taxon 1034878; the backbone supplies no descendants. This source-classification count does not claim AH46 was never cultivated. |

The exact query `txid1034878[Organism:noexp]` returned one Nuccore UID, 333497027. Complete [JF777523.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497027), references and features were inspected, excluding sequence bases. This is a 1,410-base 16S rRNA marker, partial at both ends. Source qualifiers identify AH46, taxon 1034878, Saharan soil, Algeria and collection year 2010; no culture-collection qualifier is supplied.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. No DOI or PMID is supplied in that metadata. These establish submitted specimen context, not a genome or deposit identity.

The exact Assembly query returned zero items with phrase-not-found/no-items messages. No assembly was retrieved under this query; absence under alternate classification or indexing was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, reports 98.4% similarity between AH46 and N. xinjiangensis. Figure 3 labels AH46 as JF777523, agreeing with NCBI. Its 1,529-1,544-base range differs from the submitted 1,410-base marker. Neither the comparison nor tree placement establishes species equivalence; the length discrepancy remains unresolved.

Neither marker length nor the literature comparison is asserted by this generated YAML. The paper does not establish a required missing representation.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034878. Empty optional slots agree with those inputs. Record-level literature evidence is optional for seeded records.

The following bounded searches included ignored/hidden files and compressed native catalogs:

- `rg --no-ignore --hidden -n -z -i` searched ID, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All 22 matches were read in full as JSON or header-aware TSV: three target backbone/name/scope rows and 19 numeric substring matches.
- An AH46/AH-46/AH 46/AH_46 screen of the BacDive inventory, native BacDive and StrainInfo returned three rows, all read in full. A supplemental alias search across the ten roots returned 15 rows: three target rows, three culture-source rows, six other-taxon backbone/name/scope rows and three assembly objects. All were read in full.
- A DSM 45467/typed BacDive and StrainInfo identifier search across the ten roots returned seven rows, all read in full, including four additional culture-crosswalk rows. Full-row retrieval was reconciled against returned addresses.
- JF777523 returned no matches across the ten roots. This is a bounded local absence, not a required missing genome link.
- Before writing, an ignored-inclusive ID/full-label/slug search of `reports/yaml_record_review` and `history` returned no matches; `find` found no prior exact-stem report.

DSM 45467 is a plausible but unproven target association:

- `data/raw/bacdive_strains.tsv:82772` and `data/bacdive/records.jsonl.gz:82771` supply BacDive 160535, Nocardiopsis xinjiangensis AH46, taxon 124285, DSM 45467, non-type, with empty native sequence information. Its species-level synonym was not transferred to the target.
- `data/straininfo/records.jsonl.gz:303612` supplies published-online SI-ID 405723, DOI 10.60712/SI-ID405723.1, BacDive 160535, AH46 and taxon 124285. Its available DSM 45467/SI-DP 912969 deposit is non-type and supplies no sequence entries.
- `data/straininfo/strain_links.tsv:59924`, `related_records.tsv.gz:140833` and line 140834 preserve this strain/deposit chain under taxon 124285. `data/raw/culture_collection_strains.tsv:81467` agrees. These are typed strain/deposit references, not genomes or target-taxonomy assertions.
- The [BacDive page](https://bacdive.dsmz.de/strain/160535) confirms AH46, DSM 45467, N. xinjiangensis, taxon 124285, Algerian Saharan soil and N. Sabaou laboratory provenance; its sequence section supplies no target accession. The native non-type flag was retained instead of treating a bare page heading as a positive type assertion.
- The [DSMZ catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-45467) identifies AH46 from N. Sabaou, LPBVB, Koupa, Algeria, with sampling year 2003, unlike the marker's 2010. It supplies neither JF777523 nor target taxon 1034878.
- Shared designation, genus, region and laboratory make the candidate plausible. Classification and collection-date differences remain explicit. No inspected source establishes the deposit-to-marker/target connection. The evidence proves neither identical nor distinct specimens; no association or synonym was inferred.

Other aliases were separated: Bacillus sp. AH46, taxon 861680 (scope line 285653, backbone line 181190, `data/catalog/ncbi_names-0004.jsonl.gz:34874`); Gluconobacter sp. VTH-AH46, taxon 1712069 (scope line 510603, backbone line 446273, `ncbi_names-0010.jsonl.gz:30920`); Klebsiella pneumoniae AH46, taxon 573 (GCA/GCF_057665365.1, SAMN54997873, GenBank shard 0053 line 16218/RefSeq shard 0008 line 44174); and separate K. pneumoniae AH_46 (GCA_053069225.1, SAMN50316528, GenBank shard 0049 line 563). A shared designation does not establish organism or genome identity.

No inspected source establishes a consequential missing target strain-to-genome relationship or required correction. DSM 45467 remains an unresolved identity lead, not an authorized join or negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's assertions. Identity, lineage, provenance and source-classification count are supported. The culture candidate and external sequence-length discrepancy remain unresolved but are not asserted by this record.

## Recommended Edits

None required on current evidence. Do not hand-edit generated YAML, attach DSM 45467 by name similarity, infer N. xinjiangensis equivalence or promote lifecycle to REVIEWED.

Before a culture-link change, obtain explicit provenance connecting DSM 45467 to JF777523/taxon 1034878 and reconcile classification/date differences. A verified correction belongs in maintained extraction/source inputs or `src/taxonmech/seed.py`, with regression coverage and controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature enrichment requires a supported persistent curation mechanism rather than direct YAML edits.

## Follow-up Checks

- Resolve the culture candidate with explicit deposit-to-accession provenance or an authoritative correction; retain remaining uncertainty.
- Reconcile publication and accession lengths before using that detail in enrichment. No author/depositor contact was made.
- After an authorized upstream/seeder change, validate and inspect a canary, then run `just verify-corpus` and `just qc`; neither gate ran here.
- Reconcile reports against actual YAML files independently of ignore rules. A report does not confer human REVIEWED status.

## Additional Notes

The 19 numeric substring matches were inspected, not treated as target-taxonomy matches:

- E. coli PNUSAE018991/PNUSAE018833/PNUSAE018830, taxon 562: BV-BRC 562.36421/562.36457/562.36503, SAMN10348781/SAMN10348785/SAMN10348789, GCA_003747865.1/.2, GCA_003755365.1/.2 and GCA_003759245.1/.2 respectively. Full objects occur in BV-BRC shard 0023 lines 36283/36313/36359, GenBank historical shard 0000 lines 10405/10449/10499 and current shard 0002 lines 47727/48094/48288. Historical .1 versions are replaced; current rows retain .2.
- M. tuberculosis ERR1034878, taxon 1773: BV-BRC shard 0006 line 6336, genome 1773.18522.
- Phycisphaerae bacterium PLAN-5, taxon 2026778: GCA_048499695.1, SAMN31034878, GenBank shard 0044 line 37003 and GTDB shard 0012 line 4473; GTDB calls it JABWBH01 sp013360585.
- Campylobacter jejuni PNUSAC013696, taxon 197: GCA_010348785.1, SAMN13353954, GenBank shard 0009 line 6277.
- Streptococcus pneumoniae isolate 399, taxon 1313: GCA_036052195.1, SAMN11116885, assembly name PDT001034878.1, GenBank shard 0033 line 35504.
- ATB row 65885 supplies S. dysgalactiae subsp. equisimilis/SAMEA1034878/ERR085060/ERZ3070262; row 569348 supplies M. tuberculosis/SAMEA3558411/ERR1034878/ERZ3501043. Rows 1502170/1502171/1502172 supply E. coli samples SAMN10348781/SAMN10348785/SAMN10348789, runs SRR8136847/SRR8136877/SRR8136853 and analyses ERZ9092393/ERZ9092394/ERZ9092396. Samples, runs and analysis identifiers were not promoted to target taxonomy or genome equivalence.

Catalog shards are under `data/catalog/`, BV-BRC shards under `data/bvbrc/`, and ATB rows at `data/catalog/allthebacteria.tsv.xz`.

DSMZ direct access initially failed; the linked page from BacDive succeeded. StrainInfo's page required JavaScript, so its complete native snapshot was used. Relevant primary-paper text and Figure 3 were inspected this turn, including the cached page-6 rendering of the [open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf). No new PDF or image was written in the repository. Phenotype and antimicrobial claims were not exhaustively curated.

Candidate objects were identity leads, not separate taxon reviews. No exhaustive external census, all-alias search, complete culture-identity resolution or whole-genome equivalence analysis is claimed.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, GitHub item or external source was changed.
