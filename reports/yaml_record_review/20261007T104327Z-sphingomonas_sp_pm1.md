# YAML Record Review: Sphingomonas sp. PM1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sphingomonas_sp_pm1.yaml`
- Started UTC: 2026-10-07T10:37:29Z
- Finished UTC: 2026-10-07T10:43:27Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:103581`, Sphingomonas sp. PM1, `SPECIES`, `BACTERIA`, parent `NCBITaxon:196159`, ten root-first ancestors, genetic code 11, `EXACT`, `SEEDED`, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, mappings, strains/deposits, genomes, definition, literature evidence, datasets or causal graph are asserted. The record denotes the pinned NCBI concept, not every isolate called PM1. Generated YAML is read-only. Maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py` own future extraction/harmonization fixes; `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` own scope and slug changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/sphingomonas_sp_pm1.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/sphingomonas_sp_pm1.yaml --out /private/tmp/sphingoPM1-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/sphingoPM1-strict.tsv` | Header only. |
| Complete backbone/lineage, seven inventory, scope/path and attestation comparisons | Bounded comparisons passed. |
| Type-material, merged-ID and dropped-record scans | No exact target rows. |
| Live NCBI EFetch and Datasets | Identifier, label, parent, rank, code and ancestry agree. |
| Exact-taxid Assembly/nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1. |
| GenBank metadata and linked publications | Target marker and alternate PM1 marker fully read excluding sequence payloads; primary abstracts inspected. |
| Entire target reread | Byte-identical to initial read. |

Not checked: full-corpus `just verify-corpus`, `just qc`, schema-all, tests, provenance hashing, generated-page drift, documentation statistics and vendored gates. Focused comparisons are not substitutes for those checks.

`just validate-products` was not run: no curator-added graph nodes exist and OAK excludes NCBI taxonomy. There are no YAML literature or internal evidence references to validate. The embedded seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target history artifact in the bounded roots below.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:18511` agrees on identifier, label, rank, parent, genetic code, empty synonyms and snapshot 2026-09-13. The complete native scientific-name row is `data/catalog/ncbi_names-0000.jsonl.gz:38519`. The unique path/scope rows are `data/taxa/PATHS.tsv:14676` and `curation/seed_scope.tsv:144157`.

All ancestor IDs, labels, ranks and ordering agree: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Sphingomonadales, Sphingomonadaceae, Sphingomonas and unclassified Sphingomonas. Live EFetch confirms the non-root chain, parent 196159, species rank, division Bacteria and code 11; Datasets includes root. No alternate names are supplied. The inspected lifecycle inventories contain no target merge, retirement or type-material row. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103581&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103581)

The unclassified parent is carried NCBI placement. `EXACT` describes identity to that source concept, not validation of the historical isolate identification. A consequential external attribution ambiguity is preserved below rather than silently reconciled.

## Evidence

The sole NCBI attestation agrees on identifier, label, count 1, unit `NAME` and snapshot. Complete backbone scanning found no direct children. Exact scans found no target rows in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore returned UID 5918671, `AF146635.1`: 1006 nt, partial 16S at both ends, strain PM1 and explicit `taxon:103581`. Submission was 28 April 1999, creation 22 September 1999 and last update 30 May 2001. The source note describes an MTBE-degrading environmental isolate. Full metadata, excluding nucleotide/translation/transcription payloads, contain no culture-collection, assembly, BioSample or BioProject crosslink. GenBank cites Hanson, Ackerman and Scow's 1999 article, PMID 10543787. [GenBank AF146635.1](https://www.ncbi.nlm.nih.gov/nuccore/AF146635.1)

