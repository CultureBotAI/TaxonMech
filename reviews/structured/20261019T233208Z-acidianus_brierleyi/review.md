# Record review: Acidianus brierleyi

- Review: 20261019T233208Z-acidianus_brierleyi
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-19T07:22:18Z
- Finished UTC: 2026-10-19T23:32:08Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Acidianus brierleyi is consistently identified by NCBI and LPSN, with two distinct BacDive strains. The Aramenus brierleyi GTDB cross-reference follows the repository's documented species closeMatch policy. Genome links remain deposit- and source-specific. No record-specific defect was established; historical aggregate counts and independent phylogenetic equivalence remain limited.

## Scope And Provenance

The entire single resolved generated TaxonRecord and its identity, nomenclature, mapping, strain, source-count and provenance assertions.

Selection: First ten unreviewed corpus paths in lexicographic order at base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; this is record 4. Reviewed means an actual target of a validated bundle from scripts/record_review.py list. Inventory coverage alone does not count.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9b5a8fff5185b38dc5c77bb35235152c81ea7765.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:41673 | data/taxa/archaea/acidianus_brierleyi.yaml | generated | Acidianus brierleyi |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact NCBI taxon, rank and lineage | passed | True | NCBITaxon:41673 | NCBITaxon:41673 denotes the species Acidianus brierleyi, parent 12914, with nine carried ancestors and genetic code 11. Current NCBI confirms the same species, while LPSN retains the Sulfolobus brierleyi basonym. Neither the alternative GTDB genus nor a genome name changes the carried NCBI identity. |
| Deposit-specific source assertions and reference resolution | passed | True | NCBITaxon:41673 | BacDive and StrainInfo keep the type strain separate from DSM 6334. SI-ID 47466.3 associates DSM 1651 with SI-DP 157456, IFO 15269 with 157457 and NBRC 15269 with 335614. The GCA_003201835 sequence belongs explicitly to DSM 1651; D26489 explicitly names DSM and IFO deposits. The JCM sequence AB304843 is not transferred because JCM 8954 is absent from the BacDive deposit set. SI-ID 48152.2/SI-DP 159955 supplies DSM 6334 context and no sequence. GOLD Go0032875 → Gp0376662 → Ga0485363 supports GCA_003201835.2/IMG 2927569001/SAMN09071529. GTDB RS_GCF_003201835.2 and NCBI GCA/GCF versions retain their distinct provenance. BV-BRC 41673.4 supplies historical GCA_003201835.1 with source status Deprecated, whereas 41673.10 supplies .2; the record does not claim every source assertion is current. All four imported nucleotide accessions resolve to NCBI taxon 41673. Exact comparisons found 12 assembly, nine genome-record and 39 related assertions for 16640, plus two related assertions and no assemblies/genomes for 16641, equal to the inputs. |
| Structured expression-module adapter | unavailable | False | NCBITaxon:41673 | No installed kg-microbe-sources runner was found. The checked local claw directory contained no project and wizard-claw did not expose this runner. The inspected iModulonDB page supplied no usable dataset text. Gene names here are sequence-description context; no expression-module or mechanism conclusion was inferred. |
| Original aggregate source-edge multiplicities | unavailable | True | NCBITaxon:41673 | Inventories support the record's counts, but the original manifest-pinned MediaDive/GOLD/Madin edge bytes were unavailable in the checked locations; current external files have different hashes. No recount of current data can validate the historical numbers. |
| Initial quality-gate setup attempt | failed | False | NCBITaxon:41673 | Exit 1: missing ruff dependency; environment repaired before the separately recorded full retry. |
| Native strict record validation | passed | True | NCBITaxon:41673 | Actual terminal exit code 0. This exact generated YAML only. |
| Repository history validation | passed | True | NCBITaxon:41673 | Actual terminal exit code 0. All 17 committed standalone history records; generated seed history also inspected in this target. |
| Full-corpus exact reproduction | passed | True | NCBITaxon:41673 | Actual terminal exit code 0. All 625,960 generated taxon YAMLs, not a focused approximation. |
| Native product ID/label gate | passed | True | NCBITaxon:41673 | Actual terminal exit code 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. |
| Authoritative complete quality gate | passed | True | NCBITaxon:41673 | Actual terminal exit code 0. Repository-wide just qc on the isolated checkout; includes corpus-wide checks. Pytest reported 1055 passed, 3 skipped and 5 deselected; the native QC recipe completed successfully. |

## Scientific And Domain Assessments

### Resolved biological taxon and carried lineage

identity: supported. Targets: NCBITaxon:41673.

NCBITaxon:41673 denotes the species Acidianus brierleyi, parent 12914, with nine carried ancestors and genetic code 11. Current NCBI confirms the same species, while LPSN retains the Sulfolobus brierleyi basonym. Neither the alternative GTDB genus nor a genome name changes the carried NCBI identity.

### Source-scoped names and nomenclatural standing

nomenclature: supported. Targets: NCBITaxon:41673.

LPSN 772573 is the correct, validly published ICNP name; retained LPSN 782311 is the homotypic Sulfolobus synonym. The author string, DSM 1651/IFO 15269/JCM 8954/NBRC 15269 type designations, D26489 and the 1986 publication DOI match the authority and DOI metadata. GTDB:s__Aramenus_brierleyi has one genome and one NCBI mapping in the inspected inventory. Its exact synonym/xref is the documented one-to-one species normalization rule, not a claim that Aramenus is the ICNP accepted genus. A missing LPSN→GTDB bridge alone is therefore not scored as a defect.

### Complete imported subtree and source assertion units

completeness: supported. Targets: NCBITaxon:41673.

Both BacDive 16640 (type strain, DSM 1651/IFO 15269/NBRC 15269) and 16641 (Sp3a/1, DSM 6334, non-type) are retained. The inventory contains no omitted strain in the target subtree. MediaDive 4, GOLD 5 and Madin 10 attestations match the raw rows but cannot be recounted against the original upstream edge snapshots. JCM 8954 in nomenclature is not automatically an existing BacDive deposit to which genome links can be transferred.

### Deposit authority, source chains and exact accessions

evidence: supported. Targets: NCBITaxon:41673.

BacDive and StrainInfo keep the type strain separate from DSM 6334. SI-ID 47466.3 associates DSM 1651 with SI-DP 157456, IFO 15269 with 157457 and NBRC 15269 with 335614. The GCA_003201835 sequence belongs explicitly to DSM 1651; D26489 explicitly names DSM and IFO deposits. The JCM sequence AB304843 is not transferred because JCM 8954 is absent from the BacDive deposit set. SI-ID 48152.2/SI-DP 159955 supplies DSM 6334 context and no sequence. GOLD Go0032875 → Gp0376662 → Ga0485363 supports GCA_003201835.2/IMG 2927569001/SAMN09071529. GTDB RS_GCF_003201835.2 and NCBI GCA/GCF versions retain their distinct provenance. BV-BRC 41673.4 supplies historical GCA_003201835.1 with source status Deprecated, whereas 41673.10 supplies .2; the record does not claim every source assertion is current. All four imported nucleotide accessions resolve to NCBI taxon 41673. Exact comparisons found 12 assembly, nine genome-record and 39 related assertions for 16640, plus two related assertions and no assemblies/genomes for 16641, equal to the inputs.

### GTDB mapping scope and source genome count

grounding: supported. Targets: NCBITaxon:41673.

GTDB RS_GCF_003201835.2 has ncbi_taxid 41673, DSM 1651 and species Aramenus brierleyi. The sole raw mapping is closeMatch to NCBITaxon:41673. This supplies the documented species normalization boundary, while the independent biological equivalence of the NCBI and GTDB species circumscriptions has not been re-estimated from sequence data.

### Seed event and scientific status boundary

provenance: supported. Targets: NCBITaxon:41673.

The NCBI identity is grounded EXACT and the record remains SEEDED. Its single seed event is consistent with the latest extraction timestamp across raw, ATB and StrainInfo manifests (2026-09-13T17:54:04Z). This review neither appends history nor promotes native status.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### verify-pinned-aggregate-edges

Recover the upstream kg-microbe edge snapshots whose SHA-256 values are pinned in data/raw/MANIFEST.yaml, then recount this exact target using the maintained extractor's source-specific counting rules. This resolves the historical-count limitation without changing generated records.

