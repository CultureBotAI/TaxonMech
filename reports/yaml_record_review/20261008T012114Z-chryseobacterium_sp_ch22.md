# YAML Record Review: Chryseobacterium sp. CH22

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/chryseobacterium_sp_ch22.yaml`
- Started UTC: 2026-10-08T01:16:26Z
- Finished UTC: 2026-10-08T01:21:14Z
- Verdict: pass

## Target

The entire 63-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1036174`, Chryseobacterium sp. CH22, rank SPECIES, domain BACTERIA, parent `NCBITaxon:2593645` (unclassified Chryseobacterium). The record has 13 root-first ancestors, grounding EXACT, mapping status SEEDED, genetic code 11, zero listed BacDive strains, one NCBI NAME attestation and one seed event. There are no synonyms, nomenclature entries, alternate mappings, genome links or experimental evidence assertions.

The full label, identifier and slug resolve one YAML. Other organisms carrying CH22 were inspected only to disambiguate source-search candidates; their YAML records were not reviewed.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/chryseobacterium_sp_ch22.yaml` | Passed; no LinkML issues. |
| `just validate-strict data/taxa/bacteria/chryseobacterium_sp_ch22.yaml --out /private/tmp/ch22-strict.tsv` | Passed; one file, zero errors; TSV contains only its header. |
| Pinned backbone comparison | Identity, rank, parent, code, all 13 ancestors and lack of synonyms agree. |
| Inventory and audit comparison | Source attestation, stable slug, scope and inline seed provenance agree. |
| Exact type/retirement checks | No target type-material, merged-ID or dropped-ID row. |
| Current public NCBI Taxonomy EFetch and Datasets | Identity, species rank, parent and lineage agree. |
| Exact-taxon NCBI sequence searches | Assembly returned zero, with a no-items/phrase-not-found warning; Nuccore returned one record. |
| Nucleotide source inspection | Complete non-sequence metadata for HQ872487.1 inspected. |

Not run: whole-corpus `just verify-corpus`, QC, source-provenance gates, rendering, documentation and product-label checks. The focused comparisons are not full-corpus reproduction. No curator-added ontology graph occurs here. Bounded ignored-inclusive searches found no separate target history artifact to pass to the history validator; schema validation covers the inline history structure.

## Identity and Grounding

Current NCBI calls this unresolved organism concept Chryseobacterium sp. CH22 and explicitly assigns species rank. An isolate-style label does not justify replacing that authority rank with STRAIN, nor does it establish a formally named species. EXACT describes grounding to the NCBI concept, not nomenclatural validity. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036174)

The current EFetch lineage and Datasets lineage identifiers support the record's chain, including the unclassified parent. The pinned backbone is `data/raw/ncbitaxon_taxa.tsv:222300`; its scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31823`. Neither supports a second name, type-strain flag or GTDB identity.

## Evidence

The sole source contribution is NCBITAXON, count 1, unit NAME, snapshot 2026-09-13. It matches the exact inventory row. A name count is not an experimental assertion, and the record does not conflate it with strains or genomes.

HQ872487.1 is a 1,550-base partial gyrB coding sequence whose source explicitly names CH22 and taxon 1036174, with host trout. The CDS uses code 11 and protein accession AEG74352.1. The complete inspected metadata contains no culture-collection, BioSample, BioProject or assembly link. Its research reference is labelled unpublished in GenBank, alongside a direct submission; that label is not a claim that no subsequent publication exists. A partial gene sequence does not establish a complete genome, resistance mechanism or pathogenicity. [GenBank HQ872487.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ872487.1)

A prospective literature lead is Chenia's 2015 paper, DOI 10.4314/ajtcam.v12i3.7. Methods and Table 1, including headers and footnotes on printed pages 56-59, were visually inspected. The study includes 36 Chryseobacterium isolates; its trout-associated CH22 row reports disk-diffusion zones, including 28/40 mm for the two cinnamaldehyde columns and 0/20 mm for ampicillin/tetracycline. These are not MICs. Author, isolate designation and host are consistent with the sequence submission, but the extracted full paper contains neither HQ872487 nor gyrB. An accession-to-assay bridge remains unconfirmed. The paper is an enrichment lead, not evidence of a defect in the present identity-only YAML. [Primary paper](https://journals.athmsi.org/index.php/ajtcam/article/download/2398/2160/9942)

