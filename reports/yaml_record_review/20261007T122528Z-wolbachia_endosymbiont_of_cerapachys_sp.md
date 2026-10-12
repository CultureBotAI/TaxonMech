# YAML Record Review: Wolbachia endosymbiont of Cerapachys sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_cerapachys_sp.yaml`
- Started UTC: 2026-10-07T12:20:27Z
- Finished UTC: 2026-10-07T12:25:28Z
- Verdict: pass

## Target

Complete generated `TaxonRecord` for `NCBITaxon:1035892`,
Wolbachia endosymbiont of Cerapachys sp., rank SPECIES, domain BACTERIA.
The entire YAML was read. It contains eleven lineage entries, exact
grounding, seeded status, one exact synonym, genetic code 11, strain
count zero, one NCBI name attestation and one inline seed event.
It asserts no strain deposits, genomes, phenotypes, nomenclature,
alternate mappings, literature claims or causal graph.

This is a bacterial taxonomy node, not the named insect host.
Source inventories and `src/taxonmech/seed.py` own generated fields;
`curation/seed_scope.tsv` owns inclusion scope. This review does not
authorize hand-editing the generated YAML.

## Validation

- `just validate data/taxa/bacteria/wolbachia_endosymbiont_of_cerapachys_sp.yaml`:
  passed with no LinkML issues.
- `just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_cerapachys_sp.yaml --out /private/tmp/wol-cerapachys-strict.tsv`:
  passed; one file, zero errors. The complete output is header-only.
- Full target/backbone, lineage, inventory, path-index, scope and
  inline-history comparisons passed.
- Live NCBI Taxonomy EFetch and Datasets checks agreed with the record.
- `just validate-products`: not applicable; no curator-added graph nodes.
- Standalone history validation: not applicable; ignored-inclusive
  history content and filename searches found no matching history record.
  The inline seed event was checked without adding a review event.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`,
  `just validate-all`, `just provenance-check`, `just render-check`,
  `just docs-check` and `just vendored-check`.
  Focused checks do not certify corpus reproduction or generated pages.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222192`
and native name rows at `data/catalog/ncbi_names-0005.jsonl.gz:31685`
and line 31686 support the identifier, scientific name and synonym.
The synonym Wolbachia endosymbiont of Cerapachys undet is recorded in
the exact-synonym column and as NCBI synonym, not an includes-name.

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035892&retmode=xml)
confirms the active name, explicit synonym, species rank, bacterial
division, parent `NCBITaxon:2640676` (unclassified Wolbachia) and
genetic code 11.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035892)
agrees on all eleven ancestor identifiers, including root. Labels and
ranks match the pinned backbone and live lineage, including Wolbachieae
at TRIBE rank. No target child, merged-ID, dropped-record or type-material
rows were found locally.

The NCBI species rank satisfies repository scope; it does not imply a
formally named species or a deposited type strain. Host wording is
preserved without inferring a host species identifier or phenotype.

Complete native name, backbone and scope rows were also read for 38
similarly named nodes: taxon IDs 1079408-1079419, 1094251, 1278574,
1414195-1414207, 1418215-1418217 and 1418496-1418503.
They are separately identified sibling nodes under the same parent,
not descendants of this target. Their voucher includes-names and
differences such as presence of "sp." are not evidence for merging them.
This is database identity disambiguation, not proof of distinct
biological species.

## Evidence

The sole attestation correctly counts one NCBI NAME for the exact target
from the 2026-09-13 snapshot. Full exact-target checks of the BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories found
no target rows. With no BacDive record in the target subtree,
`strain_count: 0` is a source-record count, not a claim that no infection,
specimen or bacterial lineage exists.

Path-index row 14691 and scope row 322452 agree with the identifier,
slug and inclusion reason. The inline seed event has the correct
NCBITAXON attribution and scope wording. Its 2026-09-13T17:54:04Z
timestamp is the latest of the raw, ATB and StrainInfo manifest
extraction timestamps, as specified by the seeder.

Exact `txid1035892[Organism:noexp]` searches returned zero Assembly
records and 21 Nuccore records, with all 21 UIDs retrieved.
Assembly also reported the organism phrase as not found; this is a
bounded index result, not proof that no sequence exists elsewhere.

All 21 GenBank records were inspected in full metadata form: every
reference and feature qualifier was read, excluding nucleotide and
translation payloads. All explicitly name taxon 1035892 and host
Cerapachys sp. Their partial coding sequences are not genome assemblies:

- [KF606015.1 through KF606024.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=557638562,557638560,557638558,557638556,557638554,557638552,557638550,557638548,557638546,557638544):
  ten partial hcpA sequences annotated as DUF28 protein, nine 444 bases
  and one 279 bases, with proteins AHA13748.1 through AHA13757.1.
