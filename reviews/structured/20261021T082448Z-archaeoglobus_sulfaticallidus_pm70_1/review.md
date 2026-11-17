# Record review: Archaeoglobus sulfaticallidus PM70-1

- Review: 20261021T082448Z-archaeoglobus_sulfaticallidus_pm70_1
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-21T07:10:14Z
- Finished UTC: 2026-10-21T08:24:48Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Archaeoglobus sulfaticallidus PM70-1 has supported NCBI strain identity and source counts, but its GTDB species exact synonym and xref overstate strain equivalence. The zero imported-strain count follows the source classification boundary.

## Scope And Provenance

Entire single generated record, including all source assertions and imported strains.

Selection: Batch-0018 target 7; next unreviewed path-order selection after excluding 225 actual covered target paths. Canonical record_review.py list over the 39-bundle current base and all seventeen actually saved branch worktrees, including ignored and hidden review bundles. Native corpus enumerated with os.walk including ignored/hidden files. Coverage only derives from explicit validated bundle targets, never inventories or reservations.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 01ca63effdf8c03a644df893ba6129b2d8448ea4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:387631 | data/taxa/archaea/archaeoglobus_sulfaticallidus_pm70_1.yaml | generated | Archaeoglobus sulfaticallidus PM70-1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact NCBI taxon, rank and lineage | passed | True | NCBITaxon:387631 | NCBITaxon:387631 is Archaeoglobus sulfaticallidus PM70-1 at STRAIN rank under species NCBITaxon:1316941, with genetic code 11. The exact target, all ten carried ancestor IDs, literal names and ranks agree with pinned NCBI and the captured current official response; the latter omits only root. Archaeoglobus sp. PM70-1 remains the source NCBI synonym. |
| Complete exact identifier and name inventory search | passed | True | NCBITaxon:387631 | Complete reads of twelve pinned source/scope/path tables, including ignored files, used the exact identifier, full name, slug, source synonym and GTDB species ID. There are no descendants and no directly classified imported BacDive strain or culture-inventory row. BacDive 18100 is classified at parent species 1316941, so its PM70-1 designation and genome links do not create a child import. NCBITAXON 1 NAME, GTDB 1 GENOME, GOLD 1 ORGANISM and MADIN 4 TRAIT_ASSERTION match their respective projection rows; the single GTDB cluster member was independently counted across all nineteen shards. GOLD and MADIN aggregate values were not independently reconstructed from manifest-matching historical primary inputs. Other named optional-source misses are bounded to these pinned tables, not worldwide biological absence. |
| Complete source-cluster membership and counts | passed | True | NCBITaxon:387631 | All native source cluster counts agree with complete selected primary clusters. Source domain conflicts, wording defects and species-versus-strain promotion are separately assessed where applicable. |
| Imported strain links | not_applicable | False | NCBITaxon:387631 | The complete native record contains no imported BacDive strain or strain-level link. Source classifications and subtype boundaries are preserved; a matching isolate name alone does not create a deposit import. |
| Complete source cluster and target-rank review | passed | True | NCBITaxon:387631 | All selected catalog and reverse rows were inspected; source count 1 is supported and the species-to-strain exact-identity promotion is recorded as a confirmed finding. |
| Gene or transcriptomics evidence applicability | not_applicable | False | NCBITaxon:387631 | No native gene, protein, regulator, pathway or transcriptomics dataset assertion requires a structured-adapter lookup for this record. |
| Original manifest-pinned aggregate recounts | unavailable | True | NCBITaxon:387631 | Pinned projection counts agree: [{"source":"GOLD","count":1,"unit":"ORGANISM","raw_projection_agrees":true,"historical_primary_aggregate_checked":false},{"source":"MADIN","count":4,"unit":"TRAIT_ASSERTION","raw_projection_agrees":true,"historical_primary_aggregate_checked":false}]. Original aggregate edges were not independently recounted. |
| Native strict record validation | passed | True | NCBITaxon:387631 | Actual terminal exit code 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. |
| Repository history validation | passed | True | NCBITaxon:387631 | Actual terminal exit code 0. The complete standalone history population; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0018 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. |
| Full-corpus exact reproduction | passed | True | NCBITaxon:387631 | Actual terminal exit code 0. All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0018 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. |
| Native product ID/label gate | passed | True | NCBITaxon:387631 | Actual terminal exit code 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0018 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. |
| Authoritative complete quality gate | passed | True | NCBITaxon:387631 | Actual terminal exit code 0. Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0018 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. 1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33) |

## Scientific And Domain Assessments

### GTDB species concept versus native strain identity

grounding: concern. Targets: NCBITaxon:387631.

The complete pinned RS232 cluster GTDB:s__Archaeoglobus_A_sulfaticallidus contains only RS_GCF_000385565.1 at data/catalog/gtdb_genomes-0017.jsonl.gz:38543. It identifies ncbi_taxid 387631 but ncbi_species_taxid 1316941. The native record is STRAIN under that separate species parent. Its supplied closeMatch and genome count 1 are supported. Promoting the GTDB species into unqualified xrefs and EXACT_SYNONYM Archaeoglobus A sulfaticallidus overstates species-to-strain identity. A singleton cluster does not make the species concept identical to its one sampled strain.

### NCBI strain names and parent-species type boundary

nomenclature: supported. Targets: NCBITaxon:387631.

Current and pinned NCBI retain Archaeoglobus sp. PM70-1 as an exact synonym of strain 387631. The LPSN species name and type designations belong to parent species 1316941. BacDive 18100 is filed directly at that parent; a genome taxid or matching PM70-1 label does not make it an imported child strain. The zero imported-strain count is source-consistent. The separate GTDB exact synonym and xref carry the species-to-strain scope defect documented in the finding.

### Exact taxon and source lineage

identity: supported. Targets: NCBITaxon:387631.

NCBITaxon:387631 is Archaeoglobus sulfaticallidus PM70-1 at STRAIN rank under species NCBITaxon:1316941, with genetic code 11. The exact target, all ten carried ancestor IDs, literal names and ranks agree with pinned NCBI and the captured current official response; the latter omits only root. Archaeoglobus sp. PM70-1 remains the source NCBI synonym.

### Name classes and nomenclatural scope

nomenclature: concern. Targets: NCBITaxon:387631.

Current and pinned NCBI retain Archaeoglobus sp. PM70-1 as an exact synonym of strain 387631. The LPSN species name and type designations belong to parent species 1316941. BacDive 18100 is filed directly at that parent; a genome taxid or matching PM70-1 label does not make it an imported child strain. The zero imported-strain count is source-consistent. The separate GTDB exact synonym and xref carry the species-to-strain scope defect documented in the finding.

### Imported subtree and source assertion units

completeness: supported. Targets: NCBITaxon:387631.

Complete reads of twelve pinned source/scope/path tables, including ignored files, used the exact identifier, full name, slug, source synonym and GTDB species ID. There are no descendants and no directly classified imported BacDive strain or culture-inventory row. BacDive 18100 is classified at parent species 1316941, so its PM70-1 designation and genome links do not create a child import. NCBITAXON 1 NAME, GTDB 1 GENOME, GOLD 1 ORGANISM and MADIN 4 TRAIT_ASSERTION match their respective projection rows; the single GTDB cluster member was independently counted across all nineteen shards. GOLD and MADIN aggregate values were not independently reconstructed from manifest-matching historical primary inputs. Other named optional-source misses are bounded to these pinned tables, not worldwide biological absence.

### Qualified species mapping and target scope

grounding: concern. Targets: NCBITaxon:387631.

The complete pinned RS232 cluster GTDB:s__Archaeoglobus_A_sulfaticallidus contains only RS_GCF_000385565.1 at data/catalog/gtdb_genomes-0017.jsonl.gz:38543. It identifies ncbi_taxid 387631 but ncbi_species_taxid 1316941. The native record is STRAIN under that separate species parent. Its supplied closeMatch and genome count 1 are supported. Promoting the GTDB species into unqualified xrefs and EXACT_SYNONYM Archaeoglobus A sulfaticallidus overstates species-to-strain identity. A singleton cluster does not make the species concept identical to its one sampled strain.

### Unchanged native status and history

provenance: supported. Targets: NCBITaxon:387631.

EXACT grounding and SEEDED mapping status retain the source state. The sole SEEDED_FROM_SOURCES event at 2026-09-13T17:54:04Z matches the maximum raw/ATB/StrainInfo manifest extraction time and exact scope/path rows. The confirmed GTDB scope finding does not justify changing the carried NCBI identity or hand-editing this generated record.

## Findings

### gtdb-strain-scope: GTDB species identity is promoted into STRAIN equivalence

major / open / confirmed; issue key: gtdb-closematch-exact-promotion-387631.

The complete pinned RS232 cluster GTDB:s__Archaeoglobus_A_sulfaticallidus contains only RS_GCF_000385565.1 at data/catalog/gtdb_genomes-0017.jsonl.gz:38543. It identifies ncbi_taxid 387631 but ncbi_species_taxid 1316941. The native record is STRAIN under that separate species parent. Its supplied closeMatch and genome count 1 are supported. Promoting the GTDB species into unqualified xrefs and EXACT_SYNONYM Archaeoglobus A sulfaticallidus overstates species-to-strain identity. A singleton cluster does not make the species concept identical to its one sampled strain.

