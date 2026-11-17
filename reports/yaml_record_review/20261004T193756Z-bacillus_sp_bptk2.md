# YAML Record Review: Bacillus sp. BPTK2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_bptk2.yaml`
- Started UTC: 2026-10-04T19:36:20Z
- Finished UTC: 2026-10-04T19:37:56Z
- Verdict: pass

## Target

Reviewed the entire generated `TaxonRecord` for `NCBITaxon:1033847`,
Bacillus sp. BPTK2. It has SPECIES rank, BACTERIA domain, parent
`NCBITaxon:185979`, ten lineage entries, `grounding_status: EXACT`,
`mapping_status: SEEDED`, genetic code 11, `strain_count: 0`, one NCBITAXON
NAME attestation and one seed event. It contains no other source mapping,
nomenclature, synonym, strain, genome, literature or graph assertion.

Exactly this target was reviewed. All seeded fields remain read-only, and
this review neither changes the record nor promotes its lifecycle status.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacillus_sp_bptk2.yaml`.
  Output: `No issues found`.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/bacillus_sp_bptk2.yaml`.
  One file scanned, zero files with errors and zero error rows. This is the
  implementation used by `just validate-strict`; its standard diagnostic
  output is `reports/instance_validation_failures.tsv`.
- Passed bounded structured comparisons of identity, code, the complete
  root-first parent chain, source attestation, filename lock, scope and
  inline seed-event wording. Complete backbone and direct inventory scans
  found no children and no additional source row for this taxon.
- Not run: `just verify-corpus`. It is a full-corpus reproduction gate;
  `--max-diffs` limits diagnostics rather than review scope. No invented
  focused reproduction validator or byte-identity claim replaces it here.
- Not applicable: `just validate-products`, because the record contains no
  curator-added causal-graph nodes. NCBI identity and lineage were checked
  directly with source APIs.
- Not run: `just validate-history`. Ignored-inclusive searches found no
  target-specific history artifact, and no history entry is created by this
  read-only review. The inline seed event was checked. Full-corpus QC,
  provenance, rendering and test-suite gates were not run.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:221318` matches the
YAML's identifier, label, rank, parent and code. Every lineage entry matches
the pinned chain, including Caryophanales, Bacillaceae, Bacillus and the
unranked direct parent, `unclassified Bacillus (in: firmicutes)`.

The live [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033847&retmode=xml)
confirms species rank, parent 185979, bacterial division, code 11 and the
same named ancestor chain. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033847)
confirms all ten ancestor IDs including root. The complete native name
object at `data/catalog/ncbi_names-0005.jsonl.gz:30654` records the same
scientific name and no alternative identity. The Taxonomy browser HTML
request was inaccessible; these conclusions rely on the inspected API
responses, not on an unviewed web page.

The strain-like suffix and informal `sp.` label do not justify changing
the NCBI taxon's explicit SPECIES rank to STRAIN. Likewise, the unranked
parent does not make this species-rank record out of scope. EXACT describes
grounding to this source concept, not an assertion that BPTK2 has a validly
published species name under the ICNP. No named Bacillus species is inferred
from the label or marker sequence.

Complete exact-ID scans of `data/raw/ncbi_type_material.tsv`,
`data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no row for
this taxon. No type-material or replacement claim should be added on that
basis.

## Evidence

The sole source attestation is supported at its stated scope:

| Assertion | Inspected evidence |
| --- | --- |
| NCBITAXON, source ID `NCBITaxon:1033847`, label Bacillus sp. BPTK2 | Backbone row 221318, native scientific-name object and both live NCBI taxonomy responses agree. |
| One NAME | The native name object records this scientific name. This is not a count of genomes, deposits, phenotypes or experiments. |
| Snapshot note `2026-09-13` | The backbone row's `taxonomy_snapshot` has this date. |
| Zero BacDive strains | The complete direct BacDive inventory scan found no row; the full backbone scan found no descendants from which a strain could be gathered. |
| Seed event and scope | `data/taxa/PATHS.tsv:13773` fixes the identifier-to-slug pair; `curation/seed_scope.tsv:321649` gives the one-source scope reason reproduced in the event. |

The inline timestamp `2026-09-13T17:54:04Z` is consistent with the newest
manifest used by the seeder. Inspected timestamps are raw
`2026-09-13T17:50:44Z`, StrainInfo `2026-09-13T17:29:00Z`, and
AllTheBacteria `2026-09-13T17:54:04Z`. Their presence in the standard seed
wording does not claim that this taxon has an ATB or StrainInfo association.

