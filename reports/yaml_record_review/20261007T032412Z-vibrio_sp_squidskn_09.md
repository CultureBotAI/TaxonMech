# YAML Record Review: Vibrio sp. squidSkn_09

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/vibrio_sp_squidskn_09.yaml`
- Started UTC: 2026-10-07T03:21:06Z
- Finished UTC: 2026-10-07T03:24:12Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035438`, `Vibrio sp. squidSkn_09`: SPECIES in BACTERIA, parent `NCBITaxon:2614977`, genetic code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, deposits, genomes, literature, discussions or graphs are asserted.

The YAML stays read-only. Maintained source inputs, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future changes, not generated artifacts.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/vibrio_sp_squidskn_09.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/vibrio_sp_squidskn_09.yaml --out /private/tmp/vsk09-strict.tsv`: exit 0, one file scanned, zero errors. Read the actual header-only TSV.
- Complete backbone, ancestor, path/scope, seven-inventory and attestation comparisons passed. These bounded checks are not a focused corpus-reproduction gate.
- Live taxonomy XML/Datasets, exact Assembly/nuccore searches, full marker metadata excluding bases and independent genome Datasets reads completed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- `just validate-products` has no applicable target graph node and was not run. No target DOI/PMID or external history reference applies. Full history validation was not run; no history event or lifecycle promotion occurred.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:222100` agrees on ID, exact label, rank, parent, code and snapshot 2026-09-13; synonyms and retirement are empty. Complete native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31580` agrees with no unique-name qualifier.

All ten pinned ancestor IDs, labels and ranks match: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Gammaproteobacteria 1236; Vibrionales 135623; Vibrionaceae 641; Vibrio 662; unclassified Vibrio 2614977.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035438&retmode=xml) agrees on identity and named lineage. [Taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035438) confirms all ancestor IDs including root. Creation is 23 May 2011, update 28 May 2011; no OtherNames/type-material assertion is supplied. Complete exact scans of pinned merged-ID, dropped and type-material tables found no target row.

NCBI species rank is not formal nomenclatural standing. EXACT grounding identifies this taxonomic node, not a culture, host or genome.

## Evidence

Path row `data/taxa/PATHS.tsv:14591` and scope row `curation/seed_scope.tsv:322371` uniquely match the ID, stem and seed reason. The attestation correctly counts one NAME.

There are no direct children in the pinned backbone. Full exact scans of raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. Strain_count 0 agrees with the BacDive inventory and target subtree.

Fresh current-turn structured reads of all three complete manifests give extracted_at values raw 2026-09-13T17:50:44Z, ATB 17:54:04Z, StrainInfo 17:29:00Z. The previously inspected, unchanged newest-manifest rule at `src/taxonmech/seed.py:139` explains the 17:54:04Z seed event. Source list and scope reason agree. Hashes were not recomputed.

Exact nuccore search returned only UID 333798010. Full [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333798010) identifies `JF792728.1`, a 1,251-base partial 16S rRNA marker, strain squidSkn_09, taxon:1035438. Its literal host qualifier is Nototodarus gouldi; its geographic qualifier identifies Auckland Fish Market, North Island, New Zealand. This report preserves submitted host spelling without asserting an independently resolved host CURIE.

No tissue/isolation_source, culture deposit, BioSample, BioProject or assembly link appears in that marker metadata. Skn is not explicit tissue evidence. The unpublished Wollenberg/Rainey/Ruby bioluminescence-study reference supplies no DOI/PMID or inspected target phenotype result. A separate Wollenberg/Ruby direct submission dates to 7 April 2011, Wisconsin-Madison. The title does not establish luminescence; market location is not capture locality.

Exact Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035438/dataset_report) returned an empty object. These bounded checks do not establish universal genome absence; the partial marker is not a genome.

Before web search, consulted all 28 rows of the fresh current-turn `kg-microbe-sources imodulondb datasets` response through `uv run --offline --project ../../culturebotai-claw`. V. natriegens is distinct from squidSkn_09; no gene/module is asserted. No component query applies; noncoverage is not negative biological evidence.

## Completeness

Optional definitions, evidence, nomenclature, mappings, deposits and graphs need not be populated without applicable support. Marker host/location metadata is optional enrichment, not a missing required representation. Its strain qualifier is not an inventoried BacDive deposit.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched ID, full label, stem and strain punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All 43 matched lines were read fully: three applicable rows, three unrelated BV-BRC rows, two unrelated GTDB rows, fourteen unrelated NCBI rows and twenty-one unrelated ATB rows.

A separate JF792728/version scan returned zero lines in those roots. At both stages all five SOURCE.json documents were parsed separately in full and history filenames searched without ignore filtering, with no additional match. These are bounded repository checks, not global absence claims.

Exact-label, punctuation, accession, strain/genome/culture, author and host web searches yielded taxonomy listings rather than an applicable inspected experiment or deposit chain. No consequential omission was established by the completed checks.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. An embedded run, sample or accession number is not an NCBI taxonomy identity.

## Recommended Edits

None required. Preserve generated YAML and SEEDED state.

Future enrichment belongs in a maintained source/extractor and inventory, or tested harmonization changes in `src/taxonmech/seed.py`; scope changes belong in `curation/seed_scope.tsv`. Correct source/kg-microbe mappings upstream. Keep taxon, host, strain, deposit, marker, sample, assembly, genome, run and project identities distinct.

## Follow-up Checks

For later authorized curation, establish whole-accession source chains, rerun target schema/strict validators and then documented full-corpus reproduction/provenance gates. Require actual squidSkn_09 experiments before phenotype claims and explicit tissue evidence before skin-origin claims. Resolve any host CURIE independently. No unresolved blocker requires enrichment now.

## Additional Notes

All unrelated candidate rows were read losslessly.

Three unrelated MAGs have `ERR1035438_bin.*_CONCOCT_v1.1_MAG` labels and project PRJEB52028. The embedded run number is not taxon 1035438:

| Assembly | Organism / taxid | BioSample | BV-BRC suffix:row | NCBI genbank-0059 row |
|---|---|---|---|---|
| GCA_937911015.1 | uncultured archaeon / 115547 | SAMEA14037578 | 0000:19442 | 2711 |
| GCA_937881055.1 | uncultured Acidimicrobiaceae / 410722 | SAMEA14037579 | 0020:7811 | 660 |
| GCA_937902985.1 | uncultured Myxococcales / 253830 | SAMEA14037580 | 0014:40950 | 2350 |

BV-BRC paths are `data/bvbrc/bvbrc-<suffix>.jsonl.gz`; NCBI path is `data/catalog/ncbi_genbank-0059.jsonl.gz`. The archaeal assembly's contamination/fragmentation flags do not concern the target.

Two complete GTDB rows concern these unrelated soil-metagenome MAGs: `data/catalog/gtdb_genomes-0017.jsonl.gz:27662` is GCA_937881055.1, representative RAAP-2 sp937881055; `data/catalog/gtdb_genomes-0007.jsonl.gz:12637` is GCA_937902985.1, representative Palsa-1150 sp937902985.

`data/catalog/ncbi_genbank-0009.jsonl.gz:6552` is GCA_010354385.1, Listeria monocytogenes taxid 1639, strain CFSAN093426, SAMN13996881, PRJNA215355. Its assembly accession merely contains the target digits.

Ten complete rows in `data/catalog/ncbi_genbank-0038.jsonl.gz` are N. gonorrhoeae taxid 485, PRJNA317462:

| Row | Assembly | BioSample |
|---|---|---|
| 28765 | GCA_042129925.1 | SAMN10354380 |
| 28767 | GCA_042129965.1 | SAMN10354381 |
| 28808 | GCA_042130785.1 | SAMN10354388 |
| 28810 | GCA_042130825.1 | SAMN10354389 |
| 49562 | GCA_042550485.1 | SAMN10354386 |
| 49563 | GCA_042550505.1 | SAMN10354387 |
| 49564 | GCA_042550525.1 | SAMN10354385 |
| 49565 | GCA_042550545.1 | SAMN10354383 |
| 49576 | GCA_042550765.1 | SAMN10354384 |
| 49577 | GCA_042550785.1 | SAMN10354382 |

All columns of twenty-one `data/catalog/allthebacteria.tsv.xz` rows were read: rows 141946-141955 are E. coli samples SAMEA110354380-389; row 141951 has unknown sylph species and SYLPH_RESULTS_FAIL flags. Rows 1503442-1503451 are N. gonorrhoeae samples SAMN10354380-89. Row 1557651 is Salmonella sample SAMN11035438, run SRR8655888, no ENA assembly accession and an assembly-submission-error flag. Their runs, analyses, filters, checksums and URLs do not supply target provenance.

Only this new report was written. No YAML, inventory, generated product, prior report, history or lifecycle state was changed. No paid research, external contact or GitHub mutation occurred.
