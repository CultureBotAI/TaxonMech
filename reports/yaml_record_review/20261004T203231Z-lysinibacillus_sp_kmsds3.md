# YAML Record Review: Lysinibacillus sp. KMSDS3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lysinibacillus_sp_kmsds3.yaml`
- Started UTC: 2026-10-04T20:31:13Z
- Finished UTC: 2026-10-04T20:32:31Z
- Verdict: pass

## Target

Read the full generated `TaxonRecord` for `NCBITaxon:1033901`,
Lysinibacillus sp. KMSDS3: SPECIES, BACTERIA, parent `NCBITaxon:2636778`,
ten root-first ancestors, code 11, EXACT grounding, SEEDED status,
zero inventoried BacDive strains, one NCBITAXON NAME attestation and
one seed event. No record, input, code, status or history was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/lysinibacillus_sp_kmsds3.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/lysinibacillus_sp_kmsds3.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded source comparisons passed for identity, all ancestor labels
  and ranks, directly mapped inventories, filename lock, scope and seed
  wording. A full backbone scan found no children.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` limits its
  diagnostic output, not scope. Bounded comparisons do not prove
  byte-identical reproduction. Full QC, rendering and tests were not run.
- Not applicable: `just validate-products`, because no curator graph nodes
  are asserted. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline event was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221335`, full native name object
`data/catalog/ncbi_names-0005.jsonl.gz:30675`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033901&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033901)
agree on identifier, label, rank, bacterial domain, parent and code 11.
All ten ancestor IDs agree, including root 1; expanded live labels and
ranks agree where supplied. The direct parent is unclassified
Lysinibacillus beneath Lysinibacillus, Bacillaceae, Caryophanales,
Bacilli, Bacillota and Bacillati.

SPECIES is NCBI's operational placeholder rank, not a nomenclatural
validity assertion. KMSDS3 is not a culture-collection accession. The
native name object and backbone supply no synonyms. Complete exact-ID
type-material, merged-ID and dropped-taxon scans returned no rows, and
the live response supplies no replacement or synonym requiring a change.

## Evidence

The sole attestation correctly reproduces the exact NCBI ID and label,
one NAME assertion and snapshot `2026-09-13`. Complete directly mapped
BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits scans returned
no target rows. With no descendants, the full descendant-inclusive
BacDive strain count is zero.

Exact-taxonomy nuccore search returned one entry. All metadata,
references and feature qualifiers were inspected:
[JF768717.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768717.1&rettype=gb&retmode=xml)
is a 1,460-base partial 16S rRNA sequence explicitly assigned to strain
KMSDS3 and taxon 1033901, from a uranium-rich site at Domiasiat, India.
It supplies no registered deposit, BioSample or genome assembly.

The sequence cites [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`. Article metadata and body were inspected
earlier in the ongoing session. A fresh
[Table 2 XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
checked headers, footnotes and the complete KMSDS3/JF768717 row:
1,460 bases and a closest match to Lysinibacillus fusiformis at 100%
similarity. Even this reported marker identity does not by itself
establish a taxonomic merger, registered deposit or genome equivalence.
The supplementary PDF was not inspected; no phenotype or causal
mechanism is asserted by the YAML or imported into it.

Exact-taxonomy Assembly search returned zero with a `phrasesnotfound`
warning for `txid1033901[Organism:noexp]`. This is a bounded query result,
not global proof that no genome exists under another classification.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. Taxon, name, slug and designation
spellings included digit-3/Roman-III near matches without equating them.
All five matching lines were inspected. Three were target backbone,
scope and scientific name; the two unrelated hits were the length
1033901 on Acidimicrobiia bacterium assembly GCA_060846805.1 and
Streptococcus pneumoniae sample SAMEA1033901. The target native name
object was read in full. A separate JF768717 search across the same
ignored-inclusive roots completed with zero matches.

No eligible deposit or strain-genome assertion was found in that scope.
Zero BacDive entries is an inventory count, not absence of a biological
isolate. The partial marker is not a missing genome assembly. Empty
optional nomenclature, mappings, definition, record-level evidence and
causal graphs are appropriate for this source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected evidence scope. Identity, lineage,
attestation, strain count, status and inline provenance are supported.
The literature's closest-match name is correctly not substituted for
the source taxonomy.

## Recommended Edits

None. Preserve generated YAML and SEEDED status. Future supported
source corrections belong in the maintained inventory pipeline and,
as appropriate, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`;
scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

On source refresh, recheck the exact taxon, KMSDS3 and JF768717 for
explicit deposit or primary genome evidence. Do not infer a merger
from the marker's closest-match similarity or transfer accessions from
other study isolates. Rerun focused validators after authorized input
changes and `just verify-corpus` after regeneration. No unresolved
blocker prevents this verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13791` locks the slug.
`curation/seed_scope.tsv:321664` supplies the September 13, 2026 addition
and one-source reason. The event at `2026-09-13T17:54:04Z` reproduces
the NCBITAXON source list and scope reason. Ignored-inclusive filename
searches in reports/history/curation found no prior target report or
target-specific history artifact before creation.

iModulonDB is not applicable to this taxonomic record, which carries no
gene, regulator, expression-module or mechanism claim. No paid research,
outside contact, GitHub mutation, generator run, status promotion or
history event occurred.
