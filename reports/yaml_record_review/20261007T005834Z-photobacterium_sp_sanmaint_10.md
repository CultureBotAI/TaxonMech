# YAML Record Review: Photobacterium sp. sanmaInt_10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_sanmaint_10.yaml`
- Started UTC: 2026-10-07T00:57:11Z
- Finished UTC: 2026-10-07T00:58:34Z
- Verdict: pass

## Target

The complete generated TaxonRecord was read: NCBITaxon:1035391,
Photobacterium sp. sanmaInt_10, SPECIES, BACTERIA, parent
NCBITaxon:2628852, genetic code 11, grounding EXACT, status
SEEDED. It has ten ancestors, strain_count 0, one NCBITAXON
NAME attestation and one seed event. It contains no synonyms,
nomenclature, mappings, deposits, genomes, literature evidence,
phenotype assertions or causal graph.

PATHS identifies this target uniquely. An ignored-inclusive filename
search found no prior report for this stem. The only write is this
new report; records, inputs, prior reports, history and status remain
unchanged.

## Validation

Commands used UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_sanmaint_10.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_sanmaint_10.yaml --out /private/tmp/psan10-strict.tsv`: exit 0, one file, zero ERROR rows. The actual TSV was read and is header-only.
- Structured source checks compared the full backbone row and
  lineage, synonyms, seven non-NCBI inventories, PATHS, scope
  and attestation. No exact type-material, merged-ID or dropped-ID
  rows were found. The pinned backbone has no child taxa.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just validate-history`, `just validate-products`,
provenance hash recomputation, tests, site drift and publication
size gates. No substitute target-only corpus check was invented.
No curator-added graph or history reference is present.

## Identity and Grounding

The full pinned row at `data/raw/ncbitaxon_taxa.tsv:222053`
agrees with every identity field. The native scientific name at
`data/catalog/ncbi_names-0005.jsonl.gz:31533` agrees.
`data/taxa/PATHS.tsv:14544` and `curation/seed_scope.tsv:322324`
support the slug and seed scope.

All ten ancestor IDs, labels and ranks agree with the pinned source:

`1 root / NO_RANK; 131567 cellular organisms / CELLULAR_ROOT; 2 Bacteria / DOMAIN; 3379134 Pseudomonadati / KINGDOM; 1224 Pseudomonadota / PHYLUM; 1236 Gammaproteobacteria / CLASS; 135623 Vibrionales / ORDER; 641 Vibrionaceae / FAMILY; 657 Photobacterium / GENUS; 2628852 unclassified Photobacterium / NO_RANK`.

The complete current [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035391&retmode=xml)
and [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035391)
confirm the name, species rank, parent and ancestry. XML confirms
code 11 and gives no alternate name or type material; Datasets
includes root.

The full sanmaInt_10 designation distinguishes this concept.
Its strain-like spelling does not change its NCBI SPECIES rank.
EXACT does not imply a formally named species or equivalence to
another numbered isolate.

## Evidence

The NCBITAXON NAME count 1, source ID, label and snapshot agree
with the backbone. The seed event agrees with the scope reason
and source list. Manifest fields read during this turn were raw
2026-09-13T17:50:44Z, ATB 2026-09-13T17:54:04Z and
StrainInfo 2026-09-13T17:29:00Z. The inspected
`src/taxonmech/seed.py::_seed_timestamp` takes their maximum,
matching the event. It remains seed provenance, not human sign-off.

The exact non-expanded nuccore search found one UID, 333797994.
Complete [JF792712.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF792712.1),
references and features identify sanmaInt_10 and taxon 1035391.
This is a 1251-base partial 16S rRNA gene, not an assembly.
Source qualifiers give Cololabis saira as host and New Zealand:
North Island, Auckland Fish Market as locality. The entry supplies
no assembly, BioSample, BioProject or registered culture deposit.

