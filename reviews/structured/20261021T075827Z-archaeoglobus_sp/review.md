# Record review: Archaeoglobus sp.

- Review: 20261021T075827Z-archaeoglobus_sp
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-21T06:45:17Z
- Finished UTC: 2026-10-21T07:58:27Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Archaeoglobus sp. has supported exact NCBI identity and source-scoped representation. Four singleton GTDB notes overstate other-taxon membership.

## Scope And Provenance

Entire single generated record, including all source assertions and imported strains.

Selection: Batch-0015 target 3; next unreviewed path-order selection after excluding 195 actual covered target paths. Canonical record_review.py list over the 39-bundle current base and all fourteen actually saved branch worktrees, including ignored and hidden review bundles. Native corpus enumerated with os.walk including ignored/hidden files. Coverage only derives from explicit validated bundle targets, never inventories or reservations.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 01ca63effdf8c03a644df893ba6129b2d8448ea4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:1872626 | data/taxa/archaea/archaeoglobus_sp.yaml | generated | Archaeoglobus sp. |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact NCBI taxon, rank and lineage | passed | True | NCBITaxon:1872626 | NCBITaxon:1872626 denotes Archaeoglobus sp. at SPECIES rank beneath NCBITaxon:2643606, genetic code 11. All 10 carried lineage entries agree with the pinned NCBI inventory and captured official EFetch; EFetch omits only root by format. Source name classes remain separate from taxon classification. |
| Complete exact identifier and name inventory search | passed | True | NCBITaxon:1872626 | Complete direct reads of twelve source/scope/path tables, including ignored files, support 0 imported BacDive strains over the exact target subtree (0 descendant taxa). Exact counts agree with their own source units: NCBITAXON 1 NAME; GTDB 6 GENOME. Counts of media, traits, organisms and genome assertions are distinct and do not establish phenotype or genome equivalence. All six GTDB clusters are represented: primary count6 plus five additional clusters. Their pooled12 catalog members are not the primary count, and only six members carry target taxid1872626. Four clusters are singletons solely at this target; fulgidus and WYZ-LMO2 have other taxids. |
| Complete primary GTDB membership and source counts | passed | True | NCBITaxon:1872626 | Selected source cluster counts and source taxon/genome identities agree; separately recorded wording and rank-scope findings remain where applicable. |
| Imported strain links | not_applicable | False | NCBITaxon:1872626 | No imported BacDive strain or strain-level link is asserted; no deposit is inferred from an isolate designation. |
| Historical aggregate edges | not_applicable | False | NCBITaxon:1872626 | No historical medium, organism or trait aggregate asserted. |
| Native strict record validation | passed | True | NCBITaxon:1872626 | Actual terminal exit code 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. |
| Repository history validation | passed | True | NCBITaxon:1872626 | Actual terminal exit code 0. The complete standalone history population; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0015 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. |
| Full-corpus exact reproduction | passed | True | NCBITaxon:1872626 | Actual terminal exit code 0. All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0015 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. |
| Native product ID/label gate | passed | True | NCBITaxon:1872626 | Actual terminal exit code 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0015 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. |
| Authoritative complete quality gate | passed | True | NCBITaxon:1872626 | Actual terminal exit code 0. Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0015 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. 1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33) |

## Scientific And Domain Assessments

### Exact taxon and source lineage

identity: supported. Targets: NCBITaxon:1872626.

NCBITaxon:1872626 denotes Archaeoglobus sp. at SPECIES rank beneath NCBITaxon:2643606, genetic code 11. All 10 carried lineage entries agree with the pinned NCBI inventory and captured official EFetch; EFetch omits only root by format. Source name classes remain separate from taxon classification.

### Name classes and nomenclatural scope

nomenclature: supported. Targets: NCBITaxon:1872626.

Pinned/current NCBI retain the literal species-rank placeholder Archaeoglobus sp. with no source name-class synonyms. The LPSN fulgidus row found through a GTDB crosslink concerns taxid2234 and is not nomenclature for this placeholder.

### Imported subtree and source assertion units

completeness: supported. Targets: NCBITaxon:1872626.

Complete direct reads of twelve source/scope/path tables, including ignored files, support 0 imported BacDive strains over the exact target subtree (0 descendant taxa). Exact counts agree with their own source units: NCBITAXON 1 NAME; GTDB 6 GENOME. Counts of media, traits, organisms and genome assertions are distinct and do not establish phenotype or genome equivalence. All six GTDB clusters are represented: primary count6 plus five additional clusters. Their pooled12 catalog members are not the primary count, and only six members carry target taxid1872626. Four clusters are singletons solely at this target; fulgidus and WYZ-LMO2 have other taxids.

### Qualified species mapping and target scope

grounding: concern. Targets: NCBITaxon:1872626.

For each affected GTDB species the complete pinned census has one genome, ncbi_taxid and ncbi_species_taxid 1872626, and the entire reverse mapping inventory has only NCBITaxon:1872626. Archaeoglobus_fulgidus has six members and four reverse NCBI taxids; WYZ-LMO2_sp011605865 has two members and two reverse taxids, so their other-taxa wording is supported. The broadMatch pooling relationship itself is supported. Counts 6,2,1,1,1,1 are correct. The GTDB attestation is primary count 6 plus five further clusters, not pooled sum 12.

### Unchanged native status and history

provenance: supported. Targets: NCBITaxon:1872626.

EXACT grounding and SEEDED status preserve source state. The sole seed event at 2026-09-13T17:54:04Z equals the latest raw/ATB/StrainInfo extraction time. No native status/history was changed.

## Findings

### pooled-note-other-taxa: Four singleton GTDB notes incorrectly assert other NCBI taxa

minor / open / confirmed; issue key: gtdb-broadmatch-note-other-taxa-1872626.

For each affected GTDB species the complete pinned census has one genome, ncbi_taxid and ncbi_species_taxid 1872626, and the entire reverse mapping inventory has only NCBITaxon:1872626. Archaeoglobus_fulgidus has six members and four reverse NCBI taxids; WYZ-LMO2_sp011605865 has two members and two reverse taxids, so their other-taxa wording is supported. The broadMatch pooling relationship itself is supported. Counts 6,2,1,1,1,1 are correct. The GTDB attestation is primary count 6 plus five further clusters, not pooled sum 12.

## Recommended Actions And Acceptance Checks

### correct-pooled-mapping-note

Condition the other-NCBI-taxa clause on actual reverse mapping evidence, or use wording limited to the supported pooling direction. Retain all six broadMatch mappings and their correct cluster counts; regenerate through native gates.

