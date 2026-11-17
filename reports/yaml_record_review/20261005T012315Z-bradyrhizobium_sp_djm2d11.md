# YAML Record Review: Bradyrhizobium sp. DJM2D11

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bradyrhizobium_sp_djm2d11.yaml`
- Started UTC: 2026-10-05T01:21:44Z
- Finished UTC: 2026-10-05T01:23:15Z
- Verdict: pass

## Target

Read the entire 54-line generated TaxonRecord for NCBITaxon:1034166, Bradyrhizobium sp. DJM2D11. It is a bacterial SPECIES-rank placeholder under NCBITaxon:2631580, with EXACT grounding, SEEDED status, genetic code 11, zero inventoried strains and one NCBI NAME attestation. Its identity is this specific NCBI entity, not another DJM isolate or an inferred named Bradyrhizobium species.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bradyrhizobium_sp_djm2d11.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/bradyrhizobium_sp_djm2d11.yaml --out /private/tmp/djm2d11-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: complete target and ten-ancestor backbone comparison, seven mapped-source inventories, PATHS and scope rows, NCBI attestation and inline-event text. No target children occur in the pinned backbone.
- PASS: complete exact-target scans of type-material, merged-ID and dropped inventories returned no rows.
- SKIPPED: `just verify-corpus` is full-corpus-only; diagnostic output limits are not target scoping.
- NOT APPLICABLE: `just validate-products`; no graph nodes or product labels.
- SKIPPED: `just validate-history`; ignored-inclusive target searches found no external history. The inline seed event was checked directly.
- No undocumented focused term/reference validator was substituted. Represented identifiers were checked against source evidence.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:221434` and complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30786` agree with the identifier and label. No source synonym is omitted.

All ten root-first ancestors match by identifier, label and rank: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Nitrobacteraceae, Bradyrhizobium and unclassified Bradyrhizobium. Live EFetch confirms the scientific name, species rank, bacterial placement, parent 2631580, code 11 and labeled ancestry; Datasets confirms ancestor identifiers including root. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034166&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034166).

EXACT denotes this NCBI identity, not a species-cluster or deposit equivalence. A SPECIES-rank isolate-associated placeholder does not establish nomenclatural validity or type material.

## Evidence

- The NCBI attestation exactly preserves the September 13 snapshot, identifier, label, count of one and NAME unit.
- Exact Nuccore query `txid1034166[Organism:noexp]` returned JF753520.1 alone. Full metadata, references and source/rRNA qualifiers identify a 623-base partial 16S marker, strain DJM2D11, taxon:1034166, and a surface-sterilized Zea seed source. This supports a marker association, not a genome or collection-deposit relationship. [GenBank JF753520.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753520.1).
- The accession explicitly cites PMID:21673982 and DOI:10.1371/journal.pone.0020396. Bibliographic identifiers agree with the previously fetched PubMed XML reread during this review. Community-wide findings and results for other isolates were not assigned to DJM2D11. [PubMed XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml).
- Exact NCBI Assembly query returned zero items with a no-items/phrase-not-found diagnostic. This is a bounded result, not proof that no resource exists under other assignments.
- `data/taxa/PATHS.tsv:13896` matches the slug. `curation/seed_scope.tsv:321752` supplies the September 13 one-source admission rationale. The inline event agrees with that rationale and the attestation list and makes no human-review claim.

## Completeness

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. No child taxon contributes descendant BacDive strains. Zero inventoried strains agrees with the source-count definition, not a biological assertion that no research isolate exists.

An ignored-inclusive, hidden-file-inclusive and compressed-file-aware identifier/name/slug/designation search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were inspected: backbone, native name and scope. A boundary-aware secondary accession/PMID/DOI search returned zero matches in these roots. Separate ignored-inclusive searches found no earlier target report or external history.

No eligible whole-deposit/genome join, additional supported mapping or missing required overlay was established. Bare DJM2D11 is not a validated culture-collection accession. Optional marker/literature enrichment remains possible; empty optional evidence and causal fields are not defects in this identity-only seed. iModulonDB is not applicable because no functional-gene or expression-module assertion occurs.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source counts and seeded provenance agree with inspected evidence. No represented phenotype relies on unreviewed supplementary rows.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future backbone corrections belong to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv` and its generator; scope changes belong in `curation/seed_scope.tsv`. Optional evidence enrichment requires an appropriate maintained input and separate curation authorization, not a hand edit of `data/taxa/`.

## Follow-up Checks

- Rerun both focused validators and the complete target/source comparison after authorized input changes.
- Run `just verify-corpus` separately before claiming corpus-wide reproducibility.
- Inspect exact DJM2D11 supplementary rows, headers, units and negative results before phenotype enrichment; do not transfer another DJM isolate's results.
- Keep JF753520.1 outside genome counts and require explicit eligible whole-deposit evidence for future strain/genome joins. Do not infer a named-species assignment from the marker alone.

## Additional Notes

The taxonomy-browser page was unavailable through the web tool; both official structured responses succeeded and were fully inspected. Previously fetched PubMed metadata and abstract were reread after independent confirmation of this accession's explicit citation. No fresh publisher full-text review or reuse of another record's verdict is claimed.

Supplementary workbooks remain uninspected: earlier web download attempts failed and the prescribed spreadsheet dependency loader was checked again and remains unavailable. This limits optional phenotype enrichment, not any represented claim. Raw marker bases were not reanalyzed. No paid research, source refresh, regeneration, history append, status promotion or GitHub mutation occurred. Only this new timestamped report was written.

