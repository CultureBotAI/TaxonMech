# YAML Record Review: Nocardiopsis sp. AH47

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah47.yaml`
- Started UTC: 2026-10-06T00:12:14Z
- Finished UTC: 2026-10-06T00:15:43Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034879`, Nocardiopsis sp. AH47, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It carries ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, xrefs, literature evidence or causal graph are asserted.

`data/taxa/PATHS.tsv:14198` uniquely resolves this ID and stem; `curation/seed_scope.tsv:322031` supplies inclusion. Only this new report was written. Records, inputs, scope, history and Eukaryota were untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah47.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah47.yaml --out /private/tmp/ah47-validation.tsv`, exit 0, one file, zero errors. The output TSV was read and contains only its header.
- PASS: full backbone row, reconstructed lineage, seven source inventories, PATHS, scope, source attestation and seed-event text agree. No target children occur in the backbone.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, complete marker metadata/references/features, relevant primary-paper text and Figure 3, and an ambiguous alias's marker metadata.
- Not applicable: graph-term, LPSN/GTDB mapping and iModulonDB checks; no corresponding graph, mapping, gene/regulator or expression-module claim is asserted.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. These checks do not establish corpus reproduction or publication readiness.

Required repository guidance, checklist and relevant schema classes were read; guidance/schema/seeder/target diffs were empty. No history entry or human REVIEWED promotion was made under the read-only review contract.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034879&retmode=xml) confirms ID, label, species rank, bacterial division, parent and genetic code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034879) agrees and includes all ten ancestor IDs, including root.

The root-first lineage matches the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies the non-root ancestry; Datasets includes root explicitly.

The informal name does not assert validly published nomenclature. A marker's strain qualifier does not change this NCBI concept's species rank. `EXACT` grounds this taxon; it does not establish equivalence to N. xinjiangensis or to another organism called AH47.

## Evidence

| Assertion | Inspected support |
|---|---|
| Identity, parent, rank and code | Complete `data/raw/ncbitaxon_taxa.tsv:221728` and both NCBI authorities. |
| Lineage | Full reconstructed backbone chain and live ancestry. |
| Name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31131`; all backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | Source, ID, label, count, unit and 2026-09-13 snapshot note agree with the backbone. NAME is not a strain or genome count. |
| Inclusion and event text | Scope line 322031 gives the exact one-source attested-rule reason and date 2026-09-13; the seed event agrees. |
| Event timestamp | Raw, ATB and StrainInfo manifest extraction times are 17:50:44Z, 17:54:04Z and 17:29:00Z on 2026-09-13. The maximum is the recorded 17:54:04Z, following `src/taxonmech/seed.py:139`. |
| Zero strains | No BacDive inventory association under this taxon and no backbone children. This classification count does not mean AH47 was never cultivated. |

The exact `txid1034879[Organism:noexp]` query returned one Nuccore UID, 333497028. Complete [JF777524.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497028), references and features were read, excluding sequence bases. It is a 1,419-base 16S rRNA marker, partial at both ends, with AH47, taxon 1034879, Saharan soil, Algeria and collection year 2010 in the source qualifiers. No culture-collection qualifier is supplied.

The metadata references name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. They supply no DOI or PMID. This supports submitted specimen context, not a culture-deposit or genome identity. The exact Assembly query returned zero items with phrase-not-found/no-items messages; no global absence under other classifications or indexing is claimed.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, includes AH47 in cluster I and reports a pooled 99.4-99.8% similarity range to N. xinjiangensis for several clusters and AH4, not a separate AH47 percentage. Figure 3 labels AH47 as JF777524, agreeing with NCBI. Its 1,529-1,544-base sequence range differs from the submitted 1,419 bases. Neither similarity nor tree placement proves species equivalence; the length discrepancy remains unresolved.

Neither length nor the comparison is asserted by this YAML. These external details do not establish a required missing representation.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034879. Empty optional slots agree with the inputs. Record-level literature evidence is optional for seeded records.

Bounded searches included ignored/hidden files and compressed native catalogs:

- `rg --no-ignore --hidden -n -z -i` searched ID, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All 17 matches were read in full as native JSON or header-aware TSV: three target backbone/name/scope rows and 14 numeric substring matches.
- An AH47/AH-47/AH 47/AH_47 search across those ten roots returned 27 rows. All were read in full: three target rows, nine rows for three other NCBI concepts, one StrainInfo object, four GOLD objects and ten other genome objects. Full-row addresses were reconciled against search results.
- No BacDive inventory or native BacDive row matched that alias search. Its only StrainInfo hit was Micrococcus luteus M. Matsuhashi AH-47, not a target culture association.
- JF777524 returned no matches across the ten roots. This is a bounded local absence, not proof of absent sequence or genome evidence elsewhere.
- Before writing, ignored-inclusive ID/full-label/slug searches of reports/history returned no hits; `find` found no prior exact-stem report.

No inspected source establishes a consequential missing target strain-to-genome relationship. Name-only joins would misattribute evidence; the aliases below remain separate. No exhaustive external census or all-alias search is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

No issue found in the YAML's assertions. Identity, lineage, provenance and source-classification count are supported. The external length discrepancy is retained without treating unasserted content as a record defect.

## Recommended Edits

None required on current evidence. Do not hand-edit generated YAML, infer N. xinjiangensis equivalence, transfer same-name culture/genome evidence or promote lifecycle to REVIEWED.

