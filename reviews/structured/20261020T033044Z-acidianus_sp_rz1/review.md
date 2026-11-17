# Record review: Acidianus sp. RZ1

- Review: 20261020T033044Z-acidianus_sp_rz1
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-19T23:34:32Z
- Finished UTC: 2026-10-20T03:30:44Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The RZ1 species record has supported NCBI identity and a locally permitted GTDB species naming link, corroborated by the DSM 29099 culture history. No record-specific defect was established; original GOLD and MediaDive aggregate verification remains incomplete.

## Scope And Provenance

Entire single generated record, including all source assertions and imported strains.

Selection: Original unreviewed path-order position 21; batch-0003 target 1. Excluded 72 actual targets from validated main and local batch-0001/0002 listings; full corpus enumeration includes ignored files.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9b5a8fff5185b38dc5c77bb35235152c81ea7765.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:1540082 | data/taxa/archaea/acidianus_sp_rz1.yaml | generated | Acidianus sp. RZ1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact NCBI taxon, rank and lineage | passed | True | NCBITaxon:1540082 | NCBITaxon:1540082 denotes Acidianus sp. RZ1 at SPECIES rank, parent NCBITaxon:2629519, genetic code 11, with 10 carried ancestors. All lineage IDs, names and ranks agree with the pinned inventory and captured NCBI EFetch, accounting for EFetch's omission of root. |
| Imported strain and genome assertion check | not_applicable | False | NCBITaxon:1540082 | No imported BacDive strain or strain-level genome assertion is present. Exact source inventory/subtree selection was checked. An external strain classified elsewhere or a genome/isolate name does not create an imported physical deposit. |
| Complete identifier and name inventory search | passed | True | NCBITaxon:1540082 | The complete pinned subtree has no descendants or directly classified BacDive entries. BacDive 131324 is filed under 1160895, so its related RZ1 designation does not authorize importing it under 1540082. NCBI 1 NAME, GTDB 2 GENOME, MediaDive 2 MEDIUM and GOLD 1 ORGANISM agree with the pinned inventories. The current DSM 29099 MediaDive page lists 88 and J176; GOLD Go0566671 explicitly carries DSM 29099 and taxon 1540082. Current supporting objects do not reproduce the historical edge snapshot. |
| Original manifest-pinned aggregate edge counts | unavailable | True | NCBITaxon:1540082 | Pinned inventories agree with the generated assertions, but original matching edge bytes are unavailable in the checked locations for gold, mediadive. Current sources cannot reproduce that historical extraction. |
| Initial quality-gate setup attempt | failed | False | NCBITaxon:1540082 | Actual exit 1: missing ruff; superseded by the separately recorded successful full retry. |
| Native strict record validation | passed | True | NCBITaxon:1540082 | Actual terminal exit code 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. |
| Repository history validation | passed | True | NCBITaxon:1540082 | Actual terminal exit code 0. All 17 standalone history records; the generated seed event was also inspected in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| Full-corpus exact reproduction | passed | True | NCBITaxon:1540082 | Actual terminal exit code 0. All 625,960 generated taxon YAMLs, not a focused approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| Native product ID/label gate | passed | True | NCBITaxon:1540082 | Actual terminal exit code 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| Authoritative complete quality gate | passed | True | NCBITaxon:1540082 | Actual terminal exit code 0. Repository-wide just qc, including native corpus-wide checks. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. Pytest reported 1055 passed, 3 skipped and 5 deselected; the native QC recipe completed successfully. |

## Scientific And Domain Assessments

### Exact taxon and source lineage

identity: supported. Targets: NCBITaxon:1540082.

NCBITaxon:1540082 denotes Acidianus sp. RZ1 at SPECIES rank, parent NCBITaxon:2629519, genetic code 11, with 10 carried ancestors. All lineage IDs, names and ranks agree with the pinned inventory and captured NCBI EFetch, accounting for EFetch's omission of root.

### Name classes and nomenclatural scope

nomenclature: supported. Targets: NCBITaxon:1540082.

NCBI supplies Acidianus sp. DSM 29099 as an exact synonym. The captured DSMZ catalogue explicitly identifies DSM 29099 as Acidianus copahuensis, designation RZ1, other deposit JCM 30227, with history Acidianus sp. RZ1. BacDive 131324 uses the copahuensis taxon 1160895 while its sequence fields retain 1540082; these source boundaries are preserved. LPSN treats Candidatus Acidianus copahuensis as not validly published with pro-valid/pro-correct status and type ALE1. This does not make RZ1 the type strain or merge the two NCBI identities.

### Imported subtree and source assertion units

completeness: supported. Targets: NCBITaxon:1540082.

The complete pinned subtree has no descendants or directly classified BacDive entries. BacDive 131324 is filed under 1160895, so its related RZ1 designation does not authorize importing it under 1540082. NCBI 1 NAME, GTDB 2 GENOME, MediaDive 2 MEDIUM and GOLD 1 ORGANISM agree with the pinned inventories. The current DSM 29099 MediaDive page lists 88 and J176; GOLD Go0566671 explicitly carries DSM 29099 and taxon 1540082. Current supporting objects do not reproduce the historical edge snapshot.

### Qualified species mapping and target scope

grounding: supported. Targets: NCBITaxon:1540082.

The GTDB species cluster contains two inspected primary genomes: ALE1 RS_GCF_000632495.1 with taxon/species 1160895 and DSM 29099 RS_GCF_013133895.1 with taxon/species 1540082. The qualified closeMatch and species-level exact name/xref follow the local harmonization policy; independent culture history supports the naming association. This does not establish physical deposit or assembly equivalence.

### Unchanged native status and history

provenance: supported. Targets: NCBITaxon:1540082.

