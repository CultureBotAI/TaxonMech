# YAML Record Review: Methylobacterium sp. DJM1A7

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_djm1a7.yaml`
- Started UTC: 2026-10-05T03:21:53Z
- Finished UTC: 2026-10-05T03:23:04Z
- Verdict: pass

## Target

Read the entire 54-line generated TaxonRecord for NCBITaxon:1034211, Methylobacterium sp. DJM1A7. This bacterial SPECIES-rank placeholder has parent NCBITaxon:2615210, EXACT grounding, SEEDED status, genetic code 11, zero inventoried strains and one NCBI NAME attestation. No named-species or culture-deposit equivalence is asserted.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/methylobacterium_sp_djm1a7.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/methylobacterium_sp_djm1a7.yaml --out /private/tmp/methylobacterium-djm1a7-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: complete target/ancestor backbone comparison, seven mapped inventories, PATHS, scope, NCBI attestation and inline-event text. No target children occur in the backbone.
- PASS: full exact-target scans of type-material, merged-ID and dropped inventories returned no rows.
- SKIPPED: `just verify-corpus` is full-corpus-only; diagnostic caps are not record scoping.
- NOT APPLICABLE: `just validate-products`; no graph nodes or product labels.
- SKIPPED: `just validate-history`; ignored-inclusive searches found no external target history. The inline seed event was checked directly.
- No undocumented focused term/reference validator was substituted; represented identifiers were checked against source evidence.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:221479` and native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30831` agree with the identifier and label. No source synonym is omitted.

All ten root-first ancestors match by identifier, label and rank: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Methylobacteriaceae, Methylobacterium and unclassified Methylobacterium. Live EFetch confirms the name, species rank, parent 2615210, bacterial placement, code 11 and labeled ancestry. Datasets confirms ancestor identifiers including root. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034211&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034211).

EXACT denotes this NCBI identity, not nomenclatural validity, type material or a broader species-cluster equivalence. The genus label alone supplies no metabolic or phenotype assertion.

## Evidence

- The NCBI attestation matches the September 13 snapshot, identifier, label, count of one and NAME unit.
- Exact Nuccore query `txid1034211[Organism:noexp]` returned JF753406.1 alone. Complete metadata, references and source/rRNA qualifiers identify a 654-base partial 16S marker, strain DJM1A7, taxon:1034211, a surface-sterilized Zea seed source and host Zea sp. This supports a marker association, not a genome or collection-deposit relationship. [GenBank JF753406.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753406.1).
- Its explicit PMID:21673982 and DOI:10.1371/journal.pone.0020396 citation agrees with previously fetched and inspected PubMed metadata and abstract. Broad study findings and other-isolate results were not transferred to DJM1A7. [PubMed XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml).
- The exact Assembly query returned zero items with the no-items/phrase-not-found diagnostic. This bounded result does not establish absence under every possible assignment.
- `data/taxa/PATHS.tsv:13941` matches the slug. `curation/seed_scope.tsv:321797` supplies the September 13 one-source rationale. The inline seed event exactly matches this rationale and source list without claiming human review.

## Completeness

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. No child taxon contributes descendant BacDive strains. Zero inventoried strains agrees with the BacDive-entry count implemented in `src/taxonmech/seed.py` despite GenBank naming a research isolate.

The identifier/name/slug/designation search included ignored and hidden files and compressed catalogs across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were inspected: backbone, native name and scope. The boundary-aware accession/PMID/DOI follow-up returned zero matches.

Separate ignored-inclusive searches found no external target history or prior exact-target report. No eligible whole-deposit/genome join, additional supported mapping or missing required overlay was established. Bare DJM1A7 is not a validated collection accession.

Optional marker/literature enrichment remains possible. Empty optional evidence and causal fields are appropriate for this identity-only seed. iModulonDB is not applicable because no functional-gene or expression-module assertion occurs.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source counts and seeded provenance agree with inspected evidence. No represented phenotype depends on uninspected supplementary rows.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future backbone corrections belong to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv`; generation logic belongs in `src/taxonmech/seed.py` and scope changes in `curation/seed_scope.tsv`. Optional evidence enrichment requires an appropriate maintained input and separate curation authorization, not a hand edit of `data/taxa/`.

## Follow-up Checks

- Rerun both focused validators and the complete target/source comparison after authorized input changes.
- Run `just verify-corpus` separately before claiming corpus-wide reproducibility.
- Inspect exact DJM1A7 supplementary rows, headers, units and negative results before phenotype enrichment.
- Keep JF753406.1 outside genome counts and require explicit eligible whole-deposit evidence for future strain/genome joins. Do not infer a named-species assignment from the marker alone.

## Additional Notes

The taxonomy-browser page was unavailable through the web tool; both official structured responses succeeded and were fully inspected. The accession's explicit citation was checked against previously inspected PubMed material; no new PubMed fetch or fresh publisher full-text review is claimed.

Supplementary workbooks remain uninspected: earlier download attempts failed and the prescribed spreadsheet dependency loader remains unavailable. This limits optional phenotype enrichment, not represented claims. Raw marker bases were not reanalyzed. No paid research, source refresh, regeneration, history append, status promotion or GitHub mutation occurred. Only this new timestamped report was written for this record.

