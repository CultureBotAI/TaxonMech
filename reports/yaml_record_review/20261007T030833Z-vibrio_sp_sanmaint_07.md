# YAML Record Review: Vibrio sp. sanmaInt_07

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/vibrio_sp_sanmaint_07.yaml`
- Started UTC: 2026-10-07T03:06:32Z
- Finished UTC: 2026-10-07T03:08:33Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1035433`, `Vibrio sp. sanmaInt_07`: SPECIES in BACTERIA, parent `NCBITaxon:2614977`, genetic code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, deposits, genomes, literature, discussions or causal graphs are asserted.

Review is read-only except for this new report. Future fixes belong in maintained source inputs, `curation/seed_scope.tsv` or `src/taxonmech/seed.py`, not generated YAML.

## Validation

Command prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/vibrio_sp_sanmaint_07.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/vibrio_sp_sanmaint_07.yaml --out /private/tmp/vsm07-strict.tsv`: exit 0, one file, zero errors. Read the actual header-only TSV.
- Complete backbone, lineage, scope/path, seven-inventory and attestation comparisons passed. These are bounded source comparisons, not a focused corpus-reproduction gate.
- Live taxonomy XML/Datasets, exact Assembly/nuccore searches, full marker metadata excluding bases, and independent genome Datasets reads completed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- `just validate-products` has no applicable target graph node and was not run. No target DOI/PMID or external history reference applies. Full history validation was not run. No lifecycle promotion or history event was made.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:222095` agrees on ID, label, SPECIES rank, parent, code and snapshot 2026-09-13; synonym and retirement fields are empty. Complete native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31575` agrees, including the case-sensitive label sanmaInt_07 and empty unique-name qualifier.

All ten pinned ancestor IDs, labels and ranks match: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Gammaproteobacteria 1236; Vibrionales 135623; Vibrionaceae 641; Vibrio 662; unclassified Vibrio 2614977.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035433&retmode=xml) agrees on identity and named lineage; [taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035433) confirms all ancestor IDs including root. Creation is 23 May 2011 and update 28 May 2011. No OtherNames/type-material assertion is supplied. Exact scans of the pinned merged, dropped and type-material tables found no target row.

NCBI species rank does not establish formal nomenclatural standing. EXACT grounding identifies this taxonomy node, not a culture deposit or genome.

## Evidence

Path row `data/taxa/PATHS.tsv:14586` and scope row `curation/seed_scope.tsv:322366` uniquely agree with ID, stem and seed reason. The NCBITAXON assertion is one NAME, not a genome or experimental count.

The pinned backbone has no direct children. Full exact scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories found no target row. Strain_count 0 agrees with the BacDive inventory and target subtree; a marker strain qualifier is not an inventoried culture.

Fresh complete manifest reads give extracted_at values raw 2026-09-13T17:50:44Z, ATB 17:54:04Z, StrainInfo 17:29:00Z. The inspected newest-manifest rule at `src/taxonmech/seed.py:139` explains the 17:54:04Z seed event. Source list and scope reason agree; hashes were not recomputed.

Exact nuccore search returned only UID 333797991. Complete [GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=333797991) identifies `JF792709.1`, a 1,251-base partial 16S rRNA marker, strain sanmaInt_07, taxon:1035433. The source explicitly names host Cololabis saira and New Zealand's North Island, Auckland Fish Market. These are submitter metadata for this marker, not evidence of a specific organ, collection locality at sea, phenotype or culture deposit.

There is no isolation_source, culture deposit, BioSample, BioProject or assembly link in that marker metadata. The unpublished Wollenberg/Rainey/Ruby bioluminescence-study reference has no DOI/PMID or inspected target experiment. A separate Wollenberg/Ruby direct submission dates to 7 April 2011, Wisconsin-Madison. The reference title does not prove luminescence, and the Int fragment does not prove intestinal isolation.

Exact Assembly search returned zero with a phrase-not-found warning; the independent [genome Datasets endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035433/dataset_report) returned an empty object. This does not prove universal genome absence; the partial marker is not a genome.

Before web search, read all 28 rows from the fresh `kg-microbe-sources imodulondb datasets` call through `uv run --offline --project ../../culturebotai-claw`. Initial sandbox DNS failure was resolved by an authorized read-only network retry. V. natriegens datasets do not cover this target, and no gene/module is asserted. No component query applies; noncoverage is not negative biological evidence.

## Completeness

Optional definitions, evidence, nomenclature, mappings, deposits and graphs need not be populated without relevant support. The discovered host/location metadata is optional enrichment, not a missing required representation in this seeded taxonomy record.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched ID, complete label, stem and strain punctuation variants through `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All 29 matched lines were read fully: three applicable rows, three unrelated GTDB rows, twelve unrelated NCBI rows and eleven unrelated ATB rows.

