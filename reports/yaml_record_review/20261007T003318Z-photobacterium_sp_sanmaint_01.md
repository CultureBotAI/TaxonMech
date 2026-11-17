# YAML Record Review: Photobacterium sp. sanmaInt_01

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_sanmaint_01.yaml`
- Started UTC: 2026-10-07T00:30:48Z
- Finished UTC: 2026-10-07T00:33:18Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read:
`NCBITaxon:1035384`, Photobacterium sp. sanmaInt_01,
`SPECIES`, `BACTERIA`, parent `NCBITaxon:2628852`,
genetic code 11, grounding EXACT and mapping status SEEDED.
It contains ten ancestors, zero BacDive strains, one NCBITAXON
NAME attestation and one seed event. It asserts no synonyms,
nomenclature, mappings, deposits, genomes, literature evidence,
definition, phenotype or causal graph.

PATHS uniquely resolves this target. An ignored-inclusive filename
search found no prior report for this stem. This review writes only
this new report, leaving YAML, code, inventories, generated products,
prior reports, history and lifecycle status unchanged.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_sanmaint_01.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_sanmaint_01.yaml --out /private/tmp/psan01-strict.tsv`: exit 0, one file scanned, zero ERROR rows. The emitted TSV was read and is header-only.
- Read-only structured comparisons checked the complete pinned
  ancestor chain, backbone, synonyms, seven non-NCBI inventories,
  PATHS, scope and attestation. Exact type-material, merged-ID and
  dropped-ID scans found no target rows. There are no children
  beneath this taxon in the pinned backbone.

Not checked: full-corpus `just verify-corpus`, `just qc`,
`just validate-all`, `just validate-history`,
`just validate-products`, provenance hash recomputation,
tests, site drift and publication size gates. No target-only
substitute was invented for a corpus gate. No curator-added graph
or history reference is asserted by the target.

## Identity and Grounding

The complete source row `data/raw/ncbitaxon_taxa.tsv:222046`
agrees with the ID, label, rank, parent, code and snapshot.
The complete native scientific-name row at
`data/catalog/ncbi_names-0005.jsonl.gz:31526` supplies the
same name, not a culture deposit.
`data/taxa/PATHS.tsv:14537` resolves the filename and
`curation/seed_scope.tsv:322317` supports its inclusion.

All ten ancestor IDs, labels and ranks match the pinned source:

`1 root / NO_RANK; 131567 cellular organisms / CELLULAR_ROOT; 2 Bacteria / DOMAIN; 3379134 Pseudomonadati / KINGDOM; 1224 Pseudomonadota / PHYLUM; 1236 Gammaproteobacteria / CLASS; 135623 Vibrionales / ORDER; 641 Vibrionaceae / FAMILY; 657 Photobacterium / GENUS; 2628852 unclassified Photobacterium / NO_RANK`.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035384&retmode=xml)
and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035384)
were read in full. They retain the same exact label, species rank,
parent and ancestor IDs; XML confirms code 11, and Datasets
explicitly includes root. No alternative name or type material is
provided by the XML.

The strain-like designation does not override NCBI's SPECIES rank.
EXACT identifies this precise unresolved taxonomic concept; it does
not assert a formally named species. Preserve sanmaInt_01 in full
and do not merge it with another sanmaInt or sanmaSkn designation.

## Evidence

The source attestation's ID, label, count 1, NAME unit and
2026-09-13 snapshot agree with the pinned backbone. The seed event
agrees with the scope reason and NCBITAXON source list.
The manifest timestamp fields were read: raw
2026-09-13T17:50:44Z, ATB 2026-09-13T17:54:04Z and
StrainInfo 2026-09-13T17:29:00Z.
`src/taxonmech/seed.py::_seed_timestamp` was inspected and
selects their maximum, matching the seed event. This is not
human review provenance.

The exact non-expanded NCBI nuccore search returned one record:
[JF792704.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792704.1),
a 1251-base partial 16S rRNA gene. Its complete metadata,
references and feature table explicitly identify sanmaInt_01
and taxon 1035384. The source annotation names Cololabis saira
as host and Auckland Fish Market, North Island, New Zealand,
as locality. It supplies no assembly, BioSample, BioProject
or registered culture deposit.

