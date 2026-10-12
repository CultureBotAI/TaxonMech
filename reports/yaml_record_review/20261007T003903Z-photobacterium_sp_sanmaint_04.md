# YAML Record Review: Photobacterium sp. sanmaInt_04

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_sanmaint_04.yaml`
- Started UTC: 2026-10-07T00:37:11Z
- Finished UTC: 2026-10-07T00:39:03Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read:
`NCBITaxon:1035386`, Photobacterium sp. sanmaInt_04,
SPECIES, BACTERIA, parent `NCBITaxon:2628852`, genetic
code 11, grounding EXACT and mapping status SEEDED.
It has ten ancestors, zero BacDive strains, one NCBITAXON NAME
attestation and one seed event. Synonyms, nomenclature, mappings,
deposits, genomes, definition, literature evidence, phenotypes and
causal graphs are not asserted.

PATHS uniquely resolves the target. A gitignore-independent report
filename search found no previous review for this stem. This new
report is the only write for this target; YAML, inventories, code,
generated products, previous reports, history and status are unchanged.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_sanmaint_04.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_sanmaint_04.yaml --out /private/tmp/psan04-strict.tsv`: exit 0, one file scanned, zero ERROR rows. The actual emitted TSV was read and is header-only.
- Read-only structured comparisons checked the entire pinned
  lineage, backbone, source synonyms, seven non-NCBI inventories,
  PATHS, scope and attestation. Exact type-material, merged-ID
  and dropped-ID scans found no target rows. The pinned backbone
  has no children beneath this taxon.

Not checked: full-corpus `just verify-corpus`, `just qc`,
`just validate-all`, `just validate-history`,
`just validate-products`, provenance hash recomputation,
tests, site drift and publication size gates. No target-only
substitute was invented for corpus reproduction or another corpus
gate. The target asserts no curator-added graph or history reference.

## Identity and Grounding

The full source row `data/raw/ncbitaxon_taxa.tsv:222048`
matches the target's ID, label, species rank, parent, code and
snapshot. Its complete native scientific-name record at
`data/catalog/ncbi_names-0005.jsonl.gz:31528` agrees.
`data/taxa/PATHS.tsv:14539` resolves the file, and
`curation/seed_scope.tsv:322319` supplies the matching
inclusion reason.

All ten ancestor IDs, labels and ranks match the pinned source:

`1 root / NO_RANK; 131567 cellular organisms / CELLULAR_ROOT; 2 Bacteria / DOMAIN; 3379134 Pseudomonadati / KINGDOM; 1224 Pseudomonadota / PHYLUM; 1236 Gammaproteobacteria / CLASS; 135623 Vibrionales / ORDER; 641 Vibrionaceae / FAMILY; 657 Photobacterium / GENUS; 2628852 unclassified Photobacterium / NO_RANK`.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035386&retmode=xml)
and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035386)
were read in full. The exact label, species rank, parent and
ancestry agree. XML confirms genetic code 11; Datasets explicitly
includes root. The XML supplies no alternative name or type
material.

Keep the full sanmaInt_04 designation. Its strain-like spelling
does not justify changing the NCBI SPECIES rank. EXACT means
identity with this unresolved NCBI taxonomic concept, not formal
species naming or equivalence with another numbered isolate.

## Evidence

The NCBITAXON attestation's ID, label, NAME unit, count 1 and
2026-09-13 snapshot agree with the pinned inventory. The seed
event matches its scope reason and source list. The three source
manifest timestamp fields read during this turn are raw
2026-09-13T17:50:44Z, ATB 2026-09-13T17:54:04Z and
StrainInfo 2026-09-13T17:29:00Z. The inspected
`src/taxonmech/seed.py::_seed_timestamp` selects their
maximum, explaining the seed event time without implying review.

The exact non-expanded nuccore search found one record:
[JF792706.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792706.1).
Its complete metadata, references and feature table explicitly
identify sanmaInt_04 and taxon 1035386. It is a 1251-base
partial 16S rRNA gene, not a genome assembly. Source annotations
name host Cololabis saira and locality Auckland Fish Market,
North Island, New Zealand. No assembly, BioSample, BioProject
or registered culture accession is supplied by this entry.

