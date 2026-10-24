# Record review: Acidianus sulfidivorans

- Review: 20261020T033115Z-acidianus_sulfidivorans
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-19T23:34:59Z
- Finished UTC: 2026-10-20T03:31:15Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The species Acidianus sulfidivorans has supported NCBI identity, LPSN nomenclature and one BacDive type strain gathered from its JP7 child. Its GTDB species xref is independently supported by the LPSN bridge. No record-specific defect was established; historical GOLD and Madin aggregates remain verified only against their pinned inventories.

## Scope And Provenance

Entire single generated record, including all source assertions and imported strains.

Selection: Original unreviewed path-order position 23; batch-0003 target 3. Excluded 72 actual targets from validated main and local batch-0001/0002 listings; full corpus enumeration includes ignored files.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9b5a8fff5185b38dc5c77bb35235152c81ea7765.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:312539 | data/taxa/archaea/acidianus_sulfidivorans.yaml | generated | Acidianus sulfidivorans |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact NCBI taxon, rank and lineage | passed | True | NCBITaxon:312539 | NCBITaxon:312539 denotes the species Acidianus sulfidivorans below genus 12914, with nine carried ancestors and genetic code 11. Pinned and current NCBI agree on name, rank, parent, lineage and authority synonym. Child 619593 is the JP7 strain; the parent record gathers its BacDive entry with classified_as rather than replacing the species identity. |
| Complete GTDB cluster membership check | passed | True | NCBITaxon:312539 | All 19 captured GTDB RS232 shards were read; the exact Acidianus sulfidivorans cluster contains one genome. Its strain/species taxids remain explicitly distinct. |
| Complete strain, deposit and genome-source assertions | passed | True | NCBITaxon:312539 | BacDive 16644 directly specifies JP7, DSM 18786 and JCM 13667, the narrower NCBI taxon 619593, unversioned GCA_003201765 and BV-BRC 619593.4/619593.7. The BV-BRC primary rows explicitly join DSM:18786 to GCA_003201765.1 and .2 respectively; .4 is Deprecated and .7 Complete in the captured source. The earlier assertion remains source history, without asserting that the two versions are identical. Both rows cite PRJNA463410 and SAMN09071530, also present in the current GenBank .2 row. RefSeq GCF_003201765.2 is explicitly paired as identical to GenBank .2 in the primary metadata, but no assembly equivalence is inferred from shared names or samples. GOLD Go0002318 explicitly identifies DSM 18786 and taxon 619593; Go0608847 explicitly identifies JCM 13667 and taxon 312539 in two distinct assertion fields. Neither organism ID occurs in the full captured GOLD sequencing-project projection, so no project/analysis chain is invented. SI-ID 309414.3 supplies its own available deposits SI-DP 720496 (DSM 18786) and 720497 (JCM 13667); its full record has no sequence assertion to transfer between deposits. CAFI recognizes the full DSM/JCM numeric accessions, while bare JP7 is ineligible as a culture-deposit join. Every one of the 3 assembly, 4 genome-record and 11 related-record assertions matches the raw/StrainInfo multiset, including source fields, versions, deposit IDs and provenance. Multiset checks: genome_assemblies=3; genome_records=4; related_records=11 |
| Original manifest-pinned aggregate edge counts | unavailable | True | NCBITaxon:312539 | Pinned inventories agree with the generated assertions, but original matching edge bytes are unavailable in the checked locations for gold, madin. Current sources cannot reproduce that historical extraction. |
| Initial quality-gate setup attempt | failed | False | NCBITaxon:312539 | Actual exit 1: missing ruff; superseded by the separately recorded successful full retry. |
| Native strict record validation | passed | True | NCBITaxon:312539 | Actual terminal exit code 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. |
| Repository history validation | passed | True | NCBITaxon:312539 | Actual terminal exit code 0. All 17 standalone history records; the generated seed event was also inspected in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| Full-corpus exact reproduction | passed | True | NCBITaxon:312539 | Actual terminal exit code 0. All 625,960 generated taxon YAMLs, not a focused approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| Native product ID/label gate | passed | True | NCBITaxon:312539 | Actual terminal exit code 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| Authoritative complete quality gate | passed | True | NCBITaxon:312539 | Actual terminal exit code 0. Repository-wide just qc, including native corpus-wide checks. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. Pytest reported 1055 passed, 3 skipped and 5 deselected; the native QC recipe completed successfully. |

## Scientific And Domain Assessments

### Exact taxon and source lineage

identity: supported. Targets: NCBITaxon:312539.

NCBITaxon:312539 denotes the species Acidianus sulfidivorans below genus 12914, with nine carried ancestors and genetic code 11. Pinned and current NCBI agree on name, rank, parent, lineage and authority synonym. Child 619593 is the JP7 strain; the parent record gathers its BacDive entry with classified_as rather than replacing the species identity.

### Name classes and nomenclatural scope

nomenclature: supported. Targets: NCBITaxon:312539.

LPSN 785735 is the legitimate, correct, validly published ICNP name Acidianus sulfidivorans Plumb et al. 2007. Its type designations DSM 18786 and JCM 13667 match BacDive deposits. The current LPSN page and original-description PubMed abstract also identify JP7 as this type strain. DOI 10.1099/ijs.0.64846-0 and PMID 17625168 identify the original description; DOI 10.1099/ijs.0.65508-0 identifies the subsequent IJSEM notification list. LPSN AY907891 resolves at NCBI as AY907891.1, a 1473-base JP7 16S rRNA sequence under taxon 619593; the record preserves the source unversioned accession. Both deposits support the parent record's derived is_type_strain flag.

### Imported subtree and source assertion units

completeness: supported. Targets: NCBITaxon:312539.

The complete pinned NCBI subtree has one child taxon and one imported BacDive entry, 16644, with both supplied deposits retained. The BacDive attestation correctly counts 1 STRAIN gathered from 1 descendant. GOLD 7 ORGANISM and Madin 3 TRAIT_ASSERTION are the direct species-level inventory counts; they are not counts of the two displayed deposit-linked GOLD organism objects and do not include the child taxon. The original historical edge multiplicities remain unavailable for independent recount.

### Qualified species mapping and target scope

grounding: supported. Targets: NCBITaxon:312539.

The LPSN 785735 inventory explicitly links the species name to GTDB:s__Acidianus_sulfidivorans, supporting the species xref under the local harmonization policy. The sole direct GTDB mapping row instead targets child NCBITaxon:619593, so absence of a parent taxonomy_mappings entry is expected. The sole GTDB primary genome RS_GCF_003201765.2 has taxon 619593, species_taxid 312539 and strain identifier JP7. Membership supports the one-genome cluster; bare JP7 does not create a GTDB deposit/assembly join. Species-level LPSN equivalence is distinct from the problematic exact species synonym on the child record.

### Strain, deposit and genome-source links

evidence: supported. Targets: NCBITaxon:312539.

BacDive 16644 directly specifies JP7, DSM 18786 and JCM 13667, the narrower NCBI taxon 619593, unversioned GCA_003201765 and BV-BRC 619593.4/619593.7. The BV-BRC primary rows explicitly join DSM:18786 to GCA_003201765.1 and .2 respectively; .4 is Deprecated and .7 Complete in the captured source. The earlier assertion remains source history, without asserting that the two versions are identical. Both rows cite PRJNA463410 and SAMN09071530, also present in the current GenBank .2 row. RefSeq GCF_003201765.2 is explicitly paired as identical to GenBank .2 in the primary metadata, but no assembly equivalence is inferred from shared names or samples. GOLD Go0002318 explicitly identifies DSM 18786 and taxon 619593; Go0608847 explicitly identifies JCM 13667 and taxon 312539 in two distinct assertion fields. Neither organism ID occurs in the full captured GOLD sequencing-project projection, so no project/analysis chain is invented. SI-ID 309414.3 supplies its own available deposits SI-DP 720496 (DSM 18786) and 720497 (JCM 13667); its full record has no sequence assertion to transfer between deposits. CAFI recognizes the full DSM/JCM numeric accessions, while bare JP7 is ineligible as a culture-deposit join. Every one of the 3 assembly, 4 genome-record and 11 related-record assertions matches the raw/StrainInfo multiset, including source fields, versions, deposit IDs and provenance.

### Unchanged native status and history

provenance: supported. Targets: NCBITaxon:312539.

