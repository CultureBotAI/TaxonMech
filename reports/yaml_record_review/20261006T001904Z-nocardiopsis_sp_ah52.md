# YAML Record Review: Nocardiopsis sp. AH52

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah52.yaml`
- Started UTC: 2026-10-06T00:17:16Z
- Finished UTC: 2026-10-06T00:19:04Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034880`, Nocardiopsis sp. AH52, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It has ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, xrefs, literature evidence or causal graph are asserted.

`data/taxa/PATHS.tsv:14199` uniquely resolves the ID and stem; `curation/seed_scope.tsv:322032` supplies inclusion. This target received only a new review report. Records, inputs, scope, history and Eukaryota were untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah52.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah52.yaml --out /private/tmp/ah52-validation.tsv`, exit 0, one file, zero errors. The output TSV was read and contains only its header.
- PASS: complete backbone row, reconstructed lineage, seven source inventories, PATHS, scope, attestation and seed-event text agree. The backbone contains no target children.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, complete marker metadata/references/features, relevant primary-paper text and Figure 3.
- Not applicable: graph-term, LPSN/GTDB mapping and iModulonDB checks. No corresponding graph, mapping, gene/regulator or expression-module assertion is present.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. These bounded checks do not prove corpus reproduction or publication readiness.

Required guidance, checklist, relevant schema classes and seed-timestamp behavior were read this turn. Guidance/schema/seeder/target diffs were empty. No history entry or lifecycle promotion was made under the read-only review contract.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034880&retmode=xml) confirms ID, exact label, species rank, bacterial division, parent and genetic code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034880) agrees and includes all ten ancestor IDs, including root.

The root-first chain matches the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies non-root ancestry; Datasets includes root explicitly.

This informal name does not assert validly published nomenclature. A submitted marker's strain qualifier does not change the NCBI concept's species rank. `EXACT` grounds this taxon, not species equivalence to a named relative or specimen equivalence to another AH52 designation.

## Evidence

| Assertion | Inspected support |
|---|---|
| Identity, rank, parent and code | Complete `data/raw/ncbitaxon_taxa.tsv:221729` and both NCBI authorities. |
| Lineage | Full reconstructed backbone chain and live ancestry. |
| Scientific name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31132`; all backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | Backbone attests only ncbitaxon; source, ID, label, count, unit and snapshot note agree. NAME is not a strain or genome count. |
| Scope and seed event | Scope line 322032 supplies 2026-09-13 and the exact one-source attested-rule reason; event text agrees. |
| Seed timestamp | 2026-09-13T17:54:04Z is the maximum of raw 17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z manifest extraction times on that date, following `src/taxonmech/seed.py:139`. |
| Zero strains | No BacDive inventory association under this taxon and no backbone children. This source-classification count does not mean AH52 was never cultivated. |

The exact `txid1034880[Organism:noexp]` query returned one Nuccore UID, 333497029. Complete [JF777525.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497029), references and features were read, excluding sequence bases. The 1,422-base 16S marker is partial at both ends. Source qualifiers identify AH52, taxon 1034880, Saharan soil, Algeria and collection year 2010, without a culture-collection qualifier.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. No DOI or PMID is supplied. This establishes submitted specimen context, not a deposit or genome identity. The exact Assembly query returned zero items with phrase-not-found/no-items messages; absence under other classifications or indexing was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, groups AH52 with AH1 in cluster V, reporting 99.3-99.6% similarity to N. litoralis and 99.0-99.4% to N. kunsanensis, not an individual AH52 value. Figure 3 labels AH52 as JF777525, agreeing with NCBI. Its 1,529-1,544-base range differs from the submitted 1,422 bases. Neither comparison establishes species equivalence; the length discrepancy remains unresolved.

Neither length nor the literature comparisons are YAML assertions or required missing fields.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034880. Empty optional slots agree with the inputs; record-level literature evidence is optional for seeded records.

The following bounded searches included ignored/hidden files and compressed native catalogs:

- `rg --no-ignore --hidden -n -z -i` searched ID, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All 20 matches were read in full as native JSON or header-aware TSV: three target backbone/name/scope rows and 17 numeric substring matches.
- An AH52/AH-52/AH 52/AH_52 search across those ten roots returned ten rows: three target rows and seven other-organism genome objects. All were read in full, and full-row addresses were reconciled against search results. No BacDive inventory, native BacDive or StrainInfo row matched this alias screen.
- JF777525 returned no matches across those roots. This bounded local absence does not establish a required missing genome link or global absence of sequence evidence.
- Before writing, ignored-inclusive ID/full-label/slug searches of reports/history returned no hits; `find` found no prior exact-stem report.

