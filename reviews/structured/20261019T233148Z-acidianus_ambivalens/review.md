# Record review: Acidianus ambivalens

- Review: 20261019T233148Z-acidianus_ambivalens
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-19T07:18:40Z
- Finished UTC: 2026-10-19T23:31:48Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The full Acidianus ambivalens record has consistent NCBI identity, LPSN nomenclature and one imported BacDive strain. Deposit-specific genome assertions reproduce the inventories and inspected primary catalog rows. No record-specific defect was established; historical aggregate source counts remain only inventory-verified.

## Scope And Provenance

The entire single resolved generated TaxonRecord and its identity, nomenclature, mapping, strain, source-count and provenance assertions.

Selection: First ten unreviewed corpus paths in lexicographic order at base 9b5a8fff5185b38dc5c77bb35235152c81ea7765; this is record 3. Reviewed means an actual target of a validated bundle from scripts/record_review.py list. Inventory coverage alone does not count.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9b5a8fff5185b38dc5c77bb35235152c81ea7765.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:2283 | data/taxa/archaea/acidianus_ambivalens.yaml | generated | Acidianus ambivalens |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact NCBI taxon, rank and lineage | passed | True | NCBITaxon:2283 | NCBITaxon:2283 is the species Acidianus ambivalens, below genus 12914, with nine carried ancestors and genetic code 11. Pinned and current NCBI taxonomy agree on this identity. The older Desulfurolobus and Sulfolobus names are source-scoped synonyms, not separate imported organisms. |
| Deposit-specific source assertions and reference resolution | passed | True | NCBITaxon:2283 | BacDive 16643 supplies direct unversioned GCA_009428885/GCA_009729015, PATRIC 2283.10/2283.11 and IMG assertions. GTDB and current NCBI culture joins support DSM 3772 for GCA/GCF_009428885.1; the separate LEI 10 genome is not transferred by a guessed deposit alias. GOLD Go0029281 → Gp0548891 → Ga0491101 supports GCA_009729015.1/IMG 8065311606, while Go0576457 → Gp0551223 → Ga0488881 supports GCA_009428885.1/IMG 8065314359. Each chain preserves its BioSample and project. StrainInfo SI-ID 47758.3 joins DSM 3772 through SI-DP 158532 and JCM 9191 through SI-DP 184904; the 18 nucleotide associations resolve in NCBI to taxon 2283. CIP 104912 is nomenclatural/source context, not an invented BacDive deposit join. Exact multiset comparison found all 12 assembly, 10 genome-record and 49 related-record assertions equal to their raw/StrainInfo inputs, including source IDs and evidence fields. |
| Structured expression-module adapter | unavailable | False | NCBITaxon:2283 | No installed kg-microbe-sources runner was found. The checked local claw directory contained no project and wizard-claw did not expose this runner. The inspected iModulonDB page supplied no usable dataset text. Gene names here are sequence-description context; no expression-module or mechanism conclusion was inferred. |
| Original aggregate source-edge multiplicities | unavailable | True | NCBITaxon:2283 | Inventories support the record's counts, but the original manifest-pinned MediaDive/GOLD/Madin edge bytes were unavailable in the checked locations; current external files have different hashes. No recount of current data can validate the historical numbers. |
| Initial quality-gate setup attempt | failed | False | NCBITaxon:2283 | Exit 1: missing ruff dependency; environment repaired before the separately recorded full retry. |
| Native strict record validation | passed | True | NCBITaxon:2283 | Actual terminal exit code 0. This exact generated YAML only. |
| Repository history validation | passed | True | NCBITaxon:2283 | Actual terminal exit code 0. All 17 committed standalone history records; generated seed history also inspected in this target. |
| Full-corpus exact reproduction | passed | True | NCBITaxon:2283 | Actual terminal exit code 0. All 625,960 generated taxon YAMLs, not a focused approximation. |
| Native product ID/label gate | passed | True | NCBITaxon:2283 | Actual terminal exit code 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. |
| Authoritative complete quality gate | passed | True | NCBITaxon:2283 | Actual terminal exit code 0. Repository-wide just qc on the isolated checkout; includes corpus-wide checks. Pytest reported 1055 passed, 3 skipped and 5 deselected; the native QC recipe completed successfully. |

## Scientific And Domain Assessments

### Resolved biological taxon and carried lineage

identity: supported. Targets: NCBITaxon:2283.

NCBITaxon:2283 is the species Acidianus ambivalens, below genus 12914, with nine carried ancestors and genetic code 11. Pinned and current NCBI taxonomy agree on this identity. The older Desulfurolobus and Sulfolobus names are source-scoped synonyms, not separate imported organisms.

### Source-scoped names and nomenclatural standing

nomenclature: supported. Targets: NCBITaxon:2283.

LPSN 772572 is the correct, validly published ICNP name; 775729 is its retained deprecated homotypic name Desulfurolobus ambivalens. Authorities, DSM 3772/JCM 9191/CIP 104912 type designations and the two 1996 publication DOIs match the inspected LPSN entries and DOI registration metadata. The GTDB species has an explicit LPSN bridge, and two catalog genomes support its cluster count. NCBI lineage remains separate from GTDB classification.

### Complete imported subtree and source assertion units

completeness: supported. Targets: NCBITaxon:2283.

One BacDive strain (16643) is imported, with DSM 3772, JCM 9191 and the unsupported join alias LEI 10 preserved. The BacDive subtree inventory contains no additional classified strain. The record's seven attestations retain their distinct NAME, GENOME, STRAIN, MEDIUM, ORGANISM and TRAIT_ASSERTION units. The counts in the raw inventories match the record; historical MediaDive/GOLD/Madin edge multiplicity could not be independently reproduced from the pinned upstream bytes.

### Deposit authority, source chains and exact accessions

evidence: supported. Targets: NCBITaxon:2283.

BacDive 16643 supplies direct unversioned GCA_009428885/GCA_009729015, PATRIC 2283.10/2283.11 and IMG assertions. GTDB and current NCBI culture joins support DSM 3772 for GCA/GCF_009428885.1; the separate LEI 10 genome is not transferred by a guessed deposit alias. GOLD Go0029281 → Gp0548891 → Ga0491101 supports GCA_009729015.1/IMG 8065311606, while Go0576457 → Gp0551223 → Ga0488881 supports GCA_009428885.1/IMG 8065314359. Each chain preserves its BioSample and project. StrainInfo SI-ID 47758.3 joins DSM 3772 through SI-DP 158532 and JCM 9191 through SI-DP 184904; the 18 nucleotide associations resolve in NCBI to taxon 2283. CIP 104912 is nomenclatural/source context, not an invented BacDive deposit join. Exact multiset comparison found all 12 assembly, 10 genome-record and 49 related-record assertions equal to their raw/StrainInfo inputs, including source IDs and evidence fields.

### GTDB mapping scope and source genome count

grounding: supported. Targets: NCBITaxon:2283.

The pinned GTDB cluster contains RS_GCF_009428885.1 (DSM 3772) and RS_GCF_009729015.1 (LEI 10). Count 2 is the cluster's genome count; it does not collapse assembly identifiers or turn both rows into one deposit assertion. The LPSN name explicitly links GTDB:s__Acidianus_ambivalens.

### Seed event and scientific status boundary