## Recommended Actions And Acceptance Checks

### guard-gtdb-strain-equivalence

Make GTDB species identity promotion rank-aware in the maintained seeder. Preserve the qualified source mapping, count, NCBI name classes and independently supported strain links. Regenerate through native gates after separately authorized curation; do not directly edit generated YAML.

- Retain the distinct NCBI STRAIN identity and species parent.
- Prevent a species-level GTDB xref or exact synonym from asserting exact strain identity.
- Retain the source closeMatch, whole-cluster count 1 and supported strain/genome evidence; retain valid species-level normalization.
- Change maintained inputs only; verify strict, history, product, corpus and QC gates after authorized regeneration.

### recover-pinned-aggregate-inputs

Recover manifest-hash-matching original aggregate inputs and independently recount the exact target assertions through the maintained extractor; do not edit generated YAML.

- Require exact original input SHA-256 before using it as historical evidence.
- Recount only the exact target with each source's own assertion unit and compare to its pinned inventory row.
- Record any discrepancy in a new review observation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/taxa/archaea/archaeoglobus_sulfaticallidus_pm70_1.yaml; entire TaxonRecord; identifier=NCBITaxon:387631 | supports | Read the entire generated YAML, including identity, lineage, names, mappings, source attestations, all imported strains and links, and seed history. |
| taxonomy-inventory | data/raw/ncbitaxon_taxa.tsv; line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""}; line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"}; line 1755: {"taxon_id":"NCBITaxon:2231","label":"Archaeoglobales","rank":"ORDER","parent_id":"NCBITaxon:183980"}; line 1756: {"taxon_id":"NCBITaxon:2232","label":"Archaeoglobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2231"}; line 1757: {"taxon_id":"NCBITaxon:2233","label":"Archaeoglobus","rank":"GENUS","parent_id":"NCBITaxon:2232"}; line 2981: {"taxon_id":"NCBITaxon:28890","label":"Methanobacteriota","rank":"PHYLUM","parent_id":"NCBITaxon:3366610"}; line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"}; line 36620: {"taxon_id":"NCBITaxon:183980","label":"Archaeoglobi","rank":"CLASS","parent_id":"NCBITaxon:28890"}; line 81841: {"taxon_id":"NCBITaxon:387631","label":"Archaeoglobus sulfaticallidus PM70-1","rank":"STRAIN","parent_id":"NCBITaxon:1316941","genetic_code":"11","exact_synonyms":"Archaeoglobus sp. PM70-1","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb&#124;gold&#124;madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"}; line 313610: {"taxon_id":"NCBITaxon:1316941","label":"Archaeoglobus sulfaticallidus","rank":"SPECIES","parent_id":"NCBITaxon:2233"}; line 621140: {"taxon_id":"NCBITaxon:3366610","label":"Methanobacteriati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"} | supports | Inspected the target and each carried ancestor, rank, parent, genetic code and source name classes. |
| scope-row | curation/seed_scope.tsv; line 24313: {"identifier":"NCBITaxon:387631","added":"2026-09-12","reason":"attested rule: Archaeoglobus sulfaticallidus PM70-1, 4 sources incl. NCBI"} | supports | Exact target is included in the declared seed scope. |
| path-row | data/taxa/PATHS.tsv; line 488904: {"identifier":"NCBITaxon:387631","slug":"archaeoglobus_sulfaticallidus_pm70_1"} | supports | Indexed path resolves to this exact NCBI taxon. |
| ncbi-live | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1798180,1915565,1915566,1915567,1915568,1316941,387631,58290,693661,1906665&amp;retmode=xml; TaxaSet/Taxon[TaxId='387631']; ten-target captured response | supports | Inspected the official response for this exact taxon: scientific name, rank, parent, source name classes, lineage and genetic code. Current authority and pinned September inventory remain distinct observations. |
| lpsn-inventory | data/raw/lpsn_names.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected exact mapped and linked LPSN names; bounded inventory absence does not establish worldwide nomenclatural absence. |
| gtdb-mappings | data/raw/gtdb_mappings.tsv; line 285381: {"gtdb_id":"GTDB:s__Archaeoglobus_A_sulfaticallidus","gtdb_label":"s__Archaeoglobus_A_sulfaticallidus","gtdb_parent":"GTDB:g__Archaeoglobus_A","ncbitaxon_id":"NCBITaxon:387631","predicate":"skos:closeMatch","genome_count":"1"} | supports | Inspected direct mappings and selected clusters' reverse mappings, retaining each source predicate and taxon boundary. |
| gtdb-species | data/raw/gtdb_species.tsv; line 12296: {"gtdb_id":"GTDB:s__Archaeoglobus_A_sulfaticallidus","label":"s__Archaeoglobus_A_sulfaticallidus","parent":"GTDB:g__Archaeoglobus_A","genome_count":"1"} | supports | Inspected source species identifiers, labels, parent clusters and genome counts. |
| bacdive-inventory | data/raw/bacdive_strains.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Complete inventory selection covers the exact target and descendants from the complete NCBI parent graph; its imported strain population was compared with the complete YAML. |
| culture-inventory | data/raw/culture_collection_strains.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected exact culture-inventory associations; an isolate name or genome does not create an inferred deposit. |
| gold-organisms | data/raw/gold_organisms.tsv; line 34035: {"taxon_id":"NCBITaxon:387631","organism_count":"1"} | supports | Inspected the exact GOLD organism count row or bounded absence, without converting counts to phenotypes. |
| mediadive-taxa | data/raw/mediadive_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact MediaDive medium count row or bounded absence, without converting counts to phenotypes. |
| madin-taxa | data/raw/madin_taxa.tsv; line 22943: {"taxon_id":"NCBITaxon:387631","assertion_count":"4"} | supports | Inspected the exact Madin trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| bactotraits-taxa | data/raw/bactotraits_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact BactoTraits trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| mapping-policy | docs/HARMONIZATION.md; Mapping predicates; Which strains belong to a record | supports | Policy permits source-scoped species-level closeMatch normalization and LPSN-linked species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage unchanged. Multiple reverse mappings do not alone establish a normalization defect or make species and strains identical. |
| equivalence-contract | src/taxonmech/schema/taxonmech.yaml; TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439 | supports | TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes under the source taxon. |
| seed-owner | src/taxonmech/seed.py; GTDB mapping construction lines 444–476; LPSN/type-strain and source-attestation construction | supports | Inspected mapping ranking, qualified predicates, fixed broadMatch wording, synonym/xref construction, primary cluster counts and same-taxon type-strain derivation. |
| manifest | data/raw/MANIFEST.yaml; kg_microbe_source, inputs, extracted_at | supports | Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd, upstream input hashes and extraction time 2026-09-13T17:50:44Z. |
| overlay-manifests | data/atb/MANIFEST.yaml; extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml | supports | Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z, matching the sole seed event. StrainInfo manifest is independently captured in source.inputs. |
| genome-catalog-1 | data/catalog/gtdb_genomes-0017.jsonl.gz; line 38543: {"accession":"RS_GCF_000385565.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus_A;s__Archaeoglobus_A sulfaticallidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Complete Genome","ncbi_assembly_name":"ASM38556v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN02028569","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"none","ncbi_date":"2013-04-30","ncbi_genbank_assembly_accession":"GCA_000385565.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus sulfaticallidus PM70-1","ncbi_protein_count":"2210","ncbi_refseq_category":"reference genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"2076931","ncbi_scaffold_n75":"2076931","ncbi_scaffold_n90":"2076931","ncbi_seq_rel_date":"2013-04-30","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1316941","ncbi_ssu_count":"1","ncbi_strain_identifiers":"PM70-1","ncbi_submitter":"University of Bergen, Centre for Geobiology, Department of Biology","ncbi_taxid":"387631","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus sulfaticallidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus sulfaticallidus;x__Archaeoglobus sulfaticallidus PM70-1","ncbi_total_gap_length":"0","ncbi_total_length":"2076931","ncbi_translation_table":"11","ncbi_trna_count":"51","ncbi_type_material_designation":"assembly from type material","ncbi_ungapped_length":"2076931","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"} | supports | Inspected every member of the selected GTDB source clusters, including original accession versions, NCBI taxid/species-taxid, source taxonomy and sample metadata. Whole-cluster counts are not counts exclusive to this NCBI taxon or proof of biological equivalence. |
| gtdb-full-scan | data/catalog/MANIFEST.json; {"target_id":"NCBITaxon:387631","source_cluster_counts":{"GTDB:s__Archaeoglobus_A_sulfaticallidus":1},"selected_members":1,"scan_receipt":"catalog-scan-receipt.json","scan_sha256":"10fe369d255a601f55990f99a4c115d91f5635fc74961265fd9fa53cb1907bb0"} | supports | All 19 pinned GTDB shards and 901341 rows match the manifest. Every selected source cluster member was inspected. Distinct source taxonomies and NCBI taxa remain separate assertions; reverse multiplicity alone is not an exact-identity defect. |
| mapping-target-rank | data/raw/ncbitaxon_taxa.tsv; [{"line":81841,"row":{"taxon_id":"NCBITaxon:387631","label":"Archaeoglobus sulfaticallidus PM70-1","rank":"STRAIN","parent_id":"NCBITaxon:1316941","genetic_code":"11","exact_synonyms":"Archaeoglobus sp. PM70-1","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb&#124;gold&#124;madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"}},{"line":313610,"row":{"taxon_id":"NCBITaxon:1316941","label":"Archaeoglobus sulfaticallidus","rank":"SPECIES","parent_id":"NCBITaxon:2233","genetic_code":"11","exact_synonyms":"","related_synonyms":"Archaeoglobus sulfaticallidus Steinsbu et al. 2010","broad_synonyms":"","attested_by":"ncbitaxon&#124;bacdive&#124;lpsn&#124;mediadive&#124;gold&#124;madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"}}] | supports | Pinned NCBI identity retains a STRAIN target and a separate species parent. |
| mapping-current-ncbi | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1798180,1915565,1915566,1915567,1915568,1316941,387631,58290,693661,1906665&amp;retmode=xml; TaxaSet/Taxon with TaxId equal to 387631: ScientificName, Rank, ParentTaxId, OtherNames, LineageEx | supports | The captured official NCBI response independently retains this exact strain rank, species parent and original source name classes. |
| mapping-pinned-direct | data/raw/gtdb_mappings.tsv; [{"line":285381,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_A_sulfaticallidus","gtdb_label":"s__Archaeoglobus_A_sulfaticallidus","gtdb_parent":"GTDB:g__Archaeoglobus_A","ncbitaxon_id":"NCBITaxon:387631","predicate":"skos:closeMatch","genome_count":"1"}}] | supports | The complete reverse scan returns only this source closeMatch, with count 1; its qualified predicate remains a supplied source assertion. |
| mapping-pinned-species | data/raw/gtdb_species.tsv; [{"line":12296,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_A_sulfaticallidus","label":"s__Archaeoglobus_A_sulfaticallidus","parent":"GTDB:g__Archaeoglobus_A","genome_count":"1"}}] | supports | The source species inventory retains the GTDB species identifier and whole-cluster genome count 1. |
| mapping-primary-genome | data/catalog/gtdb_genomes-0017.jsonl.gz; {"line":38543,"row":{"accession":"RS_GCF_000385565.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus_A;s__Archaeoglobus_A sulfaticallidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Complete Genome","ncbi_assembly_name":"ASM38556v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN02028569","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"none","ncbi_date":"2013-04-30","ncbi_genbank_assembly_accession":"GCA_000385565.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus sulfaticallidus PM70-1","ncbi_protein_count":"2210","ncbi_refseq_category":"reference genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"2076931","ncbi_scaffold_n75":"2076931","ncbi_scaffold_n90":"2076931","ncbi_seq_rel_date":"2013-04-30","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1316941","ncbi_ssu_count":"1","ncbi_strain_identifiers":"PM70-1","ncbi_submitter":"University of Bergen, Centre for Geobiology, Department of Biology","ncbi_taxid":"387631","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus sulfaticallidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus sulfaticallidus;x__Archaeoglobus sulfaticallidus PM70-1","ncbi_total_gap_length":"0","ncbi_total_length":"2076931","ncbi_translation_table":"11","ncbi_trna_count":"51","ncbi_type_material_designation":"assembly from type material","ncbi_ungapped_length":"2076931","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"}} | supports | The complete selected GTDB cluster consists of this versioned RefSeq genome. Its strain taxid differs from its species_taxid. The supplied GenBank accession remains a separate typed field; no sequence equivalence or physical deposit join is inferred. |
| mapping-full-census | data/catalog/MANIFEST.json; {"snapshot":"RS232","members":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":38543,"row":{"accession":"RS_GCF_000385565.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus_A;s__Archaeoglobus_A sulfaticallidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Complete Genome","ncbi_assembly_name":"ASM38556v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN02028569","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"none","ncbi_date":"2013-04-30","ncbi_genbank_assembly_accession":"GCA_000385565.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus sulfaticallidus PM70-1","ncbi_protein_count":"2210","ncbi_refseq_category":"reference genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"2076931","ncbi_scaffold_n75":"2076931","ncbi_scaffold_n90":"2076931","ncbi_seq_rel_date":"2013-04-30","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1316941","ncbi_ssu_count":"1","ncbi_strain_identifiers":"PM70-1","ncbi_submitter":"University of Bergen, Centre for Geobiology, Department of Biology","ncbi_taxid":"387631","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus sulfaticallidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus sulfaticallidus;x__Archaeoglobus sulfaticallidus PM70-1","ncbi_total_gap_length":"0","ncbi_total_length":"2076931","ncbi_translation_table":"11","ncbi_trna_count":"51","ncbi_type_material_designation":"assembly from type material","ncbi_ungapped_length":"2076931","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"},"selection_basis":["species_identifier"]}],"reverse_rows":[{"line":285381,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_A_sulfaticallidus","gtdb_label":"s__Archaeoglobus_A_sulfaticallidus","gtdb_parent":"GTDB:g__Archaeoglobus_A","ncbitaxon_id":"NCBITaxon:387631","predicate":"skos:closeMatch","genome_count":"1"}}],"scan_receipt":"catalog-scan-receipt.json","scan_sha256":"10fe369d255a601f55990f99a4c115d91f5635fc74961265fd9fa53cb1907bb0"} | supports | All 19 GTDB shards and 901341 rows match the pinned RS232 manifest. Exactly one member was found for this source species, and the complete reverse table has one target. |
| mapping-policy-scope | docs/HARMONIZATION.md; Mapping predicates, lines122–144; Which strains belong to a record, lines146–168; Type strains, lines174–183 | supports | Local policy permits species-level normalization while preserving source taxonomy and asymmetric BacDive subtree imports. The finding is specifically about species identity asserted on a strain-ranked target, not a generic closeMatch-versus-exact distinction. |
| mapping-equivalence-contract | src/taxonmech/schema/taxonmech.yaml; TaxonRecord.xrefs, lines180–185; TaxonomyMapping.mapping_predicate and genome_count, lines428–436 | supports | TaxonRecord.xrefs is reserved for true equivalences; broader/narrower relations remain qualified. TaxonomyMapping.genome_count counts the complete source taxon. |
| mapping-maintained-owner | src/taxonmech/seed.py; GTDB mapping construction, lines443–473; identity at455 and xref/exact-synonym promotion at470–473 | supports | The maintained seeder treats every closeMatch as identity and promotes its GTDB species identifier and normalized exact synonym without checking the native target rank. |
| mapping-parent-nomenclature | data/raw/lpsn_names.tsv; [{"line":25993,"row":{"lpsn_id":"lpsn:788917","name":"Archaeoglobus sulfaticallidus","rank":"SPECIES","authority":"Steinsbu et al. 2010","url":"https://lpsn.dsmz.de/species/archaeoglobus-sulfaticallidus","deprecated":"0","status":"legitimate=True; validly published under the ICNP; correct name","validly_published":"1","legitimate":"1","is_correct_name":"1","parent_lpsn_id":"lpsn:516970","ncbitaxon_ids":"NCBITaxon:1316941","gtdb_ids":"","type_strain_ids":"kgmicrobe.strain:DSM-19444&#124;kgmicrobe.strain:JCM-14716","synonym_of":"","synonyms":"","publications":"PMID:20061497&#124;doi:10.1099/ijs.0.016105-0&#124;doi:10.1099/ijs.0.031948-0","sequence_accessions":"INSDC:FJ810190"}}] | supports | The relevant LPSN name maps to the distinct species parent and has empty gtdb_ids; it supplies no alternate GTDB identity bridge to this strain target. |
| mapping-bacdive-classification | data/raw/bacdive_strains.tsv; [{"line":17909,"row":{"strain_id":"kgmicrobe.strain:bacdive_18100","bacdive_id":"18100","designation":"PM70-1","taxon_ids":"NCBITaxon:1316941","lpsn_ids":"lpsn:788917","culture_collection_ids":"kgmicrobe.strain:DSM-19444&#124;kgmicrobe.strain:JCM-14716","medium_count":"0"}}] | supports | BacDive retains its own exact source taxon classification. Name similarity or a species type designation does not move the classification into a child strain record. |
| finding-deduplication | Owned review worktrees structured bundles; {"keys":["gtdb-closematch-exact-promotion-387631"],"yaml_files_read":780,"unique_review_id_and_byte_hash_pairs":169} | supports | No same-target saved review or matching stable finding key was found in the bounded ignored-inclusive search. This is not a corpus coverage claim. |
| historical-gold-edge | data/raw/MANIFEST.yaml; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/gold/edges.tsv;expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12;observed=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d | partial | Retained configured-path source check found bytes differing from the manifest-pinned original; this does not establish global absence. |
| historical-madin-edge | data/raw/MANIFEST.yaml; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv;expected=3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f;observed=c19bfc848e1b410548614c54a2b99e2c58452d58aeb61f972c99fcb3039a1d24 | partial | Retained configured-path source check found bytes differing from the manifest-pinned original; this does not establish global absence. |
| native-gate-reuse | /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0018/native-gate-reuse.json; base, native_inputs_unchanged, source_directory, gates, input_proof_path and input_proof_sha256 | supports | Retained explicit verification of identical base/native inputs authorizes historical native-gate reuse; original command receipts remain separately cited. |
| strict-receipt | just validate-strict data/taxa/archaea/archaeoglobus_sulfaticallidus_pm70_1.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0018/strict-07.tsv; This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0018/repo; started 2026-10-21T07:10:20Z, finished 2026-10-21T07:10:23Z, exit 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times.<br>Validating 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0016/src/taxonmech/schema/taxonmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0018/strict-07.tsv |
| history-receipt | just validate-history; The complete standalone history population; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0018 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T06:42:11Z, exit 0. The complete standalone history population; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0018 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check.<br>history links: 18 record(s), 0 invalid<br>No issues found<br>18 history record(s) valid against src/taxonmech/schema/history.yaml |
| corpus-receipt | just verify-corpus; All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0018 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T06:48:01Z, exit 0. All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0018 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check.<br>uv run python scripts/verify_corpus.py <br>expected 626048 records, found 626048 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ and curation/seed_scope.tsv |
| products-receipt | just validate-products; Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0018 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T07:19:10Z, exit 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0018 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check.<br>uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml<br><br>id↔label correspondence summary:<br><br>✅ All id↔label pairs correspond. |
| qc-receipt | just qc; Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0018 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T07:50:51Z, exit 0. Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0018 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check.<br>All checks passed!<br>1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33)<br>Validating 626048 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0014/src/taxonmech/schema/taxonmech.yaml<br>  files scanned:      626048<br>expected 626048 records, found 626048 on disk<br>pages/ is current<br>Site publication: 530,946,096 bytes (budget 950,000,000)<br>626048 taxon records<br>  NCBITAXON        626048<br>All TaxonMech quality gates passed.<br>  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890 strains (not genome counts)<br>  Related STRAININFO_DEPOSIT: 107277 strain-record pairs, 106843 identifiers, 53890 strains (not genome counts)<br>  Related NUCLEOTIDE_SEQUENCE: 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)<br>LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809 records mapped, 324404579 genomes summed across record attestations (not deduplicated)<br>Causal graphs: 0 records (0 evidence-backed edges)<br><br>All TaxonMech quality gates passed. |

