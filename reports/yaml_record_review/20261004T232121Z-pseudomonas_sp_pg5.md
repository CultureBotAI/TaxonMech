# YAML Record Review: Pseudomonas sp. PG5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_pg5.yaml`
- Started UTC: 2026-10-04T23:20:18Z
- Finished UTC: 2026-10-04T23:21:21Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`, `NCBITaxon:1033974`, Pseudomonas
sp. PG5. It asserts SPECIES rank, BACTERIA domain, parent 196821, ten
ancestors, code 11, EXACT grounding, SEEDED status, zero inventoried
strains, one NCBITAXON NAME attestation and one seed event. No record,
input, code, status or history changed.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_pg5.yaml`; no issues.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_pg5.yaml`; one file, zero errors; emits `reports/instance_validation_failures.tsv`.
- Bounded backbone, full lineage, mapped inventories, scope, filename and inline-event comparisons passed.
- Not run: full-corpus `just verify-corpus`, QC, tests or rendering. `--max-diffs` limits diagnostics, not scope; bounded comparisons do not prove byte reproduction.
- Not applicable: `just validate-products`; no curator graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target history artifact. Inline provenance was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221403`, full native name object
`data/catalog/ncbi_names-0005.jsonl.gz:30743`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033974&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033974)
agree on identifier, label, rank, domain, parent and genetic code.
All ten ancestor IDs match: root, cellular organisms, Bacteria,
Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales,
Pseudomonadaceae, Pseudomonas, unclassified Pseudomonas. Expanded labels
and ranks agree where supplied. SPECIES and EXACT do not establish a
formally named or resolved species.

The backbone has no synonyms; the native name is scientific only.
Complete exact-ID type-material, merged-ID and dropped-taxon scans
returned no rows. No conflicting authority replacement was found.

## Evidence

The sole attestation matches exact NCBI identity, label, one NAME assertion
and snapshot 2026-09-13. Complete directly mapped BacDive, LPSN, GTDB,
GOLD, MediaDive, Madin and BactoTraits scans found no target rows.
A complete backbone scan found no children, supporting zero
descendant-inclusive inventoried strains without denying this isolate.

Exact-taxonomy nuccore search returned one entry. Full metadata,
references and feature qualifiers of
[JF345177.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF345177.1&rettype=gb&retmode=xml)
identify a 1498-base partial 16S marker, PG5, taxon 1033974, and a
February 17, 2011 University of Florida submission by Ghosh,
Rathinasabapathi and Ma. No registered deposit, BioSample or assembly
identifier is supplied. This marker is not a genome.

Its reference identifies [PMID 21840210](https://pubmed.ncbi.nlm.nih.gov/21840210/)
and DOI `10.1016/j.biortech.2011.07.064`. The full PubMed XML, abstract
and identifier list were inspected during the immediately preceding PG12
review in this session. They agree with the bibliographic reference.
The abstract concerns arsenic-resistant rhizosphere bacteria and Pteris
vittata but supplies no named PG5 result. Full text and isolate tables
remain unchecked; no PMC identifier was supplied. No phenotype or
causal assertion was inferred from the shared reference.

Exact-taxonomy Assembly search returned zero with a phrasesnotfound
warning for `txid1033974[Organism:noexp]`; this is a bounded result,
not proof of global genome absence.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json`. Exact ID, slug and PG5 separator variants
returned 34 contexts, all inspected. Unrelated hits include Polaribacter
PG-5; Bacillus PG-5-5, -6, -7 and -9; Arthrobacter PG5-MRL;
Nitrosomonas supralitoralis A PG5; Phlebiopsis expression projects;
E. coli BD_EC_PG_5 and Alteromonas macleodii PG 5. Their deposit and
genome identifiers cannot be transferred by the shared name fragment.
SAMEA1033974 describes Streptococcus pneumoniae, not this target.

A separate JF345177 search in the same ignored-inclusive roots returned
zero matches. No eligible deposit or strain-genome association was found
within this scope. Optional nomenclature, mappings, definition, evidence
and graph slots are appropriately empty for this source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, strain inventory,
attestation, status and inline provenance are supported.

## Recommended Edits

None. Preserve generated YAML and SEEDED status. Future corrections
belong in maintained inputs and, as appropriate,
`src/taxonmech/extract.py` or `src/taxonmech/seed.py`; scope changes
belong in `curation/seed_scope.tsv`. Do not join genomes by PG5 alone.

## Follow-up Checks

Inspect the primary paper's individual isolate data before adding a PG5
phenotype or deposit. Recheck exact taxon and marker on refresh. After
authorized changes, regenerate and run focused validators plus full
`just verify-corpus`. No unresolved blocker remains.

## Additional Notes

`data/taxa/PATHS.tsv:13859` pins the slug;
`curation/seed_scope.tsv:321730` supplies the September 13, 2026 date
and one-source reason. The event at `2026-09-13T17:54:04Z` agrees.
Ignored-inclusive filename and history-content searches found no prior
target report or history artifact. iModulonDB is not applicable: no gene,
regulator or expression module is asserted. No paid research, outside
contact, GitHub mutation, generator run or status promotion occurred.
