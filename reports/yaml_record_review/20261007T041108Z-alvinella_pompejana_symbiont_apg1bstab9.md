# YAML Record Review: Alvinella pompejana symbiont APG1Bstab9

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab9.yaml`
- Started UTC: 2026-10-07T04:09:26Z
- Finished UTC: 2026-10-07T04:11:08Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103554`, `Alvinella pompejana symbiont APG1Bstab9`: SPECIES in BACTERIA, parent `NCBITaxon:122728`, genetic code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, taxonomy mappings, strains, genomes, literature or causal graphs are asserted.

This bacterial symbiont taxon is distinct from the Alvinella host and other APG1B clones. Generated YAML is read-only; maintained inventories, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future fixes.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab9.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab9.yaml --out /private/tmp/apg9-strict.tsv`: exit 0, one file, zero errors. Read the actual header-only TSV.
- Complete backbone, lineage, seven-inventory, path/scope and attestation comparisons passed; these bounded checks do not reproduce the corpus.
- Live taxonomy XML/Datasets, exact Assembly/nuccore searches, complete marker metadata except bases, independent genome Datasets and primary-source inspection completed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- No graph node requires `just validate-products`. Full history validation was not run; no external target history reference or lifecycle promotion applies.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:18506` matches ID, label, rank, parent, code and snapshot 2026-09-13. Synonym and retirement fields are empty. Complete native scientific-name row `data/catalog/ncbi_names-0000.jsonl.gz:38514` matches and has empty unique_name.

All six pinned ancestors match in order, ID, label and rank: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Campylobacterota 29547; unclassified Campylobacterota 122728.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103554&retmode=xml) confirms identity, lineage and code. [Taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103554) confirms ancestor IDs including root. Creation is 2 September 1999 and update 19 January 2005. No OtherNames or type-material assertion appears. Exact pinned type-material, merged-ID and dropped scans found no target row.

The unclassified position is carried from NCBI without inferred intermediate ranks. SPECIES does not establish formal nomenclatural standing or a culture deposit. EXACT identifies this taxonomic node, not its host or every organism in its community.

## Evidence

`data/taxa/PATHS.tsv:14602` and `curation/seed_scope.tsv:144152` uniquely agree on identifier, stem and reason. The single NCBITAXON attestation correctly counts one NAME.

No direct target children occur in the complete pinned backbone. Exact BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw-inventory scans found no target row. Strain_count 0 agrees with inventory and subtree; it does not assert biological unculturability.

All three source manifests were parsed in full: raw extracted_at 2026-09-13T17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z. The newest-manifest rule at `src/taxonmech/seed.py:139` explains the 17:54:04Z seed event. Attested source and scope reason agree. Hashes were not recomputed.

Exact nuccore search returned only UID 5901791. Complete [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=5901791) identifies `AF180318.1`, a 172-base partial 16S rRNA sequence, taxon:103554 and clone APG1Bstab9. No strain, deposit, BioSample, BioProject, assembly, explicit host, location or isolation_source qualifier is supplied. The host-associated name is not an independently grounded host CURIE.

The marker cites Campbell and Cary, AEM 67(1):110-117 (2001), PMID:11133434; an unpublished molecular-method comparison; and direct submission on 24 August 1999 from the University of Delaware. No experiment is inferred from the unpublished title.

The inspected [primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC92526/), DOI:10.1128/AEM.67.1.110-117.2001, includes AF180318 in its DGGE-product accession series. It provides community provenance, not APG1Bstab9-specific physiological or genome evidence.