- Recovered edge files match the manifest SHA-256 values before any comparison.
- Recount only the target's explicit MediaDive METPO:2000517 medium set, GOLD Go subclass assertions and Madin taxon-subject assertions that this record actually attests; preserve their distinct units and direct-taxon boundaries.
- Compare the resulting counts and medium identifiers with the exact inventoried rows cited in this review, and retain any discrepancy as a new observation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/taxa/archaea/acidianus_brierleyi.yaml; entire TaxonRecord; identifier=NCBITaxon:41673 | supports | Read the entire generated YAML, including identity, all synonyms, mappings, source attestations, every strain assertion and seed history. |
| taxonomy-inventory | data/raw/ncbitaxon_taxa.tsv; line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""}; line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"}; line 1798: {"taxon_id":"NCBITaxon:2281","label":"Sulfolobales","rank":"ORDER","parent_id":"NCBITaxon:183924"}; line 2648: {"taxon_id":"NCBITaxon:12914","label":"Acidianus","rank":"GENUS","parent_id":"NCBITaxon:118883"}; line 2980: {"taxon_id":"NCBITaxon:28889","label":"Thermoproteota","rank":"PHYLUM","parent_id":"NCBITaxon:1783275"}; line 4858: {"taxon_id":"NCBITaxon:41673","label":"Acidianus brierleyi","rank":"SPECIES","parent_id":"NCBITaxon:12914","genetic_code":"11","exact_synonyms":"Sulfolobus brierleyi","related_synonyms":"Acidianus brierleyi (Zillig et al. 1980) Segerer et al. 1986&#124;Sulfolobus brierleyi Zillig et al. 1980","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb&#124;bacdive&#124;lpsn&#124;mediadive&#124;gold&#124;madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"}; line 22254: {"taxon_id":"NCBITaxon:118883","label":"Sulfolobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2281"}; line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"}; line 36612: {"taxon_id":"NCBITaxon:183924","label":"Thermoprotei","rank":"CLASS","parent_id":"NCBITaxon:28889"}; line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"} | supports | Inspected the exact target row and every carried ancestor. Rank, label, parent, genetic code and typed source names were compared with the complete record. |
| scope-row | curation/seed_scope.tsv; line 5224: {"identifier":"NCBITaxon:41673","added":"2026-09-12","reason":"attested rule: Acidianus brierleyi, 7 sources incl. NCBI"} | supports | The exact target is explicitly included in the seed scope. |
| path-row | data/taxa/PATHS.tsv; line 498669: {"identifier":"NCBITaxon:41673","slug":"acidianus_brierleyi"} | supports | The indexed path resolves to the same NCBI taxon and generated target. |
| ncbi-live | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=41673; TaxaSet/Taxon[TaxId='41673']; captured together with the other nine explicitly selected batch taxa | supports | Inspected the official current taxonomy response for this exact taxon: scientific name, rank, parent, source name classes, lineage identifiers and genetic code. Compared it with the separately pinned September taxonomy. |
| lpsn-inventory | data/raw/lpsn_names.tsv; line 14848: {"lpsn_id":"lpsn:772573","name":"Acidianus brierleyi","rank":"SPECIES","authority":"(Zillig et al. 1980) Segerer et al. 1986","url":"https://lpsn.dsmz.de/species/acidianus-brierleyi","deprecated":"0","status":"legitimate=True; validly published under the ICNP; correct name","validly_published":"1","legitimate":"1","is_correct_name":"1","parent_lpsn_id":"lpsn:516964","ncbitaxon_ids":"NCBITaxon:41673","gtdb_ids":"","type_strain_ids":"kgmicrobe.strain:DSM-1651&#124;kgmicrobe.strain:IFO-15269&#124;kgmicrobe.strain:JCM-8954&#124;kgmicrobe.strain:NBRC-15269","synonym_of":"lpsn:782311","synonyms":"lpsn:782311","publications":"doi:10.1099/00207713-36-4-559","sequence_accessions":"INSDC:D26489"}; line 20801: {"lpsn_id":"lpsn:782311","name":"Sulfolobus brierleyi","rank":"SPECIES","authority":"Zillig et al. 1980","url":"https://lpsn.dsmz.de/species/sulfolobus-brierleyi","deprecated":"1","status":"legitimate=True; validly published under the ICNP; synonym","validly_published":"1","legitimate":"1","is_correct_name":"0","parent_lpsn_id":"lpsn:517122","ncbitaxon_ids":"","gtdb_ids":"","type_strain_ids":"kgmicrobe.strain:DSM-1651&#124;kgmicrobe.strain:IFO-15269&#124;kgmicrobe.strain:JCM-8954&#124;kgmicrobe.strain:NBRC-15269","synonym_of":"lpsn:772573","synonyms":"lpsn:772573","publications":"doi:10.1007/bf00446886&#124;doi:10.1099/00207713-30-4-676","sequence_accessions":"INSDC:D26489"} | supports | Inspected all exact taxon/name mappings and linked synonymous LPSN names, retaining statuses and type-designation scope. |
| gtdb-mappings | data/raw/gtdb_mappings.tsv; line 288072: {"gtdb_id":"GTDB:s__Aramenus_brierleyi","gtdb_label":"s__Aramenus_brierleyi","gtdb_parent":"GTDB:g__Aramenus","ncbitaxon_id":"NCBITaxon:41673","predicate":"skos:closeMatch","genome_count":"1"} | supports | Inspected this taxon's GTDB mappings and every reverse mapping of the same selected source cluster; predicates and counts remain source-scoped. |
| gtdb-species | data/raw/gtdb_species.tsv; line 12258: {"gtdb_id":"GTDB:s__Aramenus_brierleyi","label":"s__Aramenus_brierleyi","parent":"GTDB:g__Aramenus","genome_count":"1"} | supports | Inspected source species identifiers, labels, parent cluster and genome counts. |
| bacdive-inventory | data/raw/bacdive_strains.tsv; line 16459: {"strain_id":"kgmicrobe.strain:bacdive_16640","bacdive_id":"16640","designation":"","taxon_ids":"NCBITaxon:41673","lpsn_ids":"lpsn:772573","culture_collection_ids":"kgmicrobe.strain:DSM-1651&#124;kgmicrobe.strain:IFO-15269&#124;kgmicrobe.strain:NBRC-15269","medium_count":"0"}; line 16460: {"strain_id":"kgmicrobe.strain:bacdive_16641","bacdive_id":"16641","designation":"Sp3a/1","taxon_ids":"NCBITaxon:41673","lpsn_ids":"lpsn:772573","culture_collection_ids":"kgmicrobe.strain:DSM-6334","medium_count":"0"} | supports | Full BacDive inventory selection used the exact taxon plus every descendant from the complete NCBI parent graph. Deposits, type status and classified_as remain separate from taxon identity. |
| culture-inventory | data/raw/culture_collection_strains.tsv; line 67489: {"strain_id":"kgmicrobe.strain:DSM-1651","taxon_ids":"NCBITaxon:41673"}; line 86119: {"strain_id":"kgmicrobe.strain:DSM-6334","taxon_ids":"NCBITaxon:41673"}; line 94080: {"strain_id":"kgmicrobe.strain:IFO-15269","taxon_ids":"NCBITaxon:41673"}; line 136671: {"strain_id":"kgmicrobe.strain:NBRC-15269","taxon_ids":"NCBITaxon:41673"} | supports | Inspected exact culture identifiers associated with the target; source aliases do not independently authorize genome joins. |
| gold-organisms | data/raw/gold_organisms.tsv; line 34902: {"taxon_id":"NCBITaxon:41673","organism_count":"5"} | supports | Inspected the exact GOLD organism count row, or its bounded absence, without converting counts to phenotypes. |
| mediadive-taxa | data/raw/mediadive_taxa.tsv; line 9998: {"taxon_id":"NCBITaxon:41673","medium_count":"4","media_ids":"mediadive.medium:150&#124;mediadive.medium:358&#124;mediadive.medium:358a&#124;mediadive.medium:J176"} | supports | Inspected the exact MediaDive medium count row, or its bounded absence, without converting counts to phenotypes. |
| madin-taxa | data/raw/madin_taxa.tsv; line 23754: {"taxon_id":"NCBITaxon:41673","assertion_count":"10"} | supports | Inspected the exact Madin trait-assertion count row, or its bounded absence, without converting counts to phenotypes. |
| bactotraits-taxa | data/raw/bactotraits_taxa.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Inspected the exact BactoTraits trait-assertion count row, or its bounded absence, without converting counts to phenotypes. |
| mapping-policy | docs/HARMONIZATION.md; Mapping predicates and Scope and lineage sections | supports | The local mapping policy permits one-to-one species closeMatch mappings and LPSN-linked species to supply xrefs/synonyms, retains pooled broadMatch entries separately, and carries NCBI lineage unchanged. |
| equivalence-contract | src/taxonmech/schema/taxonmech.yaml; TaxonRecord.xrefs (lines 180–187); TaxonomyMapping (lines 417–439) | supports | TaxonRecord.xrefs denotes true equivalence, while broader/narrower relationships belong in taxonomy_mappings; TaxonomyMapping.genome_count counts genomes under the source taxon. |
| seed-owner | src/taxonmech/seed.py; GTDB mapping construction and identity promotion, lines 440–472 | supports | The identity branch accepts an LPSN GTDB bridge or any skos:closeMatch, then emits an equivalent xref and, if the text differs, an EXACT_SYNONYM. It does not guard against a strain-rank target. |
| manifest | data/raw/MANIFEST.yaml; kg_microbe_source, inputs, extracted_at | supports | The source manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd and hashes individual upstream inputs; extraction time is 2026-09-13T17:50:44Z. |
| overlay-manifests | data/atb/MANIFEST.yaml; extracted_at, together with data/straininfo/MANIFEST.yaml | supports | Compared raw, ATB and StrainInfo extraction timestamps. Their maximum, 2026-09-13T17:54:04Z, matches the sole generated seed event. The StrainInfo manifest is separately captured in source.inputs. |
| primary-source-1 | data/bacdive/records.jsonl.gz; decompressed JSONL lines 16458, 16459 | supports | Inspected complete selected source objects, including identifier/deposit fields and explicit source relationships. Source grouping and taxonomic similarity do not transfer sequence assertions across deposits. |
| primary-source-2 | data/straininfo/records.jsonl.gz; decompressed JSONL lines 35397, 36044 | supports | Inspected complete selected source objects, including identifier/deposit fields and explicit source relationships. Source grouping and taxonomic similarity do not transfer sequence assertions across deposits. |
| primary-source-3 | data/gold/organisms.jsonl.gz; decompressed JSONL lines 28004, 434170, 434171 | supports | Inspected complete selected source objects, including identifier/deposit fields and explicit source relationships. These are organism/project/analysis records, not interchangeable genome identifiers. |
| primary-source-4 | data/gold/projects.jsonl.gz; decompressed JSONL lines 264243 | supports | Inspected complete selected source objects, including identifier/deposit fields and explicit source relationships. These are organism/project/analysis records, not interchangeable genome identifiers. |
| primary-source-5 | data/gold/analyses.jsonl.gz; decompressed JSONL lines 312978 | supports | Inspected complete selected source objects, including identifier/deposit fields and explicit source relationships. These are organism/project/analysis records, not interchangeable genome identifiers. |
| assembly-inputs | data/raw/strain_assemblies.tsv; selected data lines 81905, 81906, 81907, 81908, 81909, 81910, 81911, 81912, 81913, 81914, 81915 | supports | Inspected every matching source row and compared all assertion fields with this record; accessions and source evidence remain distinct. |
| genome-inputs | data/raw/strain_genome_records.tsv; selected data lines 64119, 64120, 64121, 64122, 64123, 64124, 64125, 64126, 64127 | supports | Inspected every matching source row and compared all assertion fields with this record; accessions and source evidence remain distinct. |
| related-inputs | data/raw/strain_related_records.tsv; selected data lines 249071, 249072, 249073, 249074, 249075, 249076, 249077, 249078, 249079, 249080, 249081, 249082, 249083, 249084, 249085, 249086, 249087, 249088, 249089, 249090, 249091, 249092, 249093, 249094, 249095, 249096, 249097, 249098 | supports | Inspected every matching source row and compared all assertion fields with this record; accessions and source evidence remain distinct. |
| straininfo-deposits | data/straininfo/strain_links.tsv; selected data lines 68768, 68769, 68770, 68779 | supports | Inspected every matching source row and compared all assertion fields with this record; accessions and source evidence remain distinct. |
| straininfo-assemblies | data/straininfo/assemblies.tsv; selected data lines 5951 | supports | Inspected every matching source row and compared all assertion fields with this record; accessions and source evidence remain distinct. |
| straininfo-related | data/straininfo/related_records.tsv.gz; selected data lines 162476, 162477, 162478, 162479, 162480, 162481, 162482, 162483, 162484, 162485, 162486, 162503, 162504 | supports | Inspected every matching source row and compared all assertion fields with this record; accessions and source evidence remain distinct. |
| atb-links | data/atb/strain_links.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Inspected every matching source row and compared all assertion fields with this record; accessions and source evidence remain distinct. |
| cafi-registry | src/taxonmech/data/cafi_acronyms.json; authority entries for the record's deposit prefixes and their regex_id.full templates | supports | The pinned collection registry governs full deposit accession matching. DSM, IFO, JCM and NBRC identifiers retain their own authorities; bare aliases and nonmatching formats do not supply inferred joins. |
| nucleotide-authority | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&amp;retmode=json&amp;id=AB088419.1,D26489.1,GQ409758.1,X90477.1; AB088419.1: Acidianus brierleyi orf290, orf1614, accC, accB, pccB, orf582 genes, partial and complete cds; D26489.1: Acidianus brierleyi 16S rRNA gene complete sequence and 23S rRNA gene 5' region; GQ409758.1: Acidianus brierleyi strain DSM 1651 propionyl-CoA carboxylase (pccB) gene, partial cds; X90477.1: A.brierleyi DNA for 16S ribosomal RNA gene | supports | All 4 imported nucleotide references resolve to NCBI taxon 41673. The accession versions returned by the current authority are recorded for resolution only; unversioned source assertions are not rewritten. Checked accession, taxid and sequence title for each entry. |
| genome-catalog-manifest | data/catalog/MANIFEST.json; coverage.sources[name=GTDB] | supports | The complete native GTDB genome catalog is the RS232 snapshot. Species clusters and MAGs remain distinct from physical strain deposits. |
| genome-catalog-1 | data/catalog/gtdb_genomes-0017.jsonl.gz; line 40680: {"accession":"RS_GCF_003201835.2","ncbi_taxid":"41673","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Aramenus;s__Aramenus brierleyi","ncbi_strain_identifiers":"DSM 1651"} | supports | Inspected the complete selected genome catalog rows. Source genome identity, taxonomic assignment, deposit fields and accession versions were assessed separately. |
| genome-catalog-2 | data/catalog/ncbi_genbank-0002.jsonl.gz; line 26074: {"assembly_accession":"GCA_003201835.2","taxid":"41673","infraspecific_name":"strain=DSM 1651"} | supports | Inspected the complete selected genome catalog rows. Source genome identity, taxonomic assignment, deposit fields and accession versions were assessed separately. |
| genome-catalog-4 | data/catalog/ncbi_refseq-0001.jsonl.gz; line 44169: {"assembly_accession":"GCF_003201835.2","taxid":"41673","infraspecific_name":"strain=DSM 1651"} | supports | Inspected the complete selected genome catalog rows. Source genome identity, taxonomic assignment, deposit fields and accession versions were assessed separately. |
| genome-catalog-5 | data/bvbrc/bvbrc-0020.jsonl.gz; line 10452: {"assembly_accession":"GCA_003201835.2","genome_id":"41673.10","taxon_id":41673,"genome_name":"Acidianus brierleyi DSM 1651","genome_status":"Complete"}; line 10453: {"assembly_accession":"GCA_003201835.1","genome_id":"41673.4","taxon_id":41673,"genome_name":"Acidianus brierleyi strain DSM 1651","genome_status":"Deprecated"} | supports | Inspected the complete selected genome catalog rows. Source genome identity, taxonomic assignment, deposit fields and accession versions were assessed separately. |
| lpsn-live | https://lpsn.dsmz.de/species/acidianus-brierleyi; Name; category; nomenclatural/taxonomic status; type designations; synonyms and cited publication metadata | supports | Inspected the authority's name, category, nomenclatural and taxonomic status, type designations, synonyms and cited publication identity. These fields were compared with the pinned inventory rather than substituted into the record. |
| doi-1986 | https://doi.org/10.1099/00207713-36-4-559; Acidianus infernus gen. nov., sp. nov., and Acidianus brierleyi Comb. nov.: Facultatively Aerobic, Extremely Acidophilic Thermophilic Sulfur-Metabolizing Archaebacteria; pages 559-564 | supports | Crossref registration confirms the cited publication identity, date and bibliographic pagination; this is metadata verification, not a review of the paper's experimental evidence. |
| historical-edge-availability | data/raw/MANIFEST.yaml; data/transformed/mediadive/edges.tsv: expected=78ea275a59d4e2de09a9cf72652ec64454c6a111d2defa1ae0a44bac8a72e523, present=4e933d1e2412fb1aad74e60719a6a64dfa34862ff0a6b84e93d78da5ce13dd8b; data/transformed/gold/edges.tsv: expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12, present=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d; data/transformed/madin_etal/edges.tsv: expected=3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f, present=c19bfc848e1b410548614c54a2b99e2c58452d58aeb61f972c99fcb3039a1d24 | partial | The exact configured external paths were checked including ignored files. They exist, but each current SHA-256 differs from the manifest-pinned snapshot; none was treated as the original extraction input. |
| qc-setup-receipt | just qc; initial setup attempt, 2026-10-19T07:17:01Z through 2026-10-19T07:17:01Z | context_only | Initial actual invocation exited 1 because the isolated environment lacked ruff. Locked ruff 0.16.7 was then installed in that environment and the full command retried; qc below records the retry result. |
| strict-receipt | just validate-strict data/taxa/archaea/acidianus_brierleyi.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/strict-04.tsv; This exact generated YAML only. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:22:20Z, finished 2026-10-19T07:22:21Z, exit 0.<br>Validating 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/strict-04.tsv |
| history-receipt | just validate-history; All 17 committed standalone history records; generated seed history also inspected in this target. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:01Z, finished 2026-10-19T07:17:03Z, exit 0.<br>history links: 17 record(s), 0 invalid<br>No issues found<br>17 history record(s) valid against src/taxonmech/schema/history.yaml |
| corpus-receipt | just verify-corpus; All 625,960 generated taxon YAMLs, not a focused approximation. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:18:23Z, finished 2026-10-19T07:24:12Z, exit 0.<br>uv run python scripts/verify_corpus.py <br>expected 625960 records, found 625960 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ and curation/seed_scope.tsv |
| products-receipt | just validate-products; Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:01Z, finished 2026-10-19T07:55:11Z, exit 0.<br>uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml<br><br>id↔label correspondence summary:<br><br>✅ All id↔label pairs correspond. |
| qc-receipt | just qc; Repository-wide just qc on the isolated checkout; includes corpus-wide checks. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:17:41Z, finished 2026-10-19T08:07:39Z, exit 0.<br>1055 passed, 3 skipped, 5 deselected in 1634.00s (0:27:13)<br>Validating 625960 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml<br>  files scanned:      625960<br>expected 625960 records, found 625960 on disk<br>pages/ is current<br>Site publication: 530,864,122 bytes (budget 950,000,000)<br>625960 taxon records<br>  NCBITAXON        625960<br>All TaxonMech quality gates passed.<br>  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890 strains (not genome counts)<br>  Related STRAININFO_DEPOSIT: 107277 strain-record pairs, 106843 identifiers, 53890 strains (not genome counts)<br>  Related NUCLEOTIDE_SEQUENCE: 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)<br>LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809 records mapped, 324404579 genomes summed across record attestations (not deduplicated)<br>Causal graphs: 0 records (0 evidence-backed edges)<br><br>All TaxonMech quality gates passed. |

