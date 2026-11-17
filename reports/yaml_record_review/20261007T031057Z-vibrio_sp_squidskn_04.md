# YAML Record Review: Vibrio sp. squidSkn_04

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/vibrio_sp_squidskn_04.yaml`
- Started UTC: 2026-10-07T03:09:34Z
- Finished UTC: 2026-10-07T03:10:57Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1035434`, `Vibrio sp. squidSkn_04`. It asserts SPECIES rank in BACTERIA, parent `NCBITaxon:2614977`, genetic code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. Synonyms, nomenclature, mappings, deposits, genomes, literature, discussions and causal graphs are not asserted.

The record remains read-only. Maintained source inputs, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future changes; generated YAML does not.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/vibrio_sp_squidskn_04.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/vibrio_sp_squidskn_04.yaml --out /private/tmp/vsk04-strict.tsv`: exit 0, one file, zero errors. Read the actual header-only TSV.
- Complete backbone, ancestor, seven-inventory, path/scope and attestation comparisons passed. These bounded checks do not reproduce the full corpus.
- Live taxonomy XML/Datasets, exact Assembly/nuccore searches, full marker metadata excluding bases and independent genome Datasets reads completed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- `just validate-products` has no applicable target graph node and was not run. No target DOI/PMID or external history reference applies. Full history validation was not run; no history event or lifecycle promotion occurred.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:222096` matches ID, exact label, rank, parent, code and snapshot 2026-09-13. All synonym and retirement fields are empty. Native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31576` agrees and has an empty unique-name qualifier.

All ten ancestor IDs, labels and ranks agree with the pinned backbone: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Gammaproteobacteria 1236; Vibrionales 135623; Vibrionaceae 641; Vibrio 662; unclassified Vibrio 2614977.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035434&retmode=xml) confirms identity and named lineage; [taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035434) confirms the ancestor chain including root. Creation is 23 May 2011, update 28 May 2011; no OtherNames/type-material assertion is supplied. Complete exact scans of the pinned merged-ID, dropped and type-material tables found no target row.

NCBI species rank does not imply formal nomenclatural standing. EXACT grounding denotes the taxonomy node, not a host, culture, marker or genome.

## Evidence

Path row `data/taxa/PATHS.tsv:14587` and scope row `curation/seed_scope.tsv:322367` uniquely match ID, stem and seed reason. The source assertion correctly counts one NAME.

The pinned backbone has no direct children. Full exact scans of raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. Strain_count 0 agrees with the BacDive inventory across this target subtree.

Fresh current-turn full manifest reads give raw extracted_at 2026-09-13T17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z. The inspected newest-manifest rule at `src/taxonmech/seed.py:139` explains the 17:54:04Z seed event. Source list and exact scope reason agree. Hashes were not recomputed.

Exact nuccore search returned only UID 333798006. Full [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333798006) identifies `JF792724.1`, a 1,251-base partial 16S rRNA marker, strain squidSkn_04, taxon:1035434. The literal host qualifier is Nototodarus gouldi; the geographic qualifier identifies Auckland Fish Market, North Island, New Zealand. This report preserves the submitted host spelling without asserting an independently resolved host taxonomy.

No isolation_source, tissue, culture deposit, BioSample, BioProject or assembly link appears in the marker metadata. Skn is not an explicit skin-isolation qualifier. The unpublished Wollenberg/Rainey/Ruby bioluminescence-study reference provides no DOI/PMID or inspected target phenotype result. A separate Wollenberg/Ruby direct submission is dated 7 April 2011, Wisconsin-Madison. The study title does not establish luminescence, and the market location is not a capture-at-sea location.

Exact Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035434/dataset_report) returned an empty object. These bounded checks do not establish universal genome absence; a marker is not a genome.

Before web search, consulted all 28 rows of the fresh current-turn `kg-microbe-sources imodulondb datasets` result through `uv run --offline --project ../../culturebotai-claw`. The initial sandbox DNS failure was resolved by an authorized read-only network retry. V. natriegens is not this target, and no target gene/module is asserted. No component query applies; noncoverage is not negative biological evidence.

## Completeness

Optional definitions, evidence, nomenclature, mappings, deposits and graphs need not be populated without relevant support. The marker host/location is optional enrichment, not a missing required representation. Its strain qualifier does not create an inventoried BacDive strain.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched ID, full label, stem and strain punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All 25 matched lines were read in full: three applicable rows, eleven unrelated NCBI rows and eleven unrelated ATB rows.

A separate JF792724/version scan returned zero lines in those roots. All five SOURCE.json documents were parsed independently in full and history filenames searched without ignore filtering at both stages; no additional match was found. These are bounded searches, not claims about all external resources or arbitrary repository paths.

Exact-label, punctuation, accession, strain/genome/culture, author and host web searches returned taxonomy listings rather than an applicable inspected experiment or deposit chain. Snippets were not evidence. No consequential omission was established.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Numeric accession matches concern other taxa.

## Recommended Edits

None required. Preserve generated YAML and SEEDED status.

Any future enrichment belongs to a maintained source/extractor and inventory, or tested harmonization changes in `src/taxonmech/seed.py`; scope changes belong in `curation/seed_scope.tsv`. Fix upstream source/kg-microbe mappings at their owner. Keep taxon, host, strain, deposit, marker, sample, genome, assembly, run and project identities distinct.

## Follow-up Checks

For later authorized curation, resolve explicit whole-accession source chains, rerun the target schema/strict commands and then documented full-corpus reproduction/provenance gates. Require actual squidSkn_04 experiments before phenotype claims and explicit tissue evidence before assigning a skin origin. Resolve the host independently if adding a host CURIE. No unresolved blocker requires enrichment now.

## Additional Notes

All unrelated candidate rows were read completely.

`data/catalog/ncbi_genbank-0009.jsonl.gz:6550` is GCA_010354345.1, Campylobacter jejuni taxid 197, strain PNUSAC012446, SAMN13005581, PRJNA239251. Its accession contains the numeric search substring.

Ten full rows in `data/catalog/ncbi_genbank-0038.jsonl.gz` are Neisseria gonorrhoeae taxid/species_taxid 485, PRJNA317462. Rows 26221, 26224, 26226, 28720, 28721, 28724, 28725, 28727, 49360 and 49361 respectively contain GCA_042078465.1, GCA_042078525.1, GCA_042078565.1, GCA_042129015.1, GCA_042129045.1, GCA_042129105.1, GCA_042129125.1, GCA_042129165.1, GCA_042546445.1 and GCA_042546465.1. Their respective samples are SAMN10354342, SAMN10354341, SAMN10354340, SAMN10354345, SAMN10354346, SAMN10354347, SAMN10354344, SAMN10354343, SAMN10354349 and SAMN10354348.

All columns of `data/catalog/allthebacteria.tsv.xz:1503402-1503411` concern N. gonorrhoeae samples SAMN10354340-49. Row 1557647 concerns Salmonella sample SAMN11035434, run SRR8655884, no ENA assembly accession and an assembly-submission-error flag. None of these run/analysis identifiers, filters, sequence checksums or URLs supplies target provenance.

Only this new report was written. No YAML, inventory, generated product, prior report, history or lifecycle state was changed. No paid research, external contact or GitHub mutation occurred.
