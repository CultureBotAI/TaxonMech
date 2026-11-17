# Record review: archaeon BMS3Abin16

- Review: 20261021T092051Z-archaeon_bms3abin16
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-21T08:37:49Z
- Finished UTC: 2026-10-21T09:20:51Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

archaeon BMS3Abin16 has supported exact NCBI identity, carried lineage and source-scoped representation. No record-specific defect was established within the inspected sources.

## Scope And Provenance

Entire single generated record, including all source assertions and imported strains.

Selection: Batch-0025 target 10; next unreviewed path-order selection after excluding 295 actual covered target paths. Canonical record_review.py list over the 39-bundle current base and all twenty-four actually saved branch worktrees, including ignored and hidden review bundles. Native corpus enumerated with os.walk including ignored/hidden files. Coverage only derives from explicit validated bundle targets, never inventories or reservations.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 01ca63effdf8c03a644df893ba6129b2d8448ea4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:2005740 | data/taxa/archaea/archaeon_bms3abin16.yaml | generated | archaeon BMS3Abin16 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact NCBI taxon, rank and lineage | passed | True | NCBITaxon:2005740 | NCBITaxon:2005740 denotes the exact SPECIES record archaeon BMS3Abin16, under NCBITaxon:93506, unclassified Archaea, with genetic code 11. All four carried ancestors and their literal names and ranks agree with the pinned taxonomy and current official NCBI response; EFetch omits root. ARCHAEA follows the taxonomic lineage, separately from EFetch Division metadata. No finer NCBI placement is inferred. |
| Complete exact identifier and name inventory search | passed | True | NCBITaxon:2005740 | Complete direct reads of all twelve named source, scope and path tables, including ignored files, used the exact target identifier, full literal label, slug and any asserted source identifier or synonym. The complete pinned NCBI parent graph has zero descendants for this target; zero imported BacDive strains agrees with the target/subtree inventory and culture-inventory slice. NCBITAXON 1 NAME and GTDB 3 GENOME agree with their source projections. All nineteen pinned GTDB genome shards were scanned and manifest-verified; all three full primary members and all three reverse mapping rows were inspected. Count 3 describes the whole source cluster, with one member explicitly classified under this NCBI target. Other optional-source misses are bounded to the pinned tables and exact queries. These misses do not establish worldwide absence of cultures, genomes, publications or biological observations. |
| Complete GTDB source-cluster count | passed | True | NCBITaxon:2005740 | The native source count 3 equals the entire pinned species cluster. Distinct NCBI member identities remain separate; the count is not restricted to this exact target taxid. |
| Species-level mapping interpretation | passed | True | NCBITaxon:2005740 | The complete pinned GTDB RS232 species GTDB:s__SZUA-236_sp002923215 contains three metagenome-derived genomes. Representative GB_GCA_002923215.1 at data/catalog/gtdb_genomes-0017.jsonl.gz line 29713 explicitly names archaeon BMS3Abin16 and gives ncbi_taxid and ncbi_species_taxid 2005740. GB_GCA_002898035.1 at line 49030 is archaeon BMS3Bbin16 with both taxids 2005739; GB_GCA_937897055.1 at line 41093 is the uncultured archaeon MAG DRR093005_bin.29_CONCOCT_v1.1_MAG with both taxids 115547. All supplied .1 accession versions are preserved. The complete reverse mapping rows retain closeMatch to 2005740 and 2005739 and broadMatch to 115547. All three NCBI targets have SPECIES rank in the pinned taxonomy; these are not strain-rank promotions. The source species row and native GTDB 3 GENOME attestation count the entire three-member cluster, of which one member explicitly carries the reviewed NCBI taxon. The separately attributed exact GTDB synonym/xref follow local species-level closeMatch normalization policy; the multiple reverse targets do not establish a defect or a globally one-to-one mapping. The native NCBI unclassified Archaea lineage remains separate from GTDB Hydrothermarchaeota/Hydrothermarchaeia classification. Each member has a different BioSample. The two BMS assemblies share project PRJDB5792, which does not establish genome or sequence identity. Their sub-seafloor sulfide-deposit metadata and the third member's marine-metagenome metadata remain member-specific source observations, not taxon-wide habitat or phenotype claims. |
| Imported strain links | not_applicable | False | NCBITaxon:2005740 | This complete native record asserts no imported BacDive strain, culture deposit or strain-level genome link. A placeholder or MAG designation does not supply a deposit identity. |
| Nomenclatural publication authorities | not_applicable | False | NCBITaxon:2005740 | No LPSN nomenclature, species-authority publication or type-strain sequence citation is asserted for this target; current NCBI name classes and bounded pinned LPSN inventory were checked. |
| Gene or transcriptomics evidence applicability | not_applicable | False | NCBITaxon:2005740 | Not applicable: the complete native record asserts no gene, protein, regulator, pathway, experimental trait, mechanism or transcriptome link. |
| Historical aggregate edges | not_applicable | False | NCBITaxon:2005740 | No historical medium, organism or trait aggregate is asserted in this target. |
| Native strict record validation | passed | True | NCBITaxon:2005740 | Actual terminal exit code 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. |
| Repository history validation | passed | True | NCBITaxon:2005740 | Actual terminal exit code 0. The complete standalone history population; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0025 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. |
| Full-corpus exact reproduction | passed | True | NCBITaxon:2005740 | Actual terminal exit code 0. All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0025 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. |
| Native product ID/label gate | passed | True | NCBITaxon:2005740 | Actual terminal exit code 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0025 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. |
| Authoritative complete quality gate | passed | True | NCBITaxon:2005740 | Actual terminal exit code 0. Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0025 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. 1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33) |

## Scientific And Domain Assessments

### Exact taxon and source lineage

identity: supported. Targets: NCBITaxon:2005740.

NCBITaxon:2005740 denotes the exact SPECIES record archaeon BMS3Abin16, under NCBITaxon:93506, unclassified Archaea, with genetic code 11. All four carried ancestors and their literal names and ranks agree with the pinned taxonomy and current official NCBI response; EFetch omits root. ARCHAEA follows the taxonomic lineage, separately from EFetch Division metadata. No finer NCBI placement is inferred.

### Name classes and nomenclatural scope

nomenclature: supported. Targets: NCBITaxon:2005740.

The pinned NCBI exact, related and broad synonym columns are empty, and current EFetch supplies no OtherNames entry for this exact taxon. Complete exact queries in the pinned LPSN inventory find no associated row. The native designation does not assert a formal nomenclatural authority, publication or type-deposit relationship. The separately attributed GTDB normalized exact synonym and xref follow local species-level closeMatch policy while the qualified source mapping remains explicit. This inventory observation does not establish worldwide nomenclatural absence.

### Imported subtree and source assertion units

completeness: supported. Targets: NCBITaxon:2005740.

Complete direct reads of all twelve named source, scope and path tables, including ignored files, used the exact target identifier, full literal label, slug and any asserted source identifier or synonym. The complete pinned NCBI parent graph has zero descendants for this target; zero imported BacDive strains agrees with the target/subtree inventory and culture-inventory slice. NCBITAXON 1 NAME and GTDB 3 GENOME agree with their source projections. All nineteen pinned GTDB genome shards were scanned and manifest-verified; all three full primary members and all three reverse mapping rows were inspected. Count 3 describes the whole source cluster, with one member explicitly classified under this NCBI target. Other optional-source misses are bounded to the pinned tables and exact queries. These misses do not establish worldwide absence of cultures, genomes, publications or biological observations.

### Qualified species mapping and target scope

grounding: supported. Targets: NCBITaxon:2005740.

The complete pinned GTDB RS232 species GTDB:s__SZUA-236_sp002923215 contains three metagenome-derived genomes. Representative GB_GCA_002923215.1 at data/catalog/gtdb_genomes-0017.jsonl.gz line 29713 explicitly names archaeon BMS3Abin16 and gives ncbi_taxid and ncbi_species_taxid 2005740. GB_GCA_002898035.1 at line 49030 is archaeon BMS3Bbin16 with both taxids 2005739; GB_GCA_937897055.1 at line 41093 is the uncultured archaeon MAG DRR093005_bin.29_CONCOCT_v1.1_MAG with both taxids 115547. All supplied .1 accession versions are preserved. The complete reverse mapping rows retain closeMatch to 2005740 and 2005739 and broadMatch to 115547. All three NCBI targets have SPECIES rank in the pinned taxonomy; these are not strain-rank promotions. The source species row and native GTDB 3 GENOME attestation count the entire three-member cluster, of which one member explicitly carries the reviewed NCBI taxon. The separately attributed exact GTDB synonym/xref follow local species-level closeMatch normalization policy; the multiple reverse targets do not establish a defect or a globally one-to-one mapping. The native NCBI unclassified Archaea lineage remains separate from GTDB Hydrothermarchaeota/Hydrothermarchaeia classification. Each member has a different BioSample. The two BMS assemblies share project PRJDB5792, which does not establish genome or sequence identity. Their sub-seafloor sulfide-deposit metadata and the third member's marine-metagenome metadata remain member-specific source observations, not taxon-wide habitat or phenotype claims.

