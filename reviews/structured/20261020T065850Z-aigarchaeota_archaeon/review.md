# Record review: Aigarchaeota archaeon

- Review: 20261020T065850Z-aigarchaeota_archaeon
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-20T04:07:18Z
- Finished UTC: 2026-10-20T06:58:50Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Aigarchaeota archaeon has supported NCBI identity and source projection within the checked inputs.

## Scope And Provenance

Entire single generated record, including all source assertions and imported strains.

Selection: Original unreviewed path-order position 73; batch-0008 target 3. Excluded 122 actual targets from validated main and local batch-0001/0002/0003/0004/0005/0006/0007 listings; full corpus enumeration includes ignored files.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9b5a8fff5185b38dc5c77bb35235152c81ea7765.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:2528703 | data/taxa/archaea/aigarchaeota_archaeon.yaml | generated | Aigarchaeota archaeon |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact NCBI taxon, rank and lineage | passed | True | NCBITaxon:2528703 | NCBITaxon:2528703 denotes Aigarchaeota archaeon at SPECIES rank, parent NCBITaxon:1104572, genetic code 11. All 6 ancestors agree in identifier, literal name and rank with pinned NCBI and current EFetch. |
| Complete exact identifier and name inventory search | passed | True | NCBITaxon:2528703 | NCBI1 NAME, GTDB3 GENOME and GOLD4 ORGANISM agree with pinned projection tables. Zero imported strains and absence of pinned descendants are supported. The historical GOLD aggregate needs separate provenance assessment; newer primary organism objects cannot substitute silently. |
| Complete primary GTDB cluster membership | passed | True | NCBITaxon:2528703 | All five broad mappings are supported by full GTDB shard scans: Geocrenenecus sp0250585153, Wolframiiraptor sp0250594153, Benthortus lauensis2, JANXDH01 sp0250597452 and Terraquivivens sp0250592052. Each contains target2528703 and at least one other NCBI taxon, supporting every other-taxa clause. No exact synonyms or equivalent xrefs are emitted. The primary attestation counts3 and references four further clusters rather than summing12. |
| Imported strain links | not_applicable | False | NCBITaxon:2528703 | No imported BacDive strain or strain-level link asserted; absence is bounded to the pinned inventories. |
| Original manifest-pinned GOLD aggregate | unavailable | True | NCBITaxon:2528703 | Pinned count4 ORGANISM agrees, but original historical input was unavailable in retained hash check. |
| Initial quality-gate setup attempt | failed | False | NCBITaxon:2528703 | Actual exit 1: missing ruff; superseded by the separately recorded successful full retry. |
| Native strict record validation | passed | True | NCBITaxon:2528703 | Actual terminal exit code 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. |
| Repository history validation | passed | True | NCBITaxon:2528703 | Actual terminal exit code 0. All 17 standalone history records; the generated seed event was also inspected in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| Full-corpus exact reproduction | passed | True | NCBITaxon:2528703 | Actual terminal exit code 0. All 625,960 generated taxon YAMLs, not a focused approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| Native product ID/label gate | passed | True | NCBITaxon:2528703 | Actual terminal exit code 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| Authoritative complete quality gate | passed | True | NCBITaxon:2528703 | Actual terminal exit code 0. Repository-wide just qc, including native corpus-wide checks. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. Pytest reported 1055 passed, 3 skipped and 5 deselected; the native QC recipe completed successfully. |

## Scientific And Domain Assessments

### Exact taxon and source lineage

identity: supported. Targets: NCBITaxon:2528703.

NCBITaxon:2528703 denotes Aigarchaeota archaeon at SPECIES rank, parent NCBITaxon:1104572, genetic code 11. All 6 ancestors agree in identifier, literal name and rank with pinned NCBI and current EFetch.

### Name classes and nomenclatural scope

nomenclature: supported. Targets: NCBITaxon:2528703.

The generic species-rank placeholder has no NCBI synonym or same-taxon LPSN assertion. No individual cultured organism identity is inferred.

### Imported subtree and source assertion units

completeness: supported. Targets: NCBITaxon:2528703.

NCBI1 NAME, GTDB3 GENOME and GOLD4 ORGANISM agree with pinned projection tables. Zero imported strains and absence of pinned descendants are supported. The historical GOLD aggregate needs separate provenance assessment; newer primary organism objects cannot substitute silently.

### Qualified species mapping and target scope

grounding: supported. Targets: NCBITaxon:2528703.

All five broad mappings are supported by full GTDB shard scans: Geocrenenecus sp0250585153, Wolframiiraptor sp0250594153, Benthortus lauensis2, JANXDH01 sp0250597452 and Terraquivivens sp0250592052. Each contains target2528703 and at least one other NCBI taxon, supporting every other-taxa clause. No exact synonyms or equivalent xrefs are emitted. The primary attestation counts3 and references four further clusters rather than summing12.

### Unchanged native status and history

provenance: supported. Targets: NCBITaxon:2528703.