Grounding EXACT and mapping SEEDED remain unchanged. The sole seed event at 2026-09-13T17:54:04Z agrees with the maximum captured extraction timestamp across raw, ATB and StrainInfo manifests. No native status or history is promoted by this review.

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
| record | data/taxa/archaea/acidianus_sp_rz1.yaml; entire TaxonRecord; identifier=NCBITaxon:1540082 | supports | Read the entire generated YAML, including identity, lineage, names, mappings, source attestations, all imported strains and links, and seed history. |
| taxonomy-inventory | data/raw/ncbitaxon_taxa.tsv; line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""}; line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"}; line 1798: {"taxon_id":"NCBITaxon:2281","label":"Sulfolobales","rank":"ORDER","parent_id":"NCBITaxon:183924"}; line 2648: {"taxon_id":"NCBITaxon:12914","label":"Acidianus","rank":"GENUS","parent_id":"NCBITaxon:118883"}; line 2980: {"taxon_id":"NCBITaxon:28889","label":"Thermoproteota","rank":"PHYLUM","parent_id":"NCBITaxon:1783275"}; line 22254: {"taxon_id":"NCBITaxon:118883","label":"Sulfolobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2281"}; line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"}; line 36612: {"taxon_id":"NCBITaxon:183924","label":"Thermoprotei","rank":"CLASS","parent_id":"NCBITaxon:28889"}; line 396703: {"taxon_id":"NCBITaxon:1540082","label":"Acidianus sp. RZ1","rank":"SPECIES","parent_id":"NCBITaxon:2629519","genetic_code":"11","exact_synonyms":"Acidianus sp. DSM 29099","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb&#124;mediadive&#124;gold","retired_into":"","taxonomy_snapshot":"2026-09-13"}; line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"}; line 538477: {"taxon_id":"NCBITaxon:2629519","label":"unclassified Acidianus","rank":"NO_RANK","parent_id":"NCBITaxon:12914"} | supports | Inspected the target and each carried ancestor, rank, parent, genetic code and source name classes. |
| scope-row | curation/seed_scope.tsv; line 15903: {"identifier":"NCBITaxon:1540082","added":"2026-09-12","reason":"attested rule: Acidianus sp. RZ1, 5 sources incl. NCBI"} | supports | Exact target is included in the declared seed scope. |
| path-row | data/taxa/PATHS.tsv; line 200999: {"identifier":"NCBITaxon:1540082","slug":"acidianus_sp_rz1"} | supports | Indexed path resolves to this exact NCBI taxon. |
| ncbi-live | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1540082,1071530,312539,619593,146920,518068,2933264,1915614,1915615,2268176; TaxaSet/Taxon[TaxId='1540082']; ten-target captured response | supports | Inspected the official response for this exact taxon: scientific name, rank, parent, source name classes, lineage and genetic code. Current authority and pinned September inventory remain distinct observations. |
| lpsn-inventory | data/raw/lpsn_names.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected exact mapped and linked LPSN names; bounded inventory absence does not establish worldwide nomenclatural absence. |
| gtdb-mappings | data/raw/gtdb_mappings.tsv; line 8805: {"gtdb_id":"GTDB:s__Acidianus_copahuensis","gtdb_label":"s__Acidianus_copahuensis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:1160895","predicate":"skos:closeMatch","genome_count":"2"}; line 36240: {"gtdb_id":"GTDB:s__Acidianus_copahuensis","gtdb_label":"s__Acidianus_copahuensis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:1540082","predicate":"skos:closeMatch","genome_count":"2"} | supports | Inspected direct mappings and selected clusters' reverse mappings, retaining each source predicate and taxon boundary. |
| gtdb-species | data/raw/gtdb_species.tsv; line 3493: {"gtdb_id":"GTDB:s__Acidianus_copahuensis","label":"s__Acidianus_copahuensis","parent":"GTDB:g__Acidianus","genome_count":"2"} | supports | Inspected source species identifiers, labels, parent clusters and genome counts. |
| bacdive-inventory | data/raw/bacdive_strains.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Complete inventory selection covers the exact target and descendants from the complete NCBI parent graph; its imported strain population was compared with the complete YAML. |
| culture-inventory | data/raw/culture_collection_strains.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected exact culture-inventory associations; an isolate name or genome does not create an inferred deposit. |
| gold-organisms | data/raw/gold_organisms.tsv; line 12258: {"taxon_id":"NCBITaxon:1540082","organism_count":"1"} | supports | Inspected the exact GOLD organism count row or bounded absence, without converting counts to phenotypes. |
| mediadive-taxa | data/raw/mediadive_taxa.tsv; line 4261: {"taxon_id":"NCBITaxon:1540082","medium_count":"2","media_ids":"mediadive.medium:88&#124;mediadive.medium:J176"} | supports | Inspected the exact MediaDive medium count row or bounded absence, without converting counts to phenotypes. |
| madin-taxa | data/raw/madin_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact Madin trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| bactotraits-taxa | data/raw/bactotraits_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact BactoTraits trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| mapping-policy | docs/HARMONIZATION.md; Mapping predicates; Which strains belong to a record | supports | Policy permits one-to-one species closeMatch normalization and LPSN-linked species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage unchanged. |
| equivalence-contract | src/taxonmech/schema/taxonmech.yaml; TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439 | supports | TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes under the source taxon. |
| seed-owner | src/taxonmech/seed.py; GTDB mapping construction lines 440–472; LPSN/type-strain and source-attestation construction | supports | Inspected mapping ranking, qualified predicates, fixed broadMatch wording, synonym/xref construction, primary cluster counts and same-taxon type-strain derivation. |
| manifest | data/raw/MANIFEST.yaml; kg_microbe_source, inputs, extracted_at | supports | Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd, upstream input hashes and extraction time 2026-09-13T17:50:44Z. |
| overlay-manifests | data/atb/MANIFEST.yaml; extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml | supports | Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z, matching the sole seed event. StrainInfo manifest is independently captured in source.inputs. |
| lpsn-copahuensis | https://lpsn.dsmz.de/species/acidianus-copahuensis; Name, nomenclatural status or strain identity and source associations | supports | NCBI supplies Acidianus sp. DSM 29099 as an exact synonym. The captured DSMZ catalogue explicitly identifies DSM 29099 as Acidianus copahuensis, designation RZ1, other deposit JCM 30227, with history Acidianus sp. RZ1. BacDive 131324 uses the copahuensis taxon 1160895 while its sequence fields retain 1540082; these source boundaries are preserved. LPSN treats Candidatus Acidianus copahuensis as not validly published with pro-valid/pro-correct status and type ALE1. This does not make RZ1 the type strain or merge the two NCBI identities. |
| dsm-29099 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-29099; Name, nomenclatural status or strain identity and source associations | supports | NCBI supplies Acidianus sp. DSM 29099 as an exact synonym. The captured DSMZ catalogue explicitly identifies DSM 29099 as Acidianus copahuensis, designation RZ1, other deposit JCM 30227, with history Acidianus sp. RZ1. BacDive 131324 uses the copahuensis taxon 1160895 while its sequence fields retain 1540082; these source boundaries are preserved. LPSN treats Candidatus Acidianus copahuensis as not validly published with pro-valid/pro-correct status and type ALE1. This does not make RZ1 the type strain or merge the two NCBI identities. |
| mediadive-dsm-29099 | https://mediadive.dsmz.de/strains/view/DSM%2029099; Name, nomenclatural status or strain identity and source associations | supports | The captured DSM 29099 page lists media 88 and J176; current association is distinct from historical aggregate reproduction. |
| rz1-genome-1 | data/catalog/gtdb_genomes-0017.jsonl.gz; line 29090: {"accession":"RS_GCF_000632495.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus copahuensis","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"AciCop1.0","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN02679956","ncbi_contig_count":"68","ncbi_contig_n50":"136672","ncbi_country":"Argentina: Copahue; Neuquen","ncbi_date":"2014-04-15","ncbi_genbank_assembly_accession":"GCA_000632495.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"hot springs","ncbi_lat_lon":"37.816611 S 71.096811 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Candidatus Acidianus copahuensis","ncbi_protein_count":"2461","ncbi_refseq_category":"reference genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2014-04-15","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1160895","ncbi_ssu_count":"1","ncbi_strain_identifiers":"ALE1","ncbi_submitter":"INDEAR","ncbi_taxid":"1160895","ncbi_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Candidatus Acidianus copahuensis","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Thermoproteota;c__Thermoprotei;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Candidatus Acidianus copahuensis","ncbi_total_gap_length":"0","ncbi_total_length":"2454023","ncbi_translation_table":"11","ncbi_trna_count":"52","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2454023","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JFZT00000000.1"}; line 41393: {"accession":"RS_GCF_013133895.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus copahuensis","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM1313389v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN14829352","ncbi_contig_count":"746","ncbi_contig_n50":"5549","ncbi_country":"Argentina","ncbi_date":"2020-05-20","ncbi_genbank_assembly_accession":"GCA_013133895.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"hot spring","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Acidianus sp. RZ1","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2020-05-20","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1540082","ncbi_ssu_count":"1","ncbi_strain_identifiers":"DSM 29099","ncbi_submitter":"Federal Institute for Geosciences and Natural Resources","ncbi_taxid":"1540082","ncbi_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Thermoproteota;c__Thermoprotei;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;x__unclassified Acidianus;s__Acidianus sp. RZ1","ncbi_total_gap_length":"0","ncbi_total_length":"2366205","ncbi_translation_table":"11","ncbi_trna_count":"27","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2366205","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JABGBQ000000000.1"} | supports | Complete selected primary objects were inspected with their source taxon, deposit and accession boundaries retained. The complete pinned subtree has no descendants or directly classified BacDive entries. BacDive 131324 is filed under 1160895, so its related RZ1 designation does not authorize importing it under 1540082. NCBI 1 NAME, GTDB 2 GENOME, MediaDive 2 MEDIUM and GOLD 1 ORGANISM agree with the pinned inventories. The current DSM 29099 MediaDive page lists 88 and J176; GOLD Go0566671 explicitly carries DSM 29099 and taxon 1540082. Current supporting objects do not reproduce the historical edge snapshot. |
| rz1-bacdive-1 | data/bacdive/records.jsonl.gz; line 53634: {"General":{"@ref":22551,"BacDive-ID":131324,"NCBI tax id":{"Matching level":"species","NCBI tax id":1160895},"doi":"10.13145/bacdive131324.20260601.11"},"Literature":{"@ref":22551,"culture collection no.":"DSM 29099, JCM 30227","straininfo link":{"@ref":126262,"straininfo":408356}},"Name and taxonomic classification":{"@ref":22551,"LPSN":{"@ref":20215,"class":"Thermoprotei","description":"domain/archaea","domain":"Archaea","family":"Sulfolobaceae","full scientific name":"&lt;I&gt;Candidatus&lt;/I&gt; Acidianus copahuensis Giaveno et al. 2013","genus":"Acidianus","keyword":"phylum/thermoproteota","order":"Sulfolobales","phylum":"Thermoproteota","species":"Acidianus copahuensis"},"class":"Thermoprotei","domain":"Archaea","family":"Sulfolobaceae","full scientific name":"Acidianus copahuensis Giaveno et al. 2013","genus":"Acidianus","order":"Sulfolobales","phylum":"Crenarchaeota","species":"Acidianus copahuensis","strain designation":"RZ1","type strain":"no"},"Sequence information":{"16S sequences":{"@ref":22551,"NCBI tax ID":1540082,"accession":"KJ921703","database":"nuccore","description":"Acidianus sp. RZ1 16S ribosomal RNA gene, partial sequence","length":934},"Genome sequences":{"@ref":67770,"BV-BRC accession":"2732866.3","IMG accession":"8065317240","INSDC accession":"GCA_013133895","NCBI tax ID":1540082,"assembly level":"contig","description":"ASM1313389v1 assembly for Acidianus sp. RZ1 DSM 29099","score":0}}} | supports | Complete selected primary objects were inspected with their source taxon, deposit and accession boundaries retained. The complete pinned subtree has no descendants or directly classified BacDive entries. BacDive 131324 is filed under 1160895, so its related RZ1 designation does not authorize importing it under 1540082. NCBI 1 NAME, GTDB 2 GENOME, MediaDive 2 MEDIUM and GOLD 1 ORGANISM agree with the pinned inventories. The current DSM 29099 MediaDive page lists 88 and J176; GOLD Go0566671 explicitly carries DSM 29099 and taxon 1540082. Current supporting objects do not reproduce the historical edge snapshot. |
| rz1-gold-1 | data/gold/organisms.jsonl.gz; line 402244: {"ORGANISM CULTURE COLLECTION ID":"DSM 29099","ORGANISM GOLD ID":"Go0566671","ORGANISM NAME":"Acidianus sp. RZ1 DSM 29099","ORGANISM NCBI TAX ID":"1540082","ORGANISM STRAIN":"DSM 29099"} | supports | Complete selected primary objects were inspected with their source taxon, deposit and accession boundaries retained. The complete pinned subtree has no descendants or directly classified BacDive entries. BacDive 131324 is filed under 1160895, so its related RZ1 designation does not authorize importing it under 1540082. NCBI 1 NAME, GTDB 2 GENOME, MediaDive 2 MEDIUM and GOLD 1 ORGANISM agree with the pinned inventories. The current DSM 29099 MediaDive page lists 88 and J176; GOLD Go0566671 explicitly carries DSM 29099 and taxon 1540082. Current supporting objects do not reproduce the historical edge snapshot. |
| historical-edge-1 | data/raw/MANIFEST.yaml; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/mediadive/edges.tsv; expected=78ea275a59d4e2de09a9cf72652ec64454c6a111d2defa1ae0a44bac8a72e523; observed=4e933d1e2412fb1aad74e60719a6a64dfa34862ff0a6b84e93d78da5ce13dd8b | partial | Configured historical input exists with a different hash. This reuses the earlier actual receipt and does not claim a fresh or worldwide search. |
| historical-edge-2 | data/raw/MANIFEST.yaml; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/gold/edges.tsv; expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12; observed=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d | partial | Configured historical input exists with a different hash. This reuses the earlier actual receipt and does not claim a fresh or worldwide search. |
| qc-setup-receipt | just qc; initial setup attempt, 2026-10-19T07:17:01Z through 2026-10-19T07:17:01Z | context_only | Initial actual invocation from /private/tmp/taxonmech-record-reviews-k0MubV/repo exited 1 because ruff was absent. Locked ruff 0.16.7 was installed only in that isolated environment before the complete retry. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| strict-receipt | just validate-strict data/taxa/archaea/acidianus_sp_rz1.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/strict-01.tsv; This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/repo; started 2026-10-19T23:34:38Z, finished 2026-10-19T23:34:41Z, exit 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times.<br>Validating 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/strict-01.tsv |
| history-receipt | just validate-history; All 17 standalone history records; the generated seed event was also inspected in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:01Z, finished 2026-10-19T07:17:03Z, exit 0. All 17 standalone history records; the generated seed event was also inspected in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>history links: 17 record(s), 0 invalid<br>No issues found<br>17 history record(s) valid against src/taxonmech/schema/history.yaml |
| corpus-receipt | just verify-corpus; All 625,960 generated taxon YAMLs, not a focused approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:18:23Z, finished 2026-10-19T07:24:12Z, exit 0. All 625,960 generated taxon YAMLs, not a focused approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>uv run python scripts/verify_corpus.py <br>expected 625960 records, found 625960 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ and curation/seed_scope.tsv |
| products-receipt | just validate-products; Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:01Z, finished 2026-10-19T07:55:11Z, exit 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml<br><br>id↔label correspondence summary:<br><br>✅ All id↔label pairs correspond. |
| qc-receipt | just qc; Repository-wide just qc, including native corpus-wide checks. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:41Z, finished 2026-10-19T08:07:39Z, exit 0. Repository-wide just qc, including native corpus-wide checks. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>1055 passed, 3 skipped, 5 deselected in 1634.00s (0:27:13)<br>Validating 625960 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml<br>  files scanned:      625960<br>expected 625960 records, found 625960 on disk<br>pages/ is current<br>Site publication: 530,864,122 bytes (budget 950,000,000)<br>625960 taxon records<br>  NCBITAXON        625960<br>All TaxonMech quality gates passed.<br>  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890 strains (not genome counts)<br>  Related STRAININFO_DEPOSIT: 107277 strain-record pairs, 106843 identifiers, 53890 strains (not genome counts)<br>  Related NUCLEOTIDE_SEQUENCE: 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)<br>LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809 records mapped, 324404579 genomes summed across record attestations (not deduplicated)<br>Causal graphs: 0 records (0 evidence-backed edges)<br><br>All TaxonMech quality gates passed. |

