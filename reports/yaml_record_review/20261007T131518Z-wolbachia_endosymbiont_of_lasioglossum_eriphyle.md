# YAML Record Review: Wolbachia endosymbiont of Lasioglossum eriphyle

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_eriphyle.yaml`
- Started UTC: 2026-10-07T13:11:26Z
- Finished UTC: 2026-10-07T13:15:18Z
- Verdict: pass

## Target

Reviewed the entire generated `TaxonRecord` for `NCBITaxon:1035904`,
Wolbachia endosymbiont of Lasioglossum eriphyle. This is a bacterial
species-rank node, not the eukaryotic host. It carries `BACTERIA`,
`EXACT` grounding, `SEEDED` lifecycle, 11 lineage entries, genetic
code 11, zero inventoried BacDive strains, one NCBITAXON name
attestation, and one inline seed event.

It asserts no synonym, nomenclature, mapping, strain/genome, literature,
phenotype, or graph objects. Generated YAML is read-only in this review;
future corrections belong to maintained source inputs and transforms.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_eriphyle.yaml`: passed; no LinkML issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_eriphyle.yaml --out /private/tmp/wol-leriphyle-strict.tsv`: passed; one file, zero errors. The complete header-only diagnostics TSV was read.
- Parsed-source comparisons passed for identity, all ancestor labels/ranks/links, empty synonym columns, attestation, unique path/scope rows, and seed-event wording. These bounded comparisons are not substitutes for the documented corpus reproduction gate.
- Live NCBI EFetch/Datasets and the sole exact-taxid Nuccore record were inspected.
- `just validate-products`: not applicable; no curated graph grounding/label pairs are present. Taxonomic identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent history-content and filename searches found no target artifact. Inline history passed schema/strict validation and provenance comparison.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, or the test suite. This report does not establish corpus-wide acceptance.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035904&retmode=xml)
and [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035904)
confirm active ID 1035904, exact label, species rank, bacterial placement,
and parent `NCBITaxon:2640676`, unclassified Wolbachia. EFetch
confirms genetic code 11 and supplies no other names. Datasets includes
root; EFetch provides the remaining labeled ancestors. All 11 local
ancestor labels/ranks/links agree with the pinned backbone and current
authority.

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222203`
matches the YAML, including empty synonym columns, blank
`retired_into`, and snapshot date 2026-09-13. The unique index row
is `data/taxa/PATHS.tsv:14702`; the explicit scope decision is
`curation/seed_scope.tsv:322463`. The complete native scientific-name
row was read at `data/catalog/ncbi_names-0005.jsonl.gz:31708`.

No child, type-material, merge, or dropped-inventory row for this target
was found in the respective parsed sources. Shared host-genus wording
does not establish synonymy or equivalence with another Wolbachia node.

## Evidence

- The NCBITAXON attestation correctly records one `NAME` assertion for this exact ID and label at the pinned snapshot, not a count of specimens or sequence submissions.
- Exact-target scans of the seven raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories found no applicable rows. With no descendants in the backbone, the zero inventoried BacDive count is consistent.
- The inline `seed_from_sources` / `SEEDED_FROM_SOURCES` event matches the source/scope wording. Its `2026-09-13T17:54:04Z` timestamp agrees with the latest extraction time among the raw, ATB, and StrainInfo manifests read in this review.
- Exact Assembly search for `txid1035904[Organism:noexp]` returned zero with NCBI's organism-phrase-not-found/no-items warning. This is a bounded index observation, not proof of global genome absence.
- The corresponding Nuccore query returned one UID, 334191854. Its full metadata, features, and references were read; nucleotide/translation payloads were omitted.

[JF902286.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902286.1) is a
617-nt partial cytochrome oxidase subunit 1 (`COI`) gene carrying
`taxon:1035904`, code 11, host Lasioglossum eriphyle, and annotated
protein `AEG66994.1`. Its specimen voucher is
`BIOUG<CAN>:LASNA719-08.w`; the BOLD cross-reference is
`ASEND079-09.COI-5P`. Source metadata give Canada and identifier
Alex Smith, but no collection date. These are specimen-scoped marker
metadata, not a cultured-strain deposit, genome assembly, or taxon-wide
distribution claim.

The entry retains the unpublished Smith citation
"Wolbachia and Barcoding Insects: Patterns, Potential and Problems"
and a 01-May-2011 direct submission. The
[similarly titled 2012 primary paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514)
describes marker recovery from insect extracts and the `.w`
sample-label convention; its methods were inspected. Exact Table S2
and independent BOLD accession reconciliation were not performed,
so the unpublished entry was not silently upgraded to an
accession-verified published citation. No reproductive effect,
prevalence, supergroup, or mechanism is inferred.

The YAML itself asserts no literature citation, DOI, PMID, sequence
accession, quotation, or biological effect.

## Completeness

Complete enough for this NCBI-only generated identity record. Empty
synonym, LPSN/type-strain, GTDB, strain, genome, literature, phenotype,
and graph slots are not defects without supported source objects.
`strain_count: 0` counts inventoried BacDive strains, not infections,
specimens, or marker submissions.

Initial and expanded searches used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`. Ignored, hidden, and compressed
content was included. The expanded pattern covered the taxon ID,
label/slug, accession, protein, voucher, and BOLD ID.

Both searches returned the same three rows: backbone, scope, and
scientific name. All were read in full. Five native `SOURCE.json`
files were separately parsed completely, and history filenames were
checked independently. No additional applicable source assertion,
culture deposit, strain-genome link, or standalone history artifact
was found in these bounded local sources. This is not a claim of
absence from all external databases or publications.

iModulonDB is not applicable: the record contains no gene, regulator,
expression module, strain-specific transcriptomic dataset, or mechanism.
The optional COI marker does not establish such a dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source units, zero BacDive count,
optional-field omissions, and seeded provenance agree with inspected
evidence.

## Recommended Edits

None required. Keep generated YAML unchanged and retain
`mapping_status: SEEDED`. Do not create a status promotion or
history event solely because this read-only report exists.

Future corrections belong to maintained NCBI/source inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope decisions belong in `curation/seed_scope.tsv`. Optional
strain/genome enrichment requires explicit authoritative links,
not shared host wording, locality, or a marker-voucher label.

## Follow-up Checks

No corrective follow-up is required.

Before optional marker/literature enrichment, reconcile the exact
accession/voucher with primary Table S2 and independent BOLD records.
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
