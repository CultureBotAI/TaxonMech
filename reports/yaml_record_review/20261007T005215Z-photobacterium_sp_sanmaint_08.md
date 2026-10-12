# YAML Record Review: Photobacterium sp. sanmaInt_08

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_sanmaint_08.yaml`
- Started UTC: 2026-10-07T00:46:46Z
- Finished UTC: 2026-10-07T00:52:15Z
- Verdict: pass

## Target

The entire generated TaxonRecord was read: NCBITaxon:1035389,
Photobacterium sp. sanmaInt_08, SPECIES, BACTERIA, parent
NCBITaxon:2628852, genetic code 11, grounding EXACT and mapping
status SEEDED. It contains ten ancestors, zero BacDive strains,
one NCBITAXON NAME attestation and one seed event. It asserts no
synonyms, nomenclature, mappings, deposits, genomes, definition,
literature evidence, phenotypes or causal graph.

PATHS uniquely resolves this target. An ignored-inclusive filename
search found no prior review for this stem. Only this new report
is written; records, code, inventories, generated products,
previous reports, history and lifecycle status remain unchanged.

## Validation

Commands used UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_sanmaint_08.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_sanmaint_08.yaml --out /private/tmp/psan08-strict.tsv`: exit 0, one file scanned, zero ERROR rows. The actual TSV was read and is header-only.
- Read-only structured comparisons checked the entire pinned
  lineage, backbone, synonyms, seven non-NCBI inventories,
  PATHS, scope and attestation. Exact type-material, merged-ID
  and dropped-ID scans found no target rows. The pinned
  backbone has no children beneath this taxon.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just validate-history`, `just validate-products`,
provenance hash recomputation, tests, site drift and publication
size gates. No target-only substitute for a corpus gate was
invented. No curator-added graph or history reference is present.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222051`
agrees with ID, label, rank, parent, code and the 2026-09-13
snapshot. The complete native scientific-name row at
`data/catalog/ncbi_names-0005.jsonl.gz:31531` agrees.
`data/taxa/PATHS.tsv:14542` and `curation/seed_scope.tsv:322322`
support the filename and scope reason.

All ten ancestor IDs, names and ranks agree with the pinned source:

`1 root / NO_RANK; 131567 cellular organisms / CELLULAR_ROOT; 2 Bacteria / DOMAIN; 3379134 Pseudomonadati / KINGDOM; 1224 Pseudomonadota / PHYLUM; 1236 Gammaproteobacteria / CLASS; 135623 Vibrionales / ORDER; 641 Vibrionaceae / FAMILY; 657 Photobacterium / GENUS; 2628852 unclassified Photobacterium / NO_RANK`.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035389&retmode=xml)
and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035389)
were read in full. They retain the exact name, species rank,
parent and ancestry. XML confirms code 11, and Datasets includes
root. XML supplies no alternative name or type material.

The full sanmaInt_08 designation must be retained. Its strain-like
name does not override NCBI's SPECIES rank. EXACT denotes this
particular unresolved taxonomic concept, not formal species
nomenclature or another numbered isolate.

## Evidence

The NCBITAXON NAME count 1, ID, label and snapshot agree with
the backbone. The seed event matches its scope reason and source
list. Manifest timestamp fields read during this turn were raw
2026-09-13T17:50:44Z, ATB 2026-09-13T17:54:04Z and
StrainInfo 2026-09-13T17:29:00Z. The inspected
`src/taxonmech/seed.py::_seed_timestamp` selects their maximum,
matching the record. This is not human review history.

The exact non-expanded nuccore search returned one record:
[JF792710.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792710.1).
Its complete metadata, references and feature table identify
sanmaInt_08 and taxon 1035389. It is a 1251-base partial
16S rRNA gene, not a whole-genome assembly. Its source names
host Cololabis saira and Auckland Fish Market, North Island,
New Zealand. The entry supplies no assembly, BioSample,
BioProject or registered culture-deposit accession.

The research reference by Wollenberg, Rainey and Ruby is marked
Unpublished, without a DOI or PMID. Its title concerns experimental
and taxonomic study of bioluminescence variation in New Zealand
Vibrionaceae isolates. Wollenberg and Ruby directly submitted the
record on 7 April 2011 from the University of Wisconsin.
These annotations do not establish an experimental bioluminescence
phenotype for sanmaInt_08.