### Unchanged native status and history

provenance: supported. Targets: NCBITaxon:2005740.

EXACT grounding and SEEDED mapping status preserve the generated source state. The sole SEEDED_FROM_SOURCES event at 2026-09-13T17:54:04Z agrees with the latest raw, ATB and StrainInfo manifest extraction. The exact seed-scope and PATHS rows preserve inclusion and path. No manual curation, scientific status promotion or new native history event is inferred.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/taxa/archaea/archaeon_bms3abin16.yaml; entire TaxonRecord; identifier=NCBITaxon:2005740 | supports | Read the entire generated YAML, including identity, lineage, names, mappings, source attestations, all imported strains and links, and seed history. |
| taxonomy-inventory | data/raw/ncbitaxon_taxa.tsv; line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""}; line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"}; line 15329: {"taxon_id":"NCBITaxon:93506","label":"unclassified Archaea","rank":"NO_RANK","parent_id":"NCBITaxon:2157"}; line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"}; line 509000: {"taxon_id":"NCBITaxon:2005740","label":"archaeon BMS3Abin16","rank":"SPECIES","parent_id":"NCBITaxon:93506","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb","retired_into":"","taxonomy_snapshot":"2026-09-13"} | supports | Inspected the target and each carried ancestor, rank, parent, genetic code and source name classes. |
| scope-row | curation/seed_scope.tsv; line 90037: {"identifier":"NCBITaxon:2005740","added":"2026-09-13","reason":"attested rule: archaeon BMS3Abin16, 2 sources incl. NCBI"} | supports | Exact target is included in the declared seed scope. |
| path-row | data/taxa/PATHS.tsv; line 318041: {"identifier":"NCBITaxon:2005740","slug":"archaeon_bms3abin16"} | supports | Indexed path resolves to this exact NCBI taxon. |
| ncbi-live | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=910144,910145,910160,910080,910081,910082,910083,910084,584993,2005740&amp;retmode=xml; TaxaSet/Taxon[TaxId='2005740']; ten-target captured response | supports | Inspected the successful official response for this exact taxon: scientific name, rank, parent, source name classes, lineage and genetic code. Current authority and pinned September inventory remain distinct observations. |
| lpsn-inventory | data/raw/lpsn_names.tsv; complete table; recorded exact query terms have no match | supports | Complete exact taxon, literal name and slug queries found no associated LPSN inventory row; this observation is bounded to the pinned inventory. |
| gtdb-mappings | data/raw/gtdb_mappings.tsv; line 7958: {"gtdb_id":"GTDB:s__SZUA-236_sp002923215","gtdb_label":"s__SZUA-236_sp002923215","gtdb_parent":"GTDB:g__SZUA-236","ncbitaxon_id":"NCBITaxon:115547","predicate":"skos:broadMatch","genome_count":"3"}; line 120235: {"gtdb_id":"GTDB:s__SZUA-236_sp002923215","gtdb_label":"s__SZUA-236_sp002923215","gtdb_parent":"GTDB:g__SZUA-236","ncbitaxon_id":"NCBITaxon:2005739","predicate":"skos:closeMatch","genome_count":"3"}; line 120236: {"gtdb_id":"GTDB:s__SZUA-236_sp002923215","gtdb_label":"s__SZUA-236_sp002923215","gtdb_parent":"GTDB:g__SZUA-236","ncbitaxon_id":"NCBITaxon:2005740","predicate":"skos:closeMatch","genome_count":"3"} | supports | Inspected the exact target and all source-ID reverse mapping rows, preserving each source predicate and whole-species genome count. |
| gtdb-species | data/raw/gtdb_species.tsv; line 162021: {"gtdb_id":"GTDB:s__SZUA-236_sp002923215","label":"s__SZUA-236_sp002923215","parent":"GTDB:g__SZUA-236","genome_count":"3"} | supports | Inspected the complete selected GTDB source-species row, including its source parent and whole-cluster count. |
| bacdive-inventory | data/raw/bacdive_strains.tsv; complete table; recorded exact query terms have no match | supports | Complete inventory selection covers the exact target and descendants from the complete NCBI parent graph; its imported strain population was compared with the complete YAML. |
| culture-inventory | data/raw/culture_collection_strains.tsv; complete table; recorded exact query terms have no match | supports | Inspected exact culture-inventory associations; an isolate name or genome does not create an inferred deposit. |
| gold-organisms | data/raw/gold_organisms.tsv; complete table; recorded exact query terms have no match | supports | Inspected the exact GOLD organism count row or bounded absence, without converting counts to phenotypes. |
| mediadive-taxa | data/raw/mediadive_taxa.tsv; complete table; recorded exact query terms have no match | supports | Inspected the exact MediaDive medium count row or bounded absence, without converting counts to phenotypes. |
| madin-taxa | data/raw/madin_taxa.tsv; complete table; recorded exact query terms have no match | supports | Inspected the exact Madin trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| bactotraits-taxa | data/raw/bactotraits_taxa.tsv; complete table; recorded exact query terms have no match | supports | Inspected the exact BactoTraits trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| mapping-policy | docs/HARMONIZATION.md; Mapping predicates; Which strains belong to a record | supports | Policy permits source-scoped species-level closeMatch normalization and LPSN-linked species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage unchanged. Multiple reverse target mappings do not alone establish a normalization defect or make genomes and physical strains identical. |
| equivalence-contract | src/taxonmech/schema/taxonmech.yaml; TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439 | supports | TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes under the source taxon. |
| seed-owner | src/taxonmech/seed.py; GTDB mapping construction lines 443–478; source attestation construction lines 551–595; seed history construction lines 630–647 | supports | Inspected source mapping normalization, NCBI NAME and whole-source-species GTDB GENOME attestation construction, and seed history. Qualified source mappings and physical strain derivation remain distinct. |
| manifest | data/raw/MANIFEST.yaml; kg_microbe_source, inputs, extracted_at | supports | Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd, upstream input hashes and extraction time 2026-09-13T17:50:44Z. |
| overlay-manifests | data/atb/MANIFEST.yaml; extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml | supports | Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z, matching the sole seed event. StrainInfo manifest is independently captured in source.inputs. |
| genome-catalog-1 | data/catalog/gtdb_genomes-0017.jsonl.gz; line 29713: {"accession":"GB_GCA_002923215.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Hydrothermarchaeota;c__Hydrothermarchaeia;o__Hydrothermarchaeales;f__SZUA-236;g__SZUA-236;s__SZUA-236 sp002923215","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM292321v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJDB5792","ncbi_biosample":"SAMD00081376","ncbi_contig_count":"175","ncbi_contig_n50":"12106","ncbi_country":"none","ncbi_date":"2018-01-25","ncbi_genbank_assembly_accession":"GCA_002923215.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"BMS3Abin16","ncbi_isolation_source":"sub-seafloor sulfide deposits","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"archaeon BMS3Abin16","ncbi_protein_count":"1863","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2018-01-25","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2005740","ncbi_ssu_count":"1","ncbi_strain_identifiers":"BMS3Abin16","ncbi_submitter":"JAMSTEC","ncbi_taxid":"2005740","ncbi_taxonomy":"d__Archaea;p__;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__unclassified Archaea;s__archaeon BMS3Abin16","ncbi_total_gap_length":"0","ncbi_total_length":"1628016","ncbi_translation_table":"11","ncbi_trna_count":"29","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1628016","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"BDTI00000000.1"}; line 41093: {"accession":"GB_GCA_937897055.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Hydrothermarchaeota;c__Hydrothermarchaeia;o__Hydrothermarchaeales;f__SZUA-236;g__SZUA-236;s__SZUA-236 sp002923215","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"DRR093005_bin.29_CONCOCT_v1.1_MAG","ncbi_assembly_type":"na","ncbi_bioproject":"PRJEB51078","ncbi_biosample":"SAMEA14074663","ncbi_contig_count":"92","ncbi_contig_n50":"57719","ncbi_country":"none","ncbi_date":"2023-01-10","ncbi_genbank_assembly_accession":"GCA_937897055.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"DRR093005_bin.29_CONCOCT_v1.1_MAG","ncbi_isolation_source":"marine metagenome","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"uncultured archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-01-10","ncbi_spanned_gaps":"0","ncbi_species_taxid":"115547","ncbi_ssu_count":"none","ncbi_strain_identifiers":"DRR093005_bin.29_CONCOCT_v1.1_MAG","ncbi_submitter":"European Bioinformatics Institute","ncbi_taxid":"115547","ncbi_taxonomy":"d__Archaea;p__;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__environmental samples;s__uncultured archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1991497","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1991497","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"CALCPX000000000.1"}; line 49030: {"accession":"GB_GCA_002898035.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Hydrothermarchaeota;c__Hydrothermarchaeia;o__Hydrothermarchaeales;f__SZUA-236;g__SZUA-236;s__SZUA-236 sp002923215","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM289803v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJDB5792","ncbi_biosample":"SAMD00081393","ncbi_contig_count":"197","ncbi_contig_n50":"6378","ncbi_country":"none","ncbi_date":"2017-12-14","ncbi_genbank_assembly_accession":"GCA_002898035.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"BMS3Bbin16","ncbi_isolation_source":"sub-seafloor sulfide deposits","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"archaeon BMS3Bbin16","ncbi_protein_count":"1292","ncbi_refseq_category":"na","ncbi_rrna_count":"1","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2017-12-14","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2005739","ncbi_ssu_count":"0","ncbi_strain_identifiers":"BMS3Bbin16","ncbi_submitter":"JAMSTEC","ncbi_taxid":"2005739","ncbi_taxonomy":"d__Archaea;p__;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__unclassified Archaea;s__archaeon BMS3Bbin16","ncbi_total_gap_length":"0","ncbi_total_length":"1164696","ncbi_translation_table":"11","ncbi_trna_count":"21","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1164696","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"BDTZ00000000.1"} | supports | Inspected the complete selected GTDB species cluster, supplied assembly versions, exact NCBI taxid/species-taxid and MAG/isolate metadata. Cluster counts are not counts of genomes exclusive to this NCBI target, physical cultures or identical sequences. |
| gtdb-full-scan | data/catalog/MANIFEST.json; {"target_id":"NCBITaxon:2005740","source_species":"GTDB:s__SZUA-236_sp002923215","cluster_count":3,"members":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":29713,"sha256":"f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6","row":{"accession":"GB_GCA_002923215.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Hydrothermarchaeota;c__Hydrothermarchaeia;o__Hydrothermarchaeales;f__SZUA-236;g__SZUA-236;s__SZUA-236 sp002923215","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM292321v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJDB5792","ncbi_biosample":"SAMD00081376","ncbi_contig_count":"175","ncbi_contig_n50":"12106","ncbi_country":"none","ncbi_date":"2018-01-25","ncbi_genbank_assembly_accession":"GCA_002923215.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"BMS3Abin16","ncbi_isolation_source":"sub-seafloor sulfide deposits","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"archaeon BMS3Abin16","ncbi_protein_count":"1863","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2018-01-25","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2005740","ncbi_ssu_count":"1","ncbi_strain_identifiers":"BMS3Abin16","ncbi_submitter":"JAMSTEC","ncbi_taxid":"2005740","ncbi_taxonomy":"d__Archaea;p__;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__unclassified Archaea;s__archaeon BMS3Abin16","ncbi_total_gap_length":"0","ncbi_total_length":"1628016","ncbi_translation_table":"11","ncbi_trna_count":"29","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1628016","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"BDTI00000000.1"}},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":41093,"sha256":"f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6","row":{"accession":"GB_GCA_937897055.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Hydrothermarchaeota;c__Hydrothermarchaeia;o__Hydrothermarchaeales;f__SZUA-236;g__SZUA-236;s__SZUA-236 sp002923215","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"DRR093005_bin.29_CONCOCT_v1.1_MAG","ncbi_assembly_type":"na","ncbi_bioproject":"PRJEB51078","ncbi_biosample":"SAMEA14074663","ncbi_contig_count":"92","ncbi_contig_n50":"57719","ncbi_country":"none","ncbi_date":"2023-01-10","ncbi_genbank_assembly_accession":"GCA_937897055.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"DRR093005_bin.29_CONCOCT_v1.1_MAG","ncbi_isolation_source":"marine metagenome","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"uncultured archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-01-10","ncbi_spanned_gaps":"0","ncbi_species_taxid":"115547","ncbi_ssu_count":"none","ncbi_strain_identifiers":"DRR093005_bin.29_CONCOCT_v1.1_MAG","ncbi_submitter":"European Bioinformatics Institute","ncbi_taxid":"115547","ncbi_taxonomy":"d__Archaea;p__;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__environmental samples;s__uncultured archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1991497","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1991497","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"CALCPX000000000.1"}},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":49030,"sha256":"f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6","row":{"accession":"GB_GCA_002898035.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Hydrothermarchaeota;c__Hydrothermarchaeia;o__Hydrothermarchaeales;f__SZUA-236;g__SZUA-236;s__SZUA-236 sp002923215","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM289803v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJDB5792","ncbi_biosample":"SAMD00081393","ncbi_contig_count":"197","ncbi_contig_n50":"6378","ncbi_country":"none","ncbi_date":"2017-12-14","ncbi_genbank_assembly_accession":"GCA_002898035.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"BMS3Bbin16","ncbi_isolation_source":"sub-seafloor sulfide deposits","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"archaeon BMS3Bbin16","ncbi_protein_count":"1292","ncbi_refseq_category":"na","ncbi_rrna_count":"1","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2017-12-14","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2005739","ncbi_ssu_count":"0","ncbi_strain_identifiers":"BMS3Bbin16","ncbi_submitter":"JAMSTEC","ncbi_taxid":"2005739","ncbi_taxonomy":"d__Archaea;p__;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__unclassified Archaea;s__archaeon BMS3Bbin16","ncbi_total_gap_length":"0","ncbi_total_length":"1164696","ncbi_translation_table":"11","ncbi_trna_count":"21","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1164696","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"BDTZ00000000.1"}}],"reverse_mappings":[{"line":7958,"row":{"gtdb_id":"GTDB:s__SZUA-236_sp002923215","gtdb_label":"s__SZUA-236_sp002923215","gtdb_parent":"GTDB:g__SZUA-236","ncbitaxon_id":"NCBITaxon:115547","predicate":"skos:broadMatch","genome_count":"3"}},{"line":120235,"row":{"gtdb_id":"GTDB:s__SZUA-236_sp002923215","gtdb_label":"s__SZUA-236_sp002923215","gtdb_parent":"GTDB:g__SZUA-236","ncbitaxon_id":"NCBITaxon:2005739","predicate":"skos:closeMatch","genome_count":"3"}},{"line":120236,"row":{"gtdb_id":"GTDB:s__SZUA-236_sp002923215","gtdb_label":"s__SZUA-236_sp002923215","gtdb_parent":"GTDB:g__SZUA-236","ncbitaxon_id":"NCBITaxon:2005740","predicate":"skos:closeMatch","genome_count":"3"}}]} | supports | All nineteen pinned RS232 shards and 901341 rows match the manifest census. The complete selected source cluster and its reverse mappings were inspected; reverse target multiplicity is preserved and is not represented as a globally one-to-one mapping. |
| gtdb-member-ranks | data/raw/ncbitaxon_taxa.tsv; line 21083: {"taxon_id":"NCBITaxon:115547","label":"uncultured archaeon","rank":"SPECIES","parent_id":"NCBITaxon:48510","genetic_code":"11","exact_synonyms":"uncultured Archaea archaeon&#124;uncultured archaeoote","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb&#124;gold","retired_into":"","taxonomy_snapshot":"2026-09-13"}; line 508999: {"taxon_id":"NCBITaxon:2005739","label":"archaeon BMS3Bbin16","rank":"SPECIES","parent_id":"NCBITaxon:93506","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb","retired_into":"","taxonomy_snapshot":"2026-09-13"}; line 509000: {"taxon_id":"NCBITaxon:2005740","label":"archaeon BMS3Abin16","rank":"SPECIES","parent_id":"NCBITaxon:93506","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb","retired_into":"","taxonomy_snapshot":"2026-09-13"} | supports | Inspected exact pinned NCBI identity, rank and parent rows for every selected source-cluster member. Each member is assigned to a distinct SPECIES target; source-species membership does not establish strain identity, sequence identity or a globally one-to-one mapping. |
| native-gate-reuse | /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0025/native-gate-reuse.json; base, native_inputs_unchanged, source_directory, gates, input_proof_path and input_proof_sha256 | supports | Retained explicit verification of identical base/native inputs authorizes historical native-gate reuse; original command receipts remain separately cited. |
| strict-receipt | just validate-strict data/taxa/archaea/archaeon_bms3abin16.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0025/strict-10.tsv; This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0025/repo; started 2026-10-21T08:38:05Z, finished 2026-10-21T08:38:09Z, exit 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times.<br>Validating 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0025/src/taxonmech/schema/taxonmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0025/strict-10.tsv |
| history-receipt | just validate-history; The complete standalone history population; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0025 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T06:42:11Z, exit 0. The complete standalone history population; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0025 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check.<br>history links: 18 record(s), 0 invalid<br>No issues found<br>18 history record(s) valid against src/taxonmech/schema/history.yaml |
| corpus-receipt | just verify-corpus; All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0025 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T06:48:01Z, exit 0. All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0025 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check.<br>uv run python scripts/verify_corpus.py <br>expected 626048 records, found 626048 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ and curation/seed_scope.tsv |
| products-receipt | just validate-products; Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0025 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T07:19:10Z, exit 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0025 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check.<br>uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml<br><br>id↔label correspondence summary:<br><br>✅ All id↔label pairs correspond. |
| qc-receipt | just qc; Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0025 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T07:50:51Z, exit 0. Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0025 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check.<br>All checks passed!<br>1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33)<br>Validating 626048 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0014/src/taxonmech/schema/taxonmech.yaml<br>  files scanned:      626048<br>expected 626048 records, found 626048 on disk<br>pages/ is current<br>Site publication: 530,946,096 bytes (budget 950,000,000)<br>626048 taxon records<br>  NCBITAXON        626048<br>All TaxonMech quality gates passed.<br>  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890 strains (not genome counts)<br>  Related STRAININFO_DEPOSIT: 107277 strain-record pairs, 106843 identifiers, 53890 strains (not genome counts)<br>  Related NUCLEOTIDE_SEQUENCE: 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)<br>LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809 records mapped, 324404579 genomes summed across record attestations (not deduplicated)<br>Causal graphs: 0 records (0 evidence-backed edges)<br><br>All TaxonMech quality gates passed. |

