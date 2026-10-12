# YAML Record Review: Pseudomonas sp. Horo_16

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_horo_16.yaml`
- Started UTC: 2026-10-04T21:59:16Z
- Finished UTC: 2026-10-04T22:00:30Z
- Verdict: pass

## Target

Read the full generated `TaxonRecord`, `NCBITaxon:1033936`,
Pseudomonas sp. Horo_16. It carries SPECIES rank, BACTERIA domain,
parent `NCBITaxon:196821`, ten ancestors, code 11, EXACT grounding,
SEEDED status, zero inventoried strains, one NCBITAXON NAME attestation
and one inline seed event. No record, code, input, status or history changed.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_horo_16.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_horo_16.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded identity, full lineage, mapped-source, filename, scope and inline-event comparisons passed.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` limits diagnostics, not scope. Bounded comparisons do not establish byte-level reproduction. Full QC, tests and rendering were not run.
- Not applicable: `just validate-products`; there are no curator graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target-specific history artifact. Inline provenance was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221370`, full native name object
`data/catalog/ncbi_names-0005.jsonl.gz:30710`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033936&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033936)
agree on exact identifier, label, rank, bacterial placement, parent and
code 11. All ten ancestor IDs match; expanded labels and ranks agree
where available. The chain preserves Pseudomonadati, Pseudomonadota,
Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae, Pseudomonas and
unclassified Pseudomonas without importing another taxonomy's placement.

The underscore-bearing label is source-native. SPECIES is NCBI's rank
for this placeholder, not nomenclatural validity. The backbone has no
synonyms; the native name object is scientific name only. Complete
exact-ID type-material, merged-ID and dropped-taxon scans returned no
rows. Live taxonomy supplies no conflicting alias, type or replacement.

## Evidence

The sole attestation matches NCBI identity, label, one NAME assertion
and snapshot `2026-09-13`. Complete directly mapped BacDive, LPSN,
GTDB, GOLD, MediaDive, Madin and BactoTraits scans returned no target
rows. A full backbone scan found no children. These support zero
descendant-inclusive BacDive strains, not biological absence of Horo_16.

Exact-taxonomy nuccore search returned one entry. Full metadata,
references and feature qualifiers of
[AB627878.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB627878.1&rettype=gb&retmode=xml)
were inspected. The 629-base partial 16S rRNA marker explicitly names
Horo_16 and taxon 1033936. Its source qualifiers give groundwater in
Horonobe, Hokkaido, Japan. References name Sakurai and Yoshikawa, an
unpublished biofilm study and an April 30, 2011 direct submission.
The entry supplies no registered deposit, BioSample or assembly
identifier. Neither its marker status nor the bare strain designation
establishes a genome or culture-deposit join.

Exact-taxonomy Assembly search returned zero with a `phrasesnotfound`
warning for `txid1033936[Organism:noexp]`. This does not establish
absence of genomes filed under other classifications.

The [JAEA later-paper metadata](https://jopss.jaea.go.jp/search/servlet/search?5030464=),
DOI `10.1080/00223131.2012.660015`, was inspected during this review
turn. It does not expose an individual Horo_16 row. Publisher access
returned 403 earlier in the ongoing session; full paper, isolate table
and figures remain unverified. No phenotype or species reassignment
was inferred from the metadata lead or search excerpts.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`, excluding only `SOURCE.json`.
Patterns covered ID, label, slug, separator variants and Horo-XVI.
All four matching contexts were inspected: three target identity/scope
rows and AllTheBacteria sample SAMEA1033936. That sample describes
Streptococcus pneumoniae, not this isolate; a numeric substring cannot
supply a Horo_16 strain-genome assertion.

A separate AB627878 search across the same ignored-inclusive roots
completed with zero matches. The native name object was read in full.
No eligible deposit, strain or strain-genome assertion was found in
this scope. Optional nomenclature, mappings, definition, evidence and
causal graphs are appropriately empty for this source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, attestation,
strain count, status and inline provenance are supported.

## Recommended Edits

None. Preserve generated YAML and SEEDED status. Future supported
corrections belong in maintained inputs and, as appropriate,
`src/taxonmech/extract.py` or `src/taxonmech/seed.py`; scope changes
belong in `curation/seed_scope.tsv`.

## Follow-up Checks

On refresh, recheck taxon 1033936 and AB627878 for explicit culture
deposits or primary genomes. Read the later paper's exact isolate row
before adding an individual claim. Keep neighboring Horo isolates
separate. After authorized changes, regenerate and run focused
validators plus full `just verify-corpus`. No unresolved blocker remains.

## Additional Notes

`data/taxa/PATHS.tsv:13826` pins the slug;
`curation/seed_scope.tsv:321698` supplies the September 13, 2026 date
and one-source reason. The `2026-09-13T17:54:04Z` seed event agrees
with the source list and scope wording. Ignored-inclusive filename and
history-content searches found no prior target review or history artifact.

iModulonDB is not applicable: no gene, regulator, expression module or
mechanism is asserted. No paid research, outside contact, GitHub mutation,
generator run, status promotion or history event occurred.