- All four listed singleton notes omit unsupported other-taxa wording.
- Retain all six broadMatch mappings, primary count6 and five further clusters.
- Preserve supported mixed-taxid membership for fulgidus and WYZ-LMO2.
- Change maintained inputs only; after separately authorized guarded regeneration, run strict, history, product, corpus and QC gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/taxa/archaea/archaeoglobus_sp.yaml; entire TaxonRecord; identifier=NCBITaxon:1872626 | supports | Read the entire generated YAML, including identity, lineage, names, mappings, source attestations, all imported strains and links, and seed history. |
| taxonomy-inventory | data/raw/ncbitaxon_taxa.tsv; line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""}; line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"}; line 1755: {"taxon_id":"NCBITaxon:2231","label":"Archaeoglobales","rank":"ORDER","parent_id":"NCBITaxon:183980"}; line 1756: {"taxon_id":"NCBITaxon:2232","label":"Archaeoglobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2231"}; line 1757: {"taxon_id":"NCBITaxon:2233","label":"Archaeoglobus","rank":"GENUS","parent_id":"NCBITaxon:2232"}; line 2981: {"taxon_id":"NCBITaxon:28890","label":"Methanobacteriota","rank":"PHYLUM","parent_id":"NCBITaxon:3366610"}; line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"}; line 36620: {"taxon_id":"NCBITaxon:183980","label":"Archaeoglobi","rank":"CLASS","parent_id":"NCBITaxon:28890"}; line 489383: {"taxon_id":"NCBITaxon:1872626","label":"Archaeoglobus sp.","rank":"SPECIES","parent_id":"NCBITaxon:2643606","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb","retired_into":"","taxonomy_snapshot":"2026-09-13"}; line 539688: {"taxon_id":"NCBITaxon:2643606","label":"unclassified Archaeoglobus","rank":"NO_RANK","parent_id":"NCBITaxon:2233"}; line 621140: {"taxon_id":"NCBITaxon:3366610","label":"Methanobacteriati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"} | supports | Inspected the target and each carried ancestor, rank, parent, genetic code and source name classes. |
| scope-row | curation/seed_scope.tsv; line 80135: {"identifier":"NCBITaxon:1872626","added":"2026-09-13","reason":"attested rule: Archaeoglobus sp., 2 sources incl. NCBI"} | supports | Exact target is included in the declared seed scope. |
| path-row | data/taxa/PATHS.tsv; line 296840: {"identifier":"NCBITaxon:1872626","slug":"archaeoglobus_sp"} | supports | Indexed path resolves to this exact NCBI taxon. |
| ncbi-live | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=84156,572546,1872626,403220,1748302,669409,669410,1934979,1934980,1934981&amp;retmode=xml; TaxaSet/Taxon[TaxId='1872626']; ten-target captured response | supports | Inspected the official response for this exact taxon: scientific name, rank, parent, source name classes, lineage and genetic code. Current authority and pinned September inventory remain distinct observations. |
| lpsn-inventory | data/raw/lpsn_names.tsv; line 15381: {"lpsn_id":"lpsn:773360","name":"Archaeoglobus fulgidus","rank":"SPECIES","authority":"Stetter 1988","url":"https://lpsn.dsmz.de/species/archaeoglobus-fulgidus","deprecated":"0","status":"legitimate=True; validly published under the ICNP; correct name","validly_published":"1","legitimate":"1","is_correct_name":"1","parent_lpsn_id":"lpsn:516970","ncbitaxon_ids":"NCBITaxon:2234","gtdb_ids":"GTDB:s__Archaeoglobus_fulgidus","type_strain_ids":"kgmicrobe.strain:ATCC-49558&#124;kgmicrobe.strain:DSM-4304&#124;kgmicrobe.strain:JCM-9628&#124;kgmicrobe.strain:NBRC-100126","synonym_of":"","synonyms":"","publications":"doi:10.1016/s0723-2020(88)80032-8&#124;doi:10.1099/00207713-38-3-328","sequence_accessions":"INSDC:X05567"} | supports | Inspected exact mapped and linked LPSN names; bounded inventory absence does not establish worldwide nomenclatural absence. |
| gtdb-mappings | data/raw/gtdb_mappings.tsv; line 20129: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1344584","predicate":"skos:closeMatch","genome_count":"6"}; line 72201: {"gtdb_id":"GTDB:s__Archaeoglobus_A_sp017656505","gtdb_label":"s__Archaeoglobus_A_sp017656505","gtdb_parent":"GTDB:g__Archaeoglobus_A","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"}; line 72202: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"6"}; line 72203: {"gtdb_id":"GTDB:s__Archaeoglobus_sp017656475","gtdb_label":"s__Archaeoglobus_sp017656475","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"}; line 72204: {"gtdb_id":"GTDB:s__Archaeoglobus_sp036742095","gtdb_label":"s__Archaeoglobus_sp036742095","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"}; line 72205: {"gtdb_id":"GTDB:s__WAPX01_sp003978865","gtdb_label":"s__WAPX01_sp003978865","gtdb_parent":"GTDB:g__WAPX01","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"}; line 72206: {"gtdb_id":"GTDB:s__WYZ-LMO2_sp011605865","gtdb_label":"s__WYZ-LMO2_sp011605865","gtdb_parent":"GTDB:g__WYZ-LMO2","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"2"}; line 177020: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:2234","predicate":"skos:closeMatch","genome_count":"6"}; line 177993: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:224325","predicate":"skos:closeMatch","genome_count":"6"}; line 178159: {"gtdb_id":"GTDB:s__WYZ-LMO2_sp011605865","gtdb_label":"s__WYZ-LMO2_sp011605865","gtdb_parent":"GTDB:g__WYZ-LMO2","ncbitaxon_id":"NCBITaxon:2250258","predicate":"skos:broadMatch","genome_count":"2"} | supports | Inspected direct mappings and selected clusters' reverse mappings, retaining each source predicate and taxon boundary. |
| gtdb-species | data/raw/gtdb_species.tsv; line 12295: {"gtdb_id":"GTDB:s__Archaeoglobus_A_sp017656505","label":"s__Archaeoglobus_A_sp017656505","parent":"GTDB:g__Archaeoglobus_A","genome_count":"1"}; line 12308: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","label":"s__Archaeoglobus_fulgidus","parent":"GTDB:g__Archaeoglobus","genome_count":"6"}; line 12311: {"gtdb_id":"GTDB:s__Archaeoglobus_sp017656475","label":"s__Archaeoglobus_sp017656475","parent":"GTDB:g__Archaeoglobus","genome_count":"1"}; line 12316: {"gtdb_id":"GTDB:s__Archaeoglobus_sp036742095","label":"s__Archaeoglobus_sp036742095","parent":"GTDB:g__Archaeoglobus","genome_count":"1"}; line 196735: {"gtdb_id":"GTDB:s__WAPX01_sp003978865","label":"s__WAPX01_sp003978865","parent":"GTDB:g__WAPX01","genome_count":"1"}; line 198200: {"gtdb_id":"GTDB:s__WYZ-LMO2_sp011605865","label":"s__WYZ-LMO2_sp011605865","parent":"GTDB:g__WYZ-LMO2","genome_count":"2"} | supports | Inspected source species identifiers, labels, parent clusters and genome counts. |
| bacdive-inventory | data/raw/bacdive_strains.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Complete inventory selection covers the exact target and descendants from the complete NCBI parent graph; its imported strain population was compared with the complete YAML. |
| culture-inventory | data/raw/culture_collection_strains.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected exact culture-inventory associations; an isolate name or genome does not create an inferred deposit. |
| gold-organisms | data/raw/gold_organisms.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact GOLD organism count row or bounded absence, without converting counts to phenotypes. |
| mediadive-taxa | data/raw/mediadive_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact MediaDive medium count row or bounded absence, without converting counts to phenotypes. |
| madin-taxa | data/raw/madin_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact Madin trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| bactotraits-taxa | data/raw/bactotraits_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact BactoTraits trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| mapping-policy | docs/HARMONIZATION.md; Mapping predicates; Which strains belong to a record | supports | Policy permits one-to-one species closeMatch normalization and LPSN-linked species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage unchanged. |
| equivalence-contract | src/taxonmech/schema/taxonmech.yaml; TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439 | supports | TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes under the source taxon. |
| seed-owner | src/taxonmech/seed.py; GTDB mapping construction lines 444–476; LPSN/type-strain and source-attestation construction | supports | Inspected mapping ranking, qualified predicates, fixed broadMatch wording, synonym/xref construction, primary cluster counts and same-taxon type-strain derivation. |
| manifest | data/raw/MANIFEST.yaml; kg_microbe_source, inputs, extracted_at | supports | Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd, upstream input hashes and extraction time 2026-09-13T17:50:44Z. |
| overlay-manifests | data/atb/MANIFEST.yaml; extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml | supports | Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z, matching the sole seed event. StrainInfo manifest is independently captured in source.inputs. |
| genome-catalog-1 | data/catalog/gtdb_genomes-0017.jsonl.gz; line 29518: {"accession":"GB_GCA_003978865.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WAPX01;s__WAPX01 sp003978865","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM397886v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA454888","ncbi_biosample":"SAMN09407821","ncbi_contig_count":"97","ncbi_contig_n50":"17226","ncbi_country":"Pacific Ocean: Mariana Back-Arc Basin vent fields","ncbi_date":"2018-12-28","ncbi_genbank_assembly_accession":"GCA_003978865.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"MAG 85","ncbi_isolation_source":"hydrothermal vent","ncbi_lat_lon":"16.96131294 N 144.8678188 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"2","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2018-12-28","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1872626","ncbi_ssu_count":"1","ncbi_strain_identifiers":"MAG 85","ncbi_submitter":"WHOI","ncbi_taxid":"1872626","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__unclassified Archaeoglobus;s__Archaeoglobus sp.","ncbi_total_gap_length":"0","ncbi_total_length":"1106720","ncbi_translation_table":"11","ncbi_trna_count":"34","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1106720","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"QNXS00000000.1"}; line 30338: {"accession":"RS_GCF_900069765.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM90006976v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMEA3879005","ncbi_contig_count":"206","ncbi_contig_n50":"67601","ncbi_country":"none","ncbi_date":"2016-09-20","ncbi_genbank_assembly_accession":"GCA_900069765.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"Archaeoglobus_fulgidus_oil","ncbi_isolation_source":"formation liquid","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus fulgidus","ncbi_protein_count":"2335","ncbi_refseq_category":"na","ncbi_rrna_count":"4","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2016-09-20","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2234","ncbi_ssu_count":"2","ncbi_strain_identifiers":"Archaeoglobus_fulgidus_oil","ncbi_submitter":"NTNU","ncbi_taxid":"2234","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_total_gap_length":"0","ncbi_total_length":"2036821","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2036821","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"FJNF00000000.1"}; line 30980: {"accession":"GB_GCA_001508745.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM150874v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA278302","ncbi_biosample":"SAMN03445115","ncbi_contig_count":"99","ncbi_contig_n50":"34454","ncbi_country":"none","ncbi_date":"2016-01-08","ncbi_genbank_assembly_accession":"GCA_001508745.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"49_95","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus fulgidus","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"0","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2016-01-08","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2234","ncbi_ssu_count":"0","ncbi_strain_identifiers":"49_95","ncbi_submitter":"Lawrence Berkeley National Lab","ncbi_taxid":"2234","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_total_gap_length":"0","ncbi_total_length":"2037571","ncbi_translation_table":"11","ncbi_trna_count":"0","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2037571","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"LGEQ00000000.1"}; line 37279: {"accession":"GB_GCA_017656505.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus_A;s__Archaeoglobus_A sp017656505","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM1765650v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA635695","ncbi_biosample":"SAMN15049708","ncbi_contig_count":"95","ncbi_contig_n50":"44138","ncbi_country":"Mexico: Guaymas Basin","ncbi_date":"2021-04-01","ncbi_genbank_assembly_accession":"GCA_017656505.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"GB_MAG3_049","ncbi_isolation_source":"deep sea sediment sample 4871-20 in thermophilic enrichment culture","ncbi_lat_lon":"27.04618 N 111.38483 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2021-04-01","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1872626","ncbi_ssu_count":"1","ncbi_strain_identifiers":"GB_MAG3_049","ncbi_submitter":"Marine Biological Laboratory","ncbi_taxid":"1872626","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__unclassified Archaeoglobus;s__Archaeoglobus sp.","ncbi_total_gap_length":"0","ncbi_total_length":"2524501","ncbi_translation_table":"11","ncbi_trna_count":"44","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2524501","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JACDNU000000000.1"}; line 40690: {"accession":"RS_GCF_017656475.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus sp017656475","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM1765647v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN15049707","ncbi_contig_count":"92","ncbi_contig_n50":"48438","ncbi_country":"Mexico: Guaymas Basin","ncbi_date":"2021-04-01","ncbi_genbank_assembly_accession":"GCA_017656475.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"GB_MAG2_100","ncbi_isolation_source":"deep sea sediment sample 4871-20 in thermophilic enrichment culture","ncbi_lat_lon":"27.04618 N 111.38483 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2021-04-01","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1872626","ncbi_ssu_count":"1","ncbi_strain_identifiers":"GB_MAG2_100","ncbi_submitter":"Marine Biological Laboratory","ncbi_taxid":"1872626","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__unclassified Archaeoglobus;s__Archaeoglobus sp.","ncbi_total_gap_length":"0","ncbi_total_length":"2039628","ncbi_translation_table":"11","ncbi_trna_count":"42","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2039628","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JACDNT000000000.1"}; line 43481: {"accession":"GB_GCA_020833165.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2 sp011605865","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2083316v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA568220","ncbi_biosample":"SAMN18938186","ncbi_contig_count":"104","ncbi_contig_n50":"22329","ncbi_country":"USA: Yellowstone National Park; GGS063 Spring","ncbi_date":"2021-11-10","ncbi_genbank_assembly_accession":"GCA_020833165.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"Bin S27","ncbi_isolation_source":"Sediments from shelf","ncbi_lat_lon":"44.69047 N 110.72917 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2021-11-10","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1872626","ncbi_ssu_count":"1","ncbi_strain_identifiers":"Bin S27","ncbi_submitter":"DOE Joint Genome Institute","ncbi_taxid":"1872626","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__unclassified Archaeoglobus;s__Archaeoglobus sp.","ncbi_total_gap_length":"0","ncbi_total_length":"1399988","ncbi_translation_table":"11","ncbi_trna_count":"43","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1399988","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAJHQV000000000.1"}; line 45270: {"accession":"RS_GCF_029982885.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2998288v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN33401081","ncbi_contig_count":"121","ncbi_contig_n50":"21098","ncbi_country":"USA: Colorado","ncbi_date":"2023-05-11","ncbi_genbank_assembly_accession":"GCA_029982885.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"DJKA110_ANT-KO_bin.46","ncbi_isolation_source":"Produced fluids from hydraulically fractured shales","ncbi_lat_lon":"40.411582 N 104.348363 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"2","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-05-11","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1872626","ncbi_ssu_count":"0","ncbi_strain_identifiers":"DJKA110_ANT-KO_bin.46","ncbi_submitter":"The Ohio State University","ncbi_taxid":"1872626","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__unclassified Archaeoglobus;s__Archaeoglobus sp.","ncbi_total_gap_length":"0","ncbi_total_length":"1934538","ncbi_translation_table":"11","ncbi_trna_count":"44","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1934538","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JARRCC000000000.1"}; line 46580: {"accession":"GB_GCA_036742095.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus sp036742095","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM3674209v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA843551","ncbi_biosample":"SAMN28746634","ncbi_contig_count":"503","ncbi_contig_n50":"5343","ncbi_country":"none","ncbi_date":"2024-02-21","ncbi_genbank_assembly_accession":"GCA_036742095.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"CTOTU24189","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobus sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"311","ncbi_scaffold_l50":"77","ncbi_scaffold_n50":"7275","ncbi_scaffold_n75":"4199","ncbi_scaffold_n90":"2702","ncbi_seq_rel_date":"2024-02-21","ncbi_spanned_gaps":"192","ncbi_species_taxid":"1872626","ncbi_ssu_count":"none","ncbi_strain_identifiers":"CTOTU24189","ncbi_submitter":"Helmholtz Centre for Environmental Research - UFZ","ncbi_taxid":"1872626","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__unclassified Archaeoglobus;s__Archaeoglobus sp.","ncbi_total_gap_length":"9222","ncbi_total_length":"1718707","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1709485","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"DAINRD000000000.1"}; line 47261: {"accession":"GB_GCA_001508815.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM150881v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA278302","ncbi_biosample":"SAMN03445123","ncbi_contig_count":"153","ncbi_contig_n50":"19697","ncbi_country":"USA:Alaska; North Slope; Kuparuk formation","ncbi_date":"2016-01-08","ncbi_genbank_assembly_accession":"GCA_001508815.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"49_2300","ncbi_isolation_source":"oil reservoir sample K2","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus fulgidus","ncbi_protein_count":"2489","ncbi_refseq_category":"na","ncbi_rrna_count":"0","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2016-01-08","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2234","ncbi_ssu_count":"0","ncbi_strain_identifiers":"49_2300","ncbi_submitter":"Lawrence Berkeley National Lab","ncbi_taxid":"2234","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_total_gap_length":"0","ncbi_total_length":"2017823","ncbi_translation_table":"11","ncbi_trna_count":"0","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2017823","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"LGEX00000000.1"}; line 47600: {"accession":"RS_GCF_000734035.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Complete Genome","ncbi_assembly_name":"ASM73403v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN03081472","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"Norway","ncbi_date":"2014-07-28","ncbi_genbank_assembly_accession":"GCA_000734035.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"marine oilfield; North sea","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus fulgidus DSM 8774","ncbi_protein_count":"2565","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"2316287","ncbi_scaffold_n75":"2316287","ncbi_scaffold_n90":"2316287","ncbi_seq_rel_date":"2014-07-28","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2234","ncbi_ssu_count":"1","ncbi_strain_identifiers":"DSM 8774","ncbi_submitter":"University Bergen","ncbi_taxid":"1344584","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus;x__Archaeoglobus fulgidus DSM 8774","ncbi_total_gap_length":"0","ncbi_total_length":"2316287","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2316287","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"}; line 47637: {"accession":"GB_GCA_011605865.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2 sp011605865","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM1160586v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA604268","ncbi_biosample":"SAMN13964307","ncbi_contig_count":"45","ncbi_contig_n50":"41011","ncbi_country":"USA: Yellowstone National Park; Smokejumper3 Hot Spring","ncbi_date":"2020-03-22","ncbi_genbank_assembly_accession":"GCA_011605865.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SJ3.Bin61","ncbi_isolation_source":"sediments from hot spring shelf","ncbi_lat_lon":"44.41595 N 110.9558 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobales archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"2","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2020-03-22","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250258","ncbi_ssu_count":"1","ncbi_strain_identifiers":"SJ3.Bin61","ncbi_submitter":"Montana State University","ncbi_taxid":"2250258","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;x__unclassified Archaeoglobales;s__Archaeoglobales archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1269726","ncbi_translation_table":"11","ncbi_trna_count":"41","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1269726","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAAOZI000000000.1"}; line 48903: {"accession":"RS_GCF_000008665.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","gtdb_type_species_of_genus":"t","ncbi_assembly_level":"Complete Genome","ncbi_assembly_name":"ASM866v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN02603985","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"none","ncbi_date":"2000-12-01","ncbi_genbank_assembly_accession":"GCA_000008665.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus fulgidus DSM 4304","ncbi_protein_count":"2431","ncbi_refseq_category":"reference genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"2178400","ncbi_scaffold_n75":"2178400","ncbi_scaffold_n90":"2178400","ncbi_seq_rel_date":"2000-12-01","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2234","ncbi_ssu_count":"1","ncbi_strain_identifiers":"DSM 4304","ncbi_submitter":"TIGR","ncbi_taxid":"224325","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus;x__Archaeoglobus fulgidus DSM 4304","ncbi_total_gap_length":"0","ncbi_total_length":"2178400","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"assembly from type material","ncbi_ungapped_length":"2178400","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"} | supports | Inspected every selected primary GTDB row, exact taxid/species-taxid, culture identifiers and accession versions. Species membership alone is not strain identity. |
| gtdb-full-scan | data/catalog/MANIFEST.json; [{"gtdb_species_id":"GTDB:s__WAPX01_sp003978865","member_rows":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":29518,"accession":"GB_GCA_003978865.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WAPX01;s__WAPX01 sp003978865","ncbi_taxid":"1872626","ncbi_species_taxid":"1872626","ncbi_organism_name":"Archaeoglobus sp.","ncbi_strain_identifiers":"MAG 85","ncbi_isolate":"MAG 85","ncbi_genome_category":"derived from metagenome","ncbi_genbank_assembly_accession":"GCA_003978865.1","ncbi_biosample":"SAMN09407821","ncbi_bioproject":"PRJNA454888"}],"reverse_mapping_rows":[{"line":72205,"row":{"gtdb_id":"GTDB:s__WAPX01_sp003978865","gtdb_label":"s__WAPX01_sp003978865","gtdb_parent":"GTDB:g__WAPX01","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"}}],"species_inventory_rows":[{"line":196735,"row":{"gtdb_id":"GTDB:s__WAPX01_sp003978865","label":"s__WAPX01_sp003978865","parent":"GTDB:g__WAPX01","genome_count":"1"}}],"observed_member_count":1,"ncbi_taxids":["1872626"],"ncbi_species_taxids":["1872626"],"reverse_mapping_target_ids":["NCBITaxon:1872626"],"scientific_scope_assessment":"GTDB species cluster. Its genome membership and source reverse mappings are retained as qualified mapping evidence; membership alone does not establish NCBI taxon identity at every rank."},{"gtdb_species_id":"GTDB:s__Archaeoglobus_fulgidus","member_rows":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":30338,"accession":"RS_GCF_900069765.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxid":"2234","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus fulgidus","ncbi_strain_identifiers":"Archaeoglobus_fulgidus_oil","ncbi_isolate":"Archaeoglobus_fulgidus_oil","ncbi_genome_category":"none","ncbi_genbank_assembly_accession":"GCA_900069765.1","ncbi_biosample":"SAMEA3879005","ncbi_bioproject":"PRJNA224116"},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":30980,"accession":"GB_GCA_001508745.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxid":"2234","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus fulgidus","ncbi_strain_identifiers":"49_95","ncbi_isolate":"49_95","ncbi_genome_category":"derived from metagenome","ncbi_genbank_assembly_accession":"GCA_001508745.1","ncbi_biosample":"SAMN03445115","ncbi_bioproject":"PRJNA278302"},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":45270,"accession":"RS_GCF_029982885.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxid":"1872626","ncbi_species_taxid":"1872626","ncbi_organism_name":"Archaeoglobus sp.","ncbi_strain_identifiers":"DJKA110_ANT-KO_bin.46","ncbi_isolate":"DJKA110_ANT-KO_bin.46","ncbi_genome_category":"derived from metagenome","ncbi_genbank_assembly_accession":"GCA_029982885.1","ncbi_biosample":"SAMN33401081","ncbi_bioproject":"PRJNA224116"},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":47261,"accession":"GB_GCA_001508815.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxid":"2234","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus fulgidus","ncbi_strain_identifiers":"49_2300","ncbi_isolate":"49_2300","ncbi_genome_category":"derived from metagenome","ncbi_genbank_assembly_accession":"GCA_001508815.1","ncbi_biosample":"SAMN03445123","ncbi_bioproject":"PRJNA278302"},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":47600,"accession":"RS_GCF_000734035.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxid":"1344584","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus fulgidus DSM 8774","ncbi_strain_identifiers":"DSM 8774","ncbi_isolate":"na","ncbi_genome_category":"none","ncbi_genbank_assembly_accession":"GCA_000734035.1","ncbi_biosample":"SAMN03081472","ncbi_bioproject":"PRJNA224116"},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":48903,"accession":"RS_GCF_000008665.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus fulgidus","ncbi_taxid":"224325","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus fulgidus DSM 4304","ncbi_strain_identifiers":"DSM 4304","ncbi_isolate":"na","ncbi_genome_category":"none","ncbi_genbank_assembly_accession":"GCA_000008665.1","ncbi_biosample":"SAMN02603985","ncbi_bioproject":"PRJNA224116"}],"reverse_mapping_rows":[{"line":20129,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1344584","predicate":"skos:closeMatch","genome_count":"6"}},{"line":72202,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"6"}},{"line":177020,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:2234","predicate":"skos:closeMatch","genome_count":"6"}},{"line":177993,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:224325","predicate":"skos:closeMatch","genome_count":"6"}}],"species_inventory_rows":[{"line":12308,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","label":"s__Archaeoglobus_fulgidus","parent":"GTDB:g__Archaeoglobus","genome_count":"6"}}],"observed_member_count":6,"ncbi_taxids":["1344584","1872626","2234","224325"],"ncbi_species_taxids":["1872626","2234"],"reverse_mapping_target_ids":["NCBITaxon:1344584","NCBITaxon:1872626","NCBITaxon:2234","NCBITaxon:224325"],"scientific_scope_assessment":"GTDB species cluster. Its genome membership and source reverse mappings are retained as qualified mapping evidence; membership alone does not establish NCBI taxon identity at every rank."},{"gtdb_species_id":"GTDB:s__Archaeoglobus_A_sp017656505","member_rows":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":37279,"accession":"GB_GCA_017656505.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus_A;s__Archaeoglobus_A sp017656505","ncbi_taxid":"1872626","ncbi_species_taxid":"1872626","ncbi_organism_name":"Archaeoglobus sp.","ncbi_strain_identifiers":"GB_MAG3_049","ncbi_isolate":"GB_MAG3_049","ncbi_genome_category":"derived from metagenome","ncbi_genbank_assembly_accession":"GCA_017656505.1","ncbi_biosample":"SAMN15049708","ncbi_bioproject":"PRJNA635695"}],"reverse_mapping_rows":[{"line":72201,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_A_sp017656505","gtdb_label":"s__Archaeoglobus_A_sp017656505","gtdb_parent":"GTDB:g__Archaeoglobus_A","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"}}],"species_inventory_rows":[{"line":12295,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_A_sp017656505","label":"s__Archaeoglobus_A_sp017656505","parent":"GTDB:g__Archaeoglobus_A","genome_count":"1"}}],"observed_member_count":1,"ncbi_taxids":["1872626"],"ncbi_species_taxids":["1872626"],"reverse_mapping_target_ids":["NCBITaxon:1872626"],"scientific_scope_assessment":"GTDB species cluster. Its genome membership and source reverse mappings are retained as qualified mapping evidence; membership alone does not establish NCBI taxon identity at every rank."},{"gtdb_species_id":"GTDB:s__Archaeoglobus_sp017656475","member_rows":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":40690,"accession":"RS_GCF_017656475.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus sp017656475","ncbi_taxid":"1872626","ncbi_species_taxid":"1872626","ncbi_organism_name":"Archaeoglobus sp.","ncbi_strain_identifiers":"GB_MAG2_100","ncbi_isolate":"GB_MAG2_100","ncbi_genome_category":"derived from metagenome","ncbi_genbank_assembly_accession":"GCA_017656475.1","ncbi_biosample":"SAMN15049707","ncbi_bioproject":"PRJNA224116"}],"reverse_mapping_rows":[{"line":72203,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_sp017656475","gtdb_label":"s__Archaeoglobus_sp017656475","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"}}],"species_inventory_rows":[{"line":12311,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_sp017656475","label":"s__Archaeoglobus_sp017656475","parent":"GTDB:g__Archaeoglobus","genome_count":"1"}}],"observed_member_count":1,"ncbi_taxids":["1872626"],"ncbi_species_taxids":["1872626"],"reverse_mapping_target_ids":["NCBITaxon:1872626"],"scientific_scope_assessment":"GTDB species cluster. Its genome membership and source reverse mappings are retained as qualified mapping evidence; membership alone does not establish NCBI taxon identity at every rank."},{"gtdb_species_id":"GTDB:s__WYZ-LMO2_sp011605865","member_rows":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":43481,"accession":"GB_GCA_020833165.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2 sp011605865","ncbi_taxid":"1872626","ncbi_species_taxid":"1872626","ncbi_organism_name":"Archaeoglobus sp.","ncbi_strain_identifiers":"Bin S27","ncbi_isolate":"Bin S27","ncbi_genome_category":"derived from metagenome","ncbi_genbank_assembly_accession":"GCA_020833165.1","ncbi_biosample":"SAMN18938186","ncbi_bioproject":"PRJNA568220"},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":47637,"accession":"GB_GCA_011605865.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2 sp011605865","ncbi_taxid":"2250258","ncbi_species_taxid":"2250258","ncbi_organism_name":"Archaeoglobales archaeon","ncbi_strain_identifiers":"SJ3.Bin61","ncbi_isolate":"SJ3.Bin61","ncbi_genome_category":"derived from metagenome","ncbi_genbank_assembly_accession":"GCA_011605865.1","ncbi_biosample":"SAMN13964307","ncbi_bioproject":"PRJNA604268"}],"reverse_mapping_rows":[{"line":72206,"row":{"gtdb_id":"GTDB:s__WYZ-LMO2_sp011605865","gtdb_label":"s__WYZ-LMO2_sp011605865","gtdb_parent":"GTDB:g__WYZ-LMO2","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"2"}},{"line":178159,"row":{"gtdb_id":"GTDB:s__WYZ-LMO2_sp011605865","gtdb_label":"s__WYZ-LMO2_sp011605865","gtdb_parent":"GTDB:g__WYZ-LMO2","ncbitaxon_id":"NCBITaxon:2250258","predicate":"skos:broadMatch","genome_count":"2"}}],"species_inventory_rows":[{"line":198200,"row":{"gtdb_id":"GTDB:s__WYZ-LMO2_sp011605865","label":"s__WYZ-LMO2_sp011605865","parent":"GTDB:g__WYZ-LMO2","genome_count":"2"}}],"observed_member_count":2,"ncbi_taxids":["1872626","2250258"],"ncbi_species_taxids":["1872626","2250258"],"reverse_mapping_target_ids":["NCBITaxon:1872626","NCBITaxon:2250258"],"scientific_scope_assessment":"GTDB species cluster. Its genome membership and source reverse mappings are retained as qualified mapping evidence; membership alone does not establish NCBI taxon identity at every rank."},{"gtdb_species_id":"GTDB:s__Archaeoglobus_sp036742095","member_rows":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":46580,"accession":"GB_GCA_036742095.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus sp036742095","ncbi_taxid":"1872626","ncbi_species_taxid":"1872626","ncbi_organism_name":"Archaeoglobus sp.","ncbi_strain_identifiers":"CTOTU24189","ncbi_isolate":"CTOTU24189","ncbi_genome_category":"derived from metagenome","ncbi_genbank_assembly_accession":"GCA_036742095.1","ncbi_biosample":"SAMN28746634","ncbi_bioproject":"PRJNA843551"}],"reverse_mapping_rows":[{"line":72204,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_sp036742095","gtdb_label":"s__Archaeoglobus_sp036742095","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"}}],"species_inventory_rows":[{"line":12316,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_sp036742095","label":"s__Archaeoglobus_sp036742095","parent":"GTDB:g__Archaeoglobus","genome_count":"1"}}],"observed_member_count":1,"ncbi_taxids":["1872626"],"ncbi_species_taxids":["1872626"],"reverse_mapping_target_ids":["NCBITaxon:1872626"],"scientific_scope_assessment":"GTDB species cluster. Its genome membership and source reverse mappings are retained as qualified mapping evidence; membership alone does not establish NCBI taxon identity at every rank."}] | supports | All nineteen pinned GTDB shards were searched with exact terminal species tokens preserving internal genus suffix underscores. Selected cluster counts, reverse mappings and taxon distributions were assessed separately from synonym/xref promotion. |
| finding-deduplication | Owned review worktrees structured bundles; {"keys":["gtdb-broadmatch-note-other-taxa-1872626"],"matches":{"gtdb-broadmatch-note-other-taxa-1872626":[]},"unique_review_ids":169} | supports | No existing target-specific finding with these stable keys was found in the bounded ignored-inclusive search at the recorded time. |
| native-gate-reuse | /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0015/native-gate-reuse.json; base, native_inputs_unchanged, source_directory, gates, input_proof_path and input_proof_sha256 | supports | Retained explicit verification of identical base/native inputs authorizes historical native-gate reuse; original command receipts remain separately cited. |
| strict-receipt | just validate-strict data/taxa/archaea/archaeoglobus_sp.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0015/strict-03.tsv; This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0015/repo; started 2026-10-21T06:45:23Z, finished 2026-10-21T06:45:24Z, exit 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times.<br>Validating 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0014/src/taxonmech/schema/taxonmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0015/strict-03.tsv |
| history-receipt | just validate-history; The complete standalone history population; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0015 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T06:42:11Z, exit 0. The complete standalone history population; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0015 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check.<br>history links: 18 record(s), 0 invalid<br>No issues found<br>18 history record(s) valid against src/taxonmech/schema/history.yaml |
| corpus-receipt | just verify-corpus; All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0015 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T06:48:01Z, exit 0. All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0015 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check.<br>uv run python scripts/verify_corpus.py <br>expected 626048 records, found 626048 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ and curation/seed_scope.tsv |
| products-receipt | just validate-products; Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0015 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T07:19:10Z, exit 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0015 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check.<br>uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml<br><br>id↔label correspondence summary:<br><br>✅ All id↔label pairs correspond. |
| qc-receipt | just qc; Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0015 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T07:50:51Z, exit 0. Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0015 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check.<br>All checks passed!<br>1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33)<br>Validating 626048 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0014/src/taxonmech/schema/taxonmech.yaml<br>  files scanned:      626048<br>expected 626048 records, found 626048 on disk<br>pages/ is current<br>Site publication: 530,946,096 bytes (budget 950,000,000)<br>626048 taxon records<br>  NCBITAXON        626048<br>All TaxonMech quality gates passed.<br>  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890 strains (not genome counts)<br>  Related STRAININFO_DEPOSIT: 107277 strain-record pairs, 106843 identifiers, 53890 strains (not genome counts)<br>  Related NUCLEOTIDE_SEQUENCE: 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)<br>LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809 records mapped, 324404579 genomes summed across record attestations (not deduplicated)<br>Causal graphs: 0 records (0 evidence-backed edges)<br><br>All TaxonMech quality gates passed. |

