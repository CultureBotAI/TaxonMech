# Record review: Archaeoglobus fulgidus

- Review: 20261021T075227Z-archaeoglobus_fulgidus
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-20T07:29:35Z
- Finished UTC: 2026-10-21T07:52:27Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Archaeoglobus fulgidus has supported exact NCBI identity and source-scoped representation. No record-specific import defect was established. The explicit StrainInfo AY354034 deposit link retains conflicting Methanococcus sequence metadata. Historical aggregate counts remain inventory-verified without an independent original-edge recount.

## Scope And Provenance

Entire single generated record, including all source assertions and imported strains.

Selection: Original unreviewed path-order position 134; batch-0014 target 4. Excluded 185 actual targets from validated freshmain and thirteen committed isolated branches; full corpus enumeration includes ignored files.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 01ca63effdf8c03a644df893ba6129b2d8448ea4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:2234 | data/taxa/archaea/archaeoglobus_fulgidus.yaml | generated | Archaeoglobus fulgidus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact NCBI taxon, rank and lineage | passed | True | NCBITaxon:2234 | NCBITaxon:2234 denotes Archaeoglobus fulgidus at SPECIES rank beneath NCBITaxon:2233, genetic code 11. All 9 carried ancestors agree with the pinned inventory and captured official NCBI response; the response omits only the root entry. Source name classes remain distinct from taxon classification. |
| Complete exact identifier and name inventory search | passed | True | NCBITaxon:2234 | Complete direct reads of twelve source/scope/path tables, including ignored files, support 3 imported BacDive strains over the exact target subtree (2 descendant taxa). All imported counts agree with their own source units: NCBITAXON 1 NAME; LPSN 1 NAME; GTDB 6 GENOME; BACDIVE 3 STRAIN; MEDIADIVE 1 MEDIUM; GOLD 4 ORGANISM; MADIN 6 TRAIT_ASSERTION. Counts of organisms, media, traits and genome assertions are not interchangeable and do not prove phenotype or biological genome equivalence. The GTDB fulgidus cluster count 6 spans four NCBI taxids; it is not the number of this target's own strain genomes. |
| Complete primary GTDB cluster membership | passed | True | NCBITaxon:2234 | All selected source counts agree; the separate notes/scope findings are retained where applicable. |
| All imported strain link assertions match pinned inventories | passed | True | NCBITaxon:2234 | kgmicrobe.strain:bacdive_18096: 9 genome_assemblies assertions (3 distinct IDs), 6 genome_records assertions (3 distinct IDs), 51 related_records assertions (27 distinct IDs). kgmicrobe.strain:bacdive_18095: 0 genome_assemblies assertions (0 distinct IDs), 0 genome_records assertions (0 distinct IDs), 2 related_records assertions (2 distinct IDs). kgmicrobe.strain:bacdive_132693: 10 genome_assemblies assertions (3 distinct IDs), 8 genome_records assertions (4 distinct IDs), 22 related_records assertions (8 distinct IDs). Every compared native assertion matches a retained inventory row with no missing or extra assertion. |
| Primary own-deposit and genome evidence | passed | True | NCBITaxon:2234 | BacDive 18096 identifies VC-16 with DSM 4304, ATCC 49558, JCM 9628 and NBRC 100126. Its primary taxonomy separates species 2234 and strain 224325. StrainInfo SI-ID46110 version 3 carries four corresponding eligible, available, non-deprecated, non-erroneous deposits (125019, 125018, 158734 and 339249). ATCC 49203/SI-DP125020 is present in that source group but is absent from the local BacDive deposit list and is not imported. All five source sequences explicitly name DSM 4304/SI-DP125019; only GCA_000008665 is a genome, while AY354034, U66886, AJ575815 and X17237 remain nucleotide references. GTDB row RS_GCF_000008665.1 names whole DSM 4304 and explicitly carries GCA_000008665.1. Primary NCBI GenBank and RefSeq rows corroborate DSM 4304/224325 and explicitly pair their .1 versions as identical in the pinned snapshot; these do not assign a version to the separately unversioned BacDive, GOLD and StrainInfo assertion. BV-BRC 224325.10 explicitly resolves to DSM 4304 and GCA_000008665.1. GOLD Go0000778 joins Gp0000778 to Ga0027554 and supplies unversioned GCA_000008665 plus IMG638154502 through the inspected culture match. Three transcriptome projects under Go0015557 correctly provide typed sample/project context rather than genome links. Additional GOLD organism rows Go0620787 and Go0620788 match NBRC and JCM deposits without transferring DSM-only sequences. The species record additionally retains distinct DSM 4139 strain Z/BacDive18095, with SI-ID47796.2/SI-DP158661 and no imported genomes, and DSM 8774 strain 7324/BacDive132693. All three are source-supported BacDive strains; two classified_as fields retain their descendant NCBI strain taxa rather than flattening strain identity into the species. |
| Current source accession and DOI resolution | passed | True | NCBITaxon:2234 | All 3 exact nested StrainInfo DOI version(s) resolve in DataCite with the correct SI-ID and version. All 6 asserted BioProject IDs and 5 BioSample IDs resolve at NCBI. Each BioSample explicitly retains the expected strain/taxon and primary BioProject link. PRJNA224116 resolves as the multispecies RefSeq annotation umbrella, preserving the qualified project-context interpretation. AJ575815, U66886 and X17237 independently resolve to Archaeoglobus fulgidus DSM 4304 (taxon224325); returned .1 versions do not alter their native unversioned source accessions. AY354034 remains a distinct unresolved source conflict. |
| Current name, publication and sequence authorities | passed | True | NCBITaxon:2234 | Pinned LPSN row 15381, lpsn:773360, and current LPSN support Archaeoglobus fulgidus Stetter 1988, validly published ICNP correct name, and ATCC 49558 / DSM 4304 / JCM 9628 / NBRC 100126 type deposits. Current NCBI preserves authority as a related name. DOI 10.1016/s0723-2020(88)80032-8 resolves to Stetter 1988 effective publication; DOI 10.1099/00207713-38-3-328 is Validation List 26. X05567.1 is the 16S RNA sequence of VC-16 / DSM 4304, taxid 224325. LPSN bridges the species to GTDB Archaeoglobus fulgidus. These nomenclatural checks do not assess every nested strain link. |
| Structured iModulonDB adapter runner | unavailable | False | NCBITaxon:2234 | Runner could not be invoked in the bounded checked locations; inspected official source fallback retained. |
| iModulonDB covered organism/dataset | not_applicable | False | NCBITaxon:2234 | No matching published organism/dataset in the inspected public index, so no gene search or component summary is applicable; metadata titles remain typed related records. |
| Original manifest-pinned aggregate recounts | unavailable | True | NCBITaxon:2234 | Pinned projection counts agree: [{"source":"MEDIADIVE","count":1,"unit":"MEDIUM","raw_projection_agrees":true,"historical_primary_aggregate_checked":false},{"source":"GOLD","count":4,"unit":"ORGANISM","raw_projection_agrees":true,"historical_primary_aggregate_checked":false},{"source":"MADIN","count":6,"unit":"TRAIT_ASSERTION","raw_projection_agrees":true,"historical_primary_aggregate_checked":false}]. Original aggregate edges were not independently recounted. |
| Native strict record validation | passed | True | NCBITaxon:2234 | Actual terminal exit code 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. |
| Repository history validation | passed | True | NCBITaxon:2234 | Actual terminal exit code 0. All 18 standalone history records; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. |
| Full-corpus exact reproduction | passed | True | NCBITaxon:2234 | Actual terminal exit code 0. All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. |
| Native product ID/label gate | passed | True | NCBITaxon:2234 | Actual terminal exit code 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. |
| Authoritative complete quality gate | passed | True | NCBITaxon:2234 | Actual terminal exit code 0. Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. 1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33) |

## Scientific And Domain Assessments

### Primary strain, deposit and accession assertions

evidence: supported. Targets: NCBITaxon:2234.

BacDive 18096 identifies VC-16 with DSM 4304, ATCC 49558, JCM 9628 and NBRC 100126. Its primary taxonomy separates species 2234 and strain 224325. StrainInfo SI-ID46110 version 3 carries four corresponding eligible, available, non-deprecated, non-erroneous deposits (125019, 125018, 158734 and 339249). ATCC 49203/SI-DP125020 is present in that source group but is absent from the local BacDive deposit list and is not imported. All five source sequences explicitly name DSM 4304/SI-DP125019; only GCA_000008665 is a genome, while AY354034, U66886, AJ575815 and X17237 remain nucleotide references. GTDB row RS_GCF_000008665.1 names whole DSM 4304 and explicitly carries GCA_000008665.1. Primary NCBI GenBank and RefSeq rows corroborate DSM 4304/224325 and explicitly pair their .1 versions as identical in the pinned snapshot; these do not assign a version to the separately unversioned BacDive, GOLD and StrainInfo assertion. BV-BRC 224325.10 explicitly resolves to DSM 4304 and GCA_000008665.1. GOLD Go0000778 joins Gp0000778 to Ga0027554 and supplies unversioned GCA_000008665 plus IMG638154502 through the inspected culture match. Three transcriptome projects under Go0015557 correctly provide typed sample/project context rather than genome links. Additional GOLD organism rows Go0620787 and Go0620788 match NBRC and JCM deposits without transferring DSM-only sequences. The species record additionally retains distinct DSM 4139 strain Z/BacDive18095, with SI-ID47796.2/SI-DP158661 and no imported genomes, and DSM 8774 strain 7324/BacDive132693. All three are source-supported BacDive strains; two classified_as fields retain their descendant NCBI strain taxa rather than flattening strain identity into the species. kgmicrobe.strain:bacdive_18096: 9 genome_assemblies assertions (3 distinct IDs), 6 genome_records assertions (3 distinct IDs), 51 related_records assertions (27 distinct IDs). kgmicrobe.strain:bacdive_18095: 0 genome_assemblies assertions (0 distinct IDs), 0 genome_records assertions (0 distinct IDs), 2 related_records assertions (2 distinct IDs). kgmicrobe.strain:bacdive_132693: 10 genome_assemblies assertions (3 distinct IDs), 8 genome_records assertions (4 distinct IDs), 22 related_records assertions (8 distinct IDs).

### Source disagreement on AY354034

evidence: concern. Targets: NCBITaxon:2234.

AY354034 is explicitly attached to DSM 4304/SI-DP125019 in StrainInfo, but its source description and captured current NCBI esummary identify Methanococcus aeolicus (NCBITaxon:42879), not Archaeoglobus fulgidus. The imported source description and typed nucleotide reference faithfully preserve that disagreement under docs/STRAININFO.md; this is not established as an extractor or seeder defect. Keep a qualified limitation and seek authoritative StrainInfo/INSDC reconciliation before treating AY354034 as biological evidence about the Archaeoglobus strain.

### Bounded current accession, sample/project and DOI identities

evidence: supported. Targets: NCBITaxon:2234.

All 3 exact nested StrainInfo DOI version(s) resolve in DataCite with the correct SI-ID and version. All 6 asserted BioProject IDs and 5 BioSample IDs resolve at NCBI. Each BioSample explicitly retains the expected strain/taxon and primary BioProject link. PRJNA224116 resolves as the multispecies RefSeq annotation umbrella, preserving the qualified project-context interpretation. AJ575815, U66886 and X17237 independently resolve to Archaeoglobus fulgidus DSM 4304 (taxon224325); returned .1 versions do not alter their native unversioned source accessions. AY354034 remains a distinct unresolved source conflict.

### Exact taxon and source lineage

identity: supported. Targets: NCBITaxon:2234.

NCBITaxon:2234 denotes Archaeoglobus fulgidus at SPECIES rank beneath NCBITaxon:2233, genetic code 11. All 9 carried ancestors agree with the pinned inventory and captured official NCBI response; the response omits only the root entry. Source name classes remain distinct from taxon classification.

### Name classes and nomenclatural scope

nomenclature: supported. Targets: NCBITaxon:2234.

Pinned LPSN row 15381, lpsn:773360, and current LPSN support Archaeoglobus fulgidus Stetter 1988, validly published ICNP correct name, and ATCC 49558 / DSM 4304 / JCM 9628 / NBRC 100126 type deposits. Current NCBI preserves authority as a related name. DOI 10.1016/s0723-2020(88)80032-8 resolves to Stetter 1988 effective publication; DOI 10.1099/00207713-38-3-328 is Validation List 26. X05567.1 is the 16S RNA sequence of VC-16 / DSM 4304, taxid 224325. LPSN bridges the species to GTDB Archaeoglobus fulgidus. These nomenclatural checks do not assess every nested strain link.

### Imported subtree and source assertion units

completeness: supported. Targets: NCBITaxon:2234.

Complete direct reads of twelve source/scope/path tables, including ignored files, support 3 imported BacDive strains over the exact target subtree (2 descendant taxa). All imported counts agree with their own source units: NCBITAXON 1 NAME; LPSN 1 NAME; GTDB 6 GENOME; BACDIVE 3 STRAIN; MEDIADIVE 1 MEDIUM; GOLD 4 ORGANISM; MADIN 6 TRAIT_ASSERTION. Counts of organisms, media, traits and genome assertions are not interchangeable and do not prove phenotype or biological genome equivalence. The GTDB fulgidus cluster count 6 spans four NCBI taxids; it is not the number of this target's own strain genomes.

### Qualified species mapping and target scope

grounding: supported. Targets: NCBITaxon:2234.

Pinned LPSN row 15381, lpsn:773360, and current LPSN support Archaeoglobus fulgidus Stetter 1988, validly published ICNP correct name, and ATCC 49558 / DSM 4304 / JCM 9628 / NBRC 100126 type deposits. Current NCBI preserves authority as a related name. DOI 10.1016/s0723-2020(88)80032-8 resolves to Stetter 1988 effective publication; DOI 10.1099/00207713-38-3-328 is Validation List 26. X05567.1 is the 16S RNA sequence of VC-16 / DSM 4304, taxid 224325. LPSN bridges the species to GTDB Archaeoglobus fulgidus. These nomenclatural checks do not assess every nested strain link.

### Unchanged native status and history

provenance: supported. Targets: NCBITaxon:2234.

EXACT grounding and SEEDED status agree with NCBI identity. The sole seed event at 2026-09-13T17:54:04Z equals the latest raw/ATB/StrainInfo extraction time; no native status/history was changed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### resolve-source-ay354034-conflict

Reconcile the conflicting organism annotation for AY354034 through authoritative StrainInfo SI-ID46110/SI-DP125019 and INSDC evidence. Retain the source-association conflict until an authoritative correction or explicit source policy supports a change; do not hand-edit generated taxon YAML.

- Inspect the authoritative strain/deposit sequence path and INSDC accession annotation; distinguish taxonomy disagreement from exact deposit-link fidelity.
- If an upstream record changes, capture a dated/hash-pinned source refresh and use separately authorized normal extraction and guarded seeding.
- Preserve supplied accession versions and related-record typing; rerun native and structured review gates after any authorized update.

### recover-pinned-aggregate-inputs

Recover manifest-hash-matching original aggregate inputs and independently recount the exact target assertions through the maintained extractor; do not edit generated YAML.

