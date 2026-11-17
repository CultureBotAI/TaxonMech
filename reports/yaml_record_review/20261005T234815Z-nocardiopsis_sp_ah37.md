# YAML Record Review: Nocardiopsis sp. AH37

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah37.yaml`
- Started UTC: 2026-10-05T23:45:30Z
- Finished UTC: 2026-10-05T23:48:15Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034874`, Nocardiopsis sp. AH37, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It carries ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence or causal graph are asserted.

`data/taxa/PATHS.tsv:14193` uniquely resolves the identifier and stem; `curation/seed_scope.tsv:322026` supplies inclusion. Only this new report was written for this target. Records, source inputs, scope, history and Eukaryota were left untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah37.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah37.yaml --out /private/tmp/ah37-validation.tsv`, exit 0, one file, zero errors. The output TSV was read and contains only its header.
- PASS: structured comparisons checked the complete backbone row, reconstructed ancestor chain, seven source inventories, PATHS, scope, exact NCBITAXON attestation and seed-event text. The backbone supplies no children of the target.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, complete metadata/features for AH37's marker and the paper's conflicting accession, relevant primary-paper text and Figure 3, and candidate BacDive/DSMZ pages.
- Not applicable: target-specific LPSN/GTDB mapping validation, graph-term validation and iModulonDB. No such mapping, graph, gene/regulator assertion or expression module is present.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. These bounded checks do not prove corpus reproduction or publication readiness.

Required guidance, relevant schema classes, validator definitions and seed-timestamp behavior were read earlier in this sequence. The review skill was reread this turn. HEAD remained unchanged; guidance/schema/seeder/target diffs were empty. The ignored-inclusive search below found no target history entry. No history entry or lifecycle promotion was made under the read-only review contract.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034874&retmode=xml) confirms identifier, exact label, species rank, bacterial division, parent 2649073 and genetic code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034874) confirms identifier/name/rank and all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies non-root ancestry; Datasets includes root explicitly.

The informal label does not assert validly published nomenclature. A marker's strain qualifier does not change the NCBI concept's species rank. `EXACT` identifies this precise taxon, not equivalence to N. terrae or DSM 45465.

## Evidence

| Claim | Inspected support |
|---|---|
| Identity, parent, rank and code | Complete `data/raw/ncbitaxon_taxa.tsv:221723` row and both live NCBI authorities. |
| Lineage | Full reconstructed backbone chain and authority ancestry. |
| Scientific name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31126`; all three backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | Backbone attests only ncbitaxon, snapshot 2026-09-13. Source, ID, label, count, unit and note agree; NAME is not a strain or genome count. |
| Scope and event | Scope line 322026 supplies date 2026-09-13 and the exact one-source attested-rule reason; embedded event text agrees. |
| Seed timestamp | The event's 2026-09-13T17:54:04Z is the maximum of the previously inspected raw, ATB and StrainInfo manifest extraction times, following `src/taxonmech/seed.py:139`. |
| Zero BacDive strains | No inventory strain is classified under taxon 1034874, and the backbone supplies no descendants. This source-classification count does not claim AH37 was never cultivated. |

The exact query `txid1034874[Organism:noexp]` returned one Nuccore UID, 333497024. Complete [JF777520.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497024), references and features were inspected, excluding sequence bases. This is a 1,418-base 16S rRNA marker, partial at both ends. Source qualifiers identify Nocardiopsis sp. AH37, strain AH37, taxon 1034874, Saharan soil, Algeria and collection year 2010; no culture-collection qualifier is supplied.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. No DOI or PMID is supplied in that metadata. These establish submitted marker/specimen context, not a genome or deposit identity.

The exact Assembly query returned zero items with phrase-not-found/no-items messages. No assembly was retrieved under this query; absence under alternate classification or indexing was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, reports 99.4% similarity between AH37 and N. terrae. Figure 3 labels both AH37 and AH0 as JF777508, while assigning JF777520 to AH38. These labels conflict with inspected NCBI annotations: JF777520.1 identifies AH37; [JF777508.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=JF777508.1) identifies AH0/taxon 1034863, 1,420 bases. The paper's 1,529-1,544-base range also differs. The publication-to-marker mapping remains unresolved; no corrected tree or species equivalence was inferred.