EXACT grounding and SEEDED mapping remain supported; the sole seed event agrees with the manifest extraction time. No native status or history is changed.

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
| record | data/taxa/archaea/aigarchaeota_archaeon.yaml; entire TaxonRecord; identifier=NCBITaxon:2528703 | supports | Read the entire generated YAML, including identity, lineage, names, mappings, source attestations, all imported strains and links, and seed history. |
| taxonomy-inventory | data/raw/ncbitaxon_taxa.tsv; line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""}; line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"}; line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"}; line 150593: {"taxon_id":"NCBITaxon:651137","label":"Nitrososphaerota","rank":"PHYLUM","parent_id":"NCBITaxon:1783275"}; line 236905: {"taxon_id":"NCBITaxon:1104572","label":"unclassified Nitrososphaerota","rank":"NO_RANK","parent_id":"NCBITaxon:651137"}; line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"}; line 529457: {"taxon_id":"NCBITaxon:2528703","label":"Aigarchaeota archaeon","rank":"SPECIES","parent_id":"NCBITaxon:1104572","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb&#124;gold","retired_into":"","taxonomy_snapshot":"2026-09-13"} | supports | Inspected the target and each carried ancestor, rank, parent, genetic code and source name classes. |
| scope-row | curation/seed_scope.tsv; line 62766: {"identifier":"NCBITaxon:2528703","added":"2026-09-12","reason":"attested rule: Aigarchaeota archaeon, 2 sources incl. NCBI"} | supports | Exact target is included in the declared seed scope. |
| path-row | data/taxa/PATHS.tsv; line 348670: {"identifier":"NCBITaxon:2528703","slug":"aigarchaeota_archaeon"} | supports | Indexed path resolves to this exact NCBI taxon. |
| ncbi-live | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=568409,3138747,2528703,1052838,1052839,1052841,1052823,1052825,1052826,1052828; TaxaSet/Taxon[TaxId='2528703']; ten-target captured response | supports | Inspected the official response for this exact taxon: scientific name, rank, parent, source name classes, lineage and genetic code. Current authority and pinned September inventory remain distinct observations. |
| lpsn-inventory | data/raw/lpsn_names.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected exact mapped and linked LPSN names; bounded inventory absence does not establish worldwide nomenclatural absence. |
| gtdb-mappings | data/raw/gtdb_mappings.tsv; line 138221: {"gtdb_id":"GTDB:s__Geocrenenecus_sp025058515","gtdb_label":"s__Geocrenenecus_sp025058515","gtdb_parent":"GTDB:g__Geocrenenecus","ncbitaxon_id":"NCBITaxon:2026795","predicate":"skos:broadMatch","genome_count":"3"}; line 138249: {"gtdb_id":"GTDB:s__JANXDH01_sp025059745","gtdb_label":"s__JANXDH01_sp025059745","gtdb_parent":"GTDB:g__JANXDH01","ncbitaxon_id":"NCBITaxon:2026795","predicate":"skos:broadMatch","genome_count":"2"}; line 138326: {"gtdb_id":"GTDB:s__Terraquivivens_sp025059205","gtdb_label":"s__Terraquivivens_sp025059205","gtdb_parent":"GTDB:g__Terraquivivens","ncbitaxon_id":"NCBITaxon:2026795","predicate":"skos:broadMatch","genome_count":"2"}; line 138370: {"gtdb_id":"GTDB:s__Wolframiiraptor_sp025059415","gtdb_label":"s__Wolframiiraptor_sp025059415","gtdb_parent":"GTDB:g__Wolframiiraptor","ncbitaxon_id":"NCBITaxon:2026795","predicate":"skos:broadMatch","genome_count":"3"}; line 179372: {"gtdb_id":"GTDB:s__Geocrenenecus_sp025058515","gtdb_label":"s__Geocrenenecus_sp025058515","gtdb_parent":"GTDB:g__Geocrenenecus","ncbitaxon_id":"NCBITaxon:2268198","predicate":"skos:broadMatch","genome_count":"3"}; line 179402: {"gtdb_id":"GTDB:s__Wolframiiraptor_sp025059415","gtdb_label":"s__Wolframiiraptor_sp025059415","gtdb_parent":"GTDB:g__Wolframiiraptor","ncbitaxon_id":"NCBITaxon:2268198","predicate":"skos:broadMatch","genome_count":"3"}; line 197396: {"gtdb_id":"GTDB:s__Benthortus_lauensis","gtdb_label":"s__Benthortus_lauensis","gtdb_parent":"GTDB:g__Benthortus","ncbitaxon_id":"NCBITaxon:2528703","predicate":"skos:broadMatch","genome_count":"2"}; line 197397: {"gtdb_id":"GTDB:s__Geocrenenecus_sp025058515","gtdb_label":"s__Geocrenenecus_sp025058515","gtdb_parent":"GTDB:g__Geocrenenecus","ncbitaxon_id":"NCBITaxon:2528703","predicate":"skos:broadMatch","genome_count":"3"}; line 197398: {"gtdb_id":"GTDB:s__JANXDH01_sp025059745","gtdb_label":"s__JANXDH01_sp025059745","gtdb_parent":"GTDB:g__JANXDH01","ncbitaxon_id":"NCBITaxon:2528703","predicate":"skos:broadMatch","genome_count":"2"}; line 197399: {"gtdb_id":"GTDB:s__Terraquivivens_sp025059205","gtdb_label":"s__Terraquivivens_sp025059205","gtdb_parent":"GTDB:g__Terraquivivens","ncbitaxon_id":"NCBITaxon:2528703","predicate":"skos:broadMatch","genome_count":"2"}; line 197400: {"gtdb_id":"GTDB:s__Wolframiiraptor_sp025059415","gtdb_label":"s__Wolframiiraptor_sp025059415","gtdb_parent":"GTDB:g__Wolframiiraptor","ncbitaxon_id":"NCBITaxon:2528703","predicate":"skos:broadMatch","genome_count":"3"}; line 242188: {"gtdb_id":"GTDB:s__Benthortus_lauensis","gtdb_label":"s__Benthortus_lauensis","gtdb_parent":"GTDB:g__Benthortus","ncbitaxon_id":"NCBITaxon:2973087","predicate":"skos:closeMatch","genome_count":"2"} | supports | Inspected direct mappings and selected clusters' reverse mappings, retaining each source predicate and taxon boundary. |
| gtdb-species | data/raw/gtdb_species.tsv; line 17093: {"gtdb_id":"GTDB:s__Benthortus_lauensis","label":"s__Benthortus_lauensis","parent":"GTDB:g__Benthortus","genome_count":"2"}; line 69863: {"gtdb_id":"GTDB:s__Geocrenenecus_sp025058515","label":"s__Geocrenenecus_sp025058515","parent":"GTDB:g__Geocrenenecus","genome_count":"3"}; line 97236: {"gtdb_id":"GTDB:s__JANXDH01_sp025059745","label":"s__JANXDH01_sp025059745","parent":"GTDB:g__JANXDH01","genome_count":"2"}; line 175377: {"gtdb_id":"GTDB:s__Terraquivivens_sp025059205","label":"s__Terraquivivens_sp025059205","parent":"GTDB:g__Terraquivivens","genome_count":"2"}; line 198640: {"gtdb_id":"GTDB:s__Wolframiiraptor_sp025059415","label":"s__Wolframiiraptor_sp025059415","parent":"GTDB:g__Wolframiiraptor","genome_count":"3"} | supports | Inspected source species identifiers, labels, parent clusters and genome counts. |
| bacdive-inventory | data/raw/bacdive_strains.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Complete inventory selection covers the exact target and descendants from the complete NCBI parent graph; its imported strain population was compared with the complete YAML. |
| culture-inventory | data/raw/culture_collection_strains.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected exact culture-inventory associations; an isolate name or genome does not create an inferred deposit. |
| gold-organisms | data/raw/gold_organisms.tsv; line 23035: {"taxon_id":"NCBITaxon:2528703","organism_count":"4"} | supports | Inspected the exact GOLD organism count row or bounded absence, without converting counts to phenotypes. |
| mediadive-taxa | data/raw/mediadive_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact MediaDive medium count row or bounded absence, without converting counts to phenotypes. |
| madin-taxa | data/raw/madin_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact Madin trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| bactotraits-taxa | data/raw/bactotraits_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact BactoTraits trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| mapping-policy | docs/HARMONIZATION.md; Mapping predicates; Which strains belong to a record | supports | Policy permits one-to-one species closeMatch normalization and LPSN-linked species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage unchanged. |
| equivalence-contract | src/taxonmech/schema/taxonmech.yaml; TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439 | supports | TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes under the source taxon. |
| seed-owner | src/taxonmech/seed.py; GTDB mapping construction lines 440–472; LPSN/type-strain and source-attestation construction | supports | Inspected mapping ranking, qualified predicates, fixed broadMatch wording, synonym/xref construction, primary cluster counts and same-taxon type-strain derivation. |
| manifest | data/raw/MANIFEST.yaml; kg_microbe_source, inputs, extracted_at | supports | Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd, upstream input hashes and extraction time 2026-09-13T17:50:44Z. |
| overlay-manifests | data/atb/MANIFEST.yaml; extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml | supports | Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z, matching the sole seed event. StrainInfo manifest is independently captured in source.inputs. |
| genome-catalog-1 | data/catalog/gtdb_genomes-0017.jsonl.gz; line 30182: {"accession":"GB_GCA_026413895.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Wolframiiraptor;s__Wolframiiraptor sp025059415","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM2641389v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJEB4990","ncbi_biosample":"SAMN30305265","ncbi_contig_count":"55","ncbi_contig_n50":"39926","ncbi_country":"Malaysia: Sungkai; Perak","ncbi_date":"2022-11-27","ncbi_genbank_assembly_accession":"GCA_026413895.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKW304","ncbi_isolation_source":"alkaline hot spring water","ncbi_lat_lon":"3.9966 N 101.3931 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Nitrososphaeria archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"48","ncbi_scaffold_l50":"8","ncbi_scaffold_n50":"39926","ncbi_scaffold_n75":"22100","ncbi_scaffold_n90":"13717","ncbi_seq_rel_date":"2022-11-27","ncbi_spanned_gaps":"7","ncbi_species_taxid":"2268198","ncbi_ssu_count":"1","ncbi_strain_identifiers":"SKW304","ncbi_submitter":"Universiti Teknologi Malaysia - Malaysia","ncbi_taxid":"2268198","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__Nitrososphaeria;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;c__Nitrososphaeria;x__unclassified Nitrososphaeria;s__Nitrososphaeria archaeon","ncbi_total_gap_length":"338","ncbi_total_length":"1008461","ncbi_translation_table":"11","ncbi_trna_count":"37","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1008123","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAOAKC000000000.1"}; line 31321: {"accession":"GB_GCA_026413845.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Geocrenenecus;s__Geocrenenecus sp025058515","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM2641384v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJEB4990","ncbi_biosample":"SAMN30305268","ncbi_contig_count":"60","ncbi_contig_n50":"96656","ncbi_country":"Malaysia: Sungkai; Perak","ncbi_date":"2022-11-27","ncbi_genbank_assembly_accession":"GCA_026413845.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKW312","ncbi_isolation_source":"alkaline hot spring water","ncbi_lat_lon":"3.9966 N 101.3931 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Nitrososphaeria archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"4","ncbi_scaffold_count":"56","ncbi_scaffold_l50":"5","ncbi_scaffold_n50":"96656","ncbi_scaffold_n75":"85111","ncbi_scaffold_n90":"34113","ncbi_seq_rel_date":"2022-11-27","ncbi_spanned_gaps":"4","ncbi_species_taxid":"2268198","ncbi_ssu_count":"1","ncbi_strain_identifiers":"SKW312","ncbi_submitter":"Universiti Teknologi Malaysia - Malaysia","ncbi_taxid":"2268198","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__Nitrososphaeria;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;c__Nitrososphaeria;x__unclassified Nitrososphaeria;s__Nitrososphaeria archaeon","ncbi_total_gap_length":"130","ncbi_total_length":"1550754","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1550624","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAOAKF000000000.1"}; line 31969: {"accession":"GB_GCA_025059205.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Terraquivivens;s__Terraquivivens sp025059205","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM2505920v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA761511","ncbi_biosample":"SAMN30304937","ncbi_contig_count":"38","ncbi_contig_n50":"299742","ncbi_country":"Malaysia: Sungkai; Perak","ncbi_date":"2022-09-07","ncbi_genbank_assembly_accession":"GCA_025059205.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYB131","ncbi_isolation_source":"brown biofilm from alkaline hot spring","ncbi_lat_lon":"3.9956 N 101.3933 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Aigarchaeota archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"4","ncbi_scaffold_count":"35","ncbi_scaffold_l50":"2","ncbi_scaffold_n50":"304507","ncbi_scaffold_n75":"72180","ncbi_scaffold_n90":"37787","ncbi_seq_rel_date":"2022-09-07","ncbi_spanned_gaps":"3","ncbi_species_taxid":"2528703","ncbi_ssu_count":"2","ncbi_strain_identifiers":"SKYB131","ncbi_submitter":"Universiti Teknologi Malaysia","ncbi_taxid":"2528703","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified Nitrososphaerota;s__Aigarchaeota archaeon","ncbi_total_gap_length":"179","ncbi_total_length":"1188966","ncbi_translation_table":"11","ncbi_trna_count":"53","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1188787","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JANXDS000000000.1"}; line 33558: {"accession":"GB_GCA_025059745.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Calditenuaceae;g__JANXDH01;s__JANXDH01 sp025059745","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2505974v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA761511","ncbi_biosample":"SAMN30304926","ncbi_contig_count":"6","ncbi_contig_n50":"733637","ncbi_country":"Malaysia: Sungkai; Perak","ncbi_date":"2022-09-07","ncbi_genbank_assembly_accession":"GCA_025059745.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYB10","ncbi_isolation_source":"brown biofilm from alkaline hot spring","ncbi_lat_lon":"3.9956 N 101.3933 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Aigarchaeota archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"4","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2022-09-07","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2528703","ncbi_ssu_count":"2","ncbi_strain_identifiers":"SKYB10","ncbi_submitter":"Universiti Teknologi Malaysia","ncbi_taxid":"2528703","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified Nitrososphaerota;s__Aigarchaeota archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1166430","ncbi_translation_table":"11","ncbi_trna_count":"43","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1166430","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JANXDH000000000.1"}; line 35896: {"accession":"GB_GCA_025058515.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Geocrenenecus;s__Geocrenenecus sp025058515","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2505851v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA761511","ncbi_biosample":"SAMN30304941","ncbi_contig_count":"53","ncbi_contig_n50":"48213","ncbi_country":"Malaysia: Sungkai; Perak","ncbi_date":"2022-09-07","ncbi_genbank_assembly_accession":"GCA_025058515.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYB24","ncbi_isolation_source":"brown biofilm from alkaline hot spring","ncbi_lat_lon":"3.9956 N 101.3933 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Aigarchaeota archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"5","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2022-09-07","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2528703","ncbi_ssu_count":"2","ncbi_strain_identifiers":"SKYB24","ncbi_submitter":"Universiti Teknologi Malaysia","ncbi_taxid":"2528703","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified Nitrososphaerota;s__Aigarchaeota archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1466662","ncbi_translation_table":"11","ncbi_trna_count":"41","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1466662","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JANXDW000000000.1"}; line 37620: {"accession":"GB_GCA_033581775.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Wolframiiraptor;s__Wolframiiraptor sp025059415","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM3358177v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA1012858","ncbi_biosample":"SAMN37334029","ncbi_contig_count":"57","ncbi_contig_n50":"32319","ncbi_country":"none","ncbi_date":"2023-11-13","ncbi_genbank_assembly_accession":"GCA_033581775.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYBB_hs_bin105","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Nitrososphaerota archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"4","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-11-13","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2026795","ncbi_ssu_count":"2","ncbi_strain_identifiers":"SKYBB_hs_bin105","ncbi_submitter":"Universiti Teknologi Malaysia","ncbi_taxid":"2026795","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified Nitrososphaerota;s__Nitrososphaerota archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1048200","ncbi_translation_table":"11","ncbi_trna_count":"34","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1048200","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAVQSO000000000.1"}; line 38067: {"accession":"GB_GCA_021650775.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Benthortus;s__Benthortus lauensis","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2165077v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA495050","ncbi_biosample":"SAMN19948827","ncbi_contig_count":"112","ncbi_contig_n50":"19743","ncbi_country":"Pacific Ocean","ncbi_date":"2022-01-27","ncbi_genbank_assembly_accession":"GCA_021650775.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"T2-175","ncbi_isolation_source":"hydrothermal vent deposit","ncbi_lat_lon":"21.9904 S 176.5692 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Candidatus Benthortus lauensis","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2022-01-27","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2973087","ncbi_ssu_count":"none","ncbi_strain_identifiers":"T2-175","ncbi_submitter":"Portland State University","ncbi_taxid":"2973087","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__Candidatus Wolframiiraptoraceae;g__Candidatus Benthortus;s__Candidatus Benthortus lauensis","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__Nitrososphaerota incertae sedis;f__Candidatus Wolframiiraptoraceae;g__Candidatus Benthortus;s__Candidatus Benthortus lauensis","ncbi_total_gap_length":"0","ncbi_total_length":"1470116","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"assembly from type material","ncbi_ungapped_length":"1470116","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAHSRM000000000.1"}; line 39953: {"accession":"GB_GCA_033582315.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Geocrenenecus;s__Geocrenenecus sp025058515","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM3358231v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA1012858","ncbi_biosample":"SAMN37334009","ncbi_contig_count":"89","ncbi_contig_n50":"91093","ncbi_country":"none","ncbi_date":"2023-11-13","ncbi_genbank_assembly_accession":"GCA_033582315.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYBB_h_bin138","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Nitrososphaerota archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"1","ncbi_scaffold_count":"85","ncbi_scaffold_l50":"5","ncbi_scaffold_n50":"91093","ncbi_scaffold_n75":"49374","ncbi_scaffold_n90":"24444","ncbi_seq_rel_date":"2023-11-13","ncbi_spanned_gaps":"4","ncbi_species_taxid":"2026795","ncbi_ssu_count":"0","ncbi_strain_identifiers":"SKYBB_h_bin138","ncbi_submitter":"Universiti Teknologi Malaysia","ncbi_taxid":"2026795","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified Nitrososphaerota;s__Nitrososphaerota archaeon","ncbi_total_gap_length":"40","ncbi_total_length":"1538472","ncbi_translation_table":"11","ncbi_trna_count":"47","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1538432","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAVQRU000000000.1"}; line 42187: {"accession":"GB_GCA_033581195.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Terraquivivens;s__Terraquivivens sp025059205","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM3358119v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA1012858","ncbi_biosample":"SAMN37334059","ncbi_contig_count":"36","ncbi_contig_n50":"597539","ncbi_country":"none","ncbi_date":"2023-11-13","ncbi_genbank_assembly_accession":"GCA_033581195.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYBB_hs_bin56","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Nitrososphaerota archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"5","ncbi_scaffold_count":"33","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"597539","ncbi_scaffold_n75":"71884","ncbi_scaffold_n90":"40245","ncbi_seq_rel_date":"2023-11-13","ncbi_spanned_gaps":"3","ncbi_species_taxid":"2026795","ncbi_ssu_count":"2","ncbi_strain_identifiers":"SKYBB_hs_bin56","ncbi_submitter":"Universiti Teknologi Malaysia","ncbi_taxid":"2026795","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified Nitrososphaerota;s__Nitrososphaerota archaeon","ncbi_total_gap_length":"30","ncbi_total_length":"1157564","ncbi_translation_table":"11","ncbi_trna_count":"52","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1157534","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAVQTS000000000.1"}; line 43420: {"accession":"GB_GCA_025059415.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Wolframiiraptor;s__Wolframiiraptor sp025059415","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM2505941v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA761511","ncbi_biosample":"SAMN30304935","ncbi_contig_count":"98","ncbi_contig_n50":"19725","ncbi_country":"Malaysia: Sungkai; Perak","ncbi_date":"2022-09-07","ncbi_genbank_assembly_accession":"GCA_025059415.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYB129","ncbi_isolation_source":"brown biofilm from alkaline hot spring","ncbi_lat_lon":"3.9956 N 101.3933 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Aigarchaeota archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"1","ncbi_scaffold_count":"71","ncbi_scaffold_l50":"11","ncbi_scaffold_n50":"24526","ncbi_scaffold_n75":"16458","ncbi_scaffold_n90":"10555","ncbi_seq_rel_date":"2022-09-07","ncbi_spanned_gaps":"27","ncbi_species_taxid":"2528703","ncbi_ssu_count":"0","ncbi_strain_identifiers":"SKYB129","ncbi_submitter":"Universiti Teknologi Malaysia","ncbi_taxid":"2528703","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified Nitrososphaerota;s__Aigarchaeota archaeon","ncbi_total_gap_length":"2650","ncbi_total_length":"985681","ncbi_translation_table":"11","ncbi_trna_count":"42","ncbi_type_material_designation":"na","ncbi_ungapped_length":"983031","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JANXDQ000000000.1"}; line 44283: {"accession":"GB_GCA_015520375.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Benthortus;s__Benthortus lauensis","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM1552037v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA546572","ncbi_biosample":"SAMN12837340","ncbi_contig_count":"144","ncbi_contig_n50":"10284","ncbi_country":"Pacific Ocean","ncbi_date":"2020-11-16","ncbi_genbank_assembly_accession":"GCA_015520375.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"S146_127","ncbi_isolation_source":"deep-sea hydrothermal deposit","ncbi_lat_lon":"34.86208959 S 179.0573881 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Aigarchaeota archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2020-11-16","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2528703","ncbi_ssu_count":"none","ncbi_strain_identifiers":"S146_127","ncbi_submitter":"Portland State University","ncbi_taxid":"2528703","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified Nitrososphaerota;s__Aigarchaeota archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1148221","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1148221","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"WAQD00000000.1"} | supports | Inspected primary cluster membership, exact taxon IDs, assembly versions and isolate labels. Historical source lineages remain distinct from current NCBI classification; no culture deposit or phenotype is inferred. |
| genome-catalog-2 | data/catalog/gtdb_genomes-0018.jsonl.gz; line 1230: {"accession":"GB_GCA_033581295.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Calditenuaceae;g__JANXDH01;s__JANXDH01 sp025059745","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM3358129v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA1012858","ncbi_biosample":"SAMN37334054","ncbi_contig_count":"24","ncbi_contig_n50":"304995","ncbi_country":"none","ncbi_date":"2023-11-13","ncbi_genbank_assembly_accession":"GCA_033581295.1","ncbi_genome_category":"derived from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYBB_hs_bin41","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Nitrososphaerota archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"5","ncbi_scaffold_count":"22","ncbi_scaffold_l50":"2","ncbi_scaffold_n50":"304995","ncbi_scaffold_n75":"282826","ncbi_scaffold_n90":"113951","ncbi_seq_rel_date":"2023-11-13","ncbi_spanned_gaps":"2","ncbi_species_taxid":"2026795","ncbi_ssu_count":"2","ncbi_strain_identifiers":"SKYBB_hs_bin41","ncbi_submitter":"Universiti Teknologi Malaysia","ncbi_taxid":"2026795","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified Nitrososphaerota;s__Nitrososphaerota archaeon","ncbi_total_gap_length":"380","ncbi_total_length":"1248770","ncbi_translation_table":"11","ncbi_trna_count":"55","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1248390","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAVQTN000000000.1"} | supports | Inspected primary cluster membership, exact taxon IDs, assembly versions and isolate labels. Historical source lineages remain distinct from current NCBI classification; no culture deposit or phenotype is inferred. |
| gtdb-full-scan | data/catalog/MANIFEST.json; {"s__Wolframiiraptor sp025059415":[{"accession":"GB_GCA_026413895.1","ncbi_taxid":"2268198","ncbi_species_taxid":"2268198","ncbi_organism_name":"Nitrososphaeria archaeon","ncbi_strain_identifiers":"SKW304","ncbi_genome_category":"derived from metagenome"},{"accession":"GB_GCA_033581775.1","ncbi_taxid":"2026795","ncbi_species_taxid":"2026795","ncbi_organism_name":"Nitrososphaerota archaeon","ncbi_strain_identifiers":"SKYBB_hs_bin105","ncbi_genome_category":"derived from metagenome"},{"accession":"GB_GCA_025059415.1","ncbi_taxid":"2528703","ncbi_species_taxid":"2528703","ncbi_organism_name":"Aigarchaeota archaeon","ncbi_strain_identifiers":"SKYB129","ncbi_genome_category":"derived from metagenome"}],"s__Geocrenenecus sp025058515":[{"accession":"GB_GCA_026413845.1","ncbi_taxid":"2268198","ncbi_species_taxid":"2268198","ncbi_organism_name":"Nitrososphaeria archaeon","ncbi_strain_identifiers":"SKW312","ncbi_genome_category":"derived from metagenome"},{"accession":"GB_GCA_025058515.1","ncbi_taxid":"2528703","ncbi_species_taxid":"2528703","ncbi_organism_name":"Aigarchaeota archaeon","ncbi_strain_identifiers":"SKYB24","ncbi_genome_category":"derived from metagenome"},{"accession":"GB_GCA_033582315.1","ncbi_taxid":"2026795","ncbi_species_taxid":"2026795","ncbi_organism_name":"Nitrososphaerota archaeon","ncbi_strain_identifiers":"SKYBB_h_bin138","ncbi_genome_category":"derived from metagenome"}],"s__Terraquivivens sp025059205":[{"accession":"GB_GCA_025059205.1","ncbi_taxid":"2528703","ncbi_species_taxid":"2528703","ncbi_organism_name":"Aigarchaeota archaeon","ncbi_strain_identifiers":"SKYB131","ncbi_genome_category":"derived from metagenome"},{"accession":"GB_GCA_033581195.1","ncbi_taxid":"2026795","ncbi_species_taxid":"2026795","ncbi_organism_name":"Nitrososphaerota archaeon","ncbi_strain_identifiers":"SKYBB_hs_bin56","ncbi_genome_category":"derived from metagenome"}],"s__JANXDH01 sp025059745":[{"accession":"GB_GCA_025059745.1","ncbi_taxid":"2528703","ncbi_species_taxid":"2528703","ncbi_organism_name":"Aigarchaeota archaeon","ncbi_strain_identifiers":"SKYB10","ncbi_genome_category":"derived from metagenome"},{"accession":"GB_GCA_033581295.1","ncbi_taxid":"2026795","ncbi_species_taxid":"2026795","ncbi_organism_name":"Nitrososphaerota archaeon","ncbi_strain_identifiers":"SKYBB_hs_bin41","ncbi_genome_category":"derived from metagenome"}],"s__Benthortus lauensis":[{"accession":"GB_GCA_021650775.1","ncbi_taxid":"2973087","ncbi_species_taxid":"2973087","ncbi_organism_name":"Candidatus Benthortus lauensis","ncbi_strain_identifiers":"T2-175","ncbi_genome_category":"derived from metagenome"},{"accession":"GB_GCA_015520375.1","ncbi_taxid":"2528703","ncbi_species_taxid":"2528703","ncbi_organism_name":"Aigarchaeota archaeon","ncbi_strain_identifiers":"S146_127","ncbi_genome_category":"derived from metagenome"}]} | supports | All nineteen GTDB shards searched for exact terminal species tokens; counts and taxon membership inspected. |
| historical-gold-edge | data/raw/MANIFEST.yaml; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/gold/edges.tsv; expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12; observed=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d | partial | Earlier actual configured-path check found source bytes differing from the manifest-pinned GOLD input. This retained observation does not establish worldwide absence. |
| qc-setup-receipt | just qc; initial setup attempt, 2026-10-19T07:17:01Z through 2026-10-19T07:17:01Z | context_only | Initial actual invocation from /private/tmp/taxonmech-record-reviews-k0MubV/repo exited 1 because ruff was absent. Locked ruff 0.16.7 was installed only in that isolated environment before the complete retry. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| strict-receipt | just validate-strict data/taxa/archaea/aigarchaeota_archaeon.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0008/strict-03.tsv; This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0008/repo; started 2026-10-20T04:07:23Z, finished 2026-10-20T04:07:24Z, exit 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times.<br>Validating 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0003/src/taxonmech/schema/taxonmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0008/strict-03.tsv |
| history-receipt | just validate-history; All 17 standalone history records; the generated seed event was also inspected in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:01Z, finished 2026-10-19T07:17:03Z, exit 0. All 17 standalone history records; the generated seed event was also inspected in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>history links: 17 record(s), 0 invalid<br>No issues found<br>17 history record(s) valid against src/taxonmech/schema/history.yaml |
| corpus-receipt | just verify-corpus; All 625,960 generated taxon YAMLs, not a focused approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:18:23Z, finished 2026-10-19T07:24:12Z, exit 0. All 625,960 generated taxon YAMLs, not a focused approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>uv run python scripts/verify_corpus.py <br>expected 625960 records, found 625960 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ and curation/seed_scope.tsv |
| products-receipt | just validate-products; Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:01Z, finished 2026-10-19T07:55:11Z, exit 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml<br><br>id↔label correspondence summary:<br><br>✅ All id↔label pairs correspond. |
| qc-receipt | just qc; Repository-wide just qc, including native corpus-wide checks. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:41Z, finished 2026-10-19T08:07:39Z, exit 0. Repository-wide just qc, including native corpus-wide checks. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>1055 passed, 3 skipped, 5 deselected in 1634.00s (0:27:13)<br>Validating 625960 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml<br>  files scanned:      625960<br>expected 625960 records, found 625960 on disk<br>pages/ is current<br>Site publication: 530,864,122 bytes (budget 950,000,000)<br>625960 taxon records<br>  NCBITAXON        625960<br>All TaxonMech quality gates passed.<br>  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890 strains (not genome counts)<br>  Related STRAININFO_DEPOSIT: 107277 strain-record pairs, 106843 identifiers, 53890 strains (not genome counts)<br>  Related NUCLEOTIDE_SEQUENCE: 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)<br>LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809 records mapped, 324404579 genomes summed across record attestations (not deduplicated)<br>Causal graphs: 0 records (0 evidence-backed edges)<br><br>All TaxonMech quality gates passed. |

