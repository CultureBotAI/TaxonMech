# YAML Record Review: Photobacterium sp. sanmaInt_09

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_sanmaint_09.yaml`
- Started UTC: 2026-10-07T00:54:15Z
- Finished UTC: 2026-10-07T00:56:14Z
- Verdict: pass

## Target

The entire generated TaxonRecord was read: NCBITaxon:1035390,
Photobacterium sp. sanmaInt_09, SPECIES, BACTERIA, parent
NCBITaxon:2628852, genetic code 11, EXACT grounding and
SEEDED mapping status. It has ten ancestors, strain_count 0,
one NCBITAXON NAME attestation and one seed event.
There are no synonyms, nomenclature entries, mappings, deposits,
genomes, literature evidence, phenotype assertions or causal graphs.

PATHS uniquely identifies the record. An ignored-inclusive filename
search under reports/yaml_record_review found no prior report for
this stem. Only this new report is written; generated YAML,
maintained inputs, previous reports, history and status are unchanged.

## Validation

Commands used UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_sanmaint_09.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_sanmaint_09.yaml --out /private/tmp/psan09-strict.tsv`: exit 0, one file scanned, zero ERROR rows. The actual TSV was read and contains only its header.
- Structured read-only comparisons checked all ten lineage entries,
  the complete backbone row, synonyms, seven non-NCBI inventories,
  PATHS, scope and attestation. Exact type-material, merged-ID and
  dropped-ID scans found no target rows. There are no children in
  the pinned backbone.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just validate-history`, `just validate-products`,
provenance hash recomputation, tests, site drift and publication-size
gates. No invented target-only substitute was used for a corpus
gate. The target contains no curator-added graph or history reference.

## Identity and Grounding

The full row at `data/raw/ncbitaxon_taxa.tsv:222052` supports the
identifier, label, rank, parent, genetic code and snapshot date.
The native scientific name at
`data/catalog/ncbi_names-0005.jsonl.gz:31532` agrees.
`data/taxa/PATHS.tsv:14543` and `curation/seed_scope.tsv:322323`
confirm the unique slug and the recorded scope reason.

The complete root-first lineage agrees with the pinned inventory:

`1 root / NO_RANK; 131567 cellular organisms / CELLULAR_ROOT; 2 Bacteria / DOMAIN; 3379134 Pseudomonadati / KINGDOM; 1224 Pseudomonadota / PHYLUM; 1236 Gammaproteobacteria / CLASS; 135623 Vibrionales / ORDER; 641 Vibrionaceae / FAMILY; 657 Photobacterium / GENUS; 2628852 unclassified Photobacterium / NO_RANK`.

Current [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035390&retmode=xml)
and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035390)
were read in full. Both retain the target name, species rank,
parent and ancestry; XML confirms code 11, Datasets includes
root, and XML supplies no alternative name or type material.

EXACT is correspondence to this unresolved NCBI concept, not
formal species nomenclature. The complete sanmaInt_09 designation
is essential; neither a nearby numbered isolate nor a named
Photobacterium species supplies its identity.

## Evidence

The NCBITAXON source_id, label, NAME count 1 and 2026-09-13
snapshot are supported by the backbone. The seed event reproduces
the scope reason and source list. Manifest extracted_at fields were
read: raw 2026-09-13T17:50:44Z, ATB 2026-09-13T17:54:04Z,
StrainInfo 2026-09-13T17:29:00Z. The inspected
`src/taxonmech/seed.py::_seed_timestamp` selects their maximum,
which is the recorded event timestamp. This is seed provenance,
not human review approval.

The exact non-expanded nuccore query returned one UID, 333797993.
Complete [JF792711.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF792711.1),
references and feature qualifiers identify sanmaInt_09 and taxon
1035390. The sequence is a 1251-base partial 16S rRNA gene.
The source gives host Cololabis saira and locality New Zealand:
North Island, Auckland Fish Market. It supplies no assembly,
BioSample, BioProject or registered culture-deposit accession.

The research reference by Wollenberg, Rainey and Ruby remains
marked Unpublished with no DOI or PMID. Its title concerns
experimental and taxonomic study of bioluminescence variation
in New Zealand Vibrionaceae isolates. A second reference records
direct submission by Wollenberg and Ruby on 7 April 2011 from
the University of Wisconsin. Neither the study title nor the
marker annotation establishes a measured phenotype for sanmaInt_09.

Exact-label, punctuation-variant, accession, author/designation and
genome/strain web queries were inspected as discovery leads. No
inspected publication was joined to this exact isolate. The shared
research title was also searched. This does not prove literature
absence, and search snippets were not promoted to evidence.

The exact non-expanded Assembly query returned zero, with a
phrase-not-found warning. The independently inspected
[NCBI Datasets genome response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035390/dataset_report)
was an empty object. This is a taxon- and date-bounded result,
not a claim covering every alternate classification.

Before open web discovery, the structured adapter was queried:
`uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`.
All 28 returned rows were inspected; none covers this
Photobacterium target. iModulonDB is not applicable here.
Vibrio datasets cannot be transferred through family membership;
noncoverage is not negative biological evidence.

## Completeness

A completed `rg --no-ignore --hidden -n -z -i` search used
`\b1035390\b|Photobacterium sp\. sanmaInt_09\b|photobacterium_sp_sanmaint_09\b|\bsanmaInt[-_ ]?09\b`
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
Ignored, hidden and compressed files were included. All three
matches, backbone, scientific name and scope, were read completely.
Five SOURCE.json files were parsed separately, and history
filenames checked independently of gitignore; no additional
target matches were found.

The whole-accession search for JF792711 completed across the
same ten roots with zero matches. Separate SOURCE.json and
history-filename checks also found none. These are bounded
local searches, not public-archive absence claims.

Exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive,
Madin or BactoTraits inventory rows. With no descendants in
the backbone, strain_count 0 is supported as a BacDive count;
it does not deny the isolate in the sequence submission.

No supported culture-deposit-to-genome chain was established.
Empty optional nomenclature, mappings, definition, literature
and graph fields are acceptable. JF792711.1 is an optional
marker-enrichment lead, not a missing required assembly link.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record's identity, lineage, attestation and seed
provenance agree with inspected sources. It makes no unsupported
genome or experimental phenotype assertion.

## Recommended Edits

None required. Do not hand-edit the generated YAML.

Future authorized marker enrichment belongs in a maintained seeder
mechanism with tests, or a deliberately designed persistent curator
overlay; an existing overlay path is not assumed. Represent
JF792711.1 as a nucleotide related record, never as an assembly.

## Follow-up Checks

- Retain the full sanmaInt_09 designation and current unresolved
  species assignment until authoritative evidence supports a change.
- Before adding deposit or genome links, verify the exact own-deposit
  and source-native accession chain. Shared names, taxonomy, host
  or study titles do not establish strain or genome equivalence.
- Require inspected isolate-specific experiments for phenotype
  enrichment in the relevant sibling repository.
- For a future authorized maintained-input change, perform source
  refresh, seed dry run/canary and actual-file inspection, rerun the
  two target validators, then full `just verify-corpus` and `just qc`.

## Additional Notes

This target was reviewed individually using its own complete YAML,
source matches, live taxonomy, nucleotide metadata and validation
results. No verdict was transferred from neighboring records.

No paid research, genome FASTA download, external contact,
GitHub mutation, history append or status promotion occurred.
Eukaryota and its completed reviews remain untouched.
