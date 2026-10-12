# YAML Record Review: Paracoccus sp. PW-P2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paracoccus_sp_pw_p2.yaml`
- Started UTC: 2026-10-04T19:51:40Z
- Finished UTC: 2026-10-04T19:53:16Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1033871`,
Paracoccus sp. PW-P2: SPECIES, BACTERIA, parent `NCBITaxon:2688777`,
`grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code 11.
It has ten root-first lineage entries, zero inventoried BacDive strains,
one NCBITAXON name attestation and one seed event. It does not assert
LPSN nomenclature, GTDB mappings, synonyms, genome links or mechanisms.

The review concerns only this record. No generated record, source input,
code, lifecycle status or curation-history entry was changed.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/paracoccus_sp_pw_p2.yaml`.
  Output: `No issues found`.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/paracoccus_sp_pw_p2.yaml`.
  One file scanned, zero files with errors and zero error rows. This is
  the implementation of `just validate-strict` and produces its standard
  `reports/instance_validation_failures.tsv` diagnostic.
- Passed read-only structured comparisons of identity, all ancestor
  labels/ranks, source inventories, scope, filename lock and seed wording.
  A complete backbone scan found no direct children, so there is no
  omitted descendant subtree from which to gather BacDive strains.
- Not run: `just verify-corpus`. Its inspected implementation compares
  the entire corpus; `--max-diffs` only caps diagnostic output. The
  bounded source checks above are not a focused reproduction gate.
- Not applicable: `just validate-products`, because the record contains
  no curator-added graph nodes. NCBI identifiers were verified at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline seed event was checked.
  Full-corpus QC, provenance, rendering and test-suite gates were not run.

## Identity and Grounding

The complete backbone row `data/raw/ncbitaxon_taxa.tsv:221321`, native
name object `data/catalog/ncbi_names-0005.jsonl.gz:30661` and inspected
[NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033871&retmode=xml)
agree on the current identifier, scientific name, species rank, parent
and bacterial genetic code. The
[Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033871)
also confirms the full lineage ID list, including root 1.

The direct parent is the unranked unclassified-Paracoccus node, beneath
genus Paracoccus; Paracoccaceae, Rhodobacterales and Alphaproteobacteria
agree with both the pinned chain and the live response. The SPECIES rank
is NCBI's operational rank for this placeholder name, not a claim of a
validly published binomial. The PW-P2 laboratory designation does not
justify changing the rank to STRAIN or inventing a culture-collection ID.

Complete exact-ID scans of type-material, merged-ID and dropped-taxon
tables found no matching rows. The live response does not indicate a
replacement or synonym; the empty synonym list agrees with the native
name object and all three backbone synonym fields.

## Evidence

The sole attestation faithfully carries the source identifier and label,
one NAME assertion and the pinned taxonomy snapshot `2026-09-13`.
The complete directly mapped BacDive, LPSN, GTDB, GOLD, MediaDive, Madin
and BactoTraits inventory scans returned no target rows. With no child
taxa, `strain_count: 0` correctly counts the inventoried BacDive records;
it is not a statement that PW-P2 is not a biological isolate.

The exact-taxonomy NCBI nucleotide search returned one entry. Its complete
sequence metadata, references and feature qualifiers were inspected
through the [NCBI sequence response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF772176.1&rettype=gb&retmode=xml):
`JF772176.1` is a 1,385-base partial 16S rRNA sequence, explicitly
classified as taxon 1033871 and strain PW-P2. Its source qualifier
records piggery wastewater, and the reference is a 2011 direct
submission, not a linked peer-reviewed species description.

That sequence supports the bounded isolate/taxon context. It does not
establish a genome assembly, a validly published name, a type strain,
a registered deposit or a physiological mechanism. No such claims were
added. The record cites no DOI or PMID requiring literature validation.

The exact-taxonomy Assembly query returned zero entries and a
`phrasesnotfound` warning for `txid1033871[Organism:noexp]`. This is a
bounded database-query result, not proof that no genome exists anywhere
or under a different classification. The web tool could not open the
Taxonomy Browser or nucleotide HTML pages; direct public NCBI APIs
successfully supplied the primary evidence described above.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i` over
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifest files. The taxon, name, slug and
PW-P2 spelling variants produced six matching lines, all inspected.

The relevant matches were the backbone, scope and native name object.
The other three were an unrelated SAR86 genome length in GenBank and
GTDB and the Streptococcus pneumoniae BioSample `SAMEA1033871` in
AllTheBacteria. These numeric collisions do not supply identity evidence.
A follow-up search for `JF772176` across the same ignored-inclusive roots
completed with zero matches.

No matching native deposit or strain-genome assertion was found within
that searched scope. No eligible BacDive strain exists here to receive
a source-backed related-sequence association. The newly inspected marker
is therefore evidence context, not a required missing genome link.
Empty optional nomenclature, mappings, definition, record-level evidence
and causal-graph sections are appropriate for this seeded record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and evidence scope. Identity,
lineage, source attestation, zero inventoried strain count, lifecycle
status and inline provenance are supported. Sparse representation alone
is not a defect.

## Recommended Edits

None. Preserve the generated record. Any future supported identity or
source-link change belongs in the maintained source inventory pipeline
and, when needed, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`,
not a manual YAML edit. A scope change belongs in
`curation/seed_scope.tsv`; no such change is justified here.

## Follow-up Checks

On a source refresh, recheck the exact taxon and PW-P2 designation for
explicit deposit evidence. Keep `JF772176.1` a nucleotide marker, not a
genome identifier, and require source-backed strain identity for any
future association. Rerun focused validators after an authorized change
and the full `just verify-corpus` gate after regeneration. No unresolved
blocker prevents the present verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13777` locks the current slug.
`curation/seed_scope.tsv:321651` records the September 13, 2026 scope
addition and one-source reason. The seed event at
`2026-09-13T17:54:04Z` reproduces that reason and the NCBITAXON source
list exactly. This read-only review does not promote SEEDED to REVIEWED
or add a curation event.

Ignored-inclusive report/history/curation filename searches found no
earlier target report or target-specific history artifact before this
report was created. iModulonDB is not applicable to a record with no
gene, regulator or expression-module claim. No paid research, outside
contact, GitHub mutation or generator run occurred.