## Limits And Additional Notes

- Review bounded to captured source versions; name and isolate labels alone do not establish a culture deposit, phenotype or mechanism.
- Original manifest-hash-matching GOLD edges were unavailable in the retained configured-path check: expected b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12, observed6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d. Pinned count4 is supported; independent historical recounting remains unresolved.
- Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base canonical recapture preserved all previously reviewed input hashes; original captures and actual transition receipts remain retained.
- Every new bundle still requires its own validate/save/check recipe; baseline native receipts do not claim these later steps have run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T065850Z-aigarchaeota_archaeon
kind: record
repository: CultureBotAI/TaxonMech
title: 'Record review: Aigarchaeota archaeon'
started_at: '2026-10-20T04:07:18Z'
finished_at: '2026-10-20T06:58:50Z'
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
summary: Aigarchaeota archaeon has supported NCBI identity and source projection within
  the checked inputs.
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
  - path: curation/seed_scope.tsv
    sha256: 5fdc0f7111b64e02439d95c6f2b51fcff1d2154c34b2d957422dd9b297e94d4b
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
    sha256: c950844feb0638ce04f7349784749dd1d728fe70bc80f7e2756d956d4ecea254
    role: context
  - path: data/taxa/archaea/aigarchaeota_archaeon.yaml
    sha256: f97b09eff47d0318b6b409f4e9731aa6b736b70386b6b17b40d922c972a5663b
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
    sha256: 6b5b065f4ae7aea022af736a22c0f63dc58a2425c7ee453259e567ab030f8257
    role: context
