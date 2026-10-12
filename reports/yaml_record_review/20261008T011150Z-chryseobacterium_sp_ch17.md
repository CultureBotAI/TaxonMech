# YAML Record Review: Chryseobacterium sp. CH17

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/chryseobacterium_sp_ch17.yaml`
- Started UTC: 2026-10-08T01:05:12Z
- Finished UTC: 2026-10-08T01:11:50Z
- Verdict: pass

## Target

The entire 63-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1036173`, `Chryseobacterium sp. CH17`, rank `SPECIES`, domain `BACTERIA`, with parent `NCBITaxon:2593645` (unclassified Chryseobacterium). The record is `EXACT`/`SEEDED`, contains 13 root-first ancestors, code 11, zero listed BacDive strains, one NCBI NAME attestation and one seed event. It has no synonyms, alternate mappings, nomenclature, genome links, evidence passages or causal graph.

The identifier and full label resolve one target. Other taxa using CH17 were inspected only as source-search candidates, not reviewed as additional YAML records.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/chryseobacterium_sp_ch17.yaml` | Passed; no LinkML issues. |
| `just validate-strict data/taxa/bacteria/chryseobacterium_sp_ch17.yaml --out /private/tmp/ch17-strict.tsv` | Passed; one file, zero errors; output TSV contains only its header. |
| Structured pinned-backbone comparison | Label, rank, domain, parent, genetic code, all 13 ancestors and absence of source synonyms agree. |
| Exact inventory, scope and index checks | NCBI attestation, scope row, stable slug and inline seed provenance agree. No descendant taxa or exact type-material, merged-ID or dropped-ID rows were found. |
| Public NCBI Taxonomy EFetch and Datasets | Current identity, species rank, parent and lineage agree with the record. |
| Exact-taxon NCBI searches | Assembly returned zero with a no-items/phrase-not-found warning; Nuccore returned one sequence. |
| Nucleotide metadata inspection | Complete non-sequence GenBank metadata for HQ872483.1 inspected. |

Not run: whole-corpus `just verify-corpus`, QC, source-provenance checks, product-label gates, rendering and documentation checks. The focused comparisons are not whole-corpus reproduction. No target-specific external history artifact was found in the bounded ignored-inclusive searches, so no external history file was passed to its validator. The inline history structure was covered by schema validation. No curator-added ontology graph is present.

## Identity and Grounding

NCBI explicitly assigns species rank to this unresolved `sp.` label. CH17 is an isolate-style designation, but that does not justify changing the authority's rank to STRAIN or assigning a formally named species. `EXACT` describes grounding to the NCBI concept, not valid publication of a binomial or certainty about species-level biological classification. The unclassified parent and intermediate clade/no-rank nodes are retained correctly. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036173)

The raw scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31822`; the matching backbone row is `data/raw/ncbitaxon_taxa.tsv:222299`. Neither supplies an additional synonym. The record appropriately avoids borrowing a nearby Chryseobacterium species name, a type-strain designation, or a GTDB mapping.

## Evidence

The sole asserted source contribution is NCBI, count 1, unit NAME, snapshot 2026-09-13. That matches the inventory exactly. The current taxonomy response supports the same identity and code. No experimental property is inferred from the count.

The one exact-taxon nucleotide record, HQ872483.1, is a 1,550-base partial gyrB coding sequence. Its source names CH17, taxon 1036173 and host trout; the CDS uses translation table 11 and protein accession AEG74348.1. Its research reference is labelled unpublished in GenBank, alongside a direct submission. This supports bounded sequence identity, not a whole genome, resistance mechanism, validated species assignment or proof of pathogenicity. It has no culture-collection, BioSample, BioProject or assembly link in the inspected metadata. [GenBank HQ872483.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ872483.1)