## Limits And Additional Notes

- SPECIES rank and the literal designation are source taxonomy assertions, not independent evidence of a formally named biological species, physical culture, phenotype or mechanism. Absence claims are limited to the specified complete pinned inputs and recorded exact queries.
- The pinned NCBI projection and current official EFetch response were compared directly. No reconstruction of the original names archive, complete primary name-catalog census or global literature/culture search was performed; no broader name-class or culture absence is claimed.
- The three-member count is the complete GTDB source species, not three genomes exclusively assigned to NCBITaxon:2005740. Distinct taxon, sample, project and assembly identities remain separate.
- GTDB membership, supplied accession versions and all 47 metadata fields per member were inspected in the pinned census. No independent ANI calculation, sequence comparison or current remote re-resolution of catalog-only assembly, BioSample and BioProject identifiers was performed. Source isolation metadata are not generalized to every member or to the broader taxon.
- Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0025 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check.
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base source transitions are verified against retained original captures and exact changed-input receipts.
- Every new bundle still requires its own validate/save/check recipe; historical native receipts do not claim these later steps have run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T092051Z-archaeon_bms3abin16
kind: record
repository: CultureBotAI/TaxonMech
title: 'Record review: archaeon BMS3Abin16'
started_at: '2026-10-21T08:37:49Z'
finished_at: '2026-10-21T09:20:51Z'
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
summary: archaeon BMS3Abin16 has supported exact NCBI identity, carried lineage and
  source-scoped representation. No record-specific defect was established within the
  inspected sources.
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
  - path: data/taxa/archaea/archaeon_bms3abin16.yaml
    sha256: 833021191387379651e16b5f0585f543b39631247b74cbefbda06a7d038b381c
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
  selection: Batch-0025 target 10; next unreviewed path-order selection after excluding
    295 actual covered target paths. Canonical record_review.py list over the 39-bundle
    current base and all twenty-four actually saved branch worktrees, including ignored
    and hidden review bundles. Native corpus enumerated with os.walk including ignored/hidden
    files. Coverage only derives from explicit validated bundle targets, never inventories
    or reservations.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - NCBITaxon:2005740