provenance: supported. Targets: NCBITaxon:2283.

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
| record | data/taxa/archaea/acidianus_ambivalens.yaml; entire TaxonRecord; identifier=NCBITaxon:2283 | supports | Read the entire generated YAML, including identity, all synonyms, mappings, source attestations, every strain assertion and seed history. |
| taxonomy-inventory | data/raw/ncbitaxon_taxa.tsv; line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""}; line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"}; line 1798: {"taxon_id":"NCBITaxon:2281","label":"Sulfolobales","rank":"ORDER","parent_id":"NCBITaxon:183924"}; line 1799: {"taxon_id":"NCBITaxon:2283","label":"Acidianus ambivalens","rank":"SPECIES","parent_id":"NCBITaxon:12914","genetic_code":"11","exact_synonyms":"Desulfurolobus ambivalens&#124;Sulfolobus ambivalens","related_synonyms":"Acidianus ambivalens (Zillig and Bock 1987) Fuchs et al. 1996&#124;Desulfurolobus ambivalens Zillig and Bock 1987","broad_synonyms":"","attested_by":"ncbitaxon&#124;gtdb&#124;bacdive&#124;lpsn&#124;mediadive&#124;gold&#124;madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"}; line 2648: {"taxon_id":"NCBITaxon:12914","label":"Acidianus","rank":"GENUS","parent_id":"NCBITaxon:118883"}; line 2980: {"taxon_id":"NCBITaxon:28889","label":"Thermoproteota","rank":"PHYLUM","parent_id":"NCBITaxon:1783275"}; line 22254: {"taxon_id":"NCBITaxon:118883","label":"Sulfolobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2281"}; line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"}; line 36612: {"taxon_id":"NCBITaxon:183924","label":"Thermoprotei","rank":"CLASS","parent_id":"NCBITaxon:28889"}; line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"} | supports | Inspected the exact target row and every carried ancestor. Rank, label, parent, genetic code and typed source names were compared with the complete record. |
| scope-row | curation/seed_scope.tsv; line 5586: {"identifier":"NCBITaxon:2283","added":"2026-09-12","reason":"attested rule: Acidianus ambivalens, 7 sources incl. NCBI"} | supports | The exact target is explicitly included in the seed scope. |
| path-row | data/taxa/PATHS.tsv; line 336041: {"identifier":"NCBITaxon:2283","slug":"acidianus_ambivalens"} | supports | The indexed path resolves to the same NCBI taxon and generated target. |
| ncbi-live | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=2283; TaxaSet/Taxon[TaxId='2283']; captured together with the other nine explicitly selected batch taxa | supports | Inspected the official current taxonomy response for this exact taxon: scientific name, rank, parent, source name classes, lineage identifiers and genetic code. Compared it with the separately pinned September taxonomy. |
| lpsn-inventory | data/raw/lpsn_names.tsv; line 14847: {"lpsn_id":"lpsn:772572","name":"Acidianus ambivalens","rank":"SPECIES","authority":"(Zillig and Böck 1987) Fuchs et al. 1996","url":"https://lpsn.dsmz.de/species/acidianus-ambivalens","deprecated":"0","status":"legitimate=True; validly published under the ICNP; correct name","validly_published":"1","legitimate":"1","is_correct_name":"1","parent_lpsn_id":"lpsn:516964","ncbitaxon_ids":"NCBITaxon:2283","gtdb_ids":"GTDB:s__Acidianus_ambivalens","type_strain_ids":"kgmicrobe.strain:CIP-104912&#124;kgmicrobe.strain:DSM-3772&#124;kgmicrobe.strain:JCM-9191","synonym_of":"lpsn:775729","synonyms":"lpsn:775729","publications":"doi:10.1016/s0723-2020(96)80009-9&#124;doi:10.1099/00207713-46-3-836","sequence_accessions":"INSDC:D85506"}; line 16814: {"lpsn_id":"lpsn:775729","name":"Desulfurolobus ambivalens","rank":"SPECIES","authority":"Zillig and Böck 1987","url":"https://lpsn.dsmz.de/species/desulfurolobus-ambivalens","deprecated":"1","status":"legitimate=True; validly published under the ICNP; synonym","validly_published":"1","legitimate":"1","is_correct_name":"0","parent_lpsn_id":"lpsn:517031","ncbitaxon_ids":"","gtdb_ids":"","type_strain_ids":"kgmicrobe.strain:CIP-104912&#124;kgmicrobe.strain:DSM-3772&#124;kgmicrobe.strain:JCM-9191","synonym_of":"lpsn:772572","synonyms":"lpsn:772572","publications":"doi:10.1016/s0723-2020(86)80077-7&#124;doi:10.1099/00207713-37-2-179","sequence_accessions":"INSDC:D85506"} | supports | Inspected all exact taxon/name mappings and linked synonymous LPSN names, retaining statuses and type-designation scope. |
| gtdb-mappings | data/raw/gtdb_mappings.tsv; line 180405: {"gtdb_id":"GTDB:s__Acidianus_ambivalens","gtdb_label":"s__Acidianus_ambivalens","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:2283","predicate":"skos:closeMatch","genome_count":"2"} | supports | Inspected this taxon's GTDB mappings and every reverse mapping of the same selected source cluster; predicates and counts remain source-scoped. |
| gtdb-species | data/raw/gtdb_species.tsv; line 3492: {"gtdb_id":"GTDB:s__Acidianus_ambivalens","label":"s__Acidianus_ambivalens","parent":"GTDB:g__Acidianus","genome_count":"2"} | supports | Inspected source species identifiers, labels, parent cluster and genome counts. |
| bacdive-inventory | data/raw/bacdive_strains.tsv; line 16462: {"strain_id":"kgmicrobe.strain:bacdive_16643","bacdive_id":"16643","designation":"","taxon_ids":"NCBITaxon:2283","lpsn_ids":"lpsn:772572","culture_collection_ids":"kgmicrobe.strain:DSM-3772&#124;kgmicrobe.strain:JCM-9191&#124;kgmicrobe.strain:LEI%2010","medium_count":"0"} | supports | Full BacDive inventory selection used the exact taxon plus every descendant from the complete NCBI parent graph. Deposits, type status and classified_as remain separate from taxon identity. |
| culture-inventory | data/raw/culture_collection_strains.tsv; line 77146: {"strain_id":"kgmicrobe.strain:DSM-3772","taxon_ids":"NCBITaxon:2283"}; line 112665: {"strain_id":"kgmicrobe.strain:JCM-9191","taxon_ids":"NCBITaxon:2283"}; line 123135: {"strain_id":"kgmicrobe.strain:LEI%2010","taxon_ids":"NCBITaxon:2283"} | supports | Inspected exact culture identifiers associated with the target; source aliases do not independently authorize genome joins. |
| gold-organisms | data/raw/gold_organisms.tsv; line 21428: {"taxon_id":"NCBITaxon:2283","organism_count":"4"} | supports | Inspected the exact GOLD organism count row, or its bounded absence, without converting counts to phenotypes. |
| mediadive-taxa | data/raw/mediadive_taxa.tsv; line 6951: {"taxon_id":"NCBITaxon:2283","medium_count":"3","media_ids":"mediadive.medium:358a&#124;mediadive.medium:J185&#124;mediadive.medium:J186"} | supports | Inspected the exact MediaDive medium count row, or its bounded absence, without converting counts to phenotypes. |
| madin-taxa | data/raw/madin_taxa.tsv; line 19682: {"taxon_id":"NCBITaxon:2283","assertion_count":"5"} | supports | Inspected the exact Madin trait-assertion count row, or its bounded absence, without converting counts to phenotypes. |
| bactotraits-taxa | data/raw/bactotraits_taxa.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Inspected the exact BactoTraits trait-assertion count row, or its bounded absence, without converting counts to phenotypes. |
| mapping-policy | docs/HARMONIZATION.md; Mapping predicates and Scope and lineage sections | supports | The local mapping policy permits one-to-one species closeMatch mappings and LPSN-linked species to supply xrefs/synonyms, retains pooled broadMatch entries separately, and carries NCBI lineage unchanged. |
| equivalence-contract | src/taxonmech/schema/taxonmech.yaml; TaxonRecord.xrefs (lines 180–187); TaxonomyMapping (lines 417–439) | supports | TaxonRecord.xrefs denotes true equivalence, while broader/narrower relationships belong in taxonomy_mappings; TaxonomyMapping.genome_count counts genomes under the source taxon. |
| seed-owner | src/taxonmech/seed.py; GTDB mapping construction and identity promotion, lines 440–472 | supports | The identity branch accepts an LPSN GTDB bridge or any skos:closeMatch, then emits an equivalent xref and, if the text differs, an EXACT_SYNONYM. It does not guard against a strain-rank target. |
| manifest | data/raw/MANIFEST.yaml; kg_microbe_source, inputs, extracted_at | supports | The source manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd and hashes individual upstream inputs; extraction time is 2026-09-13T17:50:44Z. |
| overlay-manifests | data/atb/MANIFEST.yaml; extracted_at, together with data/straininfo/MANIFEST.yaml | supports | Compared raw, ATB and StrainInfo extraction timestamps. Their maximum, 2026-09-13T17:54:04Z, matches the sole generated seed event. The StrainInfo manifest is separately captured in source.inputs. |
| primary-source-1 | data/bacdive/records.jsonl.gz; decompressed JSONL lines 16461 | supports | Inspected complete selected source objects, including identifier/deposit fields and explicit source relationships. Source grouping and taxonomic similarity do not transfer sequence assertions across deposits. |
| primary-source-2 | data/straininfo/records.jsonl.gz; decompressed JSONL lines 35670 | supports | Inspected complete selected source objects, including identifier/deposit fields and explicit source relationships. Source grouping and taxonomic similarity do not transfer sequence assertions across deposits. |
| primary-source-3 | data/gold/organisms.jsonl.gz; decompressed JSONL lines 24887, 411927, 449279 | supports | Inspected complete selected source objects, including identifier/deposit fields and explicit source relationships. These are organism/project/analysis records, not interchangeable genome identifiers. |
| primary-source-4 | data/gold/projects.jsonl.gz; decompressed JSONL lines 402657, 404988 | supports | Inspected complete selected source objects, including identifier/deposit fields and explicit source relationships. These are organism/project/analysis records, not interchangeable genome identifiers. |
| primary-source-5 | data/gold/analyses.jsonl.gz; decompressed JSONL lines 316269, 318460 | supports | Inspected complete selected source objects, including identifier/deposit fields and explicit source relationships. These are organism/project/analysis records, not interchangeable genome identifiers. |
| assembly-inputs | data/raw/strain_assemblies.tsv; selected data lines 81977, 81978, 81979, 81980, 81981, 81982, 81983, 81984, 81985, 81986, 81987 | supports | Inspected every matching source row and compared all assertion fields with this record; accessions and source evidence remain distinct. |
| genome-inputs | data/raw/strain_genome_records.tsv; selected data lines 64210, 64211, 64212, 64213, 64214, 64215, 64216, 64217, 64218, 64219 | supports | Inspected every matching source row and compared all assertion fields with this record; accessions and source evidence remain distinct. |
| related-inputs | data/raw/strain_related_records.tsv; selected data lines 249181, 249182, 249183, 249184, 249185, 249186, 249187, 249188, 249189, 249190, 249191, 249192, 249193, 249194, 249195, 249196, 249197, 249198, 249199, 249200, 249201, 249202, 249203, 249204, 249205, 249206, 249207 | supports | Inspected every matching source row and compared all assertion fields with this record; accessions and source evidence remain distinct. |
| straininfo-deposits | data/straininfo/strain_links.tsv; selected data lines 68791, 68792 | supports | Inspected every matching source row and compared all assertion fields with this record; accessions and source evidence remain distinct. |
| straininfo-assemblies | data/straininfo/assemblies.tsv; selected data lines 5953 | supports | Inspected every matching source row and compared all assertion fields with this record; accessions and source evidence remain distinct. |
| straininfo-related | data/straininfo/related_records.tsv.gz; selected data lines 162531, 162532, 162533, 162534, 162535, 162536, 162537, 162538, 162539, 162540, 162541, 162542, 162543, 162544, 162545, 162546, 162547, 162548, 162549, 162550, 162551, 162552 | supports | Inspected every matching source row and compared all assertion fields with this record; accessions and source evidence remain distinct. |
| atb-links | data/atb/strain_links.tsv; complete table; exact target/subtree/source-identifier search had no matching row | supports | Inspected every matching source row and compared all assertion fields with this record; accessions and source evidence remain distinct. |
| cafi-registry | src/taxonmech/data/cafi_acronyms.json; authority entries for the record's deposit prefixes and their regex_id.full templates | supports | The pinned collection registry governs full deposit accession matching. DSM, IFO, JCM and NBRC identifiers retain their own authorities; bare aliases and nonmatching formats do not supply inferred joins. |
| nucleotide-authority | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&amp;retmode=json&amp;id=AB304842.1,AJ249983.1,AJ320523.1,AJ489504.1,D85506.1,FN999991.1,FN999992.1,FR734215.1,FR734216.1,X56616.3,X63438.1,X64202.1,X90484.1,X95989.1,Y08729.1,Y08730.1,Y08735.1,Y09614.1; AB304842.1: Acidianus ambivalens gene for Cbf5, partial cds; AJ249983.1: Acidianus ambivalens partial rubA gene for rubrerythrin; AJ320523.1: Acidianus ambivalens partial ORF1, sdhF gene, sdhE gene, sdhB gene, ORF2, tatC gene, tatB gene, tatA gene, hydS gene, isp1 gene, isp2 gene, hydL gene, hyd1 gene, hyd2 gene, hypD gene, hypC gene, hypD gene, hyp1 gene, hyp2 gene, hoxM gene and nanT gene; AJ489504.1: Acidianus ambivalens noxA gene for NADH oxidase; D85506.1: Acidianus ambivalens 16S rRNA gene, almost full-length sequence; FN999991.1: Acidianus ambivalens ORF1 (partial), aorA, aorD, aorE, ORF2, odc and aspB (partial) genes, strain DSM3772; FN999992.1: Acidianus ambivalens cobA gene (partial), troR, aorB, aorC, mobA, ORF1, coxG, coxG2 and tuF genes, strain DSM3772; FR734215.1: Acidianus ambivalens tth1 gene for tetrathionate hydrolase, strain DSM 3772; FR734216.1: Acidianus ambivalens trpB gene (partial), tth2 gene and treY gene (partial), strain DSM 3772; X56616.3: Desulfurolobus ambivalens tnpA, tnpB, rfbD and sor genes and ORF2, ORF3, ORF4 and ORF5; X63438.1: D.ambivalens lig gene for DNA ligase; X64202.1: D.ambivalens gene bps2; X90484.1: D.ambivalens DNA for 16S ribosomal RNA gene; X95989.1: D.ambivalens ORF1 and ORF2, sra &amp; secE genes; Y08729.1: A.ambivalens doxB gene locus with doxB, doxC, doxE, and doxF genes; Y08730.1: A.ambivalens doxA gene locus with doxD and doxA genes; Y08735.1: Acidianus ambivalens ffh gene; Y09614.1: A.ambivalens doxD gene, second doxA gene locus, orf2 and orf3 | supports | All 18 imported nucleotide references resolve to NCBI taxon 2283. The accession versions returned by the current authority are recorded for resolution only; unversioned source assertions are not rewritten. Checked accession, taxid and sequence title for each entry. |
| genome-catalog-manifest | data/catalog/MANIFEST.json; coverage.sources[name=GTDB] | supports | The complete native GTDB genome catalog is the RS232 snapshot. Species clusters and MAGs remain distinct from physical strain deposits. |
| genome-catalog-1 | data/catalog/gtdb_genomes-0017.jsonl.gz; line 44803: {"accession":"RS_GCF_009729015.1","ncbi_taxid":"2283","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus ambivalens","ncbi_strain_identifiers":"LEI 10"}; line 49626: {"accession":"RS_GCF_009428885.1","ncbi_taxid":"2283","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus ambivalens","ncbi_strain_identifiers":"DSM 3772"} | supports | Inspected the complete selected genome catalog rows. Source genome identity, taxonomic assignment, deposit fields and accession versions were assessed separately. |
| genome-catalog-2 | data/catalog/ncbi_genbank-0008.jsonl.gz; line 15543: {"assembly_accession":"GCA_009428885.1","taxid":"2283","infraspecific_name":"strain=DSM 3772"}; line 29342: {"assembly_accession":"GCA_009729015.1","taxid":"2283","infraspecific_name":"strain=LEI 10"} | supports | Inspected the complete selected genome catalog rows. Source genome identity, taxonomic assignment, deposit fields and accession versions were assessed separately. |
| genome-catalog-3 | data/catalog/ncbi_refseq-0002.jsonl.gz; line 33554: {"assembly_accession":"GCF_009428885.1","taxid":"2283","infraspecific_name":"strain=DSM 3772"}; line 35738: {"assembly_accession":"GCF_009729015.1","taxid":"2283","infraspecific_name":"strain=LEI 10"} | supports | Inspected the complete selected genome catalog rows. Source genome identity, taxonomic assignment, deposit fields and accession versions were assessed separately. |
| genome-catalog-4 | data/bvbrc/bvbrc-0013.jsonl.gz; line 30551: {"assembly_accession":"GCA_009428885.1","genome_id":"2283.10","taxon_id":2283,"genome_name":"Acidianus ambivalens strain DSM 3772","genome_status":"WGS"}; line 30552: {"assembly_accession":"GCA_009729015.1","genome_id":"2283.11","taxon_id":2283,"genome_name":"Acidianus ambivalens strain LEI 10","genome_status":"Complete"} | supports | Inspected the complete selected genome catalog rows. Source genome identity, taxonomic assignment, deposit fields and accession versions were assessed separately. |
| lpsn-live | https://lpsn.dsmz.de/species/acidianus-ambivalens; Name; category; nomenclatural/taxonomic status; type designations; synonyms and cited publication metadata | supports | Inspected the authority's name, category, nomenclatural and taxonomic status, type designations, synonyms and cited publication identity. These fields were compared with the pinned inventory rather than substituted into the record. |
| doi-ambivalens1996 | https://doi.org/10.1016/s0723-2020(96)80009-9; 16S rDNA-based Phylogeny of the Archaeal Order Sulfolobales and Reclassification of Desulfurolobus ambivalens as Acidianus ambivalens comb. nov.; pages 56-60 | supports | Crossref registration confirms the cited publication identity, date and bibliographic pagination; this is metadata verification, not a review of the paper's experimental evidence. |
| doi-validation1996 | https://doi.org/10.1099/00207713-46-3-836; Validation of the Publication of New Names and New Combinations Previously Effectively Published Outside the IJSB: List No. 58; pages 836-837 | supports | Crossref registration confirms the cited publication identity, date and bibliographic pagination; this is metadata verification, not a review of the paper's experimental evidence. |
| historical-edge-availability | data/raw/MANIFEST.yaml; data/transformed/mediadive/edges.tsv: expected=78ea275a59d4e2de09a9cf72652ec64454c6a111d2defa1ae0a44bac8a72e523, present=4e933d1e2412fb1aad74e60719a6a64dfa34862ff0a6b84e93d78da5ce13dd8b; data/transformed/gold/edges.tsv: expected=b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12, present=6b3375a06d4dabc86fdcb14a48cea55b86a7003634ba1d3ee449bcac32b89f9d; data/transformed/madin_etal/edges.tsv: expected=3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f, present=c19bfc848e1b410548614c54a2b99e2c58452d58aeb61f972c99fcb3039a1d24 | partial | The exact configured external paths were checked including ignored files. They exist, but each current SHA-256 differs from the manifest-pinned snapshot; none was treated as the original extraction input. |
| qc-setup-receipt | just qc; initial setup attempt, 2026-10-19T07:17:01Z through 2026-10-19T07:17:01Z | context_only | Initial actual invocation exited 1 because the isolated environment lacked ruff. Locked ruff 0.16.7 was then installed in that environment and the full command retried; qc below records the retry result. |
| strict-receipt | just validate-strict data/taxa/archaea/acidianus_ambivalens.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/strict-03.tsv; This exact generated YAML only. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo; started 2026-10-19T07:18:41Z, finished 2026-10-19T07:18:44Z, exit 0.<br>Validating 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/strict-03.tsv |
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
review_id: 20261019T233148Z-acidianus_ambivalens
kind: record
repository: CultureBotAI/TaxonMech
title: 'Record review: Acidianus ambivalens'
started_at: '2026-10-19T07:18:40Z'
finished_at: '2026-10-19T23:31:48Z'
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
summary: The full Acidianus ambivalens record has consistent NCBI identity, LPSN nomenclature
  and one imported BacDive strain. Deposit-specific genome assertions reproduce the
  inventories and inspected primary catalog rows. No record-specific defect was established;
  historical aggregate source counts remain only inventory-verified.
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
  - path: conf/straininfo.yaml
    sha256: 2b5a46e2d39e235f3353089b8728862dc1feea40489a64bd89bc9ae374f4cafd
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
  - path: data/bvbrc/bvbrc-0013.jsonl.gz
    sha256: ba814e4c647d96e5d00512c336e83a6fd2448549c7f9ef46cc8fd59e1790235b
    role: context
  - path: data/catalog/MANIFEST.json
    sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
    role: context
  - path: data/catalog/gtdb_genomes-0017.jsonl.gz
    sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
    role: context
  - path: data/catalog/ncbi_genbank-0008.jsonl.gz
    sha256: 6b31a395d770af741d40a6832c0d74026c4c82f5b95216023df867e3cdebd764
    role: context
  - path: data/catalog/ncbi_refseq-0002.jsonl.gz
    sha256: f22a85bd89937e6e2a8c7774d699102bcbf26a31af296a6cc77976d5f2a40f72
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
  - path: data/taxa/archaea/acidianus_ambivalens.yaml
    sha256: e7ba7690b3523dd664794dc426a935383c9a3eb6e69a43f9a00ca5bdbf51676b
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
    this is record 3. Reviewed means an actual target of a validated bundle from scripts/record_review.py
    list. Inventory coverage alone does not count.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - NCBITaxon:2283
