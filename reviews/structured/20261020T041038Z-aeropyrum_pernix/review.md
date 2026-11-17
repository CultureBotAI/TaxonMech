# Record review: Aeropyrum pernix

- Review: 20261020T041038Z-aeropyrum_pernix
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-20T03:58:06Z
- Finished UTC: 2026-10-20T04:10:38Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Aeropyrum pernix has supported exact NCBI identity and faithfully projected source assertions.

## Scope And Provenance

Entire single generated record, including all source assertions and imported strains.

Selection: Original unreviewed path-order position 68; batch-0007 target 8. Excluded 112 actual targets from validated main and local batch-0001/0002/0003/0004/0005/0006 listings; full corpus enumeration includes ignored files.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9b5a8fff5185b38dc5c77bb35235152c81ea7765.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:56636 | data/taxa/archaea/aeropyrum_pernix.yaml | generated | Aeropyrum pernix |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact NCBI taxon, rank and lineage | passed | True | NCBITaxon:56636 | NCBITaxon:56636 denotes Aeropyrum pernix, rank SPECIES, parent NCBITaxon:56635, genetic code11. All 9 carried ancestors, literal labels and ranks agree with pinned NCBI and current EFetch. |
| Complete exact identifier and name inventory search | passed | True | NCBITaxon:56636 | The one species-filed BacDive strain is retained even though some genome objects refer to child272557. Direct-species historical MediaDive2, GOLD3 and Madin6 units are not descendant sums. Source projects and samples remain narrow contextual links; optional expression-module coverage is not established. |
| Complete primary GTDB cluster membership | passed | True | NCBITaxon:56636 | Exact source cluster counts agree with carried mappings where present; LPSN-only species bridges remain distinct from direct GTDB attestations. |
| Optional structured expression-module context | unavailable | False | NCBITaxon:56636 | No matching Aeropyrum dataset/component was established. Cbf5/accession and transcriptome-project names remain source descriptions, not inferred functions. |
| Complete strain and genome-source assertions | passed | True | NCBITaxon:56636 | BacDive4195 is explicitly filed at species56636, with K1 and ATCC700893/DSM11879/JCM9820/NBRC100138. Same-species LPSN deposits support the derived type flag. StrainInfo44195.3 supports four distinct deposits118657/118658/118659/335948 and no sequence list. GOLD Go0000767 ATCC700893 links to four projects: Gp0000767, Gp0102910, Gp0225950 and Gp0225951. Only Gp0000767 is linked in the inspected analyses to Ga0039428/GCA_000011125.1/IMG2923402010; the two named transcriptome projects retain their own samples and are not treated as genome analyses. Full discovery finds no project for Go0624942 JCM or Go0624943 DSM. BV272557.25 supplies the explicit BacDive-associated genome; BV272557.33 explicitly matches NBRC:100138 and has no assembly_accession field, so the absent BV assembly assertion is supported. Bare K1 fails culture-key normalization. The2 assembly,4 genome and28 related assertions exactly match the imported multiset. |
| Original manifest-pinned aggregate edges | unavailable | True | NCBITaxon:56636 | Pinned inventory counts agree; independent historical recounting remains unavailable for gold, mediadive, madin_etal. |
| Initial quality-gate setup attempt | failed | False | NCBITaxon:56636 | Actual exit 1: missing ruff; superseded by the separately recorded successful full retry. |
| Native strict record validation | passed | True | NCBITaxon:56636 | Actual terminal exit code 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. |
| Repository history validation | passed | True | NCBITaxon:56636 | Actual terminal exit code 0. All 17 standalone history records; the generated seed event was also inspected in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| Full-corpus exact reproduction | passed | True | NCBITaxon:56636 | Actual terminal exit code 0. All 625,960 generated taxon YAMLs, not a focused approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| Native product ID/label gate | passed | True | NCBITaxon:56636 | Actual terminal exit code 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| Authoritative complete quality gate | passed | True | NCBITaxon:56636 | Actual terminal exit code 0. Repository-wide just qc, including native corpus-wide checks. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. Pytest reported 1055 passed, 3 skipped and 5 deselected; the native QC recipe completed successfully. |

## Scientific And Domain Assessments

### Exact taxon and source lineage

identity: supported. Targets: NCBITaxon:56636.

NCBITaxon:56636 denotes Aeropyrum pernix, rank SPECIES, parent NCBITaxon:56635, genetic code11. All 9 carried ancestors, literal labels and ranks agree with pinned NCBI and current EFetch.

### Name classes and nomenclatural scope

nomenclature: supported. Targets: NCBITaxon:56636.

LPSN772925 supports Sako et al.1996, valid ICNP publication and correct-name status, with type K1 and four deposits. Both DOIs resolve and PMID8863437 supports the original description and JCM9820 type designation. AB008745.2 resolves at taxon56636 with strainK1; its title describes rRNA and an intron-encoded homing endonuclease, not a new functional assertion in this review.

### Imported subtree and source assertion units

completeness: supported. Targets: NCBITaxon:56636.

The one species-filed BacDive strain is retained even though some genome objects refer to child272557. Direct-species historical MediaDive2, GOLD3 and Madin6 units are not descendant sums. Source projects and samples remain narrow contextual links; optional expression-module coverage is not established.

### Qualified species mapping and target scope

grounding: supported. Targets: NCBITaxon:56636.

The same-taxon LPSN bridge supports the GTDB:s__Aeropyrum_pernix closeMatch, xref and count2. Primary membership comprises K1 taxon272557 and YK1-12-2013 taxon56636. Source species count2 is retained separately from the single imported BacDive strain.

### Strain, deposit and genome-source links

evidence: supported. Targets: NCBITaxon:56636.

BacDive4195 is explicitly filed at species56636, with K1 and ATCC700893/DSM11879/JCM9820/NBRC100138. Same-species LPSN deposits support the derived type flag. StrainInfo44195.3 supports four distinct deposits118657/118658/118659/335948 and no sequence list. GOLD Go0000767 ATCC700893 links to four projects: Gp0000767, Gp0102910, Gp0225950 and Gp0225951. Only Gp0000767 is linked in the inspected analyses to Ga0039428/GCA_000011125.1/IMG2923402010; the two named transcriptome projects retain their own samples and are not treated as genome analyses. Full discovery finds no project for Go0624942 JCM or Go0624943 DSM. BV272557.25 supplies the explicit BacDive-associated genome; BV272557.33 explicitly matches NBRC:100138 and has no assembly_accession field, so the absent BV assembly assertion is supported. Bare K1 fails culture-key normalization. The2 assembly,4 genome and28 related assertions exactly match the imported multiset.

### Unchanged native status and history

provenance: supported. Targets: NCBITaxon:56636.

Grounding EXACT, mapping SEEDED and the sole 2026-09-13T17:54:04Z seed event remain unchanged and agree with the latest extraction time. No curation history or native status is promoted.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### recover-pinned-aggregate-inputs

Recover manifest-hash-matching original aggregate inputs and independently recount the exact target assertions through the maintained extractor; do not edit generated YAML.

