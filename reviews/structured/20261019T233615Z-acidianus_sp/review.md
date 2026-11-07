# Record review: Acidianus sp.

- Review: 20261019T233615Z-acidianus_sp
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-19T07:41:46Z
- Finished UTC: 2026-10-19T23:36:15Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete generated record identifies NCBITaxon:1872104 as the NCBI species-rank placeholder Acidianus sp. Its rank, parent, carried lineage and genetic code agree with the pinned taxonomy and current NCBI response. Both GTDB associations remain pooled broadMatch mappings, with source-cluster counts of seven and six; no exact GTDB synonym or xref is asserted. Historical verification of the one-medium attestation remains unavailable because the original edge snapshot could not be recovered from the checked locations. No record-specific curation finding was established.

## Scope And Provenance

The entire single resolved generated TaxonRecord and its identity, nomenclature, mapping, imported strain, source-count and provenance assertions.

Selection: Path-ordered unreviewed record 11 at unchanged base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; batch-0002 record 1. The first batch's ten newly saved targets were excluded using validated bundle listings, together with the 52 previously covered actual corpus targets. Reviewed means an actual target of a validated bundle listed by scripts/record_review.py list; historical TSV inventories do not substitute for bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9b5a8fff5185b38dc5c77bb35235152c81ea7765.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:1872104 | data/taxa/archaea/acidianus_sp.yaml | generated | Acidianus sp. |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact NCBI taxon, rank and lineage | passed | True | NCBITaxon:1872104 | The exact target is NCBITaxon:1872104, distinct from its unclassified Acidianus parent 2629519, genus 12914 and named Acidianus species. NCBI assigns SPECIES rank even though its scientific label is Acidianus sp. All ten carried ancestors, including root and the unclassified parent, and genetic code 11 agree with the pinned taxonomy; the current NCBI response confirms the same identity and parent chain. No physical strain identity is inferred from species rank. |
| Imported strain and genome assertion check | not_applicable | False | NCBITaxon:1872104 | There is no imported BacDive strain or strain-level genome assertion. Exact source inventory/subtree selection was checked; genome catalog entries and isolate names do not create physical deposits. |
| Bounded GTDB primary-row and cluster-count check | passed | True | NCBITaxon:1872104 | GTDB:s__Acidianus_hospitalis: selected rows=7, inventory count=7, exact target taxid rows=4; GTDB:s__Acidilobus_sp000495735: selected rows=6, inventory count=6, exact target taxid rows=1. Source counts agree within the explicitly scanned shards; no whole-catalog absence or sequence-equivalence claim is made. |
| Original MediaDive medium set | unavailable | True | NCBITaxon:1872104 | The inventory supports one medium, mediadive.medium:88, but the original manifest-pinned MediaDive edge bytes were unavailable in the checked locations. The differently hashed current file cannot independently reproduce the historical taxon-to-medium association. |
| Initial quality-gate setup attempt | failed | False | NCBITaxon:1872104 | Actual exit 1: missing ruff; superseded by the separately recorded successful full retry. |
| Native strict record validation | passed | True | NCBITaxon:1872104 | Actual terminal exit code 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. |
| Repository history validation | passed | True | NCBITaxon:1872104 | Actual terminal exit code 0. All 17 standalone history records; the generated seed event was also inspected in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| Full-corpus exact reproduction | passed | True | NCBITaxon:1872104 | Actual terminal exit code 0. All 625,960 generated taxon YAMLs, not a focused approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| Native product ID/label gate | passed | True | NCBITaxon:1872104 | Actual terminal exit code 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| Authoritative complete quality gate | passed | True | NCBITaxon:1872104 | Actual terminal exit code 0. Repository-wide just qc, including native corpus-wide checks. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. Pytest reported 1055 passed, 3 skipped and 5 deselected; the native QC recipe completed successfully. |

## Scientific And Domain Assessments

### Resolved biological taxon and carried lineage

identity: supported. Targets: NCBITaxon:1872104.

The exact target is NCBITaxon:1872104, distinct from its unclassified Acidianus parent 2629519, genus 12914 and named Acidianus species. NCBI assigns SPECIES rank even though its scientific label is Acidianus sp. All ten carried ancestors, including root and the unclassified parent, and genetic code 11 agree with the pinned taxonomy; the current NCBI response confirms the same identity and parent chain. No physical strain identity is inferred from species rank.

### Source-scoped names and nomenclatural standing

nomenclature: supported. Targets: NCBITaxon:1872104.

The literal NCBI scientific name is retained. Neither the pinned NCBI inventory nor the current NCBI response supplies an additional name class for this target. The inspected LPSN inventory has no exact mapped name. Both GTDB names remain source-qualified mappings rather than exact synonyms or equivalent xrefs. The record makes no ICNP-validity or type-material claim.

### Complete imported subtree and source assertion units

completeness: supported. Targets: NCBITaxon:1872104.

Complete pinned inventory and parent-graph selection found no descendant taxon, BacDive strain or culture-collection row for this target. Zero imported strains is consistent with those inputs despite the independently observed catalog genomes; genome entries are not automatically physical strain deposits. The three source attestations retain distinct units: one NCBI name, seven genomes in the primary pooled GTDB cluster, and one MediaDive medium. The exact MediaDive inventory row names medium 88. GOLD, Madin and BactoTraits have no exact target row in their inspected complete inventories. This is bounded imported-source coverage, not worldwide absence.

### GTDB source mapping scope and cluster counts

grounding: supported. Targets: NCBITaxon:1872104.

The complete selected RS232 catalog rows reproduce the seven-member Acidianus hospitalis cluster and six-member Acidilobus sp000495735 cluster. Four hospitalis genomes and one Acidilobus genome carry target taxid 1872104; the other members carry different NCBI taxa. These are pooled source-cluster counts, not seven and six genomes assigned exclusively to this NCBI target. Both broadMatch predicates and their explanatory notes preserve that scope. The primary GTDB attestation reports seven and points to the additional cluster in taxonomy_mappings; it does not claim a combined thirteen-genome total. GB_GCA_032248955.1 (RBS.bin.4) explicitly carries NCBI Acidianus sp. while GTDB places it in Acidilobus; the record correctly preserves both source classifications without replacing the NCBI lineage.

### Seed event and scientific-status boundary

provenance: supported. Targets: NCBITaxon:1872104.

EXACT grounding denotes the resolved NCBI identity. SEEDED status and the single 2026-09-13T17:54:04Z seed event remain unchanged and agree with the maximum source-manifest extraction timestamp. A review does not confer native human-reviewed status.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### verify-pinned-mediadive-edges

Recover the upstream MediaDive edge snapshot with the SHA-256 pinned in data/raw/MANIFEST.yaml, then use extract_mediadive's exact-target METPO:2000517 selection to independently verify the distinct medium set for NCBITaxon:1872104. This resolves the historical association limitation without editing generated records.