scope:
  description: Entire single generated record, including all source assertions and
    imported strains.
  selection: Original unreviewed path-order position 73; batch-0008 target 3. Excluded
    122 actual targets from validated main and local batch-0001/0002/0003/0004/0005/0006/0007
    listings; full corpus enumeration includes ignored files.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - NCBITaxon:2528703
targets:
- target_id: NCBITaxon:2528703
  path: data/taxa/archaea/aigarchaeota_archaeon.yaml
  label: Aigarchaeota archaeon
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
  summary: NCBITaxon:2528703 denotes Aigarchaeota archaeon at SPECIES rank, parent
    NCBITaxon:1104572, genetic code 11. All 6 ancestors agree in identifier, literal
    name and rank with pinned NCBI and current EFetch.
  target_ids:
  - NCBITaxon:2528703
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
  summary: NCBI1 NAME, GTDB3 GENOME and GOLD4 ORGANISM agree with pinned projection
    tables. Zero imported strains and absence of pinned descendants are supported.
    The historical GOLD aggregate needs separate provenance assessment; newer primary
    organism objects cannot substitute silently.
  target_ids:
  - NCBITaxon:2528703
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
  summary: 'All five broad mappings are supported by full GTDB shard scans: Geocrenenecus
    sp0250585153, Wolframiiraptor sp0250594153, Benthortus lauensis2, JANXDH01 sp0250597452
    and Terraquivivens sp0250592052. Each contains target2528703 and at least one
    other NCBI taxon, supporting every other-taxa clause. No exact synonyms or equivalent
    xrefs are emitted. The primary attestation counts3 and references four further
    clusters rather than summing12.'
  target_ids:
  - NCBITaxon:2528703
  evidence_ids:
  - gtdb-full-scan
  - gtdb-species
  - gtdb-mappings
  - genome-catalog-1
  - genome-catalog-2
  scope_note: Full nineteen-shard search; literal species tokens and exact NCBI taxon
    membership.
