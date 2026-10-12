# YAML Record Review: Wolbachia endosymbiont of Lasioglossum egregium

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_egregium.yaml`
- Started UTC: 2026-10-07T13:08:15Z
- Finished UTC: 2026-10-07T13:10:23Z
- Verdict: pass

## Target

Reviewed the complete generated `TaxonRecord` for `NCBITaxon:1035903`,
Wolbachia endosymbiont of Lasioglossum egregium. It denotes a bacterial
species-rank taxonomic node, not its eukaryotic host. The record carries
`BACTERIA`, `EXACT` grounding, `SEEDED` lifecycle, 11 lineage
entries, genetic code 11, zero inventoried BacDive strains, one
NCBITAXON name attestation, and one inline seed event.

It asserts no synonym, nomenclature, mapping, strain/genome, literature,
phenotype, or graph objects. Generated YAML is read-only in this review;
future fixes belong to maintained inputs and transforms.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_egregium.yaml`: passed; no LinkML issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_egregium.yaml --out /private/tmp/wol-legregium-strict.tsv`: passed; one file, zero errors. Read the complete header-only diagnostics TSV.
- Parsed-source comparisons passed for identity, all ancestor labels/ranks/links, empty synonym columns, attestation, unique path/scope rows, and seed-event wording. These bounded checks do not substitute for the documented corpus reproduction gate.
- Live NCBI EFetch/Datasets and all four exact-taxid Nuccore records were inspected.
- `just validate-products`: not applicable; there are no curated graph grounding/label pairs. Taxonomic identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent history-content and filename searches found no target artifact. Inline history was schema/strict validated and compared to provenance.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, or the test suite. This is not corpus-wide acceptance evidence.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035903&retmode=xml)
and [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035903)
confirm active ID 1035903, exact label, species rank, bacterial placement,
and parent `NCBITaxon:2640676`, unclassified Wolbachia. EFetch
confirms genetic code 11 and supplies no other names. Datasets includes
root; EFetch provides the remaining labeled ancestors. All 11 local
ancestor labels/ranks/links agree with the pinned backbone and current
authority.

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222202`
matches the YAML, including empty synonym columns, blank
`retired_into`, and snapshot date 2026-09-13. The unique index row
is `data/taxa/PATHS.tsv:14701`; the explicit scope decision is
`curation/seed_scope.tsv:322462`. The complete native scientific-name
row was read at `data/catalog/ncbi_names-0005.jsonl.gz:31707`.

No child, type-material, merge, or dropped-inventory row for this target
was found in the respective parsed sources. No synonym or taxonomic
equivalence with other Lasioglossum-associated Wolbachia is inferred
from shared host-genus wording.

## Evidence

- The NCBITAXON attestation correctly records one `NAME` assertion for this exact ID and label at the pinned snapshot, not a count of specimens or marker submissions.
- Exact-target scans of the seven raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories found no applicable rows. With no descendants in the backbone, the zero inventoried BacDive count is consistent.
- The inline `seed_from_sources` / `SEEDED_FROM_SOURCES` event matches the source/scope wording. Its `2026-09-13T17:54:04Z` timestamp agrees with the latest extraction time among the raw, ATB, and StrainInfo manifests read in this review.
- Exact Assembly search for `txid1035903[Organism:noexp]` returned zero, with NCBI's organism-phrase-not-found/no-items warning. This is a bounded index observation, not proof of global genome absence.
- The corresponding Nuccore query returned four UIDs, all retrieved. Full metadata, features, and references were inspected; nucleotide/translation payloads were omitted.

| GenBank record | Specimen voucher | BOLD cross-reference | Annotated protein |
|---|---|---|---|
| [JF902282.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902282.1) | `BIOUG<CAN>:LASNA067-08.w` | `ASEND093-09.COI-5P` | `AEG66990.1` |
| [JF902283.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902283.1) | `BIOUG<CAN>:LASNA068-08.w` | `ASEND094-09.COI-5P` | `AEG66991.1` |
| [JF902284.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902284.1) | `BIOUG<CAN>:LASNA069-08.w` | `ASEND095-09.COI-5P` | `AEG66992.1` |
| [JF902285.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902285.1) | `BIOUG<CAN>:LASNA073-08.w` | `ASEND097-09.COI-5P` | `AEG66993.1` |

All four are 657-nt partial cytochrome oxidase subunit 1 (`COI`)
genes with `taxon:1035903`, code 11, and host Lasioglossum egregium.
Their common source metadata give USA, Idaho, Blaine County,
43.379 N 113.722 W, collection date 27-May-2007, and collectors
Cory Sheffield and Jason Gibbs. The distinct voucher names do not
establish cultured strains, and the shared date/locality do not
establish strain identity. These are specimen-scoped marker submissions,
not genome assemblies or taxon-wide distribution claims.

All retain the unpublished Smith citation
"Wolbachia and Barcoding Insects: Patterns, Potential and Problems"
and a 01-May-2011 direct submission. The
[similarly titled 2012 primary paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
whose methods were inspected in this continuing review session,
describes marker recovery from insect extracts and the `.w`
sample-label convention. Exact Table S2/BOLD accession reconciliation
was not performed; the unpublished entries were not silently upgraded
to accession-verified published citations. No reproductive effect,
prevalence, supergroup, or mechanism is inferred.

The YAML itself asserts no literature citation, DOI, PMID, sequence
accession, quotation, or biological effect.

## Completeness

Complete enough for this NCBI-only generated identity record. Empty
synonym, LPSN/type-strain, GTDB, strain, genome, literature, phenotype,
and graph slots are not defects without supported source objects.
`strain_count: 0` counts inventoried BacDive strains, not infections,
specimens, or sequence submissions.

Initial and expanded searches used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`. Ignored, hidden, and compressed
content was included. The expanded pattern covered the taxon ID,
label/slug, all four accessions, proteins, vouchers, and BOLD IDs.

Both searches returned the same three rows: backbone, scope, and
scientific name. All three were read in full. Five native
`SOURCE.json` files were separately parsed completely, and history
filenames were checked independently. No additional applicable source
assertion, culture deposit, strain-genome link, or standalone history
artifact was found in these bounded local sources. This is not a
claim of absence from all external databases or publications.

iModulonDB is not applicable: the record contains no gene, regulator,
expression module, strain-specific transcriptomic dataset, or mechanism.
Optional COI markers do not establish such a dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source units, zero BacDive count,
optional-field omissions, and seeded provenance agree with the
inspected evidence.

## Recommended Edits

None required. Keep the generated YAML unchanged and retain
`mapping_status: SEEDED`. Do not create a status promotion or
history event solely because this read-only report exists.

Future corrections belong to maintained NCBI/source inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope decisions belong in `curation/seed_scope.tsv`. Optional
strain/genome enrichment requires explicit authoritative links, not
shared host wording, locality, or marker-voucher labels.

## Follow-up Checks

No corrective follow-up is required.

Before optional marker/literature enrichment, reconcile exact
accessions/vouchers with primary Table S2 and independent BOLD records.
Verify a proposed assembly at its authority and establish a defensible
strain link before creating a genome object.

After a later authorized maintained-input correction, rerun the
appropriate extraction/seeding workflow and documented schema,
strict, corpus-reproduction, provenance, and QC gates. Apply product
or history validation if those objects are introduced.

## Additional Notes

- Baseline: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`.
- The entire YAML was reread unchanged before writing this report.
- This review creates only this new report; no source, YAML, generated product, audit event, GitHub object, branch, or worktree was changed.
- Eukaryota is already fully covered and was not re-reviewed.