An accession-search lead was traced to inspected primary
[Sebald et al. (2016)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0153476),
DOI 10.1371/journal.pone.0153476, PMID 27093431, and its
[S1 workbook](https://journals.plos.org/plosone/article/file?id=10.1371%2Fjournal.pone.0153476.s005&type=supplementary).
The study clustered Drosophila gut 16S amplicons at 97% identity
against SILVA 111. Workbook headers and the complete matching
row were read: before_filtering row 1247 names JF792710,
with wild-type replicates 7/14/6, mutant replicates 0/4/0,
and blank 22; taxonomy stops at Photobacterium. All rows
of both worksheets were scanned; after_filtering has no
JF792710 match. My interpretation: reference-OTU use does
not establish the exact sanmaInt_08 isolate in flies, an
isolate-specific phenotype, or publication of the original
unpublished submission study.

Exact-label, designation-variant and accession web searches were
bounded discovery, not an exhaustive literature-absence proof.
The ResearchGate copy was only a lead; the PLOS methods and
native workbook supplied the inspected evidence. A browser-tool
attachment fetch failed, but a read-only direct fetch succeeded
and the XLSX XML was parsed in memory without changing files.

The exact non-expanded Assembly search returned zero with a
phrase-not-found warning. The
[NCBI Datasets genome endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035389/dataset_report)
returned an empty object. These observations concern this taxon
and retrieval date, not every alternative classification.

The structured iModulonDB inventory was queried earlier in this
turn before open web research:
`uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`.
All 28 returned dataset rows were inspected. None covers this
Photobacterium target. Vibrio datasets cannot be transferred by
family membership. The adapter is not applicable; noncoverage
is not negative biological evidence.

## Completeness

A completed `rg --no-ignore --hidden -n -z -i` search used
`\b1035389\b|Photobacterium sp\. sanmaInt_08\b|photobacterium_sp_sanmaint_08\b|\bsanmaInt[-_ ]?08\b`
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
Ignored, hidden and compressed files were included. All three
matches, backbone, scientific name and scope, were read in full.
Five SOURCE.json files were separately parsed, and history
filenames checked independently of gitignore; no additional
target matches were found.

A completed whole-accession search for JF792710 across the same
ten roots returned zero matches. Its separate SOURCE.json and
history-filename checks also found none. These are bounded local
findings, not statements about all public archives.

Exact-taxonomy scans found no BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventory row. With no
descendants, zero BacDive strains is supported; the count does
not deny the isolate represented by the nucleotide submission.

No supported whole-deposit or assembly chain was established.
Optional nomenclature, mappings, definition, literature and graph
fields may remain empty. The partial marker is an optional
enrichment lead, not a missing required genome link. The
reference-OTU literature hit does not require an isolate-level
host or phenotype assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, full lineage, attestation and seed provenance
agree with the inspected evidence. The YAML does not overstate
the marker submission, unpublished study or reference-OTU use.

## Recommended Edits

None required. Do not hand-edit the generated YAML.

Future authorized marker enrichment belongs in a maintained seeder
mechanism with tests or a deliberately designed persistent curator
overlay; no existing overlay path is assumed. Preserve JF792710.1
as a nucleotide related record, not an assembly. Do not infer a
Drosophila host association from reference-OTU assignment.

## Follow-up Checks

- Preserve the full sanmaInt_08 designation and unresolved
  species assignment unless an authority supports a change.
- Before adding a culture or genome link, verify the complete
  own-deposit/source-native identity chain and accession status.
  Shared genus, host, locality or study title is insufficient.
- Require inspected isolate-specific experiments for phenotype
  enrichment in the relevant sibling repository.
- After authorized maintained-input changes, use source refresh,
  seed dry run/canary and actual-file inspection, rerun both target
  validators, then full `just verify-corpus` and `just qc`.
  No curation was performed here.

## Additional Notes

This record was reviewed individually using its own complete YAML,
source matches, taxonomy, nucleotide metadata and validation
results. Neighboring sanmaInt or similarly numbered sanmaSkn
entries do not supply identity evidence for it.

No paid research, genome FASTA download, external contact, GitHub
mutation, history append or lifecycle promotion occurred.
Eukaryota and its completed reviews were not changed.