## Limits And Additional Notes

- Source assertions are scoped to the captured inputs and access times. The review does not independently establish phylogenetic species boundaries, infer physical deposit/assembly equivalence, or infer mechanisms from names.
- No imported strains means no matching entry under the maintained pinned taxon/subtree rule; it is not a worldwide strain census.
- Required independent historical aggregate verification remains unavailable: the configured original kg-microbe edge paths were found with bytes differing from the manifest-pinned hashes. Current source pages and primary projections do not substitute for that extraction snapshot.
- Authority page metadata was inspected; original publication full texts and sequence records were not independently reassessed for these contextual names.
- Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base canonical recapture preserved all previously reviewed input hashes; original captures and actual transition receipts remain retained.
- Every new bundle still requires its own validate/save/check recipe; baseline native receipts do not claim these later steps have run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T033044Z-acidianus_sp_rz1
kind: record
repository: CultureBotAI/TaxonMech
title: 'Record review: Acidianus sp. RZ1'
started_at: '2026-10-19T23:34:32Z'
finished_at: '2026-10-20T03:30:44Z'
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
summary: The RZ1 species record has supported NCBI identity and a locally permitted
  GTDB species naming link, corroborated by the DSM 29099 culture history. No record-specific
  defect was established; original GOLD and MediaDive aggregate verification remains
  incomplete.
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
  - path: data/bacdive/records.jsonl.gz
    sha256: b27d0f50f06aa33615e7cc2aae4acb7c2767df930c85292e76fbb462ac136080
    role: context
  - path: data/catalog/MANIFEST.json
    sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
    role: context
  - path: data/catalog/gtdb_genomes-0017.jsonl.gz
    sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
    role: context
  - path: data/catalog/gtdb_genomes-0018.jsonl.gz
    sha256: 8baa314877815777abcdf600079c6ee42f2ea5340398df9f2e18de9c18fd4347
    role: context
  - path: data/gold/organisms.jsonl.gz
    sha256: 8c1a055214cb240c58fadda0815efbefcb60848245e8a7474e6b1b41d123235c
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
  - path: data/taxa/archaea/acidianus_sp_rz1.yaml
    sha256: e3923ad8c3f13c8ed842775a7e9cb5e6873d3d0a077bc21f6179024ba86fb967
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
  - path: tests/test_seed.py
    sha256: df25fd35d9f8e714b105f20642975e35a6ee57941e763cd7a6bc6a6166e89d17
    role: context
