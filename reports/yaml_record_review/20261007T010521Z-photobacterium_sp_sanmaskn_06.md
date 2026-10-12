# YAML Record Review: Photobacterium sp. sanmaSkn_06

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_sanmaskn_06.yaml`
- Started UTC: 2026-10-07T01:02:49Z
- Finished UTC: 2026-10-07T01:05:21Z
- Verdict: pass

## Target

The entire generated TaxonRecord was read: NCBITaxon:1035393,
Photobacterium sp. sanmaSkn_06, SPECIES, BACTERIA, parent
NCBITaxon:2628852, genetic code 11, EXACT grounding, SEEDED
mapping status. It has ten ancestors, strain_count 0, one
NCBITAXON NAME attestation and one seed event. It asserts no
synonyms, nomenclature, mappings, deposits, genomes, definition,
literature evidence, phenotype or causal graph.

PATHS uniquely resolves this target. An ignored-inclusive filename
search found no prior report for this stem. Only this new report
is written; records, inputs, previous reports, history and status
remain unchanged.

## Validation

Commands used UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_sanmaskn_06.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_sanmaskn_06.yaml --out /private/tmp/pskn06-strict.tsv`: exit 0, one file scanned, zero ERROR rows; the actual TSV was read and is header-only.
- Structured comparisons checked the complete backbone row,
  lineage, synonyms, seven non-NCBI inventories, PATHS,
  scope and attestation. No exact type-material, merged-ID
  or dropped-ID rows were found. The pinned backbone has
  no children beneath this taxon.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just validate-history`, `just validate-products`,
provenance hash recomputation, tests, site drift and publication-size
gates. These corpus-wide gates were not run for this individual
read-only review; no target-only substitute was invented. There
is no curator-added graph or history reference in the record.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222055`
agrees with all identity fields and the snapshot. The native
scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31535`
agrees. `data/taxa/PATHS.tsv:14546` and `curation/seed_scope.tsv:322326`
support the slug and scope reason.

All ancestor IDs, labels and ranks were compared, root-first:

`1 root / NO_RANK; 131567 cellular organisms / CELLULAR_ROOT; 2 Bacteria / DOMAIN; 3379134 Pseudomonadati / KINGDOM; 1224 Pseudomonadota / PHYLUM; 1236 Gammaproteobacteria / CLASS; 135623 Vibrionales / ORDER; 641 Vibrionaceae / FAMILY; 657 Photobacterium / GENUS; 2628852 unclassified Photobacterium / NO_RANK`.

Complete current [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035393&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035393)
retain the exact name, species rank, parent and ancestry. XML
confirms code 11, with no alternative name or type material;
Datasets includes root.

The full sanmaSkn_06 designation is essential. A strain-like label
does not override NCBI's SPECIES rank. EXACT is correspondence
to this unresolved concept, not formal nomenclature or equivalence
to a similarly numbered isolate.

## Evidence

The NCBITAXON source ID, label, count 1, unit NAME and
2026-09-13 snapshot agree with the backbone. The seed event's
source list and scope reason match. Manifest extracted_at fields
were read: raw 2026-09-13T17:50:44Z, ATB
2026-09-13T17:54:04Z, StrainInfo 2026-09-13T17:29:00Z.
The inspected `src/taxonmech/seed.py::_seed_timestamp` takes
their maximum, explaining the event timestamp. It is seed
provenance, not human sign-off.

The exact non-expanded nuccore query returned UID 333797996.
Complete [JF792714.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF792714.1),
references and features explicitly name sanmaSkn_06 and taxon
1035393. It is a 1251-base partial 16S rRNA gene. Source
qualifiers identify host Cololabis saira and locality New Zealand:
North Island, Auckland Fish Market. No assembly, BioSample,
BioProject or registered culture-deposit accession is supplied.

The Wollenberg, Rainey and Ruby research reference remains marked
Unpublished without DOI or PMID. Its title concerns experimental
and taxonomic study of bioluminescence variation in New Zealand
Vibrionaceae isolates. The direct submission by Wollenberg and
Ruby is dated 7 April 2011, University of Wisconsin. These
annotations do not establish a measured bioluminescence phenotype
or an anatomical source for this isolate.

Exact-label, punctuation-variant, marker-accession,
author/designation and research-title web queries produced no
inspected publication joined to this exact isolate. Taxonomy
listings were only discovery leads. This is not an exhaustive
literature-absence claim.

The exact non-expanded Assembly query returned zero with a
phrase-not-found warning. The separately read
[Datasets genome endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035393/dataset_report)
returned an empty object. This result is bounded to this taxon
and retrieval date, not alternate classifications.

The structured adapter was queried before open web discovery:
`uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`.
All 28 dataset rows were inspected. None covers this
Photobacterium target. iModulonDB is not applicable; neighboring
Vibrio datasets cannot be transferred, and noncoverage is not
negative biological evidence.

## Completeness

A completed `rg --no-ignore --hidden -n -z -i` search used
`\b1035393\b|Photobacterium sp\. sanmaSkn_06\b|photobacterium_sp_sanmaskn_06\b|\bsanmaSkn[-_ ]?06\b`
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
Ignored, hidden and compressed files were included. All three
matches, backbone, scientific name and scope, were read in full.
Five SOURCE.json files were separately parsed and history
filenames checked independently of gitignore; no additional target
matches were found.

The completed whole-accession JF792714 search across the same
ten roots found zero matches. Separate SOURCE.json and
history-filename scans likewise found none. These are bounded
local results, not public-archive absence claims.

Exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive,
Madin or BactoTraits inventory rows. With no descendants,
strain_count 0 is supported as a BacDive count and does not deny
the submitted isolate. No supported own-deposit/genome chain was
established. Empty optional nomenclature, mappings, definition,
literature and graph slots are acceptable. The partial marker is
an optional enrichment lead, not a missing required assembly.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, attestation and seed provenance
are supported. The YAML does not inflate marker or study-title
metadata into genome, tissue or phenotype assertions.

## Recommended Edits

None required. Do not hand-edit generated YAML.

Future authorized marker enrichment belongs in a maintained seeder
mechanism with tests or a deliberately designed persistent curator
overlay; no existing overlay path is assumed. Preserve JF792714.1
as a nucleotide related record, not an assembly.

## Follow-up Checks

- Keep the entire sanmaSkn_06 designation until authoritative
  evidence supports a change.
- Verify future culture/genome links through exact own-deposit
  and source-native identities; shared taxonomy, locality or
  study titles do not establish equivalence.
- Require explicit isolate-specific experiments or annotations
  for phenotype or tissue enrichment in the appropriate sibling
  repository; do not infer tissue from the strain abbreviation.
- After authorized maintained-input changes, use source refresh,
  seed dry run/canary and actual-file inspection, repeat both
  target validators, then full `just verify-corpus` and `just qc`.

## Additional Notes

This record was reviewed individually using its complete YAML,
own source matches, live taxonomy, sequence metadata and validation.
No neighboring record supplied its verdict.

No paid research, genome FASTA download, external contact,
GitHub mutation, history append or status promotion occurred.
Eukaryota and its completed reviews remain untouched.