## Limits And Additional Notes

- Assessment is bounded to the exact target and captured source versions; identifier and metadata checks do not establish experimental phenotypes, sequence equivalence or phylogenetic species boundaries.
- Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0015 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check.
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base source transitions are verified against retained original captures and exact changed-input receipts.
- Every new bundle still requires its own validate/save/check recipe; historical native receipts do not claim these later steps have run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T075827Z-archaeoglobus_sp
kind: record
repository: CultureBotAI/TaxonMech
title: 'Record review: Archaeoglobus sp.'
started_at: '2026-10-21T06:45:17Z'
finished_at: '2026-10-21T07:58:27Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: The reviewer did not author the existing generated target; this
    review changes only new review artifacts in an isolated checkout.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Archaeoglobus sp. has supported exact NCBI identity and source-scoped representation.
  Four singleton GTDB notes overstate other-taxon membership.
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
  - path: data/straininfo/MANIFEST.yaml
    sha256: 25dd601c8cf6d4d84e5cc756d1e642ebef89f565bd31967152bf0026fa072847
    role: context
  - path: data/taxa/PATHS.tsv
    sha256: f8f2e0721cb6839b30530b44be0d3004b9f0e6e2d4be8736f235b10117a8bd99
    role: context
  - path: data/taxa/archaea/archaeoglobus_sp.yaml
    sha256: e63785714adadc18731b62c87d73aa9b300dd17c616d067ae22476fd31386443
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
  - path: src/taxonmech/extract.py
    sha256: 7c5b5bf385e0c060f1cb3dbac304d05ddb941e4c83c900017a04133efd6d1822
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
scope:
  description: Entire single generated record, including all source assertions and
    imported strains.
  selection: Batch-0015 target 3; next unreviewed path-order selection after excluding
    195 actual covered target paths. Canonical record_review.py list over the 39-bundle
    current base and all fourteen actually saved branch worktrees, including ignored
    and hidden review bundles. Native corpus enumerated with os.walk including ignored/hidden
    files. Coverage only derives from explicit validated bundle targets, never inventories
    or reservations.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - NCBITaxon:1872626