The NCBI identity is grounded EXACT and the record remains SEEDED. Its single seed event is consistent with the latest extraction timestamp across raw, ATB and StrainInfo manifests (2026-09-13T17:54:04Z). This review neither appends history nor promotes native status.

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
| record | data/taxa/archaea/acidianus_sulfidivorans.yaml; entire TaxonRecord; identifier=NCBITaxon:312539 | supports | Read the entire generated YAML, including identity, lineage, names, mappings, source attestations, all imported strains and links, and seed history. |
| taxonomy-inventory | data/raw/ncbitaxon_taxa.tsv; line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""}; line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"}; line 1798: {"taxon_id":"NCBITaxon:2281","label":"Sulfolobales","rank":"ORDER","parent_id":"NCBITaxon:183924"}; line 2648: {"taxon_id":"NCBITaxon:12914","label":"Acidianus","rank":"GENUS","parent_id":"NCBITaxon:118883"}; line 2980: {"taxon_id":"NCBITaxon:28889","label":"Thermoproteota","rank":"PHYLUM","parent_id":"NCBITaxon:1783275"}; line 22254: {"taxon_id":"NCBITaxon:118883","label":"Sulfolobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2281"}; line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"}; line 36612: {"taxon_id":"NCBITaxon:183924","label":"Thermoprotei","rank":"CLASS","parent_id":"NCBITaxon:28889"}; line 63923: {"taxon_id":"NCBITaxon:312539","label":"Acidianus sulfidivorans","rank":"SPECIES","parent_id":"NCBITaxon:12914","genetic_code":"11","exact_synonyms":"","related_synonyms":"Acidianus sulfidivorans Plumb et al. 2007","broad_synonyms":"","attested_by":"ncbitaxon&#124;lpsn&#124;gold&#124;madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"}; line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"} | supports | Inspected the target and each carried ancestor, rank, parent, genetic code and source name classes. |
| scope-row | curation/seed_scope.tsv; line 24103: {"identifier":"NCBITaxon:312539","added":"2026-09-12","reason":"attested rule: Acidianus sulfidivorans, 4 sources incl. NCBI"} | supports | Exact target is included in the declared seed scope. |
| path-row | data/taxa/PATHS.tsv; line 426226: {"identifier":"NCBITaxon:312539","slug":"acidianus_sulfidivorans"} | supports | Indexed path resolves to this exact NCBI taxon. |
| ncbi-live | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1540082,1071530,312539,619593,146920,518068,2933264,1915614,1915615,2268176; TaxaSet/Taxon[TaxId='312539']; ten-target captured response | supports | Inspected the official response for this exact taxon: scientific name, rank, parent, source name classes, lineage and genetic code. Current authority and pinned September inventory remain distinct observations. |
| lpsn-inventory | data/raw/lpsn_names.tsv; line 23508: {"lpsn_id":"lpsn:785735","name":"Acidianus sulfidivorans","rank":"SPECIES","authority":"Plumb et al. 2007","url":"https://lpsn.dsmz.de/species/acidianus-sulfidivorans","deprecated":"0","status":"legitimate=True; validly published under the ICNP; correct name","validly_published":"1","legitimate":"1","is_correct_name":"1","parent_lpsn_id":"lpsn:516964","ncbitaxon_ids":"NCBITaxon:312539","gtdb_ids":"GTDB:s__Acidianus_sulfidivorans","type_strain_ids":"kgmicrobe.strain:DSM-18786&#124;kgmicrobe.strain:JCM-13667","synonym_of":"","synonyms":"","publications":"PMID:17625168&#124;doi:10.1099/ijs.0.64846-0&#124;doi:10.1099/ijs.0.65508-0","sequence_accessions":"INSDC:AY907891"} | supports | Inspected exact mapped and linked LPSN names; bounded inventory absence does not establish worldwide nomenclatural absence. |
| gtdb-mappings | data/raw/gtdb_mappings.tsv; line 299830: {"gtdb_id":"GTDB:s__Acidianus_sulfidivorans","gtdb_label":"s__Acidianus_sulfidivorans","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:619593","predicate":"skos:closeMatch","genome_count":"1"} | supports | Inspected direct mappings and selected clusters' reverse mappings, retaining each source predicate and taxon boundary. |
| gtdb-species | data/raw/gtdb_species.tsv; line 3499: {"gtdb_id":"GTDB:s__Acidianus_sulfidivorans","label":"s__Acidianus_sulfidivorans","parent":"GTDB:g__Acidianus","genome_count":"1"} | supports | Inspected source species identifiers, labels, parent clusters and genome counts. |
| bacdive-inventory | data/raw/bacdive_strains.tsv; line 16463: {"strain_id":"kgmicrobe.strain:bacdive_16644","bacdive_id":"16644","designation":"JP7","taxon_ids":"NCBITaxon:619593","lpsn_ids":"lpsn:785735","culture_collection_ids":"kgmicrobe.strain:DSM-18786&#124;kgmicrobe.strain:JCM-13667","medium_count":"0"} | supports | Complete inventory selection covers the exact target and descendants from the complete NCBI parent graph; its imported strain population was compared with the complete YAML. |
| culture-inventory | data/raw/culture_collection_strains.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected exact culture-inventory associations; an isolate name or genome does not create an inferred deposit. |
| gold-organisms | data/raw/gold_organisms.tsv; line 31532: {"taxon_id":"NCBITaxon:312539","organism_count":"7"} | supports | Inspected the exact GOLD organism count row or bounded absence, without converting counts to phenotypes. |
| mediadive-taxa | data/raw/mediadive_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact MediaDive medium count row or bounded absence, without converting counts to phenotypes. |
| madin-taxa | data/raw/madin_taxa.tsv; line 21330: {"taxon_id":"NCBITaxon:312539","assertion_count":"3"} | supports | Inspected the exact Madin trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| bactotraits-taxa | data/raw/bactotraits_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact BactoTraits trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| mapping-policy | docs/HARMONIZATION.md; Mapping predicates; Which strains belong to a record | supports | Policy permits one-to-one species closeMatch normalization and LPSN-linked species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage unchanged. |
| equivalence-contract | src/taxonmech/schema/taxonmech.yaml; TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439 | supports | TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes under the source taxon. |
| seed-owner | src/taxonmech/seed.py; GTDB mapping construction lines 440–472; LPSN/type-strain and source-attestation construction | supports | Inspected mapping ranking, qualified predicates, fixed broadMatch wording, synonym/xref construction, primary cluster counts and same-taxon type-strain derivation. |
| manifest | data/raw/MANIFEST.yaml; kg_microbe_source, inputs, extracted_at | supports | Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd, upstream input hashes and extraction time 2026-09-13T17:50:44Z. |
| overlay-manifests | data/atb/MANIFEST.yaml; extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml | supports | Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z, matching the sole seed event. StrainInfo manifest is independently captured in source.inputs. |
| strain-table-1 | data/raw/strain_assemblies.tsv; line 82003: {"strain_id":"kgmicrobe.strain:bacdive_16644","assembly_id":"ncbi.assembly:GCA_003201765","source":"BACDIVE","source_id":"bacdive:16644","source_reference_id":"66792","assembly_level":"complete","assembly_name":"ASM320176v2 assembly for Acidianus sulfidivorans JP7","taxon_id":"NCBITaxon:619593","source_field":"Sequence information.Genome sequences.INSDC accession","matched_strain_id":"","source_strain_identifiers":"","source_strain_field":"","source_organism_id":"","source_project_id":""}; line 82004: {"strain_id":"kgmicrobe.strain:bacdive_16644","assembly_id":"ncbi.assembly:GCA_003201765.1","source":"BV_BRC","source_id":"patric:619593.4","source_reference_id":"","assembly_level":"","assembly_name":"Acidianus sulfidivorans JP7","taxon_id":"NCBITaxon:619593","source_field":"assembly_accession","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""}; line 82005: {"strain_id":"kgmicrobe.strain:bacdive_16644","assembly_id":"ncbi.assembly:GCA_003201765.2","source":"BV_BRC","source_id":"patric:619593.7","source_reference_id":"","assembly_level":"","assembly_name":"Acidianus sulfidivorans JP7","taxon_id":"NCBITaxon:619593","source_field":"assembly_accession","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""} | supports | Exact imported strain/deposit assertions, source fields, identifiers and versions were compared with the complete record; no cross-source Cartesian product was inferred. |
| strain-table-2 | data/raw/strain_genome_records.tsv; line 64245: {"strain_id":"kgmicrobe.strain:bacdive_16644","genome_id":"patric:619593.4","source_database":"patric","source":"BACDIVE","source_id":"bacdive:16644","source_reference_id":"66792","assembly_level":"complete","genome_name":"Acidianus sulfidivorans JP7","taxon_id":"NCBITaxon:619593","source_field":"Sequence information.Genome sequences.BV-BRC accession","matched_strain_id":"","source_strain_identifiers":"","source_strain_field":"","source_organism_id":"","source_project_id":""}; line 64246: {"strain_id":"kgmicrobe.strain:bacdive_16644","genome_id":"patric:619593.4","source_database":"patric","source":"BV_BRC","source_id":"patric:619593.4","source_reference_id":"","assembly_level":"","genome_name":"Acidianus sulfidivorans JP7","taxon_id":"NCBITaxon:619593","source_field":"genome_id","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""}; line 64247: {"strain_id":"kgmicrobe.strain:bacdive_16644","genome_id":"patric:619593.7","source_database":"patric","source":"BACDIVE","source_id":"bacdive:16644","source_reference_id":"66792","assembly_level":"complete","genome_name":"ASM320176v2 assembly for Acidianus sulfidivorans JP7","taxon_id":"NCBITaxon:619593","source_field":"Sequence information.Genome sequences.BV-BRC accession","matched_strain_id":"","source_strain_identifiers":"","source_strain_field":"","source_organism_id":"","source_project_id":""}; line 64248: {"strain_id":"kgmicrobe.strain:bacdive_16644","genome_id":"patric:619593.7","source_database":"patric","source":"BV_BRC","source_id":"patric:619593.7","source_reference_id":"","assembly_level":"","genome_name":"Acidianus sulfidivorans JP7","taxon_id":"NCBITaxon:619593","source_field":"genome_id","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""} | supports | Exact imported strain/deposit assertions, source fields, identifiers and versions were compared with the complete record; no cross-source Cartesian product was inferred. |
| strain-table-3 | data/raw/strain_related_records.tsv; line 249229: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"bioproject:PRJNA463410","record_type":"BIOPROJECT","source":"BV_BRC","source_id":"patric:619593.4","source_reference_id":"","taxon_id":"NCBITaxon:619593","record_name":"","source_field":"bioproject_accession","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""}; line 249230: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"bioproject:PRJNA463410","record_type":"BIOPROJECT","source":"BV_BRC","source_id":"patric:619593.7","source_reference_id":"","taxon_id":"NCBITaxon:619593","record_name":"","source_field":"bioproject_accession","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""}; line 249231: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"biosample:SAMN09071530","record_type":"BIOSAMPLE","source":"BV_BRC","source_id":"patric:619593.4","source_reference_id":"","taxon_id":"NCBITaxon:619593","record_name":"","source_field":"biosample_accession","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""}; line 249232: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"biosample:SAMN09071530","record_type":"BIOSAMPLE","source":"BV_BRC","source_id":"patric:619593.7","source_reference_id":"","taxon_id":"NCBITaxon:619593","record_name":"","source_field":"biosample_accession","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""}; line 249233: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"gold:Go0002318","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0002318","source_reference_id":"","taxon_id":"NCBITaxon:619593","record_name":"Acidianus sulfidivorans JP7","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM 18786","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0002318","source_project_id":""}; line 249234: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"gold:Go0608847","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0608847","source_reference_id":"","taxon_id":"NCBITaxon:312539","record_name":"Acidianus sulfidivorans JCM 13667","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:JCM-13667","source_strain_identifiers":"JCM 13667","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0608847","source_project_id":""}; line 249235: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"gold:Go0608847","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0608847","source_reference_id":"","taxon_id":"NCBITaxon:312539","record_name":"Acidianus sulfidivorans JCM 13667","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:JCM-13667","source_strain_identifiers":"JCM 13667","source_strain_field":"ORGANISM STRAIN","source_organism_id":"gold:Go0608847","source_project_id":""} | supports | Exact imported strain/deposit assertions, source fields, identifiers and versions were compared with the complete record; no cross-source Cartesian product was inferred. |
| strain-table-4 | data/straininfo/strain_links.tsv; line 68797: {"strain_id":"kgmicrobe.strain:bacdive_16644","straininfo_strain_id":"straininfo.strain:309414","straininfo_deposit_id":"straininfo.deposit:720496","matched_strain_id":"kgmicrobe.strain:DSM-18786","deposit_designation":"DSM 18786","strain_doi":"DOI:10.60712/SI-ID309414.3","strain_status":"published online","deposit_status":"available","source_bacdive_id":"bacdive:16644","taxon_id":"NCBITaxon:312539"}; line 68798: {"strain_id":"kgmicrobe.strain:bacdive_16644","straininfo_strain_id":"straininfo.strain:309414","straininfo_deposit_id":"straininfo.deposit:720497","matched_strain_id":"kgmicrobe.strain:JCM-13667","deposit_designation":"JCM 13667","strain_doi":"DOI:10.60712/SI-ID309414.3","strain_status":"published online","deposit_status":"available","source_bacdive_id":"bacdive:16644","taxon_id":"NCBITaxon:312539"} | supports | Exact imported strain/deposit assertions, source fields, identifiers and versions were compared with the complete record; no cross-source Cartesian product was inferred. |
| strain-table-5 | data/straininfo/assemblies.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Exact imported strain/deposit assertions, source fields, identifiers and versions were compared with the complete record; no cross-source Cartesian product was inferred. |
| strain-table-6 | data/straininfo/related_records.tsv.gz; line 162561: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"straininfo.deposit:720496","record_type":"STRAININFO_DEPOSIT","source":"STRAININFO","source_id":"straininfo.strain:309414","source_reference_id":"","taxon_id":"NCBITaxon:312539","record_name":"DSM 18786","source_field":"deposits.siDP","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM 18786","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"DSM 18786\",\"deposit_id\":\"straininfo.deposit:720496\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:16644\",\"strain_doi\":\"DOI:10.60712/SI-ID309414.3\",\"strain_id\":\"straininfo.strain:309414\",\"strain_status\":\"published online\"}"}; line 162562: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"straininfo.deposit:720497","record_type":"STRAININFO_DEPOSIT","source":"STRAININFO","source_id":"straininfo.strain:309414","source_reference_id":"","taxon_id":"NCBITaxon:312539","record_name":"JCM 13667","source_field":"deposits.siDP","matched_strain_id":"kgmicrobe.strain:JCM-13667","source_strain_identifiers":"JCM 13667","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"JCM 13667\",\"deposit_id\":\"straininfo.deposit:720497\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:16644\",\"strain_doi\":\"DOI:10.60712/SI-ID309414.3\",\"strain_id\":\"straininfo.strain:309414\",\"strain_status\":\"published online\"}"}; line 162563: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"straininfo.strain:309414","record_type":"STRAININFO_STRAIN","source":"STRAININFO","source_id":"straininfo.strain:309414","source_reference_id":"","taxon_id":"NCBITaxon:312539","record_name":"DSM 18786","source_field":"strain.siID","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM 18786","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"DSM 18786\",\"deposit_id\":\"straininfo.deposit:720496\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:16644\",\"strain_doi\":\"DOI:10.60712/SI-ID309414.3\",\"strain_id\":\"straininfo.strain:309414\",\"strain_status\":\"published online\"}"}; line 162564: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"straininfo.strain:309414","record_type":"STRAININFO_STRAIN","source":"STRAININFO","source_id":"straininfo.strain:309414","source_reference_id":"","taxon_id":"NCBITaxon:312539","record_name":"JCM 13667","source_field":"strain.siID","matched_strain_id":"kgmicrobe.strain:JCM-13667","source_strain_identifiers":"JCM 13667","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"JCM 13667\",\"deposit_id\":\"straininfo.deposit:720497\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:16644\",\"strain_doi\":\"DOI:10.60712/SI-ID309414.3\",\"strain_id\":\"straininfo.strain:309414\",\"strain_status\":\"published online\"}"} | supports | Exact imported strain/deposit assertions, source fields, identifiers and versions were compared with the complete record; no cross-source Cartesian product was inferred. |
| strain-table-7 | data/atb/strain_links.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Exact imported strain/deposit assertions, source fields, identifiers and versions were compared with the complete record; no cross-source Cartesian product was inferred. |
| strain-primary-1 | data/bacdive/records.jsonl.gz; line 16462: {"General":{"@ref":7697,"BacDive-ID":16644,"NCBI tax id":[{"Matching level":"strain","NCBI tax id":619593},{"Matching level":"species","NCBI tax id":312539}],"doi":"10.13145/bacdive16644.20260601.11"},"Literature":{"@ref":7697,"culture collection no.":"DSM 18786, JCM 13667","straininfo link":{"@ref":126262,"straininfo":309414}},"Name and taxonomic classification":{"@ref":7697,"LPSN":{"@ref":20215,"class":"Thermoprotei","description":"domain/archaea","domain":"Archaea","family":"Sulfolobaceae","full scientific name":"&lt;I&gt;Acidianus&lt;/I&gt; &lt;I&gt;sulfidivorans&lt;/I&gt; Plumb et al. 2007","genus":"Acidianus","keyword":"phylum/thermoproteota","order":"Sulfolobales","phylum":"Thermoproteota","species":"Acidianus sulfidivorans"},"class":"Thermoprotei","domain":"Archaea","family":"Sulfolobaceae","full scientific name":"Acidianus sulfidivorans Plumb et al. 2007","genus":"Acidianus","order":"Sulfolobales","phylum":"Crenarchaeota","species":"Acidianus sulfidivorans","strain designation":"JP7","type strain":"yes"},"Sequence information":{"16S sequences":{"@ref":7697,"NCBI tax ID":619593,"accession":"AY907891","database":"nuccore","description":"Acidianus sulfidivorans JP7 16S ribosomal RNA gene, partial sequence","length":1473},"Genome sequences":[{"@ref":66792,"BV-BRC accession":"619593.7","INSDC accession":"GCA_003201765","NCBI tax ID":619593,"assembly level":"complete","description":"ASM320176v2 assembly for Acidianus sulfidivorans JP7","score":94.06},{"@ref":66792,"BV-BRC accession":"619593.4","NCBI tax ID":619593,"assembly level":"complete","description":"Acidianus sulfidivorans JP7","score":97.9}]}} | supports | Read complete selected primary source objects for BacDive 16644, StrainInfo 309414.3 and the two distinct deposit-linked GOLD organisms; source IDs, deposits, source fields and taxon assignments remain distinct. |
| strain-primary-2 | data/straininfo/records.jsonl.gz; line 237891: {"deposits":[{"cultureCollection":{"ccID":1,"code":"DSMZ","deprecated":false,"name":"DSMZ-German Collection of Microorganisms and Cell Cultures"},"designation":"DSM 18786","lastUpdate":"2024-12-03","siDP":720496,"status":"available","taxon":{"lpsn":785735,"name":"Acidianus sulfidivorans","ncbi":312539},"typeStrain":true},{"cultureCollection":{"ccID":14,"code":"JCM","deprecated":false,"name":"Japan Collection of Microorganisms"},"designation":"JCM 13667","lastUpdate":"2007-09-10","siDP":720497,"status":"available","taxon":{"lpsn":785735,"name":"Acidianus sulfidivorans","ncbi":312539},"typeStrain":true}],"strain":{"archive":[{"date":"2024-05-31","doi":"10.60712/SI-ID309414.1","title":"StrainInfo SI-ID 309414.1"},{"date":"2024-06-05","doi":"10.60712/SI-ID309414.2","title":"StrainInfo SI-ID 309414.2"},{"date":"2025-02-25","doi":"10.60712/SI-ID309414.3","title":"StrainInfo SI-ID 309414.3"}],"bdID":16644,"doi":"10.60712/SI-ID309414.3","relation":{"deposit":[{"ccID":1,"designation":"DSM 18786","erroneous":false,"siDP":720496},{"ccID":14,"designation":"JCM 13667","erroneous":false,"siDP":720497}],"designation":["JP7"]},"siID":309414,"status":"published online","taxon":{"lpsn":785735,"name":"Acidianus sulfidivorans","ncbi":312539}}} | supports | Read complete selected primary source objects for BacDive 16644, StrainInfo 309414.3 and the two distinct deposit-linked GOLD organisms; source IDs, deposits, source fields and taxon assignments remain distinct. |
| strain-primary-3 | data/gold/organisms.jsonl.gz; line 2081: {"ORGANISM CULTURE COLLECTION ID":"DSM 18786","ORGANISM GOLD ID":"Go0002318","ORGANISM NAME":"Acidianus sulfidivorans JP7","ORGANISM NCBI TAX ID":"619593","ORGANISM STRAIN":"JP7"}; line 439814: {"ORGANISM CULTURE COLLECTION ID":"JCM 13667","ORGANISM GOLD ID":"Go0608847","ORGANISM NAME":"Acidianus sulfidivorans JCM 13667","ORGANISM NCBI TAX ID":"312539","ORGANISM STRAIN":"JCM 13667"} | supports | Read complete selected primary source objects for BacDive 16644, StrainInfo 309414.3 and the two distinct deposit-linked GOLD organisms; source IDs, deposits, source fields and taxon assignments remain distinct. |
| strain-primary-4 | data/gold/projects.jsonl.gz; complete projection; Full captured GOLD project projection, including ignored files, exact organism fields for Go0002318 and Go0608847; neither organism occurs, so no project/analysis chain is inferred. | supports | Read complete selected primary source objects for BacDive 16644, StrainInfo 309414.3 and the two distinct deposit-linked GOLD organisms; source IDs, deposits, source fields and taxon assignments remain distinct. |
| genome-catalog-1 | data/catalog/gtdb_genomes-0017.jsonl.gz; line 34258: {"accession":"RS_GCF_003201765.2","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus sulfidivorans","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Complete Genome","ncbi_assembly_name":"ASM320176v2","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN09071530","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"Papua New Guinea: Lihr Island","ncbi_date":"2020-03-10","ncbi_genbank_assembly_accession":"GCA_003201765.2","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"Edge of acidic hot spring","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Acidianus sulfidivorans JP7","ncbi_protein_count":"2312","ncbi_refseq_category":"reference genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"2265309","ncbi_scaffold_n75":"2265309","ncbi_scaffold_n90":"2265309","ncbi_seq_rel_date":"2020-03-10","ncbi_spanned_gaps":"0","ncbi_species_taxid":"312539","ncbi_ssu_count":"1","ncbi_strain_identifiers":"JP7","ncbi_submitter":"North Carolina State University","ncbi_taxid":"619593","ncbi_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus sulfidivorans","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Thermoproteota;c__Thermoprotei;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus sulfidivorans;x__Acidianus sulfidivorans JP7","ncbi_total_gap_length":"0","ncbi_total_length":"2265309","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"assembly from type material","ncbi_ungapped_length":"2265309","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"} | supports | Read complete selected GTDB, GenBank, RefSeq and BV-BRC primary objects; retained source accession versions, explicit deposit/sample/project chains, BV-BRC statuses and the explicit paired-assembly relationship. |
| genome-catalog-2 | data/catalog/ncbi_genbank-0002.jsonl.gz; line 26071: {"annotation_date":"2019-10-23","annotation_name":"NCBI Prokaryotic Genome Annotation Pipeline (PGAP)","annotation_provider":"NCBI","asm_name":"ASM320176v2","asm_not_live_date":"na","asm_submitter":"North Carolina State University","assembly_accession":"GCA_003201765.2","assembly_level":"Complete Genome","assembly_type":"haploid","bioproject":"PRJNA463410","biosample":"SAMN09071530","contig_count":"1","excluded_from_refseq":"na","ftp_path":"https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/003/201/765/GCA_003201765.2_ASM320176v2/","gbrs_paired_asm":"GCF_003201765.2","gc_percent":"31.000000","genome_rep":"Full","genome_size":"2265309","genome_size_ungapped":"2265309","group":"archaea","infraspecific_name":"strain=JP7","isolate":"na","non_coding_gene_count":"51","organism_name":"Acidianus sulfidivorans JP7","paired_asm_comp":"identical","protein_coding_gene_count":"2259","pubmed_id":"na","refseq_category":"reference genome","relation_to_type_material":"assembly from type material","release_type":"Major","replicon_count":"1","scaffold_count":"1","seq_rel_date":"2020-03-10","species_taxid":"312539","taxid":"619593","total_gene_count":"2339","version_status":"latest","wgs_master":"na"} | supports | Read complete selected GTDB, GenBank, RefSeq and BV-BRC primary objects; retained source accession versions, explicit deposit/sample/project chains, BV-BRC statuses and the explicit paired-assembly relationship. |
| genome-catalog-3 | data/catalog/ncbi_refseq-0001.jsonl.gz; line 44166: {"annotation_date":"2026-03-30","annotation_name":"GCF_003201765.2-RS_2026_03_30","annotation_provider":"NCBI RefSeq","asm_name":"ASM320176v2","asm_not_live_date":"na","asm_submitter":"North Carolina State University","assembly_accession":"GCF_003201765.2","assembly_level":"Complete Genome","assembly_type":"haploid","bioproject":"PRJNA224116","biosample":"SAMN09071530","contig_count":"1","excluded_from_refseq":"na","ftp_path":"https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/003/201/765/GCF_003201765.2_ASM320176v2/","gbrs_paired_asm":"GCA_003201765.2","gc_percent":"31.000000","genome_rep":"Full","genome_size":"2265309","genome_size_ungapped":"2265309","group":"archaea","infraspecific_name":"strain=JP7","isolate":"na","non_coding_gene_count":"51","organism_name":"Acidianus sulfidivorans JP7","paired_asm_comp":"identical","protein_coding_gene_count":"2290","pubmed_id":"na","refseq_category":"reference genome","relation_to_type_material":"assembly from type material","release_type":"Major","replicon_count":"1","scaffold_count":"1","seq_rel_date":"2020-03-10","species_taxid":"312539","taxid":"619593","total_gene_count":"2356","version_status":"latest","wgs_master":"na"} | supports | Read complete selected GTDB, GenBank, RefSeq and BV-BRC primary objects; retained source accession versions, explicit deposit/sample/project chains, BV-BRC statuses and the explicit paired-assembly relationship. |
| genome-catalog-4 | data/bvbrc/bvbrc-0025.jsonl.gz; line 39144: {"assembly_accession":"GCA_003201765.1","bioproject_accession":"PRJNA463410","biosample_accession":"SAMN09071530","culture_collection":"DSM:18786","date_modified":"2018-07-15T23:29:48.127Z","genbank_accessions":"CP029288","genome_id":"619593.4","genome_name":"Acidianus sulfidivorans JP7","genome_status":"Deprecated","public":true,"strain":"JP7","superkingdom":"Archaea","taxon_id":619593,"taxon_lineage_ids":["131567","2157","1783275","28889","183924","2281","118883","12914","312539","619593"],"taxon_lineage_names":["cellular organisms","Archaea","Thermoproteati","Thermoproteota","Thermoprotei","Sulfolobales","Sulfolobaceae","Acidianus","Acidianus sulfidivorans","Acidianus sulfidivorans JP7"]}; line 39145: {"assembly_accession":"GCA_003201765.2","bioproject_accession":"PRJNA463410","biosample_accession":"SAMN09071530","culture_collection":"DSM:18786","date_modified":"2022-11-30T21:06:24.497Z","genbank_accessions":"CP029288","genome_id":"619593.7","genome_name":"Acidianus sulfidivorans JP7","genome_status":"Complete","public":true,"reference_genome":"Representative","strain":"JP7","superkingdom":"Archaea","taxon_id":619593,"taxon_lineage_ids":["131567","2157","1783275","28889","183924","2281","118883","12914","312539","619593"],"taxon_lineage_names":["cellular organisms","Archaea","Thermoproteati","Thermoproteota","Thermoprotei","Sulfolobales","Sulfolobaceae","Acidianus","Acidianus sulfidivorans","Acidianus sulfidivorans JP7"]} | supports | Read complete selected GTDB, GenBank, RefSeq and BV-BRC primary objects; retained source accession versions, explicit deposit/sample/project chains, BV-BRC statuses and the explicit paired-assembly relationship. |
| genome-catalog-manifest | data/catalog/MANIFEST.json; coverage.sources[name=GTDB] | supports | GTDB RS232 provenance; this JP7 source review independently scanned all 19 captured GTDB primary shards. |
| gtdb-full-count | data/catalog/MANIFEST.json; {"paths":["data/catalog/gtdb_genomes-0000.jsonl.gz","data/catalog/gtdb_genomes-0001.jsonl.gz","data/catalog/gtdb_genomes-0002.jsonl.gz","data/catalog/gtdb_genomes-0003.jsonl.gz","data/catalog/gtdb_genomes-0004.jsonl.gz","data/catalog/gtdb_genomes-0005.jsonl.gz","data/catalog/gtdb_genomes-0006.jsonl.gz","data/catalog/gtdb_genomes-0007.jsonl.gz","data/catalog/gtdb_genomes-0008.jsonl.gz","data/catalog/gtdb_genomes-0009.jsonl.gz","data/catalog/gtdb_genomes-0010.jsonl.gz","data/catalog/gtdb_genomes-0011.jsonl.gz","data/catalog/gtdb_genomes-0012.jsonl.gz","data/catalog/gtdb_genomes-0013.jsonl.gz","data/catalog/gtdb_genomes-0014.jsonl.gz","data/catalog/gtdb_genomes-0015.jsonl.gz","data/catalog/gtdb_genomes-0016.jsonl.gz","data/catalog/gtdb_genomes-0017.jsonl.gz","data/catalog/gtdb_genomes-0018.jsonl.gz"],"count":1,"member":"data/catalog/gtdb_genomes-0017.jsonl.gz:34258"} | supports | Exact species-cluster selection found one genome, RS_GCF_003201765.2, at shard 0017 line 34258; ncbi_taxid 619593 differs from species_taxid 312539. |
| cafi-registry | src/taxonmech/data/cafi_acronyms.json; {"accessed_at":"2026-10-19T23:38:53.156143+00:00","registry_rows":{"1":{"acr":"DSM","acr_synonym":["DSMZ"],"active":true,"catalogue":["https://www.dsmz.de/collection/catalogue/details/culture/{acr}-{id}"],"code":"DSMZ","country":"DE","gbif":"883f3d24-35e9-462d-b7a3-13c2b9b7260e","homepage":"https://www.dsmz.de/","name":"DSMZ-German Collection of Microorganisms and Cell Cultures","regex_ccno":"^DSM\\s*\\d+$","regex_id":{"full":"^\\d+$"},"ror":"02tyer376"},"14":{"acr":"JCM","active":true,"catalogue":["https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?{acr}={id}"],"code":"JCM","country":"JP","gbif":"fce1f744-ca76-46bb-9428-d92cfebe39d4","homepage":"https://jcm.brc.riken.jp/en/","name":"Japan Collection of Microorganisms","regex_ccno":"^JCM\\s*\\d+$","regex_id":{"full":"^\\d+$"},"ror":"00s05em53"}},"normalization":{"DSM 18786":"DSM-18786","DSM:18786":"DSM-18786","JCM 13667":"JCM-13667","JP7":""}} | supports | Pinned registry entries 1 (DSM) and 14 (JCM) require the full numeric accession. DSM 18786/DSM:18786 and JCM 13667 normalize as eligible; bare JP7 is rejected. |
| source-metadata-16 | data/bacdive/SOURCE.json; source snapshot metadata | supports | Source capture/projection provenance was inspected separately from the historical kg-microbe aggregate input. |
| source-metadata-17 | data/bvbrc/SOURCE.json; source snapshot metadata | supports | Source capture/projection provenance was inspected separately from the historical kg-microbe aggregate input. |
| source-metadata-18 | data/gold/SOURCE.json; source snapshot metadata | supports | Source capture/projection provenance was inspected separately from the historical kg-microbe aggregate input. |
| source-metadata-19 | data/catalog/PRIMARY.json; source snapshot metadata | supports | Source capture/projection provenance was inspected separately from the historical kg-microbe aggregate input. |
| lpsn-live | https://lpsn.dsmz.de/species/acidianus-sulfidivorans; Name, status, type strain, publications and sequence accession AY907891 | supports | Current LPSN 785735 identifies the legitimate, correct, validly published species and JP7 = DSM 18786 = JCM 13667 type material. |
| doi-original | https://api.crossref.org/works/10.1099%2Fijs.0.64846-0; message DOI, title, author and publication fields | supports | Crossref identifies DOI 10.1099/ijs.0.64846-0 as the original species description; publication metadata is distinct from full-text reassessment. |
| doi-notification | https://api.crossref.org/works/10.1099%2Fijs.0.65508-0; message DOI, title and publication fields | supports | Crossref identifies DOI 10.1099/ijs.0.65508-0 as the subsequent IJSEM notification list. |
| pubmed-original | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=17625168&amp;retmode=xml; PubmedArticle/MedlineCitation/Article and Abstract | supports | Inspected PMID 17625168 metadata and abstract, including the JP7 type-strain designation and species description; no experimental mechanism is inferred. |
| nucleotide-authority | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&amp;id=AY907891&amp;retmode=json; nuccore result accessionversion, title, slen and taxid | supports | NCBI resolves source accession AY907891 to AY907891.1, the 1,473-base JP7 16S rRNA sequence under taxon 619593. This is accession identity, not a genome or expression-module claim. |
| historical-edge-1 | data/raw/MANIFEST.yaml; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/gold/edges.tsv; expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12; observed=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d | partial | Configured historical input exists with a different hash. This reuses the earlier actual receipt and does not claim a fresh or worldwide search. |
| historical-edge-2 | data/raw/MANIFEST.yaml; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv; expected=3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f; observed=c19bfc848e1b410548614c54a2b99e2c58452d58aeb61f972c99fcb3039a1d24 | partial | Configured historical input exists with a different hash. This reuses the earlier actual receipt and does not claim a fresh or worldwide search. |
| qc-setup-receipt | just qc; initial setup attempt, 2026-10-19T07:17:01Z through 2026-10-19T07:17:01Z | context_only | Initial actual invocation from /private/tmp/taxonmech-record-reviews-k0MubV/repo exited 1 because ruff was absent. Locked ruff 0.16.7 was installed only in that isolated environment before the complete retry. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. |
| strict-receipt | just validate-strict data/taxa/archaea/acidianus_sulfidivorans.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/strict-03.tsv; This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/repo; started 2026-10-19T23:35:07Z, finished 2026-10-19T23:35:09Z, exit 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times.<br>Validating 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/strict-03.tsv |
| history-receipt | just validate-history; All 17 standalone history records; the generated seed event was also inspected in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:01Z, finished 2026-10-19T07:17:03Z, exit 0. All 17 standalone history records; the generated seed event was also inspected in this target. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>history links: 17 record(s), 0 invalid<br>No issues found<br>17 history record(s) valid against src/taxonmech/schema/history.yaml |
| corpus-receipt | just verify-corpus; All 625,960 generated taxon YAMLs, not a focused approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:18:23Z, finished 2026-10-19T07:24:12Z, exit 0. All 625,960 generated taxon YAMLs, not a focused approximation. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>uv run python scripts/verify_corpus.py <br>expected 625960 records, found 625960 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ and curation/seed_scope.tsv |
| products-receipt | just validate-products; Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:01Z, finished 2026-10-19T07:55:11Z, exit 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml<br><br>id↔label correspondence summary:<br><br>✅ All id↔label pairs correspond. |
| qc-receipt | just qc; Repository-wide just qc, including native corpus-wide checks. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:41Z, finished 2026-10-19T08:07:39Z, exit 0. Repository-wide just qc, including native corpus-wide checks. Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.<br>1055 passed, 3 skipped, 5 deselected in 1634.00s (0:27:13)<br>Validating 625960 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml<br>  files scanned:      625960<br>expected 625960 records, found 625960 on disk<br>pages/ is current<br>Site publication: 530,864,122 bytes (budget 950,000,000)<br>625960 taxon records<br>  NCBITAXON        625960<br>All TaxonMech quality gates passed.<br>  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890 strains (not genome counts)<br>  Related STRAININFO_DEPOSIT: 107277 strain-record pairs, 106843 identifiers, 53890 strains (not genome counts)<br>  Related NUCLEOTIDE_SEQUENCE: 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)<br>LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809 records mapped, 324404579 genomes summed across record attestations (not deduplicated)<br>Causal graphs: 0 records (0 evidence-backed edges)<br><br>All TaxonMech quality gates passed. |