## Limits And Additional Notes

- The singleton GTDB cluster count and accession versions are supported; this finding does not assert multiple cluster members or a strain-link defect.
- GTDB species normalization remains allowed for species-level targets. This is an explicit rank/scope mismatch, independent of generic SKOS predicate differences.
- GOLD 1 ORGANISM and MADIN 4 TRAIT_ASSERTION agree with pinned inventory projections; no independent recount from the original manifest-hash-matching aggregate inputs was performed. Counts do not establish a phenotype or mechanism.
- A matching type-strain label or genome taxid does not move a BacDive classification from the parent species into this child. No deposited-culture absence is claimed.
- Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained original cwd, times, commands, log hashes and terminal exit codes identify the executions. Reused repository-wide receipts require the explicit same-base/native-input certificate; these are historical runs, not new batch-0018 invocations. Missing terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts retain their original execution context. New review bundles still require individual validation/save/check.
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base source transitions are verified against retained original captures and exact changed-input receipts.
- Every new bundle still requires its own validate/save/check recipe; historical native receipts do not claim these later steps have run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T082448Z-archaeoglobus_sulfaticallidus_pm70_1
kind: record
repository: CultureBotAI/TaxonMech
title: 'Record review: Archaeoglobus sulfaticallidus PM70-1'
started_at: '2026-10-21T07:10:14Z'
finished_at: '2026-10-21T08:24:48Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: The reviewer did not author the existing generated target; this
    review changes only new review artifacts in an isolated checkout.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Archaeoglobus sulfaticallidus PM70-1 has supported NCBI strain identity and
  source counts, but its GTDB species exact synonym and xref overstate strain equivalence.
  The zero imported-strain count follows the source classification boundary.
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
  - path: data/taxa/archaea/archaeoglobus_sulfaticallidus_pm70_1.yaml
    sha256: 98bf4bc00431715b6eadf611ded387e1ef40adb504e9580fa65f3d0b211b63f6
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
  selection: Batch-0018 target 7; next unreviewed path-order selection after excluding
    225 actual covered target paths. Canonical record_review.py list over the 39-bundle
    current base and all seventeen actually saved branch worktrees, including ignored
    and hidden review bundles. Native corpus enumerated with os.walk including ignored/hidden
    files. Coverage only derives from explicit validated bundle targets, never inventories
    or reservations.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - NCBITaxon:387631
