# YAML Record Review: Nocardiopsis sp. AH19

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah19.yaml`
- Started UTC: 2026-10-05T23:19:29Z
- Finished UTC: 2026-10-05T23:21:39Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034868`, Nocardiopsis sp. AH19, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It has ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. It asserts no synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence or causal graph.

`data/taxa/PATHS.tsv:14187` uniquely resolves its identifier and stem; `curation/seed_scope.tsv:322020` supplies inclusion. Only this new report was written for this target. No record, inventory, scope, history or generated product was changed; Eukaryota was left untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah19.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah19.yaml --out /private/tmp/ah19-strict-20261005.tsv`, exit 0, one file, zero errors. The TSV was read and contains only its header.
- PASS: structured comparisons checked the complete backbone row, reconstructed ancestor chain, seven inventories, PATHS, scope, exact NCBITAXON attestation and seed-event text. The backbone supplies no children of this taxon.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, complete marker metadata/features, relevant primary-paper text and Figure 3, plus the candidate's BacDive and DSMZ pages.
- Not applicable: target-specific LPSN/GTDB mapping validation, graph-term validation and iModulonDB. No such mappings, graph, gene/regulator assertion or expression module is present. Candidate culture classification was inspected separately without transferring it.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. Bounded comparisons do not certify corpus reproduction or publication readiness.

Required guidance and schema classes were read earlier in this sequence; CLAUDE.md, both record skills, checklist, validator definitions, seed-timestamp function and manifest timestamps were reread during the preceding AH17 review in this turn. HEAD remained unchanged, and guidance/schema/seeder/target diffs were empty. The ignored-inclusive search below found no target history entry. No history entry or lifecycle promotion was made, following the read-only review contract.

## Identity and Grounding

The [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034868&retmode=xml) confirms taxon 1034868, exact label, species rank, bacterial division, parent 2649073 and genetic code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034868) confirms identifier/name/rank and all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies the non-root ancestry; Datasets includes root explicitly.

The informal label does not assert validly published nomenclature. A sequence's strain qualifier does not change this NCBI concept's species rank. `EXACT` identifies the precise NCBI taxon, not a demonstrated equivalence to DSM 45463 or a named Nocardiopsis species.

## Evidence

| Claim | Inspected support |
|---|---|
| Identity, parent, rank and code | Full `data/raw/ncbitaxon_taxa.tsv:221717` row and both live NCBI authorities. |
| Lineage | Full reconstructed backbone chain and authority ancestry. |
| Name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31120` supplies the scientific name; all three backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | The backbone lists only ncbitaxon, snapshot 2026-09-13. Source, ID, label, count, unit and note agree. NAME is not a strain or genome count. |
| Scope and seed event | Scope line 322020 supplies date 2026-09-13 and the exact one-source attested-rule reason; embedded event text agrees. |
| Seed timestamp | Raw, ATB and StrainInfo manifests give 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. The event takes their maximum, following `src/taxonmech/seed.py:139`. |
| Zero BacDive strains | No inventory strain is classified under taxon 1034868, and the backbone supplies no descendants. This source-classification count does not claim AH19 was never cultivated. |

The exact query `txid1034868[Organism:noexp]` returned one Nuccore UID, 379286573. Its [JF777514.2 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=379286573) was inspected in full, including references, comment and features but excluding sequence bases. It is a 1,524-base partial 16S rRNA gene, partial at both ends. Source qualifiers supply Nocardiopsis sp. AH19, strain AH19, taxon 1034868, Saharan soil, Algeria and collection year 2010, without a culture-collection qualifier.

The original references name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. A 2012-03-06 submitter update adds Bouras, Schumann, Sproer and Klenk to the reference authors. The comment explicitly says this version replaced JF777514.1 on that date. The current version is .2, not .1; no DOI or PMID is supplied. This is marker/specimen context, not a genome or deposit link.

