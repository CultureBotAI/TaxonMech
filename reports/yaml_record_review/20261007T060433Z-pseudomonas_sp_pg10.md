# YAML Record Review: Pseudomonas sp. PG10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_pg10.yaml`
- Started UTC: 2026-10-07T06:02:25Z
- Finished UTC: 2026-10-07T06:04:33Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035594`, `Pseudomonas sp. PG10`, rank `SPECIES`, domain `BACTERIA`. It has parent `NCBITaxon:196821`, genetic code 11, ten root-first lineage entries, `grounding_status: EXACT`, `mapping_status: SEEDED`, `strain_count: 0`, one NCBI name attestation, and one seed event.

No synonyms, nomenclature, taxonomy mappings, strains, genome links, definition, literature evidence, discussion, dataset, replacement, or causal graph is asserted. This NCBI placeholder taxon carries an isolate designation; PG10 alone is not a culture-collection accession or an identity link.

The YAML is generated and read-only. Any future correction belongs to maintained extraction/source inputs, `src/taxonmech/seed.py` with tests, `curation/seed_scope.tsv` for membership, or `data/taxa/PATHS.tsv` for the locked slug. No such correction is required by this review.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` with offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudomonas_sp_pg10.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_pg10.yaml --out /private/tmp/p10-strict.tsv` | Exit 0; one file scanned, zero ERROR rows. |
| `cat /private/tmp/p10-strict.tsv` | Actual TSV inspected; header only. |
| Structured comparison of backbone, complete lineage, scope, path lock, source inventories and attestation | All bounded comparisons passed. |
| Exact scans of type material, merged IDs and dropped records | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, fully inspected. |
| Structured iModulonDB dataset listing | Successful; no exact PG10 dataset, so not applicable. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. The bounded source comparison does not prove byte-for-byte reproduction.

`just validate-products` was not run: `conf/id_label_targets.yaml` checks curator-added graph nodes, of which this record has none; NCBI lineage is not resolved through that OAK gate. There are no literature or internal evidence references in the YAML. The seed event was checked, but `just validate-history` was not run because the ignored-independent content/path searches found no target history artifact and this review creates none.

## Identity and Grounding

The complete row at `data/raw/ncbitaxon_taxa.tsv:222122` agrees on identifier, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The full native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31601` agrees. The unique path and scope rows are `data/taxa/PATHS.tsv:14624` and `curation/seed_scope.tsv:322392`.

Every ancestor identifier, label, rank and position agrees with the committed NCBI parent chain. Live EFetch verifies the nine non-root ancestors, and Datasets verifies the same chain including root. Both resolve taxid 1035594 as Pseudomonas sp. PG10, species rank; EFetch also confirms parent 196821 and code 11. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035594&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035594)

The NCBI parent remains unclassified Pseudomonas. `EXACT` means exact grounding to this source concept, not species identification from a nearest-neighbor sequence or equivalence to other isolates called PG10.

## Evidence

The single `NCBITAXON` attestation correctly carries source ID `NCBITaxon:1035594`, the exact label, count 1, unit `NAME`, and the snapshot note. No cross-source units are summed. The backbone scan found no direct children. Exact target scans found no rows in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, or `bactotraits_taxa.tsv`.

