# YAML Record Review: Nocardiopsis sp. AH38

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah38.yaml`
- Started UTC: 2026-10-05T23:51:02Z
- Finished UTC: 2026-10-05T23:55:19Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034875`, Nocardiopsis sp. AH38, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It carries ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, xrefs, literature evidence or causal graph are asserted.

`data/taxa/PATHS.tsv:14194` uniquely resolves the identifier and stem; `curation/seed_scope.tsv:322027` supplies inclusion. Only this new report was written for this target. Records, source inputs, scope, history and Eukaryota were left untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah38.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah38.yaml --out /private/tmp/ah38-validation.tsv`, exit 0, one file, zero errors. The TSV was read and contains only its header.
- PASS: complete backbone row, reconstructed lineage, seven source inventories, PATHS, scope, attestation and seed-event text agree. The backbone supplies no children of this target.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy; exact Assembly/Nuccore queries; complete marker metadata, references and features; relevant primary-paper text and Figure 3; candidate BacDive and DSMZ pages.
- Not applicable: LPSN/GTDB mapping validation, graph-term validation and iModulonDB. No corresponding mapping, graph, gene/regulator or expression-module assertion is present.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. These bounded checks do not prove corpus reproduction or publication readiness.

Required guidance, relevant schema classes, validators and seed-timestamp behavior were read earlier in this sequence. The review skill and field checklist were reread this turn. HEAD remained unchanged; guidance/schema/seeder/target diffs were empty. No history entry or lifecycle promotion was made under the read-only review contract.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034875&retmode=xml) confirms ID, exact label, species rank, bacterial division, parent 2649073 and code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034875) agrees and supplies all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies the non-root ancestry; Datasets includes root explicitly.

This informal label does not assert validly published nomenclature. A marker's strain qualifier does not change the NCBI concept's species rank. `EXACT` identifies this taxon, not equivalence to N. litoralis, N. xinjiangensis or DSM 45466.

## Evidence

| Claim | Inspected support |
|---|---|
| Identity, rank, parent and code | Complete `data/raw/ncbitaxon_taxa.tsv:221724` row and both live NCBI authorities. |
| Lineage | Reconstructed backbone chain and authority ancestry. |
| Scientific name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31127`; all backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | Backbone attests only ncbitaxon, snapshot 2026-09-13; ID, label, count, unit and note agree. NAME is not a strain or genome count. |
| Scope and event | Scope line 322027 gives date 2026-09-13 and the exact one-source attested-rule reason; event text agrees. |
| Seed timestamp | 2026-09-13T17:54:04Z is the maximum of the previously inspected raw, ATB and StrainInfo extraction times, following `src/taxonmech/seed.py:139`. |
| Zero BacDive strains | No inventory strain is classified under taxon 1034875, and the backbone supplies no descendants. This is a source-classification count, not a claim that AH38 was never cultivated. |

The exact query `txid1034875[Organism:noexp]` returned one Nuccore UID, 333497025. Complete [JF777521.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497025), references and features were inspected, excluding sequence bases. It is a 1,419-base 16S rRNA marker, partial at both ends. Source qualifiers identify AH38, taxon 1034875, Saharan soil, Algeria and collection year 2010, without a culture-collection qualifier.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. No DOI or PMID is supplied in that metadata. These establish submitted marker context, not genome or deposit identity.

The exact Assembly query returned zero items with phrase-not-found/no-items messages. No assembly was retrieved under this query; absence under alternate classification or indexing was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, reports 99.2% similarity between AH38 and N. litoralis. Figure 3 labels AH38 as JF777520, conflicting with inspected NCBI annotations: JF777521.1 identifies AH38; [JF777520.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=JF777520.1) identifies AH37/taxon 1034874, 1,418 bases. The paper's 1,529-1,544-base range also differs. Publication-to-marker mapping remains unresolved; no corrected tree or species equivalence was inferred.

The second accession was inspected in complete metadata/features only to distinguish the submitted identities, not to rereview AH37. Neither marker nor publication labels are asserted YAML fields here.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034875. Empty optional slots agree with those inputs; literature evidence is optional for a seeded record.

