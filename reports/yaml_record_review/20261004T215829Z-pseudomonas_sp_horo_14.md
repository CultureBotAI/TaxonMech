# YAML Record Review: Pseudomonas sp. Horo_14

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_horo_14.yaml`
- Started UTC: 2026-10-04T21:57:19Z
- Finished UTC: 2026-10-04T21:58:29Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`, `NCBITaxon:1033935`,
Pseudomonas sp. Horo_14. It asserts SPECIES, BACTERIA, parent
`NCBITaxon:196821`, ten ancestors, code 11, EXACT grounding, SEEDED
status, zero inventoried strains, one NCBITAXON NAME attestation and
one inline seed event. No record, code, input, status or history changed.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_horo_14.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_horo_14.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded identity, complete lineage, mapped-source, filename, scope and inline-event comparisons passed.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` caps diagnostics, not scope. Bounded comparisons do not prove byte-level reproduction. Full QC, tests and rendering were not run.
- Not applicable: `just validate-products`; no curator graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target-specific history artifact. Inline provenance was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221369`, full native name object
`data/catalog/ncbi_names-0005.jsonl.gz:30709`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033935&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033935)
agree on identifier, exact label, rank, bacterial domain, parent and
code 11. All ten ancestor IDs match; expanded labels and ranks agree
where supplied. Root-first lineage correctly retains Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae,
Pseudomonas and unclassified Pseudomonas.

The underscore-bearing name is source-native. SPECIES is NCBI's
placeholder rank, not formal species-name validity. No synonyms are
present in the backbone; the native name is scientific name only.
Complete exact-ID type-material, merged-ID and dropped-taxon scans
returned no rows. Live taxonomy supplies no conflicting name or replacement.

## Evidence

The NCBITAXON attestation matches exact identity, label, one NAME
assertion and snapshot `2026-09-13`. Complete directly mapped BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits scans returned no
target rows. The full backbone has no children, supporting zero
descendant-inclusive BacDive strains, not absence of the isolate.

Exact-taxonomy nuccore search returned one entry. Full metadata,
references and feature qualifiers of
[AB627876.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB627876.1&rettype=gb&retmode=xml)
were read. It is a 599-base partial 16S rRNA marker explicitly naming
Horo_14 and taxon 1033935. Source qualifiers identify groundwater in
Horonobe, Hokkaido, Japan. References name Sakurai and Yoshikawa, an
unpublished biofilm study and an April 30, 2011 direct submission.
No registered culture deposit, BioSample or assembly identifier is
supplied. The marker is not a genome and the strain designation is not
a verified culture-collection accession.

Exact-taxonomy Assembly search returned zero with a `phrasesnotfound`
warning for `txid1033935[Organism:noexp]`. It does not prove genome
absence under other classifications.

The freshly inspected [JAEA publication metadata](https://jopss.jaea.go.jp/search/servlet/search?5030464=)
confirms DOI `10.1080/00223131.2012.660015`, but has no isolate-level
Horo_14 row. Publisher access returned 403 earlier in the ongoing
review session. Full paper, tables and figures remain unverified;
no individual phenotype or species reassignment was inferred from
that lead or search excerpts.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`, excluding only `SOURCE.json`.
Patterns included ID, label, slug, separator variants and Horo-XIV.
All four matching contexts were inspected: three target identity/scope
rows and AllTheBacteria sample SAMEA1033935, which identifies
Streptococcus pneumoniae. The latter is a numeric near miss, not a
Horo_14 sample or strain-genome link.

A separate AB627876 search over the same ignored-inclusive roots
completed with zero matches. The native name object was read in full.
No eligible deposit, strain or strain-genome assertion was found within
this scope. Optional nomenclature, mappings, definition, evidence and
graph slots are appropriately empty for the source-attested seed.

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

On refresh, recheck the exact taxon and AB627876 for explicit deposits
or primary genomes. Inspect the later paper's individual isolate row
before using it for a claim. Keep neighboring Horo isolates separate.
After authorized changes, regenerate and run focused validators plus
full `just verify-corpus`. No unresolved blocker remains.

## Additional Notes

`data/taxa/PATHS.tsv:13825` pins the slug;
`curation/seed_scope.tsv:321697` supplies the September 13, 2026 date
and one-source reason. The `2026-09-13T17:54:04Z` seed event matches
source list and scope wording. Ignored-inclusive filename and history
content searches found no prior target review or history artifact.

iModulonDB is not applicable: no gene, regulator, expression module or
mechanism is asserted. No paid research, outside contact, GitHub mutation,
generator run, status promotion or history event occurred.
