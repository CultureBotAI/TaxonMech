# YAML Record Review: Vibrio sp. squidSkn_05

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/vibrio_sp_squidskn_05.yaml`
- Started UTC: 2026-10-07T03:11:52Z
- Finished UTC: 2026-10-07T03:13:19Z
- Verdict: pass

## Target

Read the full generated TaxonRecord for `NCBITaxon:1035435`, `Vibrio sp. squidSkn_05`: SPECIES in BACTERIA, parent `NCBITaxon:2614977`, genetic code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, deposits, genomes, literature, discussions or causal graphs are asserted.

This is an individual, read-only review except for the new report. Maintained source inputs, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future fixes, not generated YAML.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/vibrio_sp_squidskn_05.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/vibrio_sp_squidskn_05.yaml --out /private/tmp/vsk05-strict.tsv`: exit 0, one file, zero errors. Read the actual header-only TSV.
- Complete backbone, ancestor, seven-inventory, scope/path and attestation comparisons passed. These bounded checks are not a focused corpus-reproduction gate.
- Live taxonomy XML/Datasets, exact Assembly/nuccore searches, full sequence metadata excluding bases, and independent genome Datasets reads completed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- `just validate-products` has no applicable target graph node and was not run. No target DOI/PMID or external history reference applies. Full history validation was not run; no lifecycle promotion or history event was made.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:222097` agrees on ID, exact label, SPECIES rank, parent, code and snapshot 2026-09-13. Synonym and retirement fields are empty. Complete native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31577` agrees and has no unique-name qualifier.

All ten pinned ancestor IDs, labels and ranks match: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Gammaproteobacteria 1236; Vibrionales 135623; Vibrionaceae 641; Vibrio 662; unclassified Vibrio 2614977.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035435&retmode=xml) agrees on identity and named lineage. [Taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035435) confirms the full ancestor-ID chain including root. Creation is 23 May 2011, update 28 May 2011; no OtherNames/type-material assertion is supplied. Exact scans of pinned merged-ID, dropped and type-material tables found no target row.

NCBI species rank does not establish formal nomenclatural standing. EXACT grounding identifies this node, not a host, culture deposit or genome.

## Evidence

Path row `data/taxa/PATHS.tsv:14588` and scope row `curation/seed_scope.tsv:322368` uniquely agree with ID, stem and seed reason. The attestation correctly counts one NAME, not a genome or experiment.

There are no direct children in the pinned backbone. Complete exact scans of raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. Strain_count 0 agrees with the BacDive inventory throughout the target subtree.

Fresh current-turn complete manifest reads give extracted_at values raw 2026-09-13T17:50:44Z, ATB 17:54:04Z, StrainInfo 17:29:00Z. The inspected newest-manifest rule at `src/taxonmech/seed.py:139` explains the 17:54:04Z seed timestamp. Source list and exact scope reason agree; hashes were not recomputed.

Exact nuccore search returned only UID 333798007. Full [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333798007) identifies `JF792725.1`, a 1,251-base partial 16S rRNA marker, strain squidSkn_05, taxon:1035435. Its literal host qualifier is Nototodarus gouldi and its geographic qualifier identifies Auckland Fish Market, North Island, New Zealand. The submitted host spelling is preserved here without an independently resolved host CURIE.

No tissue/isolation_source, culture deposit, BioSample, BioProject or assembly link appears in that metadata. Skn does not independently establish skin isolation. The unpublished Wollenberg/Rainey/Ruby bioluminescence-study reference has no DOI/PMID or inspected squidSkn_05 experiment. A separate Wollenberg/Ruby direct submission is dated 7 April 2011, Wisconsin-Madison. A study title is not proof of luminescence; a market location does not establish capture locality.

Exact Assembly search returned zero with a phrase-not-found warning. The independent [genome Datasets request](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035435/dataset_report) returned an empty object. These are bounded checks, not universal genome-absence proof; the marker is not a genome.

Consulted all 28 rows of the fresh current-turn `kg-microbe-sources imodulondb datasets` result through `uv run --offline --project ../../culturebotai-claw` before web search. The initial sandbox DNS failure was resolved by an authorized read-only network retry. The V. natriegens datasets are not this target, which asserts no gene/module. No component query applies; noncoverage is not negative biological evidence.