targets:
- target_id: NCBITaxon:1872626
  path: data/taxa/archaea/archaeoglobus_sp.yaml
  label: Archaeoglobus sp.
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
  summary: NCBITaxon:1872626 denotes Archaeoglobus sp. at SPECIES rank beneath NCBITaxon:2643606,
    genetic code 11. All 10 carried lineage entries agree with the pinned NCBI inventory
    and captured official EFetch; EFetch omits only root by format. Source name classes
    remain separate from taxon classification.
  target_ids:
  - NCBITaxon:1872626
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
    files, support 0 imported BacDive strains over the exact target subtree (0 descendant
    taxa). Exact counts agree with their own source units: NCBITAXON 1 NAME; GTDB
    6 GENOME. Counts of media, traits, organisms and genome assertions are distinct
    and do not establish phenotype or genome equivalence. All six GTDB clusters are
    represented: primary count6 plus five additional clusters. Their pooled12 catalog
    members are not the primary count, and only six members carry target taxid1872626.
    Four clusters are singletons solely at this target; fulgidus and WYZ-LMO2 have
    other taxids.'
  target_ids:
  - NCBITaxon:1872626
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
  - gtdb-full-scan
  scope_note: Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs.
- check_id: gtdb-primary-counts
  name: Complete primary GTDB membership and source counts
  status: passed
  required: true
  summary: Selected source cluster counts and source taxon/genome identities agree;
    separately recorded wording and rank-scope findings remain where applicable.
  target_ids:
  - NCBITaxon:1872626
  evidence_ids:
  - gtdb-full-scan
  - gtdb-species
  - gtdb-mappings
  - genome-catalog-1
  scope_note: All nineteen pinned shards and exact selected cluster/reverse-mapping
    populations; explicit genome selection where the native record has no taxon-level
    GTDB mapping.
- check_id: strain-genome-evidence
  name: Imported strain links
  status: not_applicable
  required: false
  summary: No imported BacDive strain or strain-level link is asserted; no deposit
    is inferred from an isolate designation.
  target_ids:
  - NCBITaxon:1872626
  evidence_ids:
  - record
  - bacdive-inventory
  - culture-inventory
- check_id: historical-source-counts
  name: Historical aggregate edges
  status: not_applicable
  required: false
  summary: No historical medium, organism or trait aggregate asserted.
  target_ids:
  - NCBITaxon:1872626
  evidence_ids:
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
- check_id: strict
  name: Native strict record validation
  status: passed
  required: true
  summary: Actual terminal exit code 0. This exact generated YAML only; its captured
    bytes remain unchanged. Actual earlier per-target invocation; the receipt retains
    its original cwd and times.
  target_ids:
  - NCBITaxon:1872626
  evidence_ids:
  - strict-receipt
  command: just validate-strict data/taxa/archaea/archaeoglobus_sp.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0015/strict-03.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: This exact generated YAML only; its captured bytes remain unchanged.
    Actual earlier per-target invocation; the receipt retains its original cwd and
    times.
