# YAML Record Review: Bacillus sp. PKSWIII

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_pkswiii.yaml`
- Started UTC: 2026-10-04T20:22:12Z
- Finished UTC: 2026-10-04T20:23:35Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1033898`,
Bacillus sp. PKSWIII: SPECIES, BACTERIA, parent `NCBITaxon:185979`,
ten root-first ancestors, genetic code 11, EXACT grounding and SEEDED
status. It carries zero inventoried BacDive strains, one NCBITAXON
NAME attestation and one seed event. No generated record, input, code,
status or history entry was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacillus_sp_pkswiii.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/bacillus_sp_pkswiii.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded structured comparisons passed for all identity and ancestor
  fields, directly mapped inventories, filename lock, scope and seed text.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` limits
  diagnostics, not its scope. The comparisons above do not prove
  byte-identical regeneration. Full QC, rendering and tests were not run.
- Not applicable: `just validate-products`, because no curator graph nodes
  are asserted. Identifiers were checked against NCBI directly.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline seed event was inspected.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:221332`, full native name
object at `data/catalog/ncbi_names-0005.jsonl.gz:30672`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033898&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033898)
agree on the target identity, rank, domain, parent and code 11. All ten
ancestor IDs agree, including root; expanded live labels and ranks agree
where supplied. The direct parent is unclassified Bacillus beneath
Bacillus, Bacillaceae, Caryophanales, Bacilli, Bacillota and Bacillati.

SPECIES is NCBI's placeholder rank, not a valid-publication assertion.
PKSWIII is not a registered culture accession. PKSW3 is a different
concept, `NCBITaxon:1033896`, confirmed by the full native name object
at line 30670 and backbone row 221330. Roman III is not normalized to 3.

The target has no supplied synonyms. Complete exact-ID type-material,
merged-ID and dropped-taxon scans returned no rows. Live taxonomy
provides no replacement or synonym requiring a change.

## Evidence

The sole attestation reproduces the exact NCBI ID and label, one NAME
assertion and snapshot `2026-09-13`. Complete directly mapped BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits scans found no target
rows. A complete backbone scan found no children; the zero BacDive count
therefore includes all descendants.

Exact-taxonomy nuccore search returned one entry. Its metadata,
references and all feature qualifiers identify
[JF768714.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768714.1&rettype=gb&retmode=xml)
as a 1,458-base partial 16S rRNA sequence explicitly assigned to
strain PKSWIII and taxon 1033898, from a uranium-rich site at Domiasiat,
India. It gives no registered deposit, BioSample or assembly accession.

The sequence cites [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`. The metadata and article body were inspected
earlier in the ongoing session. A fresh
[Table 2 XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
checked headers, footnotes and complete separate rows for PKSWIII and
PKSW3. PKSWIII/JF768714 has 1,458 bases and a closest match to Bacillus
pseudomycoides at 99.93%; PKSW3/JF768712 instead has 1,446 bases and a
closest match to Bacillus isronensis at 99.59%. These distinct rows
reinforce the non-equivalence of the labels. Closest-match similarity
is not a formal taxonomic merger or culture deposit. The supplementary
PDF was not inspected, and no phenotype or mechanism was imported.

Exact-taxonomy Assembly search returned zero with a `phrasesnotfound`
warning for `txid1033898[Organism:noexp]`. This is a bounded search,
not proof that no genome could exist under another classification.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. Taxon, label, slug and designation
searches deliberately included PKSW3 as a near-match control. All seven
matching lines were inspected: three target entries, three PKSW3 entries
and the unrelated Streptococcus pneumoniae sample SAMEA1033898.
Both matching native scientific-name objects were read in full.
A separate ignored-inclusive JF768714 search across those roots returned
zero matches.

No eligible PKSWIII deposit or strain-genome assertion was found in that
scope. A zero BacDive count is an inventory count, not absence of a
biological isolate. A partial 16S marker is not a missing assembly.
Empty optional nomenclature, mapping, definition, record-level evidence
and causal-graph fields are appropriate for this source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected evidence scope. Identity, lineage,
attestation, strain count, status and inline provenance are supported.
The generated record does not conflate PKSWIII with PKSW3.

## Recommended Edits

None. Preserve generated YAML and SEEDED status. Future supported
corrections belong in the maintained source pipeline and, as appropriate,
`src/taxonmech/extract.py` or `src/taxonmech/seed.py`; scope corrections
belong in `curation/seed_scope.tsv`.

## Follow-up Checks

On source refresh, recheck the exact taxon, PKSWIII and JF768714 for
explicit culture-deposit or primary genome evidence, preserving the
distinction from PKSW3. Rerun focused validators after authorized input
changes and `just verify-corpus` after regeneration. No unresolved
blocker prevents this verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13788` fixes the slug, and
`curation/seed_scope.tsv:321662` supplies the September 13, 2026 scope
addition and one-source reason. The event at `2026-09-13T17:54:04Z`
matches the NCBITAXON source list and scope reason exactly.
Ignored-inclusive report/history/curation filename searches found no
prior target report or target-specific history artifact before creation.

iModulonDB is not applicable to this taxonomic record, which asserts no
gene, expression module or mechanism. No paid research, outside contact,
GitHub mutation, generator run, status promotion or history event occurred.
