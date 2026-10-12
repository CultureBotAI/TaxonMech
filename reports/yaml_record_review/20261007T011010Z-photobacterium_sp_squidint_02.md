# YAML Record Review: Photobacterium sp. squidInt_02

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_squidint_02.yaml`
- Started UTC: 2026-10-07T01:08:46Z
- Finished UTC: 2026-10-07T01:10:10Z
- Verdict: pass

## Target

The entire generated TaxonRecord was read: NCBITaxon:1035395,
Photobacterium sp. squidInt_02, SPECIES, BACTERIA, parent
NCBITaxon:2628852, code 11, EXACT grounding and SEEDED
mapping status. It has ten ancestors, zero BacDive strains,
one NCBITAXON NAME attestation and one seed event. There are
no synonyms, nomenclature, mappings, deposits, genomes,
definition, literature evidence, phenotypes or causal graph.

PATHS uniquely resolves this target. An ignored-inclusive report
filename search found no prior review for this stem. The only
write is this new report; YAML, inputs, previous reports, history
and lifecycle status remain unchanged.

## Validation

Commands used UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_squidint_02.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_squidint_02.yaml --out /private/tmp/psqi02-strict.tsv`: exit 0, one file scanned, zero ERROR rows; the actual TSV was read and is header-only.
- Structured comparisons checked the complete pinned backbone,
  all lineage entries, synonyms, seven non-NCBI inventories,
  PATHS, scope and attestation. Exact type-material, merged-ID
  and dropped-ID scans found no target rows. The pinned backbone
  has no children beneath this taxon.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just validate-history`, `just validate-products`,
provenance hash recomputation, tests, site drift and publication-size
gates. These corpus-wide gates were skipped for this individual
read-only review; no target-only substitute was invented.
The target contains no curator-added graph or history reference.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222057`
supports every identity field and the 2026-09-13 snapshot.
The native scientific-name row at
`data/catalog/ncbi_names-0005.jsonl.gz:31537` agrees.
`data/taxa/PATHS.tsv:14548` and `curation/seed_scope.tsv:322328`
confirm the unique slug and exact scope reason.

All ancestor IDs, names and ranks agree with the pinned source:

`1 root / NO_RANK; 131567 cellular organisms / CELLULAR_ROOT; 2 Bacteria / DOMAIN; 3379134 Pseudomonadati / KINGDOM; 1224 Pseudomonadota / PHYLUM; 1236 Gammaproteobacteria / CLASS; 135623 Vibrionales / ORDER; 641 Vibrionaceae / FAMILY; 657 Photobacterium / GENUS; 2628852 unclassified Photobacterium / NO_RANK`.

The full current [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035395&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035395)
were inspected. They retain the exact name, species rank,
parent and ancestry. XML confirms code 11 and supplies no
alternative name or type material; Datasets includes root.

EXACT denotes correspondence to this unresolved NCBI concept,
not formal species nomenclature. Preserve squidInt_02 in full:
other numbered squidInt or squidSkn isolates are not equivalent.
The strain-like label does not override NCBI's SPECIES rank.

## Evidence

The NCBITAXON source_id, source_label, count 1, unit NAME and
snapshot match the backbone. The seed event matches its scope
reason and source list. Manifest timestamp fields read this turn
were raw 2026-09-13T17:50:44Z, ATB
2026-09-13T17:54:04Z and StrainInfo
2026-09-13T17:29:00Z. The inspected
`src/taxonmech/seed.py::_seed_timestamp` selects their maximum,
matching the event. This is seed provenance, not human approval.

The exact non-expanded nuccore query returned UID 333797998.
Complete [JF792716.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF792716.1),
references and features explicitly name squidInt_02 and taxon
1035395. It is a 1251-base partial 16S rRNA gene, not
an assembly. The host qualifier reads "Nototodarus gouldi";
this report preserves that submitted spelling. Locality is
New Zealand: North Island, Auckland Fish Market. No assembly,
BioSample, BioProject or registered culture-deposit accession
is supplied by the entry.

The Wollenberg, Rainey and Ruby research reference is marked
Unpublished without DOI or PMID. Its title concerns experimental
and taxonomic study of bioluminescence variation in New Zealand
Vibrionaceae isolates. Direct submission by Wollenberg and Ruby
is dated 7 April 2011, University of Wisconsin. These annotations
do not establish a measured bioluminescence phenotype or specific
tissue source for squidInt_02.

Exact label, punctuation variants, marker accession,
author/designation and genome/strain web queries supplied no
inspected publication joined to this exact isolate. The common
research title was searched earlier this turn. These bounded
queries are not an exhaustive literature-absence proof; taxonomy
search listings were not used as experimental evidence.

The exact non-expanded Assembly search returned zero, with a
phrase-not-found warning. The independently inspected
[Datasets genome response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035395/dataset_report)
was an empty object. This result is bounded to this taxon and
retrieval date, not every alternative classification.

The structured adapter inventory was successfully queried earlier
this turn before open web discovery:
`uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`.
All 28 returned rows were inspected. None covers this
Photobacterium target. iModulonDB is not applicable; related
Vibrio datasets cannot be transferred, and noncoverage is not
negative biological evidence.

## Completeness

A completed `rg --no-ignore --hidden -n -z -i` search used
`\b1035395\b|Photobacterium sp\. squidInt_02\b|photobacterium_sp_squidint_02\b|\bsquidInt[-_ ]?02\b`
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
including ignored, hidden and compressed files. All three
matches, backbone, scientific name and scope, were read in full.
Five SOURCE.json files were separately parsed and history
filenames checked independently of gitignore; no further target
matches were found.

A completed whole-accession JF792716 search across the same ten
roots returned zero matches. Separate SOURCE.json and history
filename scans also found none. These are bounded local
findings, not statements about every public archive.

Exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive,
Madin or BactoTraits inventory rows. With no descendants,
strain_count 0 is supported as a BacDive count and does not
deny the isolate in the nucleotide submission. No supported
culture-deposit-to-genome chain was established.

Optional nomenclature, mappings, definition, literature and graph
fields can remain empty. The partial marker is an optional
enrichment lead, not a missing required assembly link.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, full lineage, attestation and seed
provenance agree with inspected evidence. The YAML does not
overstate the sequence or unpublished-study annotations.

## Recommended Edits

None required. Do not hand-edit generated YAML.

Future authorized marker enrichment belongs in a maintained seeder
mechanism with tests or a deliberately designed persistent curator
overlay; no existing overlay path is assumed. Preserve JF792716.1
as a nucleotide related record, not a genome identifier.

## Follow-up Checks

- Preserve the complete squidInt_02 designation and unresolved
  species assignment unless an authority supports a change.
- Verify future culture/genome links through full own-deposit
  and source-native identities. Shared host or study does not
  establish strain or genome equivalence.
- Preserve the source host spelling as provenance; any normalized
  host or tissue assertion needs its own supporting authority or
  annotation. Do not infer anatomy from the isolate abbreviation.
- Require isolate-specific experiments for phenotype enrichment
  in the appropriate sibling repository.
- After authorized maintained-input changes, use source refresh,
  seed dry run/canary and actual-file inspection, rerun both
  target validators, then full `just verify-corpus` and `just qc`.

## Additional Notes

This target was reviewed individually using its entire YAML,
own source matches, live taxonomy, nucleotide metadata and
validation results. Neighboring record verdicts were not evidence.

No paid research, genome FASTA download, external contact,
GitHub mutation, history append or lifecycle promotion occurred.
Eukaryota and its completed reports remain unchanged.
