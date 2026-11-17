# YAML Record Review: Nocardiopsis sp. AH4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah4.yaml`
- Started UTC: 2026-10-05T23:57:33Z
- Finished UTC: 2026-10-06T00:00:22Z
- Verdict: pass

## Target

The entire 53-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034876`, Nocardiopsis sp. AH4, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It carries ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, xrefs, literature evidence or causal graph are asserted.

`data/taxa/PATHS.tsv:14195` uniquely resolves the ID and stem; `curation/seed_scope.tsv:322028` supplies inclusion. Only this new report was written for this target. Records, inputs, scope, history and Eukaryota were untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah4.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah4.yaml --out /private/tmp/ah4-validation.tsv`, exit 0, one file, zero errors. The TSV was read and contains only its header.
- PASS: complete backbone row, reconstructed lineage, seven source inventories, PATHS, scope, source attestation and seed-event text agree. The backbone supplies no children of this target.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, complete marker metadata/references/features, and relevant primary-paper text and Figure 3.
- Not applicable: LPSN/GTDB mapping validation, graph-term validation and iModulonDB. No corresponding mapping, graph, gene/regulator or expression-module assertion is present.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. These bounded checks do not prove corpus reproduction or publication readiness.

The review skill, CLAUDE.md, justfile, curation skill/checklist, curation/harmonization/schema guides, history guidance and relevant schema classes were read this turn. Guidance/schema/seeder/target diffs were empty at unchanged HEAD. No history entry or lifecycle promotion was made under the read-only review contract.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034876&retmode=xml) confirms the ID, exact label, species rank, bacterial division, parent 2649073 and genetic code 11, without alternate names. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034876) agrees and supplies all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies non-root ancestry; Datasets includes root explicitly.

This informal name does not assert validly published nomenclature. The submitted marker's strain qualifier does not change the NCBI concept's species rank. `EXACT` means this exact taxon, not equivalence to N. xinjiangensis or every strain named AH4.

## Evidence