## Limits And Additional Notes

- This review is limited to the entire generated record and the specified source evidence. It does not independently re-estimate phylogenetic species boundaries or establish experimental mechanisms from database annotations.
- The NCBI taxonomy snapshot is dated 2026-09-13. Current authority checks are distinguished from pinned source assertions; source coverage and zero imported strains are not worldwide absence claims.
- Historical source counts match the committed inventories, but the locally configured kg-microbe MediaDive, GOLD and Madin edge files have hashes different from data/raw/MANIFEST.yaml. They cannot reproduce the original counts. Required historical edge verification is unavailable; completion remains partial.
- Publication identifiers were checked against LPSN and DOI registration metadata; original paper full text was not reassessed. Nucleotide descriptions were checked at NCBI. An iModulonDB structured runner was unavailable in the checked environment; source pages supplied no usable dataset coverage, so no expression-module or experimental-mechanism inference was made.
- No generated record, page or curation history was edited. Findings and actions are proposed work, not completed fixes or native scientific-status promotion.
- The initial just qc attempt failed because ruff was absent. The locked ruff 0.16.7 dependency was installed only in this isolated environment, and the complete command was retried; the final retry result is recorded above.
- The initial whole-corpus listing found 52 existing actual record targets among 625,960 corpus records. Historical TSV inventories are not substituted for one-record structured bundles.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T233208Z-acidianus_brierleyi
kind: record
repository: CultureBotAI/TaxonMech
title: 'Record review: Acidianus brierleyi'
started_at: '2026-10-19T07:22:18Z'
finished_at: '2026-10-19T23:32:08Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: The reviewer did not author or curate the target records. This
    pass only inspects existing data and authors new review bundles in an isolated
    clone.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: Acidianus brierleyi is consistently identified by NCBI and LPSN, with two
  distinct BacDive strains. The Aramenus brierleyi GTDB cross-reference follows the
  repository's documented species closeMatch policy. Genome links remain deposit-
  and source-specific. No record-specific defect was established; historical aggregate
  counts and independent phylogenetic equivalence remain limited.
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
  - path: data/bvbrc/bvbrc-0020.jsonl.gz
    sha256: ce96b1844f603b80f97dd4d814dafe8d4091e976a8b9e3a4e59fafffd28ad553
    role: context
  - path: data/catalog/MANIFEST.json
    sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
    role: context
  - path: data/catalog/gtdb_genomes-0017.jsonl.gz
    sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
    role: context
  - path: data/catalog/ncbi_genbank-0002.jsonl.gz
    sha256: 5931b3c1684ae211b5a726b0ac459abe095cb6d27a4eb8f6f54cc34aca211f75
    role: context
  - path: data/catalog/ncbi_genbank-0052.jsonl.gz
    sha256: 09f90de7c34454c61e3cbb8e91780b6011db46309550657b0eaad6bd99670b91
    role: context
  - path: data/catalog/ncbi_refseq-0001.jsonl.gz
    sha256: 06282ae41e57cf37ac73b236eab58ecaa081a04bf54d834b1fb61ac065ad56dc
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
    sha256: c950844feb0638ce04f7349784749dd1d728fe70bc80f7e2756d956d4ecea254
    role: context
  - path: data/taxa/archaea/acidianus_brierleyi.yaml
    sha256: 1447cb07cbb4e7822c47d61536c92a99d534e716d6aec7253d8400c4cca54730
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
    nomenclature, mapping, strain, source-count and provenance assertions.
  selection: First ten unreviewed corpus paths in lexicographic order at base 9b5a8fff5185b38dc5c77bb35235152c81ea7765;
    this is record 4. Reviewed means an actual target of a validated bundle from scripts/record_review.py
    list. Inventory coverage alone does not count.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - NCBITaxon:41673
