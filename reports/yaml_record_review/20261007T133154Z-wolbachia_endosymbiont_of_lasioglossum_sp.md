# YAML Record Review: Wolbachia endosymbiont of Lasioglossum sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_sp.yaml`
- Started UTC: 2026-10-07T13:29:23Z
- Finished UTC: 2026-10-07T13:31:54Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035909`,
Wolbachia endosymbiont of Lasioglossum sp. It denotes a bacterial
species-rank NCBI node, not the host genus or an aggregate of all
Lasioglossum-associated Wolbachia. The record carries `BACTERIA`,
`EXACT` grounding, `SEEDED` lifecycle, 11 ancestors, code 11,
one exact synonym, zero inventoried BacDive strains, one NCBITAXON
name attestation, and one inline seed event.

It asserts no nomenclature, mapping, strain/genome, literature,
phenotype, or graph objects. Generated YAML is read-only in this
review; maintained inputs and transforms own future corrections.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_sp.yaml`: passed, no LinkML issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_sp.yaml --out /private/tmp/wol-lsp-strict.tsv`: passed, one file and zero errors. The complete header-only diagnostics TSV was read.
- Parsed-source comparisons passed for identity, all ancestor labels/ranks/links, source attestation, unique path/scope rows, and seed wording. The synonym was compared to the complete native name row, pinned backbone, live authority, and inspected transformation rule. These bounded comparisons are not corpus-reproduction validation.
- Live NCBI EFetch/Datasets and all three exact-taxid Nuccore records were inspected.
- `just validate-products`: not applicable; no curated graph grounding/label pairs. Taxonomic identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema/strict validation and provenance comparison.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, or the test suite. This is not corpus-wide acceptance evidence.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035909&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035909)
confirm the active ID, exact label, species rank, bacterial placement,
and parent `NCBITaxon:2640676`, unclassified Wolbachia. Code 11
matches. Datasets includes root and EFetch provides the remaining
labeled ancestors; all 11 local ancestor labels/ranks/links match the
pinned backbone and current authority.

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222208`
matches identity and snapshot 2026-09-13, with blank `retired_into`.
The sole exact synonym is "Wolbachia endosymbiont of Lasioglossum";
related/broad synonym columns are empty. EFetch lists that same
synonym. Native rows at `data/catalog/ncbi_names-0005.jsonl.gz:31713`
and line 31714 respectively contain the scientific name and the
NCBI name class `synonym`, both attached to this exact taxon ID.

The inspected rule in `src/taxonmech/ncbi_taxdump.py:91` maps
NCBI `synonym` and `equivalent name` classes to
`EXACT_SYNONYM`; `src/taxonmech/seed.py:381` preserves that
scope and NCBITaxon provenance. The YAML synonym is therefore
supported, not an inferred equivalence from host wording.

Unique rows `data/taxa/PATHS.tsv:14707` and
`curation/seed_scope.tsv:322468` confirm the slug and scope.
No child, type-material, merged-ID, or dropped row for this target
was found in the respective parsed sources. Generic host wording
does not turn this bacterial species-rank node into a higher-rank
record or establish a relationship to another host-associated taxon.

## Evidence

- The NCBITAXON attestation correctly records one `NAME` assertion for the exact ID and label, not the number of synonyms, specimens, or sequence submissions.
- Exact-target scans of the seven raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories found no applicable rows. With no descendants in the backbone, zero inventoried BacDive strains is consistent.
- The inline `seed_from_sources` / `SEEDED_FROM_SOURCES` event matches source/scope wording. Its `2026-09-13T17:54:04Z` timestamp agrees with the latest extraction time in the raw, ATB, and StrainInfo manifests inspected.
- Exact Assembly search `txid1035909[Organism:noexp]` returned zero with NCBI's organism-phrase-not-found/no-items warning. This is a bounded index observation, not proof of global genome absence.
- Exact Nuccore search returned three UIDs, 334191868, 334191860, and 334191858; all were retrieved. Full metadata, features, and references were inspected, excluding nucleotide/translation payloads.

