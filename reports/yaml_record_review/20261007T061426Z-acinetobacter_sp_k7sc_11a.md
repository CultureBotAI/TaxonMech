# YAML Record Review: Acinetobacter sp. K7SC-11A

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acinetobacter_sp_k7sc_11a.yaml`
- Started UTC: 2026-10-07T06:09:57Z
- Finished UTC: 2026-10-07T06:14:26Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035596`, `Acinetobacter sp. K7SC-11A`, rank `SPECIES`, domain `BACTERIA`. It has parent `NCBITaxon:196816`, genetic code 11, ten root-first lineage entries, `grounding_status: EXACT`, `mapping_status: SEEDED`, `strain_count: 0`, one NCBI name attestation, and one seed event.

No synonyms, nomenclature, taxonomy mappings, strains, genome links, definition, literature evidence, discussion, datasets, replacement, or causal graph is asserted. This NCBI placeholder species concept carries an isolate designation; that designation alone does not establish a culture-collection accession.

The YAML is generated and read-only. Future fixes belong to maintained extraction/source inputs or `src/taxonmech/seed.py` with tests; scope and locked-slug changes belong to `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`. No correction is required by this review.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` with offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/acinetobacter_sp_k7sc_11a.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/acinetobacter_sp_k7sc_11a.yaml --out /private/tmp/a11-strict.tsv` | Exit 0; one file scanned, zero ERROR rows. |
| `cat /private/tmp/a11-strict.tsv` | Actual TSV inspected; header only. |
| Structured comparison of backbone, complete lineage, scope, path lock, source inventories and attestation | All bounded comparisons passed. |
| Exact scans of type material, merged IDs and dropped records | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |
| Structured iModulonDB dataset listing | Successful; no exact target dataset, so not applicable. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not establish byte-for-byte corpus reproduction.

`just validate-products` was not run: the configured OAK gate concerns curator-added graph nodes, and this record has none. The NCBI lineage is not resolved through that gate. No literature or internal evidence references occur in the YAML. The seed event was checked; `just validate-history` was not run because ignored-independent content/path searches found no target history artifact and this review creates none.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222124` agrees on identifier, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The full native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31603` agrees. The unique path and scope rows are `data/taxa/PATHS.tsv:14626` and `curation/seed_scope.tsv:322394`.

Every ancestor identifier, label, rank and position agrees with the committed NCBI chain. Live EFetch confirms nine non-root ancestors, and Datasets includes the same chain plus root. Both resolve taxid 1035596 as Acinetobacter sp. K7SC-11A at species rank; EFetch confirms parent 196816 and code 11. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035596&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035596)

The parent is unclassified Acinetobacter. `EXACT` denotes exact grounding to this source concept, not a formally named species identification or equivalence to a nearest-neighbor sequence.

## Evidence

The sole `NCBITAXON` attestation correctly carries source ID `NCBITaxon:1035596`, the exact label, count 1, unit `NAME`, and the snapshot note. No cross-source units are summed. The complete backbone scan found no direct children. Exact target scans found no rows in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, or `bactotraits_taxa.tsv`.

Nuccore UID `334361524` resolves to `JF799965.1`, a 1,527-nt partial 16S rRNA sequence. Its source explicitly identifies strain K7SC-11A and `taxon:1035596`, with soil isolation and geographic qualifier India: Kafni Glacier. Complete metadata contains no culture-collection, assembly, BioSample or BioProject link. The submission is dated 11 April 2011; creation and update are 6 June 2011. This marker is not a genome. Its bibliography names an unpublished Kafni culturable-diversity study and direct submission, without a DOI or PMID. [GenBank JF799965.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799965.1)