- Require exact original input SHA-256 before using it as historical evidence.
- Recount only the exact target with each source's own assertion unit and compare to its pinned inventory row.
- Record any discrepancy in a new review observation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/taxa/archaea/aeropyrum_pernix.yaml; entire TaxonRecord; identifier=NCBITaxon:56636 | supports | Read the entire generated YAML, including identity, lineage, names, mappings, source attestations, all imported strains and links, and seed history. |
| taxonomy-inventory | data/raw/ncbitaxon_taxa.tsv; line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""}; line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"}; line 2980: {"taxon_id":"NCBITaxon:28889","label":"Thermoproteota","rank":"PHYLUM","parent_id":"NCBITaxon:1783275"}; line 7138: {"taxon_id":"NCBITaxon:56635","label":"Aeropyrum","rank":"GENUS","parent_id":"NCBITaxon:871007"}; line 7139: {"taxon_id":"NCBITaxon:56636","label":"Aeropyrum pernix","rank":"SPECIES","parent_id":"NCBITaxon:56635","genetic_code":"11","exact_synonyms":"","related_synonyms":"Aeropyrum pernix Sako et al. 1996","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb&#124;bacdive&#124;lpsn&#124;mediadive&#124;gold&#124;madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"}; line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"}; line 36612: {"taxon_id":"NCBITaxon:183924","label":"Thermoprotei","rank":"CLASS","parent_id":"NCBITaxon:28889"}; line 184681: {"taxon_id":"NCBITaxon:871006","label":"Acidilobales","rank":"ORDER","parent_id":"NCBITaxon:183924"}; line 184682: {"taxon_id":"NCBITaxon:871007","label":"Acidilobaceae","rank":"FAMILY","parent_id":"NCBITaxon:871006"}; line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"} | supports | Inspected the target and each carried ancestor, rank, parent, genetic code and source name classes. |
| scope-row | curation/seed_scope.tsv; line 5718: {"identifier":"NCBITaxon:56636","added":"2026-09-12","reason":"attested rule: Aeropyrum pernix, 7 sources incl. NCBI"} | supports | Exact target is included in the declared seed scope. |
| path-row | data/taxa/PATHS.tsv; line 542412: {"identifier":"NCBITaxon:56636","slug":"aeropyrum_pernix"} | supports | Indexed path resolves to this exact NCBI taxon. |
| ncbi-live | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1872114,3402690,1293648,3697131,439481,229980,1198449,56636,272557,1872399; TaxaSet/Taxon[TaxId='56636']; ten-target captured response | supports | Inspected the official response for this exact taxon: scientific name, rank, parent, source name classes, lineage and genetic code. Current authority and pinned September inventory remain distinct observations. |
| lpsn-inventory | data/raw/lpsn_names.tsv; line 15094: {"lpsn_id":"lpsn:772925","name":"Aeropyrum pernix","rank":"SPECIES","authority":"Sako et al. 1996","url":"https://lpsn.dsmz.de/species/aeropyrum-pernix","deprecated":"0","status":"legitimate=True; validly published under the ICNP; correct name","validly_published":"1","legitimate":"1","is_correct_name":"1","parent_lpsn_id":"lpsn:516966","ncbitaxon_ids":"NCBITaxon:56636","gtdb_ids":"GTDB:s__Aeropyrum_pernix","type_strain_ids":"kgmicrobe.strain:ATCC-700893&#124;kgmicrobe.strain:DSM-11879&#124;kgmicrobe.strain:JCM-9820&#124;kgmicrobe.strain:NBRC-100138","synonym_of":"","synonyms":"","publications":"PMID:8863437&#124;doi:10.1099/00207713-46-4-1070&#124;doi:10.1099/00207713-47-1-243","sequence_accessions":"INSDC:AB008745"} | supports | Inspected exact mapped and linked LPSN names; bounded inventory absence does not establish worldwide nomenclatural absence. |
| gtdb-mappings | data/raw/gtdb_mappings.tsv; line 210667: {"gtdb_id":"GTDB:s__Aeropyrum_pernix","gtdb_label":"s__Aeropyrum_pernix","gtdb_parent":"GTDB:g__Aeropyrum","ncbitaxon_id":"NCBITaxon:272557","predicate":"skos:closeMatch","genome_count":"2"}; line 296799: {"gtdb_id":"GTDB:s__Aeropyrum_pernix","gtdb_label":"s__Aeropyrum_pernix","gtdb_parent":"GTDB:g__Aeropyrum","ncbitaxon_id":"NCBITaxon:56636","predicate":"skos:closeMatch","genome_count":"2"} | supports | Inspected direct mappings and selected clusters' reverse mappings, retaining each source predicate and taxon boundary. |
| gtdb-species | data/raw/gtdb_species.tsv; line 5678: {"gtdb_id":"GTDB:s__Aeropyrum_pernix","label":"s__Aeropyrum_pernix","parent":"GTDB:g__Aeropyrum","genome_count":"2"} | supports | Inspected source species identifiers, labels, parent clusters and genome counts. |
| bacdive-inventory | data/raw/bacdive_strains.tsv; line 4091: {"strain_id":"kgmicrobe.strain:bacdive_4195","bacdive_id":"4195","designation":"K1","taxon_ids":"NCBITaxon:56636","lpsn_ids":"lpsn:772925","culture_collection_ids":"kgmicrobe.strain:ATCC-700893&#124;kgmicrobe.strain:DSM-11879&#124;kgmicrobe.strain:JCM-9820&#124;kgmicrobe.strain:NBRC-100138","medium_count":"0"} | supports | Complete inventory selection covers the exact target and descendants from the complete NCBI parent graph; its imported strain population was compared with the complete YAML. |
| culture-inventory | data/raw/culture_collection_strains.tsv; line 7036: {"strain_id":"kgmicrobe.strain:ATCC-700893","taxon_ids":"NCBITaxon:56636"}; line 64871: {"strain_id":"kgmicrobe.strain:DSM-11879","taxon_ids":"NCBITaxon:56636"}; line 112866: {"strain_id":"kgmicrobe.strain:JCM-9820","taxon_ids":"NCBITaxon:56636"}; line 132216: {"strain_id":"kgmicrobe.strain:NBRC-100138","taxon_ids":"NCBITaxon:56636"} | supports | Inspected exact culture-inventory associations; an isolate name or genome does not create an inferred deposit. |
| gold-organisms | data/raw/gold_organisms.tsv; line 39006: {"taxon_id":"NCBITaxon:56636","organism_count":"3"} | supports | Inspected the exact GOLD organism count row or bounded absence, without converting counts to phenotypes. |
| mediadive-taxa | data/raw/mediadive_taxa.tsv; line 11590: {"taxon_id":"NCBITaxon:56636","medium_count":"2","media_ids":"mediadive.medium:514&#124;mediadive.medium:J224"} | supports | Inspected the exact MediaDive medium count row or bounded absence, without converting counts to phenotypes. |
| madin-taxa | data/raw/madin_taxa.tsv; line 27086: {"taxon_id":"NCBITaxon:56636","assertion_count":"6"} | supports | Inspected the exact Madin trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| bactotraits-taxa | data/raw/bactotraits_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact BactoTraits trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| mapping-policy | docs/HARMONIZATION.md; Mapping predicates; Which strains belong to a record | supports | Policy permits one-to-one species closeMatch normalization and LPSN-linked species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage unchanged. |
| equivalence-contract | src/taxonmech/schema/taxonmech.yaml; TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439 | supports | TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes under the source taxon. |
| seed-owner | src/taxonmech/seed.py; GTDB mapping construction lines 440–472; LPSN/type-strain and source-attestation construction | supports | Inspected mapping ranking, qualified predicates, fixed broadMatch wording, synonym/xref construction, primary cluster counts and same-taxon type-strain derivation. |
| manifest | data/raw/MANIFEST.yaml; kg_microbe_source, inputs, extracted_at | supports | Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd, upstream input hashes and extraction time 2026-09-13T17:50:44Z. |
| overlay-manifests | data/atb/MANIFEST.yaml; extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml | supports | Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z, matching the sole seed event. StrainInfo manifest is independently captured in source.inputs. |
| genome-catalog-1 | data/catalog/gtdb_genomes-0017.jsonl.gz; line 43686: {"accession":"RS_GCF_004323575.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Aeropyrum;s__Aeropyrum pernix","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM432357v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMD00074121","ncbi_contig_count":"148","ncbi_contig_n50":"27581","ncbi_country":"Japan:Kagoshima; Ibusuki; Yamagawa Beach","ncbi_date":"2019-01-18","ncbi_genbank_assembly_accession":"GCA_004323575.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"sediment","ncbi_lat_lon":"31.1058 N 130.3659 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Aeropyrum pernix","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"10","ncbi_scaffold_count":"144","ncbi_scaffold_l50":"17","ncbi_scaffold_n50":"27581","ncbi_scaffold_n75":"15253","ncbi_scaffold_n90":"7108","ncbi_seq_rel_date":"2019-01-18","ncbi_spanned_gaps":"4","ncbi_species_taxid":"56636","ncbi_ssu_count":"5","ncbi_strain_identifiers":"YK1-12-2013","ncbi_submitter":"Laboratory of Marine Microbiology, Graduate School of Agriculture, Kyoto University","ncbi_taxid":"56636","ncbi_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei;o__Desulfurococcales;f__Desulfurococcaceae;g__Aeropyrum;s__Aeropyrum pernix","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Thermoproteota;c__Thermoprotei;o__Desulfurococcales;f__Desulfurococcaceae;g__Aeropyrum;s__Aeropyrum pernix","ncbi_total_gap_length":"56","ncbi_total_length":"1601052","ncbi_translation_table":"11","ncbi_trna_count":"45","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1600996","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"BDMD00000000.1"}; line 46966: {"accession":"RS_GCF_000011125.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Aeropyrum;s__Aeropyrum pernix","gtdb_type_species_of_genus":"t","ncbi_assembly_level":"Complete Genome","ncbi_assembly_name":"ASM1112v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMD00061092","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"none","ncbi_date":"2006-11-28","ncbi_genbank_assembly_accession":"GCA_000011125.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Aeropyrum pernix K1","ncbi_protein_count":"none","ncbi_refseq_category":"reference genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"1669696","ncbi_scaffold_n75":"1669696","ncbi_scaffold_n90":"1669696","ncbi_seq_rel_date":"2006-11-28","ncbi_spanned_gaps":"0","ncbi_species_taxid":"56636","ncbi_ssu_count":"1","ncbi_strain_identifiers":"K1","ncbi_submitter":"NITE","ncbi_taxid":"272557","ncbi_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei;o__Desulfurococcales;f__Desulfurococcaceae;g__Aeropyrum;s__Aeropyrum pernix","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Thermoproteota;c__Thermoprotei;o__Desulfurococcales;f__Desulfurococcaceae;g__Aeropyrum;s__Aeropyrum pernix;x__Aeropyrum pernix K1","ncbi_total_gap_length":"0","ncbi_total_length":"1669696","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"assembly from type material","ncbi_ungapped_length":"1669696","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"} | supports | Inspected primary membership and exact assembly/genome identifiers, retaining NCBI species/strain boundaries, source labels, accession versions, deposit fields and separate project/sample identities. No sequence equivalence or culture identity is inferred from names alone. |
| genome-catalog-2 | data/catalog/ncbi_genbank-0000.jsonl.gz; line 227: {"annotation_date":"2016-10-08","annotation_name":"Annotation submitted by NITE","annotation_provider":"NITE","asm_name":"ASM1112v1","asm_not_live_date":"na","asm_submitter":"NITE","assembly_accession":"GCA_000011125.1","assembly_level":"Complete Genome","assembly_type":"haploid","bioproject":"PRJNA211","biosample":"SAMD00061092","contig_count":"1","excluded_from_refseq":"na","ftp_path":"https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/011/125/GCA_000011125.1_ASM1112v1/","gbrs_paired_asm":"GCF_000011125.1","gc_percent":"56.500000","genome_rep":"Full","genome_size":"1669696","genome_size_ungapped":"1669696","group":"archaea","infraspecific_name":"strain=K1","isolate":"na","non_coding_gene_count":"52","organism_name":"Aeropyrum pernix K1","paired_asm_comp":"identical","protein_coding_gene_count":"1700","pubmed_id":"10382966;16455681;16769697","refseq_category":"reference genome","relation_to_type_material":"assembly from type material","release_type":"Major","replicon_count":"1","scaffold_count":"1","seq_rel_date":"2006-10-11","species_taxid":"56636","taxid":"272557","total_gene_count":"1752","version_status":"latest","wgs_master":"na"} | supports | Inspected primary membership and exact assembly/genome identifiers, retaining NCBI species/strain boundaries, source labels, accession versions, deposit fields and separate project/sample identities. No sequence equivalence or culture identity is inferred from names alone. |
| genome-catalog-3 | data/bvbrc/bvbrc-0015.jsonl.gz; line 17056: {"assembly_accession":"GCA_000011125.1","bioproject_accession":"PRJNA211","biosample_accession":"-","date_modified":"2015-03-16T03:17:09.594Z","genbank_accessions":"BA000002.3","genome_id":"272557.25","genome_name":"Aeropyrum pernix K1","genome_status":"Complete","public":true,"reference_genome":"Representative","refseq_accessions":"NC_000854.2","strain":"K1","superkingdom":"Archaea","taxon_id":272557,"taxon_lineage_ids":["131567","2157","1783275","28889","183924","114380","2272","56635","56636","272557"],"taxon_lineage_names":["cellular organisms","Archaea","Thermoproteati","Thermoproteota","Thermoprotei","Desulfurococcales","Desulfurococcaceae","Aeropyrum","Aeropyrum pernix","Aeropyrum pernix K1"]}; line 17057: {"bioproject_accession":"PRJNA224116","biosample_accession":"SAMD00061092","culture_collection":"NBRC:100138","date_modified":"2026-02-03T15:48:59.329Z","genbank_accessions":"NC_000854","genome_id":"272557.33","genome_name":"Aeropyrum pernix K1","genome_status":"WGS","public":true,"strain":"K1","superkingdom":"Archaea","taxon_id":272557,"taxon_lineage_ids":["131567","2157","1783275","28889","183924","114380","2272","56635","56636","272557"],"taxon_lineage_names":["cellular organisms","Archaea","Thermoproteati","Thermoproteota","Thermoprotei","Desulfurococcales","Desulfurococcaceae","Aeropyrum","Aeropyrum pernix","Aeropyrum pernix K1"]} | supports | Inspected primary membership and exact assembly/genome identifiers, retaining NCBI species/strain boundaries, source labels, accession versions, deposit fields and separate project/sample identities. No sequence equivalence or culture identity is inferred from names alone. |
| gtdb-full-scan | data/catalog/MANIFEST.json; {"paths":["data/catalog/gtdb_genomes-0000.jsonl.gz","data/catalog/gtdb_genomes-0001.jsonl.gz","data/catalog/gtdb_genomes-0002.jsonl.gz","data/catalog/gtdb_genomes-0003.jsonl.gz","data/catalog/gtdb_genomes-0004.jsonl.gz","data/catalog/gtdb_genomes-0005.jsonl.gz","data/catalog/gtdb_genomes-0006.jsonl.gz","data/catalog/gtdb_genomes-0007.jsonl.gz","data/catalog/gtdb_genomes-0008.jsonl.gz","data/catalog/gtdb_genomes-0009.jsonl.gz","data/catalog/gtdb_genomes-0010.jsonl.gz","data/catalog/gtdb_genomes-0011.jsonl.gz","data/catalog/gtdb_genomes-0012.jsonl.gz","data/catalog/gtdb_genomes-0013.jsonl.gz","data/catalog/gtdb_genomes-0014.jsonl.gz","data/catalog/gtdb_genomes-0015.jsonl.gz","data/catalog/gtdb_genomes-0016.jsonl.gz","data/catalog/gtdb_genomes-0017.jsonl.gz","data/catalog/gtdb_genomes-0018.jsonl.gz"],"clusters":[{"id":"GTDB:s__Aeropyrum_pernix","count":2,"ncbi_taxids":{"56636":1,"272557":1},"other_taxa_note_supported":true}]} | supports | All nineteen GTDB shards were hashed and searched with exact terminal species tokens. Source counts and taxon distributions were inspected; a cluster is not equated with an individual strain. |
| strain-table-1 | data/raw/strain_assemblies.tsv; line 125234: {"strain_id":"kgmicrobe.strain:bacdive_4195","assembly_id":"ncbi.assembly:GCA_000011125","source":"BACDIVE","source_id":"bacdive:4195","source_reference_id":"66792","assembly_level":"complete","assembly_name":"ASM1112v1 assembly for Aeropyrum pernix K1","taxon_id":"NCBITaxon:272557","source_field":"Sequence information.Genome sequences.INSDC accession","matched_strain_id":"","source_strain_identifiers":"","source_strain_field":"","source_organism_id":"","source_project_id":""}; line 125235: {"strain_id":"kgmicrobe.strain:bacdive_4195","assembly_id":"ncbi.assembly:GCA_000011125.1","source":"GOLD","source_id":"gold:Ga0039428","source_reference_id":"","assembly_level":"","assembly_name":"Aeropyrum pernix K1","taxon_id":"NCBITaxon:272557","source_field":"AP GENBANK.assemblyAccession","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0000767"} | supports | Compared the complete imported assertion multiset, retaining multiplicity, literal source fields, versions and deposit scope. |
| strain-table-2 | data/raw/strain_genome_records.tsv; line 100637: {"strain_id":"kgmicrobe.strain:bacdive_4195","genome_id":"img.taxon:2923402010","source_database":"img","source":"BACDIVE","source_id":"bacdive:4195","source_reference_id":"66792","assembly_level":"complete","genome_name":"ASM1112v1 assembly for Aeropyrum pernix K1","taxon_id":"NCBITaxon:272557","source_field":"Sequence information.Genome sequences.IMG accession","matched_strain_id":"","source_strain_identifiers":"","source_strain_field":"","source_organism_id":"","source_project_id":""}; line 100638: {"strain_id":"kgmicrobe.strain:bacdive_4195","genome_id":"img.taxon:2923402010","source_database":"img","source":"GOLD","source_id":"gold:Ga0039428","source_reference_id":"","assembly_level":"","genome_name":"Aeropyrum pernix K1","taxon_id":"NCBITaxon:272557","source_field":"AP IMG TAXON ID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0000767"}; line 100639: {"strain_id":"kgmicrobe.strain:bacdive_4195","genome_id":"patric:272557.25","source_database":"patric","source":"BACDIVE","source_id":"bacdive:4195","source_reference_id":"66792","assembly_level":"complete","genome_name":"ASM1112v1 assembly for Aeropyrum pernix K1","taxon_id":"NCBITaxon:272557","source_field":"Sequence information.Genome sequences.BV-BRC accession","matched_strain_id":"","source_strain_identifiers":"","source_strain_field":"","source_organism_id":"","source_project_id":""}; line 100640: {"strain_id":"kgmicrobe.strain:bacdive_4195","genome_id":"patric:272557.33","source_database":"patric","source":"BV_BRC","source_id":"patric:272557.33","source_reference_id":"","assembly_level":"","genome_name":"Aeropyrum pernix K1","taxon_id":"NCBITaxon:272557","source_field":"genome_id","matched_strain_id":"kgmicrobe.strain:NBRC-100138","source_strain_identifiers":"NBRC:100138","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""} | supports | Compared the complete imported assertion multiset, retaining multiplicity, literal source fields, versions and deposit scope. |
| strain-table-3 | data/raw/strain_related_records.tsv; line 361165: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"bioproject:PRJNA211","record_type":"BIOPROJECT","source":"GOLD","source_id":"gold:Gp0000767","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI BIOPROJECT ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0000767"}; line 361166: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"bioproject:PRJNA224116","record_type":"BIOPROJECT","source":"BV_BRC","source_id":"patric:272557.33","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"bioproject_accession","matched_strain_id":"kgmicrobe.strain:NBRC-100138","source_strain_identifiers":"NBRC:100138","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""}; line 361167: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"bioproject:PRJNA263076","record_type":"BIOPROJECT","source":"GOLD","source_id":"gold:Gp0102910","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI BIOPROJECT ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0102910"}; line 361168: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"bioproject:PRJNA425658","record_type":"BIOPROJECT","source":"GOLD","source_id":"gold:Gp0225950","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI BIOPROJECT ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0225950"}; line 361169: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"bioproject:PRJNA425659","record_type":"BIOPROJECT","source":"GOLD","source_id":"gold:Gp0225951","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI BIOPROJECT ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0225951"}; line 361170: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"biosample:SAMD00061092","record_type":"BIOSAMPLE","source":"BV_BRC","source_id":"patric:272557.33","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"biosample_accession","matched_strain_id":"kgmicrobe.strain:NBRC-100138","source_strain_identifiers":"NBRC:100138","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""}; line 361171: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"biosample:SAMD00061092","record_type":"BIOSAMPLE","source":"GOLD","source_id":"gold:Gp0000767","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI BIOSAMPLE ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0000767"}; line 361172: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"biosample:SAMN03097722","record_type":"BIOSAMPLE","source":"GOLD","source_id":"gold:Gp0102910","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI BIOSAMPLE ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0102910"}; line 361173: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"biosample:SAMN08221418","record_type":"BIOSAMPLE","source":"GOLD","source_id":"gold:Gp0225951","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI BIOSAMPLE ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0225951"}; line 361174: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"biosample:SAMN08221419","record_type":"BIOSAMPLE","source":"GOLD","source_id":"gold:Gp0225950","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI BIOSAMPLE ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0225950"}; line 361175: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Ga0039428","record_type":"GOLD_ANALYSIS","source":"GOLD","source_id":"gold:Ga0039428","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"Aeropyrum pernix K1","source_field":"AP GOLD ID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0000767"}; line 361176: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Go0000767","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0000767","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"Aeropyrum pernix K1","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":""}; line 361177: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Go0624942","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0624942","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"Aeropyrum pernix JCM 9820","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:JCM-9820","source_strain_identifiers":"JCM 9820","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0624942","source_project_id":""}; line 361178: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Go0624942","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0624942","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"Aeropyrum pernix JCM 9820","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:JCM-9820","source_strain_identifiers":"JCM 9820","source_strain_field":"ORGANISM STRAIN","source_organism_id":"gold:Go0624942","source_project_id":""}; line 361179: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Go0624943","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0624943","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"Aeropyrum pernix DSM 11879","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:DSM-11879","source_strain_identifiers":"DSM 11879","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0624943","source_project_id":""}; line 361180: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Go0624943","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0624943","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"Aeropyrum pernix DSM 11879","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:DSM-11879","source_strain_identifiers":"DSM 11879","source_strain_field":"ORGANISM STRAIN","source_organism_id":"gold:Go0624943","source_project_id":""}; line 361181: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Gp0000767","record_type":"GOLD_PROJECT","source":"GOLD","source_id":"gold:Gp0000767","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"Aeropyrum pernix K1","source_field":"PROJECT GOLD ID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0000767"}; line 361182: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Gp0102910","record_type":"GOLD_PROJECT","source":"GOLD","source_id":"gold:Gp0102910","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"Aeropyrum pernix K1","source_field":"PROJECT GOLD ID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0102910"}; line 361183: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Gp0225950","record_type":"GOLD_PROJECT","source":"GOLD","source_id":"gold:Gp0225950","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"Aeropyrum pernix K1 transcriptome - Ape E","source_field":"PROJECT GOLD ID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0225950"}; line 361184: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Gp0225951","record_type":"GOLD_PROJECT","source":"GOLD","source_id":"gold:Gp0225951","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"Aeropyrum pernix K1 transcriptome - Ape S","source_field":"PROJECT GOLD ID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0225951"} | supports | Compared the complete imported assertion multiset, retaining multiplicity, literal source fields, versions and deposit scope. |
| strain-table-4 | data/straininfo/strain_links.tsv; line 88615: {"strain_id":"kgmicrobe.strain:bacdive_4195","straininfo_strain_id":"straininfo.strain:44195","straininfo_deposit_id":"straininfo.deposit:118657","matched_strain_id":"kgmicrobe.strain:ATCC-700893","deposit_designation":"ATCC 700893","strain_doi":"DOI:10.60712/SI-ID44195.3","strain_status":"published online","deposit_status":"available","source_bacdive_id":"bacdive:4195","taxon_id":"NCBITaxon:56636"}; line 88616: {"strain_id":"kgmicrobe.strain:bacdive_4195","straininfo_strain_id":"straininfo.strain:44195","straininfo_deposit_id":"straininfo.deposit:118658","matched_strain_id":"kgmicrobe.strain:JCM-9820","deposit_designation":"JCM 9820","strain_doi":"DOI:10.60712/SI-ID44195.3","strain_status":"published online","deposit_status":"available","source_bacdive_id":"bacdive:4195","taxon_id":"NCBITaxon:56636"}; line 88617: {"strain_id":"kgmicrobe.strain:bacdive_4195","straininfo_strain_id":"straininfo.strain:44195","straininfo_deposit_id":"straininfo.deposit:118659","matched_strain_id":"kgmicrobe.strain:DSM-11879","deposit_designation":"DSM 11879","strain_doi":"DOI:10.60712/SI-ID44195.3","strain_status":"published online","deposit_status":"available","source_bacdive_id":"bacdive:4195","taxon_id":"NCBITaxon:56636"}; line 88618: {"strain_id":"kgmicrobe.strain:bacdive_4195","straininfo_strain_id":"straininfo.strain:44195","straininfo_deposit_id":"straininfo.deposit:335948","matched_strain_id":"kgmicrobe.strain:NBRC-100138","deposit_designation":"NBRC 100138","strain_doi":"DOI:10.60712/SI-ID44195.3","strain_status":"published online","deposit_status":"available","source_bacdive_id":"bacdive:4195","taxon_id":"NCBITaxon:56636"} | supports | Compared the complete imported assertion multiset, retaining multiplicity, literal source fields, versions and deposit scope. |
| strain-table-5 | data/straininfo/assemblies.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Compared the complete imported assertion multiset, retaining multiplicity, literal source fields, versions and deposit scope. |
| strain-table-6 | data/straininfo/related_records.tsv.gz; line 214082: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.deposit:118657","record_type":"STRAININFO_DEPOSIT","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"ATCC 700893","source_field":"deposits.siDP","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"ATCC 700893\",\"deposit_id\":\"straininfo.deposit:118657\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published online\"}"}; line 214083: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.deposit:118658","record_type":"STRAININFO_DEPOSIT","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"JCM 9820","source_field":"deposits.siDP","matched_strain_id":"kgmicrobe.strain:JCM-9820","source_strain_identifiers":"JCM 9820","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"JCM 9820\",\"deposit_id\":\"straininfo.deposit:118658\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published online\"}"}; line 214084: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.deposit:118659","record_type":"STRAININFO_DEPOSIT","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"DSM 11879","source_field":"deposits.siDP","matched_strain_id":"kgmicrobe.strain:DSM-11879","source_strain_identifiers":"DSM 11879","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"DSM 11879\",\"deposit_id\":\"straininfo.deposit:118659\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published online\"}"}; line 214085: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.deposit:335948","record_type":"STRAININFO_DEPOSIT","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"NBRC 100138","source_field":"deposits.siDP","matched_strain_id":"kgmicrobe.strain:NBRC-100138","source_strain_identifiers":"NBRC 100138","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"NBRC 100138\",\"deposit_id\":\"straininfo.deposit:335948\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published online\"}"}; line 214086: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.strain:44195","record_type":"STRAININFO_STRAIN","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"ATCC 700893","source_field":"strain.siID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC 700893","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"ATCC 700893\",\"deposit_id\":\"straininfo.deposit:118657\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published online\"}"}; line 214087: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.strain:44195","record_type":"STRAININFO_STRAIN","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"DSM 11879","source_field":"strain.siID","matched_strain_id":"kgmicrobe.strain:DSM-11879","source_strain_identifiers":"DSM 11879","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"DSM 11879\",\"deposit_id\":\"straininfo.deposit:118659\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published online\"}"}; line 214088: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.strain:44195","record_type":"STRAININFO_STRAIN","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"JCM 9820","source_field":"strain.siID","matched_strain_id":"kgmicrobe.strain:JCM-9820","source_strain_identifiers":"JCM 9820","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"JCM 9820\",\"deposit_id\":\"straininfo.deposit:118658\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published online\"}"}; line 214089: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.strain:44195","record_type":"STRAININFO_STRAIN","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"NBRC 100138","source_field":"strain.siID","matched_strain_id":"kgmicrobe.strain:NBRC-100138","source_strain_identifiers":"NBRC 100138","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"NBRC 100138\",\"deposit_id\":\"straininfo.deposit:335948\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published online\"}"} | supports | Compared the complete imported assertion multiset, retaining multiplicity, literal source fields, versions and deposit scope. |
| strain-table-7 | data/atb/strain_links.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Compared the complete imported assertion multiset, retaining multiplicity, literal source fields, versions and deposit scope. |
| strain-primary-1 | data/bacdive/records.jsonl.gz; line 4090: {"General":{"@ref":4521,"BacDive-ID":4195,"NCBI tax id":{"Matching level":"species","NCBI tax id":56636},"doi":"10.13145/bacdive4195.20260601.11"},"Literature":{"@ref":4521,"culture collection no.":"DSM 11879, JCM 9820, ATCC 700893, NBRC 100138","straininfo link":{"@ref":126262,"straininfo":44195}},"Name and taxonomic classification":{"@ref":4521,"LPSN":{"@ref":20215,"class":"Thermoprotei","description":"domain/archaea","domain":"Archaea","family":"Acidilobaceae","full scientific name":"&lt;I&gt;Aeropyrum&lt;/I&gt; &lt;I&gt;pernix&lt;/I&gt; Sako et al. 1996","genus":"Aeropyrum","keyword":"phylum/thermoproteota","order":"Acidilobales","phylum":"Thermoproteota","species":"Aeropyrum pernix"},"class":"Thermoprotei","domain":"Archaea","family":"Desulfurococcaceae","full scientific name":"Aeropyrum pernix Sako et al. 1996","genus":"Aeropyrum","order":"Desulfurococcales","phylum":"Crenarchaeota","species":"Aeropyrum pernix","strain designation":"K1","type strain":"yes"},"Sequence information":{"16S sequences":[{"@ref":4521,"NCBI tax ID":56636,"accession":"D83259","database":"nuccore","description":"Aeropyrum pernix gene for 16S rRNA, partial sequence","length":1444},{"@ref":67770,"NCBI tax ID":56636,"accession":"AB008745","database":"nuccore","description":"Aeropyrum pernix genes for 16S rRNA, 23S rRNA and rRNA intron-encoded homing endonuclease, complete cds","length":10777}],"Genome sequences":{"@ref":66792,"BV-BRC accession":"272557.25","IMG accession":"2923402010","INSDC accession":"GCA_000011125","NCBI tax ID":272557,"assembly level":"complete","description":"ASM1112v1 assembly for Aeropyrum pernix K1","score":96.94}}} | supports | Inspected complete selected BacDive, StrainInfo and GOLD primary objects. Explicit deposits and project/analysis chains support only their narrow claims. Historical aggregates are not recounted by these newer objects. |
| strain-primary-2 | data/straininfo/records.jsonl.gz; line 32365: {"deposits":[{"cultureCollection":{"ccID":4,"code":"ATCC","deprecated":false,"name":"American Type Culture Collection"},"designation":"ATCC 700893","lastUpdate":"2005-10-22","siDP":118657,"status":"available","taxon":{"lpsn":772925,"name":"Aeropyrum pernix","ncbi":56636},"typeStrain":true},{"cultureCollection":{"ccID":14,"code":"JCM","deprecated":false,"name":"Japan Collection of Microorganisms"},"designation":"JCM 9820","lastUpdate":"2005-10-22","siDP":118658,"status":"available","taxon":{"lpsn":772925,"name":"Aeropyrum pernix","ncbi":56636},"typeStrain":true},{"cultureCollection":{"ccID":1,"code":"DSMZ","deprecated":false,"name":"DSMZ-German Collection of Microorganisms and Cell Cultures"},"designation":"DSM 11879","lastUpdate":"2024-12-03","siDP":118659,"status":"available","taxon":{"lpsn":772925,"name":"Aeropyrum pernix","ncbi":56636},"typeStrain":true},{"cultureCollection":{"ccID":12,"code":"NBRC","deprecated":false,"name":"Biological Resource Center, NITE"},"designation":"NBRC 100138","lastUpdate":"2005-10-22","siDP":335948,"status":"available","taxon":{"lpsn":772925,"name":"Aeropyrum pernix","ncbi":56636},"typeStrain":true}],"strain":{"archive":[{"date":"2024-05-31","doi":"10.60712/SI-ID44195.1","title":"StrainInfo SI-ID 44195.1"},{"date":"2024-06-05","doi":"10.60712/SI-ID44195.2","title":"StrainInfo SI-ID 44195.2"},{"date":"2025-02-25","doi":"10.60712/SI-ID44195.3","title":"StrainInfo SI-ID 44195.3"}],"bdID":4195,"doi":"10.60712/SI-ID44195.3","relation":{"deposit":[{"ccID":4,"designation":"ATCC 700893","erroneous":false,"origin":118658,"siDP":118657},{"ccID":14,"designation":"JCM 9820","erroneous":false,"siDP":118658},{"ccID":1,"designation":"DSM 11879","erroneous":false,"origin":118658,"siDP":118659},{"ccID":12,"designation":"NBRC 100138","erroneous":false,"origin":118658,"siDP":335948}],"designation":["Nomura K1"]},"siID":44195,"status":"published online","taxon":{"lpsn":772925,"name":"Aeropyrum pernix","ncbi":56636}}} | supports | Inspected complete selected BacDive, StrainInfo and GOLD primary objects. Explicit deposits and project/analysis chains support only their narrow claims. Historical aggregates are not recounted by these newer objects. |
| strain-primary-3 | data/gold/organisms.jsonl.gz; line 727: {"ORGANISM CULTURE COLLECTION ID":"ATCC 700893","ORGANISM GOLD ID":"Go0000767","ORGANISM NAME":"Aeropyrum pernix K1","ORGANISM NCBI TAX ID":"272557","ORGANISM STRAIN":"K1"}; line 455549: {"ORGANISM CULTURE COLLECTION ID":"JCM 9820","ORGANISM GOLD ID":"Go0624942","ORGANISM NAME":"Aeropyrum pernix JCM 9820","ORGANISM NCBI TAX ID":"56636","ORGANISM STRAIN":"JCM 9820"}; line 455550: {"ORGANISM CULTURE COLLECTION ID":"DSM 11879","ORGANISM GOLD ID":"Go0624943","ORGANISM NAME":"Aeropyrum pernix DSM 11879","ORGANISM NCBI TAX ID":"56636","ORGANISM STRAIN":"DSM 11879"} | supports | Inspected complete selected BacDive, StrainInfo and GOLD primary objects. Explicit deposits and project/analysis chains support only their narrow claims. Historical aggregates are not recounted by these newer objects. |
| strain-primary-4 | data/gold/projects.jsonl.gz; line 744: {"NCBI BIOPROJECT ACCESSION":"PRJNA211","NCBI BIOSAMPLE ACCESSION":"SAMD00061092","ORGANISM GOLD ID":"Go0000767","PROJECT GOLD ID":"Gp0000767","PROJECT NAME":"Aeropyrum pernix K1"}; line 59212: {"NCBI BIOPROJECT ACCESSION":"PRJNA263076","NCBI BIOSAMPLE ACCESSION":"SAMN03097722","ORGANISM GOLD ID":"Go0000767","PROJECT GOLD ID":"Gp0102910","PROJECT NAME":"Aeropyrum pernix K1"}; line 150393: {"NCBI BIOPROJECT ACCESSION":"PRJNA425658","NCBI BIOSAMPLE ACCESSION":"SAMN08221419","ORGANISM GOLD ID":"Go0000767","PROJECT GOLD ID":"Gp0225950","PROJECT NAME":"Aeropyrum pernix K1 transcriptome - Ape E"}; line 150394: {"NCBI BIOPROJECT ACCESSION":"PRJNA425659","NCBI BIOSAMPLE ACCESSION":"SAMN08221418","ORGANISM GOLD ID":"Go0000767","PROJECT GOLD ID":"Gp0225951","PROJECT NAME":"Aeropyrum pernix K1 transcriptome - Ape S"} | supports | Inspected complete selected BacDive, StrainInfo and GOLD primary objects. Explicit deposits and project/analysis chains support only their narrow claims. Historical aggregates are not recounted by these newer objects. |
| strain-primary-5 | data/gold/analyses.jsonl.gz; line 25149: {"AP GENBANK":"[{\"genbankId\":\"BA000002\",\"assemblyAccession\":\"GCA_000011125.1\"}]","AP GOLD ID":"Ga0039428","AP IMG TAXON ID":"2923402010","AP NAME":"Aeropyrum pernix K1","AP ORGANISM GOLD ID":"","AP PROJECT GOLD IDS":"Gp0000767","AP TYPE":"Genome Analysis (Isolate)"} | supports | Inspected complete selected BacDive, StrainInfo and GOLD primary objects. Explicit deposits and project/analysis chains support only their narrow claims. Historical aggregates are not recounted by these newer objects. |
| gold-project-discovery | data/gold/projects.jsonl.gz; [{"line":744,"row":{"NCBI BIOPROJECT ACCESSION":"PRJNA211","NCBI BIOSAMPLE ACCESSION":"SAMD00061092","ORGANISM GOLD ID":"Go0000767","PROJECT GOLD ID":"Gp0000767","PROJECT NAME":"Aeropyrum pernix K1"}},{"line":59212,"row":{"NCBI BIOPROJECT ACCESSION":"PRJNA263076","NCBI BIOSAMPLE ACCESSION":"SAMN03097722","ORGANISM GOLD ID":"Go0000767","PROJECT GOLD ID":"Gp0102910","PROJECT NAME":"Aeropyrum pernix K1"}},{"line":150393,"row":{"NCBI BIOPROJECT ACCESSION":"PRJNA425658","NCBI BIOSAMPLE ACCESSION":"SAMN08221419","ORGANISM GOLD ID":"Go0000767","PROJECT GOLD ID":"Gp0225950","PROJECT NAME":"Aeropyrum pernix K1 transcriptome - Ape E"}},{"line":150394,"row":{"NCBI BIOPROJECT ACCESSION":"PRJNA425659","NCBI BIOSAMPLE ACCESSION":"SAMN08221418","ORGANISM GOLD ID":"Go0000767","PROJECT GOLD ID":"Gp0225951","PROJECT NAME":"Aeropyrum pernix K1 transcriptome - Ape S"}}] | supports | Full exact organism-field search verifies the available project chains and bounded absences for the explicitly selected organism IDs; no project or analysis is inferred from an empty filtered artifact. |
| cafi-registry | src/taxonmech/data/cafi_acronyms.json; {"accessed_at":"2026-10-20T04:02:21.239529+00:00","registry_rows":{"1":{"acr":"DSM","acr_synonym":["DSMZ"],"active":true,"catalogue":["https://www.dsmz.de/collection/catalogue/details/culture/{acr}-{id}"],"code":"DSMZ","country":"DE","gbif":"883f3d24-35e9-462d-b7a3-13c2b9b7260e","homepage":"https://www.dsmz.de/","name":"DSMZ-German Collection of Microorganisms and Cell Cultures","regex_ccno":"^DSM\\s*\\d+$","regex_id":{"full":"^\\d+$"},"ror":"02tyer376"},"4":{"acr":"ATCC","active":true,"catalogue":["https://www.atcc.org/products/{id}"],"code":"ATCC","country":"US","gbif":"25160e92-1a80-4226-9afb-b25691622ac6","homepage":"https://www.atcc.org/","name":"American Type Culture Collection","regex_ccno":"^ATCC\\s*((BAA&#124;TSD&#124;MYA&#124;SD&#124;VR&#124;PTA)-)?\\d+$","regex_id":{"core":"\\d+","full":"^((BAA&#124;TSD&#124;MYA&#124;SD&#124;VR&#124;PTA)-)?\\d+$","pre":"(BAA&#124;TSD&#124;MYA&#124;SD&#124;VR&#124;PTA)"},"ror":"03thhhv76"},"14":{"acr":"JCM","active":true,"catalogue":["https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?{acr}={id}"],"code":"JCM","country":"JP","gbif":"fce1f744-ca76-46bb-9428-d92cfebe39d4","homepage":"https://jcm.brc.riken.jp/en/","name":"Japan Collection of Microorganisms","regex_ccno":"^JCM\\s*\\d+$","regex_id":{"full":"^\\d+$"},"ror":"00s05em53"},"12":{"acr":"NBRC","acr_synonym":["NITE:NBRC"],"active":true,"catalogue":["https://www.nite.go.jp/nbrc/catalogue/NBRCCatalogueDetailServlet?ID=NBRC&amp;CAT={core0:8}"],"code":"NBRC","country":"JP","gbif":"abab42d0-0a95-4166-a0fc-6fe5cd9b66ff","homepage":"https://www.nite.go.jp/en/nbrc/","name":"Biological Resource Center","regex_ccno":"^NBRC\\s*\\d+$","regex_id":{"full":"^\\d+$"}}},"normalization":{"DSM 19572":"DSM-19572","ATCC BAA-758":"ATCC-BAA-758","DSM 16960":"DSM-16960","JCM 12091":"JCM-12091","ATCC 700893":"ATCC-700893","DSM 11879":"DSM-11879","JCM 9820":"JCM-9820","NBRC 100138":"NBRC-100138","T469":"","SY1":"","K1":""}} | supports | Explicit registered deposit keys pass the authority/accession rule. Bare T469, SY1 and K1 do not; genome association alone is not a deposit join. |
| lpsn-live | https://lpsn.dsmz.de/species/aeropyrum-pernix; Name, publication status, type deposits and accession | supports | LPSN772925 supports Sako et al.1996, valid ICNP publication and correct-name status, with type K1 and four deposits. Both DOIs resolve and PMID8863437 supports the original description and JCM9820 type designation. AB008745.2 resolves at taxon56636 with strainK1; its title describes rRNA and an intron-encoded homing endonuclease, not a new functional assertion in this review. |
| doi-original | https://api.crossref.org/works/10.1099/00207713-46-4-1070; message DOI,title,published | supports | Original description DOI resolves with matching publication identity. |
| doi-notification | https://api.crossref.org/works/10.1099/00207713-47-1-243; message DOI,title,published | supports | Separately cited notification DOI resolves to the expected list. |
| pubmed-original | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=15023940,8863437&amp;retmode=xml; PMID8863437 | supports | Publication identity and explicit type-strain statements inspected; no phenotype is inferred. |
| nucleotide-authority | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&amp;id=AB109559,AB245529,AB008745&amp;retmode=json; AB008745.2 taxon56636 strainK1 | supports | Accession metadata supports source name, strain and taxon context without silently upgrading unversioned assertions or inferring gene function. |
| adapter-page-1 | https://imodulondb.org/; Captured landing page; no resolved matching organism/dataset/component | context_only | Inspected bounded fallback source: legacy organism headings have no Aeropyrum; modern landing page does not establish complete dataset coverage. No absence of a biological function or transcriptomic effect is inferred. |
| adapter-page-2 | https://legacy.imodulondb.org/; Captured landing page; no resolved matching organism/dataset/component | context_only | Inspected bounded fallback source: legacy organism headings have no Aeropyrum; modern landing page does not establish complete dataset coverage. No absence of a biological function or transcriptomic effect is inferred. |
| adapter-resolution | kg-microbe-sources runner resolution; {"accessed_at":"2026-10-20T04:02:21.239865+00:00","console_runner":null,"bounded_project_search":{"/Users/marcin/Documents/VIMSS/ontology/Mechs/claw":{"exists":false},"/Users/marcin/Documents/VIMSS/ontology/Mechs/culturebotai-claw":{"exists":false},"/Users/marcin/Documents/VIMSS/ontology/Mechs/wizard-claw":{"exists":false}},"scope":"Installed PATH lookup and gitignore-independent checks of the three explicit candidate locations only; not a worldwide availability claim."} | partial | Installed runner absent and no runner resolved in explicitly checked candidate locations; optional expression context remains unavailable. |
| historical-edge-1 | data/raw/MANIFEST.yaml; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/mediadive/edges.tsv; expected=78ea275a59d4e2de09a9cf72652ec64454c6a111d2defa1ae0a44bac8a72e523; observed=4e933d1e2412fb1aad74e60719a6a64dfa34862ff0a6b84e93d78da5ce13dd8b | partial | Earlier actual check found configured source bytes differing from the manifest-pinned historical input; this is not a new or worldwide search. |
| historical-edge-2 | data/raw/MANIFEST.yaml; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/gold/edges.tsv; expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12; observed=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d | partial | Earlier actual check found configured source bytes differing from the manifest-pinned historical input; this is not a new or worldwide search. |
| historical-edge-3 | data/raw/MANIFEST.yaml; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv; expected=3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f; observed=c19bfc848e1b410548614c54a2b99e2c58452d58aeb61f972c99fcb3039a1d24 | partial | Earlier actual check found configured source bytes differing from the manifest-pinned historical input; this is not a new or worldwide search. |
| qc-setup-receipt | just qc; initial setup attempt, 2026-10-19T07:17:01Z through 2026-10-19T07:17:01Z | context_only | Initial actual invocation from /private/tmp/taxonmech-record-reviews-k0MubV/repo exited 1 because ruff was absent. Locked ruff 0.16.7 was installed only in that isolated environment before the complete retry. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| strict-receipt | just validate-strict data/taxa/archaea/aeropyrum_pernix.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0007/strict-08.tsv; This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0007/repo; started 2026-10-20T03:58:14Z, finished 2026-10-20T03:58:15Z, exit 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times.<br>Validating 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0003/src/taxonmech/schema/taxonmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0007/strict-08.tsv |
| history-receipt | just validate-history; All 17 standalone history records; the generated seed event was also inspected in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:01Z, finished 2026-10-19T07:17:03Z, exit 0. All 17 standalone history records; the generated seed event was also inspected in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>history links: 17 record(s), 0 invalid<br>No issues found<br>17 history record(s) valid against src/taxonmech/schema/history.yaml |
| corpus-receipt | just verify-corpus; All 625,960 generated taxon YAMLs, not a focused approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:18:23Z, finished 2026-10-19T07:24:12Z, exit 0. All 625,960 generated taxon YAMLs, not a focused approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>uv run python scripts/verify_corpus.py <br>expected 625960 records, found 625960 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ and curation/seed_scope.tsv |
| products-receipt | just validate-products; Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:01Z, finished 2026-10-19T07:55:11Z, exit 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml<br><br>id↔label correspondence summary:<br><br>✅ All id↔label pairs correspond. |
| qc-receipt | just qc; Repository-wide just qc, including native corpus-wide checks. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:41Z, finished 2026-10-19T08:07:39Z, exit 0. Repository-wide just qc, including native corpus-wide checks. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>1055 passed, 3 skipped, 5 deselected in 1634.00s (0:27:13)<br>Validating 625960 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml<br>  files scanned:      625960<br>expected 625960 records, found 625960 on disk<br>pages/ is current<br>Site publication: 530,864,122 bytes (budget 950,000,000)<br>625960 taxon records<br>  NCBITAXON        625960<br>All TaxonMech quality gates passed.<br>  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890 strains (not genome counts)<br>  Related STRAININFO_DEPOSIT: 107277 strain-record pairs, 106843 identifiers, 53890 strains (not genome counts)<br>  Related NUCLEOTIDE_SEQUENCE: 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)<br>LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809 records mapped, 324404579 genomes summed across record attestations (not deduplicated)<br>Causal graphs: 0 records (0 evidence-backed edges)<br><br>All TaxonMech quality gates passed. |

