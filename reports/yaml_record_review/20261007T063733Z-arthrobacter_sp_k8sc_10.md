# YAML Record Review: Arthrobacter sp. K8SC-10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_k8sc_10.yaml`
- Started UTC: 2026-10-07T06:35:38Z
- Finished UTC: 2026-10-07T06:37:33Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035602`, Arthrobacter sp. K8SC-10. It carries rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:235627`, ten root-first ancestors, genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, mappings, strain deposits, genomes, definition, literature evidence, discussion, datasets, replacement or causal graph is asserted. K8SC-10 is part of the source placeholder label, not a verified culture-collection accession.

The generated YAML is read-only. Future corrections belong to maintained source/extraction inputs or `src/taxonmech/seed.py` with tests; scope and slug changes belong to `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`. None is needed for this review.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` with offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/arthrobacter_sp_k8sc_10.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/arthrobacter_sp_k8sc_10.yaml --out /private/tmp/k810-strict.tsv` | Exit 0; one file scanned, zero ERROR rows. |
| `cat /private/tmp/k810-strict.tsv` | Actual TSV read; header only. |
| Structured source, full lineage, scope, path and attestation comparisons | All bounded comparisons passed. |
| Exact scans of type material, merged IDs and dropped records | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Identity and ancestry agree. |
| Exact-taxid Assembly and nuccore queries | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata read. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. The bounded source comparisons do not prove full-corpus reproduction.

`just validate-products` was not run: the configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded from that gate. There are no literature or internal evidence references in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target history artifact, and this read-only review writes none.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222130` agrees on identifier, exact label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31609` agrees. Unique path and scope rows occur at `data/taxa/PATHS.tsv:14632` and `curation/seed_scope.tsv:322400`.

All ten ancestor identifiers, labels, ranks and positions match the committed parent chain. Live EFetch confirms taxid 1035602, the exact label, species rank, parent 235627, code 11 and nine non-root ancestors. Datasets confirms the same chain including root. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035602&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035602)

The parent remains unclassified Arthrobacter. `EXACT` is exact grounding to this source concept, not a formal species-name determination or equivalence to another K8SC isolate.

## Evidence

The sole `NCBITAXON` attestation agrees on source ID, exact label, count 1, unit `NAME` and snapshot note. No unlike units are summed. A complete backbone scan found no direct children. Exact target scans found no row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Nuccore UID `334361531` is `JF799972.1`, a 1,500-nt partial 16S rRNA marker. The complete metadata identifies Arthrobacter sp. K8SC-10, strain K8SC-10 and `taxon:1035602`; its source qualifiers specify soil and India: Kafni Glacier. There are no culture-collection, assembly, BioSample or BioProject links in that metadata. Submission is dated 11 April 2011; creation and update are 6 June 2011. Its references are an unpublished Kafni culturable-diversity study by Shivaji, Pratibha and Srinivas and a direct submission, without DOI or PMID. This is a marker, not a genome. [GenBank JF799972.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799972.1)

A related published Kafni study is `PMID:21918795`, `DOI:10.1007/s00792-011-0398-8`. The primary article's complete eleven-isolate Table 3 and nearby results were inspected as HTML-extracted text in this session. K8SC-10 is not listed, and a fresh exact-designation search of the extraction found no match. Supplements were not inspected, so the finding is limited to the inspected text. No exact association with the tested cohort is established; growth and enzyme results are not transferred to this record. [Primary article text](https://www.researchgate.net/publication/51644024_Comparison_of_bacterial_diversity_in_proglacial_soil_from_Kafni_Glacier_Himalayan_Mountain_ranges_India_with_the_bacterial_diversity_of_other_glaciers_in_the_world), [Publisher record](https://link.springer.com/article/10.1007/s00792-011-0398-8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21918795/)

The recent successful structured iModulonDB listing from this session was re-inspected, not re-fetched for this target: 28 dataset rows and none for Arthrobacter. No covered target or gene/regulator/omics claim occurs here. The adapter is not applicable; absence from it is not negative phenotype evidence.

## Completeness

The zero BacDive strain count and optional omissions agree with the inspected inventories. A GenBank strain label is not an omitted BacDive deposit. Record-level literature evidence is optional for seeded records.

Two local search stages included ignored and hidden files and compressed catalogs with `rg --no-ignore --hidden -n -z -i`. Roots were `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full for each stage, and history filenames independently traversed.

The identity stage searched taxid 1035602, full label, slug and K8SC-10 separator/case variants. Exactly three lines matched: the backbone, native scientific name and scope rows above, all read in full. No additional target source-native strain, genome or deposit record was established in the searched roots.

The accession/citation stage searched JF799972 with optional version, PMID 21918795 and the related DOI. No matches were found. Neither stage found matching source metadata values or history paths. These absence claims include ignored files and are bounded to the stated roots and terms.

Web searches used the exact label, K8SC-10 with Kafni context and verified accession JF799972. No additional exact-isolate primary experiment or deposit/genome chain was established. The exact-taxid Assembly zero includes a phrase-not-found warning and does not prove no genome exists under another identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. Identity, lineage, attestation, source count, lifecycle and optional-field omissions are supported within the inspected scope. An unestablished relationship to a published cohort is not evidence for adding experiments.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status; this report is not human sign-off.

Future enrichment requires explicit deposit or genome identity evidence. Phenotype and habitat assertions belong in the appropriate sibling corpus. Any authorized TaxonMech addition needs maintained source/seeder support and tests, not a manual generated-YAML patch.

## Follow-up Checks

- Before attaching experimental evidence, establish explicit K8SC-10/JF799972 identity in inspected primary text or supplements; other Kafni isolates are not substitutes.
- Require an explicit culture-deposit/genome relationship before adding a genome link; the 16S sequence alone does not provide it.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`; full-corpus gates remain skipped here.

## Additional Notes

Primary taxonomy and nucleotide APIs succeeded. The related article was read as HTML extraction, not a visually verified PDF. Supplements remain uninspected; no numerical phenotype or gene claim is inferred.

Seed wording agrees with scope and attestation. The timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review time.

The entire target was reread unchanged before report creation. An ignored-independent filename search found no previous report for this stem. Only this new report is added; no generated record, inventory, page, prior report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