targets:
- target_id: NCBITaxon:387631
  path: data/taxa/archaea/archaeoglobus_sulfaticallidus_pm70_1.yaml
  label: Archaeoglobus sulfaticallidus PM70-1
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
  summary: NCBITaxon:387631 is Archaeoglobus sulfaticallidus PM70-1 at STRAIN rank
    under species NCBITaxon:1316941, with genetic code 11. The exact target, all ten
    carried ancestor IDs, literal names and ranks agree with pinned NCBI and the captured
    current official response; the latter omits only root. Archaeoglobus sp. PM70-1
    remains the source NCBI synonym.
  target_ids:
  - NCBITaxon:387631
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
  summary: Complete reads of twelve pinned source/scope/path tables, including ignored
    files, used the exact identifier, full name, slug, source synonym and GTDB species
    ID. There are no descendants and no directly classified imported BacDive strain
    or culture-inventory row. BacDive 18100 is classified at parent species 1316941,
    so its PM70-1 designation and genome links do not create a child import. NCBITAXON
    1 NAME, GTDB 1 GENOME, GOLD 1 ORGANISM and MADIN 4 TRAIT_ASSERTION match their
    respective projection rows; the single GTDB cluster member was independently counted
    across all nineteen shards. GOLD and MADIN aggregate values were not independently
    reconstructed from manifest-matching historical primary inputs. Other named optional-source
    misses are bounded to these pinned tables, not worldwide biological absence.
  target_ids:
  - NCBITaxon:387631
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
  - mapping-target-rank
  - mapping-current-ncbi
  - mapping-pinned-direct
  - mapping-pinned-species
  - mapping-primary-genome
  - mapping-full-census
  - mapping-policy-scope
  - mapping-equivalence-contract
  - mapping-maintained-owner
  - mapping-parent-nomenclature
  - mapping-bacdive-classification
  scope_note: Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs.
- check_id: gtdb-primary-counts
  name: Complete source-cluster membership and counts
  status: passed
  required: true
  summary: All native source cluster counts agree with complete selected primary clusters.
    Source domain conflicts, wording defects and species-versus-strain promotion are
    separately assessed where applicable.
  target_ids:
  - NCBITaxon:387631
  evidence_ids:
  - gtdb-full-scan
  - gtdb-mappings
  - gtdb-species
  - genome-catalog-1
  scope_note: All manifest-matching pinned GTDB shards and complete selected cluster
    membership.
- check_id: strain-genome-evidence
  name: Imported strain links
  status: not_applicable
  required: false
  summary: The complete native record contains no imported BacDive strain or strain-level
    link. Source classifications and subtype boundaries are preserved; a matching
    isolate name alone does not create a deposit import.
  target_ids:
  - NCBITaxon:387631
  evidence_ids:
  - record
  - bacdive-inventory
  - culture-inventory
- check_id: mapping-source-scope-review
  name: Complete source cluster and target-rank review
  status: passed
  required: true
  summary: All selected catalog and reverse rows were inspected; source count 1 is
    supported and the species-to-strain exact-identity promotion is recorded as a
    confirmed finding.
  target_ids:
  - NCBITaxon:387631
  evidence_ids:
  - record
  - mapping-target-rank
  - mapping-current-ncbi
  - mapping-pinned-direct
  - mapping-pinned-species
  - mapping-primary-genome
  - mapping-full-census
  - mapping-policy-scope
  - mapping-equivalence-contract
  - mapping-maintained-owner
  - mapping-parent-nomenclature
  - mapping-bacdive-classification
- check_id: structured-adapter-applicability
  name: Gene or transcriptomics evidence applicability
  status: not_applicable
  required: false
  summary: No native gene, protein, regulator, pathway or transcriptomics dataset
    assertion requires a structured-adapter lookup for this record.
  target_ids:
  - NCBITaxon:387631
  evidence_ids:
  - record