targets:
- target_id: NCBITaxon:2283
  path: data/taxa/archaea/acidianus_ambivalens.yaml
  label: Acidianus ambivalens
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
  summary: NCBITaxon:2283 is the species Acidianus ambivalens, below genus 12914,
    with nine carried ancestors and genetic code 11. Pinned and current NCBI taxonomy
    agree on this identity. The older Desulfurolobus and Sulfolobus names are source-scoped
    synonyms, not separate imported organisms.
  target_ids:
  - NCBITaxon:2283
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
  summary: BacDive 16643 supplies direct unversioned GCA_009428885/GCA_009729015,
    PATRIC 2283.10/2283.11 and IMG assertions. GTDB and current NCBI culture joins
    support DSM 3772 for GCA/GCF_009428885.1; the separate LEI 10 genome is not transferred
    by a guessed deposit alias. GOLD Go0029281 → Gp0548891 → Ga0491101 supports GCA_009729015.1/IMG
    8065311606, while Go0576457 → Gp0551223 → Ga0488881 supports GCA_009428885.1/IMG
    8065314359. Each chain preserves its BioSample and project. StrainInfo SI-ID 47758.3
    joins DSM 3772 through SI-DP 158532 and JCM 9191 through SI-DP 184904; the 18
    nucleotide associations resolve in NCBI to taxon 2283. CIP 104912 is nomenclatural/source
    context, not an invented BacDive deposit join. Exact multiset comparison found
    all 12 assembly, 10 genome-record and 49 related-record assertions equal to their
    raw/StrainInfo inputs, including source IDs and evidence fields.
  target_ids:
  - NCBITaxon:2283
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
  - NCBITaxon:2283
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
  - NCBITaxon:2283
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
  - NCBITaxon:2283
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
  - NCBITaxon:2283
  evidence_ids:
  - strict-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/uv-cache
    just validate-strict data/taxa/archaea/acidianus_ambivalens.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/strict-03.tsv
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
  - NCBITaxon:2283
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
  - NCBITaxon:2283
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
  - NCBITaxon:2283
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
  - NCBITaxon:2283
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
  reference: data/taxa/archaea/acidianus_ambivalens.yaml
  accessed_at: '2026-10-19T23:31:48Z'
  support: supports
  summary: Read the entire generated YAML, including identity, all synonyms, mappings,
    source attestations, every strain assertion and seed history.
  locator: entire TaxonRecord; identifier=NCBITaxon:2283
  snapshot_sha256: e7ba7690b3523dd664794dc426a935383c9a3eb6e69a43f9a00ca5bdbf51676b