There is no DOI, PMID, quoted passage, protein assertion, trait or causal edge in the YAML itself. iModulonDB was not applicable to this identity-only record; a gene annotation discovered externally does not create an expression-module assertion. No database absence was treated as biological negative evidence.

## Completeness

No exact target row occurs in the seven BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories. The backbone has no direct children. Zero listed BacDive strains is consistent with these inputs; it does not deny that a named isolate was sequenced.

Ignored-inclusive compressed-input searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Queries included bounded taxon ID 1036174, CH22, the slug, HQ872487 and AEG74352. All 55 candidate addresses were read in full: three target rows (backbone, scientific name and scope), and 52 other-name/deposit candidates. No supported extra target link resulted.

The candidates include CH22 genomes of Streptococcus, Staphylococcus, Salmonella, Mycoplasmopsis and other taxa, and the distinct designation CH22-21 of Aquihabitans daechungensis. None is a valid join on short designation alone.

One StrainInfo candidate needs explicit qualification: `data/straininfo/records.jsonl.gz:46868` links CH22 to SI-ID 59212 and deposit NCIMB 1936, but supplies no taxon. NCIMB's own account identifies NCIMB 1936 as Pseudoalteromonas ruthenica from coastal sediment near Nice. This resolves the collection candidate away from the Chryseobacterium target rather than treating missing StrainInfo taxonomy as a match. [NCIMB collection account](https://www.ncimb.com/blog/around-the-world-in-80-strains-a-cheeseboard-in-france/)

Record/report resolution additionally searched `data/taxa` and `reports`, including ignored files, and found no prior target report. All five source metadata JSON files and history filenames were checked. Absence statements are limited to these roots and the stated exact-taxon queries, not a universal census of publications, genomes or deposits.

The marker sequence and uncertain assay lead are optional enrichment, not required missing fields. Do not invent a BacDive strain entry or promote a partial gene to a genome identifier to accommodate them.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the record's asserted identity, lineage, source contribution or audit state. The unresolved paper-to-accession relationship limits prospective enrichment, not the existing verdict.

## Recommended Edits

None required. Leave the generated record and SEEDED status unchanged.

For any later authorized enrichment, establish the accession/deposit relationship first. Changes to source relationships belong in the maintained extractor or overlay, with representation logic in `src/taxonmech/extract.py` or `src/taxonmech/seed.py` and focused tests. A new representation outside the current model would also require a reviewed non-vendored schema change, not a hand-edited generated YAML or fabricated deposit.

## Follow-up Checks

Confirm a primary accession bridge before adding assay evidence. Preserve assay conditions and distinguish marker, genome, deposit and taxon identity. Neither gyrB annotation nor inhibition-zone measurements alone support a resistance mechanism.

After any authorized maintained-input change, run the documented seed dry-run, then `just seed-canary NCBITaxon:1036174`, inspect the biological diff and rerun the focused schema and strict validators. Shared behavior changes require the full documented corpus, QC, provenance, product, rendering and documentation gates before publication. No regeneration was necessary for this read-only review.

## Additional Notes

Scope admission is 2026-09-13 at `curation/seed_scope.tsv:322552`; the stable slug is at `data/taxa/PATHS.tsv:14805`. The seed event remains `2026-09-13T17:54:04Z`.

The paper's existing locally rendered pages were reinspected; the earlier read-only rendering used macOS PDFKit because Poppler was unavailable. No PDF artifact was authored.

Reviewed HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Target SHA256 remained `5a6c8f4d9f020fc9e9949c6eb5b45e1b46116b48c3eb8bb58bea80eebdcced05`. Only this new Markdown report was added for this review. No generated YAML, lifecycle, curation history, source snapshot, GitHub state, worktree or Eukaryota record was changed.

