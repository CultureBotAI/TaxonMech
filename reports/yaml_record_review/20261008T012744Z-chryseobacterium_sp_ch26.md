# YAML Record Review: Chryseobacterium sp. CH26

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/chryseobacterium_sp_ch26.yaml`
- Started UTC: 2026-10-08T01:22:18Z
- Finished UTC: 2026-10-08T01:27:44Z
- Verdict: pass

## Target

The entire 63-line generated `TaxonRecord` was read. It denotes Chryseobacterium sp. CH26, `NCBITaxon:1036175`, rank SPECIES, domain BACTERIA, parent `NCBITaxon:2593645` (unclassified Chryseobacterium). It carries 13 root-first ancestors, genetic code 11, EXACT grounding, SEEDED mapping status, zero listed BacDive strains, one NCBI NAME attestation and one seed event. No alternate mappings, synonyms, nomenclature, genome relationships, evidence passages or causal graph are asserted.

The identifier, full name and slug resolve one YAML. Other CH26 names were checked only as candidate source matches; no additional taxon YAML was reviewed.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/chryseobacterium_sp_ch26.yaml` | Passed; no LinkML issues. |
| `just validate-strict data/taxa/bacteria/chryseobacterium_sp_ch26.yaml --out /private/tmp/ch26-strict.tsv` | Passed; one file, zero errors; TSV is header-only. |
| Structured pinned-source comparison | Label, rank, parent, genetic code, all 13 ancestors, absent synonyms, NCBI attestation and inline seed provenance agree. |
| Exact inventory/status checks | Stable slug and scope agree; no target descendant, type-material, merged-ID or dropped-ID row found. |
| Public NCBI Taxonomy EFetch and Datasets | Current name, species rank, parent and lineage agree. |
| Exact-taxon Assembly and Nuccore searches | Zero assemblies, with a no-items/phrase-not-found warning; one nucleotide record. |
| Complete non-sequence nucleotide metadata | HQ872491.1 inspected, including source qualifiers, CDS identifiers and reference metadata. |
| Candidate source inspection | All 52 search-hit addresses read in full; no supported additional target relationship found. |

Not run: whole-corpus `just verify-corpus`, QC, source-provenance, product-label, rendering and documentation gates. Focused source comparisons do not establish whole-corpus reproduction. There is no curator-added ontology graph. No separate target history artifact was found in the bounded ignored-inclusive searches, so none was passed to the history validator; inline history shape was covered by schema validation.

The ATCC MYA-2456 page was unavailable through the web tool, and the PMC copy of its relevant paper showed a browser check. The research institute's public PDF was inspected instead, including a rendered page. This limitation concerns an excluded candidate, not an unresolved reference in the YAML.

## Identity and Grounding

NCBI explicitly assigns species rank to this unresolved `sp.` concept. CH26 being a strain-style designation does not override that authority rank or establish a formal binomial. EXACT means exact grounding to this NCBI taxon, not validated species nomenclature. The record preserves the unclassified parent and the intervening clade/no-rank nodes rather than reconciling taxonomy itself. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036175)