- check_id: strain-genome-evidence
  name: Imported strain links
  status: not_applicable
  required: false
  summary: No imported BacDive strain or strain-level link asserted; absence is bounded
    to the pinned inventories.
  target_ids:
  - NCBITaxon:2528703
  evidence_ids:
  - record
  - bacdive-inventory
  - culture-inventory
- check_id: historical-source-counts
  name: Original manifest-pinned GOLD aggregate
  status: unavailable
  required: true
  summary: Pinned count4 ORGANISM agrees, but original historical input was unavailable
    in retained hash check.
  target_ids:
  - NCBITaxon:2528703
  evidence_ids:
  - manifest
  - gold-organisms
  - historical-gold-edge
- check_id: qc-setup-attempt
  name: Initial quality-gate setup attempt
  status: failed
  required: false
  summary: 'Actual exit 1: missing ruff; superseded by the separately recorded successful
    full retry.'
  target_ids:
  - NCBITaxon:2528703
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
  - NCBITaxon:2528703
  evidence_ids:
  - strict-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0008/uv-cache
    just validate-strict data/taxa/archaea/aigarchaeota_archaeon.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0008/strict-03.tsv
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
  - NCBITaxon:2528703
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
  - NCBITaxon:2528703
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
  - NCBITaxon:2528703
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
  - NCBITaxon:2528703
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
  reference: data/taxa/archaea/aigarchaeota_archaeon.yaml
  accessed_at: '2026-10-20T06:58:50Z'
  support: supports
  summary: Read the entire generated YAML, including identity, lineage, names, mappings,
    source attestations, all imported strains and links, and seed history.
  locator: entire TaxonRecord; identifier=NCBITaxon:2528703
  snapshot_sha256: f97b09eff47d0318b6b409f4e9731aa6b736b70386b6b17b40d922c972a5663b