## Limits And Additional Notes

- The review covers each complete generated target and the explicitly inspected source evidence. It does not independently re-estimate phylogenetic species boundaries or infer experimental mechanisms from database annotations.
- The NCBI snapshot is dated 2026-09-13. Current NCBI, LPSN, publication and nucleotide checks are kept distinct from source snapshot assertions; imported strain counts are not worldwide strain censuses.
- Publication identifiers, DOI metadata and the PubMed abstract were checked; the full original article and notification-list text were not reassessed. AY907891 resolves to the JP7 16S sequence, not a genome assembly. No expression-module or physiological inference is needed to establish this accession identity.
- Historical GOLD and Madin counts match the committed species-level inventories. Parent-session checks found that configured local historical edge files differ from the original hashes in data/raw/MANIFEST.yaml; those files cannot independently reproduce the pinned counts. Required historical aggregate verification remains unavailable.
- Reused actual native validation on the unchanged shared base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; the recorded cwd and timestamps identify the original execution. These native corpus/source inputs are unchanged; only new review files differ. This receipt is not a new run on the batch branch and does not validate subsequently saved review bundles.
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base canonical recapture preserved all previously reviewed input hashes; original captures and actual transition receipts remain retained.
- Every new bundle still requires its own validate/save/check recipe; baseline native receipts do not claim these later steps have run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T033115Z-acidianus_sulfidivorans
kind: record
repository: CultureBotAI/TaxonMech
title: 'Record review: Acidianus sulfidivorans'
started_at: '2026-10-19T23:34:59Z'
finished_at: '2026-10-20T03:31:15Z'
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
summary: The species Acidianus sulfidivorans has supported NCBI identity, LPSN nomenclature
  and one BacDive type strain gathered from its JP7 child. Its GTDB species xref is
  independently supported by the LPSN bridge. No record-specific defect was established;
  historical GOLD and Madin aggregates remain verified only against their pinned inventories.
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
  - path: data/bvbrc/bvbrc-0025.jsonl.gz
    sha256: 6d40fd7201112c415d5a8112b19b4ce388a4e44ea98fd879e4814897959befaf
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
  - path: data/catalog/ncbi_genbank-0002.jsonl.gz
    sha256: 5931b3c1684ae211b5a726b0ac459abe095cb6d27a4eb8f6f54cc34aca211f75
    role: context
  - path: data/catalog/ncbi_refseq-0001.jsonl.gz
    sha256: 06282ae41e57cf37ac73b236eab58ecaa081a04bf54d834b1fb61ac065ad56dc
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
  - path: data/taxa/archaea/acidianus_sulfidivorans.yaml
    sha256: 7de0a8ca04edffd076dc3a5cebe0d0f6bfa3e47877fc8a147eb3897cd55bff1d
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
  selection: Original unreviewed path-order position 23; batch-0003 target 3. Excluded
    72 actual targets from validated main and local batch-0001/0002 listings; full
    corpus enumeration includes ignored files.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - NCBITaxon:312539
