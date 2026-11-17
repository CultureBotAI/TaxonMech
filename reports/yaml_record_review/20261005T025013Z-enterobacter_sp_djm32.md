# YAML Record Review: Enterobacter sp. DJM32

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterobacter_sp_djm32.yaml`
- Started UTC: 2026-10-05T02:49:01Z
- Finished UTC: 2026-10-05T02:50:13Z
- Verdict: pass

## Target

Read the entire 54-line generated TaxonRecord for NCBITaxon:1034199, Enterobacter sp. DJM32. This bacterial SPECIES-rank placeholder has parent NCBITaxon:2608935, EXACT grounding, SEEDED status, genetic code 11, zero inventoried strains and one NCBI NAME attestation. It denotes DJM32, not another DJM isolate or a named Enterobacter species.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/enterobacter_sp_djm32.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/enterobacter_sp_djm32.yaml --out /private/tmp/djm32-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: complete target and ten-ancestor backbone comparison, seven mapped-source inventories, PATHS and scope rows, NCBI attestation and inline-event text. No target children occur in the pinned backbone.
- PASS: full exact-target scans of type-material, merged-ID and dropped inventories returned no rows.
- SKIPPED: `just verify-corpus` is full-corpus-only; diagnostic output limits are not record scoping.
- NOT APPLICABLE: `just validate-products`; no graph nodes or product labels.
- SKIPPED: `just validate-history`; ignored-inclusive searches found no external target history. The inline seed event was checked directly.
- No undocumented focused term/reference validator was substituted. Represented identifiers were checked against source evidence.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:221467` and complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30819` agree with the identifier and label. No source synonym is omitted.

All ten root-first ancestors match by identifier, label and rank: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Enterobacter and unclassified Enterobacter. Live EFetch confirms the name, species rank, bacterial placement, parent 2608935, code 11 and labeled ancestry; Datasets confirms ancestor identifiers including root. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034199&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034199).

EXACT denotes this NCBI identity, not a species-cluster or culture-deposit equivalence. The source SPECIES rank does not establish nomenclatural validity or type material for this isolate-associated placeholder.

## Evidence

- The NCBI attestation exactly matches the September 13 snapshot, identifier, label, count of one and NAME unit.
- Exact Nuccore query `txid1034199[Organism:noexp]` returned JF753551.1 alone. Full metadata, references and source/rRNA qualifiers identify a 395-base partial 16S marker, strain DJM32, taxon:1034199, and a surface-sterilized Zea seed source. This supports a marker association, not a genome or collection-deposit relationship. [GenBank JF753551.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753551.1).
- Its explicit citation to PMID:21673982 and DOI:10.1371/journal.pone.0020396 agrees with previously fetched PubMed metadata and the abstract reread this turn. Broader study findings and results for named Enterobacter species were not transferred to DJM32. [PubMed XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml).
- The exact Assembly query returned zero items with the no-items/phrase-not-found diagnostic. This bounded result is not proof of absence under every other assignment.
- `data/taxa/PATHS.tsv:13929` matches the slug. `curation/seed_scope.tsv:321785` supplies the September 13 one-source admission rationale. The inline event matches this rationale and the attestation list without claiming human review.

## Completeness

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. No child taxon contributes descendant BacDive strains. Zero inventoried strains agrees with the BacDive-entry count implemented in `src/taxonmech/seed.py` despite a research isolate being named in GenBank.

The ignored-inclusive, hidden-file-inclusive and compressed-file-aware identifier/name/slug/designation search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were inspected: backbone, native name and scope. A boundary-aware accession/PMID/DOI follow-up search returned zero matches in those roots. Separate ignored-inclusive searches found no previous target report or external history.

No eligible whole-deposit/genome join, additional supported mapping or missing required overlay was established. Bare DJM32 is not a validated collection accession. Optional marker/literature enrichment remains possible; empty optional evidence and causal fields are appropriate for the represented identity-only seed. iModulonDB is not applicable because no functional-gene or expression-module assertion occurs.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source counts and seeded provenance agree with inspected evidence. The short external marker is not misrepresented as a genome or a named-species identification in the YAML. No represented phenotype relies on unreviewed supplementary rows.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future backbone corrections belong to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv`; generation logic belongs in `src/taxonmech/seed.py` and scope changes in `curation/seed_scope.tsv`. Optional evidence enrichment requires an appropriate maintained input and separate curation authorization, not a hand edit of `data/taxa/`.

## Follow-up Checks

- Rerun both focused validators and the complete target/source comparison after authorized input changes.
- Run `just verify-corpus` separately before claiming corpus-wide reproducibility.
- Inspect exact DJM32 supplementary rows, headers, units and negative results before phenotype enrichment; do not transfer other isolate results.
- Keep JF753551.1 outside genome counts and require explicit eligible whole-deposit evidence for future strain/genome joins. The short partial marker alone does not justify a named-species assignment.

## Additional Notes

The taxonomy-browser page was unavailable through the web tool; both official structured responses succeeded and were fully inspected. This accession's explicit citation was checked independently against PubMed material already fetched and reread this turn; no fresh publisher full-text review is claimed.

Supplementary workbooks remain uninspected: earlier web download attempts failed and the prescribed spreadsheet dependency loader remains unavailable. This limits optional phenotype enrichment, not any represented claim. Raw marker bases were not reanalyzed. No paid research, source refresh, regeneration, history append, status promotion or GitHub mutation occurred. Only this new timestamped report was written.