## Limits And Additional Notes

- The review is bounded to captured sources and versions. Names alone do not establish deposit identity, genome equivalence, phenotype or mechanism; source taxonomy disagreements are preserved.
- Original manifest-hash-matching historical aggregate edges were unavailable in the retained configured-path checks; pinned projection counts agree, but independent historical recounting remains unresolved.
- Optional iModulonDB adapter context unavailable in bounded runner checks. Legacy site and search fallback did not establish matching Aeropyrum coverage; the modern landing page does not prove exhaustive absence.
- Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base canonical recapture preserved all previously reviewed input hashes; original captures and actual transition receipts remain retained.
- Every new bundle still requires its own validate/save/check recipe; baseline native receipts do not claim these later steps have run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T041038Z-aeropyrum_pernix
kind: record
repository: CultureBotAI/TaxonMech
title: 'Record review: Aeropyrum pernix'
started_at: '2026-10-20T03:58:06Z'
finished_at: '2026-10-20T04:10:38Z'
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
summary: Aeropyrum pernix has supported exact NCBI identity and faithfully projected
  source assertions.
source:
  git_revision: 9b5a8fff5185b38dc5c77bb35235152c81ea7765
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
    sha256: 8ae749dbc22700080dcf5e1a0b7ed75710dee6a27f5c7f9e7c6790c26176e5c8
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
  - path: conf/sources.yaml
    sha256: 759ef444b1890559846fd4ab7818c8dbca74ab6bee2f6b9466a1aff6b5f4d8c8
    role: context
  - path: curation/seed_scope.tsv
    sha256: 5fdc0f7111b64e02439d95c6f2b51fcff1d2154c34b2d957422dd9b297e94d4b
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
  - path: data/catalog/PRIMARY.json
    sha256: 8ae7c5d329ebfccb98670f1b40d58932e400d1f3423e45135dc3926d412c17e5
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
    sha256: c950844feb0638ce04f7349784749dd1d728fe70bc80f7e2756d956d4ecea254
    role: context
  - path: data/taxa/archaea/aeropyrum_pernix.yaml
    sha256: 3d842c2e978630216733593e302600470fa015cbc8341ea1ec23f9876bd1e845
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
    sha256: d98d6944810090bf9c344ab218d82f8927d73eaad432322b94a876fe9e891334
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
    sha256: 6b5b065f4ae7aea022af736a22c0f63dc58a2425c7ee453259e567ab030f8257
    role: context
