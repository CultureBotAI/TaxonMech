# YAML Record Review: Pseudomonas sp. Horo_8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_horo_8.yaml`
- Started UTC: 2026-10-04T21:44:27Z
- Finished UTC: 2026-10-04T21:45:13Z
- Verdict: pass

## Target

Read the full generated `TaxonRecord`, `NCBITaxon:1033930`,
Pseudomonas sp. Horo_8. It asserts SPECIES, BACTERIA, parent
`NCBITaxon:196821`, ten ancestors, code 11, EXACT grounding, SEEDED
status, zero inventoried strains, one NCBITAXON NAME attestation and
one inline seed event. No record, code, input, status or history was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_horo_8.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_horo_8.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded identity, complete lineage, mapped-source, filename, scope and inline-event comparisons passed.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` caps diagnostic output, not scope. Bounded checks do not prove byte-level reproduction. Full QC, tests and rendering were not run.
- Not applicable: `just validate-products`; there are no curator graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target-specific history artifact. Inline provenance was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221364`, the full scientific-name
object `data/catalog/ncbi_names-0005.jsonl.gz:30704`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033930&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033930)
agree on exact identifier, label, rank, bacterial domain, parent and
code 11. All ten root-first lineage IDs match; expanded labels and
ranks agree where supplied. Pseudomonadati, Pseudomonadota,
Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae, Pseudomonas
and its unclassified parent are preserved.

The underscore-bearing label is correct. SPECIES is an NCBI placeholder
rank, not formal species-name validity. Backbone and native names have
no synonyms. Complete exact-ID type-material, merged-ID and dropped-taxon
scans returned no rows. Live taxonomy supplies no alias, type designation
or replacement requiring a change.

## Evidence

The sole attestation matches exact NCBI identity, label, one NAME
assertion and snapshot `2026-09-13`. Complete directly mapped BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits scans returned no
target rows. A complete backbone scan found no children, supporting
zero descendant-inclusive BacDive strains.

Exact-taxonomy nuccore search returned one entry. Complete metadata,
references and feature qualifiers were read:
[AB627870.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB627870.1&rettype=gb&retmode=xml),
a 629-base partial 16S rRNA sequence explicitly assigned to Horo_8 and
taxon 1033930. Source qualifiers specify groundwater in Horonobe,
Hokkaido, Japan. The references list Sakurai and Yoshikawa, an unpublished
biofilm study and an April 30, 2011 direct submission. No registered
culture deposit, BioSample or assembly identifier is supplied.
A partial marker is not a genome; Horo_8 is a laboratory designation.

Exact-taxonomy Assembly search returned zero with a `phrasesnotfound`
warning for `txid1033930[Organism:noexp]`. This is not proof of genome
absence under every possible classification.

The [JAEA publication metadata](https://jopss.jaea.go.jp/search/servlet/search?5030464=)
for DOI `10.1080/00223131.2012.660015` was inspected earlier this turn
during Horo_6 review. It supplies no Horo_8 row. Direct publisher
access returned 403 earlier in the ongoing session; full paper,
isolate table and figures remain unverified. No phenotype or species
reassignment was inferred from that lead or search excerpts.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`, excluding only `SOURCE.json`.
Patterns included ID, label, slug, separator alternatives and Horo-VIII.
All five matching contexts were inspected: three target identity/scope
rows and two unrelated numeric matches.
GCA_038921345.1 is a Kaistiaceae bacterium whose genome length matches
the taxon digits; SAMEA1033930 is a Streptococcus pneumoniae sample.
Neither supports a Horo_8 identity or genome join.

A separate AB627870 search over the same ignored-inclusive roots
completed with zero matches. The native name object was read in full.
No eligible strain, deposit or strain-genome assertion for Horo_8 was
found within this scope. Zero inventoried strains does not deny the
isolate's existence. Empty optional nomenclature, mappings, definition,
evidence and graph slots are appropriate for this source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, attestation,
strain inventory, status and inline provenance are supported.

## Recommended Edits

None. Preserve the generated YAML and SEEDED status. Future supported
corrections belong in maintained inputs and, as appropriate,
`src/taxonmech/extract.py` or `src/taxonmech/seed.py`; scope changes
belong in `curation/seed_scope.tsv`.

## Follow-up Checks

On refresh, recheck the exact taxon and AB627870 for explicit deposits
or primary genomes. Inspect the later paper's exact isolate row before
using it for a new claim, keeping other Horo isolates separate.
After authorized changes, regenerate and run focused validators plus
full `just verify-corpus`. No unresolved blocker remains.

## Additional Notes

`data/taxa/PATHS.tsv:13820` locks the slug;
`curation/seed_scope.tsv:321692` supplies the September 13, 2026 date
and one-source reason. The event at `2026-09-13T17:54:04Z` matches
the source list and scope wording. Ignored-inclusive filename and
history-content searches found no prior target report or history artifact.

iModulonDB is not applicable: no gene, regulator, expression module or
mechanism is asserted. No paid research, outside contact, GitHub mutation,
generator run, status promotion or history event occurred.

