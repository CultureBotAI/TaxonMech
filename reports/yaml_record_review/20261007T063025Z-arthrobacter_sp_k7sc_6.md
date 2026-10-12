# YAML Record Review: Arthrobacter sp. K7SC-6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_k7sc_6.yaml`
- Started UTC: 2026-10-07T06:26:40Z
- Finished UTC: 2026-10-07T06:30:25Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035600`, `Arthrobacter sp. K7SC-6`, rank `SPECIES`, domain `BACTERIA`. It asserts parent `NCBITaxon:235627`, ten root-first ancestors, genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, strains, genome links, definition, literature evidence, datasets, discussion, replacement or causal graph is asserted. The strain-like suffix is part of this NCBI placeholder species label, not a culture-collection accession or evidence of formal species naming.

The generated YAML is read-only. Any future correction belongs to maintained source/extraction inputs or `src/taxonmech/seed.py` with tests; scope and slug ownership are `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`. No correction is required here.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/arthrobacter_sp_k7sc_6.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/arthrobacter_sp_k7sc_6.yaml --out /private/tmp/ar6-strict.tsv` | Exit 0; one file scanned, zero ERROR rows. |
| `cat /private/tmp/ar6-strict.tsv` | Actual TSV inspected; header only. |
| Structured comparison of backbone, complete lineage, path lock, scope, source inventories and attestation | All bounded comparisons passed. |
| Exact scans of type material, merged IDs and dropped records | No target row. |
| NCBI Taxonomy EFetch and Datasets | Exact identity and ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not establish byte-for-byte reproduction of the corpus.

`just validate-products` was not run: its configured OAK targets are curator-added graph nodes, absent here; the NCBI lineage is not resolved by that gate. The YAML contains no literature or internal evidence references. The seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target history artifact, and this read-only review creates none.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222128` agrees on identifier, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31607` agrees. The unique path-lock and scope rows are `data/taxa/PATHS.tsv:14630` and `curation/seed_scope.tsv:322398`.

All ten ancestor identifiers, labels, ranks and positions match the committed parent chain. Live EFetch resolves taxid 1035600 to the exact label, species rank, parent 235627 and code 11, with nine non-root ancestors. Datasets confirms the same ancestry including root. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035600&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035600)

The parent is unclassified Arthrobacter. `EXACT` denotes agreement with this source concept, not equivalence to a named Arthrobacter species or another K7SC isolate.

## Evidence

The sole `NCBITAXON` attestation agrees on exact ID and label, count 1, unit `NAME` and snapshot note. No unlike source units are summed. The backbone scan found no direct children. Exact scans found no target rows in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Nuccore UID `334361517` is `JF799958.1`, a 1,512-nt partial 16S rRNA marker. Its complete metadata explicitly identifies Arthrobacter sp. K7SC-6, strain K7SC-6 and `taxon:1035600`, with soil isolation and India: Kafni Glacier as the geographic qualifier. It contains no culture-collection, assembly, BioSample or BioProject link. Submission is dated 11 April 2011; creation and update are 6 June 2011. This marker is not a genome. Its references are an unpublished Kafni culturable-diversity study by Shivaji, Pratibha and Srinivas and a direct submission, without DOI or PMID. [GenBank JF799958.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799958.1)

A related Kafni paper is `PMID:21918795`, `DOI:10.1007/s00792-011-0398-8`. Its complete eleven-isolate Table 3 and nearby results were inspected as primary article HTML-extracted text in this session, along with the publisher abstract and methods. K7SC-6 is not listed in that table; a fresh exact-designation search of the extracted article found no match. Supplements were not inspected, so this does not establish absence from all associated material. No exact link to the experimental cohort is established, and no growth or enzyme result is assigned to this record. [Primary article text](https://www.researchgate.net/publication/51644024_Comparison_of_bacterial_diversity_in_proglacial_soil_from_Kafni_Glacier_Himalayan_Mountain_ranges_India_with_the_bacterial_diversity_of_other_glaciers_in_the_world), [Publisher record](https://link.springer.com/article/10.1007/s00792-011-0398-8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21918795/)

The recent successful structured iModulonDB dataset listing from this session was re-inspected, not re-fetched for this target: 28 dataset rows, none for Arthrobacter. There is no covered target, gene, regulator or omics assertion here. iModulonDB is not applicable; its absence is not negative phenotype evidence.

## Completeness

The zero BacDive strain count and optional-field omissions agree with the inspected inventories. A GenBank strain designation is not an omitted BacDive deposit row. Literature evidence is optional for this seeded record.

Two gitignore-independent searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history` using `rg --no-ignore --hidden -n -z -i`, including compressed catalogs. All five excluded `SOURCE.json` files were separately parsed in full for both stages; history filenames were independently traversed.

The identity search included taxid 1035600, full label, slug and K7SC-6 separator/case variants. Five lines matched: the three exact backbone/name/scope rows above, plus two unrelated assembly rows read in full:

- `data/catalog/gtdb_genomes-0006.jsonl.gz:8861`: `GB_GCA_018650645.1`, Candidatus Magasanikiibacteriota bacterium, taxid/species taxid 2026717, isolate SI053_bin23. The number 1035600 is `ncbi_total_length` and `ncbi_ungapped_length`, not taxonomy.
- `data/catalog/ncbi_genbank-0017.jsonl.gz:3883`: the same `GCA_018650645.1` and organism/taxid; 1035600 is `genome_size` and `genome_size_ungapped`. This hypoxic-seawater MAG and its sample/project links do not identify K7SC-6.

The accession/citation search included JF799958 with optional version, PMID 21918795 and the related DOI. No matches were found. Neither stage found matching source metadata values or history paths. These absence findings include ignored files and are bounded to the stated roots and terms.

Web searches used the exact full label, K7SC-6 with bacterial context and verified accession JF799958. No additional exact-isolate primary experiment or deposit/genome chain was established; near-matches to other K7SC isolates were not transferred. The zero exact-taxid Assembly result includes a phrase-not-found warning and does not prove that no genome exists under another identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. Identity, lineage, attestation, source count, lifecycle and optional-field omissions are supported within the inspected scope. Unrelated assembly-length matches and an unestablished literature association do not justify new assertions.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status; this review is not human sign-off.

Future enrichment requires an explicit identity chain for deposits and genomes. Phenotype and habitat evidence belongs in the appropriate sibling corpus. An authorized TaxonMech addition requires maintained source/seeder support and tests, not a manual generated-YAML patch.

## Follow-up Checks

- Before linking a published experiment, establish explicit K7SC-6/JF799958 identity in inspected primary text or supplements; other Kafni isolates are not substitutes.
- Require an explicit culture-deposit/genome relationship before adding genome links. Numeric matches must be checked against source field semantics.
- After an authorized maintained-input change, rerun the two single-record validators, then `just verify-corpus` and `just qc`. Full-corpus gates remain skipped here.

## Additional Notes

Taxonomy and nucleotide APIs succeeded. The related article was read as HTML extraction, not a visually checked PDF; supplements were not inspected. No numerical phenotype or gene claim is inferred.

The seed event wording agrees with the scope and attestation. Its timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date.

The full target was reread unchanged before report creation. An ignored-independent filename search found no prior report for this stem. Only this new report is added; no generated record, inventory, page, prior report, history, lifecycle status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
