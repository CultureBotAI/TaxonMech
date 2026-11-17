# YAML Record Review: Vibrio sp. squidSkn_08

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/vibrio_sp_squidskn_08.yaml`
- Started UTC: 2026-10-07T03:18:04Z
- Finished UTC: 2026-10-07T03:20:00Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035437`, `Vibrio sp. squidSkn_08`: SPECIES in BACTERIA, parent `NCBITaxon:2614977`, code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, deposits, genomes, literature, discussions or graphs are asserted.

The YAML stays read-only. Maintained source inputs, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future changes, not generated artifacts.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/vibrio_sp_squidskn_08.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/vibrio_sp_squidskn_08.yaml --out /private/tmp/vsk08-strict.tsv`: exit 0, one file scanned, zero errors. Read the actual header-only TSV.
- Complete backbone, ancestor, path/scope, seven-inventory and attestation comparisons passed. These bounded checks are not a focused corpus-reproduction gate.
- Live taxonomy XML/Datasets, taxonomy browser, exact Assembly/nuccore searches, full marker metadata excluding bases and independent genome Datasets reads completed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- `just validate-products` has no applicable target graph node and was not run. No target DOI/PMID or external history reference applies. Full history validation was not run; no history event or lifecycle promotion occurred.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:222099` agrees on ID, exact label, rank, parent, code and snapshot 2026-09-13; synonyms and retirement are empty. Complete native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31579` agrees with no unique-name qualifier.

All ten pinned ancestor IDs, labels and ranks match: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Gammaproteobacteria 1236; Vibrionales 135623; Vibrionaceae 641; Vibrio 662; unclassified Vibrio 2614977.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035437&retmode=xml) agrees on identity and named lineage. [Taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035437) confirms all ancestor IDs including root. Creation is 23 May 2011, update 28 May 2011; no OtherNames/type-material assertion is supplied. Complete exact scans of pinned merged-ID, dropped and type-material tables found no target row.

The inspected [taxonomy browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1035437&lvl=3&mode=node) agrees and links one nucleotide record. NCBI species rank is not formal nomenclatural standing. EXACT grounding identifies this node, not a culture, host or genome.

## Evidence

Path row `data/taxa/PATHS.tsv:14590` and scope row `curation/seed_scope.tsv:322370` uniquely match the ID, stem and seed reason. The attestation correctly counts one NAME.

There are no direct children in the pinned backbone. Full exact scans of raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. Strain_count 0 agrees with the BacDive inventory and target subtree.

Fresh current-turn structured reads of all three complete manifests give extracted_at values raw 2026-09-13T17:50:44Z, ATB 17:54:04Z, StrainInfo 17:29:00Z. The previously inspected, unchanged newest-manifest rule at `src/taxonmech/seed.py:139` explains the 17:54:04Z seed event. Source list and scope reason agree. Hashes were not recomputed.

Exact nuccore search returned only UID 333798009. Full [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333798009) identifies `JF792727.1`, a 1,251-base partial 16S rRNA marker, strain squidSkn_08, taxon:1035437. Its literal host qualifier is Nototodarus gouldi; its geographic qualifier identifies Auckland Fish Market, North Island, New Zealand. This report preserves submitted host spelling without asserting an independently resolved host CURIE.

No tissue/isolation_source, culture deposit, BioSample, BioProject or assembly link appears in that marker metadata. Skn is not explicit tissue evidence. The unpublished Wollenberg/Rainey/Ruby bioluminescence-study reference supplies no DOI/PMID or inspected target phenotype result. A separate Wollenberg/Ruby direct submission dates to 7 April 2011, Wisconsin-Madison. The title does not establish luminescence; market location is not capture locality.

Exact Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035437/dataset_report) returned an empty object. These bounded checks do not establish universal genome absence; the partial marker is not a genome.

Before web search, consulted all 28 rows of the fresh current-turn `kg-microbe-sources imodulondb datasets` response through `uv run --offline --project ../../culturebotai-claw`. V. natriegens is distinct from squidSkn_08; no gene/module is asserted. No component query applies; noncoverage is not negative biological evidence.

## Completeness

Optional definitions, evidence, nomenclature, mappings, deposits and graphs need not be populated without applicable support. Marker host/location metadata is optional enrichment, not a missing required representation. Its strain qualifier is not an inventoried BacDive deposit.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched ID, full label, stem and strain punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All 56 matched lines were read fully: three applicable rows, ten unrelated BV-BRC rows, four unrelated GTDB rows, eighteen unrelated NCBI rows and twenty-one unrelated ATB rows.

A separate JF792727/version scan returned zero lines in those roots. At both stages all five SOURCE.json documents were parsed separately in full and history filenames searched without ignore filtering, with no additional match. These are bounded repository checks, not global absence claims.

Exact-label, punctuation, accession, strain/genome/culture, author and host web searches yielded taxonomy pages rather than an applicable inspected experiment or deposit chain. An indexed taxonomy snippet mentioned GloBI, but the fetched live browser page did not expose that link or any interaction evidence. No ecological claim was adopted from that snippet; GloBI interaction records were not independently checked. No consequential omission was established by the completed checks.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. An ERR run or PRJNA project number is not an NCBI taxonomy identity.

## Recommended Edits

None required. Preserve generated YAML and SEEDED state.

Future enrichment belongs in a maintained source/extractor and inventory, or tested harmonization changes in `src/taxonmech/seed.py`; scope changes belong in `curation/seed_scope.tsv`. Correct source/kg-microbe mappings upstream. Keep taxon, host, strain, deposit, marker, sample, assembly, genome, run and project identities distinct.

## Follow-up Checks

For later authorized curation, establish whole-accession source chains, rerun target schema/strict validators and then documented full-corpus reproduction/provenance gates. Require actual squidSkn_08 experiments before phenotype claims and explicit tissue evidence before skin-origin claims. Resolve any host CURIE independently and trace any future GloBI lead to its original observation. No unresolved blocker requires enrichment now.

## Additional Notes

All unrelated candidate rows were read losslessly.

Seven MAGs have `ERR1035437_bin.*_CONCOCT_v1.1_MAG` labels and project PRJEB52028; the embedded run number is not taxon 1035437. Their complete BV-BRC and NCBI addresses are:

| Assembly | Taxid | BioSample | BV-BRC file suffix:row | NCBI genbank-0059 row |
|---|---|---|---|---|
| GCA_937889595.1 | 77133 | SAMEA14037571 | 0027:10390 | 1028 |
| GCA_937902605.1 | 171953 | SAMEA14037572 | 0005:22563 | 2313 |
| GCA_937902785.1 | 257470 | SAMEA14037573 | 0014:43950 | 2330 |
| GCA_937888775.1 | 152507 | SAMEA14037574 | 0003:38295 | 948 |
| GCA_937910425.1 | 1798923 | SAMEA14037575 | 0006:43755 | 2653 |
| GCA_937881125.1 | 187319 | SAMEA14037576 | 0007:24774 | 666 |
| GCA_937889395.1 | 153809 | SAMEA14037577 | 0003:45216 | 1008 |

BV-BRC paths are `data/bvbrc/bvbrc-<suffix>.jsonl.gz`; NCBI path is `data/catalog/ncbi_genbank-0059.jsonl.gz`. These denote uncultured bacteria from distinct groups, not Vibrio; their contamination, fragmentation and other flags cannot be transferred to squidSkn_08.

Four complete GTDB rows concern the same unrelated MAGs: `data/catalog/gtdb_genomes-0013.jsonl.gz:19006` is GCA_937902605.1, `gtdb_genomes-0007.jsonl.gz:39508` is GCA_937889595.1, `gtdb_genomes-0000.jsonl.gz:9303` is GCA_937910425.1, and `gtdb_genomes-0015.jsonl.gz:12535` is GCA_937889395.1. All four are metagenome-derived GTDB representatives with unrelated classifications and soil-metagenome metadata.

`data/bvbrc/bvbrc-0018.jsonl.gz:45637-45639` are Pseudomonas sp. JS3066 genome IDs 3090665.3, .4 and .5, taxid 3090665, SAMN38088603, project PRJNA1035437, nucleotide accessions CP143312/CP143313. `data/catalog/ncbi_genbank-0033.jsonl.gz:49107` is the corresponding GCA_036328175.1 assembly. Project-number equality does not connect it to the target.

Ten complete NCBI rows are N. gonorrhoeae taxid/species_taxid 485, PRJNA317462. In `data/catalog/ncbi_genbank-0038.jsonl.gz`, rows 28730, 28731, 28732, 49201, 49210, 49580, 49582 and 49844 respectively contain GCA_042129225.1, GCA_042129245.1, GCA_042129265.1, GCA_042543265.1, GCA_042543445.1, GCA_042550845.1, GCA_042550885.1 and GCA_042556125.1, samples SAMN10354379, 78, 77, 70, 73, 75, 76 and 72 respectively. In `data/catalog/ncbi_genbank-0039.jsonl.gz`, rows 12 and 30 are GCA_042559485.1/SAMN10354371 and GCA_042559845.1/SAMN10354374.

All columns of twenty-one `data/catalog/allthebacteria.tsv.xz` rows were read: rows 141936-141945 are E. coli samples SAMEA110354370-379; rows 1503432-1503441 are N. gonorrhoeae samples SAMN10354370-79; row 1557650 is Salmonella sample SAMN11035437, run SRR8655883, no ENA assembly accession and an assembly-submission-error flag. Their runs, analyses, filters, checksums and URLs do not supply target provenance.

Only this new report was written. No YAML, inventory, generated product, prior report, history or lifecycle state was changed. No paid research, external contact or GitHub mutation occurred.
