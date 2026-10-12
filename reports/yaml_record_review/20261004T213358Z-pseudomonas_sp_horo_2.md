# YAML Record Review: Pseudomonas sp. Horo_2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_horo_2.yaml`
- Started UTC: 2026-10-04T21:33:07Z
- Finished UTC: 2026-10-04T21:33:58Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`, `NCBITaxon:1033924`,
Pseudomonas sp. Horo_2: SPECIES, BACTERIA, parent
`NCBITaxon:196821`, ten root-first ancestors, code 11, EXACT grounding,
SEEDED status, zero inventoried strains, one NCBITAXON NAME attestation
and one inline seed event. No record, code, input, status or history was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_horo_2.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_horo_2.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded identity, full lineage, mapped-source, filename, scope and event comparisons passed.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` limits diagnostics, not scope. Bounded checks do not prove byte-level reproduction. Full QC, tests and rendering were not run.
- Not applicable: `just validate-products`, because there are no curator graph nodes. NCBI identifiers were verified at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target-specific history artifact. Inline provenance was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221358`, the full native
scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30698`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033924&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033924)
agree on identity, label, rank, bacterial domain, parent and code 11.
All ten lineage IDs match, including root; expanded labels and ranks
match where supplied. The chain passes through Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae,
Pseudomonas and unclassified Pseudomonas.

The underscore-bearing Horo_2 label is preserved. SPECIES is an NCBI
placeholder rank, not a formally published species name. Backbone and
native names supply no synonyms. Full exact-ID type-material, merged-ID
and dropped-taxon scans returned no rows, and live taxonomy supplies no
replacement or synonym requiring a change.

## Evidence

The sole attestation exactly matches the NCBI identifier, label, one NAME
assertion and snapshot `2026-09-13`. Complete directly mapped BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventory scans found
no target rows. No children were found in a complete backbone scan;
the descendant-inclusive BacDive strain count is consequently zero.

Exact-taxonomy nuccore search returned one entry. Its complete metadata,
references and feature qualifiers were read:
[AB627864.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB627864.1&rettype=gb&retmode=xml)
is a 631-base partial 16S rRNA sequence explicitly identifying Horo_2
and taxon 1033924, from groundwater in Horonobe, Hokkaido, Japan.
The source lists Sakurai and Yoshikawa, an unpublished biofilm-study
reference, and direct submission dated April 30, 2011.
No registered culture deposit, BioSample or assembly identifier is supplied.
This marker and laboratory designation do not establish a genome link.

Exact-taxonomy Assembly search returned zero with a
`phrasesnotfound` warning for `txid1033924[Organism:noexp]`.
This is not a global claim that no genome exists under any classification.

The [JAEA publication metadata](https://jopss.jaea.go.jp/search/servlet/search?5030464=)
inspected earlier this turn identifies the later Sakurai/Yoshikawa
paper, DOI `10.1080/00223131.2012.660015`. It does not expose Horo_2's
accession or assay row. Direct publisher access returned 403 during
the preceding Horo_1 review; no successful full-text/table inspection
is claimed here. No phenotype or species reassignment was inferred.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`, excluding only `SOURCE.json`.
Patterns included exact ID, label, slug, separator alternatives and
Horo-II. All five matching contexts were inspected: three target
identity/scope rows and two unrelated numeric matches.
GCA_006269055.1 is Salmonella enterica strain FDA1033924-S001-003;
SAMEA1033924 is a Streptococcus pneumoniae sample. Neither supports a join.

A separate AB627864 search over the same ignored-inclusive roots completed
with zero matches. The native name object was read in full.
No eligible strain, deposit or strain-genome assertion was found in
that scope. Empty optional nomenclature, mappings, definition, evidence
and graph slots are appropriate for this seed; zero BacDive strains
does not deny the isolate's existence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, attestation,
strain inventory and audit metadata are supported.

## Recommended Edits

None. Preserve the generated YAML and SEEDED status. Future supported
corrections belong in maintained inventories and, as appropriate,
`src/taxonmech/extract.py` or `src/taxonmech/seed.py`; scope changes
belong in `curation/seed_scope.tsv`.

## Follow-up Checks

On refresh, check the exact taxon and AB627864 for explicit deposits or
primary genomes. Obtain the exact isolate table before importing any
later-paper claim; nearby Horo designations are not interchangeable.
After authorized changes, regenerate and run focused validators plus
full `just verify-corpus`. No unresolved blocker remains.

## Additional Notes

`data/taxa/PATHS.tsv:13814` locks the slug;
`curation/seed_scope.tsv:321686` supplies the September 13, 2026 date
and one-source reason. The event at `2026-09-13T17:54:04Z` matches
the source list and scope wording. Ignored-inclusive filename and
history-content searches found no prior report or target history.

iModulonDB is not applicable: no gene, regulator, expression module or
mechanism is asserted. No paid research, outside contact, GitHub mutation,
generator run, status promotion or history event occurred.