scope:
  description: Entire single generated record, including all source assertions and
    imported strains.
  selection: Original unreviewed path-order position 68; batch-0007 target 8. Excluded
    112 actual targets from validated main and local batch-0001/0002/0003/0004/0005/0006
    listings; full corpus enumeration includes ignored files.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - NCBITaxon:56636
targets:
- target_id: NCBITaxon:56636
  path: data/taxa/archaea/aeropyrum_pernix.yaml
  label: Aeropyrum pernix
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
  summary: NCBITaxon:56636 denotes Aeropyrum pernix, rank SPECIES, parent NCBITaxon:56635,
    genetic code11. All 9 carried ancestors, literal labels and ranks agree with pinned
    NCBI and current EFetch.
  target_ids:
  - NCBITaxon:56636
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
  summary: The one species-filed BacDive strain is retained even though some genome
    objects refer to child272557. Direct-species historical MediaDive2, GOLD3 and
    Madin6 units are not descendant sums. Source projects and samples remain narrow
    contextual links; optional expression-module coverage is not established.
  target_ids:
  - NCBITaxon:56636
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
  scope_note: Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs.
- check_id: gtdb-primary-counts
  name: Complete primary GTDB cluster membership
  status: passed
  required: true
  summary: Exact source cluster counts agree with carried mappings where present;
    LPSN-only species bridges remain distinct from direct GTDB attestations.
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - gtdb-full-scan
  - gtdb-species
  - gtdb-mappings
  - genome-catalog-1
  - genome-catalog-2
  - genome-catalog-3
  scope_note: Full nineteen-shard source search and exact primary identifiers.
- check_id: imodulondb-adapter
  name: Optional structured expression-module context
  status: unavailable
  required: false
  summary: No matching Aeropyrum dataset/component was established. Cbf5/accession
    and transcriptome-project names remain source descriptions, not inferred functions.
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - adapter-resolution
  - adapter-page-1
  - adapter-page-2
  - nucleotide-authority
  scope_note: Legacy rendered organism headings contain no Aeropyrum entry. Modern
    homepage is a JavaScript application and does not establish complete dataset coverage.
    Search queries for Aeropyrum/Cbf5/pernix did not resolve a matching dataset; search
    misses are not negative scientific evidence.
- check_id: strain-genome-evidence
  name: Complete strain and genome-source assertions
  status: passed
  required: true
  summary: 'BacDive4195 is explicitly filed at species56636, with K1 and ATCC700893/DSM11879/JCM9820/NBRC100138.
    Same-species LPSN deposits support the derived type flag. StrainInfo44195.3 supports
    four distinct deposits118657/118658/118659/335948 and no sequence list. GOLD Go0000767
    ATCC700893 links to four projects: Gp0000767, Gp0102910, Gp0225950 and Gp0225951.
    Only Gp0000767 is linked in the inspected analyses to Ga0039428/GCA_000011125.1/IMG2923402010;
    the two named transcriptome projects retain their own samples and are not treated
    as genome analyses. Full discovery finds no project for Go0624942 JCM or Go0624943
    DSM. BV272557.25 supplies the explicit BacDive-associated genome; BV272557.33
    explicitly matches NBRC:100138 and has no assembly_accession field, so the absent
    BV assembly assertion is supported. Bare K1 fails culture-key normalization. The2
    assembly,4 genome and28 related assertions exactly match the imported multiset.'
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - record
  - bacdive-inventory
  - culture-inventory
  - lpsn-inventory
  - strain-table-1
  - strain-table-2
  - strain-table-3
  - strain-table-4
  - strain-table-5
  - strain-table-6
  - strain-table-7
  - strain-primary-1
  - strain-primary-2
  - strain-primary-3
  - strain-primary-4
  - strain-primary-5
  - gold-project-discovery
  - cafi-registry
  - adapter-page-1
  - adapter-page-2
  - lpsn-live
  - doi-original
  - doi-notification
  - pubmed-original
  - nucleotide-authority
  - genome-catalog-1
  - genome-catalog-2
  - genome-catalog-3
  scope_note: Complete assertion multiset comparison plus inspected primary objects;
    distinct deposit, genome, project and analysis scopes preserved.
- check_id: historical-source-counts
  name: Original manifest-pinned aggregate edges
  status: unavailable
  required: true
  summary: Pinned inventory counts agree; independent historical recounting remains
    unavailable for gold, mediadive, madin_etal.
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - manifest
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
  - historical-edge-1
  - historical-edge-2
  - historical-edge-3
- check_id: qc-setup-attempt
  name: Initial quality-gate setup attempt
  status: failed
  required: false
  summary: 'Actual exit 1: missing ruff; superseded by the separately recorded successful
    full retry.'
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - qc-setup-receipt
  command: just qc
  exit_code: 1
  expected_exit_code: 0
  scope_note: Earlier shared-base environment setup attempt; not the final quality-gate
    result.
- check_id: strict
  name: Native strict record validation
  status: passed
  required: true
  summary: Actual terminal exit code 0. This exact generated YAML only; its captured
    bytes remain unchanged. Actual earlier per-target invocation; the receipt retains
    its original cwd and times.
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - strict-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0007/uv-cache
    just validate-strict data/taxa/archaea/aeropyrum_pernix.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0007/strict-08.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: This exact generated YAML only; its captured bytes remain unchanged.
    Actual earlier per-target invocation; the receipt retains its original cwd and
    times.
- check_id: history
  name: Repository history validation
  status: passed
  required: true
  summary: Actual terminal exit code 0. All 17 standalone history records; the generated
    seed event was also inspected in this target. Reused actual native validation
    on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded
    cwd and timestamps identify the original execution. These native corpus/source
    inputs are unchanged; only new review files differ. This receipt is not a new
    run on the batch branch and does not validate subsequently saved review bundles.
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - history-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/uv-cache
    just validate-history
  exit_code: 0
  expected_exit_code: 0
  scope_note: All 17 standalone history records; the generated seed event was also
    inspected in this target. Reused actual native validation on the unchanged shared
    base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps
    identify the original execution. These native corpus/source inputs are unchanged;
    only new review files differ. This receipt is not a new run on the batch branch
    and does not validate subsequently saved review bundles.
- check_id: corpus
  name: Full-corpus exact reproduction
  status: passed
  required: true
  summary: Actual terminal exit code 0. All 625,960 generated taxon YAMLs, not a focused
    approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765;
    the recorded cwd and timestamps identify the original execution. These native
    corpus/source inputs are unchanged; only new review files differ. This receipt
    is not a new run on the batch branch and does not validate subsequently saved
    review bundles.
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - corpus-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/uv-cache
    just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  scope_note: All 625,960 generated taxon YAMLs, not a focused approximation. Reused
    actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765;
    the recorded cwd and timestamps identify the original execution. These native
    corpus/source inputs are unchanged; only new review files differ. This receipt
    is not a new run on the batch branch and does not validate subsequently saved
    review bundles.
- check_id: products
  name: Native product ID/label gate
  status: passed
  required: true
  summary: Actual terminal exit code 0. Full configured corpus scan for curator-added
    graph nodes; this target contains no causal graph. Reused actual native validation
    on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded
    cwd and timestamps identify the original execution. These native corpus/source
    inputs are unchanged; only new review files differ. This receipt is not a new
    run on the batch branch and does not validate subsequently saved review bundles.
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - products-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/uv-cache
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: Full configured corpus scan for curator-added graph nodes; this target
    contains no causal graph. Reused actual native validation on the unchanged shared
    base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps
    identify the original execution. These native corpus/source inputs are unchanged;
    only new review files differ. This receipt is not a new run on the batch branch
    and does not validate subsequently saved review bundles.
- check_id: qc
  name: Authoritative complete quality gate
  status: passed
  required: true
  summary: Actual terminal exit code 0. Repository-wide just qc, including native
    corpus-wide checks. Reused actual native validation on the unchanged shared base
    9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify
    the original execution. These native corpus/source inputs are unchanged; only
    new review files differ. This receipt is not a new run on the batch branch and
    does not validate subsequently saved review bundles. Pytest reported 1055 passed,
    3 skipped and 5 deselected; the native QC recipe completed successfully.
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - qc-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/uv-cache
    just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: Repository-wide just qc, including native corpus-wide checks. Reused
    actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765;
    the recorded cwd and timestamps identify the original execution. These native
    corpus/source inputs are unchanged; only new review files differ. This receipt
    is not a new run on the batch branch and does not validate subsequently saved
    review bundles.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/taxa/archaea/aeropyrum_pernix.yaml
  accessed_at: '2026-10-20T04:10:38Z'
  support: supports
  summary: Read the entire generated YAML, including identity, lineage, names, mappings,
    source attestations, all imported strains and links, and seed history.
  locator: entire TaxonRecord; identifier=NCBITaxon:56636
  snapshot_sha256: 3d842c2e978630216733593e302600470fa015cbc8341ea1ec23f9876bd1e845