- Recovered data/transformed/mediadive/edges.tsv bytes match the manifest SHA-256 before use.
- Select only subject NCBITaxon:1872104 with predicate METPO:2000517; preserve the direct-taxon boundary and count distinct medium objects.
- Compare that set with data/raw/mediadive_taxa.tsv line 5650: medium_count 1 and media_ids mediadive.medium:88. Retain any discrepancy in a new observation instead of editing this immutable review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/taxa/archaea/acidianus_sp.yaml; entire TaxonRecord; identifier=NCBITaxon:1872104 | supports | Read the entire generated YAML, including identity, lineage, names, mappings, source attestations, imported strain count and seed history. |
| taxonomy-inventory | data/raw/ncbitaxon_taxa.tsv; line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""}; line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"}; line 1798: {"taxon_id":"NCBITaxon:2281","label":"Sulfolobales","rank":"ORDER","parent_id":"NCBITaxon:183924"}; line 2648: {"taxon_id":"NCBITaxon:12914","label":"Acidianus","rank":"GENUS","parent_id":"NCBITaxon:118883"}; line 2980: {"taxon_id":"NCBITaxon:28889","label":"Thermoproteota","rank":"PHYLUM","parent_id":"NCBITaxon:1783275"}; line 22254: {"taxon_id":"NCBITaxon:118883","label":"Sulfolobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2281"}; line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"}; line 36612: {"taxon_id":"NCBITaxon:183924","label":"Thermoprotei","rank":"CLASS","parent_id":"NCBITaxon:28889"}; line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"}; line 489187: {"taxon_id":"NCBITaxon:1872104","label":"Acidianus sp.","rank":"SPECIES","parent_id":"NCBITaxon:2629519","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb&#124;mediadive","retired_into":"","taxonomy_snapshot":"2026-09-13"}; line 538477: {"taxon_id":"NCBITaxon:2629519","label":"unclassified Acidianus","rank":"NO_RANK","parent_id":"NCBITaxon:12914"} | supports | Inspected the exact target row and every carried ancestor; compared rank, label, parent, genetic code and source name classes with the complete record. |
| scope-row | curation/seed_scope.tsv; line 30915: {"identifier":"NCBITaxon:1872104","added":"2026-09-12","reason":"attested rule: Acidianus sp., 3 sources incl. NCBI"} | supports | The exact target is explicitly included in the seed scope. |
| path-row | data/taxa/PATHS.tsv; line 296625: {"identifier":"NCBITaxon:1872104","slug":"acidianus_sp"} | supports | The indexed path resolves to the same NCBI taxon and generated target. |
| ncbi-live | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1872104; TaxaSet/Taxon[TaxId='1872104']; captured with the other nine selected batch-0002 taxa | supports | Inspected the official taxonomy response for this exact taxon: scientific name, rank, parent, source name classes, lineage identifiers and genetic code. The current response is distinguished from the pinned September inventory. |
| lpsn-inventory | data/raw/lpsn_names.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Inspected exact mapped LPSN names and any linked names; a bounded inventory miss does not establish worldwide nomenclatural absence. |
| gtdb-mappings | data/raw/gtdb_mappings.tsv; line 25048: {"gtdb_id":"GTDB:s__Acidilobus_sp000495735","gtdb_label":"s__Acidilobus_sp000495735","gtdb_parent":"GTDB:g__Acidilobus","ncbitaxon_id":"NCBITaxon:1410573","predicate":"skos:closeMatch","genome_count":"6"}; line 25050: {"gtdb_id":"GTDB:s__Acidilobus_sp000495735","gtdb_label":"s__Acidilobus_sp000495735","gtdb_parent":"GTDB:g__Acidilobus","ncbitaxon_id":"NCBITaxon:1410575","predicate":"skos:closeMatch","genome_count":"6"}; line 25051: {"gtdb_id":"GTDB:s__Acidilobus_sp000495735","gtdb_label":"s__Acidilobus_sp000495735","gtdb_parent":"GTDB:g__Acidilobus","ncbitaxon_id":"NCBITaxon:1410576","predicate":"skos:closeMatch","genome_count":"6"}; line 70969: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","gtdb_label":"s__Acidianus_hospitalis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:1872104","predicate":"skos:broadMatch","genome_count":"7"}; line 70970: {"gtdb_id":"GTDB:s__Acidilobus_sp000495735","gtdb_label":"s__Acidilobus_sp000495735","gtdb_parent":"GTDB:g__Acidilobus","ncbitaxon_id":"NCBITaxon:1872104","predicate":"skos:broadMatch","genome_count":"6"}; line 70987: {"gtdb_id":"GTDB:s__Acidilobus_sp000495735","gtdb_label":"s__Acidilobus_sp000495735","gtdb_parent":"GTDB:g__Acidilobus","ncbitaxon_id":"NCBITaxon:1872109","predicate":"skos:broadMatch","genome_count":"6"}; line 296668: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","gtdb_label":"s__Acidianus_hospitalis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:563177","predicate":"skos:closeMatch","genome_count":"7"}; line 320834: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","gtdb_label":"s__Acidianus_hospitalis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:933801","predicate":"skos:closeMatch","genome_count":"7"} | supports | Inspected this taxon's mappings and reverse mappings of the selected clusters; retained source predicates and cluster-scoped counts. |
| gtdb-species | data/raw/gtdb_species.tsv; line 3494: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","label":"s__Acidianus_hospitalis","parent":"GTDB:g__Acidianus","genome_count":"7"}; line 3967: {"gtdb_id":"GTDB:s__Acidilobus_sp000495735","label":"s__Acidilobus_sp000495735","parent":"GTDB:g__Acidilobus","genome_count":"6"} | supports | Inspected source species identifiers, labels, parent cluster and genome counts. |
| bacdive-inventory | data/raw/bacdive_strains.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Full inventory selection used the exact taxon and every descendant from the complete NCBI parent graph; no classified BacDive strain was found in this bounded subtree. |
| culture-inventory | data/raw/culture_collection_strains.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Inspected exact culture-inventory associations with the target; a genome or isolate name does not supply an inferred physical deposit. |
| gold-organisms | data/raw/gold_organisms.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Inspected the exact GOLD organism count row, or its bounded absence, without converting counts to phenotypes. |
| mediadive-taxa | data/raw/mediadive_taxa.tsv; line 5650: {"taxon_id":"NCBITaxon:1872104","medium_count":"1","media_ids":"mediadive.medium:88"} | supports | Inspected the exact MediaDive medium count row, or its bounded absence, without converting counts to phenotypes. |
| madin-taxa | data/raw/madin_taxa.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Inspected the exact Madin trait-assertion count row, or its bounded absence, without converting counts to phenotypes. |
| bactotraits-taxa | data/raw/bactotraits_taxa.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Inspected the exact BactoTraits trait-assertion count row, or its bounded absence, without converting counts to phenotypes. |
| mapping-policy | docs/HARMONIZATION.md; Mapping predicates and Which strains belong to a record sections | supports | The local policy permits one-to-one species closeMatch mappings and LPSN-linked species to supply xrefs/synonyms, retains pooled broadMatch entries separately and carries NCBI lineage unchanged. |
| equivalence-contract | src/taxonmech/schema/taxonmech.yaml; TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439 | supports | TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes under the source taxon. |
| seed-owner | src/taxonmech/seed.py; GTDB mapping construction, lines 440–472, and source-attestation construction | supports | Inspected the maintained mapping ranking, source predicate retention, synonym/xref construction and primary-source genome-count selection against this target's represented fields. |
| manifest | data/raw/MANIFEST.yaml; kg_microbe_source, inputs, extracted_at | supports | The manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd and individual upstream input hashes; extraction time is 2026-09-13T17:50:44Z. |
| overlay-manifests | data/atb/MANIFEST.yaml; extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml | supports | Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z, matching this record's sole generated seed event. The StrainInfo manifest is independently captured in source.inputs. |
| genome-catalog-manifest | data/catalog/MANIFEST.json; coverage.sources[name=GTDB] | supports | The native GTDB catalog records the RS232 source snapshot. This review's primary-row scan is bounded to shards 0017 and 0018. |
| genome-catalog-1 | data/catalog/gtdb_genomes-0017.jsonl.gz; line 29105: {"accession":"GB_GCA_032248955.1","gtdb_representative":"f","ncbi_taxid":"1872104","ncbi_species_taxid":"1872104","ncbi_organism_name":"Acidianus sp.","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Acidilobus;s__Acidilobus sp000495735","ncbi_strain_identifiers":"RBS.bin.4"}; line 31775: {"accession":"GB_GCA_028277005.1","gtdb_representative":"f","ncbi_taxid":"1872109","ncbi_species_taxid":"1872109","ncbi_organism_name":"Acidilobus sp.","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Acidilobus;s__Acidilobus sp000495735","ncbi_strain_identifiers":"RSEP6"}; line 32156: {"accession":"GB_GCA_032249015.1","gtdb_representative":"f","ncbi_taxid":"1872104","ncbi_species_taxid":"1872104","ncbi_organism_name":"Acidianus sp.","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus hospitalis","ncbi_strain_identifiers":"RBS.bin.2"}; line 37598: {"accession":"RS_GCF_046537415.1","gtdb_representative":"f","ncbi_taxid":"1872104","ncbi_species_taxid":"1872104","ncbi_organism_name":"Acidianus sp.","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus hospitalis","ncbi_strain_identifiers":"Alice.S.bin.1"}; line 37916: {"accession":"GB_GCA_046533895.1","gtdb_representative":"t","ncbi_taxid":"563177","ncbi_species_taxid":"563177","ncbi_organism_name":"Acidianus hospitalis","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus hospitalis","ncbi_strain_identifiers":"RHS.bin.1"}; line 38348: {"accession":"GB_GCA_000495715.1","gtdb_representative":"f","ncbi_taxid":"1410575","ncbi_species_taxid":"1410575","ncbi_organism_name":"uncultured Acidilobus sp. OSP8","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Acidilobus;s__Acidilobus sp000495735","ncbi_strain_identifiers":"none"}; line 43564: {"accession":"GB_GCA_000495735.1","gtdb_representative":"t","ncbi_taxid":"1410576","ncbi_species_taxid":"1410576","ncbi_organism_name":"uncultured Acidilobus sp. JCHS","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Acidilobus;s__Acidilobus sp000495735","ncbi_strain_identifiers":"none"}; line 43616: {"accession":"GB_GCA_022759325.1","gtdb_representative":"f","ncbi_taxid":"1872109","ncbi_species_taxid":"1872109","ncbi_organism_name":"Acidilobus sp.","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Acidilobus;s__Acidilobus sp000495735","ncbi_strain_identifiers":"2016_B01_C_1"}; line 46762: {"accession":"GB_GCA_003086435.1","gtdb_representative":"f","ncbi_taxid":"563177","ncbi_species_taxid":"563177","ncbi_organism_name":"Acidianus hospitalis","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus hospitalis","ncbi_strain_identifiers":"SCGC AC-742_N10"}; line 47899: {"accession":"RS_GCF_046534395.1","gtdb_representative":"f","ncbi_taxid":"1872104","ncbi_species_taxid":"1872104","ncbi_organism_name":"Acidianus sp.","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus hospitalis","ncbi_strain_identifiers":"Moose.S.bin.11"}; line 49253: {"accession":"RS_GCF_000213215.1","gtdb_representative":"f","ncbi_taxid":"933801","ncbi_species_taxid":"563177","ncbi_organism_name":"Acidianus hospitalis W1","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus hospitalis","ncbi_strain_identifiers":"W1"}; line 49816: {"accession":"GB_GCA_000495675.1","gtdb_representative":"f","ncbi_taxid":"1410573","ncbi_species_taxid":"1410573","ncbi_organism_name":"uncultured Acidilobus sp. MG","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Acidilobus;s__Acidilobus sp000495735","ncbi_strain_identifiers":"none"} | supports | Inspected complete selected primary genome rows, separating source genome identifiers, taxon assignments and isolate labels. Source cluster membership does not establish assembly or deposit equivalence. |
| genome-catalog-2 | data/catalog/gtdb_genomes-0018.jsonl.gz; line 1150: {"accession":"GB_GCA_046533515.1","gtdb_representative":"f","ncbi_taxid":"1872104","ncbi_species_taxid":"1872104","ncbi_organism_name":"Acidianus sp.","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus hospitalis","ncbi_strain_identifiers":"SBS.bin.13"} | supports | Inspected complete selected primary genome rows, separating source genome identifiers, taxon assignments and isolate labels. Source cluster membership does not establish assembly or deposit equivalence. |
| historical-edge-availability | data/raw/MANIFEST.yaml; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/mediadive/edges.tsv; expected=78ea275a59d4e2de09a9cf72652ec64454c6a111d2defa1ae0a44bac8a72e523; observed=4e933d1e2412fb1aad74e60719a6a64dfa34862ff0a6b84e93d78da5ce13dd8b | partial | At the recorded access time, the configured MediaDive edge file existed but its SHA-256 differed from the pinned extraction input. The earlier actual hash receipt is reused; this is not a fresh external-file check or a claim about every storage location. |
| medium-count-owner | src/taxonmech/extract.py; extract_mediadive, lines 388–400; GROWS_IN constant | supports | extract_mediadive selects METPO:2000517 edges with an exact NCBI taxon subject and counts the distinct medium objects; this is the maintained rule needed to reproduce the historical row. |
| qc-setup-receipt | just qc; initial setup attempt, 2026-10-19T07:17:01Z through 2026-10-19T07:17:01Z | context_only | Initial actual invocation from /private/tmp/taxonmech-record-reviews-k0MubV/repo exited 1 because ruff was absent. Locked ruff 0.16.7 was installed only in that isolated environment before the complete retry. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| strict-receipt | just validate-strict data/taxa/archaea/acidianus_sp.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0002/strict-01.tsv; This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0002/repo; started 2026-10-19T07:44:34Z, finished 2026-10-19T07:44:40Z, exit 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times.<br>Validating 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0002/strict-01.tsv |
| history-receipt | just validate-history; All 17 standalone history records; the generated seed event was also inspected in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:01Z, finished 2026-10-19T07:17:03Z, exit 0. All 17 standalone history records; the generated seed event was also inspected in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>history links: 17 record(s), 0 invalid<br>No issues found<br>17 history record(s) valid against src/taxonmech/schema/history.yaml |
| corpus-receipt | just verify-corpus; All 625,960 generated taxon YAMLs, not a focused approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:18:23Z, finished 2026-10-19T07:24:12Z, exit 0. All 625,960 generated taxon YAMLs, not a focused approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>uv run python scripts/verify_corpus.py <br>expected 625960 records, found 625960 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ and curation/seed_scope.tsv |
| products-receipt | just validate-products; Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:01Z, finished 2026-10-19T07:55:11Z, exit 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml<br><br>id↔label correspondence summary:<br><br>✅ All id↔label pairs correspond. |
| qc-receipt | just qc; Repository-wide just qc, including native corpus-wide checks. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:41Z, finished 2026-10-19T08:07:39Z, exit 0. Repository-wide just qc, including native corpus-wide checks. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>1055 passed, 3 skipped, 5 deselected in 1634.00s (0:27:13)<br>Validating 625960 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml<br>  files scanned:      625960<br>expected 625960 records, found 625960 on disk<br>pages/ is current<br>Site publication: 530,864,122 bytes (budget 950,000,000)<br>625960 taxon records<br>  NCBITAXON        625960<br>All TaxonMech quality gates passed.<br>  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890 strains (not genome counts)<br>  Related STRAININFO_DEPOSIT: 107277 strain-record pairs, 106843 identifiers, 53890 strains (not genome counts)<br>  Related NUCLEOTIDE_SEQUENCE: 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)<br>LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809 records mapped, 324404579 genomes summed across record attestations (not deduplicated)<br>Causal graphs: 0 records (0 evidence-backed edges)<br><br>All TaxonMech quality gates passed. |

