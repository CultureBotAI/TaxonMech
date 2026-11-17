# YAML Record Review: Nocardiopsis sp. AH25

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah25.yaml`
- Started UTC: 2026-10-05T23:28:00Z
- Finished UTC: 2026-10-05T23:30:24Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034870`, Nocardiopsis sp. AH25, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It has ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. It asserts no synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence or causal graph.

`data/taxa/PATHS.tsv:14189` uniquely resolves the identifier and stem; `curation/seed_scope.tsv:322022` supplies inclusion. Only this new report was written for this target. No record, inventory, scope, history or generated product was changed; Eukaryota was left untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah25.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah25.yaml --out /private/tmp/ah25-strict-20261005.tsv`, exit 0, one file, zero errors. The TSV was read and contains only its header.
- PASS: structured comparisons checked the complete backbone row, reconstructed ancestor chain, seven inventories, PATHS, scope, exact NCBITAXON attestation and seed-event text. The backbone supplies no children of this taxon.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, complete marker metadata/features, relevant primary-paper text and Figure 3, plus the candidate's BacDive and DSMZ pages. A MediaDive listing supplied navigation to those pages, not target-level identity evidence.
- Not applicable: target-specific LPSN/GTDB mapping validation, graph-term validation and iModulonDB. No such mappings, graph, gene/regulator assertion or expression module is present. Candidate source classifications were preserved separately.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. Bounded checks do not certify corpus reproduction or publication readiness.

Required guidance and relevant schema classes were read earlier in this sequence. The review skill, checklist, validator definitions, seed-timestamp function and manifest timestamps were reread during the AH24 review in this turn. HEAD remained unchanged; guidance/schema/seeder/target diffs were empty. The ignored-inclusive search below found no target history entry. No history entry or lifecycle promotion was made, following the read-only review contract.

## Identity and Grounding

The [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034870&retmode=xml) confirms taxon 1034870, exact label, species rank, bacterial division, parent 2649073 and genetic code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034870) confirms identifier/name/rank and all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies non-root ancestry; Datasets includes root explicitly.

The informal label does not assert validly published nomenclature. A sequence's strain qualifier does not change the NCBI concept's species rank. `EXACT` identifies this precise NCBI taxon, not proven equivalence to DSM 45464 or a named species.

## Evidence

| Claim | Inspected support |
|---|---|
| Identity, parent, rank and code | Full `data/raw/ncbitaxon_taxa.tsv:221719` row and both live NCBI authorities. |
| Lineage | Full reconstructed backbone chain and authority ancestry. |
| Name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31122` supplies the scientific name; all three backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | The backbone lists only ncbitaxon, snapshot 2026-09-13. Source, ID, label, count, unit and note agree. NAME is not a strain or genome count. |
| Scope and seed event | Scope line 322022 supplies date 2026-09-13 and the exact one-source attested-rule reason; embedded event text agrees. |
| Seed timestamp | Raw, ATB and StrainInfo manifests give 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. The event takes their maximum, following `src/taxonmech/seed.py:139`. |
| Zero BacDive strains | No inventory strain is classified under taxon 1034870, and the backbone supplies no descendants. This source-classification count does not claim AH25 was never cultivated. |

The exact query `txid1034870[Organism:noexp]` returned one Nuccore UID, 333497020. Its [JF777516.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497020) was inspected in full, including references and features but excluding sequence bases. It is a 1,419-base partial 16S rRNA gene, partial at both ends. Source qualifiers supply Nocardiopsis sp. AH25, strain AH25, taxon 1034870, Saharan soil, Algeria and collection year 2010, without a culture-collection qualifier.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. The metadata supply no DOI or PMID. These establish submitted marker/specimen context, not a genome or deposit identity.

The exact Assembly query returned zero items with phrase-not-found/no-items messages. No assembly was retrieved under this query; absence under alternate classification or indexing was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, groups AH25 with AH62 in cluster III. Its 99.4-99.8% N. xinjiangensis similarity range covers several groups, not AH25 alone. Inspected Figure 3 pairs AH25 with JF777516. The reported 1,529-1,544-base range differs from the accession's 1,419 bases. This unresolved discrepancy does not establish a YAML error or species equivalence.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034870. Empty optional fields agree with those inputs. Literature evidence is optional for seeded records; the paper does not establish a required missing field.