- evidence_id: taxonomy-inventory
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Inspected the target and each carried ancestor, rank, parent, genetic code
    and source name classes.
  locator: 'line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""};
    line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"};
    line 2980: {"taxon_id":"NCBITaxon:28889","label":"Thermoproteota","rank":"PHYLUM","parent_id":"NCBITaxon:1783275"};
    line 7138: {"taxon_id":"NCBITaxon:56635","label":"Aeropyrum","rank":"GENUS","parent_id":"NCBITaxon:871007"};
    line 7139: {"taxon_id":"NCBITaxon:56636","label":"Aeropyrum pernix","rank":"SPECIES","parent_id":"NCBITaxon:56635","genetic_code":"11","exact_synonyms":"","related_synonyms":"Aeropyrum
    pernix Sako et al. 1996","broad_synonyms":"","attested_by":"ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"};
    line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"};
    line 36612: {"taxon_id":"NCBITaxon:183924","label":"Thermoprotei","rank":"CLASS","parent_id":"NCBITaxon:28889"};
    line 184681: {"taxon_id":"NCBITaxon:871006","label":"Acidilobales","rank":"ORDER","parent_id":"NCBITaxon:183924"};
    line 184682: {"taxon_id":"NCBITaxon:871007","label":"Acidilobaceae","rank":"FAMILY","parent_id":"NCBITaxon:871006"};
    line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
- evidence_id: scope-row
  kind: database
  reference: curation/seed_scope.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Exact target is included in the declared seed scope.
  locator: 'line 5718: {"identifier":"NCBITaxon:56636","added":"2026-09-12","reason":"attested
    rule: Aeropyrum pernix, 7 sources incl. NCBI"}'
  snapshot_sha256: 5fdc0f7111b64e02439d95c6f2b51fcff1d2154c34b2d957422dd9b297e94d4b
- evidence_id: path-row
  kind: database
  reference: data/taxa/PATHS.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Indexed path resolves to this exact NCBI taxon.
  locator: 'line 542412: {"identifier":"NCBITaxon:56636","slug":"aeropyrum_pernix"}'
  snapshot_sha256: c950844feb0638ce04f7349784749dd1d728fe70bc80f7e2756d956d4ecea254
- evidence_id: ncbi-live
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1872114,3402690,1293648,3697131,439481,229980,1198449,56636,272557,1872399
  accessed_at: '2026-10-20T03:57:36Z'
  support: supports
  summary: 'Inspected the official response for this exact taxon: scientific name,
    rank, parent, source name classes, lineage and genetic code. Current authority
    and pinned September inventory remain distinct observations.'
  locator: TaxaSet/Taxon[TaxId='56636']; ten-target captured response
  snapshot_sha256: acd80e3bf24a6e49824d16abdb5eeaafa698c9de051130f9d27faec7e90b2cd8
- evidence_id: lpsn-inventory
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Inspected exact mapped and linked LPSN names; bounded inventory absence
    does not establish worldwide nomenclatural absence.
  locator: 'line 15094: {"lpsn_id":"lpsn:772925","name":"Aeropyrum pernix","rank":"SPECIES","authority":"Sako
    et al. 1996","url":"https://lpsn.dsmz.de/species/aeropyrum-pernix","deprecated":"0","status":"legitimate=True;
    validly published under the ICNP; correct name","validly_published":"1","legitimate":"1","is_correct_name":"1","parent_lpsn_id":"lpsn:516966","ncbitaxon_ids":"NCBITaxon:56636","gtdb_ids":"GTDB:s__Aeropyrum_pernix","type_strain_ids":"kgmicrobe.strain:ATCC-700893|kgmicrobe.strain:DSM-11879|kgmicrobe.strain:JCM-9820|kgmicrobe.strain:NBRC-100138","synonym_of":"","synonyms":"","publications":"PMID:8863437|doi:10.1099/00207713-46-4-1070|doi:10.1099/00207713-47-1-243","sequence_accessions":"INSDC:AB008745"}'
  snapshot_sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
- evidence_id: gtdb-mappings
  kind: database
  reference: data/raw/gtdb_mappings.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Inspected direct mappings and selected clusters' reverse mappings, retaining
    each source predicate and taxon boundary.
  locator: 'line 210667: {"gtdb_id":"GTDB:s__Aeropyrum_pernix","gtdb_label":"s__Aeropyrum_pernix","gtdb_parent":"GTDB:g__Aeropyrum","ncbitaxon_id":"NCBITaxon:272557","predicate":"skos:closeMatch","genome_count":"2"};
    line 296799: {"gtdb_id":"GTDB:s__Aeropyrum_pernix","gtdb_label":"s__Aeropyrum_pernix","gtdb_parent":"GTDB:g__Aeropyrum","ncbitaxon_id":"NCBITaxon:56636","predicate":"skos:closeMatch","genome_count":"2"}'
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
- evidence_id: gtdb-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Inspected source species identifiers, labels, parent clusters and genome
    counts.
  locator: 'line 5678: {"gtdb_id":"GTDB:s__Aeropyrum_pernix","label":"s__Aeropyrum_pernix","parent":"GTDB:g__Aeropyrum","genome_count":"2"}'
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
- evidence_id: bacdive-inventory
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Complete inventory selection covers the exact target and descendants from
    the complete NCBI parent graph; its imported strain population was compared with
    the complete YAML.
  locator: 'line 4091: {"strain_id":"kgmicrobe.strain:bacdive_4195","bacdive_id":"4195","designation":"K1","taxon_ids":"NCBITaxon:56636","lpsn_ids":"lpsn:772925","culture_collection_ids":"kgmicrobe.strain:ATCC-700893|kgmicrobe.strain:DSM-11879|kgmicrobe.strain:JCM-9820|kgmicrobe.strain:NBRC-100138","medium_count":"0"}'
  snapshot_sha256: 029fd6d1f53ef7f90684130bf0d644ed3edd1d8fbeb065a511ae928f160b1eea
- evidence_id: culture-inventory
  kind: database
  reference: data/raw/culture_collection_strains.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Inspected exact culture-inventory associations; an isolate name or genome
    does not create an inferred deposit.
  locator: 'line 7036: {"strain_id":"kgmicrobe.strain:ATCC-700893","taxon_ids":"NCBITaxon:56636"};
    line 64871: {"strain_id":"kgmicrobe.strain:DSM-11879","taxon_ids":"NCBITaxon:56636"};
    line 112866: {"strain_id":"kgmicrobe.strain:JCM-9820","taxon_ids":"NCBITaxon:56636"};
    line 132216: {"strain_id":"kgmicrobe.strain:NBRC-100138","taxon_ids":"NCBITaxon:56636"}'
  snapshot_sha256: 810fdcb16abd6330fb15bb03d4c74b18db86be36a7c599df7c6b2498d9735c95
- evidence_id: gold-organisms
  kind: database
  reference: data/raw/gold_organisms.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Inspected the exact GOLD organism count row or bounded absence, without
    converting counts to phenotypes.
  locator: 'line 39006: {"taxon_id":"NCBITaxon:56636","organism_count":"3"}'
  snapshot_sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
- evidence_id: mediadive-taxa
  kind: database
  reference: data/raw/mediadive_taxa.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Inspected the exact MediaDive medium count row or bounded absence, without
    converting counts to phenotypes.
  locator: 'line 11590: {"taxon_id":"NCBITaxon:56636","medium_count":"2","media_ids":"mediadive.medium:514|mediadive.medium:J224"}'
  snapshot_sha256: 3f74b78cadfcdb6aeae953e09fdb39e34fd9c5d5ed0be65a04a5d7fb02355905
- evidence_id: madin-taxa
  kind: database
  reference: data/raw/madin_taxa.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Inspected the exact Madin trait-assertion count row or bounded absence,
    without converting counts to phenotypes.
  locator: 'line 27086: {"taxon_id":"NCBITaxon:56636","assertion_count":"6"}'
  snapshot_sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
- evidence_id: bactotraits-taxa
  kind: database
  reference: data/raw/bactotraits_taxa.tsv
  accessed_at: '2026-10-20T03:58:07Z'
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
  accessed_at: '2026-10-20T04:10:38Z'
  support: supports
  summary: Policy permits one-to-one species closeMatch normalization and LPSN-linked
    species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage
    unchanged.
  locator: Mapping predicates; Which strains belong to a record
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
- evidence_id: equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-20T04:10:38Z'
  support: supports
  summary: TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations
    remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes
    under the source taxon.
  locator: TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
- evidence_id: seed-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-20T04:10:38Z'
  support: supports
  summary: Inspected mapping ranking, qualified predicates, fixed broadMatch wording,
    synonym/xref construction, primary cluster counts and same-taxon type-strain derivation.
  locator: GTDB mapping construction lines 440–472; LPSN/type-strain and source-attestation
    construction
  snapshot_sha256: 6b5b065f4ae7aea022af736a22c0f63dc58a2425c7ee453259e567ab030f8257
- evidence_id: manifest
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-20T04:10:38Z'
  support: supports
  summary: Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd,
    upstream input hashes and extraction time 2026-09-13T17:50:44Z.
  locator: kg_microbe_source, inputs, extracted_at
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
- evidence_id: overlay-manifests
  kind: record_content
  reference: data/atb/MANIFEST.yaml
  accessed_at: '2026-10-20T04:10:38Z'
  support: supports
  summary: Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z,
    matching the sole seed event. StrainInfo manifest is independently captured in
    source.inputs.
  locator: extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml
  snapshot_sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
- evidence_id: genome-catalog-1
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0017.jsonl.gz
  accessed_at: '2026-10-20T04:02:05Z'
  support: supports
  summary: Inspected primary membership and exact assembly/genome identifiers, retaining
    NCBI species/strain boundaries, source labels, accession versions, deposit fields
    and separate project/sample identities. No sequence equivalence or culture identity
    is inferred from names alone.
  locator: 'line 43686: {"accession":"RS_GCF_004323575.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Aeropyrum;s__Aeropyrum
    pernix","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM432357v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMD00074121","ncbi_contig_count":"148","ncbi_contig_n50":"27581","ncbi_country":"Japan:Kagoshima;
    Ibusuki; Yamagawa Beach","ncbi_date":"2019-01-18","ncbi_genbank_assembly_accession":"GCA_004323575.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"sediment","ncbi_lat_lon":"31.1058
    N 130.3659 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Aeropyrum
    pernix","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"10","ncbi_scaffold_count":"144","ncbi_scaffold_l50":"17","ncbi_scaffold_n50":"27581","ncbi_scaffold_n75":"15253","ncbi_scaffold_n90":"7108","ncbi_seq_rel_date":"2019-01-18","ncbi_spanned_gaps":"4","ncbi_species_taxid":"56636","ncbi_ssu_count":"5","ncbi_strain_identifiers":"YK1-12-2013","ncbi_submitter":"Laboratory
    of Marine Microbiology, Graduate School of Agriculture, Kyoto University","ncbi_taxid":"56636","ncbi_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei;o__Desulfurococcales;f__Desulfurococcaceae;g__Aeropyrum;s__Aeropyrum
    pernix","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Thermoproteota;c__Thermoprotei;o__Desulfurococcales;f__Desulfurococcaceae;g__Aeropyrum;s__Aeropyrum
    pernix","ncbi_total_gap_length":"56","ncbi_total_length":"1601052","ncbi_translation_table":"11","ncbi_trna_count":"45","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1600996","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"BDMD00000000.1"};
    line 46966: {"accession":"RS_GCF_000011125.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Aeropyrum;s__Aeropyrum
    pernix","gtdb_type_species_of_genus":"t","ncbi_assembly_level":"Complete Genome","ncbi_assembly_name":"ASM1112v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMD00061092","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"none","ncbi_date":"2006-11-28","ncbi_genbank_assembly_accession":"GCA_000011125.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Aeropyrum
    pernix K1","ncbi_protein_count":"none","ncbi_refseq_category":"reference genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"1669696","ncbi_scaffold_n75":"1669696","ncbi_scaffold_n90":"1669696","ncbi_seq_rel_date":"2006-11-28","ncbi_spanned_gaps":"0","ncbi_species_taxid":"56636","ncbi_ssu_count":"1","ncbi_strain_identifiers":"K1","ncbi_submitter":"NITE","ncbi_taxid":"272557","ncbi_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei;o__Desulfurococcales;f__Desulfurococcaceae;g__Aeropyrum;s__Aeropyrum
    pernix","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Thermoproteota;c__Thermoprotei;o__Desulfurococcales;f__Desulfurococcaceae;g__Aeropyrum;s__Aeropyrum
    pernix;x__Aeropyrum pernix K1","ncbi_total_gap_length":"0","ncbi_total_length":"1669696","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"assembly
    from type material","ncbi_ungapped_length":"1669696","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"}'
  snapshot_sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
- evidence_id: genome-catalog-2
  kind: primary_source
  reference: data/catalog/ncbi_genbank-0000.jsonl.gz
  accessed_at: '2026-10-20T04:02:05Z'
  support: supports
  summary: Inspected primary membership and exact assembly/genome identifiers, retaining
    NCBI species/strain boundaries, source labels, accession versions, deposit fields
    and separate project/sample identities. No sequence equivalence or culture identity
    is inferred from names alone.
  locator: 'line 227: {"annotation_date":"2016-10-08","annotation_name":"Annotation
    submitted by NITE","annotation_provider":"NITE","asm_name":"ASM1112v1","asm_not_live_date":"na","asm_submitter":"NITE","assembly_accession":"GCA_000011125.1","assembly_level":"Complete
    Genome","assembly_type":"haploid","bioproject":"PRJNA211","biosample":"SAMD00061092","contig_count":"1","excluded_from_refseq":"na","ftp_path":"https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/011/125/GCA_000011125.1_ASM1112v1/","gbrs_paired_asm":"GCF_000011125.1","gc_percent":"56.500000","genome_rep":"Full","genome_size":"1669696","genome_size_ungapped":"1669696","group":"archaea","infraspecific_name":"strain=K1","isolate":"na","non_coding_gene_count":"52","organism_name":"Aeropyrum
    pernix K1","paired_asm_comp":"identical","protein_coding_gene_count":"1700","pubmed_id":"10382966;16455681;16769697","refseq_category":"reference
    genome","relation_to_type_material":"assembly from type material","release_type":"Major","replicon_count":"1","scaffold_count":"1","seq_rel_date":"2006-10-11","species_taxid":"56636","taxid":"272557","total_gene_count":"1752","version_status":"latest","wgs_master":"na"}'
  snapshot_sha256: 2d0f73ddded027424214ecc6c9f0c91ec229278cacf8d0e1d63e5745c8064ea7
- evidence_id: genome-catalog-3
  kind: primary_source
  reference: data/bvbrc/bvbrc-0015.jsonl.gz
  accessed_at: '2026-10-20T04:02:05Z'
  support: supports
  summary: Inspected primary membership and exact assembly/genome identifiers, retaining
    NCBI species/strain boundaries, source labels, accession versions, deposit fields
    and separate project/sample identities. No sequence equivalence or culture identity
    is inferred from names alone.
  locator: 'line 17056: {"assembly_accession":"GCA_000011125.1","bioproject_accession":"PRJNA211","biosample_accession":"-","date_modified":"2015-03-16T03:17:09.594Z","genbank_accessions":"BA000002.3","genome_id":"272557.25","genome_name":"Aeropyrum
    pernix K1","genome_status":"Complete","public":true,"reference_genome":"Representative","refseq_accessions":"NC_000854.2","strain":"K1","superkingdom":"Archaea","taxon_id":272557,"taxon_lineage_ids":["131567","2157","1783275","28889","183924","114380","2272","56635","56636","272557"],"taxon_lineage_names":["cellular
    organisms","Archaea","Thermoproteati","Thermoproteota","Thermoprotei","Desulfurococcales","Desulfurococcaceae","Aeropyrum","Aeropyrum
    pernix","Aeropyrum pernix K1"]}; line 17057: {"bioproject_accession":"PRJNA224116","biosample_accession":"SAMD00061092","culture_collection":"NBRC:100138","date_modified":"2026-02-03T15:48:59.329Z","genbank_accessions":"NC_000854","genome_id":"272557.33","genome_name":"Aeropyrum
    pernix K1","genome_status":"WGS","public":true,"strain":"K1","superkingdom":"Archaea","taxon_id":272557,"taxon_lineage_ids":["131567","2157","1783275","28889","183924","114380","2272","56635","56636","272557"],"taxon_lineage_names":["cellular
    organisms","Archaea","Thermoproteati","Thermoproteota","Thermoprotei","Desulfurococcales","Desulfurococcaceae","Aeropyrum","Aeropyrum
    pernix","Aeropyrum pernix K1"]}'
  snapshot_sha256: 6387f2db4e0dd8b1c4f91a1506223687dd465f05b213bcae74968644805af13e
- evidence_id: gtdb-full-scan
  kind: search
  reference: data/catalog/MANIFEST.json
  accessed_at: '2026-10-20T04:02:05Z'
  support: supports
  summary: All nineteen GTDB shards were hashed and searched with exact terminal species
    tokens. Source counts and taxon distributions were inspected; a cluster is not
    equated with an individual strain.
  locator: '{"paths":["data/catalog/gtdb_genomes-0000.jsonl.gz","data/catalog/gtdb_genomes-0001.jsonl.gz","data/catalog/gtdb_genomes-0002.jsonl.gz","data/catalog/gtdb_genomes-0003.jsonl.gz","data/catalog/gtdb_genomes-0004.jsonl.gz","data/catalog/gtdb_genomes-0005.jsonl.gz","data/catalog/gtdb_genomes-0006.jsonl.gz","data/catalog/gtdb_genomes-0007.jsonl.gz","data/catalog/gtdb_genomes-0008.jsonl.gz","data/catalog/gtdb_genomes-0009.jsonl.gz","data/catalog/gtdb_genomes-0010.jsonl.gz","data/catalog/gtdb_genomes-0011.jsonl.gz","data/catalog/gtdb_genomes-0012.jsonl.gz","data/catalog/gtdb_genomes-0013.jsonl.gz","data/catalog/gtdb_genomes-0014.jsonl.gz","data/catalog/gtdb_genomes-0015.jsonl.gz","data/catalog/gtdb_genomes-0016.jsonl.gz","data/catalog/gtdb_genomes-0017.jsonl.gz","data/catalog/gtdb_genomes-0018.jsonl.gz"],"clusters":[{"id":"GTDB:s__Aeropyrum_pernix","count":2,"ncbi_taxids":{"56636":1,"272557":1},"other_taxa_note_supported":true}]}'
  snapshot_sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
  search_scope: Full explicit reads of every enumerated GTDB, NCBI GenBank/RefSeq
    and BV-BRC primary shard including ignored files. Exact terminal GTDB species
    token; exact assembly accession stem or explicit genome identifier. Versions remain
    separate.
- evidence_id: strain-table-1
  kind: database
  reference: data/raw/strain_assemblies.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Compared the complete imported assertion multiset, retaining multiplicity,
    literal source fields, versions and deposit scope.
  locator: 'line 125234: {"strain_id":"kgmicrobe.strain:bacdive_4195","assembly_id":"ncbi.assembly:GCA_000011125","source":"BACDIVE","source_id":"bacdive:4195","source_reference_id":"66792","assembly_level":"complete","assembly_name":"ASM1112v1
    assembly for Aeropyrum pernix K1","taxon_id":"NCBITaxon:272557","source_field":"Sequence
    information.Genome sequences.INSDC accession","matched_strain_id":"","source_strain_identifiers":"","source_strain_field":"","source_organism_id":"","source_project_id":""};
    line 125235: {"strain_id":"kgmicrobe.strain:bacdive_4195","assembly_id":"ncbi.assembly:GCA_000011125.1","source":"GOLD","source_id":"gold:Ga0039428","source_reference_id":"","assembly_level":"","assembly_name":"Aeropyrum
    pernix K1","taxon_id":"NCBITaxon:272557","source_field":"AP GENBANK.assemblyAccession","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0000767"}'
  snapshot_sha256: 71344b934db3081bfcac9562a0bd1fd8fddcfdabb8af60e208ca09035e818315
- evidence_id: strain-table-2
  kind: database
  reference: data/raw/strain_genome_records.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Compared the complete imported assertion multiset, retaining multiplicity,
    literal source fields, versions and deposit scope.
  locator: 'line 100637: {"strain_id":"kgmicrobe.strain:bacdive_4195","genome_id":"img.taxon:2923402010","source_database":"img","source":"BACDIVE","source_id":"bacdive:4195","source_reference_id":"66792","assembly_level":"complete","genome_name":"ASM1112v1
    assembly for Aeropyrum pernix K1","taxon_id":"NCBITaxon:272557","source_field":"Sequence
    information.Genome sequences.IMG accession","matched_strain_id":"","source_strain_identifiers":"","source_strain_field":"","source_organism_id":"","source_project_id":""};
    line 100638: {"strain_id":"kgmicrobe.strain:bacdive_4195","genome_id":"img.taxon:2923402010","source_database":"img","source":"GOLD","source_id":"gold:Ga0039428","source_reference_id":"","assembly_level":"","genome_name":"Aeropyrum
    pernix K1","taxon_id":"NCBITaxon:272557","source_field":"AP IMG TAXON ID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0000767"};
    line 100639: {"strain_id":"kgmicrobe.strain:bacdive_4195","genome_id":"patric:272557.25","source_database":"patric","source":"BACDIVE","source_id":"bacdive:4195","source_reference_id":"66792","assembly_level":"complete","genome_name":"ASM1112v1
    assembly for Aeropyrum pernix K1","taxon_id":"NCBITaxon:272557","source_field":"Sequence
    information.Genome sequences.BV-BRC accession","matched_strain_id":"","source_strain_identifiers":"","source_strain_field":"","source_organism_id":"","source_project_id":""};
    line 100640: {"strain_id":"kgmicrobe.strain:bacdive_4195","genome_id":"patric:272557.33","source_database":"patric","source":"BV_BRC","source_id":"patric:272557.33","source_reference_id":"","assembly_level":"","genome_name":"Aeropyrum
    pernix K1","taxon_id":"NCBITaxon:272557","source_field":"genome_id","matched_strain_id":"kgmicrobe.strain:NBRC-100138","source_strain_identifiers":"NBRC:100138","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""}'
  snapshot_sha256: 47ed80be55660aad4bd82d37d889ea60f8686cec1aeeccf72e5af22bf43728ab
- evidence_id: strain-table-3
  kind: database
  reference: data/raw/strain_related_records.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Compared the complete imported assertion multiset, retaining multiplicity,
    literal source fields, versions and deposit scope.
  locator: 'line 361165: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"bioproject:PRJNA211","record_type":"BIOPROJECT","source":"GOLD","source_id":"gold:Gp0000767","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI
    BIOPROJECT ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0000767"};
    line 361166: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"bioproject:PRJNA224116","record_type":"BIOPROJECT","source":"BV_BRC","source_id":"patric:272557.33","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"bioproject_accession","matched_strain_id":"kgmicrobe.strain:NBRC-100138","source_strain_identifiers":"NBRC:100138","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""};
    line 361167: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"bioproject:PRJNA263076","record_type":"BIOPROJECT","source":"GOLD","source_id":"gold:Gp0102910","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI
    BIOPROJECT ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0102910"};
    line 361168: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"bioproject:PRJNA425658","record_type":"BIOPROJECT","source":"GOLD","source_id":"gold:Gp0225950","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI
    BIOPROJECT ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0225950"};
    line 361169: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"bioproject:PRJNA425659","record_type":"BIOPROJECT","source":"GOLD","source_id":"gold:Gp0225951","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI
    BIOPROJECT ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0225951"};
    line 361170: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"biosample:SAMD00061092","record_type":"BIOSAMPLE","source":"BV_BRC","source_id":"patric:272557.33","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"biosample_accession","matched_strain_id":"kgmicrobe.strain:NBRC-100138","source_strain_identifiers":"NBRC:100138","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""};
    line 361171: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"biosample:SAMD00061092","record_type":"BIOSAMPLE","source":"GOLD","source_id":"gold:Gp0000767","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI
    BIOSAMPLE ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0000767"};
    line 361172: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"biosample:SAMN03097722","record_type":"BIOSAMPLE","source":"GOLD","source_id":"gold:Gp0102910","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI
    BIOSAMPLE ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0102910"};
    line 361173: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"biosample:SAMN08221418","record_type":"BIOSAMPLE","source":"GOLD","source_id":"gold:Gp0225951","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI
    BIOSAMPLE ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0225951"};
    line 361174: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"biosample:SAMN08221419","record_type":"BIOSAMPLE","source":"GOLD","source_id":"gold:Gp0225950","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"","source_field":"NCBI
    BIOSAMPLE ACCESSION","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0225950"};
    line 361175: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Ga0039428","record_type":"GOLD_ANALYSIS","source":"GOLD","source_id":"gold:Ga0039428","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"Aeropyrum
    pernix K1","source_field":"AP GOLD ID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0000767"};
    line 361176: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Go0000767","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0000767","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"Aeropyrum
    pernix K1","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":""};
    line 361177: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Go0624942","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0624942","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"Aeropyrum
    pernix JCM 9820","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:JCM-9820","source_strain_identifiers":"JCM
    9820","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0624942","source_project_id":""};
    line 361178: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Go0624942","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0624942","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"Aeropyrum
    pernix JCM 9820","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:JCM-9820","source_strain_identifiers":"JCM
    9820","source_strain_field":"ORGANISM STRAIN","source_organism_id":"gold:Go0624942","source_project_id":""};
    line 361179: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Go0624943","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0624943","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"Aeropyrum
    pernix DSM 11879","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:DSM-11879","source_strain_identifiers":"DSM
    11879","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0624943","source_project_id":""};
    line 361180: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Go0624943","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0624943","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"Aeropyrum
    pernix DSM 11879","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:DSM-11879","source_strain_identifiers":"DSM
    11879","source_strain_field":"ORGANISM STRAIN","source_organism_id":"gold:Go0624943","source_project_id":""};
    line 361181: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Gp0000767","record_type":"GOLD_PROJECT","source":"GOLD","source_id":"gold:Gp0000767","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"Aeropyrum
    pernix K1","source_field":"PROJECT GOLD ID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0000767"};
    line 361182: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Gp0102910","record_type":"GOLD_PROJECT","source":"GOLD","source_id":"gold:Gp0102910","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"Aeropyrum
    pernix K1","source_field":"PROJECT GOLD ID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0102910"};
    line 361183: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Gp0225950","record_type":"GOLD_PROJECT","source":"GOLD","source_id":"gold:Gp0225950","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"Aeropyrum
    pernix K1 transcriptome - Ape E","source_field":"PROJECT GOLD ID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0225950"};
    line 361184: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"gold:Gp0225951","record_type":"GOLD_PROJECT","source":"GOLD","source_id":"gold:Gp0225951","source_reference_id":"","taxon_id":"NCBITaxon:272557","record_name":"Aeropyrum
    pernix K1 transcriptome - Ape S","source_field":"PROJECT GOLD ID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0000767","source_project_id":"gold:Gp0225951"}'
  snapshot_sha256: c33a9bf4c6b94dc6971f1c0d46565092c37ba7c2d462a6bc9c20ccbf58fb9c56
- evidence_id: strain-table-4
  kind: database
  reference: data/straininfo/strain_links.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Compared the complete imported assertion multiset, retaining multiplicity,
    literal source fields, versions and deposit scope.
  locator: 'line 88615: {"strain_id":"kgmicrobe.strain:bacdive_4195","straininfo_strain_id":"straininfo.strain:44195","straininfo_deposit_id":"straininfo.deposit:118657","matched_strain_id":"kgmicrobe.strain:ATCC-700893","deposit_designation":"ATCC
    700893","strain_doi":"DOI:10.60712/SI-ID44195.3","strain_status":"published online","deposit_status":"available","source_bacdive_id":"bacdive:4195","taxon_id":"NCBITaxon:56636"};
    line 88616: {"strain_id":"kgmicrobe.strain:bacdive_4195","straininfo_strain_id":"straininfo.strain:44195","straininfo_deposit_id":"straininfo.deposit:118658","matched_strain_id":"kgmicrobe.strain:JCM-9820","deposit_designation":"JCM
    9820","strain_doi":"DOI:10.60712/SI-ID44195.3","strain_status":"published online","deposit_status":"available","source_bacdive_id":"bacdive:4195","taxon_id":"NCBITaxon:56636"};
    line 88617: {"strain_id":"kgmicrobe.strain:bacdive_4195","straininfo_strain_id":"straininfo.strain:44195","straininfo_deposit_id":"straininfo.deposit:118659","matched_strain_id":"kgmicrobe.strain:DSM-11879","deposit_designation":"DSM
    11879","strain_doi":"DOI:10.60712/SI-ID44195.3","strain_status":"published online","deposit_status":"available","source_bacdive_id":"bacdive:4195","taxon_id":"NCBITaxon:56636"};
    line 88618: {"strain_id":"kgmicrobe.strain:bacdive_4195","straininfo_strain_id":"straininfo.strain:44195","straininfo_deposit_id":"straininfo.deposit:335948","matched_strain_id":"kgmicrobe.strain:NBRC-100138","deposit_designation":"NBRC
    100138","strain_doi":"DOI:10.60712/SI-ID44195.3","strain_status":"published online","deposit_status":"available","source_bacdive_id":"bacdive:4195","taxon_id":"NCBITaxon:56636"}'
  snapshot_sha256: 615ac119e61df3a9d296ab16674bca6de3fdbf6478ca21a61312014f0ebbae8f
- evidence_id: strain-table-5
  kind: database
  reference: data/straininfo/assemblies.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Compared the complete imported assertion multiset, retaining multiplicity,
    literal source fields, versions and deposit scope.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: d55ba39ab7cb81076a8edb61226de2bdf0aea699a7fb003cdf3ffb3ddc2f3f52
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: strain-table-6
  kind: database
  reference: data/straininfo/related_records.tsv.gz
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Compared the complete imported assertion multiset, retaining multiplicity,
    literal source fields, versions and deposit scope.
  locator: 'line 214082: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.deposit:118657","record_type":"STRAININFO_DEPOSIT","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"ATCC
    700893","source_field":"deposits.siDP","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"ATCC
    700893\",\"deposit_id\":\"straininfo.deposit:118657\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published
    online\"}"}; line 214083: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.deposit:118658","record_type":"STRAININFO_DEPOSIT","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"JCM
    9820","source_field":"deposits.siDP","matched_strain_id":"kgmicrobe.strain:JCM-9820","source_strain_identifiers":"JCM
    9820","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"JCM
    9820\",\"deposit_id\":\"straininfo.deposit:118658\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published
    online\"}"}; line 214084: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.deposit:118659","record_type":"STRAININFO_DEPOSIT","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"DSM
    11879","source_field":"deposits.siDP","matched_strain_id":"kgmicrobe.strain:DSM-11879","source_strain_identifiers":"DSM
    11879","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"DSM
    11879\",\"deposit_id\":\"straininfo.deposit:118659\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published
    online\"}"}; line 214085: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.deposit:335948","record_type":"STRAININFO_DEPOSIT","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"NBRC
    100138","source_field":"deposits.siDP","matched_strain_id":"kgmicrobe.strain:NBRC-100138","source_strain_identifiers":"NBRC
    100138","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"NBRC
    100138\",\"deposit_id\":\"straininfo.deposit:335948\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published
    online\"}"}; line 214086: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.strain:44195","record_type":"STRAININFO_STRAIN","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"ATCC
    700893","source_field":"strain.siID","matched_strain_id":"kgmicrobe.strain:ATCC-700893","source_strain_identifiers":"ATCC
    700893","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"ATCC
    700893\",\"deposit_id\":\"straininfo.deposit:118657\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published
    online\"}"}; line 214087: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.strain:44195","record_type":"STRAININFO_STRAIN","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"DSM
    11879","source_field":"strain.siID","matched_strain_id":"kgmicrobe.strain:DSM-11879","source_strain_identifiers":"DSM
    11879","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"DSM
    11879\",\"deposit_id\":\"straininfo.deposit:118659\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published
    online\"}"}; line 214088: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.strain:44195","record_type":"STRAININFO_STRAIN","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"JCM
    9820","source_field":"strain.siID","matched_strain_id":"kgmicrobe.strain:JCM-9820","source_strain_identifiers":"JCM
    9820","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"JCM
    9820\",\"deposit_id\":\"straininfo.deposit:118658\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published
    online\"}"}; line 214089: {"strain_id":"kgmicrobe.strain:bacdive_4195","record_id":"straininfo.strain:44195","record_type":"STRAININFO_STRAIN","source":"STRAININFO","source_id":"straininfo.strain:44195","source_reference_id":"","taxon_id":"NCBITaxon:56636","record_name":"NBRC
    100138","source_field":"strain.siID","matched_strain_id":"kgmicrobe.strain:NBRC-100138","source_strain_identifiers":"NBRC
    100138","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"NBRC
    100138\",\"deposit_id\":\"straininfo.deposit:335948\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:4195\",\"strain_doi\":\"DOI:10.60712/SI-ID44195.3\",\"strain_id\":\"straininfo.strain:44195\",\"strain_status\":\"published
    online\"}"}'
  snapshot_sha256: c7a262df4f970b2b11a2cf7a0a05c631ff84938e6a19cdb1d98680bb4fb35108