- Require exact original input SHA-256 before using it as historical evidence.
- Recount only the exact target with each source's own assertion unit and compare to its pinned inventory row.
- Record any discrepancy in a new review observation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/taxa/archaea/archaeoglobus_fulgidus.yaml; entire TaxonRecord; identifier=NCBITaxon:2234 | supports | Read the entire generated YAML, including identity, lineage, names, mappings, source attestations, all imported strains and links, and seed history. |
| taxonomy-inventory | data/raw/ncbitaxon_taxa.tsv; line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""}; line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"}; line 1755: {"taxon_id":"NCBITaxon:2231","label":"Archaeoglobales","rank":"ORDER","parent_id":"NCBITaxon:183980"}; line 1756: {"taxon_id":"NCBITaxon:2232","label":"Archaeoglobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2231"}; line 1757: {"taxon_id":"NCBITaxon:2233","label":"Archaeoglobus","rank":"GENUS","parent_id":"NCBITaxon:2232"}; line 1758: {"taxon_id":"NCBITaxon:2234","label":"Archaeoglobus fulgidus","rank":"SPECIES","parent_id":"NCBITaxon:2233","genetic_code":"11","exact_synonyms":"","related_synonyms":"Archaeoglobus fulgidus Stetter 1988","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb&#124;bacdive&#124;lpsn&#124;mediadive&#124;gold&#124;madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"}; line 2981: {"taxon_id":"NCBITaxon:28890","label":"Methanobacteriota","rank":"PHYLUM","parent_id":"NCBITaxon:3366610"}; line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"}; line 36620: {"taxon_id":"NCBITaxon:183980","label":"Archaeoglobi","rank":"CLASS","parent_id":"NCBITaxon:28890"}; line 621140: {"taxon_id":"NCBITaxon:3366610","label":"Methanobacteriati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"} | supports | Inspected the target and each carried ancestor, rank, parent, genetic code and source name classes. |
| scope-row | curation/seed_scope.tsv; line 5581: {"identifier":"NCBITaxon:2234","added":"2026-09-12","reason":"attested rule: Archaeoglobus fulgidus, 7 sources incl. NCBI"} | supports | Exact target is included in the declared seed scope. |
| path-row | data/taxa/PATHS.tsv; line 334390: {"identifier":"NCBITaxon:2234","slug":"archaeoglobus_fulgidus"} | supports | Indexed path resolves to this exact NCBI taxon. |
| ncbi-live | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=2012529,2250530,1935016,2234,224325,1344584,403219,1121009,138903,2798580; TaxaSet/Taxon[TaxId='2234']; ten-target captured response | supports | Inspected the official response for this exact taxon: scientific name, rank, parent, source name classes, lineage and genetic code. Current authority and pinned September inventory remain distinct observations. |
| lpsn-inventory | data/raw/lpsn_names.tsv; line 15381: {"lpsn_id":"lpsn:773360","name":"Archaeoglobus fulgidus","rank":"SPECIES","authority":"Stetter 1988","url":"https://lpsn.dsmz.de/species/archaeoglobus-fulgidus","deprecated":"0","status":"legitimate=True; validly published under the ICNP; correct name","validly_published":"1","legitimate":"1","is_correct_name":"1","parent_lpsn_id":"lpsn:516970","ncbitaxon_ids":"NCBITaxon:2234","gtdb_ids":"GTDB:s__Archaeoglobus_fulgidus","type_strain_ids":"kgmicrobe.strain:ATCC-49558&#124;kgmicrobe.strain:DSM-4304&#124;kgmicrobe.strain:JCM-9628&#124;kgmicrobe.strain:NBRC-100126","synonym_of":"","synonyms":"","publications":"doi:10.1016/s0723-2020(88)80032-8&#124;doi:10.1099/00207713-38-3-328","sequence_accessions":"INSDC:X05567"} | supports | Inspected exact mapped and linked LPSN names; bounded inventory absence does not establish worldwide nomenclatural absence. |
| gtdb-mappings | data/raw/gtdb_mappings.tsv; line 20129: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1344584","predicate":"skos:closeMatch","genome_count":"6"}; line 72202: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"6"}; line 177020: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:2234","predicate":"skos:closeMatch","genome_count":"6"}; line 177993: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:224325","predicate":"skos:closeMatch","genome_count":"6"} | supports | Inspected direct mappings and selected clusters' reverse mappings, retaining each source predicate and taxon boundary. |
| gtdb-species | data/raw/gtdb_species.tsv; line 12308: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","label":"s__Archaeoglobus_fulgidus","parent":"GTDB:g__Archaeoglobus","genome_count":"6"} | supports | Inspected source species identifiers, labels, parent clusters and genome counts. |
| bacdive-inventory | data/raw/bacdive_strains.tsv; line 17904: {"strain_id":"kgmicrobe.strain:bacdive_18095","bacdive_id":"18095","designation":"Z","taxon_ids":"NCBITaxon:2234","lpsn_ids":"lpsn:773360","culture_collection_ids":"kgmicrobe.strain:DSM-4139","medium_count":"0"}; line 17905: {"strain_id":"kgmicrobe.strain:bacdive_18096","bacdive_id":"18096","designation":"VC-16","taxon_ids":"NCBITaxon:224325","lpsn_ids":"lpsn:773360","culture_collection_ids":"kgmicrobe.strain:ATCC-49558&#124;kgmicrobe.strain:DSM-4304&#124;kgmicrobe.strain:JCM-9628&#124;kgmicrobe.strain:NBRC-100126","medium_count":"0"}; line 55004: {"strain_id":"kgmicrobe.strain:bacdive_132693","bacdive_id":"132693","designation":"7324","taxon_ids":"NCBITaxon:1344584","lpsn_ids":"lpsn:773360","culture_collection_ids":"kgmicrobe.strain:DSM-8774","medium_count":"0"} | supports | Complete inventory selection covers the exact target and descendants from the complete NCBI parent graph; its imported strain population was compared with the complete YAML. |
| culture-inventory | data/raw/culture_collection_strains.tsv; line 78450: {"strain_id":"kgmicrobe.strain:DSM-4139","taxon_ids":"NCBITaxon:2234"} | supports | Inspected exact culture-inventory associations; an isolate name or genome does not create an inferred deposit. |
| gold-organisms | data/raw/gold_organisms.tsv; line 21140: {"taxon_id":"NCBITaxon:2234","organism_count":"4"} | supports | Inspected the exact GOLD organism count row or bounded absence, without converting counts to phenotypes. |
| mediadive-taxa | data/raw/mediadive_taxa.tsv; line 6868: {"taxon_id":"NCBITaxon:2234","medium_count":"1","media_ids":"mediadive.medium:399"} | supports | Inspected the exact MediaDive medium count row or bounded absence, without converting counts to phenotypes. |
| madin-taxa | data/raw/madin_taxa.tsv; line 19569: {"taxon_id":"NCBITaxon:2234","assertion_count":"6"} | supports | Inspected the exact Madin trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| bactotraits-taxa | data/raw/bactotraits_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact BactoTraits trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| mapping-policy | docs/HARMONIZATION.md; Mapping predicates; Which strains belong to a record | supports | Policy permits one-to-one species closeMatch normalization and LPSN-linked species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage unchanged. |
| equivalence-contract | src/taxonmech/schema/taxonmech.yaml; TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439 | supports | TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes under the source taxon. |
| seed-owner | src/taxonmech/seed.py; GTDB mapping construction lines 444–476; LPSN/type-strain and source-attestation construction | supports | Inspected mapping ranking, qualified predicates, fixed broadMatch wording, synonym/xref construction, primary cluster counts and same-taxon type-strain derivation. |
| manifest | data/raw/MANIFEST.yaml; kg_microbe_source, inputs, extracted_at | supports | Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd, upstream input hashes and extraction time 2026-09-13T17:50:44Z. |
| overlay-manifests | data/atb/MANIFEST.yaml; extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml | supports | Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z, matching the sole seed event. StrainInfo manifest is independently captured in source.inputs. |
| genome-catalog-1 | data/catalog/gtdb_genomes-0017.jsonl.gz; line 30338: {"accession":"RS_GCF_900069765.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM90006976v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMEA3879005","ncbi_contig_count":"206","ncbi_contig_n50":"67601","ncbi_country":"none","ncbi_date":"2016-09-20","ncbi_genbank_assembly_accession":"GCA_900069765.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"Archaeoglobus_fulgidus_oil","ncbi_isolation_source":"formation liquid","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus fulgidus","ncbi_protein_count":"2335","ncbi_refseq_category":"na","ncbi_rrna_count":"4","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2016-09-20","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2234","ncbi_ssu_count":"2","ncbi_strain_identifiers":"Archaeoglobus_fulgidus_oil","ncbi_submitter":"NTNU","ncbi_taxid":"2234","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_total_gap_length":"0","ncbi_total_length":"2036821","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2036821","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"FJNF00000000.1"}; line 30980: {"accession":"GB_GCA_001508745.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM150874v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA278302","ncbi_biosample":"SAMN03445115","ncbi_contig_count":"99","ncbi_contig_n50":"34454","ncbi_country":"none","ncbi_date":"2016-01-08","ncbi_genbank_assembly_accession":"GCA_001508745.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"49_95","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus fulgidus","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"0","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2016-01-08","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2234","ncbi_ssu_count":"0","ncbi_strain_identifiers":"49_95","ncbi_submitter":"Lawrence Berkeley National Lab","ncbi_taxid":"2234","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_total_gap_length":"0","ncbi_total_length":"2037571","ncbi_translation_table":"11","ncbi_trna_count":"0","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2037571","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"LGEQ00000000.1"}; line 45270: {"accession":"RS_GCF_029982885.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2998288v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN33401081","ncbi_contig_count":"121","ncbi_contig_n50":"21098","ncbi_country":"USA: Colorado","ncbi_date":"2023-05-11","ncbi_genbank_assembly_accession":"GCA_029982885.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"DJKA110_ANT-KO_bin.46","ncbi_isolation_source":"Produced fluids from hydraulically fractured shales","ncbi_lat_lon":"40.411582 N 104.348363 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"2","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-05-11","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1872626","ncbi_ssu_count":"0","ncbi_strain_identifiers":"DJKA110_ANT-KO_bin.46","ncbi_submitter":"The Ohio State University","ncbi_taxid":"1872626","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__unclassified Archaeoglobus;s__Archaeoglobus sp.","ncbi_total_gap_length":"0","ncbi_total_length":"1934538","ncbi_translation_table":"11","ncbi_trna_count":"44","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1934538","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JARRCC000000000.1"}; line 47261: {"accession":"GB_GCA_001508815.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM150881v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA278302","ncbi_biosample":"SAMN03445123","ncbi_contig_count":"153","ncbi_contig_n50":"19697","ncbi_country":"USA:Alaska; North Slope; Kuparuk formation","ncbi_date":"2016-01-08","ncbi_genbank_assembly_accession":"GCA_001508815.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"49_2300","ncbi_isolation_source":"oil reservoir sample K2","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus fulgidus","ncbi_protein_count":"2489","ncbi_refseq_category":"na","ncbi_rrna_count":"0","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2016-01-08","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2234","ncbi_ssu_count":"0","ncbi_strain_identifiers":"49_2300","ncbi_submitter":"Lawrence Berkeley National Lab","ncbi_taxid":"2234","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_total_gap_length":"0","ncbi_total_length":"2017823","ncbi_translation_table":"11","ncbi_trna_count":"0","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2017823","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"LGEX00000000.1"}; line 47600: {"accession":"RS_GCF_000734035.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Complete Genome","ncbi_assembly_name":"ASM73403v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN03081472","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"Norway","ncbi_date":"2014-07-28","ncbi_genbank_assembly_accession":"GCA_000734035.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"marine oilfield; North sea","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus fulgidus DSM 8774","ncbi_protein_count":"2565","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"2316287","ncbi_scaffold_n75":"2316287","ncbi_scaffold_n90":"2316287","ncbi_seq_rel_date":"2014-07-28","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2234","ncbi_ssu_count":"1","ncbi_strain_identifiers":"DSM 8774","ncbi_submitter":"University Bergen","ncbi_taxid":"1344584","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus;x__Archaeoglobus fulgidus DSM 8774","ncbi_total_gap_length":"0","ncbi_total_length":"2316287","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2316287","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"}; line 48903: {"accession":"RS_GCF_000008665.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","gtdb_type_species_of_genus":"t","ncbi_assembly_level":"Complete Genome","ncbi_assembly_name":"ASM866v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN02603985","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"none","ncbi_date":"2000-12-01","ncbi_genbank_assembly_accession":"GCA_000008665.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus fulgidus DSM 4304","ncbi_protein_count":"2431","ncbi_refseq_category":"reference genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"2178400","ncbi_scaffold_n75":"2178400","ncbi_scaffold_n90":"2178400","ncbi_seq_rel_date":"2000-12-01","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2234","ncbi_ssu_count":"1","ncbi_strain_identifiers":"DSM 4304","ncbi_submitter":"TIGR","ncbi_taxid":"224325","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus;x__Archaeoglobus fulgidus DSM 4304","ncbi_total_gap_length":"0","ncbi_total_length":"2178400","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"assembly from type material","ncbi_ungapped_length":"2178400","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"} | supports | Inspected every selected GTDB cluster member, exact taxid/species-taxid, culture identifiers and accession versions. Species membership alone is not a strain identity. |
| gtdb-full-scan | data/catalog/MANIFEST.json; {"target":"NCBITaxon:2234","rank":"SPECIES","mappings":[{"source_id":"GTDB:s__Archaeoglobus_fulgidus","predicate":"skos:closeMatch","genome_count":6,"ncbi_taxids":{"2234":3,"1872626":1,"1344584":1,"224325":1},"ncbi_species_taxids":{"2234":5,"1872626":1},"members":[{"accession":"RS_GCF_900069765.1","ncbi_taxid":"2234","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus fulgidus","ncbi_strain_identifiers":"Archaeoglobus_fulgidus_oil","ncbi_genbank_assembly_accession":"GCA_900069765.1"},{"accession":"GB_GCA_001508745.1","ncbi_taxid":"2234","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus fulgidus","ncbi_strain_identifiers":"49_95","ncbi_genbank_assembly_accession":"GCA_001508745.1"},{"accession":"RS_GCF_029982885.1","ncbi_taxid":"1872626","ncbi_species_taxid":"1872626","ncbi_organism_name":"Archaeoglobus sp.","ncbi_strain_identifiers":"DJKA110_ANT-KO_bin.46","ncbi_genbank_assembly_accession":"GCA_029982885.1"},{"accession":"GB_GCA_001508815.1","ncbi_taxid":"2234","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus fulgidus","ncbi_strain_identifiers":"49_2300","ncbi_genbank_assembly_accession":"GCA_001508815.1"},{"accession":"RS_GCF_000734035.1","ncbi_taxid":"1344584","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus fulgidus DSM 8774","ncbi_strain_identifiers":"DSM 8774","ncbi_genbank_assembly_accession":"GCA_000734035.1"},{"accession":"RS_GCF_000008665.1","ncbi_taxid":"224325","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus fulgidus DSM 4304","ncbi_strain_identifiers":"DSM 4304","ncbi_genbank_assembly_accession":"GCA_000008665.1"}]}]} | supports | All nineteen GTDB shards were searched with exact terminal species tokens preserving internal genus suffix underscores. Source cluster counts and taxon distributions were assessed independently of exact-identity promotion. |
| strain-primary-bacdive | data/bacdive/records.jsonl.gz; line 17903; line 17904; line 55003 | supports | Inspected exact asserted source records and their original strain, deposit, taxon, sequence and organism/project/analysis fields. These rows support source assertions at their own scope. |
| strain-primary-straininfo | data/straininfo/records.jsonl.gz; line 34115; line 35705; line 36421 | supports | Inspected exact asserted source records and their original strain, deposit, taxon, sequence and organism/project/analysis fields. These rows support source assertions at their own scope. |
| strain-primary-gold-organisms | data/gold/organisms.jsonl.gz; line 737; line 13388; line 57651; line 451419; line 451420 | supports | Inspected exact asserted source records and their original strain, deposit, taxon, sequence and organism/project/analysis fields. These rows support source assertions at their own scope. |
| strain-primary-gold-projects | data/gold/projects.jsonl.gz; line 755; line 58778; line 59171; line 150647; line 150648 | supports | Inspected exact asserted source records and their original strain, deposit, taxon, sequence and organism/project/analysis fields. These rows support source assertions at their own scope. |
| strain-primary-gold-analyses | data/gold/analyses.jsonl.gz; line 18031; line 36927 | supports | Inspected exact asserted source records and their original strain, deposit, taxon, sequence and organism/project/analysis fields. These rows support source assertions at their own scope. |
| strain-gtdb-primary-1 | data/catalog/gtdb_genomes-0017.jsonl.gz; line 30338; line 30980; line 45270; line 47261; line 47600; line 48903 | supports | Inspected primary source accessions, source taxon/strain identifiers, supplied versions and explicit assembly pairings where present. Taxon and assembly identity are distinct; matching labels alone do not establish a strain join. |
| strain-assembly-primary-1 | data/catalog/ncbi_genbank-0000.jsonl.gz; line 110; line 27228 | supports | Inspected primary source accessions, source taxon/strain identifiers, supplied versions and explicit assembly pairings where present. Taxon and assembly identity are distinct; matching labels alone do not establish a strain join. |
| strain-assembly-primary-2 | data/catalog/ncbi_refseq-0000.jsonl.gz; line 103; line 23649 | supports | Inspected primary source accessions, source taxon/strain identifiers, supplied versions and explicit assembly pairings where present. Taxon and assembly identity are distinct; matching labels alone do not establish a strain join. |
| strain-assembly-primary-3 | data/bvbrc/bvbrc-0002.jsonl.gz; line 22662 | supports | Inspected primary source accessions, source taxon/strain identifiers, supplied versions and explicit assembly pairings where present. Taxon and assembly identity are distinct; matching labels alone do not establish a strain join. |
| strain-assembly-primary-4 | data/bvbrc/bvbrc-0013.jsonl.gz; line 23931 | supports | Inspected primary source accessions, source taxon/strain identifiers, supplied versions and explicit assembly pairings where present. Taxon and assembly identity are distinct; matching labels alone do not establish a strain join. |
| strain-inventory-1 | data/raw/strain_assemblies.tsv; line 26058; line 26059; line 26060; line 26061; line 26062; line 26063; line 26064; line 26065; line 26066; line 103468; line 103469; line 103470; line 103471; line 103472; line 103473; line 103474; line 103475 | supports | Exact listed-strain inventory selection; source rows and evidence fields were compared with all native link assertions. Absence is bounded to the pinned import tables. |
| strain-inventory-2 | data/raw/strain_genome_records.tsv; line 20814; line 20815; line 20816; line 20817; line 20818; line 20819; line 20820; line 20821; line 83323; line 83324; line 83325; line 83326; line 83327; line 83328 | supports | Exact listed-strain inventory selection; source rows and evidence fields were compared with all native link assertions. Absence is bounded to the pinned import tables. |
| strain-inventory-3 | data/raw/strain_related_records.tsv; line 72201; line 72202; line 72203; line 72204; line 72205; line 72206; line 72207; line 72208; line 72209; line 72210; line 72211; line 72212; line 72213; line 72214; line 72215; line 72216; line 72217; line 72218; line 72219; line 72220; line 299409; line 299410; line 299411; line 299412; line 299413; line 299414; line 299415; line 299416; line 299417; line 299418; line 299419; line 299420; line 299421; line 299422; line 299423; line 299424; line 299425; line 299426; line 299427; line 299428; line 299429; line 299430; line 299431; line 299432; line 299433; line 299434; line 299435; line 299436; line 299437; line 299438; line 299439; line 299440; line 299441; line 299442; line 299443; line 299444; line 299445; line 299446; line 299447 | supports | Exact listed-strain inventory selection; source rows and evidence fields were compared with all native link assertions. Absence is bounded to the pinned import tables. |
| strain-inventory-4 | data/straininfo/strain_links.tsv; line 13811; line 78049; line 78050; line 78051; line 78052; line 78053 | supports | Exact listed-strain inventory selection; source rows and evidence fields were compared with all native link assertions. Absence is bounded to the pinned import tables. |
| strain-inventory-5 | data/straininfo/assemblies.tsv; line 2299; line 7440 | supports | Exact listed-strain inventory selection; source rows and evidence fields were compared with all native link assertions. Absence is bounded to the pinned import tables. |
| strain-inventory-6 | data/straininfo/related_records.tsv.gz; line 34648; line 34649; line 186690; line 186691; line 186692; line 186693; line 186694; line 186695; line 186696; line 186697; line 186698; line 186699; line 186700; line 186701; line 186702; line 186703 | supports | Exact listed-strain inventory selection; source rows and evidence fields were compared with all native link assertions. Absence is bounded to the pinned import tables. |
| strain-inventory-7 | data/atb/strain_links.tsv; Complete table selection for exact listed local BacDive strain IDs has no match. | supports | Exact listed-strain inventory selection; source rows and evidence fields were compared with all native link assertions. Absence is bounded to the pinned import tables. |
| strain-policy | docs/STRAIN_GENOMES.md; Culture-collection authorities; GTDB genome metadata; Primary GOLD organism and project metadata; Accessions and evidence rules | supports | Whole eligible culture deposits establish joins; taxonomy, bare names and shared samples do not. Original versions and typed related references are preserved. |
| straininfo-policy | docs/STRAININFO.md; Import boundary and evidence | supports | An eligible rich source deposit must match its own full designation. Every sequence explicitly names that SI-DP. Source groups may conflict without declaring biological equivalence. |
| strain-cafi | src/taxonmech/data/cafi_acronyms.json; acr/acr_synonym and regex_id.full for DSM, ATCC, JCM, NBRC and VKM; whole-string results in retained strain-authority-agent-check.json | supports | Pinned CAFI authority and full accession templates validate the whole source deposit identifiers; retained aliases do not automatically become deposits. |
| strain-cafi-pin | src/taxonmech/data/cafi_acronyms.metadata.json; source_commit, sha256, retrieved_date, modifications | supports | Registry pin effeca350ac72faeb01d19c2c14830a905c5d116; SHA256 d51abac898f8796dbc2c7b127bb4e61a8ada7f4350fdce689cf755d926446061. |
| strain-join-owner | src/taxonmech/genome_sources.py; normalize_culture_identifier, culture_curie_key, extract_gtdb_strain_genomes | supports | Native matching normalizes only authority case and initial separator, then uses a case-sensitive full accession template. GTDB strains require whole semicolon-delimited deposit tokens. |
| straininfo-join-owner | src/taxonmech/straininfo_links.py; build_links, lines112–275 | supports | Source strain status, own rich deposit status, non-erroneous relation and non-deprecated collection are checked. Sequences import only through their explicit same-deposit path. |
| strain-source-pin-bacdive | data/bacdive/SOURCE.json; source snapshot metadata | supports | BacDive v2 capture 2026-09-13T17:17:21.092811+00:00. This snapshot context is distinct from current remote availability. |
| strain-source-pin-straininfo | data/straininfo/SOURCE.json; source snapshot metadata | supports | StrainInfo API2.1.0 capture 2026-09-13T17:29:00Z. This snapshot context is distinct from current remote availability. |
| strain-source-pin-gold | data/gold/SOURCE.json; source snapshot metadata | supports | Primary public GOLD workbook projection; workbook SHA256 7d22ea3f2c9ac40d513cd4af1410f7d19f3525347eb272787ba1c20525340370. This snapshot context is distinct from current remote availability. |
| strain-source-pin-bvbrc | data/bvbrc/SOURCE.json; source snapshot metadata | supports | BV-BRC capture 2026-09-13T17:42:47.000815+00:00. This snapshot context is distinct from current remote availability. |
| strain-ay354034-authority | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&amp;id=AY354034&amp;retmode=json; result.34017063: caption, accessionversion, title, organism, taxid, strain | refutes | Current NCBI nucleotide summary identifies AY354034.1 as Methanococcus aeolicus, taxon42879, while retaining strain text DSM4304. This corroborates the conflict in the StrainInfo source description. |
| remaining-straininfo-doi-authority | https://api.datacite.org/dois?query=doi%3A%28%2210.60712%2FSI-ID407496.2%22+OR+%2210.60712%2FSI-ID407782.3%22+OR+%2210.60712%2FSI-ID46110.3%22+OR+%2210.60712%2FSI-ID47796.2%22+OR+%2210.60712%2FSI-ID48540.3%22%29&amp;page%5Bsize%5D=100; data[attributes.doi=10.60712/si-id46110.3].attributes: doi/identifiers/titles/version/url/state; data[attributes.doi=10.60712/si-id47796.2].attributes: doi/identifiers/titles/version/url/state; data[attributes.doi=10.60712/si-id48540.3].attributes: doi/identifiers/titles/version/url/state | supports | Resolved exact nested StrainInfo DOI versions: 10.60712/SI-ID46110.3, 10.60712/SI-ID47796.2, 10.60712/SI-ID48540.3. Each is findable with the matching SI-ID, title, version and resource URL. |
| remaining-bioproject-authority | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=bioproject&amp;id=686870%2C425494%2C425493%2C263072%2C224116%2C208006%2C104&amp;retmode=json; PRJNA104: result.104.project_acc/project_target_scope/project_target_material/project_data_type/organism_name/organism_strain/taxid; PRJNA208006: result.208006.project_acc/project_target_scope/project_target_material/project_data_type/organism_name/organism_strain/taxid; PRJNA224116: result.224116.project_acc/project_target_scope/project_target_material/project_data_type/organism_name/organism_strain/taxid; PRJNA263072: result.263072.project_acc/project_target_scope/project_target_material/project_data_type/organism_name/organism_strain/taxid; PRJNA425493: result.425493.project_acc/project_target_scope/project_target_material/project_data_type/organism_name/organism_strain/taxid; PRJNA425494: result.425494.project_acc/project_target_scope/project_target_material/project_data_type/organism_name/organism_strain/taxid | supports | Resolved exact asserted BioProject IDs: PRJNA104, PRJNA208006, PRJNA224116, PRJNA263072, PRJNA425493, PRJNA425494. Expected organism/strain scope is retained, with PRJNA224116 recognized as multispecies RefSeq annotation context where present. |
| remaining-biosample-authority | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=biosample&amp;id=17126929%2C3097703%2C2603985%2C8220156%2C8220155%2C3081472&amp;retmode=json; SAMN02603985: result.2603985.accession/taxonomy/organism; embedded sampledata BioSample/Attributes/Attribute with attribute_name equal to strain and Links/Link with target equal to bioproject; SAMN03081472: result.3081472.accession/taxonomy/organism; embedded sampledata BioSample/Attributes/Attribute with attribute_name equal to strain and Links/Link with target equal to bioproject; SAMN03097703: result.3097703.accession/taxonomy/organism; embedded sampledata BioSample/Attributes/Attribute with attribute_name equal to strain and Links/Link with target equal to bioproject; SAMN08220155: result.8220155.accession/taxonomy/organism; embedded sampledata BioSample/Attributes/Attribute with attribute_name equal to strain and Links/Link with target equal to bioproject; SAMN08220156: result.8220156.accession/taxonomy/organism; embedded sampledata BioSample/Attributes/Attribute with attribute_name equal to strain and Links/Link with target equal to bioproject | supports | Resolved exact asserted BioSample IDs: SAMN02603985, SAMN03081472, SAMN03097703, SAMN08220155, SAMN08220156. Each explicit strain/taxon and primary BioProject link agrees with its inspected source chain. |
| remaining-nuccore-authority | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&amp;id=AJ575815%2CU66886%2CX17237&amp;retmode=json; INSDC:AJ575815: result.32485664.caption/accessionversion/title/organism/taxid/strain; INSDC:U66886: result.2586074.caption/accessionversion/title/organism/taxid/strain; INSDC:X17237: result.38795.caption/accessionversion/title/organism/taxid/strain | supports | Exact AJ575815, U66886 and X17237 accession summaries resolve to Archaeoglobus fulgidus DSM 4304, taxon224325, with returned .1 versions retained as separate authority observations. |
| nomenclature-authority-1 | https://lpsn.dsmz.de/species/archaeoglobus-fulgidus; lpsn-fulgidus.html; Pinned LPSN row 15381, lpsn:773360, and current LPSN support Archaeoglobus fulgidus Stetter 1988, validly published ICNP correct name, and ATCC 49558 / DSM 4304 / JCM 9628 / NBRC 100126 type deposits. Current NCBI preserves authority as a related name. DOI 10.1016/s0723-2020(88)80032-8 resolves to Stetter 1988 effective publication; DOI 10.1099/00207713-38-3-328 is Validation List 26. X05567.1 is the 16S RNA sequence of VC-16 / DSM 4304, taxid 224325. LPSN bridges the species to GTDB Archaeoglobus fulgidus. These nomenclatural checks do not assess every nested strain link. | supports | Inspected authority/source text for exact nomenclatural name, publication identity or type-strain sequence/deposit. Publication abstracts and registry entries do not certify whole-paper phenotypic claims. |
| nomenclature-authority-2 | https://api.crossref.org/works/10.1016%2Fs0723-2020(88)80032-8; crossref-fulgidus.json; Pinned LPSN row 15381, lpsn:773360, and current LPSN support Archaeoglobus fulgidus Stetter 1988, validly published ICNP correct name, and ATCC 49558 / DSM 4304 / JCM 9628 / NBRC 100126 type deposits. Current NCBI preserves authority as a related name. DOI 10.1016/s0723-2020(88)80032-8 resolves to Stetter 1988 effective publication; DOI 10.1099/00207713-38-3-328 is Validation List 26. X05567.1 is the 16S RNA sequence of VC-16 / DSM 4304, taxid 224325. LPSN bridges the species to GTDB Archaeoglobus fulgidus. These nomenclatural checks do not assess every nested strain link. | supports | Inspected authority/source text for exact nomenclatural name, publication identity or type-strain sequence/deposit. Publication abstracts and registry entries do not certify whole-paper phenotypic claims. |
| nomenclature-authority-3 | https://api.crossref.org/works/10.1099%2F00207713-38-3-328; nomenclature-agent-fulgidus-validation.json; Pinned LPSN row 15381, lpsn:773360, and current LPSN support Archaeoglobus fulgidus Stetter 1988, validly published ICNP correct name, and ATCC 49558 / DSM 4304 / JCM 9628 / NBRC 100126 type deposits. Current NCBI preserves authority as a related name. DOI 10.1016/s0723-2020(88)80032-8 resolves to Stetter 1988 effective publication; DOI 10.1099/00207713-38-3-328 is Validation List 26. X05567.1 is the 16S RNA sequence of VC-16 / DSM 4304, taxid 224325. LPSN bridges the species to GTDB Archaeoglobus fulgidus. These nomenclatural checks do not assess every nested strain link. | supports | Inspected authority/source text for exact nomenclatural name, publication identity or type-strain sequence/deposit. Publication abstracts and registry entries do not certify whole-paper phenotypic claims. |
| nomenclature-authority-4 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&amp;id=X05567,AB274307,MW531883&amp;retmode=json; nomenclature-agent-sequences.json; Pinned LPSN row 15381, lpsn:773360, and current LPSN support Archaeoglobus fulgidus Stetter 1988, validly published ICNP correct name, and ATCC 49558 / DSM 4304 / JCM 9628 / NBRC 100126 type deposits. Current NCBI preserves authority as a related name. DOI 10.1016/s0723-2020(88)80032-8 resolves to Stetter 1988 effective publication; DOI 10.1099/00207713-38-3-328 is Validation List 26. X05567.1 is the 16S RNA sequence of VC-16 / DSM 4304, taxid 224325. LPSN bridges the species to GTDB Archaeoglobus fulgidus. These nomenclatural checks do not assess every nested strain link. | supports | Inspected authority/source text for exact nomenclatural name, publication identity or type-strain sequence/deposit. Publication abstracts and registry entries do not certify whole-paper phenotypic claims. |
| adapter-availability | Bounded local kg-microbe-sources runner lookup; {"accessed_at":"2026-10-21T06:39:20.334208+00:00","console_runner":null,"owned_environment_runner":false,"bounded_project_search":{"/Users/marcin/Documents/VIMSS/ontology/Mechs/claw":{"exists":false,"pyproject_exists":false},"/Users/marcin/Documents/VIMSS/ontology/Mechs/culturebotai-claw":{"exists":false,"pyproject_exists":false},"/Users/marcin/Documents/VIMSS/ontology/Mechs/wizard-claw":{"exists":false,"pyproject_exists":false}},"scope":"PATH lookup, owned environment executable check, and direct gitignore-independent existence checks of three explicit candidate project directories. No ignored-file filtering. Not a machine-wide availability claim."} | supports | The CLI was unavailable in PATH, the owned environment and three explicit candidate CLAW roots; source fallback followed the skill. |
| imodulondb-datasets | https://imodulondb.org/api/datasets; All returned organism/dataset keys; exact names and synonyms in adapter assessment | supports | Inspected the complete public dataset-index response:20 organisms/28 datasets, no Archaeoglobus or Methanococcus match. This bounds applicability, not biological absence. |
| historical-mediadive-edge | data/raw/MANIFEST.yaml; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/mediadive/edges.tsv; expected=78ea275a59d4e2de09a9cf72652ec64454c6a111d2defa1ae0a44bac8a72e523; observed=4e933d1e2412fb1aad74e60719a6a64dfa34862ff0a6b84e93d78da5ce13dd8b | partial | Retained configured-path source check found bytes differing from the manifest-pinned original; this does not establish global absence. |
| historical-gold-edge | data/raw/MANIFEST.yaml; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/gold/edges.tsv; expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12; observed=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d | partial | Retained configured-path source check found bytes differing from the manifest-pinned original; this does not establish global absence. |
| historical-madin-edge | data/raw/MANIFEST.yaml; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv; expected=3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f; observed=c19bfc848e1b410548614c54a2b99e2c58452d58aeb61f972c99fcb3039a1d24 | partial | Retained configured-path source check found bytes differing from the manifest-pinned original; this does not establish global absence. |
| strict-receipt | just validate-strict data/taxa/archaea/archaeoglobus_fulgidus.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/strict-04.tsv; This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-20T07:29:45Z, finished 2026-10-20T07:29:47Z, exit 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times.<br>Validating 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0012/src/taxonmech/schema/taxonmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/strict-04.tsv |
| history-receipt | just validate-history; All 18 standalone history records; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T06:42:11Z, exit 0. All 18 standalone history records; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check.<br>history links: 18 record(s), 0 invalid<br>No issues found<br>18 history record(s) valid against src/taxonmech/schema/history.yaml |
| corpus-receipt | just verify-corpus; All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T06:48:01Z, exit 0. All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check.<br>uv run python scripts/verify_corpus.py <br>expected 626048 records, found 626048 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ and curation/seed_scope.tsv |
| products-receipt | just validate-products; Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T07:19:10Z, exit 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check.<br>uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml<br><br>id↔label correspondence summary:<br><br>✅ All id↔label pairs correspond. |
| qc-receipt | just qc; Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T07:50:51Z, exit 0. Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check.<br>All checks passed!<br>1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33)<br>Validating 626048 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0014/src/taxonmech/schema/taxonmech.yaml<br>  files scanned:      626048<br>expected 626048 records, found 626048 on disk<br>pages/ is current<br>Site publication: 530,946,096 bytes (budget 950,000,000)<br>626048 taxon records<br>  NCBITAXON        626048<br>All TaxonMech quality gates passed.<br>  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890 strains (not genome counts)<br>  Related STRAININFO_DEPOSIT: 107277 strain-record pairs, 106843 identifiers, 53890 strains (not genome counts)<br>  Related NUCLEOTIDE_SEQUENCE: 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)<br>LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809 records mapped, 324404579 genomes summed across record attestations (not deduplicated)<br>Causal graphs: 0 records (0 evidence-backed edges)<br><br>All TaxonMech quality gates passed. |