A verified future identity or link correction belongs in maintained extraction/source inputs or `src/taxonmech/seed.py`, with regression coverage and controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature enrichment needs a supported persistent curation mechanism rather than a direct YAML edit.

## Follow-up Checks

- Reconcile the publication and accession lengths before using that detail in enrichment. No author or depositor was contacted.
- Require an explicit target/deposit/sequence provenance chain before adding a strain or genome link; preserve accession versions and entity types.
- After an authorized upstream/seeder change, inspect and validate a canary, then run `just verify-corpus` and `just qc`; neither ran here.
- Reconcile report coverage against actual YAML files independently of ignore rules. A report does not confer human REVIEWED status.

## Additional Notes

Other AH47 aliases were inspected and not joined:

- Bacterium AH47, taxon 124432: scope line 148449, backbone line 23715, `ncbi_names-0000.jsonl.gz:45206`. An exact NCBI query returned one marker UID, 11544610. Complete [AJ289963.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=11544610) identifies a 1,430-base 16S sequence from Germany: Lake Fuchskuhle, classified in Bacteroidota and submitted on 2000-04-07. That source context distinguishes the alias from the Algerian Nocardiopsis submission. Its cited publication was not separately reviewed; no findings about that paper are asserted.
- Streptomyces sp. AH47, taxon 684556: scope 267674, backbone 160706, `ncbi_names-0004.jsonl.gz:11171`. Burkholderia sp. AH47, taxon 861699: scope 285672, backbone 181209, the same names shard line 34893.
- Micrococcus luteus M. Matsuhashi AH-47, taxon 1270: `data/straininfo/records.jsonl.gz:53801` supplies SI-ID 66506, DOI 10.60712/SI-ID66506.1, own available CCM 3394/SI-DP 219362, non-type, with no sequence entries. `data/gold/organisms.jsonl.gz:154265` supplies Go0216093 under the same classification. Neither asserts a target link.
- E. coli AH47, taxon 562: GCA/GCF_003291415.1, SAMN08148349, BV-BRC 562.30493, GTDB RS_GCF_003291415.1. Full objects occur in GenBank shard 0002 line 29780, RefSeq 0001 line 45843, BV-BRC 0023 line 33828 and GTDB 0007 line 19688. GTDB classifies it as ECMA0423 sp047199055. GOLD organism Go0464163 (line 319002), project Gp0337439 (231816) and analysis Ga0323139 (188417) retain an explicit project chain to that assembly, not to this target. Go/Gp/Ga remain organism/project references.
- Another E. coli AH47: GCA_019369835.1 and suppressed historical GCF_019369835.1, SAMN17183268, GenBank shard 0017 line 38878 and RefSeq historical 0000 line 43037. No name-based equivalence to the preceding assembly was inferred.
- K. pneumoniae AH47, taxon 573: GCA/GCF_057665345.1, SAMN54997874, GenBank shard 0053 line 16217 and RefSeq 0008 line 44173. Separate K. pneumoniae AH_47: GCA_053064105.1, SAMN50315381, GenBank 0049 line 312.
- N. gonorrhoeae ah47, taxon 485: GCA_046241905.1, SAMEA114004403, GenBank shard 0042 line 32143. This is another organism's isolate metadata, not target evidence.

The 14 numeric substring matches were also read in full:

- E. coli PNUSAE018723 and PNUSAE018722: SAMN10348792/SAMN10348795, BV-BRC 562.36511/562.36568, GCA_003759805.1/.2 and GCA_003765465.1/.2. BV-BRC shard 0023 lines 36367/36417, GenBank historical 0000 lines 10508/10559 and current 0002 lines 48316/48594 retain the replaced .1 and current .2 versions.
- M. tuberculosis ERR1034879, taxon 1773: BV-BRC shard 0006 line 6347, genome 1773.18532.
- Candidatus Zambryskiibacteriota bacterium PATE-6, taxon 2053652: GCA_048499675.1, SAMN31034879, GenBank shard 0044 line 37002 and GTDB 0008 line 7160. GTDB calls it JASNZL01 sp048499675.
- Faecousia sp. rk3_bin_270, taxon 2952921: GCA_965334735.1, SAMEA118408455, GenBank shard 0064 line 18158. The match is its genome size, 1034879, not taxonomy.
- ATB row 65886 identifies S. dysgalactiae subsp. equisimilis/SAMEA1034879/ERR085065/ERZ3070267; row 569349 identifies M. tuberculosis/SAMEA3558412/ERR1034879/ERZ3501045. Rows 1502173/1502174 identify E. coli samples SAMN10348792/SAMN10348795, runs SRR8136845/SRR8136864 and analyses ERZ9092398/ERZ9092399. These samples/runs/analyses do not establish target identity.

Catalog shards are under `data/catalog/`, BV-BRC shards under `data/bvbrc/`, and ATB rows in `data/catalog/allthebacteria.tsv.xz`. GOLD rows are in their respective organism/project/analysis native files. Candidate objects were identity leads, not separate taxon reviews.

Relevant primary-paper text and the cached page-6 rendering of its [open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf) were inspected this turn. Phenotype and antimicrobial claims were not exhaustively curated. No new PDF or image was written in the repository.

Review performed on `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, GitHub item or external source was changed.
