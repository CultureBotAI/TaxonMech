# YAML Record Review: Enterococcus sp. DJM16

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterococcus_sp_djm16.yaml`
- Started UTC: 2026-10-05T02:53:17Z
- Finished UTC: 2026-10-05T02:58:09Z
- Verdict: pass

## Target

Read the entire 54-line generated TaxonRecord for NCBITaxon:1034201, Enterococcus sp. DJM16. It represents a bacterial SPECIES-rank placeholder with parent NCBITaxon:2608891, EXACT grounding, SEEDED status, genetic code 11, zero inventoried strains and one NCBI NAME attestation. No named-species or culture-deposit equivalence is asserted.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/enterococcus_sp_djm16.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/enterococcus_sp_djm16.yaml --out /private/tmp/djm16-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: full backbone comparison of the target and all ten ancestors, seven mapped inventories, PATHS and scope entries, NCBI attestation and inline seed-event text. No target children occur in the pinned backbone.
- PASS: complete exact-target scans of type-material, merged-ID and dropped inventories returned no rows.
- SKIPPED: `just verify-corpus` is full-corpus-only; diagnostic caps are not record scoping.
- NOT APPLICABLE: `just validate-products`; no graph nodes or product labels.
- SKIPPED: `just validate-history`; ignored-inclusive searches found no separate target history. The inline event was checked directly.
- No undocumented focused term/reference validator was substituted; represented identifiers were checked against source evidence.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:221469` and native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30821` agree with the identifier and label. No source synonym is omitted.

All ten root-first ancestors match by identifier, label and rank: root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Lactobacillales, Enterococcaceae, Enterococcus and unclassified Enterococcus. Live EFetch confirms the name, species rank, parent 2608891, bacterial placement, genetic code 11 and labeled ancestry; Datasets confirms the ancestor identifiers including root. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034201&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034201).

EXACT denotes this NCBI identity. The source SPECIES rank does not establish nomenclatural validity, type material or identity with a named Enterococcus species.

## Evidence

- The NCBI attestation matches the September 13 snapshot, identifier, label, count of one and NAME unit.
- Exact Nuccore query `txid1034201[Organism:noexp]` returned JF753536.1 alone. Complete sequence metadata, references and source/rRNA qualifiers identify a 565-base partial 16S marker, strain DJM16, taxon:1034201, a surface-sterilized Zea seed source and host Zea sp. This is a marker association, not a genome or collection-deposit relationship. [GenBank JF753536.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753536.1).
- Its explicit PMID:21673982 and DOI:10.1371/journal.pone.0020396 citation matches previously fetched PubMed metadata and abstract, reread during this review. Broad study results and findings for other isolates were not transferred to DJM16. [PubMed XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml).
- The exact Assembly query returned zero items with a no-items/phrase-not-found diagnostic. This bounded query does not prove absence under every possible assignment.
- `data/taxa/PATHS.tsv:13931` matches the slug; `curation/seed_scope.tsv:321787` supplies the September 13 one-source rationale. The inline September 13 seed event agrees with the source list and scope text without claiming human review.

## Completeness

Complete mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. No child taxon supplies descendant BacDive strains. Zero inventoried strains agrees with the BacDive-entry count implemented in `src/taxonmech/seed.py`; a GenBank research-isolate qualifier does not change that inventory count.

The identifier/name/slug/designation search included ignored and hidden files and compressed catalogs across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were inspected: backbone, native scientific name and scope. The boundary-aware accession/PMID/DOI follow-up returned zero matches in those roots.

Separate ignored-inclusive searches found no external target history or prior exact-target review report. No eligible whole-deposit/genome join, additional supported mapping or missing required overlay was established. Bare DJM16 is not a validated collection accession.

Optional marker or literature enrichment remains possible. Empty optional evidence and causal fields are appropriate for this identity-only seed. iModulonDB is not applicable because there is no functional-gene or expression-module assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, ancestry, inventory counts and seed provenance agree with inspected evidence. No represented phenotype depends on uninspected supplementary rows.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Any future backbone correction belongs to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv`; generation logic belongs in `src/taxonmech/seed.py` and scope changes in `curation/seed_scope.tsv`. Optional evidence enrichment requires an appropriate maintained input and separate curation authorization, not a hand edit of `data/taxa/`.

## Follow-up Checks

- Rerun both focused validators and the full target/source comparison after authorized input changes.
- Run `just verify-corpus` separately before claiming corpus-wide reproducibility.
- Inspect exact DJM16 supplementary rows, headers, units and negative results before phenotype enrichment; do not transfer study-wide or other-isolate findings.
- Keep JF753536.1 outside genome counts and require explicit eligible whole-deposit evidence before future strain/genome joins.

## Additional Notes

The taxonomy-browser page was unavailable through the web tool. Both official structured responses succeeded and were fully inspected. After a context transition hid earlier command output, terminal handles were confirmed unavailable and the taxonomy, sequence and primary catalog checks were repeated; the inspected replacement outputs support this report.

The PubMed material was previously fetched and reread, not a fresh publisher full-text review. Supplementary workbooks remain uninspected: earlier downloads failed and the prescribed spreadsheet dependency loader was unavailable. This limits optional phenotype enrichment, not represented claims. Raw marker bases were not reanalyzed.

No paid research, source refresh, regeneration, history append, status promotion or GitHub mutation occurred. Only this new timestamped report was written for this record.