targets:
- target_id: NCBITaxon:2005740
  path: data/taxa/archaea/archaeon_bms3abin16.yaml
  label: archaeon BMS3Abin16
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
  summary: NCBITaxon:2005740 denotes the exact SPECIES record archaeon BMS3Abin16,
    under NCBITaxon:93506, unclassified Archaea, with genetic code 11. All four carried
    ancestors and their literal names and ranks agree with the pinned taxonomy and
    current official NCBI response; EFetch omits root. ARCHAEA follows the taxonomic
    lineage, separately from EFetch Division metadata. No finer NCBI placement is
    inferred.
  target_ids:
  - NCBITaxon:2005740
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
  summary: Complete direct reads of all twelve named source, scope and path tables,
    including ignored files, used the exact target identifier, full literal label,
    slug and any asserted source identifier or synonym. The complete pinned NCBI parent
    graph has zero descendants for this target; zero imported BacDive strains agrees
    with the target/subtree inventory and culture-inventory slice. NCBITAXON 1 NAME
    and GTDB 3 GENOME agree with their source projections. All nineteen pinned GTDB
    genome shards were scanned and manifest-verified; all three full primary members
    and all three reverse mapping rows were inspected. Count 3 describes the whole
    source cluster, with one member explicitly classified under this NCBI target.
    Other optional-source misses are bounded to the pinned tables and exact queries.
    These misses do not establish worldwide absence of cultures, genomes, publications
    or biological observations.
  target_ids:
  - NCBITaxon:2005740
  evidence_ids:
  - record
  - taxonomy-inventory
  - lpsn-inventory
  - gtdb-mappings
  - gtdb-species
  - bacdive-inventory
  - culture-inventory
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
  - scope-row
  - path-row
  - genome-catalog-1
  - gtdb-full-scan
  - gtdb-member-ranks
  scope_note: Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs.
- check_id: gtdb-primary-counts
  name: Complete GTDB source-cluster count
  status: passed
  required: true
  summary: The native source count 3 equals the entire pinned species cluster. Distinct
    NCBI member identities remain separate; the count is not restricted to this exact
    target taxid.
  target_ids:
  - NCBITaxon:2005740
  evidence_ids:
  - gtdb-full-scan
  - gtdb-species
  - gtdb-mappings
  - gtdb-member-ranks
  - genome-catalog-1
  scope_note: All nineteen manifest-matching pinned GTDB shards; every selected cluster
    member and exact reverse-mapping row.
- check_id: gtdb-species-normalization
  name: Species-level mapping interpretation
  status: passed
  required: true
  summary: The complete pinned GTDB RS232 species GTDB:s__SZUA-236_sp002923215 contains
    three metagenome-derived genomes. Representative GB_GCA_002923215.1 at data/catalog/gtdb_genomes-0017.jsonl.gz
    line 29713 explicitly names archaeon BMS3Abin16 and gives ncbi_taxid and ncbi_species_taxid
    2005740. GB_GCA_002898035.1 at line 49030 is archaeon BMS3Bbin16 with both taxids
    2005739; GB_GCA_937897055.1 at line 41093 is the uncultured archaeon MAG DRR093005_bin.29_CONCOCT_v1.1_MAG
    with both taxids 115547. All supplied .1 accession versions are preserved. The
    complete reverse mapping rows retain closeMatch to 2005740 and 2005739 and broadMatch
    to 115547. All three NCBI targets have SPECIES rank in the pinned taxonomy; these
    are not strain-rank promotions. The source species row and native GTDB 3 GENOME
    attestation count the entire three-member cluster, of which one member explicitly
    carries the reviewed NCBI taxon. The separately attributed exact GTDB synonym/xref
    follow local species-level closeMatch normalization policy; the multiple reverse
    targets do not establish a defect or a globally one-to-one mapping. The native
    NCBI unclassified Archaea lineage remains separate from GTDB Hydrothermarchaeota/Hydrothermarchaeia
    classification. Each member has a different BioSample. The two BMS assemblies
    share project PRJDB5792, which does not establish genome or sequence identity.
    Their sub-seafloor sulfide-deposit metadata and the third member's marine-metagenome
    metadata remain member-specific source observations, not taxon-wide habitat or
    phenotype claims.
  target_ids:
  - NCBITaxon:2005740
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - gtdb-mappings
  - gtdb-species
  - mapping-policy
  - equivalence-contract
  - seed-owner
  - gtdb-full-scan
  - gtdb-member-ranks
  - genome-catalog-1
  scope_note: Local species-level closeMatch normalization; no strain/species conflation
    inferred from reverse multiplicity alone.
