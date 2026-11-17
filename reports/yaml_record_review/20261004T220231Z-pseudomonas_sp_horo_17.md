# YAML Record Review: Pseudomonas sp. Horo_17

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_horo_17.yaml`
- Started UTC: 2026-10-04T22:01:16Z
- Finished UTC: 2026-10-04T22:02:31Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord`, `NCBITaxon:1033937`,
Pseudomonas sp. Horo_17. It asserts SPECIES rank, BACTERIA domain,
parent `NCBITaxon:196821`, ten ancestors, code 11, EXACT grounding,
SEEDED status, zero inventoried strains, one NCBITAXON NAME attestation
and one inline seed event. No record, code, input, status or history changed.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_horo_17.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_horo_17.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded identity, full lineage, mapped-source, filename, scope and inline-event comparisons passed.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` caps diagnostics, not scope. Bounded comparisons are not proof of byte-level reproduction. Full QC, tests and rendering were not run.
- Not applicable: `just validate-products`; there are no curator graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target-specific history artifact. Inline provenance was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221371`, full native name object
`data/catalog/ncbi_names-0005.jsonl.gz:30711`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033937&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033937)
agree on exact identifier, label, rank, bacterial domain, parent and
code 11. All ten root-first ancestor IDs agree; expanded labels and
ranks match where supplied. The chain correctly preserves Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae,
Pseudomonas and unclassified Pseudomonas.

The underscore-bearing label is source-native. SPECIES is NCBI's
placeholder rank, not formal species-name validity. No synonyms are
present in the backbone; the native name object is scientific name only.
Complete exact-ID type-material, merged-ID and dropped-taxon scans
returned no rows. Live taxonomy supplies no conflicting alias or successor.

## Evidence

The sole attestation agrees with NCBI identity, label, one NAME assertion
and snapshot `2026-09-13`. Complete directly mapped BacDive, LPSN,
GTDB, GOLD, MediaDive, Madin and BactoTraits scans found no target rows.
A complete backbone scan found no children. Together these support zero
descendant-inclusive BacDive strains, not nonexistence of the isolate.

Exact-taxonomy nuccore search returned one entry. Full metadata,
references and feature qualifiers of
[AB627879.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB627879.1&rettype=gb&retmode=xml)
were inspected. It is a 630-base partial 16S rRNA marker explicitly
naming Horo_17 and taxon 1033937. Source qualifiers identify groundwater
in Horonobe, Hokkaido, Japan. References name Sakurai and Yoshikawa,
an unpublished biofilm study and an April 30, 2011 direct submission.
No registered culture deposit, BioSample or assembly identifier is
supplied. The marker is not a genome; a bare strain designation does
not establish a registered culture accession.

Exact-taxonomy Assembly search returned zero with a `phrasesnotfound`
warning for `txid1033937[Organism:noexp]`. This bounded result does
not prove genome absence under all classifications.

The [JAEA later-paper metadata](https://jopss.jaea.go.jp/search/servlet/search?5030464=),
DOI `10.1080/00223131.2012.660015`, was inspected during this turn.
It exposes no individual Horo_17 row. Direct publisher access returned
403 earlier in the ongoing session; full paper, isolate table and
figures remain unverified. No phenotype or species reassignment was
inferred from this lead or search excerpts.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`, excluding only `SOURCE.json`.
Patterns included ID, label, slug, separator alternatives and Horo-XVII.
All eight matching contexts were inspected: three target identity/scope
rows and five contexts containing unrelated BioSample SAMEA1033937.

The BV-BRC record 1313.8839, GenBank GCA_900053815.1, RefSeq
GCF_900053815.1, matching GTDB catalog row and AllTheBacteria entry
describe Streptococcus pneumoniae, with B18042 supplied where a strain
is named. Their sample-accession suffix is not Horo_17's taxonomy ID
and supports no target identity or genome join.

A separate AB627879 search over the same ignored-inclusive roots found
one match, also inspected: AllTheBacteria sample SAMN46882674,
Streptococcus pyogenes. The match occurs only inside SeqKit checksum
`seqkit.v0.1_DLS_k0_fab6278794439f73339b92992c0c38fc`, not an
accession assertion. It is not evidence for this isolate.

The native scientific-name object was read in full. No eligible deposit,
strain or strain-genome assertion was found within this search scope.
Optional nomenclature, mappings, definition, evidence and graph slots
are appropriately empty for the source-attested seed.

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

On refresh, recheck exact taxon 1033937 and AB627879 for explicit
deposits or primary genomes. Inspect the later paper's individual
isolate row before adding a claim. Keep Horo isolates distinct; do
not join on sample suffixes or checksum substrings. After authorized
changes, regenerate and run focused validators plus full
`just verify-corpus`. No unresolved blocker remains.

## Additional Notes

`data/taxa/PATHS.tsv:13827` pins the slug;
`curation/seed_scope.tsv:321699` supplies the September 13, 2026 date
and one-source reason. The `2026-09-13T17:54:04Z` event matches
source list and scope wording. Ignored-inclusive filename and history
content searches found no prior target review or history artifact.

iModulonDB is not applicable: no gene, regulator, expression module or
mechanism is asserted. No paid research, outside contact, GitHub mutation,
generator run, status promotion or history event occurred.