- evidence_id: taxonomy-inventory
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-20T04:07:19Z'
  support: supports
  summary: Inspected the target and each carried ancestor, rank, parent, genetic code
    and source name classes.
  locator: 'line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""};
    line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"};
    line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"};
    line 150593: {"taxon_id":"NCBITaxon:651137","label":"Nitrososphaerota","rank":"PHYLUM","parent_id":"NCBITaxon:1783275"};
    line 236905: {"taxon_id":"NCBITaxon:1104572","label":"unclassified Nitrososphaerota","rank":"NO_RANK","parent_id":"NCBITaxon:651137"};
    line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"};
    line 529457: {"taxon_id":"NCBITaxon:2528703","label":"Aigarchaeota archaeon","rank":"SPECIES","parent_id":"NCBITaxon:1104572","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon|gtdb|gold","retired_into":"","taxonomy_snapshot":"2026-09-13"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
- evidence_id: scope-row
  kind: database
  reference: curation/seed_scope.tsv
  accessed_at: '2026-10-20T04:07:19Z'
  support: supports
  summary: Exact target is included in the declared seed scope.
  locator: 'line 62766: {"identifier":"NCBITaxon:2528703","added":"2026-09-12","reason":"attested
    rule: Aigarchaeota archaeon, 2 sources incl. NCBI"}'
  snapshot_sha256: 5fdc0f7111b64e02439d95c6f2b51fcff1d2154c34b2d957422dd9b297e94d4b
- evidence_id: path-row
  kind: database
  reference: data/taxa/PATHS.tsv
  accessed_at: '2026-10-20T04:07:19Z'
  support: supports
  summary: Indexed path resolves to this exact NCBI taxon.
  locator: 'line 348670: {"identifier":"NCBITaxon:2528703","slug":"aigarchaeota_archaeon"}'
  snapshot_sha256: c950844feb0638ce04f7349784749dd1d728fe70bc80f7e2756d956d4ecea254
- evidence_id: ncbi-live
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=568409,3138747,2528703,1052838,1052839,1052841,1052823,1052825,1052826,1052828
  accessed_at: '2026-10-20T04:07:54Z'
  support: supports
  summary: 'Inspected the official response for this exact taxon: scientific name,
    rank, parent, source name classes, lineage and genetic code. Current authority
    and pinned September inventory remain distinct observations.'
  locator: TaxaSet/Taxon[TaxId='2528703']; ten-target captured response
  snapshot_sha256: 28850f1b86a3f5cacf0ba40b87c52a38e7cf9c3fe3478359b1e621fa837ce71c
- evidence_id: lpsn-inventory
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-20T04:07:19Z'
  support: supports
  summary: Inspected exact mapped and linked LPSN names; bounded inventory absence
    does not establish worldwide nomenclatural absence.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: gtdb-mappings
  kind: database
  reference: data/raw/gtdb_mappings.tsv
  accessed_at: '2026-10-20T04:07:19Z'
  support: supports
  summary: Inspected direct mappings and selected clusters' reverse mappings, retaining
    each source predicate and taxon boundary.
  locator: 'line 138221: {"gtdb_id":"GTDB:s__Geocrenenecus_sp025058515","gtdb_label":"s__Geocrenenecus_sp025058515","gtdb_parent":"GTDB:g__Geocrenenecus","ncbitaxon_id":"NCBITaxon:2026795","predicate":"skos:broadMatch","genome_count":"3"};
    line 138249: {"gtdb_id":"GTDB:s__JANXDH01_sp025059745","gtdb_label":"s__JANXDH01_sp025059745","gtdb_parent":"GTDB:g__JANXDH01","ncbitaxon_id":"NCBITaxon:2026795","predicate":"skos:broadMatch","genome_count":"2"};
    line 138326: {"gtdb_id":"GTDB:s__Terraquivivens_sp025059205","gtdb_label":"s__Terraquivivens_sp025059205","gtdb_parent":"GTDB:g__Terraquivivens","ncbitaxon_id":"NCBITaxon:2026795","predicate":"skos:broadMatch","genome_count":"2"};
    line 138370: {"gtdb_id":"GTDB:s__Wolframiiraptor_sp025059415","gtdb_label":"s__Wolframiiraptor_sp025059415","gtdb_parent":"GTDB:g__Wolframiiraptor","ncbitaxon_id":"NCBITaxon:2026795","predicate":"skos:broadMatch","genome_count":"3"};
    line 179372: {"gtdb_id":"GTDB:s__Geocrenenecus_sp025058515","gtdb_label":"s__Geocrenenecus_sp025058515","gtdb_parent":"GTDB:g__Geocrenenecus","ncbitaxon_id":"NCBITaxon:2268198","predicate":"skos:broadMatch","genome_count":"3"};
    line 179402: {"gtdb_id":"GTDB:s__Wolframiiraptor_sp025059415","gtdb_label":"s__Wolframiiraptor_sp025059415","gtdb_parent":"GTDB:g__Wolframiiraptor","ncbitaxon_id":"NCBITaxon:2268198","predicate":"skos:broadMatch","genome_count":"3"};
    line 197396: {"gtdb_id":"GTDB:s__Benthortus_lauensis","gtdb_label":"s__Benthortus_lauensis","gtdb_parent":"GTDB:g__Benthortus","ncbitaxon_id":"NCBITaxon:2528703","predicate":"skos:broadMatch","genome_count":"2"};
    line 197397: {"gtdb_id":"GTDB:s__Geocrenenecus_sp025058515","gtdb_label":"s__Geocrenenecus_sp025058515","gtdb_parent":"GTDB:g__Geocrenenecus","ncbitaxon_id":"NCBITaxon:2528703","predicate":"skos:broadMatch","genome_count":"3"};
    line 197398: {"gtdb_id":"GTDB:s__JANXDH01_sp025059745","gtdb_label":"s__JANXDH01_sp025059745","gtdb_parent":"GTDB:g__JANXDH01","ncbitaxon_id":"NCBITaxon:2528703","predicate":"skos:broadMatch","genome_count":"2"};
    line 197399: {"gtdb_id":"GTDB:s__Terraquivivens_sp025059205","gtdb_label":"s__Terraquivivens_sp025059205","gtdb_parent":"GTDB:g__Terraquivivens","ncbitaxon_id":"NCBITaxon:2528703","predicate":"skos:broadMatch","genome_count":"2"};
    line 197400: {"gtdb_id":"GTDB:s__Wolframiiraptor_sp025059415","gtdb_label":"s__Wolframiiraptor_sp025059415","gtdb_parent":"GTDB:g__Wolframiiraptor","ncbitaxon_id":"NCBITaxon:2528703","predicate":"skos:broadMatch","genome_count":"3"};
    line 242188: {"gtdb_id":"GTDB:s__Benthortus_lauensis","gtdb_label":"s__Benthortus_lauensis","gtdb_parent":"GTDB:g__Benthortus","ncbitaxon_id":"NCBITaxon:2973087","predicate":"skos:closeMatch","genome_count":"2"}'
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
- evidence_id: gtdb-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-20T04:07:19Z'
  support: supports
  summary: Inspected source species identifiers, labels, parent clusters and genome
    counts.
  locator: 'line 17093: {"gtdb_id":"GTDB:s__Benthortus_lauensis","label":"s__Benthortus_lauensis","parent":"GTDB:g__Benthortus","genome_count":"2"};
    line 69863: {"gtdb_id":"GTDB:s__Geocrenenecus_sp025058515","label":"s__Geocrenenecus_sp025058515","parent":"GTDB:g__Geocrenenecus","genome_count":"3"};
    line 97236: {"gtdb_id":"GTDB:s__JANXDH01_sp025059745","label":"s__JANXDH01_sp025059745","parent":"GTDB:g__JANXDH01","genome_count":"2"};
    line 175377: {"gtdb_id":"GTDB:s__Terraquivivens_sp025059205","label":"s__Terraquivivens_sp025059205","parent":"GTDB:g__Terraquivivens","genome_count":"2"};
    line 198640: {"gtdb_id":"GTDB:s__Wolframiiraptor_sp025059415","label":"s__Wolframiiraptor_sp025059415","parent":"GTDB:g__Wolframiiraptor","genome_count":"3"}'
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
- evidence_id: bacdive-inventory
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-20T04:07:19Z'
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
  accessed_at: '2026-10-20T04:07:19Z'
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
  accessed_at: '2026-10-20T04:07:19Z'
  support: supports
  summary: Inspected the exact GOLD organism count row or bounded absence, without
    converting counts to phenotypes.
  locator: 'line 23035: {"taxon_id":"NCBITaxon:2528703","organism_count":"4"}'
  snapshot_sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
- evidence_id: mediadive-taxa
  kind: database
  reference: data/raw/mediadive_taxa.tsv
  accessed_at: '2026-10-20T04:07:19Z'
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
  accessed_at: '2026-10-20T04:07:19Z'
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
  accessed_at: '2026-10-20T04:07:19Z'
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
  accessed_at: '2026-10-20T06:58:50Z'
  support: supports
  summary: Policy permits one-to-one species closeMatch normalization and LPSN-linked
    species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage
    unchanged.
  locator: Mapping predicates; Which strains belong to a record
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
- evidence_id: equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-20T06:58:50Z'
  support: supports
  summary: TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations
    remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes
    under the source taxon.
  locator: TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
- evidence_id: seed-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-20T06:58:50Z'
  support: supports
  summary: Inspected mapping ranking, qualified predicates, fixed broadMatch wording,
    synonym/xref construction, primary cluster counts and same-taxon type-strain derivation.
  locator: GTDB mapping construction lines 440–472; LPSN/type-strain and source-attestation
    construction
  snapshot_sha256: 6b5b065f4ae7aea022af736a22c0f63dc58a2425c7ee453259e567ab030f8257
- evidence_id: manifest
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-20T06:58:50Z'
  support: supports
  summary: Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd,
    upstream input hashes and extraction time 2026-09-13T17:50:44Z.
  locator: kg_microbe_source, inputs, extracted_at
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
- evidence_id: overlay-manifests
  kind: record_content
  reference: data/atb/MANIFEST.yaml
  accessed_at: '2026-10-20T06:58:50Z'
  support: supports
  summary: Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z,
    matching the sole seed event. StrainInfo manifest is independently captured in
    source.inputs.
  locator: extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml
  snapshot_sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
- evidence_id: genome-catalog-1
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0017.jsonl.gz
  accessed_at: '2026-10-20T06:52:51Z'
  support: supports
  summary: Inspected primary cluster membership, exact taxon IDs, assembly versions
    and isolate labels. Historical source lineages remain distinct from current NCBI
    classification; no culture deposit or phenotype is inferred.
  locator: 'line 30182: {"accession":"GB_GCA_026413895.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Wolframiiraptor;s__Wolframiiraptor
    sp025059415","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM2641389v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJEB4990","ncbi_biosample":"SAMN30305265","ncbi_contig_count":"55","ncbi_contig_n50":"39926","ncbi_country":"Malaysia:
    Sungkai; Perak","ncbi_date":"2022-11-27","ncbi_genbank_assembly_accession":"GCA_026413895.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKW304","ncbi_isolation_source":"alkaline
    hot spring water","ncbi_lat_lon":"3.9966 N 101.3931 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Nitrososphaeria
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"48","ncbi_scaffold_l50":"8","ncbi_scaffold_n50":"39926","ncbi_scaffold_n75":"22100","ncbi_scaffold_n90":"13717","ncbi_seq_rel_date":"2022-11-27","ncbi_spanned_gaps":"7","ncbi_species_taxid":"2268198","ncbi_ssu_count":"1","ncbi_strain_identifiers":"SKW304","ncbi_submitter":"Universiti
    Teknologi Malaysia - Malaysia","ncbi_taxid":"2268198","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__Nitrososphaeria;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;c__Nitrososphaeria;x__unclassified
    Nitrososphaeria;s__Nitrososphaeria archaeon","ncbi_total_gap_length":"338","ncbi_total_length":"1008461","ncbi_translation_table":"11","ncbi_trna_count":"37","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1008123","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAOAKC000000000.1"};
    line 31321: {"accession":"GB_GCA_026413845.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Geocrenenecus;s__Geocrenenecus
    sp025058515","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM2641384v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJEB4990","ncbi_biosample":"SAMN30305268","ncbi_contig_count":"60","ncbi_contig_n50":"96656","ncbi_country":"Malaysia:
    Sungkai; Perak","ncbi_date":"2022-11-27","ncbi_genbank_assembly_accession":"GCA_026413845.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKW312","ncbi_isolation_source":"alkaline
    hot spring water","ncbi_lat_lon":"3.9966 N 101.3931 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Nitrososphaeria
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"4","ncbi_scaffold_count":"56","ncbi_scaffold_l50":"5","ncbi_scaffold_n50":"96656","ncbi_scaffold_n75":"85111","ncbi_scaffold_n90":"34113","ncbi_seq_rel_date":"2022-11-27","ncbi_spanned_gaps":"4","ncbi_species_taxid":"2268198","ncbi_ssu_count":"1","ncbi_strain_identifiers":"SKW312","ncbi_submitter":"Universiti
    Teknologi Malaysia - Malaysia","ncbi_taxid":"2268198","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__Nitrososphaeria;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;c__Nitrososphaeria;x__unclassified
    Nitrososphaeria;s__Nitrososphaeria archaeon","ncbi_total_gap_length":"130","ncbi_total_length":"1550754","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1550624","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAOAKF000000000.1"};
    line 31969: {"accession":"GB_GCA_025059205.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Terraquivivens;s__Terraquivivens
    sp025059205","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM2505920v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA761511","ncbi_biosample":"SAMN30304937","ncbi_contig_count":"38","ncbi_contig_n50":"299742","ncbi_country":"Malaysia:
    Sungkai; Perak","ncbi_date":"2022-09-07","ncbi_genbank_assembly_accession":"GCA_025059205.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYB131","ncbi_isolation_source":"brown
    biofilm from alkaline hot spring","ncbi_lat_lon":"3.9956 N 101.3933 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Aigarchaeota
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"4","ncbi_scaffold_count":"35","ncbi_scaffold_l50":"2","ncbi_scaffold_n50":"304507","ncbi_scaffold_n75":"72180","ncbi_scaffold_n90":"37787","ncbi_seq_rel_date":"2022-09-07","ncbi_spanned_gaps":"3","ncbi_species_taxid":"2528703","ncbi_ssu_count":"2","ncbi_strain_identifiers":"SKYB131","ncbi_submitter":"Universiti
    Teknologi Malaysia","ncbi_taxid":"2528703","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified
    Nitrososphaerota;s__Aigarchaeota archaeon","ncbi_total_gap_length":"179","ncbi_total_length":"1188966","ncbi_translation_table":"11","ncbi_trna_count":"53","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1188787","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JANXDS000000000.1"};
    line 33558: {"accession":"GB_GCA_025059745.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Calditenuaceae;g__JANXDH01;s__JANXDH01
    sp025059745","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2505974v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA761511","ncbi_biosample":"SAMN30304926","ncbi_contig_count":"6","ncbi_contig_n50":"733637","ncbi_country":"Malaysia:
    Sungkai; Perak","ncbi_date":"2022-09-07","ncbi_genbank_assembly_accession":"GCA_025059745.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYB10","ncbi_isolation_source":"brown
    biofilm from alkaline hot spring","ncbi_lat_lon":"3.9956 N 101.3933 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Aigarchaeota
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"4","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2022-09-07","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2528703","ncbi_ssu_count":"2","ncbi_strain_identifiers":"SKYB10","ncbi_submitter":"Universiti
    Teknologi Malaysia","ncbi_taxid":"2528703","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified
    Nitrososphaerota;s__Aigarchaeota archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1166430","ncbi_translation_table":"11","ncbi_trna_count":"43","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1166430","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JANXDH000000000.1"};
    line 35896: {"accession":"GB_GCA_025058515.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Geocrenenecus;s__Geocrenenecus
    sp025058515","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2505851v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA761511","ncbi_biosample":"SAMN30304941","ncbi_contig_count":"53","ncbi_contig_n50":"48213","ncbi_country":"Malaysia:
    Sungkai; Perak","ncbi_date":"2022-09-07","ncbi_genbank_assembly_accession":"GCA_025058515.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYB24","ncbi_isolation_source":"brown
    biofilm from alkaline hot spring","ncbi_lat_lon":"3.9956 N 101.3933 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Aigarchaeota
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"5","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2022-09-07","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2528703","ncbi_ssu_count":"2","ncbi_strain_identifiers":"SKYB24","ncbi_submitter":"Universiti
    Teknologi Malaysia","ncbi_taxid":"2528703","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified
    Nitrososphaerota;s__Aigarchaeota archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1466662","ncbi_translation_table":"11","ncbi_trna_count":"41","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1466662","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JANXDW000000000.1"};
    line 37620: {"accession":"GB_GCA_033581775.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Wolframiiraptor;s__Wolframiiraptor
    sp025059415","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM3358177v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA1012858","ncbi_biosample":"SAMN37334029","ncbi_contig_count":"57","ncbi_contig_n50":"32319","ncbi_country":"none","ncbi_date":"2023-11-13","ncbi_genbank_assembly_accession":"GCA_033581775.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYBB_hs_bin105","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Nitrososphaerota
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"4","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2023-11-13","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2026795","ncbi_ssu_count":"2","ncbi_strain_identifiers":"SKYBB_hs_bin105","ncbi_submitter":"Universiti
    Teknologi Malaysia","ncbi_taxid":"2026795","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified
    Nitrososphaerota;s__Nitrososphaerota archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1048200","ncbi_translation_table":"11","ncbi_trna_count":"34","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1048200","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAVQSO000000000.1"};
    line 38067: {"accession":"GB_GCA_021650775.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Benthortus;s__Benthortus
    lauensis","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM2165077v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA495050","ncbi_biosample":"SAMN19948827","ncbi_contig_count":"112","ncbi_contig_n50":"19743","ncbi_country":"Pacific
    Ocean","ncbi_date":"2022-01-27","ncbi_genbank_assembly_accession":"GCA_021650775.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"T2-175","ncbi_isolation_source":"hydrothermal
    vent deposit","ncbi_lat_lon":"21.9904 S 176.5692 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Candidatus
    Benthortus lauensis","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2022-01-27","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2973087","ncbi_ssu_count":"none","ncbi_strain_identifiers":"T2-175","ncbi_submitter":"Portland
    State University","ncbi_taxid":"2973087","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__Candidatus
    Wolframiiraptoraceae;g__Candidatus Benthortus;s__Candidatus Benthortus lauensis","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__Nitrososphaerota
    incertae sedis;f__Candidatus Wolframiiraptoraceae;g__Candidatus Benthortus;s__Candidatus
    Benthortus lauensis","ncbi_total_gap_length":"0","ncbi_total_length":"1470116","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"assembly
    from type material","ncbi_ungapped_length":"1470116","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAHSRM000000000.1"};
    line 39953: {"accession":"GB_GCA_033582315.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Geocrenenecus;s__Geocrenenecus
    sp025058515","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM3358231v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA1012858","ncbi_biosample":"SAMN37334009","ncbi_contig_count":"89","ncbi_contig_n50":"91093","ncbi_country":"none","ncbi_date":"2023-11-13","ncbi_genbank_assembly_accession":"GCA_033582315.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYBB_h_bin138","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Nitrososphaerota
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"1","ncbi_scaffold_count":"85","ncbi_scaffold_l50":"5","ncbi_scaffold_n50":"91093","ncbi_scaffold_n75":"49374","ncbi_scaffold_n90":"24444","ncbi_seq_rel_date":"2023-11-13","ncbi_spanned_gaps":"4","ncbi_species_taxid":"2026795","ncbi_ssu_count":"0","ncbi_strain_identifiers":"SKYBB_h_bin138","ncbi_submitter":"Universiti
    Teknologi Malaysia","ncbi_taxid":"2026795","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified
    Nitrososphaerota;s__Nitrososphaerota archaeon","ncbi_total_gap_length":"40","ncbi_total_length":"1538472","ncbi_translation_table":"11","ncbi_trna_count":"47","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1538432","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAVQRU000000000.1"};
    line 42187: {"accession":"GB_GCA_033581195.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Terraquivivens;s__Terraquivivens
    sp025059205","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM3358119v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA1012858","ncbi_biosample":"SAMN37334059","ncbi_contig_count":"36","ncbi_contig_n50":"597539","ncbi_country":"none","ncbi_date":"2023-11-13","ncbi_genbank_assembly_accession":"GCA_033581195.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYBB_hs_bin56","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Nitrososphaerota
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"5","ncbi_scaffold_count":"33","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"597539","ncbi_scaffold_n75":"71884","ncbi_scaffold_n90":"40245","ncbi_seq_rel_date":"2023-11-13","ncbi_spanned_gaps":"3","ncbi_species_taxid":"2026795","ncbi_ssu_count":"2","ncbi_strain_identifiers":"SKYBB_hs_bin56","ncbi_submitter":"Universiti
    Teknologi Malaysia","ncbi_taxid":"2026795","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified
    Nitrososphaerota;s__Nitrososphaerota archaeon","ncbi_total_gap_length":"30","ncbi_total_length":"1157564","ncbi_translation_table":"11","ncbi_trna_count":"52","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1157534","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAVQTS000000000.1"};
    line 43420: {"accession":"GB_GCA_025059415.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Wolframiiraptor;s__Wolframiiraptor
    sp025059415","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM2505941v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA761511","ncbi_biosample":"SAMN30304935","ncbi_contig_count":"98","ncbi_contig_n50":"19725","ncbi_country":"Malaysia:
    Sungkai; Perak","ncbi_date":"2022-09-07","ncbi_genbank_assembly_accession":"GCA_025059415.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYB129","ncbi_isolation_source":"brown
    biofilm from alkaline hot spring","ncbi_lat_lon":"3.9956 N 101.3933 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Aigarchaeota
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"1","ncbi_scaffold_count":"71","ncbi_scaffold_l50":"11","ncbi_scaffold_n50":"24526","ncbi_scaffold_n75":"16458","ncbi_scaffold_n90":"10555","ncbi_seq_rel_date":"2022-09-07","ncbi_spanned_gaps":"27","ncbi_species_taxid":"2528703","ncbi_ssu_count":"0","ncbi_strain_identifiers":"SKYB129","ncbi_submitter":"Universiti
    Teknologi Malaysia","ncbi_taxid":"2528703","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified
    Nitrososphaerota;s__Aigarchaeota archaeon","ncbi_total_gap_length":"2650","ncbi_total_length":"985681","ncbi_translation_table":"11","ncbi_trna_count":"42","ncbi_type_material_designation":"na","ncbi_ungapped_length":"983031","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JANXDQ000000000.1"};
    line 44283: {"accession":"GB_GCA_015520375.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Wolframiiraptoraceae;g__Benthortus;s__Benthortus
    lauensis","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM1552037v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA546572","ncbi_biosample":"SAMN12837340","ncbi_contig_count":"144","ncbi_contig_n50":"10284","ncbi_country":"Pacific
    Ocean","ncbi_date":"2020-11-16","ncbi_genbank_assembly_accession":"GCA_015520375.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"S146_127","ncbi_isolation_source":"deep-sea
    hydrothermal deposit","ncbi_lat_lon":"34.86208959 S 179.0573881 E","ncbi_molecule_count":"0","ncbi_ncrna_count":"none","ncbi_organism_name":"Aigarchaeota
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"none","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2020-11-16","ncbi_spanned_gaps":"0","ncbi_species_taxid":"2528703","ncbi_ssu_count":"none","ncbi_strain_identifiers":"S146_127","ncbi_submitter":"Portland
    State University","ncbi_taxid":"2528703","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified
    Nitrososphaerota;s__Aigarchaeota archaeon","ncbi_total_gap_length":"0","ncbi_total_length":"1148221","ncbi_translation_table":"none","ncbi_trna_count":"none","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1148221","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"WAQD00000000.1"}'
  snapshot_sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
- evidence_id: genome-catalog-2
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0018.jsonl.gz
  accessed_at: '2026-10-20T06:52:51Z'
  support: supports
  summary: Inspected primary cluster membership, exact taxon IDs, assembly versions
    and isolate labels. Historical source lineages remain distinct from current NCBI
    classification; no culture deposit or phenotype is inferred.
  locator: 'line 1230: {"accession":"GB_GCA_033581295.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Nitrososphaeria_A;o__Caldarchaeales;f__Calditenuaceae;g__JANXDH01;s__JANXDH01
    sp025059745","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Scaffold","ncbi_assembly_name":"ASM3358129v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA1012858","ncbi_biosample":"SAMN37334054","ncbi_contig_count":"24","ncbi_contig_n50":"304995","ncbi_country":"none","ncbi_date":"2023-11-13","ncbi_genbank_assembly_accession":"GCA_033581295.1","ncbi_genome_category":"derived
    from metagenome","ncbi_genome_representation":"full","ncbi_isolate":"SKYBB_hs_bin41","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Nitrososphaerota
    archaeon","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"5","ncbi_scaffold_count":"22","ncbi_scaffold_l50":"2","ncbi_scaffold_n50":"304995","ncbi_scaffold_n75":"282826","ncbi_scaffold_n90":"113951","ncbi_seq_rel_date":"2023-11-13","ncbi_spanned_gaps":"2","ncbi_species_taxid":"2026795","ncbi_ssu_count":"2","ncbi_strain_identifiers":"SKYBB_hs_bin41","ncbi_submitter":"Universiti
    Teknologi Malaysia","ncbi_taxid":"2026795","ncbi_taxonomy":"d__Archaea;p__Nitrososphaerota;c__;o__;f__;g__;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Nitrososphaerota;x__unclassified
    Nitrososphaerota;s__Nitrososphaerota archaeon","ncbi_total_gap_length":"380","ncbi_total_length":"1248770","ncbi_translation_table":"11","ncbi_trna_count":"55","ncbi_type_material_designation":"na","ncbi_ungapped_length":"1248390","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JAVQTN000000000.1"}'
  snapshot_sha256: 8baa314877815777abcdf600079c6ee42f2ea5340398df9f2e18de9c18fd4347
- evidence_id: gtdb-full-scan
  kind: search
  reference: data/catalog/MANIFEST.json
  accessed_at: '2026-10-20T06:52:51Z'
  support: supports
  summary: All nineteen GTDB shards searched for exact terminal species tokens; counts
    and taxon membership inspected.
  locator: '{"s__Wolframiiraptor sp025059415":[{"accession":"GB_GCA_026413895.1","ncbi_taxid":"2268198","ncbi_species_taxid":"2268198","ncbi_organism_name":"Nitrososphaeria
    archaeon","ncbi_strain_identifiers":"SKW304","ncbi_genome_category":"derived from
    metagenome"},{"accession":"GB_GCA_033581775.1","ncbi_taxid":"2026795","ncbi_species_taxid":"2026795","ncbi_organism_name":"Nitrososphaerota
    archaeon","ncbi_strain_identifiers":"SKYBB_hs_bin105","ncbi_genome_category":"derived
    from metagenome"},{"accession":"GB_GCA_025059415.1","ncbi_taxid":"2528703","ncbi_species_taxid":"2528703","ncbi_organism_name":"Aigarchaeota
    archaeon","ncbi_strain_identifiers":"SKYB129","ncbi_genome_category":"derived
    from metagenome"}],"s__Geocrenenecus sp025058515":[{"accession":"GB_GCA_026413845.1","ncbi_taxid":"2268198","ncbi_species_taxid":"2268198","ncbi_organism_name":"Nitrososphaeria
    archaeon","ncbi_strain_identifiers":"SKW312","ncbi_genome_category":"derived from
    metagenome"},{"accession":"GB_GCA_025058515.1","ncbi_taxid":"2528703","ncbi_species_taxid":"2528703","ncbi_organism_name":"Aigarchaeota
    archaeon","ncbi_strain_identifiers":"SKYB24","ncbi_genome_category":"derived from
    metagenome"},{"accession":"GB_GCA_033582315.1","ncbi_taxid":"2026795","ncbi_species_taxid":"2026795","ncbi_organism_name":"Nitrososphaerota
    archaeon","ncbi_strain_identifiers":"SKYBB_h_bin138","ncbi_genome_category":"derived
    from metagenome"}],"s__Terraquivivens sp025059205":[{"accession":"GB_GCA_025059205.1","ncbi_taxid":"2528703","ncbi_species_taxid":"2528703","ncbi_organism_name":"Aigarchaeota
    archaeon","ncbi_strain_identifiers":"SKYB131","ncbi_genome_category":"derived
    from metagenome"},{"accession":"GB_GCA_033581195.1","ncbi_taxid":"2026795","ncbi_species_taxid":"2026795","ncbi_organism_name":"Nitrososphaerota
    archaeon","ncbi_strain_identifiers":"SKYBB_hs_bin56","ncbi_genome_category":"derived
    from metagenome"}],"s__JANXDH01 sp025059745":[{"accession":"GB_GCA_025059745.1","ncbi_taxid":"2528703","ncbi_species_taxid":"2528703","ncbi_organism_name":"Aigarchaeota
    archaeon","ncbi_strain_identifiers":"SKYB10","ncbi_genome_category":"derived from
    metagenome"},{"accession":"GB_GCA_033581295.1","ncbi_taxid":"2026795","ncbi_species_taxid":"2026795","ncbi_organism_name":"Nitrososphaerota
    archaeon","ncbi_strain_identifiers":"SKYBB_hs_bin41","ncbi_genome_category":"derived
    from metagenome"}],"s__Benthortus lauensis":[{"accession":"GB_GCA_021650775.1","ncbi_taxid":"2973087","ncbi_species_taxid":"2973087","ncbi_organism_name":"Candidatus
    Benthortus lauensis","ncbi_strain_identifiers":"T2-175","ncbi_genome_category":"derived
    from metagenome"},{"accession":"GB_GCA_015520375.1","ncbi_taxid":"2528703","ncbi_species_taxid":"2528703","ncbi_organism_name":"Aigarchaeota
    archaeon","ncbi_strain_identifiers":"S146_127","ncbi_genome_category":"derived
    from metagenome"}]}'
  snapshot_sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
  search_scope: Full explicit reads of every enumerated GTDB primary shard including
    ignored files. Exact terminal GTDB species token; exact assembly accession stem
    or explicit genome identifier. Versions remain separate.
- evidence_id: historical-gold-edge
  kind: search
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T07:30:22Z'
  support: partial
  summary: Earlier actual configured-path check found source bytes differing from
    the manifest-pinned GOLD input. This retained observation does not establish worldwide
    absence.
  locator: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/gold/edges.tsv;
    expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12; observed=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
  search_scope: Exact configured historical input path, including ignored files; retained
    receipt, not a new search.
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
  reference: just validate-strict data/taxa/archaea/aigarchaeota_archaeon.yaml --out
    /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0008/strict-03.tsv
  accessed_at: '2026-10-20T04:07:24Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0008/repo;\
    \ started 2026-10-20T04:07:23Z, finished 2026-10-20T04:07:24Z, exit 0. This exact\
    \ generated YAML only; its captured bytes remain unchanged. Actual earlier per-target\
    \ invocation; the receipt retains its original cwd and times.\nValidating 1 files\
    \ with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0003/src/taxonmech/schema/taxonmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0008/strict-03.tsv"
  locator: This exact generated YAML only; its captured bytes remain unchanged. Actual
    earlier per-target invocation; the receipt retains its original cwd and times.
  snapshot_sha256: 5bb0e348ba78690aceebe0d3757c2c064c244274e3735b6dade58bde8bc02f27
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
  summary: NCBITaxon:2528703 denotes Aigarchaeota archaeon at SPECIES rank, parent
    NCBITaxon:1104572, genetic code 11. All 6 ancestors agree in identifier, literal
    name and rank with pinned NCBI and current EFetch.
  target_ids:
  - NCBITaxon:2528703
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
  summary: The generic species-rank placeholder has no NCBI synonym or same-taxon
    LPSN assertion. No individual cultured organism identity is inferred.
  target_ids:
  - NCBITaxon:2528703
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - lpsn-inventory
  - mapping-policy
- assessment_id: completeness
  area: completeness
  topic: Imported subtree and source assertion units
  outcome: supported
  summary: NCBI1 NAME, GTDB3 GENOME and GOLD4 ORGANISM agree with pinned projection
    tables. Zero imported strains and absence of pinned descendants are supported.
    The historical GOLD aggregate needs separate provenance assessment; newer primary
    organism objects cannot substitute silently.
  target_ids:
  - NCBITaxon:2528703
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
- assessment_id: taxonomy-mapping
  area: grounding
  topic: Qualified species mapping and target scope
  outcome: supported
  summary: 'All five broad mappings are supported by full GTDB shard scans: Geocrenenecus
    sp0250585153, Wolframiiraptor sp0250594153, Benthortus lauensis2, JANXDH01 sp0250597452
    and Terraquivivens sp0250592052. Each contains target2528703 and at least one
    other NCBI taxon, supporting every other-taxa clause. No exact synonyms or equivalent
    xrefs are emitted. The primary attestation counts3 and references four further
    clusters rather than summing12.'
  target_ids:
  - NCBITaxon:2528703
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
  summary: EXACT grounding and SEEDED mapping remain supported; the sole seed event
    agrees with the manifest extraction time. No native status or history is changed.
  target_ids:
  - NCBITaxon:2528703
  evidence_ids:
  - record
  - manifest
  - overlay-manifests
findings: []
actions:
- action_id: recover-pinned-aggregate-inputs
  finding_ids: []
  target_ids:
  - NCBITaxon:2528703
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
- Review bounded to captured source versions; name and isolate labels alone do not
  establish a culture deposit, phenotype or mechanism.
- 'Original manifest-hash-matching GOLD edges were unavailable in the retained configured-path
  check: expected b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12,
  observed6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d. Pinned
  count4 is supported; independent historical recounting remains unresolved.'
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
- batch-0008
- archaea
- generated
- source-checked
```