scope:
  description: Entire single generated record, including all source assertions and
    imported strains.
  selection: Original unreviewed path-order position 21; batch-0003 target 1. Excluded
    72 actual targets from validated main and local batch-0001/0002 listings; full
    corpus enumeration includes ignored files.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - NCBITaxon:1540082
targets:
- target_id: NCBITaxon:1540082
  path: data/taxa/archaea/acidianus_sp_rz1.yaml
  label: Acidianus sp. RZ1
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
  summary: NCBITaxon:1540082 denotes Acidianus sp. RZ1 at SPECIES rank, parent NCBITaxon:2629519,
    genetic code 11, with 10 carried ancestors. All lineage IDs, names and ranks agree
    with the pinned inventory and captured NCBI EFetch, accounting for EFetch's omission
    of root.
  target_ids:
  - NCBITaxon:1540082
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - scope-row
  - path-row
- check_id: strain-genome-evidence
  name: Imported strain and genome assertion check
  status: not_applicable
  required: false
  summary: No imported BacDive strain or strain-level genome assertion is present.
    Exact source inventory/subtree selection was checked. An external strain classified
    elsewhere or a genome/isolate name does not create an imported physical deposit.
  target_ids:
  - NCBITaxon:1540082
  evidence_ids:
  - record
  - bacdive-inventory
  - culture-inventory