- check_id: history
  name: Repository history validation
  status: passed
  required: true
  summary: Actual terminal exit code 0. The complete standalone history population;
    the generated seed event was also inspected in this target. Actual native gate
    execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original
    cwd, times, commands, log hashes and terminal exit codes identify the executions.
    Reused repository-wide receipts require the explicit same-base/native-input certificate;
    these are historical runs, not new batch-0015 invocations. Missing terminal receipts
    or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts
    retain their original execution context. New review bundles still require individual
    validation/save/check.
  target_ids:
  - NCBITaxon:1872626
  evidence_ids:
  - history-receipt
  - native-gate-reuse
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  scope_note: The complete standalone history population; the generated seed event
    was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained original cwd, times, commands, log hashes and terminal exit codes identify
    the executions. Reused repository-wide receipts require the explicit same-base/native-input
    certificate; these are historical runs, not new batch-0015 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check.
- check_id: corpus
  name: Full-corpus exact reproduction
  status: passed
  required: true
  summary: Actual terminal exit code 0. All 626,048 generated taxon YAMLs, not a focused
    approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained original cwd, times, commands, log hashes and terminal exit codes identify
    the executions. Reused repository-wide receipts require the explicit same-base/native-input
    certificate; these are historical runs, not new batch-0015 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check.
  target_ids:
  - NCBITaxon:1872626
  evidence_ids:
  - corpus-receipt
  - native-gate-reuse
  command: just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  scope_note: All 626,048 generated taxon YAMLs, not a focused approximation. Actual
    native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
    original cwd, times, commands, log hashes and terminal exit codes identify the
    executions. Reused repository-wide receipts require the explicit same-base/native-input
    certificate; these are historical runs, not new batch-0015 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check.
- check_id: products
  name: Native product ID/label gate
  status: passed
  required: true
  summary: Actual terminal exit code 0. Full configured corpus scan for curator-added
    graph nodes; this target contains no causal graph. Actual native gate execution
    at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times,
    commands, log hashes and terminal exit codes identify the executions. Reused repository-wide
    receipts require the explicit same-base/native-input certificate; these are historical
    runs, not new batch-0015 invocations. Missing terminal receipts or reuse proof
    remain unavailable in unsaved previews. Exact-target strict receipts retain their
    original execution context. New review bundles still require individual validation/save/check.
  target_ids:
  - NCBITaxon:1872626
  evidence_ids:
  - products-receipt
  - native-gate-reuse
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: Full configured corpus scan for curator-added graph nodes; this target
    contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained original cwd, times, commands, log hashes and terminal exit codes identify
    the executions. Reused repository-wide receipts require the explicit same-base/native-input
    certificate; these are historical runs, not new batch-0015 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check.
- check_id: qc
  name: Authoritative complete quality gate
  status: passed
  required: true
  summary: Actual terminal exit code 0. Repository-wide just qc, including native
    corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained original cwd, times, commands, log hashes and terminal exit codes identify
    the executions. Reused repository-wide receipts require the explicit same-base/native-input
    certificate; these are historical runs, not new batch-0015 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check. 1073 passed, 3 skipped, 5 deselected
    in 1293.90s (0:21:33)
  target_ids:
  - NCBITaxon:1872626
  evidence_ids:
  - qc-receipt
  - native-gate-reuse
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: Repository-wide just qc, including native corpus-wide checks. Actual
    native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
    original cwd, times, commands, log hashes and terminal exit codes identify the
    executions. Reused repository-wide receipts require the explicit same-base/native-input
    certificate; these are historical runs, not new batch-0015 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/taxa/archaea/archaeoglobus_sp.yaml
  accessed_at: '2026-10-21T07:58:27Z'
  support: supports
  summary: Read the entire generated YAML, including identity, lineage, names, mappings,
    source attestations, all imported strains and links, and seed history.
  locator: entire TaxonRecord; identifier=NCBITaxon:1872626
  snapshot_sha256: e63785714adadc18731b62c87d73aa9b300dd17c616d067ae22476fd31386443
