# YAML Record Review: Arthrobacter sp. DJM1F3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_djm1f3.yaml`
- Started UTC: 2026-10-05T00:46:36Z
- Finished UTC: 2026-10-05T00:49:07Z
- Verdict: pass

## Target

Read the entire 54-line generated TaxonRecord for NCBITaxon:1034153, Arthrobacter sp. DJM1F3. It is a bacterial SPECIES-rank placeholder under unclassified Arthrobacter (NCBITaxon:235627), with EXACT grounding, SEEDED status, genetic code 11, zero inventoried strains and one NCBI NAME attestation. This is the isolate-associated taxon, not the genus, its plant host or all seed endophytes.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/arthrobacter_sp_djm1f3.yaml`; LinkML exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/arthrobacter_sp_djm1f3.yaml --out /private/tmp/djm1f3-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: structured comparison of the entire backbone row, all ten ancestors, seven mapped-source inventories, PATHS and scope entries, NCBI attestation and inline-event text. The pinned backbone has no target children.
- PASS: full exact-target scans of type-material, merged-ID and dropped inventories returned no rows.
- SKIPPED: `just verify-corpus`, a full-corpus-only reproducibility check. A diagnostic cap is not target scoping.
- NOT APPLICABLE: `just validate-products`; no curator-added graph nodes or product labels.
- SKIPPED: `just validate-history`; ignored-inclusive target searches found no external history. The inline seed event was checked directly.
- No undocumented focused term/reference validator was substituted. Represented identifiers were checked against source evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221421` and the complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30773` agree on the identifier and label; neither provides a synonym.

All ten ancestors agree by identifier, label and rank: root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Micrococcaceae, Arthrobacter and unclassified Arthrobacter. Live NCBI EFetch confirms the labeled lineage, parent, name, species rank and code 11; Datasets confirms the lineage identifiers including root. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034153&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034153).

EXACT means identity with this NCBI taxon. NCBI's SPECIES rank for an isolate-named placeholder is not a claim of valid nomenclatural publication or a type-strain designation. No named-species assignment is inferred from genus membership or sequence similarity.

## Evidence

- The NCBI attestation exactly preserves the September 13 snapshot, identifier, label, count of one and NAME unit.
- Exact Nuccore query `txid1034153[Organism:noexp]` returned one record, JF753454.1. Full metadata, references and source/rRNA qualifiers identify a 657-base partial 16S marker, strain DJM1F3, taxon:1034153, and a surface-sterilized Zea seed source. This establishes a marker association, not a genome or culture-deposit link. [GenBank JF753454.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753454.1).
- The accession cites Johnston-Monje and Raizada's 2011 PLoS ONE paper, PMID:21673982 and DOI:10.1371/journal.pone.0020396. PubMed XML and the publisher's title, authors, citation and abstract agree. Inspected methods distinguish cloned sequences from cultured-isolate sequences and place JF753454 inside the latter accession interval, JF753401-JF753552. This is evidence of culture-derived sequence provenance, not a collection deposit. Community-level persistence and other isolates' growth-promotion results were not assigned to DJM1F3. [Primary article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396), [PubMed metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml).
- Exact NCBI Assembly query returned zero items with the service's no-items/phrase-not-found diagnostic. This is a bounded query result, not universal proof that no genome exists under another assignment.
- `data/taxa/PATHS.tsv:13883` matches the slug. `curation/seed_scope.tsv:321739` supplies the September 13 one-source admission rationale. The inline event matches the source list and scope text; SEEDED does not imply human review.

## Completeness

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. No child taxon contributes descendant BacDive strains. Zero inventoried strains therefore agrees with source scope even though a research isolate was cultured. The bare DJM1F3 designation does not establish an eligible culture-collection accession.

The ignored-inclusive, hidden-file-inclusive and compressed-file-aware identifier/name/slug/designation search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were read: backbone, native name and scope. A boundary-aware secondary search for JF753454, PMID 21673982 and the DOI returned no matches in those roots. A preliminary unbounded PMID search matched the unrelated run SRR21673982 in a Staphylococcus aureus ATB row; that is not citation or strain evidence and was excluded.

Separate ignored-inclusive searches found no previous target report or external history. No eligible deposit/genome join, additional taxonomy mapping or missing required overlay was established. Optional literature and marker enrichment remains possible; its omission is not a defect in this identity-only seed. Optional evidence/causal fields may stay empty. iModulonDB is not applicable because the record makes no functional-gene or expression-module assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, count semantics and seeded provenance agree with inspected evidence. Supplementary phenotype rows remain unreviewed, but no such claim occurs in the YAML.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future backbone corrections belong to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv` and its generator; scope changes belong in `curation/seed_scope.tsv`. Optional evidence enrichment requires an appropriate maintained input and separately authorized curation, not a hand edit of `data/taxa/`.

## Follow-up Checks

- Rerun both focused validators and the complete target/source comparison after authorized input changes.
- Run `just verify-corpus` separately before claiming corpus-wide reproducibility.
- Before phenotype enrichment, inspect the exact DJM1F3 row, headers and units in primary Tables S3/S4, including any isolate-specific negative results. Do not transfer community or neighboring-isolate traits.
- Keep JF753454.1 outside genome counts and require explicit eligible deposit evidence for any strain/genome join.

## Additional Notes

The NCBI taxonomy-browser page was unavailable through the web tool; both official structured taxonomy responses succeeded and were fully inspected. PubMed HTML presented a browser check, but its XML metadata and abstract succeeded. The publisher's relevant article sections were inspected, not every reference or supplementary row. Tables S3/S4 download links failed through the web tool, and the prescribed spreadsheet dependency loader was unavailable, so workbook inspection was blocked and no spreadsheet was authored or substituted. Raw marker bases were not reanalyzed.

No paid research, source refresh, regeneration, history append, status promotion or GitHub mutation occurred. Only this new timestamped report was written.

