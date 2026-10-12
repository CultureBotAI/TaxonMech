# YAML Record Review: Lysinibacillus sp. KMSDS4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lysinibacillus_sp_kmsds4.yaml`
- Started UTC: 2026-10-04T20:34:10Z
- Finished UTC: 2026-10-04T20:35:42Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1033902`,
Lysinibacillus sp. KMSDS4: SPECIES, BACTERIA, parent `NCBITaxon:2636778`,
ten root-first ancestors, genetic code 11, EXACT grounding and SEEDED
status. It has zero inventoried BacDive strains, one NCBITAXON NAME
attestation and one seed event. No record, input, code, status or
history entry was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/lysinibacillus_sp_kmsds4.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/lysinibacillus_sp_kmsds4.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded source comparisons passed for identity, every ancestor label
  and rank, direct inventories, filename lock, scope and seed text.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` controls
  diagnostic output, not verification scope. The bounded comparisons
  do not establish byte-level reproduction. Full QC, rendering and
  tests were not run.
- Not applicable: `just validate-products`, because no curator graph nodes
  are asserted. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline seed event was checked.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221336`, full native name object
`data/catalog/ncbi_names-0005.jsonl.gz:30676`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033902&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033902)
agree on ID, label, rank, bacterial domain, parent and code 11.
All ten ancestor IDs agree, including root; live expanded labels and
ranks agree where supplied. The direct parent is unclassified
Lysinibacillus beneath Lysinibacillus, Bacillaceae, Caryophanales,
Bacilli, Bacillota and Bacillati.

SPECIES is NCBI's operational placeholder rank, not a nomenclatural
validity claim. KMSDS4 is a laboratory designation, not a culture
accession. The native name object and backbone provide no synonyms.
Complete exact-ID type-material, merged-ID and dropped-taxon scans
returned no rows, and live taxonomy supplies no successor or synonym
requiring a change. Taxonomy Browser HTML was inaccessible, but the
two direct NCBI APIs succeeded.

## Evidence

The sole attestation matches the exact NCBI ID and label, one NAME
assertion and snapshot `2026-09-13`. Complete directly mapped BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits scans returned no
target rows. A complete backbone scan found no children, so zero is
also the complete descendant-inclusive BacDive count.

The exact-taxonomy nuccore query returned two entries. Both entries'
metadata, references and feature qualifiers were inspected:

- [JF768718.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768718.1&rettype=gb&retmode=xml)
  is a 1,463-base partial 16S rRNA sequence explicitly assigned to
  KMSDS4 and taxon 1033902, from a uranium-rich site at Domiasiat, India.
- [JN034436.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JN034436.1&rettype=gb&retmode=xml)
  is a 699-base partial CDS for the same taxon/strain, annotated as a
  heavy-metal-transporting P-type ATPase. It has a cadA-type similarity
  note, translation table 11 and protein accession AEI91706.1. Its
  references are an unpublished study title and direct submission,
  without a linked published PMID.

Neither sequence supplies a registered deposit or assembly. A partial
CDS and similarity annotation do not prove a complete transporter,
substrate specificity or causal resistance mechanism. No gene or
phenotype claim was added to the YAML.

The marker cites [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`, whose metadata and article body were
inspected earlier in the ongoing session. A fresh
[Table 2 XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
checked headers, footnotes, the KMSDS4/JF768718 row and merged cells:
1,463 bases and closest match Lysinibacillus xylanilyticus at greater
than 99.6% similarity. This is marker context, not a formal taxonomic
merger or deposit. Supplementary PDF content was not inspected.

Exact-taxonomy Assembly search returned zero with a `phrasesnotfound`
warning for `txid1033902[Organism:noexp]`. This is not proof of global
genome absence under every classification.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. ID, label, slug and designation
searches included digit-4/Roman-IV near matches without equating them.
All four matching lines were inspected: target backbone, scope and
scientific name, plus unrelated Streptococcus pneumoniae sample
SAMEA1033902. The target native name object was read in full. A separate
ignored-inclusive JF768718/JN034436/AEI91706 search over the same roots
completed with zero matches.

No eligible deposit or strain-genome assertion was found in this scope.
Zero BacDive entries does not deny the isolate's existence. Neither a
partial marker nor a partial CDS is a missing genome identifier. Empty
optional nomenclature, mapping, definition, record-level evidence and
causal-graph fields are appropriate for this source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected evidence scope. Identity, lineage,
attestation, strain count, status and inline provenance are supported.
Partial sequence evidence is not inflated into genome or mechanism claims.

## Recommended Edits

None. Preserve generated YAML and SEEDED status. Future supported
corrections belong in the maintained inventory pipeline and, as
appropriate, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`;
scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

On source refresh, recheck KMSDS4, its exact taxon and both nucleotide
accessions for explicit deposits or primary genomes. Keep sequence
types and isolate scope intact. After authorized changes, rerun focused
validators and the full `just verify-corpus` gate after regeneration.
No unresolved blocker prevents this verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13792` locks the slug.
`curation/seed_scope.tsv:321665` supplies the September 13, 2026 addition
and one-source reason. The event at `2026-09-13T17:54:04Z` reproduces
the NCBITAXON source list and scope reason. Ignored-inclusive filename
searches in reports/history/curation found no earlier target report or
target-specific history artifact before this report was created.

iModulonDB is not applicable to the asserted taxonomic claims; the
incidental partial CDS was inspected as context, not added as a gene
or expression-module claim. No paid research, outside contact, GitHub
mutation, generator run, status promotion or history event occurred.
