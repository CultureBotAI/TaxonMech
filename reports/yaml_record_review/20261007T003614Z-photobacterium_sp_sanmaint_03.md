# YAML Record Review: Photobacterium sp. sanmaInt_03

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_sanmaint_03.yaml`
- Started UTC: 2026-10-07T00:34:30Z
- Finished UTC: 2026-10-07T00:36:14Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read:
`NCBITaxon:1035385`, Photobacterium sp. sanmaInt_03,
SPECIES, BACTERIA, parent `NCBITaxon:2628852`, genetic
code 11, grounding EXACT and mapping status SEEDED.
Its ten ancestors, zero BacDive strains, single NCBITAXON NAME
attestation and single seed event were examined. It has no
synonyms, nomenclature, taxonomy mappings, deposits, genomes,
definition, literature evidence, phenotype or causal graph.

The PATHS entry uniquely identifies the file. An ignored-inclusive
filename search found no prior report for this stem. Only this new
report is written; the YAML, inventories, code, generated products,
prior reports, history and lifecycle status remain unchanged.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_sanmaint_03.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_sanmaint_03.yaml --out /private/tmp/psan03-strict.tsv`: exit 0, one file scanned, zero ERROR rows. The actual TSV was read and is header-only.
- Read-only structured comparisons checked every pinned ancestor,
  the backbone and synonym fields, seven non-NCBI inventories,
  PATHS, scope and attestation. Exact type-material, merged-ID
  and dropped-ID scans found no target rows. There are no
  descendant taxa beneath this record in the pinned backbone.

Not checked: full-corpus `just verify-corpus`, `just qc`,
`just validate-all`, `just validate-history`,
`just validate-products`, provenance hash recomputation,
tests, generated-site drift and publication size gates.
No target-only substitute was invented for a corpus gate.
There are no curator-added graph or history references to resolve.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222047` and the complete native
scientific-name row at
`data/catalog/ncbi_names-0005.jsonl.gz:31527` agree with
the exact target identity. The backbone additionally agrees with
the species rank, parent, genetic code and 2026-09-13 snapshot.
`data/taxa/PATHS.tsv:14538` and
`curation/seed_scope.tsv:322318` agree with the filename
and inclusion reason.

All ten ancestor IDs, labels and ranks match the pinned source:

`1 root / NO_RANK; 131567 cellular organisms / CELLULAR_ROOT; 2 Bacteria / DOMAIN; 3379134 Pseudomonadati / KINGDOM; 1224 Pseudomonadota / PHYLUM; 1236 Gammaproteobacteria / CLASS; 135623 Vibrionales / ORDER; 641 Vibrionaceae / FAMILY; 657 Photobacterium / GENUS; 2628852 unclassified Photobacterium / NO_RANK`.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035385&retmode=xml)
and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035385)
were read in full. They retain this exact label, species rank,
parent and ancestry. XML confirms code 11; Datasets includes
root. XML supplies no alternative name or type material.

Preserve the full sanmaInt_03 designation and NCBI's SPECIES
rank despite the strain-like name. EXACT is correspondence with
this unresolved taxonomic concept, not a claim that its species
has a formal nomenclatural identity.

## Evidence

The one NCBITAXON NAME assertion and its snapshot trace to the
backbone. The seed event reproduces the source list and exact
scope reason. The three manifest timestamp fields were read
during this turn: raw 2026-09-13T17:50:44Z,
ATB 2026-09-13T17:54:04Z and StrainInfo
2026-09-13T17:29:00Z. The inspected
`src/taxonmech/seed.py::_seed_timestamp` selects their
maximum, supporting the seed timestamp. It is not human review.

An exact non-expanded nuccore search returned one entry:
[JF792705.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792705.1).
Its complete metadata, references and feature table identify
sanmaInt_03 and taxon 1035385. This is a 1251-base partial
16S rRNA gene, not an assembly. Source annotations name host
Cololabis saira and Auckland Fish Market, North Island, New
Zealand. The entry supplies no BioSample, BioProject, registered
culture deposit or assembly accession.

The research reference, by Wollenberg, Rainey and Ruby, is marked
Unpublished. Its title concerns experimental and taxonomic study
of bioluminescence variation among New Zealand Vibrionaceae
isolates; no DOI or PMID is supplied. Wollenberg and Ruby submitted
the record on 7 April 2011 from the University of Wisconsin.
This metadata is not direct evidence of a sanmaInt_03
bioluminescence phenotype.

Exact-label, punctuation-variant, accession and author/designation
web searches produced taxonomy listings but no inspected
publication joined to this exact isolate. Searches for the shared
research title and author/topic were also conducted during this
turn; no resulting lead was used as experimental evidence for
sanmaInt_03. This is not an exhaustive literature-absence claim.

The exact non-expanded Assembly search returned zero with a
phrase-not-found warning, and the
[NCBI Datasets genome endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035385/dataset_report)
returned an empty object. Both results are bounded to this taxon
and date, not every alternative assignment.

The structured iModulonDB inventory was successfully queried and
all 28 rows inspected earlier in this same turn, before open web
research, using
`uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`.
No Photobacterium dataset covers sanmaInt_03. Vibrio datasets
are not transferable by family membership. This adapter is not
applicable; noncoverage does not contradict biological claims.

## Completeness

A completed `rg --no-ignore --hidden -n -z -i` search used
`\b1035385\b|Photobacterium sp\. sanmaInt_03\b|photobacterium_sp_sanmaint_03\b|\bsanmaInt[-_ ]?03\b`
over `data/raw`, `data/catalog`, `data/bacdive`,
`data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and
`history`. It included ignored, hidden and compressed files.
All three matching rows, backbone, scientific name and scope,
were inspected in full. Five SOURCE.json files were separately
parsed and history filenames checked independently of gitignore;
no further target matches were found.

