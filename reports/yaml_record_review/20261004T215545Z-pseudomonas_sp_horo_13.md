# YAML Record Review: Pseudomonas sp. Horo_13

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_horo_13.yaml`
- Started UTC: 2026-10-04T21:52:31Z
- Finished UTC: 2026-10-04T21:55:45Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord`, `NCBITaxon:1033934`,
Pseudomonas sp. Horo_13. It carries SPECIES rank, BACTERIA domain,
parent `NCBITaxon:196821`, ten root-first ancestors, genetic code 11,
EXACT grounding, SEEDED status, zero inventoried strains, one NCBITAXON
NAME attestation and one inline seed event. No record or maintained
input was changed.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_horo_13.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_horo_13.yaml`; one file, zero errors. This is the implementation of `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded identity, full lineage, mapped-source, slug, scope and inline-provenance comparisons passed.
- Not run: full-corpus `just verify-corpus`; its `--max-diffs` option limits diagnostics, not corpus scope. The bounded comparisons are not proof of byte-level reproduction. Full QC, tests and rendering were not run.
- Not applicable: `just validate-products`; the record has no curator-added graph nodes. NCBI identifiers were checked at their authority.
- Not run: `just validate-history`; ignored-inclusive searches found no target-specific history artifact. The inline seed event was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221368`, the complete native
scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30708`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033934&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033934)
agree on identifier, exact label, rank, bacterial placement, parent
and code 11. All ten root-first ancestor IDs match; labels and ranks
agree where expanded by the live sources. The lineage correctly retains
Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales,
Pseudomonadaceae, Pseudomonas and unclassified Pseudomonas.

The underscore-bearing label is source-native. NCBI's SPECIES rank for
this placeholder does not imply a validly published species name.
The backbone has no synonyms, and the native name object is scientific
name only. Complete exact-ID type-material, merged-ID and dropped-taxon
scans returned no rows. Live taxonomy supplies no conflicting alias,
type designation or replacement requiring a change.

## Evidence

The sole attestation preserves the NCBI identifier and label, one NAME
assertion and snapshot `2026-09-13`. Complete directly mapped BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits scans found no target
rows. A complete backbone scan found no children. Together these support
zero descendant-inclusive BacDive strains; they do not deny the isolate.

Exact-taxonomy nuccore search returned one entry. Its full metadata,
references and feature qualifiers were inspected:
[AB627875.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB627875.1&rettype=gb&retmode=xml),
a 613-base partial 16S rRNA sequence explicitly naming strain Horo_13
and taxon 1033934. Source qualifiers specify groundwater in Horonobe,
Hokkaido, Japan. References identify Sakurai and Yoshikawa, an unpublished
biofilm study and an April 30, 2011 direct submission. No registered
culture deposit, BioSample or assembly identifier is supplied. This
marker sequence is not a genome, and Horo_13 is not itself a verified
culture-collection accession.

Exact-taxonomy Assembly search returned zero with a `phrasesnotfound`
warning for `txid1033934[Organism:noexp]`. This limited query does not
prove genome absence under all classifications.

The [JAEA later-paper metadata](https://jopss.jaea.go.jp/search/servlet/search?5030464=),
DOI `10.1080/00223131.2012.660015`, was inspected earlier in the
ongoing review session. It exposes no individual Horo_13 row. Direct
publisher access returned 403 earlier in that session; the full paper,
isolate table and figures remain unverified. No individual phenotype,
closest-match identification or species reassignment is inferred from
that lead or search excerpts.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`, excluding only `SOURCE.json`.
Patterns included identifier, label, slug, separator alternatives and
Horo-XIII. All six matching contexts were inspected: three target
identity/scope rows, two unrelated genome-length matches and one
unrelated sample-accession match.

GenBank `GCA_027619835.1` and its GTDB catalog counterpart describe
Bacteroidota bacterium, taxon 1898104, isolate casp40-mb.227; their
1033934 match is a sequence-length value, not taxonomic identity.
AllTheBacteria sample SAMEA1033934 denotes Streptococcus pneumoniae.
None supplies a Horo_13 strain-genome join.

A separate AB627875 search over the same ignored-inclusive roots
completed with zero matches. The native scientific-name object was
read in full. No eligible deposit, strain or strain-genome assertion
for Horo_13 was found within this search scope. Optional nomenclature,
mappings, definition, evidence and causal graph slots are appropriately
empty for this source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, attestation,
strain count, status and inline provenance are supported.

## Recommended Edits

None. Preserve the generated YAML and SEEDED status. Future supported
corrections belong in maintained inputs and, as appropriate,
`src/taxonmech/extract.py` or `src/taxonmech/seed.py`; scope changes
belong in `curation/seed_scope.tsv`.

## Follow-up Checks

On source refresh, recheck exact taxon 1033934 and AB627875 for explicit
deposits or primary genomes. Inspect the later paper's individual isolate
row before adding a claim. Keep neighboring Horo isolates distinct and
do not join on sequence-length or sample-accession substrings. After
authorized changes, regenerate and run focused validators plus full
`just verify-corpus`. No unresolved blocker remains.

## Additional Notes

`data/taxa/PATHS.tsv:13824` pins the slug;
`curation/seed_scope.tsv:321696` supplies the September 13, 2026 scope
date and one-source reason. The event at `2026-09-13T17:54:04Z`
matches the source list and scope wording. Ignored-inclusive filename
and history-content searches found no prior target review or history
artifact before this report was created.

iModulonDB is not applicable: no gene, regulator, expression module or
mechanism is asserted. No paid research, outside contact, GitHub mutation,
generator run, status promotion or history event occurred.
