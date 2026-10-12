# YAML Record Review: Arthrobacter sp. K8SC-11

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_k8sc_11.yaml`
- Started UTC: 2026-10-07T06:39:19Z
- Finished UTC: 2026-10-07T06:41:06Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035603`, Arthrobacter sp. K8SC-11, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:235627`, ten root-first ancestors and genetic code 11. It has `EXACT` grounding, `SEEDED` mapping status, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, strain deposits, genomes, definition, literature evidence, discussion, datasets, replacement or causal graph is asserted. The strain-like suffix is part of an NCBI placeholder name, not a verified culture accession.

This generated YAML is read-only. Future fixes belong to maintained source/extraction inputs or `src/taxonmech/seed.py` with tests; scope and slug ownership are `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`. No fix is required here.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/arthrobacter_sp_k8sc_11.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/arthrobacter_sp_k8sc_11.yaml --out /private/tmp/k811-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/k811-strict.tsv` | Actual TSV inspected; header only. |
| Structured backbone, full lineage, scope, path, inventory and attestation comparisons | All bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Identity and ancestry agree. |
| Exact-taxid Assembly and nuccore queries | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata read. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not prove byte-for-byte corpus reproduction.

`just validate-products` was not run: it targets curator-added graph nodes, absent here, and excludes NCBI taxonomy from OAK resolution. There are no literature or internal evidence references in the YAML. The seed event was checked; `just validate-history` was not run because ignored-independent content/path searches found no target history artifact, and this review creates none.

## Identity and Grounding

The full row at `data/raw/ncbitaxon_taxa.tsv:222131` agrees on taxid, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31610` agrees. The unique path and scope rows are `data/taxa/PATHS.tsv:14633` and `curation/seed_scope.tsv:322401`.

All ten ancestors match the committed parent chain in identifier, label, rank and order. Live EFetch resolves the exact label at species rank, parent 235627 and code 11, with nine non-root ancestors. Datasets confirms the same ancestry including root. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035603&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035603)

The parent remains unclassified Arthrobacter. `EXACT` denotes this source concept, not a formal species-name determination or equivalence to another K8SC isolate.

## Evidence

The sole `NCBITAXON` attestation agrees on source ID, exact label, count 1, unit `NAME` and snapshot note. Unlike units are not summed. The backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Nuccore UID `334361532` resolves to `JF799973.1`, a 1,504-nt partial 16S rRNA marker. Complete metadata explicitly identifies strain K8SC-11 and `taxon:1035603`, with soil isolation and India: Kafni Glacier as the geographic qualifier. It contains no culture-collection, assembly, BioSample or BioProject link. Submission is dated 11 April 2011; creation and update are 6 June 2011. Its references are an unpublished Kafni culturable-diversity study by Shivaji, Pratibha and Srinivas and a direct submission, without DOI or PMID. The marker is not a genome. [GenBank JF799973.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799973.1)

The related Kafni paper `PMID:21918795`, `DOI:10.1007/s00792-011-0398-8` was inspected as primary article HTML-extracted text. Its complete eleven-isolate Table 3 does not include K8SC-11; a fresh exact-designation search of the extraction found no match. No exact connection to the experimental cohort is established, so its growth and enzyme results are not transferred. Supplements were not inspected and are outside this absence claim. [Primary article text](https://www.researchgate.net/publication/51644024_Comparison_of_bacterial_diversity_in_proglacial_soil_from_Kafni_Glacier_Himalayan_Mountain_ranges_India_with_the_bacterial_diversity_of_other_glaciers_in_the_world), [Publisher record](https://link.springer.com/article/10.1007/s00792-011-0398-8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21918795/)

The recent successful structured iModulonDB listing from this session was re-inspected, not re-fetched for this target: 28 dataset rows, none for Arthrobacter. There is no covered target or gene/regulator/omics claim here. The adapter is not applicable; its absence supplies no negative phenotype evidence.

## Completeness

The zero BacDive strain count and optional omissions agree with the inspected inventories. A GenBank strain designation is not a missing BacDive deposit. Literature evidence is optional for seeded records.

Two ignored-independent searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed catalogs. All five excluded `SOURCE.json` files were parsed in full separately for each stage; history filenames were independently traversed.

The identity stage searched taxid 1035603, full label, slug and K8SC-11 separator/case variants. Exactly three lines matched: the full backbone, scientific-name and scope rows above. The second stage searched JF799973 with optional version, PMID 21918795 and its DOI; it found no matches. Neither stage found matching metadata values or history paths. Absence claims include ignored files and are bounded to these roots and terms.

Web searches used the full label, K8SC-11 with Kafni context and verified accession JF799973. No additional exact-isolate primary experiment or deposit/genome chain was established. The exact-taxid Assembly zero has a phrase-not-found warning and is not proof that no genome exists under another identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. Identity, lineage, attestation, source count, lifecycle and optional omissions are supported within the inspected scope. The unestablished publication association does not justify new claims.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status; this report is not human sign-off. Any later enrichment needs explicit identity evidence and maintained source/seeder support with tests. Phenotype and habitat evidence belongs in the appropriate sibling corpus.

## Follow-up Checks

- Establish explicit K8SC-11/JF799973 identity in primary text or supplements before attaching published experiments.
- Require a source-supported culture-deposit/genome chain; the 16S marker alone is insufficient.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`. Full-corpus gates remain skipped here.

## Additional Notes

Primary taxonomy and nucleotide APIs succeeded. The related article was inspected as HTML extraction, not a visually verified PDF; supplements were not inspected. No numerical phenotype or gene claim is inferred.

Seed wording agrees with scope and attestation. The timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date.

The whole target was reread unchanged before report creation. An ignored-independent filename search found no previous report for this stem. Only this report is added; no generated record, inventory, page, prior report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
