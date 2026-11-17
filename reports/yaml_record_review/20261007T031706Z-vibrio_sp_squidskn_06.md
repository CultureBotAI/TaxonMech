# YAML Record Review: Vibrio sp. squidSkn_06

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/vibrio_sp_squidskn_06.yaml`
- Started UTC: 2026-10-07T03:15:10Z
- Finished UTC: 2026-10-07T03:17:06Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035436`, `Vibrio sp. squidSkn_06`: SPECIES in BACTERIA, parent `NCBITaxon:2614977`, code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. Synonyms, nomenclature, mappings, deposits, genomes, literature, discussions and graphs are not asserted.

Review leaves generated YAML read-only. Future fixes belong in maintained source inputs, `curation/seed_scope.tsv` or `src/taxonmech/seed.py`.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/vibrio_sp_squidskn_06.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/vibrio_sp_squidskn_06.yaml --out /private/tmp/vsk06-strict.tsv`: exit 0, one file scanned, zero errors. Read the actual header-only TSV.
- Complete backbone, ancestor, scope/path, seven-inventory and attestation comparisons passed. These bounded source checks do not reproduce the full corpus.
- Live taxonomy XML/Datasets, exact Assembly/nuccore searches, full marker metadata excluding bases and independent genome Datasets reads completed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- `just validate-products` has no applicable target graph node and was not run. No target DOI/PMID or external history reference applies. Full history validation was not run; no history event or status promotion was made.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:222098` agrees on ID, exact label, rank, parent, code and snapshot 2026-09-13. Synonym and retirement fields are empty. Native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31578` agrees with no unique-name qualifier.

All ten pinned ancestor IDs, labels and ranks match: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Gammaproteobacteria 1236; Vibrionales 135623; Vibrionaceae 641; Vibrio 662; unclassified Vibrio 2614977.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035436&retmode=xml) agrees on identity and named lineage; [taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035436) confirms all ancestor IDs including root. Creation is 23 May 2011 and update 28 May 2011. No OtherNames/type-material assertion is supplied. Complete exact scans of pinned merged-ID, dropped and type-material tables found no target row.

NCBI species rank does not establish formal nomenclatural standing. EXACT grounding identifies this node, not a host, culture deposit, marker or genome.

## Evidence

Path row `data/taxa/PATHS.tsv:14589` and scope row `curation/seed_scope.tsv:322369` uniquely match the ID, stem and seed reason. The source correctly attests one NAME.

No direct children occur in the pinned backbone. Full exact scans of raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. Strain_count 0 agrees with the BacDive inventory throughout this target subtree.

Fresh structured reads of all three complete manifests give extracted_at values raw 2026-09-13T17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z. The previously inspected, unchanged newest-manifest rule at `src/taxonmech/seed.py:139` explains the 17:54:04Z seed event. Source list and scope reason agree; hashes were not recomputed.

Exact nuccore search returned only UID 333798008. Full [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333798008) identifies `JF792726.1`, a 1,251-base partial 16S rRNA marker, strain squidSkn_06, taxon:1035436. The literal submitted host is Nototodarus gouldi, and the geographic qualifier identifies Auckland Fish Market, North Island, New Zealand. The host spelling is preserved without asserting an independently resolved host CURIE.

No tissue/isolation_source, culture deposit, BioSample, BioProject or assembly link appears in that marker metadata. Skn does not independently establish skin isolation. The unpublished Wollenberg/Rainey/Ruby bioluminescence-study reference provides no DOI/PMID or inspected squidSkn_06 phenotype result. A separate Wollenberg/Ruby direct submission is dated 7 April 2011, Wisconsin-Madison. A study title does not establish luminescence, and market location is not capture locality.

Exact Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets request](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035436/dataset_report) returned an empty object. These bounded checks do not establish universal genome absence; a partial marker is not a genome.

Before web search, read all 28 rows of the fresh `kg-microbe-sources imodulondb datasets` response, obtained through `uv run --offline --project ../../culturebotai-claw` with authorized read-only network access. V. natriegens is distinct from the target, which asserts no gene/module. No component query applies; noncoverage is not negative biological evidence.

## Completeness

Optional definitions, evidence, nomenclature, mappings, deposits and graphs need not be filled without applicable support. Marker host/location metadata is optional enrichment, not a missing required representation. Its bare strain qualifier does not create an inventoried BacDive culture.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched ID, complete label, stem and strain punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All 38 matched lines were read fully: three applicable rows, one unrelated GTDB row, eleven unrelated NCBI rows and twenty-three unrelated ATB rows.

A separate JF792726/version scan returned zero lines in the same roots. All five SOURCE.json documents were separately parsed in full and history filenames searched without ignore filtering at both stages, with no additional match. These bounded searches do not establish absence from arbitrary files or all external resources.

Exact-label, punctuation, accession, strain/genome/culture, author and host web searches yielded taxonomy listings rather than an applicable inspected experiment or deposit chain. Snippets were not evidence. No consequential omission was established.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Lengths, sample numbers and checksum substrings do not establish target identity.

## Recommended Edits

None required; preserve generated YAML and SEEDED state.

Future enrichment belongs to a maintained source/extractor and inventory or tested harmonization changes in `src/taxonmech/seed.py`; scope edits belong in `curation/seed_scope.tsv`. Fix source/kg-microbe mappings upstream. Keep taxon, host, strain, deposit, marker, sample, genome, assembly, run and project identities distinct.

## Follow-up Checks

For later authorized curation, establish whole-accession provenance, rerun the target schema/strict commands and then documented full-corpus reproduction/provenance gates. Require actual squidSkn_06 experiments for phenotype claims, explicit tissue metadata for skin origin, and a separately resolved host identity before adding a host CURIE. No unresolved blocker requires enrichment now.

## Additional Notes

All unrelated candidate rows were read losslessly.

`data/catalog/gtdb_genomes-0001.jsonl.gz:1260` and `data/catalog/ncbi_genbank-0000.jsonl.gz:34272` identify GCA_000995295.1, Candidatus Peregrinibacteria bacterium GW2011_GWE2_39_6, taxid 1619064, SAMN03319484, PRJNA273161. The match is total genome length 1035436, not target taxonomy; its aquifer-sediment metadata cannot be transferred.

`data/catalog/ncbi_genbank-0009.jsonl.gz:6551` is GCA_010354365.1, Campylobacter coli taxid 195, FSIS12028248, SAMN13977788, PRJNA287430, matching accession digits.

Nine full `data/catalog/ncbi_genbank-0038.jsonl.gz` rows are Neisseria gonorrhoeae taxid/species_taxid 485, PRJNA317462. Rows 28726, 28728, 28729, 28734, 49200, 49203, 49204, 49205 and 49206 respectively contain GCA_042129145.1, GCA_042129185.1, GCA_042129205.1, GCA_042129305.1, GCA_042543245.1, GCA_042543305.1, GCA_042543325.1, GCA_042543345.1 and GCA_042543365.1. Their respective samples are SAMN10354368, SAMN10354367, SAMN10354366, SAMN10354369, SAMN10354364, SAMN10354363, SAMN10354362, SAMN10354360 and SAMN10354361.

All columns of twenty-three `data/catalog/allthebacteria.tsv.xz` rows were read:

- Rows 141926-141935 concern E. coli samples SAMEA110354360-369. Row 141935 carries quality-filter failures; these concern that unrelated assembly.
- Rows 1503422-1503431 concern N. gonorrhoeae samples SAMN10354360-69, including sample SAMN10354365 not among the nine NCBI hits.
- Row 1557649 is Salmonella sample SAMN11035436, run SRR8655882, no ENA assembly accession and an assembly-submission-error flag.
- Row 1735002 is C. jejuni sample SAMN13413588, run SRR25376991, analysis ERZ26399866; the digits occur inside its SeqKit checksum.
- Row 3173605 is K. pneumoniae sample SAMN46375949, run SRR32146497, analysis ERZ27188864; again the match is inside the checksum.

None of these rows' run/analysis IDs, filters, checksums or URLs supplies target provenance.

Only this new report was written. No YAML, inventory, generated product, prior report, history or lifecycle state was changed. No paid research, external contact or GitHub mutation occurred.