- evidence_id: strain-table-7
  kind: database
  reference: data/atb/strain_links.tsv
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Compared the complete imported assertion multiset, retaining multiplicity,
    literal source fields, versions and deposit scope.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 50683192c8015badf14a8a2aab73929a21b830117449ce329d1216a698abf1c0
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: strain-primary-1
  kind: primary_source
  reference: data/bacdive/records.jsonl.gz
  accessed_at: '2026-10-20T03:59:22Z'
  support: supports
  summary: Inspected complete selected BacDive, StrainInfo and GOLD primary objects.
    Explicit deposits and project/analysis chains support only their narrow claims.
    Historical aggregates are not recounted by these newer objects.
  locator: 'line 4090: {"General":{"@ref":4521,"BacDive-ID":4195,"NCBI tax id":{"Matching
    level":"species","NCBI tax id":56636},"doi":"10.13145/bacdive4195.20260601.11"},"Literature":{"@ref":4521,"culture
    collection no.":"DSM 11879, JCM 9820, ATCC 700893, NBRC 100138","straininfo link":{"@ref":126262,"straininfo":44195}},"Name
    and taxonomic classification":{"@ref":4521,"LPSN":{"@ref":20215,"class":"Thermoprotei","description":"domain/archaea","domain":"Archaea","family":"Acidilobaceae","full
    scientific name":"<I>Aeropyrum</I> <I>pernix</I> Sako et al. 1996","genus":"Aeropyrum","keyword":"phylum/thermoproteota","order":"Acidilobales","phylum":"Thermoproteota","species":"Aeropyrum
    pernix"},"class":"Thermoprotei","domain":"Archaea","family":"Desulfurococcaceae","full
    scientific name":"Aeropyrum pernix Sako et al. 1996","genus":"Aeropyrum","order":"Desulfurococcales","phylum":"Crenarchaeota","species":"Aeropyrum
    pernix","strain designation":"K1","type strain":"yes"},"Sequence information":{"16S
    sequences":[{"@ref":4521,"NCBI tax ID":56636,"accession":"D83259","database":"nuccore","description":"Aeropyrum
    pernix gene for 16S rRNA, partial sequence","length":1444},{"@ref":67770,"NCBI
    tax ID":56636,"accession":"AB008745","database":"nuccore","description":"Aeropyrum
    pernix genes for 16S rRNA, 23S rRNA and rRNA intron-encoded homing endonuclease,
    complete cds","length":10777}],"Genome sequences":{"@ref":66792,"BV-BRC accession":"272557.25","IMG
    accession":"2923402010","INSDC accession":"GCA_000011125","NCBI tax ID":272557,"assembly
    level":"complete","description":"ASM1112v1 assembly for Aeropyrum pernix K1","score":96.94}}}'
  snapshot_sha256: b27d0f50f06aa33615e7cc2aae4acb7c2767df930c85292e76fbb462ac136080