The complete 1999 PubMed abstract and citation confirm DOI `10.1128/AEM.65.11.4788-4792.1999`. The study reports MTBE utilization and mineralization by a compost-biofilter isolate called PM1. These experimental results are about that study's culture; the abstract does not settle the identity of the old Sphingomonas sequence. Full article text was not obtained: PMC browser access presented a challenge, Europe PMC fullTextXML returned HTTP 500, and NCBI's article XML exposed the title/abstract without a body. [PubMed 10543787](https://pubmed.ncbi.nlm.nih.gov/10543787/)

The complete abstract of Bruns et al. 2001, PMID 11321538, DOI `10.1046/j.1462-2920.2001.00184.x`, places the MTBE-degrading PM1 isolate in a distinct lineage of the Leptothrix subgroup of Betaproteobacteria, using nearly full-length 16S and ribosomal spacer evidence. It also describes nonspecific products in T/DGGE profiling. PubMed associates both AF146635 and AF176594 with this paper. The later placement differs from the current alphaproteobacterial AF146635 annotation. The full 2001 article was not obtained, so the precise historical sample or amplification explanation remains unresolved; neither contamination nor sequence replacement is asserted. [PubMed 11321538](https://pubmed.ncbi.nlm.nih.gov/11321538/)

The alternate record `AF176594.1`, UID 6063088, was read in full excluding sequence payloads. It is 2208 nt comprising partial 16S, complete intergenic spacer and partial 23S, annotated as Methylibium petroleiphilum PM1, `taxon:420662`, compost biofilter, and type strain. It links the 2001 paper and the 2006 species description, PMID 16627642 / DOI `10.1099/ijs.0.63524-0`. The publisher's complete abstract of that description places PM1 in Betaproteobacteria and names ATCC BAA-1232 and LMG 22953 as its type-strain deposits. Those names do not create a verified deposit link to taxon 103581. [GenBank AF176594.1](https://www.ncbi.nlm.nih.gov/nuccore/AF176594.1), [2006 species description](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.63524-0)

The local backbone independently retains Methylibium petroleiphilum PM1 as a separate strain concept, `NCBITaxon:420662`, at `data/raw/ncbitaxon_taxa.tsv:92277`; its path row is `data/taxa/PATHS.tsv:499765`. This is context for non-conflation, not a second record review. No inspected authority merges 103581 into 420662. TaxonMech's carried-lineage rule does not authorize relabeling or reparenting the first concept from a shared strain designation. The target YAML itself asserts neither MTBE degradation nor equivalence to the Methylibium culture.

The broader local search's non-target matches were examined as typed identity/matched-field projections. Important distinctions are Sphingomonas sp. PM14 (taxid 279884), Gluconobacter wancherniae NBRC 103581 (taxid 656744), Cronobacter muytjensii CIP 103581 (taxid 413501), and BacDive ID 103581, which belongs to Rhodococcus sp. (taxid 194249). Other hits include unrelated sequence/run accessions, isolate names and numeric assembly statistics. The BacDive SOURCE metadata match is a request for BacDive ID 103581, not an NCBI taxid assertion. None provides a target deposit or genome chain.

The seed event matches the scope reason and NCBI-only source list. Fresh manifest reads give raw 2026-09-13T17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z; the inspected seeder chooses the latest of those extraction times. The event's 17:54:04Z is consistent without a target ATB association. No review event or status promotion was made.

iModulonDB is not applicable to the assertions under review: no regulator, functional gene, pathway or transcriptomic module is asserted. A transcriptomic paper about Methylibium PM1 is not evidence for this distinct NCBI concept without resolving identity first.

## Completeness

No consequential missing required representation was demonstrated. `strain_count: 0` counts BacDive source records in the taxon subtree, not every laboratory isolate with a name. The partial marker is not a genome. Optional literature, definitions and causal graphs should not be filled from unresolved historical attribution.

Local searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored/hidden files and compressed catalogs. The broad taxid/name/slug search returned 206 rows. All were parsed and their identity/matched-field projections inspected; this is not a claim that every unrelated full source record was read. Target backbone, native name and scope rows, plus neighboring backbone/name/scope rows used for disambiguation, were read in full.

The refined whole-designation/slug and AF146635 with optional .1 search returned only the same three target rows. No marker-accession hit occurred in those bounded roots. At both stages all five excluded `SOURCE.json` files were fully parsed and history filenames independently traversed. The expanded metadata search found no target hit; no target history filename was found. An ignored-independent traversal found no previous report for this stem before creation.

Exact-taxid Assembly returned zero with a phrase-not-found warning, which does not exclude assemblies under other classifications. Exhaustive literature/supplement retrieval, sequence alignment and independent phylogenetic analysis were not performed. The historical relationship between the two PM1 accessions is an unresolved enrichment constraint, not evidence that the generated YAML disagrees with its declared source.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the inspected YAML and committed-inventory contract. Identity, lineage, attestation, BacDive count and seed event agree. The pass is limited to those assertions; the historical PM1 attribution conflict is not considered resolved or suitable for phenotype/deposit transfer.

## Recommended Edits

None required to the current generated record. Preserve the complete label, NCBI placement and `SEEDED` status. Do not import MTBE phenotypes, ATCC BAA-1232, LMG 22953 or Methylibium genome data through a bare PM1 match.

Before enrichment, resolve the historical AF146635/AF176594 relationship from the full 2001 paper and authoritative accession/taxonomy history. Any confirmed identity correction belongs upstream with NCBI and in the maintained source-refresh path; do not manually reconcile the lineage in YAML.

## Follow-up Checks

Retrieve the full 2001 study and accession revision/provenance records. Establish which biological material each accession represents and whether the authority has an explicit merge or correction. Preserve conflicting source statements until that chain is demonstrated.

For an authorized source change, repeat NCBI identity/lineage and exact Assembly/nuccore queries, inspect updated inventories, run `just seed` and an authorized `just seed-canary NCBITaxon:103581`, inspect the complete emitted YAML and repeat focused schema/strict validation. Then run `just verify-corpus` and `just qc`. No regeneration was performed here.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Current tracked state and unchanged guidance/schema/seeder files were checked; the justfile and target were reread. The final target bytes match the initial read.

An initially combined diagnostic display was truncated; complete stored candidate projections were subsequently grouped and inspected in two untruncated slices covering all 206 rows. Source fields omitted by those deliberate projections were not used as evidence. Failed full-text retrieval attempts are recorded above, not treated as inspected article bodies.

This new report is the only repository write for this exact-record review. No YAML, inventories, prior reports, history/status, generated pages, worktrees or GitHub items were changed.