- check_id: historical-source-counts
  name: Original manifest-pinned aggregate recounts
  status: unavailable
  required: true
  summary: 'Pinned projection counts agree: [{"source":"GOLD","count":1,"unit":"ORGANISM","raw_projection_agrees":true,"historical_primary_aggregate_checked":false},{"source":"MADIN","count":4,"unit":"TRAIT_ASSERTION","raw_projection_agrees":true,"historical_primary_aggregate_checked":false}].
    Original aggregate edges were not independently recounted.'
  target_ids:
  - NCBITaxon:387631
  evidence_ids:
  - manifest
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
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
  - NCBITaxon:387631
  evidence_ids:
  - strict-receipt
  command: just validate-strict data/taxa/archaea/archaeoglobus_sulfaticallidus_pm70_1.yaml
    --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0018/strict-07.tsv
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
    these are historical runs, not new batch-0018 invocations. Missing terminal receipts
    or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts
    retain their original execution context. New review bundles still require individual
    validation/save/check.
  target_ids:
  - NCBITaxon:387631
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
    certificate; these are historical runs, not new batch-0018 invocations. Missing
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
    certificate; these are historical runs, not new batch-0018 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check.
  target_ids:
  - NCBITaxon:387631
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
    certificate; these are historical runs, not new batch-0018 invocations. Missing
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
    runs, not new batch-0018 invocations. Missing terminal receipts or reuse proof
    remain unavailable in unsaved previews. Exact-target strict receipts retain their
    original execution context. New review bundles still require individual validation/save/check.
  target_ids:
  - NCBITaxon:387631
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
    certificate; these are historical runs, not new batch-0018 invocations. Missing
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
    certificate; these are historical runs, not new batch-0018 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check. 1073 passed, 3 skipped, 5 deselected
    in 1293.90s (0:21:33)
  target_ids:
  - NCBITaxon:387631
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
    certificate; these are historical runs, not new batch-0018 invocations. Missing
    terminal receipts or reuse proof remain unavailable in unsaved previews. Exact-target
    strict receipts retain their original execution context. New review bundles still
    require individual validation/save/check.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/taxa/archaea/archaeoglobus_sulfaticallidus_pm70_1.yaml
  accessed_at: '2026-10-21T08:24:48Z'
  support: supports
  summary: Read the entire generated YAML, including identity, lineage, names, mappings,
    source attestations, all imported strains and links, and seed history.
  locator: entire TaxonRecord; identifier=NCBITaxon:387631
  snapshot_sha256: 98bf4bc00431715b6eadf611ded387e1ef40adb504e9580fa65f3d0b211b63f6