A separate inspected [name-matching study](https://pmc.ncbi.nlm.nih.gov/articles/PMC4910497/) lists the exact target label among symbiont-name examples. That section concerns ambiguity between host and symbiont names; it supplies no experimental characterization of this clone. It is not an additional biological attestation for the YAML.

Exact Assembly search returned zero with a phrase-not-found warning; the independent [genome Datasets endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103554/dataset_report) returned an empty object. These bounded checks do not prove global genome absence. A short marker is not a genome.

Before web search, all 28 fresh `kg-microbe-sources imodulondb datasets` rows were read through `uv run --offline --project ../../culturebotai-claw`. No covered organism matches and no gene/module is asserted; component queries are not applicable. Noncoverage is not negative biological evidence.

## Completeness

No consequential gap was established. Definitions, evidence, nomenclature, mappings, strain links and graphs are optional here. Marker/literature context is optional enrichment; a clone name does not establish a culture deposit.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched numeric-boundary 103554, exact label, stem and APG1Bstab9 punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All 24 matched rows were fully read: three applicable identity/scope rows and 21 non-target or unsupported numeric matches.

A separate AF180318/version scan returned zero rows in those roots. At both stages all five SOURCE.json files were independently parsed in full and history filenames searched without ignore filtering. The initial BacDive requested-ID/URL match denotes native BacDive 103554, not NCBITaxon:103554. No target history filename was found. An ignored-inclusive report filename search found no prior target report. Absence claims are limited to these repository roots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, attestation, source count and SEEDED lifecycle are supported. No missing required representation was established.

## Recommended Edits

None required. Preserve generated YAML and SEEDED status.

Future enrichment belongs in maintained sources/extractors and inventories or tested `src/taxonmech/seed.py` changes. Identity fixes belong upstream; scope fixes belong in `curation/seed_scope.tsv`. Do not transfer culture/genome data from another namespace or treat a name-matching example as biological evidence.

## Follow-up Checks

For authorized enrichment, establish whole-accession source chains, independently ground any host assertion and require clone-specific support for phenotype claims. Rerun target schema/strict checks followed by documented corpus reproduction/provenance gates. Keep taxon, host, clone, strain, deposit, marker, sample, run, assembly, genome and project identities distinct. No unresolved blocker requires enrichment now.

## Additional Notes

All candidate native JSON fields and TSV columns were read losslessly. Logical decompressed addresses:

- BacDive 103554 is Corynebacterium pseudodiphtheriticum STI10120, taxon 37637: raw row 27688/native row 27687. This resolves the SOURCE.json request match.
- StrainInfo native row 31035 has CIP 103554, Bacillus viscosus But 25, taxon 33023, SI-ID42832/SI-DP149173. Its strain-level classification is broader Bacillus 1386. The X77792 marker explicitly names ATCC 51155/SI-DP115246, not the CIP deposit or target.
- StrainInfo native row 129241 has KY103554, a ribosomal marker for Hanseniaspora uvarum CBS 286, taxon 29833, SI-ID177136/SI-DP452697. It is not a symbiont marker; reading this collision did not reopen a Eukaryota review.
- CP103554 belongs to Klebsiella michiganensis 5088, taxon 1134687, GCA_024917295.1, SAMN28174081: BV-BRC shard 0000 rows 15880/15885 and GOLD analysis 401931, Ga0608781/Gp0745353.
- GOLD project row 587982, Gp0789131, and analysis row 423717, Ga0634603, concern NPDC103554_429_G03, a stored microbial culture described as a low-complexity metagenome, with IMG 3300074664. The native rows contain no organism GOLD ID, NCBI BioSample/BioProject or target-taxonomy chain. Numeric overlap is insufficient to attach this entry to APG1Bstab9; no organism identity is invented for it.
- MGBC103554 is uncultured Muribaculaceae bacterium 2301481, GCA_948822625.1, SAMEA112377496: BV-BRC shard 0013 row 47204, GTDB shard 0008 row 27489 and GenBank shard 0060 row 33274. GTDB's CAG-873 assignment is not a target mapping.
- MarMAG_103554 is uncultured bacterium 77133, SAMEA120729224: BV-BRC shard 0027 row 1296 and GenBank shard 0065 row 7270. GenBank supplies GCA_977586475.1; the native BV-BRC row has no assembly_accession field.
- Four GTDB hits are N50 values equal to 103554: shard 0008 row 4949, GCA_017529865.1 (Bacteroidaceae); shard 0005 row 2323, GCA_034144305.1 (Phocaeicola vulgatus); shard 0005 row 22226, GCF_900060415.1 (Legionella pneumophila); shard 0001 row 6780, GCA_902475755.1 (uncultured Coriobacteriia).
- GenBank shard 0022 row 816 is Shigella boydii PNUSAE103554, taxon 621, GCA_023794715.1, SAMN28960858. Shard 0007 row 34958 is Salmonella enterica PNUSAS103554, taxon 28901, GCA_008803595.1, SAMN12875730.
- AllTheBacteria row 6150 is E. coli O26:H11, DRR103554, SAMD00075897, ERZ25075534. Available FASTA, PASS filters, source URLs and SeqKit sum establish no target relationship.

Only this new report was written for this target. No YAML, inventory, generated product, earlier report, history or lifecycle state changed. Eukaryota records remain untouched. No paid research, external contact or GitHub mutation occurred.