A completed whole-accession search for JF792705 across the same
ten roots returned zero matches. Its separate SOURCE.json and
history-filename checks also found none. These are bounded local
results, not claims about all public archives.

The exact-taxonomy scans found no BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventory rows. With no descendants,
zero BacDive strains is supported; it does not deny the isolate
represented by the marker submission.

No supported whole-deposit or assembly chain was established by
the inspected evidence. Optional nomenclature, mappings, definition,
literature and causal-graph fields may remain empty. The marker is
an optional enrichment lead, not a missing required genome link.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The identity, complete lineage, source attestation and
seed provenance agree with the inspected evidence. The YAML does
not overstate the marker record or unpublished research reference.

## Recommended Edits

None required. Do not hand-edit generated YAML.

Any future authorized marker representation belongs in a maintained
seeder mechanism with tests or a deliberately designed persistent
curator overlay; no existing overlay path is assumed.
Keep JF792705.1 as a nucleotide related record, never an assembly.
Do not transfer sanmaInt_01's distinct JF792704.1 marker into
this record merely because the submissions share context.

## Follow-up Checks

- Preserve sanmaInt_03, including case and leading zero, until
  explicit authority evidence supports a changed identity.
- Before a deposit or genome link is added, verify its complete
  own-deposit/source identity chain and accession status. Shared
  host, locality, genus or research title is insufficient.
- Require inspected isolate-specific experiments for any phenotype
  enrichment in the relevant sibling repository.
- After authorized maintained-input changes, use source refresh,
  seed dry run/canary and actual-file inspection, then both
  target validators and full `just verify-corpus` and
  `just qc`. No such curation was performed here.

## Additional Notes

The target was reviewed individually, with its own taxonomy,
source rows, searches, nucleotide entry and validation results.
Neither neighboring sanmaInt records nor sanmaSkn records supply
identity evidence for it.

No paid research, genome FASTA download, external contact, GitHub
mutation, history append or lifecycle promotion occurred.
Eukaryota and its completed reports were not changed.