Nuccore UID `333494188` is `JF345180.1`, a 1,497-nt partial 16S rRNA sequence with source strain PG10 and explicit `taxon:1035594`. Complete metadata contains no culture-collection, assembly, BioSample, BioProject, host or isolation-source qualifier. It was submitted on 17 February 2011, created on 15 August, and updated on 29 August. The sequence bibliography links the 2011 study; this marker is not a genome. [GenBank JF345180.1](https://www.ncbi.nlm.nih.gov/nuccore/JF345180.1)

The primary abstract and extracted article text for `PMID:21840210`, `DOI:10.1016/j.biortech.2011.07.064`, were inspected. Table 2 explicitly pairs PG10 with JF345180 and treats P. putida AY622320.1 as a nearest-neighbor comparator. The latter is not PG10's accession. The plant experiment used a seven-isolate mixture, so its outcomes cannot be assigned to PG10 alone. [2011 primary article](https://www.academia.edu/22554591/Arsenic_resistant_bacteria_solubilized_arsenic_in_the_growth_media_and_increased_growth_of_arsenic_hyperaccumulator_Pteris_vittata_L), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21840210/)

The inspected phosphorus study includes PG10 in spent-medium assays but selects PG6 and PG12 for tomato experiments: `PMID:25880602`, `DOI:10.1016/j.chemosphere.2015.03.048`. Neither another strain's plant effect nor a defined enzyme identity is transferred to PG10. [2015 primary article](https://www.academia.edu/22554621/Phosphorus_solubilization_and_plant_growth_enhancement_by_arsenic_resistant_bacteria), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25880602/)

The complete primary abstracts and identifier metadata of two further studies were read. `PMID:25576133`, `DOI:10.1016/j.chemosphere.2014.12.046`, includes PG10 in a comparative arsenate-reduction group, but group ranges are not individual PG10 measurements. `PMID:26547029`, `DOI:10.1016/j.chemosphere.2015.10.096`, does not establish PG10-specific plant effects in its abstract. Their full methods were not inspected, and no quantitative phenotype or gene claim is inferred. [Arsenic-transformation abstract](https://pubmed.ncbi.nlm.nih.gov/25576133/), [Plant-study abstract](https://pubmed.ncbi.nlm.nih.gov/26547029/)

The fresh structured iModulonDB listing contained 28 dataset rows, including other Pseudomonas species but no exact PG10 match. It is not applicable and supplies no negative phenotype evidence.

## Completeness

The zero BacDive count and empty optional fields agree with the inspected inventories. Literature evidence is optional for a seeded record. A published isolate or marker does not establish a missing culture deposit, BacDive identity or strain-to-genome relationship.

Two ignored-independent search stages covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using `rg --no-ignore --hidden -n -z -i`, including compressed catalogs. All five excluded `SOURCE.json` files were separately parsed in full, and history filenames independently traversed.

The identity stage searched taxid 1035594, full label, slug and genus-associated PG10 separator variants. Six lines matched: three exact identity/name/scope rows and these three rejected candidates, all read in full:

| Native candidate | Why it does not support the target |
| --- | --- |
| `data/gold/organisms.jsonl.gz:162585`, `Go0224429` | Pseudomonas syringae Dye PG10, taxid 317, with no culture ID; not the target NCBI concept. |
| `data/straininfo/records.jsonl.gz:4413`, SI-ID 4413 | Designations Dye PG10 and Hayward B1353; P. syringae / pv. lachrymans deposits LMG 5457, ICMP 3401, NCPPB 1401, PDDCC 3401 and CFBP 6451. No target-taxid or exact-source chain supports transferring them. |
| `data/catalog/ncbi_genbank-0059.jsonl.gz:21021`, `GCA_946000915.1` | An uncultured Lachnospiraceae MAG, taxid 297314; 1035594 occurs as genome length, not taxonomy. |

The accession stage searched JF345180 with optional version plus the four cited DOI/PMID pairs; it found no matches. Neither stage found matching source metadata values or history paths. Absence claims apply only to those roots and terms, not to every possible database or publication.

A web-search near match was checked directly in GenBank: `KU350591.1` is Pseudomonas reinekei strain PG10, taxid 395598, from diesel-contaminated soil in Belgium, with a different submission and bibliography. Its repeated short designation is not evidence of equivalence to JF345180.1. No hydrocarbon-degradation or other trait was transferred. [GenBank KU350591.1](https://www.ncbi.nlm.nih.gov/nuccore/KU350591.1)

No supported missing assembly was found. The Assembly zero with its explicit warning is a bounded exact-taxid result, not proof that no genome could exist under another source identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. Identity, lineage, attestation, source count, lifecycle and optional-field omissions are supported within the inspected scope. Rejected name/number matches do not justify new strains, genome links or synonyms.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status; this report is not human sign-off.

Future enrichment must establish exact identity before joining deposits or genomes. Phenotype and growth-context evidence belongs in the appropriate sibling corpus; any authorized TaxonMech addition must have maintained source/seeder support and tests, rather than a manual YAML edit.

## Follow-up Checks

- Before quantitative literature curation, inspect original PDF pages and strain-specific methods/results. Preserve the distinction between a mixed inoculum, cell-free spent medium and an individual strain.
- Do not use Dye PG10, KU350591.1, or the nearest-neighbor marker as an identity shortcut. Require an explicit source chain for any proposed equivalence.
- After an authorized maintained-input change, rerun the two single-record validators, then `just verify-corpus` and `just qc`. Full-corpus checks remain skipped here.

## Additional Notes

NCBI browser HTML failed to fetch, but both primary taxonomy APIs succeeded. Article passages were inspected through primary abstracts and author-associated HTML full-text extraction, not visually verified PDFs. No claim of exhaustive supplementary-material or numerical-table verification is made.

The seed event wording matches the scope and attestation. Its timestamp `2026-09-13T17:54:04Z` agrees with the newest raw/ATB/StrainInfo manifest timestamp under `src/taxonmech/seed.py:_seed_timestamp`; it is not a review timestamp.

The complete target was reread unchanged before report creation. Only this new report is added. No generated record, inventory, page, prior report, curation history, lifecycle status, GitHub object or cross-repository artifact is modified. No paid research or outbound contact was used.