The second accession was fetched in full metadata/features to distinguish the actual submitted identities, not to rereview AH0. Neither the conflicting publication labels nor a marker sequence is an asserted YAML field here.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034874. Empty optional slots agree with those inputs. Literature evidence is optional for seeded records; the paper does not establish a required missing representation.

The following searches included ignored/hidden files and compressed native catalogs:

- `rg --no-ignore --hidden -n -z -i` searched identifier, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All 21 matches were read in full as JSON or header-aware TSV.
- Three matches are target backbone/name/scope. `data/bvbrc/bvbrc-0006.jsonl.gz:6337` is Mycobacterium tuberculosis ERR1034874, taxon 1773, genome 1773.18523.
- `data/bvbrc/bvbrc-0021.jsonl.gz:22970`, `data/catalog/ncbi_genbank-0044.jsonl.gz:37008` and `gtdb_genomes-0010.jsonl.gz:21453` concern Rubrivivax sp. PROT-6, taxon 50259, genome 50259.272, GCA_048499795.1 and SAMN31034874. GTDB supplies Rubrivivax sp011525985; none identifies Nocardiopsis.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6275` is Campylobacter jejuni FSIS21926105, taxon 197, GCA_010348745.1. `ncbi_genbank-0002.jsonl.gz:8293` is Rhodobiaceae bacterium NP1304, taxon 2026785, GCA_002730695.1; its genome size is 1,034,874, not a target taxon reference.
- Escherichia coli PNUSAE015895 and PNUSAE015712, taxon 562, carry samples SAMN10348744/SAMN10348749. `data/bvbrc/bvbrc-0023.jsonl.gz:36379` and line 36627 supply genomes 562.36523/562.36780 and GCA_003760405.1/GCA_003775855.1. `data/catalog/ncbi_genbank-0002.jsonl.gz:48346` and line 49111 supply the respective .2 assemblies; historical shard 0000 lines 10516/10658 retain replaced .1 versions. Neither the samples nor assembly versions imply target identity.
- `data/catalog/ncbi_genbank-0033.jsonl.gz:35508` is Streptococcus pneumoniae isolate 414, taxon 1313, GCA_036052275.1, assembly name PDT001034874.1.
- `data/catalog/allthebacteria.tsv.xz:65881` supplies Streptococcus dysgalactiae subsp. equisimilis sample SAMEA1034874, run ERR084990 and ERZ3070256. Row 569344 supplies Mycobacterium tuberculosis run ERR1034874, sample SAMEA3558407 and ERZ3501025. Rows 1502165/1502166 supply Escherichia coli samples SAMN10348744/SAMN10348749, runs SRR8136837/SRR8136838, analyses ERZ9092384/ERZ9092387. Row 3092404 supplies E. coli sample SAMN44338756/run SRR31034874/ERZ27111264 with non-HQ and Sylph-failure flags. These are not target associations; no sample-to-assembly equivalence was inferred.
- A separate JF777520/JF777508 search across the ten roots returned zero matches. These are bounded local absences, not required missing genome links.
- An AH37/AH-37/AH 37/AH_37 screen of the BacDive inventory, native BacDive and StrainInfo returned three rows, all read in full. A supplemental alias search across the ten roots returned 17 rows, all read in full: three target rows, three culture-source rows, six other-taxon name/backbone/scope rows and five assembly objects.
- A DSM 45465/typed BacDive and StrainInfo identifier search across the ten roots returned seven rows, all read in full, including four additional culture-crosswalk rows.
- Before writing, an ignored-inclusive identifier/full-label/slug search of `reports/yaml_record_review` and `history` returned no matches; a filesystem search found no prior exact-stem report.

DSM 45465 is a plausible but unproven target association:

- `data/raw/bacdive_strains.tsv:82933` and `data/bacdive/records.jsonl.gz:82932` supply BacDive 160696, Nocardiopsis terrae AH37, taxon 372655, DSM 45465, non-type, with empty native sequence information.
- `data/straininfo/records.jsonl.gz:296748` supplies published-online SI-ID 398859, DOI 10.60712/SI-ID398859.2, BacDive 160696, designation AH37 and taxon 372655. Its own available DSM 45465/SI-DP 905603 deposit is non-type and supplies no sequence entries.
- `data/straininfo/strain_links.tsv:60221`, `related_records.tsv.gz:141506` and line 141507 preserve this deposit/strain chain under taxon 372655. `data/raw/culture_collection_strains.tsv:81465` agrees. These are typed strain/deposit references, not genomes, and none classifies the deposit under target taxon 1034874.
- The [BacDive page](https://bacdive.dsmz.de/strain/160696) confirms the designation, deposit, N. terrae classification, taxon 372655, Algerian Saharan soil and N. Sabaou laboratory provenance; no target accession is supplied. The native non-type flag was retained rather than reading a bare page heading as a type assertion.
- The inspected [DSMZ catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-45465) identifies N. terrae AH37 from N. Sabaou, LPBVB, Kouba, and gives sampling year 2003, unlike the marker's 2010. It supplies neither JF777520 nor taxon 1034874.
- Shared designation, genus, region and laboratory make the candidate plausible. Classification and collection-date differences remain explicit. No inspected source establishes the deposit-to-marker/target connection. The evidence proves neither identical nor distinct specimens; no association or synonym was inferred.

Other supplemental aliases were separated:

- Bacillus sp. AH37, taxon 861676: scope line 285649, backbone line 181186, `data/catalog/ncbi_names-0004.jsonl.gz:34870`. Acetobacter sp. VTH-AH37, taxon 1769148: scope line 524180, backbone line 462080, `ncbi_names-0010.jsonl.gz:47937`.
- Escherichia coli AH37, taxon 562: paired GCA_019369915.1/GCF_019369915.1, SAMN17183264, `data/catalog/ncbi_genbank-0017.jsonl.gz:38882` and `ncbi_refseq_historical-0000.jsonl.gz:43041`. The RefSeq record is suppressed.
- Klebsiella pneumoniae AH37, taxon 573: paired GCA_057665605.1/GCF_057665605.1, SAMN54997867, `data/catalog/ncbi_genbank-0053.jsonl.gz:16230` and `ncbi_refseq-0008.jsonl.gz:44180`. Separate AH_37 assembly GCA_053075325.1/SAMN50316222 occurs in `ncbi_genbank-0049.jsonl.gz:868`.

No inspected source establishes a consequential missing target strain-to-genome relationship or required correction. DSM 45465 remains an unresolved identity lead, not an authorized join or negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's assertions. Identity, lineage, provenance and source-classification count are supported. The culture candidate and publication/accession conflicts remain unresolved, but are not asserted by this generated record.

## Recommended Edits

None required on current evidence. Do not hand-edit the generated YAML, attach DSM 45465 by name similarity, infer N. terrae equivalence, substitute the paper's accession labels or promote the lifecycle to REVIEWED.

Before a culture-link change, obtain explicit primary-source provenance connecting DSM 45465 to JF777520/taxon 1034874 and reconcile classification/date differences. Resolve the publication's accession assignments before using its tree as target-specific evidence. A verified correction belongs in maintained extraction/source inputs or `src/taxonmech/seed.py` with regression coverage and controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature enrichment requires a supported persistent curation mechanism rather than direct YAML edits.

## Follow-up Checks

- Resolve the DSM candidate with explicit deposit-to-accession provenance or an authoritative correction; retain remaining uncertainty.
- Investigate the paper's conflicting labels and sequence lengths before literature enrichment. No author/depositor contact was made.
- After an authorized upstream/seeder change, validate and inspect a canary, then run `just verify-corpus` and `just qc`; neither gate ran here.
- Reconcile report coverage against actual YAML files independently of ignore rules. A report does not confer human REVIEWED status.

## Additional Notes

DSMZ's direct open initially failed; the link from BacDive succeeded. StrainInfo's web page required JavaScript; its complete native snapshot was used instead. No external source was edited and no access control was bypassed.

Relevant primary-paper text and Figure 3 were inspected during this turn, including the cached page-6 rendering of the [published open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf), downloaded during the AH0 review. No new image or PDF was written in the repository. The paper was checked for identity context, not exhaustively curated for phenotype or antimicrobial claims.

Candidate objects were inspected as identity leads, not counted as reviews of their taxa. No exhaustive external census, all-alias search, complete culture-identity resolution or whole-genome equivalence analysis is claimed.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, GitHub item or external source was changed.
