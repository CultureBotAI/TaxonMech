# YAML Record Review: Photobacterium sp. sanmaSkn_01

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_sanmaskn_01.yaml`
- Started UTC: 2026-10-07T00:59:32Z
- Finished UTC: 2026-10-07T01:00:53Z
- Verdict: pass

## Target

The full generated TaxonRecord was read: NCBITaxon:1035392,
Photobacterium sp. sanmaSkn_01, SPECIES, BACTERIA, parent
NCBITaxon:2628852, genetic code 11, grounding EXACT, mapping
status SEEDED. It has ten ancestors, zero BacDive strains,
one NCBITAXON NAME attestation and one seed event. No synonyms,
nomenclature, mappings, deposits, genome links, definition,
literature evidence, phenotype or causal graph is asserted.

PATHS uniquely resolves the target. An ignored-inclusive filename
search found no earlier review for this stem. Only this new report
is written; generated records, maintained inputs, previous reports,
history and lifecycle status are unchanged.

## Validation

Commands used UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_sanmaskn_01.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_sanmaskn_01.yaml --out /private/tmp/pskn01-strict.tsv`: exit 0, one file scanned, zero ERROR rows. The actual output TSV was read and is header-only.
- Read-only structured comparisons checked the full backbone,
  lineage, synonyms, seven non-NCBI inventories, PATHS, scope
  and attestation. Exact type-material, merged-ID and dropped-ID
  scans found no target rows. There are no children beneath this
  taxon in the pinned backbone.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just validate-history`, `just validate-products`,
provenance hash recomputation, tests, site drift and publication-size
gates. No target-only substitute for a corpus gate was invented.
No curator-added graph or history reference is present.

## Identity and Grounding

The complete row at `data/raw/ncbitaxon_taxa.tsv:222054`
supports the ID, label, rank, parent, code and 2026-09-13
snapshot. The complete native scientific-name row at
`data/catalog/ncbi_names-0005.jsonl.gz:31534` agrees.
`data/taxa/PATHS.tsv:14545` and `curation/seed_scope.tsv:322325`
confirm the unique filename and recorded scope reason.

All ten ancestor IDs, names and ranks agree with the pinned source:

`1 root / NO_RANK; 131567 cellular organisms / CELLULAR_ROOT; 2 Bacteria / DOMAIN; 3379134 Pseudomonadati / KINGDOM; 1224 Pseudomonadota / PHYLUM; 1236 Gammaproteobacteria / CLASS; 135623 Vibrionales / ORDER; 641 Vibrionaceae / FAMILY; 657 Photobacterium / GENUS; 2628852 unclassified Photobacterium / NO_RANK`.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035392&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035392)
were read in full. They retain the exact name, species rank,
parent and ancestry. XML confirms code 11 and supplies no
alternate name or type material; Datasets includes root.

Preserve sanmaSkn_01 in full. sanmaInt_01 or another numbered
sanmaSkn isolate is not interchangeable. The strain-like label
does not override NCBI's SPECIES rank. EXACT means this
unresolved taxonomic concept, not a formal species name.

## Evidence

The NCBITAXON source ID, label, NAME count 1 and snapshot agree
with the backbone. The seed event agrees with the scope reason
and source list. Manifest timestamp fields read this turn were
raw 2026-09-13T17:50:44Z, ATB 2026-09-13T17:54:04Z and
StrainInfo 2026-09-13T17:29:00Z. The inspected
`src/taxonmech/seed.py::_seed_timestamp` chooses their maximum,
matching the record. It does not denote human review approval.

The exact non-expanded nuccore query returned one UID, 333797995.
Complete [JF792713.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF792713.1),
references and features explicitly identify sanmaSkn_01 and
taxon 1035392. It is a 1251-base partial 16S rRNA gene,
not a whole-genome assembly. Source qualifiers name host
Cololabis saira and locality New Zealand: North Island,
Auckland Fish Market. No assembly, BioSample, BioProject or
registered culture-deposit accession is supplied in the entry.

The Wollenberg, Rainey and Ruby research reference is marked
Unpublished and contains no DOI or PMID. Its title concerns
experimental and taxonomic study of bioluminescence variation in
New Zealand Vibrionaceae isolates. The direct-submission reference
names Wollenberg and Ruby, 7 April 2011, University of Wisconsin.
Neither that title nor the sequence annotation establishes a
measured bioluminescence phenotype or a specific tissue source.

Exact label, punctuation variants, marker accession,
author/designation and genome/strain web searches supplied no
inspected publication joined to this exact isolate. The common
research title was searched earlier this turn. This is bounded
discovery, not an exhaustive literature-absence claim.

The exact non-expanded Assembly query returned zero with a
phrase-not-found warning. The separately inspected
[NCBI Datasets genome endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035392/dataset_report)
returned an empty object. These results are specific to this
taxon and retrieval date, not all possible alternate classifications.

The structured adapter inventory was successfully queried earlier
this turn, before open web discovery:
`uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`.
All 28 rows were inspected; none covers this Photobacterium
target. iModulonDB is not applicable. Vibrio datasets cannot
be transferred through family membership, and noncoverage is
not negative biological evidence.

## Completeness

The completed `rg --no-ignore --hidden -n -z -i` search used
`\b1035392\b|Photobacterium sp\. sanmaSkn_01\b|photobacterium_sp_sanmaskn_01\b|\bsanmaSkn[-_ ]?01\b`
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
Ignored, hidden and compressed files were included. All three
matching rows, backbone, scientific name and scope, were read
fully. Five SOURCE.json files were parsed separately and history
filenames checked independently of gitignore; no additional target
matches were found.

A completed whole-accession JF792713 search across the same ten
roots returned zero matches. Its SOURCE.json and history-filename
checks also found none. These are bounded local findings, not
claims that public evidence cannot exist elsewhere.

Exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive,
Madin or BactoTraits inventory rows. With no descendants,
strain_count 0 is supported as a BacDive count; it does not deny
the isolate represented in the nucleotide submission.

No supported culture-deposit-to-genome chain was established.
Optional nomenclature, mappings, definition, literature and
causal graph fields can remain empty. The marker is an optional
enrichment lead, not a missing required assembly link.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The identity, full lineage, attestation and seed
provenance agree with the inspected evidence. The record does not
overstate sequence metadata as genome, tissue or phenotype evidence.

## Recommended Edits

None required. Keep generated YAML unchanged.

Future authorized marker enrichment belongs in a maintained seeder
mechanism with tests or a deliberately designed persistent curator
overlay; no existing overlay path is assumed. Preserve JF792713.1
as a nucleotide related record, not a genome identifier.

## Follow-up Checks

- Preserve the full sanmaSkn_01 designation and unresolved species
  assignment unless authoritative evidence supports a change.
- Verify any culture or genome accession through the full own-deposit
  and source-native identity chain. Related isolate names, hosts,
  localities or shared submission titles do not establish equivalence.
- Require explicit source evidence for tissue or phenotype enrichment
  in the relevant sibling repository; do not decode the isolate
  abbreviation into an unsupported biological assertion.
- After authorized maintained-input changes, perform source refresh,
  seed dry run/canary and actual-file inspection, repeat both target
  validators, then full `just verify-corpus` and `just qc`.

## Additional Notes

The target was reviewed individually from its full YAML, own
source rows, live taxonomy, sequence metadata and validation
results. Neighboring records did not supply its verdict.

No paid research, genome FASTA download, external contact,
GitHub mutation, history append or lifecycle promotion occurred.
Eukaryota and its completed reviews remain unchanged.