## Limits And Additional Notes

- The review assesses exact identifiers, nomenclature, source placement and import completeness at the captured versions; it does not establish experimental phenotypes, assembly sequence equivalence or a phylogenetic species boundary.
- The original manifest-pinned aggregate source bytes were unavailable at the configured historical paths in retained hash observations. Inventory counts agree, but original aggregate-edge recounts remain unavailable; primary deposit chains do not replace those historical aggregates.
- AY354034 is explicitly attached to DSM 4304/SI-DP125019 in StrainInfo, but its source description and captured current NCBI esummary identify Methanococcus aeolicus (NCBITaxon:42879), not Archaeoglobus fulgidus. The imported source description and typed nucleotide reference faithfully preserve that disagreement under docs/STRAININFO.md; this is not established as an extractor or seeder defect. Keep a qualified limitation and seek authoritative StrainInfo/INSDC reconciliation before treating AY354034 as biological evidence about the Archaeoglobus strain.
- Source assertions, deposit identities and primary accession metadata were assessed at the captured snapshot versions. Their presence does not establish current culture availability, biological equivalence across databases or whole-paper experimental support.
- IMG2528311132 is supported by the BacDive132693 sequence row; no independent IMG record or GOLD analysis for that identifier was inspected.
- Current NCBI summaries verify the requested identifiers and reported taxon/strain context; they do not establish cross-database biological genome equivalence or experimentally validate metadata titles.
- The exact nested StrainInfo dataset DOI versions resolve at DataCite, but current availability of the physical cultures and the full contents of live deposit records were not independently checked.
- IMG identifiers retain inspected BacDive and, where present, GOLD source support; no direct IMG record response was inspected.
- AJ575815, U66886 and X17237 were verified through NCBI ESummary identity metadata; complete sequence records and gene function were not reassessed. The returned .1 versions do not modify native unversioned assertions, and AY354034 remains the separately documented conflict.
- iModulonDB CLI unavailable in bounded checks; official public index inspected instead. No covered Archaeoglobus dataset was found at that capture; this is not negative phenotype or transcriptomic evidence.
- Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check.
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base recapture preserves target/source-table bytes; five changed guidance/scope/path/seeder inputs were explicitly reassessed. Original captures and exact transition receipts remain retained.
- Every new bundle still requires its own validate/save/check recipe; baseline native receipts do not claim these later steps have run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T075227Z-archaeoglobus_fulgidus
kind: record
repository: CultureBotAI/TaxonMech
title: 'Record review: Archaeoglobus fulgidus'
started_at: '2026-10-20T07:29:35Z'
finished_at: '2026-10-21T07:52:27Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: The reviewer did not author the existing generated target; this
    review changes only new review artifacts in an isolated checkout.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: Archaeoglobus fulgidus has supported exact NCBI identity and source-scoped
  representation. No record-specific import defect was established. The explicit StrainInfo
  AY354034 deposit link retains conflicting Methanococcus sequence metadata. Historical
  aggregate counts remain inventory-verified without an independent original-edge
  recount.