- evidence_id: taxonomy-inventory
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-21T06:45:18Z'
  support: supports
  summary: Inspected the target and each carried ancestor, rank, parent, genetic code
    and source name classes.
  locator: 'line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""};
    line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"};
    line 1755: {"taxon_id":"NCBITaxon:2231","label":"Archaeoglobales","rank":"ORDER","parent_id":"NCBITaxon:183980"};
    line 1756: {"taxon_id":"NCBITaxon:2232","label":"Archaeoglobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2231"};
    line 1757: {"taxon_id":"NCBITaxon:2233","label":"Archaeoglobus","rank":"GENUS","parent_id":"NCBITaxon:2232"};
    line 2981: {"taxon_id":"NCBITaxon:28890","label":"Methanobacteriota","rank":"PHYLUM","parent_id":"NCBITaxon:3366610"};
    line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"};
    line 36620: {"taxon_id":"NCBITaxon:183980","label":"Archaeoglobi","rank":"CLASS","parent_id":"NCBITaxon:28890"};
    line 489383: {"taxon_id":"NCBITaxon:1872626","label":"Archaeoglobus sp.","rank":"SPECIES","parent_id":"NCBITaxon:2643606","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon|gtdb","retired_into":"","taxonomy_snapshot":"2026-09-13"};
    line 539688: {"taxon_id":"NCBITaxon:2643606","label":"unclassified Archaeoglobus","rank":"NO_RANK","parent_id":"NCBITaxon:2233"};
    line 621140: {"taxon_id":"NCBITaxon:3366610","label":"Methanobacteriati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
- evidence_id: scope-row
  kind: database
  reference: curation/seed_scope.tsv
  accessed_at: '2026-10-21T06:45:18Z'
  support: supports
  summary: Exact target is included in the declared seed scope.
  locator: 'line 80135: {"identifier":"NCBITaxon:1872626","added":"2026-09-13","reason":"attested
    rule: Archaeoglobus sp., 2 sources incl. NCBI"}'
  snapshot_sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
- evidence_id: path-row
  kind: database
  reference: data/taxa/PATHS.tsv
  accessed_at: '2026-10-21T06:45:18Z'
  support: supports
  summary: Indexed path resolves to this exact NCBI taxon.
  locator: 'line 296840: {"identifier":"NCBITaxon:1872626","slug":"archaeoglobus_sp"}'
  snapshot_sha256: f8f2e0721cb6839b30530b44be0d3004b9f0e6e2d4be8736f235b10117a8bd99
- evidence_id: ncbi-live
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=84156,572546,1872626,403220,1748302,669409,669410,1934979,1934980,1934981&retmode=xml
  accessed_at: '2026-10-21T06:44:59Z'
  support: supports
  summary: 'Inspected the official response for this exact taxon: scientific name,
    rank, parent, source name classes, lineage and genetic code. Current authority
    and pinned September inventory remain distinct observations.'
  locator: TaxaSet/Taxon[TaxId='1872626']; ten-target captured response
  snapshot_sha256: b09530be27adc4834683f44a881b9a8f0a5efed248c5318bd06a298cc1934239
- evidence_id: lpsn-inventory
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-21T06:45:18Z'
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
  accessed_at: '2026-10-21T06:45:18Z'
  support: supports
  summary: Inspected direct mappings and selected clusters' reverse mappings, retaining
    each source predicate and taxon boundary.
  locator: 'line 20129: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1344584","predicate":"skos:closeMatch","genome_count":"6"};
    line 72201: {"gtdb_id":"GTDB:s__Archaeoglobus_A_sp017656505","gtdb_label":"s__Archaeoglobus_A_sp017656505","gtdb_parent":"GTDB:g__Archaeoglobus_A","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"};
    line 72202: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"6"};
    line 72203: {"gtdb_id":"GTDB:s__Archaeoglobus_sp017656475","gtdb_label":"s__Archaeoglobus_sp017656475","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"};
    line 72204: {"gtdb_id":"GTDB:s__Archaeoglobus_sp036742095","gtdb_label":"s__Archaeoglobus_sp036742095","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"};
    line 72205: {"gtdb_id":"GTDB:s__WAPX01_sp003978865","gtdb_label":"s__WAPX01_sp003978865","gtdb_parent":"GTDB:g__WAPX01","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"};
    line 72206: {"gtdb_id":"GTDB:s__WYZ-LMO2_sp011605865","gtdb_label":"s__WYZ-LMO2_sp011605865","gtdb_parent":"GTDB:g__WYZ-LMO2","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"2"};
    line 177020: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:2234","predicate":"skos:closeMatch","genome_count":"6"};
    line 177993: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:224325","predicate":"skos:closeMatch","genome_count":"6"};
    line 178159: {"gtdb_id":"GTDB:s__WYZ-LMO2_sp011605865","gtdb_label":"s__WYZ-LMO2_sp011605865","gtdb_parent":"GTDB:g__WYZ-LMO2","ncbitaxon_id":"NCBITaxon:2250258","predicate":"skos:broadMatch","genome_count":"2"}'
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
- evidence_id: gtdb-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-21T06:45:18Z'
  support: supports
  summary: Inspected source species identifiers, labels, parent clusters and genome
    counts.
  locator: 'line 12295: {"gtdb_id":"GTDB:s__Archaeoglobus_A_sp017656505","label":"s__Archaeoglobus_A_sp017656505","parent":"GTDB:g__Archaeoglobus_A","genome_count":"1"};
    line 12308: {"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","label":"s__Archaeoglobus_fulgidus","parent":"GTDB:g__Archaeoglobus","genome_count":"6"};
    line 12311: {"gtdb_id":"GTDB:s__Archaeoglobus_sp017656475","label":"s__Archaeoglobus_sp017656475","parent":"GTDB:g__Archaeoglobus","genome_count":"1"};
    line 12316: {"gtdb_id":"GTDB:s__Archaeoglobus_sp036742095","label":"s__Archaeoglobus_sp036742095","parent":"GTDB:g__Archaeoglobus","genome_count":"1"};
    line 196735: {"gtdb_id":"GTDB:s__WAPX01_sp003978865","label":"s__WAPX01_sp003978865","parent":"GTDB:g__WAPX01","genome_count":"1"};
    line 198200: {"gtdb_id":"GTDB:s__WYZ-LMO2_sp011605865","label":"s__WYZ-LMO2_sp011605865","parent":"GTDB:g__WYZ-LMO2","genome_count":"2"}'
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
- evidence_id: bacdive-inventory
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-21T06:45:18Z'
  support: supports
  summary: Complete inventory selection covers the exact target and descendants from
    the complete NCBI parent graph; its imported strain population was compared with
    the complete YAML.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 029fd6d1f53ef7f90684130bf0d644ed3edd1d8fbeb065a511ae928f160b1eea
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: culture-inventory
  kind: database
  reference: data/raw/culture_collection_strains.tsv
  accessed_at: '2026-10-21T06:45:18Z'
  support: supports
  summary: Inspected exact culture-inventory associations; an isolate name or genome
    does not create an inferred deposit.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 810fdcb16abd6330fb15bb03d4c74b18db86be36a7c599df7c6b2498d9735c95
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: gold-organisms
  kind: database
  reference: data/raw/gold_organisms.tsv
  accessed_at: '2026-10-21T06:45:18Z'
  support: supports
  summary: Inspected the exact GOLD organism count row or bounded absence, without
    converting counts to phenotypes.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: mediadive-taxa
  kind: database
  reference: data/raw/mediadive_taxa.tsv
  accessed_at: '2026-10-21T06:45:18Z'
  support: supports
  summary: Inspected the exact MediaDive medium count row or bounded absence, without
    converting counts to phenotypes.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 3f74b78cadfcdb6aeae953e09fdb39e34fd9c5d5ed0be65a04a5d7fb02355905
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: madin-taxa
  kind: database
  reference: data/raw/madin_taxa.tsv
  accessed_at: '2026-10-21T06:45:18Z'
  support: supports
  summary: Inspected the exact Madin trait-assertion count row or bounded absence,
    without converting counts to phenotypes.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: bactotraits-taxa
  kind: database
  reference: data/raw/bactotraits_taxa.tsv
  accessed_at: '2026-10-21T06:45:18Z'
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
  accessed_at: '2026-10-21T07:58:27Z'
  support: supports
  summary: Policy permits one-to-one species closeMatch normalization and LPSN-linked
    species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage
    unchanged.
  locator: Mapping predicates; Which strains belong to a record
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
- evidence_id: equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-21T07:58:27Z'
  support: supports
  summary: TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations
    remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes
    under the source taxon.
  locator: TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
- evidence_id: seed-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-21T07:58:27Z'
  support: supports
  summary: Inspected mapping ranking, qualified predicates, fixed broadMatch wording,
    synonym/xref construction, primary cluster counts and same-taxon type-strain derivation.
  locator: GTDB mapping construction lines 444–476; LPSN/type-strain and source-attestation
    construction
  snapshot_sha256: 3cc30f6413a293165385dfc1860505fe389e5adfe9aa3d168f76aa4cb2ac36bd
- evidence_id: manifest
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-21T07:58:27Z'
  support: supports
  summary: Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd,
    upstream input hashes and extraction time 2026-09-13T17:50:44Z.
  locator: kg_microbe_source, inputs, extracted_at
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
- evidence_id: overlay-manifests
  kind: record_content
  reference: data/atb/MANIFEST.yaml
  accessed_at: '2026-10-21T07:58:27Z'
  support: supports
  summary: Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z,
    matching the sole seed event. StrainInfo manifest is independently captured in
    source.inputs.
  locator: extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml
  snapshot_sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
- evidence_id: genome-catalog-1
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0017.jsonl.gz
  accessed_at: '2026-10-21T06:50:54Z'
  support: supports
  summary: Inspected every selected primary GTDB row, exact taxid/species-taxid, culture
    identifiers and accession versions. Species membership alone is not strain identity.
  locator: 'line 29518: {"accession":"GB_GCA_003978865.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WAPX01;s__WAPX01
    sp003978865","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM397886v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA454888","ncbi_biosample":"SAMN09407821","ncbi_contig_count":"97","ncbi_contig_n50":"17226","ncbi_country":"Pacific
    Ocean: Mariana Back-Arc Basin vent fields","ncbi_date":"2018-12-28","ncbi_genbank_assembly_accession":"GCA_003978865.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"MAG 85","ncbi_isolation_source":"hydrothermal
    vent","ncbi_lat_lon":"16.96131294 N 144.8678188 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus
    sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"2","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2018-12-28","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1872626","ncbi_ssu_count":"1","ncbi_strain_identifiers":"MAG
    85","ncbi_submitter":"WHOI","ncbi_taxid":"1872626","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__unclassified
    Archaeoglobus;s__Archaeoglobus sp.","ncbi_total_gap_length":"0","ncbi_total_length":"1106720","ncbi_translation_table":"11","ncbi_trna_count":"34","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1106720","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"QNXS00000000.1"};
    line 30338: {"accession":"RS_GCF_900069765.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
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
    line 37279: {"accession":"GB_GCA_017656505.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus_A;s__Archaeoglobus_A
    sp017656505","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM1765650v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA635695","ncbi_biosample":"SAMN15049708","ncbi_contig_count":"95","ncbi_contig_n50":"44138","ncbi_country":"Mexico:
    Guaymas Basin","ncbi_date":"2021-04-01","ncbi_genbank_assembly_accession":"GCA_017656505.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"GB_MAG3_049","ncbi_isolation_source":"deep
    sea sediment sample 4871-20 in thermophilic enrichment culture","ncbi_lat_lon":"27.04618
    N 111.38483 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus
    sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2021-04-01","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1872626","ncbi_ssu_count":"1","ncbi_strain_identifiers":"GB_MAG3_049","ncbi_submitter":"Marine
    Biological Laboratory","ncbi_taxid":"1872626","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__unclassified
    Archaeoglobus;s__Archaeoglobus sp.","ncbi_total_gap_length":"0","ncbi_total_length":"2524501","ncbi_translation_table":"11","ncbi_trna_count":"44","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2524501","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JACDNU000000000.1"};
    line 40690: {"accession":"RS_GCF_017656475.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    sp017656475","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM1765647v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN15049707","ncbi_contig_count":"92","ncbi_contig_n50":"48438","ncbi_country":"Mexico:
    Guaymas Basin","ncbi_date":"2021-04-01","ncbi_genbank_assembly_accession":"GCA_017656475.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"GB_MAG2_100","ncbi_isolation_source":"deep
    sea sediment sample 4871-20 in thermophilic enrichment culture","ncbi_lat_lon":"27.04618
    N 111.38483 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus
    sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2021-04-01","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1872626","ncbi_ssu_count":"1","ncbi_strain_identifiers":"GB_MAG2_100","ncbi_submitter":"Marine
    Biological Laboratory","ncbi_taxid":"1872626","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__unclassified
    Archaeoglobus;s__Archaeoglobus sp.","ncbi_total_gap_length":"0","ncbi_total_length":"2039628","ncbi_translation_table":"11","ncbi_trna_count":"42","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2039628","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JACDNT000000000.1"};
    line 43481: {"accession":"GB_GCA_020833165.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2
    sp011605865","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2083316v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA568220","ncbi_biosample":"SAMN18938186","ncbi_contig_count":"104","ncbi_contig_n50":"22329","ncbi_country":"USA:
    Yellowstone National Park; GGS063 Spring","ncbi_date":"2021-11-10","ncbi_genbank_assembly_accession":"GCA_020833165.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"Bin S27","ncbi_isolation_source":"Sediments
    from shelf","ncbi_lat_lon":"44.69047 N 110.72917 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus
    sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2021-11-10","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1872626","ncbi_ssu_count":"1","ncbi_strain_identifiers":"Bin
    S27","ncbi_submitter":"DOE Joint Genome Institute","ncbi_taxid":"1872626","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__unclassified
    Archaeoglobus;s__Archaeoglobus sp.","ncbi_total_gap_length":"0","ncbi_total_length":"1399988","ncbi_translation_table":"11","ncbi_trna_count":"43","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1399988","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAJHQV000000000.1"};
    line 45270: {"accession":"RS_GCF_029982885.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2998288v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN33401081","ncbi_contig_count":"121","ncbi_contig_n50":"21098","ncbi_country":"USA:
    Colorado","ncbi_date":"2023-05-11","ncbi_genbank_assembly_accession":"GCA_029982885.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"DJKA110_ANT-KO_bin.46","ncbi_isolation_source":"Produced
    fluids from hydraulically fractured shales","ncbi_lat_lon":"40.411582 N 104.348363
    W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus
    sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"2","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-05-11","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1872626","ncbi_ssu_count":"0","ncbi_strain_identifiers":"DJKA110_ANT-KO_bin.46","ncbi_submitter":"The
    Ohio State University","ncbi_taxid":"1872626","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__unclassified
    Archaeoglobus;s__Archaeoglobus sp.","ncbi_total_gap_length":"0","ncbi_total_length":"1934538","ncbi_translation_table":"11","ncbi_trna_count":"44","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1934538","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JARRCC000000000.1"};
    line 46580: {"accession":"GB_GCA_036742095.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    sp036742095","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM3674209v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA843551","ncbi_biosample":"SAMN28746634","ncbi_contig_count":"503","ncbi_contig_n50":"5343","ncbi_country":"none","ncbi_date":"2024-02-21","ncbi_genbank_assembly_accession":"GCA_036742095.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"CTOTU24189","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobus
    sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"311","ncbi_scaffold_l50":"77","ncbi_scaffold_n50":"7275","ncbi_scaffold_n75":"4199","ncbi_scaffold_n90":"2702","ncbi_seq_rel_date":"2024-02-21","ncbi_spanned_gaps":"192","ncbi_species_taxid":"1872626","ncbi_ssu_count":"none","ncbi_strain_identifiers":"CTOTU24189","ncbi_submitter":"Helmholtz
    Centre for Environmental Research - UFZ","ncbi_taxid":"1872626","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__unclassified
    Archaeoglobus;s__Archaeoglobus sp.","ncbi_total_gap_length":"9222","ncbi_total_length":"1718707","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1709485","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"DAINRD000000000.1"};
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
    line 47637: {"accession":"GB_GCA_011605865.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2
    sp011605865","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM1160586v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA604268","ncbi_biosample":"SAMN13964307","ncbi_contig_count":"45","ncbi_contig_n50":"41011","ncbi_country":"USA:
    Yellowstone National Park; Smokejumper3 Hot Spring","ncbi_date":"2020-03-22","ncbi_genbank_assembly_accession":"GCA_011605865.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SJ3.Bin61","ncbi_isolation_source":"sediments
    from hot spring shelf","ncbi_lat_lon":"44.41595 N 110.9558 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobales
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"2","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2020-03-22","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250258","ncbi_ssu_count":"1","ncbi_strain_identifiers":"SJ3.Bin61","ncbi_submitter":"Montana
    State University","ncbi_taxid":"2250258","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;x__unclassified
    Archaeoglobales;s__Archaeoglobales archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1269726","ncbi_translation_table":"11","ncbi_trna_count":"41","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1269726","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAAOZI000000000.1"};
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
  accessed_at: '2026-10-21T06:50:54Z'
  support: supports
  summary: All nineteen pinned GTDB shards were searched with exact terminal species
    tokens preserving internal genus suffix underscores. Selected cluster counts,
    reverse mappings and taxon distributions were assessed separately from synonym/xref
    promotion.
  locator: '[{"gtdb_species_id":"GTDB:s__WAPX01_sp003978865","member_rows":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":29518,"accession":"GB_GCA_003978865.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WAPX01;s__WAPX01
    sp003978865","ncbi_taxid":"1872626","ncbi_species_taxid":"1872626","ncbi_organism_name":"Archaeoglobus
    sp.","ncbi_strain_identifiers":"MAG 85","ncbi_isolate":"MAG 85","ncbi_genome_category":"derived
    from metagenome","ncbi_genbank_assembly_accession":"GCA_003978865.1","ncbi_biosample":"SAMN09407821","ncbi_bioproject":"PRJNA454888"}],"reverse_mapping_rows":[{"line":72205,"row":{"gtdb_id":"GTDB:s__WAPX01_sp003978865","gtdb_label":"s__WAPX01_sp003978865","gtdb_parent":"GTDB:g__WAPX01","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"}}],"species_inventory_rows":[{"line":196735,"row":{"gtdb_id":"GTDB:s__WAPX01_sp003978865","label":"s__WAPX01_sp003978865","parent":"GTDB:g__WAPX01","genome_count":"1"}}],"observed_member_count":1,"ncbi_taxids":["1872626"],"ncbi_species_taxids":["1872626"],"reverse_mapping_target_ids":["NCBITaxon:1872626"],"scientific_scope_assessment":"GTDB
    species cluster. Its genome membership and source reverse mappings are retained
    as qualified mapping evidence; membership alone does not establish NCBI taxon
    identity at every rank."},{"gtdb_species_id":"GTDB:s__Archaeoglobus_fulgidus","member_rows":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":30338,"accession":"RS_GCF_900069765.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","ncbi_taxid":"2234","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus
    fulgidus","ncbi_strain_identifiers":"Archaeoglobus_fulgidus_oil","ncbi_isolate":"Archaeoglobus_fulgidus_oil","ncbi_genome_category":"none","ncbi_genbank_assembly_accession":"GCA_900069765.1","ncbi_biosample":"SAMEA3879005","ncbi_bioproject":"PRJNA224116"},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":30980,"accession":"GB_GCA_001508745.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","ncbi_taxid":"2234","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus
    fulgidus","ncbi_strain_identifiers":"49_95","ncbi_isolate":"49_95","ncbi_genome_category":"derived
    from metagenome","ncbi_genbank_assembly_accession":"GCA_001508745.1","ncbi_biosample":"SAMN03445115","ncbi_bioproject":"PRJNA278302"},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":45270,"accession":"RS_GCF_029982885.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","ncbi_taxid":"1872626","ncbi_species_taxid":"1872626","ncbi_organism_name":"Archaeoglobus
    sp.","ncbi_strain_identifiers":"DJKA110_ANT-KO_bin.46","ncbi_isolate":"DJKA110_ANT-KO_bin.46","ncbi_genome_category":"derived
    from metagenome","ncbi_genbank_assembly_accession":"GCA_029982885.1","ncbi_biosample":"SAMN33401081","ncbi_bioproject":"PRJNA224116"},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":47261,"accession":"GB_GCA_001508815.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","ncbi_taxid":"2234","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus
    fulgidus","ncbi_strain_identifiers":"49_2300","ncbi_isolate":"49_2300","ncbi_genome_category":"derived
    from metagenome","ncbi_genbank_assembly_accession":"GCA_001508815.1","ncbi_biosample":"SAMN03445123","ncbi_bioproject":"PRJNA278302"},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":47600,"accession":"RS_GCF_000734035.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","ncbi_taxid":"1344584","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus
    fulgidus DSM 8774","ncbi_strain_identifiers":"DSM 8774","ncbi_isolate":"na","ncbi_genome_category":"none","ncbi_genbank_assembly_accession":"GCA_000734035.1","ncbi_biosample":"SAMN03081472","ncbi_bioproject":"PRJNA224116"},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":48903,"accession":"RS_GCF_000008665.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    fulgidus","ncbi_taxid":"224325","ncbi_species_taxid":"2234","ncbi_organism_name":"Archaeoglobus
    fulgidus DSM 4304","ncbi_strain_identifiers":"DSM 4304","ncbi_isolate":"na","ncbi_genome_category":"none","ncbi_genbank_assembly_accession":"GCA_000008665.1","ncbi_biosample":"SAMN02603985","ncbi_bioproject":"PRJNA224116"}],"reverse_mapping_rows":[{"line":20129,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1344584","predicate":"skos:closeMatch","genome_count":"6"}},{"line":72202,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"6"}},{"line":177020,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:2234","predicate":"skos:closeMatch","genome_count":"6"}},{"line":177993,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","gtdb_label":"s__Archaeoglobus_fulgidus","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:224325","predicate":"skos:closeMatch","genome_count":"6"}}],"species_inventory_rows":[{"line":12308,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_fulgidus","label":"s__Archaeoglobus_fulgidus","parent":"GTDB:g__Archaeoglobus","genome_count":"6"}}],"observed_member_count":6,"ncbi_taxids":["1344584","1872626","2234","224325"],"ncbi_species_taxids":["1872626","2234"],"reverse_mapping_target_ids":["NCBITaxon:1344584","NCBITaxon:1872626","NCBITaxon:2234","NCBITaxon:224325"],"scientific_scope_assessment":"GTDB
    species cluster. Its genome membership and source reverse mappings are retained
    as qualified mapping evidence; membership alone does not establish NCBI taxon
    identity at every rank."},{"gtdb_species_id":"GTDB:s__Archaeoglobus_A_sp017656505","member_rows":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":37279,"accession":"GB_GCA_017656505.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus_A;s__Archaeoglobus_A
    sp017656505","ncbi_taxid":"1872626","ncbi_species_taxid":"1872626","ncbi_organism_name":"Archaeoglobus
    sp.","ncbi_strain_identifiers":"GB_MAG3_049","ncbi_isolate":"GB_MAG3_049","ncbi_genome_category":"derived
    from metagenome","ncbi_genbank_assembly_accession":"GCA_017656505.1","ncbi_biosample":"SAMN15049708","ncbi_bioproject":"PRJNA635695"}],"reverse_mapping_rows":[{"line":72201,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_A_sp017656505","gtdb_label":"s__Archaeoglobus_A_sp017656505","gtdb_parent":"GTDB:g__Archaeoglobus_A","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"}}],"species_inventory_rows":[{"line":12295,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_A_sp017656505","label":"s__Archaeoglobus_A_sp017656505","parent":"GTDB:g__Archaeoglobus_A","genome_count":"1"}}],"observed_member_count":1,"ncbi_taxids":["1872626"],"ncbi_species_taxids":["1872626"],"reverse_mapping_target_ids":["NCBITaxon:1872626"],"scientific_scope_assessment":"GTDB
    species cluster. Its genome membership and source reverse mappings are retained
    as qualified mapping evidence; membership alone does not establish NCBI taxon
    identity at every rank."},{"gtdb_species_id":"GTDB:s__Archaeoglobus_sp017656475","member_rows":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":40690,"accession":"RS_GCF_017656475.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    sp017656475","ncbi_taxid":"1872626","ncbi_species_taxid":"1872626","ncbi_organism_name":"Archaeoglobus
    sp.","ncbi_strain_identifiers":"GB_MAG2_100","ncbi_isolate":"GB_MAG2_100","ncbi_genome_category":"derived
    from metagenome","ncbi_genbank_assembly_accession":"GCA_017656475.1","ncbi_biosample":"SAMN15049707","ncbi_bioproject":"PRJNA224116"}],"reverse_mapping_rows":[{"line":72203,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_sp017656475","gtdb_label":"s__Archaeoglobus_sp017656475","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"}}],"species_inventory_rows":[{"line":12311,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_sp017656475","label":"s__Archaeoglobus_sp017656475","parent":"GTDB:g__Archaeoglobus","genome_count":"1"}}],"observed_member_count":1,"ncbi_taxids":["1872626"],"ncbi_species_taxids":["1872626"],"reverse_mapping_target_ids":["NCBITaxon:1872626"],"scientific_scope_assessment":"GTDB
    species cluster. Its genome membership and source reverse mappings are retained
    as qualified mapping evidence; membership alone does not establish NCBI taxon
    identity at every rank."},{"gtdb_species_id":"GTDB:s__WYZ-LMO2_sp011605865","member_rows":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":43481,"accession":"GB_GCA_020833165.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2
    sp011605865","ncbi_taxid":"1872626","ncbi_species_taxid":"1872626","ncbi_organism_name":"Archaeoglobus
    sp.","ncbi_strain_identifiers":"Bin S27","ncbi_isolate":"Bin S27","ncbi_genome_category":"derived
    from metagenome","ncbi_genbank_assembly_accession":"GCA_020833165.1","ncbi_biosample":"SAMN18938186","ncbi_bioproject":"PRJNA568220"},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":47637,"accession":"GB_GCA_011605865.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2
    sp011605865","ncbi_taxid":"2250258","ncbi_species_taxid":"2250258","ncbi_organism_name":"Archaeoglobales
    archaeon","ncbi_strain_identifiers":"SJ3.Bin61","ncbi_isolate":"SJ3.Bin61","ncbi_genome_category":"derived
    from metagenome","ncbi_genbank_assembly_accession":"GCA_011605865.1","ncbi_biosample":"SAMN13964307","ncbi_bioproject":"PRJNA604268"}],"reverse_mapping_rows":[{"line":72206,"row":{"gtdb_id":"GTDB:s__WYZ-LMO2_sp011605865","gtdb_label":"s__WYZ-LMO2_sp011605865","gtdb_parent":"GTDB:g__WYZ-LMO2","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"2"}},{"line":178159,"row":{"gtdb_id":"GTDB:s__WYZ-LMO2_sp011605865","gtdb_label":"s__WYZ-LMO2_sp011605865","gtdb_parent":"GTDB:g__WYZ-LMO2","ncbitaxon_id":"NCBITaxon:2250258","predicate":"skos:broadMatch","genome_count":"2"}}],"species_inventory_rows":[{"line":198200,"row":{"gtdb_id":"GTDB:s__WYZ-LMO2_sp011605865","label":"s__WYZ-LMO2_sp011605865","parent":"GTDB:g__WYZ-LMO2","genome_count":"2"}}],"observed_member_count":2,"ncbi_taxids":["1872626","2250258"],"ncbi_species_taxids":["1872626","2250258"],"reverse_mapping_target_ids":["NCBITaxon:1872626","NCBITaxon:2250258"],"scientific_scope_assessment":"GTDB
    species cluster. Its genome membership and source reverse mappings are retained
    as qualified mapping evidence; membership alone does not establish NCBI taxon
    identity at every rank."},{"gtdb_species_id":"GTDB:s__Archaeoglobus_sp036742095","member_rows":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":46580,"accession":"GB_GCA_036742095.1","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    sp036742095","ncbi_taxid":"1872626","ncbi_species_taxid":"1872626","ncbi_organism_name":"Archaeoglobus
    sp.","ncbi_strain_identifiers":"CTOTU24189","ncbi_isolate":"CTOTU24189","ncbi_genome_category":"derived
    from metagenome","ncbi_genbank_assembly_accession":"GCA_036742095.1","ncbi_biosample":"SAMN28746634","ncbi_bioproject":"PRJNA843551"}],"reverse_mapping_rows":[{"line":72204,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_sp036742095","gtdb_label":"s__Archaeoglobus_sp036742095","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:1872626","predicate":"skos:broadMatch","genome_count":"1"}}],"species_inventory_rows":[{"line":12316,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_sp036742095","label":"s__Archaeoglobus_sp036742095","parent":"GTDB:g__Archaeoglobus","genome_count":"1"}}],"observed_member_count":1,"ncbi_taxids":["1872626"],"ncbi_species_taxids":["1872626"],"reverse_mapping_target_ids":["NCBITaxon:1872626"],"scientific_scope_assessment":"GTDB
    species cluster. Its genome membership and source reverse mappings are retained
    as qualified mapping evidence; membership alone does not establish NCBI taxon
    identity at every rank."}]'
  snapshot_sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
  search_scope: All enumerated GTDB primary shards, including ignored files. Exact
    source species ID from terminal species token with spaces converted to underscores;
    internal genus/epithet underscores preserved. Exact supplied GTDB genome accession
    also selected. No broad biological absence claim.
- evidence_id: finding-deduplication
  kind: search
  reference: Owned review worktrees structured bundles
  accessed_at: '2026-10-21T06:55:30Z'
  support: supports
  summary: No existing target-specific finding with these stable keys was found in
    the bounded ignored-inclusive search at the recorded time.
  locator: '{"keys":["gtdb-broadmatch-note-other-taxa-1872626"],"matches":{"gtdb-broadmatch-note-other-taxa-1872626":[]},"unique_review_ids":169}'
  snapshot_sha256: 602326f3f4d3f8274ddec4baa03de97febd69440b17e85f3b4e3719083a44487
  search_scope: Fresh-main-containing owned repo-batch-0014 plus owned branches 0001
    through 0013; recursive os.walk over complete reviews/structured directories,
    including ignored and hidden files. Parent may save later reviews after this timestamp.
- evidence_id: native-gate-reuse
  kind: validation
  reference: /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0015/native-gate-reuse.json
  accessed_at: '2026-10-21T07:51:59Z'
  support: supports
  summary: Retained explicit verification of identical base/native inputs authorizes
    historical native-gate reuse; original command receipts remain separately cited.
  locator: base, native_inputs_unchanged, source_directory, gates, input_proof_path
    and input_proof_sha256
  snapshot_sha256: ab0bbc1610fb997b62ec9fe0c01610fd4b5b197dc1ff661a804c563572afbe95
- evidence_id: strict-receipt
  kind: validation
  reference: just validate-strict data/taxa/archaea/archaeoglobus_sp.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0015/strict-03.tsv
  accessed_at: '2026-10-21T06:45:24Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0015/repo;\
    \ started 2026-10-21T06:45:23Z, finished 2026-10-21T06:45:24Z, exit 0. This exact\
    \ generated YAML only; its captured bytes remain unchanged. Actual earlier per-target\
    \ invocation; the receipt retains its original cwd and times.\nValidating 1 files\
    \ with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0014/src/taxonmech/schema/taxonmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0015/strict-03.tsv"
  locator: This exact generated YAML only; its captured bytes remain unchanged. Actual
    earlier per-target invocation; the receipt retains its original cwd and times.
  snapshot_sha256: 61bfe0293562533db89cc071a126b0795e555a8b5216268215035925b31ec89c
- evidence_id: history-receipt
  kind: validation
  reference: just validate-history
  accessed_at: '2026-10-21T06:42:11Z'
  support: supports
  summary: 'Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo;
    started 2026-10-21T06:42:09Z, finished 2026-10-21T06:42:11Z, exit 0. The complete
    standalone history population; the generated seed event was also inspected in
    this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained original cwd, times, commands, log hashes and terminal exit codes identify
    the executions. Reused repository-wide receipts require the explicit same-base/native-input
    certificate; these are historical runs, not new batch-0015 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check.

    history links: 18 record(s), 0 invalid

    No issues found

    18 history record(s) valid against src/taxonmech/schema/history.yaml'
  locator: The complete standalone history population; the generated seed event was
    also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained original cwd, times, commands, log hashes and terminal exit codes identify
    the executions. Reused repository-wide receipts require the explicit same-base/native-input
    certificate; these are historical runs, not new batch-0015 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check.
  snapshot_sha256: 98b39b3ec0f369362dd50578fb05797d78334edf5b6961dd70e82283af0ac3ca
- evidence_id: corpus-receipt
  kind: validation
  reference: just verify-corpus
  accessed_at: '2026-10-21T06:48:01Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo;\
    \ started 2026-10-21T06:42:09Z, finished 2026-10-21T06:48:01Z, exit 0. All 626,048\
    \ generated taxon YAMLs, not a focused approximation. Actual native gate execution\
    \ at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times,\
    \ commands, log hashes and terminal exit codes identify the executions. Reused\
    \ repository-wide receipts require the explicit same-base/native-input certificate;\
    \ these are historical runs, not new batch-0015 invocations. Missing terminal\
    \ receipts or reuse proof remain unavailable in unsaved previews. Exact-target\
    \ strict receipts retain their original execution context. New review bundles\
    \ still require individual validation/save/check.\nuv run python scripts/verify_corpus.py\
    \ \nexpected 626048 records, found 626048 on disk\n  missing:   0\n  extra:  \
    \   0\n  differing: 0\n\ncorpus reproduces exactly from data/raw/ and curation/seed_scope.tsv"
  locator: All 626,048 generated taxon YAMLs, not a focused approximation. Actual
    native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
    original cwd, times, commands, log hashes and terminal exit codes identify the
    executions. Reused repository-wide receipts require the explicit same-base/native-input
    certificate; these are historical runs, not new batch-0015 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check.
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
    retained original cwd, times, commands, log hashes and terminal exit codes identify
    the executions. Reused repository-wide receipts require the explicit same-base/native-input
    certificate; these are historical runs, not new batch-0015 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check.

    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml


    id↔label correspondence summary:


    ✅ All id↔label pairs correspond.'
  locator: Full configured corpus scan for curator-added graph nodes; this target
    contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained original cwd, times, commands, log hashes and terminal exit codes identify
    the executions. Reused repository-wide receipts require the explicit same-base/native-input
    certificate; these are historical runs, not new batch-0015 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check.
  snapshot_sha256: 48dd07515706dc62199fc2205c4b0bfdd5750028037d9b800179f254d2f1eb07
- evidence_id: qc-receipt
  kind: validation
  reference: just qc
  accessed_at: '2026-10-21T07:50:51Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo;\
    \ started 2026-10-21T06:42:09Z, finished 2026-10-21T07:50:51Z, exit 0. Repository-wide\
    \ just qc, including native corpus-wide checks. Actual native gate execution at\
    \ base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times,\
    \ commands, log hashes and terminal exit codes identify the executions. Reused\
    \ repository-wide receipts require the explicit same-base/native-input certificate;\
    \ these are historical runs, not new batch-0015 invocations. Missing terminal\
    \ receipts or reuse proof remain unavailable in unsaved previews. Exact-target\
    \ strict receipts retain their original execution context. New review bundles\
    \ still require individual validation/save/check.\nAll checks passed!\n1073 passed,\
    \ 3 skipped, 5 deselected in 1293.90s (0:21:33)\nValidating 626048 files with\
    \ 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0014/src/taxonmech/schema/taxonmech.yaml\n\
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
    gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original
    cwd, times, commands, log hashes and terminal exit codes identify the executions.
    Reused repository-wide receipts require the explicit same-base/native-input certificate;
    these are historical runs, not new batch-0015 invocations. Missing terminal receipts
    or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts
    retain their original execution context. New review bundles still require individual
    validation/save/check.
  snapshot_sha256: dcb3f98d5c8ce264240732733ca70a5b93ee3e818d03f809d428748abffefca3
assessments:
- assessment_id: identity
  area: identity
  topic: Exact taxon and source lineage
  outcome: supported
  summary: NCBITaxon:1872626 denotes Archaeoglobus sp. at SPECIES rank beneath NCBITaxon:2643606,
    genetic code 11. All 10 carried lineage entries agree with the pinned NCBI inventory
    and captured official EFetch; EFetch omits only root by format. Source name classes
    remain separate from taxon classification.
  target_ids:
  - NCBITaxon:1872626
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
  summary: Pinned/current NCBI retain the literal species-rank placeholder Archaeoglobus
    sp. with no source name-class synonyms. The LPSN fulgidus row found through a
    GTDB crosslink concerns taxid2234 and is not nomenclature for this placeholder.
  target_ids:
  - NCBITaxon:1872626
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - lpsn-inventory
  - mapping-policy
  - genome-catalog-1
  - gtdb-full-scan
- assessment_id: completeness
  area: completeness
  topic: Imported subtree and source assertion units
  outcome: supported
  summary: 'Complete direct reads of twelve source/scope/path tables, including ignored
    files, support 0 imported BacDive strains over the exact target subtree (0 descendant
    taxa). Exact counts agree with their own source units: NCBITAXON 1 NAME; GTDB
    6 GENOME. Counts of media, traits, organisms and genome assertions are distinct
    and do not establish phenotype or genome equivalence. All six GTDB clusters are
    represented: primary count6 plus five additional clusters. Their pooled12 catalog
    members are not the primary count, and only six members carry target taxid1872626.
    Four clusters are singletons solely at this target; fulgidus and WYZ-LMO2 have
    other taxids.'
  target_ids:
  - NCBITaxon:1872626
  evidence_ids:
  - record
  - taxonomy-inventory
  - scope-row
  - path-row
  - lpsn-inventory
  - bacdive-inventory
  - culture-inventory
  - gtdb-species
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
  - genome-catalog-1
  - gtdb-full-scan
- assessment_id: taxonomy-mapping
  area: grounding
  topic: Qualified species mapping and target scope
  outcome: concern
  summary: For each affected GTDB species the complete pinned census has one genome,
    ncbi_taxid and ncbi_species_taxid 1872626, and the entire reverse mapping inventory
    has only NCBITaxon:1872626. Archaeoglobus_fulgidus has six members and four reverse
    NCBI taxids; WYZ-LMO2_sp011605865 has two members and two reverse taxids, so their
    other-taxa wording is supported. The broadMatch pooling relationship itself is
    supported. Counts 6,2,1,1,1,1 are correct. The GTDB attestation is primary count
    6 plus five further clusters, not pooled sum 12.
  target_ids:
  - NCBITaxon:1872626
  evidence_ids:
  - record
  - lpsn-inventory
  - gtdb-mappings
  - gtdb-species
  - mapping-policy
  - equivalence-contract
  - seed-owner
  - genome-catalog-1
  - gtdb-full-scan
- assessment_id: native-status
  area: provenance
  topic: Unchanged native status and history
  outcome: supported
  summary: EXACT grounding and SEEDED status preserve source state. The sole seed
    event at 2026-09-13T17:54:04Z equals the latest raw/ATB/StrainInfo extraction
    time. No native status/history was changed.
  target_ids:
  - NCBITaxon:1872626
  evidence_ids:
  - record
  - manifest
  - overlay-manifests
  - scope-row
  - path-row
findings:
- finding_id: pooled-note-other-taxa
  issue_key: gtdb-broadmatch-note-other-taxa-1872626
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Four singleton GTDB notes incorrectly assert other NCBI taxa
  description: For each affected GTDB species the complete pinned census has one genome,
    ncbi_taxid and ncbi_species_taxid 1872626, and the entire reverse mapping inventory
    has only NCBITaxon:1872626. Archaeoglobus_fulgidus has six members and four reverse
    NCBI taxids; WYZ-LMO2_sp011605865 has two members and two reverse taxids, so their
    other-taxa wording is supported. The broadMatch pooling relationship itself is
    supported. Counts 6,2,1,1,1,1 are correct. The GTDB attestation is primary count
    6 plus five further clusters, not pooled sum 12.
  target_ids:
  - NCBITaxon:1872626
  field_paths:
  - taxonomy_mappings[source_id=GTDB:s__Archaeoglobus_A_sp017656505].notes
  - taxonomy_mappings[source_id=GTDB:s__Archaeoglobus_sp017656475].notes
  - taxonomy_mappings[source_id=GTDB:s__Archaeoglobus_sp036742095].notes
  - taxonomy_mappings[source_id=GTDB:s__WAPX01_sp003978865].notes
  evidence_ids:
  - record
  - gtdb-mappings
  - gtdb-species
  - gtdb-full-scan
  - mapping-policy
  - equivalence-contract
  - seed-owner
  rule_id: docs/HARMONIZATION.md:Mapping predicates; TaxonRecord.xrefs equivalence;
    review skill:preserve claim scope
  native_severity: minor
  normalization_reason: Non-blocking wording defect; mapping predicates, source counts
    and exact target identity remain supported.
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Maintained GTDB mapping notes and synonym/xref scope
actions:
- action_id: correct-pooled-mapping-note
  description: Condition the other-NCBI-taxa clause on actual reverse mapping evidence,
    or use wording limited to the supported pooling direction. Retain all six broadMatch
    mappings and their correct cluster counts; regenerate through native gates.
  finding_ids:
  - pooled-note-other-taxa
  target_ids:
  - NCBITaxon:1872626
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Maintained GTDB mapping notes and synonym/xref scope
  acceptance_checks:
  - All four listed singleton notes omit unsupported other-taxa wording.
  - Retain all six broadMatch mappings, primary count6 and five further clusters.
  - Preserve supported mixed-taxid membership for fulgidus and WYZ-LMO2.
  - Change maintained inputs only; after separately authorized guarded regeneration,
    run strict, history, product, corpus and QC gates.
limitations:
- Assessment is bounded to the exact target and captured source versions; identifier
  and metadata checks do not establish experimental phenotypes, sequence equivalence
  or phylogenetic species boundaries.
- Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
  original cwd, times, commands, log hashes and terminal exit codes identify the executions.
  Reused repository-wide receipts require the explicit same-base/native-input certificate;
  these are historical runs, not new batch-0015 invocations. Missing terminal receipts
  or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts
  retain their original execution context. New review bundles still require individual
  validation/save/check.
notes:
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base source transitions are verified against retained original captures and
  exact changed-input receipts.
- Every new bundle still requires its own validate/save/check recipe; historical native
  receipts do not claim these later steps have run.
tags:
- record-review
- batch-0015
- archaea
- generated
- source-checked
```
