# YAML Record Review: Photobacterium sp. sanmaInt_06

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_sanmaint_06.yaml`
- Started UTC: 2026-10-07T00:43:52Z
- Finished UTC: 2026-10-07T00:45:57Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read:
`NCBITaxon:1035388`, Photobacterium sp. sanmaInt_06,
SPECIES, BACTERIA, parent `NCBITaxon:2628852`, genetic
code 11, grounding EXACT and mapping status SEEDED.
It contains ten ancestors, zero BacDive strains, one NCBITAXON
NAME attestation and one seed event. It asserts no synonyms,
nomenclature, mappings, deposits, genomes, definition, literature
evidence, phenotypes or causal graph.

PATHS uniquely resolves this target. An ignored-inclusive filename
search found no prior review for this stem. Only this new report
is written; the YAML, code, inventories, generated products,
previous reports, history and lifecycle status remain unchanged.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_sanmaint_06.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_sanmaint_06.yaml --out /private/tmp/psan06-strict.tsv`: exit 0, one file scanned, zero ERROR rows. The actual TSV was read and is header-only.
- Read-only structured comparisons checked the full pinned lineage,
  backbone and synonyms, seven non-NCBI inventories, PATHS,
  scope and attestation. Exact type-material, merged-ID and
  dropped-ID scans found no target rows. The pinned backbone has
  no children beneath this taxon.

Not checked: full-corpus `just verify-corpus`, `just qc`,
`just validate-all`, `just validate-history`,
`just validate-products`, provenance hash recomputation,
tests, site drift and publication size gates. No target-only
substitute for a corpus gate was invented. No curator-added
graph or history reference is present in the target.

## Identity and Grounding

The complete backbone row at
`data/raw/ncbitaxon_taxa.tsv:222050` agrees with ID, label,
rank, parent, code and the 2026-09-13 snapshot.
The complete native scientific-name row at
`data/catalog/ncbi_names-0005.jsonl.gz:31530` agrees.
`data/taxa/PATHS.tsv:14541` and
`curation/seed_scope.tsv:322321` support the filename and
scope reason.

All ten ancestor IDs, names and ranks agree with the pinned source:

`1 root / NO_RANK; 131567 cellular organisms / CELLULAR_ROOT; 2 Bacteria / DOMAIN; 3379134 Pseudomonadati / KINGDOM; 1224 Pseudomonadota / PHYLUM; 1236 Gammaproteobacteria / CLASS; 135623 Vibrionales / ORDER; 641 Vibrionaceae / FAMILY; 657 Photobacterium / GENUS; 2628852 unclassified Photobacterium / NO_RANK`.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035388&retmode=xml)
and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035388)
were read in full. They retain the exact name, species rank,
parent and ancestry. XML confirms code 11, and Datasets includes
root. XML supplies no alternative name or type material.

The full sanmaInt_06 designation must be retained. Its strain-like
name does not override NCBI's SPECIES rank. EXACT denotes
correspondence with this particular unresolved taxonomic concept,
not a formally named species or another numbered isolate.

## Evidence

The NCBITAXON NAME count 1, ID, label and snapshot agree with
the backbone. The seed event matches its scope reason and
NCBITAXON source list. Manifest timestamp fields read during this
turn were raw 2026-09-13T17:50:44Z,
ATB 2026-09-13T17:54:04Z and StrainInfo
2026-09-13T17:29:00Z. The inspected
`src/taxonmech/seed.py::_seed_timestamp` selects their
maximum, matching the record. This is not human review history.

The exact non-expanded nuccore search returned one record:
[JF792708.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792708.1).
Its full metadata, references and feature table explicitly identify
sanmaInt_06 and taxon 1035388. It is a 1251-base partial
16S rRNA gene, not a whole-genome assembly. The source names
host Cololabis saira and Auckland Fish Market, North Island,
New Zealand, as locality. No assembly, BioSample, BioProject or
registered culture-deposit accession is supplied by the entry.

The research reference by Wollenberg, Rainey and Ruby is marked
Unpublished, without a DOI or PMID. Its title concerns experimental
and taxonomic study of bioluminescence variation in New Zealand
Vibrionaceae isolates. Wollenberg and Ruby directly submitted
the record on 7 April 2011 from the University of Wisconsin.
These annotations do not establish an experimental bioluminescence
phenotype for sanmaInt_06.

Exact-label, punctuation-variant, marker-accession and
author/designation web searches produced taxonomy listings but
no inspected publication joined to this exact isolate. The shared
research title was also searched earlier in this turn; no result
was used as experimental evidence for sanmaInt_06. This is not
an exhaustive literature-absence claim.

The exact non-expanded Assembly search returned zero with a
phrase-not-found warning. The
[NCBI Datasets genome endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035388/dataset_report)
returned an empty object. These observations are bounded to this
taxon and date, not all alternative classifications.

The structured iModulonDB inventory was queried earlier in this
turn before open web research:
`uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`.
All 28 returned dataset rows were inspected. None covers this
Photobacterium target. Vibrio datasets cannot be transferred by
family membership. The adapter is not applicable; noncoverage
is not negative biological evidence.

## Completeness

A completed `rg --no-ignore --hidden -n -z -i` search used
`\b1035388\b|Photobacterium sp\. sanmaInt_06\b|photobacterium_sp_sanmaint_06\b|\bsanmaInt[-_ ]?06\b`
across `data/raw`, `data/catalog`, `data/bacdive`,
`data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and
`history`. Ignored, hidden and compressed files were included.
All three matches, backbone, scientific name and scope, were
read in full. Five SOURCE.json files were separately parsed,
and history filenames checked independently of gitignore; no
additional target matches were found.

A completed whole-accession search for JF792708 across the same
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
enrichment lead, not a missing required genome link.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, full lineage, attestation and seed provenance
agree with the inspected evidence. The YAML does not overstate
the marker submission or the unpublished study reference.

## Recommended Edits

None required. Do not hand-edit the generated YAML.

Future authorized marker enrichment belongs in a maintained seeder
mechanism with tests or a deliberately designed persistent curator
overlay; no existing overlay path is assumed. Preserve JF792708.1
as a nucleotide related record if represented, not as an assembly.

## Follow-up Checks

- Preserve the complete sanmaInt_06 designation and unresolved
  species assignment unless an authority supports a change.
- Before adding a culture or genome link, verify the complete
  own-deposit/source-native identity chain and current accession
  status. Shared genus, host, locality or study title is insufficient.
- Require inspected isolate-specific experiments for phenotype
  enrichment in the relevant sibling repository.
- After authorized maintained-input changes, use source refresh,
  seed dry run/canary and actual-file inspection, rerun both
  target validators, then full `just verify-corpus` and
  `just qc`. No curation was performed here.

## Additional Notes

This record was reviewed individually using its own complete
YAML, source matches, taxonomy, nucleotide metadata and validation
results. Neighboring sanmaInt or similarly numbered sanmaSkn
entries do not supply identity evidence for it.

No paid research, genome FASTA download, external contact, GitHub
mutation, history append or lifecycle promotion occurred.
Eukaryota and its completed reviews were not changed.