source:
  git_revision: 01ca63effdf8c03a644df893ba6129b2d8448ea4
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 8e8fd97c64fbff27e023c7a768b4c806c98f56cd6571e7102217a2c833284df6
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 4c7090b9d7fd0c6f7f2b4e47b48cbf64835e8d27b44944649e1ccd9038ce462d
    role: context
  - path: AGENTS.md
    sha256: bde64bd1943c4fc64b332cdbc76b89c1460294d9b1042beeedbfa91160a70331
    role: context
  - path: CLAUDE.md
    sha256: 7ffd88ac6de931cabf76781935be14d465472038e3bb654208b837c3e2df8258
    role: context
  - path: conf/id_label_targets.yaml
    sha256: bfd1b248f7b189cd054e15b7ad0171042a30980d2ebdbdd8e7d85cea68dde9c8
    role: context
  - path: conf/ncbi_taxdump.yaml
    sha256: 1d734bbb3ebf9d36e304d8030c5852fa4f0f306fca2849be5dec8f3dff86f887
    role: context
  - path: conf/record_review.yaml
    sha256: 366312506b771fc18fc5bfc30d5ec942b2c96212e1f4f95c463cfa1707fbebaa
    role: context
  - path: curation/seed_scope.tsv
    sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
    role: context
  - path: data/atb/MANIFEST.yaml
    sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
    role: context
  - path: data/atb/strain_links.tsv
    sha256: 50683192c8015badf14a8a2aab73929a21b830117449ce329d1216a698abf1c0
    role: context
  - path: data/bacdive/SOURCE.json
    sha256: 16c898e46bca4544e4d9f1908db229aa3d360c8cf7018e036a5389a979dc3716
    role: context
  - path: data/bacdive/records.jsonl.gz
    sha256: b27d0f50f06aa33615e7cc2aae4acb7c2767df930c85292e76fbb462ac136080
    role: context
  - path: data/bvbrc/SOURCE.json
    sha256: 0e00cbb6c5fa55ceb60f8d9359a86f605feaf26ddfa4f91dab084bc52f1d1fe4
    role: context
  - path: data/bvbrc/bvbrc-0000.jsonl.gz
    sha256: 2596cba5d338aec8efba41ffd2fd41575dc7902ca8efa11927ce08317575911f
    role: context
  - path: data/bvbrc/bvbrc-0001.jsonl.gz
    sha256: 57e653d914dc3ad6774a586f40a5059361654319423b5e92cc31909593d75ae8
    role: context
  - path: data/bvbrc/bvbrc-0002.jsonl.gz
    sha256: bef1faede27841f9cf4c19b1d10c19055c5abae8b662dede01dfdcc99c4d4e61
    role: context
  - path: data/bvbrc/bvbrc-0003.jsonl.gz
    sha256: 8bb3c271889d5fa2a0c07ebec1ab3ef53814cb05669e6527862e72344414db57
    role: context
  - path: data/bvbrc/bvbrc-0004.jsonl.gz
    sha256: a41fba508df434ec13223ff5bd0fe0129f8725d34002602a69244f98f935e4d7
    role: context
  - path: data/bvbrc/bvbrc-0005.jsonl.gz
    sha256: 2888bdd5c63eaf62325334a2e027dafb2261ad4dfbf80e2a9809a496037c2dcd
    role: context
  - path: data/bvbrc/bvbrc-0006.jsonl.gz
    sha256: 61c0401e39f33dc39277f32315a517f763f9272330fab2b0aed6d0458c693c44
    role: context
  - path: data/bvbrc/bvbrc-0007.jsonl.gz
    sha256: ecec1a204901c3d4db320a7e9dcd22e4103913b82711263108f8413133337dd2
    role: context
  - path: data/bvbrc/bvbrc-0008.jsonl.gz
    sha256: 24a1a20ec12f7c0857e5457cc70df82ad71b6e5a2420f9ab64ebc89213f0d866
    role: context
  - path: data/bvbrc/bvbrc-0009.jsonl.gz
    sha256: f78ffa7e07a829537c004f561e31124837565ec354dce4db11630f0f11cc000b
    role: context
  - path: data/bvbrc/bvbrc-0010.jsonl.gz
    sha256: 8836863434baa22b0910abdb5ef4bdb263fa2ed628bfa80e79f2be98f81fe872
    role: context
  - path: data/bvbrc/bvbrc-0011.jsonl.gz
    sha256: 3ed26d0ec9d06ebf36f16e83d6c65ea76e6f50a3b9355ed2f0a6b899d5e4cb87
    role: context
  - path: data/bvbrc/bvbrc-0012.jsonl.gz
    sha256: 90763f4d476afd14ff08c5cac4d38743cad2f8919d72c756755b76179f766f16
    role: context
  - path: data/bvbrc/bvbrc-0013.jsonl.gz
    sha256: ba814e4c647d96e5d00512c336e83a6fd2448549c7f9ef46cc8fd59e1790235b
    role: context
  - path: data/bvbrc/bvbrc-0014.jsonl.gz
    sha256: 741df59559faa6e84faad9216adf238d4506198332b9d441a74a5b1ff09364cc
    role: context
  - path: data/bvbrc/bvbrc-0015.jsonl.gz
    sha256: 6387f2db4e0dd8b1c4f91a1506223687dd465f05b213bcae74968644805af13e
    role: context
  - path: data/bvbrc/bvbrc-0016.jsonl.gz
    sha256: 2a653d62267adbf5f930680c75fdc402e77c771c770e3600d81f4eae9c3a61d8
    role: context
  - path: data/bvbrc/bvbrc-0017.jsonl.gz
    sha256: 56b0b9a6d669ac631000b4469eb875627f7c7aa658875955a7956b06fa63468a
    role: context
  - path: data/bvbrc/bvbrc-0018.jsonl.gz
    sha256: 7d8ded4bfb5c1f6597ef5aa1de1fd84d437c281affa257c2900f884319cc75fe
    role: context
  - path: data/bvbrc/bvbrc-0019.jsonl.gz
    sha256: 1f46317fc56c582f17dfa6c0ea30c6d80a5cc5f2730dc4ac491b0aed2b8c9876
    role: context
  - path: data/bvbrc/bvbrc-0020.jsonl.gz
    sha256: ce96b1844f603b80f97dd4d814dafe8d4091e976a8b9e3a4e59fafffd28ad553
    role: context
  - path: data/bvbrc/bvbrc-0021.jsonl.gz
    sha256: 5cb3e9b76ea660b12b003d61ee6cf680dc486928f359d819002171603afdba3b
    role: context
  - path: data/bvbrc/bvbrc-0022.jsonl.gz
    sha256: 12db5676a406f1c32dcb2d130785d2a046493b8535ba95dd806135850e21b8ff
    role: context
  - path: data/bvbrc/bvbrc-0023.jsonl.gz
    sha256: 5eaec8d122bdfcabd4483693821bb0c761b8509806006ecdf436926f620926fd
    role: context
  - path: data/bvbrc/bvbrc-0024.jsonl.gz
    sha256: b4f07a81b1af211aa9c77595e9d1d9fb300eb3e57bc183157c3fceecfac54d73
    role: context
  - path: data/bvbrc/bvbrc-0025.jsonl.gz
    sha256: 6d40fd7201112c415d5a8112b19b4ce388a4e44ea98fd879e4814897959befaf
    role: context
  - path: data/bvbrc/bvbrc-0026.jsonl.gz
    sha256: eb239c5e814a8434429a6977bfa6e1a909f45763423ff73a8834adb735f8dfe8
    role: context
  - path: data/bvbrc/bvbrc-0027.jsonl.gz
    sha256: 1ddd098b0401da6d7b63ceb6e3eb02ded4d4811a9959e8074dc68d3410fc65de
    role: context
  - path: data/bvbrc/bvbrc-0028.jsonl.gz
    sha256: 46b20814a333c68d624f1451c15c3059dbf6a7d5fa81bc99715b1b903aa34dc1
    role: context
  - path: data/catalog/MANIFEST.json
    sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
    role: context
  - path: data/catalog/gtdb_genomes-0000.jsonl.gz
    sha256: 2392b3f07a712e9198bb9a5088cc1389ccc7d426f7bd2f5462dedb88b1f69ccf
    role: context
  - path: data/catalog/gtdb_genomes-0001.jsonl.gz
    sha256: 806fe9de52b466a3bf143e780aa8a047bf9b91272f1a3025200e81a19c39db11
    role: context
  - path: data/catalog/gtdb_genomes-0002.jsonl.gz
    sha256: a80402c55fc62af4e29455b3ff541a9898c547941bb6979ae32768130b457878
    role: context
  - path: data/catalog/gtdb_genomes-0003.jsonl.gz
    sha256: 27952cd83f56e084919e6bc31778365b9e7495d80a9fe6bbc97055a586ce8344
    role: context
  - path: data/catalog/gtdb_genomes-0004.jsonl.gz
    sha256: f600f5d831d44c43e2d0872bd4d3d497d5e3550309650a2061b5f277f8c00e32
    role: context
  - path: data/catalog/gtdb_genomes-0005.jsonl.gz
    sha256: 43bdf17b0d30e3faa3ca880d89b5204fd9e79939bd82f32e5c1109b9d8674dfc
    role: context
  - path: data/catalog/gtdb_genomes-0006.jsonl.gz
    sha256: 70cf49ec754904337e0beb7fddb86bb57cf1affde8d326aef821b4b0628f8199
    role: context
  - path: data/catalog/gtdb_genomes-0007.jsonl.gz
    sha256: 0ba5c74cb32e97a3b85e26e1f43501dc2aac915bd8b26d71beab56e4b30bfd2d
    role: context
  - path: data/catalog/gtdb_genomes-0008.jsonl.gz
    sha256: f085fdc8d521b2edc10d58092170e5bc8364a3ab9d9aff5faca718f54939c7b8
    role: context
  - path: data/catalog/gtdb_genomes-0009.jsonl.gz
    sha256: 455c03d8df2b955d3a8e9cb2e502b36e62114996ed114c8c34f273854c48b4ef
    role: context
  - path: data/catalog/gtdb_genomes-0010.jsonl.gz
    sha256: aeb33045242e4c215fad2acb25ea21402e11a07164e93c54ce19a1d6408e60b3
    role: context
  - path: data/catalog/gtdb_genomes-0011.jsonl.gz
    sha256: 36fe03c7caf806752d9005fc1855616dd722a65e0b123bebbd8fea37068e3fb5
    role: context
  - path: data/catalog/gtdb_genomes-0012.jsonl.gz
    sha256: 415d91c43886d172cff6cee466abce5fccac75dfcea5d587d6290f693ba2b7e6
    role: context
  - path: data/catalog/gtdb_genomes-0013.jsonl.gz
    sha256: 1a64663893af28bb7f2a99832c81c9f2bc4203b4e5e3b318431d179c0e0ebd3b
    role: context
  - path: data/catalog/gtdb_genomes-0014.jsonl.gz
    sha256: 18d06a6dc475b9f9a7b03c57a44ad0ce3c099e2c5878a85d8385cdb48189582e
    role: context
  - path: data/catalog/gtdb_genomes-0015.jsonl.gz
    sha256: 294a24c5f36f7a2fcd8543962ca061494f3f705d65b53e525f680dd362f15d42
    role: context
  - path: data/catalog/gtdb_genomes-0016.jsonl.gz
    sha256: d97a816a4d84c4af63bbdc904ba5d8a399436da32c38a9463fa1b8497d3373d6
    role: context
  - path: data/catalog/gtdb_genomes-0017.jsonl.gz
    sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
    role: context
  - path: data/catalog/gtdb_genomes-0018.jsonl.gz
    sha256: 8baa314877815777abcdf600079c6ee42f2ea5340398df9f2e18de9c18fd4347
    role: context
  - path: data/catalog/ncbi_genbank-0000.jsonl.gz
    sha256: 2d0f73ddded027424214ecc6c9f0c91ec229278cacf8d0e1d63e5745c8064ea7
    role: context
  - path: data/catalog/ncbi_genbank-0001.jsonl.gz
    sha256: a3d1c13cd71857ef301afb53b7207af6f42f6fe2d729579660869201608c5337
    role: context
  - path: data/catalog/ncbi_genbank-0002.jsonl.gz
    sha256: 5931b3c1684ae211b5a726b0ac459abe095cb6d27a4eb8f6f54cc34aca211f75
    role: context
  - path: data/catalog/ncbi_genbank-0003.jsonl.gz
    sha256: 8e0b9562cce19621f04e26b859273d35b04ff59d581f331d266936f73de20157
    role: context
  - path: data/catalog/ncbi_genbank-0004.jsonl.gz
    sha256: 1a2f01cd2f3fd80d4af0c3cb66a8e240dae417da7c590c9cf3ba5a8f1b277840
    role: context
  - path: data/catalog/ncbi_genbank-0005.jsonl.gz
    sha256: a98802ec69b24c4c30ee290e19c3276dd6d09886e92d94d310860a36eac00f50
    role: context
  - path: data/catalog/ncbi_genbank-0006.jsonl.gz
    sha256: c3a9d0123c4b6b030567500e1be4d1612097012390a81755f01d3608ba28ac0f
    role: context
  - path: data/catalog/ncbi_genbank-0007.jsonl.gz
    sha256: 0585d70867b6c9ee2a28e88bc2c3f287af525e8a2068280a00aa78bdd22067a0
    role: context
  - path: data/catalog/ncbi_genbank-0008.jsonl.gz
    sha256: 6b31a395d770af741d40a6832c0d74026c4c82f5b95216023df867e3cdebd764
    role: context
  - path: data/catalog/ncbi_genbank-0009.jsonl.gz
    sha256: 90c09802a6726dc9feebf7f731a1429719501f2b7e72fde7a2c1bbba35645aa8
    role: context
  - path: data/catalog/ncbi_genbank-0010.jsonl.gz
    sha256: bd3b25c26922b8bb4d07330b2def9f458751eca751c053b3c8fad28b96d8fcff
    role: context
  - path: data/catalog/ncbi_genbank-0011.jsonl.gz
    sha256: c83ab7738f13d73d3a12e80fb9e375f3c606a8edf1e5033497022b1171bf18a9
    role: context
  - path: data/catalog/ncbi_genbank-0012.jsonl.gz
    sha256: 682fedc09b37ef04be14ddd277328faeb355a07e306db6b4e6f7e2744bd4f967
    role: context
  - path: data/catalog/ncbi_genbank-0013.jsonl.gz
    sha256: 4acf04eb8c8508428b6551aa5f11d32166a9e480bdb9a183903f1ff100846a14
    role: context
  - path: data/catalog/ncbi_genbank-0014.jsonl.gz
    sha256: b6359ecb36d82f0452e6a475116ed1570120a71975ab9b3223a11255a14184c3
    role: context
  - path: data/catalog/ncbi_genbank-0015.jsonl.gz
    sha256: f01fd32080be9cd013bf43115c6fc205cb05922a2b764e08e7d963a1505d4d53
    role: context
  - path: data/catalog/ncbi_genbank-0016.jsonl.gz
    sha256: 4079d0d4ccf46146db7c2cc422fe5ffbc1db60aa7c27c8a0b1ca900af13232df
    role: context
  - path: data/catalog/ncbi_genbank-0017.jsonl.gz
    sha256: f518ac6440bb9e7904fd0469915b543b14498052ea23bbc3d5b8d269e2283f6b
    role: context
  - path: data/catalog/ncbi_genbank-0018.jsonl.gz
    sha256: 3acd95b3da5fc1a7ba5eb3ca935dfeaf9876b56bd6649a1a9a2c495d70ac9215
    role: context
  - path: data/catalog/ncbi_genbank-0019.jsonl.gz
    sha256: 43c3cf300889cf57c0f216fea556d26538373930283384cb2ea6e6ad76bd2d87
    role: context
  - path: data/catalog/ncbi_genbank-0020.jsonl.gz
    sha256: e156e63235d049eea79fbd6ba18ee36789cfb8e292cfd45e91ab0c66c9732147
    role: context
  - path: data/catalog/ncbi_genbank-0021.jsonl.gz
    sha256: ea9debf9ba38dc8d89229a7a00fbbf8d064ae3aa0558004ecec9cae88793e74c
    role: context
  - path: data/catalog/ncbi_genbank-0022.jsonl.gz
    sha256: 469a26d5bf58e8af7dc9902606792f36ec63e2555d4f389ab4cbf83a897c6c3d
    role: context
  - path: data/catalog/ncbi_genbank-0023.jsonl.gz
    sha256: 41b2e6a6f8e2dbf771ba9a4b08af9fcbdb7ba63e5f5dd609512807bf2bdd21a8
    role: context
  - path: data/catalog/ncbi_genbank-0024.jsonl.gz
    sha256: 9c18f881e3b3de3fb7efb9c2b8789a7e2a6da03589d2b4e4db29b75fa4031ac0
    role: context
  - path: data/catalog/ncbi_genbank-0025.jsonl.gz
    sha256: 38750d3827d1c67eba306be889b709dce7476389853c7152d79ec0f6b1dfa944
    role: context
  - path: data/catalog/ncbi_genbank-0026.jsonl.gz
    sha256: 1136718b09392eb9cf4db29e1a7e75d87b50e37dd09eeceb53d4f1683beaa31f
    role: context
  - path: data/catalog/ncbi_genbank-0027.jsonl.gz
    sha256: ac95b037a0444ba889e1f6c8315fe2851ab6af365468599da9e453d16b18c44b
    role: context
  - path: data/catalog/ncbi_genbank-0028.jsonl.gz
    sha256: a1bfcfc8149eb6ed239f3cb02ac99b32ed846d8752b1ab7387d2687c1d5771fa
    role: context
  - path: data/catalog/ncbi_genbank-0029.jsonl.gz
    sha256: 5980edac340d816bff1150ac52ce927941089d586ca044f32cf4d2d41ffda6c8
    role: context
  - path: data/catalog/ncbi_genbank-0030.jsonl.gz
    sha256: 6b55fcf1e58ee2fd454641f8bbb94d18460855248bce17f383d01ef09a003e07
    role: context
  - path: data/catalog/ncbi_genbank-0031.jsonl.gz
    sha256: b0a3bd7b8d737619ecf3060c3c0420e5608ca56d420c16dcff3470fca4eefb8e
    role: context
  - path: data/catalog/ncbi_genbank-0032.jsonl.gz
    sha256: e2f086237fa93b8f8a696c707b98e130bad83d4744129d5743a938048e362bc1
    role: context
  - path: data/catalog/ncbi_genbank-0033.jsonl.gz
    sha256: fe98183240729cac317960e7121336da1562d6c3742db7022b449f8a5ea75e8a
    role: context
  - path: data/catalog/ncbi_genbank-0034.jsonl.gz
    sha256: 1e1a05cb78e41e6351c0bef175095aaea97424aaa58b7d521394c5a060d051b9
    role: context
  - path: data/catalog/ncbi_genbank-0035.jsonl.gz
    sha256: 9bb70597de12ccf7693a757a2e037ed85714ccb9a7283699652c59aeb913f5af
    role: context
  - path: data/catalog/ncbi_genbank-0036.jsonl.gz
    sha256: 0d1ae12a380e63b3668cdb0aad1b2f2e8ffdb6403502d6087cd3b7528cbdc278
    role: context
  - path: data/catalog/ncbi_genbank-0037.jsonl.gz
    sha256: a805deb41c1b79774d25f8fa2bcd3a362697e6a6c099d974081dc9de8f2371cc
    role: context
  - path: data/catalog/ncbi_genbank-0038.jsonl.gz
    sha256: 4fb74b5bace0a0c9f7b1285fdfba600323d70ec0e463bb651bb28487af4cfa7a
    role: context
  - path: data/catalog/ncbi_genbank-0039.jsonl.gz
    sha256: e84ae88ba419d93ad67157323d87bdb38e683974a9ec2cfde5de82dd3337225f
    role: context
  - path: data/catalog/ncbi_genbank-0040.jsonl.gz
    sha256: 4b5f18231e8901aa20d058470317754b8f6f694a41c461b487ae54bf0d7d3ab5
    role: context
  - path: data/catalog/ncbi_genbank-0041.jsonl.gz
    sha256: 1aa59ca0100eafc71c52dbff7254b814a7446b64d25cd18238e393765d842801
    role: context
  - path: data/catalog/ncbi_genbank-0042.jsonl.gz
    sha256: 05943522e7acc7d26d699abcaea1789047569bd7577f3358b250cb663865d159
    role: context
  - path: data/catalog/ncbi_genbank-0043.jsonl.gz
    sha256: 814c09850d5e9b7ae09701979e333fce91a2f8d68417839d4ac48919d929f875
    role: context
  - path: data/catalog/ncbi_genbank-0044.jsonl.gz
    sha256: 2a302507e7a9e7757589b0df7a708e45400c29c2417719d8446b4405ae5ef7e0
    role: context
  - path: data/catalog/ncbi_genbank-0045.jsonl.gz
    sha256: dbe2d8292d237125a2c614a6be589ca7df814698982f9a42baa0cab27c023798
    role: context
  - path: data/catalog/ncbi_genbank-0046.jsonl.gz
    sha256: aae02918afda531c03c3a0ce09a91544161615aa6991679941f9d98429b1bf3a
    role: context
  - path: data/catalog/ncbi_genbank-0047.jsonl.gz
    sha256: adfd221d87cf34824e331dd2b6ea05c2f5d4b0ee61731d27a0e96a25d3e635c2
    role: context
  - path: data/catalog/ncbi_genbank-0048.jsonl.gz
    sha256: 414ebf1659198f48aad082325acc72bb10f8308008885fad797b75f2d9971ee0
    role: context
  - path: data/catalog/ncbi_genbank-0049.jsonl.gz
    sha256: 467c948218f1ffbd318c3e10fd67169adbf04116b97b85a4503c9283ac58ad74
    role: context
  - path: data/catalog/ncbi_genbank-0050.jsonl.gz
    sha256: 3255e0b4b642bd0052a8868567154f0f56e1e0d3c4f20389f24ca107d3c03664
    role: context
  - path: data/catalog/ncbi_genbank-0051.jsonl.gz
    sha256: f16fcea27063ebcc95b962c6897cdbc9f1c744dc0dcd65f92a6a42c921b2db88
    role: context
  - path: data/catalog/ncbi_genbank-0052.jsonl.gz
    sha256: 09f90de7c34454c61e3cbb8e91780b6011db46309550657b0eaad6bd99670b91
    role: context
  - path: data/catalog/ncbi_genbank-0053.jsonl.gz
    sha256: de3f65f1634101e204dadf5f857bfccbe386a2f6c41f93a5044b8b1e08f4f1a2
    role: context
  - path: data/catalog/ncbi_genbank-0054.jsonl.gz
    sha256: d60db2aae2f5d820154fb2299ff0cbca1034ef057084b816497eab8ad6146643
    role: context
  - path: data/catalog/ncbi_genbank-0055.jsonl.gz
    sha256: 53dcb61e34c587557e8508725122fc6c1b6f3b17b2e193fcf051c32ebe583c4f
    role: context
  - path: data/catalog/ncbi_genbank-0056.jsonl.gz
    sha256: b3ce949155fa51ffb24841db9d308b9a4ab2215919542b4babe6e33dc42a9e66
    role: context
  - path: data/catalog/ncbi_genbank-0057.jsonl.gz
    sha256: 4ec73a547c2c9ccf0b44651e250e0761ead089321762967dd05a0480b3efceaa
    role: context
  - path: data/catalog/ncbi_genbank-0058.jsonl.gz
    sha256: 042ed969a534ff871b1f2a8af346c374ed22958141fb051522a9a628acde00a2
    role: context
  - path: data/catalog/ncbi_genbank-0059.jsonl.gz
    sha256: 41b8b3bc2dd519acfaac5e9fde412031b774b03e6a35a84b342f64292b9bae8b
    role: context
  - path: data/catalog/ncbi_genbank-0060.jsonl.gz
    sha256: 543178fd8e56953dc1148ea86dd4c042aada07c6011e390288fe888dedeebc84
    role: context
  - path: data/catalog/ncbi_genbank-0061.jsonl.gz
    sha256: ce7f731cb4689c3f1dde97fa2625be006bf05caa8730e33a93ce6be9ffcb7e11
    role: context
  - path: data/catalog/ncbi_genbank-0062.jsonl.gz
    sha256: 806652a7d24466aa814d3ff5d744cabbde12f1080d5f3e6482165a29b9d51451
    role: context
  - path: data/catalog/ncbi_genbank-0063.jsonl.gz
    sha256: cd7930d65598b83cad7de491f5f0a5c3e6ea8bdf884ab15b7d68e62a3f1051fb
    role: context
  - path: data/catalog/ncbi_genbank-0064.jsonl.gz
    sha256: c6021a2fb86726043c595711d082c0ecbad948407383a9a84f65052c985cbbcd
    role: context
  - path: data/catalog/ncbi_genbank-0065.jsonl.gz
    sha256: d47bd3c6bc300d7cda873ed20dcd439e4cb0f9ffb6d96fb593e281702a0fe113
    role: context
  - path: data/catalog/ncbi_genbank-0066.jsonl.gz
    sha256: bd87ee943f3c2561e9aa5a46f178f095f9251c6f698acfc07600df92896a443d
    role: context
  - path: data/catalog/ncbi_genbank-0067.jsonl.gz
    sha256: 0ae1684b88136de08e4cb4358929b0886290c120f162ec67d1eac4ef1d0905f3
    role: context
  - path: data/catalog/ncbi_refseq-0000.jsonl.gz
    sha256: 57d1b732198a6443d2df08f26786e669a15fdf1dbb9627bedf58407ae9cd849f
    role: context
  - path: data/catalog/ncbi_refseq-0001.jsonl.gz
    sha256: 06282ae41e57cf37ac73b236eab58ecaa081a04bf54d834b1fb61ac065ad56dc
    role: context
  - path: data/catalog/ncbi_refseq-0002.jsonl.gz
    sha256: f22a85bd89937e6e2a8c7774d699102bcbf26a31af296a6cc77976d5f2a40f72
    role: context
  - path: data/catalog/ncbi_refseq-0003.jsonl.gz
    sha256: b474d886f9ea8191aac95542314c20da96980c39753bdc32f6404fa9fdbe27fc
    role: context
  - path: data/catalog/ncbi_refseq-0004.jsonl.gz
    sha256: 3d589aeabe75cff6ff95df3cbc6b5f24d36aab5a3a42790ac770c2df692c9429
    role: context
  - path: data/catalog/ncbi_refseq-0005.jsonl.gz
    sha256: 01c2478189da678fb45af2d4e9eb2174daf2a15202757af463f68d71773fed79
    role: context
  - path: data/catalog/ncbi_refseq-0006.jsonl.gz
    sha256: fee429f92cc3820d078608de37317f71fe90054b05e4163720cc4543b9e48409
    role: context
  - path: data/catalog/ncbi_refseq-0007.jsonl.gz
    sha256: f1572d8421305b87b836f67f3d382414b166997d8dd29275d638ab906333ee6c
    role: context
  - path: data/catalog/ncbi_refseq-0008.jsonl.gz
    sha256: a47074dcd480b25d2044fcb6ed15725031e355649e7dca9c18b73408000daef9
    role: context
  - path: data/catalog/ncbi_refseq-0009.jsonl.gz
    sha256: e33402526f960a69d7e9d74c8e37e00774659987b29b9b99c6a9c14eec462851
    role: context
  - path: data/catalog/ncbi_refseq-0010.jsonl.gz
    sha256: 50cf8e902a4041cf5078a815c39c9ec44573f3499aa2e4cd9501ad59f94baae8
    role: context
  - path: data/gold/SOURCE.json
    sha256: c7ff51dc6be17c45b18cd031500fde0bd83fb6275e7c021e51bedf68f75ecf2d
    role: context
  - path: data/gold/analyses.jsonl.gz
    sha256: d597f0d5f31fc8b387caaf659f3c6a337959219870529e907a1c0287e3877b7a
    role: context
  - path: data/gold/organisms.jsonl.gz
    sha256: 8c1a055214cb240c58fadda0815efbefcb60848245e8a7474e6b1b41d123235c
    role: context
  - path: data/gold/projects.jsonl.gz
    sha256: 0d852fe0144afd778609fef82b266fd1507a4c0be949efd2f53c7c34526b6c95
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
    role: context
  - path: data/raw/bacdive_strains.tsv
    sha256: 029fd6d1f53ef7f90684130bf0d644ed3edd1d8fbeb065a511ae928f160b1eea
    role: context
  - path: data/raw/bactotraits_taxa.tsv
    sha256: 976d109cef832d8bf27cc105f67a42efbe900b6946736298602ef6d11158b197
    role: context
  - path: data/raw/culture_collection_strains.tsv
    sha256: 810fdcb16abd6330fb15bb03d4c74b18db86be36a7c599df7c6b2498d9735c95
    role: context
  - path: data/raw/gold_organisms.tsv
    sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
    role: context
  - path: data/raw/gtdb_mappings.tsv
    sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
    role: context
  - path: data/raw/gtdb_species.tsv
    sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
    role: context
  - path: data/raw/lpsn_names.tsv
    sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
    role: context
  - path: data/raw/madin_taxa.tsv
    sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
    role: context
  - path: data/raw/mediadive_taxa.tsv
    sha256: 3f74b78cadfcdb6aeae953e09fdb39e34fd9c5d5ed0be65a04a5d7fb02355905
    role: context
  - path: data/raw/ncbitaxon_taxa.tsv
    sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
    role: context
  - path: data/raw/strain_assemblies.tsv
    sha256: 71344b934db3081bfcac9562a0bd1fd8fddcfdabb8af60e208ca09035e818315
    role: context
  - path: data/raw/strain_genome_records.tsv
    sha256: 47ed80be55660aad4bd82d37d889ea60f8686cec1aeeccf72e5af22bf43728ab
    role: context
  - path: data/raw/strain_related_records.tsv
    sha256: c33a9bf4c6b94dc6971f1c0d46565092c37ba7c2d462a6bc9c20ccbf58fb9c56
    role: context
  - path: data/straininfo/MANIFEST.yaml
    sha256: 25dd601c8cf6d4d84e5cc756d1e642ebef89f565bd31967152bf0026fa072847
    role: context
  - path: data/straininfo/SOURCE.json
    sha256: 75f53bb29032b192833020b37decbc1d98fb12937e3a3cfa486ec273620453b5
    role: context
  - path: data/straininfo/assemblies.tsv
    sha256: d55ba39ab7cb81076a8edb61226de2bdf0aea699a7fb003cdf3ffb3ddc2f3f52
    role: context
  - path: data/straininfo/records.jsonl.gz
    sha256: 8f8e6093f0617317e0488463e52de153f566effa7a5d43b44d17dabab9692819
    role: context
  - path: data/straininfo/related_records.tsv.gz
    sha256: c7a262df4f970b2b11a2cf7a0a05c631ff84938e6a19cdb1d98680bb4fb35108
    role: context
  - path: data/straininfo/strain_links.tsv
    sha256: 615ac119e61df3a9d296ab16674bca6de3fdbf6478ca21a61312014f0ebbae8f
    role: context
  - path: data/taxa/PATHS.tsv
    sha256: f8f2e0721cb6839b30530b44be0d3004b9f0e6e2d4be8736f235b10117a8bd99
    role: context
  - path: data/taxa/archaea/archaeoglobus_fulgidus.yaml
    sha256: 0450088fac05df8893b49ecdd60aa2c3e9c37e98b6570c25e018a23c8f023d50
    role: target
  - path: docs/ALLTHEBACTERIA.md
    sha256: a1b0c298988782ad4b7dbb80c661c483a67cd0e478366eddbea7d1ba7595e7cd
    role: context
  - path: docs/CURATION.md
    sha256: 9e09c97bcd617f2b3d0090f775b80565fccc9d00e4c398ed58d3a31192a8fa8e
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
    role: context
  - path: docs/SCHEMA.md
    sha256: 9e767cebb2506f8372c65ceb5f75e5ef2df2b23c2be3727cfd198f447a6a0e30
    role: context
  - path: docs/SOURCE_COVERAGE.md
    sha256: 43f17c3c80815d395136aab53f310be3190a8d614a45fc2f4a3942faeb0bc9e9
    role: context
  - path: docs/STRAININFO.md
    sha256: 65d274e7126fcf7810da746366b0e60c1957f05df9016fb0900600932b278241
    role: context
  - path: docs/STRAIN_GENOMES.md
    sha256: 7cfdbc8a600173d6569f885b409b1543098bb6022e8764324d91879eaed2b597
    role: context
  - path: docs/record-review-profile.md
    sha256: bc2074242edcf09f510aae8d9cf40961ea0c1155ca497808765bdabfb35ee721
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: c46d88186cad450fbd47ce5176bf2afc8289252e287324245ad30090753c750e
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/run_qc.py
    sha256: d3a8e398b0484fef1ce4ae13e639a03dd41467c1d597d753132e4dba04df9da3
    role: context
  - path: scripts/validate_history.py
    sha256: aa8fd8528a28cf56a92768c05d57aea7ff48745510796126f144856b8fd7ae8b
    role: context
  - path: scripts/validate_id_label_correspondence.py
    sha256: b5ff41bb52d24f5d7819fb12769e216440f75ec3fb3df3e3cb2c5082fffb40e0
    role: context
  - path: scripts/validate_strict.py
    sha256: d0d75cc805cc746053076b5f75f5e6c817ab15c75a9362f8ce3be53bd4ec7382
    role: context
  - path: scripts/verify_corpus.py
    sha256: 48c4ef707543d1b836052013e8991d530d14559f9b58aa3ff9faf02c4e1ffc2e
    role: context
  - path: src/taxonmech/data/cafi_acronyms.json
    sha256: d51abac898f8796dbc2c7b127bb4e61a8ada7f4350fdce689cf755d926446061
    role: context
  - path: src/taxonmech/data/cafi_acronyms.metadata.json
    sha256: 0f2370de617bddc9d12203f9ba6e35612e61bbaf44554b30203545123bb70958
    role: context
  - path: src/taxonmech/extract.py
    sha256: 7c5b5bf385e0c060f1cb3dbac304d05ddb941e4c83c900017a04133efd6d1822
    role: context
  - path: src/taxonmech/genome_sources.py
    sha256: a8c2e1e54adcea6e223a03851ef9fd38303896bf51997a4d4c83d8512676230e
    role: context
  - path: src/taxonmech/ncbi_taxdump.py
    sha256: 83e3bfd53721a1f85291022511de6504d84caa58e899c0fd8d1797e9f00f67cf
    role: context
  - path: src/taxonmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/taxonmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/taxonmech/schema/taxonmech.yaml
    sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
    role: context
  - path: src/taxonmech/seed.py
    sha256: 3cc30f6413a293165385dfc1860505fe389e5adfe9aa3d168f76aa4cb2ac36bd
    role: context
  - path: src/taxonmech/straininfo_links.py
    sha256: b753f48edb804d588107206faeadcb2b627c5225f43fdb1a484bbf78a9d06297
    role: context