The research reference is marked Unpublished and lists Wollenberg,
Rainey and Ruby, under the title *Experimental and taxonomic study
of in vitro bioluminescence variation in natural Vibrionaceae
isolates from New Zealand*. Wollenberg and Ruby submitted the
entry on 7 April 2011 from the University of Wisconsin.
No DOI or PMID is supplied. The research title alone does not
establish an experimental bioluminescence phenotype for this isolate.

Exact-label, designation, marker-accession, title and author/topic
web searches yielded no inspected publication explicitly linked to
this marker or isolate. Taxonomy listings, unrelated matches and
an investigator biography were leads only. This is not a claim
that no publication exists.

The exact non-expanded Assembly search returned zero with a
phrase-not-found warning. The
[NCBI Datasets genome endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035384/dataset_report)
returned an empty object. These results are bounded to this taxon
and review date, not every possible alternative classification.

Before open web research, the structured iModulonDB dataset adapter
was attempted. Its initial sandboxed request failed DNS resolution;
the authorized read-only retry succeeded:
`uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`.
All 28 returned rows were inspected. No dataset matches this
Photobacterium target. Vibrio datasets cannot be transferred by
family membership. The adapter is not applicable; noncoverage
is not negative biological evidence.

## Completeness

A completed `rg --no-ignore --hidden -n -z -i` search used
`\b1035384\b|Photobacterium sp\. sanmaInt_01\b|photobacterium_sp_sanmaint_01\b|\bsanmaInt[-_ ]?01\b`
across `data/raw`, `data/catalog`, `data/bacdive`,
`data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and
`history`. Ignored, hidden and compressed files were included.
All three matches were read in full: backbone, scientific name
and scope. Five SOURCE.json files were separately parsed and
history filenames checked independently of gitignore, without
additional target matches.

A subsequent completed whole-accession search for JF792704 across
the same ten roots returned zero matches. Its separate SOURCE.json
and history-filename checks also found none. These are bounded
local findings, not exhaustive claims about public archives.

Exact-taxonomy scans found no BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventory row. With no descendants,
zero BacDive strains is supported. This count does not deny the
isolate represented by the nucleotide submission.

No supported culture-deposit or assembly chain was found in the
inspected sources. Optional nomenclature, literature, definition and
graph fields can remain empty. The partial 16S record is an
optional enrichment lead, not a missing required genome link.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, attestation and seed provenance
agree with the inspected evidence. The YAML does not promote
marker metadata or a research title into a genome or phenotype claim.

## Recommended Edits

None required. Do not hand-edit the generated YAML.

Future authorized marker enrichment belongs in a maintained seeder
mechanism with tests, or a deliberately designed curator overlay
that survives regeneration; no existing overlay path is assumed.
Represent JF792704.1 as a nucleotide related record if later
supported by that model, never as an assembly or genome identifier.

## Follow-up Checks

- Retain the full sanmaInt_01 designation and unresolved species
  assignment unless an authority supports a change.
- Before adding a culture or genome link, verify the complete
  own-deposit and source-native identity chain. Shared genus,
  host, locality or research reference is insufficient.
- Require inspected isolate-specific experiments before phenotype
  enrichment in a sibling repository; the marker and unpublished
  research title do not supply such evidence.
- After an authorized maintained-input change, use source refresh,
  seed dry run/canary and actual-file inspection, rerun both target
  validators, then the actual `just verify-corpus` and `just qc`
  corpus gates. No curation was performed here.

## Additional Notes

The reviewed taxon is sanmaInt_01, not the neighboring sanmaInt_03,
other numbered sanmaInt isolates, sanmaSkn entries or squid isolates.
The source's capitalization and leading zero are preserved.

No paid research, genome FASTA download, external contact, GitHub
mutation, history append or lifecycle promotion occurred.
Eukaryota records and their completed reviews were not changed.
