# Record review: Archaeoglobi archaeon

- Review: 20261021T075202Z-archaeoglobi_archaeon
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-20T07:29:19Z
- Finished UTC: 2026-10-21T07:52:02Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Archaeoglobi archaeon has supported exact NCBI identity and source-scoped representation. Three singleton cluster notes overstate other-taxon membership. 

## Scope And Provenance

Entire single generated record, including all source assertions and imported strains.

Selection: Original unreviewed path-order position 132; batch-0014 target 2. Excluded 185 actual targets from validated freshmain and thirteen committed isolated branches; full corpus enumeration includes ignored files.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 01ca63effdf8c03a644df893ba6129b2d8448ea4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:2250530 | data/taxa/archaea/archaeoglobi_archaeon.yaml | generated | Archaeoglobi archaeon |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact NCBI taxon, rank and lineage | passed | True | NCBITaxon:2250530 | NCBITaxon:2250530 denotes Archaeoglobi archaeon at SPECIES rank beneath NCBITaxon:1935015, genetic code 11. All 7 carried ancestors agree with the pinned inventory and captured official NCBI response; the response omits only the root entry. Source name classes remain distinct from taxon classification. |
| Complete exact identifier and name inventory search | passed | True | NCBITaxon:2250530 | Complete direct reads of twelve source/scope/path tables, including ignored files, support 0 imported BacDive strains over the exact target subtree (0 descendant taxa). All imported counts agree with their own source units: NCBITAXON 1 NAME; GTDB 4 GENOME. Counts of organisms, media, traits and genome assertions are not interchangeable and do not prove phenotype or biological genome equivalence. GTDB primary count 4 denotes the first cluster and eight further clusters are recorded; total 18 cluster members are not the primary attestation count. |
| Complete primary GTDB cluster membership | passed | True | NCBITaxon:2250530 | All selected source counts agree; the separate notes/scope findings are retained where applicable. |
| Imported strain links | not_applicable | False | NCBITaxon:2250530 | No imported BacDive strain or strain-level link is asserted; no deposit is inferred from an isolate designation. |
| Historical aggregate edges | not_applicable | False | NCBITaxon:2250530 | No historical medium, organism or trait aggregate asserted. |
| Native strict record validation | passed | True | NCBITaxon:2250530 | Actual terminal exit code 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. |
| Repository history validation | passed | True | NCBITaxon:2250530 | Actual terminal exit code 0. All 18 standalone history records; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. |
| Full-corpus exact reproduction | passed | True | NCBITaxon:2250530 | Actual terminal exit code 0. All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. |
| Native product ID/label gate | passed | True | NCBITaxon:2250530 | Actual terminal exit code 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. |
| Authoritative complete quality gate | passed | True | NCBITaxon:2250530 | Actual terminal exit code 0. Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. 1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33) |

## Scientific And Domain Assessments

### Exact taxon and source lineage

identity: supported. Targets: NCBITaxon:2250530.

NCBITaxon:2250530 denotes Archaeoglobi archaeon at SPECIES rank beneath NCBITaxon:1935015, genetic code 11. All 7 carried ancestors agree with the pinned inventory and captured official NCBI response; the response omits only the root entry. Source name classes remain distinct from taxon classification.

### Name classes and nomenclatural scope

nomenclature: concern. Targets: NCBITaxon:2250530.

NCBI 2250530 identity, species rank and parent 1935015 agree. All nine GTDB broad mappings preserve source predicates and whole-cluster counts. The first six clusters have other NCBI members, whereas the final three are singleton clusters containing only this NCBI taxon. Their fixed pooled-note clause is unsupported. The primary attestation count is 4 genomes plus eight further species, not a sum of counts.

### Imported subtree and source assertion units

completeness: supported. Targets: NCBITaxon:2250530.

Complete direct reads of twelve source/scope/path tables, including ignored files, support 0 imported BacDive strains over the exact target subtree (0 descendant taxa). All imported counts agree with their own source units: NCBITAXON 1 NAME; GTDB 4 GENOME. Counts of organisms, media, traits and genome assertions are not interchangeable and do not prove phenotype or biological genome equivalence. GTDB primary count 4 denotes the first cluster and eight further clusters are recorded; total 18 cluster members are not the primary attestation count.

### Qualified species mapping and target scope

grounding: concern. Targets: NCBITaxon:2250530.

NCBI 2250530 identity, species rank and parent 1935015 agree. All nine GTDB broad mappings preserve source predicates and whole-cluster counts. The first six clusters have other NCBI members, whereas the final three are singleton clusters containing only this NCBI taxon. Their fixed pooled-note clause is unsupported. The primary attestation count is 4 genomes plus eight further species, not a sum of counts.

### Unchanged native status and history

provenance: supported. Targets: NCBITaxon:2250530.

EXACT grounding and SEEDED status agree with NCBI identity. The sole seed event at 2026-09-13T17:54:04Z equals the latest raw/ATB/StrainInfo extraction time; no native status/history was changed.

## Findings

### pooled-note-other-taxa: Three singleton GTDB cluster notes incorrectly assert other NCBI taxa

minor / open / confirmed; issue key: gtdb-broadmatch-note-other-taxa-2250530.

All nineteen GTDB shards were searched with exact terminal species tokens. Each listed cluster contains one genome, solely NCBITaxon:2250530, and reverse mappings agree. The fixed clause asserting other NCBI taxa is unsupported for these three clusters. The other six clusters have mixed taxids; pooling nine GTDB species under the NCBI placeholder still supports broadMatch.

## Recommended Actions And Acceptance Checks

### correct-pooled-mapping-note

Revise the maintained broadMatch note to describe pooling without asserting other NCBI taxa for each source cluster; preserve qualified predicates, counts and carried lineage.