The matching pinned row is `data/raw/ncbitaxon_taxa.tsv:222301`; the source-native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31824`. Neither supplies an extra synonym, LPSN type designation or GTDB mapping. The current NCBI lineage identifiers match every ancestor in the generated record.

## Evidence

The NCBITAXON attestation, source ID and label, count 1, unit NAME and 2026-09-13 snapshot agree with the pinned inventory. The record makes no experimental claim from that count.

The exact-taxon nucleotide result is HQ872491.1, a 1,550-base partial gyrB coding sequence. The source qualifiers explicitly identify CH26, taxon 1036175 and host tilapia; its CDS uses translation table 11 and protein accession AEG74356.1. The inspected metadata contains no culture-collection, BioSample, BioProject or assembly link. The research reference is labelled unpublished in GenBank and is accompanied by a direct submission. This is bounded sequence-source evidence, not proof of a whole genome, disease causation or resistance mechanism. [GenBank HQ872491.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ872491.1)

Chenia's 2015 paper (DOI 10.4314/ajtcam.v12i3.7), inspected in this review session with Table 1 headers, footnotes and methods, includes a tilapia-associated CH26 row. Its ampicillin/tetracycline inhibition zones are 0/16 mm, not MICs. Neither HQ872491 nor gyrB was found in the extracted full text. The paper-to-accession identity remains unconfirmed; this is only an enrichment lead. [Primary paper](https://journals.athmsi.org/index.php/ajtcam/article/download/2398/2160/9942)

The YAML itself contains no DOI, PMID, evidence quotation, gene/protein claim, transcriptomic assertion or causal edge. iModulonDB was not applicable to this identity-only record. The externally discovered marker annotation does not create an expression-module claim, and database absence is not negative phenotype evidence.

## Completeness

No exact target row was found in the seven raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. There are no direct child taxa in the backbone. The zero BacDive strain count is therefore consistent with the source model; it does not mean that the sequence-bearing isolate never existed.

Ignored-inclusive compressed-input searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 1036175 and CH26, the slug, HQ872491 and AEG74356. All 52 addresses were inspected: three target rows (backbone, scientific name and scope), plus 49 other-name/deposit candidates.

Other CH26 genomes belong to Streptococcus, Rhizobium, Aliarcobacter, Salmonella, Mycoplasmopsis, Escherichia or an archaeon; suffixed CH26-1/2/3/6 labels also denote different taxa. They do not establish a genome link to this Chryseobacterium record.

Two StrainInfo rows omit taxonomy and were not accepted on designation alone:

- `data/straininfo/records.jsonl.gz:46869`: SI-ID 59213, CH26, deposit NCIMB 1937. NCIMB identifies its deposit as Pseudoalteromonas sp., isolated near Nice. This is not the target Chryseobacterium concept. [NCIMB collection account](https://www.ncimb.com/blog/around-the-world-in-80-strains-a-cheeseboard-in-france/)
- `data/straininfo/records.jsonl.gz:147166`: SI-ID 204327, CH26, deposit ATCC MYA-2456. The inspected taxonomic paper associates this accession and CH-26 with Exserohilum parlierense from Pistacia vera, explicitly noting that the holotype was not seen. This excludes a bacterial identity join; it is not an independent audit of the fungal deposit or its present nomenclature. The complete relevant section on printed page 101 was visually checked. [Taxonomic research paper](https://wi.knaw.nl/images/ResearchGroups/Phytopathology/pdf/2018HernandezExserohilum.pdf)

Resolution additionally searched `data/taxa` and `reports`, including ignored files, and found no prior target report or separate target history. All five source metadata JSON files and history filenames were checked. These absence statements are bounded by the stated roots and queries, not universal claims about all cultures, genomes or literature.

Neither the optional marker sequence nor an unconfirmed assay lead makes a required field missing. Do not invent a BacDive deposit or treat a partial gene as a genome identifier to add them.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the existing identity, lineage, source attestation or audit claims. The uncertain assay linkage and unavailable candidate ATCC page do not undermine the currently asserted YAML fields.

## Recommended Edits

None required. Preserve the generated YAML and its SEEDED status.

Any future authorized enrichment must first establish an explicit accession/deposit relationship. Source changes belong in the maintained inventory/overlay and its extractor; representation logic belongs in `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, with focused tests. A genuinely new representation would require a reviewed non-vendored schema extension, not a generated-record patch.

## Follow-up Checks

Before adding optional evidence, verify the primary link between the target accession and assay isolate; preserve condition and organism scope. Resolve deposits through their full collection accession, not a short designation, and retain marker/genome distinctions.

For a later authorized change, run the seed dry-run and `just seed-canary NCBITaxon:1036175`, inspect the biological diff and repeat both focused validators. Shared behavior changes also require the full documented corpus, QC, provenance, product, rendering and documentation gates. No regeneration was required for this read-only review.

## Additional Notes

The scope row is `curation/seed_scope.tsv:322553`, added 2026-09-13; the slug is `data/taxa/PATHS.tsv:14806`. The unchanged seed event is `2026-09-13T17:54:04Z`.

Relevant PDF pages were read using existing renders and a read-only macOS PDFKit render for the excluded ATCC candidate because Poppler was unavailable. No PDF artifact was authored or published.

Reviewed HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Unchanged target SHA256: `eae5841bf7cb8c0a8461cd206b4b9145de80078c8df0fe8b6d2e047ad01c2ad6`. Only this new Markdown report was added for this review. No YAML, source snapshot, lifecycle, history, GitHub or worktree mutation occurred, and no Eukaryota record was re-reviewed.