targets:
- target_id: NCBITaxon:41673
  path: data/taxa/archaea/acidianus_brierleyi.yaml
  label: Acidianus brierleyi
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
  summary: NCBITaxon:41673 denotes the species Acidianus brierleyi, parent 12914,
    with nine carried ancestors and genetic code 11. Current NCBI confirms the same
    species, while LPSN retains the Sulfolobus brierleyi basonym. Neither the alternative
    GTDB genus nor a genome name changes the carried NCBI identity.
  target_ids:
  - NCBITaxon:41673
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - scope-row
  - path-row
- check_id: strain-genome-evidence
  name: Deposit-specific source assertions and reference resolution
  status: passed
  required: true
  summary: BacDive and StrainInfo keep the type strain separate from DSM 6334. SI-ID
    47466.3 associates DSM 1651 with SI-DP 157456, IFO 15269 with 157457 and NBRC
    15269 with 335614. The GCA_003201835 sequence belongs explicitly to DSM 1651;
    D26489 explicitly names DSM and IFO deposits. The JCM sequence AB304843 is not
    transferred because JCM 8954 is absent from the BacDive deposit set. SI-ID 48152.2/SI-DP
    159955 supplies DSM 6334 context and no sequence. GOLD Go0032875 → Gp0376662 →
    Ga0485363 supports GCA_003201835.2/IMG 2927569001/SAMN09071529. GTDB RS_GCF_003201835.2
    and NCBI GCA/GCF versions retain their distinct provenance. BV-BRC 41673.4 supplies
    historical GCA_003201835.1 with source status Deprecated, whereas 41673.10 supplies
    .2; the record does not claim every source assertion is current. All four imported
    nucleotide accessions resolve to NCBI taxon 41673. Exact comparisons found 12
    assembly, nine genome-record and 39 related assertions for 16640, plus two related
    assertions and no assemblies/genomes for 16641, equal to the inputs.
  target_ids:
  - NCBITaxon:41673
  evidence_ids:
  - record
  - bacdive-inventory
  - primary-source-1
  - primary-source-2
  - primary-source-3
  - primary-source-4
  - primary-source-5
  - assembly-inputs
  - genome-inputs
  - related-inputs
  - straininfo-deposits
  - straininfo-assemblies
  - straininfo-related
  - atb-links
  - cafi-registry
  - nucleotide-authority
  scope_note: Entire strain list and every imported assembly/genome/related assertion;
    hand inspection of primary source rows plus exact raw/StrainInfo multiset comparison.
    Not a replacement for full-corpus reproduction.
- check_id: imodulondb-adapter
  name: Structured expression-module adapter
  status: unavailable
  required: false
  summary: No installed kg-microbe-sources runner was found. The checked local claw
    directory contained no project and wizard-claw did not expose this runner. The
    inspected iModulonDB page supplied no usable dataset text. Gene names here are
    sequence-description context; no expression-module or mechanism conclusion was
    inferred.
  target_ids:
  - NCBITaxon:41673
  evidence_ids:
  - nucleotide-authority
  command: command -v kg-microbe-sources
  scope_note: Optional context for genes named in imported nucleotide descriptions;
    coverage not established, so no absence claim about Acidianus datasets.
- check_id: historical-source-counts
  name: Original aggregate source-edge multiplicities
  status: unavailable
  required: true
  summary: Inventories support the record's counts, but the original manifest-pinned
    MediaDive/GOLD/Madin edge bytes were unavailable in the checked locations; current
    external files have different hashes. No recount of current data can validate
    the historical numbers.
  target_ids:
  - NCBITaxon:41673
  evidence_ids:
  - manifest
  - historical-edge-availability
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
- check_id: qc-setup-attempt
  name: Initial quality-gate setup attempt
  status: failed
  required: false
  summary: 'Exit 1: missing ruff dependency; environment repaired before the separately
    recorded full retry.'
  target_ids:
  - NCBITaxon:41673
  evidence_ids:
  - qc-setup-receipt
  command: just qc
  exit_code: 1
  expected_exit_code: 0
  scope_note: Superseded environment setup attempt, not the final native QC result.
- check_id: strict
  name: Native strict record validation
  status: passed
  required: true
  summary: Actual terminal exit code 0. This exact generated YAML only.
  target_ids:
  - NCBITaxon:41673
  evidence_ids:
  - strict-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/uv-cache
    just validate-strict data/taxa/archaea/acidianus_brierleyi.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/strict-04.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: This exact generated YAML only.
- check_id: history
  name: Repository history validation
  status: passed
  required: true
  summary: Actual terminal exit code 0. All 17 committed standalone history records;
    generated seed history also inspected in this target.
  target_ids:
  - NCBITaxon:41673
  evidence_ids:
  - history-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/uv-cache
    just validate-history
  exit_code: 0
  expected_exit_code: 0
  scope_note: All 17 committed standalone history records; generated seed history
    also inspected in this target.
- check_id: corpus
  name: Full-corpus exact reproduction
  status: passed
  required: true
  summary: Actual terminal exit code 0. All 625,960 generated taxon YAMLs, not a focused
    approximation.
  target_ids:
  - NCBITaxon:41673
  evidence_ids:
  - corpus-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/uv-cache
    just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  scope_note: All 625,960 generated taxon YAMLs, not a focused approximation.
