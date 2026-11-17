# YAML Record Review: Wolbachia endosymbiont of Halictidae sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_halictidae_sp.yaml`
- Started UTC: 2026-10-07T13:00:23Z
- Finished UTC: 2026-10-07T13:02:37Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035901`,
Wolbachia endosymbiont of Halictidae sp. The record represents an
NCBI species-rank bacterial node, not the eukaryotic host family
Halictidae or the separately identified Halictus-associated Wolbachia
node `NCBITaxon:1035900`.

It has `SPECIES` rank, `BACTERIA` domain, `EXACT` grounding,
`SEEDED` lifecycle, 11 lineage entries, one exact synonym,
genetic code 11, zero inventoried BacDive strains, one NCBITAXON
name attestation, and one inline seed event. It asserts no strain,
genome, nomenclature, mapping, literature-evidence, or causal-graph
objects. Future corrections belong to maintained inputs/transforms,
not direct edits to the generated YAML.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_halictidae_sp.yaml`: passed; no LinkML issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_halictidae_sp.yaml --out /private/tmp/wol-halictidae-strict.tsv`: passed; one file, zero errors. Read the complete header-only diagnostics TSV.
- Bounded parsed-source comparisons passed for identity, every ancestor label/rank/link, synonym source scope, source attestation, unique path/scope entries, and inline event wording. These are not substitutes for the documented full-corpus reproduction gate.
- Live NCBI Taxonomy EFetch/Datasets reads and all four exact-taxid Nuccore metadata/feature/reference reads succeeded.
- `just validate-products`: not applicable; no curated graph grounding/label pairs. Taxonomic identifiers were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent history-content and filename searches found no target artifact. The inline event was schema/strict validated and compared with source provenance.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, or the test suite. This review is not corpus-wide acceptance evidence.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035901&retmode=xml)
and [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035901)
confirm the active identifier, exact label, bacterial species rank,
and parent `NCBITaxon:2640676`, unclassified Wolbachia. EFetch
confirms genetic code 11. The local root-first lineage agrees with
the pinned backbone; Datasets includes root and EFetch provides the
remaining labeled ancestors.

The full source row at `data/raw/ncbitaxon_taxa.tsv:222200` agrees
with all seeded identity values, the synonym, blank `retired_into`,
and the 2026-09-13 snapshot. The unique index row is
`data/taxa/PATHS.tsv:14699`; the explicit scope decision is
`curation/seed_scope.tsv:322460`.

The synonym "Wolbachia endosymbiont of Halictidae" is explicitly
a `Synonym` in live EFetch and a `synonym` in the native name
row. Its `EXACT_SYNONYM` scope and `NCBITaxon` source are
correct. Read both complete native rows, scientific name and synonym,
at `data/catalog/ncbi_names-0005.jsonl.gz:31704` and 31705.
No broad or related synonym is asserted or required by these rows.

No child, type-material, merged-ID, or dropped-inventory entry for
the target was found in the corresponding parsed inventories.
Host-family wording does not make this bacterial node a higher-rank
record or establish equivalence to other host-associated Wolbachia taxa.

## Evidence

- The NCBITAXON attestation correctly represents one `NAME` assertion for this exact ID and label. Its synonym and four marker submissions do not multiply that inventory unit.
- Exact-target scans of the seven raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories found no applicable rows. With no children in the backbone, the zero inventoried BacDive count is consistent.
- The inline `seed_from_sources` / `SEEDED_FROM_SOURCES` event matches the source/scope wording. Its `2026-09-13T17:54:04Z` timestamp agrees with the latest extraction time among the raw, ATB, and StrainInfo manifests read during this review.
- Exact Assembly search for `txid1035901[Organism:noexp]` returned zero records, with NCBI's organism-phrase-not-found/no-items warning. This is a bounded index observation, not universal proof of genome absence.
- Exact Nuccore search returned four UIDs, all retrieved and read with full metadata, features, and references; nucleotide and translated-sequence payloads were omitted.

| GenBank record | Length | Specimen voucher | BOLD cross-reference | Annotated protein |
|---|---:|---|---|---|
| [JF902274.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902274.1) | 656 nt | `BIOUG<CAN>:DAIL680-06.w` | `ASEND109-09.COI-5P` | `AEG66982.1` |
| [JF902275.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902275.1) | 657 nt | `BIOUG<CAN>:LASNA018-08.w` | `ASEND101-09.COI-5P` | `AEG66983.1` |
| [JF902276.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902276.1) | 619 nt | `BIOUG<CAN>:LASNA024-08.w` | `ASEND103-09.COI-5P` | `AEG66984.1` |
| [JF902277.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902277.1) | 620 nt | `BIOUG<CAN>:LASNA043-08.w` | `ASEND105-09.COI-5P` | `AEG66985.1` |

All four are partial cytochrome oxidase subunit 1 (`COI`) genes,
with `taxon:1035901`, translation table 11, host Halictidae sp.,
and USA geographic metadata. Their inspected source features do not
supply a narrower locality, collection date, culture deposit, or
assembly accession. The voucher metadata should not be recast as
cultured-strain evidence, nor the short markers as genome objects.

Each carries a Smith unpublished bibliographic entry titled
"Wolbachia and Barcoding Insects: Patterns, Potential and Problems"
and a 01-May-2011 direct submission. The
[similarly titled primary 2012 paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514)
was inspected for methods: it describes marker recovery from insect
extracts, the `.w` labeling convention, and accession/host details
in Table S2. Exact accession-to-supplement and independent BOLD
reconciliation were not performed. The unpublished sequence citations
were not silently replaced with published ones.

These are specimen-level source assertions, not evidence for a
taxon-wide host range, geographic distribution, prevalence,
reproductive phenotype, supergroup assignment, or causal mechanism.
The YAML itself asserts no DOI, PMID, sequence citation, direct
quotation, or biological effect.

## Completeness

Complete enough for an NCBI-only generated identity record. Empty
nomenclature, type-strain, GTDB, strain, genome, literature, phenotype,
and graph slots are not defects without corresponding supported
evidence. `strain_count: 0` means no inventoried BacDive strains,
not no infected hosts or sequenced specimens.

Initial and expanded local searches used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`, including ignored, hidden, and
compressed content. The expanded search included the numeric ID,
label/synonym/slug, all four sequence accessions, annotated protein
IDs, vouchers, and BOLD IDs.

