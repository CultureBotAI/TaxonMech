# YAML Record Review: Arthrobacter sp. K7SC-11B

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_k7sc_11b.yaml`
- Started UTC: 2026-10-07T06:20:01Z
- Finished UTC: 2026-10-07T06:21:59Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035598`, `Arthrobacter sp. K7SC-11B`, rank `SPECIES`, domain `BACTERIA`. It has parent `NCBITaxon:235627`, genetic code 11, ten root-first lineage entries, `grounding_status: EXACT`, `mapping_status: SEEDED`, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, strains, genome links, definition, literature evidence, discussion, datasets, replacement or causal graph is asserted. This isolate-labelled NCBI concept is not a culture-collection accession. The terminal B in the designation must be preserved; Acinetobacter K7SC-11A is not this record.

The YAML is generated and read-only. Future fixes belong to maintained extraction/source inputs or `src/taxonmech/seed.py` with tests; scope and locked-slug changes belong to `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`. No correction is required here.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` with offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/arthrobacter_sp_k7sc_11b.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/arthrobacter_sp_k7sc_11b.yaml --out /private/tmp/ar11-strict.tsv` | Exit 0; one file scanned, zero ERROR rows. |
| `cat /private/tmp/ar11-strict.tsv` | Actual TSV inspected; header only. |
| Structured comparison of backbone, complete lineage, scope, path lock, source inventories and attestation | All bounded comparisons passed. |
| Exact scans of type material, merged IDs and dropped records | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |
| Structured iModulonDB dataset listing | Successful; no Arthrobacter dataset, so not applicable. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded source comparisons do not establish byte-for-byte corpus reproduction.

`just validate-products` was not run: `conf/id_label_targets.yaml` checks curator-added graph nodes, of which this record has none, and excludes NCBI lineage from OAK resolution. There are no literature or internal evidence references in the YAML. The seed event was checked; `just validate-history` was not run because ignored-independent content/path searches found no target history artifact and this review creates none.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222126` agrees on identifier, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The full native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31605` agrees. The unique path and scope rows are `data/taxa/PATHS.tsv:14628` and `curation/seed_scope.tsv:322396`.

Every ancestor identifier, label, rank and position agrees with the committed parent chain. Live EFetch confirms the nine non-root ancestors; Datasets confirms the same chain including root. Both resolve taxid 1035598 as Arthrobacter sp. K7SC-11B at species rank. EFetch confirms parent 235627 and code 11. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035598&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035598)

The parent remains unclassified Arthrobacter. `EXACT` means exact grounding to this NCBI concept, not identification as a formally named species or equivalence to another isolate with a similar code.

## Evidence

The sole `NCBITAXON` attestation agrees on source ID `NCBITaxon:1035598`, exact label, count 1, unit `NAME` and snapshot note. Units are not summed across sources. The backbone scan found no direct children. Exact target scans found no rows in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Nuccore UID `334361525` is `JF799966.1`, a 1,516-nt partial 16S rRNA sequence. Its source explicitly identifies strain K7SC-11B and `taxon:1035598`, with soil isolation and India: Kafni Glacier as the geographic qualifier. Complete metadata contains no culture-collection, assembly, BioSample or BioProject link. The submission is dated 11 April 2011; creation and update are 6 June 2011. This marker is not a genome. [GenBank JF799966.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799966.1)

The sequence bibliography contains an unpublished Kafni culturable-diversity study by Shivaji, Pratibha and Srinivas and a direct-submission entry, without a DOI or PMID. A related published Kafni study is `PMID:21918795`, `DOI:10.1007/s00792-011-0398-8`. Its publisher abstract and extracted primary article methods/results/Table 3 were inspected during this review turn. The complete eleven-isolate table includes Acinetobacter K7Sc-11a and K7Sc-8a, but not Arthrobacter K7Sc-11b. A search of the extracted article text also found no exact K7Sc-11b designation. This is not proof of absence from uninspected supplements; it does mean the inspected material does not establish the target as one of the tested isolates. Their growth and enzyme outcomes are not transferred to this record. [Publisher record](https://link.springer.com/article/10.1007/s00792-011-0398-8), [Primary article text](https://www.researchgate.net/publication/51644024_Comparison_of_bacterial_diversity_in_proglacial_soil_from_Kafni_Glacier_Himalayan_Mountain_ranges_India_with_the_bacterial_diversity_of_other_glaciers_in_the_world), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21918795/)

Bounded web searches used the full label, exact strain designation with Arthrobacter/Kafni context, and JF799966. They did not establish an additional exact-isolate publication or deposit/genome chain. Search snippets and taxonomy mirrors were not treated as independent primary evidence.

The fresh structured iModulonDB listing contained 28 dataset rows and no Arthrobacter dataset. It is not applicable and supplies no negative phenotype evidence.

## Completeness

The zero BacDive strain count and optional-field omissions agree with the inspected inventories. The GenBank strain designation is not an omitted BacDive row; its marker is not an assembly. Literature evidence is optional for a seeded record.

Two ignored-independent search stages covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using `rg --no-ignore --hidden -n -z -i`, including compressed catalogs. All five excluded `SOURCE.json` files were separately parsed in full for each stage, and history filenames independently traversed.

The identity stage searched taxid 1035598, full label, slug and K7SC-11B separator/case variants. Only the backbone, native scientific-name and scope rows above matched; each was read in full. The accession/citation stage searched JF799966 with optional version, PMID 21918795 and its DOI. No matches were found. Neither stage found matching metadata values or history paths. These absence claims are bounded to the stated roots and terms.

The Assembly zero with its phrase-not-found warning is a bounded exact-taxid result, not proof that no genome could exist under another identity. No supported missing strain-genome relationship, required attestation or required taxonomy field was identified.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. Identity, lineage, attestation, source count, lifecycle and optional-field omissions are supported within the inspected scope. An unestablished literature connection is not an unsupported claim in this taxonomy-only record.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status; this report is not human sign-off.

Future enrichment must establish an exact source chain before joining deposits or genomes. Phenotype and habitat evidence belongs in the appropriate sibling corpus; any authorized TaxonMech addition needs maintained input/seeder support and tests rather than a manual YAML edit.

## Follow-up Checks

- Before linking the published Kafni experiment, establish an explicit K7SC-11B/JF799966 association in primary full text or supplementary material. Do not substitute K7SC-11A or another group member.
- Before adding a strain-genome relationship, require a source-backed culture-deposit and genome association, not a shared place, submitter, genus or short designation.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`. Full-corpus gates remain skipped here.

## Additional Notes

Primary taxonomy and sequence APIs succeeded. The related 2011 paper was inspected as publisher abstract and primary article HTML extraction, not as a visually checked PDF. Supplementary material was not inspected. No quantitative phenotype or gene claim is inferred.

The seed event wording agrees with the scope and source attestation. Its timestamp `2026-09-13T17:54:04Z` matches the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date.

The entire target was reread unchanged before report creation. An ignored-independent filename search found no prior report for this stem. Only this new report is added; no generated record, inventory, page, prior report, history, lifecycle status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