- check_id: strain-genome-evidence
  name: Imported strain links
  status: not_applicable
  required: false
  summary: This complete native record asserts no imported BacDive strain, culture
    deposit or strain-level genome link. A placeholder or MAG designation does not
    supply a deposit identity.
  target_ids:
  - NCBITaxon:2005740
  evidence_ids:
  - record
  - bacdive-inventory
  - culture-inventory
- check_id: nomenclature-authorities
  name: Nomenclatural publication authorities
  status: not_applicable
  required: false
  summary: No LPSN nomenclature, species-authority publication or type-strain sequence
    citation is asserted for this target; current NCBI name classes and bounded pinned
    LPSN inventory were checked.
  target_ids:
  - NCBITaxon:2005740
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - lpsn-inventory
- check_id: structured-adapter-applicability
  name: Gene or transcriptomics evidence applicability
  status: not_applicable
  required: false
  summary: 'Not applicable: the complete native record asserts no gene, protein, regulator,
    pathway, experimental trait, mechanism or transcriptome link.'
  target_ids:
  - NCBITaxon:2005740
  evidence_ids:
  - record
- check_id: historical-source-counts
  name: Historical aggregate edges
  status: not_applicable
  required: false
  summary: No historical medium, organism or trait aggregate is asserted in this target.
  target_ids:
  - NCBITaxon:2005740
  evidence_ids:
  - record
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
  - NCBITaxon:2005740
  evidence_ids:
  - strict-receipt
  command: just validate-strict data/taxa/archaea/archaeon_bms3abin16.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0025/strict-10.tsv
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
    these are historical runs, not new batch-0025 invocations. Missing terminal receipts
    or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts
    retain their original execution context. New review bundles still require individual
    validation/save/check.
  target_ids:
  - NCBITaxon:2005740
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
    certificate; these are historical runs, not new batch-0025 invocations. Missing
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
    certificate; these are historical runs, not new batch-0025 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check.
  target_ids:
  - NCBITaxon:2005740
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
    certificate; these are historical runs, not new batch-0025 invocations. Missing
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
    runs, not new batch-0025 invocations. Missing terminal receipts or reuse proof
    remain unavailable in unsaved previews. Exact-target strict receipts retain their
    original execution context. New review bundles still require individual validation/save/check.
  target_ids:
  - NCBITaxon:2005740
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
    certificate; these are historical runs, not new batch-0025 invocations. Missing
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
    certificate; these are historical runs, not new batch-0025 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check. 1073 passed, 3 skipped, 5 deselected
    in 1293.90s (0:21:33)
  target_ids:
  - NCBITaxon:2005740
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
    certificate; these are historical runs, not new batch-0025 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/taxa/archaea/archaeon_bms3abin16.yaml
  accessed_at: '2026-10-21T09:20:51Z'
  support: supports
  summary: Read the entire generated YAML, including identity, lineage, names, mappings,
    source attestations, all imported strains and links, and seed history.
  locator: entire TaxonRecord; identifier=NCBITaxon:2005740
  snapshot_sha256: 833021191387379651e16b5f0585f543b39631247b74cbefbda06a7d038b381c