The seven non-target alias objects concern Acinetobacter haemolyticus WU_MDCI_Ah52 and Klebsiella pneumoniae AH52/AH_52, detailed below. None establishes a target culture or genome connection. No inspected source establishes a consequential missing target strain-to-genome relationship. No exhaustive external census or all-alias search is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

No issue found in the YAML's assertions. Identity, lineage, provenance and source-classification count are supported. The external length discrepancy remains unresolved but is not asserted by this record.

## Recommended Edits

None required on current evidence. Do not hand-edit generated YAML, equate AH52 with named Nocardiopsis relatives, transfer another organism's same-name genome links or promote lifecycle to REVIEWED.

A verified future correction belongs in maintained extraction/source inputs or `src/taxonmech/seed.py`, with regression coverage and controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature enrichment needs a supported persistent curation mechanism rather than direct YAML edits.

## Follow-up Checks

- Reconcile publication and accession lengths before enrichment. No author or depositor contact was made.
- Require explicit deposit-to-target/sequence provenance before adding strain or genome links; preserve source versions and entity types.
- After an authorized upstream/seeder change, inspect and validate a canary, then run `just verify-corpus` and `just qc`; neither gate ran here.
- Reconcile reports against actual YAML files independently of ignore rules. Report coverage does not confer human REVIEWED status.

## Additional Notes

All seven non-target alias objects were inspected:

- Acinetobacter haemolyticus WU_MDCI_Ah52, taxon 29430: GCA/GCF_025562235.1, SAMN19774085, BV-BRC 29430.126 and GTDB RS_GCF_025562235.1. Full objects occur in BV-BRC shard 0017 line 34031, GenBank shard 0023 line 35345, RefSeq 0004 line 28342 and GTDB 0006 line 13614. GTDB retains A. haemolyticus and respiratory-tract/St. Louis source context, not the Algerian Nocardiopsis marker context.
- K. pneumoniae AH52, taxon 573: GCA/GCF_057664905.1, SAMN54997889, GenBank shard 0053 line 16196 and RefSeq 0008 line 44158.
- Separate K. pneumoniae AH_52: GCA_053068405.1, SAMN50315171, GenBank shard 0049 line 522. No name-based equivalence to the preceding strain or this target was inferred.

The 17 numeric substring matches were inspected and not treated as target-taxonomy matches:

- E. coli PNUSAE018417, taxon 562: BV-BRC 562.36560, SAMN10348808, GCA_003764505.1/.2. Full objects occur in BV-BRC shard 0023 line 36410, GenBank historical 0000 line 10548 and current 0002 line 48550. The historical .1 is replaced; .2 is current.
- E. coli PNUSAE018829: BV-BRC 562.36569, SAMN10348800, GCA_003765485.1/.2/.3. BV-BRC 0023 line 36418, GenBank historical 0000 lines 10560/10561 and current 0002 line 48595 preserve replaced .1/.2 and current .3.
- E. coli PNUSAE018828: GCA_016556185.1, SAMN10348804, GenBank shard 0015 line 3886.
- M. tuberculosis ERR1034880, taxon 1773: BV-BRC shard 0006 line 6346, genome 1773.18531.
- Campylobacter jejuni PNUSAC013705, taxon 197: GCA_010348805.1, SAMN13354235, GenBank shard 0009 line 6278.
- Ardenticatenaceae bacterium CHLO-12, taxon 2614247: GCA_048499655.1, SAMN31034880, GenBank shard 0044 line 37001 and GTDB 0001 line 42456. GTDB calls it CAADGU01 sp023382655.
- ATB row 65887 supplies S. dysgalactiae subsp. equisimilis/SAMEA1034880/ERR085035/ERZ3070261; row 569350 supplies M. tuberculosis/SAMEA3558413/ERR1034880/ERZ3501044. Rows 1502175/1502176/1502177 supply E. coli samples SAMN10348800/SAMN10348804/SAMN10348808, runs SRR8136869/SRR8136859/SRR8136834 and analyses ERZ9092400/ERZ9092401/ERZ9092404. Samples, runs and analyses do not establish target taxonomy or genome equivalence.

Catalog shards are under `data/catalog/`, BV-BRC shards under `data/bvbrc/`, and ATB rows in `data/catalog/allthebacteria.tsv.xz`. These candidate objects were identity leads, not separate taxon reviews.

Relevant primary-paper text and Figure 3 were inspected this turn, including the cached page-6 rendering of the [open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf). No new PDF or image was written in the repository. Phenotype and antimicrobial claims were not exhaustively curated.

Review performed on `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, GitHub item or external source was changed.
