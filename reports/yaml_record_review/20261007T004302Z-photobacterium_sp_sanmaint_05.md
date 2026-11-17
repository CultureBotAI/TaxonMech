# YAML Record Review: Photobacterium sp. sanmaInt_05

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_sanmaint_05.yaml`
- Started UTC: 2026-10-07T00:40:52Z
- Finished UTC: 2026-10-07T00:43:02Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read:
`NCBITaxon:1035387`, Photobacterium sp. sanmaInt_05,
SPECIES, BACTERIA, parent `NCBITaxon:2628852`, genetic
code 11, grounding EXACT and mapping status SEEDED.
It has ten ancestors, zero BacDive strains, one NCBITAXON NAME
attestation and one seed event. No synonyms, nomenclature,
mappings, deposits, genomes, definition, literature evidence,
phenotypes or causal graphs are asserted.

PATHS uniquely resolves the file. A gitignore-independent filename
search found no previous report for this stem. Only this new report
is written; YAML, code, inventories, generated products, prior
reports, history and lifecycle status remain unchanged.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_sanmaint_05.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_sanmaint_05.yaml --out /private/tmp/psan05-strict.tsv`: exit 0, one file scanned, zero ERROR rows. The actual TSV was read and is header-only.
- Read-only structured comparisons checked every pinned ancestor,
  backbone and synonym field, seven non-NCBI inventories, PATHS,
  scope and attestation. Exact type-material, merged-ID and
  dropped-ID scans found no target rows. The pinned backbone has
  no children beneath this taxon.

Not checked: full-corpus `just verify-corpus`, `just qc`,
`just validate-all`, `just validate-history`,
`just validate-products`, provenance hash recomputation,
tests, site drift and publication size gates. No target-only
replacement was invented for a corpus gate. No curator-added
graph or history reference is asserted by this target.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222049`
agrees with the ID, label, rank, parent, code and 2026-09-13
snapshot. The complete native scientific-name row at
`data/catalog/ncbi_names-0005.jsonl.gz:31529` agrees.
`data/taxa/PATHS.tsv:14540` and
`curation/seed_scope.tsv:322320` support the filename and
inclusion reason.

All ten ancestor IDs, labels and ranks match the pinned source:

`1 root / NO_RANK; 131567 cellular organisms / CELLULAR_ROOT; 2 Bacteria / DOMAIN; 3379134 Pseudomonadati / KINGDOM; 1224 Pseudomonadota / PHYLUM; 1236 Gammaproteobacteria / CLASS; 135623 Vibrionales / ORDER; 641 Vibrionaceae / FAMILY; 657 Photobacterium / GENUS; 2628852 unclassified Photobacterium / NO_RANK`.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035387&retmode=xml)
and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035387)
were read in full. They retain the exact target name, species
rank, parent and ancestry. XML confirms code 11; Datasets includes
root. XML supplies no alternative name or type material.

The full sanmaInt_05 designation is essential. Its strain-like
spelling does not override NCBI's SPECIES rank. EXACT identifies
this particular unresolved taxonomic concept, not a formally
published species or equivalence with neighboring numbered isolates.

## Evidence

The NCBITAXON count 1, NAME unit, ID, label and snapshot agree
with the pinned inventory. The seed event reproduces the scope
reason and source list. The manifest timestamp fields were read:
raw 2026-09-13T17:50:44Z, ATB 2026-09-13T17:54:04Z,
StrainInfo 2026-09-13T17:29:00Z. The inspected
`src/taxonmech/seed.py::_seed_timestamp` selects their
maximum, matching this record. That event is not human review.

The exact non-expanded nuccore search returned one record,
[JF792707.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792707.1).
Its complete metadata, references and feature table explicitly
identify sanmaInt_05 and taxon 1035387. It is a 1251-base
partial 16S rRNA gene, not an assembly. Source annotations name
host Cololabis saira and locality Auckland Fish Market, North
Island, New Zealand. The entry supplies no assembly, BioSample,
BioProject or registered culture-deposit accession.

The research reference by Wollenberg, Rainey and Ruby is marked
Unpublished, with no DOI or PMID. Its title concerns experimental
and taxonomic study of bioluminescence variation among New Zealand
Vibrionaceae isolates. Wollenberg and Ruby directly submitted the
entry on 7 April 2011 from the University of Wisconsin.
This metadata supports the marker identity and submission context,
not a demonstrated bioluminescence phenotype for sanmaInt_05.

Exact-label, punctuation-variant, marker-accession,
author/designation and research-title web searches yielded no
inspected publication joined to this exact isolate. Taxonomy
listings and unrelated results were leads only. No exhaustive
literature-absence claim is made.

The exact non-expanded Assembly search returned zero with a
phrase-not-found warning. The
[NCBI Datasets genome endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035387/dataset_report)
returned an empty object. These observations are bounded to this
exact taxon and review date, not every possible classification.

Before open web research,
`uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`
successfully returned 28 dataset rows, all inspected. No dataset
covers this Photobacterium target. Vibrio datasets cannot be
transferred by family membership. The adapter is not applicable;
noncoverage is not negative biological evidence.

## Completeness

A completed `rg --no-ignore --hidden -n -z -i` search used
`\b1035387\b|Photobacterium sp\. sanmaInt_05\b|photobacterium_sp_sanmaint_05\b|\bsanmaInt[-_ ]?05\b`
over `data/raw`, `data/catalog`, `data/bacdive`,
`data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and
`history`. Ignored, hidden and compressed files were included.
All three matching rows were read in full: backbone, scientific
name and scope. Five SOURCE.json files were separately parsed,
and history filenames checked independently of gitignore; neither
check found another target match.

A completed whole-accession search for JF792707 across the same
ten roots returned zero matches. Its separate SOURCE.json and
history-filename checks also found none. These are bounded local
results, not claims about every public archive.

Exact-taxonomy scans found no BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventory rows. With no
descendants, zero BacDive strains is supported; it does not deny
the isolate represented by the marker submission.

No supported whole-deposit or assembly chain was established by
these checks. Optional nomenclature, mappings, definition,
literature and graph fields can remain empty. The partial 16S
marker is an optional enrichment lead, not a missing required genome.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source attestation and seed
provenance agree with the inspected evidence. No genome or
experimental phenotype is improperly inferred by the YAML.

## Recommended Edits

None required. Do not hand-edit generated YAML.

Future authorized marker enrichment belongs in a maintained
seeder mechanism with tests or a deliberately designed persistent
curator overlay; no existing overlay path is assumed.
Preserve JF792707.1 as a nucleotide related record if represented,
never as an assembly or genome identifier.

## Follow-up Checks

- Keep the exact sanmaInt_05 designation and unresolved species
  assignment unless authority evidence supports a change.
- Require a complete source-native own-deposit identity chain
  before adding a culture or genome link. Shared genus, host,
  locality or research title is insufficient.
- Require inspected isolate-specific experiments before adding
  phenotype evidence in the appropriate sibling repository.
- After an authorized maintained-input change, use source refresh,
  seed dry run/canary and actual-file inspection, rerun both
  target validators and full `just verify-corpus` and
  `just qc`. No curation was performed here.

## Additional Notes

The exact target was reviewed individually. Neither other
sanmaInt isolates nor similarly numbered sanmaSkn records
supply its identity, markers or culture associations.

No paid research, genome FASTA download, external contact, GitHub
mutation, history append or lifecycle promotion occurred.
Eukaryota records and their completed reviews were not changed.
