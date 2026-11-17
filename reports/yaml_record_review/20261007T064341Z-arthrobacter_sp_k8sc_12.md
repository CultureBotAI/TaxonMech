# YAML Record Review: Arthrobacter sp. K8SC-12

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_k8sc_12.yaml`
- Started UTC: 2026-10-07T06:42:10Z
- Finished UTC: 2026-10-07T06:43:41Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035604`, Arthrobacter sp. K8SC-12, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:235627`, ten root-first ancestors and genetic code 11. It has `EXACT` grounding, `SEEDED` mapping status, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, strain deposits, genomes, definition, literature evidence, discussion, datasets, replacement or causal graph is asserted. K8SC-12 is a source strain-like placeholder designation, not a verified culture-collection accession.

The generated YAML is read-only. Future fixes belong to maintained source/extraction inputs or `src/taxonmech/seed.py` with tests; scope and slug ownership are `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`. No fix is required here.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/arthrobacter_sp_k8sc_12.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/arthrobacter_sp_k8sc_12.yaml --out /private/tmp/k812-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/k812-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, full lineage, scope, path, inventory and attestation comparisons | All bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Identity and ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata read. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not prove byte-for-byte reproduction.

`just validate-products` was not run: its configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded from that gate. The YAML has no literature or internal evidence references. The seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target history artifact; none is written by this review.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222132` agrees on identifier, exact label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31611` agrees. Path and scope are unique at `data/taxa/PATHS.tsv:14634` and `curation/seed_scope.tsv:322402`.

Every ancestor identifier, label, rank and position matches the committed parent chain. Live EFetch verifies the exact species label, parent 235627, code 11 and nine non-root ancestors. Datasets verifies the same chain including root. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035604&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035604)

The parent remains unclassified Arthrobacter. `EXACT` denotes this source concept, not a formally named species identification or equivalence to another K8SC isolate.

## Evidence

The `NCBITAXON` attestation agrees on source ID, exact label, count 1, unit `NAME` and snapshot note. No unlike units are summed. The complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Nuccore UID `334361533` is `JF799974.1`, a 1,506-nt partial 16S rRNA marker. Complete metadata explicitly identifies strain K8SC-12 and `taxon:1035604`, with soil isolation and India: Kafni Glacier as the geographic qualifier. It contains no culture-collection, assembly, BioSample or BioProject link. Submission is dated 11 April 2011; creation and update are 6 June 2011. Its bibliography lists an unpublished Kafni culturable-diversity study by Shivaji, Pratibha and Srinivas and a direct submission, without DOI or PMID. The marker is not a genome. [GenBank JF799974.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799974.1)

The related Kafni paper `PMID:21918795`, `DOI:10.1007/s00792-011-0398-8` was inspected as primary article HTML-extracted text in this session. Its complete eleven-isolate Table 3 does not list K8SC-12; a fresh exact-designation search of the extraction found no match. No exact connection to its tested cohort is established, so growth and enzyme results are not transferred. Supplements were not inspected and are outside this absence finding. [Primary article text](https://www.researchgate.net/publication/51644024_Comparison_of_bacterial_diversity_in_proglacial_soil_from_Kafni_Glacier_Himalayan_Mountain_ranges_India_with_the_bacterial_diversity_of_other_glaciers_in_the_world), [Publisher record](https://link.springer.com/article/10.1007/s00792-011-0398-8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21918795/)

The recent successful structured iModulonDB listing from this session was re-inspected, not re-fetched for this target: 28 dataset rows, none for Arthrobacter. No covered target or gene/regulator/omics claim occurs here. The adapter is not applicable; its absence is not negative phenotype evidence.

## Completeness

The zero BacDive strain count and optional omissions agree with the inspected inventories. A GenBank strain label is not an omitted BacDive deposit row. Literature evidence is optional for seeded records.

Two local search stages included ignored and hidden files and compressed catalogs using `rg --no-ignore --hidden -n -z -i`. Roots were `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full for each stage; history filenames were independently traversed.

The identity stage searched taxid 1035604, full label, slug and K8SC-12 separator/case variants. Exactly three lines matched: the full backbone, scientific-name and scope rows above. The second stage searched JF799974 with optional version, PMID 21918795 and the related DOI; no matches were found. Neither stage found matching metadata values or history paths. Absence claims include ignored files and are bounded to these roots and terms.

Web searches used the full label, K8SC-12 with Kafni context and verified accession JF799974. No additional exact-isolate primary experiment or deposit/genome chain was established. The exact-taxid Assembly zero includes a phrase-not-found warning and does not prove no genome exists under another identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. Identity, lineage, attestation, source count, lifecycle and optional omissions are supported within the inspected scope. An unestablished literature association is not evidence for adding experiments.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status; this review is not human sign-off. Future enrichment needs explicit identity evidence and maintained source/seeder support with tests. Phenotype and habitat evidence belongs in the appropriate sibling corpus.

## Follow-up Checks

- Establish explicit K8SC-12/JF799974 identity in primary text or supplements before attaching published experiments.
- Require an explicit culture-deposit/genome relationship; the marker alone is insufficient.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`. Full-corpus gates remain skipped here.

## Additional Notes

Primary taxonomy and nucleotide APIs succeeded. The related article was read as HTML extraction, not a visually verified PDF; supplements remain uninspected. No numerical phenotype or gene claim is inferred.

Seed wording agrees with scope and attestation. Its timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review time.

The whole target was reread unchanged before report creation. An ignored-independent filename search found no prior report for this stem. Only this new report is added; no generated record, inventory, page, prior report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