## Limits And Additional Notes

- The original manifest-pinned MediaDive edge bytes were unavailable in the checked locations. The configured current file exists but has a different SHA-256; its contents cannot independently validate the historical one-medium count. The pinned inventory supports the represented count and medium identifier.
- The review checks source representation and taxonomic identity, not new phylogenetic analysis, assembly sequence equivalence, growth conditions or a medium formulation. No trait or mechanism is inferred from the aggregate attestation.
- Zero imported BacDive strains describes the declared snapshot coverage. The selected GTDB rows demonstrate catalog genomes but do not establish physical deposits or license joins by isolate labels.
- Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.
- The primary GTDB scan covered shards 0017 and 0018 only; all selected rows were inspected and their counts agree with the pinned inventories. Other catalog shards were not scanned, so this is not an independent whole-catalog absence claim.
- No generated record, page or curation history was edited. Any action is proposed follow-up, not completed curation or native scientific-status promotion.
- The initial shared-base just qc attempt failed because ruff was absent. Locked ruff 0.16.7 was installed in that isolated environment before the successful full retry; both actual receipts are retained.
- The original listing found 52 existing actual record targets among 625,960 corpus records. Batch-0001 added ten validated single-target bundles; this batch continues with original unreviewed positions 11–20 after excluding those targets.
- New structured bundles require their own review-validate, review-save and review-check invocations. Reused native baseline receipts do not claim those later bundle checks have already run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T233615Z-acidianus_sp
kind: record
repository: CultureBotAI/TaxonMech
title: 'Record review: Acidianus sp.'
started_at: '2026-10-19T07:41:46Z'
finished_at: '2026-10-19T23:36:15Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: The reviewer did not author or curate the target record. This
    pass inspects existing data and writes only a new review observation in an isolated
    checkout.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: The complete generated record identifies NCBITaxon:1872104 as the NCBI species-rank
  placeholder Acidianus sp. Its rank, parent, carried lineage and genetic code agree
  with the pinned taxonomy and current NCBI response. Both GTDB associations remain
  pooled broadMatch mappings, with source-cluster counts of seven and six; no exact
  GTDB synonym or xref is asserted. Historical verification of the one-medium attestation
  remains unavailable because the original edge snapshot could not be recovered from
  the checked locations. No record-specific curation finding was established.
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
  - path: data/catalog/MANIFEST.json
    sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
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
  - path: data/taxa/archaea/acidianus_sp.yaml
    sha256: 6b18dae81f7ff5a90166696d8c524c8e0e1f8e7b6d8faeda77dba17038421184
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
  description: The entire single resolved generated TaxonRecord and its identity,
    nomenclature, mapping, imported strain, source-count and provenance assertions.
  selection: Path-ordered unreviewed record 11 at unchanged base 9b5a8fff5185b38dc5c77bb35235152c81ea7765;
    batch-0002 record 1. The first batch's ten newly saved targets were excluded using
    validated bundle listings, together with the 52 previously covered actual corpus
    targets. Reviewed means an actual target of a validated bundle listed by scripts/record_review.py
    list; historical TSV inventories do not substitute for bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - NCBITaxon:1872104
