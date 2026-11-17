# YAML Record Review: Brevibacillus sp. DJM3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/brevibacillus_sp_djm3.yaml`
- Started UTC: 2026-10-05T01:24:03Z
- Finished UTC: 2026-10-05T01:25:16Z
- Verdict: pass

## Target

Read the entire 54-line generated TaxonRecord for NCBITaxon:1034167, Brevibacillus sp. DJM3. This bacterial SPECIES-rank placeholder has parent NCBITaxon:2684853, EXACT grounding, SEEDED status, genetic code 11, zero inventoried strains and one NCBI NAME attestation. The target is this specific isolate-associated NCBI entity, not another DJM isolate or an inferred named species.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/brevibacillus_sp_djm3.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/brevibacillus_sp_djm3.yaml --out /private/tmp/djm3-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: complete target and ten-ancestor backbone comparison, seven mapped-source inventories, PATHS and scope rows, NCBI attestation and inline-event text. No target children occur in the pinned backbone.
- PASS: full exact-target scans of type-material, merged-ID and dropped inventories returned no rows.
- SKIPPED: `just verify-corpus` is full-corpus-only; diagnostic output limits are not target scoping.
- NOT APPLICABLE: `just validate-products`; no graph nodes or product labels.
- SKIPPED: `just validate-history`; ignored-inclusive searches found no external target history. The inline seed event was checked directly.
- No undocumented focused term/reference validator was substituted. Represented identifiers were checked against source evidence.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:221435` and complete native name object at `data/catalog/ncbi_names-0005.jsonl.gz:30787` agree on identifier and scientific name. No source synonym is omitted.

The ten root-first ancestors match by identifier, label and rank: root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Paenibacillaceae, Brevibacillus and unclassified Brevibacillus. Live EFetch confirms the name, species rank, bacterial placement, parent 2684853, code 11 and labeled ancestry; Datasets confirms ancestor identifiers including root. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034167&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034167).

EXACT is justified for this NCBI identity. It does not assert culture-deposit or species-cluster equivalence. NCBI's SPECIES rank does not establish nomenclatural validity or type material for the placeholder.

## Evidence

- The NCBI NAME attestation matches the snapshot date, identifier, label, count and unit exactly.
- Exact Nuccore query `txid1034167[Organism:noexp]` returned JF753523.1 alone. Full metadata, references and source/rRNA qualifiers identify a 628-base partial 16S marker, strain DJM3, taxon:1034167, and a surface-sterilized Zea seed source. This supports a marker association, not a genome or collection-deposit relationship. [GenBank JF753523.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753523.1).
- Its explicit PMID:21673982 and DOI:10.1371/journal.pone.0020396 citation agrees with the previously fetched PubMed metadata and abstract reread in this turn. Broader study findings were not transferred to DJM3. [PubMed XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml).
- The exact Assembly query returned zero items with the no-items/phrase-not-found diagnostic. This bounded result is not a claim that no resource exists under any other taxonomic assignment.
- `data/taxa/PATHS.tsv:13897` agrees with the slug. `curation/seed_scope.tsv:321753` supplies the September 13 one-source admission rationale. The inline seed event matches this rationale and the attestation list without claiming human review.

## Completeness

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. There are no child taxa contributing descendant BacDive strains. Zero inventoried strains is consistent with the count definition despite a research isolate being named in GenBank.

The ignored-inclusive, hidden-file-inclusive and compressed-file-aware identifier/name/slug/designation search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were inspected: backbone, native name and scope. The boundary-aware accession/PMID/DOI follow-up search returned zero matches in those roots. Separate ignored-inclusive searches found no previous target report or external history.

No eligible whole-deposit/genome join, additional supported mapping or missing required overlay was established. Bare DJM3 is not a validated collection accession. Optional marker/literature enrichment remains possible; empty optional evidence and causal fields are appropriate for the represented identity-only seed. iModulonDB is not applicable because the record makes no functional-gene or expression-module assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, attestation counts and seeded provenance agree with inspected sources. No represented phenotype depends on unreviewed supplementary rows.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Any future backbone correction belongs to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv` and its generator; scope changes belong in `curation/seed_scope.tsv`. Optional evidence enrichment requires an appropriate maintained input and separate authorization, not a hand edit of `data/taxa/`.

## Follow-up Checks

- Rerun both focused validators and the complete target/source comparison after authorized input changes.
- Run `just verify-corpus` separately before claiming corpus-wide reproducibility.
- Inspect exact DJM3 supplementary rows, including headers, units and negative results, before phenotype enrichment.
- Keep JF753523.1 outside genome counts. Require explicit eligible whole-deposit evidence for future strain/genome joins, and do not infer a named-species assignment from this marker.

## Additional Notes

The taxonomy-browser page was unavailable through the web tool; both official structured responses succeeded and were fully inspected. The accession's citation was checked independently against PubMed material already fetched and reread this turn; no fresh publisher full-text review is claimed.

Supplementary workbooks remain uninspected because prior web download attempts failed and the prescribed spreadsheet dependency loader remains unavailable. This limits optional phenotype enrichment, not a represented claim. Raw marker bases were not reanalyzed. No paid research, source refresh, regeneration, history append, status promotion or GitHub mutation occurred. Only this new timestamped report was written.