The research reference lists Wollenberg, Rainey and Ruby and
is marked Unpublished. Its title concerns an experimental and
taxonomic study of bioluminescence variation in natural
Vibrionaceae isolates from New Zealand. There is no DOI or PMID.
The direct submission is by Wollenberg and Ruby, dated 7 April
2011, from the University of Wisconsin. This reference metadata
does not establish an experimental bioluminescence phenotype for
sanmaInt_04.

Exact-label, punctuation-variant, marker-accession and
author/designation web searches returned taxonomy listings but
no inspected publication joined to this exact isolate. Searches
for the shared reference title and author/topic were conducted
earlier in this turn; none supplied isolate-specific experimental
evidence. No exhaustive literature-absence claim is made.

The exact non-expanded Assembly search returned zero with a
phrase-not-found warning, and the
[NCBI Datasets genome endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035386/dataset_report)
returned an empty object. These observations are bounded to
this exact taxon and date, not every possible classification.

The structured iModulonDB dataset inventory was queried and all
28 rows inspected earlier in this turn, before open web research,
using
`uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`.
No Photobacterium dataset covers sanmaInt_04. Neighboring
Vibrio datasets cannot be transferred by family membership.
The adapter is not applicable; noncoverage is not negative
biological evidence.

## Completeness

The completed `rg --no-ignore --hidden -n -z -i` search used
`\b1035386\b|Photobacterium sp\. sanmaInt_04\b|photobacterium_sp_sanmaint_04\b|\bsanmaInt[-_ ]?04\b`
across `data/raw`, `data/catalog`, `data/bacdive`,
`data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and
`history`. Ignored, hidden and compressed files were included.
All three matching rows were read in full: backbone, scientific
name and scope. Five SOURCE.json files were separately parsed;
history filenames were also checked independently of gitignore.
No additional target match was found in those checks.

A subsequent completed whole-accession search for JF792706
across the same ten roots returned zero matches. Its separate
SOURCE.json and history-filename checks also found none.
These are bounded local results, not claims of global absence.

Exact-taxonomy scans found no BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventory rows. With no
descendants, zero BacDive strains agrees with the pinned source.
It does not deny the isolate represented by the nucleotide entry.

The inspected sources establish no supported whole-deposit or
assembly chain. Optional nomenclature, mappings, definition,
literature and graph slots can remain empty. The partial 16S
marker is an enrichment lead, not a missing required genome.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, full lineage, source attestation and seed
provenance agree with the inspected evidence. The YAML makes
no unsupported genome or experimental phenotype claim.

## Recommended Edits

None required. Do not hand-edit the generated YAML.

Future authorized marker enrichment belongs in a maintained seeder
mechanism with tests or a deliberately designed curator overlay
that survives regeneration; no existing overlay path is assumed.
JF792706.1 must remain a nucleotide related record if represented,
not an assembly identifier. Do not transfer neighboring isolates'
markers, source claims or culture associations by name similarity.

## Follow-up Checks

- Preserve the exact sanmaInt_04 designation and unresolved
  species assignment unless an authority supports a change.
- Before adding a culture or genome link, verify its whole
  own-deposit and source-native identity chain and current status.
  Shared host, locality, genus or study reference is insufficient.
- Require inspected isolate-specific experiments for phenotype
  enrichment in the appropriate sibling repository.
- After an authorized maintained-input change, use source refresh,
  seed dry run/canary and actual-file inspection; rerun both
  target validators and full `just verify-corpus` and
  `just qc`. No curation was performed in this review.

## Additional Notes

This target was reviewed individually, including its own complete
YAML, taxonomy, source matches, nucleotide metadata and validations.
The independently inspected source identifies sanmaInt_04, not
sanmaInt_01, sanmaInt_03 or a similarly numbered sanmaSkn entry.

No paid research, genome FASTA download, external contact, GitHub
mutation, history append or lifecycle promotion occurred.
Eukaryota records and their completed reviews were not changed.