The Wollenberg, Rainey and Ruby research reference is marked
Unpublished, without DOI or PMID. Its title concerns experimental
and taxonomic study of bioluminescence variation in New Zealand
Vibrionaceae isolates. Direct submission by Wollenberg and Ruby
is dated 7 April 2011 from the University of Wisconsin. Those
annotations do not establish an isolate-specific experimental
bioluminescence phenotype.

Exact label, punctuation variants, marker accession,
author/designation and genome/strain web searches yielded no
inspected publication joined to this isolate. The shared research
title was searched earlier in this turn. These bounded discovery
queries are not an exhaustive literature-absence proof.

The exact non-expanded Assembly search returned zero, with a
phrase-not-found warning. The independently read
[Datasets genome endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035391/dataset_report)
returned an empty object. The claim is limited to this taxon and
retrieval date.

A local assembly-catalog candidate was rejected after its complete
row was read: `data/catalog/ncbi_genbank-0051.jsonl.gz:30006`
contains GCA_055846675.1, Pseudomonadota bacterium,
taxid/species_taxid 1977087, isolate DRTY-6_201705_bins_173.
The match to 1035391 is only its genome_size_ungapped value.
Neither that assembly nor its sample/project can be assigned
to sanmaInt_10 from this numeric collision.

The successful iModulonDB dataset inventory query earlier in this
turn preceded open web discovery:
`uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`.
All 28 rows were inspected. No Photobacterium dataset covers the
target, so the adapter is not applicable. Related Vibrio datasets
are not transferable evidence, and noncoverage is not a phenotype.

## Completeness

The completed `rg --no-ignore --hidden -n -z -i` query used
`\b1035391\b|Photobacterium sp\. sanmaInt_10\b|photobacterium_sp_sanmaint_10\b|\bsanmaInt[-_ ]?10\b`
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
including ignored, hidden and compressed files. All four matching
rows were read completely: backbone, scientific name, scope and
the unrelated assembly-length collision. Five SOURCE.json files
were separately parsed and history filenames checked independently
of gitignore, with no further target matches.

A completed whole-accession JF792712 search in those same ten
roots returned zero matches. Separate SOURCE.json and
history-filename checks likewise found none. These are bounded
local findings, not universal public-resource absence claims.

Exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive,
Madin or BactoTraits inventory rows. With no descendants,
strain_count 0 is supported as a BacDive count and does not
deny the submitted isolate's existence.

No supported culture-deposit-to-genome chain was established.
Optional nomenclature, mappings, definition, literature and graph
fields can remain empty. The partial marker is an optional related
record lead, not a missing required whole-genome link.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, attestation and seed provenance
are supported. The record correctly avoids importing the unrelated
assembly or inferring a phenotype from a study title.

## Recommended Edits

None required. Keep generated YAML unchanged.

A future authorized marker enrichment would belong in a maintained
seeder mechanism with tests or a deliberately designed persistent
curator overlay, not a direct record edit. No existing overlay path
is assumed. Keep JF792712.1 typed as a nucleotide sequence,
separate from genome identifiers.

## Follow-up Checks

- Preserve the complete sanmaInt_10 designation and unresolved
  species identity until an authoritative change is supported.
- Verify any future deposit/genome link through exact own-deposit
  and source-native identities. Numeric search hits require field
  inspection; genome lengths are not taxon identifiers.
- Require isolate-specific experiments for phenotype enrichment
  in the relevant sibling repository.
- After authorized maintained-input changes, use source refresh,
  seed dry run/canary and actual-file inspection, repeat both
  target validators, then full `just verify-corpus` and `just qc`.

## Additional Notes

The review used this target's complete YAML, own source rows,
live taxonomy, sequence metadata and individual validation.
Neighboring record verdicts were not treated as evidence.

No paid research, genome FASTA download, external contact,
GitHub mutation, history append or lifecycle promotion occurred.
Eukaryota and its completed reports were not changed.