- evidence_id: taxonomy-inventory
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-21T08:39:25Z'
  support: supports
  summary: Inspected the target and each carried ancestor, rank, parent, genetic code
    and source name classes.
  locator: 'line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""};
    line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"};
    line 15329: {"taxon_id":"NCBITaxon:93506","label":"unclassified Archaea","rank":"NO_RANK","parent_id":"NCBITaxon:2157"};
    line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"};
    line 509000: {"taxon_id":"NCBITaxon:2005740","label":"archaeon BMS3Abin16","rank":"SPECIES","parent_id":"NCBITaxon:93506","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon|gtdb","retired_into":"","taxonomy_snapshot":"2026-09-13"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bms3abin16","archaeon_bms3abin16","gtdb:s__szua-236_sp002923215","ncbitaxon:2005740","szua-236
    sp002923215"]; complete table data rows: 650767.'
- evidence_id: scope-row
  kind: database
  reference: curation/seed_scope.tsv
  accessed_at: '2026-10-21T08:39:25Z'
  support: supports
  summary: Exact target is included in the declared seed scope.
  locator: 'line 90037: {"identifier":"NCBITaxon:2005740","added":"2026-09-13","reason":"attested
    rule: archaeon BMS3Abin16, 2 sources incl. NCBI"}'
  snapshot_sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bms3abin16","archaeon_bms3abin16","gtdb:s__szua-236_sp002923215","ncbitaxon:2005740","szua-236
    sp002923215"]; complete table data rows: 626048.'
- evidence_id: path-row
  kind: database
  reference: data/taxa/PATHS.tsv
  accessed_at: '2026-10-21T08:39:25Z'
  support: supports
  summary: Indexed path resolves to this exact NCBI taxon.
  locator: 'line 318041: {"identifier":"NCBITaxon:2005740","slug":"archaeon_bms3abin16"}'
  snapshot_sha256: f8f2e0721cb6839b30530b44be0d3004b9f0e6e2d4be8736f235b10117a8bd99
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bms3abin16","archaeon_bms3abin16","gtdb:s__szua-236_sp002923215","ncbitaxon:2005740","szua-236
    sp002923215"]; complete table data rows: 626048.'
- evidence_id: ncbi-live
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=910144,910145,910160,910080,910081,910082,910083,910084,584993,2005740&retmode=xml
  accessed_at: '2026-10-21T08:37:11Z'
  support: supports
  summary: 'Inspected the successful official response for this exact taxon: scientific
    name, rank, parent, source name classes, lineage and genetic code. Current authority
    and pinned September inventory remain distinct observations.'
  locator: TaxaSet/Taxon[TaxId='2005740']; ten-target captured response
  snapshot_sha256: 54b336ddf0ac593cf79111cc2b14bb78e80a930fc437e81dce98d3999f947598
- evidence_id: lpsn-inventory
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-21T08:39:25Z'
  support: supports
  summary: Complete exact taxon, literal name and slug queries found no associated
    LPSN inventory row; this observation is bounded to the pinned inventory.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bms3abin16","archaeon_bms3abin16","gtdb:s__szua-236_sp002923215","ncbitaxon:2005740","szua-236
    sp002923215"]; complete table data rows: 34301.'
- evidence_id: gtdb-mappings
  kind: database
  reference: data/raw/gtdb_mappings.tsv
  accessed_at: '2026-10-21T08:39:25Z'
  support: supports
  summary: Inspected the exact target and all source-ID reverse mapping rows, preserving
    each source predicate and whole-species genome count.
  locator: 'line 7958: {"gtdb_id":"GTDB:s__SZUA-236_sp002923215","gtdb_label":"s__SZUA-236_sp002923215","gtdb_parent":"GTDB:g__SZUA-236","ncbitaxon_id":"NCBITaxon:115547","predicate":"skos:broadMatch","genome_count":"3"};
    line 120235: {"gtdb_id":"GTDB:s__SZUA-236_sp002923215","gtdb_label":"s__SZUA-236_sp002923215","gtdb_parent":"GTDB:g__SZUA-236","ncbitaxon_id":"NCBITaxon:2005739","predicate":"skos:closeMatch","genome_count":"3"};
    line 120236: {"gtdb_id":"GTDB:s__SZUA-236_sp002923215","gtdb_label":"s__SZUA-236_sp002923215","gtdb_parent":"GTDB:g__SZUA-236","ncbitaxon_id":"NCBITaxon:2005740","predicate":"skos:closeMatch","genome_count":"3"}'
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bms3abin16","archaeon_bms3abin16","gtdb:s__szua-236_sp002923215","ncbitaxon:2005740","szua-236
    sp002923215"]; complete table data rows: 322327.'
- evidence_id: gtdb-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-21T08:39:25Z'
  support: supports
  summary: Inspected the complete selected GTDB source-species row, including its
    source parent and whole-cluster count.
  locator: 'line 162021: {"gtdb_id":"GTDB:s__SZUA-236_sp002923215","label":"s__SZUA-236_sp002923215","parent":"GTDB:g__SZUA-236","genome_count":"3"}'
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bms3abin16","archaeon_bms3abin16","gtdb:s__szua-236_sp002923215","ncbitaxon:2005740","szua-236
    sp002923215"]; complete table data rows: 199923.'
- evidence_id: bacdive-inventory
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-21T08:39:25Z'
  support: supports
  summary: Complete inventory selection covers the exact target and descendants from
    the complete NCBI parent graph; its imported strain population was compared with
    the complete YAML.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: 029fd6d1f53ef7f90684130bf0d644ed3edd1d8fbeb065a511ae928f160b1eea
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bms3abin16","archaeon_bms3abin16","gtdb:s__szua-236_sp002923215","ncbitaxon:2005740","szua-236
    sp002923215"]; complete table data rows: 101417.'
- evidence_id: culture-inventory
  kind: database
  reference: data/raw/culture_collection_strains.tsv
  accessed_at: '2026-10-21T08:39:25Z'
  support: supports
  summary: Inspected exact culture-inventory associations; an isolate name or genome
    does not create an inferred deposit.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: 810fdcb16abd6330fb15bb03d4c74b18db86be36a7c599df7c6b2498d9735c95
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bms3abin16","archaeon_bms3abin16","gtdb:s__szua-236_sp002923215","ncbitaxon:2005740","szua-236
    sp002923215"]; complete table data rows: 154969.'
- evidence_id: gold-organisms
  kind: database
  reference: data/raw/gold_organisms.tsv
  accessed_at: '2026-10-21T08:39:25Z'
  support: supports
  summary: Inspected the exact GOLD organism count row or bounded absence, without
    converting counts to phenotypes.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bms3abin16","archaeon_bms3abin16","gtdb:s__szua-236_sp002923215","ncbitaxon:2005740","szua-236
    sp002923215"]; complete table data rows: 45616.'
- evidence_id: mediadive-taxa
  kind: database
  reference: data/raw/mediadive_taxa.tsv
  accessed_at: '2026-10-21T08:39:25Z'
  support: supports
  summary: Inspected the exact MediaDive medium count row or bounded absence, without
    converting counts to phenotypes.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: 3f74b78cadfcdb6aeae953e09fdb39e34fd9c5d5ed0be65a04a5d7fb02355905
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bms3abin16","archaeon_bms3abin16","gtdb:s__szua-236_sp002923215","ncbitaxon:2005740","szua-236
    sp002923215"]; complete table data rows: 14225.'
- evidence_id: madin-taxa
  kind: database
  reference: data/raw/madin_taxa.tsv
  accessed_at: '2026-10-21T08:39:25Z'
  support: supports
  summary: Inspected the exact Madin trait-assertion count row or bounded absence,
    without converting counts to phenotypes.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bms3abin16","archaeon_bms3abin16","gtdb:s__szua-236_sp002923215","ncbitaxon:2005740","szua-236
    sp002923215"]; complete table data rows: 34148.'
- evidence_id: bactotraits-taxa
  kind: database
  reference: data/raw/bactotraits_taxa.tsv
  accessed_at: '2026-10-21T08:39:25Z'
  support: supports
  summary: Inspected the exact BactoTraits trait-assertion count row or bounded absence,
    without converting counts to phenotypes.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: 976d109cef832d8bf27cc105f67a42efbe900b6946736298602ef6d11158b197
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bms3abin16","archaeon_bms3abin16","gtdb:s__szua-236_sp002923215","ncbitaxon:2005740","szua-236
    sp002923215"]; complete table data rows: 9658.'
- evidence_id: mapping-policy
  kind: record_content
  reference: docs/HARMONIZATION.md
  accessed_at: '2026-10-21T09:20:51Z'
  support: supports
  summary: Policy permits source-scoped species-level closeMatch normalization and
    LPSN-linked species xrefs/synonyms, retains pooled broadMatch entries and carries
    NCBI lineage unchanged. Multiple reverse target mappings do not alone establish
    a normalization defect or make genomes and physical strains identical.
  locator: Mapping predicates; Which strains belong to a record
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
- evidence_id: equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-21T09:20:51Z'
  support: supports
  summary: TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations
    remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes
    under the source taxon.
  locator: TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
- evidence_id: seed-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-21T09:20:51Z'
  support: supports
  summary: Inspected source mapping normalization, NCBI NAME and whole-source-species
    GTDB GENOME attestation construction, and seed history. Qualified source mappings
    and physical strain derivation remain distinct.
  locator: GTDB mapping construction lines 443–478; source attestation construction
    lines 551–595; seed history construction lines 630–647
  snapshot_sha256: 3cc30f6413a293165385dfc1860505fe389e5adfe9aa3d168f76aa4cb2ac36bd
- evidence_id: manifest
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-21T09:20:51Z'
  support: supports
  summary: Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd,
    upstream input hashes and extraction time 2026-09-13T17:50:44Z.
  locator: kg_microbe_source, inputs, extracted_at
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
- evidence_id: overlay-manifests
  kind: record_content
  reference: data/atb/MANIFEST.yaml
  accessed_at: '2026-10-21T09:20:51Z'
  support: supports
  summary: Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z,
    matching the sole seed event. StrainInfo manifest is independently captured in
    source.inputs.
  locator: extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml
  snapshot_sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
- evidence_id: genome-catalog-1
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0017.jsonl.gz
  accessed_at: '2026-10-21T08:38:56Z'
  support: supports
  summary: Inspected the complete selected GTDB species cluster, supplied assembly
    versions, exact NCBI taxid/species-taxid and MAG/isolate metadata. Cluster counts
    are not counts of genomes exclusive to this NCBI target, physical cultures or
    identical sequences.
  locator: 'line 29713: {"accession":"GB_GCA_002923215.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Hydrothermarchaeota;c__Hydrothermarchaeia;o__Hydrothermarchaeales;f__SZUA-236;g__SZUA-236;s__SZUA-236
    sp002923215","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM292321v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJDB5792","ncbi_biosample":"SAMD00081376","ncbi_contig_count":"175","ncbi_contig_n50":"12106","ncbi_country":"none","ncbi_date":"2018-01-25","ncbi_genbank_assembly_accession":"GCA_002923215.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"BMS3Abin16","ncbi_isolation_source":"sub-seafloor
    sulfide deposits","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"archaeon
    BMS3Abin16","ncbi_protein_count":"1863","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2018-01-25","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2005740","ncbi_ssu_count":"1","ncbi_strain_identifiers":"BMS3Abin16","ncbi_submitter":"JAMSTEC","ncbi_taxid":"2005740","ncbi_taxonomy":"d__Archaea;p__;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__unclassified
    Archaea;s__archaeon BMS3Abin16","ncbi_total_gap_length":"0","ncbi_total_length":"1628016","ncbi_translation_table":"11","ncbi_trna_count":"29","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1628016","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"BDTI00000000.1"};
    line 41093: {"accession":"GB_GCA_937897055.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Hydrothermarchaeota;c__Hydrothermarchaeia;o__Hydrothermarchaeales;f__SZUA-236;g__SZUA-236;s__SZUA-236
    sp002923215","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"DRR093005_bin.29_CONCOCT_v1.1_MAG","ncbi_assembly_type":"na","ncbi_bioproject":"PRJEB51078","ncbi_biosample":"SAMEA14074663","ncbi_contig_count":"92","ncbi_contig_n50":"57719","ncbi_country":"none","ncbi_date":"2023-01-10","ncbi_genbank_assembly_accession":"GCA_937897055.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"DRR093005_bin.29_CONCOCT_v1.1_MAG","ncbi_isolation_source":"marine
    metagenome","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"uncultured
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-01-10","ncbi_spanned_gaps":"0","ncbi_species_taxid":"115547","ncbi_ssu_count":"none","ncbi_strain_identifiers":"DRR093005_bin.29_CONCOCT_v1.1_MAG","ncbi_submitter":"European
    Bioinformatics Institute","ncbi_taxid":"115547","ncbi_taxonomy":"d__Archaea;p__;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__environmental
    samples;s__uncultured archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1991497","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1991497","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"CALCPX000000000.1"};
    line 49030: {"accession":"GB_GCA_002898035.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Hydrothermarchaeota;c__Hydrothermarchaeia;o__Hydrothermarchaeales;f__SZUA-236;g__SZUA-236;s__SZUA-236
    sp002923215","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM289803v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJDB5792","ncbi_biosample":"SAMD00081393","ncbi_contig_count":"197","ncbi_contig_n50":"6378","ncbi_country":"none","ncbi_date":"2017-12-14","ncbi_genbank_assembly_accession":"GCA_002898035.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"BMS3Bbin16","ncbi_isolation_source":"sub-seafloor
    sulfide deposits","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"archaeon
    BMS3Bbin16","ncbi_protein_count":"1292","ncbi_refseq_category":"na","ncbi_rrna_count":"1","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2017-12-14","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2005739","ncbi_ssu_count":"0","ncbi_strain_identifiers":"BMS3Bbin16","ncbi_submitter":"JAMSTEC","ncbi_taxid":"2005739","ncbi_taxonomy":"d__Archaea;p__;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__unclassified
    Archaea;s__archaeon BMS3Bbin16","ncbi_total_gap_length":"0","ncbi_total_length":"1164696","ncbi_translation_table":"11","ncbi_trna_count":"21","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1164696","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"BDTZ00000000.1"}'
  snapshot_sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