- All three listed singleton notes omit unsupported other-taxa wording.
- Retain all nine mappings, primary count 4 and eight additional clusters; preserve actual mixed-taxid membership.
- Change maintained inputs only; after separately authorized guarded regeneration, run strict, history, product, corpus and QC gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/taxa/archaea/archaeoglobi_archaeon.yaml; entire TaxonRecord; identifier=NCBITaxon:2250530 | supports | Read the entire generated YAML, including identity, lineage, names, mappings, source attestations, all imported strains and links, and seed history. |
| taxonomy-inventory | data/raw/ncbitaxon_taxa.tsv; line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""}; line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"}; line 2981: {"taxon_id":"NCBITaxon:28890","label":"Methanobacteriota","rank":"PHYLUM","parent_id":"NCBITaxon:3366610"}; line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"}; line 36620: {"taxon_id":"NCBITaxon:183980","label":"Archaeoglobi","rank":"CLASS","parent_id":"NCBITaxon:28890"}; line 496673: {"taxon_id":"NCBITaxon:1935015","label":"unclassified Archaeoglobi","rank":"NO_RANK","parent_id":"NCBITaxon:183980"}; line 522268: {"taxon_id":"NCBITaxon:2250530","label":"Archaeoglobi archaeon","rank":"SPECIES","parent_id":"NCBITaxon:1935015","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb","retired_into":"","taxonomy_snapshot":"2026-09-13"}; line 621140: {"taxon_id":"NCBITaxon:3366610","label":"Methanobacteriati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"} | supports | Inspected the target and each carried ancestor, rank, parent, genetic code and source name classes. |
| scope-row | curation/seed_scope.tsv; line 93317: {"identifier":"NCBITaxon:2250530","added":"2026-09-13","reason":"attested rule: Archaeoglobi archaeon, 2 sources incl. NCBI"} | supports | Exact target is included in the declared seed scope. |
| path-row | data/taxa/PATHS.tsv; line 334847: {"identifier":"NCBITaxon:2250530","slug":"archaeoglobi_archaeon"} | supports | Indexed path resolves to this exact NCBI taxon. |
| ncbi-live | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=2012529,2250530,1935016,2234,224325,1344584,403219,1121009,138903,2798580; TaxaSet/Taxon[TaxId='2250530']; ten-target captured response | supports | Inspected the official response for this exact taxon: scientific name, rank, parent, source name classes, lineage and genetic code. Current authority and pinned September inventory remain distinct observations. |
| lpsn-inventory | data/raw/lpsn_names.tsv; line 21971: {"lpsn_id":"lpsn:783902","name":"Geoglobus ahangari","rank":"SPECIES","authority":"Kashefi et al. 2002","url":"https://lpsn.dsmz.de/species/geoglobus-ahangari","deprecated":"0","status":"legitimate=True; validly published under the ICNP; correct name","validly_published":"1","legitimate":"1","is_correct_name":"1","parent_lpsn_id":"lpsn:517237","ncbitaxon_ids":"NCBITaxon:113653","gtdb_ids":"GTDB:s__Geoglobus_ahangari","type_strain_ids":"kgmicrobe.strain:ATCC-BAA-425&#124;kgmicrobe.strain:DSM-27542","synonym_of":"","synonyms":"","publications":"PMID:12054231&#124;doi:10.1099/ijs.0.01953-0&#124;doi:10.1099/ijs.0.02435-0","sequence_accessions":"INSDC:AF220165"} | supports | Inspected exact mapped and linked LPSN names; bounded inventory absence does not establish worldwide nomenclatural absence. |
| gtdb-mappings | data/raw/gtdb_mappings.tsv; line 6158: {"gtdb_id":"GTDB:s__Geoglobus_ahangari","gtdb_label":"s__Geoglobus_ahangari","gtdb_parent":"GTDB:g__Geoglobus","ncbitaxon_id":"NCBITaxon:113653","predicate":"skos:closeMatch","genome_count":"2"}; line 98719: {"gtdb_id":"GTDB:s__JdFR-42_sp002010305","gtdb_label":"s__JdFR-42_sp002010305","gtdb_parent":"GTDB:g__JdFR-42","ncbitaxon_id":"NCBITaxon:1935016","predicate":"skos:closeMatch","genome_count":"2"}; line 178158: {"gtdb_id":"GTDB:s__WYZ-LMO2_sp004347865","gtdb_label":"s__WYZ-LMO2_sp004347865","gtdb_parent":"GTDB:g__WYZ-LMO2","ncbitaxon_id":"NCBITaxon:2250258","predicate":"skos:broadMatch","genome_count":"4"}; line 178627: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259335","gtdb_label":"s__Archaeoglobus_sp029259335","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"2"}; line 178628: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259345","gtdb_label":"s__Archaeoglobus_sp029259345","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"1"}; line 178629: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259415","gtdb_label":"s__Archaeoglobus_sp029259415","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"1"}; line 178630: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259455","gtdb_label":"s__Archaeoglobus_sp029259455","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"1"}; line 178631: {"gtdb_id":"GTDB:s__B5-G16_sp021163065","gtdb_label":"s__B5-G16_sp021163065","gtdb_parent":"GTDB:g__B5-G16","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"2"}; line 178632: {"gtdb_id":"GTDB:s__Geoglobus_ahangari","gtdb_label":"s__Geoglobus_ahangari","gtdb_parent":"GTDB:g__Geoglobus","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"2"}; line 178633: {"gtdb_id":"GTDB:s__JdFR-42_sp002010305","gtdb_label":"s__JdFR-42_sp002010305","gtdb_parent":"GTDB:g__JdFR-42","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"2"}; line 178634: {"gtdb_id":"GTDB:s__Mnemosynella_bozhongmuii","gtdb_label":"s__Mnemosynella_bozhongmuii","gtdb_parent":"GTDB:g__Mnemosynella","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"3"}; line 178635: {"gtdb_id":"GTDB:s__WYZ-LMO2_sp004347865","gtdb_label":"s__WYZ-LMO2_sp004347865","gtdb_parent":"GTDB:g__WYZ-LMO2","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"4"}; line 196440: {"gtdb_id":"GTDB:s__B5-G16_sp021163065","gtdb_label":"s__B5-G16_sp021163065","gtdb_parent":"GTDB:g__B5-G16","ncbitaxon_id":"NCBITaxon:2511821","predicate":"skos:broadMatch","genome_count":"2"}; line 208008: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259335","gtdb_label":"s__Archaeoglobus_sp029259335","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:269247","predicate":"skos:closeMatch","genome_count":"2"}; line 255970: {"gtdb_id":"GTDB:s__Mnemosynella_bozhongmuii","gtdb_label":"s__Mnemosynella_bozhongmuii","gtdb_parent":"GTDB:g__Mnemosynella","ncbitaxon_id":"NCBITaxon:3072938","predicate":"skos:closeMatch","genome_count":"3"}; line 260291: {"gtdb_id":"GTDB:s__WYZ-LMO2_sp004347865","gtdb_label":"s__WYZ-LMO2_sp004347865","gtdb_parent":"GTDB:g__WYZ-LMO2","ncbitaxon_id":"NCBITaxon:3101521","predicate":"skos:closeMatch","genome_count":"4"} | supports | Inspected direct mappings and selected clusters' reverse mappings, retaining each source predicate and taxon boundary. |
| gtdb-species | data/raw/gtdb_species.tsv; line 12312: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259335","label":"s__Archaeoglobus_sp029259335","parent":"GTDB:g__Archaeoglobus","genome_count":"2"}; line 12313: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259345","label":"s__Archaeoglobus_sp029259345","parent":"GTDB:g__Archaeoglobus","genome_count":"1"}; line 12314: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259415","label":"s__Archaeoglobus_sp029259415","parent":"GTDB:g__Archaeoglobus","genome_count":"1"}; line 12315: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259455","label":"s__Archaeoglobus_sp029259455","parent":"GTDB:g__Archaeoglobus","genome_count":"1"}; line 14792: {"gtdb_id":"GTDB:s__B5-G16_sp021163065","label":"s__B5-G16_sp021163065","parent":"GTDB:g__B5-G16","genome_count":"2"}; line 69911: {"gtdb_id":"GTDB:s__Geoglobus_ahangari","label":"s__Geoglobus_ahangari","parent":"GTDB:g__Geoglobus","genome_count":"2"}; line 107304: {"gtdb_id":"GTDB:s__JdFR-42_sp002010305","label":"s__JdFR-42_sp002010305","parent":"GTDB:g__JdFR-42","genome_count":"2"}; line 121996: {"gtdb_id":"GTDB:s__Mnemosynella_bozhongmuii","label":"s__Mnemosynella_bozhongmuii","parent":"GTDB:g__Mnemosynella","genome_count":"3"}; line 198199: {"gtdb_id":"GTDB:s__WYZ-LMO2_sp004347865","label":"s__WYZ-LMO2_sp004347865","parent":"GTDB:g__WYZ-LMO2","genome_count":"4"} | supports | Inspected source species identifiers, labels, parent clusters and genome counts. |
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
| genome-catalog-1 | data/catalog/gtdb_genomes-0017.jsonl.gz; line 29829: {"accession":"GB_GCA_021163065.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__B5-G16;s__B5-G16 sp021163065","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2116306v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA713414","ncbi_biosample":"SAMN18353649","ncbi_contig_count":"234","ncbi_contig_n50":"10604","ncbi_country":"Pacific Ocean: Mexico; Pescadero Basin","ncbi_date":"2021-12-10","ncbi_genbank_assembly_accession":"GCA_021163065.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"AUK153","ncbi_isolation_source":"marine hydrothermal sediment","ncbi_lat_lon":"23.957043 N 108.862273 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobaceae archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2021-12-10","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2511821","ncbi_ssu_count":"1","ncbi_strain_identifiers":"AUK153","ncbi_submitter":"California Institute of Technology","ncbi_taxid":"2511821","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;x__unclassified Archaeoglobaceae;s__Archaeoglobaceae archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1905055","ncbi_translation_table":"11","ncbi_trna_count":"45","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1905055","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAGGXN000000000.1"}; line 30412: {"accession":"GB_GCA_029259415.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus sp029259415","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2925941v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA891685","ncbi_biosample":"SAMN31357530","ncbi_contig_count":"104","ncbi_contig_n50":"27508","ncbi_country":"Mexico: Guaymas Basin; Gulf of California","ncbi_date":"2023-03-17","ncbi_genbank_assembly_accession":"GCA_029259415.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"S5B4_HD70","ncbi_isolation_source":"hydrothermal vent sediment; anoxic hexadecane-degrading enrichment at 70 degrees Celsius","ncbi_lat_lon":"27.0075 N 111.409 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-03-17","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"none","ncbi_strain_identifiers":"S5B4_HD70","ncbi_submitter":"Max Planck Institute for Marine Microbiology","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1941972","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1941972","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAPDIW000000000.1"}; line 31243: {"accession":"GB_GCA_965552265.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus sp029259335","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"SRR24791474_maxbin2_1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJEB88069","ncbi_biosample":"SAMEA118547580","ncbi_contig_count":"158","ncbi_contig_n50":"25832","ncbi_country":"none","ncbi_date":"2025-07-08","ncbi_genbank_assembly_accession":"GCA_965552265.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SRR24791474_maxbin2_1","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"uncultured Archaeoglobus sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2025-07-08","ncbi_spanned_gaps":"0","ncbi_species_taxid":"269247","ncbi_ssu_count":"none","ncbi_strain_identifiers":"SRR24791474_maxbin2_1","ncbi_submitter":"EMG","ncbi_taxid":"269247","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__environmental samples;s__uncultured Archaeoglobus sp.","ncbi_total_gap_length":"0","ncbi_total_length":"2357242","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2357242","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"CBEVRN000000000.1"}; line 31723: {"accession":"GB_GCA_011605875.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2 sp004347865","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM1160587v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA604268","ncbi_biosample":"SAMN13964306","ncbi_contig_count":"73","ncbi_contig_n50":"31899","ncbi_country":"USA: Yellowstone National Park; Smokejumper3 Hot Spring","ncbi_date":"2020-03-22","ncbi_genbank_assembly_accession":"GCA_011605875.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SJ3.Bin34","ncbi_isolation_source":"sediments from hot spring shelf","ncbi_lat_lon":"44.41595 N 110.9558 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobales archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"1","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2020-03-22","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250258","ncbi_ssu_count":"0","ncbi_strain_identifiers":"SJ3.Bin34","ncbi_submitter":"Montana State University","ncbi_taxid":"2250258","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;x__unclassified Archaeoglobales;s__Archaeoglobales archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1467518","ncbi_translation_table":"11","ncbi_trna_count":"42","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1467518","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAAOZH000000000.1"}; line 33626: {"accession":"GB_GCA_036867765.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2 sp004347865","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM3686776v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA1014417","ncbi_biosample":"SAMN39201948","ncbi_contig_count":"20","ncbi_contig_n50":"147257","ncbi_country":"none","ncbi_date":"2024-02-25","ncbi_genbank_assembly_accession":"GCA_036867765.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"LCB24","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Candidatus Methanoglobus sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"19","ncbi_scaffold_l50":"5","ncbi_scaffold_n50":"147257","ncbi_scaffold_n75":"85097","ncbi_scaffold_n90":"45659","ncbi_seq_rel_date":"2024-02-25","ncbi_spanned_gaps":"1","ncbi_species_taxid":"3101521","ncbi_ssu_count":"1","ncbi_strain_identifiers":"LCB24","ncbi_submitter":"Montana State University","ncbi_taxid":"3101521","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Candidatus Methanoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Candidatus Methanoglobus;x__unclassified Candidatus Methanoglobus;s__Candidatus Methanoglobus sp.","ncbi_total_gap_length":"100","ncbi_total_length":"1623778","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1623678","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JBAJGN000000000.1"}; line 35414: {"accession":"GB_GCA_014361165.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Mnemosynellales;f__Mnemosynellaceae;g__Mnemosynella;s__Mnemosynella bozhongmuii","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM1436116v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA635524","ncbi_biosample":"SAMN15637566","ncbi_contig_count":"159","ncbi_contig_n50":"13044","ncbi_country":"China: Dongying","ncbi_date":"2020-09-01","ncbi_genbank_assembly_accession":"GCA_014361165.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"MAG-16","ncbi_isolation_source":"Shengli oilfield at Shandong province","ncbi_lat_lon":"38.15 N 118.5 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Candidatus Mnemosynella bozhongmuii","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"2","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2020-09-01","ncbi_spanned_gaps":"0","ncbi_species_taxid":"3072938","ncbi_ssu_count":"1","ncbi_strain_identifiers":"MAG-16","ncbi_submitter":"East China University of Science and Technology","ncbi_taxid":"3072938","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Candidatus Mnemosynellales;f__Candidatus Mnemosynellaceae;g__Candidatus Mnemosynella;s__Candidatus Mnemosynella bozhongmuii","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Candidatus Mnemosynellales;f__Candidatus Mnemosynellaceae;g__Candidatus Mnemosynella;s__Candidatus Mnemosynella bozhongmuii","ncbi_total_gap_length":"0","ncbi_total_length":"1166237","ncbi_translation_table":"11","ncbi_trna_count":"34","ncbi_type_material_designation":"assembly from type material","ncbi_ungapped_length":"1166237","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JACIWD000000000.1"}; line 38660: {"accession":"GB_GCA_004347865.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2 sp004347865","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM434786v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA475886","ncbi_biosample":"SAMN09404985","ncbi_contig_count":"220","ncbi_contig_n50":"10901","ncbi_country":"USA: Yellowstone National Park; Wyoming; USA","ncbi_date":"2019-03-12","ncbi_genbank_assembly_accession":"GCA_004347865.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"WYZ-LMO2","ncbi_isolation_source":"hot springs sediment","ncbi_lat_lon":"44.6100 N 110.4400 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"1","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2019-03-12","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"0","ncbi_strain_identifiers":"WYZ-LMO2","ncbi_submitter":"Shanghai Jiao Tong University","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1514415","ncbi_translation_table":"11","ncbi_trna_count":"44","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1514415","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"QNUZ00000000.1"}; line 39381: {"accession":"GB_GCA_013151125.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Geoglobus;s__Geoglobus ahangari","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM1315112v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA557557","ncbi_biosample":"SAMN12405721","ncbi_contig_count":"181","ncbi_contig_n50":"8575","ncbi_country":"Pacific Ocean: East Pacific Rise","ncbi_date":"2020-05-22","ncbi_genbank_assembly_accession":"GCA_013151125.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"M_MetaBat.67","ncbi_isolation_source":"Deepsea hydrothermal sulfide chimney","ncbi_lat_lon":"9.7712 N 104.2789 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"2","ncbi_scaffold_count":"163","ncbi_scaffold_l50":"43","ncbi_scaffold_n50":"9877","ncbi_scaffold_n75":"6138","ncbi_scaffold_n90":"4287","ncbi_seq_rel_date":"2020-05-22","ncbi_spanned_gaps":"18","ncbi_species_taxid":"2250530","ncbi_ssu_count":"1","ncbi_strain_identifiers":"M_MetaBat.67","ncbi_submitter":"Lab of Microbial Oceanography","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"1128","ncbi_total_length":"1352038","ncbi_translation_table":"11","ncbi_trna_count":"36","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1350910","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAADIT000000000.1"}; line 39729: {"accession":"GB_GCA_029259335.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus sp029259335","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2925933v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA891685","ncbi_biosample":"SAMN31357532","ncbi_contig_count":"101","ncbi_contig_n50":"24995","ncbi_country":"Mexico: Guaymas Basin; Gulf of California","ncbi_date":"2023-03-17","ncbi_genbank_assembly_accession":"GCA_029259335.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"S5B9_HD70","ncbi_isolation_source":"hydrothermal vent sediment; anoxic hexadecane-degrading enrichment at 70 degrees Celsius","ncbi_lat_lon":"27.0075 N 111.409 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-03-17","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"none","ncbi_strain_identifiers":"S5B9_HD70","ncbi_submitter":"Max Planck Institute for Marine Microbiology","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1749908","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1749908","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAPDIY000000000.1"}; line 41225: {"accession":"GB_GCA_029259345.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus sp029259345","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM2925934v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA891685","ncbi_biosample":"SAMN31357531","ncbi_contig_count":"89","ncbi_contig_n50":"24936","ncbi_country":"Mexico: Guaymas Basin; Gulf of California","ncbi_date":"2023-03-17","ncbi_genbank_assembly_accession":"GCA_029259345.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"S5B8_HD70","ncbi_isolation_source":"hydrothermal vent sediment; anoxic hexadecane-degrading enrichment at 70 degrees Celsius","ncbi_lat_lon":"27.0075 N 111.409 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"88","ncbi_scaffold_l50":"20","ncbi_scaffold_n50":"24936","ncbi_scaffold_n75":"17574","ncbi_scaffold_n90":"8601","ncbi_seq_rel_date":"2023-03-17","ncbi_spanned_gaps":"1","ncbi_species_taxid":"2250530","ncbi_ssu_count":"none","ncbi_strain_identifiers":"S5B8_HD70","ncbi_submitter":"Max Planck Institute for Marine Microbiology","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"10","ncbi_total_length":"1486306","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1486296","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAPDIX000000000.1"}; line 43252: {"accession":"GB_GCA_029982835.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Mnemosynellales;f__Mnemosynellaceae;g__Mnemosynella;s__Mnemosynella bozhongmuii","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2998283v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA308326","ncbi_biosample":"SAMN33401079","ncbi_contig_count":"100","ncbi_contig_n50":"9386","ncbi_country":"USA: Colorado","ncbi_date":"2023-05-11","ncbi_genbank_assembly_accession":"GCA_029982835.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"DJKA110_ANT-KO_bin.29","ncbi_isolation_source":"Produced fluids from hydraulically fractured shales","ncbi_lat_lon":"40.411582 N 104.348363 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"0","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-05-11","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"0","ncbi_strain_identifiers":"DJKA110_ANT-KO_bin.29","ncbi_submitter":"The Ohio State University","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"942654","ncbi_translation_table":"11","ncbi_trna_count":"0","ncbi_type_material_designation":"na","ncbi_ungapped_length":"942654","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JARRCA000000000.1"}; line 43594: {"accession":"RS_GCF_001006045.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Geoglobus;s__Geoglobus ahangari","gtdb_type_species_of_genus":"t","ncbi_assembly_level":"Complete Genome","ncbi_assembly_name":"ASM100604v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN02988852","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"USA: Guaymas basin","ncbi_date":"2015-05-11","ncbi_genbank_assembly_accession":"GCA_001006045.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"marine hydrothermal vent","ncbi_lat_lon":"27 N 111 W","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Geoglobus ahangari","ncbi_protein_count":"2007","ncbi_refseq_category":"reference genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"1770093","ncbi_scaffold_n75":"1770093","ncbi_scaffold_n90":"1770093","ncbi_seq_rel_date":"2015-05-11","ncbi_spanned_gaps":"0","ncbi_species_taxid":"113653","ncbi_ssu_count":"1","ncbi_strain_identifiers":"234","ncbi_submitter":"Michigan State University","ncbi_taxid":"113653","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Geoglobus;s__Geoglobus ahangari","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Geoglobus;s__Geoglobus ahangari","ncbi_total_gap_length":"0","ncbi_total_length":"1770093","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"assembly from type material","ncbi_ungapped_length":"1770093","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"}; line 43618: {"accession":"GB_GCA_024437945.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2 sp004347865","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2443794v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA859922","ncbi_biosample":"SAMN29809817","ncbi_contig_count":"179","ncbi_contig_n50":"8067","ncbi_country":"USA: Yellowstone National Park; WY","ncbi_date":"2022-07-25","ncbi_genbank_assembly_accession":"GCA_024437945.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"LCB024-003","ncbi_isolation_source":"hot spring sediment","ncbi_lat_lon":"44.57347 N 110.79504 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"2","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2022-07-25","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"0","ncbi_strain_identifiers":"LCB024-003","ncbi_submitter":"Montana State University","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1156727","ncbi_translation_table":"11","ncbi_trna_count":"33","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1156727","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JANFND000000000.1"}; line 45221: {"accession":"GB_GCA_029259455.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus sp029259455","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2925945v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA891685","ncbi_biosample":"SAMN31357527","ncbi_contig_count":"82","ncbi_contig_n50":"15423","ncbi_country":"Mexico: Guaymas Basin; Gulf of California","ncbi_date":"2023-03-17","ncbi_genbank_assembly_accession":"GCA_029259455.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"S5B11_HD70","ncbi_isolation_source":"hydrothermal vent sediment; anoxic hexadecane-degrading enrichment at 70 degrees Celsius","ncbi_lat_lon":"27.0075 N 111.409 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-03-17","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"none","ncbi_strain_identifiers":"S5B11_HD70","ncbi_submitter":"Max Planck Institute for Marine Microbiology","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"879016","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"879016","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAPDIT000000000.1"}; line 45671: {"accession":"GB_GCA_002010305.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__JdFR-42;g__JdFR-42;s__JdFR-42 sp002010305","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM201030v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA269163","ncbi_biosample":"SAMN06226359","ncbi_contig_count":"42","ncbi_contig_n50":"70809","ncbi_country":"Pacific Ocean","ncbi_date":"2017-03-02","ncbi_genbank_assembly_accession":"GCA_002010305.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"JdFR-42","ncbi_isolation_source":"basaltic crustal fluids","ncbi_lat_lon":"47.76 N 127.76 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobi archaeon JdFR-42","ncbi_protein_count":"0","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2017-03-02","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1935016","ncbi_ssu_count":"none","ncbi_strain_identifiers":"JdFR-42","ncbi_submitter":"University of Hawaii","ncbi_taxid":"1935016","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified Archaeoglobi;s__Archaeoglobi archaeon JdFR-42","ncbi_total_gap_length":"0","ncbi_total_length":"2148619","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2148619","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"MTND00000000.1"}; line 46752: {"accession":"GB_GCA_003935005.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__JdFR-42;g__JdFR-42;s__JdFR-42 sp002010305","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM393500v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA266365","ncbi_biosample":"SAMN10474933","ncbi_contig_count":"24","ncbi_contig_n50":"113045","ncbi_country":"Pacific Ocean: Juan de Fuca Ridge","ncbi_date":"2018-12-11","ncbi_genbank_assembly_accession":"GCA_003935005.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"rG16","ncbi_isolation_source":"basaltic crust aquifer fluid","ncbi_lat_lon":"47.76 N 127.76 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"21","ncbi_scaffold_l50":"4","ncbi_scaffold_n50":"233158","ncbi_scaffold_n75":"78927","ncbi_scaffold_n90":"57605","ncbi_seq_rel_date":"2018-12-11","ncbi_spanned_gaps":"3","ncbi_species_taxid":"2250530","ncbi_ssu_count":"none","ncbi_strain_identifiers":"rG16","ncbi_submitter":"University of Hawaii","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"300","ncbi_total_length":"2128522","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2128222","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"RSFX00000000.1"} | supports | Inspected every selected GTDB cluster member, exact taxid/species-taxid, culture identifiers and accession versions. Species membership alone is not a strain identity. |
| genome-catalog-2 | data/catalog/gtdb_genomes-0018.jsonl.gz; line 257: {"accession":"GB_GCA_029259425.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__B5-G16;s__B5-G16 sp021163065","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2925942v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA891685","ncbi_biosample":"SAMN31357529","ncbi_contig_count":"112","ncbi_contig_n50":"30933","ncbi_country":"Mexico: Guaymas Basin; Gulf of California","ncbi_date":"2023-03-17","ncbi_genbank_assembly_accession":"GCA_029259425.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"S5B2_HD70","ncbi_isolation_source":"hydrothermal vent sediment; anoxic hexadecane-degrading enrichment at 70 degrees Celsius","ncbi_lat_lon":"27.0075 N 111.409 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-03-17","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"none","ncbi_strain_identifiers":"S5B2_HD70","ncbi_submitter":"Max Planck Institute for Marine Microbiology","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"2003750","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2003750","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAPDIV000000000.1"}; line 704: {"accession":"GB_GCA_030153425.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Mnemosynellales;f__Mnemosynellaceae;g__Mnemosynella;s__Mnemosynella bozhongmuii","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM3015342v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA308326","ncbi_biosample":"SAMN33401153","ncbi_contig_count":"70","ncbi_contig_n50":"21655","ncbi_country":"USA: Colorado","ncbi_date":"2023-06-02","ncbi_genbank_assembly_accession":"GCA_030153425.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"DJKA128_NP-F35_bin.23","ncbi_isolation_source":"Produced fluids from hydraulically fractured shales","ncbi_lat_lon":"40.411582 N 104.348363 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"0","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-06-02","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"0","ncbi_strain_identifiers":"DJKA128_NP-F35_bin.23","ncbi_submitter":"The Ohio State University","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1191577","ncbi_translation_table":"11","ncbi_trna_count":"0","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1191577","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JASKJO000000000.1"} | supports | Inspected every selected GTDB cluster member, exact taxid/species-taxid, culture identifiers and accession versions. Species membership alone is not a strain identity. |
| gtdb-full-scan | data/catalog/MANIFEST.json; {"target":"NCBITaxon:2250530","rank":"SPECIES","mappings":[{"source_id":"GTDB:s__WYZ-LMO2_sp004347865","predicate":"skos:broadMatch","genome_count":4,"ncbi_taxids":{"2250258":1,"3101521":1,"2250530":2},"ncbi_species_taxids":{"2250258":1,"3101521":1,"2250530":2},"members":[{"accession":"GB_GCA_011605875.1","ncbi_taxid":"2250258","ncbi_species_taxid":"2250258","ncbi_organism_name":"Archaeoglobales archaeon","ncbi_strain_identifiers":"SJ3.Bin34","ncbi_genbank_assembly_accession":"GCA_011605875.1"},{"accession":"GB_GCA_036867765.1","ncbi_taxid":"3101521","ncbi_species_taxid":"3101521","ncbi_organism_name":"Candidatus Methanoglobus sp.","ncbi_strain_identifiers":"LCB24","ncbi_genbank_assembly_accession":"GCA_036867765.1"},{"accession":"GB_GCA_004347865.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_strain_identifiers":"WYZ-LMO2","ncbi_genbank_assembly_accession":"GCA_004347865.1"},{"accession":"GB_GCA_024437945.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_strain_identifiers":"LCB024-003","ncbi_genbank_assembly_accession":"GCA_024437945.1"}]},{"source_id":"GTDB:s__Mnemosynella_bozhongmuii","predicate":"skos:broadMatch","genome_count":3,"ncbi_taxids":{"3072938":1,"2250530":2},"ncbi_species_taxids":{"3072938":1,"2250530":2},"members":[{"accession":"GB_GCA_014361165.1","ncbi_taxid":"3072938","ncbi_species_taxid":"3072938","ncbi_organism_name":"Candidatus Mnemosynella bozhongmuii","ncbi_strain_identifiers":"MAG-16","ncbi_genbank_assembly_accession":"GCA_014361165.1"},{"accession":"GB_GCA_029982835.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_strain_identifiers":"DJKA110_ANT-KO_bin.29","ncbi_genbank_assembly_accession":"GCA_029982835.1"},{"accession":"GB_GCA_030153425.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_strain_identifiers":"DJKA128_NP-F35_bin.23","ncbi_genbank_assembly_accession":"GCA_030153425.1"}]},{"source_id":"GTDB:s__Archaeoglobus_sp029259335","predicate":"skos:broadMatch","genome_count":2,"ncbi_taxids":{"269247":1,"2250530":1},"ncbi_species_taxids":{"269247":1,"2250530":1},"members":[{"accession":"GB_GCA_965552265.1","ncbi_taxid":"269247","ncbi_species_taxid":"269247","ncbi_organism_name":"uncultured Archaeoglobus sp.","ncbi_strain_identifiers":"SRR24791474_maxbin2_1","ncbi_genbank_assembly_accession":"GCA_965552265.1"},{"accession":"GB_GCA_029259335.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_strain_identifiers":"S5B9_HD70","ncbi_genbank_assembly_accession":"GCA_029259335.1"}]},{"source_id":"GTDB:s__B5-G16_sp021163065","predicate":"skos:broadMatch","genome_count":2,"ncbi_taxids":{"2511821":1,"2250530":1},"ncbi_species_taxids":{"2511821":1,"2250530":1},"members":[{"accession":"GB_GCA_021163065.1","ncbi_taxid":"2511821","ncbi_species_taxid":"2511821","ncbi_organism_name":"Archaeoglobaceae archaeon","ncbi_strain_identifiers":"AUK153","ncbi_genbank_assembly_accession":"GCA_021163065.1"},{"accession":"GB_GCA_029259425.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_strain_identifiers":"S5B2_HD70","ncbi_genbank_assembly_accession":"GCA_029259425.1"}]},{"source_id":"GTDB:s__Geoglobus_ahangari","predicate":"skos:broadMatch","genome_count":2,"ncbi_taxids":{"2250530":1,"113653":1},"ncbi_species_taxids":{"2250530":1,"113653":1},"members":[{"accession":"GB_GCA_013151125.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_strain_identifiers":"M_MetaBat.67","ncbi_genbank_assembly_accession":"GCA_013151125.1"},{"accession":"RS_GCF_001006045.1","ncbi_taxid":"113653","ncbi_species_taxid":"113653","ncbi_organism_name":"Geoglobus ahangari","ncbi_strain_identifiers":"234","ncbi_genbank_assembly_accession":"GCA_001006045.1"}]},{"source_id":"GTDB:s__JdFR-42_sp002010305","predicate":"skos:broadMatch","genome_count":2,"ncbi_taxids":{"1935016":1,"2250530":1},"ncbi_species_taxids":{"1935016":1,"2250530":1},"members":[{"accession":"GB_GCA_002010305.1","ncbi_taxid":"1935016","ncbi_species_taxid":"1935016","ncbi_organism_name":"Archaeoglobi archaeon JdFR-42","ncbi_strain_identifiers":"JdFR-42","ncbi_genbank_assembly_accession":"GCA_002010305.1"},{"accession":"GB_GCA_003935005.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_strain_identifiers":"rG16","ncbi_genbank_assembly_accession":"GCA_003935005.1"}]},{"source_id":"GTDB:s__Archaeoglobus_sp029259345","predicate":"skos:broadMatch","genome_count":1,"ncbi_taxids":{"2250530":1},"ncbi_species_taxids":{"2250530":1},"members":[{"accession":"GB_GCA_029259345.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_strain_identifiers":"S5B8_HD70","ncbi_genbank_assembly_accession":"GCA_029259345.1"}]},{"source_id":"GTDB:s__Archaeoglobus_sp029259415","predicate":"skos:broadMatch","genome_count":1,"ncbi_taxids":{"2250530":1},"ncbi_species_taxids":{"2250530":1},"members":[{"accession":"GB_GCA_029259415.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_strain_identifiers":"S5B4_HD70","ncbi_genbank_assembly_accession":"GCA_029259415.1"}]},{"source_id":"GTDB:s__Archaeoglobus_sp029259455","predicate":"skos:broadMatch","genome_count":1,"ncbi_taxids":{"2250530":1},"ncbi_species_taxids":{"2250530":1},"members":[{"accession":"GB_GCA_029259455.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi archaeon","ncbi_strain_identifiers":"S5B11_HD70","ncbi_genbank_assembly_accession":"GCA_029259455.1"}]}]} | supports | All nineteen GTDB shards were searched with exact terminal species tokens preserving internal genus suffix underscores. Source cluster counts and taxon distributions were assessed independently of exact-identity promotion. |
| finding-deduplication | Owned review worktrees structured bundles; {"target_index":2,"issue_key":"gtdb-broadmatch-note-other-taxa-2250530","finding_id":"pooled-note-other-taxa","target_ids":["NCBITaxon:2250530"],"matching_review_ids":[],"matching_findings":[],"result":"no duplicate stable issue key found"} | supports | No existing target-specific finding with this stable key was found in the bounded ignored-inclusive search. |
| strict-receipt | just validate-strict data/taxa/archaea/archaeoglobi_archaeon.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/strict-02.tsv; This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-20T07:29:26Z, finished 2026-10-20T07:29:27Z, exit 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times.<br>Validating 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0012/src/taxonmech/schema/taxonmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/strict-02.tsv |
| history-receipt | just validate-history; All 18 standalone history records; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T06:42:11Z, exit 0. All 18 standalone history records; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check.<br>history links: 18 record(s), 0 invalid<br>No issues found<br>18 history record(s) valid against src/taxonmech/schema/history.yaml |
| corpus-receipt | just verify-corpus; All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T06:48:01Z, exit 0. All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check.<br>uv run python scripts/verify_corpus.py <br>expected 626048 records, found 626048 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ and curation/seed_scope.tsv |
| products-receipt | just validate-products; Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T07:19:10Z, exit 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check.<br>uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml<br><br>id↔label correspondence summary:<br><br>✅ All id↔label pairs correspond. |
| qc-receipt | just qc; Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T07:50:51Z, exit 0. Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check.<br>All checks passed!<br>1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33)<br>Validating 626048 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0014/src/taxonmech/schema/taxonmech.yaml<br>  files scanned:      626048<br>expected 626048 records, found 626048 on disk<br>pages/ is current<br>Site publication: 530,946,096 bytes (budget 950,000,000)<br>626048 taxon records<br>  NCBITAXON        626048<br>All TaxonMech quality gates passed.<br>  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890 strains (not genome counts)<br>  Related STRAININFO_DEPOSIT: 107277 strain-record pairs, 106843 identifiers, 53890 strains (not genome counts)<br>  Related NUCLEOTIDE_SEQUENCE: 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)<br>LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809 records mapped, 324404579 genomes summed across record attestations (not deduplicated)<br>Causal graphs: 0 records (0 evidence-backed edges)<br><br>All TaxonMech quality gates passed. |