The exact Assembly query returned zero items with phrase-not-found/no-items messages. No assembly was retrieved under this query; absence under alternate classification or indexing was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, reports AH19's 99.3% similarity to N. halotolerans. Inspected Figure 3 pairs AH19 with JF777514. The paper's 1,529-1,544-base range differs from the current 1,524-base accession. This unresolved discrepancy and phylogenetic proximity do not establish species or deposit equivalence.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034868. Empty optional fields agree with those inputs. Literature evidence is optional for seeded records; the inspected literature does not establish a required missing field.

The searches included ignored/hidden files and compressed native catalogs:

- Identifier, full-label variants and slug were searched with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All nine rows were read in full as JSON or header-aware TSV.
- Three rows are target backbone/name/scope. `data/bvbrc/bvbrc-0006.jsonl.gz:6331` instead supplies Mycobacterium tuberculosis ERR1034868, genome 1773.18518, taxon 1773.
- `data/catalog/allthebacteria.tsv.xz:65875` supplies Streptococcus dysgalactiae subsp. equisimilis sample SAMEA1034868, run ERR085014, analysis ERZ3070252. Row 569338 supplies Mycobacterium tuberculosis run ERR1034868, sample SAMEA3558401, analysis ERZ3500998.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:13910` supplies Escherichia coli taxon 562, strain 1034868, assembly GCA_015740925.1, BioSample SAMN16989454. A numeric strain designation is not the target taxon identifier.
- `data/catalog/ncbi_genbank-0027.jsonl.gz:12834` supplies Flavobacteriaceae bacterium taxon 1871037, metagenome isolate cluster2_bin.179, assembly GCA_029268635.1, BioSample SAMN32744386. Its genome length is 1034868. `data/catalog/gtdb_genomes-0008.jsonl.gz:15394` is the same accession and length, GTDB Marifrigoribacter sp029268635. Genome length coincidence is not a taxon association.
- A separate JF777514 search across the same ten roots returned no matches. This bounded local absence does not establish a missing required genome link.
- An AH19/AH-19/AH 19 screen of the BacDive inventory, native BacDive and native StrainInfo returned three rows, all read in full. They support the DSM candidate below.
- A supplemental JF777514 or AH19/AH-19/AH 19 search across the same ten roots returned 13 rows, all read in full: three target rows, three culture rows, two GOLD objects and five assembly objects.
- A DSM 45463/typed BacDive and StrainInfo identifier search across the same roots returned seven rows, all read in full, including four additional culture-crosswalk rows.
- Before report creation, an ignored-inclusive identifier/full-label/slug search of `reports` and `history` returned no matches; a filesystem search found no prior exact-stem report.

DSM 45463 remains a plausible, unresolved identity lead:

- `data/raw/bacdive_strains.tsv:81662` and `data/bacdive/records.jsonl.gz:81661` supply BacDive 159425, Nocardiopsis xinjiangensis AH19, taxon 124285, DSM 45463, non-type. Native sequence information is empty.
- `data/straininfo/records.jsonl.gz:299505` supplies SI-ID 401616, version DOI 10.60712/SI-ID401616.2, published-online status, BacDive 159425 and designation AH19. Its own available deposit DSM 45463/SI-DP 908566 is likewise N. xinjiangensis taxon 124285 and non-type; no sequence entries are supplied.
- `data/straininfo/strain_links.tsv:58430`, `related_records.tsv.gz:137553` and line 137554 preserve that exact DSM deposit chain as typed strain/deposit references under taxon 124285. `data/raw/culture_collection_strains.tsv:81463` agrees. These are not marker or assembly assertions.
- The inspected [BacDive page](https://bacdive.dsmz.de/strain/159425) confirms AH19/DSM 45463, taxon 124285, Algerian Saharan soil and N. Sabaou laboratory provenance. Its sequence section provides no target accession. The native non-type flag was retained; a bare page heading was not treated as a type-strain assertion.
- The [DSMZ catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-45463) identifies N. xinjiangensis AH19, supplied by N. Sabaou, LPBVB, Kouba, with sampling before 2010-03-24. That bound is compatible with the marker's year 2010 but does not establish identity. The inspected catalogue does not supply JF777514 or taxon 1034868.
- Shared designation, genus, region and laboratory make the candidate plausible. The record classifications and literature proximity differ, and no explicit target-to-deposit connection was established. The evidence proves neither that the specimens are identical nor that they are distinct. No culture link, synonym, phenotype or reclassification was inferred.

The other supplemental matches do not supply target links:

- `data/gold/projects.jsonl.gz:385448` supplies Gp0528460, PRJNA533779, SAMN11466678, an Iowa agricultural-soil community sample SC49_AH19_S19_L006. `data/gold/analyses.jsonl.gz:297756` supplies its metagenome analysis Ga0468801, with no organism identifier or GenBank accession.
- `data/catalog/ncbi_genbank-0017.jsonl.gz:38888` and `ncbi_refseq_historical-0000.jsonl.gz:43047` supply paired GCA_019370035.1/GCF_019370035.1, Escherichia coli taxon 562, strain AH19, BioSample SAMN17183256. The RefSeq object is suppressed.
- `data/catalog/ncbi_genbank-0023.jsonl.gz:20000` and `ncbi_refseq_historical-0001.jsonl.gz:5459` supply paired GCA_025242345.1/GCF_025242345.1, Escherichia coli taxon 562, strain AH19, BioSample SAMN26939947. The RefSeq object is also suppressed.
- `data/catalog/ncbi_genbank-0042.jsonl.gz:32172` supplies GCA_046242495.1, Neisseria gonorrhoeae taxon 485, isolate ah19, BioSample SAMEA114004429.

No inspected source establishes a consequential missing strain-to-genome relationship or required correction to the target YAML. DSM 45463 remains an explicit identity question, not an authorized join or negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the target YAML's assertions. Identity, lineage, provenance and source-classification count are supported. The DSM candidate and external sequence-length discrepancy remain unresolved; neither establishes an error in this generated record.

## Recommended Edits

None required on current evidence. Do not hand-edit the generated target, add DSM 45463 by name similarity, infer species synonymy from sequence proximity or promote the lifecycle to REVIEWED.

Before a culture-link change, establish explicit primary-source provenance connecting DSM 45463 to JF777514.2/taxon 1034868 and reconcile any classification disagreement. A verified correction belongs in maintained extraction/source inputs or `src/taxonmech/seed.py` with regression coverage, followed by controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature context requires a supported persistent curation mechanism rather than direct YAML edits.

## Follow-up Checks

- Resolve the DSM candidate with explicit deposit-to-accession provenance or an authoritative correction, retaining unresolved classification differences.
- Before marker-based enrichment, preserve accession version .2 and investigate the external length discrepancy. No author/depositor contact was made.
- After an authorized upstream/seeder change, validate and inspect a canary, then run `just verify-corpus` and `just qc`; neither gate ran here.
- Reconcile report coverage against actual YAML files independently of ignore rules. Report-file coverage is not human REVIEWED lifecycle status.

## Additional Notes

NCBI browser HTML was inaccessible through the web reader; EFetch and Datasets succeeded. The first DSMZ direct open failed, but following its BacDive link returned the substantive catalogue. StrainInfo's web page required JavaScript; its complete native snapshot was inspected instead. No access control was bypassed.

Figure 3 was inspected in this turn from the cached PDFKit rendering of page 6 of the [published open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf), downloaded during the AH0 review. No new PDF/image was written in the repository. The paper was checked for identity context, not exhaustively curated for phenotype, habitat, medium or antimicrobial evidence.

Other objects were inspected as identity leads, not counted as reviews of their taxa. No exhaustive external-source census, all-alias search, complete culture-identity resolution or whole-genome equivalence analysis is claimed.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, issue, pull request or external source was changed.
