# YAML Record Review: Paenibacillus sp. BIA1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_sp_bia1.yaml`
- Started UTC: 2026-10-04T20:40:31Z
- Finished UTC: 2026-10-04T20:41:51Z
- Verdict: pass

## Target

Read the full generated `TaxonRecord` for `NCBITaxon:1033905`,
Paenibacillus sp. BIA1: SPECIES, BACTERIA, parent `NCBITaxon:185978`,
ten root-first ancestors, code 11, EXACT grounding and SEEDED status.
It contains zero inventoried BacDive strains, one NCBITAXON NAME
attestation and one seed event. No record, input, code, status or
history entry was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/paenibacillus_sp_bia1.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/paenibacillus_sp_bia1.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded structured comparisons passed for identity, every ancestor,
  directly mapped inventories, filename lock, scope and seed wording.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` caps diagnostics,
  not verification scope. Bounded comparisons do not establish byte-level
  reproduction. Full QC, rendering and tests were not run.
- Not applicable: `just validate-products`, because no curator graph nodes
  are asserted. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline event was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221339`, full native name object
`data/catalog/ncbi_names-0005.jsonl.gz:30679`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033905&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033905)
agree on identity, label, rank, bacterial domain, parent and code 11.
All ten lineage IDs match, including root; expanded live labels and
ranks agree where supplied. The chain includes Bacillati, Bacillota,
Bacilli, Caryophanales, Paenibacillaceae, Paenibacillus and unclassified
Paenibacillus.

SPECIES is NCBI's operational placeholder rank, not formal nomenclatural
validity. BIA1 is not a registered deposit accession. In particular, it
is not Propionibacterium freudenreichii subsp. shermanii CIRM-BIA1,
`NCBITaxon:754252`; that distinct concept's full native scientific-name
object at `data/catalog/ncbi_names-0004.jsonl.gz:26834` was inspected.

The target native name object and backbone provide no synonyms. Complete
exact-ID type-material, merged-ID and dropped-taxon scans returned no
rows, and live taxonomy supplies no replacement or synonym requiring a
change.

## Evidence

The sole attestation matches the exact NCBI ID and label, one NAME
assertion and snapshot `2026-09-13`. Complete directly mapped BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits scans found no target
rows. A complete backbone scan found no children, so zero is also the
full descendant-inclusive BacDive count.

Exact-taxonomy nuccore search returned one entry. All metadata,
references and feature qualifiers were inspected:
[JF768721.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768721.1&rettype=gb&retmode=xml)
is a 1,455-base partial 16S rRNA sequence for strain BIA1 and taxon
1033905, from a uranium-rich site at Domiasiat, India. It supplies no
registered deposit, BioSample or assembly.

The marker cites [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`, whose metadata and article body were
inspected earlier in the ongoing session. A fresh
[Table 2 XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
checked headers, footnotes and the complete BIA1/JF768721 row:
1,455 bases and closest match Paenibacillus taichungensis at 98.82%
similarity. This marker context does not establish a formal taxonomic
merger, deposit or genome identity. The supplementary PDF was not
inspected. No phenotype or causal mechanism is asserted by the YAML
or imported from the paper.

Exact-taxonomy Assembly search returned zero with a `phrasesnotfound`
warning for `txid1033905[Organism:noexp]`. This is a bounded search,
not proof of genome absence under every classification.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. ID, label, slug and bounded
BIA1 spelling searches produced 38 matching lines, all inspected in
their source context. Three were target backbone, scope and native name.
The remaining hits were excluded for explicit identity reasons:

- CIRM-BIA1 entries identify Propionibacterium taxon 754252, including
  its genome, GOLD and BacDive-associated rows. The matching ATCC 9614,
  BacDive 12643 and GCA/GCF_000091725.1 belong to that source concept,
  not this Paenibacillus isolate. A suffix match cannot transfer them.
- GOLD and StrainInfo biA1/BIA 1 designations identify Aspergillus
  nidulans, taxon 162425. Their displayed source taxon and designation
  contexts distinguish them from BIA1; no eukaryotic record was reviewed
  or changed as part of this check.
- SAMEA1033905 is a Streptococcus pneumoniae sample, a numeric collision.

The target native name object was read in full. A separate JF768721
search across the same ignored-inclusive roots completed with zero
matches. No eligible deposit or strain-genome assertion for the target
was found in that scope.

Zero BacDive entries does not deny a biological isolate's existence.
A partial 16S sequence is not a missing genome identifier. Empty optional
nomenclature, mappings, definition, record-level evidence and causal
graphs are appropriate for this source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, attestation,
strain count, status and inline provenance are supported. The generated
record does not inherit the unrelated CIRM-BIA1 or Aspergillus evidence.

## Recommended Edits

None. Preserve generated YAML and SEEDED status. Future supported
corrections belong in the maintained inventory pipeline and, as
appropriate, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`;
scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Recheck the exact taxon, full Paenibacillus label and JF768721 on source
refresh for explicit deposit or primary genome evidence. Preserve whole
identifier and organism boundaries; do not join BIA1 to CIRM-BIA1 or
biA1 designations. After authorized changes, rerun focused validators
and `just verify-corpus` after regeneration. No unresolved blocker
prevents this verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13795` locks the slug.
`curation/seed_scope.tsv:321668` supplies the September 13, 2026 addition
and one-source reason. The event at `2026-09-13T17:54:04Z` reproduces
the NCBITAXON source list and scope reason. Ignored-inclusive filename
searches in reports/history/curation found no prior target report or
target-specific history artifact before creation.

iModulonDB is not applicable to this taxonomic record, which asserts no
gene, regulator, expression module or mechanism. No paid research,
outside contact, GitHub mutation, generator run, status promotion or
history event occurred.
