# YAML Record Review: Arthrobacter sp. RSBA1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_rsba1.yaml`
- Started UTC: 2026-10-04T20:04:43Z
- Finished UTC: 2026-10-04T20:05:50Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1033892`,
Arthrobacter sp. RSBA1: SPECIES, BACTERIA, parent `NCBITaxon:235627`,
`grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code 11.
It has ten root-first ancestors, zero inventoried BacDive strains, one
NCBITAXON name attestation and one seed event. No external equivalence,
deposit, genome or mechanism is asserted. RSBA2 and similarly named
study isolates are not this review's target.

No record, source input, code, lifecycle status or curation history was
changed. This report is the sole new review artifact for this target.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/arthrobacter_sp_rsba1.yaml`.
  Output: `No issues found`.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/arthrobacter_sp_rsba1.yaml`.
  One file scanned, zero files with errors and zero error rows. This is
  the implementation of `just validate-strict`; its standard diagnostic
  is `reports/instance_validation_failures.tsv`.
- Passed bounded source comparisons of identity, every ancestor label
  and rank, source inventories, scope, filename lock and seed wording.
  A complete backbone scan found no child taxa.
- Not run: `just verify-corpus`. It compares the entire corpus;
  `--max-diffs` limits diagnostics, not scope. Bounded comparisons here
  do not establish byte-level reproduction.
- Not applicable: `just validate-products`, because the record has no
  curator-added graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline event was checked.
  Full-corpus QC, provenance, rendering and test-suite gates were not run.

## Identity and Grounding

The complete backbone row `data/raw/ncbitaxon_taxa.tsv:221326`, native
name object `data/catalog/ncbi_names-0005.jsonl.gz:30666` and live
[NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033892&retmode=xml)
agree on identifier, label, species rank, unclassified-Arthrobacter
parent, bacterial domain and code 11. The
[Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033892)
confirms all ten lineage IDs, including root 1. Expanded live lineage
labels and ranks agree with the pinned backbone where supplied.

The genus/family/order chain is Arthrobacter, Micrococcaceae and
Micrococcales under Actinomycetes, Actinomycetota and Bacillati. This
carried NCBI hierarchy does not assert a formal species description.
The laboratory designation RSBA1 does not justify changing the source
rank to STRAIN or inventing a culture accession.

The native name object has only the scientific name and the backbone
synonym fields are empty. Complete exact-ID scans of type-material,
merged-ID and dropped-taxon tables found no matching rows; the live
response gives no replacement or synonym.

## Evidence

The sole attestation exactly reproduces the NCBI identifier and label,
one NAME assertion and snapshot `2026-09-13`. Complete directly mapped
BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventory
scans found no target rows. With no child taxa, there is no descendant
BacDive pool to add to the zero strain count.

The exact-taxonomy nuccore search returned one entry. Its metadata,
references and feature qualifiers were inspected through the
[NCBI sequence response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768708.1&rettype=gb&retmode=xml).
`JF768708.1` is a 1,428-base partial 16S rRNA sequence with explicit
taxon 1033892 and strain RSBA1 qualifiers. The source describes a
uranium-rich site at Domiasiat, India, but supplies no registered
culture deposit or assembly accession.

The sequence links [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`. Its metadata and article body were already
inspected during the ongoing review session. A fresh
[Europe PMC XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
verified Table 2's RSBA1/JF768708 row, headers and footnotes. The
row-spanning closest-match cells report Arthrobacter nicotinovorans
and similarity greater than 99.20%. This is literature identification,
not an NCBI merge or culture-deposit identity. Supplementary PDF
content was not inspected.

No phenotype or gene result is imported from that study. The seeded
record's name attestation is sufficient provenance under the local
model; adding optional literature evidence is not required for a pass.

The exact-taxonomy Assembly query returned zero entries with a
`phrasesnotfound` warning for `txid1033892[Organism:noexp]`. This is
not proof that no genome exists under any classification. Taxonomy
Browser HTML was inaccessible to the web tool; direct NCBI public APIs
successfully supplied the primary taxonomy and sequence evidence.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. The taxon, name, slug and
RSBA1 spelling variants produced four matching lines, all inspected.
The matching native name object was subsequently read in full.

Three matches were the backbone, scope and scientific name. The fourth
was unrelated Streptococcus pneumoniae BioSample `SAMEA1033892` in
AllTheBacteria, a numeric collision rather than taxon identity evidence.
A separate ignored-inclusive search for `JF768708` across the same
roots completed with zero matches.

No eligible native deposit or strain-genome assertion for RSBA1 was
found within that searched scope. Zero BacDive strains is an inventory
count, not a statement that RSBA1 is not an isolate. Its partial marker
and literature closest match do not establish a missing genome link.
Empty optional nomenclature, mappings, definitions, record-level
evidence and causal-graph sections are appropriate.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected evidence scope. Identity, lineage,
attestation, strain count, lifecycle status and inline provenance are
supported. Literature identification remains separate from NCBI identity.

## Recommended Edits

None. Preserve the generated YAML. Future supported source or identity
corrections belong in the maintained inventory pipeline and, when
needed, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`. Scope
changes belong in `curation/seed_scope.tsv`. Neither a manual patch nor
a status promotion is justified here.

## Follow-up Checks

On a source refresh, recheck the exact taxon and RSBA1/JF768708 pair
for explicit deposit or genome evidence. Keep other study isolates and
comparison cultures separate. Preserve a marker as a nucleotide
sequence, not an assembly. Rerun focused validators after an authorized
change and the full `just verify-corpus` gate after regeneration.
No unresolved blocker prevents this verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13782` locks the slug, and
`curation/seed_scope.tsv:321656` records the September 13, 2026 scope
addition with its one-source reason. The event at
`2026-09-13T17:54:04Z` exactly reproduces the NCBITAXON source list and
scope reason. This review does not promote SEEDED to REVIEWED or append
an event.

Ignored-inclusive report/history/curation filename searches found no
earlier target report or target-specific history artifact before this
report was created. iModulonDB is not applicable to this taxonomic
record; no gene or expression-module assertion was added from the paper.
No paid research, outside contact, GitHub mutation or generator run
occurred.
