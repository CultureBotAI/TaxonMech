# YAML Record Review: Alvinella pompejana symbiont APG1Bstab8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab8.yaml`
- Started UTC: 2026-10-07T04:14:10Z
- Finished UTC: 2026-10-07T04:16:52Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:103555`, `Alvinella pompejana symbiont APG1Bstab8`: SPECIES in BACTERIA, parent 122728, genetic code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, strains, genomes, literature or causal graphs are asserted.

This bacterial taxon is distinct from the host, community and neighboring APG1B clones. Generated YAML is read-only. Maintained inventories, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future fixes.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab8.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg1bstab8.yaml --out /private/tmp/apg8-strict.tsv`: exit 0, one file, zero errors. Read the actual header-only TSV.
- Complete backbone/lineage, seven-inventory, path/scope, status and attestation comparisons passed; these bounded checks do not reproduce the corpus.
- Live taxonomy XML/Datasets, exact Assembly/nuccore searches, full marker metadata except bases, independent genome Datasets and relevant primary-paper text were inspected.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- No graph node requires `just validate-products`. Full history validation was not run; no external target history reference or lifecycle promotion applies.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:18507` matches identifier, label, rank, parent, code and snapshot 2026-09-13. Synonym and retirement fields are empty. Complete native scientific-name row `data/catalog/ncbi_names-0000.jsonl.gz:38515` matches, with empty unique_name.

All six pinned ancestors match in order, ID, label and rank: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Campylobacterota 29547; unclassified Campylobacterota 122728.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103555&retmode=xml) confirms identity, lineage and code. [Taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103555) confirms root-inclusive ancestor IDs. Creation is 2 September 1999; update is 19 January 2005. No OtherNames or type-material assertion appears. Exact pinned type-material, merged-ID and dropped scans found no target row.

The unclassified position is carried without inferred ranks. SPECIES does not establish formal nomenclatural standing or a culture deposit; EXACT identifies this node, not all organisms sharing its host.

## Evidence

`data/taxa/PATHS.tsv:14603` and `curation/seed_scope.tsv:144153` uniquely agree on ID, stem and scope reason. The NCBITAXON attestation correctly counts one NAME.

No direct children occur in the complete pinned backbone. Exact BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw-inventory scans found no target row. Strain_count 0 agrees with inventory and subtree, not a claim of biological unculturability.

All three source manifests were parsed in full: raw extracted_at 2026-09-13T17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z. The newest-manifest rule at `src/taxonmech/seed.py:139` explains the seed timestamp. Attested source and scope reason match the event; hashes were not recomputed.

Exact nuccore search returned only UID 5901792. Complete [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=5901792) identifies `AF180319.1`, a 172-base partial 16S rRNA sequence, taxon:103555 and clone APG1Bstab8. It supplies no strain, deposit, BioSample, BioProject, assembly, explicit host, location or isolation_source qualifier.

The marker cites Campbell and Cary, AEM 67(1):110-117 (2001), PMID:11133434; an unpublished molecular-method comparison; and direct submission on 24 August 1999 from the University of Delaware. An unpublished title is not inspected experimental evidence.

The inspected [primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC92526/), DOI:10.1128/AEM.67.1.110-117.2001, includes AF180319 in its DGGE-fragment accession series. It supplies community/method provenance, not target-specific physiological or whole-genome evidence. The spirochete APG10 is a different clone, AF180309; its phenotype and abundance must not be transferred.

Exact Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103555/dataset_report) returned an empty object. These bounded checks do not prove global genome absence; a short marker is not a genome.

Before web search, all 28 fresh `kg-microbe-sources imodulondb datasets` rows were read through `uv run --offline --project ../../culturebotai-claw`. Initial sandbox DNS failed; the approved read-only retry succeeded. No covered organism matches and no gene/module is asserted. Component queries are not applicable; noncoverage is not negative biological evidence.

## Completeness

No consequential gap was established. Definitions, citations, nomenclature, mappings, strains and graphs are optional here. Marker/literature context is optional enrichment, not grounds to invent a strain or host CURIE.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched numeric-boundary 103555, exact label, stem and APG1Bstab8 punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All 20 matched rows were fully read: three applicable identity/scope rows and 17 unrelated numeric matches.

A separate AF180319/version scan found no rows in those roots. At both stages all five SOURCE.json files were independently parsed in full and history filenames searched without ignore filtering. Initial metadata matches were the BacDive request for native ID 103555 and a StrainInfo response byte count of 103555, neither a taxonomic assertion. The latter response object was separately read completely. No target history filename was found. An ignored-inclusive report filename search found no prior target report. Absence findings are bounded to these roots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, attestation, source count and SEEDED lifecycle are supported. No missing required representation was established.

## Recommended Edits

None required. Preserve generated YAML and SEEDED status.

Future enrichment belongs in maintained sources/extractors and inventories or tested `src/taxonmech/seed.py` changes. Scope changes belong in `curation/seed_scope.tsv`; taxonomy corrections belong upstream. Do not join another namespace's numerical ID or another clone's evidence.

## Follow-up Checks

For authorized enrichment, establish complete source chains for culture/genome associations, independently ground host identity and require clone-specific support for biological claims. Rerun target schema/strict checks followed by documented corpus reproduction/provenance gates. Keep taxon, host, clone, strain, deposit, marker, sample, run, assembly, genome and project identities distinct. No unresolved blocker requires enrichment now.

## Additional Notes

All candidate native JSON fields and TSV columns were read losslessly. Logical decompressed addresses:

- BacDive native row 27688/raw row 27689 is Corynebacterium pseudodiphtheriticum STI10121, taxon 37637, BacDive 103555, without a collection deposit or sequence.
- StrainInfo row 26713 is E. coli ATCC 23978, taxon 562, SI-ID38312/SI-DP103555. Row 31034 is But 24, SI-ID42831, with CIP 103555/SI-DP149174 classified as Bacillus viscosus 33023 and broader strain-level Bacillus 1386.
- StrainInfo row 129857 has KY103555 for Hanseniaspora uvarum CBS 2586, taxon 29833, SI-ID177788/SI-DP453857. Reading this collision did not reopen a Eukaryota review.
- CP103555 belongs to Klebsiella michiganensis 5088, taxon 1134687, GCA_024917295.1, SAMN28174081: BV-BRC shard 0000 rows 15880/15885 and GOLD analysis row 401931, Ga0608781/Gp0745353.
- MGBC103555 belongs to Lactobacillus hominis 1203033, GCA_948822745.1, SAMEA112377497: BV-BRC shard 0000 row 28873, GTDB shard 0011 row 14845 and GenBank shard 0060 row 33286.
- GTDB shard 0005 row 15585 matches scaffold N50 103555: Stenotrophomonas maltophilia UBA7712, taxon 40324, GCA_002482325.1.
- GenBank shard 0007 row 34806 is Salmonella enterica PNUSAS103555, taxon 28901, GCA_008795095.1, SAMN12875740. Shard 0065 row 9752 is Xanthomarina gelatinilytica MarMAG_103555, taxon 1137281, GCA_977611295.1, SAMEA120729229.
- AllTheBacteria row 6151 is E. coli O26:H11, DRR103555, SAMD00075898, ERZ25075537. Rows 1997382 and 2908150 match SeqKit-sum substrings: E. coli SAMN17833549/ERZ25882543 and Shigella flexneri SAMN41384064/ERZ26727946. Available FASTA, PASS filters and URLs establish no target relationship.

PMC initially presented a browser check; a subsequent canonical request returned the inspected article text. No conclusion relies on the failed retrieval.

Only this new report was written for this target. No YAML, inventory, generated product, earlier report, history or lifecycle state changed. Eukaryota records remain untouched. No paid research, external contact or GitHub mutation occurred.
