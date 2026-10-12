# YAML Record Review: Bacillus sp. PKSW3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_pksw3.yaml`
- Started UTC: 2026-10-04T20:14:11Z
- Finished UTC: 2026-10-04T20:17:15Z
- Verdict: pass

## Target

Read the full generated `TaxonRecord` for `NCBITaxon:1033896`,
Bacillus sp. PKSW3: SPECIES, BACTERIA, parent `NCBITaxon:185979`,
`grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code 11.
It contains ten root-first ancestors, zero inventoried BacDive strains,
one NCBITAXON name attestation and one seed event. It asserts no
external identity, deposit, genome or mechanism.

This review concerns PKSW3 alone. No generated record, source input,
code, status or curation-history entry was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacillus_sp_pksw3.yaml`.
  Output: `No issues found`.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/bacillus_sp_pksw3.yaml`.
  One file scanned, zero files with errors and zero error rows. This is
  the implementation of `just validate-strict`, with the standard
  `reports/instance_validation_failures.tsv` diagnostic.
- Passed bounded source comparisons of identity, every ancestor label
  and rank, directly mapped inventories, filename lock, scope and seed
  wording. A complete backbone scan found no child taxa.
- Not run: `just verify-corpus`. It checks the full corpus;
  `--max-diffs` controls diagnostic output only. Bounded comparisons do
  not establish byte-level reproduction.
- Not applicable: `just validate-products`, because the record has no
  curator-added graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline event was checked.
  Full-corpus QC, provenance, rendering and test-suite gates were not run.

## Identity and Grounding

The complete backbone row `data/raw/ncbitaxon_taxa.tsv:221330`, native
name object `data/catalog/ncbi_names-0005.jsonl.gz:30670` and inspected
[NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033896&retmode=xml)
agree on identifier, label, species rank, parent, bacterial domain and
code 11. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033896)
confirms the ten lineage IDs, including root 1. Expanded live lineage
labels and ranks agree with the pinned backbone where supplied.

The direct parent is unclassified Bacillus beneath Bacillus,
Bacillaceae, Caryophanales, Bacilli, Bacillota and Bacillati. SPECIES
is NCBI's operational rank for this placeholder, not a nomenclatural
validity claim. PKSW3 is not interpreted as a culture accession.

The native name object contains only the scientific name and all
backbone synonym fields are empty. Complete exact-ID scans of
type-material, merged-ID and dropped-taxon tables returned no matching
rows. The live response supplies no successor or synonym requiring a
status change.

## Evidence

The sole attestation reproduces the exact NCBI identifier and label,
one NAME assertion and taxonomy snapshot `2026-09-13`. Complete directly
mapped BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits
inventory scans found no target rows. With no child taxa, zero is also
the complete descendant-inclusive BacDive count.

The exact-taxonomy nuccore query returned two entries. Both entries'
metadata, references and feature qualifiers were inspected:

- [JF768712.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768712.1&rettype=gb&retmode=xml)
  is a 1,446-base partial 16S rRNA sequence explicitly assigned to
  taxon 1033896 and strain PKSW3, from a uranium-rich site at
  Domiasiat, India.
- [JN034437.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JN034437.1&rettype=gb&retmode=xml)
  is a 747-base partial CDS assigned to the same taxon/strain. Its
  heavy-metal-transporting P-type ATPase annotation includes a note
  describing similarity to cadA-type transporters, translation table
  11 and protein accession AEI91707.1. Its references are an unpublished
  study title and direct submission, not a linked published PMID.

Neither entry supplies a registered deposit or genome assembly. The
partial-CDS annotation and similarity note are not proof of a complete
transporter, substrate specificity or causal resistance mechanism.
No gene or phenotype claim was added to the YAML from this context.

The marker links [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`, whose metadata and article body were
already inspected in the ongoing review session. A fresh
[Table 2 XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
confirmed PKSW3/JF768712 and the 1,446-base length. Headers, footnotes,
the full target row and expanded table cells identify Bacillus
isronensis as its closest 16S match at 99.59% similarity. This is
literature context, not an NCBI merger, formal species identification
or culture-deposit assertion. Supplementary PDF content was not
inspected.

The exact-taxonomy Assembly query returned zero entries with a
`phrasesnotfound` warning for `txid1033896[Organism:noexp]`. This is
not proof of global genome absence under every classification.
Taxonomy Browser HTML was inaccessible, but direct NCBI APIs succeeded.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. Taxon, name, slug and PKSW3
spelling variants produced four matching lines, all inspected. The
matching native NCBI name object was read in full.

Three relevant matches were the backbone, scope and scientific name.
AllTheBacteria sample `SAMEA1033896` is Streptococcus pneumoniae, a
numeric collision rather than target evidence. A separate ignored-
inclusive search for JF768712, JN034437 and AEI91707 across the same
roots completed with zero matches.

No eligible deposit or strain-genome assertion for PKSW3 was found
within that searched scope. Zero inventoried BacDive strains is not
absence of a biological isolate. The two partial nucleotide sequences
are not missing genome identifiers. Empty optional nomenclature,
mappings, definition, record-level evidence and causal-graph fields
are appropriate for this source-attested seeded taxon.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected evidence scope. Identity, lineage,
attestation, strain count, status and inline provenance are supported.
Partial sequences and closest-match literature are not inflated into
genome, mechanism or formal species-identity claims.

## Recommended Edits

None. Preserve the generated record. Future evidence-backed source or
identity corrections belong in the maintained inventory pipeline and,
when needed, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`.
Scope changes belong in `curation/seed_scope.tsv`; no manual patch or
status promotion is justified here.

## Follow-up Checks

On a source refresh, recheck the exact taxon, PKSW3 and both nucleotide
accessions for explicit deposit or primary genome evidence. Preserve
marker/partial-CDS types and do not transfer results from other study
isolates. Rerun focused validators after an authorized change and the
full `just verify-corpus` gate after regeneration. No unresolved blocker
prevents the present verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13786` locks the slug.
`curation/seed_scope.tsv:321660` supplies the September 13, 2026 scope
addition and one-source reason. The event at `2026-09-13T17:54:04Z`
reproduces the NCBITAXON source list and scope reason exactly. This
review does not promote SEEDED to REVIEWED or append an event.

Ignored-inclusive report/history/curation filename searches found no
earlier target report or target-specific history artifact before this
report was created. iModulonDB is not applicable to this taxonomic
record; the incidental partial CDS was inspected as source context,
not added as a gene or expression-module claim. No paid research,
outside contact, GitHub mutation or generator run occurred.