Ignored/hidden files and compressed native catalogs were included in the following bounded searches:

- `rg --no-ignore --hidden -n -z -i` searched the ID, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All 26 matches were read in full as JSON or header-aware TSV. Three are the target backbone/name/scope rows; the other 23 are numeric substrings, not target associations.
- An AH38/AH-38/AH 38/AH_38 search across those ten roots returned 13 rows, all read in full: three target rows, three culture-source rows, three Burkholderia taxon rows and four unrelated assembly objects.
- A deposit/typed-identifier search returned seven rows, all read in full, including four additional culture-crosswalk rows.
- A JF777521/JF777520 search across the ten roots returned no matches. This is a bounded local absence, not a required missing genome link.
- Before writing, an ignored-inclusive ID/full-label/slug search of `reports/yaml_record_review` and `history` returned no matches; `find` found no prior exact-stem report.

DSM 45466 is a plausible but unproven target association:

- `data/raw/bacdive_strains.tsv:82771` and `data/bacdive/records.jsonl.gz:82770` supply BacDive 160534, Nocardiopsis xinjiangensis AH38, taxon 124285, DSM 45466, non-type, with empty native sequence information. The species-level synonym in that object was not transferred to the target.
- `data/straininfo/records.jsonl.gz:298913` supplies published-online SI-ID 401024, DOI 10.60712/SI-ID401024.1, BacDive 160534, AH38 and taxon 124285. Its available DSM 45466/SI-DP 907924 deposit is non-type and supplies no sequence entries.
- `data/straininfo/strain_links.tsv:59923`, `related_records.tsv.gz:140831` and line 140832 preserve the strain/deposit chain under taxon 124285. `data/raw/culture_collection_strains.tsv:81466` agrees. These are typed strain/deposit references, not genomes or target-taxonomy assertions.
- The [BacDive page](https://bacdive.dsmz.de/strain/160534) confirms AH38, DSM 45466, N. xinjiangensis, taxon 124285, Algerian Saharan soil and N. Sabaou laboratory provenance, but supplies no target accession. The native non-type flag was retained; a bare page heading was not treated as a positive type assertion.
- The [DSMZ catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-45466) gives AH38 from N. Sabaou, LPBVB, Koupa, Algeria, and sampling year 2003, unlike the marker's 2010. It supplies neither JF777521 nor target taxon 1034875.
- Shared designation, genus, region and laboratory make the candidate plausible. Classification and collection-date differences remain explicit. No inspected source establishes the deposit-to-marker/target connection. The evidence proves neither identical nor distinct specimens; no join or synonym was inferred.

Other aliases were separated: Burkholderia sp. AH38, taxon 861694 (scope line 285667, backbone line 181204, `data/catalog/ncbi_names-0004.jsonl.gz:34888`); Klebsiella pneumoniae AH38, taxon 573 (paired GCA_057665585.1/GCF_057665585.1, SAMN54997868, GenBank shard 0053 line 16229/RefSeq shard 0008 line 44179); separate K. pneumoniae AH_38 (GCA_053071385.1, SAMN50316420, GenBank shard 0049 line 671); and Neisseria gonorrhoeae ah38, taxon 485 (GCA_046241415.1, SAMEA114004428, GenBank shard 0042 line 32118).

No inspected source establishes a consequential missing target strain-to-genome relationship or required correction. DSM 45466 remains an unresolved lead, not an authorized join or negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's assertions. Identity, lineage, provenance and source-classification count are supported. The culture candidate and publication/accession conflicts remain unresolved but are not asserted by this generated record.

## Recommended Edits

None required on current evidence. Do not hand-edit the generated YAML, attach DSM 45466 by designation alone, infer named-species equivalence, substitute paper accession labels or promote lifecycle to REVIEWED.

Before a culture-link change, obtain explicit provenance connecting DSM 45466 to JF777521/taxon 1034875 and reconcile classification/date differences. Resolve the publication's accession assignments before using its tree as target-specific evidence. A verified correction belongs in maintained extraction/source inputs or `src/taxonmech/seed.py`, with regression coverage and controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature enrichment needs a supported persistent curation mechanism rather than direct YAML edits.

## Follow-up Checks

- Resolve the culture candidate with explicit deposit-to-accession provenance or an authoritative correction; retain uncertainty until then.
- Reconcile paper labels and sequence lengths before literature enrichment. No author/depositor contact was made.
- After an authorized upstream/seeder change, validate and inspect a canary, then run `just verify-corpus` and `just qc`; neither gate ran here.
- Reconcile report coverage against actual YAML files independently of ignore rules. A report does not confer human REVIEWED status.

## Additional Notes

The 23 non-target numeric matches were inspected, not silently discarded:

- Pseudomonas aeruginosa Pae_CF67.07p, taxon 287: BV-BRC genome 287.1595, GCA/GCF_001034875.1, SAMN03566360, PRJNA282164 and LEGG. Full objects: BV-BRC shard 0016 line 22030; GenBank shard 0000 line 36022; RefSeq shard 0000 line 30427; GTDB shard 0003 line 26610; GOLD analyses line 101298. GOLD Ga0158519/Gp0189750 supplies no organism-ID chain to infer.
- Escherichia coli PNUSAE015711, taxon 562: BV-BRC genome 562.36555, SAMN10348755, GCA_003764265.1/.2. Full objects: BV-BRC shard 0023 line 36405; GenBank historical shard 0000 line 10544 (replaced .1); current shard 0002 line 48538 (.2). ATB row 1502167 gives that sample, SRR8136833 and ERZ9092389.
- Mycobacterium tuberculosis ERR1034875, taxon 1773: BV-BRC shard 0006 line 6338, genome 1773.18524. ATB row 569345 gives SAMEA3558408, ERR1034875 and ERZ3501030.
- Klebsiella pneumoniae isolate 1922694, taxon 573: GCA_031034875.1/.2/.3, SAMN34998330. GenBank historical shard 0001 lines 21159/21160 holds replaced versions; current shard 0028 line 43432 holds .3.
- Eubacterium ramulus 1757_1757L_C_2, taxon 39490: GCA_061034875.1, SAMN60702911, GenBank shard 0056 line 27270, metagenomic origin.
- Anaerolineales bacterium CHLO-4, taxon 2073117: GCA_048499755.1, SAMN31034875, GenBank shard 0044 line 37006 and GTDB shard 0016 line 19739. GTDB supplies Villigracilis sp023382575, not a target mapping.
- Streptococcus pneumoniae isolate 411, taxon 1313: GCA_036052255.1, assembly name PDT001034875.1, SAMN11116897, GenBank shard 0033 line 35507.
- Remaining ATB rows: 65882, Streptococcus dysgalactiae subsp. equisimilis/SAMEA1034875/ERR085000/ERZ3070255; 1715003, Campylobacter jejuni/SAMN13116673/SRR10348756/ERZ25672197; 1715004, E. coli/SAMN13116685/SRR10348758/ERZ25672209; 1715005, E. coli/SAMN13116687/SRR10348757/ERZ25672221; 3092400, E. coli/SAMN44338752/SRR31034875/ERZ27111240. Samples, runs and analysis accessions were not recast as target taxa or genome equivalence.

Catalog shard paths above are under `data/catalog/`, BV-BRC shards under `data/bvbrc/`, GOLD analyses at `data/gold/analyses.jsonl.gz`, and ATB rows at `data/catalog/allthebacteria.tsv.xz`.

DSMZ direct access initially failed; the linked page from BacDive succeeded. StrainInfo's rendered web result supplied no substantive record text, so the complete native snapshot was used. Relevant paper text and Figure 3 were inspected, including the cached page-6 rendering of the [open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf). No new PDF or image was written in the repository. Phenotype and antimicrobial claims were not exhaustively curated.

Candidate objects were identity leads, not separate taxon reviews. No exhaustive external census, all-alias search, complete culture-identity resolution or whole-genome equivalence analysis is claimed.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, GitHub item or external source was changed.