The following searches included ignored/hidden files and compressed native catalogs:

- Identifier, full-label variants and slug were searched with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All six rows were read in full as JSON or header-aware TSV.
- Three rows are target backbone/name/scope. `data/bvbrc/bvbrc-0006.jsonl.gz:6329` supplies Mycobacterium tuberculosis ERR1034870, genome 1773.18516, taxon 1773.
- `data/catalog/allthebacteria.tsv.xz:65877` supplies Streptococcus dysgalactiae subsp. equisimilis sample SAMEA1034870, run ERR085024, analysis ERZ3070248. Row 569340 supplies Mycobacterium tuberculosis run ERR1034870, sample SAMEA3558403, analysis ERZ3501011. Shared digits do not establish a target relationship.
- A separate JF777516 search across the same ten roots returned no matches. This is bounded local absence, not a missing required genome link.
- An AH25/AH-25/AH 25 screen of the BacDive inventory, native BacDive and native StrainInfo returned four rows, all read in full: the three DSM candidate rows and a separate Streptococcus source strain.
- A supplemental JF777516 or AH25/AH-25/AH 25 search across the same ten roots returned 28 rows, all read in full: three target rows, four culture rows, twelve other-taxon name/backbone/scope rows, five GOLD objects, one BV-BRC object and three genome-catalog objects.
- A DSM 45464/typed BacDive and StrainInfo identifier search across the same roots returned seven rows, all read in full, including four additional culture-crosswalk rows.
- Before writing, an ignored-inclusive identifier/full-label/slug search of `reports` and `history` returned no matches; a filesystem search found no prior exact-stem report.

DSM 45464 is a plausible but unproven target association:

- `data/raw/bacdive_strains.tsv:82624` and `data/bacdive/records.jsonl.gz:82623` supply BacDive 160387, Nocardiopsis sp. AH25, taxon 310350, DSM 45464, non-type, with empty native sequence information.
- `data/straininfo/records.jsonl.gz:304674` supplies SI-ID 406785, version DOI 10.60712/SI-ID406785.1, published-online status, BacDive 160387 and designation AH25. Its own available DSM 45464/SI-DP 914111 deposit is classified as Nocardiopsis, genus taxon 2013, and non-type; no sequence entries are supplied.
- `data/straininfo/strain_links.tsv:59645` and `related_records.tsv.gz:140217`/line 140218 preserve the DSM deposit chain as typed strain/deposit references under taxon 2013. `data/raw/culture_collection_strains.tsv:81464` instead preserves taxon 310350, matching the BacDive inventory. Neither classification is the target taxon 1034870; these references are not genomes.
- The inspected [BacDive page](https://bacdive.dsmz.de/strain/160387) confirms the designation/deposit, taxon 310350, Algerian Saharan soil and N. Sabaou laboratory provenance. Its sequence section supplies no target accession. The native non-type flag was retained rather than reading a bare page heading as a type assertion.
- The [DSMZ catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-45464) identifies Nocardiopsis sp. AH25 from N. Sabaou, LPBVB, Kouba, with sampling year 2003, unlike the marker's 2010. It supplies neither JF777516 nor taxon 1034870.
- Shared designation, genus, region and laboratory make the candidate plausible. Classification granularity and collection-date differences remain explicit. No inspected source establishes the deposit-to-marker/target connection. The evidence proves neither identical nor distinct specimens; no association or synonym was inferred.

The other matches were distinguished as follows:

- `data/straininfo/records.jsonl.gz:9417` is published-online SI-ID 9417, DOI 10.60712/SI-ID9417.2, BacDive 137239, Streptococcus gallolyticus taxon 315405. Designations include AH 25 and AH 25 RH. Its own deposits are LMG 15049, CIP 103232, NCFB 2019, CCUG 34831, NCDO 2019 and NCIMB 702019, all non-type. Individual deposit classifications include S. gallolyticus subsp. gallolyticus, S. gallolyticus and S. equinus; no sequence entries or Nocardiopsis identity are supplied.
- Pseudomonas sp. AH25, taxon 595563: scope line 250216, backbone line 141395, `data/catalog/ncbi_names-0003.jsonl.gz:38680`. Pseudomonas sp. AH25(2010), taxon 861728: scope line 285699, backbone line 181236, `ncbi_names-0004.jsonl.gz:34920`.
- Viridibacillus sp. AH25, taxon 1167428: scope line 351151, backbone line 257860, `data/catalog/ncbi_names-0006.jsonl.gz:24868`. Cyanobium sp. AH25, taxon 1519448: scope line 460927, backbone line 391195, `ncbi_names-0009.jsonl.gz:20860`.
- `data/gold/organisms.jsonl.gz:149686`, line 149687 and line 149696 supply Go0211504, Go0211505 and Go0211514 for Streptococcus gallolyticus taxon 315405 with AH 25 variants; culture-collection fields are empty. These do not establish target or cross-source genome identity.
- `data/gold/projects.jsonl.gz:385452` supplies Gp0528464, PRJNA533779, SAMN11466682, an Iowa agricultural-soil community sample SC53_AH25_S29_L006. `data/gold/analyses.jsonl.gz:301256` supplies its metagenome analysis Ga0472467 without an organism ID or GenBank accession.
- `data/bvbrc/bvbrc-0023.jsonl.gz:45576` supplies Escherichia coli AH25, taxon 562, genome 562.61704, assembly GCA_013371725.1, BioSample SAMN15229442 and accessions CP055256/CP055257/CP055258. `data/catalog/ncbi_genbank-0012.jsonl.gz:1998` and `ncbi_refseq-0003.jsonl.gz:473` supply paired GCA_013371725.1/GCF_013371725.1. `data/catalog/gtdb_genomes-0001.jsonl.gz:29709` supplies RS_GCF_013371725.1, GTDB ECMA0423 sp047199055, still explicitly associated with NCBI taxon 562 and AH25. None identifies the target Nocardiopsis strain.

No inspected source establishes a consequential missing strain-to-genome relationship or required target correction. DSM 45464 remains an unresolved identity lead, not an authorized join or negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's assertions. Identity, lineage, provenance and source-classification count are supported. The DSM candidate and external length discrepancy remain unresolved; neither establishes an error in this generated record.

## Recommended Edits

None required on current evidence. Do not hand-edit the generated target, attach DSM 45464 by name similarity, change the NCBI lineage based on broader culture classification or promote the lifecycle to REVIEWED.

Before a culture-link change, obtain explicit primary-source provenance connecting DSM 45464 to JF777516/taxon 1034870 and reconcile classification/date differences. A verified correction belongs in maintained extraction/source inputs or `src/taxonmech/seed.py` with regression coverage, followed by controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature enrichment requires a supported persistent curation mechanism rather than direct YAML edits.

## Follow-up Checks

- Resolve the DSM candidate using explicit deposit-to-accession provenance or an authoritative correction; retain remaining uncertainty.
- Investigate the paper/accession length discrepancy before literature enrichment. No author/depositor contact was made.
- After an authorized upstream/seeder change, validate and inspect a canary, then run `just verify-corpus` and `just qc`; neither gate ran here.
- Reconcile report coverage against actual YAML files independently of ignore rules. Report-file coverage is not human REVIEWED lifecycle status.

## Additional Notes

NCBI browser HTML was inaccessible through the web reader; EFetch and Datasets succeeded. Initial direct BacDive/DSMZ opens failed; links from the inspected [MediaDive listing](https://mediadive.dsmz.de/strains/medium/1260) succeeded. MediaDive's culture listing was not transferred to the target. StrainInfo's page required JavaScript; its complete native snapshot was used instead.

The first BacDive result was an older cached representation with a 2025 citation; following DSMZ's BacDive link returned the 2026 representation matching the native version. DSMZ's link caption incorrectly names Limosilactobacillus pontis while its destination is this Nocardiopsis BacDive record. That external caption inconsistency is not a supported taxonomic reassignment or an error in the target YAML. No source was edited and no access control was bypassed.

Relevant paper text and Figure 3 were inspected during this turn, including the cached PDFKit rendering of page 6 of the [published open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf), downloaded during the AH0 review. No new PDF/image was written in the repository. The paper was checked for identity context, not exhaustively curated for phenotype, habitat, medium or antimicrobial evidence.

Candidate objects were inspected as identity leads, not counted as reviews of their taxa. No exhaustive external-source census, all-alias search, complete culture-identity resolution or whole-genome equivalence analysis is claimed.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, issue, pull request or external source was changed.