targets:
- target_id: NCBITaxon:312539
  path: data/taxa/archaea/acidianus_sulfidivorans.yaml
  label: Acidianus sulfidivorans
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
  summary: NCBITaxon:312539 denotes the species Acidianus sulfidivorans below genus
    12914, with nine carried ancestors and genetic code 11. Pinned and current NCBI
    agree on name, rank, parent, lineage and authority synonym. Child 619593 is the
    JP7 strain; the parent record gathers its BacDive entry with classified_as rather
    than replacing the species identity.
  target_ids:
  - NCBITaxon:312539
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - scope-row
  - path-row
- check_id: gtdb-primary-counts
  name: Complete GTDB cluster membership check
  status: passed
  required: true
  summary: All 19 captured GTDB RS232 shards were read; the exact Acidianus sulfidivorans
    cluster contains one genome. Its strain/species taxids remain explicitly distinct.
  target_ids:
  - NCBITaxon:312539
  evidence_ids:
  - gtdb-full-count
  - gtdb-species
  - gtdb-mappings
  - genome-catalog-manifest
  - genome-catalog-1
  - genome-catalog-2
  - genome-catalog-3
  - genome-catalog-4
  scope_note: Full reads of all 19 captured GTDB RS232 primary JSONL shards, including
    ignored files, exact terminal species-taxon equality.
- check_id: strain-genome-evidence
  name: Complete strain, deposit and genome-source assertions
  status: passed
  required: true
  summary: 'BacDive 16644 directly specifies JP7, DSM 18786 and JCM 13667, the narrower
    NCBI taxon 619593, unversioned GCA_003201765 and BV-BRC 619593.4/619593.7. The
    BV-BRC primary rows explicitly join DSM:18786 to GCA_003201765.1 and .2 respectively;
    .4 is Deprecated and .7 Complete in the captured source. The earlier assertion
    remains source history, without asserting that the two versions are identical.
    Both rows cite PRJNA463410 and SAMN09071530, also present in the current GenBank
    .2 row. RefSeq GCF_003201765.2 is explicitly paired as identical to GenBank .2
    in the primary metadata, but no assembly equivalence is inferred from shared names
    or samples. GOLD Go0002318 explicitly identifies DSM 18786 and taxon 619593; Go0608847
    explicitly identifies JCM 13667 and taxon 312539 in two distinct assertion fields.
    Neither organism ID occurs in the full captured GOLD sequencing-project projection,
    so no project/analysis chain is invented. SI-ID 309414.3 supplies its own available
    deposits SI-DP 720496 (DSM 18786) and 720497 (JCM 13667); its full record has
    no sequence assertion to transfer between deposits. CAFI recognizes the full DSM/JCM
    numeric accessions, while bare JP7 is ineligible as a culture-deposit join. Every
    one of the 3 assembly, 4 genome-record and 11 related-record assertions matches
    the raw/StrainInfo multiset, including source fields, versions, deposit IDs and
    provenance. Multiset checks: genome_assemblies=3; genome_records=4; related_records=11'
  target_ids:
  - NCBITaxon:312539
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
  - genome-catalog-1
  - genome-catalog-2
  - genome-catalog-3
  - genome-catalog-4
  - cafi-registry
  - source-metadata-16
  - source-metadata-17
  - source-metadata-18
  - source-metadata-19
  - lpsn-live
  - pubmed-original
  - nucleotide-authority
  scope_note: Every imported strain link was compared by full assertion multiset,
    including provenance/source fields; complete selected primary records were inspected.
