# YAML Record Review: Herbaspirillum sp. ZM319

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/herbaspirillum_sp_zm319.yaml`
- Started UTC: 2026-10-07T03:29:36Z
- Finished UTC: 2026-10-07T03:32:12Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035440`, `Herbaspirillum sp. ZM319`: SPECIES in BACTERIA, parent `NCBITaxon:2624150`, genetic code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, deposits, genomes, literature, discussions or graphs are asserted.

The YAML stays read-only. Maintained source inputs, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future changes, not generated artifacts.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/herbaspirillum_sp_zm319.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/herbaspirillum_sp_zm319.yaml --out /private/tmp/hz319-strict.tsv`: exit 0, one file scanned, zero errors. Read the actual header-only TSV.
- Complete backbone, ancestor, path/scope, seven-inventory and attestation comparisons passed. These bounded checks do not reproduce the corpus.
- Live taxonomy XML/Datasets, exact Assembly/nuccore searches, full marker metadata excluding bases and independent genome Datasets reads completed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- `just validate-products` has no applicable target graph node and was not run. No DOI/PMID or external history reference is asserted by the YAML. Full history validation was not run; no history event or lifecycle promotion occurred.
- Literature limitation: the optional soil-fertilization PDF lead could not be fetched. Web fetch timed out; `curl --fail --location --max-time 60 --output /private/tmp/hz319-paper.pdf https://cdn.sciengine.com/doi/pdfView/4DE937B1EDF04CAE9BCE2B7009DE8E74` ended with exit 6, host-resolution failure. DOI and journal landing-page attempts were also inaccessible. No PDF text, figure, table or full methods were independently inspected. `pdftotext` was not on the shell PATH; no installation was attempted.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:222102` agrees on ID, label, rank, parent, code and snapshot 2026-09-13; synonyms and retirement are empty. Complete native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31582` agrees with no unique-name qualifier.

All ten pinned ancestor IDs, labels and ranks match: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Oxalobacteraceae 75682; Herbaspirillum 963; unclassified Herbaspirillum 2624150.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035440&retmode=xml) agrees on identity and named lineage. [Taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035440) confirms all ancestor IDs including root. Creation is 23 May 2011, update 28 May 2011; no OtherNames/type-material assertion is supplied. Complete exact scans of pinned merged-ID, dropped and type-material tables found no target row.

NCBI species rank is not formal nomenclatural standing. EXACT grounding identifies this taxonomic node; it does not identify a named species, deposited culture or genome by implication.

## Evidence

Path row `data/taxa/PATHS.tsv:14593` and scope row `curation/seed_scope.tsv:322373` uniquely match the ID, stem and seed reason. The attestation correctly counts one NAME.

There are no direct children in the pinned backbone. Full exact scans of raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. Strain_count 0 agrees with the BacDive inventory and target subtree.

Fresh current-turn structured reads of all three complete manifests give extracted_at values raw 2026-09-13T17:50:44Z, ATB 17:54:04Z, StrainInfo 17:29:00Z. The inspected newest-manifest rule at `src/taxonmech/seed.py:139` explains the 17:54:04Z seed event. Source list and scope reason agree. Hashes were not recomputed.

Exact nuccore search returned only UID 333797943. Full [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333797943) identifies `JF792360.1`, a 1,360-base partial 16S rRNA marker, strain ZM319, taxon:1035440. Its literal host is Zea mays and its geographic qualifier is China. No independently resolved host CURIE is asserted here.

The Luo/Sui reference concerns nitrogen levels and maize-rhizosphere bacterial diversity, but is marked unpublished and supplies no DOI/PMID or inspected ZM319 response result. A separate direct submission dates to 7 April 2011, China Agricultural University. No isolation_source, tissue, culture deposit, BioSample, BioProject or assembly link appears in the complete marker metadata. Neither the study title nor the genus assignment proves nitrogen fixation, nitrogen-response phenotype, plant-growth promotion or a specific root compartment.

Exact Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035440/dataset_report) returned an empty object. These bounded checks do not establish universal genome absence; the partial marker is not a genome.

Before web search, consulted all 28 rows of the fresh current-turn `kg-microbe-sources imodulondb datasets` response through `uv run --offline --project ../../culturebotai-claw`. Herbaspirillum is not covered and no gene/module is asserted. No component query applies; noncoverage is not negative biological evidence.

## Completeness

Optional definitions, evidence, nomenclature, mappings, deposits and graphs need not be populated without applicable support. Marker host/location metadata is optional enrichment, not a missing required representation. Its strain qualifier is not an inventoried culture deposit.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched ID, full label, stem and strain punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All 33 matched lines were read fully: three applicable rows, one unrelated GTDB row, eleven unrelated NCBI assembly rows and eighteen unrelated ATB rows.