- [KF490332.1 through KF490341.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=564283538,564283536,564283534,564283532,564283530,564283528,564283526,564283524,564283522,564283520):
  ten partial COI sequences, eight 402 bases, one 369 bases and one
  383 bases, with proteins AHB82693.1 through AHB82702.1.
- [JF902255.1 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=334191892):
  a 657-base partial COI sequence, protein AEG67013.1, voucher
  `BIOUG<CAN>:ASAZ037-06.w`, BOLD `ASEND051-09.COI-5P`.
  The source records a Zambian host specimen collected on 02-Dec-2005.

The first two groups share ten voucher strings: ASANE701-10.w,
ASANE714-10.w, ASANE715-10.w, ASANE723-10.w, ASANE724-10.w and
ASANZ031-10.w through ASANZ035-10.w. Their BOLD process identifiers
are ASFTA852-12, ASFTA857-12, ASFTA858-12, ASFTA861-12, ASFTA862-12
and ASFTA1235-12 through ASFTA1239-12, with locus-specific suffixes.
They record Malagasy host collections in 2006, 2007, 2009 and 2010.
These are specimen/sequence annotations, not microbial culture deposits.
Twenty marker accessions do not establish twenty strains, and shared
vouchers do not establish that the two loci belong to a single clonal
bacterial isolate.

The two Tsoi/Smith/Fisher submission groups cite "Patterns of Intraspecific
Variation as Influenced by Dispersal in Malagasy Ants" and "A Survey of
Wolbachia Infection in Malagasy Ants: Patterns and Protocols" as
Unpublished. Exact-title web searches did not establish a corresponding
primary publication. This is an unresolved bibliography lead, not a
claim that no publication exists.

JF902255.1 cites Smith's barcoding work as Unpublished.
The inspected methods of
[Smith et al., Wolbachia and DNA Barcoding Insects: Patterns, Potential, and Problems](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514)
describe bacterial COI fragments obtained from insect extracts and the
".w" specimen-label convention. That supports interpretation of the
identifier type, not this target's prevalence or reproductive effects.
The exact accession-to-paper linkage in Table S2 was not independently
verified; the supplementary XLS was not parsed. BOLD records were not
independently checked. GenBank remains the inspected authority for the
accession metadata above.

No functional claim is present in the YAML. Marker product annotations
do not justify adding mechanisms or gene-function assertions to it.
iModulonDB is not applicable to this bare taxonomy record; optional
external marker leads do not create a transcriptomic claim to validate.

## Completeness

Complete enough for the current minimal seeded representation. The exact
NCBI synonym is retained. Empty optional strain, genome, nomenclature,
mapping, phenotype and causal-graph slots are not defects.

Ignored and hidden files, including compressed text, were searched using
`rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`.
Queries covered the bounded taxon ID, name, synonym-bearing name pattern,
slug and similarly named entries, then every inspected accession,
protein identifier, voucher base and BOLD process identifier.

All 142 matched source rows were read in full: 39 scope rows,
39 backbone rows and 64 native name rows. The expanded accession/voucher
search returned the same addresses, with no additional source rows.
All five native `SOURCE.json` files were parsed separately; history
filenames were also checked independently. No additional target evidence,
strain-deposit link or matching standalone history was found within those
bounded roots and metadata files. This does not cover every external
database or arbitrary binary artifact.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Current taxonomy and pinned source rows support the material
assertions. Optional marker and bibliography leads are not required
fields and do not invalidate the faithful minimal record.

## Recommended Edits

None required. Do not hand-edit the generated YAML, change the BacDive
count to a sequence count, or promote SEEDED status.

Any future taxonomy correction belongs at the authoritative source,
followed by the maintained extraction and seeding workflow. Any optional
sequence enrichment requires an authorized maintained input and a
representation that preserves marker, voucher, host and taxon scope.
Neither name similarity nor a partial marker is a strain-genome join key.

## Follow-up Checks

Before optional enrichment, recheck accession assignments, specimen
identity and the exact primary-publication/supplement links. Obtain
independent culture-deposit evidence before attaching strain-genome links.

After an authorized maintained-input change, follow the documented seed
dry-run and canary workflow, both focused validators, relevant tests and
full corpus-reproduction/QC gates. No regeneration was performed here.

## Additional Notes

Reviewed on `codex/record-review-extensimonas-20261003` at
`b6a6508faca1388b88feb5740b1095e9f64cfdb8`.
The YAML is byte-for-byte unchanged. Only this new report was written
for this record. Sources, scope, history, statuses, generated pages,
existing worktrees and GitHub were not modified.