- check_id: products
  name: Native product ID/label gate
  status: passed
  required: true
  summary: Actual terminal exit code 0. Full configured corpus scan for curator-added
    graph nodes; this target contains no causal graph.
  target_ids:
  - NCBITaxon:41673
  evidence_ids:
  - products-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/uv-cache
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: Full configured corpus scan for curator-added graph nodes; this target
    contains no causal graph.
- check_id: qc
  name: Authoritative complete quality gate
  status: passed
  required: true
  summary: Actual terminal exit code 0. Repository-wide just qc on the isolated checkout;
    includes corpus-wide checks. Pytest reported 1055 passed, 3 skipped and 5 deselected;
    the native QC recipe completed successfully.
  target_ids:
  - NCBITaxon:41673
  evidence_ids:
  - qc-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/uv-cache
    just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: Repository-wide just qc on the isolated checkout; includes corpus-wide
    checks.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/taxa/archaea/acidianus_brierleyi.yaml
  accessed_at: '2026-10-19T23:32:08Z'
  support: supports
  summary: Read the entire generated YAML, including identity, all synonyms, mappings,
    source attestations, every strain assertion and seed history.
  locator: entire TaxonRecord; identifier=NCBITaxon:41673
  snapshot_sha256: 1447cb07cbb4e7822c47d61536c92a99d534e716d6aec7253d8400c4cca54730
