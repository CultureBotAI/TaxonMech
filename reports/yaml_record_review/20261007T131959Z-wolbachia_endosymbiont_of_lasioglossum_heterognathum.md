# YAML Record Review: Wolbachia endosymbiont of Lasioglossum heterognathum

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_heterognathum.yaml`
- Started UTC: 2026-10-07T13:17:23Z
- Finished UTC: 2026-10-07T13:19:59Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035905`,
Wolbachia endosymbiont of Lasioglossum heterognathum. It denotes a
bacterial species-rank node, not its eukaryotic host. Its identity is
`EXACT`, lifecycle `SEEDED`, domain `BACTERIA`, genetic code 11,
with 11 ancestors, zero inventoried BacDive strains, one NCBITAXON
name attestation, and one inline seed event.

There are no synonym, nomenclature, mapping, strain/genome, literature,
phenotype, or graph objects. Generated YAML remains read-only; future
corrections belong to maintained inputs or transforms.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_heterognathum.yaml`: passed, no LinkML issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_heterognathum.yaml --out /private/tmp/wol-lheterognathum-strict.tsv`: passed, one file and zero errors. The complete header-only diagnostics TSV was read.
- Parsed-source comparisons passed for identity, all ancestor labels/ranks/links, synonym columns, source attestation, unique path/scope rows, and seed wording. These are bounded source checks, not corpus-reproduction validation.
- Live NCBI EFetch/Datasets and the sole exact-taxid Nuccore record were inspected.
- `just validate-products`: not applicable; no curated graph grounding/label pairs. Taxonomic identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target history artifact. Inline history passed schema/strict validation and source comparison.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, or the test suite. No corpus-wide acceptance claim is made.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035905&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035905)
confirm the active ID, exact label, species rank, and bacterial
placement. Parent `NCBITaxon:2640676` is unclassified Wolbachia;
code 11 matches. EFetch supplies no other names. All 11 local
ancestor IDs, labels, ranks, and links agree with the pinned backbone;
Datasets includes root and EFetch supplies the remaining labeled chain.

The complete source row at `data/raw/ncbitaxon_taxa.tsv:222204`
has the same identity, empty synonym columns, blank `retired_into`,
and snapshot 2026-09-13. Unique rows at `data/taxa/PATHS.tsv:14703`
and `curation/seed_scope.tsv:322464` confirm the slug and scope
reason. The complete scientific-name row was inspected at
`data/catalog/ncbi_names-0005.jsonl.gz:31709`.

Parsed backbone/status sources contain no child, type-material,
merged-ID, or dropped row for the target. Host-genus similarity
does not establish equivalence with other Wolbachia records.

## Evidence

- The NCBITAXON attestation is exactly one `NAME` assertion for this ID and label at the pinned snapshot, not one specimen, strain, or sequence.
- Exact-target scans of raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories found no applicable rows. With no descendants in the backbone, zero inventoried BacDive strains is consistent.
- The seed event's source/scope wording matches the parsed inventories. Its `2026-09-13T17:54:04Z` timestamp is the latest extraction time among the raw, ATB, and StrainInfo manifests inspected.
- Exact Assembly search `txid1035905[Organism:noexp]` returned zero with an organism-phrase-not-found/no-items warning. This is a bounded index result, not proof that no genome exists anywhere.
- Exact Nuccore search returned UID 334191856. All metadata, features, and references were inspected; sequence/translation payloads were omitted.

[JF902287.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902287.1) is a
642-nt partial cytochrome oxidase subunit 1 (`COI`) marker. It
explicitly names this host and `taxon:1035905`, uses code 11,
and annotates protein `AEG66995.1`. The specimen voucher is
`BIOUG<CAN>:LASNA044-08.w`, BOLD cross-reference
`ASEND106-09.COI-5P`, geographic field USA, and identifier
Alex Smith. No collection date is supplied. These metadata do not
establish a cultured deposit or an assembly, and the locality is
specimen-scoped rather than a taxon-wide distribution assertion.

The sequence retains an unpublished Smith citation,
"Wolbachia and Barcoding Insects: Patterns, Potential and Problems",
and a 01-May-2011 direct submission. The inspected methods of the
[similarly titled 2012 primary paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514)
describe COI recovery from insect extracts and the `.w` sample
suffix. Exact Table S2 and independent BOLD reconciliation were not
performed. The sequence citation is not silently promoted to an
accession-verified published citation. No prevalence, reproductive
effect, supergroup, or mechanism is inferred.

The YAML asserts no citation, DOI, PMID, sequence accession, quotation,
or biological effect.

## Completeness

Complete enough for this generated NCBI-only identity record. Empty
optional synonym, nomenclature, mapping, strain, genome, literature,
and graph fields are not defects without applicable supported objects.
`strain_count: 0` counts inventoried BacDive strains, not infections,
specimens, or marker sequences.

Initial and expanded searches used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`. Ignored, hidden, and compressed
content was included. The expanded pattern covered taxon ID,
label/slug, accession, protein, voucher, and BOLD ID.

Both searches returned four rows, all read in full. Three are the
target backbone, scope, and name rows. The fourth,
`data/catalog/ncbi_genbank-0066.jsonl.gz:47851`, describes
`GCA_984251885.1`, Chloroflexota bacterium, taxid 2026724,
isolate `TARA_SAMEA2623463_MAG_00000193`. The matching number
1035905 occurs in `genome_size`, not `taxid` or
`species_taxid`; it supplies no evidence for this Wolbachia record.

Five native `SOURCE.json` files were separately parsed completely;
history filenames were searched independently. No additional
applicable source assertion, culture deposit, strain-genome link,
or standalone history artifact was found in these bounded local
sources. No claim of global external absence is made.

iModulonDB is not applicable: this identity record asserts no gene,
regulator, expression module, transcriptomic dataset, or mechanism.
The optional COI marker does not establish a dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source units, zero BacDive count,
optional omissions, and seed provenance agree with inspected sources.

## Recommended Edits

None required. Keep generated YAML unchanged and retain
`mapping_status: SEEDED`. A read-only review does not authorize
a lifecycle promotion or history event.

Future source corrections belong to maintained inventories and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope decisions belong in `curation/seed_scope.tsv`. Optional
strain/genome enrichment requires explicit authoritative links,
not a shared host name, voucher label, or coincidental number.

## Follow-up Checks

No corrective follow-up is required.

Before optional marker/literature enrichment, reconcile the exact
accession/voucher against primary Table S2 and independent BOLD
metadata. Verify any proposed assembly at its authority and establish
a defensible strain link before adding a genome object.

After any later authorized maintained-input correction, rerun the
appropriate extraction/seeding workflow and documented schema,
strict, corpus-reproduction, provenance, and QC gates. Validate
products or history if those objects are introduced.

## Additional Notes

- Baseline: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`.
- The entire YAML was reread byte-identical before writing this report.
- Only this new report is created; no YAML, source, generated product, audit event, GitHub object, branch, or worktree is changed.
- Eukaryota is already fully covered and was not re-reviewed.