| GenBank record | Specimen voucher | BOLD cross-reference | Annotated protein | Source locality |
|---|---|---|---|---|
| [JF902288.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902288.1) | `BIOUG<CAN>:LASNA751-08.w` | `ASEND080-09.COI-5P` | `AEG66996.1` | USA |
| [JF902289.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902289.1) | `BIOUG<CAN>:LASNA845-08.w` | `ASEND081-09.COI-5P` | `AEG66997.1` | USA |
| [JF902293.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902293.1) | `BIOUG<CAN>:LASNA517-08.w` | `ASEND060-09.COI-5P` | `AEG67001.1` | Kenya: Mormodica |

All three are 657-nt partial cytochrome oxidase subunit 1 (`COI`)
markers with `taxon:1035909`, code 11, host Lasioglossum sp.,
and identifier Alex Smith. None supplies a collection date.
Distinct vouchers and localities do not establish cultured-strain
identities, assemblies, or taxon-wide distribution. Three marker
submissions do not contradict `strain_count: 0`.

All retain the unpublished Smith citation
"Wolbachia and Barcoding Insects: Patterns, Potential and Problems"
and a 01-May-2011 direct submission. The inspected methods of the
[similarly titled 2012 primary paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514)
describe COI recovery from insect extracts and the `.w` sample
suffix. Exact Table S2/BOLD reconciliation was not performed; these
entries are not silently upgraded to accession-verified published
citations. No prevalence, reproductive effect, supergroup, or
mechanism is inferred.

The YAML itself asserts no citation, DOI, PMID, sequence accession,
quotation, or biological effect.

## Completeness

Complete enough for this generated NCBI-only identity record. The
supported exact synonym is preserved. Empty optional nomenclature,
mapping, strain, genome, literature, and graph slots are not defects
without applicable source objects. `strain_count` counts inventoried
BacDive strains, not infections, specimens, or markers.

Initial and expanded searches used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`. Ignored, hidden, and compressed
content was included. The expanded pattern covered the exact taxon
ID, label/slug, synonym, all three accessions, proteins, vouchers,
and BOLD IDs.

Both searches returned the same four rows: backbone, scope,
scientific name, and synonym. All were read in full. Five native
`SOURCE.json` files were separately parsed completely, and history
filenames were independently checked. No additional applicable
source assertion, deposit, strain-genome link, or standalone history
artifact was found in these bounded local sources. No global
external absence is claimed.

iModulonDB is not applicable: the identity record contains no gene,
regulator, expression module, strain-specific transcriptomic dataset,
or mechanism. Optional COI markers do not establish such a dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, synonym scope, source units, zero
BacDive count, optional omissions, and seed provenance agree with
inspected evidence.

## Recommended Edits

None required. Keep generated YAML unchanged and retain
`mapping_status: SEEDED`. This read-only review does not authorize
a lifecycle promotion or history event.

Future source corrections belong to maintained inputs and
`src/taxonmech/ncbi_taxdump.py`/`src/taxonmech/extract.py`/
`src/taxonmech/seed.py`; scope decisions belong in
`curation/seed_scope.tsv`. Optional strain/genome enrichment
requires explicit authoritative links, not host wording, locality,
or marker-voucher labels.

## Follow-up Checks

No corrective follow-up is required.

Before optional marker/literature enrichment, reconcile exact
accessions/vouchers against primary Table S2 and independent BOLD
records. Verify proposed assemblies at their authorities and establish
defensible strain links before adding genome objects.

After a later authorized maintained-input correction, rerun the
appropriate extraction/seeding workflow and documented schema,
strict, corpus-reproduction, provenance, and QC gates. Apply product
or history validation if those objects are introduced.

## Additional Notes

- Baseline: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`.
- The complete YAML was reread byte-identical before writing this report.
- Only this new report is created; no YAML, source, generated product, audit event, GitHub object, branch, or worktree is changed.
- Eukaryota is already fully covered and was not re-reviewed.
