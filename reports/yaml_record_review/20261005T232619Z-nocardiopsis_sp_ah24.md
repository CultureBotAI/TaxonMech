# YAML Record Review: Nocardiopsis sp. AH24

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah24.yaml`
- Started UTC: 2026-10-05T23:23:58Z
- Finished UTC: 2026-10-05T23:26:19Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034869`, Nocardiopsis sp. AH24, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It has ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. It asserts no synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence or causal graph.

`data/taxa/PATHS.tsv:14188` uniquely resolves its identifier and stem; `curation/seed_scope.tsv:322021` supplies inclusion. Only this new report was written for this target. No record, inventory, scope, history or generated product was changed; Eukaryota was left untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah24.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah24.yaml --out /private/tmp/ah24-strict-20261005.tsv`, exit 0, one file, zero errors. The TSV was read and contains only its header.
- PASS: structured comparisons checked the complete backbone row, reconstructed ancestor chain, seven source inventories, PATHS, scope, exact NCBITAXON attestation and seed-event text. The backbone supplies no children of this taxon.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, complete marker metadata/features, relevant primary-paper text and Figure 3, plus the candidate's BacDive and DSMZ pages.
- Not applicable: target-specific LPSN/GTDB mapping validation, graph-term validation and iModulonDB. No such mappings, graph, gene/regulator assertion or expression module is present. Candidate culture classification was inspected separately without transferring it.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. Bounded comparisons do not certify corpus reproduction or publication readiness.

Required guidance and relevant schema classes were read earlier in this sequence at unchanged HEAD. The review skill, checklist, validator definitions, seed-timestamp function and manifest timestamps were reread for this target; guidance/schema/seeder/target diffs were empty. The ignored-inclusive search below found no target history entry. No history entry or lifecycle promotion was made, following the read-only review contract.

## Identity and Grounding

The [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034869&retmode=xml) confirms taxon 1034869, exact label, species rank, bacterial division, parent 2649073 and genetic code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034869) confirms identifier/name/rank and all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies non-root ancestry; Datasets includes root explicitly.

The informal name does not assert validly published nomenclature. A sequence's strain qualifier does not change the NCBI concept's species rank. `EXACT` identifies this precise NCBI taxon, not proven equivalence to DSM 45470 or a named Nocardiopsis species.

## Evidence

| Claim | Inspected support |
|---|---|
| Identity, parent, rank and code | Complete `data/raw/ncbitaxon_taxa.tsv:221718` row and both live NCBI authorities. |
| Lineage | Full reconstructed backbone chain and authority ancestry. |
| Name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31121` supplies the scientific name; all three backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | The backbone lists only ncbitaxon, snapshot 2026-09-13. Source, ID, label, count, unit and note agree. NAME is not a strain or genome count. |
| Scope and seed event | Scope line 322021 gives date 2026-09-13 and the exact one-source attested-rule reason; embedded event text agrees. |
| Seed timestamp | Raw, ATB and StrainInfo manifests give 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. The event takes their maximum, following `src/taxonmech/seed.py:139`. |
| Zero BacDive strains | No inventory strain is classified under taxon 1034869, and the backbone supplies no descendants. This source-classification count does not claim AH24 was never cultivated. |

The exact query `txid1034869[Organism:noexp]` returned one Nuccore UID, 333497019. Its [JF777515.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497019) was read in full, including references and features but excluding sequence bases. It is a 1,420-base partial 16S rRNA gene with both ends partial. Source qualifiers supply Nocardiopsis sp. AH24, strain AH24, taxon 1034869, Saharan soil, Algeria and collection year 2010, without a culture-collection qualifier.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. The metadata supply no DOI or PMID. These establish marker/specimen context, not a complete genome or deposit identity.

The exact Assembly query returned zero items with phrase-not-found/no-items messages. No assembly was retrieved under this query; absence under alternate indexing or classification was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, reports AH24 as a single isolate with 98.9% 16S similarity to N. xinjiangensis, while calling for further molecular classification work. Figure 3, page 6 of the [published article PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf), was visually reread and pairs AH24 with JF777515. The paper's 1,529-1,544-base sequence range differs from the accession's 1,420 bases; the discrepancy remains unresolved. Neither similarity nor the figure establishes formal synonymy or deposit equivalence. No phenotype or species assignment was transferred.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034869. Empty optional fields agree with those inputs. Literature evidence is optional for seeded records; the paper does not establish a required missing field.

Searches included ignored/hidden files and compressed native catalogs:

- Identifier, full-label variants and slug were searched with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All six rows were read in full as JSON or header-aware TSV.
- Three are target backbone/name/scope. `data/bvbrc/bvbrc-0006.jsonl.gz:6330` instead supplies Mycobacterium tuberculosis ERR1034869, genome 1773.18517, taxon 1773.
- `data/catalog/allthebacteria.tsv.xz:65876` supplies Streptococcus dysgalactiae subsp. equisimilis sample SAMEA1034869, run ERR085010, analysis ERZ3070249. Row 569339 supplies Mycobacterium tuberculosis run ERR1034869, sample SAMEA3558402, analysis ERZ3500999. Shared digits do not identify the target.
- A separate JF777515 search across the same roots returned no matches. This is bounded local absence, not a missing required genome assertion.
- An AH24/AH-24/AH 24 screen of the BacDive inventory, native BacDive and native StrainInfo returned three rows, all read in full, supporting the DSM candidate below.
- A supplemental JF777515 or AH24/AH-24/AH 24 search across the same ten roots returned 18 rows, all read in full: three target rows, three culture rows, six other-taxon name/backbone/scope rows, two GOLD objects and four assembly objects.
- A DSM 45470/typed BacDive and StrainInfo identifier search across the same roots returned seven rows, all read in full, including four additional culture-crosswalk rows.
- Before writing, an ignored-inclusive identifier/full-label/slug search of `reports` and `history` returned no matches; a filesystem search found no prior exact-stem report.