targets:
- target_id: NCBITaxon:1872104
  path: data/taxa/archaea/acidianus_sp.yaml
  label: Acidianus sp.
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
  summary: The exact target is NCBITaxon:1872104, distinct from its unclassified Acidianus
    parent 2629519, genus 12914 and named Acidianus species. NCBI assigns SPECIES
    rank even though its scientific label is Acidianus sp. All ten carried ancestors,
    including root and the unclassified parent, and genetic code 11 agree with the
    pinned taxonomy; the current NCBI response confirms the same identity and parent
    chain. No physical strain identity is inferred from species rank.
  target_ids:
  - NCBITaxon:1872104
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
  summary: There is no imported BacDive strain or strain-level genome assertion. Exact
    source inventory/subtree selection was checked; genome catalog entries and isolate
    names do not create physical deposits.
  target_ids:
  - NCBITaxon:1872104
  evidence_ids:
  - record
  - bacdive-inventory
  - culture-inventory
- check_id: gtdb-primary-counts
  name: Bounded GTDB primary-row and cluster-count check
  status: passed
  required: true
  summary: 'GTDB:s__Acidianus_hospitalis: selected rows=7, inventory count=7, exact
    target taxid rows=4; GTDB:s__Acidilobus_sp000495735: selected rows=6, inventory
    count=6, exact target taxid rows=1. Source counts agree within the explicitly
    scanned shards; no whole-catalog absence or sequence-equivalence claim is made.'
  target_ids:
  - NCBITaxon:1872104
  evidence_ids:
  - gtdb-mappings
  - gtdb-species
  - genome-catalog-manifest
  - genome-catalog-1
  - genome-catalog-2
  scope_note: Full explicit reads of gtdb_genomes-0017.jsonl.gz (50,000 rows) and
    0018 (1,341 rows), including ignored files. Other catalog shards were not scanned.
    Exact terminal species tokens selected the rows.
