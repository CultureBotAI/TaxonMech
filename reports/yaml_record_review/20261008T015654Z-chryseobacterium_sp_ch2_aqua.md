# YAML Record Review: Chryseobacterium sp. CH2(AQUA)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/chryseobacterium_sp_ch2_aqua.yaml`
- Started UTC: 2026-10-08T01:50:26Z
- Finished UTC: 2026-10-08T01:56:54Z
- Verdict: pass

## Target

The entire 63-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1036178`, Chryseobacterium sp. CH2(AQUA), rank SPECIES, domain BACTERIA, parent `NCBITaxon:2593645` (unclassified Chryseobacterium). Its 13 root-first ancestors, EXACT grounding, SEEDED status, code 11, zero listed strains, single NCBI NAME attestation and seed event were checked. No synonyms, nomenclature, alternate mappings, genome links or experimental claims occur.

Identifier, full label and slug resolve one target. The separate Chryseobacterium sp. Ch2 concept and other short-name matches were considered only for identity exclusion, not reviewed as additional YAML records.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/chryseobacterium_sp_ch2_aqua.yaml` | Passed; no LinkML issues. |
| `just validate-strict data/taxa/bacteria/chryseobacterium_sp_ch2_aqua.yaml --out /private/tmp/ch2aqua-strict.tsv` | Passed; one file, zero errors; TSV header only. |
| Structured pinned-source comparison | Identity, rank, parent, genetic code, all ancestors, empty synonyms, attestation, slug, scope and seed provenance agree. |
| Exact status checks | No target child, type-material, merged-ID or dropped-ID row. |
| Current NCBI Taxonomy EFetch and Datasets | Identity, species rank, bacterial classification and complete carried lineage agree. |
| Exact-taxon sequence search | Assembly: zero with no-items/phrase-not-found warning. Nuccore: one record. |
| Nucleotide metadata | Complete non-sequence metadata of HQ872468.1 inspected. |

Not run: whole-corpus `just verify-corpus`, QC, provenance, product-label, rendering and documentation gates. The focused checks do not establish full-corpus reproduction. No curator-added ontology graph occurs. Ignored-inclusive bounded searches found no separate target history artifact; schema validation covered inline history shape.

## Identity and Grounding

NCBI explicitly assigns species rank to this unresolved `sp.` concept. Its strain-style designation does not justify changing that rank or inventing a formal binomial. EXACT is grounding to the NCBI concept, not a nomenclatural-validity claim. Current taxonomy agrees with the parent and all carried ancestor IDs, labels and ranks. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036178)

The pinned identity is `data/raw/ncbitaxon_taxa.tsv:222304`; the native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31831`. The distinct taxon 864706, Chryseobacterium sp. Ch2, has its own complete backbone and name objects at `data/raw/ncbitaxon_taxa.tsv:181990` and `data/catalog/ncbi_names-0004.jsonl.gz:35837`. No equivalence evidence was found that would merge it with CH2(AQUA).

## Evidence

The NCBITAXON attestation correctly records one NAME with the target ID/label and snapshot 2026-09-13. It is a source-name count, not a phenotype or genome count.

HQ872468.1 is a 1,550-base partial gyrB coding sequence. Its source specifies organism CH2(AQUA), strain CH2, host tilapia and taxon 1036178; the CDS uses code 11 and protein AEG74333.1. The inspected metadata carries neither culture-collection nor BioSample, BioProject or assembly links. Its research reference is labelled unpublished and a direct submission is present. That label does not prove no later publication exists. [GenBank HQ872468.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ872468.1)

Chenia's 2015 paper, DOI 10.4314/ajtcam.v12i3.7, includes a tilapia-associated CH2 row. Methods, Table 1 headers, row and footnotes were visually inspected on printed pages 56-59. Ampicillin/tetracycline zones are 0/14 mm, not MICs. The extracted paper contains neither HQ872468 nor gyrB. Matching author, host and designation provide a lead, but the accession-to-assay bridge remains unconfirmed. [Primary paper](https://journals.athmsi.org/index.php/ajtcam/article/download/2398/2160/9942)

No DOI, PMID, quotation, gene/protein assertion, trait or causal edge is present in the YAML. iModulonDB was not applicable to this identity-only record; the external marker annotation creates no expression-module claim.

## Completeness

The seven raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories contain no exact-target row. With no child taxa or established collection-deposit link, zero listed BacDive strains agrees with the model. It does not deny existence of the sequenced isolate.

Ignored-inclusive compressed-input searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Exact taxon/full-designation/slug terms produced three rows, all read in full. Expanding to bounded CH2, HQ872468 and AEG74333 produced 331 candidate addresses. Their identity and matching fields were screened; this was not a full biological review of every candidate. Target rows, the same-genus near match and the taxonomically unspecified StrainInfo candidate were read in full before disposition.

The latter is SI-ID 210848, with own deposit SI-DP 525140 / CCMP166 and alias Ch2, but no taxon in its native object. The primary collection identifies CCMP166 as Chaetoceros ceratosporum and explicitly lists CH2. This excludes it from the bacterial target without inventing taxonomy for the incomplete StrainInfo object. [NCMA CCMP166](https://ncma.bigelow.org/CCMP166)

Other candidates explicitly concern different genera, suffixed isolates, environmental clones or metagenomic bins. BacDive hits concern Halorubrum coriense and Agrobacterium fabacearum. The AllTheBacteria hit at `data/catalog/allthebacteria.tsv.xz:2869316` concerns Psychrobacter and SAMN40891036. No short-name, substring or cross-namespace number was accepted as a join.

Resolution additionally searched `data/taxa` and `reports`, including ignored files, with no previous target report. All five source metadata JSON files and history filenames were checked. Negative findings are bounded to those roots and exact-taxon queries, not all possible deposits or literature.

The marker and uncertain assay lead are optional enrichment, not missing required slots. Do not turn a partial gene into a genome or infer a collection deposit from CH2 alone.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the asserted identity, lineage, attestation or audit state. The unresolved literature bridge limits enrichment but does not undermine the current record.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Any later authorized enrichment should first establish an explicit accession-to-deposit or accession-to-assay relationship. A maintained input adapter, overlay or transformation in the relevant pipeline, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, owns future representation changes. Do not hand-edit the generated record or invent an identity bridge.

## Follow-up Checks

Resolve the primary accession-to-assay link before adding paper-derived phenotypes; retain assay conditions and measurement units. Test exclusion of taxon 864706 and unrelated CH2 deposits if introducing new matching logic.

For authorized input or generator changes, run the seed dry-run and `just seed-canary NCBITaxon:1036178`, inspect the biological diff and repeat both focused validators. Shared changes require the documented full-corpus, QC, provenance, product, rendering and documentation gates. No regeneration was performed here.

## Additional Notes

Scope: `curation/seed_scope.tsv:322555`, added 2026-09-13. Slug: `data/taxa/PATHS.tsv:14809`. Seed event remains `2026-09-13T17:54:04Z`.

Previously rendered local PDF pages were visually reinspected. No PDF artifact was authored, and no Eukaryota YAML was re-reviewed while excluding the CCMP candidate.

Reviewed HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Unchanged target SHA256: `b49e88305da1a785df1bf08376ae7ffd91cf8f133633c20dba985db835f44873`. Only this new Markdown report was added for the individual review. No YAML, history, lifecycle, source snapshot, GitHub or worktree changes occurred.