A prospective literature lead was inspected: Chenia's 2015 paper, DOI 10.4314/ajtcam.v12i3.7. Its methods and Table 1, including headers and footnotes on printed pages 56-59, were visually checked. Among 36 Chryseobacterium isolates, the trout-associated CH17 row reports inhibition zones, including 28 and 40 mm for the two displayed cinnamaldehyde concentrations and 0/20 mm in the ampicillin/tetracycline columns. These are disk-diffusion observations, not MICs or direct mechanism evidence. The author, isolate label and host are consistent with the sequence submission, but a search of the extracted full paper found no HQ872483 or gyrB reference. The accession-to-assay link remains unconfirmed; this is a follow-up lead, not an imported phenotype or a finding against the current YAML. [Primary paper](https://journals.athmsi.org/index.php/ajtcam/article/download/2398/2160/9942)

No quoted evidence passage, DOI, PMID, mechanism edge or protein assertion occurs in the YAML itself. The externally discovered gene annotation does not create an expression-module claim. iModulonDB was not applicable to this identity-only record; no absence from it was used as negative evidence.

## Completeness

The seven exact raw-source inventories contain no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. With no descendant taxa or eligible source-native deposit match, `strain_count: 0` is consistent with the model. It means no listed BacDive cultures, not that the sequenced isolate does not exist.

Ignored-inclusive compressed-input searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Queries included 1036173, the name/slug, bounded CH17, HQ872483 and AEG74348. All 65 candidate addresses were inspected: three target rows (backbone, scientific name and scope), and 62 other-organism or environmental-label matches. None supplied a supported additional link to this target.

For example, the CH17 genomes belonging to Streptococcus, Salmonella and other genera are different organisms. GOLD's viral and environmental CH17 labels are also not bacterial isolate identity evidence. No match was accepted solely on the short designation.

Record/report resolution additionally searched `data/taxa` and `reports`, including ignored files; no prior target report or separate history record was found. All five source metadata JSON files and history filenames were checked. These statements are limited to the specified roots and current exact-taxon searches, not universal claims that no genome, culture deposit or further literature exists.

The partial gene sequence and candidate assay paper are optional future enrichment, not missing required representation. Do not create an unsupported BacDive strain entry merely to attach a nucleotide accession, and do not treat a partial gyrB sequence as a genome identifier.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the record's present identity, lineage, attestation or audit claims. The uncertain literature-to-accession linkage limits prospective enrichment, not the existing record verdict.

## Recommended Edits

None required. Preserve the generated record and its SEEDED status.

If enrichment is later requested, first establish the paper-isolate-to-accession relationship and retain assay-specific scope. Any representation outside the existing source/deposit model needs a maintained-source or schema/seeder design, not a manual YAML patch or a fictitious deposit. Owners for an authorized change would be `src/taxonmech/extract.py`, `src/taxonmech/seed.py`, and, only if needed, the non-vendored local schema and focused tests.

## Follow-up Checks

For later curation, verify a stable deposit or primary accession bridge before adding genome/sequence or phenotype evidence. Recheck the exact NCBI concept rather than joining other CH17 labels. Do not infer a resistance mechanism from either gyrB annotation or inhibition zones.

After any authorized maintained-input change, use the documented seed dry-run and `just seed-canary NCBITaxon:1036173`, inspect the biological diff and rerun both focused validators. Broader shared changes require the full documented corpus, QC, provenance, product, rendering and documentation gates before publication. No regeneration was needed for this read-only pass.

## Additional Notes

The local PDF renderer fallback used macOS PDFKit because Poppler was unavailable; the relevant rendered pages were inspected. No PDF artifact was authored or published.

Scope admission is 2026-09-13 (`curation/seed_scope.tsv:322551`), and the unchanged seed event is `2026-09-13T17:54:04Z`. No lifecycle promotion, curation/history event, source refresh, GitHub mutation or Eukaryota re-review occurred.

Reviewed HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Target SHA256 before report creation: `7f365548378c0c8684dde7d9d8e9596ae5c81d22174636f2795cd719050e8394`. Only this new Markdown report was added to the repository for this review.
