# YAML Record Review: Microbacterium sp. PSSUR4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microbacterium_sp_pssur4.yaml`
- Started UTC: 2026-10-04T20:36:31Z
- Finished UTC: 2026-10-04T20:37:40Z
- Verdict: pass

## Target

Read the full generated `TaxonRecord` for `NCBITaxon:1033903`,
Microbacterium sp. PSSUR4: SPECIES, BACTERIA, parent `NCBITaxon:2609290`,
ten root-first ancestors, code 11, EXACT grounding and SEEDED status.
It contains zero inventoried BacDive strains, one NCBITAXON NAME
attestation and one seed event. No record, input, code, status or
history entry was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/microbacterium_sp_pssur4.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/microbacterium_sp_pssur4.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded structured comparisons passed for identity, every ancestor,
  direct inventories, filename lock, scope and seed text.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` caps diagnostics,
  not scope. Bounded comparisons do not establish byte-level reproduction.
  Full QC, rendering and tests were not run.
- Not applicable: `just validate-products`, because no curator graph nodes
  are asserted. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline event was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221337`, full native name object
`data/catalog/ncbi_names-0005.jsonl.gz:30677`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033903&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033903)
agree on identity, label, rank, bacterial domain, parent and code 11.
All ten lineage IDs match, including root; expanded live labels and
ranks agree where supplied. The chain includes Bacillati,
Actinomycetota, Actinomycetes, Micrococcales, Microbacteriaceae,
Microbacterium and unclassified Microbacterium.

SPECIES is NCBI's operational placeholder rank, not formal nomenclatural
validity. PSSUR4 is not a registered culture accession. No synonyms are
supplied by the native name object or backbone. Complete exact-ID
type-material, merged-ID and dropped-taxon scans returned no rows, and
live taxonomy supplies no replacement or synonym requiring a change.

## Evidence

The sole attestation matches the exact NCBI ID and label, one NAME
assertion and snapshot `2026-09-13`. Complete directly mapped BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits scans found no target
rows. A complete backbone scan found no children, so zero is also the
full descendant-inclusive BacDive count.

Exact-taxonomy nuccore search returned one entry. Its metadata,
references and feature qualifiers identify
[JF768719.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768719.1&rettype=gb&retmode=xml)
as a 1,431-base partial 16S rRNA sequence for taxon 1033903 and strain
PSSUR4, from a uranium-rich site at Domiasiat, India. It supplies no
registered deposit, BioSample or genome assembly.

The marker cites [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`, whose metadata and article body were
inspected earlier in the ongoing session. A fresh
[Table 2 XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
checked headers, footnotes and the full PSSUR4/JF768719 row: 1,431 bases,
with Microbacterium azadirachtae as the closest match at 99.34%
similarity. This is marker-similarity context, not a taxonomic merger,
registered deposit or genome identity. The supplementary PDF was not
inspected. No phenotype or mechanism is asserted by the YAML or added.

Exact-taxonomy Assembly search returned zero with a `phrasesnotfound`
warning for `txid1033903[Organism:noexp]`. This bounded result is not
proof of genome absence under every possible classification.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. ID, label, slug and designation
searches included digit-4/Roman-IV near matches without equating them.
All four matching lines were inspected: target backbone, scope and
scientific name, plus unrelated Streptococcus pneumoniae sample
SAMEA1033903. The matching target name object was read in full. A
separate JF768719 search over the same ignored-inclusive roots completed
with zero matches.

No eligible deposit or strain-genome assertion was found in that scope.
Zero BacDive inventory entries does not deny the isolate's existence.
A partial 16S sequence is not a missing genome identifier. Empty optional
nomenclature, mappings, definition, record-level evidence and causal
graphs are appropriate for this source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected evidence scope. Identity, lineage,
attestation, strain count, status and inline provenance are supported.
The literature's closest-match name is not substituted for NCBI identity.

## Recommended Edits

None. Preserve generated YAML and SEEDED status. Future supported
source corrections belong in the maintained inventory pipeline and,
as appropriate, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`;
scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Recheck PSSUR4, its exact taxon and JF768719 on source refresh for
explicit deposits or primary genomes. Keep study-isolate scope intact.
After authorized changes, rerun focused validators and the full
`just verify-corpus` gate after regeneration. No unresolved blocker
prevents this verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13793` locks the slug.
`curation/seed_scope.tsv:321666` supplies the September 13, 2026 addition
and one-source reason. The event at `2026-09-13T17:54:04Z` reproduces
that reason and the NCBITAXON source list. Ignored-inclusive filename
searches in reports/history/curation found no prior target report or
target-specific history artifact before creation.

iModulonDB is not applicable to this taxonomic record, which asserts no
gene, regulator, expression module or mechanism. No paid research,
outside contact, GitHub mutation, generator run, status promotion or
history event occurred.