- evidence_id: strain-primary-2
  kind: primary_source
  reference: data/straininfo/records.jsonl.gz
  accessed_at: '2026-10-20T03:59:22Z'
  support: supports
  summary: Inspected complete selected BacDive, StrainInfo and GOLD primary objects.
    Explicit deposits and project/analysis chains support only their narrow claims.
    Historical aggregates are not recounted by these newer objects.
  locator: 'line 32365: {"deposits":[{"cultureCollection":{"ccID":4,"code":"ATCC","deprecated":false,"name":"American
    Type Culture Collection"},"designation":"ATCC 700893","lastUpdate":"2005-10-22","siDP":118657,"status":"available","taxon":{"lpsn":772925,"name":"Aeropyrum
    pernix","ncbi":56636},"typeStrain":true},{"cultureCollection":{"ccID":14,"code":"JCM","deprecated":false,"name":"Japan
    Collection of Microorganisms"},"designation":"JCM 9820","lastUpdate":"2005-10-22","siDP":118658,"status":"available","taxon":{"lpsn":772925,"name":"Aeropyrum
    pernix","ncbi":56636},"typeStrain":true},{"cultureCollection":{"ccID":1,"code":"DSMZ","deprecated":false,"name":"DSMZ-German
    Collection of Microorganisms and Cell Cultures"},"designation":"DSM 11879","lastUpdate":"2024-12-03","siDP":118659,"status":"available","taxon":{"lpsn":772925,"name":"Aeropyrum
    pernix","ncbi":56636},"typeStrain":true},{"cultureCollection":{"ccID":12,"code":"NBRC","deprecated":false,"name":"Biological
    Resource Center, NITE"},"designation":"NBRC 100138","lastUpdate":"2005-10-22","siDP":335948,"status":"available","taxon":{"lpsn":772925,"name":"Aeropyrum
    pernix","ncbi":56636},"typeStrain":true}],"strain":{"archive":[{"date":"2024-05-31","doi":"10.60712/SI-ID44195.1","title":"StrainInfo
    SI-ID 44195.1"},{"date":"2024-06-05","doi":"10.60712/SI-ID44195.2","title":"StrainInfo
    SI-ID 44195.2"},{"date":"2025-02-25","doi":"10.60712/SI-ID44195.3","title":"StrainInfo
    SI-ID 44195.3"}],"bdID":4195,"doi":"10.60712/SI-ID44195.3","relation":{"deposit":[{"ccID":4,"designation":"ATCC
    700893","erroneous":false,"origin":118658,"siDP":118657},{"ccID":14,"designation":"JCM
    9820","erroneous":false,"siDP":118658},{"ccID":1,"designation":"DSM 11879","erroneous":false,"origin":118658,"siDP":118659},{"ccID":12,"designation":"NBRC
    100138","erroneous":false,"origin":118658,"siDP":335948}],"designation":["Nomura
    K1"]},"siID":44195,"status":"published online","taxon":{"lpsn":772925,"name":"Aeropyrum
    pernix","ncbi":56636}}}'
  snapshot_sha256: 8f8e6093f0617317e0488463e52de153f566effa7a5d43b44d17dabab9692819
- evidence_id: strain-primary-3
  kind: primary_source
  reference: data/gold/organisms.jsonl.gz
  accessed_at: '2026-10-20T03:59:22Z'
  support: supports
  summary: Inspected complete selected BacDive, StrainInfo and GOLD primary objects.
    Explicit deposits and project/analysis chains support only their narrow claims.
    Historical aggregates are not recounted by these newer objects.
  locator: 'line 727: {"ORGANISM CULTURE COLLECTION ID":"ATCC 700893","ORGANISM GOLD
    ID":"Go0000767","ORGANISM NAME":"Aeropyrum pernix K1","ORGANISM NCBI TAX ID":"272557","ORGANISM
    STRAIN":"K1"}; line 455549: {"ORGANISM CULTURE COLLECTION ID":"JCM 9820","ORGANISM
    GOLD ID":"Go0624942","ORGANISM NAME":"Aeropyrum pernix JCM 9820","ORGANISM NCBI
    TAX ID":"56636","ORGANISM STRAIN":"JCM 9820"}; line 455550: {"ORGANISM CULTURE
    COLLECTION ID":"DSM 11879","ORGANISM GOLD ID":"Go0624943","ORGANISM NAME":"Aeropyrum
    pernix DSM 11879","ORGANISM NCBI TAX ID":"56636","ORGANISM STRAIN":"DSM 11879"}'
  snapshot_sha256: 8c1a055214cb240c58fadda0815efbefcb60848245e8a7474e6b1b41d123235c
- evidence_id: strain-primary-4
  kind: primary_source
  reference: data/gold/projects.jsonl.gz
  accessed_at: '2026-10-20T03:59:22Z'
  support: supports
  summary: Inspected complete selected BacDive, StrainInfo and GOLD primary objects.
    Explicit deposits and project/analysis chains support only their narrow claims.
    Historical aggregates are not recounted by these newer objects.
  locator: 'line 744: {"NCBI BIOPROJECT ACCESSION":"PRJNA211","NCBI BIOSAMPLE ACCESSION":"SAMD00061092","ORGANISM
    GOLD ID":"Go0000767","PROJECT GOLD ID":"Gp0000767","PROJECT NAME":"Aeropyrum pernix
    K1"}; line 59212: {"NCBI BIOPROJECT ACCESSION":"PRJNA263076","NCBI BIOSAMPLE ACCESSION":"SAMN03097722","ORGANISM
    GOLD ID":"Go0000767","PROJECT GOLD ID":"Gp0102910","PROJECT NAME":"Aeropyrum pernix
    K1"}; line 150393: {"NCBI BIOPROJECT ACCESSION":"PRJNA425658","NCBI BIOSAMPLE
    ACCESSION":"SAMN08221419","ORGANISM GOLD ID":"Go0000767","PROJECT GOLD ID":"Gp0225950","PROJECT
    NAME":"Aeropyrum pernix K1 transcriptome - Ape E"}; line 150394: {"NCBI BIOPROJECT
    ACCESSION":"PRJNA425659","NCBI BIOSAMPLE ACCESSION":"SAMN08221418","ORGANISM GOLD
    ID":"Go0000767","PROJECT GOLD ID":"Gp0225951","PROJECT NAME":"Aeropyrum pernix
    K1 transcriptome - Ape S"}'
  snapshot_sha256: 0d852fe0144afd778609fef82b266fd1507a4c0be949efd2f53c7c34526b6c95
- evidence_id: strain-primary-5
  kind: primary_source
  reference: data/gold/analyses.jsonl.gz
  accessed_at: '2026-10-20T03:59:22Z'
  support: supports
  summary: Inspected complete selected BacDive, StrainInfo and GOLD primary objects.
    Explicit deposits and project/analysis chains support only their narrow claims.
    Historical aggregates are not recounted by these newer objects.
  locator: 'line 25149: {"AP GENBANK":"[{\"genbankId\":\"BA000002\",\"assemblyAccession\":\"GCA_000011125.1\"}]","AP
    GOLD ID":"Ga0039428","AP IMG TAXON ID":"2923402010","AP NAME":"Aeropyrum pernix
    K1","AP ORGANISM GOLD ID":"","AP PROJECT GOLD IDS":"Gp0000767","AP TYPE":"Genome
    Analysis (Isolate)"}'
  snapshot_sha256: d597f0d5f31fc8b387caaf659f3c6a337959219870529e907a1c0287e3877b7a
- evidence_id: gold-project-discovery
  kind: search
  reference: data/gold/projects.jsonl.gz
  accessed_at: '2026-10-20T04:02:21Z'
  support: supports
  summary: Full exact organism-field search verifies the available project chains
    and bounded absences for the explicitly selected organism IDs; no project or analysis
    is inferred from an empty filtered artifact.
  locator: '[{"line":744,"row":{"NCBI BIOPROJECT ACCESSION":"PRJNA211","NCBI BIOSAMPLE
    ACCESSION":"SAMD00061092","ORGANISM GOLD ID":"Go0000767","PROJECT GOLD ID":"Gp0000767","PROJECT
    NAME":"Aeropyrum pernix K1"}},{"line":59212,"row":{"NCBI BIOPROJECT ACCESSION":"PRJNA263076","NCBI
    BIOSAMPLE ACCESSION":"SAMN03097722","ORGANISM GOLD ID":"Go0000767","PROJECT GOLD
    ID":"Gp0102910","PROJECT NAME":"Aeropyrum pernix K1"}},{"line":150393,"row":{"NCBI
    BIOPROJECT ACCESSION":"PRJNA425658","NCBI BIOSAMPLE ACCESSION":"SAMN08221419","ORGANISM
    GOLD ID":"Go0000767","PROJECT GOLD ID":"Gp0225950","PROJECT NAME":"Aeropyrum pernix
    K1 transcriptome - Ape E"}},{"line":150394,"row":{"NCBI BIOPROJECT ACCESSION":"PRJNA425659","NCBI
    BIOSAMPLE ACCESSION":"SAMN08221418","ORGANISM GOLD ID":"Go0000767","PROJECT GOLD
    ID":"Gp0225951","PROJECT NAME":"Aeropyrum pernix K1 transcriptome - Ape S"}}]'
  snapshot_sha256: 0d852fe0144afd778609fef82b266fd1507a4c0be949efd2f53c7c34526b6c95
  search_scope: Full explicit project source read including ignored files; exact selected
    ORGANISM GOLD ID fields. Empty selected artifacts were not treated as full-file
    absence evidence.
- evidence_id: cafi-registry
  kind: authority
  reference: src/taxonmech/data/cafi_acronyms.json
  accessed_at: '2026-10-20T04:02:21Z'
  support: supports
  summary: Explicit registered deposit keys pass the authority/accession rule. Bare
    T469, SY1 and K1 do not; genome association alone is not a deposit join.
  locator: '{"accessed_at":"2026-10-20T04:02:21.239529+00:00","registry_rows":{"1":{"acr":"DSM","acr_synonym":["DSMZ"],"active":true,"catalogue":["https://www.dsmz.de/collection/catalogue/details/culture/{acr}-{id}"],"code":"DSMZ","country":"DE","gbif":"883f3d24-35e9-462d-b7a3-13c2b9b7260e","homepage":"https://www.dsmz.de/","name":"DSMZ-German
    Collection of Microorganisms and Cell Cultures","regex_ccno":"^DSM\\s*\\d+$","regex_id":{"full":"^\\d+$"},"ror":"02tyer376"},"4":{"acr":"ATCC","active":true,"catalogue":["https://www.atcc.org/products/{id}"],"code":"ATCC","country":"US","gbif":"25160e92-1a80-4226-9afb-b25691622ac6","homepage":"https://www.atcc.org/","name":"American
    Type Culture Collection","regex_ccno":"^ATCC\\s*((BAA|TSD|MYA|SD|VR|PTA)-)?\\d+$","regex_id":{"core":"\\d+","full":"^((BAA|TSD|MYA|SD|VR|PTA)-)?\\d+$","pre":"(BAA|TSD|MYA|SD|VR|PTA)"},"ror":"03thhhv76"},"14":{"acr":"JCM","active":true,"catalogue":["https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?{acr}={id}"],"code":"JCM","country":"JP","gbif":"fce1f744-ca76-46bb-9428-d92cfebe39d4","homepage":"https://jcm.brc.riken.jp/en/","name":"Japan
    Collection of Microorganisms","regex_ccno":"^JCM\\s*\\d+$","regex_id":{"full":"^\\d+$"},"ror":"00s05em53"},"12":{"acr":"NBRC","acr_synonym":["NITE:NBRC"],"active":true,"catalogue":["https://www.nite.go.jp/nbrc/catalogue/NBRCCatalogueDetailServlet?ID=NBRC&CAT={core0:8}"],"code":"NBRC","country":"JP","gbif":"abab42d0-0a95-4166-a0fc-6fe5cd9b66ff","homepage":"https://www.nite.go.jp/en/nbrc/","name":"Biological
    Resource Center","regex_ccno":"^NBRC\\s*\\d+$","regex_id":{"full":"^\\d+$"}}},"normalization":{"DSM
    19572":"DSM-19572","ATCC BAA-758":"ATCC-BAA-758","DSM 16960":"DSM-16960","JCM
    12091":"JCM-12091","ATCC 700893":"ATCC-700893","DSM 11879":"DSM-11879","JCM 9820":"JCM-9820","NBRC
    100138":"NBRC-100138","T469":"","SY1":"","K1":""}}'
  snapshot_sha256: d51abac898f8796dbc2c7b127bb4e61a8ada7f4350fdce689cf755d926446061
- evidence_id: lpsn-live
  kind: authority
  reference: https://lpsn.dsmz.de/species/aeropyrum-pernix
  accessed_at: '2026-10-20T04:00:04Z'
  support: supports
  summary: LPSN772925 supports Sako et al.1996, valid ICNP publication and correct-name
    status, with type K1 and four deposits. Both DOIs resolve and PMID8863437 supports
    the original description and JCM9820 type designation. AB008745.2 resolves at
    taxon56636 with strainK1; its title describes rRNA and an intron-encoded homing
    endonuclease, not a new functional assertion in this review.
  locator: Name, publication status, type deposits and accession
  snapshot_sha256: c2d6211baad990b9d3b37b1aa4550f96c788e32b25f5e6ea85ba4efbc7a365e5
- evidence_id: doi-original
  kind: authority
  reference: https://api.crossref.org/works/10.1099/00207713-46-4-1070
  accessed_at: '2026-10-20T04:00:05Z'
  support: supports
  summary: Original description DOI resolves with matching publication identity.
  locator: message DOI,title,published
  snapshot_sha256: 2620d281febd5d64cae3940c60341563fa6d4d2154b89b3cde9cb12355bae10d
- evidence_id: doi-notification
  kind: authority
  reference: https://api.crossref.org/works/10.1099/00207713-47-1-243
  accessed_at: '2026-10-20T04:00:05Z'
  support: supports
  summary: Separately cited notification DOI resolves to the expected list.
  locator: message DOI,title,published
  snapshot_sha256: e3bb0787a8393e38d8fab7606be973148d738e15260f6f1e2f483de682f35a2d
- evidence_id: pubmed-original
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=15023940,8863437&retmode=xml
  accessed_at: '2026-10-20T04:00:11Z'
  support: supports
  summary: Publication identity and explicit type-strain statements inspected; no
    phenotype is inferred.
  locator: PMID8863437
  snapshot_sha256: a7088089ad63440e06dec0f84af8a481cdfcc4e88d3b979c966995ac1e6ca1ee
- evidence_id: nucleotide-authority
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&id=AB109559,AB245529,AB008745&retmode=json
  accessed_at: '2026-10-20T04:00:12Z'
  support: supports
  summary: Accession metadata supports source name, strain and taxon context without
    silently upgrading unversioned assertions or inferring gene function.
  locator: AB008745.2 taxon56636 strainK1
  snapshot_sha256: c538d9149d33eb2a0cb15b2865be8f1a2fdd523030338b308d4ba18bcbdc067b
