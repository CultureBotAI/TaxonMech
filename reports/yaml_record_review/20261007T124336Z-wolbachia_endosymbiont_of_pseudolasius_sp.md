# YAML Record Review: Wolbachia endosymbiont of Pseudolasius sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_pseudolasius_sp.yaml`
- Started UTC: 2026-10-07T12:41:30Z
- Finished UTC: 2026-10-07T12:43:36Z
- Verdict: pass

## Target

Complete generated `TaxonRecord` for `NCBITaxon:1035897`,
Wolbachia endosymbiont of Pseudolasius sp., read in full before judging.
It has SPECIES rank, BACTERIA domain, eleven lineage entries,
EXACT grounding, SEEDED status, one exact synonym, genetic code 11,
strain count zero, one NCBI NAME attestation and one inline seed event.
It carries no strain deposits, genomes, nomenclature, alternate mappings,
literature assertions, phenotypes or causal graph.

This is a bacterial taxonomy node, not the named insect host.
Source inventories and `src/taxonmech/seed.py` own generated values;
`curation/seed_scope.tsv` owns inclusion scope. The generated YAML
is read-only for this review.

## Validation

- `just validate data/taxa/bacteria/wolbachia_endosymbiont_of_pseudolasius_sp.yaml`:
  passed with no LinkML issues.
- `just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_pseudolasius_sp.yaml --out /private/tmp/wol-pseudolasius-strict.tsv`:
  passed; one file, zero errors. The complete output TSV is header-only.
- Complete target/backbone, lineage, inventory, path-index, scope and
  inline-history comparisons passed.
- Live NCBI EFetch and Datasets checks agreed with the record.
- `just validate-products`: not applicable; no curator-added graph nodes.
- Standalone history validation: not applicable; ignored-inclusive history
  content and filename checks found no matching separate history record.
  Inline history was checked without adding a review event.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`,
  `just validate-all`, `just provenance-check`, `just render-check`,
  `just docs-check` and `just vendored-check`.
  Focused checks do not certify corpus reproduction or generated pages.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222196`
supports the identifier, scientific name, species rank, parent and genetic
code. Native names at `data/catalog/ncbi_names-0005.jsonl.gz:31691`
and line 31692 explicitly classify the full name as scientific name and
Wolbachia endosymbiont of Pseudolasius as synonym. The latter is retained
in the exact-synonym column, not an includes-name misfiled as exact.

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035897&retmode=xml)
confirms the active name, explicit synonym, species rank, bacterial
division, genetic code 11 and parent `NCBITaxon:2640676`,
unclassified Wolbachia.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035897)
agrees on all eleven ancestor identifiers, including root.
Every ancestor label and rank agrees with the pinned backbone and live
lineage, including Wolbachieae at TRIBE rank.

No target child, merged-ID, dropped-record or type-material rows were
found in the checked inventories. Species rank satisfies repository
scope without implying a formally named bacterial species or a deposited
type strain. Host wording is retained verbatim without inferring a host
species identifier or host-specific phenotype.

## Evidence

The NCBI attestation correctly identifies the target and counts one NAME
from the 2026-09-13 snapshot. Full exact-target checks of BacDive, LPSN,
GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target
rows. With no BacDive record in the target subtree, `strain_count: 0`
is the correct upstream-record count, not a claim that no infected
specimen or bacterial lineage exists.

Path-index row 14695 and scope row 322456 agree with the identifier,
slug and inclusion reason. The inline seed event correctly names NCBITAXON
and the scope reason. Its 2026-09-13T17:54:04Z timestamp is the latest
of the raw, ATB and StrainInfo extraction timestamps, as specified by
the inspected `_seed_timestamp()` implementation.

Exact `txid1035897[Organism:noexp]` queries returned zero Assembly
records and one Nuccore record. Assembly also reported the organism
phrase as not found. This is a bounded index result, not proof of
genome absence from every source.

[Complete GenBank metadata for JF902273.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=334191928)
identify a 657-base partial COI coding sequence, protein AEG67031.1,
explicitly assigned to taxon 1035897. All metadata, features and references
were read, excluding nucleotide and translation payloads.
The source names host Pseudolasius sp., voucher
`BIOUG<CAN>:ASPNA176-08.w` and BOLD ASEND068-09.COI-5P.
It reports Baitabag village, Madang, Papua New Guinea, coordinates
5.133 S 145.783 E, collection date 21-Oct-2004, collectors Janda and
NGBRC, and Alex Smith as identifier.

These are specimen/sequence annotations, not an eligible microbial culture
deposit or genome assembly. The source does not establish a clonal isolate,
culture availability, a bacterial phenotype, infection prevalence or a
mechanism for the entire taxon. The YAML makes none of those claims.

The accession cites Smith's barcoding work as Unpublished and records a
direct submission dated 01-May-2011. The inspected methods of
[Smith et al., Wolbachia and DNA Barcoding Insects: Patterns, Potential, and Problems](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514)
describe bacterial COI recovery from insect extracts and the ".w"
specimen-label convention. This supports identifier-type interpretation
only, not a taxon-specific effect. The exact accession-to-paper link
in supplementary Table S2 was not independently verified; its XLS was
not parsed. BOLD was not independently checked. GenBank remains the
inspected authority for the accession metadata.

No literature or transcriptomic assertion is present in the YAML.
iModulonDB is not applicable to this bare taxonomic record; an optional
external marker lead does not create a required gene-function assertion.

## Completeness

Complete enough for the current minimal seeded representation.
The exact synonym is retained, and empty optional strain, genome,
nomenclature, mapping, phenotype and graph slots are not defects.

Ignored and hidden files, including compressed text, were searched with
`rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`.
Queries covered the bounded taxon ID, label, synonym-bearing name pattern,
slug and Wolbachia/Pseudolasius near names, then JF902273, AEG67031,
ASPNA176-08 and ASEND068-09.

All four matching source rows were read in full: scope, backbone and
two native name rows. The expanded accession/voucher search returned
the same addresses. Five native `SOURCE.json` files were fully parsed
separately; history filenames were independently checked. Neither
supplied additional matches.

No additional target source evidence, culture-deposit link or standalone
history was found in those bounded roots and metadata files.
This does not cover every external database or arbitrary binary artifact.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Current authority and pinned sources support every material
assertion. Optional marker and publication leads do not invalidate the
minimal source-seeded representation.

## Recommended Edits

None required. Do not hand-edit the generated YAML, replace the BacDive
count with a sequence count or promote SEEDED status.

Any future taxonomy correction belongs at the authoritative upstream
source, followed by maintained extraction and seeding. Optional sequence
enrichment requires an authorized maintained input and preservation of
marker, specimen, taxon and culture-deposit identity. Broader host or
functional claims require their own narrowly scoped primary evidence.

## Follow-up Checks

Before optional enrichment, recheck the accession assignment and any
exact publication, specimen and culture-deposit links. Do not treat a
specimen voucher or partial COI sequence as a strain-genome join key.

After authorized maintained-input changes, use the documented seed dry-run
and canary workflow, both focused validators, relevant tests and full
corpus-reproduction/QC gates. No regeneration was performed here.

## Additional Notes

Reviewed on `codex/record-review-extensimonas-20261003` at
`b6a6508faca1388b88feb5740b1095e9f64cfdb8`.
The target YAML is byte-for-byte unchanged. Only this new report was
written for this record. Source inventories, scope, statuses, history,
generated pages, existing worktrees and GitHub were not modified.