A separate JF792709/version scan returned zero matches in those roots. All five SOURCE.json documents were parsed independently in full and history filenames searched without ignore filtering at both stages; no additional match was found. These are bounded repository checks, not global absence claims.

Exact-label, punctuation, accession, culture/genome, author and host web searches yielded taxonomy listings rather than an applicable inspected experiment or deposit chain. Search snippets were not evidence. No consequential omission was established.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Numeric length statistics and accession substrings are not taxonomic matches.

## Recommended Edits

None required; preserve YAML and SEEDED status. Future enrichment belongs to a maintained source/extractor and inventory, or tested harmonization logic in `src/taxonmech/seed.py`; scope edits belong in `curation/seed_scope.tsv`. Correct source/kg-microbe mappings upstream. Keep taxon, strain, deposit, marker, sample, assembly, genome, run and project identities distinct.

## Follow-up Checks

For later authorized curation, establish explicit source chains and complete culture accessions, rerun the target schema/strict commands and documented full-corpus reproduction/provenance gates. Require direct sanmaInt_07 experimental evidence before phenotype claims and actual tissue metadata before specifying an organ. Repeat authority checks when refreshing sources. No unresolved blocker requires enrichment now.

## Additional Notes

All non-target candidate rows were read losslessly.

- `data/catalog/gtdb_genomes-0013.jsonl.gz:19084`: RS_GCF_037148075.1, Gordonia malaquae, taxid 410332, MMO-152, SAMN37642804. The match is contig N50 1035433.
- `data/catalog/gtdb_genomes-0010.jsonl.gz:2388`: RS_GCF_006334005.1, Mycoplasmopsis pullorum, taxid 48003, UBP16-398-3Cl3, SAMN08428798. The match is ungapped length 1035433.
- `data/catalog/gtdb_genomes-0011.jsonl.gz:24709`: RS_GCF_001946835.1, Mycobacterium tuberculosis, taxid 1773, I0004243-7, SAMN06010419. The match is contig N50 1035433.
- `data/catalog/ncbi_genbank-0005.jsonl.gz:15235` and `data/catalog/ncbi_refseq-0002.jsonl.gz:23284`: paired GCA/GCF_006334005.1, the same M. pullorum sample and strain, again matching ungapped genome length rather than taxon ID.

Ten complete rows in `data/catalog/ncbi_genbank-0038.jsonl.gz` are Neisseria gonorrhoeae taxid/species_taxid 485, PRJNA317462. Rows 26222, 27607, 27610, 49362, 49363, 49364, 49513, 49514, 49515 and 49516 contain respectively GCA_042078485.1, GCA_042106765.1, GCA_042106825.1, GCA_042546485.1, GCA_042546505.1, GCA_042546525.1, GCA_042549505.1, GCA_042549525.1, GCA_042549545.1 and GCA_042549555.1. Their respective samples are SAMN10354339, SAMN10354338, SAMN10354337, SAMN10354336, SAMN10354335, SAMN10354334, SAMN10354330, SAMN10354331, SAMN10354333 and SAMN10354332.

All columns of `data/catalog/allthebacteria.tsv.xz:1503392-1503401` concern N. gonorrhoeae samples SAMN10354330-39. Row 1557646 concerns Salmonella sample SAMN11035433, run SRR8655904, no ENA assembly accession and an assembly-submission-error flag. None of those rows' run/analysis IDs, filters, sequence checksums or URLs establishes sanmaInt_07 provenance.

Only this new report was written. No YAML, inventory, generated product, prior report, history or lifecycle status was changed. No paid research, external contact or GitHub mutation occurred.