- check_id: complete-inventory-search
  name: Complete identifier and name inventory search
  status: passed
  required: true
  summary: The complete pinned subtree has no descendants or directly classified BacDive
    entries. BacDive 131324 is filed under 1160895, so its related RZ1 designation
    does not authorize importing it under 1540082. NCBI 1 NAME, GTDB 2 GENOME, MediaDive
    2 MEDIUM and GOLD 1 ORGANISM agree with the pinned inventories. The current DSM
    29099 MediaDive page lists 88 and J176; GOLD Go0566671 explicitly carries DSM
    29099 and taxon 1540082. Current supporting objects do not reproduce the historical
    edge snapshot.
  target_ids:
  - NCBITaxon:1540082
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - scope-row
  - path-row
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
  - lpsn-inventory
  - bacdive-inventory
  - culture-inventory
  scope_note: Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. RZ1 also searches related copahuensis taxid and culture deposits, reported
    as related classification not direct target rows. All claims of no rows are limited
    to these complete pinned inputs.
- check_id: historical-source-counts
  name: Original manifest-pinned aggregate edge counts
  status: unavailable
  required: true
  summary: Pinned inventories agree with the generated assertions, but original matching
    edge bytes are unavailable in the checked locations for gold, mediadive. Current
    sources cannot reproduce that historical extraction.
  target_ids:
  - NCBITaxon:1540082
  evidence_ids:
  - manifest
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
  - historical-edge-1
  - historical-edge-2
- check_id: qc-setup-attempt
  name: Initial quality-gate setup attempt
  status: failed
  required: false
  summary: 'Actual exit 1: missing ruff; superseded by the separately recorded successful
    full retry.'
  target_ids:
  - NCBITaxon:1540082
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
  - NCBITaxon:1540082
  evidence_ids:
  - strict-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/uv-cache
    just validate-strict data/taxa/archaea/acidianus_sp_rz1.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/strict-01.tsv
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
  - NCBITaxon:1540082
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
  - NCBITaxon:1540082
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
  - NCBITaxon:1540082
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
  - NCBITaxon:1540082
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
  reference: data/taxa/archaea/acidianus_sp_rz1.yaml
  accessed_at: '2026-10-20T03:30:44Z'
  support: supports
  summary: Read the entire generated YAML, including identity, lineage, names, mappings,
    source attestations, all imported strains and links, and seed history.
  locator: entire TaxonRecord; identifier=NCBITaxon:1540082
  snapshot_sha256: e3923ad8c3f13c8ed842775a7e9cb5e6873d3d0a077bc21f6179024ba86fb967
