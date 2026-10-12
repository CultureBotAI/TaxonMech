# YAML Record Review: Photobacterium sp. squidInt_01

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_squidint_01.yaml`
- Started UTC: 2026-10-07T01:06:19Z
- Finished UTC: 2026-10-07T01:07:51Z
- Verdict: pass

## Target

The entire generated TaxonRecord was read: NCBITaxon:1035394,
Photobacterium sp. squidInt_01, SPECIES, BACTERIA, parent
NCBITaxon:2628852, genetic code 11, EXACT grounding and SEEDED
status. It has ten ancestors, strain_count 0, one NCBITAXON
NAME attestation and one seed event. It contains no synonyms,
nomenclature, mappings, deposits, genomes, definition, literature
evidence, phenotype assertions or causal graph.

PATHS resolves the target uniquely. An ignored-inclusive filename
search found no prior report for this stem. Only this new report
is written; YAML, inputs, previous reports, history and lifecycle
status remain unchanged.

## Validation

Commands used UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_squidint_01.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_squidint_01.yaml --out /private/tmp/psqi01-strict.tsv`: exit 0, one file scanned, zero ERROR rows. The actual TSV was read and is header-only.
- Structured read-only comparisons checked the complete backbone
  and lineage, synonyms, seven non-NCBI inventories, PATHS,
  scope and attestation. Exact type-material, merged-ID and
  dropped-ID scans found no target rows. There are no child
  taxa in the pinned backbone.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just validate-history`, `just validate-products`,
provenance hash recomputation, tests, site drift and publication-size
gates. These full-corpus gates were skipped for this individual
read-only review, with no invented target-only substitute.
No curator-added graph or history reference is present.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222056`
supports ID, label, rank, parent, code and snapshot date.
The native scientific-name row at
`data/catalog/ncbi_names-0005.jsonl.gz:31536` agrees.
`data/taxa/PATHS.tsv:14547` and `curation/seed_scope.tsv:322327`
support the slug and exact scope reason.

Every ancestor ID, label and rank agrees with the pinned source:

`1 root / NO_RANK; 131567 cellular organisms / CELLULAR_ROOT; 2 Bacteria / DOMAIN; 3379134 Pseudomonadati / KINGDOM; 1224 Pseudomonadota / PHYLUM; 1236 Gammaproteobacteria / CLASS; 135623 Vibrionales / ORDER; 641 Vibrionaceae / FAMILY; 657 Photobacterium / GENUS; 2628852 unclassified Photobacterium / NO_RANK`.

The full current [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035394&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035394)
were inspected. They retain the exact name, species rank,
parent and ancestry. XML confirms genetic code 11 and supplies
no alternate name or type material; Datasets includes root.

Preserve squidInt_01 in full; another squidInt, squidSkn or
sanmaInt designation does not denote this target. EXACT concerns
the unresolved NCBI concept, not formal nomenclature. The
strain-like name does not override NCBI's SPECIES rank.

## Evidence

The NCBITAXON source ID, label, count 1, unit NAME and
2026-09-13 snapshot agree with the backbone. The seed event
matches the scope reason and source list. Manifest timestamp
fields read this turn were raw 2026-09-13T17:50:44Z,
ATB 2026-09-13T17:54:04Z and StrainInfo
2026-09-13T17:29:00Z. The inspected
`src/taxonmech/seed.py::_seed_timestamp` chooses their maximum,
matching the event. This is not human review approval.

The exact non-expanded nuccore query returned UID 333797997.
Complete [JF792715.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF792715.1),
references and feature qualifiers explicitly identify squidInt_01
and taxon 1035394. The entry is a 1251-base partial 16S
rRNA gene, not a whole-genome assembly. Its host qualifier is
"Nototodarus gouldi", preserving the submitted spelling.
Locality is New Zealand: North Island, Auckland Fish Market.
The entry supplies no assembly, BioSample, BioProject or
registered culture-deposit accession.

The research reference by Wollenberg, Rainey and Ruby is
marked Unpublished, without DOI or PMID. Its title concerns
experimental and taxonomic study of bioluminescence variation
in New Zealand Vibrionaceae isolates. Direct submission by
Wollenberg and Ruby is dated 7 April 2011 from the University
of Wisconsin. These annotations do not establish an experimental
bioluminescence phenotype, a specific tissue source, or equivalence
to another isolate associated with the same host.

Exact-label, punctuation-variant, marker-accession,
author/designation and genome/strain web searches supplied no
inspected publication joined to this exact isolate. The shared
research title was also searched earlier this turn. These bounded
queries are not an exhaustive literature-absence proof; taxonomy
listings were not promoted into experimental evidence.

The exact non-expanded Assembly query returned zero with a
phrase-not-found warning. The separately inspected
[Datasets genome response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035394/dataset_report)
was an empty object. This is bounded to the exact taxon and
retrieval date, not all alternate classifications.

The current-turn structured adapter query preceded open web
discovery:
`uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`.
All 28 rows were inspected. No dataset covers this Photobacterium
target. iModulonDB is not applicable; Vibrio datasets cannot
supply evidence through family membership, and noncoverage is
not negative biological evidence.

## Completeness

A completed `rg --no-ignore --hidden -n -z -i` search used
`\b1035394\b|Photobacterium sp\. squidInt_01\b|photobacterium_sp_squidint_01\b|\bsquidInt[-_ ]?01\b`
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
including ignored, hidden and compressed files. All three
matching rows, backbone, scientific name and scope, were read
in full. Five SOURCE.json files were separately parsed, and
history filenames checked independently of gitignore; no further
target matches were found.

The completed whole-accession JF792715 search across the same
ten roots returned zero matches. Separate SOURCE.json and
history-filename checks also found none. These are bounded
local results, not universal archive-absence claims.

Exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive,
Madin or BactoTraits inventory rows. With no descendants,
strain_count 0 is supported as a BacDive count; it does not deny
the isolate in the nucleotide submission. No supported
culture-deposit-to-genome chain was established.

Optional nomenclature, mappings, definition, literature and graph
fields can remain empty. The marker is an optional enrichment
lead, not a missing required assembly link.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, attestation and seed provenance
agree with inspected sources. The YAML does not overstate marker,
host or unpublished-study metadata.

## Recommended Edits

None required. Keep generated YAML unchanged.

Future authorized marker enrichment belongs in a maintained seeder
mechanism with tests or a deliberately designed persistent curator
overlay; no existing overlay path is assumed. Keep JF792715.1
typed as a nucleotide sequence, not a genome.

## Follow-up Checks

- Retain the complete squidInt_01 designation and unresolved
  species assignment unless an authority supports a change.
- Verify future culture/genome links through exact own-deposit
  and source-native identities. Host or study overlap is insufficient.
- Preserve the source host spelling as provenance. Any normalized
  host or tissue assertion requires its own supporting authority
  or annotation; do not infer anatomy from the isolate abbreviation.
- Require isolate-specific experiments for phenotype enrichment
  in the appropriate sibling repository.
- Following authorized maintained-input changes, perform source
  refresh, seed dry run/canary and actual-file inspection, rerun
  both target validators, then full `just verify-corpus` and `just qc`.

## Additional Notes

This target was reviewed individually using its complete YAML,
own source rows, live taxonomy, sequence metadata and validation
results. A neighboring record's verdict was not used as evidence.

No paid research, genome FASTA download, external contact,
GitHub mutation, history append or status promotion occurred.
Eukaryota and its completed reviews remain unchanged.
