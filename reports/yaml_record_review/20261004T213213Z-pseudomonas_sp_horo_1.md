# YAML Record Review: Pseudomonas sp. Horo_1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_horo_1.yaml`
- Started UTC: 2026-10-04T21:30:40Z
- Finished UTC: 2026-10-04T21:32:13Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`, `NCBITaxon:1033923`,
Pseudomonas sp. Horo_1. It asserts SPECIES, BACTERIA, parent
`NCBITaxon:196821`, ten ancestors, code 11, EXACT grounding, SEEDED
status, zero inventoried BacDive strains, one NCBITAXON NAME attestation
and one inline seed event. No record, code, input, status or history was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_horo_1.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_horo_1.yaml`; one file, zero errors. This implements `just validate-strict`, producing `reports/instance_validation_failures.tsv`.
- Bounded identity, complete lineage, mapped-source, scope, filename and inline-event comparisons passed.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` caps diagnostics, not scope. Bounded comparisons are not byte-level reproduction. Full QC, rendering and tests were not run.
- Not applicable: `just validate-products`, as no curator graph nodes are asserted. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target-specific history artifact. The inline event was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221357`, full native scientific-name
object `data/catalog/ncbi_names-0005.jsonl.gz:30697`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033923&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033923)
agree on the exact identifier, underscore-bearing label, rank, domain,
parent and code 11. All ten lineage IDs match, including root; expanded
labels and ranks agree where supplied. The chain includes Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae,
Pseudomonas and unclassified Pseudomonas.

SPECIES is the NCBI placeholder rank, not evidence of formal nomenclatural
validity. Backbone and native names provide no synonyms. Complete
exact-ID type-material, merged-ID and dropped-taxon scans returned no
rows; live taxonomy supplies no replacement or synonym requiring a change.

## Evidence

The sole attestation exactly matches NCBI identity, one NAME assertion
and snapshot `2026-09-13`. Complete directly mapped BacDive, LPSN,
GTDB, GOLD, MediaDive, Madin and BactoTraits scans returned no target
rows. A complete backbone scan found no children, supporting the zero
descendant-inclusive BacDive strain count.

Exact-taxonomy nuccore search returned one entry. Its complete metadata,
references and feature qualifiers were inspected:
[AB627863.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB627863.1&rettype=gb&retmode=xml),
a 626-base partial 16S rRNA sequence explicitly assigned to Horo_1 and
taxon 1033923. Its source is groundwater in Horonobe, Hokkaido, Japan.
It lists Sakurai and Yoshikawa, an unpublished biofilm-study reference,
and direct submission on April 30, 2011. It supplies no registered
culture deposit, BioSample or assembly identifier. Horo_1 is a laboratory
designation; the marker is not a genome.

Exact-taxonomy Assembly search returned zero, with a `phrasesnotfound`
warning for `txid1033923[Organism:noexp]`. This is a bounded negative
result, not proof of genome absence under every classification.

A literature lead was pursued to the inspected
[JAEA publication record](https://jopss.jaea.go.jp/search/servlet/search?5030464=):
Sakurai and Yoshikawa, 2012, DOI `10.1080/00223131.2012.660015`,
on biofilm-forming isolates from deep groundwater. The publisher's direct
full-text URL returned 403. JAEA confirms bibliographic and cohort
context, but provides neither Horo_1's accession row nor its assay
values. Publisher search text was treated as a lead, not record-level
evidence. The isolate table, full paper and figures were not verified;
no species reassignment or phenotype was inferred from them.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`, excluding only `SOURCE.json`.
Patterns covered the taxon ID, label, slug, Horo-1/Horo_1/Horo 1 and
Roman-I variants. All 29 matching line contexts were inspected.
Twenty-seven were identity/scope/name rows for Horo_1 and eight distinct
Horo_1-prefixed isolates; these do not establish equivalence.
Two were unrelated numeric matches: genome length 1033923 for
GCA_984472015.1, an Alphaproteobacteria MAG, and SAMEA1033923,
a Streptococcus pneumoniae sample.

A separate AB627863/publication-DOI search over the same ignored-inclusive
roots completed with zero matches. The full native scientific-name
object was read. No eligible strain, deposit or strain-genome assertion
for Horo_1 was found in that scope. Zero inventoried strains does not
deny the isolate's existence. Empty optional nomenclature, mappings,
definition, evidence and causal-graph slots are appropriate for this seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, attestation,
strain inventory, status and inline provenance are supported. Unavailable
paper details are not needed to support a phenotype-free taxonomy seed.

## Recommended Edits

None. Preserve the generated YAML and SEEDED status. Future supported
source corrections belong in maintained inventory inputs and, as
appropriate, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`;
scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

On source refresh, recheck the exact taxon and AB627863 for explicit
deposits or primary genomes. Before using the later paper for a new
strain-specific claim, inspect its exact Horo_1 table row and distinguish
preliminary marker identification from formal taxonomy. After authorized
changes, regenerate and run focused validators plus full
`just verify-corpus`. No unresolved blocker remains.

## Additional Notes

`data/taxa/PATHS.tsv:13813` locks the slug;
`curation/seed_scope.tsv:321685` supplies the September 13, 2026 date
and one-source reason. The event at `2026-09-13T17:54:04Z` matches
the source list and scope wording. Ignored-inclusive filename and
history-content searches found no prior target report or target history.

iModulonDB is not applicable: the YAML asserts no gene, regulator,
expression module or mechanism. No paid research, outside contact,
GitHub mutation, generator run, status promotion or history event occurred.