- evidence_id: taxonomy-inventory
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-19T23:34:33Z'
  support: supports
  summary: Inspected the target and each carried ancestor, rank, parent, genetic code
    and source name classes.
  locator: 'line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""};
    line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"};
    line 1798: {"taxon_id":"NCBITaxon:2281","label":"Sulfolobales","rank":"ORDER","parent_id":"NCBITaxon:183924"};
    line 2648: {"taxon_id":"NCBITaxon:12914","label":"Acidianus","rank":"GENUS","parent_id":"NCBITaxon:118883"};
    line 2980: {"taxon_id":"NCBITaxon:28889","label":"Thermoproteota","rank":"PHYLUM","parent_id":"NCBITaxon:1783275"};
    line 22254: {"taxon_id":"NCBITaxon:118883","label":"Sulfolobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2281"};
    line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"};
    line 36612: {"taxon_id":"NCBITaxon:183924","label":"Thermoprotei","rank":"CLASS","parent_id":"NCBITaxon:28889"};
    line 396703: {"taxon_id":"NCBITaxon:1540082","label":"Acidianus sp. RZ1","rank":"SPECIES","parent_id":"NCBITaxon:2629519","genetic_code":"11","exact_synonyms":"Acidianus
    sp. DSM 29099","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon|gtdb|mediadive|gold","retired_into":"","taxonomy_snapshot":"2026-09-13"};
    line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"};
    line 538477: {"taxon_id":"NCBITaxon:2629519","label":"unclassified Acidianus","rank":"NO_RANK","parent_id":"NCBITaxon:12914"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
- evidence_id: scope-row
  kind: database
  reference: curation/seed_scope.tsv
  accessed_at: '2026-10-19T23:34:33Z'
  support: supports
  summary: Exact target is included in the declared seed scope.
  locator: 'line 15903: {"identifier":"NCBITaxon:1540082","added":"2026-09-12","reason":"attested
    rule: Acidianus sp. RZ1, 5 sources incl. NCBI"}'
  snapshot_sha256: 5fdc0f7111b64e02439d95c6f2b51fcff1d2154c34b2d957422dd9b297e94d4b
- evidence_id: path-row
  kind: database
  reference: data/taxa/PATHS.tsv
  accessed_at: '2026-10-19T23:34:33Z'
  support: supports
  summary: Indexed path resolves to this exact NCBI taxon.
  locator: 'line 200999: {"identifier":"NCBITaxon:1540082","slug":"acidianus_sp_rz1"}'
  snapshot_sha256: c950844feb0638ce04f7349784749dd1d728fe70bc80f7e2756d956d4ecea254
- evidence_id: ncbi-live
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1540082,1071530,312539,619593,146920,518068,2933264,1915614,1915615,2268176
  accessed_at: '2026-10-19T23:34:56Z'
  support: supports
  summary: 'Inspected the official response for this exact taxon: scientific name,
    rank, parent, source name classes, lineage and genetic code. Current authority
    and pinned September inventory remain distinct observations.'
  locator: TaxaSet/Taxon[TaxId='1540082']; ten-target captured response
  snapshot_sha256: 99397970b64f5c68856c849b0cf98a385c6a79d2af56761ed2043bd65693d471
- evidence_id: lpsn-inventory
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-19T23:34:33Z'
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
  accessed_at: '2026-10-19T23:34:33Z'
  support: supports
  summary: Inspected direct mappings and selected clusters' reverse mappings, retaining
    each source predicate and taxon boundary.
  locator: 'line 8805: {"gtdb_id":"GTDB:s__Acidianus_copahuensis","gtdb_label":"s__Acidianus_copahuensis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:1160895","predicate":"skos:closeMatch","genome_count":"2"};
    line 36240: {"gtdb_id":"GTDB:s__Acidianus_copahuensis","gtdb_label":"s__Acidianus_copahuensis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:1540082","predicate":"skos:closeMatch","genome_count":"2"}'
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
- evidence_id: gtdb-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-19T23:34:33Z'
  support: supports
  summary: Inspected source species identifiers, labels, parent clusters and genome
    counts.
  locator: 'line 3493: {"gtdb_id":"GTDB:s__Acidianus_copahuensis","label":"s__Acidianus_copahuensis","parent":"GTDB:g__Acidianus","genome_count":"2"}'
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
- evidence_id: bacdive-inventory
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-19T23:34:33Z'
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
  accessed_at: '2026-10-19T23:34:33Z'
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
  accessed_at: '2026-10-19T23:34:33Z'
  support: supports
  summary: Inspected the exact GOLD organism count row or bounded absence, without
    converting counts to phenotypes.
  locator: 'line 12258: {"taxon_id":"NCBITaxon:1540082","organism_count":"1"}'
  snapshot_sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
- evidence_id: mediadive-taxa
  kind: database
  reference: data/raw/mediadive_taxa.tsv
  accessed_at: '2026-10-19T23:34:33Z'
  support: supports
  summary: Inspected the exact MediaDive medium count row or bounded absence, without
    converting counts to phenotypes.
  locator: 'line 4261: {"taxon_id":"NCBITaxon:1540082","medium_count":"2","media_ids":"mediadive.medium:88|mediadive.medium:J176"}'
  snapshot_sha256: 3f74b78cadfcdb6aeae953e09fdb39e34fd9c5d5ed0be65a04a5d7fb02355905
- evidence_id: madin-taxa
  kind: database
  reference: data/raw/madin_taxa.tsv
  accessed_at: '2026-10-19T23:34:33Z'
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
  accessed_at: '2026-10-19T23:34:33Z'
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
  accessed_at: '2026-10-20T03:30:44Z'
  support: supports
  summary: Policy permits one-to-one species closeMatch normalization and LPSN-linked
    species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage
    unchanged.
  locator: Mapping predicates; Which strains belong to a record
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
- evidence_id: equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-20T03:30:44Z'
  support: supports
  summary: TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations
    remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes
    under the source taxon.
  locator: TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
- evidence_id: seed-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-20T03:30:44Z'
  support: supports
  summary: Inspected mapping ranking, qualified predicates, fixed broadMatch wording,
    synonym/xref construction, primary cluster counts and same-taxon type-strain derivation.
  locator: GTDB mapping construction lines 440–472; LPSN/type-strain and source-attestation
    construction
  snapshot_sha256: 6b5b065f4ae7aea022af736a22c0f63dc58a2425c7ee453259e567ab030f8257
- evidence_id: manifest
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-20T03:30:44Z'
  support: supports
  summary: Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd,
    upstream input hashes and extraction time 2026-09-13T17:50:44Z.
  locator: kg_microbe_source, inputs, extracted_at
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
- evidence_id: overlay-manifests
  kind: record_content
  reference: data/atb/MANIFEST.yaml
  accessed_at: '2026-10-20T03:30:44Z'
  support: supports
  summary: Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z,
    matching the sole seed event. StrainInfo manifest is independently captured in
    source.inputs.
  locator: extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml
  snapshot_sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
- evidence_id: lpsn-copahuensis
  kind: authority
  reference: https://lpsn.dsmz.de/species/acidianus-copahuensis
  accessed_at: '2026-10-19T23:40:47Z'
  support: supports
  summary: NCBI supplies Acidianus sp. DSM 29099 as an exact synonym. The captured
    DSMZ catalogue explicitly identifies DSM 29099 as Acidianus copahuensis, designation
    RZ1, other deposit JCM 30227, with history Acidianus sp. RZ1. BacDive 131324 uses
    the copahuensis taxon 1160895 while its sequence fields retain 1540082; these
    source boundaries are preserved. LPSN treats Candidatus Acidianus copahuensis
    as not validly published with pro-valid/pro-correct status and type ALE1. This
    does not make RZ1 the type strain or merge the two NCBI identities.
  locator: Name, nomenclatural status or strain identity and source associations
  snapshot_sha256: 9d47ac9ffcc7277969961c712a92c2482479ef181f58a707a1c9949302b392d2
- evidence_id: dsm-29099
  kind: authority
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-29099
  accessed_at: '2026-10-19T23:40:48Z'
  support: supports
  summary: NCBI supplies Acidianus sp. DSM 29099 as an exact synonym. The captured
    DSMZ catalogue explicitly identifies DSM 29099 as Acidianus copahuensis, designation
    RZ1, other deposit JCM 30227, with history Acidianus sp. RZ1. BacDive 131324 uses
    the copahuensis taxon 1160895 while its sequence fields retain 1540082; these
    source boundaries are preserved. LPSN treats Candidatus Acidianus copahuensis
    as not validly published with pro-valid/pro-correct status and type ALE1. This
    does not make RZ1 the type strain or merge the two NCBI identities.
  locator: Name, nomenclatural status or strain identity and source associations
  snapshot_sha256: f66d700fcbb8e818e031c9832131d1e936bdd8d5a9ca3fd108070095d9fbddf8
- evidence_id: mediadive-dsm-29099
  kind: authority
  reference: https://mediadive.dsmz.de/strains/view/DSM%2029099
  accessed_at: '2026-10-19T23:40:48Z'
  support: supports
  summary: The captured DSM 29099 page lists media 88 and J176; current association
    is distinct from historical aggregate reproduction.
  locator: Name, nomenclatural status or strain identity and source associations
  snapshot_sha256: e9c1cb3eb85aa7d7a95b7fcc4962d2d310d08c18f77ed94295004e98ac55a573
- evidence_id: rz1-genome-1
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0017.jsonl.gz
  accessed_at: '2026-10-19T23:43:10Z'
  support: supports
  summary: Complete selected primary objects were inspected with their source taxon,
    deposit and accession boundaries retained. The complete pinned subtree has no
    descendants or directly classified BacDive entries. BacDive 131324 is filed under
    1160895, so its related RZ1 designation does not authorize importing it under
    1540082. NCBI 1 NAME, GTDB 2 GENOME, MediaDive 2 MEDIUM and GOLD 1 ORGANISM agree
    with the pinned inventories. The current DSM 29099 MediaDive page lists 88 and
    J176; GOLD Go0566671 explicitly carries DSM 29099 and taxon 1540082. Current supporting
    objects do not reproduce the historical edge snapshot.
  locator: 'line 29090: {"accession":"RS_GCF_000632495.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    copahuensis","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"AciCop1.0","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN02679956","ncbi_contig_count":"68","ncbi_contig_n50":"136672","ncbi_country":"Argentina:
    Copahue; Neuquen","ncbi_date":"2014-04-15","ncbi_genbank_assembly_accession":"GCA_000632495.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"hot
    springs","ncbi_lat_lon":"37.816611 S 71.096811 W","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Candidatus
    Acidianus copahuensis","ncbi_protein_count":"2461","ncbi_refseq_category":"reference
    genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2014-04-15","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1160895","ncbi_ssu_count":"1","ncbi_strain_identifiers":"ALE1","ncbi_submitter":"INDEAR","ncbi_taxid":"1160895","ncbi_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Candidatus
    Acidianus copahuensis","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Thermoproteota;c__Thermoprotei;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Candidatus
    Acidianus copahuensis","ncbi_total_gap_length":"0","ncbi_total_length":"2454023","ncbi_translation_table":"11","ncbi_trna_count":"52","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2454023","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JFZT00000000.1"};
    line 41393: {"accession":"RS_GCF_013133895.1","gtdb_representative":"f","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    copahuensis","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Contig","ncbi_assembly_name":"ASM1313389v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN14829352","ncbi_contig_count":"746","ncbi_contig_n50":"5549","ncbi_country":"Argentina","ncbi_date":"2020-05-20","ncbi_genbank_assembly_accession":"GCA_013133895.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"hot
    spring","ncbi_lat_lon":"none","ncbi_molecule_count":"0","ncbi_ncrna_count":"0","ncbi_organism_name":"Acidianus
    sp. RZ1","ncbi_protein_count":"none","ncbi_refseq_category":"na","ncbi_rrna_count":"3","ncbi_scaffold_count":"none","ncbi_scaffold_l50":"none","ncbi_scaffold_n50":"none","ncbi_scaffold_n75":"none","ncbi_scaffold_n90":"none","ncbi_seq_rel_date":"2020-05-20","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1540082","ncbi_ssu_count":"1","ncbi_strain_identifiers":"DSM
    29099","ncbi_submitter":"Federal Institute for Geosciences and Natural Resources","ncbi_taxid":"1540082","ncbi_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Thermoproteota;c__Thermoprotei;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;x__unclassified
    Acidianus;s__Acidianus sp. RZ1","ncbi_total_gap_length":"0","ncbi_total_length":"2366205","ncbi_translation_table":"11","ncbi_trna_count":"27","ncbi_type_material_designation":"na","ncbi_ungapped_length":"2366205","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"JABGBQ000000000.1"}'
  snapshot_sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
- evidence_id: rz1-bacdive-1
  kind: primary_source
  reference: data/bacdive/records.jsonl.gz
  accessed_at: '2026-10-19T23:43:10Z'
  support: supports
  summary: Complete selected primary objects were inspected with their source taxon,
    deposit and accession boundaries retained. The complete pinned subtree has no
    descendants or directly classified BacDive entries. BacDive 131324 is filed under
    1160895, so its related RZ1 designation does not authorize importing it under
    1540082. NCBI 1 NAME, GTDB 2 GENOME, MediaDive 2 MEDIUM and GOLD 1 ORGANISM agree
    with the pinned inventories. The current DSM 29099 MediaDive page lists 88 and
    J176; GOLD Go0566671 explicitly carries DSM 29099 and taxon 1540082. Current supporting
    objects do not reproduce the historical edge snapshot.
  locator: 'line 53634: {"General":{"@ref":22551,"BacDive-ID":131324,"NCBI tax id":{"Matching
    level":"species","NCBI tax id":1160895},"doi":"10.13145/bacdive131324.20260601.11"},"Literature":{"@ref":22551,"culture
    collection no.":"DSM 29099, JCM 30227","straininfo link":{"@ref":126262,"straininfo":408356}},"Name
    and taxonomic classification":{"@ref":22551,"LPSN":{"@ref":20215,"class":"Thermoprotei","description":"domain/archaea","domain":"Archaea","family":"Sulfolobaceae","full
    scientific name":"<I>Candidatus</I> Acidianus copahuensis Giaveno et al. 2013","genus":"Acidianus","keyword":"phylum/thermoproteota","order":"Sulfolobales","phylum":"Thermoproteota","species":"Acidianus
    copahuensis"},"class":"Thermoprotei","domain":"Archaea","family":"Sulfolobaceae","full
    scientific name":"Acidianus copahuensis Giaveno et al. 2013","genus":"Acidianus","order":"Sulfolobales","phylum":"Crenarchaeota","species":"Acidianus
    copahuensis","strain designation":"RZ1","type strain":"no"},"Sequence information":{"16S
    sequences":{"@ref":22551,"NCBI tax ID":1540082,"accession":"KJ921703","database":"nuccore","description":"Acidianus
    sp. RZ1 16S ribosomal RNA gene, partial sequence","length":934},"Genome sequences":{"@ref":67770,"BV-BRC
    accession":"2732866.3","IMG accession":"8065317240","INSDC accession":"GCA_013133895","NCBI
    tax ID":1540082,"assembly level":"contig","description":"ASM1313389v1 assembly
    for Acidianus sp. RZ1 DSM 29099","score":0}}}'
  snapshot_sha256: b27d0f50f06aa33615e7cc2aae4acb7c2767df930c85292e76fbb462ac136080
- evidence_id: rz1-gold-1
  kind: primary_source
  reference: data/gold/organisms.jsonl.gz
  accessed_at: '2026-10-19T23:43:10Z'
  support: supports
  summary: Complete selected primary objects were inspected with their source taxon,
    deposit and accession boundaries retained. The complete pinned subtree has no
    descendants or directly classified BacDive entries. BacDive 131324 is filed under
    1160895, so its related RZ1 designation does not authorize importing it under
    1540082. NCBI 1 NAME, GTDB 2 GENOME, MediaDive 2 MEDIUM and GOLD 1 ORGANISM agree
    with the pinned inventories. The current DSM 29099 MediaDive page lists 88 and
    J176; GOLD Go0566671 explicitly carries DSM 29099 and taxon 1540082. Current supporting
    objects do not reproduce the historical edge snapshot.
  locator: 'line 402244: {"ORGANISM CULTURE COLLECTION ID":"DSM 29099","ORGANISM GOLD
    ID":"Go0566671","ORGANISM NAME":"Acidianus sp. RZ1 DSM 29099","ORGANISM NCBI TAX
    ID":"1540082","ORGANISM STRAIN":"DSM 29099"}'
  snapshot_sha256: 8c1a055214cb240c58fadda0815efbefcb60848245e8a7474e6b1b41d123235c
- evidence_id: historical-edge-1
  kind: search
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T07:30:21Z'
  support: partial
  summary: Configured historical input exists with a different hash. This reuses the
    earlier actual receipt and does not claim a fresh or worldwide search.
  locator: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/mediadive/edges.tsv;
    expected=78ea275a59d4e2de09a9cf72652ec64454c6a111d2defa1ae0a44bac8a72e523; observed=4e933d1e2412fb1aad74e60719a6a64dfa34862ff0a6b84e93d78da5ce13dd8b
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
  search_scope: Exact configured historical input path including ignored files; bounded
    to the earlier recorded locations.
- evidence_id: historical-edge-2
  kind: search
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T07:30:22Z'
  support: partial
  summary: Configured historical input exists with a different hash. This reuses the
    earlier actual receipt and does not claim a fresh or worldwide search.
  locator: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/gold/edges.tsv;
    expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12; observed=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
  search_scope: Exact configured historical input path including ignored files; bounded
    to the earlier recorded locations.
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
  reference: just validate-strict data/taxa/archaea/acidianus_sp_rz1.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/strict-01.tsv
  accessed_at: '2026-10-19T23:34:41Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/repo;\
    \ started 2026-10-19T23:34:38Z, finished 2026-10-19T23:34:41Z, exit 0. This exact\
    \ generated YAML only; its captured bytes remain unchanged. Actual earlier per-target\
    \ invocation; the receipt retains its original cwd and times.\nValidating 1 files\
    \ with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/strict-01.tsv"
  locator: This exact generated YAML only; its captured bytes remain unchanged. Actual
    earlier per-target invocation; the receipt retains its original cwd and times.
  snapshot_sha256: 9f0b680200670d75c2fd8d014a38ee585ca4c3ee389d18378f2a77fec0bad8f3
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
  summary: NCBITaxon:1540082 denotes Acidianus sp. RZ1 at SPECIES rank, parent NCBITaxon:2629519,
    genetic code 11, with 10 carried ancestors. All lineage IDs, names and ranks agree
    with the pinned inventory and captured NCBI EFetch, accounting for EFetch's omission
    of root.
  target_ids:
  - NCBITaxon:1540082
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
  summary: NCBI supplies Acidianus sp. DSM 29099 as an exact synonym. The captured
    DSMZ catalogue explicitly identifies DSM 29099 as Acidianus copahuensis, designation
    RZ1, other deposit JCM 30227, with history Acidianus sp. RZ1. BacDive 131324 uses
    the copahuensis taxon 1160895 while its sequence fields retain 1540082; these
    source boundaries are preserved. LPSN treats Candidatus Acidianus copahuensis
    as not validly published with pro-valid/pro-correct status and type ALE1. This
    does not make RZ1 the type strain or merge the two NCBI identities.
  target_ids:
  - NCBITaxon:1540082
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - lpsn-inventory
  - mapping-policy
  - lpsn-copahuensis
  - dsm-29099
  - mediadive-dsm-29099
- assessment_id: completeness
  area: completeness
  topic: Imported subtree and source assertion units
  outcome: supported
  summary: The complete pinned subtree has no descendants or directly classified BacDive
    entries. BacDive 131324 is filed under 1160895, so its related RZ1 designation
    does not authorize importing it under 1540082. NCBI 1 NAME, GTDB 2 GENOME, MediaDive
    2 MEDIUM and GOLD 1 ORGANISM agree with the pinned inventories. The current DSM
    29099 MediaDive page lists 88 and J176; GOLD Go0566671 explicitly carries DSM
    29099 and taxon 1540082. Current supporting objects do not reproduce the historical
    edge snapshot.
  target_ids:
  - NCBITaxon:1540082
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
  - rz1-genome-1
  - rz1-bacdive-1
  - rz1-gold-1
- assessment_id: taxonomy-mapping
  area: grounding
  topic: Qualified species mapping and target scope
  outcome: supported
  summary: 'The GTDB species cluster contains two inspected primary genomes: ALE1
    RS_GCF_000632495.1 with taxon/species 1160895 and DSM 29099 RS_GCF_013133895.1
    with taxon/species 1540082. The qualified closeMatch and species-level exact name/xref
    follow the local harmonization policy; independent culture history supports the
    naming association. This does not establish physical deposit or assembly equivalence.'
  target_ids:
  - NCBITaxon:1540082
  evidence_ids:
  - record
  - gtdb-mappings
  - gtdb-species
  - mapping-policy
  - equivalence-contract
  - seed-owner
  - rz1-genome-1
  - rz1-bacdive-1
  - rz1-gold-1
- assessment_id: native-status
  area: provenance
  topic: Unchanged native status and history
  outcome: supported
  summary: Grounding EXACT and mapping SEEDED remain unchanged. The sole seed event
    at 2026-09-13T17:54:04Z agrees with the maximum captured extraction timestamp
    across raw, ATB and StrainInfo manifests. No native status or history is promoted
    by this review.
  target_ids:
  - NCBITaxon:1540082
  evidence_ids:
  - record
  - manifest
  - overlay-manifests
findings: []
actions:
- action_id: recover-pinned-aggregate-inputs
  finding_ids: []
  target_ids:
  - NCBITaxon:1540082
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
- Source assertions are scoped to the captured inputs and access times. The review
  does not independently establish phylogenetic species boundaries, infer physical
  deposit/assembly equivalence, or infer mechanisms from names.
- No imported strains means no matching entry under the maintained pinned taxon/subtree
  rule; it is not a worldwide strain census.
- 'Required independent historical aggregate verification remains unavailable: the
  configured original kg-microbe edge paths were found with bytes differing from the
  manifest-pinned hashes. Current source pages and primary projections do not substitute
  for that extraction snapshot.'
- Authority page metadata was inspected; original publication full texts and sequence
  records were not independently reassessed for these contextual names.
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
- batch-0003
- archaea
- generated
- source-checked
```