DSM 45470 remains a plausible, unresolved identity lead:

- `data/raw/bacdive_strains.tsv:81663` and `data/bacdive/records.jsonl.gz:81662` supply BacDive 159426, Nocardiopsis xinjiangensis AH24, taxon 124285, DSM 45470, non-type, with empty native sequence information.
- `data/straininfo/records.jsonl.gz:296823` supplies SI-ID 398934, version DOI 10.60712/SI-ID398934.2, published-online status, BacDive 159426 and designation AH24. Its own available DSM 45470/SI-DP 905685 deposit is likewise N. xinjiangensis taxon 124285 and non-type; no sequence entries are supplied.
- `data/straininfo/strain_links.tsv:58431`, `related_records.tsv.gz:137555` and line 137556 preserve that exact DSM deposit chain as typed strain/deposit references under taxon 124285. `data/raw/culture_collection_strains.tsv:81471` agrees. These are not marker or assembly assertions.
- The inspected [BacDive page](https://bacdive.dsmz.de/strain/159426) supports AH24/DSM 45470, non-type status, taxon 124285, Algerian Saharan soil and N. Sabaou laboratory provenance. Its returned text supplies no target accession. The older web representation was not treated as a current snapshot refresh.
- The [DSMZ catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-45470) identifies N. xinjiangensis AH24 from N. Sabaou, LPBVB, Kouba, and says it was preserved as Nocardiopsis sp. until 2014. Its sampling year is 2003, unlike the marker's 2010. The inspected catalogue supplies neither JF777515 nor taxon 1034869.
- Shared designation, genus, region and laboratory support a plausible candidate, not a demonstrated equivalence. Different classifications and collection dates remain explicit. The evidence proves neither identical nor distinct specimens. No culture link, synonym, phenotype or reclassification was inferred.

Other supplemental results do not establish target relationships:

- Hydrogenophaga sp. AH-24, taxon 435877: scope line 210006, backbone line 96401 and `data/catalog/ncbi_names-0002.jsonl.gz:35252`.
- Burkholderiales bacterium AH24, taxon 861722: scope line 285694, backbone line 181231 and `data/catalog/ncbi_names-0004.jsonl.gz:34915`. Neither is a Nocardiopsis identity.
- `data/gold/projects.jsonl.gz:385451`: Gp0528463, PRJNA533779, SAMN11466681, an Iowa agricultural-soil community sample SC52_AH24_S28_L006. `data/gold/analyses.jsonl.gz:301164` supplies its metagenome analysis Ga0472372 with no organism identifier or GenBank accession.
- `data/catalog/ncbi_genbank-0017.jsonl.gz:38886` and `ncbi_refseq_historical-0000.jsonl.gz:43045` supply paired GCA_019370005.1/GCF_019370005.1, Escherichia coli taxon 562, strain AH24, BioSample SAMN17183259. The RefSeq object is suppressed.
- `data/catalog/ncbi_genbank-0053.jsonl.gz:16236` and `ncbi_refseq-0008.jsonl.gz:44183` supply paired GCA_057665725.1/GCF_057665725.1, Klebsiella pneumoniae taxon 573, strain AH24, BioSample SAMN54997863.

No inspected source establishes a consequential missing strain-to-genome relationship or required correction to the target YAML. DSM 45470 remains an explicit identity question, not an authorized join or negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the target YAML's assertions. Its identity, lineage, provenance and source-classification count are supported. The unresolved DSM relationship and external length discrepancy do not establish an error in this generated record.

## Recommended Edits

None required on current evidence. Do not hand-edit the generated target, add DSM 45470 by name similarity, infer species synonymy from sequence proximity or promote the lifecycle to REVIEWED.

Before a culture-link change, establish explicit primary-source provenance connecting DSM 45470 to JF777515/taxon 1034869 and reconcile the differing dates and classifications. A verified correction belongs in maintained extraction/source inputs or `src/taxonmech/seed.py` with regression coverage, followed by controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature context needs a supported persistent curation mechanism rather than direct YAML edits.

## Follow-up Checks

- Resolve the DSM candidate using explicit deposit-to-accession provenance or an authoritative correction; retain unresolved classification and date differences.
- Investigate the paper/accession length discrepancy before literature enrichment. No author/depositor contact was made.
- After an authorized upstream/seeder change, validate and inspect a canary, then run `just verify-corpus` and `just qc`; neither gate ran here.
- Reconcile report coverage against actual YAML files independently of ignore rules. Report-file coverage is not human REVIEWED lifecycle status.

## Additional Notes

NCBI browser HTML was inaccessible through the web reader; EFetch and Datasets succeeded. The first direct DSMZ open failed, but its BacDive link returned substantive catalogue text. The returned BacDive page was an older cached representation with a 2024 citation, whereas the native snapshot has a 2026 version; inspected identity/deposit fields agreed. StrainInfo's web page required JavaScript, so its complete native snapshot supplied the record details. No access control was bypassed.

Figure 3 was inspected from the cached PDFKit rendering of the published open-access PDF downloaded during the AH0 review. No new PDF/image was written in the repository. The paper was checked for identity context, not exhaustively curated for phenotype, habitat, medium or antimicrobial evidence.

Other objects were inspected as identity leads, not counted as reviews of their taxa. No exhaustive external-source census, all-alias search, complete culture-identity resolution or whole-genome equivalence analysis is claimed.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, issue, pull request or external source was changed.
