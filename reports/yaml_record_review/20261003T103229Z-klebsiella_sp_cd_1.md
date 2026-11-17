# YAML Record Review: Klebsiella sp. Cd-1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/klebsiella_sp_cd_1.yaml`
- Started UTC: 2026-10-03T10:30:52Z
- Finished UTC: 2026-10-03T10:32:29Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:101654`, label Klebsiella sp. Cd-1,
rank SPECIES, domain BACTERIA. The entire YAML was read before judgment.
It has ten root-first ancestors, parent `NCBITaxon:2608929` (unclassified
Klebsiella), genetic code 11, zero BacDive strains and one NCBITAXON NAME
attestation. Grounding is EXACT and mapping status remains SEEDED. The
embedded event is dated 2026-09-13T17:54:04Z.

`data/taxa/PATHS.tsv` row 9836 resolves the unique identifier/slug;
`curation/seed_scope.tsv` row 143338 records its inclusion. This earlier
coverage gap was confirmed by an ignored-inclusive report-filename search.
The pass concerns consistency and support in the pinned source snapshot;
current authority availability remains a disclosed verification limit.

## Validation

- `just validate data/taxa/bacteria/klebsiella_sp_cd_1.yaml`: PASS, no issues.
- `just validate-strict data/taxa/bacteria/klebsiella_sp_cd_1.yaml`: PASS,
  one file, zero ERROR rows, including the embedded curation event.
- Structured full-inventory CSV/YAML comparison: PASS for identifier,
  label, rank, parent, genetic code and all ancestor labels, ranks and
  parent links. A complete taxonomy scan found no direct children, so
  there is no descendant subtree whose BacDive entries were overlooked.
- `git diff --exit-code -- data/taxa/bacteria/klebsiella_sp_cd_1.yaml`:
  PASS, no change to the target.
- `just verify-corpus`: not run. Its documented interface is full-corpus
  only, with no target selector; inventory comparisons do not establish
  full byte-for-byte regeneration.
- `just validate-history`: not run. An ignored-inclusive search of
  `history/` by exact ID, label and slug found no separate target artifact.
  No history record was created by the review.
- `just validate-products`: not applicable; there is no causal graph or
  curator-added ontology node. Full QC, rendering, tests and source replay
  were not run for this read-only review.
- Live NCBI Taxonomy Browser, NCBI Datasets, NCBI EFetch and ENA taxonomy
  requests for 101654 returned access/fetch errors. These were not treated
  as evidence that the taxon is deleted, merged or invalid.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv` row 17638 agrees with every identity field.
Its exact, related and broad synonym columns and retirement target are
empty. The complete native name search finds one scientific-name row in
`data/catalog/ncbi_names-0000.jsonl.gz`, row 37527, explicitly pairing
Klebsiella sp. Cd-1 with `NCBITaxon:101654`.

The retained ancestry is root, cellular organisms, Bacteria, Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae,
Klebsiella, unclassified Klebsiella. It matches the pinned inventory without
an inferred species reassignment. SPECIES is the database rank; it does not
assert that this provisional `sp.` name is validly published under the ICNP.
The isolate-like suffix does not independently justify converting the rank
to STRAIN or assigning a formally named Klebsiella species.

EXACT grounds this record to its own NCBI concept, not to a culture deposit,
sequenced genome or species guessed from the genus. There is no LPSN or
GTDB equivalence assertion to overinterpret. No present-day authority page
was successfully inspected, so the snapshot identity is supported while
the current label/rank/retirement state is not independently revalidated.

## Evidence

- The NCBI NAME attestation has the correct target ID, label, count one,
  unit and 2026-09-13 snapshot note. It agrees with the only source listed
  in the raw taxonomy row and the scope reason. A NAME count is not a
  genome count, phenotype measurement or taxonomic publication.
- The native scientific-name row supports the exact spelling and ID. No
  additional native name row for that ID was found by the complete
  compressed-catalog search, including ignored files.