## Limits And Additional Notes

- The review assesses exact identifiers, nomenclature, source placement and import completeness at the captured versions; it does not establish experimental phenotypes, assembly sequence equivalence or a phylogenetic species boundary.
- Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check.
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base recapture preserves target/source-table bytes; five changed guidance/scope/path/seeder inputs were explicitly reassessed. Original captures and exact transition receipts remain retained.
- Every new bundle still requires its own validate/save/check recipe; baseline native receipts do not claim these later steps have run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T075202Z-archaeoglobi_archaeon
kind: record
repository: CultureBotAI/TaxonMech
title: 'Record review: Archaeoglobi archaeon'
started_at: '2026-10-20T07:29:19Z'
finished_at: '2026-10-21T07:52:02Z'
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
summary: 'Archaeoglobi archaeon has supported exact NCBI identity and source-scoped
  representation. Three singleton cluster notes overstate other-taxon membership. '
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
  - path: data/taxa/archaea/archaeoglobi_archaeon.yaml
    sha256: 8addef5f490d1cf2d3fb9c31287418ee752ac8c4e74304be851325178b1f53e0
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
  selection: Original unreviewed path-order position 132; batch-0014 target 2. Excluded
    185 actual targets from validated freshmain and thirteen committed isolated branches;
    full corpus enumeration includes ignored files.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - NCBITaxon:2250530
