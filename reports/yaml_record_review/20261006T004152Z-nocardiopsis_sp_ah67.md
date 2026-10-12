# YAML Record Review: Nocardiopsis sp. AH67

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_ah67.yaml`
- Started UTC: 2026-10-06T00:40:31Z
- Finished UTC: 2026-10-06T00:41:52Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1034885`, Nocardiopsis sp. AH67, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649073` (unclassified Nocardiopsis). It asserts ten ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, xrefs, literature evidence or causal graph are asserted.

`data/taxa/PATHS.tsv:14204` uniquely resolves this ID and stem; `curation/seed_scope.tsv:322037` supplies inclusion. Only a new review report was written. Records, inputs, scope, history and Eukaryota were untouched.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardiopsis_sp_ah67.yaml`, exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardiopsis_sp_ah67.yaml --out /private/tmp/ah67-validation.tsv`, exit 0, one file, zero errors. The TSV was read and is header-only.
- PASS: complete backbone row, reconstructed lineage, seven inventories, PATHS, scope, attestation and seed-event text agree. The backbone has no target children.
- PASS: exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Authority/reference checks: live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore queries, full target and conflicting-accession metadata/references/features, and relevant primary-paper text/Figure 3.
- Not applicable: graph-term, LPSN/GTDB mapping and iModulonDB checks. No corresponding graph, mapping, gene/regulator or expression-module assertion exists.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, rendered-site drift, README statistics, publication-size and vendored-sync gates. These bounded checks do not prove corpus reproduction or publication readiness.

Required guidance/schema/seeder behavior were fully read in preceding reviews at this HEAD. The review skill, checklist and seed-timestamp implementation were reread this turn, and the three manifests' timestamps were checked. Relevant guidance/schema/seeder and both target diffs were empty. No history entry or human REVIEWED promotion was made.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034885&retmode=xml) confirms ID, exact label, species rank, bacterial division, parent and code 11. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034885) agrees and supplies all ten ancestor IDs, including root.

The root-first chain agrees with the pinned backbone: root (`NO_RANK`), cellular organisms (`CELLULAR_ROOT`), Bacteria (`DOMAIN`), Bacillati (`KINGDOM`), Actinomycetota (`PHYLUM`), Actinomycetes (`CLASS`), Streptosporangiales (`ORDER`), Nocardiopsidaceae (`FAMILY`), Nocardiopsis (`GENUS`), unclassified Nocardiopsis (`NO_RANK`). EFetch supplies non-root ancestry; Datasets includes root explicitly.

This informal name is not a claim of validly published nomenclature. A marker's strain qualifier does not alter the NCBI concept's rank. `EXACT` grounds this taxon, not equivalence to N. litoralis, N. kunsanensis or another organism called AH67.

## Evidence

| Assertion | Inspected support |
|---|---|
| Identity, parent, rank and code | Complete `data/raw/ncbitaxon_taxa.tsv:221734` and both NCBI authorities. |
| Lineage | Full reconstructed backbone chain and authority ancestry. |
| Scientific name without synonyms | `data/catalog/ncbi_names-0005.jsonl.gz:31137`; backbone synonym fields and live alternate names are empty. |
| NCBITAXON NAME count 1 | Source, ID, label, count, unit and snapshot note agree with the backbone; this is not a strain/genome count. |
| Inclusion and event | Scope line 322037 provides 2026-09-13 and the exact one-source attested-rule reason; seed-event text agrees. |
| Seed timestamp | 2026-09-13T17:54:04Z is the maximum of raw 17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z extraction times on that date, following `src/taxonmech/seed.py:139`. |
| Zero strains | No BacDive inventory association under this taxon and no backbone descendants. This source-classification count does not mean AH67 was never cultivated. |

The exact `txid1034885[Organism:noexp]` queries returned zero Assembly items with phrase-not-found/no-items messages and one Nuccore UID, 333497034. Complete [JF777530.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333497034), references and features were read, excluding bases. It is a 1,420-base 16S marker, partial at both ends. Source qualifiers identify AH67, taxon 1034885, Saharan soil, Algeria and collection year 2010, without a culture-collection qualifier.

References name Boudjelal, Zitouni, Mathieu, Lebrihi and Sabaou, an unpublished study and direct submission on 2011-03-07, with no DOI/PMID. These support submitted specimen context, not deposit or genome identity. The exact Assembly query does not establish absence under other classifications or indexing.

[Boudjelal et al., 2023](https://onlinelibrary.wiley.com/doi/10.1155/2023/1061176), DOI 10.1155/2023/1061176, places AH67 with AH0 in cluster IV, reporting 99.7% similarity to N. litoralis and 99.5% to N. kunsanensis. Neither establishes species equivalence. Figure 3 labels AH67 as JF777532, conflicting with NCBI's JF777530; its 1,529-1,544-base range also differs from 1,420. These external discrepancies remain unresolved.

Complete [JF777532.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=JF777532) identifies Botrytis sp. CA3, taxon 1086082, not Nocardiopsis. It is 463 bases spanning partial ITS1, complete 5.8S rRNA and partial ITS2, with blackberry as isolation source and direct submission on 2011-04-04. Its reference section supplies a separate fungal study, DOI 10.3852/11-218 and PMID 22314589; these were read as native reference metadata, not used as target evidence. No Eukaryota record was reviewed or changed.

The fungal accession must not be attached to AH67. The external figure/sequence-length issues do not invalidate any current YAML assertion because no accession, sequence length or paper-specific identification is asserted.

## Completeness

Exact inventory lookups found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin or BactoTraits association under taxon 1034885. Empty optional slots agree with the inputs; optional literature evidence is not mandatory for a seeded record.

Bounded searches included ignored/hidden files and compressed native catalogs:

- `rg --no-ignore --hidden -n -z -i` searched ID, full-label variants and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding SOURCE.json manifests. All 18 matches were read fully: three target backbone/name/scope rows and fifteen numeric substring matches.
- AH67/AH-67/AH 67/AH_67 returned 12 rows: three target, three other-NCBI-concept and six genome rows. All were read fully as native JSON or header-aware TSV, with address reconciliation. No BacDive inventory/native or StrainInfo row matched this alias screen.
- JF777530/JF777532 returned no local matches across those ten roots, including ignored files. This is not a global external absence claim.
- An ignored-inclusive ID/full-label/slug search of reports/history found AH67 as conflicting-accession context in the AH65 report, not a prior target review. `find` found no prior exact-stem AH67 report.

The same-designation genome objects concern Aeromonas, Klebsiella and Helicobacter; none establishes a target strain-to-genome relationship. No consequential missing required representation was found within these bounds. No exhaustive culture/genome census or all-alias search is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's assertions. Identity, lineage, provenance and source-classification count are supported. The external figure links to an unrelated fungal marker and has an unresolved sequence-length discrepancy; those conflicts must constrain future enrichment.

## Recommended Edits

None required on current evidence. Do not hand-edit generated YAML, transfer another AH67's genomes, attach JF777532, infer species equivalence from similarity percentages or promote lifecycle to REVIEWED.

Resolve external accession/length conflicts before optional enrichment. A verified source/link correction belongs in maintained source/extraction inputs or `src/taxonmech/seed.py`, with regression coverage and controlled regeneration. `curation/seed_scope.tsv` owns inclusion, not identity. Optional literature curation requires a persistent supported mechanism rather than direct generated-YAML edits.

## Follow-up Checks

- Obtain authoritative clarification of the figure accession and sequence-length discrepancy before reusing those details. No author/depositor contact was made.
- Require explicit target/deposit/sequence provenance for future links; retain accession versions, taxonomic scope and entity types.
- After an authorized upstream change, inspect and validate a canary, then run `just verify-corpus` and `just qc`; neither gate ran here.
- Reconcile reports against actual YAML files independently of ignore rules. A report does not confer human REVIEWED status.

## Additional Notes

All same-designation objects were inspected and kept separate:

- Burkholderia sp. AH67, taxon 861705: scope line 285677, backbone line 181214, names shard 0004 line 34898, parent 2613784.
- Aeromonas veronii AH67, taxon 654: GCA/GCF_050875195.1, SAMN48819329, BV-BRC 654.1979 and GTDB RS_GCF_050875195.1. Full rows: BV-BRC shard 0026 line 11240; GenBank 0046 line 48682; RefSeq 0007 line 31670; GTDB 0015 line 14246.
- K. pneumoniae AH67, taxon 573: GCA_039677585.1, SAMN41160374, GenBank shard 0036 line 11962.
- H. pylori AH67, taxon 210: GCA_054764255.1, SAMD00751842, GenBank shard 0050 line 29723.

All fifteen numeric substring matches were also read in full:

- M. tuberculosis ERR1034885, taxon 1773: BV-BRC shard 0006 line 6349, genome 1773.18534.
- K. pneumoniae zj02087, taxon 573: GCA_041034885.1, SAMN37542655, GenBank 0037 line 25632.
- Paracoccaceae bacterium PROT-3, taxon 1904441: GCA_048499575.1, SAMN31034885, GenBank 0044 line 36997 and GTDB 0005 line 19950; GTDB calls it JAHDXW01 sp023383015.
- V. parahaemolyticus VP20074, taxon 670: GCA_051034885.1, SAMN46338808, GenBank 0047 line 6704; historical GCF_051034885.1 in RefSeq historical shard 0001 line 38974 is marked suppressed. Current GenBank and historical RefSeq status were kept distinct.
- E. hormaechei IW555-2, taxon 158836: GCA_021034885.1, SAMEA8581494, GenBank 0019 line 18977.
- ATB row 65892: S. dysgalactiae subsp. equisimilis/SAMEA1034885/ERR084995/ERZ3070275, with SYLPH_RESULTS_FAIL and unknown sylph species; row 569355: M. tuberculosis/SAMEA3558418/ERR1034885/ERZ3501063. These values are not target taxon identifiers.
- ATB rows 140973-140978 respectively supply Shigella sonnei samples SAMEA110348854 through SAMEA110348859, runs ERR9940540 through ERR9940545, and analyses ERZ25116977, ERZ25116986, ERZ25116999, ERZ25117007, ERZ25117016 and ERZ25117024. Their sylph classification is E. coli. Neither numeric substrings nor this non-target classification difference establish target identity.

Catalog shards are under `data/catalog/`, BV-BRC shards under `data/bvbrc/`, and ATB rows in `data/catalog/allthebacteria.tsv.xz`. Candidate objects and the fungal marker were identity checks, not separate record reviews.

Relevant primary-paper text and Figure 3 were inspected this turn, including the cached page-6 rendering of the [open-access PDF](https://pdfs.semanticscholar.org/39ee/83aa10b4046d60074edb22b2c144950e2f20.pdf). No new PDF/image was written in the repository; phenotype and antimicrobial claims were not exhaustively curated.

Review performed on `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, history, scope, lifecycle, GitHub item or external source was changed.