- evidence_id: taxonomy-inventory
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: Inspected the exact target row and every carried ancestor. Rank, label,
    parent, genetic code and typed source names were compared with the complete record.
  locator: 'line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""};
    line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"};
    line 1798: {"taxon_id":"NCBITaxon:2281","label":"Sulfolobales","rank":"ORDER","parent_id":"NCBITaxon:183924"};
    line 1799: {"taxon_id":"NCBITaxon:2283","label":"Acidianus ambivalens","rank":"SPECIES","parent_id":"NCBITaxon:12914","genetic_code":"11","exact_synonyms":"Desulfurolobus
    ambivalens|Sulfolobus ambivalens","related_synonyms":"Acidianus ambivalens (Zillig
    and Bock 1987) Fuchs et al. 1996|Desulfurolobus ambivalens Zillig and Bock 1987","broad_synonyms":"","attested_by":"ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"};
    line 2648: {"taxon_id":"NCBITaxon:12914","label":"Acidianus","rank":"GENUS","parent_id":"NCBITaxon:118883"};
    line 2980: {"taxon_id":"NCBITaxon:28889","label":"Thermoproteota","rank":"PHYLUM","parent_id":"NCBITaxon:1783275"};
    line 22254: {"taxon_id":"NCBITaxon:118883","label":"Sulfolobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2281"};
    line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"};
    line 36612: {"taxon_id":"NCBITaxon:183924","label":"Thermoprotei","rank":"CLASS","parent_id":"NCBITaxon:28889"};
    line 464838: {"taxon_id":"NCBITaxon:1783275","label":"Thermoproteati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
- evidence_id: scope-row
  kind: database
  reference: curation/seed_scope.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: The exact target is explicitly included in the seed scope.
  locator: 'line 5586: {"identifier":"NCBITaxon:2283","added":"2026-09-12","reason":"attested
    rule: Acidianus ambivalens, 7 sources incl. NCBI"}'
  snapshot_sha256: 5fdc0f7111b64e02439d95c6f2b51fcff1d2154c34b2d957422dd9b297e94d4b
- evidence_id: path-row
  kind: database
  reference: data/taxa/PATHS.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: The indexed path resolves to the same NCBI taxon and generated target.
  locator: 'line 336041: {"identifier":"NCBITaxon:2283","slug":"acidianus_ambivalens"}'
  snapshot_sha256: c950844feb0638ce04f7349784749dd1d728fe70bc80f7e2756d956d4ecea254
- evidence_id: ncbi-live
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=2283
  accessed_at: '2026-10-19T07:21:19Z'
  support: supports
  summary: 'Inspected the official current taxonomy response for this exact taxon:
    scientific name, rank, parent, source name classes, lineage identifiers and genetic
    code. Compared it with the separately pinned September taxonomy.'
  locator: TaxaSet/Taxon[TaxId='2283']; captured together with the other nine explicitly
    selected batch taxa
  snapshot_sha256: 520faf6a04c00bf6a23ceda7be536ac20f87f878e83936a21df23f283c23db51
- evidence_id: lpsn-inventory
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: Inspected all exact taxon/name mappings and linked synonymous LPSN names,
    retaining statuses and type-designation scope.
  locator: 'line 14847: {"lpsn_id":"lpsn:772572","name":"Acidianus ambivalens","rank":"SPECIES","authority":"(Zillig
    and Böck 1987) Fuchs et al. 1996","url":"https://lpsn.dsmz.de/species/acidianus-ambivalens","deprecated":"0","status":"legitimate=True;
    validly published under the ICNP; correct name","validly_published":"1","legitimate":"1","is_correct_name":"1","parent_lpsn_id":"lpsn:516964","ncbitaxon_ids":"NCBITaxon:2283","gtdb_ids":"GTDB:s__Acidianus_ambivalens","type_strain_ids":"kgmicrobe.strain:CIP-104912|kgmicrobe.strain:DSM-3772|kgmicrobe.strain:JCM-9191","synonym_of":"lpsn:775729","synonyms":"lpsn:775729","publications":"doi:10.1016/s0723-2020(96)80009-9|doi:10.1099/00207713-46-3-836","sequence_accessions":"INSDC:D85506"};
    line 16814: {"lpsn_id":"lpsn:775729","name":"Desulfurolobus ambivalens","rank":"SPECIES","authority":"Zillig
    and Böck 1987","url":"https://lpsn.dsmz.de/species/desulfurolobus-ambivalens","deprecated":"1","status":"legitimate=True;
    validly published under the ICNP; synonym","validly_published":"1","legitimate":"1","is_correct_name":"0","parent_lpsn_id":"lpsn:517031","ncbitaxon_ids":"","gtdb_ids":"","type_strain_ids":"kgmicrobe.strain:CIP-104912|kgmicrobe.strain:DSM-3772|kgmicrobe.strain:JCM-9191","synonym_of":"lpsn:772572","synonyms":"lpsn:772572","publications":"doi:10.1016/s0723-2020(86)80077-7|doi:10.1099/00207713-37-2-179","sequence_accessions":"INSDC:D85506"}'
  snapshot_sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
- evidence_id: gtdb-mappings
  kind: database
  reference: data/raw/gtdb_mappings.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: Inspected this taxon's GTDB mappings and every reverse mapping of the same
    selected source cluster; predicates and counts remain source-scoped.
  locator: 'line 180405: {"gtdb_id":"GTDB:s__Acidianus_ambivalens","gtdb_label":"s__Acidianus_ambivalens","gtdb_parent":"GTDB:g__Acidianus","ncbitaxon_id":"NCBITaxon:2283","predicate":"skos:closeMatch","genome_count":"2"}'
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
- evidence_id: gtdb-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: Inspected source species identifiers, labels, parent cluster and genome
    counts.
  locator: 'line 3492: {"gtdb_id":"GTDB:s__Acidianus_ambivalens","label":"s__Acidianus_ambivalens","parent":"GTDB:g__Acidianus","genome_count":"2"}'
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
- evidence_id: bacdive-inventory
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: Full BacDive inventory selection used the exact taxon plus every descendant
    from the complete NCBI parent graph. Deposits, type status and classified_as remain
    separate from taxon identity.
  locator: 'line 16462: {"strain_id":"kgmicrobe.strain:bacdive_16643","bacdive_id":"16643","designation":"","taxon_ids":"NCBITaxon:2283","lpsn_ids":"lpsn:772572","culture_collection_ids":"kgmicrobe.strain:DSM-3772|kgmicrobe.strain:JCM-9191|kgmicrobe.strain:LEI%2010","medium_count":"0"}'
  snapshot_sha256: 029fd6d1f53ef7f90684130bf0d644ed3edd1d8fbeb065a511ae928f160b1eea
- evidence_id: culture-inventory
  kind: database
  reference: data/raw/culture_collection_strains.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: Inspected exact culture identifiers associated with the target; source
    aliases do not independently authorize genome joins.
  locator: 'line 77146: {"strain_id":"kgmicrobe.strain:DSM-3772","taxon_ids":"NCBITaxon:2283"};
    line 112665: {"strain_id":"kgmicrobe.strain:JCM-9191","taxon_ids":"NCBITaxon:2283"};
    line 123135: {"strain_id":"kgmicrobe.strain:LEI%2010","taxon_ids":"NCBITaxon:2283"}'
  snapshot_sha256: 810fdcb16abd6330fb15bb03d4c74b18db86be36a7c599df7c6b2498d9735c95
- evidence_id: gold-organisms
  kind: database
  reference: data/raw/gold_organisms.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: Inspected the exact GOLD organism count row, or its bounded absence, without
    converting counts to phenotypes.
  locator: 'line 21428: {"taxon_id":"NCBITaxon:2283","organism_count":"4"}'
  snapshot_sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
- evidence_id: mediadive-taxa
  kind: database
  reference: data/raw/mediadive_taxa.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: Inspected the exact MediaDive medium count row, or its bounded absence,
    without converting counts to phenotypes.
  locator: 'line 6951: {"taxon_id":"NCBITaxon:2283","medium_count":"3","media_ids":"mediadive.medium:358a|mediadive.medium:J185|mediadive.medium:J186"}'
  snapshot_sha256: 3f74b78cadfcdb6aeae953e09fdb39e34fd9c5d5ed0be65a04a5d7fb02355905
- evidence_id: madin-taxa
  kind: database
  reference: data/raw/madin_taxa.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: Inspected the exact Madin trait-assertion count row, or its bounded absence,
    without converting counts to phenotypes.
  locator: 'line 19682: {"taxon_id":"NCBITaxon:2283","assertion_count":"5"}'
  snapshot_sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
- evidence_id: bactotraits-taxa
  kind: database
  reference: data/raw/bactotraits_taxa.tsv
  accessed_at: '2026-10-19T07:19:43Z'
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
  accessed_at: '2026-10-19T23:31:48Z'
  support: supports
  summary: The local mapping policy permits one-to-one species closeMatch mappings
    and LPSN-linked species to supply xrefs/synonyms, retains pooled broadMatch entries
    separately, and carries NCBI lineage unchanged.
  locator: Mapping predicates and Scope and lineage sections
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
- evidence_id: equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-19T23:31:48Z'
  support: supports
  summary: TaxonRecord.xrefs denotes true equivalence, while broader/narrower relationships
    belong in taxonomy_mappings; TaxonomyMapping.genome_count counts genomes under
    the source taxon.
  locator: TaxonRecord.xrefs (lines 180–187); TaxonomyMapping (lines 417–439)
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
- evidence_id: seed-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-19T23:31:48Z'
  support: supports
  summary: The identity branch accepts an LPSN GTDB bridge or any skos:closeMatch,
    then emits an equivalent xref and, if the text differs, an EXACT_SYNONYM. It does
    not guard against a strain-rank target.
  locator: GTDB mapping construction and identity promotion, lines 440–472
  snapshot_sha256: 6b5b065f4ae7aea022af736a22c0f63dc58a2425c7ee453259e567ab030f8257
- evidence_id: manifest
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T23:31:48Z'
  support: supports
  summary: The source manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd
    and hashes individual upstream inputs; extraction time is 2026-09-13T17:50:44Z.
  locator: kg_microbe_source, inputs, extracted_at
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
- evidence_id: overlay-manifests
  kind: record_content
  reference: data/atb/MANIFEST.yaml
  accessed_at: '2026-10-19T23:31:48Z'
  support: supports
  summary: Compared raw, ATB and StrainInfo extraction timestamps. Their maximum,
    2026-09-13T17:54:04Z, matches the sole generated seed event. The StrainInfo manifest
    is separately captured in source.inputs.
  locator: extracted_at, together with data/straininfo/MANIFEST.yaml
  snapshot_sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
- evidence_id: primary-source-1
  kind: primary_source
  reference: data/bacdive/records.jsonl.gz
  accessed_at: '2026-10-19T07:20:17Z'
  support: supports
  summary: Inspected complete selected source objects, including identifier/deposit
    fields and explicit source relationships. Source grouping and taxonomic similarity
    do not transfer sequence assertions across deposits.
  locator: decompressed JSONL lines 16461
  snapshot_sha256: b27d0f50f06aa33615e7cc2aae4acb7c2767df930c85292e76fbb462ac136080
- evidence_id: primary-source-2
  kind: primary_source
  reference: data/straininfo/records.jsonl.gz
  accessed_at: '2026-10-19T07:20:17Z'
  support: supports
  summary: Inspected complete selected source objects, including identifier/deposit
    fields and explicit source relationships. Source grouping and taxonomic similarity
    do not transfer sequence assertions across deposits.
  locator: decompressed JSONL lines 35670
  snapshot_sha256: 8f8e6093f0617317e0488463e52de153f566effa7a5d43b44d17dabab9692819
- evidence_id: primary-source-3
  kind: primary_source
  reference: data/gold/organisms.jsonl.gz
  accessed_at: '2026-10-19T07:20:17Z'
  support: supports
  summary: Inspected complete selected source objects, including identifier/deposit
    fields and explicit source relationships. These are organism/project/analysis
    records, not interchangeable genome identifiers.
  locator: decompressed JSONL lines 24887, 411927, 449279
  snapshot_sha256: 8c1a055214cb240c58fadda0815efbefcb60848245e8a7474e6b1b41d123235c
- evidence_id: primary-source-4
  kind: primary_source
  reference: data/gold/projects.jsonl.gz
  accessed_at: '2026-10-19T07:20:17Z'
  support: supports
  summary: Inspected complete selected source objects, including identifier/deposit
    fields and explicit source relationships. These are organism/project/analysis
    records, not interchangeable genome identifiers.
  locator: decompressed JSONL lines 402657, 404988
  snapshot_sha256: 0d852fe0144afd778609fef82b266fd1507a4c0be949efd2f53c7c34526b6c95
- evidence_id: primary-source-5
  kind: primary_source
  reference: data/gold/analyses.jsonl.gz
  accessed_at: '2026-10-19T07:20:17Z'
  support: supports
  summary: Inspected complete selected source objects, including identifier/deposit
    fields and explicit source relationships. These are organism/project/analysis
    records, not interchangeable genome identifiers.
  locator: decompressed JSONL lines 316269, 318460
  snapshot_sha256: d597f0d5f31fc8b387caaf659f3c6a337959219870529e907a1c0287e3877b7a
- evidence_id: assembly-inputs
  kind: database
  reference: data/raw/strain_assemblies.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: Inspected every matching source row and compared all assertion fields with
    this record; accessions and source evidence remain distinct.
  locator: selected data lines 81977, 81978, 81979, 81980, 81981, 81982, 81983, 81984,
    81985, 81986, 81987
  snapshot_sha256: 71344b934db3081bfcac9562a0bd1fd8fddcfdabb8af60e208ca09035e818315
- evidence_id: genome-inputs
  kind: database
  reference: data/raw/strain_genome_records.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: Inspected every matching source row and compared all assertion fields with
    this record; accessions and source evidence remain distinct.
  locator: selected data lines 64210, 64211, 64212, 64213, 64214, 64215, 64216, 64217,
    64218, 64219
  snapshot_sha256: 47ed80be55660aad4bd82d37d889ea60f8686cec1aeeccf72e5af22bf43728ab
- evidence_id: related-inputs
  kind: database
  reference: data/raw/strain_related_records.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: Inspected every matching source row and compared all assertion fields with
    this record; accessions and source evidence remain distinct.
  locator: selected data lines 249181, 249182, 249183, 249184, 249185, 249186, 249187,
    249188, 249189, 249190, 249191, 249192, 249193, 249194, 249195, 249196, 249197,
    249198, 249199, 249200, 249201, 249202, 249203, 249204, 249205, 249206, 249207
  snapshot_sha256: c33a9bf4c6b94dc6971f1c0d46565092c37ba7c2d462a6bc9c20ccbf58fb9c56
- evidence_id: straininfo-deposits
  kind: database
  reference: data/straininfo/strain_links.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: Inspected every matching source row and compared all assertion fields with
    this record; accessions and source evidence remain distinct.
  locator: selected data lines 68791, 68792
  snapshot_sha256: 615ac119e61df3a9d296ab16674bca6de3fdbf6478ca21a61312014f0ebbae8f
- evidence_id: straininfo-assemblies
  kind: database
  reference: data/straininfo/assemblies.tsv
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: Inspected every matching source row and compared all assertion fields with
    this record; accessions and source evidence remain distinct.
  locator: selected data lines 5953
  snapshot_sha256: d55ba39ab7cb81076a8edb61226de2bdf0aea699a7fb003cdf3ffb3ddc2f3f52
- evidence_id: straininfo-related
  kind: database
  reference: data/straininfo/related_records.tsv.gz
  accessed_at: '2026-10-19T07:19:43Z'
  support: supports
  summary: Inspected every matching source row and compared all assertion fields with
    this record; accessions and source evidence remain distinct.
  locator: selected data lines 162531, 162532, 162533, 162534, 162535, 162536, 162537,
    162538, 162539, 162540, 162541, 162542, 162543, 162544, 162545, 162546, 162547,
    162548, 162549, 162550, 162551, 162552
  snapshot_sha256: c7a262df4f970b2b11a2cf7a0a05c631ff84938e6a19cdb1d98680bb4fb35108
- evidence_id: atb-links
  kind: database
  reference: data/atb/strain_links.tsv
  accessed_at: '2026-10-19T07:19:43Z'
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
  accessed_at: '2026-10-19T23:31:48Z'
  support: supports
  summary: The pinned collection registry governs full deposit accession matching.
    DSM, IFO, JCM and NBRC identifiers retain their own authorities; bare aliases
    and nonmatching formats do not supply inferred joins.
  locator: authority entries for the record's deposit prefixes and their regex_id.full
    templates
  snapshot_sha256: d51abac898f8796dbc2c7b127bb4e61a8ada7f4350fdce689cf755d926446061
- evidence_id: nucleotide-authority
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&retmode=json&id=AB304842.1,AJ249983.1,AJ320523.1,AJ489504.1,D85506.1,FN999991.1,FN999992.1,FR734215.1,FR734216.1,X56616.3,X63438.1,X64202.1,X90484.1,X95989.1,Y08729.1,Y08730.1,Y08735.1,Y09614.1
  accessed_at: '2026-10-19T07:21:02Z'
  support: supports
  summary: All 18 imported nucleotide references resolve to NCBI taxon 2283. The accession
    versions returned by the current authority are recorded for resolution only; unversioned
    source assertions are not rewritten. Checked accession, taxid and sequence title
    for each entry.
  locator: 'AB304842.1: Acidianus ambivalens gene for Cbf5, partial cds; AJ249983.1:
    Acidianus ambivalens partial rubA gene for rubrerythrin; AJ320523.1: Acidianus
    ambivalens partial ORF1, sdhF gene, sdhE gene, sdhB gene, ORF2, tatC gene, tatB
    gene, tatA gene, hydS gene, isp1 gene, isp2 gene, hydL gene, hyd1 gene, hyd2 gene,
    hypD gene, hypC gene, hypD gene, hyp1 gene, hyp2 gene, hoxM gene and nanT gene;
    AJ489504.1: Acidianus ambivalens noxA gene for NADH oxidase; D85506.1: Acidianus
    ambivalens 16S rRNA gene, almost full-length sequence; FN999991.1: Acidianus ambivalens
    ORF1 (partial), aorA, aorD, aorE, ORF2, odc and aspB (partial) genes, strain DSM3772;
    FN999992.1: Acidianus ambivalens cobA gene (partial), troR, aorB, aorC, mobA,
    ORF1, coxG, coxG2 and tuF genes, strain DSM3772; FR734215.1: Acidianus ambivalens
    tth1 gene for tetrathionate hydrolase, strain DSM 3772; FR734216.1: Acidianus
    ambivalens trpB gene (partial), tth2 gene and treY gene (partial), strain DSM
    3772; X56616.3: Desulfurolobus ambivalens tnpA, tnpB, rfbD and sor genes and ORF2,
    ORF3, ORF4 and ORF5; X63438.1: D.ambivalens lig gene for DNA ligase; X64202.1:
    D.ambivalens gene bps2; X90484.1: D.ambivalens DNA for 16S ribosomal RNA gene;
    X95989.1: D.ambivalens ORF1 and ORF2, sra & secE genes; Y08729.1: A.ambivalens
    doxB gene locus with doxB, doxC, doxE, and doxF genes; Y08730.1: A.ambivalens
    doxA gene locus with doxD and doxA genes; Y08735.1: Acidianus ambivalens ffh gene;
    Y09614.1: A.ambivalens doxD gene, second doxA gene locus, orf2 and orf3'
  snapshot_sha256: f710ad5e2196d2145c8cff11807baa1cd12d42d9d6534f77dc2787fda16f28c9
- evidence_id: genome-catalog-manifest
  kind: record_content
  reference: data/catalog/MANIFEST.json
  accessed_at: '2026-10-19T23:31:48Z'
  support: supports
  summary: The complete native GTDB genome catalog is the RS232 snapshot. Species
    clusters and MAGs remain distinct from physical strain deposits.
  locator: coverage.sources[name=GTDB]
  snapshot_sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
- evidence_id: genome-catalog-1
  kind: primary_source
  reference: data/catalog/gtdb_genomes-0017.jsonl.gz
  accessed_at: '2026-10-19T07:21:35Z'
  support: supports
  summary: Inspected the complete selected genome catalog rows. Source genome identity,
    taxonomic assignment, deposit fields and accession versions were assessed separately.
  locator: 'line 44803: {"accession":"RS_GCF_009729015.1","ncbi_taxid":"2283","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    ambivalens","ncbi_strain_identifiers":"LEI 10"}; line 49626: {"accession":"RS_GCF_009428885.1","ncbi_taxid":"2283","gtdb_taxonomy":"d__Archaea;p__Thermoproteota;c__Thermoprotei_A;o__Sulfolobales;f__Sulfolobaceae;g__Acidianus;s__Acidianus
    ambivalens","ncbi_strain_identifiers":"DSM 3772"}'
  snapshot_sha256: f2a4d2c5b7927184206c6614540746b5e9c298e7a924bd149fc86c0f0c046ff6
- evidence_id: genome-catalog-2
  kind: primary_source
  reference: data/catalog/ncbi_genbank-0008.jsonl.gz
  accessed_at: '2026-10-19T07:21:35Z'
  support: supports
  summary: Inspected the complete selected genome catalog rows. Source genome identity,
    taxonomic assignment, deposit fields and accession versions were assessed separately.
  locator: 'line 15543: {"assembly_accession":"GCA_009428885.1","taxid":"2283","infraspecific_name":"strain=DSM
    3772"}; line 29342: {"assembly_accession":"GCA_009729015.1","taxid":"2283","infraspecific_name":"strain=LEI
    10"}'
  snapshot_sha256: 6b31a395d770af741d40a6832c0d74026c4c82f5b95216023df867e3cdebd764
- evidence_id: genome-catalog-3
  kind: primary_source
  reference: data/catalog/ncbi_refseq-0002.jsonl.gz
  accessed_at: '2026-10-19T07:21:35Z'
  support: supports
  summary: Inspected the complete selected genome catalog rows. Source genome identity,
    taxonomic assignment, deposit fields and accession versions were assessed separately.
  locator: 'line 33554: {"assembly_accession":"GCF_009428885.1","taxid":"2283","infraspecific_name":"strain=DSM
    3772"}; line 35738: {"assembly_accession":"GCF_009729015.1","taxid":"2283","infraspecific_name":"strain=LEI
    10"}'
  snapshot_sha256: f22a85bd89937e6e2a8c7774d699102bcbf26a31af296a6cc77976d5f2a40f72
- evidence_id: genome-catalog-4
  kind: primary_source
  reference: data/bvbrc/bvbrc-0013.jsonl.gz
  accessed_at: '2026-10-19T07:21:35Z'
  support: supports
  summary: Inspected the complete selected genome catalog rows. Source genome identity,
    taxonomic assignment, deposit fields and accession versions were assessed separately.
  locator: 'line 30551: {"assembly_accession":"GCA_009428885.1","genome_id":"2283.10","taxon_id":2283,"genome_name":"Acidianus
    ambivalens strain DSM 3772","genome_status":"WGS"}; line 30552: {"assembly_accession":"GCA_009729015.1","genome_id":"2283.11","taxon_id":2283,"genome_name":"Acidianus
    ambivalens strain LEI 10","genome_status":"Complete"}'
  snapshot_sha256: ba814e4c647d96e5d00512c336e83a6fd2448549c7f9ef46cc8fd59e1790235b
- evidence_id: lpsn-live
  kind: authority
  reference: https://lpsn.dsmz.de/species/acidianus-ambivalens
  accessed_at: '2026-10-19T07:36:00Z'
  support: supports
  summary: Inspected the authority's name, category, nomenclatural and taxonomic status,
    type designations, synonyms and cited publication identity. These fields were
    compared with the pinned inventory rather than substituted into the record.
  locator: Name; category; nomenclatural/taxonomic status; type designations; synonyms
    and cited publication metadata
- evidence_id: doi-ambivalens1996
  kind: authority
  reference: https://doi.org/10.1016/s0723-2020(96)80009-9
  accessed_at: '2026-10-19T07:30:53Z'
  support: supports
  summary: Crossref registration confirms the cited publication identity, date and
    bibliographic pagination; this is metadata verification, not a review of the paper's
    experimental evidence.
  locator: 16S rDNA-based Phylogeny of the Archaeal Order Sulfolobales and Reclassification
    of Desulfurolobus ambivalens as Acidianus ambivalens comb. nov.; pages 56-60
  snapshot_sha256: de3bbef4955bd71aaa342b2d19b994634554217be0eb2ed1695a79fed1e30a09
- evidence_id: doi-validation1996
  kind: authority
  reference: https://doi.org/10.1099/00207713-46-3-836
  accessed_at: '2026-10-19T07:30:54Z'
  support: supports
  summary: Crossref registration confirms the cited publication identity, date and
    bibliographic pagination; this is metadata verification, not a review of the paper's
    experimental evidence.
  locator: 'Validation of the Publication of New Names and New Combinations Previously
    Effectively Published Outside the IJSB: List No. 58; pages 836-837'
  snapshot_sha256: 0fb296c925567586b40f8dc9f4bf1ef53a6e4d5cf8abbba23193f63ef779bb68
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
  reference: just validate-strict data/taxa/archaea/acidianus_ambivalens.yaml --out
    /private/tmp/taxonmech-record-reviews-k0MubV/strict-03.tsv
  accessed_at: '2026-10-19T07:18:44Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo;\
    \ started 2026-10-19T07:18:41Z, finished 2026-10-19T07:18:44Z, exit 0.\nValidating\
    \ 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo/src/taxonmech/schema/taxonmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/strict-03.tsv"
  locator: This exact generated YAML only.
  snapshot_sha256: 9588b7c89672c2ab12dff8e1ad91f0486af00ec5d7c0029d83f3e210791cad29
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
  summary: NCBITaxon:2283 is the species Acidianus ambivalens, below genus 12914,
    with nine carried ancestors and genetic code 11. Pinned and current NCBI taxonomy
    agree on this identity. The older Desulfurolobus and Sulfolobus names are source-scoped
    synonyms, not separate imported organisms.
  target_ids:
  - NCBITaxon:2283
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
  summary: LPSN 772572 is the correct, validly published ICNP name; 775729 is its
    retained deprecated homotypic name Desulfurolobus ambivalens. Authorities, DSM
    3772/JCM 9191/CIP 104912 type designations and the two 1996 publication DOIs match
    the inspected LPSN entries and DOI registration metadata. The GTDB species has
    an explicit LPSN bridge, and two catalog genomes support its cluster count. NCBI
    lineage remains separate from GTDB classification.
  target_ids:
  - NCBITaxon:2283
  evidence_ids:
  - record
  - taxonomy-inventory
  - lpsn-inventory
  - gtdb-mappings
  - mapping-policy
  - lpsn-live
  - doi-ambivalens1996
  - doi-validation1996
- assessment_id: completeness
  area: completeness
  topic: Complete imported subtree and source assertion units
  outcome: supported
  summary: One BacDive strain (16643) is imported, with DSM 3772, JCM 9191 and the
    unsupported join alias LEI 10 preserved. The BacDive subtree inventory contains
    no additional classified strain. The record's seven attestations retain their
    distinct NAME, GENOME, STRAIN, MEDIUM, ORGANISM and TRAIT_ASSERTION units. The
    counts in the raw inventories match the record; historical MediaDive/GOLD/Madin
    edge multiplicity could not be independently reproduced from the pinned upstream
    bytes.
  target_ids:
  - NCBITaxon:2283
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
    value: 'NCBITAXON: 1 NAME; LPSN: 1 NAME; GTDB: 2 GENOME; BACDIVE: 1 STRAIN; MEDIADIVE:
      3 MEDIUM; GOLD: 4 ORGANISM; MADIN: 5 TRAIT_ASSERTION'
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
  summary: BacDive 16643 supplies direct unversioned GCA_009428885/GCA_009729015,
    PATRIC 2283.10/2283.11 and IMG assertions. GTDB and current NCBI culture joins
    support DSM 3772 for GCA/GCF_009428885.1; the separate LEI 10 genome is not transferred
    by a guessed deposit alias. GOLD Go0029281 → Gp0548891 → Ga0491101 supports GCA_009729015.1/IMG
    8065311606, while Go0576457 → Gp0551223 → Ga0488881 supports GCA_009428885.1/IMG
    8065314359. Each chain preserves its BioSample and project. StrainInfo SI-ID 47758.3
    joins DSM 3772 through SI-DP 158532 and JCM 9191 through SI-DP 184904; the 18
    nucleotide associations resolve in NCBI to taxon 2283. CIP 104912 is nomenclatural/source
    context, not an invented BacDive deposit join. Exact multiset comparison found
    all 12 assembly, 10 genome-record and 49 related-record assertions equal to their
    raw/StrainInfo inputs, including source IDs and evidence fields.
  target_ids:
  - NCBITaxon:2283
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
  - genome-catalog-3
  - genome-catalog-4
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
  summary: The pinned GTDB cluster contains RS_GCF_009428885.1 (DSM 3772) and RS_GCF_009729015.1
    (LEI 10). Count 2 is the cluster's genome count; it does not collapse assembly
    identifiers or turn both rows into one deposit assertion. The LPSN name explicitly
    links GTDB:s__Acidianus_ambivalens.
  target_ids:
  - NCBITaxon:2283
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
  - NCBITaxon:2283
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
  - NCBITaxon:2283
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