- evidence_id: taxonomy-inventory
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-21T07:10:15Z'
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
    line 81841: {"taxon_id":"NCBITaxon:387631","label":"Archaeoglobus sulfaticallidus
    PM70-1","rank":"STRAIN","parent_id":"NCBITaxon:1316941","genetic_code":"11","exact_synonyms":"Archaeoglobus
    sp. PM70-1","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon|gtdb|gold|madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"};
    line 313610: {"taxon_id":"NCBITaxon:1316941","label":"Archaeoglobus sulfaticallidus","rank":"SPECIES","parent_id":"NCBITaxon:2233"};
    line 621140: {"taxon_id":"NCBITaxon:3366610","label":"Methanobacteriati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
- evidence_id: scope-row
  kind: database
  reference: curation/seed_scope.tsv
  accessed_at: '2026-10-21T07:10:15Z'
  support: supports
  summary: Exact target is included in the declared seed scope.
  locator: 'line 24313: {"identifier":"NCBITaxon:387631","added":"2026-09-12","reason":"attested
    rule: Archaeoglobus sulfaticallidus PM70-1, 4 sources incl. NCBI"}'
  snapshot_sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
- evidence_id: path-row
  kind: database
  reference: data/taxa/PATHS.tsv
  accessed_at: '2026-10-21T07:10:15Z'
  support: supports
  summary: Indexed path resolves to this exact NCBI taxon.
  locator: 'line 488904: {"identifier":"NCBITaxon:387631","slug":"archaeoglobus_sulfaticallidus_pm70_1"}'
  snapshot_sha256: f8f2e0721cb6839b30530b44be0d3004b9f0e6e2d4be8736f235b10117a8bd99
- evidence_id: ncbi-live
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1798180,1915565,1915566,1915567,1915568,1316941,387631,58290,693661,1906665&retmode=xml
  accessed_at: '2026-10-21T07:10:07Z'
  support: supports
  summary: 'Inspected the official response for this exact taxon: scientific name,
    rank, parent, source name classes, lineage and genetic code. Current authority
    and pinned September inventory remain distinct observations.'
  locator: TaxaSet/Taxon[TaxId='387631']; ten-target captured response
  snapshot_sha256: 1ec169d5de9ceedc7ca4cb4b8f37dc2b0ba6e45602d47668125e0e50197368ce
- evidence_id: lpsn-inventory
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-21T07:10:15Z'
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
  accessed_at: '2026-10-21T07:10:15Z'
  support: supports
  summary: Inspected direct mappings and selected clusters' reverse mappings, retaining
    each source predicate and taxon boundary.
  locator: 'line 285381: {"gtdb_id":"GTDB:s__Archaeoglobus_A_sulfaticallidus","gtdb_label":"s__Archaeoglobus_A_sulfaticallidus","gtdb_parent":"GTDB:g__Archaeoglobus_A","ncbitaxon_id":"NCBITaxon:387631","predicate":"skos:closeMatch","genome_count":"1"}'
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
- evidence_id: gtdb-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-21T07:10:15Z'
  support: supports
  summary: Inspected source species identifiers, labels, parent clusters and genome
    counts.
  locator: 'line 12296: {"gtdb_id":"GTDB:s__Archaeoglobus_A_sulfaticallidus","label":"s__Archaeoglobus_A_sulfaticallidus","parent":"GTDB:g__Archaeoglobus_A","genome_count":"1"}'
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
- evidence_id: bacdive-inventory
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-21T07:10:15Z'
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
  accessed_at: '2026-10-21T07:10:15Z'
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
  accessed_at: '2026-10-21T07:10:15Z'
  support: supports
  summary: Inspected the exact GOLD organism count row or bounded absence, without
    converting counts to phenotypes.
  locator: 'line 34035: {"taxon_id":"NCBITaxon:387631","organism_count":"1"}'
  snapshot_sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
- evidence_id: mediadive-taxa
  kind: database
  reference: data/raw/mediadive_taxa.tsv
  accessed_at: '2026-10-21T07:10:15Z'
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
  accessed_at: '2026-10-21T07:10:15Z'
  support: supports
  summary: Inspected the exact Madin trait-assertion count row or bounded absence,
    without converting counts to phenotypes.
  locator: 'line 22943: {"taxon_id":"NCBITaxon:387631","assertion_count":"4"}'
  snapshot_sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
- evidence_id: bactotraits-taxa
  kind: database
  reference: data/raw/bactotraits_taxa.tsv
  accessed_at: '2026-10-21T07:10:15Z'
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
  accessed_at: '2026-10-21T08:24:48Z'
  support: supports
  summary: Policy permits source-scoped species-level closeMatch normalization and
    LPSN-linked species xrefs/synonyms, retains pooled broadMatch entries and carries
    NCBI lineage unchanged. Multiple reverse mappings do not alone establish a normalization
    defect or make species and strains identical.
  locator: Mapping predicates; Which strains belong to a record
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
- evidence_id: equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-21T08:24:48Z'
  support: supports
  summary: TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations
    remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes
    under the source taxon.
  locator: TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
- evidence_id: seed-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-21T08:24:48Z'
  support: supports
  summary: Inspected mapping ranking, qualified predicates, fixed broadMatch wording,
    synonym/xref construction, primary cluster counts and same-taxon type-strain derivation.
  locator: GTDB mapping construction lines 444–476; LPSN/type-strain and source-attestation
    construction
  snapshot_sha256: 3cc30f6413a293165385dfc1860505fe389e5adfe9aa3d168f76aa4cb2ac36bd
- evidence_id: manifest
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-21T08:24:48Z'
  support: supports
  summary: Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd,
    upstream input hashes and extraction time 2026-09-13T17:50:44Z.
  locator: kg_microbe_source, inputs, extracted_at
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
- evidence_id: overlay-manifests
  kind: record_content
  reference: data/atb/MANIFEST.yaml
  accessed_at: '2026-10-21T08:24:48Z'
  support: supports
  summary: Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z,
    matching the sole seed event. StrainInfo manifest is independently captured in
    source.inputs.
  locator: extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml
  snapshot_sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
- evidence_id: genome-catalog-1
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0017.jsonl.gz
  accessed_at: '2026-10-21T07:20:43Z'
  support: supports
  summary: Inspected every member of the selected GTDB source clusters, including
    original accession versions, NCBI taxid/species-taxid, source taxonomy and sample
    metadata. Whole-cluster counts are not counts exclusive to this NCBI taxon or
    proof of biological equivalence.
  locator: 'line 38543: {"accession":"RS_GCF_000385565.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus_A;s__Archaeoglobus_A
    sulfaticallidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Complete
    Genome","ncbi_assembly_name":"ASM38556v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN02028569","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"none","ncbi_date":"2013-04-30","ncbi_genbank_assembly_accession":"GCA_000385565.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus
    sulfaticallidus PM70-1","ncbi_protein_count":"2210","ncbi_refseq_category":"reference
    genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"2076931","ncbi_scaffold_n75":"2076931","ncbi_scaffold_n90":"2076931","ncbi_seq_rel_date":"2013-04-30","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1316941","ncbi_ssu_count":"1","ncbi_strain_identifiers":"PM70-1","ncbi_submitter":"University
    of Bergen, Centre for Geobiology, Department of Biology","ncbi_taxid":"387631","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    sulfaticallidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    sulfaticallidus;x__Archaeoglobus sulfaticallidus PM70-1","ncbi_total_gap_length":"0","ncbi_total_length":"2076931","ncbi_translation_table":"11","ncbi_trna_count":"51","ncbi_type_material_designation":"assembly
    from type material","ncbi_ungapped_length":"2076931","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"}'
  snapshot_sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
- evidence_id: gtdb-full-scan
  kind: search
  reference: data/catalog/MANIFEST.json
  accessed_at: '2026-10-21T07:20:43Z'
  support: supports
  summary: All 19 pinned GTDB shards and 901341 rows match the manifest. Every selected
    source cluster member was inspected. Distinct source taxonomies and NCBI taxa
    remain separate assertions; reverse multiplicity alone is not an exact-identity
    defect.
  locator: '{"target_id":"NCBITaxon:387631","source_cluster_counts":{"GTDB:s__Archaeoglobus_A_sulfaticallidus":1},"selected_members":1,"scan_receipt":"catalog-scan-receipt.json","scan_sha256":"10fe369d255a601f55990f99a4c115d91f5635fc74961265fd9fa53cb1907bb0"}'
  snapshot_sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
  search_scope: All enumerated GTDB primary shards, including ignored files. Exact
    source species ID from terminal species token with spaces converted to underscores;
    internal genus/epithet underscores preserved. Exact supplied GTDB genome accession
    also selected. No broad biological absence claim.
- evidence_id: mapping-target-rank
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-21T07:10:15Z'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
  support: supports
  summary: Pinned NCBI identity retains a STRAIN target and a separate species parent.
  locator: '[{"line":81841,"row":{"taxon_id":"NCBITaxon:387631","label":"Archaeoglobus
    sulfaticallidus PM70-1","rank":"STRAIN","parent_id":"NCBITaxon:1316941","genetic_code":"11","exact_synonyms":"Archaeoglobus
    sp. PM70-1","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon|gtdb|gold|madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"}},{"line":313610,"row":{"taxon_id":"NCBITaxon:1316941","label":"Archaeoglobus
    sulfaticallidus","rank":"SPECIES","parent_id":"NCBITaxon:2233","genetic_code":"11","exact_synonyms":"","related_synonyms":"Archaeoglobus
    sulfaticallidus Steinsbu et al. 2010","broad_synonyms":"","attested_by":"ncbitaxon|bacdive|lpsn|mediadive|gold|madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"}}]'
- evidence_id: mapping-current-ncbi
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1798180,1915565,1915566,1915567,1915568,1316941,387631,58290,693661,1906665&retmode=xml
  accessed_at: '2026-10-21T07:10:07Z'
  snapshot_sha256: 1ec169d5de9ceedc7ca4cb4b8f37dc2b0ba6e45602d47668125e0e50197368ce
  support: supports
  summary: The captured official NCBI response independently retains this exact strain
    rank, species parent and original source name classes.
  locator: 'TaxaSet/Taxon with TaxId equal to 387631: ScientificName, Rank, ParentTaxId,
    OtherNames, LineageEx'
- evidence_id: mapping-pinned-direct
  kind: database
  reference: data/raw/gtdb_mappings.tsv
  accessed_at: '2026-10-21T07:10:15Z'
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
  support: supports
  summary: The complete reverse scan returns only this source closeMatch, with count
    1; its qualified predicate remains a supplied source assertion.
  locator: '[{"line":285381,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_A_sulfaticallidus","gtdb_label":"s__Archaeoglobus_A_sulfaticallidus","gtdb_parent":"GTDB:g__Archaeoglobus_A","ncbitaxon_id":"NCBITaxon:387631","predicate":"skos:closeMatch","genome_count":"1"}}]'
  search_scope: Complete table of 322327 rows, including ignored location; exact source
    species identifier GTDB:s__Archaeoglobus_A_sulfaticallidus
- evidence_id: mapping-pinned-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-21T07:10:15Z'
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
  support: supports
  summary: The source species inventory retains the GTDB species identifier and whole-cluster
    genome count 1.
  locator: '[{"line":12296,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_A_sulfaticallidus","label":"s__Archaeoglobus_A_sulfaticallidus","parent":"GTDB:g__Archaeoglobus_A","genome_count":"1"}}]'
- evidence_id: mapping-primary-genome
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0017.jsonl.gz
  accessed_at: '2026-10-21T07:20:43Z'
  snapshot_sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
  support: supports
  summary: The complete selected GTDB cluster consists of this versioned RefSeq genome.
    Its strain taxid differs from its species_taxid. The supplied GenBank accession
    remains a separate typed field; no sequence equivalence or physical deposit join
    is inferred.
  locator: '{"line":38543,"row":{"accession":"RS_GCF_000385565.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus_A;s__Archaeoglobus_A
    sulfaticallidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Complete
    Genome","ncbi_assembly_name":"ASM38556v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN02028569","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"none","ncbi_date":"2013-04-30","ncbi_genbank_assembly_accession":"GCA_000385565.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus
    sulfaticallidus PM70-1","ncbi_protein_count":"2210","ncbi_refseq_category":"reference
    genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"2076931","ncbi_scaffold_n75":"2076931","ncbi_scaffold_n90":"2076931","ncbi_seq_rel_date":"2013-04-30","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1316941","ncbi_ssu_count":"1","ncbi_strain_identifiers":"PM70-1","ncbi_submitter":"University
    of Bergen, Centre for Geobiology, Department of Biology","ncbi_taxid":"387631","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    sulfaticallidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    sulfaticallidus;x__Archaeoglobus sulfaticallidus PM70-1","ncbi_total_gap_length":"0","ncbi_total_length":"2076931","ncbi_translation_table":"11","ncbi_trna_count":"51","ncbi_type_material_designation":"assembly
    from type material","ncbi_ungapped_length":"2076931","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"}}'
- evidence_id: mapping-full-census
  kind: search
  reference: data/catalog/MANIFEST.json
  accessed_at: '2026-10-21T07:20:43Z'
  snapshot_sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
  support: supports
  summary: All 19 GTDB shards and 901341 rows match the pinned RS232 manifest. Exactly
    one member was found for this source species, and the complete reverse table has
    one target.
  locator: '{"snapshot":"RS232","members":[{"path":"data/catalog/gtdb_genomes-0017.jsonl.gz","line":38543,"row":{"accession":"RS_GCF_000385565.1","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Halobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus_A;s__Archaeoglobus_A
    sulfaticallidus","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Complete
    Genome","ncbi_assembly_name":"ASM38556v1","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN02028569","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"none","ncbi_date":"2013-04-30","ncbi_genbank_assembly_accession":"GCA_000385565.1","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"none","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Archaeoglobus
    sulfaticallidus PM70-1","ncbi_protein_count":"2210","ncbi_refseq_category":"reference
    genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"2076931","ncbi_scaffold_n75":"2076931","ncbi_scaffold_n90":"2076931","ncbi_seq_rel_date":"2013-04-30","ncbi_spanned_gaps":"0","ncbi_species_taxid":"1316941","ncbi_ssu_count":"1","ncbi_strain_identifiers":"PM70-1","ncbi_submitter":"University
    of Bergen, Centre for Geobiology, Department of Biology","ncbi_taxid":"387631","ncbi_taxonomy":"d__Archaea;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    sulfaticallidus","ncbi_taxonomy_unfiltered":"d__Archaea;x__Methanobacteriati;p__Methanobacteriota;c__Archaeoglobi;o__Archaeoglobales;f__Archaeoglobaceae;g__Archaeoglobus;s__Archaeoglobus
    sulfaticallidus;x__Archaeoglobus sulfaticallidus PM70-1","ncbi_total_gap_length":"0","ncbi_total_length":"2076931","ncbi_translation_table":"11","ncbi_trna_count":"51","ncbi_type_material_designation":"assembly
    from type material","ncbi_ungapped_length":"2076931","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"},"selection_basis":["species_identifier"]}],"reverse_rows":[{"line":285381,"row":{"gtdb_id":"GTDB:s__Archaeoglobus_A_sulfaticallidus","gtdb_label":"s__Archaeoglobus_A_sulfaticallidus","gtdb_parent":"GTDB:g__Archaeoglobus_A","ncbitaxon_id":"NCBITaxon:387631","predicate":"skos:closeMatch","genome_count":"1"}}],"scan_receipt":"catalog-scan-receipt.json","scan_sha256":"10fe369d255a601f55990f99a4c115d91f5635fc74961265fd9fa53cb1907bb0"}'
  search_scope: All enumerated GTDB primary shards, including ignored files. Exact
    source species ID from terminal species token with spaces converted to underscores;
    internal genus/epithet underscores preserved. Exact supplied GTDB genome accession
    also selected. No broad biological absence claim.
- evidence_id: mapping-policy-scope
  kind: record_content
  reference: docs/HARMONIZATION.md
  accessed_at: '2026-10-21T07:10:15Z'
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
  support: supports
  summary: Local policy permits species-level normalization while preserving source
    taxonomy and asymmetric BacDive subtree imports. The finding is specifically about
    species identity asserted on a strain-ranked target, not a generic closeMatch-versus-exact
    distinction.
  locator: Mapping predicates, lines122–144; Which strains belong to a record, lines146–168;
    Type strains, lines174–183
- evidence_id: mapping-equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-21T07:10:15Z'
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
  support: supports
  summary: TaxonRecord.xrefs is reserved for true equivalences; broader/narrower relations
    remain qualified. TaxonomyMapping.genome_count counts the complete source taxon.
  locator: TaxonRecord.xrefs, lines180–185; TaxonomyMapping.mapping_predicate and
    genome_count, lines428–436
- evidence_id: mapping-maintained-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-21T07:10:15Z'
  snapshot_sha256: 3cc30f6413a293165385dfc1860505fe389e5adfe9aa3d168f76aa4cb2ac36bd
  support: supports
  summary: The maintained seeder treats every closeMatch as identity and promotes
    its GTDB species identifier and normalized exact synonym without checking the
    native target rank.
  locator: GTDB mapping construction, lines443–473; identity at455 and xref/exact-synonym
    promotion at470–473
- evidence_id: mapping-parent-nomenclature
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-21T07:10:15Z'
  snapshot_sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
  support: supports
  summary: The relevant LPSN name maps to the distinct species parent and has empty
    gtdb_ids; it supplies no alternate GTDB identity bridge to this strain target.
  locator: '[{"line":25993,"row":{"lpsn_id":"lpsn:788917","name":"Archaeoglobus sulfaticallidus","rank":"SPECIES","authority":"Steinsbu
    et al. 2010","url":"https://lpsn.dsmz.de/species/archaeoglobus-sulfaticallidus","deprecated":"0","status":"legitimate=True;
    validly published under the ICNP; correct name","validly_published":"1","legitimate":"1","is_correct_name":"1","parent_lpsn_id":"lpsn:516970","ncbitaxon_ids":"NCBITaxon:1316941","gtdb_ids":"","type_strain_ids":"kgmicrobe.strain:DSM-19444|kgmicrobe.strain:JCM-14716","synonym_of":"","synonyms":"","publications":"PMID:20061497|doi:10.1099/ijs.0.016105-0|doi:10.1099/ijs.0.031948-0","sequence_accessions":"INSDC:FJ810190"}}]'
- evidence_id: mapping-bacdive-classification
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-21T07:10:15Z'
  snapshot_sha256: 029fd6d1f53ef7f90684130bf0d644ed3edd1d8fbeb065a511ae928f160b1eea
  support: supports
  summary: BacDive retains its own exact source taxon classification. Name similarity
    or a species type designation does not move the classification into a child strain
    record.
  locator: '[{"line":17909,"row":{"strain_id":"kgmicrobe.strain:bacdive_18100","bacdive_id":"18100","designation":"PM70-1","taxon_ids":"NCBITaxon:1316941","lpsn_ids":"lpsn:788917","culture_collection_ids":"kgmicrobe.strain:DSM-19444|kgmicrobe.strain:JCM-14716","medium_count":"0"}}]'
- evidence_id: finding-deduplication
  kind: search
  reference: Owned review worktrees structured bundles
  accessed_at: '2026-10-21T07:15:46Z'
  support: supports
  summary: No same-target saved review or matching stable finding key was found in
    the bounded ignored-inclusive search. This is not a corpus coverage claim.
  locator: '{"keys":["gtdb-closematch-exact-promotion-387631"],"yaml_files_read":780,"unique_review_id_and_byte_hash_pairs":169}'
  snapshot_sha256: f06c6cb0b771b811e95de0b6d5129d8301835044453e140b953bda42736cc126
  search_scope: os.walk over every existing owned repo/repo-batch-* reviews/structured
    directory, including hidden and gitignored files; all .yaml/.yml files read directly.
    No TSV inventory or unsaved preview counts treated as reviewed targets.
- evidence_id: historical-gold-edge
  kind: search
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T07:30:22Z'
  support: partial
  summary: Retained configured-path source check found bytes differing from the manifest-pinned
    original; this does not establish global absence.
  locator: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/gold/edges.tsv;expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12;observed=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d
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
  locator: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv;expected=3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f;observed=c19bfc848e1b410548614c54a2b99e2c58452d58aeb61f972c99fcb3039a1d24
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
  search_scope: Exact configured historical input path, including ignored files; retained
    actual receipt, not a new source search.
- evidence_id: native-gate-reuse
  kind: validation
  reference: /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0018/native-gate-reuse.json
  accessed_at: '2026-10-21T07:51:59Z'
  support: supports
  summary: Retained explicit verification of identical base/native inputs authorizes
    historical native-gate reuse; original command receipts remain separately cited.
  locator: base, native_inputs_unchanged, source_directory, gates, input_proof_path
    and input_proof_sha256
  snapshot_sha256: f927228bb46e9a24de608c8abfc9e455adf6b616b10ba75e55d7162cb7c085ba
- evidence_id: strict-receipt
  kind: validation
  reference: just validate-strict data/taxa/archaea/archaeoglobus_sulfaticallidus_pm70_1.yaml
    --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0018/strict-07.tsv
  accessed_at: '2026-10-21T07:10:23Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0018/repo;\
    \ started 2026-10-21T07:10:20Z, finished 2026-10-21T07:10:23Z, exit 0. This exact\
    \ generated YAML only; its captured bytes remain unchanged. Actual earlier per-target\
    \ invocation; the receipt retains its original cwd and times.\nValidating 1 files\
    \ with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0016/src/taxonmech/schema/taxonmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0018/strict-07.tsv"
  locator: This exact generated YAML only; its captured bytes remain unchanged. Actual
    earlier per-target invocation; the receipt retains its original cwd and times.
  snapshot_sha256: 55bab943d303a9baf262e27784beaeabe82054108f42edb9d685ab8d0eaedaee
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
    certificate; these are historical runs, not new batch-0018 invocations. Missing
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
    certificate; these are historical runs, not new batch-0018 invocations. Missing
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
    \ these are historical runs, not new batch-0018 invocations. Missing terminal\
    \ receipts or reuse proof remain unavailable in unsaved previews. Exact-target\
    \ strict receipts retain their original execution context. New review bundles\
    \ still require individual validation/save/check.\nuv run python scripts/verify_corpus.py\
    \ \nexpected 626048 records, found 626048 on disk\n  missing:   0\n  extra:  \
    \   0\n  differing: 0\n\ncorpus reproduces exactly from data/raw/ and curation/seed_scope.tsv"
  locator: All 626,048 generated taxon YAMLs, not a focused approximation. Actual
    native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
    original cwd, times, commands, log hashes and terminal exit codes identify the
    executions. Reused repository-wide receipts require the explicit same-base/native-input
    certificate; these are historical runs, not new batch-0018 invocations. Missing
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
    certificate; these are historical runs, not new batch-0018 invocations. Missing
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
    certificate; these are historical runs, not new batch-0018 invocations. Missing
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
    \ these are historical runs, not new batch-0018 invocations. Missing terminal\
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
    these are historical runs, not new batch-0018 invocations. Missing terminal receipts
    or reuse proof remain unavailable in unsaved previews. Exact-target strict receipts
    retain their original execution context. New review bundles still require individual
    validation/save/check.
  snapshot_sha256: dcb3f98d5c8ce264240732733ca70a5b93ee3e818d03f809d428748abffefca3
assessments:
- assessment_id: mapping-rank-scope
  area: grounding
  topic: GTDB species concept versus native strain identity
  outcome: concern
  summary: The complete pinned RS232 cluster GTDB:s__Archaeoglobus_A_sulfaticallidus
    contains only RS_GCF_000385565.1 at data/catalog/gtdb_genomes-0017.jsonl.gz:38543.
    It identifies ncbi_taxid 387631 but ncbi_species_taxid 1316941. The native record
    is STRAIN under that separate species parent. Its supplied closeMatch and genome
    count 1 are supported. Promoting the GTDB species into unqualified xrefs and EXACT_SYNONYM
    Archaeoglobus A sulfaticallidus overstates species-to-strain identity. A singleton
    cluster does not make the species concept identical to its one sampled strain.
  target_ids:
  - NCBITaxon:387631
  evidence_ids:
  - record
  - mapping-target-rank
  - mapping-current-ncbi
  - mapping-pinned-direct
  - mapping-pinned-species
  - mapping-primary-genome
  - mapping-full-census
  - mapping-policy-scope
  - mapping-equivalence-contract
  - mapping-maintained-owner
  - mapping-parent-nomenclature
  - mapping-bacdive-classification
- assessment_id: mapping-ncbi-name-classes
  area: nomenclature
  topic: NCBI strain names and parent-species type boundary
  outcome: supported
  summary: Current and pinned NCBI retain Archaeoglobus sp. PM70-1 as an exact synonym
    of strain 387631. The LPSN species name and type designations belong to parent
    species 1316941. BacDive 18100 is filed directly at that parent; a genome taxid
    or matching PM70-1 label does not make it an imported child strain. The zero imported-strain
    count is source-consistent. The separate GTDB exact synonym and xref carry the
    species-to-strain scope defect documented in the finding.
  target_ids:
  - NCBITaxon:387631
  evidence_ids:
  - record
  - mapping-target-rank
  - mapping-current-ncbi
  - mapping-pinned-direct
  - mapping-pinned-species
  - mapping-primary-genome
  - mapping-full-census
  - mapping-policy-scope
  - mapping-equivalence-contract
  - mapping-maintained-owner
  - mapping-parent-nomenclature
  - mapping-bacdive-classification
- assessment_id: identity
  area: identity
  topic: Exact taxon and source lineage
  outcome: supported
  summary: NCBITaxon:387631 is Archaeoglobus sulfaticallidus PM70-1 at STRAIN rank
    under species NCBITaxon:1316941, with genetic code 11. The exact target, all ten
    carried ancestor IDs, literal names and ranks agree with pinned NCBI and the captured
    current official response; the latter omits only root. Archaeoglobus sp. PM70-1
    remains the source NCBI synonym.
  target_ids:
  - NCBITaxon:387631
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - scope-row
  - path-row
  dimensions:
  - name: native-rank
    value: STRAIN
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
  summary: Current and pinned NCBI retain Archaeoglobus sp. PM70-1 as an exact synonym
    of strain 387631. The LPSN species name and type designations belong to parent
    species 1316941. BacDive 18100 is filed directly at that parent; a genome taxid
    or matching PM70-1 label does not make it an imported child strain. The zero imported-strain
    count is source-consistent. The separate GTDB exact synonym and xref carry the
    species-to-strain scope defect documented in the finding.
  target_ids:
  - NCBITaxon:387631
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - lpsn-inventory
  - mapping-policy
  - mapping-target-rank
  - mapping-current-ncbi
  - mapping-pinned-direct
  - mapping-pinned-species
  - mapping-primary-genome
  - mapping-full-census
  - mapping-policy-scope
  - mapping-equivalence-contract
  - mapping-maintained-owner
  - mapping-parent-nomenclature
  - mapping-bacdive-classification
  - genome-catalog-1
  - gtdb-full-scan
- assessment_id: completeness
  area: completeness
  topic: Imported subtree and source assertion units
  outcome: supported
  summary: Complete reads of twelve pinned source/scope/path tables, including ignored
    files, used the exact identifier, full name, slug, source synonym and GTDB species
    ID. There are no descendants and no directly classified imported BacDive strain
    or culture-inventory row. BacDive 18100 is classified at parent species 1316941,
    so its PM70-1 designation and genome links do not create a child import. NCBITAXON
    1 NAME, GTDB 1 GENOME, GOLD 1 ORGANISM and MADIN 4 TRAIT_ASSERTION match their
    respective projection rows; the single GTDB cluster member was independently counted
    across all nineteen shards. GOLD and MADIN aggregate values were not independently
    reconstructed from manifest-matching historical primary inputs. Other named optional-source
    misses are bounded to these pinned tables, not worldwide biological absence.
  target_ids:
  - NCBITaxon:387631
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
  - mapping-target-rank
  - mapping-current-ncbi
  - mapping-pinned-direct
  - mapping-pinned-species
  - mapping-primary-genome
  - mapping-full-census
  - mapping-policy-scope
  - mapping-equivalence-contract
  - mapping-maintained-owner
  - mapping-parent-nomenclature
  - mapping-bacdive-classification
- assessment_id: taxonomy-mapping
  area: grounding
  topic: Qualified species mapping and target scope
  outcome: concern
  summary: The complete pinned RS232 cluster GTDB:s__Archaeoglobus_A_sulfaticallidus
    contains only RS_GCF_000385565.1 at data/catalog/gtdb_genomes-0017.jsonl.gz:38543.
    It identifies ncbi_taxid 387631 but ncbi_species_taxid 1316941. The native record
    is STRAIN under that separate species parent. Its supplied closeMatch and genome
    count 1 are supported. Promoting the GTDB species into unqualified xrefs and EXACT_SYNONYM
    Archaeoglobus A sulfaticallidus overstates species-to-strain identity. A singleton
    cluster does not make the species concept identical to its one sampled strain.
  target_ids:
  - NCBITaxon:387631
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
  - mapping-target-rank
  - mapping-current-ncbi
  - mapping-pinned-direct
  - mapping-pinned-species
  - mapping-primary-genome
  - mapping-full-census
  - mapping-policy-scope
  - mapping-equivalence-contract
  - mapping-maintained-owner
  - mapping-parent-nomenclature
  - mapping-bacdive-classification
- assessment_id: native-status
  area: provenance
  topic: Unchanged native status and history
  outcome: supported
  summary: EXACT grounding and SEEDED mapping status retain the source state. The
    sole SEEDED_FROM_SOURCES event at 2026-09-13T17:54:04Z matches the maximum raw/ATB/StrainInfo
    manifest extraction time and exact scope/path rows. The confirmed GTDB scope finding
    does not justify changing the carried NCBI identity or hand-editing this generated
    record.
  target_ids:
  - NCBITaxon:387631
  evidence_ids:
  - record
  - manifest
  - overlay-manifests
  - scope-row
  - path-row
findings:
- finding_id: gtdb-strain-scope
  issue_key: gtdb-closematch-exact-promotion-387631
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: GTDB species identity is promoted into STRAIN equivalence
  description: The complete pinned RS232 cluster GTDB:s__Archaeoglobus_A_sulfaticallidus
    contains only RS_GCF_000385565.1 at data/catalog/gtdb_genomes-0017.jsonl.gz:38543.
    It identifies ncbi_taxid 387631 but ncbi_species_taxid 1316941. The native record
    is STRAIN under that separate species parent. Its supplied closeMatch and genome
    count 1 are supported. Promoting the GTDB species into unqualified xrefs and EXACT_SYNONYM
    Archaeoglobus A sulfaticallidus overstates species-to-strain identity. A singleton
    cluster does not make the species concept identical to its one sampled strain.
  target_ids:
  - NCBITaxon:387631
  field_paths:
  - synonyms[source=GTDB,synonym_text=Archaeoglobus A sulfaticallidus]
  - xrefs[GTDB:s__Archaeoglobus_A_sulfaticallidus]
  evidence_ids:
  - record
  - mapping-target-rank
  - mapping-current-ncbi
  - mapping-pinned-direct
  - mapping-pinned-species
  - mapping-primary-genome
  - mapping-full-census
  - mapping-policy-scope
  - mapping-equivalence-contract
  - mapping-maintained-owner
  - mapping-parent-nomenclature
  - mapping-bacdive-classification
  rule_id: TaxonRecord.xrefs equivalence contract; docs/HARMONIZATION.md Mapping predicates;
    preserve species-versus-strain claim scope
  native_severity: major
  normalization_reason: Material species-to-strain scope inflation; native NCBI identity
    and the supplied qualified mapping remain supported.
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Maintained GTDB identity promotion and target-rank scope
actions:
- action_id: guard-gtdb-strain-equivalence
  description: Make GTDB species identity promotion rank-aware in the maintained seeder.
    Preserve the qualified source mapping, count, NCBI name classes and independently
    supported strain links. Regenerate through native gates after separately authorized
    curation; do not directly edit generated YAML.
  finding_ids:
  - gtdb-strain-scope
  target_ids:
  - NCBITaxon:387631
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Maintained GTDB identity promotion and target-rank scope
  acceptance_checks:
  - Retain the distinct NCBI STRAIN identity and species parent.
  - Prevent a species-level GTDB xref or exact synonym from asserting exact strain
    identity.
  - Retain the source closeMatch, whole-cluster count 1 and supported strain/genome
    evidence; retain valid species-level normalization.
  - Change maintained inputs only; verify strict, history, product, corpus and QC
    gates after authorized regeneration.
- action_id: recover-pinned-aggregate-inputs
  finding_ids: []
  target_ids:
  - NCBITaxon:387631
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
- The singleton GTDB cluster count and accession versions are supported; this finding
  does not assert multiple cluster members or a strain-link defect.
- GTDB species normalization remains allowed for species-level targets. This is an
  explicit rank/scope mismatch, independent of generic SKOS predicate differences.
- GOLD 1 ORGANISM and MADIN 4 TRAIT_ASSERTION agree with pinned inventory projections;
  no independent recount from the original manifest-hash-matching aggregate inputs
  was performed. Counts do not establish a phenotype or mechanism.
- A matching type-strain label or genome taxid does not move a BacDive classification
  from the parent species into this child. No deposited-culture absence is claimed.
- Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
  original cwd, times, commands, log hashes and terminal exit codes identify the executions.
  Reused repository-wide receipts require the explicit same-base/native-input certificate;
  these are historical runs, not new batch-0018 invocations. Missing terminal receipts
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
- batch-0018
- archaea
- generated
- source-checked
```
