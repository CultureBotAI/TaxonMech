# YAML Record Review: Enterococcus sp. DJM22

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterococcus_sp_djm22.yaml`
- Started UTC: 2026-10-05T02:59:54Z
- Finished UTC: 2026-10-05T03:01:19Z
- Verdict: pass

## Target

Read the entire 54-line generated TaxonRecord for NCBITaxon:1034202, Enterococcus sp. DJM22. This bacterial SPECIES-rank placeholder has parent NCBITaxon:2608891, EXACT grounding, SEEDED status, code 11, zero inventoried strains and one NCBI NAME attestation. It does not assert identity with a named Enterococcus species or culture deposit.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/enterococcus_sp_djm22.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/enterococcus_sp_djm22.yaml --out /private/tmp/djm22-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: full target/ancestor backbone comparison, seven mapped inventories, PATHS, scope, NCBI attestation and inline-event text. No target children occur in the backbone.
- PASS: exact-target full scans of type-material, merged-ID and dropped inventories returned no rows.
- SKIPPED: `just verify-corpus` is full-corpus-only; a diagnostic cap is not record scoping.
- NOT APPLICABLE: `just validate-products`; no graph nodes or product labels.
- SKIPPED: `just validate-history`; the ignored-inclusive target-history search returned no external record. The inline seed event was inspected.
- No undocumented focused term/reference validator was substituted; represented identifiers were checked against sources.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:221470` and native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30822` agree with the identifier and label. No source synonym is omitted.

All ten root-first ancestors match by identifier, label and rank: root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Lactobacillales, Enterococcaceae, Enterococcus and unclassified Enterococcus. Live EFetch confirms the name, parent 2608891, species rank, bacterial placement, code 11 and labeled ancestry. Datasets confirms the ancestor identifiers including root. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034202&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034202).

EXACT denotes this NCBI identity, not nomenclatural validity, type material or a broader species-cluster equivalence.

## Evidence

- The NCBI attestation matches the September 13 snapshot, identifier, label, count of one and NAME unit.
- Exact Nuccore query `txid1034202[Organism:noexp]` returned JF753541.1 alone. Full metadata, references and source/rRNA qualifiers identify a 607-base partial 16S marker, strain DJM22, taxon:1034202, a surface-sterilized Zea seed source and host Zea sp. It is not a genome or collection-deposit relationship. [GenBank JF753541.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753541.1).
- Its explicit citation to PMID:21673982 and DOI:10.1371/journal.pone.0020396 agrees with previously fetched PubMed metadata and the abstract reread this turn. Community-level results and findings for other isolates were not transferred to DJM22. [PubMed XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml).
- The exact Assembly query returned zero items with the no-items/phrase-not-found diagnostic. This is a bounded result, not proof of absence under all assignments.
- `data/taxa/PATHS.tsv:13932` matches the slug. `curation/seed_scope.tsv:321788` supplies the September 13 one-source admission rationale. The inline seed event exactly matches that rationale and source list without claiming human review.

## Completeness

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. No child taxon contributes descendant BacDive strains. Zero inventoried strains agrees with the BacDive-entry count in `src/taxonmech/seed.py` despite GenBank naming a research isolate.

The identifier/name/slug/designation search included ignored and hidden files and compressed catalogs in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were inspected: backbone, native name and scope. A boundary-aware accession/PMID/DOI follow-up returned zero matches.

Separate ignored-inclusive searches found no external target history or prior exact-target review report. No eligible whole-deposit/genome join, additional supported mapping or missing required overlay was established. Bare DJM22 is not a validated collection accession.

Optional marker/literature enrichment remains possible. Empty optional evidence and causal fields are appropriate for this identity-only seed. iModulonDB is not applicable because no functional-gene or expression-module assertion occurs.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, counts and seeded provenance agree with inspected evidence. No represented phenotype depends on uninspected supplementary rows.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future backbone corrections belong to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv`; generation logic belongs in `src/taxonmech/seed.py` and scope changes in `curation/seed_scope.tsv`. Optional evidence enrichment requires an appropriate maintained input and separate curation authorization, not a hand edit of `data/taxa/`.

## Follow-up Checks

- Rerun both focused validators and the complete target/source comparison after authorized input changes.
- Run `just verify-corpus` separately before claiming corpus-wide reproducibility.
- Inspect exact DJM22 supplementary rows, headers, units and negative results before phenotype enrichment.
- Keep JF753541.1 outside genome counts; require explicit eligible whole-deposit evidence for future strain/genome joins.

## Additional Notes

The taxonomy-browser page was unavailable through the web tool; both official structured responses succeeded and were fully inspected. Previously fetched PubMed metadata and abstract were reread; no fresh publisher full-text review is claimed.

Supplementary workbooks remain uninspected: earlier downloads failed and the prescribed spreadsheet dependency loader is still unavailable. This limits optional phenotype enrichment, not represented claims. Raw marker bases were not reanalyzed. No paid research, source refresh, regeneration, history append, status promotion or GitHub mutation occurred. Only this new timestamped report was written for this record.