Each search returned the same four candidate rows: one backbone,
one scope, one scientific name, and one synonym. All four were read
in full. The five native `SOURCE.json` files were parsed separately
in full, and history filenames were checked independently.
No additional applicable culture deposit, strain-genome link, source
attestation, or standalone history artifact was found in these bounded
local surfaces. This does not assert absence from all external sources.

iModulonDB is not applicable: the reviewed record contains no gene,
regulator, expression module, strain-specific transcriptomic dataset,
or mechanistic assertion. Optional COI leads do not establish one.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, exact-synonym scope, source units,
zero BacDive count, optional-field omissions, and seeded audit state
agree with the inspected evidence.

## Recommended Edits

None required. Keep the generated YAML unchanged and retain
`mapping_status: SEEDED`. Do not add marker specimens as
cultured strains or infer genomes/biological effects from them.

Future corrections belong to maintained NCBI/source inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope decisions belong in `curation/seed_scope.tsv`. Any
strain/genome enrichment must first establish explicit, authoritative
source links and correct specimen scope.

## Follow-up Checks

No corrective follow-up is required.

Before optional literature or marker enrichment, reconcile exact
accessions and vouchers with primary Table S2 and independent BOLD
records. Verify any proposed genome at its assembly authority and
establish the strain link before creating a genome object.

After a later authorized maintained-input change, rerun the
corresponding extraction/seeding workflow and documented schema,
strict, corpus-reproduction, provenance, and QC gates. Apply graph
and history validators if those objects are introduced.

## Additional Notes

- Baseline: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`.
- The entire YAML was reread unchanged before this report was written.
- This review creates only this timestamped report; no record, source, generated product, audit event, GitHub object, branch, or worktree was modified.
- Eukaryota remains fully covered and outside this continuing review queue.