scope:
  description: Entire single generated record, including all source assertions and
    imported strains.
  selection: Original unreviewed path-order position 134; batch-0014 target 4. Excluded
    185 actual targets from validated freshmain and thirteen committed isolated branches;
    full corpus enumeration includes ignored files.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - NCBITaxon:2234
targets:
- target_id: NCBITaxon:2234
  path: data/taxa/archaea/archaeoglobus_fulgidus.yaml
  label: Archaeoglobus fulgidus
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Maintained generated-record builder
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: Maintained source inventory extractor
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/ncbi_taxdump.py
    role: Maintained NCBI primary-taxonomy projection
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxon identity, name classes and carried ancestry
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit species-or-below scope
checks:
- check_id: identity-authority
  name: Exact NCBI taxon, rank and lineage
  status: passed
  required: true
  summary: NCBITaxon:2234 denotes Archaeoglobus fulgidus at SPECIES rank beneath NCBITaxon:2233,
    genetic code 11. All 9 carried ancestors agree with the pinned inventory and captured
    official NCBI response; the response omits only the root entry. Source name classes
    remain distinct from taxon classification.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - scope-row
  - path-row
- check_id: optional-inventories
  name: Complete exact identifier and name inventory search
  status: passed
  required: true
  summary: 'Complete direct reads of twelve source/scope/path tables, including ignored
    files, support 3 imported BacDive strains over the exact target subtree (2 descendant
    taxa). All imported counts agree with their own source units: NCBITAXON 1 NAME;
    LPSN 1 NAME; GTDB 6 GENOME; BACDIVE 3 STRAIN; MEDIADIVE 1 MEDIUM; GOLD 4 ORGANISM;
    MADIN 6 TRAIT_ASSERTION. Counts of organisms, media, traits and genome assertions
    are not interchangeable and do not prove phenotype or biological genome equivalence.
    The GTDB fulgidus cluster count 6 spans four NCBI taxids; it is not the number
    of this target''s own strain genomes.'
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - record
  - taxonomy-inventory
  - lpsn-inventory
  - bacdive-inventory
  - culture-inventory
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
  - scope-row
  - path-row
  - gtdb-species
  - genome-catalog-1
  scope_note: Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs.
- check_id: gtdb-primary-counts
  name: Complete primary GTDB cluster membership
  status: passed
  required: true
  summary: All selected source counts agree; the separate notes/scope findings are
    retained where applicable.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - gtdb-full-scan
  - gtdb-species
  - gtdb-mappings
  - genome-catalog-1
  scope_note: All nineteen pinned shards; full selected cluster populations and reverse
    mapping rows.
- check_id: strain-link-inventory
  name: All imported strain link assertions match pinned inventories
  status: passed
  required: true
  summary: 'kgmicrobe.strain:bacdive_18096: 9 genome_assemblies assertions (3 distinct
    IDs), 6 genome_records assertions (3 distinct IDs), 51 related_records assertions
    (27 distinct IDs). kgmicrobe.strain:bacdive_18095: 0 genome_assemblies assertions
    (0 distinct IDs), 0 genome_records assertions (0 distinct IDs), 2 related_records
    assertions (2 distinct IDs). kgmicrobe.strain:bacdive_132693: 10 genome_assemblies
    assertions (3 distinct IDs), 8 genome_records assertions (4 distinct IDs), 22
    related_records assertions (8 distinct IDs). Every compared native assertion matches
    a retained inventory row with no missing or extra assertion.'
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - strain-inventory-1
  - strain-inventory-2
  - strain-inventory-3
  - strain-inventory-4
  - strain-inventory-5
  - strain-inventory-6
  - strain-inventory-7
  - record
  command: /private/tmp/taxonmech-record-reviews-k0MubV/repo/.venv/bin/python /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/compare_links.py
    4
  exit_code: 0
  expected_exit_code: 0
  scope_note: Actual earlier per-target comparison in the owned checkout. Full selected
    strain lists, not a pagination sample.
- check_id: strain-genome-evidence
  name: Primary own-deposit and genome evidence
  status: passed
  required: true
  summary: BacDive 18096 identifies VC-16 with DSM 4304, ATCC 49558, JCM 9628 and
    NBRC 100126. Its primary taxonomy separates species 2234 and strain 224325. StrainInfo
    SI-ID46110 version 3 carries four corresponding eligible, available, non-deprecated,
    non-erroneous deposits (125019, 125018, 158734 and 339249). ATCC 49203/SI-DP125020
    is present in that source group but is absent from the local BacDive deposit list
    and is not imported. All five source sequences explicitly name DSM 4304/SI-DP125019;
    only GCA_000008665 is a genome, while AY354034, U66886, AJ575815 and X17237 remain
    nucleotide references. GTDB row RS_GCF_000008665.1 names whole DSM 4304 and explicitly
    carries GCA_000008665.1. Primary NCBI GenBank and RefSeq rows corroborate DSM
    4304/224325 and explicitly pair their .1 versions as identical in the pinned snapshot;
    these do not assign a version to the separately unversioned BacDive, GOLD and
    StrainInfo assertion. BV-BRC 224325.10 explicitly resolves to DSM 4304 and GCA_000008665.1.
    GOLD Go0000778 joins Gp0000778 to Ga0027554 and supplies unversioned GCA_000008665
    plus IMG638154502 through the inspected culture match. Three transcriptome projects
    under Go0015557 correctly provide typed sample/project context rather than genome
    links. Additional GOLD organism rows Go0620787 and Go0620788 match NBRC and JCM
    deposits without transferring DSM-only sequences. The species record additionally
    retains distinct DSM 4139 strain Z/BacDive18095, with SI-ID47796.2/SI-DP158661
    and no imported genomes, and DSM 8774 strain 7324/BacDive132693. All three are
    source-supported BacDive strains; two classified_as fields retain their descendant
    NCBI strain taxa rather than flattening strain identity into the species.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - record
  - bacdive-inventory
  - strain-primary-bacdive
  - strain-primary-straininfo
  - strain-primary-gold-organisms
  - strain-primary-gold-projects
  - strain-primary-gold-analyses
  - strain-gtdb-primary-1
  - strain-assembly-primary-1
  - strain-assembly-primary-2
  - strain-assembly-primary-3
  - strain-assembly-primary-4
  - strain-inventory-1
  - strain-inventory-2
  - strain-inventory-3
  - strain-inventory-4
  - strain-inventory-5
  - strain-inventory-6
  - strain-inventory-7
  - strain-policy
  - straininfo-policy
  - strain-cafi
  - strain-cafi-pin
  - strain-join-owner
  - straininfo-join-owner
  - strain-source-pin-bacdive
  - strain-source-pin-straininfo
  - strain-source-pin-gold
  - strain-source-pin-bvbrc
  scope_note: Claim-level inspection of captured BacDive, StrainInfo, GOLD and applicable
    NCBI/GTDB/BV-BRC source rows; current remote resolution and cross-database biological
    equivalence remain bounded limitations.
- check_id: remaining-authority-identifiers
  name: Current source accession and DOI resolution
  status: passed
  required: true
  summary: All 3 exact nested StrainInfo DOI version(s) resolve in DataCite with the
    correct SI-ID and version. All 6 asserted BioProject IDs and 5 BioSample IDs resolve
    at NCBI. Each BioSample explicitly retains the expected strain/taxon and primary
    BioProject link. PRJNA224116 resolves as the multispecies RefSeq annotation umbrella,
    preserving the qualified project-context interpretation. AJ575815, U66886 and
    X17237 independently resolve to Archaeoglobus fulgidus DSM 4304 (taxon224325);
    returned .1 versions do not alter their native unversioned source accessions.
    AY354034 remains a distinct unresolved source conflict.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - remaining-straininfo-doi-authority
  - remaining-bioproject-authority
  - remaining-biosample-authority
  - remaining-nuccore-authority
- check_id: nomenclature-authorities
  name: Current name, publication and sequence authorities
  status: passed
  required: true
  summary: Pinned LPSN row 15381, lpsn:773360, and current LPSN support Archaeoglobus
    fulgidus Stetter 1988, validly published ICNP correct name, and ATCC 49558 / DSM
    4304 / JCM 9628 / NBRC 100126 type deposits. Current NCBI preserves authority
    as a related name. DOI 10.1016/s0723-2020(88)80032-8 resolves to Stetter 1988
    effective publication; DOI 10.1099/00207713-38-3-328 is Validation List 26. X05567.1
    is the 16S RNA sequence of VC-16 / DSM 4304, taxid 224325. LPSN bridges the species
    to GTDB Archaeoglobus fulgidus. These nomenclatural checks do not assess every
    nested strain link.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - nomenclature-authority-1
  - nomenclature-authority-2
  - nomenclature-authority-3
  - nomenclature-authority-4
- check_id: imodulondb-runner
  name: Structured iModulonDB adapter runner
  status: unavailable
  required: false
  summary: Runner could not be invoked in the bounded checked locations; inspected
    official source fallback retained.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - adapter-availability
- check_id: imodulondb-applicability
  name: iModulonDB covered organism/dataset
  status: not_applicable
  required: false
  summary: No matching published organism/dataset in the inspected public index, so
    no gene search or component summary is applicable; metadata titles remain typed
    related records.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - imodulondb-datasets
- check_id: historical-source-counts
  name: Original manifest-pinned aggregate recounts
  status: unavailable
  required: true
  summary: 'Pinned projection counts agree: [{"source":"MEDIADIVE","count":1,"unit":"MEDIUM","raw_projection_agrees":true,"historical_primary_aggregate_checked":false},{"source":"GOLD","count":4,"unit":"ORGANISM","raw_projection_agrees":true,"historical_primary_aggregate_checked":false},{"source":"MADIN","count":6,"unit":"TRAIT_ASSERTION","raw_projection_agrees":true,"historical_primary_aggregate_checked":false}].
    Original aggregate edges were not independently recounted.'
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - manifest
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
  - historical-mediadive-edge
  - historical-gold-edge
  - historical-madin-edge
- check_id: strict
  name: Native strict record validation
  status: passed
  required: true
  summary: Actual terminal exit code 0. This exact generated YAML only; its captured
    bytes remain unchanged. Actual earlier per-target invocation; the receipt retains
    its original cwd and times.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - strict-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/uv-cache
    just validate-strict data/taxa/archaea/archaeoglobus_fulgidus.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/strict-04.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: This exact generated YAML only; its captured bytes remain unchanged.
    Actual earlier per-target invocation; the receipt retains its original cwd and
    times.
- check_id: history
  name: Repository history validation
  status: passed
  required: true
  summary: Actual terminal exit code 0. All 18 standalone history records; the generated
    seed event was also inspected in this target. Actual native gate execution at
    base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes
    and terminal exit codes identify these runs. Expanded-corpus gate results are
    represented only by the corresponding terminal receipts; running gates remain
    unavailable in unsaved previews. Earlier unchanged-target strict receipts remain
    explicitly historical; new review bundles still require individual validation/save/check.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - history-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/uv-cache
    just validate-history
  exit_code: 0
  expected_exit_code: 0
  scope_note: All 18 standalone history records; the generated seed event was also
    inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
- check_id: corpus
  name: Full-corpus exact reproduction
  status: passed
  required: true
  summary: Actual terminal exit code 0. All 626,048 generated taxon YAMLs, not a focused
    approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - corpus-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/uv-cache
    just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  scope_note: All 626,048 generated taxon YAMLs, not a focused approximation. Actual
    native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
    cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
- check_id: products
  name: Native product ID/label gate
  status: passed
  required: true
  summary: Actual terminal exit code 0. Full configured corpus scan for curator-added
    graph nodes; this target contains no causal graph. Actual native gate execution
    at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes
    and terminal exit codes identify these runs. Expanded-corpus gate results are
    represented only by the corresponding terminal receipts; running gates remain
    unavailable in unsaved previews. Earlier unchanged-target strict receipts remain
    explicitly historical; new review bundles still require individual validation/save/check.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - products-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/uv-cache
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: Full configured corpus scan for curator-added graph nodes; this target
    contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
- check_id: qc
  name: Authoritative complete quality gate
  status: passed
  required: true
  summary: Actual terminal exit code 0. Repository-wide just qc, including native
    corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check. 1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33)
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - qc-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/uv-cache
    just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: Repository-wide just qc, including native corpus-wide checks. Actual
    native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
    cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/taxa/archaea/archaeoglobus_fulgidus.yaml
  accessed_at: '2026-10-21T07:52:27Z'
  support: supports
  summary: Read the entire generated YAML, including identity, lineage, names, mappings,
    source attestations, all imported strains and links, and seed history.
  locator: entire TaxonRecord; identifier=NCBITaxon:2234
  snapshot_sha256: 0450088fac05df8893b49ecdd60aa2c3e9c37e98b6570c25e018a23c8f023d50