A separate JF792360/version scan returned zero lines in those roots. At both stages all five SOURCE.json documents were parsed separately in full and history filenames searched without ignore filtering, with no additional match. These are bounded repository checks, not global absence claims.

Web searches using the exact label, strain, accession and soil/fertilization terms found taxonomy and one potentially relevant paper. The paper is an unresolved optional enrichment lead, not inspected support for a new biological claim. The pass verdict covers the existing taxonomy-only seed and completed checks, not literature exhaustiveness. No missing required representation was established.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the existing record. Literature access is a review limitation, not evidence that a seeded field is wrong.

## Recommended Edits

None required. Preserve generated YAML and SEEDED state.

Future enrichment belongs in a maintained source/extractor and inventory, or tested harmonization changes in `src/taxonmech/seed.py`; scope changes belong in `curation/seed_scope.tsv`. Correct source/kg-microbe mappings upstream. Keep taxon, host, strain, deposit, marker, sample, assembly, genome, run and project identities distinct.

## Follow-up Checks

Retrieve the optional Huang et al. paper when its primary host is accessible. Verify its bibliographic identity, amplicon classification method, sequence/reference accessions and target-specific results before deciding whether any taxon-level ecological enrichment is supported. Do not convert an OTU/community abundance association into a pure-strain phenotype, nitrogen fixation or crop-yield mechanism.

For later authorized curation, establish whole-accession source chains, rerun target schema/strict validators and then documented full-corpus reproduction/provenance gates. Resolve host CURIEs independently. No unresolved blocker affects the current taxonomy claims.

## Additional Notes

All unrelated repository candidates were read losslessly.

`data/catalog/ncbi_genbank-0009.jsonl.gz:6553` is GCA_010354405.1, Campylobacter jejuni/197, strain PNUSAC012435, SAMN13005575, PRJNA239251. Its accession merely contains the target digits.

`data/catalog/ncbi_genbank-0061.jsonl.gz:16180` and `data/catalog/gtdb_genomes-0001.jsonl.gz:45519` concern GCA_949372535.1, uncultured Woeseiaceae bacterium/1983305, SAMEA112743517, PRJEB58071, isolate FRAM_WSC20_S10_BML_bin_28_1. The match is genome length 1035440, not taxid. GTDB places this seawater MAG in UBA1847 sp018699395 and marks it non-representative; it is not Herbaspirillum.

Nine complete NCBI rows are N. gonorrhoeae taxid 485, PRJNA317462. In `data/catalog/ncbi_genbank-0038.jsonl.gz`, rows 28786, 49366, 49488, 49489, 49504, 49509, 49517 and 49518 respectively identify GCA_042130335.1, GCA_042546565.1, GCA_042549005.1, GCA_042549025.1, GCA_042549325.1, GCA_042549425.1, GCA_042549585.1 and GCA_042549605.1; their samples are SAMN10354401, 03, 08, 07, 06, 05, 00 and 02 respectively. `data/catalog/ncbi_genbank-0039.jsonl.gz:91` is GCA_042561065.1/SAMN10354409.

All columns of eighteen `data/catalog/allthebacteria.tsv.xz` rows were read: 141965-141972 are E. coli samples SAMEA110354400, 401, 403 and 405-409 with assorted contamination, contig-count, N50 or sylph flags; 1503461-1503469 are N. gonorrhoeae samples SAMN10354400-403 and 405-409; 1557653 is Salmonella sample SAMN11035440, run SRR8655886, no ENA assembly accession and an assembly-submission-error flag. Their runs, analyses, filters, checksums and URLs do not supply target provenance.

The [unretrieved PDF lead](https://cdn.sciengine.com/doi/pdfView/4DE937B1EDF04CAE9BCE2B7009DE8E74) is indexed as Huang Ruilin, Zhang Na, Sun Bo and Liang Yuting, Community Structure of Burkholderiales and Its Diversity in Typical Maize Rhizosphere Soil, Acta Pedologica Sinica 57(4):975-985 (2020), candidate DOI `10.11766/trxb201901040008`. Its search excerpt mentions ZM319 in a community-sequencing/fertilization context. Those indexed details remain leads, not independently inspected paper evidence. No phenotype, effect size, p-value, treatment recommendation or new citation was inserted into the record.

Only this new report was written. No YAML, inventory, generated product, prior report, history or lifecycle state was changed. No paid research, external contact or GitHub mutation occurred.
