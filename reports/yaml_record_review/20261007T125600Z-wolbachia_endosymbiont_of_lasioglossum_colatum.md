# YAML Record Review: Wolbachia endosymbiont of Lasioglossum colatum

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_colatum.yaml`
- Started UTC: 2026-10-07T12:53:42Z
- Finished UTC: 2026-10-07T12:56:00Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035899`,
Wolbachia endosymbiont of Lasioglossum colatum. It denotes the bacterial
endosymbiont taxon, not the eukaryotic host. Its rank is `SPECIES`,
domain `BACTERIA`, grounding `EXACT`, and lifecycle `SEEDED`.
It has 11 lineage entries, genetic code 11, `strain_count: 0`, one
NCBITAXON name attestation, and one inline seed event. It contains no
synonyms, nomenclature, strain/genome objects, mappings, or causal graph.

The record is generated from maintained source inventories and scope
decisions. Review does not authorize direct curation of this YAML.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_colatum.yaml`: passed; no LinkML issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_colatum.yaml --out /private/tmp/wol-lcolatum-strict.tsv`: passed; one file, zero errors. The complete diagnostics TSV was header-only.
- Parsed-source comparisons confirmed identity, every ancestor label/rank/link, attestation values, scope reason, and inline event wording. These are bounded source checks, not the full-corpus reproduction validator.
- Read live NCBI Taxonomy EFetch/Datasets responses and both exact-taxid Nuccore metadata/feature/reference records.
- `just validate-products`: not applicable; no curated causal-graph groundings. Taxonomic IDs and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable; ignored-independent history-content and filename searches found no target artifact. Inline history was schema/strict validated and compared to source provenance.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite. This report is not corpus-wide acceptance evidence.

## Identity and Grounding

The [NCBI EFetch record](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035899&retmode=xml)
and [Datasets record](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035899)
confirm the active identifier, exact label, species rank, bacterial placement,
and parent `NCBITaxon:2640676` (unclassified Wolbachia). EFetch confirms
genetic code 11 and exposes no other names. The local root-first lineage
matches all pinned ancestor labels/ranks/links; Datasets includes root and
EFetch supplies the remaining labeled ancestors.

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222198` agrees
with the YAML, including empty synonym columns, blank `retired_into`,
and the 2026-09-13 snapshot. The unique path index is
`data/taxa/PATHS.tsv:14697`; the explicit seed-scope decision is
`curation/seed_scope.tsv:322458`. The native scientific-name row was
read in full at `data/catalog/ncbi_names-0005.jsonl.gz:31702`.
No target child, type-material row, merge row, or dropped-inventory row
was found in the corresponding parsed local inventories.

The host name is part of the source bacterial label. It is not a reason
to ground this record to the host, another Lasioglossum-associated
Wolbachia taxon, or Wolbachia pipientis.

## Evidence

- The NCBITAXON attestation is exactly one `NAME` assertion for the record ID and label, not a count of specimens or sequences.
- Exact-target scans of `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, and `bactotraits_taxa.tsv` under `data/raw/` found no applicable rows. With no children in the backbone, the zero inventoried BacDive count is consistent.
- Inline history retains the correct `seed_from_sources` / `SEEDED_FROM_SOURCES` event and source/scope wording. Its `2026-09-13T17:54:04Z` timestamp agrees with the latest extraction timestamp among the raw, ATB, and StrainInfo manifests.
- Exact Assembly search for `txid1035899[Organism:noexp]` returned zero, with NCBI's organism-phrase-not-found/no-items warning. This is a bounded index result, not universal proof of genome absence.
- The corresponding Nuccore query returned two UIDs, both retrieved. Full metadata, features, and references were inspected, excluding nucleotide/translation payloads.

| GenBank record | Length | Voucher | BOLD cross-reference | Annotated protein |
|---|---:|---|---|---|
| [JF902279.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902279.1) | 657 nt | `BIOUG<CAN>:LASNA065-08.w` | `ASEND091-09.COI-5P` | `AEG66987.1` |
| [JF902280.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902280.1) | 613 nt | `BIOUG<CAN>:LASNA066-08.w` | `ASEND092-09.COI-5P` | `AEG66988.1` |