- evidence_id: taxonomy-inventory
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-21T06:43:42Z'
  support: supports
  summary: Inspected the target and each carried ancestor, rank, parent, genetic code
    and source name classes.
  locator: 'line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""};
    line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"};
    line 1755: {"taxon_id":"NCBITaxon:2231","label":"Archaeoglobales","rank":"ORDER","parent_id":"NCBITaxon:183980"};
    line 1756: {"taxon_id":"NCBITaxon:2232","label":"Archaeoglobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2231"};
    line 1757: {"taxon_id":"NCBITaxon:2233","label":"Archaeoglobus","rank":"GENUS","parent_id":"NCBITaxon:2232"};
    line 1758: {"taxon_id":"NCBITaxon:2234","label":"Archaeoglobus fulgidus","rank":"SPECIES","parent_id":"NCBITaxon:2233","genetic_code":"11","exact_synonyms":"","related_synonyms":"Archaeoglobus
    fulgidus Stetter 1988","broad_synonyms":"","attested_by":"ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"};
    line 2981: {"taxon_id":"NCBITaxon:28890","label":"Methanobacteriota","rank":"PHYLUM","parent_id":"NCBITaxon:3366610"};
    line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"};
    line 36620: {"taxon_id":"NCBITaxon:183980","label":"Archaeoglobi","rank":"CLASS","parent_id":"NCBITaxon:28890"};
    line 621140: {"taxon_id":"NCBITaxon:3366610","label":"Methanobacteriati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
- evidence_id: scope-row
  kind: database
  reference: curation/seed_scope.tsv
  accessed_at: '2026-10-21T06:43:42Z'
  support: supports
  summary: Exact target is included in the declared seed scope.
  locator: 'line 5581: {"identifier":"NCBITaxon:2234","added":"2026-09-12","reason":"attested
    rule: Archaeoglobus fulgidus, 7 sources incl. NCBI"}'
  snapshot_sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
- evidence_id: path-row
  kind: database
  reference: data/taxa/PATHS.tsv
  accessed_at: '2026-10-21T06:43:42Z'
  support: supports
  summary: Indexed path resolves to this exact NCBI taxon.
  locator: 'line 334390: {"identifier":"NCBITaxon:2234","slug":"archaeoglobus_fulgidus"}'
  snapshot_sha256: f8f2e0721cb6839b30530b44be0d3004b9f0e6e2d4be8736f235b10117a8bd99
- evidence_id: ncbi-live
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=2012529,2250530,1935016,2234,224325,1344584,403219,1121009,138903,2798580
  accessed_at: '2026-10-20T07:29:20Z'
  support: supports
  summary: 'Inspected the official response for this exact taxon: scientific name,
    rank, parent, source name classes, lineage and genetic code. Current authority
    and pinned September inventory remain distinct observations.'
  locator: TaxaSet/Taxon[TaxId='2234']; ten-target captured response
  snapshot_sha256: 8a3866adad1ff61fdfd0bfdd06ad5f4159708e114acc5cb803032f23e4828b9f
- evidence_id: lpsn-inventory
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-21T06:43:42Z'
  support: supports
  summary: Inspected exact mapped and linked LPSN names; bounded inventory absence
    does not establish worldwide nomenclatural absence.
  locator: 'line 15381: {"lpsn_id":"lpsn:773360","name":"Archaeoglobus fulgidus","rank":"SPECIES","authority":"Stetter
    1988","url":"https://lpsn.dsmz.de/species/archaeoglobus-fulgidus","deprecated":"0","status":"legitimate=True;
    validly published under the ICNP; correct name","validly_published":"1","legitimate":"1","is_correct_name":"1","parent_lpsn_id":"lpsn:516970","ncbitaxon_ids":"NCBITaxon:2234","gtdb_ids":"GTDB:s__Archaeoglobus_fulgidus","type_strain_ids":"kgmicrobe.strain:ATCC-49558|kgmicrobe.strain:DSM-4304|kgmicrobe.strain:JCM-9628|kgmicrobe.strain:NBRC-100126","synonym_of":"","synonyms":"","publications":"doi:10.1016/s0723-2020(88)80032-8|doi:10.1099/00207713-38-3-328","sequence_accessions":"INSDC:X05567"}'
  snapshot_sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
- evidence_id: gtdb-mappings
  kind: database
  reference: data/raw/gtdb_mappings.tsv
  accessed_at: '2026-10-21T06:43:42Z'
  support: supports
  summary: Inspected direct mappings and selected clusters' reverse mappings, retaining
    each source predicate and taxon boundary.
  locator: 'line 20129: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1344584","predicate":"skos:closeMatch","genome_count":"6"};
    line 72202: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"6"};
    line 177020: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:2234","predicate":"skos:closeMatch","genome_count":"6"};
    line 177993: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:224325","predicate":"skos:closeMatch","genome_count":"6"}'
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
- evidence_id: gtdb-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-21T06:43:42Z'
  support: supports
  summary: Inspected source species identifiers, labels, parent clusters and genome
    counts.
  locator: 'line 12308: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","label":"s__Archaeoglobus_fulgidus","parent":"GTDB:g__Archaeoglobus","genome_count":"6"}'
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
- evidence_id: bacdive-inventory
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-21T06:43:42Z'
  support: supports
  summary: Complete inventory selection covers the exact target and descendants from
    the complete NCBI parent graph; its imported strain population was compared with
    the complete YAML.
  locator: 'line 17904: {"strain_id":"kgmicrobe.strain:bacdive_18095","bacdive_id":"18095","designation":"Z","taxon_ids":"NCBITaxon:2234","lpsn_ids":"lpsn:773360","culture_collection_ids":"kgmicrobe.strain:DSM-4139","medium_count":"0"};
    line 17905: {"strain_id":"kgmicrobe.strain:bacdive_18096","bacdive_id":"18096","designation":"VC-16","taxon_ids":"NCBITaxon:224325","lpsn_ids":"lpsn:773360","culture_collection_ids":"kgmicrobe.strain:ATCC-49558|kgmicrobe.strain:DSM-4304|kgmicrobe.strain:JCM-9628|kgmicrobe.strain:NBRC-100126","medium_count":"0"};
    line 55004: {"strain_id":"kgmicrobe.strain:bacdive_132693","bacdive_id":"132693","designation":"7324","taxon_ids":"NCBITaxon:1344584","lpsn_ids":"lpsn:773360","culture_collection_ids":"kgmicrobe.strain:DSM-8774","medium_count":"0"}'
  snapshot_sha256: 029fd6d1f53ef7f90684130bf0d644ed3edd1d8fbeb065a511ae928f160b1eea
- evidence_id: culture-inventory
  kind: database
  reference: data/raw/culture_collection_strains.tsv
  accessed_at: '2026-10-21T06:43:42Z'
  support: supports
  summary: Inspected exact culture-inventory associations; an isolate name or genome
    does not create an inferred deposit.
  locator: 'line 78450: {"strain_id":"kgmicrobe.strain:DSM-4139","taxon_ids":"NCBITaxon:2234"}'
  snapshot_sha256: 810fdcb16abd6330fb15bb03d4c74b18db86be36a7c599df7c6b2498d9735c95
- evidence_id: gold-organisms
  kind: database
  reference: data/raw/gold_organisms.tsv
  accessed_at: '2026-10-21T06:43:42Z'
  support: supports
  summary: Inspected the exact GOLD organism count row or bounded absence, without
    converting counts to phenotypes.
  locator: 'line 21140: {"taxon_id":"NCBITaxon:2234","organism_count":"4"}'
  snapshot_sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
- evidence_id: mediadive-taxa
  kind: database
  reference: data/raw/mediadive_taxa.tsv
  accessed_at: '2026-10-21T06:43:42Z'
  support: supports
  summary: Inspected the exact MediaDive medium count row or bounded absence, without
    converting counts to phenotypes.
  locator: 'line 6868: {"taxon_id":"NCBITaxon:2234","medium_count":"1","media_ids":"mediadive.medium:399"}'
  snapshot_sha256: 3f74b78cadfcdb6aeae953e09fdb39e34fd9c5d5ed0be65a04a5d7fb02355905
- evidence_id: madin-taxa
  kind: database
  reference: data/raw/madin_taxa.tsv
  accessed_at: '2026-10-21T06:43:42Z'
  support: supports
  summary: Inspected the exact Madin trait-assertion count row or bounded absence,
    without converting counts to phenotypes.
  locator: 'line 19569: {"taxon_id":"NCBITaxon:2234","assertion_count":"6"}'
  snapshot_sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
- evidence_id: bactotraits-taxa
  kind: database
  reference: data/raw/bactotraits_taxa.tsv
  accessed_at: '2026-10-21T06:43:42Z'
  support: supports
  summary: Inspected the exact BactoTraits trait-assertion count row or bounded absence,
    without converting counts to phenotypes.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 976d109cef832d8bf27cc105f67a42efbe900b6946736298602ef6d11158b197
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: mapping-policy
  kind: record_content
  reference: docs/HARMONIZATION.md
  accessed_at: '2026-10-21T07:52:27Z'
  support: supports
  summary: Policy permits one-to-one species closeMatch normalization and LPSN-linked
    species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage
    unchanged.
  locator: Mapping predicates; Which strains belong to a record
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
- evidence_id: equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-21T07:52:27Z'
  support: supports
  summary: TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations
    remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes
    under the source taxon.
  locator: TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
- evidence_id: seed-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-21T07:52:27Z'
  support: supports
  summary: Inspected mapping ranking, qualified predicates, fixed broadMatch wording,
    synonym/xref construction, primary cluster counts and same-taxon type-strain derivation.
  locator: GTDB mapping construction lines 444–476; LPSN/type-strain and source-attestation
    construction
  snapshot_sha256: 3cc30f6413a293165385dfc1860505fe389e5adfe9aa3d168f76aa4cb2ac36bd
- evidence_id: manifest
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-21T07:52:27Z'
  support: supports
  summary: Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd,
    upstream input hashes and extraction time 2026-09-13T17:50:44Z.
  locator: kg_microbe_source, inputs, extracted_at
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
- evidence_id: overlay-manifests
  kind: record_content
  reference: data/atb/MANIFEST.yaml
  accessed_at: '2026-10-21T07:52:27Z'
  support: supports
  summary: Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z,
    matching the sole seed event. StrainInfo manifest is independently captured in
    source.inputs.
  locator: extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml
  snapshot_sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
- evidence_id: genome-catalog-1
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0017.jsonl.gz
  accessed_at: '2026-10-20T07:31:11Z'
  support: supports
  summary: Inspected every selected GTDB cluster member, exact taxid/species-taxid,
    culture identifiers and accession versions. Species membership alone is not a
    strain identity.
  locator: 'line 30338: {"accession":"RS_GCF_900069765.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM90006976v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMEA3879005","ncbi_contig_count":"206","ncbi_contig_n50":"67601","ncbi_country":"none","ncbi_date":"2016-09-20","ncbi_genbank_assembly_accession":"GCA_900069765.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"Archaeoglobus_fulgidus_oil","ncbi_isolation_source":"formation
    liquid","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus
    fulgidus","ncbi_protein_count":"2335","ncbi_refseq_category":"na","ncbi_rrna_count":"4","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2016-09-20","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2234","ncbi_ssu_count":"2","ncbi_strain_identifiers":"Archaeoglobus_fulgidus_oil","ncbi_submitter":"NTNU","ncbi_taxid":"2234","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","ncbi_total_gap_length":"0","ncbi_total_length":"2036821","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2036821","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"FJNF00000000.1"};
    line 30980: {"accession":"GB_GCA_001508745.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM150874v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA278302","ncbi_biosample":"SAMN03445115","ncbi_contig_count":"99","ncbi_contig_n50":"34454","ncbi_country":"none","ncbi_date":"2016-01-08","ncbi_genbank_assembly_accession":"GCA_001508745.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"49_95","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus
    fulgidus","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"0","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2016-01-08","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2234","ncbi_ssu_count":"0","ncbi_strain_identifiers":"49_95","ncbi_submitter":"Lawrence
    Berkeley National Lab","ncbi_taxid":"2234","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","ncbi_total_gap_length":"0","ncbi_total_length":"2037571","ncbi_translation_table":"11","ncbi_trna_count":"0","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2037571","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"LGEQ00000000.1"};
    line 45270: {"accession":"RS_GCF_029982885.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2998288v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN33401081","ncbi_contig_count":"121","ncbi_contig_n50":"21098","ncbi_country":"USA:
    Colorado","ncbi_date":"2023-05-11","ncbi_genbank_assembly_accession":"GCA_029982885.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"DJKA110_ANT-KO_bin.46","ncbi_isolation_source":"Produced
    fluids from hydraulically fractured shales","ncbi_lat_lon":"40.411582 N 104.348363
    W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus
    sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"2","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-05-11","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1872626","ncbi_ssu_count":"0","ncbi_strain_identifiers":"DJKA110_ANT-KO_bin.46","ncbi_submitter":"The
    Ohio State University","ncbi_taxid":"1872626","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__unclassified
    Archaeoglobus;s__Archaeoglobus sp.","ncbi_total_gap_length":"0","ncbi_total_length":"1934538","ncbi_translation_table":"11","ncbi_trna_count":"44","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1934538","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JARRCC000000000.1"};
    line 47261: {"accession":"GB_GCA_001508815.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM150881v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA278302","ncbi_biosample":"SAMN03445123","ncbi_contig_count":"153","ncbi_contig_n50":"19697","ncbi_country":"USA:Alaska;
    North Slope; Kuparuk formation","ncbi_date":"2016-01-08","ncbi_genbank_assembly_accession":"GCA_001508815.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"49_2300","ncbi_isolation_source":"oil
    reservoir sample K2","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus
    fulgidus","ncbi_protein_count":"2489","ncbi_refseq_category":"na","ncbi_rrna_count":"0","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2016-01-08","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2234","ncbi_ssu_count":"0","ncbi_strain_identifiers":"49_2300","ncbi_submitter":"Lawrence
    Berkeley National Lab","ncbi_taxid":"2234","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","ncbi_total_gap_length":"0","ncbi_total_length":"2017823","ncbi_translation_table":"11","ncbi_trna_count":"0","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2017823","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"LGEX00000000.1"};
    line 47600: {"accession":"RS_GCF_000734035.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Complete Genome","ncbi_assembly_name":"ASM73403v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN03081472","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"Norway","ncbi_date":"2014-07-28","ncbi_genbank_assembly_accession":"GCA_000734035.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"marine
    oilfield; North sea","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus
    fulgidus DSM 8774","ncbi_protein_count":"2565","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"2316287","ncbi_scaffold_n75":"2316287","ncbi_scaffold_n90":"2316287","ncbi_seq_rel_date":"2014-07-28","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2234","ncbi_ssu_count":"1","ncbi_strain_identifiers":"DSM
    8774","ncbi_submitter":"University Bergen","ncbi_taxid":"1344584","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus;x__Archaeoglobus fulgidus DSM 8774","ncbi_total_gap_length":"0","ncbi_total_length":"2316287","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2316287","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"};
    line 48903: {"accession":"RS_GCF_000008665.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","gtdb_type_species_of_genus":"t","ncbi_assembly_level":"Complete Genome","ncbi_assembly_name":"ASM866v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN02603985","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"none","ncbi_date":"2000-12-01","ncbi_genbank_assembly_accession":"GCA_000008665.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus
    fulgidus DSM 4304","ncbi_protein_count":"2431","ncbi_refseq_category":"reference
    genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"2178400","ncbi_scaffold_n75":"2178400","ncbi_scaffold_n90":"2178400","ncbi_seq_rel_date":"2000-12-01","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2234","ncbi_ssu_count":"1","ncbi_strain_identifiers":"DSM
    4304","ncbi_submitter":"TIGR","ncbi_taxid":"224325","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus;x__Archaeoglobus fulgidus DSM 4304","ncbi_total_gap_length":"0","ncbi_total_length":"2178400","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"assembly
    from type material","ncbi_ungapped_length":"2178400","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"}'
  snapshot_sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
- evidence_id: gtdb-full-scan
  kind: search
  reference: data/catalog/MANIFEST.json
  accessed_at: '2026-10-20T07:31:11Z'
  support: supports
  summary: All nineteen GTDB shards were searched with exact terminal species tokens
    preserving internal genus suffix underscores. Source cluster counts and taxon
    distributions were assessed independently of exact-identity promotion.
  locator: '{"target":"NCBITaxon:2234","rank":"SPECIES","mappings":[{"source_id":"GTDB:s__Archaeoglobus_fulgidus","predicate":"skos:closeMatch","genome_count":6,"ncbi_taxids":{"2234":3,"1872626":1,"1344584":1,"224325":1},"ncbi_species_taxids":{"2234":5,"1872626":1},"members":[{"accession":"RS_GCF_900069765.1","ncbi_taxid":"2234","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus
    fulgidus","ncbi_strain_identifiers":"Archaeoglobus_fulgidus_oil","ncbi_genbank_assembly_accession":"GCA_900069765.1"},{"accession":"GB_GCA_001508745.1","ncbi_taxid":"2234","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus
    fulgidus","ncbi_strain_identifiers":"49_95","ncbi_genbank_assembly_accession":"GCA_001508745.1"},{"accession":"RS_GCF_029982885.1","ncbi_taxid":"1872626","ncbi_species_taxid":"1872626","ncbi_organism_name":"Archaeoglobus
    sp.","ncbi_strain_identifiers":"DJKA110_ANT-KO_bin.46","ncbi_genbank_assembly_accession":"GCA_029982885.1"},{"accession":"GB_GCA_001508815.1","ncbi_taxid":"2234","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus
    fulgidus","ncbi_strain_identifiers":"49_2300","ncbi_genbank_assembly_accession":"GCA_001508815.1"},{"accession":"RS_GCF_000734035.1","ncbi_taxid":"1344584","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus
    fulgidus DSM 8774","ncbi_strain_identifiers":"DSM 8774","ncbi_genbank_assembly_accession":"GCA_000734035.1"},{"accession":"RS_GCF_000008665.1","ncbi_taxid":"224325","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus
    fulgidus DSM 4304","ncbi_strain_identifiers":"DSM 4304","ncbi_genbank_assembly_accession":"GCA_000008665.1"}]}]}'
  snapshot_sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
  search_scope: Full explicit reads of every enumerated GTDB primary shard including
    ignored files. Exact terminal GTDB species token; exact assembly accession stem
    or explicit genome identifier. Versions remain separate.
- evidence_id: strain-primary-bacdive
  kind: primary_source
  reference: data/bacdive/records.jsonl.gz
  accessed_at: '2026-10-20T07:31:07Z'
  support: supports
  summary: Inspected exact asserted source records and their original strain, deposit,
    taxon, sequence and organism/project/analysis fields. These rows support source
    assertions at their own scope.
  locator: line 17903; line 17904; line 55003
  snapshot_sha256: b27d0f50f06aa33615e7cc2aae4acb7c2767df930c85292e76fbb462ac136080
- evidence_id: strain-primary-straininfo
  kind: primary_source
  reference: data/straininfo/records.jsonl.gz
  accessed_at: '2026-10-20T07:31:07Z'
  support: supports
  summary: Inspected exact asserted source records and their original strain, deposit,
    taxon, sequence and organism/project/analysis fields. These rows support source
    assertions at their own scope.
  locator: line 34115; line 35705; line 36421
  snapshot_sha256: 8f8e6093f0617317e0488463e52de153f566effa7a5d43b44d17dabab9692819
- evidence_id: strain-primary-gold-organisms
  kind: primary_source
  reference: data/gold/organisms.jsonl.gz
  accessed_at: '2026-10-20T07:31:07Z'
  support: supports
  summary: Inspected exact asserted source records and their original strain, deposit,
    taxon, sequence and organism/project/analysis fields. These rows support source
    assertions at their own scope.
  locator: line 737; line 13388; line 57651; line 451419; line 451420
  snapshot_sha256: 8c1a055214cb240c58fadda0815efbefcb60848245e8a7474e6b1b41d123235c
- evidence_id: strain-primary-gold-projects
  kind: primary_source
  reference: data/gold/projects.jsonl.gz
  accessed_at: '2026-10-20T07:31:07Z'
  support: supports
  summary: Inspected exact asserted source records and their original strain, deposit,
    taxon, sequence and organism/project/analysis fields. These rows support source
    assertions at their own scope.
  locator: line 755; line 58778; line 59171; line 150647; line 150648
  snapshot_sha256: 0d852fe0144afd778609fef82b266fd1507a4c0be949efd2f53c7c34526b6c95
- evidence_id: strain-primary-gold-analyses
  kind: primary_source
  reference: data/gold/analyses.jsonl.gz
  accessed_at: '2026-10-20T07:31:07Z'
  support: supports
  summary: Inspected exact asserted source records and their original strain, deposit,
    taxon, sequence and organism/project/analysis fields. These rows support source
    assertions at their own scope.
  locator: line 18031; line 36927
  snapshot_sha256: d597f0d5f31fc8b387caaf659f3c6a337959219870529e907a1c0287e3877b7a
- evidence_id: strain-gtdb-primary-1
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0017.jsonl.gz
  accessed_at: '2026-10-20T07:31:11Z'
  support: supports
  summary: Inspected primary source accessions, source taxon/strain identifiers, supplied
    versions and explicit assembly pairings where present. Taxon and assembly identity
    are distinct; matching labels alone do not establish a strain join.
  locator: line 30338; line 30980; line 45270; line 47261; line 47600; line 48903
  snapshot_sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
- evidence_id: strain-assembly-primary-1
  kind: primary_source
  reference: data/catalog/ncbi_genbank-0000.jsonl.gz
  accessed_at: '2026-10-20T07:34:36Z'
  support: supports
  summary: Inspected primary source accessions, source taxon/strain identifiers, supplied
    versions and explicit assembly pairings where present. Taxon and assembly identity
    are distinct; matching labels alone do not establish a strain join.
  locator: line 110; line 27228
  snapshot_sha256: 2d0f73ddded027424214ecc6c9f0c91ec229278cacf8d0e1d63e5745c8064ea7
- evidence_id: strain-assembly-primary-2
  kind: primary_source
  reference: data/catalog/ncbi_refseq-0000.jsonl.gz
  accessed_at: '2026-10-20T07:34:36Z'
  support: supports
  summary: Inspected primary source accessions, source taxon/strain identifiers, supplied
    versions and explicit assembly pairings where present. Taxon and assembly identity
    are distinct; matching labels alone do not establish a strain join.
  locator: line 103; line 23649
  snapshot_sha256: 57d1b732198a6443d2df08f26786e669a15fdf1dbb9627bedf58407ae9cd849f
- evidence_id: strain-assembly-primary-3
  kind: primary_source
  reference: data/bvbrc/bvbrc-0002.jsonl.gz
  accessed_at: '2026-10-20T07:34:36Z'
  support: supports
  summary: Inspected primary source accessions, source taxon/strain identifiers, supplied
    versions and explicit assembly pairings where present. Taxon and assembly identity
    are distinct; matching labels alone do not establish a strain join.
  locator: line 22662
  snapshot_sha256: bef1faede27841f9cf4c19b1d10c19055c5abae8b662dede01dfdcc99c4d4e61
- evidence_id: strain-assembly-primary-4
  kind: primary_source
  reference: data/bvbrc/bvbrc-0013.jsonl.gz
  accessed_at: '2026-10-20T07:34:36Z'
  support: supports
  summary: Inspected primary source accessions, source taxon/strain identifiers, supplied
    versions and explicit assembly pairings where present. Taxon and assembly identity
    are distinct; matching labels alone do not establish a strain join.
  locator: line 23931
  snapshot_sha256: ba814e4c647d96e5d00512c336e83a6fd2448549c7f9ef46cc8fd59e1790235b
- evidence_id: strain-inventory-1
  kind: database
  reference: data/raw/strain_assemblies.tsv
  accessed_at: '2026-10-20T07:29:38Z'
  support: supports
  summary: Exact listed-strain inventory selection; source rows and evidence fields
    were compared with all native link assertions. Absence is bounded to the pinned
    import tables.
  locator: line 26058; line 26059; line 26060; line 26061; line 26062; line 26063;
    line 26064; line 26065; line 26066; line 103468; line 103469; line 103470; line
    103471; line 103472; line 103473; line 103474; line 103475
  snapshot_sha256: 71344b934db3081bfcac9562a0bd1fd8fddcfdabb8af60e208ca09035e818315
- evidence_id: strain-inventory-2
  kind: database
  reference: data/raw/strain_genome_records.tsv
  accessed_at: '2026-10-20T07:29:38Z'
  support: supports
  summary: Exact listed-strain inventory selection; source rows and evidence fields
    were compared with all native link assertions. Absence is bounded to the pinned
    import tables.
  locator: line 20814; line 20815; line 20816; line 20817; line 20818; line 20819;
    line 20820; line 20821; line 83323; line 83324; line 83325; line 83326; line 83327;
    line 83328
  snapshot_sha256: 47ed80be55660aad4bd82d37d889ea60f8686cec1aeeccf72e5af22bf43728ab
- evidence_id: strain-inventory-3
  kind: database
  reference: data/raw/strain_related_records.tsv
  accessed_at: '2026-10-20T07:29:38Z'
  support: supports
  summary: Exact listed-strain inventory selection; source rows and evidence fields
    were compared with all native link assertions. Absence is bounded to the pinned
    import tables.
  locator: line 72201; line 72202; line 72203; line 72204; line 72205; line 72206;
    line 72207; line 72208; line 72209; line 72210; line 72211; line 72212; line 72213;
    line 72214; line 72215; line 72216; line 72217; line 72218; line 72219; line 72220;
    line 299409; line 299410; line 299411; line 299412; line 299413; line 299414;
    line 299415; line 299416; line 299417; line 299418; line 299419; line 299420;
    line 299421; line 299422; line 299423; line 299424; line 299425; line 299426;
    line 299427; line 299428; line 299429; line 299430; line 299431; line 299432;
    line 299433; line 299434; line 299435; line 299436; line 299437; line 299438;
    line 299439; line 299440; line 299441; line 299442; line 299443; line 299444;
    line 299445; line 299446; line 299447
  snapshot_sha256: c33a9bf4c6b94dc6971f1c0d46565092c37ba7c2d462a6bc9c20ccbf58fb9c56
- evidence_id: strain-inventory-4
  kind: database
  reference: data/straininfo/strain_links.tsv
  accessed_at: '2026-10-20T07:29:38Z'
  support: supports
  summary: Exact listed-strain inventory selection; source rows and evidence fields
    were compared with all native link assertions. Absence is bounded to the pinned
    import tables.
  locator: line 13811; line 78049; line 78050; line 78051; line 78052; line 78053
  snapshot_sha256: 615ac119e61df3a9d296ab16674bca6de3fdbf6478ca21a61312014f0ebbae8f
- evidence_id: strain-inventory-5
  kind: database
  reference: data/straininfo/assemblies.tsv
  accessed_at: '2026-10-20T07:29:38Z'
  support: supports
  summary: Exact listed-strain inventory selection; source rows and evidence fields
    were compared with all native link assertions. Absence is bounded to the pinned
    import tables.
  locator: line 2299; line 7440
  snapshot_sha256: d55ba39ab7cb81076a8edb61226de2bdf0aea699a7fb003cdf3ffb3ddc2f3f52
- evidence_id: strain-inventory-6
  kind: database
  reference: data/straininfo/related_records.tsv.gz
  accessed_at: '2026-10-20T07:29:38Z'
  support: supports
  summary: Exact listed-strain inventory selection; source rows and evidence fields
    were compared with all native link assertions. Absence is bounded to the pinned
    import tables.
  locator: line 34648; line 34649; line 186690; line 186691; line 186692; line 186693;
    line 186694; line 186695; line 186696; line 186697; line 186698; line 186699;
    line 186700; line 186701; line 186702; line 186703
  snapshot_sha256: c7a262df4f970b2b11a2cf7a0a05c631ff84938e6a19cdb1d98680bb4fb35108
- evidence_id: strain-inventory-7
  kind: database
  reference: data/atb/strain_links.tsv
  accessed_at: '2026-10-20T07:29:38Z'
  support: supports
  summary: Exact listed-strain inventory selection; source rows and evidence fields
    were compared with all native link assertions. Absence is bounded to the pinned
    import tables.
  locator: Complete table selection for exact listed local BacDive strain IDs has
    no match.
  snapshot_sha256: 50683192c8015badf14a8a2aab73929a21b830117449ce329d1216a698abf1c0
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: strain-policy
  kind: record_content
  reference: docs/STRAIN_GENOMES.md
  accessed_at: '2026-10-21T06:39:41Z'
  support: supports
  summary: Whole eligible culture deposits establish joins; taxonomy, bare names and
    shared samples do not. Original versions and typed related references are preserved.
  locator: Culture-collection authorities; GTDB genome metadata; Primary GOLD organism
    and project metadata; Accessions and evidence rules
  snapshot_sha256: 7cfdbc8a600173d6569f885b409b1543098bb6022e8764324d91879eaed2b597
- evidence_id: straininfo-policy
  kind: record_content
  reference: docs/STRAININFO.md
  accessed_at: '2026-10-21T06:39:41Z'
  support: supports
  summary: An eligible rich source deposit must match its own full designation. Every
    sequence explicitly names that SI-DP. Source groups may conflict without declaring
    biological equivalence.
  locator: Import boundary and evidence
  snapshot_sha256: 65d274e7126fcf7810da746366b0e60c1957f05df9016fb0900600932b278241
- evidence_id: strain-cafi
  kind: authority
  reference: src/taxonmech/data/cafi_acronyms.json
  accessed_at: '2026-10-21T06:39:41Z'
  support: supports
  summary: Pinned CAFI authority and full accession templates validate the whole source
    deposit identifiers; retained aliases do not automatically become deposits.
  locator: acr/acr_synonym and regex_id.full for DSM, ATCC, JCM, NBRC and VKM; whole-string
    results in retained strain-authority-agent-check.json
  snapshot_sha256: d51abac898f8796dbc2c7b127bb4e61a8ada7f4350fdce689cf755d926446061
- evidence_id: strain-cafi-pin
  kind: record_content
  reference: src/taxonmech/data/cafi_acronyms.metadata.json
  accessed_at: '2026-10-21T06:39:41Z'
  support: supports
  summary: Registry pin effeca350ac72faeb01d19c2c14830a905c5d116; SHA256 d51abac898f8796dbc2c7b127bb4e61a8ada7f4350fdce689cf755d926446061.
  locator: source_commit, sha256, retrieved_date, modifications
  snapshot_sha256: 0f2370de617bddc9d12203f9ba6e35612e61bbaf44554b30203545123bb70958
- evidence_id: strain-join-owner
  kind: record_content
  reference: src/taxonmech/genome_sources.py
  accessed_at: '2026-10-21T06:39:41Z'
  support: supports
  summary: Native matching normalizes only authority case and initial separator, then
    uses a case-sensitive full accession template. GTDB strains require whole semicolon-delimited
    deposit tokens.
  locator: normalize_culture_identifier, culture_curie_key, extract_gtdb_strain_genomes
  snapshot_sha256: a8c2e1e54adcea6e223a03851ef9fd38303896bf51997a4d4c83d8512676230e
- evidence_id: straininfo-join-owner
  kind: record_content
  reference: src/taxonmech/straininfo_links.py
  accessed_at: '2026-10-21T06:39:41Z'
  support: supports
  summary: Source strain status, own rich deposit status, non-erroneous relation and
    non-deprecated collection are checked. Sequences import only through their explicit
    same-deposit path.
  locator: build_links, lines112–275
  snapshot_sha256: b753f48edb804d588107206faeadcb2b627c5225f43fdb1a484bbf78a9d06297
- evidence_id: strain-source-pin-bacdive
  kind: record_content
  reference: data/bacdive/SOURCE.json
  accessed_at: '2026-10-21T06:39:41Z'
  support: supports
  summary: BacDive v2 capture 2026-09-13T17:17:21.092811+00:00. This snapshot context
    is distinct from current remote availability.
  locator: source snapshot metadata
  snapshot_sha256: 16c898e46bca4544e4d9f1908db229aa3d360c8cf7018e036a5389a979dc3716
- evidence_id: strain-source-pin-straininfo
  kind: record_content
  reference: data/straininfo/SOURCE.json
  accessed_at: '2026-10-21T06:39:41Z'
  support: supports
  summary: StrainInfo API2.1.0 capture 2026-09-13T17:29:00Z. This snapshot context
    is distinct from current remote availability.
  locator: source snapshot metadata
  snapshot_sha256: 75f53bb29032b192833020b37decbc1d98fb12937e3a3cfa486ec273620453b5
- evidence_id: strain-source-pin-gold
  kind: record_content
  reference: data/gold/SOURCE.json
  accessed_at: '2026-10-21T06:39:41Z'
  support: supports
  summary: Primary public GOLD workbook projection; workbook SHA256 7d22ea3f2c9ac40d513cd4af1410f7d19f3525347eb272787ba1c20525340370.
    This snapshot context is distinct from current remote availability.
  locator: source snapshot metadata
  snapshot_sha256: c7ff51dc6be17c45b18cd031500fde0bd83fb6275e7c021e51bedf68f75ecf2d
- evidence_id: strain-source-pin-bvbrc
  kind: record_content
  reference: data/bvbrc/SOURCE.json
  accessed_at: '2026-10-21T06:39:41Z'
  support: supports
  summary: BV-BRC capture 2026-09-13T17:42:47.000815+00:00. This snapshot context
    is distinct from current remote availability.
  locator: source snapshot metadata
  snapshot_sha256: 0e00cbb6c5fa55ceb60f8d9359a86f605feaf26ddfa4f91dab084bc52f1d1fe4
- evidence_id: strain-ay354034-authority
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&id=AY354034&retmode=json
  accessed_at: '2026-10-20T07:36:04Z'
  support: refutes
  summary: Current NCBI nucleotide summary identifies AY354034.1 as Methanococcus
    aeolicus, taxon42879, while retaining strain text DSM4304. This corroborates the
    conflict in the StrainInfo source description.
  locator: 'result.34017063: caption, accessionversion, title, organism, taxid, strain'
  snapshot_sha256: 9a225419e437a33162142edd667346465cf4cd37682aea296d000d0ff03c42d0
- evidence_id: remaining-straininfo-doi-authority
  kind: authority
  reference: https://api.datacite.org/dois?query=doi%3A%28%2210.60712%2FSI-ID407496.2%22+OR+%2210.60712%2FSI-ID407782.3%22+OR+%2210.60712%2FSI-ID46110.3%22+OR+%2210.60712%2FSI-ID47796.2%22+OR+%2210.60712%2FSI-ID48540.3%22%29&page%5Bsize%5D=100
  accessed_at: '2026-10-21T06:48:12Z'
  snapshot_sha256: 62b435d6eb17a9cdc7b4d48fea9b2ba84002ffb90889b3cb9c6d0180904edd57
  support: supports
  summary: 'Resolved exact nested StrainInfo DOI versions: 10.60712/SI-ID46110.3,
    10.60712/SI-ID47796.2, 10.60712/SI-ID48540.3. Each is findable with the matching
    SI-ID, title, version and resource URL.'
  locator: 'data[attributes.doi=10.60712/si-id46110.3].attributes: doi/identifiers/titles/version/url/state;
    data[attributes.doi=10.60712/si-id47796.2].attributes: doi/identifiers/titles/version/url/state;
    data[attributes.doi=10.60712/si-id48540.3].attributes: doi/identifiers/titles/version/url/state'
- evidence_id: remaining-bioproject-authority
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=bioproject&id=686870%2C425494%2C425493%2C263072%2C224116%2C208006%2C104&retmode=json
  accessed_at: '2026-10-21T06:48:08Z'
  snapshot_sha256: 3e011d4911f76fa5dacd92bfeb8d4ecfff147c5914468789c85a8cc2142467c0
  support: supports
  summary: 'Resolved exact asserted BioProject IDs: PRJNA104, PRJNA208006, PRJNA224116,
    PRJNA263072, PRJNA425493, PRJNA425494. Expected organism/strain scope is retained,
    with PRJNA224116 recognized as multispecies RefSeq annotation context where present.'
  locator: 'PRJNA104: result.104.project_acc/project_target_scope/project_target_material/project_data_type/organism_name/organism_strain/taxid;
    PRJNA208006: result.208006.project_acc/project_target_scope/project_target_material/project_data_type/organism_name/organism_strain/taxid;
    PRJNA224116: result.224116.project_acc/project_target_scope/project_target_material/project_data_type/organism_name/organism_strain/taxid;
    PRJNA263072: result.263072.project_acc/project_target_scope/project_target_material/project_data_type/organism_name/organism_strain/taxid;
    PRJNA425493: result.425493.project_acc/project_target_scope/project_target_material/project_data_type/organism_name/organism_strain/taxid;
    PRJNA425494: result.425494.project_acc/project_target_scope/project_target_material/project_data_type/organism_name/organism_strain/taxid'
- evidence_id: remaining-biosample-authority
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=biosample&id=17126929%2C3097703%2C2603985%2C8220156%2C8220155%2C3081472&retmode=json
  accessed_at: '2026-10-21T06:48:10Z'
  snapshot_sha256: 48e13362a294ed094eef67153ea5f941c4a5b452529aa92a451447102de9a2f5
  support: supports
  summary: 'Resolved exact asserted BioSample IDs: SAMN02603985, SAMN03081472, SAMN03097703,
    SAMN08220155, SAMN08220156. Each explicit strain/taxon and primary BioProject
    link agrees with its inspected source chain.'
  locator: 'SAMN02603985: result.2603985.accession/taxonomy/organism; embedded sampledata
    BioSample/Attributes/Attribute with attribute_name equal to strain and Links/Link
    with target equal to bioproject; SAMN03081472: result.3081472.accession/taxonomy/organism;
    embedded sampledata BioSample/Attributes/Attribute with attribute_name equal to
    strain and Links/Link with target equal to bioproject; SAMN03097703: result.3097703.accession/taxonomy/organism;
    embedded sampledata BioSample/Attributes/Attribute with attribute_name equal to
    strain and Links/Link with target equal to bioproject; SAMN08220155: result.8220155.accession/taxonomy/organism;
    embedded sampledata BioSample/Attributes/Attribute with attribute_name equal to
    strain and Links/Link with target equal to bioproject; SAMN08220156: result.8220156.accession/taxonomy/organism;
    embedded sampledata BioSample/Attributes/Attribute with attribute_name equal to
    strain and Links/Link with target equal to bioproject'
- evidence_id: remaining-nuccore-authority
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&id=AJ575815%2CU66886%2CX17237&retmode=json
  accessed_at: '2026-10-21T06:48:06Z'
  snapshot_sha256: 923c74d9e3e20e17198e548d8e4536ed23866e102cbf5d1060dac126c9ca2fd9
  support: supports
  summary: Exact AJ575815, U66886 and X17237 accession summaries resolve to Archaeoglobus
    fulgidus DSM 4304, taxon224325, with returned .1 versions retained as separate
    authority observations.
  locator: 'INSDC:AJ575815: result.32485664.caption/accessionversion/title/organism/taxid/strain;
    INSDC:U66886: result.2586074.caption/accessionversion/title/organism/taxid/strain;
    INSDC:X17237: result.38795.caption/accessionversion/title/organism/taxid/strain'
- evidence_id: nomenclature-authority-1
  kind: authority
  reference: https://lpsn.dsmz.de/species/archaeoglobus-fulgidus
  accessed_at: '2026-10-20T07:36:03Z'
  support: supports
  summary: Inspected authority/source text for exact nomenclatural name, publication
    identity or type-strain sequence/deposit. Publication abstracts and registry entries
    do not certify whole-paper phenotypic claims.
  locator: lpsn-fulgidus.html; Pinned LPSN row 15381, lpsn:773360, and current LPSN
    support Archaeoglobus fulgidus Stetter 1988, validly published ICNP correct name,
    and ATCC 49558 / DSM 4304 / JCM 9628 / NBRC 100126 type deposits. Current NCBI
    preserves authority as a related name. DOI 10.1016/s0723-2020(88)80032-8 resolves
    to Stetter 1988 effective publication; DOI 10.1099/00207713-38-3-328 is Validation
    List 26. X05567.1 is the 16S RNA sequence of VC-16 / DSM 4304, taxid 224325. LPSN
    bridges the species to GTDB Archaeoglobus fulgidus. These nomenclatural checks
    do not assess every nested strain link.
  snapshot_sha256: 2247f877ed2fee0bc971718d0cfc1309bef8ae2a59f02ade6af38be7f8bd4ebe
- evidence_id: nomenclature-authority-2
  kind: authority
  reference: https://api.crossref.org/works/10.1016%2Fs0723-2020(88)80032-8
  accessed_at: '2026-10-20T07:36:04Z'
  support: supports
  summary: Inspected authority/source text for exact nomenclatural name, publication
    identity or type-strain sequence/deposit. Publication abstracts and registry entries
    do not certify whole-paper phenotypic claims.
  locator: crossref-fulgidus.json; Pinned LPSN row 15381, lpsn:773360, and current
    LPSN support Archaeoglobus fulgidus Stetter 1988, validly published ICNP correct
    name, and ATCC 49558 / DSM 4304 / JCM 9628 / NBRC 100126 type deposits. Current
    NCBI preserves authority as a related name. DOI 10.1016/s0723-2020(88)80032-8
    resolves to Stetter 1988 effective publication; DOI 10.1099/00207713-38-3-328
    is Validation List 26. X05567.1 is the 16S RNA sequence of VC-16 / DSM 4304, taxid
    224325. LPSN bridges the species to GTDB Archaeoglobus fulgidus. These nomenclatural
    checks do not assess every nested strain link.
  snapshot_sha256: 528fb239ae9537f8afb53812700bf586f420b125679dfacc87d57ad4db04e82b
- evidence_id: nomenclature-authority-3
  kind: authority
  reference: https://api.crossref.org/works/10.1099%2F00207713-38-3-328
  accessed_at: '2026-10-21T06:36:40Z'
  support: supports
  summary: Inspected authority/source text for exact nomenclatural name, publication
    identity or type-strain sequence/deposit. Publication abstracts and registry entries
    do not certify whole-paper phenotypic claims.
  locator: nomenclature-agent-fulgidus-validation.json; Pinned LPSN row 15381, lpsn:773360,
    and current LPSN support Archaeoglobus fulgidus Stetter 1988, validly published
    ICNP correct name, and ATCC 49558 / DSM 4304 / JCM 9628 / NBRC 100126 type deposits.
    Current NCBI preserves authority as a related name. DOI 10.1016/s0723-2020(88)80032-8
    resolves to Stetter 1988 effective publication; DOI 10.1099/00207713-38-3-328
    is Validation List 26. X05567.1 is the 16S RNA sequence of VC-16 / DSM 4304, taxid
    224325. LPSN bridges the species to GTDB Archaeoglobus fulgidus. These nomenclatural
    checks do not assess every nested strain link.
  snapshot_sha256: 68d028d0af5a20f70c9772e7e535da50af9452add321b9dac6c99358714e03b7
- evidence_id: nomenclature-authority-4
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&id=X05567,AB274307,MW531883&retmode=json
  accessed_at: '2026-10-21T06:36:41Z'
  support: supports
  summary: Inspected authority/source text for exact nomenclatural name, publication
    identity or type-strain sequence/deposit. Publication abstracts and registry entries
    do not certify whole-paper phenotypic claims.
  locator: nomenclature-agent-sequences.json; Pinned LPSN row 15381, lpsn:773360,
    and current LPSN support Archaeoglobus fulgidus Stetter 1988, validly published
    ICNP correct name, and ATCC 49558 / DSM 4304 / JCM 9628 / NBRC 100126 type deposits.
    Current NCBI preserves authority as a related name. DOI 10.1016/s0723-2020(88)80032-8
    resolves to Stetter 1988 effective publication; DOI 10.1099/00207713-38-3-328
    is Validation List 26. X05567.1 is the 16S RNA sequence of VC-16 / DSM 4304, taxid
    224325. LPSN bridges the species to GTDB Archaeoglobus fulgidus. These nomenclatural
    checks do not assess every nested strain link.
  snapshot_sha256: f36b4e3e3c50660fe3afb4a9261b9742e18fc6daecd4c19f81b0ef4cb16151be
- evidence_id: adapter-availability
  kind: search
  reference: Bounded local kg-microbe-sources runner lookup
  accessed_at: '2026-10-21T06:39:20Z'
  support: supports
  summary: The CLI was unavailable in PATH, the owned environment and three explicit
    candidate CLAW roots; source fallback followed the skill.
  locator: '{"accessed_at":"2026-10-21T06:39:20.334208+00:00","console_runner":null,"owned_environment_runner":false,"bounded_project_search":{"/Users/marcin/Documents/VIMSS/ontology/Mechs/claw":{"exists":false,"pyproject_exists":false},"/Users/marcin/Documents/VIMSS/ontology/Mechs/culturebotai-claw":{"exists":false,"pyproject_exists":false},"/Users/marcin/Documents/VIMSS/ontology/Mechs/wizard-claw":{"exists":false,"pyproject_exists":false}},"scope":"PATH
    lookup, owned environment executable check, and direct gitignore-independent existence
    checks of three explicit candidate project directories. No ignored-file filtering.
    Not a machine-wide availability claim."}'
  snapshot_sha256: 988fdfd25b5297cd0b5459e4a854cf7959c76c47f2a9d0d268a723c60e99e68f
  search_scope: PATH lookup, owned environment executable check, and direct gitignore-independent
    existence checks of three explicit candidate project directories. No ignored-file
    filtering. Not a machine-wide availability claim.
- evidence_id: imodulondb-datasets
  kind: authority
  reference: https://imodulondb.org/api/datasets
  accessed_at: '2026-10-21T06:40:01Z'
  support: supports
  summary: Inspected the complete public dataset-index response:20 organisms/28 datasets,
    no Archaeoglobus or Methanococcus match. This bounds applicability, not biological
    absence.
  locator: All returned organism/dataset keys; exact names and synonyms in adapter
    assessment
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: historical-mediadive-edge
  kind: search
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T07:30:21Z'
  support: partial
  summary: Retained configured-path source check found bytes differing from the manifest-pinned
    original; this does not establish global absence.
  locator: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/mediadive/edges.tsv;
    expected=78ea275a59d4e2de09a9cf72652ec64454c6a111d2defa1ae0a44bac8a72e523; observed=4e933d1e2412fb1aad74e60719a6a64dfa34862ff0a6b84e93d78da5ce13dd8b
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
  search_scope: Exact configured historical input path, including ignored files; retained
    actual receipt, not a new source search.
- evidence_id: historical-gold-edge
  kind: search
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T07:30:22Z'
  support: partial
  summary: Retained configured-path source check found bytes differing from the manifest-pinned
    original; this does not establish global absence.
  locator: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/gold/edges.tsv;
    expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12; observed=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
  search_scope: Exact configured historical input path, including ignored files; retained
    actual receipt, not a new source search.
- evidence_id: historical-madin-edge
  kind: search
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T07:30:22Z'
  support: partial
  summary: Retained configured-path source check found bytes differing from the manifest-pinned
    original; this does not establish global absence.
  locator: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv;
    expected=3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f; observed=c19bfc848e1b410548614c54a2b99e2c58452d58aeb61f972c99fcb3039a1d24
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
  search_scope: Exact configured historical input path, including ignored files; retained
    actual receipt, not a new source search.
- evidence_id: strict-receipt
  kind: validation
  reference: just validate-strict data/taxa/archaea/archaeoglobus_fulgidus.yaml --out
    /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/strict-04.tsv
  accessed_at: '2026-10-20T07:29:47Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo;\
    \ started 2026-10-20T07:29:45Z, finished 2026-10-20T07:29:47Z, exit 0. This exact\
    \ generated YAML only; its captured bytes remain unchanged. Actual earlier per-target\
    \ invocation; the receipt retains its original cwd and times.\nValidating 1 files\
    \ with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0012/src/taxonmech/schema/taxonmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/strict-04.tsv"
  locator: This exact generated YAML only; its captured bytes remain unchanged. Actual
    earlier per-target invocation; the receipt retains its original cwd and times.
  snapshot_sha256: af88a00e9a4b2b43ba48a5c243d40ccb77a1f6f205ea7ba62065e8dea0885a46
- evidence_id: history-receipt
  kind: validation
  reference: just validate-history
  accessed_at: '2026-10-21T06:42:11Z'
  support: supports
  summary: 'Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo;
    started 2026-10-21T06:42:09Z, finished 2026-10-21T06:42:11Z, exit 0. All 18 standalone
    history records; the generated seed event was also inspected in this target. Actual
    native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
    cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.

    history links: 18 record(s), 0 invalid

    No issues found

    18 history record(s) valid against src/taxonmech/schema/history.yaml'
  locator: All 18 standalone history records; the generated seed event was also inspected
    in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
  snapshot_sha256: 98b39b3ec0f369362dd50578fb05797d78334edf5b6961dd70e82283af0ac3ca
- evidence_id: corpus-receipt
  kind: validation
  reference: just verify-corpus
  accessed_at: '2026-10-21T06:48:01Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo;\
    \ started 2026-10-21T06:42:09Z, finished 2026-10-21T06:48:01Z, exit 0. All 626,048\
    \ generated taxon YAMLs, not a focused approximation. Actual native gate execution\
    \ at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes\
    \ and terminal exit codes identify these runs. Expanded-corpus gate results are\
    \ represented only by the corresponding terminal receipts; running gates remain\
    \ unavailable in unsaved previews. Earlier unchanged-target strict receipts remain\
    \ explicitly historical; new review bundles still require individual validation/save/check.\n\
    uv run python scripts/verify_corpus.py \nexpected 626048 records, found 626048\
    \ on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces\
    \ exactly from data/raw/ and curation/seed_scope.tsv"
  locator: All 626,048 generated taxon YAMLs, not a focused approximation. Actual
    native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
    cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
  snapshot_sha256: 223185ba1237af69c7392ba3608374e92d93c219292d3303af5c06592b84b4e6
- evidence_id: products-receipt
  kind: validation
  reference: just validate-products
  accessed_at: '2026-10-21T07:19:10Z'
  support: supports
  summary: 'Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo;
    started 2026-10-21T06:42:09Z, finished 2026-10-21T07:19:10Z, exit 0. Full configured
    corpus scan for curator-added graph nodes; this target contains no causal graph.
    Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.

    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml


    id↔label correspondence summary:


    ✅ All id↔label pairs correspond.'
  locator: Full configured corpus scan for curator-added graph nodes; this target
    contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
  snapshot_sha256: 48dd07515706dc62199fc2205c4b0bfdd5750028037d9b800179f254d2f1eb07
- evidence_id: qc-receipt
  kind: validation
  reference: just qc
  accessed_at: '2026-10-21T07:50:51Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo;\
    \ started 2026-10-21T06:42:09Z, finished 2026-10-21T07:50:51Z, exit 0. Repository-wide\
    \ just qc, including native corpus-wide checks. Actual native gate execution at\
    \ base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes\
    \ and terminal exit codes identify these runs. Expanded-corpus gate results are\
    \ represented only by the corresponding terminal receipts; running gates remain\
    \ unavailable in unsaved previews. Earlier unchanged-target strict receipts remain\
    \ explicitly historical; new review bundles still require individual validation/save/check.\n\
    All checks passed!\n1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33)\n\
    Validating 626048 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0014/src/taxonmech/schema/taxonmech.yaml\n\
    \  files scanned:      626048\nexpected 626048 records, found 626048 on disk\n\
    pages/ is current\nSite publication: 530,946,096 bytes (budget 950,000,000)\n\
    626048 taxon records\n  NCBITAXON        626048\nAll TaxonMech quality gates passed.\n\
    \  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890\
    \ strains (not genome counts)\n  Related STRAININFO_DEPOSIT: 107277 strain-record\
    \ pairs, 106843 identifiers, 53890 strains (not genome counts)\n  Related NUCLEOTIDE_SEQUENCE:\
    \ 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)\n\
    LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809\
    \ records mapped, 324404579 genomes summed across record attestations (not deduplicated)\n\
    Causal graphs: 0 records (0 evidence-backed edges)\n\nAll TaxonMech quality gates\
    \ passed."
  locator: Repository-wide just qc, including native corpus-wide checks. Actual native
    gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd,
    times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
  snapshot_sha256: dcb3f98d5c8ce264240732733ca70a5b93ee3e818d03f809d428748abffefca3
assessments:
- assessment_id: strain-source-support
  area: evidence
  topic: Primary strain, deposit and accession assertions
  outcome: supported
  summary: 'BacDive 18096 identifies VC-16 with DSM 4304, ATCC 49558, JCM 9628 and
    NBRC 100126. Its primary taxonomy separates species 2234 and strain 224325. StrainInfo
    SI-ID46110 version 3 carries four corresponding eligible, available, non-deprecated,
    non-erroneous deposits (125019, 125018, 158734 and 339249). ATCC 49203/SI-DP125020
    is present in that source group but is absent from the local BacDive deposit list
    and is not imported. All five source sequences explicitly name DSM 4304/SI-DP125019;
    only GCA_000008665 is a genome, while AY354034, U66886, AJ575815 and X17237 remain
    nucleotide references. GTDB row RS_GCF_000008665.1 names whole DSM 4304 and explicitly
    carries GCA_000008665.1. Primary NCBI GenBank and RefSeq rows corroborate DSM
    4304/224325 and explicitly pair their .1 versions as identical in the pinned snapshot;
    these do not assign a version to the separately unversioned BacDive, GOLD and
    StrainInfo assertion. BV-BRC 224325.10 explicitly resolves to DSM 4304 and GCA_000008665.1.
    GOLD Go0000778 joins Gp0000778 to Ga0027554 and supplies unversioned GCA_000008665
    plus IMG638154502 through the inspected culture match. Three transcriptome projects
    under Go0015557 correctly provide typed sample/project context rather than genome
    links. Additional GOLD organism rows Go0620787 and Go0620788 match NBRC and JCM
    deposits without transferring DSM-only sequences. The species record additionally
    retains distinct DSM 4139 strain Z/BacDive18095, with SI-ID47796.2/SI-DP158661
    and no imported genomes, and DSM 8774 strain 7324/BacDive132693. All three are
    source-supported BacDive strains; two classified_as fields retain their descendant
    NCBI strain taxa rather than flattening strain identity into the species. kgmicrobe.strain:bacdive_18096:
    9 genome_assemblies assertions (3 distinct IDs), 6 genome_records assertions (3
    distinct IDs), 51 related_records assertions (27 distinct IDs). kgmicrobe.strain:bacdive_18095:
    0 genome_assemblies assertions (0 distinct IDs), 0 genome_records assertions (0
    distinct IDs), 2 related_records assertions (2 distinct IDs). kgmicrobe.strain:bacdive_132693:
    10 genome_assemblies assertions (3 distinct IDs), 8 genome_records assertions
    (4 distinct IDs), 22 related_records assertions (8 distinct IDs).'
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - record
  - bacdive-inventory
  - strain-primary-bacdive
  - strain-primary-straininfo
  - strain-primary-gold-organisms
  - strain-primary-gold-projects
  - strain-primary-gold-analyses
  - strain-gtdb-primary-1
  - strain-assembly-primary-1
  - strain-assembly-primary-2
  - strain-assembly-primary-3
  - strain-assembly-primary-4
  - strain-inventory-1
  - strain-inventory-2
  - strain-inventory-3
  - strain-inventory-4
  - strain-inventory-5
  - strain-inventory-6
  - strain-inventory-7
  - strain-policy
  - straininfo-policy
  - strain-cafi
  - strain-cafi-pin
  - strain-join-owner
  - straininfo-join-owner
  - strain-source-pin-bacdive
  - strain-source-pin-straininfo
  - strain-source-pin-gold
  - strain-source-pin-bvbrc
  dimensions:
  - name: deposit-authority
    value: DSM4304, ATCC49558, JCM9628, NBRC100126, DSM4139 and DSM8774 have supported
      whole-deposit keys. VC-16, Z and 7324 are designations, not the reviewed join
      keys. ATCC49203 is an eligible source deposit but is not carried in the local
      BacDive list and is not imported.
    definition: Pinned CAFI authority plus full accession match, distinct from bare
      labels and source group membership.
    evidence_ids:
    - strain-cafi
    - strain-cafi-pin
    - strain-join-owner
  - name: source-snapshot
    value: BacDive and StrainInfo September2026 captures; pinned primary GOLD workbook
      and NCBI/GTDB/BV-BRC catalogs; versions preserved.
    definition: Source-specific observations, not a claim of current worldwide resolution.
    evidence_ids:
    - strain-policy
    - straininfo-policy
    - strain-cafi
    - strain-cafi-pin
    - strain-join-owner
    - straininfo-join-owner
    - strain-source-pin-bacdive
    - strain-source-pin-straininfo
    - strain-source-pin-gold
    - strain-source-pin-bvbrc
  - name: assertion-units
    value: 'kgmicrobe.strain:bacdive_18096: 9 genome_assemblies assertions (3 distinct
      IDs), 6 genome_records assertions (3 distinct IDs), 51 related_records assertions
      (27 distinct IDs). kgmicrobe.strain:bacdive_18095: 0 genome_assemblies assertions
      (0 distinct IDs), 0 genome_records assertions (0 distinct IDs), 2 related_records
      assertions (2 distinct IDs). kgmicrobe.strain:bacdive_132693: 10 genome_assemblies
      assertions (3 distinct IDs), 8 genome_records assertions (4 distinct IDs), 22
      related_records assertions (8 distinct IDs).'
    definition: Assertions and distinct IDs are separate; neither counts unique biological
      genomes. SI, sample/project and nucleotide IDs remain outside genome counts.
    evidence_ids:
    - strain-inventory-1
    - strain-inventory-2
    - strain-inventory-3
    - strain-inventory-4
    - strain-inventory-5
    - strain-inventory-6
    - strain-inventory-7
- assessment_id: strain-nucleotide-conflict
  area: evidence
  topic: Source disagreement on AY354034
  outcome: concern
  summary: AY354034 is explicitly attached to DSM 4304/SI-DP125019 in StrainInfo,
    but its source description and captured current NCBI esummary identify Methanococcus
    aeolicus (NCBITaxon:42879), not Archaeoglobus fulgidus. The imported source description
    and typed nucleotide reference faithfully preserve that disagreement under docs/STRAININFO.md;
    this is not established as an extractor or seeder defect. Keep a qualified limitation
    and seek authoritative StrainInfo/INSDC reconciliation before treating AY354034
    as biological evidence about the Archaeoglobus strain.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - record
  - strain-primary-straininfo
  - straininfo-policy
  - straininfo-join-owner
  - strain-ay354034-authority
- assessment_id: current-source-identifiers
  area: evidence
  topic: Bounded current accession, sample/project and DOI identities
  outcome: supported
  summary: All 3 exact nested StrainInfo DOI version(s) resolve in DataCite with the
    correct SI-ID and version. All 6 asserted BioProject IDs and 5 BioSample IDs resolve
    at NCBI. Each BioSample explicitly retains the expected strain/taxon and primary
    BioProject link. PRJNA224116 resolves as the multispecies RefSeq annotation umbrella,
    preserving the qualified project-context interpretation. AJ575815, U66886 and
    X17237 independently resolve to Archaeoglobus fulgidus DSM 4304 (taxon224325);
    returned .1 versions do not alter their native unversioned source accessions.
    AY354034 remains a distinct unresolved source conflict.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - record
  - remaining-straininfo-doi-authority
  - remaining-bioproject-authority
  - remaining-biosample-authority
  - remaining-nuccore-authority
- assessment_id: identity
  area: identity
  topic: Exact taxon and source lineage
  outcome: supported
  summary: NCBITaxon:2234 denotes Archaeoglobus fulgidus at SPECIES rank beneath NCBITaxon:2233,
    genetic code 11. All 9 carried ancestors agree with the pinned inventory and captured
    official NCBI response; the response omits only the root entry. Source name classes
    remain distinct from taxon classification.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - scope-row
  - path-row
  dimensions:
  - name: native-rank
    value: SPECIES
    definition: Rank of this exact NCBI target, distinct from source species mappings
      and strain genome records.
    evidence_ids:
    - record
    - taxonomy-inventory
    - ncbi-live
- assessment_id: nomenclature
  area: nomenclature
  topic: Name classes and nomenclatural scope
  outcome: supported
  summary: Pinned LPSN row 15381, lpsn:773360, and current LPSN support Archaeoglobus
    fulgidus Stetter 1988, validly published ICNP correct name, and ATCC 49558 / DSM
    4304 / JCM 9628 / NBRC 100126 type deposits. Current NCBI preserves authority
    as a related name. DOI 10.1016/s0723-2020(88)80032-8 resolves to Stetter 1988
    effective publication; DOI 10.1099/00207713-38-3-328 is Validation List 26. X05567.1
    is the 16S RNA sequence of VC-16 / DSM 4304, taxid 224325. LPSN bridges the species
    to GTDB Archaeoglobus fulgidus. These nomenclatural checks do not assess every
    nested strain link.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - lpsn-inventory
  - mapping-policy
  - nomenclature-authority-1
  - nomenclature-authority-2
  - nomenclature-authority-3
  - nomenclature-authority-4
  - genome-catalog-1
  - gtdb-full-scan
- assessment_id: completeness
  area: completeness
  topic: Imported subtree and source assertion units
  outcome: supported
  summary: 'Complete direct reads of twelve source/scope/path tables, including ignored
    files, support 3 imported BacDive strains over the exact target subtree (2 descendant
    taxa). All imported counts agree with their own source units: NCBITAXON 1 NAME;
    LPSN 1 NAME; GTDB 6 GENOME; BACDIVE 3 STRAIN; MEDIADIVE 1 MEDIUM; GOLD 4 ORGANISM;
    MADIN 6 TRAIT_ASSERTION. Counts of organisms, media, traits and genome assertions
    are not interchangeable and do not prove phenotype or biological genome equivalence.
    The GTDB fulgidus cluster count 6 spans four NCBI taxids; it is not the number
    of this target''s own strain genomes.'
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - record
  - taxonomy-inventory
  - scope-row
  - path-row
  - bacdive-inventory
  - culture-inventory
  - gtdb-species
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
  - genome-catalog-1
- assessment_id: taxonomy-mapping
  area: grounding
  topic: Qualified species mapping and target scope
  outcome: supported
  summary: Pinned LPSN row 15381, lpsn:773360, and current LPSN support Archaeoglobus
    fulgidus Stetter 1988, validly published ICNP correct name, and ATCC 49558 / DSM
    4304 / JCM 9628 / NBRC 100126 type deposits. Current NCBI preserves authority
    as a related name. DOI 10.1016/s0723-2020(88)80032-8 resolves to Stetter 1988
    effective publication; DOI 10.1099/00207713-38-3-328 is Validation List 26. X05567.1
    is the 16S RNA sequence of VC-16 / DSM 4304, taxid 224325. LPSN bridges the species
    to GTDB Archaeoglobus fulgidus. These nomenclatural checks do not assess every
    nested strain link.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - record
  - gtdb-mappings
  - gtdb-species
  - mapping-policy
  - equivalence-contract
  - seed-owner
  - genome-catalog-1
  - gtdb-full-scan
  - nomenclature-authority-1
  - nomenclature-authority-2
  - nomenclature-authority-3
  - nomenclature-authority-4
- assessment_id: native-status
  area: provenance
  topic: Unchanged native status and history
  outcome: supported
  summary: EXACT grounding and SEEDED status agree with NCBI identity. The sole seed
    event at 2026-09-13T17:54:04Z equals the latest raw/ATB/StrainInfo extraction
    time; no native status/history was changed.
  target_ids:
  - NCBITaxon:2234
  evidence_ids:
  - record
  - manifest
  - overlay-manifests
  - scope-row
  - path-row
findings: []
actions:
- action_id: resolve-source-ay354034-conflict
  description: Reconcile the conflicting organism annotation for AY354034 through
    authoritative StrainInfo SI-ID46110/SI-DP125019 and INSDC evidence. Retain the
    source-association conflict until an authoritative correction or explicit source
    policy supports a change; do not hand-edit generated taxon YAML.
  finding_ids: []
  target_ids:
  - NCBITaxon:2234
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: data/straininfo/records.jsonl.gz
    role: Pinned source projection of SI-ID46110 and explicit SI-DP125019 sequence
      association; upstream correction needed before refresh
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/straininfo_links.py
    role: Maintains faithful same-deposit import boundary; no code defect established
  acceptance_checks:
  - Inspect the authoritative strain/deposit sequence path and INSDC accession annotation;
    distinguish taxonomy disagreement from exact deposit-link fidelity.
  - If an upstream record changes, capture a dated/hash-pinned source refresh and
    use separately authorized normal extraction and guarded seeding.
  - Preserve supplied accession versions and related-record typing; rerun native and
    structured review gates after any authorized update.
- action_id: recover-pinned-aggregate-inputs
  finding_ids: []
  target_ids:
  - NCBITaxon:2234
  description: Recover manifest-hash-matching original aggregate inputs and independently
    recount the exact target assertions through the maintained extractor; do not edit
    generated YAML.
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: data/raw/MANIFEST.yaml
    role: Original source hashes
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: Source-specific count semantics
  acceptance_checks:
  - Require exact original input SHA-256 before using it as historical evidence.
  - Recount only the exact target with each source's own assertion unit and compare
    to its pinned inventory row.
  - Record any discrepancy in a new review observation.
limitations:
- The review assesses exact identifiers, nomenclature, source placement and import
  completeness at the captured versions; it does not establish experimental phenotypes,
  assembly sequence equivalence or a phylogenetic species boundary.
- The original manifest-pinned aggregate source bytes were unavailable at the configured
  historical paths in retained hash observations. Inventory counts agree, but original
  aggregate-edge recounts remain unavailable; primary deposit chains do not replace
  those historical aggregates.
- AY354034 is explicitly attached to DSM 4304/SI-DP125019 in StrainInfo, but its source
  description and captured current NCBI esummary identify Methanococcus aeolicus (NCBITaxon:42879),
  not Archaeoglobus fulgidus. The imported source description and typed nucleotide
  reference faithfully preserve that disagreement under docs/STRAININFO.md; this is
  not established as an extractor or seeder defect. Keep a qualified limitation and
  seek authoritative StrainInfo/INSDC reconciliation before treating AY354034 as biological
  evidence about the Archaeoglobus strain.
- Source assertions, deposit identities and primary accession metadata were assessed
  at the captured snapshot versions. Their presence does not establish current culture
  availability, biological equivalence across databases or whole-paper experimental
  support.
- IMG2528311132 is supported by the BacDive132693 sequence row; no independent IMG
  record or GOLD analysis for that identifier was inspected.
- Current NCBI summaries verify the requested identifiers and reported taxon/strain
  context; they do not establish cross-database biological genome equivalence or experimentally
  validate metadata titles.
- The exact nested StrainInfo dataset DOI versions resolve at DataCite, but current
  availability of the physical cultures and the full contents of live deposit records
  were not independently checked.
- IMG identifiers retain inspected BacDive and, where present, GOLD source support;
  no direct IMG record response was inspected.
- AJ575815, U66886 and X17237 were verified through NCBI ESummary identity metadata;
  complete sequence records and gene function were not reassessed. The returned .1
  versions do not modify native unversioned assertions, and AY354034 remains the separately
  documented conflict.
- iModulonDB CLI unavailable in bounded checks; official public index inspected instead.
  No covered Archaeoglobus dataset was found at that capture; this is not negative
  phenotype or transcriptomic evidence.
- Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
  cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
  gate results are represented only by the corresponding terminal receipts; running
  gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts
  remain explicitly historical; new review bundles still require individual validation/save/check.
notes:
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base recapture preserves target/source-table bytes; five changed guidance/scope/path/seeder
  inputs were explicitly reassessed. Original captures and exact transition receipts
  remain retained.
- Every new bundle still requires its own validate/save/check recipe; baseline native
  receipts do not claim these later steps have run.
tags:
- record-review
- batch-0014
- archaea
- generated
- source-checked
```
