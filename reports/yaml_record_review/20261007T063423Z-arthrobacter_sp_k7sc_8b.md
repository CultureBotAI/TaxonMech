# YAML Record Review: Arthrobacter sp. K7SC-8B

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_k7sc_8b.yaml`
- Started UTC: 2026-10-07T06:32:36Z
- Finished UTC: 2026-10-07T06:34:23Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035601`, Arthrobacter sp. K7SC-8B: rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:235627`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` mapping status. It contains one NCBI name attestation, `strain_count: 0` and one seed event.

No synonyms, nomenclature, taxonomy mappings, strain deposits, genomes, definition, literature evidence, datasets, discussion, replacement or causal graph is asserted. The K7SC-8B suffix is part of a source placeholder name, not a culture-collection accession.

The YAML is generated and read-only. Future fixes belong to maintained source/extraction inputs or `src/taxonmech/seed.py` with tests; scope and slug changes belong to `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`. No fix is required here.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/arthrobacter_sp_k7sc_8b.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/arthrobacter_sp_k7sc_8b.yaml --out /private/tmp/ar8-strict.tsv` | Exit 0; one file scanned, zero ERROR rows. |
| `cat /private/tmp/ar8-strict.tsv` | Actual TSV inspected; header only. |
| Structured backbone, complete lineage, scope, path and source comparisons | All bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Identity and ancestry agree. |
| Exact-taxid Assembly and nuccore queries | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata read. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons are not proof of corpus reproduction.

`just validate-products` was not run: its configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded from that gate. No literature or internal evidence references occur in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content and path searches found no target history artifact; none is created by this review.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222129` agrees on taxid, exact label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The full scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31608` agrees. Path and scope are unique at `data/taxa/PATHS.tsv:14631` and `curation/seed_scope.tsv:322399`.

Every ancestor identifier, label, rank and position matches the committed parent chain. Live EFetch resolves the exact species label, parent 235627, code 11 and nine non-root ancestors. Datasets confirms the same ancestry including root. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035601&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035601)

The parent is unclassified Arthrobacter. `EXACT` denotes this source concept, not a formally named species identification or equivalence to Acinetobacter K7SC-8A or another Kafni isolate.

## Evidence

The `NCBITAXON` attestation agrees on source ID, exact label, count 1, unit `NAME` and snapshot. Unlike units are not summed. The backbone scan found no direct children. Exact scans found no target rows in the seven maintained inventories `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` and `bactotraits_taxa.tsv`.

Nuccore UID `334361520` resolves to `JF799961.1`, a 1,508-nt partial 16S rRNA marker. Complete metadata explicitly identifies strain K7SC-8B and `taxon:1035601`, with soil isolation and India: Kafni Glacier as its geographic qualifier. No culture-collection, assembly, BioSample or BioProject link occurs in that metadata. Submission is dated 11 April 2011; creation and update are 6 June 2011. The bibliography contains an unpublished Kafni culturable-diversity study by Shivaji, Pratibha and Srinivas and a direct submission, without DOI or PMID. This sequence is not a genome. [GenBank JF799961.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799961.1)

The related Kafni paper `PMID:21918795`, `DOI:10.1007/s00792-011-0398-8` was checked in primary article HTML-extracted text. Its complete eleven-isolate Table 3 does not list K7SC-8B, and a fresh exact-designation search of the extraction found no match. The table does include K7SC-8A, which is not this record. Supplements were not inspected, so no absence claim extends to them. No exact association with a published experimental cohort is established; growth and enzyme results are not transferred. [Primary article text](https://www.researchgate.net/publication/51644024_Comparison_of_bacterial_diversity_in_proglacial_soil_from_Kafni_Glacier_Himalayan_Mountain_ranges_India_with_the_bacterial_diversity_of_other_glaciers_in_the_world), [Publisher record](https://link.springer.com/article/10.1007/s00792-011-0398-8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21918795/)

The recent successful iModulonDB structured listing from this session was re-inspected, not re-fetched for this target: 28 dataset rows, none for Arthrobacter. There is no covered target or gene/regulator/omics claim, so the adapter is not applicable. Absence from that database is not negative phenotype evidence.

## Completeness

The optional omissions and zero BacDive strain count agree with the inspected inventories. A GenBank strain designation is not a missing BacDive deposit row. Literature evidence is optional for seeded records.

Both local search stages included ignored and hidden files and compressed catalogs, using `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The five excluded `SOURCE.json` files were each parsed in full separately, and history filenames independently traversed.

The identity stage searched taxid 1035601, full label, slug and K7SC-8B separator/case variants. Five lines matched: the three identity/name/scope rows above and two unrelated rows, both read in full:

- `data/catalog/gtdb_genomes-0017.jsonl.gz:49503`: `GB_GCA_038880915.1`, Sulfolobales archaeon, taxid/species taxid 2268200, isolate DRTY-7_201803_bins_39. The number 1035601 is `ncbi_ungapped_length`.
- `data/catalog/ncbi_genbank-0035.jsonl.gz:48585`: the same archaeal MAG `GCA_038880915.1`; 1035601 is `genome_size_ungapped`, not a taxid. Its sample, project and publication do not supply a K7SC-8B identity chain.

The second stage searched JF799961 with optional version, PMID 21918795 and its DOI. It found no matches. Neither stage found matching source metadata values or history paths. Absence findings are bounded to these roots and terms, with ignored files included.

Web searches used the exact label, K7SC-8B with bacterial context and JF799961. No additional exact-isolate primary experiment or deposit/genome chain was established. The Assembly zero has a phrase-not-found warning and is not proof that a genome cannot exist under another identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. Identity, lineage, source count, attestation, lifecycle and optional omissions are supported within the inspected scope. Genome-length coincidences and neighboring isolate names do not justify adding claims.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status; this report is not human sign-off.

Future enrichment requires explicit source evidence connecting this isolate to deposits or genomes. Phenotype and habitat evidence belongs in the appropriate sibling corpus. Any authorized TaxonMech addition must be supported by maintained inputs/seeder logic and tests, not a manual generated-file edit.

## Follow-up Checks

- Before attaching published experiments, establish explicit K7SC-8B/JF799961 identity in primary text or supplements.
- Require an explicit culture-deposit/genome relationship; reject numeric matches whose source field is a sequence length.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`; full-corpus gates remain skipped here.

## Additional Notes

Primary taxonomy and nucleotide APIs succeeded. The related article was inspected as HTML extraction, not a visually verified PDF. Supplements remain uninspected; no numerical phenotype or gene claim is inferred.

Seed wording agrees with the scope and attestation. The timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp chosen by `src/taxonmech/seed.py:_seed_timestamp`, not a review time.

The whole target was reread unchanged before report creation. An ignored-independent filename search found no previous report for this stem. Only this new report is added; no record, inventory, page, prior report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