- check_id: historical-source-counts
  name: Original MediaDive medium set
  status: unavailable
  required: true
  summary: The inventory supports one medium, mediadive.medium:88, but the original
    manifest-pinned MediaDive edge bytes were unavailable in the checked locations.
    The differently hashed current file cannot independently reproduce the historical
    taxon-to-medium association.
  target_ids:
  - NCBITaxon:1872104
  evidence_ids:
  - manifest
  - historical-edge-availability
  - mediadive-taxa
  - medium-count-owner
- check_id: qc-setup-attempt
  name: Initial quality-gate setup attempt
  status: failed
  required: false
  summary: 'Actual exit 1: missing ruff; superseded by the separately recorded successful
    full retry.'
  target_ids:
  - NCBITaxon:1872104
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
  - NCBITaxon:1872104
  evidence_ids:
  - strict-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0002/uv-cache
    just validate-strict data/taxa/archaea/acidianus_sp.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0002/strict-01.tsv
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
  - NCBITaxon:1872104
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
  - NCBITaxon:1872104
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
  - NCBITaxon:1872104
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
  - NCBITaxon:1872104
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
  reference: data/taxa/archaea/acidianus_sp.yaml
  accessed_at: '2026-10-19T23:36:15Z'
  support: supports
  summary: Read the entire generated YAML, including identity, lineage, names, mappings,
    source attestations, imported strain count and seed history.
  locator: entire TaxonRecord; identifier=NCBITaxon:1872104
  snapshot_sha256: 6b18dae81f7ff5a90166696d8c524c8e0e1f8e7b6d8faeda77dba17038421184
