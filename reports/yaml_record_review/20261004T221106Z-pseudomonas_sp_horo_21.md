# YAML Record Review: Pseudomonas sp. Horo_21

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_horo_21.yaml`
- Started UTC: 2026-10-04T22:10:03Z
- Finished UTC: 2026-10-04T22:11:06Z
- Verdict: pass

## Target

Read the full generated `TaxonRecord`, `NCBITaxon:1033941`,
Pseudomonas sp. Horo_21. It carries SPECIES rank, BACTERIA domain,
parent `NCBITaxon:196821`, ten ancestors, code 11, EXACT grounding,
SEEDED status, zero inventoried strains, one NCBITAXON NAME attestation
and one inline seed event. No record, code, input, status or history changed.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_horo_21.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_horo_21.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded identity, complete lineage, mapped-source, filename, scope and inline-event comparisons passed.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` limits diagnostics, not scope. Bounded comparisons do not establish byte-level reproduction. Full QC, tests and rendering were not run.
- Not applicable: `just validate-products`; no curator graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target-specific history artifact. Inline provenance was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221375`, full native name object
`data/catalog/ncbi_names-0005.jsonl.gz:30715`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033941&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033941)
agree on exact identifier, label, rank, bacterial domain, parent and
code 11. All ten ancestor IDs match; expanded labels and ranks agree
where supplied. The root-first chain preserves Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae,
Pseudomonas and unclassified Pseudomonas.

The underscore-bearing label is source-native. SPECIES is NCBI's
placeholder rank, not formal species-name validity. The backbone has
no synonyms and the native name object is scientific name only.
Complete exact-ID type-material, merged-ID and dropped-taxon scans
returned no rows. Live taxonomy supplies no conflicting alias or successor.

## Evidence

The sole attestation matches exact NCBI identity, label, one NAME
assertion and snapshot `2026-09-13`. Complete directly mapped BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits scans found no target
rows. A full backbone scan found no children. These support zero
descendant-inclusive BacDive strains, not biological absence of Horo_21.

Exact-taxonomy nuccore search returned one entry. Full metadata,
references and feature qualifiers of
[AB627883.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB627883.1&rettype=gb&retmode=xml)
were inspected. It is a 623-base partial 16S rRNA marker explicitly
naming Horo_21 and taxon 1033941. Source qualifiers identify groundwater
in Horonobe, Hokkaido, Japan. References name Sakurai and Yoshikawa,
an unpublished biofilm study and an April 30, 2011 direct submission.
No registered deposit, BioSample or assembly identifier is supplied.
The marker is not a genome, and the bare strain designation does not
establish a culture-collection accession.

Exact-taxonomy Assembly search returned zero with a `phrasesnotfound`
warning for `txid1033941[Organism:noexp]`. This does not prove genome
absence under other classifications.

The [JAEA later-paper metadata](https://jopss.jaea.go.jp/search/servlet/search?5030464=),
DOI `10.1080/00223131.2012.660015`, was inspected earlier in the
ongoing review session. It exposes no individual Horo_21 row. Publisher
access returned 403 earlier in that session; full paper, isolate table
and figures remain unverified. No phenotype or species reassignment
was inferred from this lead or search excerpts.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`, excluding only `SOURCE.json`.
Patterns included ID, label, slug, separator variants and Horo-XXI.
All four matching contexts were inspected: three target identity/scope
rows and AllTheBacteria sample SAMEA1033941, which describes
Streptococcus pneumoniae. Its accession suffix supports no Horo_21
identity or strain-genome assertion.

A separate AB627883 search over the same ignored-inclusive roots
completed with zero matches. The native name object was read in full.
No eligible deposit, strain or strain-genome assertion was found within
this scope. Optional nomenclature, mappings, definition, evidence and
causal graph slots are appropriately empty for the source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, attestation,
strain inventory, status and inline provenance are supported.

## Recommended Edits

None. Preserve generated YAML and SEEDED status. Future supported
corrections belong in maintained inputs and, as appropriate,
`src/taxonmech/extract.py` or `src/taxonmech/seed.py`; scope changes
belong in `curation/seed_scope.tsv`.

## Follow-up Checks

On refresh, recheck exact taxon 1033941 and AB627883 for explicit
deposits or primary genomes. Inspect the later paper's individual
isolate row before adding a claim. Keep neighboring Horo isolates
separate. After authorized changes, regenerate and run focused
validators plus full `just verify-corpus`. No unresolved blocker remains.

## Additional Notes

`data/taxa/PATHS.tsv:13831` pins the slug;
`curation/seed_scope.tsv:321703` supplies the September 13, 2026 date
and one-source reason. The event at `2026-09-13T17:54:04Z` agrees
with source list and scope wording. Ignored-inclusive filename and
history-content searches found no prior target review or history artifact.

iModulonDB is not applicable: no gene, regulator, expression module or
mechanism is asserted. No paid research, outside contact, GitHub mutation,
generator run, status promotion or history event occurred.