- evidence_id: gtdb-full-scan
  kind: search
  reference: data/catalog/MANIFEST.json
  accessed_at: '2026-10-21T08:38:56Z'
  support: supports
  summary: All nineteen pinned RS232 shards and 901341 rows match the manifest census.
    The complete selected source cluster and its reverse mappings were inspected;
    reverse target multiplicity is preserved and is not represented as a globally
    one-to-one mapping.
  locator: '{"target_id":"NCBITaxon:2005740","source_species":"GTDB:s__SZUA-236_sp002923215","cluster_count":3,"members":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":29713,"sha256":"f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6","row":{"accession":"GB_GCA_002923215.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Hydrothermarchaeota;c__Hydrothermarchaeia;o__Hydrothermarchaeales;f__SZUA-236;g__SZUA-236;s__SZUA-236
    sp002923215","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM292321v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJDB5792","ncbi_biosample":"SAMD00081376","ncbi_contig_count":"175","ncbi_contig_n50":"12106","ncbi_country":"none","ncbi_date":"2018-01-25","ncbi_genbank_assembly_accession":"GCA_002923215.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"BMS3Abin16","ncbi_isolation_source":"sub-seafloor
    sulfide deposits","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"archaeon
    BMS3Abin16","ncbi_protein_count":"1863","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2018-01-25","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2005740","ncbi_ssu_count":"1","ncbi_strain_identifiers":"BMS3Abin16","ncbi_submitter":"JAMSTEC","ncbi_taxid":"2005740","ncbi_taxonomy":"d__Archaea;p__;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__unclassified
    Archaea;s__archaeon BMS3Abin16","ncbi_total_gap_length":"0","ncbi_total_length":"1628016","ncbi_translation_table":"11","ncbi_trna_count":"29","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1628016","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"BDTI00000000.1"}},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":41093,"sha256":"f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6","row":{"accession":"GB_GCA_937897055.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Hydrothermarchaeota;c__Hydrothermarchaeia;o__Hydrothermarchaeales;f__SZUA-236;g__SZUA-236;s__SZUA-236
    sp002923215","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"DRR093005_bin.29_CONCOCT_v1.1_MAG","ncbi_assembly_type":"na","ncbi_bioproject":"PRJEB51078","ncbi_biosample":"SAMEA14074663","ncbi_contig_count":"92","ncbi_contig_n50":"57719","ncbi_country":"none","ncbi_date":"2023-01-10","ncbi_genbank_assembly_accession":"GCA_937897055.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"DRR093005_bin.29_CONCOCT_v1.1_MAG","ncbi_isolation_source":"marine
    metagenome","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"uncultured
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-01-10","ncbi_spanned_gaps":"0","ncbi_species_taxid":"115547","ncbi_ssu_count":"none","ncbi_strain_identifiers":"DRR093005_bin.29_CONCOCT_v1.1_MAG","ncbi_submitter":"European
    Bioinformatics Institute","ncbi_taxid":"115547","ncbi_taxonomy":"d__Archaea;p__;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__environmental
    samples;s__uncultured archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1991497","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1991497","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"CALCPX000000000.1"}},{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":49030,"sha256":"f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6","row":{"accession":"GB_GCA_002898035.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Hydrothermarchaeota;c__Hydrothermarchaeia;o__Hydrothermarchaeales;f__SZUA-236;g__SZUA-236;s__SZUA-236
    sp002923215","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM289803v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJDB5792","ncbi_biosample":"SAMD00081393","ncbi_contig_count":"197","ncbi_contig_n50":"6378","ncbi_country":"none","ncbi_date":"2017-12-14","ncbi_genbank_assembly_accession":"GCA_002898035.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"BMS3Bbin16","ncbi_isolation_source":"sub-seafloor
    sulfide deposits","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"archaeon
    BMS3Bbin16","ncbi_protein_count":"1292","ncbi_refseq_category":"na","ncbi_rrna_count":"1","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2017-12-14","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2005739","ncbi_ssu_count":"0","ncbi_strain_identifiers":"BMS3Bbin16","ncbi_submitter":"JAMSTEC","ncbi_taxid":"2005739","ncbi_taxonomy":"d__Archaea;p__;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__unclassified
    Archaea;s__archaeon BMS3Bbin16","ncbi_total_gap_length":"0","ncbi_total_length":"1164696","ncbi_translation_table":"11","ncbi_trna_count":"21","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1164696","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"BDTZ00000000.1"}}],"reverse_mappings":[{"line":7958,"row":{"gtdb_id":"GTDB:s__SZUA-236_sp002923215","gtdb_label":"s__SZUA-236_sp002923215","gtdb_parent":"GTDB:g__SZUA-236","ncbitaxon_id":"NCBITaxon:115547","predicate":"skos:broadMatch","genome_count":"3"}},{"line":120235,"row":{"gtdb_id":"GTDB:s__SZUA-236_sp002923215","gtdb_label":"s__SZUA-236_sp002923215","gtdb_parent":"GTDB:g__SZUA-236","ncbitaxon_id":"NCBITaxon:2005739","predicate":"skos:closeMatch","genome_count":"3"}},{"line":120236,"row":{"gtdb_id":"GTDB:s__SZUA-236_sp002923215","gtdb_label":"s__SZUA-236_sp002923215","gtdb_parent":"GTDB:g__SZUA-236","ncbitaxon_id":"NCBITaxon:2005740","predicate":"skos:closeMatch","genome_count":"3"}}]}'
  snapshot_sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
  search_scope: All enumerated GTDB primary shards, including ignored files. Exact
    source species ID from terminal species token with spaces converted to underscores;
    internal genus/epithet underscores preserved. Exact supplied GTDB genome accession
    also selected. No broad biological absence claim.