Both are partial cytochrome oxidase subunit 1 (`COI`) genes with
`taxon:1035899`, translation table 11, and host Lasioglossum colatum.
They record Canada, Alberta, Cypress hill, coordinates 49.638 N 110.254 W,
collection date 13-Jun-2007, and collectors Cory Sheffield and Jason Gibbs.
Those are specimen-scoped submission assertions, not species-wide
distribution or phenotype evidence. Neither sequence is a genome assembly
or a documented cultured strain.

Both GenBank records retain an unpublished Smith bibliographic entry,
"Wolbachia and Barcoding Insects: Patterns, Potential and Problems",
and a 01-May-2011 direct submission. The similarly titled
[primary 2012 paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
whose methods were inspected in this continuing review session, explains
Wolbachia marker recovery from insect extracts and the `.w` label
convention. Exact accession-to-supplement/BOLD reconciliation was not
performed; do not silently turn these unpublished entries into
accession-verified published citations.

An additional search lead, the
[2017 Canadian bee barcoding study](https://www.cambridge.org/core/journals/canadian-entomologist/article/contribution-of-dna-barcoding-to-the-study-of-the-bees-hymenoptera-apoidea-of-canada-progress-to-date/816569B164437DB5BF07CAE95A1317DA),
lists L. colatum among hosts lacking compliant barcode index numbers and
discusses Wolbachia coamplification in other campaigns. The inspected
passage does not establish a genome, cultured strain, prevalence, or
mechanism for `NCBITaxon:1035899`. It is not sufficient to add such claims.

No DOI, PMID, sequence accession, direct quotation, or mechanistic
evidence claim is asserted by the YAML itself.

## Completeness

Complete enough for an NCBI-only generated identity record. Optional
synonym, LPSN/type-strain, GTDB, strain, genome, literature, phenotype,
and graph slots may remain empty. `strain_count: 0` means no
inventoried BacDive strains, not no infections or sequenced specimens.

Initial and expanded searches used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`. They included ignored, hidden, and
compressed data. The expanded search covered the taxon ID, label/slug,
both accessions, both protein IDs, vouchers, and BOLD IDs. Native
`SOURCE.json` metadata files were parsed separately in full, and
history filenames were checked independently.

Each search returned four candidate rows, all read in full: the backbone,
scope, native scientific name, and one unrelated genome-catalog row.
The latter, `data/catalog/ncbi_genbank-0040.jsonl.gz:11619`, is
`GCA_043824205.1`, Patescibacteria group bacterium,
`taxid: 2052139`, isolate `MEGAHIT-group-3.60`. It matched only
because its genome size is `1035899`. Its complete source row rules
out a target genome/strain link; no external authority lookup was needed
to adopt this rejected candidate, because it was not adopted.

No additional applicable culture, genome link, attestation, or standalone
history was found in these bounded local sources. This is not a claim of
absence from every external database or publication.

iModulonDB was not applicable: the record asserts no gene, regulator,
strain-specific expression dataset, module, or transcriptomic mechanism.
The optional COI leads do not establish any such dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record's identity, lineage, source units, zero BacDive
count, empty optional fields, and seeded audit state are consistent with
the inspected evidence.

## Recommended Edits

None required. Do not add marker specimens as strains, short sequences
as genomes, or general Wolbachia reproductive effects as taxon-specific
causal claims. Do not promote `SEEDED` or append a curation event
solely because this report exists.

Future corrections belong to the maintained NCBI/source inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`; scope changes
belong to `curation/seed_scope.tsv`. Any optional strain/genome
enrichment requires verified source records and explicit joins, not
shared host wording.

## Follow-up Checks

No corrective follow-up is required.

Before optional marker/literature enrichment, inspect exact supplement
rows and independent BOLD records to establish accession-to-specimen
provenance. A proposed genome must resolve at its assembly authority
and have a defensible strain link.

After a later authorized maintained-input change, rerun the corresponding
extraction/seeding workflow and documented schema, strict,
corpus-reproduction, provenance, and QC gates. Apply product/history
validators if those objects are introduced.

## Additional Notes

- Baseline: `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`.
- The complete YAML was reread unchanged before report creation.
- This review writes only this new timestamped report; no record, source, generated product, audit history, GitHub object, or worktree was modified.
- Eukaryota is already fully covered and remains outside the continuing queue.
