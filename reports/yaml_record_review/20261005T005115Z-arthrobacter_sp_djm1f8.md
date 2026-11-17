# YAML Record Review: Arthrobacter sp. DJM1F8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_djm1f8.yaml`
- Started UTC: 2026-10-05T00:49:52Z
- Finished UTC: 2026-10-05T00:51:15Z
- Verdict: pass

## Target

Read the entire 54-line generated TaxonRecord for NCBITaxon:1034154, Arthrobacter sp. DJM1F8. It is a bacterial SPECIES-rank placeholder under NCBITaxon:235627, unclassified Arthrobacter, with EXACT grounding, SEEDED status, genetic code 11, zero inventoried strains and one NCBI NAME attestation. This is DJM1F8, not DJM1F3 or the host plant.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/arthrobacter_sp_djm1f8.yaml`; LinkML exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/arthrobacter_sp_djm1f8.yaml --out /private/tmp/djm1f8-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: complete backbone and ten-ancestor comparison, seven mapped-source inventories, PATHS and seed-scope entries, NCBI attestation and inline-event text. There are no target children in the pinned backbone.
- PASS: full exact-target scans of type-material, merged-ID and dropped inventories returned no rows.
- SKIPPED: `just verify-corpus`, a full-corpus-only check. Diagnostic output limits do not provide record scoping.
- NOT APPLICABLE: `just validate-products`; no graph nodes or product labels.
- SKIPPED: `just validate-history`; ignored-inclusive target searches found no external target history. The inline event was checked directly.
- No undocumented focused term/reference validator was substituted. Represented identifiers were checked against their source evidence.

## Identity and Grounding

The backbone row at `data/raw/ncbitaxon_taxa.tsv:221422` and complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30774` agree on the identifier and label and supply no synonym.

All ten root-first ancestors match by identifier, label and rank: root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Micrococcaceae, Arthrobacter and unclassified Arthrobacter. Live official EFetch and Datasets responses agree with the name, rank, domain, parent, code and ancestry. EFetch provides the labeled chain excluding root; Datasets additionally includes root identifier 1. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034154&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034154).

EXACT is identity with this NCBI taxon, not a named-species or culture-collection equivalence. SPECIES is the authority's rank for this isolate-associated placeholder; it does not establish valid nomenclatural publication or a type strain.

## Evidence

- The NCBI attestation exactly preserves the September 13 snapshot, identifier, label, assertion count of one and NAME unit.
- Exact Nuccore query `txid1034154[Organism:noexp]` returned one record, JF753458.1. Full metadata, references and source/rRNA qualifiers identify a 657-base partial 16S marker, strain DJM1F8, taxon:1034154, with a surface-sterilized Zea seed source. A marker is not a genome and a bare isolate designation is not a deposit accession. [GenBank JF753458.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753458.1).
- This accession explicitly cites PMID:21673982 and DOI:10.1371/journal.pone.0020396. Both resolve to the inspected Johnston-Monje and Raizada (2011) article. Its methods place this accession in a culture-derived interval; no phenotype was imported. [Primary article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396), [PubMed XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml).
- Exact NCBI Assembly query returned zero items with the no-items/phrase-not-found diagnostic. This is bounded to the query, not proof that no resource exists elsewhere or under another assignment.
- `data/taxa/PATHS.tsv:13884` matches the slug. `curation/seed_scope.tsv:321740` supplies the September 13 one-source rationale, and the inline seed event matches both scope text and attestation list.

## Completeness

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. No child taxon contributes descendant BacDive strains. Zero inventoried strains therefore agrees with the repository's count semantics; it does not deny the existence of a cultured research isolate.

The ignored-inclusive, hidden-file-inclusive and compressed-file-aware identifier/name/slug/designation search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were read: backbone, native name and scope. A second boundary-aware accession/PMID/DOI search returned zero matches in those roots. Separate ignored-inclusive searches found no previous target report or external target history.

No supported deposit/genome join, additional taxonomy mapping or missing required overlay was established. Optional literature and marker evidence may be curated later; empty optional evidence and causal fields are not defects in this identity-only seed. iModulonDB is not applicable because no functional-gene or expression-module assertion occurs.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, count semantics and seeded provenance agree with the inspected sources. Unreviewed supplementary phenotype data do not contradict a phenotype claim, because none is represented.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Any future backbone correction belongs to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv` and its generator. Scope changes belong in `curation/seed_scope.tsv`. Optional evidence enrichment requires an appropriate maintained input and separately authorized curation, not a direct edit to `data/taxa/`.

## Follow-up Checks

- Rerun both focused validators and the full target/source comparison after authorized input changes.
- Run `just verify-corpus` separately before claiming corpus-wide reproducibility.
- Inspect DJM1F8-specific supplementary rows, headers, units and negative results before phenotype enrichment; do not inherit DJM1F3's or community-level properties.
- Keep JF753458.1 outside genome counts and require eligible whole-deposit evidence for strain/genome joins.

## Additional Notes

The NCBI taxonomy-browser page was unavailable through the web tool; both official structured responses succeeded and were fully inspected. The cited primary article's relevant sections and PubMed metadata/abstract had been inspected earlier in this review turn and were reused only after independently confirming this accession's explicit citation. No other record's verdict or phenotype was reused.

The paper's supplementary workbook links failed through the web tool, and the prescribed spreadsheet dependency loader was unavailable. Their rows were not inspected; optional phenotype enrichment remains limited accordingly. Raw sequence bases were not reanalyzed. No paid research, source refresh, regeneration, history append, status promotion or GitHub mutation occurred. Only this new timestamped report was written.

