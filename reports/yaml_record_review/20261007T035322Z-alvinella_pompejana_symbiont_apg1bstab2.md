# YAML Record Review: Alvinella pompejana symbiont APG1Bstab2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab2.yaml`
- Started UTC: 2026-10-07T03:50:43Z
- Finished UTC: 2026-10-07T03:53:22Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103550`, `Alvinella pompejana symbiont APG1Bstab2`: SPECIES in BACTERIA, parent `NCBITaxon:122728`, genetic code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, deposits, genomes, literature, discussions or causal graphs are asserted.

The target is a bacterial symbiont taxon, not the Alvinella host or another APG1B clone. Generated YAML is read-only; maintained inputs, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future corrections.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab2.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab2.yaml --out /private/tmp/apg2-strict.tsv`: exit 0, one file scanned, zero errors. Read the actual header-only TSV.
- Complete backbone, ancestor, seven-inventory, path/scope and attestation comparisons passed. These bounded checks are not full-corpus reproduction.
- Live taxonomy XML/Datasets, exact Assembly/nuccore searches, full marker metadata except bases and independent genome Datasets reads completed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- `just validate-products` has no applicable graph node and was not run. Full history validation was not run. No external target history reference, new history event or lifecycle promotion applies.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:18502` agrees on ID, label, rank, parent, code and snapshot 2026-09-13; synonym and retirement fields are empty. Complete native scientific-name row `data/catalog/ncbi_names-0000.jsonl.gz:38510` agrees and has empty unique_name.

All six pinned ancestors agree in order, ID, label and rank: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Campylobacterota 29547; unclassified Campylobacterota 122728.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103550&retmode=xml) confirms identity, named lineage and code. [Taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103550) confirms ancestor IDs including root. Creation is 2 September 1999, update 19 January 2005; no OtherNames or type-material assertion appears. Exact pinned type-material, merged-ID and dropped scans found no target row.

The unclassified placement is carried from NCBI; intermediate ranks are not inferred. SPECIES is an NCBI rank, not formal nomenclatural standing or evidence of a deposited strain. EXACT grounding denotes this taxonomic node, not its host, marker, or other community members.

## Evidence

`data/taxa/PATHS.tsv:14598` and `curation/seed_scope.tsv:144148` uniquely match ID, stem and reason. The NCBITAXON attestation correctly counts one NAME.

No direct children occur in the complete pinned backbone. Full exact scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories found no target row. Strain_count 0 agrees with source inventory and target subtree; it is not a biological claim of unculturability.

All three manifests were parsed in full this turn: raw extracted_at 2026-09-13T17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z. The inspected newest-manifest rule at `src/taxonmech/seed.py:139` explains the 17:54:04Z event. Source list and scope reason agree. Hashes were not recomputed.

Exact nuccore search returned only UID 5901787. Full [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=5901787) identifies `AF180314.1`, a 172-base partial 16S rRNA marker, taxon:103550 and clone APG1Bstab2. It has no strain, culture-deposit, BioSample, BioProject, assembly, explicit host, location or isolation_source qualifier. The label names the host association without supplying an independently grounded host CURIE.

The marker cites Campbell and Cary, AEM 67(1):110-117 (2001), PMID:11133434; an unpublished comparison of molecular methods; and direct submission on 24 August 1999 from the University of Delaware. No independent experiment is inferred from the unpublished title.

The inspected [primary paper](https://journals.asm.org/doi/full/10.1128/aem.67.1.110-117.2001), DOI:10.1128/AEM.67.1.110-117.2001, places AF180314 in its DGGE-product accession series. Its community context supports provenance, not APG1Bstab2-specific physiological claims or equivalence to its spirochetes.

Exact Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103550/dataset_report) returned an empty object. These bounded checks do not establish universal genome absence; a partial 16S marker is not a genome.

Before web search, read all 28 rows of the fresh `kg-microbe-sources imodulondb datasets` result through `uv run --offline --project ../../culturebotai-claw`. No covered organism matches and no module/gene is asserted. No component query applies; iModulonDB noncoverage is not negative biological evidence.

## Completeness

Optional definitions, evidence, nomenclature, taxonomy mappings, strains and graphs need not be invented. Marker and literature context are optional enrichment, not missing required fields. A clone name is not a culture-deposit identity.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched numeric-boundary 103550, exact label, stem and APG1Bstab2 punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All 44 matched rows were read losslessly: three applicable identity/scope rows and 41 unrelated rows.

A separate AF180314/version scan found zero rows in those roots. At both stages all five SOURCE.json files were parsed independently in full and history filenames searched without ignore filtering. The initial BacDive fetch-ID/URL match is native ID 103550, not NCBITaxon:103550; no target history filename was found. These are bounded repository checks, not universal absence claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, source counts and SEEDED lifecycle are supported. No consequential omission was established by the completed checks.

## Recommended Edits

None required. Preserve generated YAML and SEEDED state.

Future enrichment belongs in a maintained source/extractor and inventory, or tested `src/taxonmech/seed.py` changes. Source/kg-microbe identity corrections belong upstream; scope changes belong in `curation/seed_scope.tsv`. Do not transfer culture/genome evidence from another identifier namespace or another clone.

## Follow-up Checks

For later authorized enrichment, establish whole-accession source chains, independently ground any host, and require clone-specific support for phenotype claims. Rerun target schema/strict validation and then documented full-corpus reproduction/provenance gates. Keep taxon, host, clone, strain, deposit, marker, sample, run, assembly, genome and project identities distinct. No unresolved blocker requires enrichment now.

## Additional Notes

All unrelated rows were fully read, including native JSON fields and TSV columns. Logical decompressed row addresses follow.

- Native BacDive 103550 is Agromyces sp. ST003013, taxon 51513: raw row 27684 and native row 27683. This resolves the SOURCE.json request match.
- CIP 103550 is Enterobacter material: raw BacDive row 4258, native row 4257, culture row 43883, raw strain-related rows 364309/364310; StrainInfo native row 26431, strain-links row 89214 and related rows 215887/215893; GOLD organism row 139917, Go0201718. The chain is BacDive 4363, SI-ID 38005, SI-DP 150515.
- Preserve this unrelated Enterobacter source disagreement: BacDive carries taxids 550 and 3029761, an E. cloacae display label, E. pasteurii LPSN classification and a negative type flag. LPSN row 7323 and NCBI type-material rows 156820-156823 associate CIP 103550 with E. pasteurii taxon 3029761 as type material; StrainInfo and GOLD retain E. cloacae. None denotes APG1Bstab2. StrainInfo's marker links name ATCC 23355 and its genome link names DSM 26481, not the CIP deposit; neither can be transferred by record grouping.
- DSM 103550 is Aurantisolimonas haloimpatiens BN130233, taxon 1638097: raw BacDive row 81035, native row 81034, culture row 59671, raw strain-related rows 211003/211004; StrainInfo native row 297819, strain-links row 57686 and related rows 135886/135887; GOLD organism row 451284, Go0620650. The current StrainInfo record is SI-ID 399930, deposit 906758; BacDive also retains a different source StrainInfo link, 287779. Its type-strain status and KP419742.1 marker are unrelated.
- StrainInfo native row 26710 contains SI-DP 103550 for Pseudomonas putida NCIB 12602, taxon 303, SI-ID 38309. A deposit ID is not an NCBI taxonomy ID.
- CP103550 occurs within Klebsiella pneumoniae 2791, taxon 573, GCA_024918075.1, SAMN28174007: BV-BRC shard 0024 rows 37626/37881 and GOLD analysis row 401969. GOLD Ga0608819/Gp0745359 are related identifiers, not target genome IDs.
- MarMAG_103550 is uncultured bacterium taxon 77133, GCA_977587515.1, SAMEA120729038: BV-BRC shard 0027 row 1378 and GenBank shard 0065 row 7374.
- MGBC103550 is an uncultured Alphaproteobacteria MAG, taxon 91750, GCA_948828215.1, SAMEA112377492: BV-BRC shard 0028 row 9308, GTDB shard 0003 row 47344 and GenBank shard 0060 row 33833. Its Enterousia GTDB placement is not a target mapping.
- GenBank shard 0007 row 34799 is Salmonella enterica PNUSAS103550, taxon 28901, GCA_008794955.1, SAMN12875684.
- Three GTDB matches are contig N50 values equal to 103550: shard 0006 row 14322, GCA_902602665.1; shard 0003 row 15814, GCF_900062685.1; shard 0015 row 49769, GCF_900062715.1. They are Actinomarina or Legionella records, not target evidence.
- AllTheBacteria row 6146 is E. coli O26:H11, run DRR103550, sample SAMD00075893, analysis ERZ25075530. Available FASTA, PASS filters, checksums and download URLs do not establish a target relationship.

Only this new report was written for this target. No YAML, inventory, generated product, earlier report, history or lifecycle state was changed. No Eukaryota review was reopened. No paid research, external contact or GitHub mutation occurred.