- evidence_id: adapter-page-1
  kind: authority
  reference: https://imodulondb.org/
  accessed_at: '2026-10-20T04:03:08Z'
  support: context_only
  summary: 'Inspected bounded fallback source: legacy organism headings have no Aeropyrum;
    modern landing page does not establish complete dataset coverage. No absence of
    a biological function or transcriptomic effect is inferred.'
  locator: Captured landing page; no resolved matching organism/dataset/component
  snapshot_sha256: 372db3e7392f2779f2d46aef5c4f7786399705355520de485f6c37ee92bf0478
- evidence_id: adapter-page-2
  kind: authority
  reference: https://legacy.imodulondb.org/
  accessed_at: '2026-10-20T04:03:08Z'
  support: context_only
  summary: 'Inspected bounded fallback source: legacy organism headings have no Aeropyrum;
    modern landing page does not establish complete dataset coverage. No absence of
    a biological function or transcriptomic effect is inferred.'
  locator: Captured landing page; no resolved matching organism/dataset/component
  snapshot_sha256: 64c45780e351937a5030ad5b67a83ac60dcf559f121425afdd2e4b7cb1c623d3
- evidence_id: adapter-resolution
  kind: search
  reference: kg-microbe-sources runner resolution
  accessed_at: '2026-10-20T04:02:21Z'
  support: partial
  summary: Installed runner absent and no runner resolved in explicitly checked candidate
    locations; optional expression context remains unavailable.
  locator: '{"accessed_at":"2026-10-20T04:02:21.239865+00:00","console_runner":null,"bounded_project_search":{"/Users/marcin/Documents/VIMSS/ontology/Mechs/claw":{"exists":false},"/Users/marcin/Documents/VIMSS/ontology/Mechs/culturebotai-claw":{"exists":false},"/Users/marcin/Documents/VIMSS/ontology/Mechs/wizard-claw":{"exists":false}},"scope":"Installed
    PATH lookup and gitignore-independent checks of the three explicit candidate locations
    only; not a worldwide availability claim."}'
  snapshot_sha256: 244f5ef59a5e5f37fde0d0f6704de9d9f8320833c906e1aad4e57389fb17dd12
  search_scope: Installed PATH lookup and gitignore-independent checks of the three
    explicit candidate locations only; not a worldwide availability claim.
- evidence_id: historical-edge-1
  kind: search
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T07:30:21Z'
  support: partial
  summary: Earlier actual check found configured source bytes differing from the manifest-pinned
    historical input; this is not a new or worldwide search.
  locator: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/mediadive/edges.tsv;
    expected=78ea275a59d4e2de09a9cf72652ec64454c6a111d2defa1ae0a44bac8a72e523; observed=4e933d1e2412fb1aad74e60719a6a64dfa34862ff0a6b84e93d78da5ce13dd8b
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
  search_scope: Exact configured historical input paths including ignored files; bounded
    retained receipt.
- evidence_id: historical-edge-2
  kind: search
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T07:30:22Z'
  support: partial
  summary: Earlier actual check found configured source bytes differing from the manifest-pinned
    historical input; this is not a new or worldwide search.
  locator: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/gold/edges.tsv;
    expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12; observed=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
  search_scope: Exact configured historical input paths including ignored files; bounded
    retained receipt.
- evidence_id: historical-edge-3
  kind: search
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T07:30:22Z'
  support: partial
  summary: Earlier actual check found configured source bytes differing from the manifest-pinned
    historical input; this is not a new or worldwide search.
  locator: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv;
    expected=3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f; observed=c19bfc848e1b410548614c54a2b99e2c58452d58aeb61f972c99fcb3039a1d24
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
  search_scope: Exact configured historical input paths including ignored files; bounded
    retained receipt.
- evidence_id: qc-setup-receipt
  kind: validation
  reference: just qc
  accessed_at: '2026-10-19T07:17:01Z'
  support: context_only
  summary: Initial actual invocation from /private/tmp/taxonmech-record-reviews-k0MubV/repo
    exited 1 because ruff was absent. Locked ruff 0.16.7 was installed only in that
    isolated environment before the complete retry. Reused actual native validation
    on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded
    cwd and timestamps identify the original execution. These native corpus/source
    inputs are unchanged; only new review files differ. This receipt is not a new
    run on the batch branch and does not validate subsequently saved review bundles.
  locator: initial setup attempt, 2026-10-19T07:17:01Z through 2026-10-19T07:17:01Z
  snapshot_sha256: 1d189beecc64b369096499a7ce4adf71897235e4c1190c69e7d0ed3a77b6a3f9
- evidence_id: strict-receipt
  kind: validation
  reference: just validate-strict data/taxa/archaea/aeropyrum_pernix.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0007/strict-08.tsv
  accessed_at: '2026-10-20T03:58:15Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0007/repo;\
    \ started 2026-10-20T03:58:14Z, finished 2026-10-20T03:58:15Z, exit 0. This exact\
    \ generated YAML only; its captured bytes remain unchanged. Actual earlier per-target\
    \ invocation; the receipt retains its original cwd and times.\nValidating 1 files\
    \ with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0003/src/taxonmech/schema/taxonmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0007/strict-08.tsv"
  locator: This exact generated YAML only; its captured bytes remain unchanged. Actual
    earlier per-target invocation; the receipt retains its original cwd and times.
  snapshot_sha256: 08199dea2ae9680423c11baa77a82053ee0c9cb50f665ebf842167f36854c950
- evidence_id: history-receipt
  kind: validation
  reference: just validate-history
  accessed_at: '2026-10-19T07:17:03Z'
  support: supports
  summary: 'Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo;
    started 2026-10-19T07:17:01Z, finished 2026-10-19T07:17:03Z, exit 0. All 17 standalone
    history records; the generated seed event was also inspected in this target. Reused
    actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765;
    the recorded cwd and timestamps identify the original execution. These native
    corpus/source inputs are unchanged; only new review files differ. This receipt
    is not a new run on the batch branch and does not validate subsequently saved
    review bundles.

    history links: 17 record(s), 0 invalid

    No issues found

    17 history record(s) valid against src/taxonmech/schema/history.yaml'
  locator: All 17 standalone history records; the generated seed event was also inspected
    in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765;
    the recorded cwd and timestamps identify the original execution. These native
    corpus/source inputs are unchanged; only new review files differ. This receipt
    is not a new run on the batch branch and does not validate subsequently saved
    review bundles.
  snapshot_sha256: 3fc63ae7bb58034c180e5dcebec02f98c487038ba74793b9f43462ddaacdcbf4
- evidence_id: corpus-receipt
  kind: validation
  reference: just verify-corpus
  accessed_at: '2026-10-19T07:24:12Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo;\
    \ started 2026-10-19T07:18:23Z, finished 2026-10-19T07:24:12Z, exit 0. All 625,960\
    \ generated taxon YAMLs, not a focused approximation. Reused actual native validation\
    \ on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded\
    \ cwd and timestamps identify the original execution. These native corpus/source\
    \ inputs are unchanged; only new review files differ. This receipt is not a new\
    \ run on the batch branch and does not validate subsequently saved review bundles.\n\
    uv run python scripts/verify_corpus.py \nexpected 625960 records, found 625960\
    \ on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces\
    \ exactly from data/raw/ and curation/seed_scope.tsv"
  locator: All 625,960 generated taxon YAMLs, not a focused approximation. Reused
    actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765;
    the recorded cwd and timestamps identify the original execution. These native
    corpus/source inputs are unchanged; only new review files differ. This receipt
    is not a new run on the batch branch and does not validate subsequently saved
    review bundles.
  snapshot_sha256: 6bcd0e5b423155259cb8f8dbecb3e4af467b5dba232906734156e9a99fb5a459
- evidence_id: products-receipt
  kind: validation
  reference: just validate-products
  accessed_at: '2026-10-19T07:55:11Z'
  support: supports
  summary: 'Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo;
    started 2026-10-19T07:17:01Z, finished 2026-10-19T07:55:11Z, exit 0. Full configured
    corpus scan for curator-added graph nodes; this target contains no causal graph.
    Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765;
    the recorded cwd and timestamps identify the original execution. These native
    corpus/source inputs are unchanged; only new review files differ. This receipt
    is not a new run on the batch branch and does not validate subsequently saved
    review bundles.

    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml


    id↔label correspondence summary:


    ✅ All id↔label pairs correspond.'
  locator: Full configured corpus scan for curator-added graph nodes; this target
    contains no causal graph. Reused actual native validation on the unchanged shared
    base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps
    identify the original execution. These native corpus/source inputs are unchanged;
    only new review files differ. This receipt is not a new run on the batch branch
    and does not validate subsequently saved review bundles.
  snapshot_sha256: 48dd07515706dc62199fc2205c4b0bfdd5750028037d9b800179f254d2f1eb07
- evidence_id: qc-receipt
  kind: validation
  reference: just qc
  accessed_at: '2026-10-19T08:07:39Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo;\
    \ started 2026-10-19T07:17:41Z, finished 2026-10-19T08:07:39Z, exit 0. Repository-wide\
    \ just qc, including native corpus-wide checks. Reused actual native validation\
    \ on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded\
    \ cwd and timestamps identify the original execution. These native corpus/source\
    \ inputs are unchanged; only new review files differ. This receipt is not a new\
    \ run on the batch branch and does not validate subsequently saved review bundles.\n\
    1055 passed, 3 skipped, 5 deselected in 1634.00s (0:27:13)\nValidating 625960\
    \ files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml\n\
    \  files scanned:      625960\nexpected 625960 records, found 625960 on disk\n\
    pages/ is current\nSite publication: 530,864,122 bytes (budget 950,000,000)\n\
    625960 taxon records\n  NCBITAXON        625960\nAll TaxonMech quality gates passed.\n\
    \  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890\
    \ strains (not genome counts)\n  Related STRAININFO_DEPOSIT: 107277 strain-record\
    \ pairs, 106843 identifiers, 53890 strains (not genome counts)\n  Related NUCLEOTIDE_SEQUENCE:\
    \ 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)\n\
    LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809\
    \ records mapped, 324404579 genomes summed across record attestations (not deduplicated)\n\
    Causal graphs: 0 records (0 evidence-backed edges)\n\nAll TaxonMech quality gates\
    \ passed."
  locator: Repository-wide just qc, including native corpus-wide checks. Reused actual
    native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765;
    the recorded cwd and timestamps identify the original execution. These native
    corpus/source inputs are unchanged; only new review files differ. This receipt
    is not a new run on the batch branch and does not validate subsequently saved
    review bundles.
  snapshot_sha256: b86a9cc6f529c3b822140f60179e9bc4046e2e6abef3ee0e67fa1035ffb1a76d
assessments:
- assessment_id: identity
  area: identity
  topic: Exact taxon and source lineage
  outcome: supported
  summary: NCBITaxon:56636 denotes Aeropyrum pernix, rank SPECIES, parent NCBITaxon:56635,
    genetic code11. All 9 carried ancestors, literal labels and ranks agree with pinned
    NCBI and current EFetch.
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - scope-row
  - path-row
- assessment_id: nomenclature
  area: nomenclature
  topic: Name classes and nomenclatural scope
  outcome: supported
  summary: LPSN772925 supports Sako et al.1996, valid ICNP publication and correct-name
    status, with type K1 and four deposits. Both DOIs resolve and PMID8863437 supports
    the original description and JCM9820 type designation. AB008745.2 resolves at
    taxon56636 with strainK1; its title describes rRNA and an intron-encoded homing
    endonuclease, not a new functional assertion in this review.
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - lpsn-inventory
  - mapping-policy
  - lpsn-live
  - doi-original
  - doi-notification
  - pubmed-original
  - nucleotide-authority
- assessment_id: completeness
  area: completeness
  topic: Imported subtree and source assertion units
  outcome: supported
  summary: The one species-filed BacDive strain is retained even though some genome
    objects refer to child272557. Direct-species historical MediaDive2, GOLD3 and
    Madin6 units are not descendant sums. Source projects and samples remain narrow
    contextual links; optional expression-module coverage is not established.
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - record
  - taxonomy-inventory
  - bacdive-inventory
  - culture-inventory
  - gtdb-species
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
  - genome-catalog-1
  - genome-catalog-2
  - genome-catalog-3
  - strain-table-1
  - strain-table-2
  - strain-table-3
  - strain-table-4
  - strain-table-5
  - strain-table-6
  - strain-table-7
  - strain-primary-1
  - strain-primary-2
  - strain-primary-3
  - strain-primary-4
  - strain-primary-5
  - gold-project-discovery
  - cafi-registry
  - adapter-page-1
  - adapter-page-2
  - lpsn-live
  - doi-original
  - doi-notification
  - pubmed-original
  - nucleotide-authority
- assessment_id: taxonomy-mapping
  area: grounding
  topic: Qualified species mapping and target scope
  outcome: supported
  summary: The same-taxon LPSN bridge supports the GTDB:s__Aeropyrum_pernix closeMatch,
    xref and count2. Primary membership comprises K1 taxon272557 and YK1-12-2013 taxon56636.
    Source species count2 is retained separately from the single imported BacDive
    strain.
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - record
  - gtdb-mappings
  - gtdb-species
  - mapping-policy
  - equivalence-contract
  - seed-owner
  - genome-catalog-1
  - genome-catalog-2
  - genome-catalog-3
  - gtdb-full-scan
- assessment_id: strain-assertions
  area: evidence
  topic: Strain, deposit and genome-source links
  outcome: supported
  summary: 'BacDive4195 is explicitly filed at species56636, with K1 and ATCC700893/DSM11879/JCM9820/NBRC100138.
    Same-species LPSN deposits support the derived type flag. StrainInfo44195.3 supports
    four distinct deposits118657/118658/118659/335948 and no sequence list. GOLD Go0000767
    ATCC700893 links to four projects: Gp0000767, Gp0102910, Gp0225950 and Gp0225951.
    Only Gp0000767 is linked in the inspected analyses to Ga0039428/GCA_000011125.1/IMG2923402010;
    the two named transcriptome projects retain their own samples and are not treated
    as genome analyses. Full discovery finds no project for Go0624942 JCM or Go0624943
    DSM. BV272557.25 supplies the explicit BacDive-associated genome; BV272557.33
    explicitly matches NBRC:100138 and has no assembly_accession field, so the absent
    BV assembly assertion is supported. Bare K1 fails culture-key normalization. The2
    assembly,4 genome and28 related assertions exactly match the imported multiset.'
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - record
  - strain-table-1
  - strain-table-2
  - strain-table-3
  - strain-table-4
  - strain-table-5
  - strain-table-6
  - strain-table-7
  - strain-primary-1
  - strain-primary-2
  - strain-primary-3
  - strain-primary-4
  - strain-primary-5
  - gold-project-discovery
  - cafi-registry
  - adapter-page-1
  - adapter-page-2
  - lpsn-live
  - doi-original
  - doi-notification
  - pubmed-original
  - nucleotide-authority
  - genome-catalog-1
  - genome-catalog-2
  - genome-catalog-3
- assessment_id: native-status
  area: provenance
  topic: Unchanged native status and history
  outcome: supported
  summary: Grounding EXACT, mapping SEEDED and the sole 2026-09-13T17:54:04Z seed
    event remain unchanged and agree with the latest extraction time. No curation
    history or native status is promoted.
  target_ids:
  - NCBITaxon:56636
  evidence_ids:
  - record
  - manifest
  - overlay-manifests
findings: []
actions:
- action_id: recover-pinned-aggregate-inputs
  finding_ids: []
  target_ids:
  - NCBITaxon:56636
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
- The review is bounded to captured sources and versions. Names alone do not establish
  deposit identity, genome equivalence, phenotype or mechanism; source taxonomy disagreements
  are preserved.
- Original manifest-hash-matching historical aggregate edges were unavailable in the
  retained configured-path checks; pinned projection counts agree, but independent
  historical recounting remains unresolved.
- Optional iModulonDB adapter context unavailable in bounded runner checks. Legacy
  site and search fallback did not establish matching Aeropyrum coverage; the modern
  landing page does not prove exhaustive absence.
- Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765;
  the recorded cwd and timestamps identify the original execution. These native corpus/source
  inputs are unchanged; only new review files differ. This receipt is not a new run
  on the batch branch and does not validate subsequently saved review bundles.
notes:
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base canonical recapture preserved all previously reviewed input hashes; original
  captures and actual transition receipts remain retained.
- Every new bundle still requires its own validate/save/check recipe; baseline native
  receipts do not claim these later steps have run.
tags:
- record-review
- batch-0007
- archaea
- generated
- source-checked
```
