# YAML Record Review: Escherichia sp. DJM1A6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/escherichia_sp_djm1a6.yaml`
- Started UTC: 2026-10-05T03:02:02Z
- Finished UTC: 2026-10-05T03:03:27Z
- Verdict: pass

## Target

Read the entire 54-line generated TaxonRecord for NCBITaxon:1034203, Escherichia sp. DJM1A6. It is a bacterial SPECIES-rank placeholder with parent NCBITaxon:2608889, EXACT grounding, SEEDED status, genetic code 11, zero inventoried strains and one NCBI NAME attestation. It makes no E. coli, named-species or culture-deposit equivalence claim.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/escherichia_sp_djm1a6.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/escherichia_sp_djm1a6.yaml --out /private/tmp/escherichia-djm1a6-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: full target and ten-ancestor backbone comparison, seven mapped inventories, PATHS, scope, NCBI attestation and inline seed-event text. No target children occur in the backbone.
- PASS: complete exact-target type-material, merged-ID and dropped-inventory scans returned no rows.
- SKIPPED: `just verify-corpus` is full-corpus-only; diagnostic limits do not make it record-scoped.
- NOT APPLICABLE: `just validate-products`; no graph nodes or product labels.
- SKIPPED: `just validate-history`; ignored-inclusive searches found no external target history. The inline seed event was inspected directly.
- No undocumented focused term/reference validator was substituted; represented identifiers were checked against source evidence.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:221471` and complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30823` agree with the identifier and label. No source synonym is omitted.

All ten root-first ancestors match by identifier, label and rank: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Escherichia and unclassified Escherichia. Live EFetch confirms the name, species rank, parent 2608889, bacterial placement, code 11 and labeled ancestry; Datasets confirms all ancestor identifiers including root. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034203&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034203).

EXACT denotes the NCBI entity. The source SPECIES rank does not establish nomenclatural validity, type material or identification as E. coli.

## Evidence

- The NCBI attestation matches the September 13 snapshot, identifier, label, count of one and NAME unit.
- Exact Nuccore query `txid1034203[Organism:noexp]` returned JF753405.1 alone. Complete metadata, references and source/rRNA qualifiers identify a 652-base partial 16S marker, strain DJM1A6, taxon:1034203, a surface-sterilized Zea seed source and host Zea sp. This supports a marker association, not a genome or collection-deposit relationship. [GenBank JF753405.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753405.1).
- Its explicit PMID:21673982 and DOI:10.1371/journal.pone.0020396 citation agrees with previously fetched PubMed metadata and abstract reread earlier this turn. Broad study findings and results for other isolates were not transferred to DJM1A6. [PubMed XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml).
- The exact Assembly query returned zero items with the no-items/phrase-not-found diagnostic. This bounded result is not proof of absence under every possible assignment.
- `data/taxa/PATHS.tsv:13933` matches the slug. `curation/seed_scope.tsv:321789` supplies the September 13 one-source rationale. The inline event exactly matches that rationale and source list without claiming human review.

## Completeness

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. No child taxon contributes descendant BacDive strains. The BacDive-entry count in `src/taxonmech/seed.py` supports zero inventoried strains despite a research isolate being named in GenBank.

The identifier/name/slug/designation search included ignored and hidden files and compressed catalogs across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were inspected: backbone, native name and scope. The boundary-aware accession/PMID/DOI follow-up returned zero matches.

Separate ignored-inclusive searches found no external target history or prior exact-target report. No eligible whole-deposit/genome join, additional supported mapping or missing required overlay was established. Bare DJM1A6 is not a validated collection accession.

Optional marker/literature enrichment remains possible. Empty optional evidence and causal fields are appropriate for the represented identity-only seed. iModulonDB is not applicable because no functional-gene or expression-module assertion occurs.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source counts and seed provenance agree with inspected evidence. No represented phenotype relies on uninspected supplementary rows.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future backbone corrections belong to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv`; generation logic belongs in `src/taxonmech/seed.py` and scope changes in `curation/seed_scope.tsv`. Optional evidence enrichment requires an appropriate maintained input and separate curation authorization, not a hand edit of `data/taxa/`.

## Follow-up Checks

- Rerun both focused validators and the complete target/source comparison after authorized input changes.
- Run `just verify-corpus` separately before claiming corpus-wide reproducibility.
- Inspect exact DJM1A6 supplementary rows, headers, units and negative results before phenotype enrichment.
- Keep JF753405.1 outside genome counts. Require explicit eligible whole-deposit evidence for strain/genome joins; do not infer E. coli identity from this marker alone.

## Additional Notes

The taxonomy-browser page was unavailable through the web tool; both official structured responses succeeded and were fully inspected. This accession's citation was independently checked against previously fetched PubMed material reread this turn; no fresh publisher full-text review is claimed.

Supplementary workbooks remain uninspected: earlier download attempts failed and the prescribed spreadsheet dependency loader remains unavailable. This limits optional phenotype enrichment, not represented claims. Raw marker bases were not reanalyzed. No paid research, source refresh, regeneration, history append, status promotion or GitHub mutation occurred. Only this new timestamped report was written for this record.

