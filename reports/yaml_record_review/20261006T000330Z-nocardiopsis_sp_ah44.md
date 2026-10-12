# YAML Record Review: Nocardiopsis sp. AH44

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah44.yaml`
- Started UTC: 2026-10-06T00:01:42Z
- Finished UTC: 2026-10-06T00:03:30Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034877`, Nocardiopsis sp. AH44, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It carries ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, xrefs, literature evidence or causal graph are asserted.

`data/taxa/PATHS.tsv:14196` uniquely resolves the identifier and stem; `curation/seed_scope.tsv:322029` supplies inclusion. Only this new report was written for this target. Records, source inputs, scope, history and Eukaryota were left untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah44.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah44.yaml --out /private/tmp/ah44-validation.tsv`, exit 0, one file, zero errors. The TSV was read and contains only its header.
- PASS: complete backbone row, reconstructed lineage, seven source inventories, PATHS, scope, attestation and seed-event text agree. The backbone supplies no children of the target.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy; exact Assembly/Nuccore queries; complete marker metadata, references and features; relevant primary-paper text and Figure 3.
- Not applicable: LPSN/GTDB mapping validation, graph-term validation and iModulonDB. No corresponding mapping, graph, gene/regulator or expression-module assertion is present.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. These bounded checks do not prove corpus reproduction or publication readiness.

The review skill, CLAUDE.md, justfile, curation skill/checklist, curation/harmonization/schema guides, history guidance and relevant schema classes were read earlier this turn. Guidance/schema/seeder/target diffs were empty at unchanged HEAD. No history entry or lifecycle promotion was made under the read-only review contract.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034877&retmode=xml) confirms ID, exact label, species rank, bacterial division, parent 2649073 and genetic code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034877) agrees and supplies all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies non-root ancestry; Datasets includes root explicitly.

This informal label does not assert validly published nomenclature. A submitted marker's strain qualifier does not change the NCBI concept's species rank. `EXACT` identifies this taxon, not equivalence to N. xinjiangensis or other AH44-labelled organisms.

## Evidence

| Assertion | Inspected support |
|---|---|
| Identity, rank, parent and code | Complete `data/raw/ncbitaxon_taxa.tsv:221726` row and both NCBI authorities. |
| Lineage | Full reconstructed backbone chain and authority ancestry. |
| Name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31129`; all backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | Backbone attests only ncbitaxon; source, ID, label, count, unit and snapshot note agree. NAME is not a strain or genome count. |
| Scope and event | Scope line 322029 gives date 2026-09-13 and the exact one-source attested-rule reason; event text agrees. |
| Seed timestamp | 2026-09-13T17:54:04Z is the maximum of the inspected raw, ATB and StrainInfo manifest extraction times, following `src/taxonmech/seed.py:139`. |
| Zero strains | No BacDive inventory strain is classified under taxon 1034877; the backbone supplies no descendants. This source count does not claim AH44 was never cultivated. |

The exact query `txid1034877[Organism:noexp]` returned one Nuccore UID, 333497026. Complete [JF777522.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497026), references and features were inspected, excluding sequence bases. This is a 1,416-base 16S rRNA marker, partial at both ends. Source qualifiers identify AH44, taxon 1034877, Saharan soil, Algeria and collection year 2010; no culture-collection qualifier is supplied.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. No DOI or PMID is supplied in the marker metadata. These establish submitted specimen context, not a genome or deposit identity.

The exact Assembly query returned zero items with phrase-not-found/no-items messages. No assembly was retrieved under this query; absence under alternate classification or indexing was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, places AH44 with AH36 in cluster II and includes them in a pooled 99.4-99.8% similarity range to N. xinjiangensis. Figure 3 labels AH44 as JF777522, agreeing with NCBI. Its 1,529-1,544-base range differs from the submitted 1,416-base marker. No exact AH44 percentage, species equivalence or resolution of the length discrepancy was inferred.

Neither marker length nor literature similarity is an asserted YAML field. The paper does not establish a required missing representation.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034877. Empty optional slots agree with those inputs. Record-level literature evidence is optional for seeded records.

The following bounded searches included ignored/hidden files and compressed native catalogs:

- `rg --no-ignore --hidden -n -z -i` searched ID, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All 21 matches were read in full as JSON or header-aware TSV: three target backbone/name/scope rows and 18 numeric substring matches.
- An AH44/AH-44/AH 44/AH_44 screen of the BacDive inventory, native BacDive and StrainInfo returned no matches. No culture candidate was found within that scope; this is not a global culture-census claim.
- The supplemental alias search across the ten roots returned ten rows, all read in full: three target rows, six other-taxon backbone/name/scope rows and one other-taxon assembly object. Full-row retrieval was reconciled against returned addresses.
- JF777522 returned no matches across the ten roots. This is a bounded local absence, not a required missing genome link.
- Before writing, an ignored-inclusive ID/full-label/slug search of `reports/yaml_record_review` and `history` returned no matches; `find` found no prior exact-stem report.

Other aliases were kept separate:

- Burkholderia sp. AH44, taxon 861698: scope line 285671, backbone line 181208, `data/catalog/ncbi_names-0004.jsonl.gz:34892`.
- Acetobacter sp. VTH-AH44, taxon 1769102: scope line 524134, backbone line 462034, `data/catalog/ncbi_names-0010.jsonl.gz:47891`.
- Klebsiella pneumoniae AH_44, taxon 573: `data/catalog/ncbi_genbank-0049.jsonl.gz:699` supplies GCA_053071945.1, SAMN50316391 and PRJNA1299801. A shared designation does not link this assembly to the target.

No inspected source establishes a consequential missing target strain-to-genome relationship or required correction. Taxon, strain designation, marker, genome, sample and project identities were kept distinct.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's assertions. Identity, lineage, provenance and source-classification count are supported. The external sequence-length discrepancy remains unresolved but is not asserted by this record.

## Recommended Edits

None required on current evidence. Do not hand-edit generated YAML, attach culture or genome links by designation alone, infer N. xinjiangensis equivalence or promote lifecycle to REVIEWED.

Any future verified correction belongs in maintained extraction/source inputs or `src/taxonmech/seed.py`, with regression coverage and controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature enrichment requires a supported persistent curation mechanism rather than direct YAML edits.

## Follow-up Checks

- Reconcile publication and accession sequence lengths before using that detail in enrichment; do not manufacture a correction.
- Require explicit deposit-to-marker or deposit-to-genome provenance before adding strain links.
- After an authorized upstream/seeder change, validate and inspect a canary, then run `just verify-corpus` and `just qc`; neither gate ran here.
- Reconcile reports against actual YAML files independently of ignore rules. A report does not confer human REVIEWED status.

## Additional Notes

The 18 numeric substring matches were inspected, not treated as target-taxonomy matches:

- `data/catalog/gtdb_genomes-0017.jsonl.gz:39634` and `ncbi_genbank-0018.jsonl.gz:36192` describe Candidatus Aenigmatarchaeota archaeon bin1364, taxon 3121606, GCA_020343575.1, SAMN17669564 and PRJNA575161. The match is ungapped genome length 1,034,877; GTDB's classification is GCA-020343575 sp020343575. This is an archaeal metagenome-derived assembly, not the target.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6341` is Mycobacterium tuberculosis ERR1034877, taxon 1773, genome 1773.18527.
- `data/catalog/ncbi_genbank-0044.jsonl.gz:37004` and `gtdb_genomes-0004.jsonl.gz:26487` describe Burkholderiales bacterium PROT-10, taxon 1891238, GCA_048499715.1, SAMN31034877, PRJNA884640. GTDB calls it VBCG01 sp016861105. The BioSample substring is not a target-taxonomy association.
- Thirteen `data/catalog/allthebacteria.tsv.xz` rows were read in full, including filter, checksum, run and URL fields. Their identifying context is listed below; none denotes Nocardiopsis AH44.

| ATB line | Scientific name | Sample | Run | Analysis |
|---|---|---|---|---|
| 65884 | Streptococcus dysgalactiae subsp. equisimilis | SAMEA1034877 | ERR085039 | ERZ3070266 |
| 569347 | Mycobacterium tuberculosis | SAMEA3558410 | ERR1034877 | ERZ3501028 |
| 1715126 | Salmonella enterica | SAMN13117030 | SRR10348775 | ERZ25673466 |
| 1715127 | Escherichia coli | SAMN13117035 | SRR10348770 | ERZ25673476 |
| 1715128 | Escherichia coli | SAMN13117039 | SRR10348774 | ERZ25673487 |
| 1715130 | Salmonella enterica | SAMN13117050 | SRR10348772 | ERZ25673507 |
| 1715131 | Salmonella enterica | SAMN13117051 | SRR10348771 | ERZ25673517 |
| 1715132 | Salmonella enterica | SAMN13117052 | SRR10348773 | ERZ25673528 |
| 1715133 | Shigella flexneri | SAMN13117072 | SRR10348776 | ERZ25673539 |
| 1715134 | Campylobacter jejuni | SAMN13117195 | SRR10348778 | ERZ25673549 |
| 1715135 | Campylobacter jejuni | SAMN13117197 | SRR10348777 | ERZ25673558 |
| 1715136 | Escherichia coli | SAMN13117230 | SRR10348779 | ERZ25673570 |
| 3092405 | Escherichia coli | SAMN44338757 | SRR31034877 | ERZ27111271 |

ATB's Sylph classifications include E. coli for the Shigella row and Campylobacter_D jejuni for the Campylobacter rows. These source differences were retained without a target join or sample-to-genome equivalence inference.

Relevant primary-paper text and Figure 3 were inspected this turn, including the cached page-6 rendering of the [open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf). No new PDF or image was written in the repository. Phenotype and antimicrobial claims were not exhaustively curated. Candidate objects were identity leads, not separate taxon reviews. No exhaustive external census or all-alias search is claimed.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, GitHub item or external source was changed.