A related 2011 publication was identified as `PMID:21918795`, `DOI:10.1007/s00792-011-0398-8`. Its complete primary abstract concerns Kafni soil libraries and eleven cultured strains. The abstract does not name this isolate. Publisher full text and table/PDF endpoints were inaccessible; a search snippet naming K7Sc-11a is only a lead, not inspected evidence. No isolate-specific physiology, species reassignment or accession-to-paper linkage is inferred from the abstract. [Kafni study abstract](https://pubmed.ncbi.nlm.nih.gov/21918795/)

The primary XML of `PMID:24712449`, `PMCID:PMC4282425`, `DOI:10.1111/jam.12516`, was inspected for methods, Table 2 caption/header, the complete target row and relevant results. The table compares environmental clone sequences to their closest GenBank relatives. Its K7SC-11A row reports one clone at 99% similarity, not recovery or testing of the original strain. The displayed accession is `JF99965.1`, which differs from the verified `JF799965.1`; that discrepancy is preserved rather than silently repaired. Biofilm, water-discolouration and chlorine-context observations must not be transferred to this taxon as strain-specific results. [Primary article XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4282425/fullTextXML), [Published article](https://academic.oup.com/jambio/article/117/1/286/6716924)

The fresh structured iModulonDB listing contained 28 dataset rows. Its Acinetobacter entry is `a_baumannii/precise139`, not this target. iModulonDB is not applicable and supplies no negative phenotype evidence.

## Completeness

The zero BacDive strain count and empty optional fields agree with the inspected source inventories. A strain designation in GenBank is not a missing BacDive row; a marker sequence is not a missing assembly. Literature evidence is optional for a seeded record.

Two ignored-independent search stages covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using `rg --no-ignore --hidden -n -z -i`, including compressed catalogs. All five excluded `SOURCE.json` files were separately parsed in full for each stage, and history filenames independently traversed.

The identity stage searched taxid 1035596, full label, slug and K7SC-11A separator/case variants. Only the backbone, native name and scope rows above matched; each was read in full. The accession/citation stage searched JF799965 and the article's differing JF99965 with optional versions, both DOI/PMID pairs, and PMC4282425. No matches were found. Neither stage found matching source metadata values or history paths. These absence claims are bounded to the stated roots and terms, not every possible source or publication.

The exact Assembly search returned zero with a phrase-not-found warning. This does not prove that no genome could exist under a different identity. No supported missing culture deposit, strain-genome link, required attestation, or required taxonomy field was identified.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. Identity, lineage, attestation, source count, lifecycle and optional-field omissions are supported within the inspected scope. The article accession discrepancy and sequence-similarity match are external-source caveats, not defects asserted by this record.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status; this report is not human sign-off.

Future enrichment must establish an explicit source chain before joining culture deposits or genomes. Phenotype and habitat evidence belongs in the appropriate sibling corpus; any authorized TaxonMech addition needs maintained source/seeder support and tests, not a manual YAML edit.

## Follow-up Checks

- Before using the 2011 literature lead, inspect its full methods, strain-specific tables and accession linkage; do not promote search snippets or cohort-level abstract claims.
- Before using the 2014 table as a cross-reference, resolve the printed accession discrepancy against primary sequence records. Preserve its closest-relative scope regardless of the accession outcome.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`. Full-corpus checks remain skipped here.

## Additional Notes

The NCBI taxonomy APIs and nucleotide metadata succeeded. PMC HTML presented a browser check; Europe PMC's primary article XML supplied the 2014 methods and table. No PDF was visually verified, and the 2011 full text remains uninspected. These limitations do not block assessment of the seeded taxonomy-only claims.

The seed event wording matches the scope and attestation. Its timestamp `2026-09-13T17:54:04Z` agrees with the newest raw/ATB/StrainInfo manifest timestamp under `src/taxonmech/seed.py:_seed_timestamp`; it is not a review timestamp.

The complete target was reread unchanged before report creation, and an ignored-independent report-path search found no prior report for this stem. Only this new report is added. No generated record, inventory, page, prior report, curation history, lifecycle status, GitHub object or cross-repository artifact is modified. No paid research or outbound contact was used.
