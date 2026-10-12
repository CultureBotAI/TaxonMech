# YAML Record Review: Wolbachia endosymbiont of Lasioglossum discum

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_discum.yaml`
- Started UTC: 2026-10-07T13:04:56Z
- Finished UTC: 2026-10-07T13:07:13Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035902`.
It denotes Wolbachia endosymbiont of Lasioglossum discum, not the
eukaryotic host: `SPECIES`, `BACTERIA`, `EXACT` grounding,
`SEEDED` lifecycle. The record has 11 lineage entries, genetic
code 11, zero inventoried BacDive strains, one NCBITAXON name
attestation, and one inline seed event. No synonym, nomenclature,
mapping, strain/genome, literature, phenotype, or graph object is asserted.

Future fixes belong to maintained source inputs/transforms, not direct
edits to this generated YAML.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_discum.yaml`: passed; no LinkML issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_discum.yaml --out /private/tmp/wol-ldiscum-strict.tsv`: passed; one file, zero errors. Read the complete header-only diagnostics TSV.
- Bounded parsed-source comparisons passed for identity, all lineage labels/ranks/links, empty synonym columns, attestation, unique path/scope entries, and seed-event wording. These are not the full-corpus reproduction validator.
- Live NCBI EFetch/Datasets and the sole exact-taxid Nuccore record were inspected.
- `just validate-products`: not applicable; no curated graph grounding/label pairs. Taxonomic identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent history-content and filename searches found no target artifact. Inline history was schema/strict validated and compared to provenance.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite. This review does not establish corpus-wide acceptance.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035902&retmode=xml)
and [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035902)
agree on active ID 1035902, exact scientific name, bacterial species
rank, and parent `NCBITaxon:2640676`, unclassified Wolbachia.
EFetch confirms code 11 and supplies no other names. Datasets includes
root in its lineage; EFetch supplies the subsequent labeled ancestors.
All 11 local ancestor labels, ranks, and parent links match the pinned
backbone and current authority.

The complete backbone row is `data/raw/ncbitaxon_taxa.tsv:222201`;
it matches the YAML, including empty synonym columns, blank
`retired_into`, and the 2026-09-13 snapshot. The unique path row is
`data/taxa/PATHS.tsv:14700`; the explicit scope decision is
`curation/seed_scope.tsv:322461`. The complete native scientific-name
row was read at `data/catalog/ncbi_names-0005.jsonl.gz:31706`.

No target child, type-material, merge, or dropped-inventory row was
found in the respective parsed sources. Shared host-genus wording
does not identify this node with another Lasioglossum-associated
Wolbachia node.

## Evidence

- The NCBITAXON attestation correctly records one `NAME` assertion for this exact ID and label, with snapshot date 2026-09-13.
- Exact-target scans of the seven raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories found no applicable rows. With no backbone descendants, the zero inventoried BacDive count is consistent.
- The inline `seed_from_sources` / `SEEDED_FROM_SOURCES` event matches the source/scope wording. Its `2026-09-13T17:54:04Z` timestamp is the latest extraction time across the raw, ATB, and StrainInfo manifests read during this review.
- Exact Assembly search for `txid1035902[Organism:noexp]` returned zero with NCBI's organism-phrase-not-found/no-items warning. This is a bounded index observation, not universal genome-absence evidence.
- The corresponding Nuccore search returned one UID, 334191844. Read its full metadata, features, and references, excluding nucleotide/translation payloads.

[JF902281.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902281.1) is a
613-nt partial cytochrome oxidase subunit 1 (`COI`) gene, annotated
protein `AEG66989.1`, translation table 11. Source features give
`taxon:1035902`, host Lasioglossum discum, voucher
`BIOUG<CAN>:LASNA525-08.w`, BOLD cross-reference
`ASEND063-09.COI-5P`, Kyrgyzstan, collection date 27-Jun-1999,
and collector J.G. Rozen. This is a specimen-scoped marker submission,
not a genome assembly, culture deposit, or species-wide distribution claim.

The sequence retains an unpublished Smith entry titled
"Wolbachia and Barcoding Insects: Patterns, Potential and Problems"
and a 01-May-2011 direct submission. The
[similarly titled 2012 primary paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
whose methods were inspected in this continuing review session,
describes Wolbachia marker recovery from insect extracts and the
`.w` sample-label convention. Exact accession-to-Table-S2 and
independent BOLD reconciliation were not performed. Do not silently
replace the unpublished entry with an accession-verified published
citation or infer a reproductive phenotype, prevalence, supergroup,
or causal mechanism.

The YAML itself asserts no DOI, PMID, sequence citation, quotation,
or mechanistic evidence claim.

## Completeness

Complete enough for this generated NCBI-only identity record. Optional
synonym, LPSN/type-strain, GTDB, strain, genome, literature, phenotype,
and graph slots may remain empty. `strain_count: 0` is a count of
inventoried BacDive strains, not infections or sequenced specimens.

Initial and expanded searches used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`. Ignored, hidden, and compressed
content was included. The expanded pattern covered the numeric ID,
label/slug, accession, protein ID, voucher, and BOLD ID.
Both searches returned the same six candidate rows; all were read
in full. Five native `SOURCE.json` metadata files were separately
parsed completely, and history filenames were checked independently.

Three hits support this target: backbone, scope, and scientific name.
Three others at `data/catalog/ncbi_genbank-0003.jsonl.gz:32547`,
32555, and 32578 are Listeria monocytogenes, taxon 1639:
`GCA_004632935.1`, `GCA_004633095.1`, and
`GCA_004633555.1`, respectively. They matched strain strings
`FDA1035902-026-001`, `FDA1035902-027-002`, and
`FDA1035902-029-008`, not the target taxon. Their complete rows
rule out a target strain/genome join; none was adopted as target evidence.

No additional applicable source assertion, culture deposit,
strain-genome link, or standalone history artifact was found in the
bounded local sources. This is not an assertion of absence from all
external databases or publications.

iModulonDB is not applicable: no gene, regulator, expression module,
strain-specific transcriptomic dataset, or mechanism is asserted
by the reviewed record. The optional COI lead does not establish one.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source units, optional-field omissions,
zero BacDive count, and seeded provenance agree with inspected evidence.

## Recommended Edits

None required. Keep the generated record unchanged and retain
`mapping_status: SEEDED`; do not create history or a status promotion
solely because this read-only report exists.

Future identity/provenance corrections belong to maintained NCBI/source
inputs and `src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope decisions belong in `curation/seed_scope.tsv`. Optional
strain/genome enrichment requires exact authoritative links, not a
marker voucher or coincident digits in another organism's strain name.

## Follow-up Checks

No corrective follow-up is required.

Before optional marker/literature enrichment, reconcile the exact
accession and voucher with the primary supplement and independent BOLD
record. Verify any proposed assembly at its authority and establish
an explicit strain link before adding a genome object.

After a later authorized maintained-input correction, rerun the
appropriate extraction/seeding workflow and documented schema,
strict, corpus-reproduction, provenance, and QC gates. Apply product
or history validation if those objects are introduced.

## Additional Notes

- Baseline: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`.
- The complete YAML was reread unchanged before report creation.
- This review creates only this report. No source, YAML, generated product, audit event, GitHub object, branch, or worktree was changed.
- Eukaryota is already fully covered and was not re-reviewed.