A bounded live sequence check provides independent identity context:

- Exact [NCBI nucleotide search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1033847%5BOrganism%3Anoexp%5D&retmode=json)
  returned one result. Its complete non-sequence GenBank metadata was read;
  the actual DNA string was not used or analyzed.
- [JF749811.1](https://www.ncbi.nlm.nih.gov/nuccore/JF749811.1) is a
  1,410-base partial 16S rRNA gene sequence. The source feature explicitly
  names Bacillus sp. BPTK2, strain BPTK2 and `taxon:1033847`.
  It contains a direct-submission reference and an isolation-source
  qualifier. Neither constitutes a new taxon-wide phenotype or a
  culture-collection deposit.
- The exact [NCBI Assembly search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=assembly&term=txid1033847%5BOrganism%3Anoexp%5D&retmode=json)
  returned zero results with a phrase-not-found warning. This only describes
  that exact-index query; it does not prove no differently classified or
  unsubmitted genome could exist.

The marker corroborates the source identity but is not a genome assembly,
not a type designation and not a missing required strain-genome link. Its
source `strain` qualifier does not override the Taxonomy rank. No literature
quotation, mechanism or phenotype is asserted in the YAML, so none was
invented for this review.

## Completeness

Ignored-inclusive, compressed-content searches used
`rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`,
`data/atb`, `curation` and `history`, excluding only `SOURCE.json`
manifest files. The search for the taxon ID, BPTK2 label token and record
slug completed with four matching lines: scope, backbone, the native NCBI
name, and one unrelated numeric match. All matching contexts were inspected.

The unrelated ATB sample `SAMEA1033847` denotes Streptococcus pneumoniae;
its numeric suffix does not link it to NCBITaxon 1033847. A follow-up search
for `JF749811` over the same ignored-inclusive roots completed with zero
matching lines (`rg` exit 1, a normal no-match result). This is a bounded
local-source absence, not a claim that the live accession is unavailable.

Complete direct inventory scans found no BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits row for this taxon. The native-source
searches found no eligible culture-deposit, StrainInfo sequence or genome
crosswalk that would require adding a strain entry. Thus `strain_count: 0`
correctly describes classified BacDive records, not the number of strains
that have ever been isolated or studied.

An ignored-independent filename search over review reports, history and
curation found no pre-existing target-stem artifact. History content was
also covered by the identifier/name/slug search. The unique PATHS row and
fully read YAML establish the one target being reviewed.

No consequential missing required representation was established. Empty
optional nomenclature, taxonomy mappings, synonyms, strains, definition,
literature evidence, discussions, datasets and causal graphs are appropriate
for this NCBI-only seeded identity. A partial marker does not authorize
minting a BacDive strain or borrowing a named species' nomenclature.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed assertions. The sparse evidence base limits
biological conclusions but is accurately represented. Skipped full-corpus
gates and the bounded exact-Assembly search are not reported as proof of
global completeness or reproduction.

## Recommended Edits

None required on the inspected evidence. Keep the generated rank, lineage,
single-source provenance and SEEDED status. Do not hand-edit the YAML to
add a species assignment, genome, type designation or inferred culture
deposit.

If future primary evidence changes the source identity or supplies an
eligible strain link, the maintained source extraction and seeding paths
own the change: `scripts/extract_source_inventory.py`,
`src/taxonmech/seed.py`, and the relevant source-matching implementation
and tests. Taxonomic reassignment belongs to its source authority; the
scope file owns corpus inclusion. No such curation is authorized here.

## Follow-up Checks

- On a later source refresh, re-resolve the NCBI taxon, its explicit rank
  and complete lineage before changing classification.
- Require an explicit eligible deposit/source chain before adding a
  strain-genome association. Preserve marker sequences as marker evidence,
  outside genome counts.
- After authorized curation, run the documented single-record schema and
  strict validators, relevant focused tests and the full
  `just verify-corpus` reproduction gate. Validate history if that later
  curation actually creates a history artifact.

## Additional Notes

The review followed the local record-review skill, write boundaries and
field checklist. Only this new Markdown report was manually created;
taxon YAML, source inventories, code, pages, prior reports and history
were left unchanged. There was no paid research or GitHub mutation.
Eukaryota coverage was not changed.

iModulonDB is not applicable: the record has no gene, locus, regulator,
pathway, stress-response or transcriptomics claim requiring a structured
expression-module check. The externally inspected 16S marker does not
create one, and absence from that resource is not used as negative evidence.
