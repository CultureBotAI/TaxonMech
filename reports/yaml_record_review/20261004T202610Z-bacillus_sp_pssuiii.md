# YAML Record Review: Bacillus sp. PSSUIII

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_pssuiii.yaml`
- Started UTC: 2026-10-04T20:24:28Z
- Finished UTC: 2026-10-04T20:26:10Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1033899`,
Bacillus sp. PSSUIII: SPECIES, BACTERIA, parent `NCBITaxon:185979`,
ten root-first ancestors, code 11, EXACT grounding, SEEDED status,
zero inventoried BacDive strains, one NCBITAXON NAME attestation and
one seed event. This review changes no record, input, code or history.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacillus_sp_pssuiii.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/bacillus_sp_pssuiii.yaml`; one file, zero errors. This implements `just validate-strict` and emits the standard `reports/instance_validation_failures.tsv` diagnostic.
- Bounded source comparisons passed for identity, every ancestor,
  directly mapped inventories, scope, filename lock and seed text.
- Not run: full-corpus `just verify-corpus`. Its `--max-diffs` controls
  diagnostics, not scope. Bounded comparisons are not proof of byte-level
  regeneration. Full QC, rendering and tests were not run.
- Not applicable: `just validate-products`, because no curator graph nodes
  are asserted. NCBI identifiers were checked against primary sources.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline event was checked.

## Identity and Grounding

The backbone `data/raw/ncbitaxon_taxa.tsv:221333`, full native name
object `data/catalog/ncbi_names-0005.jsonl.gz:30673`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033899&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033899)
agree on ID, label, rank, bacterial domain, parent and genetic code.
All ten lineage IDs match, including root 1; expanded live labels and
ranks agree where supplied. The parent is unclassified Bacillus beneath
Bacillus, Bacillaceae, Caryophanales, Bacilli, Bacillota and Bacillati.

SPECIES denotes NCBI's operational placeholder rank, not formal
nomenclatural validity. PSSUIII is not a registered culture accession.
The native name object and backbone supply no synonyms. Complete exact-ID
type-material, merged-ID and dropped-taxon scans returned no rows, and
live taxonomy supplies no replacement or synonym requiring a change.

## Evidence

The attestation correctly carries the exact NCBI ID and label, one NAME
assertion and snapshot `2026-09-13`. Complete directly mapped BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventory scans found
no target rows. The complete backbone scan found no children, so the
descendant-inclusive BacDive count is also zero.

Exact-taxonomy nuccore search returned one entry, whose metadata,
references and all feature qualifiers were inspected.
[JF768715.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768715.1&rettype=gb&retmode=xml)
is a 1,457-base partial 16S rRNA sequence for taxon 1033899 and strain
PSSUIII, from a uranium-rich site at Domiasiat, India. It supplies no
registered deposit, BioSample or genome assembly.

The marker cites [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`, whose metadata and article body were
inspected earlier in the ongoing session. A fresh
[Table 2 XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
checked headers, footnotes, the PSSUIII/JF768715 row and inherited merged
cells: 1,457 bases and closest match Bacillus thuringiensis at greater
than 99.8% similarity. Closest-match literature does not establish a
taxonomic merger or deposit. The supplementary PDF was not inspected.
No phenotype or causal mechanism is asserted by the YAML or added here.

Exact-taxonomy Assembly search returned zero with a `phrasesnotfound`
warning for `txid1033899[Organism:noexp]`; this is not proof of global
genome absence under every possible classification.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. ID, label, slug and designation
searches included Roman-III/digit-3 near-match spellings without equating
them. All four matching lines were inspected: target backbone, scope
and scientific name, plus unrelated Streptococcus pneumoniae sample
SAMEA1033899. The target native name object was read in full. A separate
JF768715 search over the same ignored-inclusive roots found zero matches.

No eligible deposit or strain-genome assertion was found in that scope.
Zero inventoried BacDive strains does not deny the isolate's existence.
The partial marker is not a missing genome identifier. Empty optional
nomenclature, mapping, definition, record-level evidence and causal-graph
slots are appropriate for this source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, attestation,
strain count, status and inline provenance are supported.

## Recommended Edits

None. Preserve generated YAML and SEEDED status. Future source corrections
belong in the maintained inventory pipeline and, as appropriate,
`src/taxonmech/extract.py` or `src/taxonmech/seed.py`; scope changes belong
in `curation/seed_scope.tsv`.

## Follow-up Checks

Recheck the exact taxon, PSSUIII and JF768715 on source refresh for explicit
deposits or primary genome evidence. Do not transfer accessions or assay
results from other isolates in the paper. Rerun focused validators after
authorized changes and `just verify-corpus` after regeneration. No
unresolved blocker prevents this verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13789` locks the slug.
`curation/seed_scope.tsv:321663` supplies the September 13, 2026 addition
and one-source reason. The event at `2026-09-13T17:54:04Z` reproduces
that reason and the NCBITAXON source list. Ignored-inclusive filename
searches in reports/history/curation found no prior target report or
target-specific history artifact before this report was created.

iModulonDB is not applicable to this taxonomic record, which carries no
gene, regulator, expression-module or mechanism claim. No paid research,
outside contact, GitHub mutation, generator run or history event occurred.
