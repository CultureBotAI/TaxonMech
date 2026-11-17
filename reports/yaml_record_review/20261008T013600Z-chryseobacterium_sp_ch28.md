# YAML Record Review: Chryseobacterium sp. CH28

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/chryseobacterium_sp_ch28.yaml`
- Started UTC: 2026-10-08T01:30:27Z
- Finished UTC: 2026-10-08T01:36:00Z
- Verdict: pass

## Target

The entire 63-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1036176`, Chryseobacterium sp. CH28, rank SPECIES, domain BACTERIA, parent `NCBITaxon:2593645` (unclassified Chryseobacterium). Its 13 root-first ancestors, code 11, EXACT grounding, SEEDED status, zero BacDive strains, single NCBI NAME attestation and seed event were inspected. No synonyms, nomenclature, alternate mappings, genome relationships or experimental claims occur.

Identifier, full label and slug resolve one target. Other organisms using CH28 were inspected as source candidates only, not reviewed as additional YAML records.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/chryseobacterium_sp_ch28.yaml` | Passed; no LinkML issues. |
| `just validate-strict data/taxa/bacteria/chryseobacterium_sp_ch28.yaml --out /private/tmp/ch28-strict.tsv` | Passed; one file, zero errors; TSV header only. |
| Structured pinned-source comparison | Identity, rank, parent, code, all ancestors, absent synonyms, attestation, slug, scope and inline provenance agree. |
| Exact status/inventory checks | No child, type-material, merged-ID or dropped-ID row for the target. |
| Public NCBI Taxonomy EFetch and Datasets | Current identity, rank, parent and lineage agree. |
| Exact-taxon sequence searches | Assembly: zero with no-items/phrase-not-found warning. Nuccore: one record. |
| Nucleotide metadata | Complete non-sequence metadata for HQ872493.1 inspected. |
| Candidate source inspection | All 75 search-hit addresses read in full. |

Not run: whole-corpus `just verify-corpus`, QC, provenance, product-label, rendering and documentation gates. Focused comparisons are not whole-corpus reproduction. No curator-added ontology graph occurs. Bounded ignored-inclusive searches found no separate target history artifact to validate; schema validation covered inline history shape.

## Identity and Grounding

Current NCBI explicitly assigns species rank to this unresolved `sp.` concept. A strain-style designation alone does not warrant changing that authority rank or assigning a formal binomial. EXACT describes grounding to the NCBI concept, not nomenclatural validity. Both current lineage responses support the record's carried hierarchy, including the unclassified parent. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036176)

The matching backbone row is `data/raw/ncbitaxon_taxa.tsv:222302`; the native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31825`. Neither provides an additional synonym, LPSN type designation or GTDB mapping.

## Evidence

The NCBITAXON attestation correctly records count 1, unit NAME, snapshot 2026-09-13 and the exact target ID/label. It is an upstream name count, not a phenotype or genome assertion.

HQ872493.1 is a 1,553-base partial gyrB coding sequence. Its source explicitly identifies CH28, taxon 1036176 and host tilapia. The CDS uses code 11 and protein accession AEG74358.1. The inspected metadata has no culture-collection, BioSample, BioProject or assembly link. A research reference labelled unpublished and a direct submission are present; that label is not proof that no later publication exists. Neither a complete genome nor a resistance mechanism follows from this marker annotation. [GenBank HQ872493.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ872493.1)

Chenia's 2015 paper, DOI 10.4314/ajtcam.v12i3.7, contains a tilapia-associated CH28 row. Methods, Table 1 headers and the row/footnotes were visually inspected on printed pages 56, 57 and 59. The ampicillin/tetracycline zones are 0/15 mm, not MICs. The extracted full paper contains neither HQ872493 nor gyrB. Consistent author, host and designation suggest a lead, but an accession-to-assay bridge remains unconfirmed. [Primary paper](https://journals.athmsi.org/index.php/ajtcam/article/download/2398/2160/9942)

The YAML itself has no DOI, PMID, quotation, gene/protein assertion, trait or causal edge. iModulonDB was not applicable to this identity-only record; the external marker annotation does not create an expression-module claim. No database absence was interpreted as negative biological evidence.

## Completeness

The seven raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories contain no exact target row. With no child taxa or eligible deposit evidence, zero listed BacDive strains is consistent with the model. It does not deny the existence of the sequenced isolate.

Ignored-inclusive compressed-input searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 1036176 and CH28, the slug, HQ872493 and AEG74358. All 75 addresses were inspected: three target rows (backbone, name and scope) and 72 non-target name/numeric candidates. No additional supported target link resulted.

Important exclusions:

- SI-ID 59724 / NCIMB 9414 explicitly denotes Janthinobacterium lividum, while SI-ID 61461 / NCIMB 701643 and NCDO1643 denotes Enterococcus faecium. Their short-designation matches do not link them to this target.
- `data/catalog/allthebacteria.tsv.xz:1543382` names Mycolicibacterium sp. CH28 and sample SAMN10867835, consistent with that organism's separate genome/source chain, not taxon 1036176.
- A GTDB metadata hit for 1036176 is `ncbi_contig_n50` on GCA_963835215.1, not its taxon ID. Its stated taxon is 91750.
- Other CH28 genomes and suffixed names belong to different genera or organism concepts. No short-name or substring join was accepted.

Resolution also searched `data/taxa` and `reports`, including ignored files, and found no prior target report or separate history artifact. All five source metadata JSON files and history filenames were checked. Absence statements are limited to the stated roots and exact-taxon queries, not all possible deposits, genomes or publications.

The optional marker and uncertain assay lead are not missing required representation. Do not invent a BacDive deposit or turn a partial gene into a genome identifier.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the record's asserted identity, lineage, source contribution or audit state. The unconfirmed literature relationship limits optional enrichment, not the current verdict.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Any authorized enrichment must first establish an explicit primary accession/deposit bridge. Maintained source or overlay changes and their transformations belong in the relevant input pipeline, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, with focused tests. A new representation outside the current model needs a reviewed non-vendored schema change, not a direct YAML patch.

## Follow-up Checks

Before adding assay evidence, resolve the sequence-to-isolate relationship and preserve condition-specific scope. Keep taxon, marker, genome and culture-deposit identities distinct.

For later authorized changes, run the seed dry-run and `just seed-canary NCBITaxon:1036176`, inspect the biological diff and repeat both focused validators. Shared behavior changes require the full documented corpus, QC, provenance, product, rendering and documentation gates. No regeneration was needed here.

## Additional Notes

Scope: `curation/seed_scope.tsv:322554`, added 2026-09-13. Slug: `data/taxa/PATHS.tsv:14807`. Seed event unchanged: `2026-09-13T17:54:04Z`.

Existing local PDF renders were reinspected; their earlier read-only generation used macOS PDFKit because Poppler was unavailable. No PDF artifact was authored or published.

Reviewed HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Unchanged target SHA256: `24b9d2b4bdf0b50290d2f7635785f71f837c3799e14ba3a7b48fde07f3052d94`. Only this new Markdown report was added for this review. No YAML, history, lifecycle, source snapshot, GitHub or worktree change occurred; Eukaryota was not re-reviewed.