- evidence_id: taxonomy-inventory
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Inspected the exact target row and every carried ancestor. Rank, label,
    parent, genetic code and typed source names were compared with the complete record.
  locator: 'line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""};
    line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"};
    line 1798: {"taxon_id":"NCBITaxon:2281","label":"Sulfolobales","rank":"ORDER","parent_id":"NCBITaxon:183924"};
    line 2648: {"taxon_id":"NCBITaxon:12914","label":"Acidianus","rank":"GENUS","parent_id":"NCBITaxon:118883"};
    line 2980: {"taxon_id":"NCBITaxon:28889","label":"Thermoproteota","rank":"PHYLUM","parent_id":"NCBITaxon:1783275"};
    line 4858: {"taxon_id":"NCBITaxon:41673","label":"Acidianus brierleyi","rank":"SPECIES","parent_id":"NCBITaxon:12914","genetic_code":"11","exact_synonyms":"Sulfolobus
    brierleyi","related_synonyms":"Acidianus brierleyi (Zillig et al. 1980) Segerer
    et al. 1986|Sulfolobus brierleyi Zillig et al. 1980","broad_synonyms":"","attested_by":"ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"};
    line 22254: {"taxon_id":"NCBITaxon:118883","label":"Sulfolobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2281"};
    line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"};
    line 36612: {"taxon_id":"NCBITaxon:183924","label":"Thermoprotei","rank":"CLASS","parent_id":"NCBITaxon:28889"};
    line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
- evidence_id: scope-row
  kind: database
  reference: curation/seed_scope.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: The exact target is explicitly included in the seed scope.
  locator: 'line 5224: {"identifier":"NCBITaxon:41673","added":"2026-09-12","reason":"attested
    rule: Acidianus brierleyi, 7 sources incl. NCBI"}'
  snapshot_sha256: 5fdc0f7111b64e02439d95c6f2b51fcff1d2154c34b2d957422dd9b297e94d4b
- evidence_id: path-row
  kind: database
  reference: data/taxa/PATHS.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: The indexed path resolves to the same NCBI taxon and generated target.
  locator: 'line 498669: {"identifier":"NCBITaxon:41673","slug":"acidianus_brierleyi"}'
  snapshot_sha256: c950844feb0638ce04f7349784749dd1d728fe70bc80f7e2756d956d4ecea254
- evidence_id: ncbi-live
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=41673
  accessed_at: '2026-10-19T07:21:19Z'
  support: supports
  summary: 'Inspected the official current taxonomy response for this exact taxon:
    scientific name, rank, parent, source name classes, lineage identifiers and genetic
    code. Compared it with the separately pinned September taxonomy.'
  locator: TaxaSet/Taxon[TaxId='41673']; captured together with the other nine explicitly
    selected batch taxa
  snapshot_sha256: 520faf6a04c00bf6a23ceda7be536ac20f87f878e83936a21df23f283c23db51
- evidence_id: lpsn-inventory
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Inspected all exact taxon/name mappings and linked synonymous LPSN names,
    retaining statuses and type-designation scope.
  locator: 'line 14848: {"lpsn_id":"lpsn:772573","name":"Acidianus brierleyi","rank":"SPECIES","authority":"(Zillig
    et al. 1980) Segerer et al. 1986","url":"https://lpsn.dsmz.de/species/acidianus-brierleyi","deprecated":"0","status":"legitimate=True;
    validly published under the ICNP; correct name","validly_published":"1","legitimate":"1","is_correct_name":"1","parent_lpsn_id":"lpsn:516964","ncbitaxon_ids":"NCBITaxon:41673","gtdb_ids":"","type_strain_ids":"kgmicrobe.strain:DSM-1651|kgmicrobe.strain:IFO-15269|kgmicrobe.strain:JCM-8954|kgmicrobe.strain:NBRC-15269","synonym_of":"lpsn:782311","synonyms":"lpsn:782311","publications":"doi:10.1099/00207713-36-4-559","sequence_accessions":"INSDC:D26489"};
    line 20801: {"lpsn_id":"lpsn:782311","name":"Sulfolobus brierleyi","rank":"SPECIES","authority":"Zillig
    et al. 1980","url":"https://lpsn.dsmz.de/species/sulfolobus-brierleyi","deprecated":"1","status":"legitimate=True;
    validly published under the ICNP; synonym","validly_published":"1","legitimate":"1","is_correct_name":"0","parent_lpsn_id":"lpsn:517122","ncbitaxon_ids":"","gtdb_ids":"","type_strain_ids":"kgmicrobe.strain:DSM-1651|kgmicrobe.strain:IFO-15269|kgmicrobe.strain:JCM-8954|kgmicrobe.strain:NBRC-15269","synonym_of":"lpsn:772573","synonyms":"lpsn:772573","publications":"doi:10.1007/bf00446886|doi:10.1099/00207713-30-4-676","sequence_accessions":"INSDC:D26489"}'
  snapshot_sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
- evidence_id: gtdb-mappings
  kind: database
  reference: data/raw/gtdb_mappings.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Inspected this taxon's GTDB mappings and every reverse mapping of the same
    selected source cluster; predicates and counts remain source-scoped.
  locator: 'line 288072: {"gtdb_id":"GTDB:s__Aramenus_brierleyi","gtdb_label":"s__Aramenus_brierleyi","gtdb_parent":"GTDB:g__Aramenus","ncbitaxon_id":"NCBITaxon:41673","predicate":"skos:closeMatch","genome_count":"1"}'
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
- evidence_id: gtdb-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Inspected source species identifiers, labels, parent cluster and genome
    counts.
  locator: 'line 12258: {"gtdb_id":"GTDB:s__Aramenus_brierleyi","label":"s__Aramenus_brierleyi","parent":"GTDB:g__Aramenus","genome_count":"1"}'
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
- evidence_id: bacdive-inventory
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Full BacDive inventory selection used the exact taxon plus every descendant
    from the complete NCBI parent graph. Deposits, type status and classified_as remain
    separate from taxon identity.
  locator: 'line 16459: {"strain_id":"kgmicrobe.strain:bacdive_16640","bacdive_id":"16640","designation":"","taxon_ids":"NCBITaxon:41673","lpsn_ids":"lpsn:772573","culture_collection_ids":"kgmicrobe.strain:DSM-1651|kgmicrobe.strain:IFO-15269|kgmicrobe.strain:NBRC-15269","medium_count":"0"};
    line 16460: {"strain_id":"kgmicrobe.strain:bacdive_16641","bacdive_id":"16641","designation":"Sp3a/1","taxon_ids":"NCBITaxon:41673","lpsn_ids":"lpsn:772573","culture_collection_ids":"kgmicrobe.strain:DSM-6334","medium_count":"0"}'
  snapshot_sha256: 029fd6d1f53ef7f90684130bf0d644ed3edd1d8fbeb065a511ae928f160b1eea
- evidence_id: culture-inventory
  kind: database
  reference: data/raw/culture_collection_strains.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Inspected exact culture identifiers associated with the target; source
    aliases do not independently authorize genome joins.
  locator: 'line 67489: {"strain_id":"kgmicrobe.strain:DSM-1651","taxon_ids":"NCBITaxon:41673"};
    line 86119: {"strain_id":"kgmicrobe.strain:DSM-6334","taxon_ids":"NCBITaxon:41673"};
    line 94080: {"strain_id":"kgmicrobe.strain:IFO-15269","taxon_ids":"NCBITaxon:41673"};
    line 136671: {"strain_id":"kgmicrobe.strain:NBRC-15269","taxon_ids":"NCBITaxon:41673"}'
  snapshot_sha256: 810fdcb16abd6330fb15bb03d4c74b18db86be36a7c599df7c6b2498d9735c95
- evidence_id: gold-organisms
  kind: database
  reference: data/raw/gold_organisms.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Inspected the exact GOLD organism count row, or its bounded absence, without
    converting counts to phenotypes.
  locator: 'line 34902: {"taxon_id":"NCBITaxon:41673","organism_count":"5"}'
  snapshot_sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
- evidence_id: mediadive-taxa
  kind: database
  reference: data/raw/mediadive_taxa.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Inspected the exact MediaDive medium count row, or its bounded absence,
    without converting counts to phenotypes.
  locator: 'line 9998: {"taxon_id":"NCBITaxon:41673","medium_count":"4","media_ids":"mediadive.medium:150|mediadive.medium:358|mediadive.medium:358a|mediadive.medium:J176"}'
  snapshot_sha256: 3f74b78cadfcdb6aeae953e09fdb39e34fd9c5d5ed0be65a04a5d7fb02355905
- evidence_id: madin-taxa
  kind: database
  reference: data/raw/madin_taxa.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Inspected the exact Madin trait-assertion count row, or its bounded absence,
    without converting counts to phenotypes.
  locator: 'line 23754: {"taxon_id":"NCBITaxon:41673","assertion_count":"10"}'
  snapshot_sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
- evidence_id: bactotraits-taxa
  kind: database
  reference: data/raw/bactotraits_taxa.tsv
  accessed_at: '2026-10-19T07:22:21Z'
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
  accessed_at: '2026-10-19T23:32:08Z'
  support: supports
  summary: The local mapping policy permits one-to-one species closeMatch mappings
    and LPSN-linked species to supply xrefs/synonyms, retains pooled broadMatch entries
    separately, and carries NCBI lineage unchanged.
  locator: Mapping predicates and Scope and lineage sections
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
- evidence_id: equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-19T23:32:08Z'
  support: supports
  summary: TaxonRecord.xrefs denotes true equivalence, while broader/narrower relationships
    belong in taxonomy_mappings; TaxonomyMapping.genome_count counts genomes under
    the source taxon.
  locator: TaxonRecord.xrefs (lines 180–187); TaxonomyMapping (lines 417–439)
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
- evidence_id: seed-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-19T23:32:08Z'
  support: supports
  summary: The identity branch accepts an LPSN GTDB bridge or any skos:closeMatch,
    then emits an equivalent xref and, if the text differs, an EXACT_SYNONYM. It does
    not guard against a strain-rank target.
  locator: GTDB mapping construction and identity promotion, lines 440–472
  snapshot_sha256: 6b5b065f4ae7aea022af736a22c0f63dc58a2425c7ee453259e567ab030f8257
- evidence_id: manifest
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T23:32:08Z'
  support: supports
  summary: The source manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd
    and hashes individual upstream inputs; extraction time is 2026-09-13T17:50:44Z.
  locator: kg_microbe_source, inputs, extracted_at
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
- evidence_id: overlay-manifests
  kind: record_content
  reference: data/atb/MANIFEST.yaml
  accessed_at: '2026-10-19T23:32:08Z'
  support: supports
  summary: Compared raw, ATB and StrainInfo extraction timestamps. Their maximum,
    2026-09-13T17:54:04Z, matches the sole generated seed event. The StrainInfo manifest
    is separately captured in source.inputs.
  locator: extracted_at, together with data/straininfo/MANIFEST.yaml
  snapshot_sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
- evidence_id: primary-source-1
  kind: primary_source
  reference: data/bacdive/records.jsonl.gz
  accessed_at: '2026-10-19T07:23:48Z'
  support: supports
  summary: Inspected complete selected source objects, including identifier/deposit
    fields and explicit source relationships. Source grouping and taxonomic similarity
    do not transfer sequence assertions across deposits.
  locator: decompressed JSONL lines 16458, 16459
  snapshot_sha256: b27d0f50f06aa33615e7cc2aae4acb7c2767df930c85292e76fbb462ac136080
- evidence_id: primary-source-2
  kind: primary_source
  reference: data/straininfo/records.jsonl.gz
  accessed_at: '2026-10-19T07:23:48Z'
  support: supports
  summary: Inspected complete selected source objects, including identifier/deposit
    fields and explicit source relationships. Source grouping and taxonomic similarity
    do not transfer sequence assertions across deposits.
  locator: decompressed JSONL lines 35397, 36044
  snapshot_sha256: 8f8e6093f0617317e0488463e52de153f566effa7a5d43b44d17dabab9692819
- evidence_id: primary-source-3
  kind: primary_source
  reference: data/gold/organisms.jsonl.gz
  accessed_at: '2026-10-19T07:23:48Z'
  support: supports
  summary: Inspected complete selected source objects, including identifier/deposit
    fields and explicit source relationships. These are organism/project/analysis
    records, not interchangeable genome identifiers.
  locator: decompressed JSONL lines 28004, 434170, 434171
  snapshot_sha256: 8c1a055214cb240c58fadda0815efbefcb60848245e8a7474e6b1b41d123235c
- evidence_id: primary-source-4
  kind: primary_source
  reference: data/gold/projects.jsonl.gz
  accessed_at: '2026-10-19T07:23:48Z'
  support: supports
  summary: Inspected complete selected source objects, including identifier/deposit
    fields and explicit source relationships. These are organism/project/analysis
    records, not interchangeable genome identifiers.
  locator: decompressed JSONL lines 264243
  snapshot_sha256: 0d852fe0144afd778609fef82b266fd1507a4c0be949efd2f53c7c34526b6c95
- evidence_id: primary-source-5
  kind: primary_source
  reference: data/gold/analyses.jsonl.gz
  accessed_at: '2026-10-19T07:23:48Z'
  support: supports
  summary: Inspected complete selected source objects, including identifier/deposit
    fields and explicit source relationships. These are organism/project/analysis
    records, not interchangeable genome identifiers.
  locator: decompressed JSONL lines 312978
  snapshot_sha256: d597f0d5f31fc8b387caaf659f3c6a337959219870529e907a1c0287e3877b7a
- evidence_id: assembly-inputs
  kind: database
  reference: data/raw/strain_assemblies.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Inspected every matching source row and compared all assertion fields with
    this record; accessions and source evidence remain distinct.
  locator: selected data lines 81905, 81906, 81907, 81908, 81909, 81910, 81911, 81912,
    81913, 81914, 81915
  snapshot_sha256: 71344b934db3081bfcac9562a0bd1fd8fddcfdabb8af60e208ca09035e818315
- evidence_id: genome-inputs
  kind: database
  reference: data/raw/strain_genome_records.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Inspected every matching source row and compared all assertion fields with
    this record; accessions and source evidence remain distinct.
  locator: selected data lines 64119, 64120, 64121, 64122, 64123, 64124, 64125, 64126,
    64127
  snapshot_sha256: 47ed80be55660aad4bd82d37d889ea60f8686cec1aeeccf72e5af22bf43728ab
- evidence_id: related-inputs
  kind: database
  reference: data/raw/strain_related_records.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Inspected every matching source row and compared all assertion fields with
    this record; accessions and source evidence remain distinct.
  locator: selected data lines 249071, 249072, 249073, 249074, 249075, 249076, 249077,
    249078, 249079, 249080, 249081, 249082, 249083, 249084, 249085, 249086, 249087,
    249088, 249089, 249090, 249091, 249092, 249093, 249094, 249095, 249096, 249097,
    249098
  snapshot_sha256: c33a9bf4c6b94dc6971f1c0d46565092c37ba7c2d462a6bc9c20ccbf58fb9c56
- evidence_id: straininfo-deposits
  kind: database
  reference: data/straininfo/strain_links.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Inspected every matching source row and compared all assertion fields with
    this record; accessions and source evidence remain distinct.
  locator: selected data lines 68768, 68769, 68770, 68779
  snapshot_sha256: 615ac119e61df3a9d296ab16674bca6de3fdbf6478ca21a61312014f0ebbae8f
- evidence_id: straininfo-assemblies
  kind: database
  reference: data/straininfo/assemblies.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Inspected every matching source row and compared all assertion fields with
    this record; accessions and source evidence remain distinct.
  locator: selected data lines 5951
  snapshot_sha256: d55ba39ab7cb81076a8edb61226de2bdf0aea699a7fb003cdf3ffb3ddc2f3f52
- evidence_id: straininfo-related
  kind: database
  reference: data/straininfo/related_records.tsv.gz
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Inspected every matching source row and compared all assertion fields with
    this record; accessions and source evidence remain distinct.
  locator: selected data lines 162476, 162477, 162478, 162479, 162480, 162481, 162482,
    162483, 162484, 162485, 162486, 162503, 162504
  snapshot_sha256: c7a262df4f970b2b11a2cf7a0a05c631ff84938e6a19cdb1d98680bb4fb35108
- evidence_id: atb-links
  kind: database
  reference: data/atb/strain_links.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: Inspected every matching source row and compared all assertion fields with
    this record; accessions and source evidence remain distinct.
  locator: complete table; exact target/subtree/source-identifier search had no matching
    row
  snapshot_sha256: 50683192c8015badf14a8a2aab73929a21b830117449ce329d1216a698abf1c0
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: cafi-registry
  kind: authority
  reference: src/taxonmech/data/cafi_acronyms.json
  accessed_at: '2026-10-19T23:32:08Z'
  support: supports
  summary: The pinned collection registry governs full deposit accession matching.
    DSM, IFO, JCM and NBRC identifiers retain their own authorities; bare aliases
    and nonmatching formats do not supply inferred joins.
  locator: authority entries for the record's deposit prefixes and their regex_id.full
    templates
  snapshot_sha256: d51abac898f8796dbc2c7b127bb4e61a8ada7f4350fdce689cf755d926446061
- evidence_id: nucleotide-authority
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&retmode=json&id=AB088419.1,D26489.1,GQ409758.1,X90477.1
  accessed_at: '2026-10-19T07:24:41Z'
  support: supports
  summary: All 4 imported nucleotide references resolve to NCBI taxon 41673. The accession
    versions returned by the current authority are recorded for resolution only; unversioned
    source assertions are not rewritten. Checked accession, taxid and sequence title
    for each entry.
  locator: 'AB088419.1: Acidianus brierleyi orf290, orf1614, accC, accB, pccB, orf582
    genes, partial and complete cds; D26489.1: Acidianus brierleyi 16S rRNA gene complete
    sequence and 23S rRNA gene 5'' region; GQ409758.1: Acidianus brierleyi strain
    DSM 1651 propionyl-CoA carboxylase (pccB) gene, partial cds; X90477.1: A.brierleyi
    DNA for 16S ribosomal RNA gene'
  snapshot_sha256: c8a315c648c5e2573974597d47a9f96a159e16db4ca1f03a106efee3fd079b80
- evidence_id: genome-catalog-manifest
  kind: record_content
  reference: data/catalog/MANIFEST.json
  accessed_at: '2026-10-19T23:32:08Z'
  support: supports
  summary: The complete native GTDB genome catalog is the RS232 snapshot. Species
    clusters and MAGs remain distinct from physical strain deposits.
  locator: coverage.sources[name=GTDB]
  snapshot_sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
- evidence_id: genome-catalog-1
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0017.jsonl.gz
  accessed_at: '2026-10-19T07:25:21Z'
  support: supports
  summary: Inspected the complete selected genome catalog rows. Source genome identity,
    taxonomic assignment, deposit fields and accession versions were assessed separately.
  locator: 'line 40680: {"accession":"RS_GCF_003201835.2","ncbi_taxid":"41673","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Aramenus;s__Aramenus
    brierleyi","ncbi_strain_identifiers":"DSM 1651"}'
  snapshot_sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
- evidence_id: genome-catalog-2
  kind: primary_source
  reference: data/catalog/ncbi_genbank-0002.jsonl.gz
  accessed_at: '2026-10-19T07:25:21Z'
  support: supports
  summary: Inspected the complete selected genome catalog rows. Source genome identity,
    taxonomic assignment, deposit fields and accession versions were assessed separately.
  locator: 'line 26074: {"assembly_accession":"GCA_003201835.2","taxid":"41673","infraspecific_name":"strain=DSM
    1651"}'
  snapshot_sha256: 5931b3c1684ae211b5a726b0ac459abe095cb6d27a4eb8f6f54cc34aca211f75
- evidence_id: genome-catalog-4
  kind: primary_source
  reference: data/catalog/ncbi_refseq-0001.jsonl.gz
  accessed_at: '2026-10-19T07:25:21Z'
  support: supports
  summary: Inspected the complete selected genome catalog rows. Source genome identity,
    taxonomic assignment, deposit fields and accession versions were assessed separately.
  locator: 'line 44169: {"assembly_accession":"GCF_003201835.2","taxid":"41673","infraspecific_name":"strain=DSM
    1651"}'
  snapshot_sha256: 06282ae41e57cf37ac73b236eab58ecaa081a04bf54d834b1fb61ac065ad56dc
- evidence_id: genome-catalog-5
  kind: primary_source
  reference: data/bvbrc/bvbrc-0020.jsonl.gz
  accessed_at: '2026-10-19T07:25:21Z'
  support: supports
  summary: Inspected the complete selected genome catalog rows. Source genome identity,
    taxonomic assignment, deposit fields and accession versions were assessed separately.
  locator: 'line 10452: {"assembly_accession":"GCA_003201835.2","genome_id":"41673.10","taxon_id":41673,"genome_name":"Acidianus
    brierleyi DSM 1651","genome_status":"Complete"}; line 10453: {"assembly_accession":"GCA_003201835.1","genome_id":"41673.4","taxon_id":41673,"genome_name":"Acidianus
    brierleyi strain DSM 1651","genome_status":"Deprecated"}'
  snapshot_sha256: ce96b1844f603b80f97dd4d814dafe8d4091e976a8b9e3a4e59fafffd28ad553
- evidence_id: lpsn-live
  kind: authority
  reference: https://lpsn.dsmz.de/species/acidianus-brierleyi
  accessed_at: '2026-10-19T07:36:00Z'
  support: supports
  summary: Inspected the authority's name, category, nomenclatural and taxonomic status,
    type designations, synonyms and cited publication identity. These fields were
    compared with the pinned inventory rather than substituted into the record.
  locator: Name; category; nomenclatural/taxonomic status; type designations; synonyms
    and cited publication metadata
- evidence_id: doi-1986
  kind: authority
  reference: https://doi.org/10.1099/00207713-36-4-559
  accessed_at: '2026-10-19T07:30:55Z'
  support: supports
  summary: Crossref registration confirms the cited publication identity, date and
    bibliographic pagination; this is metadata verification, not a review of the paper's
    experimental evidence.
  locator: 'Acidianus infernus gen. nov., sp. nov., and Acidianus brierleyi Comb.
    nov.: Facultatively Aerobic, Extremely Acidophilic Thermophilic Sulfur-Metabolizing
    Archaebacteria; pages 559-564'
  snapshot_sha256: 93f33b21e115370eaf87ad815b8fb5e1ad61afa9d3e11726c047be45e695d73a
- evidence_id: historical-edge-availability
  kind: search
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T07:30:22Z'
  support: partial
  summary: The exact configured external paths were checked including ignored files.
    They exist, but each current SHA-256 differs from the manifest-pinned snapshot;
    none was treated as the original extraction input.
  locator: 'data/transformed/mediadive/edges.tsv: expected=78ea275a59d4e2de09a9cf72652ec64454c6a111d2defa1ae0a44bac8a72e523,
    present=4e933d1e2412fb1aad74e60719a6a64dfa34862ff0a6b84e93d78da5ce13dd8b; data/transformed/gold/edges.tsv:
    expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12, present=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d;
    data/transformed/madin_etal/edges.tsv: expected=3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f,
    present=c19bfc848e1b410548614c54a2b99e2c58452d58aeb61f972c99fcb3039a1d24'
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
  search_scope: Exact files beneath the kg_microbe_root in conf/sources.yaml, plus
    an ignored-inclusive search of this isolated clone. No claim that the historical
    snapshots are absent from all storage.
- evidence_id: qc-setup-receipt
  kind: validation
  reference: just qc
  accessed_at: '2026-10-19T07:17:01Z'
  support: context_only
  summary: Initial actual invocation exited 1 because the isolated environment lacked
    ruff. Locked ruff 0.16.7 was then installed in that environment and the full command
    retried; qc below records the retry result.
  locator: initial setup attempt, 2026-10-19T07:17:01Z through 2026-10-19T07:17:01Z
  snapshot_sha256: 1d189beecc64b369096499a7ce4adf71897235e4c1190c69e7d0ed3a77b6a3f9
- evidence_id: strict-receipt
  kind: validation
  reference: just validate-strict data/taxa/archaea/acidianus_brierleyi.yaml --out
    /private/tmp/taxonmech-record-reviews-k0MubV/strict-04.tsv
  accessed_at: '2026-10-19T07:22:21Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo;\
    \ started 2026-10-19T07:22:20Z, finished 2026-10-19T07:22:21Z, exit 0.\nValidating\
    \ 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/strict-04.tsv"
  locator: This exact generated YAML only.
  snapshot_sha256: ceaafb0785ee655d066c5d8ffd1f0c4ab17a65dfbaafde96bc6cfa69ff940393
- evidence_id: history-receipt
  kind: validation
  reference: just validate-history
  accessed_at: '2026-10-19T07:17:03Z'
  support: supports
  summary: 'Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo;
    started 2026-10-19T07:17:01Z, finished 2026-10-19T07:17:03Z, exit 0.

    history links: 17 record(s), 0 invalid

    No issues found

    17 history record(s) valid against src/taxonmech/schema/history.yaml'
  locator: All 17 committed standalone history records; generated seed history also
    inspected in this target.
  snapshot_sha256: 3fc63ae7bb58034c180e5dcebec02f98c487038ba74793b9f43462ddaacdcbf4
- evidence_id: corpus-receipt
  kind: validation
  reference: just verify-corpus
  accessed_at: '2026-10-19T07:24:12Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo;\
    \ started 2026-10-19T07:18:23Z, finished 2026-10-19T07:24:12Z, exit 0.\nuv run\
    \ python scripts/verify_corpus.py \nexpected 625960 records, found 625960 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/ and curation/seed_scope.tsv"
  locator: All 625,960 generated taxon YAMLs, not a focused approximation.
  snapshot_sha256: 6bcd0e5b423155259cb8f8dbecb3e4af467b5dba232906734156e9a99fb5a459
- evidence_id: products-receipt
  kind: validation
  reference: just validate-products
  accessed_at: '2026-10-19T07:55:11Z'
  support: supports
  summary: 'Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo;
    started 2026-10-19T07:17:01Z, finished 2026-10-19T07:55:11Z, exit 0.

    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml


    id↔label correspondence summary:


    ✅ All id↔label pairs correspond.'
  locator: Full configured corpus scan for curator-added graph nodes; this target
    contains no causal graph.
  snapshot_sha256: 48dd07515706dc62199fc2205c4b0bfdd5750028037d9b800179f254d2f1eb07
- evidence_id: qc-receipt
  kind: validation
  reference: just qc
  accessed_at: '2026-10-19T08:07:39Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo;\
    \ started 2026-10-19T07:17:41Z, finished 2026-10-19T08:07:39Z, exit 0.\n1055 passed,\
    \ 3 skipped, 5 deselected in 1634.00s (0:27:13)\nValidating 625960 files with\
    \ 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml\n\
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
  locator: Repository-wide just qc on the isolated checkout; includes corpus-wide
    checks.
  snapshot_sha256: b86a9cc6f529c3b822140f60179e9bc4046e2e6abef3ee0e67fa1035ffb1a76d
assessments:
- assessment_id: identity
  area: identity
  topic: Resolved biological taxon and carried lineage
  outcome: supported
  summary: NCBITaxon:41673 denotes the species Acidianus brierleyi, parent 12914,
    with nine carried ancestors and genetic code 11. Current NCBI confirms the same
    species, while LPSN retains the Sulfolobus brierleyi basonym. Neither the alternative
    GTDB genus nor a genome name changes the carried NCBI identity.
  target_ids:
  - NCBITaxon:41673
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - scope-row
  - path-row
  dimensions:
  - name: taxon-rank
    value: SPECIES
    definition: NCBI rank of the reviewed target, distinct from strain/deposit/genome
      identity.
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
  summary: LPSN 772573 is the correct, validly published ICNP name; retained LPSN
    782311 is the homotypic Sulfolobus synonym. The author string, DSM 1651/IFO 15269/JCM
    8954/NBRC 15269 type designations, D26489 and the 1986 publication DOI match the
    authority and DOI metadata. GTDB:s__Aramenus_brierleyi has one genome and one
    NCBI mapping in the inspected inventory. Its exact synonym/xref is the documented
    one-to-one species normalization rule, not a claim that Aramenus is the ICNP accepted
    genus. A missing LPSN→GTDB bridge alone is therefore not scored as a defect.
  target_ids:
  - NCBITaxon:41673
  evidence_ids:
  - record
  - taxonomy-inventory
  - lpsn-inventory
  - gtdb-mappings
  - mapping-policy
  - lpsn-live
  - doi-1986
- assessment_id: completeness
  area: completeness
  topic: Complete imported subtree and source assertion units
  outcome: supported
  summary: Both BacDive 16640 (type strain, DSM 1651/IFO 15269/NBRC 15269) and 16641
    (Sp3a/1, DSM 6334, non-type) are retained. The inventory contains no omitted strain
    in the target subtree. MediaDive 4, GOLD 5 and Madin 10 attestations match the
    raw rows but cannot be recounted against the original upstream edge snapshots.
    JCM 8954 in nomenclature is not automatically an existing BacDive deposit to which
    genome links can be transferred.
  target_ids:
  - NCBITaxon:41673
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
  dimensions:
  - name: assertion-units
    value: 'NCBITAXON: 1 NAME; LPSN: 1 NAME; GTDB: 1 GENOME; BACDIVE: 2 STRAIN; MEDIADIVE:
      4 MEDIUM; GOLD: 5 ORGANISM; MADIN: 10 TRAIT_ASSERTION'
    definition: Native source-specific counts; not interchangeable biological measurements.
    evidence_ids:
    - record
    - gold-organisms
    - mediadive-taxa
    - madin-taxa
    - bactotraits-taxa
- assessment_id: strain-genome-links
  area: evidence
  topic: Deposit authority, source chains and exact accessions
  outcome: supported
  summary: BacDive and StrainInfo keep the type strain separate from DSM 6334. SI-ID
    47466.3 associates DSM 1651 with SI-DP 157456, IFO 15269 with 157457 and NBRC
    15269 with 335614. The GCA_003201835 sequence belongs explicitly to DSM 1651;
    D26489 explicitly names DSM and IFO deposits. The JCM sequence AB304843 is not
    transferred because JCM 8954 is absent from the BacDive deposit set. SI-ID 48152.2/SI-DP
    159955 supplies DSM 6334 context and no sequence. GOLD Go0032875 → Gp0376662 →
    Ga0485363 supports GCA_003201835.2/IMG 2927569001/SAMN09071529. GTDB RS_GCF_003201835.2
    and NCBI GCA/GCF versions retain their distinct provenance. BV-BRC 41673.4 supplies
    historical GCA_003201835.1 with source status Deprecated, whereas 41673.10 supplies
    .2; the record does not claim every source assertion is current. All four imported
    nucleotide accessions resolve to NCBI taxon 41673. Exact comparisons found 12
    assembly, nine genome-record and 39 related assertions for 16640, plus two related
    assertions and no assemblies/genomes for 16641, equal to the inputs.
  target_ids:
  - NCBITaxon:41673
  evidence_ids:
  - record
  - bacdive-inventory
  - culture-inventory
  - primary-source-1
  - primary-source-2
  - primary-source-3
  - primary-source-4
  - primary-source-5
  - assembly-inputs
  - genome-inputs
  - related-inputs
  - straininfo-deposits
  - straininfo-assemblies
  - straininfo-related
  - atb-links
  - cafi-registry
  - nucleotide-authority
  - genome-catalog-1
  - genome-catalog-2
  - genome-catalog-4
  - genome-catalog-5
  dimensions:
  - name: deposit-boundary
    value: CAFI whole authority and full accession; StrainInfo own SI-DP; GOLD organism→project→analysis
    definition: Independent identity boundaries used to inspect each source assertion;
      no taxonomy/name-only joins.
    evidence_ids:
    - cafi-registry
    - straininfo-deposits
    - assembly-inputs
- assessment_id: taxonomy-mapping
  area: grounding
  topic: GTDB mapping scope and source genome count
  outcome: supported
  summary: GTDB RS_GCF_003201835.2 has ncbi_taxid 41673, DSM 1651 and species Aramenus
    brierleyi. The sole raw mapping is closeMatch to NCBITaxon:41673. This supplies
    the documented species normalization boundary, while the independent biological
    equivalence of the NCBI and GTDB species circumscriptions has not been re-estimated
    from sequence data.
  target_ids:
  - NCBITaxon:41673
  evidence_ids:
  - record
  - gtdb-mappings
  - gtdb-species
  - mapping-policy
  - equivalence-contract
  - seed-owner
  - genome-catalog-1
  dimensions:
  - name: gtdb-release
    value: RS232
    definition: GTDB metadata release recorded in the pinned native catalog manifest;
      not NCBI taxon rank.
    evidence_ids:
    - genome-catalog-manifest
    - genome-catalog-1
- assessment_id: native-status
  area: provenance
  topic: Seed event and scientific status boundary
  outcome: supported
  summary: The NCBI identity is grounded EXACT and the record remains SEEDED. Its
    single seed event is consistent with the latest extraction timestamp across raw,
    ATB and StrainInfo manifests (2026-09-13T17:54:04Z). This review neither appends
    history nor promotes native status.
  target_ids:
  - NCBITaxon:41673
  evidence_ids:
  - record
  - manifest
  - overlay-manifests
findings: []
actions:
- action_id: verify-pinned-aggregate-edges
  description: Recover the upstream kg-microbe edge snapshots whose SHA-256 values
    are pinned in data/raw/MANIFEST.yaml, then recount this exact target using the
    maintained extractor's source-specific counting rules. This resolves the historical-count
    limitation without changing generated records.
  finding_ids: []
  target_ids:
  - NCBITaxon:41673
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: data/raw/MANIFEST.yaml
    role: Exact historical input identifiers and hashes
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: MediaDive, GOLD and trait assertion counting rules
  acceptance_checks:
  - Recovered edge files match the manifest SHA-256 values before any comparison.
  - Recount only the target's explicit MediaDive METPO:2000517 medium set, GOLD Go
    subclass assertions and Madin taxon-subject assertions that this record actually
    attests; preserve their distinct units and direct-taxon boundaries.
  - Compare the resulting counts and medium identifiers with the exact inventoried
    rows cited in this review, and retain any discrepancy as a new observation.
limitations:
- This review is limited to the entire generated record and the specified source evidence.
  It does not independently re-estimate phylogenetic species boundaries or establish
  experimental mechanisms from database annotations.
- The NCBI taxonomy snapshot is dated 2026-09-13. Current authority checks are distinguished
  from pinned source assertions; source coverage and zero imported strains are not
  worldwide absence claims.
- Historical source counts match the committed inventories, but the locally configured
  kg-microbe MediaDive, GOLD and Madin edge files have hashes different from data/raw/MANIFEST.yaml.
  They cannot reproduce the original counts. Required historical edge verification
  is unavailable; completion remains partial.
- Publication identifiers were checked against LPSN and DOI registration metadata;
  original paper full text was not reassessed. Nucleotide descriptions were checked
  at NCBI. An iModulonDB structured runner was unavailable in the checked environment;
  source pages supplied no usable dataset coverage, so no expression-module or experimental-mechanism
  inference was made.
notes:
- No generated record, page or curation history was edited. Findings and actions are
  proposed work, not completed fixes or native scientific-status promotion.
- The initial just qc attempt failed because ruff was absent. The locked ruff 0.16.7
  dependency was installed only in this isolated environment, and the complete command
  was retried; the final retry result is recorded above.
- The initial whole-corpus listing found 52 existing actual record targets among 625,960
  corpus records. Historical TSV inventories are not substituted for one-record structured
  bundles.
tags:
- record-review
- batch-0001
- archaea
- generated
- source-checked
```