| Assertion | Inspected support |
|---|---|
| Identity, rank, parent and code | Complete `data/raw/ncbitaxon_taxa.tsv:221725` row and both NCBI authorities. |
| Lineage | Full reconstructed backbone chain and authority ancestry. |
| Name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31128`; all three backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | Backbone attests only ncbitaxon; source, ID, label, count, unit and snapshot note agree. NAME is not a strain or genome count. |
| Scope and seed event | Scope line 322028 gives date 2026-09-13 and the exact one-source attested-rule reason; event text agrees. |
| Timestamp | Event 2026-09-13T17:54:04Z equals the maximum extracted_at across raw (17:50:44Z), ATB (17:54:04Z) and StrainInfo (17:29:00Z) manifests, following `src/taxonmech/seed.py:139`. |
| Zero strains | No BacDive inventory strain is classified under taxon 1034876; the backbone supplies no descendants. This does not claim AH4 was never cultivated. |

The exact query `txid1034876[Organism:noexp]` returned one Nuccore UID, 333497014. Complete [JF777510.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497014), references and features were inspected, excluding sequence bases. This is a 1,419-base 16S rRNA marker, partial at both ends. Source qualifiers identify AH4, taxon 1034876, Saharan soil, Algeria and collection year 2010, without a culture-collection qualifier.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished halophilic-Nocardiopsis study, and direct submission on 2011-03-07. No DOI or PMID is supplied in the marker metadata. This establishes submitted specimen context, not a genome or deposit identity.

The exact Assembly query returned zero items with phrase-not-found/no-items messages. No assembly was retrieved under that query; absence under alternate classification or indexing was not established.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, includes AH4 among isolates with 99.4-99.8% similarity to N. xinjiangensis. That pooled range is not an AH4-specific percentage or species-equivalence assertion. Figure 3 labels AH4 as JF777510, agreeing with the inspected accession. The paper's 1,529-1,544-base range differs from the submitted 1,419-base marker; that discrepancy remains unresolved.

Neither a marker length nor this literature comparison is asserted by the generated YAML. The paper does not establish a required missing representation.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034876. Empty optional slots agree with those inputs. Record-level literature evidence is optional for seeded records.

The following bounded searches included ignored/hidden files and compressed native catalogs:

- `rg --no-ignore --hidden -n -z -i` searched ID, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding `SOURCE.json` manifests. All 35 matches were read in full as JSON or header-aware TSV: three target backbone/name/scope rows and 32 numeric substring matches.
- An AH4/AH-4/AH 4/AH_4 screen of the BacDive inventory, native BacDive and StrainInfo returned no matches. No culture candidate was found within that scope; this is not a global culture-census claim.
- The supplemental alias search across the ten roots returned 84 rows. All were read in full: three target rows and 81 source objects for other taxa, strain designations or environmental communities. Full-row retrieval was reconciled against the returned addresses.
- JF777510 returned no matches across the ten roots. This is a bounded local absence, not a required missing genome link.
- Before writing, an ignored-inclusive ID/full-label/slug search of `reports/yaml_record_review` and `history` returned no matches; `find` found no prior exact-stem report.

Other name-bearing NCBI concepts were kept separate: Aeromonas hydrophila (`644`, includes Aeromonas sp. Ah4), actinobacterium Shinshu-ah4 (`221585`), Massilia sp. AH4 (`595561`, synonym Naxibacter sp. AH4), Streptomyces sp. AH4 (`732119`), Chroococcidiopsis sp. AH4 (`946466`, synonym AH 4), Marinobacter sp. AH4 (`1142079`), Bacillus sp. enrichment culture clone MNSS-AH-4 (`1534750`), Acinetobacter sp. AH4 (`1707297`), bacterium Ah4 (`1848779`), Vibrio sp. AH4 (`2919577`) and Ruegeria sp. AH4 (`3437463`). Their full backbone/name rows were inspected, plus the ten matching scope rows. No synonym or organism identity was transferred from a shared designation.

The following alias-associated genomes likewise do not establish a target association:

| Source classification/designation | Inspected identifiers and distinctions |
|---|---|
| Fructilactobacillus sanfranciscensis Ah4, taxon 1625 | GCA/GCF_006334415.1, SAMN09095731, BV-BRC 1625.45; BV-BRC uses the older Lactobacillus genus. GTDB and GOLD Go0572458/Gp0547053/Ga0489853 retain this classification/context. |
| Enterococcus gallinarum AH4, taxon 1353 | GCA/GCF_030270565.1, SAMD00599702, BV-BRC 1353.342; GTDB uses Enterococcus_D gallinarum. |
| Xanthomonas oryzae pv. oryzae AH4, taxon 64187 | GCA_003298205.1, SAMN05952987, BV-BRC 64187.468; GOLD Go0460873/Gp0334149/Ga0319042. |
| Burkholderia pseudomallei AH4, taxon 28450 | GCA/GCF_001320325.1, SAMEA1483588, BV-BRC 28450.256; GOLD Go0121507/Gp0129403/Ga0110065 supplies IMG 2657245415. GTDB calls the genome Burkholderia mallei; neither classification denotes Nocardiopsis. |
| Pseudomonas fluorescens AH4, taxon 294 | GCA/GCF_002022265.1, SAMN05589716, BV-BRC 294.255, culture qualifier NRRL:B-30482. Historical RefSeq is suppressed for unverified source organism; GTDB uses Aquipseudomonas lactucae. No deposit link was transferred. |
| Vibrio sp. AH4, taxon 2919577 | GCA/GCF_030710545.1, SAMN26149593, distinct BV-BRC records 2919577.3 and 2919577.4. GTDB/Sylph use Vibrio metoecus; ATB row 2250208 supplies ERZ26439982 and SRR18101041. |
| Ruegeria sp. AH4, taxon 3437463 | GCA/GCF_056541395.1, SAMN48980489. |
| Escherichia coli AH4, taxon 562 | GCA/GCF_019369885.1, SAMN17183265; historical RefSeq is suppressed. |
| Klebsiella pneumoniae AH4 / AH_4, taxon 573 | GCA/GCF_057666145.1, SAMN54997855; separate GCA_053075265.1, SAMN50316225. The similar aliases do not establish identical specimens. |
| Enterococcus faecalis AH_4, taxon 1351 | GCA_060033305.1, SAMN60612254. |

GOLD's environmental AH4 matches concern wine-grape microbial communities (Gp0281230/Ga0236350 and metatranscriptome Gp0281244/Ga0236364, SAMN05963489) and hospital-effluent communities (Gp0476155/Ga0433654, SAMEA3712777). These have no organism-ID link or supplied genome/IMG accession in the inspected objects. Community, sample, project and analysis identifiers were not promoted into target strain/genome links.

No inspected source establishes a consequential missing target strain-to-genome relationship or required correction. Search results about Streptomyces AH4 were not treated as evidence about Nocardiopsis AH4.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's assertions. Identity, lineage, provenance and source-classification count are supported. The external sequence-length discrepancy is retained but is not a YAML assertion.

## Recommended Edits

None required on current evidence. Do not hand-edit generated YAML, attach genomes or deposits by the AH4 designation alone, infer N. xinjiangensis equivalence or promote lifecycle to REVIEWED.

Any future verified source correction belongs in maintained extraction/source inputs or `src/taxonmech/seed.py`, with regression coverage and controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature enrichment needs a supported persistent curation mechanism rather than direct YAML edits.

## Follow-up Checks

- Reconcile publication and accession sequence lengths before using that detail in enrichment; do not manufacture a correction.
- Require an explicit deposit-to-marker or deposit-to-genome provenance chain before adding strain links.
- After an authorized upstream/seeder change, validate and inspect a canary, then run `just verify-corpus` and `just qc`; neither gate ran here.
- Reconcile review reports against actual YAML files independently of ignore rules. A report does not confer human REVIEWED status.

## Additional Notes

The 32 numeric substring matches were inspected, not treated as taxon-ID matches:

- E. coli PNUSAE019495/PNUSAE019496: BV-BRC 562.36504/562.36550, SAMN10348763/SAMN10348760, GCA_003759285.1/.2 and GCA_003764045.1/.2. Full objects occur in BV-BRC shard 0023 lines 36360/36400, GenBank historical shard 0000 lines 10500/10540 and current shard 0002 lines 48290/48527. GOLD project row 274436 is Gp0386962/Go0502685 for PNUSAE019495, not a target association.
- M. tuberculosis ERR1034876: BV-BRC shard 0006 line 6339, genome 1773.18525, taxon 1773.
- Comamonas sp. PROT-5: taxon 34028, BV-BRC 34028.125, GCA_048499735.1, SAMN31034876. BV-BRC shard 0019 line 27755, GenBank shard 0044 line 37005 and GTDB shard 0015 line 26392 agree on that context; GTDB calls it Simplicispira sedimenti.
- Campylobacter jejuni PNUSAC013692: taxon 197, GCA_010348765.1, SAMN13353938, GenBank shard 0009 line 6276.
- Streptococcus pneumoniae isolate 412: taxon 1313, GCA_036052215.1, SAMN11116898, assembly name PDT001034876.1, GenBank shard 0033 line 35505.
- Uncultured Clostridia bacterium Reindeer_2_mag_61: taxon 244328, GCA_905235765.1, SAMEA8030383. GenBank shard 0058 line 26536 and GTDB shard 0011 line 26468 match genome length 1,034,876, not target taxonomy; GTDB calls it UBA1259 sp905235765.
- ATB rows 65883, 569346, 1502168/1502169, 1715077-1715085, 1715129, 2464376, 2766307 and 3092403 were read in full. They concern S. dysgalactiae subsp. equisimilis, M. tuberculosis, E. coli, Listeria monocytogenes or S. pneumoniae. Matches occur in sample/run accessions or SeqKit sums. Examples are SAMEA1034876/ERR085030/ERZ3070263; SAMEA3558409/ERR1034876/ERZ3501024; and SAMN44338755/SRR31034876/ERZ27111260. No sample, run, checksum or analysis accession was recast as a taxon or genome-equivalence assertion.

Catalog shards are under `data/catalog/`, BV-BRC shards under `data/bvbrc/`, GOLD rows under `data/gold/`, and ATB rows at `data/catalog/allthebacteria.tsv.xz`. Alias checks inspected complete source objects, not projections alone; cross-source identifier chains above preserve their source context without creating target joins.

Relevant paper text and Figure 3 were inspected, including the cached page-6 rendering of the [open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf). No new PDF or image was written in the repository. Phenotype and antimicrobial claims were not exhaustively curated. Candidate objects were identity leads, not separate taxon reviews. No exhaustive external census or all-alias search is claimed.

Review performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, GitHub item or external source was changed.
