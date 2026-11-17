# YAML Record Review: Paenibacillus sp. KMSDS2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_sp_kmsds2.yaml`
- Started UTC: 2026-10-04T20:47:22Z
- Finished UTC: 2026-10-04T20:48:30Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1033908`,
Paenibacillus sp. KMSDS2: SPECIES, BACTERIA, parent `NCBITaxon:185978`,
ten root-first ancestors, genetic code 11, EXACT grounding and SEEDED
status. It contains zero inventoried BacDive strains, one NCBITAXON
NAME attestation and one seed event. No record, input, code, status or
history entry was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/paenibacillus_sp_kmsds2.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/paenibacillus_sp_kmsds2.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded structured comparisons passed for identity, all ancestors,
  directly mapped inventories, filename lock, scope and seed wording.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` limits
  diagnostics, not scope. Bounded comparisons do not establish byte-level
  reproduction. Full QC, rendering and tests were not run.
- Not applicable: `just validate-products`, because no curator graph nodes
  are asserted. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline event was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221342`, full native name object
`data/catalog/ncbi_names-0005.jsonl.gz:30682`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033908&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033908)
agree on ID, label, rank, bacterial domain, parent and code 11.
All ten lineage IDs match, including root; expanded live labels and
ranks agree where supplied. The chain includes Bacillati, Bacillota,
Bacilli, Caryophanales, Paenibacillaceae, Paenibacillus and unclassified
Paenibacillus.

SPECIES is NCBI's operational placeholder rank, not formal nomenclatural
validity. KMSDS2 is not a registered culture accession. The native name
object and backbone supply no synonyms. Complete exact-ID type-material,
merged-ID and dropped-taxon scans returned no rows; live taxonomy
provides no replacement or synonym requiring a change.

## Evidence

The sole attestation matches the exact NCBI ID and label, one NAME
assertion and snapshot `2026-09-13`. Complete directly mapped BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits scans found no target
rows. A complete backbone scan found no children, so zero is also the
full descendant-inclusive BacDive count.

Exact-taxonomy nuccore search returned one entry. All metadata,
references and feature qualifiers were inspected:
[JF768723.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768723.1&rettype=gb&retmode=xml)
is a 1,500-base partial 16S rRNA sequence explicitly assigned to
KMSDS2 and taxon 1033908, from a uranium-rich site at Domiasiat, India.
It supplies no registered deposit, BioSample or assembly identifier.

The marker cites [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`, whose metadata and article body were
inspected earlier in the ongoing session. A fresh
[Table 2 XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
checked headers, footnotes, the KMSDS2/JF768723 row and inherited merged
cells: 1,500 bases and closest match Paenibacillus pabuli at greater
than 99.3% similarity. This is marker context, not a formal taxonomic
merger, deposit or genome identity. The supplementary PDF was not
inspected. No phenotype or mechanism is asserted by the YAML or
imported from the paper.

Exact-taxonomy Assembly search returned zero with a `phrasesnotfound`
warning for `txid1033908[Organism:noexp]`. This bounded result is not
proof of genome absence under every possible classification.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. ID, name, slug and designation
searches included digit-2/Roman-II near matches without equating them.
All five matching lines were inspected in source context: target
backbone, scope and scientific name, plus two unrelated numeric matches.
SAMEA1033908 is a Streptococcus pneumoniae sample; 1033908 is a genome
length on GCA_902782915.1, classified as an uncultured Erysipelotrichaceae
bacterium. Neither supports a KMSDS2 join.

The target native name object was read in full. A separate JF768723
search over the same ignored-inclusive roots completed with zero
matches. No eligible deposit or strain-genome assertion for KMSDS2 was
found in that scope.

Zero BacDive inventory entries does not deny the isolate's existence.
A partial 16S marker is not a missing genome identifier. Empty optional
nomenclature, mappings, definition, record-level evidence and causal
graphs are appropriate for this source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, attestation,
strain count, status and inline provenance are supported. The closest
16S match is not substituted for the source taxonomy.

## Recommended Edits

None. Preserve generated YAML and SEEDED status. Future supported
corrections belong in the maintained inventory pipeline and, as
appropriate, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`;
scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

On source refresh, recheck KMSDS2, its exact taxon and JF768723 for
explicit deposits or primary genomes. Keep other KMSDS isolates and
their accessions separate. After authorized changes, rerun focused
validators and the full `just verify-corpus` gate after regeneration.
No unresolved blocker prevents this verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13798` locks the slug.
`curation/seed_scope.tsv:321671` supplies the September 13, 2026 addition
and one-source reason. The event at `2026-09-13T17:54:04Z` reproduces
that reason and the NCBITAXON source list. Ignored-inclusive filename
searches in reports/history/curation found no prior target report or
target-specific history artifact before creation.

iModulonDB is not applicable to this taxonomic record, which asserts no
gene, regulator, expression module or mechanism. No paid research,
outside contact, GitHub mutation, generator run, status promotion or
history event occurred.
