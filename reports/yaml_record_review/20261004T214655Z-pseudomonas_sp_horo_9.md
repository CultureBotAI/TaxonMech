# YAML Record Review: Pseudomonas sp. Horo_9

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_horo_9.yaml`
- Started UTC: 2026-10-04T21:46:06Z
- Finished UTC: 2026-10-04T21:46:55Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`, `NCBITaxon:1033931`,
Pseudomonas sp. Horo_9. It asserts SPECIES, BACTERIA, parent
`NCBITaxon:196821`, ten root-first ancestors, code 11, EXACT grounding,
SEEDED status, zero inventoried strains, one NCBITAXON NAME attestation
and one inline seed event. No record, code, input, status or history was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_horo_9.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_horo_9.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded identity, full lineage, mapped-source, filename, scope and inline-event comparisons passed.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` caps diagnostics, not scope. Bounded checks are not byte-level reproduction. Full QC, tests and rendering were not run.
- Not applicable: `just validate-products`; there are no curator graph nodes. NCBI identifiers were verified at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target-specific history artifact. Inline provenance was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221365`, full native
scientific-name object `data/catalog/ncbi_names-0005.jsonl.gz:30705`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033931&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033931)
agree on exact identity, label, species rank, bacterial domain, parent
and code 11. All ten lineage IDs match, including root; expanded labels
and ranks agree where supplied. The chain preserves Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae,
Pseudomonas and unclassified Pseudomonas.

The underscore-bearing label is correct. SPECIES is NCBI's placeholder
rank, not formal species-name validity. Backbone and native names
provide no synonyms. Complete exact-ID type-material, merged-ID and
dropped-taxon scans returned no rows. Live taxonomy supplies no alias,
type designation or replacement requiring a change.

## Evidence

The sole attestation matches NCBI identity, label, one NAME assertion
and snapshot `2026-09-13`. Complete directly mapped BacDive, LPSN,
GTDB, GOLD, MediaDive, Madin and BactoTraits scans found no target
rows. A complete backbone scan found no children, supporting zero
descendant-inclusive BacDive strains.

Exact-taxonomy nuccore search returned one entry. Complete metadata,
references and feature qualifiers were read:
[AB627871.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB627871.1&rettype=gb&retmode=xml),
a 629-base partial 16S rRNA sequence explicitly identifying Horo_9
and taxon 1033931. Source qualifiers give groundwater in Horonobe,
Hokkaido, Japan. Its references list Sakurai and Yoshikawa, an
unpublished biofilm study and direct submission on April 30, 2011.
No registered culture deposit, BioSample or assembly identifier is
supplied. This marker is not a genome and Horo_9 is a laboratory
designation. Equal marker lengths do not identify different Horo isolates
as the same organism.

Exact-taxonomy Assembly search returned zero with a
`phrasesnotfound` warning for `txid1033931[Organism:noexp]`.
This does not prove genome absence under every classification.

The [JAEA metadata](https://jopss.jaea.go.jp/search/servlet/search?5030464=)
for DOI `10.1080/00223131.2012.660015` was read earlier this turn
during Horo_6 review. It supplies no Horo_9 row. Direct publisher
access returned 403 earlier in the ongoing session; full paper,
isolate table and figures remain unverified. No phenotype or species
reassignment was inferred from this lead or search excerpts.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`, excluding only `SOURCE.json`.
Patterns included ID, label, slug, separator alternatives and Horo-IX.
All four matching contexts were inspected: three target identity/scope
rows and unrelated Streptococcus pneumoniae sample SAMEA1033931.
The latter is a numeric near match, not a Horo_9 genome association.

A separate AB627871 search across the same ignored-inclusive roots
completed with zero matches. The native name object was read in full.
No eligible strain, deposit or strain-genome assertion for Horo_9 was
found in this scope. Zero inventoried strains does not deny the isolate's
existence. Empty optional nomenclature, mappings, definition, evidence
and graph slots are appropriate for this source-attested seed.

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

On refresh, recheck the exact taxon and AB627871 for explicit deposits
or primary genomes. Inspect the later paper's exact isolate row before
using it for a new claim. Keep other Horo isolates separate.
After authorized changes, regenerate and run focused validators plus
full `just verify-corpus`. No unresolved blocker remains.

## Additional Notes

`data/taxa/PATHS.tsv:13821` locks the slug;
`curation/seed_scope.tsv:321693` supplies the September 13, 2026 date
and one-source reason. The event at `2026-09-13T17:54:04Z` matches
the source list and scope wording. Ignored-inclusive filename and
history-content searches found no prior target report or history artifact.

iModulonDB is not applicable: no gene, regulator, expression module or
mechanism is asserted. No paid research, outside contact, GitHub mutation,
generator run, status promotion or history event occurred.

