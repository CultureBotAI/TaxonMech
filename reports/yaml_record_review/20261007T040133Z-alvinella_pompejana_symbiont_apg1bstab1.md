# YAML Record Review: Alvinella pompejana symbiont APG1Bstab1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab1.yaml`
- Started UTC: 2026-10-07T03:55:35Z
- Finished UTC: 2026-10-07T04:01:33Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103551`, `Alvinella pompejana symbiont APG1Bstab1`: SPECIES in BACTERIA, parent `NCBITaxon:122728`, genetic code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, deposits, genomes, literature, discussions or causal graphs are asserted.

This is a bacterial symbiont taxon, not the Alvinella host, APG1Bstab10, or the 6C6 epibiont taxon discussed below. Generated YAML remains read-only; maintained inventories, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future corrections.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab1.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab1.yaml --out /private/tmp/apg1-strict.tsv`: exit 0, one file scanned, zero errors. Read the actual header-only TSV.
- Complete backbone, ancestor, seven-inventory, path/scope and attestation comparisons passed. These are bounded source checks, not corpus reproduction.
- Live taxonomy XML/Datasets, exact Assembly/nuccore searches, complete target marker metadata except bases, independent genome Datasets and primary literature checks completed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- `just validate-products` has no applicable graph node and was not run. Full history validation was not run. No external target history reference, new history event or lifecycle promotion applies.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:18503` agrees on ID, label, rank, parent, code and snapshot 2026-09-13; synonym and retirement fields are empty. Complete native scientific-name row `data/catalog/ncbi_names-0000.jsonl.gz:38511` agrees.

All six pinned ancestors agree in order, ID, label and rank: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Campylobacterota 29547; unclassified Campylobacterota 122728.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103551&retmode=xml) confirms identity, named lineage and code. [Taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103551) confirms ancestor IDs including root. Creation is 2 September 1999, update 19 January 2005; no OtherNames or type-material assertion appears. Exact pinned type-material, merged-ID and dropped scans found no target row.

Unclassified placement is carried from NCBI without inferred intermediate ranks. SPECIES denotes the NCBI rank, not formal nomenclatural standing or a deposited strain. EXACT identifies this taxonomic node, not its host or every similar community sequence.

## Evidence

`data/taxa/PATHS.tsv:14599` and `curation/seed_scope.tsv:144149` uniquely match ID, stem and reason. The NCBITAXON attestation correctly counts one NAME.

No direct children occur in the complete pinned backbone. Exact scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories found no target row. Strain_count 0 agrees with inventory and subtree; it does not assert biological unculturability.

All three manifests were parsed in full: raw extracted_at 2026-09-13T17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z. The newest-manifest rule at `src/taxonmech/seed.py:139` explains the seed event at 17:54:04Z. The event source list and scope reason agree. Hashes were not recomputed.

Exact nuccore search returned only UID 5901788. Complete [GenBank marker metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=5901788) identifies `AF180315.1`, a 172-base partial 16S rRNA sequence, taxon:103551 and clone APG1Bstab1. It has no strain, deposit, BioSample, BioProject, assembly, explicit host, location or isolation_source qualifier. Its label is not an independently grounded host CURIE.

The marker cites Campbell and Cary, AEM 67(1):110-117 (2001), PMID:11133434; an unpublished comparison of molecular methods; and direct submission on 24 August 1999 from the University of Delaware. The inspected [2001 primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC92526/), DOI:10.1128/AEM.67.1.110-117.2001, includes AF180315 in its DGGE-product accession series. It identifies APG1B as an Elsa sample from 1991. Its spirochete A is APG10, not this target; community observations are not clone-specific physiological evidence.

A second inspected [primary paper](https://journals.asm.org/doi/10.1128/aem.69.9.5070-5078.2003), Campbell, Stein and Cary (2003), DOI:10.1128/AEM.69.9.5070-5078.2003, PMID:12957888, reports 100% identity between AF180315 and fosmid 6C6 in the compared 16S region. The fosmid physically links ribosomal and ATP citrate lyase sequences; expression experiments concern communities. PubMed confirms the citation. This is useful marker-level context, not whole-genome equivalence or direct demonstration of APG1Bstab1 physiology.

Inspected [6C6 sequence identity, reference and relevant feature metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=AY312990) identifies `AY312990.1`, 38,233 bases, Alvinella pompejana epibiont 6C6, taxon:244799, and fosmid clone 6C6. The host qualifier belongs to that source record. Its citrate lyase subunit annotations are putative sequence-similarity assignments. A complete fosmid sequence is not a complete organism genome, and its different taxon must not be silently merged with 103551.

Exact Assembly search returned zero with a phrase-not-found warning; the independent [genome Datasets endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103551/dataset_report) returned an empty object. These bounded checks do not prove universal genome absence.

Before web search, all 28 rows of fresh `kg-microbe-sources imodulondb datasets` output were read through `uv run --offline --project ../../culturebotai-claw`. No covered organism matches. No module or gene is asserted in the YAML, so no component query applies. iModulonDB noncoverage is not negative biological evidence.

## Completeness

Optional definition, evidence, nomenclature, taxonomy mappings, strain and graph fields need not be invented. The marker and literature link are optional enrichment, not missing required representations. Neither a clone name nor regional sequence identity establishes a culture deposit.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched numeric-boundary 103551, exact label, stem and APG1Bstab1 punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. The clone suffix boundary excluded APG1Bstab10. All 55 matched rows were read losslessly: three applicable identity/scope rows and 52 unrelated rows.

Separate AF180315/version and AY312990/version searches returned zero rows in those roots. For each search stage all five SOURCE.json files were independently parsed in full and history filenames searched without ignore filtering. The initial BacDive request-ID/URL match denotes native BacDive 103551, not NCBITaxon:103551. No target history filename or previous target report was found in the respective ignored-inclusive searches. These statements are bounded repository results, not global absence claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, source counts and SEEDED lifecycle are supported. No consequential omission was established. The source discrepancies below concern optional future enrichment, not claims made by this YAML.

## Recommended Edits

None required. Preserve generated YAML and SEEDED state.

Future enrichment belongs in a maintained source/extractor and inventory, or tested `src/taxonmech/seed.py` changes. Taxonomic identity corrections belong upstream; scope changes belong in `curation/seed_scope.tsv`. Retain the marker/fosmid distinction and do not promote community expression or putative annotation to clone-specific phenotype evidence.

## Follow-up Checks

For authorized enrichment, resolve sampling-date and probe-assignment discrepancies, establish whole-accession source chains, and independently ground any host assertion. Rerun target schema/strict validation followed by documented corpus reproduction/provenance gates. Keep taxon, host, clone, strain, deposit, marker, sample, run, assembly, genome and project identities distinct. No unresolved blocker requires enrichment now.

## Additional Notes

The 2001 paper's methods/Table 1 date APG1B to 1991; the 2003 paper's Figure 3 caption dates APG1B to 1994. Also, the 2003 methods and results reverse the 5A/13B probe assignments for 6C6/7G3. Preserve these conflicts instead of assigning an unqualified collection date or probe identity. Neither discrepancy changes the current record's supported taxonomy.

All 52 unrelated local rows were fully read, including native JSON fields and TSV columns. Logical decompressed addresses and disambiguation:

- BacDive 103551 is Agromyces sp. ST003014, taxon 51513: raw row 27685, native row 27684. This resolves the SOURCE.json request match.
- CIP 103551: BacDive 139233, LRA 004 03 73, ATCC 43862; raw row 61532, native row 61531, culture row 43884. StrainInfo SI-ID46853/SI-DP154968 appears in native row 34813, strain-links 25628 and related rows 62102/62103. GOLD Go0226665 appears in organism row 164821 and raw strain-related rows 123485/123486. BacDive/CIP classify Serratia nematodiphila 458197; GOLD and StrainInfo's strain-level classification retain S. marcescens 615. Preserve that unrelated source disagreement.
- DSM 103551 is Rapidithrix thailandica 413964: BacDive 140017, raw row 62311/native 62310; culture row 59672; StrainInfo native 239173, strain-links 26863, related 64860/64861, SI-ID310999/SI-DP911638. GOLD Go0511099/Gp0401154/Ga0373371 appears in organism 359573, project 287513, analysis 230612 and raw strain-related rows 127426/127427, 127432/127433, 127436/127437. AB265192 names TISTR 1750; LC191863 and unversioned GCA_039710355 name JCM 23209. Those links are not target evidence or automatic links to every grouped deposit.
- StrainInfo native 26711 contains SI-DP103551 for E. coli ATCC 23976, taxon 562, SI-ID38310. Native 63978 contains KY103551, a ribosomal marker for Hanseniaspora uvarum CBS 287, taxon 29833, SI-ID77018. Neither namespace denotes the target.
- Bacillus subtilis SRCM103551, taxon 1423: GOLD organism 365703/project 315469/analysis 253493, Go0519679/Gp0443830/Ga0399554, IMG 2969155270; BV-BRC shard 0003 row 11704; GTDB shard 0005 row 36550; GenBank shard 0003 row 9070; RefSeq shard 0002 row 11708. GCA/GCF_004103555.1, CP035230 and SAMN10754253 are unrelated.
- CP103551 belongs to Klebsiella pneumoniae 2791, taxon 573, GCA_024918075.1, SAMN28174007: BV-BRC shard 0024 rows 37626/37881 and GOLD analysis 401969, Ga0608819/Gp0745359.
- K. pneumoniae isolate 103551, SAMEA12055395: GenBank shard 0058 row 41528 carries GCA_926280155.1; historical RefSeq shard 0002 row 6969 carries suppressed GCF_926280155.1. Neither is this symbiont.
- MGBC103551 is uncultured Muribaculum 1918613, GCA_948792225.1, SAMEA112377493: BV-BRC shard 0008 row 35034, GTDB shard 0010 row 21648, GenBank shard 0060 row 30234. GTDB's Muribaculum arabinoxylanisolvens assignment does not map the target.
- MarMAG_103551 is uncultured bacterium 77133, GCA_977601635.1, SAMEA120729097: BV-BRC shard 0027 row 2076 and GenBank shard 0065 row 8786.
- GenBank shard 0064 row 1866 is Rhodoluna sp. 1969481, GCA_965026725.1, SAMEA117462197; 103551 occurs inside its isolate designation. Shard 0007 row 34730 is Salmonella enterica PNUSAS103551, taxon 28901, GCA_008793545.1, SAMN12875683.
- Two GTDB hits are N50 values equal to 103551: shard 0010 row 33960, GCA_964523715.1, uncultured Verrucomicrobiota 156588; shard 0002 row 23620, GCF_022974895.1, E. coli 562.
- AllTheBacteria row 6147 is E. coli O26:H11, run DRR103551, sample SAMD00075894, analysis ERZ25075531. Available FASTA and PASS filters do not establish a target relationship.

Only this new report was written for this target. No YAML, inventory, generated product, prior report, history or lifecycle state was changed. No Eukaryota review was reopened. No paid research, external contact or GitHub mutation occurred.