targets:
- target_id: NCBITaxon:2250530
  path: data/taxa/archaea/archaeoglobi_archaeon.yaml
  label: Archaeoglobi archaeon
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
  summary: NCBITaxon:2250530 denotes Archaeoglobi archaeon at SPECIES rank beneath
    NCBITaxon:1935015, genetic code 11. All 7 carried ancestors agree with the pinned
    inventory and captured official NCBI response; the response omits only the root
    entry. Source name classes remain distinct from taxon classification.
  target_ids:
  - NCBITaxon:2250530
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
    taxa). All imported counts agree with their own source units: NCBITAXON 1 NAME;
    GTDB 4 GENOME. Counts of organisms, media, traits and genome assertions are not
    interchangeable and do not prove phenotype or biological genome equivalence. GTDB
    primary count 4 denotes the first cluster and eight further clusters are recorded;
    total 18 cluster members are not the primary attestation count.'
  target_ids:
  - NCBITaxon:2250530
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
  - genome-catalog-2
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
  - NCBITaxon:2250530
  evidence_ids:
  - gtdb-full-scan
  - gtdb-species
  - gtdb-mappings
  - genome-catalog-1
  - genome-catalog-2
  scope_note: All nineteen pinned shards; full selected cluster populations and reverse
    mapping rows.
