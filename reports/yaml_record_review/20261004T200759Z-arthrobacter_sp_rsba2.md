# YAML Record Review: Arthrobacter sp. RSBA2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_rsba2.yaml`
- Started UTC: 2026-10-04T20:06:51Z
- Finished UTC: 2026-10-04T20:07:59Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1033893`,
Arthrobacter sp. RSBA2: SPECIES, BACTERIA, parent `NCBITaxon:235627`,
`grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code 11.
It contains ten root-first ancestors, zero inventoried BacDive strains,
one NCBITAXON name attestation and one seed event. It makes no deposit,
genome, external equivalence or mechanism claim. This target is distinct
from RSBA1 and other study isolates.

No generated record, input, code, status or curation history was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/arthrobacter_sp_rsba2.yaml`.
  Output: `No issues found`.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/arthrobacter_sp_rsba2.yaml`.
  One file scanned, zero files with errors and zero error rows. This is
  the implementation of `just validate-strict`; it emits the standard
  `reports/instance_validation_failures.tsv` diagnostic.
- Passed bounded source comparisons of identity, all ancestor labels
  and ranks, directly mapped inventories, filename lock, scope and seed
  wording. A complete backbone scan found no child taxa.
- Not run: `just verify-corpus`. It is a full-corpus byte-comparison
  gate; `--max-diffs` limits diagnostics only. Bounded comparisons are
  not a focused substitute.
- Not applicable: `just validate-products`, because there are no
  curator-added graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline event was inspected.
  Full-corpus QC, provenance, rendering and test-suite gates were not run.

## Identity and Grounding

The complete backbone row `data/raw/ncbitaxon_taxa.tsv:221327`, native
name object `data/catalog/ncbi_names-0005.jsonl.gz:30667` and live
[NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033893&retmode=xml)
agree on identifier, label, species rank, bacterial domain, parent and
code 11. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033893)
confirms all ten lineage IDs, including root 1. The expanded live lineage
matches the pinned backbone's labels and ranks where supplied.

The direct parent is unclassified Arthrobacter beneath Arthrobacter,
Micrococcaceae, Micrococcales, Actinomycetes, Actinomycetota and Bacillati.
SPECIES is NCBI's rank for the placeholder concept, not an assertion of
formal nomenclatural validity. RSBA2 is a laboratory designation, not a
registered culture accession inferred by this record.

The native name object contains only the scientific name and all
backbone synonym fields are empty. Complete exact-ID scans of
type-material, merged-ID and dropped-taxon tables found no matching
rows; the live response supplies no successor or synonym.

## Evidence

The source attestation exactly reproduces one NAME assertion, the NCBI
identifier and label, and snapshot `2026-09-13`. Complete directly
mapped BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits
inventory scans returned no target rows. There is no descendant pool
to add to the zero BacDive strain count.

The exact-taxonomy nuccore query returned two entries. Both entries'
metadata, references and feature qualifiers were read, not inferred from
search titles:

- [JF768709.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768709.1&rettype=gb&retmode=xml)
  is a 1,436-base partial 16S rRNA sequence explicitly assigned to
  taxon 1033893 and strain RSBA2.
- [JN634869.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JN634869.1&rettype=gb&retmode=xml)
  is a 702-base partial CDS from the same taxon/strain. Its product is
  annotated as a putative heavy-metal-transporting P-type ATPase and
  uses translation table 11. Its references comprise an unpublished
  study title and direct submission, not a linked published PMID.

Both sources describe a uranium-rich site at Domiasiat, India. Neither
provides a registered culture deposit or genome assembly. A putative
partial-CDS annotation is not proof of a complete transporter, substrate
specificity or a causal uranium-resistance mechanism. No such claim was
added to the taxon record.

The marker links [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`, whose metadata and article body were
inspected earlier in the ongoing review session. A fresh
[Europe PMC XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
verified Table 2's RSBA2/JF768709 row, headers and footnotes. Its closest
16S match is Arthrobacter mysorens at 99.02% similarity. This does not
constitute an NCBI merge or deposit identity. The supplementary PDF
was not inspected.

The exact-taxonomy Assembly search returned zero entries with a
`phrasesnotfound` warning for `txid1033893[Organism:noexp]`; it does
not prove global genome absence. Taxonomy Browser HTML was inaccessible
to the web tool, while direct public NCBI APIs succeeded.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. The taxon, label, slug and
RSBA2 spelling variants yielded four matching lines, all inspected.
The complete native NCBI name object was subsequently read.

Three matches were the backbone, scope and native name. AllTheBacteria
sample `SAMEA1033893` belongs to Streptococcus pneumoniae and is a
numeric collision, not taxon evidence. A separate ignored-inclusive
search for JF768709, JN634869 and its supplied protein accession
AEY70468 across the same roots completed with zero matches.

No eligible native deposit or strain-genome assertion for RSBA2 was
found within that searched scope. Zero inventoried BacDive strains does
not imply absence of an isolate. The marker and partial CDS remain
nucleotide evidence, not missing genome identifiers. Empty optional
nomenclature, mappings, definitions, record-level evidence and
causal-graph fields are appropriate to this seeded name-only record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected evidence scope. Identity, lineage,
attestation, strain count, status and inline provenance agree with the
available source assertions. Partial sequence evidence has not been
overstated as a genome or an experimentally established mechanism.

## Recommended Edits

None. Preserve the generated record. Future source-backed identity or
strain-link corrections belong in the maintained inventory pipeline and,
as needed, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`. Scope
changes belong in `curation/seed_scope.tsv`. Literature similarity alone
does not justify changing the NCBI identity.

## Follow-up Checks

On a source refresh, recheck the exact taxon, RSBA2 and both nucleotide
accessions for explicit deposit or primary genome evidence. Preserve
partial gene and marker types and the source's putative qualifier.
Rerun focused validators after an authorized change and the full
`just verify-corpus` gate after regeneration. There is no unresolved
blocker to the present verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13783` locks the slug.
`curation/seed_scope.tsv:321657` supplies the September 13, 2026 scope
addition and one-source reason. The event at `2026-09-13T17:54:04Z`
exactly reproduces that reason and the NCBITAXON source list. This
review does not promote SEEDED to REVIEWED or append an event.

Ignored-inclusive report/history/curation filename searches found no
earlier target report or target-specific history artifact before this
report was created. iModulonDB is not applicable to the record's
taxonomic assertions: the incidental partial CDS was inspected as
sequence context, not added as a gene, regulator or expression-module
claim. No paid research, outside contact, GitHub mutation or generator
run occurred.