- evidence_id: taxonomy-inventory
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-19T07:41:48Z'
  support: supports
  summary: Inspected the exact target row and every carried ancestor; compared rank,
    label, parent, genetic code and source name classes with the complete record.
  locator: 'line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""};
    line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"};
    line 1798: {"taxon_id":"NCBITaxon:2281","label":"Sulfolobales","rank":"ORDER","parent_id":"NCBITaxon:183924"};
    line 2648: {"taxon_id":"NCBITaxon:12914","label":"Acidianus","rank":"GENUS","parent_id":"NCBITaxon:118883"};
    line 2980: {"taxon_id":"NCBITaxon:28889","label":"Thermoproteota","rank":"PHYLUM","parent_id":"NCBITaxon:1783275"};
    line 22254: {"taxon_id":"NCBITaxon:118883","label":"Sulfolobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2281"};
    line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"};
    line 36612: {"taxon_id":"NCBITaxon:183924","label":"Thermoprotei","rank":"CLASS","parent_id":"NCBITaxon:28889"};
    line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"};
    line 489187: {"taxon_id":"NCBITaxon:1872104","label":"Acidianus sp.","rank":"SPECIES","parent_id":"NCBITaxon:2629519","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon|gtdb|mediadive","retired_into":"","taxonomy_snapshot":"2026-09-13"};
    line 538477: {"taxon_id":"NCBITaxon:2629519","label":"unclassified Acidianus","rank":"NO_RANK","parent_id":"NCBITaxon:12914"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
- evidence_id: scope-row
  kind: database
  reference: curation/seed_scope.tsv
  accessed_at: '2026-10-19T07:41:48Z'
  support: supports
  summary: The exact target is explicitly included in the seed scope.
  locator: 'line 30915: {"identifier":"NCBITaxon:1872104","added":"2026-09-12","reason":"attested
    rule: Acidianus sp., 3 sources incl. NCBI"}'
  snapshot_sha256: 5fdc0f7111b64e02439d95c6f2b51fcff1d2154c34b2d957422dd9b297e94d4b
- evidence_id: path-row
  kind: database
  reference: data/taxa/PATHS.tsv
  accessed_at: '2026-10-19T07:41:48Z'
  support: supports
  summary: The indexed path resolves to the same NCBI taxon and generated target.
  locator: 'line 296625: {"identifier":"NCBITaxon:1872104","slug":"acidianus_sp"}'
  snapshot_sha256: c950844feb0638ce04f7349784749dd1d728fe70bc80f7e2756d956d4ecea254
- evidence_id: ncbi-live
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1872104
  accessed_at: '2026-10-19T07:39:48Z'
  support: supports
  summary: 'Inspected the official taxonomy response for this exact taxon: scientific
    name, rank, parent, source name classes, lineage identifiers and genetic code.
    The current response is distinguished from the pinned September inventory.'
  locator: TaxaSet/Taxon[TaxId='1872104']; captured with the other nine selected batch-0002
    taxa
  snapshot_sha256: ecc25dfb94e05dc5f6be7f9108242b66996662404d615dab3a4ec4a0fdd4b064
- evidence_id: lpsn-inventory
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-19T07:41:48Z'
  support: supports
  summary: Inspected exact mapped LPSN names and any linked names; a bounded inventory
    miss does not establish worldwide nomenclatural absence.
  locator: complete table; exact target/subtree/source-identifier search had no matching
    row
  snapshot_sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: gtdb-mappings
  kind: database
  reference: data/raw/gtdb_mappings.tsv
  accessed_at: '2026-10-19T07:41:48Z'
  support: supports
  summary: Inspected this taxon's mappings and reverse mappings of the selected clusters;
    retained source predicates and cluster-scoped counts.
  locator: 'line 25048: {"gtdb_id":"GTDB:s__Acidilobus_sp000495735","gtdb_label":"s__Acidilobus_sp000495735","gtdb_parent":"GTDB:g__Acidilobus","ncbitaxon_id":"NCBITaxon:1410573","predicate":"skos:closeMatch","genome_count":"6"};
    line 25050: {"gtdb_id":"GTDB:s__Acidilobus_sp000495735","gtdb_label":"s__Acidilobus_sp000495735","gtdb_parent":"GTDB:g__Acidilobus","ncbitaxon_id":"NCBITaxon:1410575","predicate":"skos:closeMatch","genome_count":"6"};
    line 25051: {"gtdb_id":"GTDB:s__Acidilobus_sp000495735","gtdb_label":"s__Acidilobus_sp000495735","gtdb_parent":"GTDB:g__Acidilobus","ncbitaxon_id":"NCBITaxon:1410576","predicate":"skos:closeMatch","genome_count":"6"};
    line 70969: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","gtdb_label":"s__Acidianus_hospitalis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:1872104","predicate":"skos:broadMatch","genome_count":"7"};
    line 70970: {"gtdb_id":"GTDB:s__Acidilobus_sp000495735","gtdb_label":"s__Acidilobus_sp000495735","gtdb_parent":"GTDB:g__Acidilobus","ncbitaxon_id":"NCBITaxon:1872104","predicate":"skos:broadMatch","genome_count":"6"};
    line 70987: {"gtdb_id":"GTDB:s__Acidilobus_sp000495735","gtdb_label":"s__Acidilobus_sp000495735","gtdb_parent":"GTDB:g__Acidilobus","ncbitaxon_id":"NCBITaxon:1872109","predicate":"skos:broadMatch","genome_count":"6"};
    line 296668: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","gtdb_label":"s__Acidianus_hospitalis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:563177","predicate":"skos:closeMatch","genome_count":"7"};
    line 320834: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","gtdb_label":"s__Acidianus_hospitalis","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:933801","predicate":"skos:closeMatch","genome_count":"7"}'
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
- evidence_id: gtdb-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-19T07:41:48Z'
  support: supports
  summary: Inspected source species identifiers, labels, parent cluster and genome
    counts.
  locator: 'line 3494: {"gtdb_id":"GTDB:s__Acidianus_hospitalis","label":"s__Acidianus_hospitalis","parent":"GTDB:g__Acidianus","genome_count":"7"};
    line 3967: {"gtdb_id":"GTDB:s__Acidilobus_sp000495735","label":"s__Acidilobus_sp000495735","parent":"GTDB:g__Acidilobus","genome_count":"6"}'
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
- evidence_id: bacdive-inventory
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-19T07:41:48Z'
  support: supports
  summary: Full inventory selection used the exact taxon and every descendant from
    the complete NCBI parent graph; no classified BacDive strain was found in this
    bounded subtree.
  locator: complete table; exact target/subtree/source-identifier search had no matching
    row
  snapshot_sha256: 029fd6d1f53ef7f90684130bf0d644ed3edd1d8fbeb065a511ae928f160b1eea
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: culture-inventory
  kind: database
  reference: data/raw/culture_collection_strains.tsv
  accessed_at: '2026-10-19T07:41:48Z'
  support: supports
  summary: Inspected exact culture-inventory associations with the target; a genome
    or isolate name does not supply an inferred physical deposit.
  locator: complete table; exact target/subtree/source-identifier search had no matching
    row
  snapshot_sha256: 810fdcb16abd6330fb15bb03d4c74b18db86be36a7c599df7c6b2498d9735c95
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: gold-organisms
  kind: database
  reference: data/raw/gold_organisms.tsv
  accessed_at: '2026-10-19T07:41:48Z'
  support: supports
  summary: Inspected the exact GOLD organism count row, or its bounded absence, without
    converting counts to phenotypes.
  locator: complete table; exact target/subtree/source-identifier search had no matching
    row
  snapshot_sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: mediadive-taxa
  kind: database
  reference: data/raw/mediadive_taxa.tsv
  accessed_at: '2026-10-19T07:41:48Z'
  support: supports
  summary: Inspected the exact MediaDive medium count row, or its bounded absence,
    without converting counts to phenotypes.
  locator: 'line 5650: {"taxon_id":"NCBITaxon:1872104","medium_count":"1","media_ids":"mediadive.medium:88"}'
  snapshot_sha256: 3f74b78cadfcdb6aeae953e09fdb39e34fd9c5d5ed0be65a04a5d7fb02355905
- evidence_id: madin-taxa
  kind: database
  reference: data/raw/madin_taxa.tsv
  accessed_at: '2026-10-19T07:41:48Z'
  support: supports
  summary: Inspected the exact Madin trait-assertion count row, or its bounded absence,
    without converting counts to phenotypes.
  locator: complete table; exact target/subtree/source-identifier search had no matching
    row
  snapshot_sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: bactotraits-taxa
  kind: database
  reference: data/raw/bactotraits_taxa.tsv
  accessed_at: '2026-10-19T07:41:48Z'
  support: supports
  summary: Inspected the exact BactoTraits trait-assertion count row, or its bounded
    absence, without converting counts to phenotypes.
  locator: complete table; exact target/subtree/source-identifier search had no matching
    row
  snapshot_sha256: 976d109cef832d8bf27cc105f67a42efbe900b6946736298602ef6d11158b197
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: mapping-policy
  kind: record_content
  reference: docs/HARMONIZATION.md
  accessed_at: '2026-10-19T23:36:15Z'
  support: supports
  summary: The local policy permits one-to-one species closeMatch mappings and LPSN-linked
    species to supply xrefs/synonyms, retains pooled broadMatch entries separately
    and carries NCBI lineage unchanged.
  locator: Mapping predicates and Which strains belong to a record sections
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
- evidence_id: equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-19T23:36:15Z'
  support: supports
  summary: TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations
    remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes
    under the source taxon.
  locator: TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
- evidence_id: seed-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-19T23:36:15Z'
  support: supports
  summary: Inspected the maintained mapping ranking, source predicate retention, synonym/xref
    construction and primary-source genome-count selection against this target's represented
    fields.
  locator: GTDB mapping construction, lines 440–472, and source-attestation construction
  snapshot_sha256: 6b5b065f4ae7aea022af736a22c0f63dc58a2425c7ee453259e567ab030f8257
- evidence_id: manifest
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T23:36:15Z'
  support: supports
  summary: The manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd
    and individual upstream input hashes; extraction time is 2026-09-13T17:50:44Z.
  locator: kg_microbe_source, inputs, extracted_at
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
- evidence_id: overlay-manifests
  kind: record_content
  reference: data/atb/MANIFEST.yaml
  accessed_at: '2026-10-19T23:36:15Z'
  support: supports
  summary: Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z,
    matching this record's sole generated seed event. The StrainInfo manifest is independently
    captured in source.inputs.
  locator: extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml
  snapshot_sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
- evidence_id: genome-catalog-manifest
  kind: record_content
  reference: data/catalog/MANIFEST.json
  accessed_at: '2026-10-19T23:36:15Z'
  support: supports
  summary: The native GTDB catalog records the RS232 source snapshot. This review's
    primary-row scan is bounded to shards 0017 and 0018.
  locator: coverage.sources[name=GTDB]
  snapshot_sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
- evidence_id: genome-catalog-1
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0017.jsonl.gz
  accessed_at: '2026-10-19T23:29:40Z'
  support: supports
  summary: Inspected complete selected primary genome rows, separating source genome
    identifiers, taxon assignments and isolate labels. Source cluster membership does
    not establish assembly or deposit equivalence.
  locator: 'line 29105: {"accession":"GB_GCA_032248955.1","gtdb_representative":"f","ncbi_taxid":"1872104","ncbi_species_taxid":"1872104","ncbi_organism_name":"Acidianus
    sp.","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Acidilobus;s__Acidilobus
    sp000495735","ncbi_strain_identifiers":"RBS.bin.4"}; line 31775: {"accession":"GB_GCA_028277005.1","gtdb_representative":"f","ncbi_taxid":"1872109","ncbi_species_taxid":"1872109","ncbi_organism_name":"Acidilobus
    sp.","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Acidilobus;s__Acidilobus
    sp000495735","ncbi_strain_identifiers":"RSEP6"}; line 32156: {"accession":"GB_GCA_032249015.1","gtdb_representative":"f","ncbi_taxid":"1872104","ncbi_species_taxid":"1872104","ncbi_organism_name":"Acidianus
    sp.","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    hospitalis","ncbi_strain_identifiers":"RBS.bin.2"}; line 37598: {"accession":"RS_GCF_046537415.1","gtdb_representative":"f","ncbi_taxid":"1872104","ncbi_species_taxid":"1872104","ncbi_organism_name":"Acidianus
    sp.","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    hospitalis","ncbi_strain_identifiers":"Alice.S.bin.1"}; line 37916: {"accession":"GB_GCA_046533895.1","gtdb_representative":"t","ncbi_taxid":"563177","ncbi_species_taxid":"563177","ncbi_organism_name":"Acidianus
    hospitalis","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    hospitalis","ncbi_strain_identifiers":"RHS.bin.1"}; line 38348: {"accession":"GB_GCA_000495715.1","gtdb_representative":"f","ncbi_taxid":"1410575","ncbi_species_taxid":"1410575","ncbi_organism_name":"uncultured
    Acidilobus sp. OSP8","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Acidilobus;s__Acidilobus
    sp000495735","ncbi_strain_identifiers":"none"}; line 43564: {"accession":"GB_GCA_000495735.1","gtdb_representative":"t","ncbi_taxid":"1410576","ncbi_species_taxid":"1410576","ncbi_organism_name":"uncultured
    Acidilobus sp. JCHS","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Acidilobus;s__Acidilobus
    sp000495735","ncbi_strain_identifiers":"none"}; line 43616: {"accession":"GB_GCA_022759325.1","gtdb_representative":"f","ncbi_taxid":"1872109","ncbi_species_taxid":"1872109","ncbi_organism_name":"Acidilobus
    sp.","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Acidilobus;s__Acidilobus
    sp000495735","ncbi_strain_identifiers":"2016_B01_C_1"}; line 46762: {"accession":"GB_GCA_003086435.1","gtdb_representative":"f","ncbi_taxid":"563177","ncbi_species_taxid":"563177","ncbi_organism_name":"Acidianus
    hospitalis","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    hospitalis","ncbi_strain_identifiers":"SCGC AC-742_N10"}; line 47899: {"accession":"RS_GCF_046534395.1","gtdb_representative":"f","ncbi_taxid":"1872104","ncbi_species_taxid":"1872104","ncbi_organism_name":"Acidianus
    sp.","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    hospitalis","ncbi_strain_identifiers":"Moose.S.bin.11"}; line 49253: {"accession":"RS_GCF_000213215.1","gtdb_representative":"f","ncbi_taxid":"933801","ncbi_species_taxid":"563177","ncbi_organism_name":"Acidianus
    hospitalis W1","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    hospitalis","ncbi_strain_identifiers":"W1"}; line 49816: {"accession":"GB_GCA_000495675.1","gtdb_representative":"f","ncbi_taxid":"1410573","ncbi_species_taxid":"1410573","ncbi_organism_name":"uncultured
    Acidilobus sp. MG","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Acidilobaceae;g__Acidilobus;s__Acidilobus
    sp000495735","ncbi_strain_identifiers":"none"}'
  snapshot_sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
- evidence_id: genome-catalog-2
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0018.jsonl.gz
  accessed_at: '2026-10-19T23:29:40Z'
  support: supports
  summary: Inspected complete selected primary genome rows, separating source genome
    identifiers, taxon assignments and isolate labels. Source cluster membership does
    not establish assembly or deposit equivalence.
  locator: 'line 1150: {"accession":"GB_GCA_046533515.1","gtdb_representative":"f","ncbi_taxid":"1872104","ncbi_species_taxid":"1872104","ncbi_organism_name":"Acidianus
    sp.","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    hospitalis","ncbi_strain_identifiers":"SBS.bin.13"}'
  snapshot_sha256: 8baa314877815777abcdf600079c6ee42f2ea5340398df9f2e18de9c18fd4347
- evidence_id: historical-edge-availability
  kind: search
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T07:30:21Z'
  support: partial
  summary: At the recorded access time, the configured MediaDive edge file existed
    but its SHA-256 differed from the pinned extraction input. The earlier actual
    hash receipt is reused; this is not a fresh external-file check or a claim about
    every storage location.
  locator: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/mediadive/edges.tsv;
    expected=78ea275a59d4e2de09a9cf72652ec64454c6a111d2defa1ae0a44bac8a72e523; observed=4e933d1e2412fb1aad74e60719a6a64dfa34862ff0a6b84e93d78da5ce13dd8b
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
  search_scope: Exact configured data/transformed/mediadive/edges.tsv beneath conf/sources.yaml's
    kg_microbe_root, including ignored files, plus the earlier ignored-inclusive isolated-checkout
    search.
- evidence_id: medium-count-owner
  kind: record_content
  reference: src/taxonmech/extract.py
  accessed_at: '2026-10-19T23:36:15Z'
  support: supports
  summary: extract_mediadive selects METPO:2000517 edges with an exact NCBI taxon
    subject and counts the distinct medium objects; this is the maintained rule needed
    to reproduce the historical row.
  locator: extract_mediadive, lines 388–400; GROWS_IN constant
  snapshot_sha256: 7c5b5bf385e0c060f1cb3dbac304d05ddb941e4c83c900017a04133efd6d1822
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
  reference: just validate-strict data/taxa/archaea/acidianus_sp.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0002/strict-01.tsv
  accessed_at: '2026-10-19T07:44:40Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0002/repo;\
    \ started 2026-10-19T07:44:34Z, finished 2026-10-19T07:44:40Z, exit 0. This exact\
    \ generated YAML only; its captured bytes remain unchanged. Actual earlier per-target\
    \ invocation; the receipt retains its original cwd and times.\nValidating 1 files\
    \ with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0002/strict-01.tsv"
  locator: This exact generated YAML only; its captured bytes remain unchanged. Actual
    earlier per-target invocation; the receipt retains its original cwd and times.
  snapshot_sha256: c3002d66694407a0c0b043e76f0a2b039fb0a9cc8ba78fcfe2a4426c1142f2ca
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
  topic: Resolved biological taxon and carried lineage
  outcome: supported
  summary: The exact target is NCBITaxon:1872104, distinct from its unclassified Acidianus
    parent 2629519, genus 12914 and named Acidianus species. NCBI assigns SPECIES
    rank even though its scientific label is Acidianus sp. All ten carried ancestors,
    including root and the unclassified parent, and genetic code 11 agree with the
    pinned taxonomy; the current NCBI response confirms the same identity and parent
    chain. No physical strain identity is inferred from species rank.
  target_ids:
  - NCBITaxon:1872104
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - scope-row
  - path-row
  dimensions:
  - name: taxon-rank
    value: SPECIES
    definition: NCBI target rank, distinct from physical strain/deposit/genome identity.
    evidence_ids:
    - record
    - taxonomy-inventory
    - ncbi-live
  - name: taxonomy-snapshot
    value: '2026-09-13'
    definition: Pinned NCBI snapshot; current authority is separately identified.
    evidence_ids:
    - taxonomy-inventory
    - manifest
- assessment_id: nomenclature
  area: nomenclature
  topic: Source-scoped names and nomenclatural standing
  outcome: supported
  summary: The literal NCBI scientific name is retained. Neither the pinned NCBI inventory
    nor the current NCBI response supplies an additional name class for this target.
    The inspected LPSN inventory has no exact mapped name. Both GTDB names remain
    source-qualified mappings rather than exact synonyms or equivalent xrefs. The
    record makes no ICNP-validity or type-material claim.
  target_ids:
  - NCBITaxon:1872104
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - lpsn-inventory
  - gtdb-mappings
  - mapping-policy
  - genome-catalog-1
  - genome-catalog-2
- assessment_id: completeness
  area: completeness
  topic: Complete imported subtree and source assertion units
  outcome: supported
  summary: 'Complete pinned inventory and parent-graph selection found no descendant
    taxon, BacDive strain or culture-collection row for this target. Zero imported
    strains is consistent with those inputs despite the independently observed catalog
    genomes; genome entries are not automatically physical strain deposits. The three
    source attestations retain distinct units: one NCBI name, seven genomes in the
    primary pooled GTDB cluster, and one MediaDive medium. The exact MediaDive inventory
    row names medium 88. GOLD, Madin and BactoTraits have no exact target row in their
    inspected complete inventories. This is bounded imported-source coverage, not
    worldwide absence.'
  target_ids:
  - NCBITaxon:1872104
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
  dimensions:
  - name: assertion-units
    value: 'NCBITAXON: 1 NAME; GTDB: 7 GENOME; MEDIADIVE: 1 MEDIUM'
    definition: Native source-specific counts; their units and source taxon boundaries
      are not interchangeable.
    evidence_ids:
    - record
    - gtdb-species
    - gold-organisms
    - mediadive-taxa
    - madin-taxa
    - bactotraits-taxa
- assessment_id: taxonomy-mapping
  area: grounding
  topic: GTDB source mapping scope and cluster counts
  outcome: supported
  summary: The complete selected RS232 catalog rows reproduce the seven-member Acidianus
    hospitalis cluster and six-member Acidilobus sp000495735 cluster. Four hospitalis
    genomes and one Acidilobus genome carry target taxid 1872104; the other members
    carry different NCBI taxa. These are pooled source-cluster counts, not seven and
    six genomes assigned exclusively to this NCBI target. Both broadMatch predicates
    and their explanatory notes preserve that scope. The primary GTDB attestation
    reports seven and points to the additional cluster in taxonomy_mappings; it does
    not claim a combined thirteen-genome total. GB_GCA_032248955.1 (RBS.bin.4) explicitly
    carries NCBI Acidianus sp. while GTDB places it in Acidilobus; the record correctly
    preserves both source classifications without replacing the NCBI lineage.
  target_ids:
  - NCBITaxon:1872104
  evidence_ids:
  - record
  - gtdb-mappings
  - gtdb-species
  - mapping-policy
  - equivalence-contract
  - seed-owner
  - genome-catalog-1
  - genome-catalog-2
  dimensions:
  - name: gtdb-release
    value: RS232
    definition: Pinned GTDB source release; primary-row checks are bounded to shards
      0017 and 0018.
    evidence_ids:
    - genome-catalog-manifest
    - genome-catalog-1
    - genome-catalog-2
- assessment_id: native-status
  area: provenance
  topic: Seed event and scientific-status boundary
  outcome: supported
  summary: EXACT grounding denotes the resolved NCBI identity. SEEDED status and the
    single 2026-09-13T17:54:04Z seed event remain unchanged and agree with the maximum
    source-manifest extraction timestamp. A review does not confer native human-reviewed
    status.
  target_ids:
  - NCBITaxon:1872104
  evidence_ids:
  - record
  - manifest
  - overlay-manifests
findings: []
actions:
- action_id: verify-pinned-mediadive-edges
  description: Recover the upstream MediaDive edge snapshot with the SHA-256 pinned
    in data/raw/MANIFEST.yaml, then use extract_mediadive's exact-target METPO:2000517
    selection to independently verify the distinct medium set for NCBITaxon:1872104.
    This resolves the historical association limitation without editing generated
    records.
  finding_ids: []
  target_ids:
  - NCBITaxon:1872104
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: data/raw/MANIFEST.yaml
    role: Pinned upstream path, revision and exact MediaDive input hash
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: Maintained extract_mediadive distinct-medium counting rule
  acceptance_checks:
  - Recovered data/transformed/mediadive/edges.tsv bytes match the manifest SHA-256
    before use.
  - Select only subject NCBITaxon:1872104 with predicate METPO:2000517; preserve the
    direct-taxon boundary and count distinct medium objects.
  - 'Compare that set with data/raw/mediadive_taxa.tsv line 5650: medium_count 1 and
    media_ids mediadive.medium:88. Retain any discrepancy in a new observation instead
    of editing this immutable review.'
limitations:
- The original manifest-pinned MediaDive edge bytes were unavailable in the checked
  locations. The configured current file exists but has a different SHA-256; its contents
  cannot independently validate the historical one-medium count. The pinned inventory
  supports the represented count and medium identifier.
- The review checks source representation and taxonomic identity, not new phylogenetic
  analysis, assembly sequence equivalence, growth conditions or a medium formulation.
  No trait or mechanism is inferred from the aggregate attestation.
- Zero imported BacDive strains describes the declared snapshot coverage. The selected
  GTDB rows demonstrate catalog genomes but do not establish physical deposits or
  license joins by isolate labels.
- Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765;
  the recorded cwd and timestamps identify the original execution. These native corpus/source
  inputs are unchanged; only new review files differ. This receipt is not a new run
  on the batch branch and does not validate subsequently saved review bundles.
- The primary GTDB scan covered shards 0017 and 0018 only; all selected rows were
  inspected and their counts agree with the pinned inventories. Other catalog shards
  were not scanned, so this is not an independent whole-catalog absence claim.
notes:
- No generated record, page or curation history was edited. Any action is proposed
  follow-up, not completed curation or native scientific-status promotion.
- The initial shared-base just qc attempt failed because ruff was absent. Locked ruff
  0.16.7 was installed in that isolated environment before the successful full retry;
  both actual receipts are retained.
- The original listing found 52 existing actual record targets among 625,960 corpus
  records. Batch-0001 added ten validated single-target bundles; this batch continues
  with original unreviewed positions 11–20 after excluding those targets.
- New structured bundles require their own review-validate, review-save and review-check
  invocations. Reused native baseline receipts do not claim those later bundle checks
  have already run.
tags:
- record-review
- batch-0002
- archaea
- generated
- source-checked
```