- check_id: historical-source-counts
  name: Original manifest-pinned aggregate edge counts
  status: unavailable
  required: true
  summary: Pinned inventories agree with the generated assertions, but original matching
    edge bytes are unavailable in the checked locations for gold, madin. Current sources
    cannot reproduce that historical extraction.
  target_ids:
  - NCBITaxon:312539
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
  - NCBITaxon:312539
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
  - NCBITaxon:312539
  evidence_ids:
  - strict-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/uv-cache
    just validate-strict data/taxa/archaea/acidianus_sulfidivorans.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/strict-03.tsv
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
  - NCBITaxon:312539
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
  - NCBITaxon:312539
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
  - NCBITaxon:312539
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
  - NCBITaxon:312539
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
  reference: data/taxa/archaea/acidianus_sulfidivorans.yaml
  accessed_at: '2026-10-20T03:31:15Z'
  support: supports
  summary: Read the entire generated YAML, including identity, lineage, names, mappings,
    source attestations, all imported strains and links, and seed history.
  locator: entire TaxonRecord; identifier=NCBITaxon:312539
  snapshot_sha256: 7de0a8ca04edffd076dc3a5cebe0d0f6bfa3e47877fc8a147eb3897cd55bff1d
- evidence_id: taxonomy-inventory
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-19T23:35:01Z'
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
    line 63923: {"taxon_id":"NCBITaxon:312539","label":"Acidianus sulfidivorans","rank":"SPECIES","parent_id":"NCBITaxon:12914","genetic_code":"11","exact_synonyms":"","related_synonyms":"Acidianus
    sulfidivorans Plumb et al. 2007","broad_synonyms":"","attested_by":"ncbitaxon|lpsn|gold|madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"};
    line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
- evidence_id: scope-row
  kind: database
  reference: curation/seed_scope.tsv
  accessed_at: '2026-10-19T23:35:01Z'
  support: supports
  summary: Exact target is included in the declared seed scope.
  locator: 'line 24103: {"identifier":"NCBITaxon:312539","added":"2026-09-12","reason":"attested
    rule: Acidianus sulfidivorans, 4 sources incl. NCBI"}'
  snapshot_sha256: 5fdc0f7111b64e02439d95c6f2b51fcff1d2154c34b2d957422dd9b297e94d4b
- evidence_id: path-row
  kind: database
  reference: data/taxa/PATHS.tsv
  accessed_at: '2026-10-19T23:35:01Z'
  support: supports
  summary: Indexed path resolves to this exact NCBI taxon.
  locator: 'line 426226: {"identifier":"NCBITaxon:312539","slug":"acidianus_sulfidivorans"}'
  snapshot_sha256: c950844feb0638ce04f7349784749dd1d728fe70bc80f7e2756d956d4ecea254
- evidence_id: ncbi-live
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1540082,1071530,312539,619593,146920,518068,2933264,1915614,1915615,2268176
  accessed_at: '2026-10-19T23:34:56Z'
  support: supports
  summary: 'Inspected the official response for this exact taxon: scientific name,
    rank, parent, source name classes, lineage and genetic code. Current authority
    and pinned September inventory remain distinct observations.'
  locator: TaxaSet/Taxon[TaxId='312539']; ten-target captured response
  snapshot_sha256: 99397970b64f5c68856c849b0cf98a385c6a79d2af56761ed2043bd65693d471
- evidence_id: lpsn-inventory
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-19T23:35:01Z'
  support: supports
  summary: Inspected exact mapped and linked LPSN names; bounded inventory absence
    does not establish worldwide nomenclatural absence.
  locator: 'line 23508: {"lpsn_id":"lpsn:785735","name":"Acidianus sulfidivorans","rank":"SPECIES","authority":"Plumb
    et al. 2007","url":"https://lpsn.dsmz.de/species/acidianus-sulfidivorans","deprecated":"0","status":"legitimate=True;
    validly published under the ICNP; correct name","validly_published":"1","legitimate":"1","is_correct_name":"1","parent_lpsn_id":"lpsn:516964","ncbitaxon_ids":"NCBITaxon:312539","gtdb_ids":"GTDB:s__Acidianus_sulfidivorans","type_strain_ids":"kgmicrobe.strain:DSM-18786|kgmicrobe.strain:JCM-13667","synonym_of":"","synonyms":"","publications":"PMID:17625168|doi:10.1099/ijs.0.64846-0|doi:10.1099/ijs.0.65508-0","sequence_accessions":"INSDC:AY907891"}'
  snapshot_sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
- evidence_id: gtdb-mappings
  kind: database
  reference: data/raw/gtdb_mappings.tsv
  accessed_at: '2026-10-19T23:35:01Z'
  support: supports
  summary: Inspected direct mappings and selected clusters' reverse mappings, retaining
    each source predicate and taxon boundary.
  locator: 'line 299830: {"gtdb_id":"GTDB:s__Acidianus_sulfidivorans","gtdb_label":"s__Acidianus_sulfidivorans","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:619593","predicate":"skos:closeMatch","genome_count":"1"}'
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
- evidence_id: gtdb-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-19T23:35:01Z'
  support: supports
  summary: Inspected source species identifiers, labels, parent clusters and genome
    counts.
  locator: 'line 3499: {"gtdb_id":"GTDB:s__Acidianus_sulfidivorans","label":"s__Acidianus_sulfidivorans","parent":"GTDB:g__Acidianus","genome_count":"1"}'
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
- evidence_id: bacdive-inventory
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-19T23:35:01Z'
  support: supports
  summary: Complete inventory selection covers the exact target and descendants from
    the complete NCBI parent graph; its imported strain population was compared with
    the complete YAML.
  locator: 'line 16463: {"strain_id":"kgmicrobe.strain:bacdive_16644","bacdive_id":"16644","designation":"JP7","taxon_ids":"NCBITaxon:619593","lpsn_ids":"lpsn:785735","culture_collection_ids":"kgmicrobe.strain:DSM-18786|kgmicrobe.strain:JCM-13667","medium_count":"0"}'
  snapshot_sha256: 029fd6d1f53ef7f90684130bf0d644ed3edd1d8fbeb065a511ae928f160b1eea
- evidence_id: culture-inventory
  kind: database
  reference: data/raw/culture_collection_strains.tsv
  accessed_at: '2026-10-19T23:35:01Z'
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
  accessed_at: '2026-10-19T23:35:01Z'
  support: supports
  summary: Inspected the exact GOLD organism count row or bounded absence, without
    converting counts to phenotypes.
  locator: 'line 31532: {"taxon_id":"NCBITaxon:312539","organism_count":"7"}'
  snapshot_sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
- evidence_id: mediadive-taxa
  kind: database
  reference: data/raw/mediadive_taxa.tsv
  accessed_at: '2026-10-19T23:35:01Z'
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
  accessed_at: '2026-10-19T23:35:01Z'
  support: supports
  summary: Inspected the exact Madin trait-assertion count row or bounded absence,
    without converting counts to phenotypes.
  locator: 'line 21330: {"taxon_id":"NCBITaxon:312539","assertion_count":"3"}'
  snapshot_sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
- evidence_id: bactotraits-taxa
  kind: database
  reference: data/raw/bactotraits_taxa.tsv
  accessed_at: '2026-10-19T23:35:01Z'
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
  accessed_at: '2026-10-20T03:31:15Z'
  support: supports
  summary: Policy permits one-to-one species closeMatch normalization and LPSN-linked
    species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage
    unchanged.
  locator: Mapping predicates; Which strains belong to a record
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
- evidence_id: equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-20T03:31:15Z'
  support: supports
  summary: TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations
    remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes
    under the source taxon.
  locator: TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
- evidence_id: seed-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-20T03:31:15Z'
  support: supports
  summary: Inspected mapping ranking, qualified predicates, fixed broadMatch wording,
    synonym/xref construction, primary cluster counts and same-taxon type-strain derivation.
  locator: GTDB mapping construction lines 440–472; LPSN/type-strain and source-attestation
    construction
  snapshot_sha256: 6b5b065f4ae7aea022af736a22c0f63dc58a2425c7ee453259e567ab030f8257
- evidence_id: manifest
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-20T03:31:15Z'
  support: supports
  summary: Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd,
    upstream input hashes and extraction time 2026-09-13T17:50:44Z.
  locator: kg_microbe_source, inputs, extracted_at
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
- evidence_id: overlay-manifests
  kind: record_content
  reference: data/atb/MANIFEST.yaml
  accessed_at: '2026-10-20T03:31:15Z'
  support: supports
  summary: Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z,
    matching the sole seed event. StrainInfo manifest is independently captured in
    source.inputs.
  locator: extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml
  snapshot_sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
- evidence_id: strain-table-1
  kind: database
  reference: data/raw/strain_assemblies.tsv
  accessed_at: '2026-10-19T23:35:01Z'
  support: supports
  summary: Exact imported strain/deposit assertions, source fields, identifiers and
    versions were compared with the complete record; no cross-source Cartesian product
    was inferred.
  locator: 'line 82003: {"strain_id":"kgmicrobe.strain:bacdive_16644","assembly_id":"ncbi.assembly:GCA_003201765","source":"BACDIVE","source_id":"bacdive:16644","source_reference_id":"66792","assembly_level":"complete","assembly_name":"ASM320176v2
    assembly for Acidianus sulfidivorans JP7","taxon_id":"NCBITaxon:619593","source_field":"Sequence
    information.Genome sequences.INSDC accession","matched_strain_id":"","source_strain_identifiers":"","source_strain_field":"","source_organism_id":"","source_project_id":""};
    line 82004: {"strain_id":"kgmicrobe.strain:bacdive_16644","assembly_id":"ncbi.assembly:GCA_003201765.1","source":"BV_BRC","source_id":"patric:619593.4","source_reference_id":"","assembly_level":"","assembly_name":"Acidianus
    sulfidivorans JP7","taxon_id":"NCBITaxon:619593","source_field":"assembly_accession","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""};
    line 82005: {"strain_id":"kgmicrobe.strain:bacdive_16644","assembly_id":"ncbi.assembly:GCA_003201765.2","source":"BV_BRC","source_id":"patric:619593.7","source_reference_id":"","assembly_level":"","assembly_name":"Acidianus
    sulfidivorans JP7","taxon_id":"NCBITaxon:619593","source_field":"assembly_accession","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""}'
  snapshot_sha256: 71344b934db3081bfcac9562a0bd1fd8fddcfdabb8af60e208ca09035e818315
- evidence_id: strain-table-2
  kind: database
  reference: data/raw/strain_genome_records.tsv
  accessed_at: '2026-10-19T23:35:01Z'
  support: supports
  summary: Exact imported strain/deposit assertions, source fields, identifiers and
    versions were compared with the complete record; no cross-source Cartesian product
    was inferred.
  locator: 'line 64245: {"strain_id":"kgmicrobe.strain:bacdive_16644","genome_id":"patric:619593.4","source_database":"patric","source":"BACDIVE","source_id":"bacdive:16644","source_reference_id":"66792","assembly_level":"complete","genome_name":"Acidianus
    sulfidivorans JP7","taxon_id":"NCBITaxon:619593","source_field":"Sequence information.Genome
    sequences.BV-BRC accession","matched_strain_id":"","source_strain_identifiers":"","source_strain_field":"","source_organism_id":"","source_project_id":""};
    line 64246: {"strain_id":"kgmicrobe.strain:bacdive_16644","genome_id":"patric:619593.4","source_database":"patric","source":"BV_BRC","source_id":"patric:619593.4","source_reference_id":"","assembly_level":"","genome_name":"Acidianus
    sulfidivorans JP7","taxon_id":"NCBITaxon:619593","source_field":"genome_id","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""};
    line 64247: {"strain_id":"kgmicrobe.strain:bacdive_16644","genome_id":"patric:619593.7","source_database":"patric","source":"BACDIVE","source_id":"bacdive:16644","source_reference_id":"66792","assembly_level":"complete","genome_name":"ASM320176v2
    assembly for Acidianus sulfidivorans JP7","taxon_id":"NCBITaxon:619593","source_field":"Sequence
    information.Genome sequences.BV-BRC accession","matched_strain_id":"","source_strain_identifiers":"","source_strain_field":"","source_organism_id":"","source_project_id":""};
    line 64248: {"strain_id":"kgmicrobe.strain:bacdive_16644","genome_id":"patric:619593.7","source_database":"patric","source":"BV_BRC","source_id":"patric:619593.7","source_reference_id":"","assembly_level":"","genome_name":"Acidianus
    sulfidivorans JP7","taxon_id":"NCBITaxon:619593","source_field":"genome_id","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""}'
  snapshot_sha256: 47ed80be55660aad4bd82d37d889ea60f8686cec1aeeccf72e5af22bf43728ab
- evidence_id: strain-table-3
  kind: database
  reference: data/raw/strain_related_records.tsv
  accessed_at: '2026-10-19T23:35:01Z'
  support: supports
  summary: Exact imported strain/deposit assertions, source fields, identifiers and
    versions were compared with the complete record; no cross-source Cartesian product
    was inferred.
  locator: 'line 249229: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"bioproject:PRJNA463410","record_type":"BIOPROJECT","source":"BV_BRC","source_id":"patric:619593.4","source_reference_id":"","taxon_id":"NCBITaxon:619593","record_name":"","source_field":"bioproject_accession","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""};
    line 249230: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"bioproject:PRJNA463410","record_type":"BIOPROJECT","source":"BV_BRC","source_id":"patric:619593.7","source_reference_id":"","taxon_id":"NCBITaxon:619593","record_name":"","source_field":"bioproject_accession","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""};
    line 249231: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"biosample:SAMN09071530","record_type":"BIOSAMPLE","source":"BV_BRC","source_id":"patric:619593.4","source_reference_id":"","taxon_id":"NCBITaxon:619593","record_name":"","source_field":"biosample_accession","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""};
    line 249232: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"biosample:SAMN09071530","record_type":"BIOSAMPLE","source":"BV_BRC","source_id":"patric:619593.7","source_reference_id":"","taxon_id":"NCBITaxon:619593","record_name":"","source_field":"biosample_accession","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM:18786","source_strain_field":"culture_collection","source_organism_id":"","source_project_id":""};
    line 249233: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"gold:Go0002318","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0002318","source_reference_id":"","taxon_id":"NCBITaxon:619593","record_name":"Acidianus
    sulfidivorans JP7","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM
    18786","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0002318","source_project_id":""};
    line 249234: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"gold:Go0608847","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0608847","source_reference_id":"","taxon_id":"NCBITaxon:312539","record_name":"Acidianus
    sulfidivorans JCM 13667","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:JCM-13667","source_strain_identifiers":"JCM
    13667","source_strain_field":"ORGANISM CULTURE COLLECTION ID","source_organism_id":"gold:Go0608847","source_project_id":""};
    line 249235: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"gold:Go0608847","record_type":"GOLD_ORGANISM","source":"GOLD","source_id":"gold:Go0608847","source_reference_id":"","taxon_id":"NCBITaxon:312539","record_name":"Acidianus
    sulfidivorans JCM 13667","source_field":"ORGANISM GOLD ID","matched_strain_id":"kgmicrobe.strain:JCM-13667","source_strain_identifiers":"JCM
    13667","source_strain_field":"ORGANISM STRAIN","source_organism_id":"gold:Go0608847","source_project_id":""}'
  snapshot_sha256: c33a9bf4c6b94dc6971f1c0d46565092c37ba7c2d462a6bc9c20ccbf58fb9c56
- evidence_id: strain-table-4
  kind: database
  reference: data/straininfo/strain_links.tsv
  accessed_at: '2026-10-19T23:35:01Z'
  support: supports
  summary: Exact imported strain/deposit assertions, source fields, identifiers and
    versions were compared with the complete record; no cross-source Cartesian product
    was inferred.
  locator: 'line 68797: {"strain_id":"kgmicrobe.strain:bacdive_16644","straininfo_strain_id":"straininfo.strain:309414","straininfo_deposit_id":"straininfo.deposit:720496","matched_strain_id":"kgmicrobe.strain:DSM-18786","deposit_designation":"DSM
    18786","strain_doi":"DOI:10.60712/SI-ID309414.3","strain_status":"published online","deposit_status":"available","source_bacdive_id":"bacdive:16644","taxon_id":"NCBITaxon:312539"};
    line 68798: {"strain_id":"kgmicrobe.strain:bacdive_16644","straininfo_strain_id":"straininfo.strain:309414","straininfo_deposit_id":"straininfo.deposit:720497","matched_strain_id":"kgmicrobe.strain:JCM-13667","deposit_designation":"JCM
    13667","strain_doi":"DOI:10.60712/SI-ID309414.3","strain_status":"published online","deposit_status":"available","source_bacdive_id":"bacdive:16644","taxon_id":"NCBITaxon:312539"}'
  snapshot_sha256: 615ac119e61df3a9d296ab16674bca6de3fdbf6478ca21a61312014f0ebbae8f
- evidence_id: strain-table-5
  kind: database
  reference: data/straininfo/assemblies.tsv
  accessed_at: '2026-10-19T23:35:01Z'
  support: supports
  summary: Exact imported strain/deposit assertions, source fields, identifiers and
    versions were compared with the complete record; no cross-source Cartesian product
    was inferred.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: d55ba39ab7cb81076a8edb61226de2bdf0aea699a7fb003cdf3ffb3ddc2f3f52
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: strain-table-6
  kind: database
  reference: data/straininfo/related_records.tsv.gz
  accessed_at: '2026-10-19T23:35:01Z'
  support: supports
  summary: Exact imported strain/deposit assertions, source fields, identifiers and
    versions were compared with the complete record; no cross-source Cartesian product
    was inferred.
  locator: 'line 162561: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"straininfo.deposit:720496","record_type":"STRAININFO_DEPOSIT","source":"STRAININFO","source_id":"straininfo.strain:309414","source_reference_id":"","taxon_id":"NCBITaxon:312539","record_name":"DSM
    18786","source_field":"deposits.siDP","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM
    18786","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"DSM
    18786\",\"deposit_id\":\"straininfo.deposit:720496\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:16644\",\"strain_doi\":\"DOI:10.60712/SI-ID309414.3\",\"strain_id\":\"straininfo.strain:309414\",\"strain_status\":\"published
    online\"}"}; line 162562: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"straininfo.deposit:720497","record_type":"STRAININFO_DEPOSIT","source":"STRAININFO","source_id":"straininfo.strain:309414","source_reference_id":"","taxon_id":"NCBITaxon:312539","record_name":"JCM
    13667","source_field":"deposits.siDP","matched_strain_id":"kgmicrobe.strain:JCM-13667","source_strain_identifiers":"JCM
    13667","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"JCM
    13667\",\"deposit_id\":\"straininfo.deposit:720497\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:16644\",\"strain_doi\":\"DOI:10.60712/SI-ID309414.3\",\"strain_id\":\"straininfo.strain:309414\",\"strain_status\":\"published
    online\"}"}; line 162563: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"straininfo.strain:309414","record_type":"STRAININFO_STRAIN","source":"STRAININFO","source_id":"straininfo.strain:309414","source_reference_id":"","taxon_id":"NCBITaxon:312539","record_name":"DSM
    18786","source_field":"strain.siID","matched_strain_id":"kgmicrobe.strain:DSM-18786","source_strain_identifiers":"DSM
    18786","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"DSM
    18786\",\"deposit_id\":\"straininfo.deposit:720496\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:16644\",\"strain_doi\":\"DOI:10.60712/SI-ID309414.3\",\"strain_id\":\"straininfo.strain:309414\",\"strain_status\":\"published
    online\"}"}; line 162564: {"strain_id":"kgmicrobe.strain:bacdive_16644","record_id":"straininfo.strain:309414","record_type":"STRAININFO_STRAIN","source":"STRAININFO","source_id":"straininfo.strain:309414","source_reference_id":"","taxon_id":"NCBITaxon:312539","record_name":"JCM
    13667","source_field":"strain.siID","matched_strain_id":"kgmicrobe.strain:JCM-13667","source_strain_identifiers":"JCM
    13667","source_strain_field":"deposits.designation","source_organism_id":"","source_project_id":"","straininfo_evidence_json":"{\"deposit_designation\":\"JCM
    13667\",\"deposit_id\":\"straininfo.deposit:720497\",\"deposit_status\":\"available\",\"match_method\":\"culture_identifier\",\"source_bacdive_id\":\"bacdive:16644\",\"strain_doi\":\"DOI:10.60712/SI-ID309414.3\",\"strain_id\":\"straininfo.strain:309414\",\"strain_status\":\"published
    online\"}"}'
  snapshot_sha256: c7a262df4f970b2b11a2cf7a0a05c631ff84938e6a19cdb1d98680bb4fb35108
- evidence_id: strain-table-7
  kind: database
  reference: data/atb/strain_links.tsv
  accessed_at: '2026-10-19T23:35:01Z'
  support: supports
  summary: Exact imported strain/deposit assertions, source fields, identifiers and
    versions were compared with the complete record; no cross-source Cartesian product
    was inferred.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 50683192c8015badf14a8a2aab73929a21b830117449ce329d1216a698abf1c0
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: strain-primary-1
  kind: primary_source
  reference: data/bacdive/records.jsonl.gz
  accessed_at: '2026-10-19T23:40:24Z'
  support: supports
  summary: Read complete selected primary source objects for BacDive 16644, StrainInfo
    309414.3 and the two distinct deposit-linked GOLD organisms; source IDs, deposits,
    source fields and taxon assignments remain distinct.
  locator: 'line 16462: {"General":{"@ref":7697,"BacDive-ID":16644,"NCBI tax id":[{"Matching
    level":"strain","NCBI tax id":619593},{"Matching level":"species","NCBI tax id":312539}],"doi":"10.13145/bacdive16644.20260601.11"},"Literature":{"@ref":7697,"culture
    collection no.":"DSM 18786, JCM 13667","straininfo link":{"@ref":126262,"straininfo":309414}},"Name
    and taxonomic classification":{"@ref":7697,"LPSN":{"@ref":20215,"class":"Thermoprotei","description":"domain/archaea","domain":"Archaea","family":"Sulfolobaceae","full
    scientific name":"<I>Acidianus</I> <I>sulfidivorans</I> Plumb et al. 2007","genus":"Acidianus","keyword":"phylum/thermoproteota","order":"Sulfolobales","phylum":"Thermoproteota","species":"Acidianus
    sulfidivorans"},"class":"Thermoprotei","domain":"Archaea","family":"Sulfolobaceae","full
    scientific name":"Acidianus sulfidivorans Plumb et al. 2007","genus":"Acidianus","order":"Sulfolobales","phylum":"Crenarchaeota","species":"Acidianus
    sulfidivorans","strain designation":"JP7","type strain":"yes"},"Sequence information":{"16S
    sequences":{"@ref":7697,"NCBI tax ID":619593,"accession":"AY907891","database":"nuccore","description":"Acidianus
    sulfidivorans JP7 16S ribosomal RNA gene, partial sequence","length":1473},"Genome
    sequences":[{"@ref":66792,"BV-BRC accession":"619593.7","INSDC accession":"GCA_003201765","NCBI
    tax ID":619593,"assembly level":"complete","description":"ASM320176v2 assembly
    for Acidianus sulfidivorans JP7","score":94.06},{"@ref":66792,"BV-BRC accession":"619593.4","NCBI
    tax ID":619593,"assembly level":"complete","description":"Acidianus sulfidivorans
    JP7","score":97.9}]}}'
  snapshot_sha256: b27d0f50f06aa33615e7cc2aae4acb7c2767df930c85292e76fbb462ac136080
- evidence_id: strain-primary-2
  kind: primary_source
  reference: data/straininfo/records.jsonl.gz
  accessed_at: '2026-10-19T23:40:24Z'
  support: supports
  summary: Read complete selected primary source objects for BacDive 16644, StrainInfo
    309414.3 and the two distinct deposit-linked GOLD organisms; source IDs, deposits,
    source fields and taxon assignments remain distinct.
  locator: 'line 237891: {"deposits":[{"cultureCollection":{"ccID":1,"code":"DSMZ","deprecated":false,"name":"DSMZ-German
    Collection of Microorganisms and Cell Cultures"},"designation":"DSM 18786","lastUpdate":"2024-12-03","siDP":720496,"status":"available","taxon":{"lpsn":785735,"name":"Acidianus
    sulfidivorans","ncbi":312539},"typeStrain":true},{"cultureCollection":{"ccID":14,"code":"JCM","deprecated":false,"name":"Japan
    Collection of Microorganisms"},"designation":"JCM 13667","lastUpdate":"2007-09-10","siDP":720497,"status":"available","taxon":{"lpsn":785735,"name":"Acidianus
    sulfidivorans","ncbi":312539},"typeStrain":true}],"strain":{"archive":[{"date":"2024-05-31","doi":"10.60712/SI-ID309414.1","title":"StrainInfo
    SI-ID 309414.1"},{"date":"2024-06-05","doi":"10.60712/SI-ID309414.2","title":"StrainInfo
    SI-ID 309414.2"},{"date":"2025-02-25","doi":"10.60712/SI-ID309414.3","title":"StrainInfo
    SI-ID 309414.3"}],"bdID":16644,"doi":"10.60712/SI-ID309414.3","relation":{"deposit":[{"ccID":1,"designation":"DSM
    18786","erroneous":false,"siDP":720496},{"ccID":14,"designation":"JCM 13667","erroneous":false,"siDP":720497}],"designation":["JP7"]},"siID":309414,"status":"published
    online","taxon":{"lpsn":785735,"name":"Acidianus sulfidivorans","ncbi":312539}}}'
  snapshot_sha256: 8f8e6093f0617317e0488463e52de153f566effa7a5d43b44d17dabab9692819
- evidence_id: strain-primary-3
  kind: primary_source
  reference: data/gold/organisms.jsonl.gz
  accessed_at: '2026-10-19T23:40:24Z'
  support: supports
  summary: Read complete selected primary source objects for BacDive 16644, StrainInfo
    309414.3 and the two distinct deposit-linked GOLD organisms; source IDs, deposits,
    source fields and taxon assignments remain distinct.
  locator: 'line 2081: {"ORGANISM CULTURE COLLECTION ID":"DSM 18786","ORGANISM GOLD
    ID":"Go0002318","ORGANISM NAME":"Acidianus sulfidivorans JP7","ORGANISM NCBI TAX
    ID":"619593","ORGANISM STRAIN":"JP7"}; line 439814: {"ORGANISM CULTURE COLLECTION
    ID":"JCM 13667","ORGANISM GOLD ID":"Go0608847","ORGANISM NAME":"Acidianus sulfidivorans
    JCM 13667","ORGANISM NCBI TAX ID":"312539","ORGANISM STRAIN":"JCM 13667"}'
  snapshot_sha256: 8c1a055214cb240c58fadda0815efbefcb60848245e8a7474e6b1b41d123235c
- evidence_id: strain-primary-4
  kind: primary_source
  reference: data/gold/projects.jsonl.gz
  accessed_at: '2026-10-19T23:40:24Z'
  support: supports
  summary: Read complete selected primary source objects for BacDive 16644, StrainInfo
    309414.3 and the two distinct deposit-linked GOLD organisms; source IDs, deposits,
    source fields and taxon assignments remain distinct.
  locator: complete projection; Full captured GOLD project projection, including ignored
    files, exact organism fields for Go0002318 and Go0608847; neither organism occurs,
    so no project/analysis chain is inferred.
  snapshot_sha256: 0d852fe0144afd778609fef82b266fd1507a4c0be949efd2f53c7c34526b6c95
  search_scope: Full captured GOLD project projection, including ignored files, exact
    organism fields for Go0002318 and Go0608847; neither organism occurs, so no project/analysis
    chain is inferred.
- evidence_id: genome-catalog-1
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0017.jsonl.gz
  accessed_at: '2026-10-19T23:40:24Z'
  support: supports
  summary: Read complete selected GTDB, GenBank, RefSeq and BV-BRC primary objects;
    retained source accession versions, explicit deposit/sample/project chains, BV-BRC
    statuses and the explicit paired-assembly relationship.
  locator: 'line 34258: {"accession":"RS_GCF_003201765.2","gtdb_representative":"t","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    sulfidivorans","gtdb_type_species_of_genus":"f","ncbi_assembly_level":"Complete
    Genome","ncbi_assembly_name":"ASM320176v2","ncbi_assembly_type":"na","ncbi_bioproject":"PRJNA224116","ncbi_biosample":"SAMN09071530","ncbi_contig_count":"none","ncbi_contig_n50":"none","ncbi_country":"Papua
    New Guinea: Lihr Island","ncbi_date":"2020-03-10","ncbi_genbank_assembly_accession":"GCA_003201765.2","ncbi_genome_category":"none","ncbi_genome_representation":"full","ncbi_isolate":"na","ncbi_isolation_source":"Edge
    of acidic hot spring","ncbi_lat_lon":"none","ncbi_molecule_count":"1","ncbi_ncrna_count":"0","ncbi_organism_name":"Acidianus
    sulfidivorans JP7","ncbi_protein_count":"2312","ncbi_refseq_category":"reference
    genome","ncbi_rrna_count":"3","ncbi_scaffold_count":"1","ncbi_scaffold_l50":"1","ncbi_scaffold_n50":"2265309","ncbi_scaffold_n75":"2265309","ncbi_scaffold_n90":"2265309","ncbi_seq_rel_date":"2020-03-10","ncbi_spanned_gaps":"0","ncbi_species_taxid":"312539","ncbi_ssu_count":"1","ncbi_strain_identifiers":"JP7","ncbi_submitter":"North
    Carolina State University","ncbi_taxid":"619593","ncbi_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    sulfidivorans","ncbi_taxonomy_unfiltered":"d__Archaea;x__Thermoproteati;p__Thermoproteota;c__Thermoprotei;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    sulfidivorans;x__Acidianus sulfidivorans JP7","ncbi_total_gap_length":"0","ncbi_total_length":"2265309","ncbi_translation_table":"11","ncbi_trna_count":"46","ncbi_type_material_designation":"assembly
    from type material","ncbi_ungapped_length":"2265309","ncbi_unspanned_gaps":"0","ncbi_wgs_master":"na"}'
  snapshot_sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
- evidence_id: genome-catalog-2
  kind: primary_source
  reference: data/catalog/ncbi_genbank-0002.jsonl.gz
  accessed_at: '2026-10-19T23:40:24Z'
  support: supports
  summary: Read complete selected GTDB, GenBank, RefSeq and BV-BRC primary objects;
    retained source accession versions, explicit deposit/sample/project chains, BV-BRC
    statuses and the explicit paired-assembly relationship.
  locator: 'line 26071: {"annotation_date":"2019-10-23","annotation_name":"NCBI Prokaryotic
    Genome Annotation Pipeline (PGAP)","annotation_provider":"NCBI","asm_name":"ASM320176v2","asm_not_live_date":"na","asm_submitter":"North
    Carolina State University","assembly_accession":"GCA_003201765.2","assembly_level":"Complete
    Genome","assembly_type":"haploid","bioproject":"PRJNA463410","biosample":"SAMN09071530","contig_count":"1","excluded_from_refseq":"na","ftp_path":"https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/003/201/765/GCA_003201765.2_ASM320176v2/","gbrs_paired_asm":"GCF_003201765.2","gc_percent":"31.000000","genome_rep":"Full","genome_size":"2265309","genome_size_ungapped":"2265309","group":"archaea","infraspecific_name":"strain=JP7","isolate":"na","non_coding_gene_count":"51","organism_name":"Acidianus
    sulfidivorans JP7","paired_asm_comp":"identical","protein_coding_gene_count":"2259","pubmed_id":"na","refseq_category":"reference
    genome","relation_to_type_material":"assembly from type material","release_type":"Major","replicon_count":"1","scaffold_count":"1","seq_rel_date":"2020-03-10","species_taxid":"312539","taxid":"619593","total_gene_count":"2339","version_status":"latest","wgs_master":"na"}'
  snapshot_sha256: 5931b3c1684ae211b5a726b0ac459abe095cb6d27a4eb8f6f54cc34aca211f75
- evidence_id: genome-catalog-3
  kind: primary_source
  reference: data/catalog/ncbi_refseq-0001.jsonl.gz
  accessed_at: '2026-10-19T23:40:24Z'
  support: supports
  summary: Read complete selected GTDB, GenBank, RefSeq and BV-BRC primary objects;
    retained source accession versions, explicit deposit/sample/project chains, BV-BRC
    statuses and the explicit paired-assembly relationship.
  locator: 'line 44166: {"annotation_date":"2026-03-30","annotation_name":"GCF_003201765.2-RS_2026_03_30","annotation_provider":"NCBI
    RefSeq","asm_name":"ASM320176v2","asm_not_live_date":"na","asm_submitter":"North
    Carolina State University","assembly_accession":"GCF_003201765.2","assembly_level":"Complete
    Genome","assembly_type":"haploid","bioproject":"PRJNA224116","biosample":"SAMN09071530","contig_count":"1","excluded_from_refseq":"na","ftp_path":"https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/003/201/765/GCF_003201765.2_ASM320176v2/","gbrs_paired_asm":"GCA_003201765.2","gc_percent":"31.000000","genome_rep":"Full","genome_size":"2265309","genome_size_ungapped":"2265309","group":"archaea","infraspecific_name":"strain=JP7","isolate":"na","non_coding_gene_count":"51","organism_name":"Acidianus
    sulfidivorans JP7","paired_asm_comp":"identical","protein_coding_gene_count":"2290","pubmed_id":"na","refseq_category":"reference
    genome","relation_to_type_material":"assembly from type material","release_type":"Major","replicon_count":"1","scaffold_count":"1","seq_rel_date":"2020-03-10","species_taxid":"312539","taxid":"619593","total_gene_count":"2356","version_status":"latest","wgs_master":"na"}'
  snapshot_sha256: 06282ae41e57cf37ac73b236eab58ecaa081a04bf54d834b1fb61ac065ad56dc
- evidence_id: genome-catalog-4
  kind: primary_source
  reference: data/bvbrc/bvbrc-0025.jsonl.gz
  accessed_at: '2026-10-19T23:40:24Z'
  support: supports
  summary: Read complete selected GTDB, GenBank, RefSeq and BV-BRC primary objects;
    retained source accession versions, explicit deposit/sample/project chains, BV-BRC
    statuses and the explicit paired-assembly relationship.
  locator: 'line 39144: {"assembly_accession":"GCA_003201765.1","bioproject_accession":"PRJNA463410","biosample_accession":"SAMN09071530","culture_collection":"DSM:18786","date_modified":"2018-07-15T23:29:48.127Z","genbank_accessions":"CP029288","genome_id":"619593.4","genome_name":"Acidianus
    sulfidivorans JP7","genome_status":"Deprecated","public":true,"strain":"JP7","superkingdom":"Archaea","taxon_id":619593,"taxon_lineage_ids":["131567","2157","1783275","28889","183924","2281","118883","12914","312539","619593"],"taxon_lineage_names":["cellular
    organisms","Archaea","Thermoproteati","Thermoproteota","Thermoprotei","Sulfolobales","Sulfolobaceae","Acidianus","Acidianus
    sulfidivorans","Acidianus sulfidivorans JP7"]}; line 39145: {"assembly_accession":"GCA_003201765.2","bioproject_accession":"PRJNA463410","biosample_accession":"SAMN09071530","culture_collection":"DSM:18786","date_modified":"2022-11-30T21:06:24.497Z","genbank_accessions":"CP029288","genome_id":"619593.7","genome_name":"Acidianus
    sulfidivorans JP7","genome_status":"Complete","public":true,"reference_genome":"Representative","strain":"JP7","superkingdom":"Archaea","taxon_id":619593,"taxon_lineage_ids":["131567","2157","1783275","28889","183924","2281","118883","12914","312539","619593"],"taxon_lineage_names":["cellular
    organisms","Archaea","Thermoproteati","Thermoproteota","Thermoprotei","Sulfolobales","Sulfolobaceae","Acidianus","Acidianus
    sulfidivorans","Acidianus sulfidivorans JP7"]}'
  snapshot_sha256: 6d40fd7201112c415d5a8112b19b4ce388a4e44ea98fd879e4814897959befaf
- evidence_id: genome-catalog-manifest
  kind: record_content
  reference: data/catalog/MANIFEST.json
  accessed_at: '2026-10-20T03:31:15Z'
  support: supports
  summary: GTDB RS232 provenance; this JP7 source review independently scanned all
    19 captured GTDB primary shards.
  locator: coverage.sources[name=GTDB]
  snapshot_sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
- evidence_id: gtdb-full-count
  kind: search
  reference: data/catalog/MANIFEST.json
  accessed_at: '2026-10-19T23:40:23Z'
  support: supports
  summary: Exact species-cluster selection found one genome, RS_GCF_003201765.2, at
    shard 0017 line 34258; ncbi_taxid 619593 differs from species_taxid 312539.
  locator: '{"paths":["data/catalog/gtdb_genomes-0000.jsonl.gz","data/catalog/gtdb_genomes-0001.jsonl.gz","data/catalog/gtdb_genomes-0002.jsonl.gz","data/catalog/gtdb_genomes-0003.jsonl.gz","data/catalog/gtdb_genomes-0004.jsonl.gz","data/catalog/gtdb_genomes-0005.jsonl.gz","data/catalog/gtdb_genomes-0006.jsonl.gz","data/catalog/gtdb_genomes-0007.jsonl.gz","data/catalog/gtdb_genomes-0008.jsonl.gz","data/catalog/gtdb_genomes-0009.jsonl.gz","data/catalog/gtdb_genomes-0010.jsonl.gz","data/catalog/gtdb_genomes-0011.jsonl.gz","data/catalog/gtdb_genomes-0012.jsonl.gz","data/catalog/gtdb_genomes-0013.jsonl.gz","data/catalog/gtdb_genomes-0014.jsonl.gz","data/catalog/gtdb_genomes-0015.jsonl.gz","data/catalog/gtdb_genomes-0016.jsonl.gz","data/catalog/gtdb_genomes-0017.jsonl.gz","data/catalog/gtdb_genomes-0018.jsonl.gz"],"count":1,"member":"data/catalog/gtdb_genomes-0017.jsonl.gz:34258"}'
  snapshot_sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
  search_scope: Full reads of all 19 captured GTDB RS232 primary JSONL shards, including
    ignored files, exact terminal species-taxon equality.
- evidence_id: cafi-registry
  kind: authority
  reference: src/taxonmech/data/cafi_acronyms.json
  accessed_at: '2026-10-19T23:38:53Z'
  support: supports
  summary: Pinned registry entries 1 (DSM) and 14 (JCM) require the full numeric accession.
    DSM 18786/DSM:18786 and JCM 13667 normalize as eligible; bare JP7 is rejected.
  locator: '{"accessed_at":"2026-10-19T23:38:53.156143+00:00","registry_rows":{"1":{"acr":"DSM","acr_synonym":["DSMZ"],"active":true,"catalogue":["https://www.dsmz.de/collection/catalogue/details/culture/{acr}-{id}"],"code":"DSMZ","country":"DE","gbif":"883f3d24-35e9-462d-b7a3-13c2b9b7260e","homepage":"https://www.dsmz.de/","name":"DSMZ-German
    Collection of Microorganisms and Cell Cultures","regex_ccno":"^DSM\\s*\\d+$","regex_id":{"full":"^\\d+$"},"ror":"02tyer376"},"14":{"acr":"JCM","active":true,"catalogue":["https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?{acr}={id}"],"code":"JCM","country":"JP","gbif":"fce1f744-ca76-46bb-9428-d92cfebe39d4","homepage":"https://jcm.brc.riken.jp/en/","name":"Japan
    Collection of Microorganisms","regex_ccno":"^JCM\\s*\\d+$","regex_id":{"full":"^\\d+$"},"ror":"00s05em53"}},"normalization":{"DSM
    18786":"DSM-18786","DSM:18786":"DSM-18786","JCM 13667":"JCM-13667","JP7":""}}'
  snapshot_sha256: d51abac898f8796dbc2c7b127bb4e61a8ada7f4350fdce689cf755d926446061
- evidence_id: source-metadata-16
  kind: record_content
  reference: data/bacdive/SOURCE.json
  accessed_at: '2026-10-20T03:31:15Z'
  support: supports
  summary: Source capture/projection provenance was inspected separately from the
    historical kg-microbe aggregate input.
  locator: source snapshot metadata
  snapshot_sha256: 16c898e46bca4544e4d9f1908db229aa3d360c8cf7018e036a5389a979dc3716
- evidence_id: source-metadata-17
  kind: record_content
  reference: data/bvbrc/SOURCE.json
  accessed_at: '2026-10-20T03:31:15Z'
  support: supports
  summary: Source capture/projection provenance was inspected separately from the
    historical kg-microbe aggregate input.
  locator: source snapshot metadata
  snapshot_sha256: 0e00cbb6c5fa55ceb60f8d9359a86f605feaf26ddfa4f91dab084bc52f1d1fe4
- evidence_id: source-metadata-18
  kind: record_content
  reference: data/gold/SOURCE.json
  accessed_at: '2026-10-20T03:31:15Z'
  support: supports
  summary: Source capture/projection provenance was inspected separately from the
    historical kg-microbe aggregate input.
  locator: source snapshot metadata
  snapshot_sha256: c7ff51dc6be17c45b18cd031500fde0bd83fb6275e7c021e51bedf68f75ecf2d
- evidence_id: source-metadata-19
  kind: record_content
  reference: data/catalog/PRIMARY.json
  accessed_at: '2026-10-20T03:31:15Z'
  support: supports
  summary: Source capture/projection provenance was inspected separately from the
    historical kg-microbe aggregate input.
  locator: source snapshot metadata
  snapshot_sha256: 8ae7c5d329ebfccb98670f1b40d58932e400d1f3423e45135dc3926d412c17e5
- evidence_id: lpsn-live
  kind: authority
  reference: https://lpsn.dsmz.de/species/acidianus-sulfidivorans
  accessed_at: '2026-10-19T23:39:12Z'
  support: supports
  summary: Current LPSN 785735 identifies the legitimate, correct, validly published
    species and JP7 = DSM 18786 = JCM 13667 type material.
  locator: Name, status, type strain, publications and sequence accession AY907891
  snapshot_sha256: 4e794d06317ac024de81fc2141947c992351ba281344636b90aa031f667b7039
- evidence_id: doi-original
  kind: authority
  reference: https://api.crossref.org/works/10.1099%2Fijs.0.64846-0
  accessed_at: '2026-10-19T23:38:10Z'
  support: supports
  summary: Crossref identifies DOI 10.1099/ijs.0.64846-0 as the original species description;
    publication metadata is distinct from full-text reassessment.
  locator: message DOI, title, author and publication fields
  snapshot_sha256: 00c0d8c1ab7134c41e29e844b0557d25347ea264d7a5e85a89ce3f4aadef2d36
- evidence_id: doi-notification
  kind: authority
  reference: https://api.crossref.org/works/10.1099%2Fijs.0.65508-0
  accessed_at: '2026-10-19T23:38:10Z'
  support: supports
  summary: Crossref identifies DOI 10.1099/ijs.0.65508-0 as the subsequent IJSEM notification
    list.
  locator: message DOI, title and publication fields
  snapshot_sha256: e4b62b19dd1b56be27271fec85ece169a5ea76b37aba061f0d6080b840a47ff9
- evidence_id: pubmed-original
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=17625168&retmode=xml
  accessed_at: '2026-10-19T23:38:11Z'
  support: supports
  summary: Inspected PMID 17625168 metadata and abstract, including the JP7 type-strain
    designation and species description; no experimental mechanism is inferred.
  locator: PubmedArticle/MedlineCitation/Article and Abstract
  snapshot_sha256: 875d29601368c55d00c2a10b43232b3ee0a72fbefc6004109bf19eb94c0474b6
- evidence_id: nucleotide-authority
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&id=AY907891&retmode=json
  accessed_at: '2026-10-19T23:38:11Z'
  support: supports
  summary: NCBI resolves source accession AY907891 to AY907891.1, the 1,473-base JP7
    16S rRNA sequence under taxon 619593. This is accession identity, not a genome
    or expression-module claim.
  locator: nuccore result accessionversion, title, slen and taxid
  snapshot_sha256: d09a9ab4f69a7117653bac936a3ba2a227fed2aad5d4102b3eabc0ea6e7cc404
- evidence_id: historical-edge-1
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
- evidence_id: historical-edge-2
  kind: search
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T07:30:22Z'
  support: partial
  summary: Configured historical input exists with a different hash. This reuses the
    earlier actual receipt and does not claim a fresh or worldwide search.
  locator: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv;
    expected=3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f; observed=c19bfc848e1b410548614c54a2b99e2c58452d58aeb61f972c99fcb3039a1d24
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
  reference: just validate-strict data/taxa/archaea/acidianus_sulfidivorans.yaml --out
    /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/strict-03.tsv
  accessed_at: '2026-10-19T23:35:09Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/repo;\
    \ started 2026-10-19T23:35:07Z, finished 2026-10-19T23:35:09Z, exit 0. This exact\
    \ generated YAML only; its captured bytes remain unchanged. Actual earlier per-target\
    \ invocation; the receipt retains its original cwd and times.\nValidating 1 files\
    \ with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0003/strict-03.tsv"
  locator: This exact generated YAML only; its captured bytes remain unchanged. Actual
    earlier per-target invocation; the receipt retains its original cwd and times.
  snapshot_sha256: 7df693f280a62330f6d4461948d17fd7d407c6d55224759f0cbe8dbff77eacd4
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
  summary: NCBITaxon:312539 denotes the species Acidianus sulfidivorans below genus
    12914, with nine carried ancestors and genetic code 11. Pinned and current NCBI
    agree on name, rank, parent, lineage and authority synonym. Child 619593 is the
    JP7 strain; the parent record gathers its BacDive entry with classified_as rather
    than replacing the species identity.
  target_ids:
  - NCBITaxon:312539
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
  summary: LPSN 785735 is the legitimate, correct, validly published ICNP name Acidianus
    sulfidivorans Plumb et al. 2007. Its type designations DSM 18786 and JCM 13667
    match BacDive deposits. The current LPSN page and original-description PubMed
    abstract also identify JP7 as this type strain. DOI 10.1099/ijs.0.64846-0 and
    PMID 17625168 identify the original description; DOI 10.1099/ijs.0.65508-0 identifies
    the subsequent IJSEM notification list. LPSN AY907891 resolves at NCBI as AY907891.1,
    a 1473-base JP7 16S rRNA sequence under taxon 619593; the record preserves the
    source unversioned accession. Both deposits support the parent record's derived
    is_type_strain flag.
  target_ids:
  - NCBITaxon:312539
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
  summary: The complete pinned NCBI subtree has one child taxon and one imported BacDive
    entry, 16644, with both supplied deposits retained. The BacDive attestation correctly
    counts 1 STRAIN gathered from 1 descendant. GOLD 7 ORGANISM and Madin 3 TRAIT_ASSERTION
    are the direct species-level inventory counts; they are not counts of the two
    displayed deposit-linked GOLD organism objects and do not include the child taxon.
    The original historical edge multiplicities remain unavailable for independent
    recount.
  target_ids:
  - NCBITaxon:312539
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
  - genome-catalog-1
  - genome-catalog-2
  - genome-catalog-3
  - genome-catalog-4
  - cafi-registry
  - source-metadata-16
  - source-metadata-17
  - source-metadata-18
  - source-metadata-19
  - lpsn-live
  - pubmed-original
  - nucleotide-authority
- assessment_id: taxonomy-mapping
  area: grounding
  topic: Qualified species mapping and target scope
  outcome: supported
  summary: The LPSN 785735 inventory explicitly links the species name to GTDB:s__Acidianus_sulfidivorans,
    supporting the species xref under the local harmonization policy. The sole direct
    GTDB mapping row instead targets child NCBITaxon:619593, so absence of a parent
    taxonomy_mappings entry is expected. The sole GTDB primary genome RS_GCF_003201765.2
    has taxon 619593, species_taxid 312539 and strain identifier JP7. Membership supports
    the one-genome cluster; bare JP7 does not create a GTDB deposit/assembly join.
    Species-level LPSN equivalence is distinct from the problematic exact species
    synonym on the child record.
  target_ids:
  - NCBITaxon:312539
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
  - genome-catalog-4
  - gtdb-full-count
  - genome-catalog-manifest
- assessment_id: strain-assertions
  area: evidence
  topic: Strain, deposit and genome-source links
  outcome: supported
  summary: BacDive 16644 directly specifies JP7, DSM 18786 and JCM 13667, the narrower
    NCBI taxon 619593, unversioned GCA_003201765 and BV-BRC 619593.4/619593.7. The
    BV-BRC primary rows explicitly join DSM:18786 to GCA_003201765.1 and .2 respectively;
    .4 is Deprecated and .7 Complete in the captured source. The earlier assertion
    remains source history, without asserting that the two versions are identical.
    Both rows cite PRJNA463410 and SAMN09071530, also present in the current GenBank
    .2 row. RefSeq GCF_003201765.2 is explicitly paired as identical to GenBank .2
    in the primary metadata, but no assembly equivalence is inferred from shared names
    or samples. GOLD Go0002318 explicitly identifies DSM 18786 and taxon 619593; Go0608847
    explicitly identifies JCM 13667 and taxon 312539 in two distinct assertion fields.
    Neither organism ID occurs in the full captured GOLD sequencing-project projection,
    so no project/analysis chain is invented. SI-ID 309414.3 supplies its own available
    deposits SI-DP 720496 (DSM 18786) and 720497 (JCM 13667); its full record has
    no sequence assertion to transfer between deposits. CAFI recognizes the full DSM/JCM
    numeric accessions, while bare JP7 is ineligible as a culture-deposit join. Every
    one of the 3 assembly, 4 genome-record and 11 related-record assertions matches
    the raw/StrainInfo multiset, including source fields, versions, deposit IDs and
    provenance.
  target_ids:
  - NCBITaxon:312539
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
  - genome-catalog-1
  - genome-catalog-2
  - genome-catalog-3
  - genome-catalog-4
  - cafi-registry
  - source-metadata-16
  - source-metadata-17
  - source-metadata-18
  - source-metadata-19
  - lpsn-live
  - pubmed-original
  - nucleotide-authority
- assessment_id: native-status
  area: provenance
  topic: Unchanged native status and history
  outcome: supported
  summary: The NCBI identity is grounded EXACT and the record remains SEEDED. Its
    single seed event is consistent with the latest extraction timestamp across raw,
    ATB and StrainInfo manifests (2026-09-13T17:54:04Z). This review neither appends
    history nor promotes native status.
  target_ids:
  - NCBITaxon:312539
  evidence_ids:
  - record
  - manifest
  - overlay-manifests
findings: []
actions:
- action_id: recover-pinned-aggregate-inputs
  finding_ids: []
  target_ids:
  - NCBITaxon:312539
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
- The review covers each complete generated target and the explicitly inspected source
  evidence. It does not independently re-estimate phylogenetic species boundaries
  or infer experimental mechanisms from database annotations.
- The NCBI snapshot is dated 2026-09-13. Current NCBI, LPSN, publication and nucleotide
  checks are kept distinct from source snapshot assertions; imported strain counts
  are not worldwide strain censuses.
- Publication identifiers, DOI metadata and the PubMed abstract were checked; the
  full original article and notification-list text were not reassessed. AY907891 resolves
  to the JP7 16S sequence, not a genome assembly. No expression-module or physiological
  inference is needed to establish this accession identity.
- Historical GOLD and Madin counts match the committed species-level inventories.
  Parent-session checks found that configured local historical edge files differ from
  the original hashes in data/raw/MANIFEST.yaml; those files cannot independently
  reproduce the pinned counts. Required historical aggregate verification remains
  unavailable.
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