## Completeness

Optional definitions, evidence, nomenclature, mappings, deposits and graphs need not be filled without relevant support. Marker host/location metadata is optional enrichment, not a missing required representation. A bare strain qualifier is not an inventoried BacDive culture.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched ID, full label, stem and strain punctuation variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All 34 matched lines were read in full: three applicable rows, fourteen unrelated NCBI rows and seventeen unrelated ATB rows.

A separate JF792725/version scan returned zero lines in the same roots. At both stages all five SOURCE.json documents were separately parsed in full and history filenames searched without ignore filtering, with no additional match. These searches are bounded, not absence claims about arbitrary files or all external resources.

Exact-label, punctuation-variant, accession, strain/genome/culture, author and host web searches yielded taxonomy listings rather than an applicable inspected experiment or deposit chain. Search snippets were not evidence. No consequential omission was established.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Matches in assembly, sample and run numbers do not identify this taxon.

## Recommended Edits

None required; preserve the generated record and SEEDED status.

Future enrichment belongs in a maintained source/extractor and inventory or tested harmonization logic in `src/taxonmech/seed.py`; scope changes belong in `curation/seed_scope.tsv`. Correct source/kg-microbe mappings upstream. Preserve distinctions among taxon, host, strain, culture deposit, marker, sample, assembly, genome, run and project.

## Follow-up Checks

For later authorized curation, establish explicit whole-accession source chains, rerun target schema/strict validators and then documented full-corpus reproduction/provenance gates. Require actual squidSkn_05 experimental evidence before phenotype claims, explicit tissue metadata before skin claims, and an independently resolved host identity before adding a host CURIE. No unresolved blocker requires enrichment now.

## Additional Notes

Full unrelated candidate rows were read losslessly.

`data/catalog/ncbi_genbank-0056.jsonl.gz:27298` is GCA_061035435.1, Ligilactobacillus salivarius taxid 1624, isolate 1937_1937H_C_15, SAMN60704084, PRJNA1464738, flagged as derived from a metagenome. Its accession contains the search digits.

`data/catalog/ncbi_genbank_historical-0001.jsonl.gz:21215-21216` contains replaced GCA_031035435.1 and .2. The current `data/catalog/ncbi_genbank-0028.jsonl.gz:43460` is GCA_031035435.3. All three are Klebsiella pneumoniae taxid 573, isolate 1922580, SAMN34998282, PRJNA288601. Historical replacement is not evidence of a target taxon merger.

Ten complete `data/catalog/ncbi_genbank-0038.jsonl.gz` rows are Neisseria gonorrhoeae taxid/species_taxid 485, PRJNA317462. Rows 49174, 49176, 49177, 49178, 49179, 49180, 49183, 49184, 49207 and 49208 respectively contain GCA_042542725.1, GCA_042542765.1, GCA_042542785.1, GCA_042542805.1, GCA_042542825.1, GCA_042542845.1, GCA_042542905.1, GCA_042542925.1, GCA_042543385.1 and GCA_042543405.1. Their respective samples are SAMN10354356, SAMN10354351, SAMN10354357, SAMN10354350, SAMN10354354, SAMN10354352, SAMN10354355, SAMN10354353, SAMN10354359 and SAMN10354358.

All columns of seventeen `data/catalog/allthebacteria.tsv.xz` rows were read:

- Rows 141921-141925 are E. coli samples SAMEA110354355-359, with respective runs ERR11813074, ERR11813076, ERR11813078, ERR11813080 and ERR11813082.
- Rows 1503412-1503421 concern N. gonorrhoeae samples SAMN10354350-59.
- Row 1557648 is Salmonella sample SAMN11035435, run SRR8655885, no ENA assembly accession and an assembly-submission-error flag.
- Row 1715528 is E. coli sample SAMN13140058, run SRR10354353, analysis ERZ25667080. The match is in the run number, not target taxonomy.

None of their run/analysis identifiers, filters, sequence checksums or URLs supplies target provenance.

Only this new report was written. No YAML, inventory, generated product, prior report, history or lifecycle state was changed. No paid research, external contact or GitHub mutation occurred.