- `conf/ncbi_taxdump.yaml` pins snapshot 2026-09-13, archive path
  `data/source_snapshots/ncbi-new-taxdump-2026-09-13.tar.gz` and SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
  `src/taxonmech/ncbi_taxdump.py` carries native rank, parent, names and
  genetic code into the extraction. A checkout-wide ignored-inclusive
  filename search found the config, source, test and bytecode, but not the
  pinned archive or nodes.dmp. Raw nodes were therefore not replayed.
- The seed event correctly names NCBITAXON as its only source and does not
  claim a human review. The record has no DOI, PMID, sequence accession,
  source-linked culture, genome, causal edge or quotation requiring a
  separate claim-level literature judgment.
- Exact-name and taxon-ID web searches produced no usable direct authority
  evidence. Unrelated article-number 101654 hits and the distinct deposit
  NBRC 101654 were rejected. A broad patent-list mention was not used as a
  strain identity, genome link or phenotype source.

## Completeness

Ignored-inclusive searches covered exact ID, label and slug in all raw
inventories, scope/configuration and history surfaces. Beyond the NCBI
backbone and scope entry they found no matching source mapping, type-material
row, BacDive strain or source attestation. The complete raw taxonomy scan
found no children. Thus the zero strain count is consistent with the
available inventory, not a claim that the organism cannot be cultured.

An ignored-inclusive compressed search of every JSONL.GZ file in
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/` and
`data/straininfo/` covered the target CURIE, native taxon-ID keys, exact
species label and the exact Cd-1 string. Its only result was the native
NCBI scientific-name row. An additional ignored-inclusive search of
`data/atb/` and `data/straininfo/` TSV and compressed TSV surfaces found no
target ID, label or slug association. These are bounded searches of the
named catalogs and accepted associations, not proof that no genome or
deposit exists anywhere. Different names without an explicit identity bridge
were not joined. The full ATB TSV.XZ was not searched.

Empty synonyms, nomenclature, mappings, xrefs, genome links, definition,
record-level evidence and causal graphs are appropriate to the supported
NCBI-only representation. No taxon-specific mechanistic or transcriptomic
claim is present; iModulonDB is not applicable to this record's assertions.
Absence from that resource is not negative biological evidence.

## Findings

None found in the inspected pinned record and source evidence.

- Blocker: 0.
- Major: 0.
- Minor: 0.

Live authority revalidation and original-node replay are incomplete checks,
not demonstrated defects. They are not inflated into a record finding or
treated as proof of current external-source agreement.

## Recommended Edits

None justified by the inspected evidence. Preserve the provisional NCBI
identity and do not add a guessed named-species mapping, culture number,
genome accession, phenotype or artificial required evidence object.

If a future primary-source check establishes a changed identity, rank or
parent, its owner is the pinned NCBI source configuration and extraction in
`conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py` and
`src/taxonmech/extract.py`, with `src/taxonmech/seed.py` responsible for
projection and tests. Scope changes belong in `curation/seed_scope.tsv`.
Do not hand-edit the generated YAML or change its slug directly.

## Follow-up Checks

Retry the [NCBI Taxonomy Browser target](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=101654)
or the official NCBI taxonomy API when reachable. Confirm the exact taxon
ID, label, rank, lineage and merged/deleted status before proposing any
refresh. This link records the attempted check, not a successfully
inspected web source. Acquire and hash-verify the pinned archive only as
part of an authorized source check if independent node replay is needed.

After any authorized source change, run the source-specific tests, the seed
dry run and `just seed-canary NCBITaxon:101654`; inspect the emitted YAML,
then re-run the two focused validators. Full corpus reproduction must be
checked with `just verify-corpus` after approved regeneration. A new
strain/genome association would require its own whole-deposit or explicit
source identity evidence; a shared name or taxon is insufficient.

## Additional Notes

This is a report-only review. No generated YAML, source data, curation
status, standalone history, site file, GitHub object or Eukaryota record
was changed. The only new review artifact is this timestamped report.
The native name projection and raw taxonomy agree, but agreement between
derived surfaces was not misrepresented as a successful current web check.