- evidence_id: gtdb-member-ranks
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-21T08:39:37Z'
  support: supports
  summary: Inspected exact pinned NCBI identity, rank and parent rows for every selected
    source-cluster member. Each member is assigned to a distinct SPECIES target; source-species
    membership does not establish strain identity, sequence identity or a globally
    one-to-one mapping.
  locator: 'line 21083: {"taxon_id":"NCBITaxon:115547","label":"uncultured archaeon","rank":"SPECIES","parent_id":"NCBITaxon:48510","genetic_code":"11","exact_synonyms":"uncultured
    Archaea archaeon|uncultured archaeoote","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon|gtdb|gold","retired_into":"","taxonomy_snapshot":"2026-09-13"};
    line 508999: {"taxon_id":"NCBITaxon:2005739","label":"archaeon BMS3Bbin16","rank":"SPECIES","parent_id":"NCBITaxon:93506","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon|gtdb","retired_into":"","taxonomy_snapshot":"2026-09-13"};
    line 509000: {"taxon_id":"NCBITaxon:2005740","label":"archaeon BMS3Abin16","rank":"SPECIES","parent_id":"NCBITaxon:93506","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon|gtdb","retired_into":"","taxonomy_snapshot":"2026-09-13"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
  search_scope: Complete ignored-inclusive direct TSV read selecting the exact ncbi_taxid
    and ncbi_species_taxid values from all three inspected GTDB members; source-rank
    context only, no broader taxonomic or strain identity inference.
- evidence_id: native-gate-reuse
  kind: validation
  reference: /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0025/native-gate-reuse.json
  accessed_at: '2026-10-21T08:41:24Z'
  support: supports
  summary: Retained explicit verification of identical base/native inputs authorizes
    historical native-gate reuse; original command receipts remain separately cited.
  locator: base, native_inputs_unchanged, source_directory, gates, input_proof_path
    and input_proof_sha256
  snapshot_sha256: 7a8386cb1c890fa7b69af0a7b328194cc8205bab7e2963b99d9822f72ce322d0
- evidence_id: strict-receipt
  kind: validation
  reference: just validate-strict data/taxa/archaea/archaeon_bms3abin16.yaml --out
    /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0025/strict-10.tsv
  accessed_at: '2026-10-21T08:38:09Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0025/repo;\
    \ started 2026-10-21T08:38:05Z, finished 2026-10-21T08:38:09Z, exit 0. This exact\
    \ generated YAML only; its captured bytes remain unchanged. Actual earlier per-target\
    \ invocation; the receipt retains its original cwd and times.\nValidating 1 files\
    \ with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0025/src/taxonmech/schema/taxonmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0025/strict-10.tsv"
  locator: This exact generated YAML only; its captured bytes remain unchanged. Actual
    earlier per-target invocation; the receipt retains its original cwd and times.
  snapshot_sha256: b123421c2c9a58f17e09af0b6e48a05e7c17568767b33e4e0ca1f37431377c18
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
    certificate; these are historical runs, not new batch-0025 invocations. Missing
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
    certificate; these are historical runs, not new batch-0025 invocations. Missing
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
    \ these are historical runs, not new batch-0025 invocations. Missing terminal\
    \ receipts or reuse proof remain unavailable in unsaved previews. Exact-target\
    \ strict receipts retain their original execution context. New review bundles\
    \ still require individual validation/save/check.\nuv run python scripts/verify_corpus.py\
    \ \nexpected 626048 records, found 626048 on disk\n  missing:   0\n  extra:  \
    \   0\n  differing: 0\n\ncorpus reproduces exactly from data/raw/ and curation/seed_scope.tsv"
  locator: All 626,048 generated taxon YAMLs, not a focused approximation. Actual
    native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
    original cwd, times, commands, log hashes and terminal exit codes identify the
    executions. Reused repository-wide receipts require the explicit same-base/native-input
    certificate; these are historical runs, not new batch-0025 invocations. Missing
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
    certificate; these are historical runs, not new batch-0025 invocations. Missing
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
    certificate; these are historical runs, not new batch-0025 invocations. Missing
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
    \ these are historical runs, not new batch-0025 invocations. Missing terminal\
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
    these are historical runs, not new batch-0025 invocations. Missing terminal receipts
    or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts
    retain their original execution context. New review bundles still require individual
    validation/save/check.
  snapshot_sha256: dcb3f98d5c8ce264240732733ca70a5b93ee3e818d03f809d428748abffefca3
assessments:
- assessment_id: identity
  area: identity
  topic: Exact taxon and source lineage
  outcome: supported
  summary: NCBITaxon:2005740 denotes the exact SPECIES record archaeon BMS3Abin16,
    under NCBITaxon:93506, unclassified Archaea, with genetic code 11. All four carried
    ancestors and their literal names and ranks agree with the pinned taxonomy and
    current official NCBI response; EFetch omits root. ARCHAEA follows the taxonomic
    lineage, separately from EFetch Division metadata. No finer NCBI placement is
    inferred.
  target_ids:
  - NCBITaxon:2005740
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
  summary: The pinned NCBI exact, related and broad synonym columns are empty, and
    current EFetch supplies no OtherNames entry for this exact taxon. Complete exact
    queries in the pinned LPSN inventory find no associated row. The native designation
    does not assert a formal nomenclatural authority, publication or type-deposit
    relationship. The separately attributed GTDB normalized exact synonym and xref
    follow local species-level closeMatch policy while the qualified source mapping
    remains explicit. This inventory observation does not establish worldwide nomenclatural
    absence.
  target_ids:
  - NCBITaxon:2005740
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - lpsn-inventory
  - mapping-policy
  - genome-catalog-1
  - gtdb-full-scan
  - gtdb-member-ranks
- assessment_id: completeness
  area: completeness
  topic: Imported subtree and source assertion units
  outcome: supported
  summary: Complete direct reads of all twelve named source, scope and path tables,
    including ignored files, used the exact target identifier, full literal label,
    slug and any asserted source identifier or synonym. The complete pinned NCBI parent
    graph has zero descendants for this target; zero imported BacDive strains agrees
    with the target/subtree inventory and culture-inventory slice. NCBITAXON 1 NAME
    and GTDB 3 GENOME agree with their source projections. All nineteen pinned GTDB
    genome shards were scanned and manifest-verified; all three full primary members
    and all three reverse mapping rows were inspected. Count 3 describes the whole
    source cluster, with one member explicitly classified under this NCBI target.
    Other optional-source misses are bounded to the pinned tables and exact queries.
    These misses do not establish worldwide absence of cultures, genomes, publications
    or biological observations.
  target_ids:
  - NCBITaxon:2005740
  evidence_ids:
  - record
  - taxonomy-inventory
  - scope-row
  - path-row
  - lpsn-inventory
  - bacdive-inventory
  - culture-inventory
  - gtdb-mappings
  - gtdb-species
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
  - genome-catalog-1
  - gtdb-full-scan
  - gtdb-member-ranks
- assessment_id: taxonomy-mapping
  area: grounding
  topic: Qualified species mapping and target scope
  outcome: supported
  summary: The complete pinned GTDB RS232 species GTDB:s__SZUA-236_sp002923215 contains
    three metagenome-derived genomes. Representative GB_GCA_002923215.1 at data/catalog/gtdb_genomes-0017.jsonl.gz
    line 29713 explicitly names archaeon BMS3Abin16 and gives ncbi_taxid and ncbi_species_taxid
    2005740. GB_GCA_002898035.1 at line 49030 is archaeon BMS3Bbin16 with both taxids
    2005739; GB_GCA_937897055.1 at line 41093 is the uncultured archaeon MAG DRR093005_bin.29_CONCOCT_v1.1_MAG
    with both taxids 115547. All supplied .1 accession versions are preserved. The
    complete reverse mapping rows retain closeMatch to 2005740 and 2005739 and broadMatch
    to 115547. All three NCBI targets have SPECIES rank in the pinned taxonomy; these
    are not strain-rank promotions. The source species row and native GTDB 3 GENOME
    attestation count the entire three-member cluster, of which one member explicitly
    carries the reviewed NCBI taxon. The separately attributed exact GTDB synonym/xref
    follow local species-level closeMatch normalization policy; the multiple reverse
    targets do not establish a defect or a globally one-to-one mapping. The native
    NCBI unclassified Archaea lineage remains separate from GTDB Hydrothermarchaeota/Hydrothermarchaeia
    classification. Each member has a different BioSample. The two BMS assemblies
    share project PRJDB5792, which does not establish genome or sequence identity.
    Their sub-seafloor sulfide-deposit metadata and the third member's marine-metagenome
    metadata remain member-specific source observations, not taxon-wide habitat or
    phenotype claims.
  target_ids:
  - NCBITaxon:2005740
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
  - gtdb-member-ranks
- assessment_id: native-status
  area: provenance
  topic: Unchanged native status and history
  outcome: supported
  summary: EXACT grounding and SEEDED mapping status preserve the generated source
    state. The sole SEEDED_FROM_SOURCES event at 2026-09-13T17:54:04Z agrees with
    the latest raw, ATB and StrainInfo manifest extraction. The exact seed-scope and
    PATHS rows preserve inclusion and path. No manual curation, scientific status
    promotion or new native history event is inferred.
  target_ids:
  - NCBITaxon:2005740
  evidence_ids:
  - record
  - manifest
  - overlay-manifests
  - scope-row
  - path-row
findings: []
actions: []
limitations:
- SPECIES rank and the literal designation are source taxonomy assertions, not independent
  evidence of a formally named biological species, physical culture, phenotype or
  mechanism. Absence claims are limited to the specified complete pinned inputs and
  recorded exact queries.
- The pinned NCBI projection and current official EFetch response were compared directly.
  No reconstruction of the original names archive, complete primary name-catalog census
  or global literature/culture search was performed; no broader name-class or culture
  absence is claimed.
- The three-member count is the complete GTDB source species, not three genomes exclusively
  assigned to NCBITaxon:2005740. Distinct taxon, sample, project and assembly identities
  remain separate.
- GTDB membership, supplied accession versions and all 47 metadata fields per member
  were inspected in the pinned census. No independent ANI calculation, sequence comparison
  or current remote re-resolution of catalog-only assembly, BioSample and BioProject
  identifiers was performed. Source isolation metadata are not generalized to every
  member or to the broader taxon.
- Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
  original cwd, times, commands, log hashes and terminal exit codes identify the executions.
  Reused repository-wide receipts require the explicit same-base/native-input certificate;
  these are historical runs, not new batch-0025 invocations. Missing terminal receipts
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
- batch-0025
- archaea
- generated
- source-checked
```