- check_id: strain-genome-evidence
  name: Imported strain links
  status: not_applicable
  required: false
  summary: No imported BacDive strain or strain-level link is asserted; no deposit
    is inferred from an isolate designation.
  target_ids:
  - NCBITaxon:2250530
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
  - NCBITaxon:2250530
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
  - NCBITaxon:2250530
  evidence_ids:
  - strict-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/uv-cache
    just validate-strict data/taxa/archaea/archaeoglobi_archaeon.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/strict-02.tsv
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
  - NCBITaxon:2250530
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
  - NCBITaxon:2250530
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
  - NCBITaxon:2250530
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
  - NCBITaxon:2250530
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
  reference: data/taxa/archaea/archaeoglobi_archaeon.yaml
  accessed_at: '2026-10-21T07:52:02Z'
  support: supports
  summary: Read the entire generated YAML, including identity, lineage, names, mappings,
    source attestations, all imported strains and links, and seed history.
  locator: entire TaxonRecord; identifier=NCBITaxon:2250530
  snapshot_sha256: 8addef5f490d1cf2d3fb9c31287418ee752ac8c4e74304be851325178b1f53e0
- evidence_id: taxonomy-inventory
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-21T06:43:34Z'
  support: supports
  summary: Inspected the target and each carried ancestor, rank, parent, genetic code
    and source name classes.
  locator: 'line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""};
    line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"};
    line 2981: {"taxon_id":"NCBITaxon:28890","label":"Methanobacteriota","rank":"PHYLUM","parent_id":"NCBITaxon:3366610"};
    line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"};
    line 36620: {"taxon_id":"NCBITaxon:183980","label":"Archaeoglobi","rank":"CLASS","parent_id":"NCBITaxon:28890"};
    line 496673: {"taxon_id":"NCBITaxon:1935015","label":"unclassified Archaeoglobi","rank":"NO_RANK","parent_id":"NCBITaxon:183980"};
    line 522268: {"taxon_id":"NCBITaxon:2250530","label":"Archaeoglobi archaeon","rank":"SPECIES","parent_id":"NCBITaxon:1935015","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon|gtdb","retired_into":"","taxonomy_snapshot":"2026-09-13"};
    line 621140: {"taxon_id":"NCBITaxon:3366610","label":"Methanobacteriati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
- evidence_id: scope-row
  kind: database
  reference: curation/seed_scope.tsv
  accessed_at: '2026-10-21T06:43:34Z'
  support: supports
  summary: Exact target is included in the declared seed scope.
  locator: 'line 93317: {"identifier":"NCBITaxon:2250530","added":"2026-09-13","reason":"attested
    rule: Archaeoglobi archaeon, 2 sources incl. NCBI"}'
  snapshot_sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
- evidence_id: path-row
  kind: database
  reference: data/taxa/PATHS.tsv
  accessed_at: '2026-10-21T06:43:34Z'
  support: supports
  summary: Indexed path resolves to this exact NCBI taxon.
  locator: 'line 334847: {"identifier":"NCBITaxon:2250530","slug":"archaeoglobi_archaeon"}'
  snapshot_sha256: f8f2e0721cb6839b30530b44be0d3004b9f0e6e2d4be8736f235b10117a8bd99
- evidence_id: ncbi-live
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=2012529,2250530,1935016,2234,224325,1344584,403219,1121009,138903,2798580
  accessed_at: '2026-10-20T07:29:20Z'
  support: supports
  summary: 'Inspected the official response for this exact taxon: scientific name,
    rank, parent, source name classes, lineage and genetic code. Current authority
    and pinned September inventory remain distinct observations.'
  locator: TaxaSet/Taxon[TaxId='2250530']; ten-target captured response
  snapshot_sha256: 8a3866adad1ff61fdfd0bfdd06ad5f4159708e114acc5cb803032f23e4828b9f
- evidence_id: lpsn-inventory
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-21T06:43:34Z'
  support: supports
  summary: Inspected exact mapped and linked LPSN names; bounded inventory absence
    does not establish worldwide nomenclatural absence.
  locator: 'line 21971: {"lpsn_id":"lpsn:783902","name":"Geoglobus ahangari","rank":"SPECIES","authority":"Kashefi
    et al. 2002","url":"https://lpsn.dsmz.de/species/geoglobus-ahangari","deprecated":"0","status":"legitimate=True;
    validly published under the ICNP; correct name","validly_published":"1","legitimate":"1","is_correct_name":"1","parent_lpsn_id":"lpsn:517237","ncbitaxon_ids":"NCBITaxon:113653","gtdb_ids":"GTDB:s__Geoglobus_ahangari","type_strain_ids":"kgmicrobe.strain:ATCC-BAA-425|kgmicrobe.strain:DSM-27542","synonym_of":"","synonyms":"","publications":"PMID:12054231|doi:10.1099/ijs.0.01953-0|doi:10.1099/ijs.0.02435-0","sequence_accessions":"INSDC:AF220165"}'
  snapshot_sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
- evidence_id: gtdb-mappings
  kind: database
  reference: data/raw/gtdb_mappings.tsv
  accessed_at: '2026-10-21T06:43:34Z'
  support: supports
  summary: Inspected direct mappings and selected clusters' reverse mappings, retaining
    each source predicate and taxon boundary.
  locator: 'line 6158: {"gtdb_id":"GTDB:s__Geoglobus_ahangari","gtdb_label":"s__Geoglobus_ahangari","gtdb_parent":"GTDB:g__Geoglobus","ncbitaxon_id":"NCBITaxon:113653","predicate":"skos:closeMatch","genome_count":"2"};
    line 98719: {"gtdb_id":"GTDB:s__JdFR-42_sp002010305","gtdb_label":"s__JdFR-42_sp002010305","gtdb_parent":"GTDB:g__JdFR-42","ncbitaxon_id":"NCBITaxon:1935016","predicate":"skos:closeMatch","genome_count":"2"};
    line 178158: {"gtdb_id":"GTDB:s__WYZ-LMO2_sp004347865","gtdb_label":"s__WYZ-LMO2_sp004347865","gtdb_parent":"GTDB:g__WYZ-LMO2","ncbitaxon_id":"NCBITaxon:2250258","predicate":"skos:broadMatch","genome_count":"4"};
    line 178627: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259335","gtdb_label":"s__Archaeoglobus_sp029259335","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"2"};
    line 178628: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259345","gtdb_label":"s__Archaeoglobus_sp029259345","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"1"};
    line 178629: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259415","gtdb_label":"s__Archaeoglobus_sp029259415","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"1"};
    line 178630: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259455","gtdb_label":"s__Archaeoglobus_sp029259455","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"1"};
    line 178631: {"gtdb_id":"GTDB:s__B5-G16_sp021163065","gtdb_label":"s__B5-G16_sp021163065","gtdb_parent":"GTDB:g__B5-G16","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"2"};
    line 178632: {"gtdb_id":"GTDB:s__Geoglobus_ahangari","gtdb_label":"s__Geoglobus_ahangari","gtdb_parent":"GTDB:g__Geoglobus","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"2"};
    line 178633: {"gtdb_id":"GTDB:s__JdFR-42_sp002010305","gtdb_label":"s__JdFR-42_sp002010305","gtdb_parent":"GTDB:g__JdFR-42","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"2"};
    line 178634: {"gtdb_id":"GTDB:s__Mnemosynella_bozhongmuii","gtdb_label":"s__Mnemosynella_bozhongmuii","gtdb_parent":"GTDB:g__Mnemosynella","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"3"};
    line 178635: {"gtdb_id":"GTDB:s__WYZ-LMO2_sp004347865","gtdb_label":"s__WYZ-LMO2_sp004347865","gtdb_parent":"GTDB:g__WYZ-LMO2","ncbitaxon_id":"NCBITaxon:2250530","predicate":"skos:broadMatch","genome_count":"4"};
    line 196440: {"gtdb_id":"GTDB:s__B5-G16_sp021163065","gtdb_label":"s__B5-G16_sp021163065","gtdb_parent":"GTDB:g__B5-G16","ncbitaxon_id":"NCBITaxon:2511821","predicate":"skos:broadMatch","genome_count":"2"};
    line 208008: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259335","gtdb_label":"s__Archaeoglobus_sp029259335","gtdb_parent":"GTDB:g__Archaeoglobus","ncbitaxon_id":"NCBITaxon:269247","predicate":"skos:closeMatch","genome_count":"2"};
    line 255970: {"gtdb_id":"GTDB:s__Mnemosynella_bozhongmuii","gtdb_label":"s__Mnemosynella_bozhongmuii","gtdb_parent":"GTDB:g__Mnemosynella","ncbitaxon_id":"NCBITaxon:3072938","predicate":"skos:closeMatch","genome_count":"3"};
    line 260291: {"gtdb_id":"GTDB:s__WYZ-LMO2_sp004347865","gtdb_label":"s__WYZ-LMO2_sp004347865","gtdb_parent":"GTDB:g__WYZ-LMO2","ncbitaxon_id":"NCBITaxon:3101521","predicate":"skos:closeMatch","genome_count":"4"}'
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
- evidence_id: gtdb-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-21T06:43:34Z'
  support: supports
  summary: Inspected source species identifiers, labels, parent clusters and genome
    counts.
  locator: 'line 12312: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259335","label":"s__Archaeoglobus_sp029259335","parent":"GTDB:g__Archaeoglobus","genome_count":"2"};
    line 12313: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259345","label":"s__Archaeoglobus_sp029259345","parent":"GTDB:g__Archaeoglobus","genome_count":"1"};
    line 12314: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259415","label":"s__Archaeoglobus_sp029259415","parent":"GTDB:g__Archaeoglobus","genome_count":"1"};
    line 12315: {"gtdb_id":"GTDB:s__Archaeoglobus_sp029259455","label":"s__Archaeoglobus_sp029259455","parent":"GTDB:g__Archaeoglobus","genome_count":"1"};
    line 14792: {"gtdb_id":"GTDB:s__B5-G16_sp021163065","label":"s__B5-G16_sp021163065","parent":"GTDB:g__B5-G16","genome_count":"2"};
    line 69911: {"gtdb_id":"GTDB:s__Geoglobus_ahangari","label":"s__Geoglobus_ahangari","parent":"GTDB:g__Geoglobus","genome_count":"2"};
    line 107304: {"gtdb_id":"GTDB:s__JdFR-42_sp002010305","label":"s__JdFR-42_sp002010305","parent":"GTDB:g__JdFR-42","genome_count":"2"};
    line 121996: {"gtdb_id":"GTDB:s__Mnemosynella_bozhongmuii","label":"s__Mnemosynella_bozhongmuii","parent":"GTDB:g__Mnemosynella","genome_count":"3"};
    line 198199: {"gtdb_id":"GTDB:s__WYZ-LMO2_sp004347865","label":"s__WYZ-LMO2_sp004347865","parent":"GTDB:g__WYZ-LMO2","genome_count":"4"}'
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
- evidence_id: bacdive-inventory
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-21T06:43:34Z'
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
  accessed_at: '2026-10-21T06:43:34Z'
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
  accessed_at: '2026-10-21T06:43:34Z'
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
  accessed_at: '2026-10-21T06:43:34Z'
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
  accessed_at: '2026-10-21T06:43:34Z'
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
  accessed_at: '2026-10-21T06:43:34Z'
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
  accessed_at: '2026-10-21T07:52:02Z'
  support: supports
  summary: Policy permits one-to-one species closeMatch normalization and LPSN-linked
    species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage
    unchanged.
  locator: Mapping predicates; Which strains belong to a record
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
- evidence_id: equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-21T07:52:02Z'
  support: supports
  summary: TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations
    remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes
    under the source taxon.
  locator: TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
- evidence_id: seed-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-21T07:52:02Z'
  support: supports
  summary: Inspected mapping ranking, qualified predicates, fixed broadMatch wording,
    synonym/xref construction, primary cluster counts and same-taxon type-strain derivation.
  locator: GTDB mapping construction lines 444–476; LPSN/type-strain and source-attestation
    construction
  snapshot_sha256: 3cc30f6413a293165385dfc1860505fe389e5adfe9aa3d168f76aa4cb2ac36bd
- evidence_id: manifest
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-21T07:52:02Z'
  support: supports
  summary: Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd,
    upstream input hashes and extraction time 2026-09-13T17:50:44Z.
  locator: kg_microbe_source, inputs, extracted_at
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
- evidence_id: overlay-manifests
  kind: record_content
  reference: data/atb/MANIFEST.yaml
  accessed_at: '2026-10-21T07:52:02Z'
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
  locator: 'line 29829: {"accession":"GB_GCA_021163065.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__B5-G16;s__B5-G16
    sp021163065","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2116306v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA713414","ncbi_biosample":"SAMN18353649","ncbi_contig_count":"234","ncbi_contig_n50":"10604","ncbi_country":"Pacific
    Ocean: Mexico; Pescadero Basin","ncbi_date":"2021-12-10","ncbi_genbank_assembly_accession":"GCA_021163065.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"AUK153","ncbi_isolation_source":"marine
    hydrothermal sediment","ncbi_lat_lon":"23.957043 N 108.862273 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobaceae
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2021-12-10","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2511821","ncbi_ssu_count":"1","ncbi_strain_identifiers":"AUK153","ncbi_submitter":"California
    Institute of Technology","ncbi_taxid":"2511821","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;x__unclassified
    Archaeoglobaceae;s__Archaeoglobaceae archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1905055","ncbi_translation_table":"11","ncbi_trna_count":"45","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1905055","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAGGXN000000000.1"};
    line 30412: {"accession":"GB_GCA_029259415.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    sp029259415","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2925941v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA891685","ncbi_biosample":"SAMN31357530","ncbi_contig_count":"104","ncbi_contig_n50":"27508","ncbi_country":"Mexico:
    Guaymas Basin; Gulf of California","ncbi_date":"2023-03-17","ncbi_genbank_assembly_accession":"GCA_029259415.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"S5B4_HD70","ncbi_isolation_source":"hydrothermal
    vent sediment; anoxic hexadecane-degrading enrichment at 70 degrees Celsius","ncbi_lat_lon":"27.0075
    N 111.409 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-03-17","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"none","ncbi_strain_identifiers":"S5B4_HD70","ncbi_submitter":"Max
    Planck Institute for Marine Microbiology","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified
    Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1941972","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1941972","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAPDIW000000000.1"};
    line 31243: {"accession":"GB_GCA_965552265.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    sp029259335","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"SRR24791474_maxbin2_1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJEB88069","ncbi_biosample":"SAMEA118547580","ncbi_contig_count":"158","ncbi_contig_n50":"25832","ncbi_country":"none","ncbi_date":"2025-07-08","ncbi_genbank_assembly_accession":"GCA_965552265.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SRR24791474_maxbin2_1","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"uncultured
    Archaeoglobus sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2025-07-08","ncbi_spanned_gaps":"0","ncbi_species_taxid":"269247","ncbi_ssu_count":"none","ncbi_strain_identifiers":"SRR24791474_maxbin2_1","ncbi_submitter":"EMG","ncbi_taxid":"269247","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;x__environmental
    samples;s__uncultured Archaeoglobus sp.","ncbi_total_gap_length":"0","ncbi_total_length":"2357242","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2357242","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"CBEVRN000000000.1"};
    line 31723: {"accession":"GB_GCA_011605875.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2
    sp004347865","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM1160587v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA604268","ncbi_biosample":"SAMN13964306","ncbi_contig_count":"73","ncbi_contig_n50":"31899","ncbi_country":"USA:
    Yellowstone National Park; Smokejumper3 Hot Spring","ncbi_date":"2020-03-22","ncbi_genbank_assembly_accession":"GCA_011605875.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SJ3.Bin34","ncbi_isolation_source":"sediments
    from hot spring shelf","ncbi_lat_lon":"44.41595 N 110.9558 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobales
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"1","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2020-03-22","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250258","ncbi_ssu_count":"0","ncbi_strain_identifiers":"SJ3.Bin34","ncbi_submitter":"Montana
    State University","ncbi_taxid":"2250258","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;x__unclassified
    Archaeoglobales;s__Archaeoglobales archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1467518","ncbi_translation_table":"11","ncbi_trna_count":"42","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1467518","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAAOZH000000000.1"};
    line 33626: {"accession":"GB_GCA_036867765.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2
    sp004347865","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM3686776v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA1014417","ncbi_biosample":"SAMN39201948","ncbi_contig_count":"20","ncbi_contig_n50":"147257","ncbi_country":"none","ncbi_date":"2024-02-25","ncbi_genbank_assembly_accession":"GCA_036867765.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"LCB24","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Candidatus
    Methanoglobus sp.","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"19","ncbi_scaffold_l50":"5","ncbi_scaffold_n50":"147257","ncbi_scaffold_n75":"85097","ncbi_scaffold_n90":"45659","ncbi_seq_rel_date":"2024-02-25","ncbi_spanned_gaps":"1","ncbi_species_taxid":"3101521","ncbi_ssu_count":"1","ncbi_strain_identifiers":"LCB24","ncbi_submitter":"Montana
    State University","ncbi_taxid":"3101521","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Candidatus
    Methanoglobus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Candidatus
    Methanoglobus;x__unclassified Candidatus Methanoglobus;s__Candidatus Methanoglobus
    sp.","ncbi_total_gap_length":"100","ncbi_total_length":"1623778","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1623678","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JBAJGN000000000.1"};
    line 35414: {"accession":"GB_GCA_014361165.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Mnemosynellales;f__Mnemosynellaceae;g__Mnemosynella;s__Mnemosynella
    bozhongmuii","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM1436116v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA635524","ncbi_biosample":"SAMN15637566","ncbi_contig_count":"159","ncbi_contig_n50":"13044","ncbi_country":"China:
    Dongying","ncbi_date":"2020-09-01","ncbi_genbank_assembly_accession":"GCA_014361165.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"MAG-16","ncbi_isolation_source":"Shengli
    oilfield at Shandong province","ncbi_lat_lon":"38.15 N 118.5 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Candidatus
    Mnemosynella bozhongmuii","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"2","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2020-09-01","ncbi_spanned_gaps":"0","ncbi_species_taxid":"3072938","ncbi_ssu_count":"1","ncbi_strain_identifiers":"MAG-16","ncbi_submitter":"East
    China University of Science and Technology","ncbi_taxid":"3072938","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Candidatus
    Mnemosynellales;f__Candidatus Mnemosynellaceae;g__Candidatus Mnemosynella;s__Candidatus
    Mnemosynella bozhongmuii","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Candidatus
    Mnemosynellales;f__Candidatus Mnemosynellaceae;g__Candidatus Mnemosynella;s__Candidatus
    Mnemosynella bozhongmuii","ncbi_total_gap_length":"0","ncbi_total_length":"1166237","ncbi_translation_table":"11","ncbi_trna_count":"34","ncbi_type_material_designation":"assembly
    from type material","ncbi_ungapped_length":"1166237","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JACIWD000000000.1"};
    line 38660: {"accession":"GB_GCA_004347865.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2
    sp004347865","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM434786v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA475886","ncbi_biosample":"SAMN09404985","ncbi_contig_count":"220","ncbi_contig_n50":"10901","ncbi_country":"USA:
    Yellowstone National Park; Wyoming; USA","ncbi_date":"2019-03-12","ncbi_genbank_assembly_accession":"GCA_004347865.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"WYZ-LMO2","ncbi_isolation_source":"hot
    springs sediment","ncbi_lat_lon":"44.6100 N 110.4400 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"1","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2019-03-12","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"0","ncbi_strain_identifiers":"WYZ-LMO2","ncbi_submitter":"Shanghai
    Jiao Tong University","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified
    Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1514415","ncbi_translation_table":"11","ncbi_trna_count":"44","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1514415","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"QNUZ00000000.1"};
    line 39381: {"accession":"GB_GCA_013151125.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Geoglobus;s__Geoglobus
    ahangari","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM1315112v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA557557","ncbi_biosample":"SAMN12405721","ncbi_contig_count":"181","ncbi_contig_n50":"8575","ncbi_country":"Pacific
    Ocean: East Pacific Rise","ncbi_date":"2020-05-22","ncbi_genbank_assembly_accession":"GCA_013151125.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"M_MetaBat.67","ncbi_isolation_source":"Deepsea
    hydrothermal sulfide chimney","ncbi_lat_lon":"9.7712 N 104.2789 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"2","ncbi_scaffold_count":"163","ncbi_scaffold_l50":"43","ncbi_scaffold_n50":"9877","ncbi_scaffold_n75":"6138","ncbi_scaffold_n90":"4287","ncbi_seq_rel_date":"2020-05-22","ncbi_spanned_gaps":"18","ncbi_species_taxid":"2250530","ncbi_ssu_count":"1","ncbi_strain_identifiers":"M_MetaBat.67","ncbi_submitter":"Lab
    of Microbial Oceanography","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified
    Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"1128","ncbi_total_length":"1352038","ncbi_translation_table":"11","ncbi_trna_count":"36","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1350910","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAADIT000000000.1"};
    line 39729: {"accession":"GB_GCA_029259335.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    sp029259335","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2925933v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA891685","ncbi_biosample":"SAMN31357532","ncbi_contig_count":"101","ncbi_contig_n50":"24995","ncbi_country":"Mexico:
    Guaymas Basin; Gulf of California","ncbi_date":"2023-03-17","ncbi_genbank_assembly_accession":"GCA_029259335.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"S5B9_HD70","ncbi_isolation_source":"hydrothermal
    vent sediment; anoxic hexadecane-degrading enrichment at 70 degrees Celsius","ncbi_lat_lon":"27.0075
    N 111.409 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-03-17","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"none","ncbi_strain_identifiers":"S5B9_HD70","ncbi_submitter":"Max
    Planck Institute for Marine Microbiology","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified
    Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1749908","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1749908","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAPDIY000000000.1"};
    line 41225: {"accession":"GB_GCA_029259345.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    sp029259345","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM2925934v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA891685","ncbi_biosample":"SAMN31357531","ncbi_contig_count":"89","ncbi_contig_n50":"24936","ncbi_country":"Mexico:
    Guaymas Basin; Gulf of California","ncbi_date":"2023-03-17","ncbi_genbank_assembly_accession":"GCA_029259345.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"S5B8_HD70","ncbi_isolation_source":"hydrothermal
    vent sediment; anoxic hexadecane-degrading enrichment at 70 degrees Celsius","ncbi_lat_lon":"27.0075
    N 111.409 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"88","ncbi_scaffold_l50":"20","ncbi_scaffold_n50":"24936","ncbi_scaffold_n75":"17574","ncbi_scaffold_n90":"8601","ncbi_seq_rel_date":"2023-03-17","ncbi_spanned_gaps":"1","ncbi_species_taxid":"2250530","ncbi_ssu_count":"none","ncbi_strain_identifiers":"S5B8_HD70","ncbi_submitter":"Max
    Planck Institute for Marine Microbiology","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified
    Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"10","ncbi_total_length":"1486306","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1486296","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAPDIX000000000.1"};
    line 43252: {"accession":"GB_GCA_029982835.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Mnemosynellales;f__Mnemosynellaceae;g__Mnemosynella;s__Mnemosynella
    bozhongmuii","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2998283v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA308326","ncbi_biosample":"SAMN33401079","ncbi_contig_count":"100","ncbi_contig_n50":"9386","ncbi_country":"USA:
    Colorado","ncbi_date":"2023-05-11","ncbi_genbank_assembly_accession":"GCA_029982835.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"DJKA110_ANT-KO_bin.29","ncbi_isolation_source":"Produced
    fluids from hydraulically fractured shales","ncbi_lat_lon":"40.411582 N 104.348363
    W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"0","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-05-11","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"0","ncbi_strain_identifiers":"DJKA110_ANT-KO_bin.29","ncbi_submitter":"The
    Ohio State University","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified
    Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"942654","ncbi_translation_table":"11","ncbi_trna_count":"0","ncbi_type_material_designation":"na","ncbi_ungapped_length":"942654","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JARRCA000000000.1"};
    line 43594: {"accession":"RS_GCF_001006045.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Geoglobus;s__Geoglobus
    ahangari","gtdb_type_species_of_genus":"t","ncbi_assembly_level":"Complete Genome","ncbi_assembly_name":"ASM100604v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN02988852","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"USA:
    Guaymas basin","ncbi_date":"2015-05-11","ncbi_genbank_assembly_accession":"GCA_001006045.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"marine
    hydrothermal vent","ncbi_lat_lon":"27 N 111 W","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Geoglobus
    ahangari","ncbi_protein_count":"2007","ncbi_refseq_category":"reference genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"1770093","ncbi_scaffold_n75":"1770093","ncbi_scaffold_n90":"1770093","ncbi_seq_rel_date":"2015-05-11","ncbi_spanned_gaps":"0","ncbi_species_taxid":"113653","ncbi_ssu_count":"1","ncbi_strain_identifiers":"234","ncbi_submitter":"Michigan
    State University","ncbi_taxid":"113653","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Geoglobus;s__Geoglobus
    ahangari","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Geoglobus;s__Geoglobus
    ahangari","ncbi_total_gap_length":"0","ncbi_total_length":"1770093","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"assembly
    from type material","ncbi_ungapped_length":"1770093","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"};
    line 43618: {"accession":"GB_GCA_024437945.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__WYZ-LMO2;s__WYZ-LMO2
    sp004347865","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2443794v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA859922","ncbi_biosample":"SAMN29809817","ncbi_contig_count":"179","ncbi_contig_n50":"8067","ncbi_country":"USA:
    Yellowstone National Park; WY","ncbi_date":"2022-07-25","ncbi_genbank_assembly_accession":"GCA_024437945.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"LCB024-003","ncbi_isolation_source":"hot
    spring sediment","ncbi_lat_lon":"44.57347 N 110.79504 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"2","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2022-07-25","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"0","ncbi_strain_identifiers":"LCB024-003","ncbi_submitter":"Montana
    State University","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified
    Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1156727","ncbi_translation_table":"11","ncbi_trna_count":"33","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1156727","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JANFND000000000.1"};
    line 45221: {"accession":"GB_GCA_029259455.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    sp029259455","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2925945v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA891685","ncbi_biosample":"SAMN31357527","ncbi_contig_count":"82","ncbi_contig_n50":"15423","ncbi_country":"Mexico:
    Guaymas Basin; Gulf of California","ncbi_date":"2023-03-17","ncbi_genbank_assembly_accession":"GCA_029259455.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"S5B11_HD70","ncbi_isolation_source":"hydrothermal
    vent sediment; anoxic hexadecane-degrading enrichment at 70 degrees Celsius","ncbi_lat_lon":"27.0075
    N 111.409 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-03-17","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"none","ncbi_strain_identifiers":"S5B11_HD70","ncbi_submitter":"Max
    Planck Institute for Marine Microbiology","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified
    Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"879016","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"879016","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAPDIT000000000.1"};
    line 45671: {"accession":"GB_GCA_002010305.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__JdFR-42;g__JdFR-42;s__JdFR-42
    sp002010305","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM201030v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA269163","ncbi_biosample":"SAMN06226359","ncbi_contig_count":"42","ncbi_contig_n50":"70809","ncbi_country":"Pacific
    Ocean","ncbi_date":"2017-03-02","ncbi_genbank_assembly_accession":"GCA_002010305.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"JdFR-42","ncbi_isolation_source":"basaltic
    crustal fluids","ncbi_lat_lon":"47.76 N 127.76 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobi
    archaeon JdFR-42","ncbi_protein_count":"0","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2017-03-02","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1935016","ncbi_ssu_count":"none","ncbi_strain_identifiers":"JdFR-42","ncbi_submitter":"University
    of Hawaii","ncbi_taxid":"1935016","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified
    Archaeoglobi;s__Archaeoglobi archaeon JdFR-42","ncbi_total_gap_length":"0","ncbi_total_length":"2148619","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2148619","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"MTND00000000.1"};
    line 46752: {"accession":"GB_GCA_003935005.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__JdFR-42;g__JdFR-42;s__JdFR-42
    sp002010305","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM393500v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA266365","ncbi_biosample":"SAMN10474933","ncbi_contig_count":"24","ncbi_contig_n50":"113045","ncbi_country":"Pacific
    Ocean: Juan de Fuca Ridge","ncbi_date":"2018-12-11","ncbi_genbank_assembly_accession":"GCA_003935005.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"rG16","ncbi_isolation_source":"basaltic
    crust aquifer fluid","ncbi_lat_lon":"47.76 N 127.76 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"21","ncbi_scaffold_l50":"4","ncbi_scaffold_n50":"233158","ncbi_scaffold_n75":"78927","ncbi_scaffold_n90":"57605","ncbi_seq_rel_date":"2018-12-11","ncbi_spanned_gaps":"3","ncbi_species_taxid":"2250530","ncbi_ssu_count":"none","ncbi_strain_identifiers":"rG16","ncbi_submitter":"University
    of Hawaii","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified
    Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"300","ncbi_total_length":"2128522","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2128222","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"RSFX00000000.1"}'
  snapshot_sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
- evidence_id: genome-catalog-2
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0018.jsonl.gz
  accessed_at: '2026-10-20T07:31:11Z'
  support: supports
  summary: Inspected every selected GTDB cluster member, exact taxid/species-taxid,
    culture identifiers and accession versions. Species membership alone is not a
    strain identity.
  locator: 'line 257: {"accession":"GB_GCA_029259425.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__B5-G16;s__B5-G16
    sp021163065","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2925942v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA891685","ncbi_biosample":"SAMN31357529","ncbi_contig_count":"112","ncbi_contig_n50":"30933","ncbi_country":"Mexico:
    Guaymas Basin; Gulf of California","ncbi_date":"2023-03-17","ncbi_genbank_assembly_accession":"GCA_029259425.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"S5B2_HD70","ncbi_isolation_source":"hydrothermal
    vent sediment; anoxic hexadecane-degrading enrichment at 70 degrees Celsius","ncbi_lat_lon":"27.0075
    N 111.409 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-03-17","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"none","ncbi_strain_identifiers":"S5B2_HD70","ncbi_submitter":"Max
    Planck Institute for Marine Microbiology","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified
    Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"2003750","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2003750","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAPDIV000000000.1"};
    line 704: {"accession":"GB_GCA_030153425.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Mnemosynellales;f__Mnemosynellaceae;g__Mnemosynella;s__Mnemosynella
    bozhongmuii","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM3015342v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA308326","ncbi_biosample":"SAMN33401153","ncbi_contig_count":"70","ncbi_contig_n50":"21655","ncbi_country":"USA:
    Colorado","ncbi_date":"2023-06-02","ncbi_genbank_assembly_accession":"GCA_030153425.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"DJKA128_NP-F35_bin.23","ncbi_isolation_source":"Produced
    fluids from hydraulically fractured shales","ncbi_lat_lon":"40.411582 N 104.348363
    W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"0","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-06-02","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2250530","ncbi_ssu_count":"0","ncbi_strain_identifiers":"DJKA128_NP-F35_bin.23","ncbi_submitter":"The
    Ohio State University","ncbi_taxid":"2250530","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;x__unclassified
    Archaeoglobi;s__Archaeoglobi archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1191577","ncbi_translation_table":"11","ncbi_trna_count":"0","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1191577","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JASKJO000000000.1"}'
  snapshot_sha256: 8baa314877815777abcdf600079c6ee42f2ea5340398df9f2e18de9c18fd4347
- evidence_id: gtdb-full-scan
  kind: search
  reference: data/catalog/MANIFEST.json
  accessed_at: '2026-10-20T07:31:11Z'
  support: supports
  summary: All nineteen GTDB shards were searched with exact terminal species tokens
    preserving internal genus suffix underscores. Source cluster counts and taxon
    distributions were assessed independently of exact-identity promotion.
  locator: '{"target":"NCBITaxon:2250530","rank":"SPECIES","mappings":[{"source_id":"GTDB:s__WYZ-LMO2_sp004347865","predicate":"skos:broadMatch","genome_count":4,"ncbi_taxids":{"2250258":1,"3101521":1,"2250530":2},"ncbi_species_taxids":{"2250258":1,"3101521":1,"2250530":2},"members":[{"accession":"GB_GCA_011605875.1","ncbi_taxid":"2250258","ncbi_species_taxid":"2250258","ncbi_organism_name":"Archaeoglobales
    archaeon","ncbi_strain_identifiers":"SJ3.Bin34","ncbi_genbank_assembly_accession":"GCA_011605875.1"},{"accession":"GB_GCA_036867765.1","ncbi_taxid":"3101521","ncbi_species_taxid":"3101521","ncbi_organism_name":"Candidatus
    Methanoglobus sp.","ncbi_strain_identifiers":"LCB24","ncbi_genbank_assembly_accession":"GCA_036867765.1"},{"accession":"GB_GCA_004347865.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_strain_identifiers":"WYZ-LMO2","ncbi_genbank_assembly_accession":"GCA_004347865.1"},{"accession":"GB_GCA_024437945.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_strain_identifiers":"LCB024-003","ncbi_genbank_assembly_accession":"GCA_024437945.1"}]},{"source_id":"GTDB:s__Mnemosynella_bozhongmuii","predicate":"skos:broadMatch","genome_count":3,"ncbi_taxids":{"3072938":1,"2250530":2},"ncbi_species_taxids":{"3072938":1,"2250530":2},"members":[{"accession":"GB_GCA_014361165.1","ncbi_taxid":"3072938","ncbi_species_taxid":"3072938","ncbi_organism_name":"Candidatus
    Mnemosynella bozhongmuii","ncbi_strain_identifiers":"MAG-16","ncbi_genbank_assembly_accession":"GCA_014361165.1"},{"accession":"GB_GCA_029982835.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_strain_identifiers":"DJKA110_ANT-KO_bin.29","ncbi_genbank_assembly_accession":"GCA_029982835.1"},{"accession":"GB_GCA_030153425.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_strain_identifiers":"DJKA128_NP-F35_bin.23","ncbi_genbank_assembly_accession":"GCA_030153425.1"}]},{"source_id":"GTDB:s__Archaeoglobus_sp029259335","predicate":"skos:broadMatch","genome_count":2,"ncbi_taxids":{"269247":1,"2250530":1},"ncbi_species_taxids":{"269247":1,"2250530":1},"members":[{"accession":"GB_GCA_965552265.1","ncbi_taxid":"269247","ncbi_species_taxid":"269247","ncbi_organism_name":"uncultured
    Archaeoglobus sp.","ncbi_strain_identifiers":"SRR24791474_maxbin2_1","ncbi_genbank_assembly_accession":"GCA_965552265.1"},{"accession":"GB_GCA_029259335.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_strain_identifiers":"S5B9_HD70","ncbi_genbank_assembly_accession":"GCA_029259335.1"}]},{"source_id":"GTDB:s__B5-G16_sp021163065","predicate":"skos:broadMatch","genome_count":2,"ncbi_taxids":{"2511821":1,"2250530":1},"ncbi_species_taxids":{"2511821":1,"2250530":1},"members":[{"accession":"GB_GCA_021163065.1","ncbi_taxid":"2511821","ncbi_species_taxid":"2511821","ncbi_organism_name":"Archaeoglobaceae
    archaeon","ncbi_strain_identifiers":"AUK153","ncbi_genbank_assembly_accession":"GCA_021163065.1"},{"accession":"GB_GCA_029259425.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_strain_identifiers":"S5B2_HD70","ncbi_genbank_assembly_accession":"GCA_029259425.1"}]},{"source_id":"GTDB:s__Geoglobus_ahangari","predicate":"skos:broadMatch","genome_count":2,"ncbi_taxids":{"2250530":1,"113653":1},"ncbi_species_taxids":{"2250530":1,"113653":1},"members":[{"accession":"GB_GCA_013151125.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_strain_identifiers":"M_MetaBat.67","ncbi_genbank_assembly_accession":"GCA_013151125.1"},{"accession":"RS_GCF_001006045.1","ncbi_taxid":"113653","ncbi_species_taxid":"113653","ncbi_organism_name":"Geoglobus
    ahangari","ncbi_strain_identifiers":"234","ncbi_genbank_assembly_accession":"GCA_001006045.1"}]},{"source_id":"GTDB:s__JdFR-42_sp002010305","predicate":"skos:broadMatch","genome_count":2,"ncbi_taxids":{"1935016":1,"2250530":1},"ncbi_species_taxids":{"1935016":1,"2250530":1},"members":[{"accession":"GB_GCA_002010305.1","ncbi_taxid":"1935016","ncbi_species_taxid":"1935016","ncbi_organism_name":"Archaeoglobi
    archaeon JdFR-42","ncbi_strain_identifiers":"JdFR-42","ncbi_genbank_assembly_accession":"GCA_002010305.1"},{"accession":"GB_GCA_003935005.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_strain_identifiers":"rG16","ncbi_genbank_assembly_accession":"GCA_003935005.1"}]},{"source_id":"GTDB:s__Archaeoglobus_sp029259345","predicate":"skos:broadMatch","genome_count":1,"ncbi_taxids":{"2250530":1},"ncbi_species_taxids":{"2250530":1},"members":[{"accession":"GB_GCA_029259345.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_strain_identifiers":"S5B8_HD70","ncbi_genbank_assembly_accession":"GCA_029259345.1"}]},{"source_id":"GTDB:s__Archaeoglobus_sp029259415","predicate":"skos:broadMatch","genome_count":1,"ncbi_taxids":{"2250530":1},"ncbi_species_taxids":{"2250530":1},"members":[{"accession":"GB_GCA_029259415.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_strain_identifiers":"S5B4_HD70","ncbi_genbank_assembly_accession":"GCA_029259415.1"}]},{"source_id":"GTDB:s__Archaeoglobus_sp029259455","predicate":"skos:broadMatch","genome_count":1,"ncbi_taxids":{"2250530":1},"ncbi_species_taxids":{"2250530":1},"members":[{"accession":"GB_GCA_029259455.1","ncbi_taxid":"2250530","ncbi_species_taxid":"2250530","ncbi_organism_name":"Archaeoglobi
    archaeon","ncbi_strain_identifiers":"S5B11_HD70","ncbi_genbank_assembly_accession":"GCA_029259455.1"}]}]}'
  snapshot_sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
  search_scope: Full explicit reads of every enumerated GTDB primary shard including
    ignored files. Exact terminal GTDB species token; exact assembly accession stem
    or explicit genome identifier. Versions remain separate.
- evidence_id: finding-deduplication
  kind: search
  reference: Owned review worktrees structured bundles
  accessed_at: '2026-10-21T06:43:12Z'
  support: supports
  summary: No existing target-specific finding with this stable key was found in the
    bounded ignored-inclusive search.
  locator: '{"target_index":2,"issue_key":"gtdb-broadmatch-note-other-taxa-2250530","finding_id":"pooled-note-other-taxa","target_ids":["NCBITaxon:2250530"],"matching_review_ids":[],"matching_findings":[],"result":"no
    duplicate stable issue key found"}'
  snapshot_sha256: fbab508a200bd4916e450c0509f0b517a00478d467f0bb78f49fe40fa37636d1
  search_scope: All YAML files recursively in main-at-01ca63 owned worktree14 and
    thirteen owned batch review directories; rg --no-ignore --hidden and pathlib rglob
    include ignored files.
- evidence_id: strict-receipt
  kind: validation
  reference: just validate-strict data/taxa/archaea/archaeoglobi_archaeon.yaml --out
    /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/strict-02.tsv
  accessed_at: '2026-10-20T07:29:27Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo;\
    \ started 2026-10-20T07:29:26Z, finished 2026-10-20T07:29:27Z, exit 0. This exact\
    \ generated YAML only; its captured bytes remain unchanged. Actual earlier per-target\
    \ invocation; the receipt retains its original cwd and times.\nValidating 1 files\
    \ with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0012/src/taxonmech/schema/taxonmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/strict-02.tsv"
  locator: This exact generated YAML only; its captured bytes remain unchanged. Actual
    earlier per-target invocation; the receipt retains its original cwd and times.
  snapshot_sha256: c356f641eb7c11bf8bb5e74b28f42f142f0e6abe60012adfa5e31077a0030fc1
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
- assessment_id: identity
  area: identity
  topic: Exact taxon and source lineage
  outcome: supported
  summary: NCBITaxon:2250530 denotes Archaeoglobi archaeon at SPECIES rank beneath
    NCBITaxon:1935015, genetic code 11. All 7 carried ancestors agree with the pinned
    inventory and captured official NCBI response; the response omits only the root
    entry. Source name classes remain distinct from taxon classification.
  target_ids:
  - NCBITaxon:2250530
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
  outcome: concern
  summary: NCBI 2250530 identity, species rank and parent 1935015 agree. All nine
    GTDB broad mappings preserve source predicates and whole-cluster counts. The first
    six clusters have other NCBI members, whereas the final three are singleton clusters
    containing only this NCBI taxon. Their fixed pooled-note clause is unsupported.
    The primary attestation count is 4 genomes plus eight further species, not a sum
    of counts.
  target_ids:
  - NCBITaxon:2250530
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - lpsn-inventory
  - mapping-policy
  - genome-catalog-1
  - genome-catalog-2
  - gtdb-full-scan
- assessment_id: completeness
  area: completeness
  topic: Imported subtree and source assertion units
  outcome: supported
  summary: 'Complete direct reads of twelve source/scope/path tables, including ignored
    files, support 0 imported BacDive strains over the exact target subtree (0 descendant
    taxa). All imported counts agree with their own source units: NCBITAXON 1 NAME;
    GTDB 4 GENOME. Counts of organisms, media, traits and genome assertions are not
    interchangeable and do not prove phenotype or biological genome equivalence. GTDB
    primary count 4 denotes the first cluster and eight further clusters are recorded;
    total 18 cluster members are not the primary attestation count.'
  target_ids:
  - NCBITaxon:2250530
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
  - genome-catalog-2
- assessment_id: taxonomy-mapping
  area: grounding
  topic: Qualified species mapping and target scope
  outcome: concern
  summary: NCBI 2250530 identity, species rank and parent 1935015 agree. All nine
    GTDB broad mappings preserve source predicates and whole-cluster counts. The first
    six clusters have other NCBI members, whereas the final three are singleton clusters
    containing only this NCBI taxon. Their fixed pooled-note clause is unsupported.
    The primary attestation count is 4 genomes plus eight further species, not a sum
    of counts.
  target_ids:
  - NCBITaxon:2250530
  evidence_ids:
  - record
  - gtdb-mappings
  - gtdb-species
  - mapping-policy
  - equivalence-contract
  - seed-owner
  - genome-catalog-1
  - genome-catalog-2
  - gtdb-full-scan
- assessment_id: native-status
  area: provenance
  topic: Unchanged native status and history
  outcome: supported
  summary: EXACT grounding and SEEDED status agree with NCBI identity. The sole seed
    event at 2026-09-13T17:54:04Z equals the latest raw/ATB/StrainInfo extraction
    time; no native status/history was changed.
  target_ids:
  - NCBITaxon:2250530
  evidence_ids:
  - record
  - manifest
  - overlay-manifests
  - scope-row
  - path-row
findings:
- finding_id: pooled-note-other-taxa
  issue_key: gtdb-broadmatch-note-other-taxa-2250530
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Three singleton GTDB cluster notes incorrectly assert other NCBI taxa
  description: All nineteen GTDB shards were searched with exact terminal species
    tokens. Each listed cluster contains one genome, solely NCBITaxon:2250530, and
    reverse mappings agree. The fixed clause asserting other NCBI taxa is unsupported
    for these three clusters. The other six clusters have mixed taxids; pooling nine
    GTDB species under the NCBI placeholder still supports broadMatch.
  target_ids:
  - NCBITaxon:2250530
  field_paths:
  - taxonomy_mappings[source_id=GTDB:s__Archaeoglobus_sp029259345].notes
  - taxonomy_mappings[source_id=GTDB:s__Archaeoglobus_sp029259415].notes
  - taxonomy_mappings[source_id=GTDB:s__Archaeoglobus_sp029259455].notes
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
  normalization_reason: Non-blocking wording defect; exact taxon identity, mapping
    predicates and source counts remain supported.
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Maintained GTDB mapping notes and synonym/xref scope
actions:
- action_id: correct-pooled-mapping-note
  description: Revise the maintained broadMatch note to describe pooling without asserting
    other NCBI taxa for each source cluster; preserve qualified predicates, counts
    and carried lineage.
  finding_ids:
  - pooled-note-other-taxa
  target_ids:
  - NCBITaxon:2250530
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Maintained GTDB mapping notes and synonym/xref scope
  acceptance_checks:
  - All three listed singleton notes omit unsupported other-taxa wording.
  - Retain all nine mappings, primary count 4 and eight additional clusters; preserve
    actual mixed-taxid membership.
  - Change maintained inputs only; after separately authorized guarded regeneration,
    run strict, history, product, corpus and QC gates.
limitations:
- The review assesses exact identifiers, nomenclature, source placement and import
  completeness at the captured versions; it does not establish experimental phenotypes,
  assembly sequence equivalence or a phylogenetic species boundary.
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
