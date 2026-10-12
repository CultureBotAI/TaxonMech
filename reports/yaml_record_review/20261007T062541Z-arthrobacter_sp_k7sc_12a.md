# YAML Record Review: Arthrobacter sp. K7SC-12A

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_k7sc_12a.yaml`
- Started UTC: 2026-10-07T06:23:59Z
- Finished UTC: 2026-10-07T06:25:41Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035599`, `Arthrobacter sp. K7SC-12A`, rank `SPECIES`, domain `BACTERIA`. It has parent `NCBITaxon:235627`, genetic code 11, ten root-first ancestors, `grounding_status: EXACT`, `mapping_status: SEEDED`, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, strains, genome links, definition, literature evidence, discussion, datasets, replacement or causal graph is asserted. The strain-like suffix in this NCBI placeholder species name is not a culture-collection accession.

This generated YAML is read-only. Future corrections belong to maintained extraction/source inputs or `src/taxonmech/seed.py` with tests; scope and locked-slug changes belong to `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`. None is required here.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` with offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/arthrobacter_sp_k7sc_12a.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/arthrobacter_sp_k7sc_12a.yaml --out /private/tmp/ar12-strict.tsv` | Exit 0; one file scanned, zero ERROR rows. |
| `cat /private/tmp/ar12-strict.tsv` | Actual TSV inspected; header only. |
| Structured comparison of backbone, full lineage, scope, path lock, source inventories and attestation | All bounded comparisons passed. |
| Exact scans of type material, merged IDs and dropped records | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not prove byte-for-byte reproduction.

`just validate-products` was not run: its configured OAK targets are curator-added graph nodes, absent here; NCBI lineage is not resolved through that gate. No literature or internal evidence references occur in the YAML. The seed event was checked; `just validate-history` was not run because ignored-independent content/path searches found no target history artifact and this review creates none.

## Identity and Grounding

The full row at `data/raw/ncbitaxon_taxa.tsv:222127` agrees on identifier, label, rank, parent, code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31606` agrees. The unique path and scope rows are `data/taxa/PATHS.tsv:14629` and `curation/seed_scope.tsv:322397`.

Every ancestor identifier, label, rank and position matches the committed parent chain. Live EFetch verifies nine non-root ancestors; Datasets verifies the same chain including root. Both resolve taxid 1035599 as Arthrobacter sp. K7SC-12A at species rank. EFetch confirms parent 235627 and code 11. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035599&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035599)

The parent remains unclassified Arthrobacter. `EXACT` means exact grounding to this source concept, not a formally named species identification or equivalence to another K7SC isolate.

## Evidence

The sole `NCBITAXON` attestation agrees on source ID, exact label, count 1, unit `NAME` and snapshot note. No cross-source units are summed. The backbone scan found no direct children. Exact scans found no target rows in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Nuccore UID `334361526` is `JF799967.1`, a 1,230-nt partial 16S rRNA sequence. Its source explicitly identifies strain K7SC-12A and `taxon:1035599`, with soil isolation and India: Kafni Glacier as the geographic qualifier. Complete metadata contains no culture-collection, assembly, BioSample or BioProject link. The submission is dated 11 April 2011; creation and update are 6 June 2011. The marker is not a genome. Its bibliography lists an unpublished Kafni culturable-diversity study by Shivaji, Pratibha and Srinivas and a direct submission, without a DOI or PMID. [GenBank JF799967.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799967.1)

A related published Kafni study is `PMID:21918795`, `DOI:10.1007/s00792-011-0398-8`. Its primary article's complete Table 3 and nearby results were read as HTML-extracted text; the publisher abstract and methods had also been inspected in this session. The eleven-isolate table does not list K7SC-12A, and a fresh exact-designation search of the extracted article found no match. This does not establish absence from uninspected supplements, but no link to the tested cohort is established. Its growth and enzyme results are not assigned to this record. [Primary article text](https://www.researchgate.net/publication/51644024_Comparison_of_bacterial_diversity_in_proglacial_soil_from_Kafni_Glacier_Himalayan_Mountain_ranges_India_with_the_bacterial_diversity_of_other_glaciers_in_the_world), [Publisher record](https://link.springer.com/article/10.1007/s00792-011-0398-8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21918795/)

The recent successful structured iModulonDB listing from this session was re-inspected: 28 dataset rows, none for Arthrobacter. The listing was not re-fetched for this target. With no covered target, gene, regulator or omics claim, iModulonDB is not applicable; its absence supplies no negative phenotype evidence.

## Completeness

The zero BacDive strain count and optional-field omissions agree with the inspected inventories. A GenBank strain designation is not an omitted BacDive row. Literature evidence is optional for seeded records.

Two ignored-independent search stages covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using `rg --no-ignore --hidden -n -z -i`, including compressed catalogs. All five excluded `SOURCE.json` files were separately parsed in full for each stage, and history filenames independently traversed.

The identity stage searched taxid 1035599, full label, slug and K7SC-12A separator/case variants. Four lines matched: the three exact identity/name/scope rows above and `data/catalog/ncbi_genbank-0066.jsonl.gz:26536`. The latter was read in full: `GCA_982657735.1` is an uncultured Candidatus Nitrosopelagicus MAG, taxid 1896163; 1035599 occurs as genome size, not taxonomy. It supplies no target assembly, sample or project link.

The accession/citation stage searched JF799967 with optional version, PMID 21918795 and its DOI. No matches were found. Neither stage found matching source metadata values or history paths. These absence claims are bounded to the stated roots and terms.

Web searches used the full label, designation with Arthrobacter/Kafni context and JF799967. No additional exact-isolate primary evidence or deposit/genome chain was established. The exact-taxid Assembly zero includes a phrase-not-found warning and is not proof that no genome could exist under another identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. Identity, lineage, attestation, source count, lifecycle and optional-field omissions are supported within the inspected scope. The unrelated genome-size match and unestablished literature association do not justify adding assertions.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status; this review is not human sign-off.

Future enrichment needs an exact source chain for deposits and genomes. Phenotype and habitat evidence belongs in the appropriate sibling corpus. An authorized TaxonMech addition requires maintained source/seeder support with tests, not a manual YAML patch.

## Follow-up Checks

- Before linking a published experiment, establish explicit K7SC-12A/JF799967 identity in primary text or supplements; do not substitute other Kafni isolates or generic Arthrobacter statements.
- Require an explicit culture-deposit/genome relationship before adding a genome link. Do not join numeric fields without their source semantics.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`. Full-corpus gates remain skipped here.

## Additional Notes

Taxonomy and nucleotide APIs succeeded. The related article was inspected as HTML extraction, not a visually checked PDF; supplementary material was not inspected. No numerical phenotype or gene claim is inferred.

The seed event wording agrees with the scope and attestation. Its timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date.

The entire target was reread unchanged before report creation. An ignored-independent filename search found no prior report for this stem. Only this new report is added; no generated record, inventory, page, prior report, history, lifecycle status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
