# YAML Record Review: Enterobacter sp. BIHB 1401

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterobacter_sp_bihb_1401.yaml`
- Started UTC: 2026-10-05T18:36:15Z
- Finished UTC: 2026-10-05T18:38:17Z
- Verdict: pass

## Target

The full 54-line generated `TaxonRecord` was read. It denotes
`NCBITaxon:1034634`, Enterobacter sp. BIHB 1401, with
`SPECIES` rank, `BACTERIA` domain, parent
`NCBITaxon:2608935`, genetic code 11, `EXACT` grounding,
`SEEDED` status, and `strain_count: 0`. It is not a genome
or culture-deposit record.

Owning inputs are `data/raw/ncbitaxon_taxa.tsv:221671` and
`curation/seed_scope.tsv:321982`.
`data/taxa/PATHS.tsv:14137` agrees in identifier and slug.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/enterobacter_sp_bihb_1401.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/enterobacter_sp_bihb_1401.yaml --out /private/tmp/bihb1401-strict-20261005.tsv`: exit 0; one file, zero files with errors and zero error rows.
- Structured reads verified the complete backbone row, ten ancestors, PATHS, scope, attestation, and seed event. Exact-ID checks covered seven raw source inventories, type material, merged IDs, and dropped records.
- `rg --no-ignore --hidden -n -z -i` searched target ID, label, slug, and BIHB 1401 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All three matches were read in full with TSV headers or JSON decoding: backbone, scope, and native NCBI name.
- Separate marker scanning over those roots found no JF766696 row. Ignored-inclusive filename and content searches under `reports` and `history` found no prior target report or separate target history artifact, including marker searches, before this report.
- Live NCBI Taxonomy EFetch/Datasets, exact nonexpanded Assembly/Nuccore searches, complete marker metadata, and three bounded PubMed queries completed. Exact-name, strain-variant, marker, and strain/topic web searches were performed. The related author-CV source had been inspected directly during this review session.
- Not checked: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused source agreement does not prove corpus reproduction.
- iModulonDB and curator-added graph ID/label checks are not applicable because the record asserts no gene, regulator, protein, phenotype, transcriptomic result, or causal graph. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

NCBI Taxonomy EFetch and Datasets agree on taxon 1034634, exact label,
species rank, parent 2608935, Bacteria division, and code 11.
Every ancestor ID, label, and rank agrees with the backbone.
The complete root-first chain is
`1 > 131567 > 2 > 3379134 > 1224 > 1236 > 91347 > 543 > 547 > 2608935`:
root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota,
Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Enterobacter,
and unclassified Enterobacter.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034634);
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034634).

The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31059`.
The backbone has no synonyms, retirement target, or direct children.
Exact type-material, merged-ID, and dropped-record checks found no
target row. Provisional species rank is not evidence of valid
nomenclatural publication; `EXACT` grounds this taxon, not genomic
equivalence or identity with other numbered BIHB isolates.

## Evidence

The NCBITAXON attestation agrees in ID, label, count 1, unit
`NAME`, and snapshot 2026-09-13. It counts a name assertion,
not a strain or genome. Scope and the
2026-09-13T17:54:04Z `seed_from_sources` /
`SEEDED_FROM_SOURCES` event agree.

The exact query `txid1034634[Organism:noexp]` returned zero
Assembly items with missing-phrase/no-items diagnostics and one
Nuccore item, UID 333496474. Complete metadata and source/rRNA
features identify `JF766696.1`, a 1,486-base partial 16S rRNA
sequence, strain BIHB 1401, taxon 1034634. Submitted source
qualifiers explicitly record rhizosphere, host pea, and country India.
They support submitted isolate provenance, not measured growth effects,
specific sampling coordinates, or whole-genome identity.
[GenBank JF766696.1](https://www.ncbi.nlm.nih.gov/nuccore/JF766696.1).

Gulati A., Rahi P., and Sharma N. directly submitted the sequence
on 1 April 2011. The associated pea-rhizosphere phosphate-solubilizing
genotypes study is marked unpublished in the inspected record.
Neither the study title nor the submitter address proves a
quantified phenotype, an exact isolation location, or a deposit.

PubMed queries for `JF766696[All Fields]`,
`"BIHB 1401"[All Fields] AND Enterobacter[All Fields]`, and
the full sequence-reference title returned zero items; query
translations and diagnostics were inspected. Bounded web queries did
not establish an experimental publication tied to this exact isolate.

The inspected author CV places a related Gulati/Rahi/Sharma 2013
pea-rhizosphere manuscript in its under-peer-review section for
FEMS Microbiology Ecology. This is a historical author listing,
not proof of eventual publication or BIHB 1401 assay results.
No phosphate-solubilization, plant-growth, cold-tolerance, or
other functional claim is imported from it.
[Author CV](https://nccs.academia.edu/PraveenRahi/CurriculumVitae).

## Completeness

The seven raw-source checks found no exact target BacDive, LPSN, GTDB,
GOLD, MediaDive, Madin, or BacTraits row. The ignored-inclusive native
search did not establish a target deposit, type material, genome,
or GTDB mapping. Optional synonyms, nomenclature, mappings, strains,
traits, and graphs are appropriately empty for this seeded record.
`strain_count: 0` describes classified inventory coverage, not
the absence of a biological isolate.

The exact marker and its explicit pea/India/rhizosphere qualifiers
are optional enrichment leads, not required genome or deposit fields
under the local checklist. No consequential missing required
representation was demonstrated. The eventual publication status and
isolate-level experimental details of the associated study remain
unresolved; no phenotype claim currently depends on them.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record. Focused validation and source
agreement do not substitute for full-corpus reproduction or establish
uninspected literature results.

## Recommended Edits

No required edit is demonstrated. Preserve generated fields and
`SEEDED` status.

If marker enrichment is separately authorized, define and test the
exact `taxon:1034634` / BIHB 1401 / `JF766696.1` relation
in maintained extraction inputs and logic
(`scripts/extract_source_inventory.py`, `src/taxonmech/extract.py`),
and adjust `scripts/seed_from_sources.py` only if needed.
`curation/seed_scope.tsv` owns scope, not inferred strain identity.
Do not patch generated YAML/pages or substitute another BIHB isolate,
culture deposit, or assembly for the verified marker.

## Follow-up Checks

Future enrichment should re-read versioned GenBank features, preserve
host/country/source at submitted-provenance scope, and test rejection
of unrelated BIHB identifiers. Regenerate through the documented
maintained pipeline, then rerun focused schema and strict validation.

Any future functional claim needs inspected primary isolate-specific
methods/results and an exact identity bridge. Before publishing
regenerated products, run full-corpus reproduction, QC, tests, strict
validation, provenance, history, and site gates. This review supplies
no such full-corpus result and does not promote status.

## Additional Notes

All three native matches are the exact source addresses above.
Generic web co-occurrences, similar BIHB numbers, and sequence-length
matches were not adopted as target evidence. Search misses apply only
to the stated sources and queries, not to all evidence globally.

No paid research, outbound contact, GitHub mutation,
YAML/inventory/scope/history edit, status promotion, regeneration,
or Eukaryota-record review occurred.

