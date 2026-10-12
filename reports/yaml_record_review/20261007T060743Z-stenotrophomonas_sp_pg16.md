# YAML Record Review: Stenotrophomonas sp. PG16

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/stenotrophomonas_sp_pg16.yaml`
- Started UTC: 2026-10-07T06:05:43Z
- Finished UTC: 2026-10-07T06:07:43Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035595`, label `Stenotrophomonas sp. PG16`, rank `SPECIES`, domain `BACTERIA`. Parent is `NCBITaxon:196198`, genetic code 11; the record contains ten root-first ancestors, `grounding_status: EXACT`, `mapping_status: SEEDED`, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, strains, genome links, definition, literature evidence, discussion, dataset, replacement or causal graph is asserted. This is an NCBI placeholder taxon with an isolate designation, not a culture-collection deposit or a claim of formally established species identity.

The YAML is generated and read-only. Future fixes belong to maintained source/extraction inputs, `src/taxonmech/seed.py` with tests, `curation/seed_scope.tsv` for scope, or `data/taxa/PATHS.tsv` for slug ownership. No fix to these inputs is required by the current review.

## Validation

The uv commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/stenotrophomonas_sp_pg16.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/stenotrophomonas_sp_pg16.yaml --out /private/tmp/s16-strict.tsv` | Exit 0; one file scanned, zero ERROR rows. |
| `cat /private/tmp/s16-strict.tsv` | Actual TSV inspected; header only. |
| Structured inventory, ancestor, scope, slug and attestation comparisons | All bounded assertions passed. |
| Exact-token type-material, merged-ID and dropped-record scans | No target rows. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and complete ancestry agree. |
| Exact-taxid Assembly / nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, whose complete metadata was inspected. |
| Structured iModulonDB listing | Successful; no exact PG16 organism/dataset match. |

Not checked: `just verify-corpus`, `just qc`, full-corpus validation, tests, provenance hashing, generated-site drift, documentation statistics and vendored checks. The bounded comparison does not demonstrate byte-identical regeneration.

`just validate-products` was not run: its configured targets are curator-added graph nodes, absent from this record; it is not the NCBI lineage validator. No literature or internal evidence references exist in the YAML to resolve. The seed event was checked, but `just validate-history` was not run because ignored-independent history content/path searches found no target artifact and no history write is authorized.

## Identity and Grounding

The complete source row at `data/raw/ncbitaxon_taxa.tsv:222123` agrees with identifier, scientific label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31602` agrees. The exact path and scope are pinned by `data/taxa/PATHS.tsv:14625` and `curation/seed_scope.tsv:322393`.

Every ancestor identifier, label, rank and position agrees with the committed backbone. Live EFetch independently confirms all nine non-root ancestors, parent 196198 and code 11; Datasets confirms the same ten-ID chain including root. Both resolve the exact Stenotrophomonas sp. PG16 concept. In particular, the record's Lysobacterales, Lysobacteraceae and Stenotrophomonas placement matches current NCBI. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035595&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035595)

`EXACT` denotes this NCBI concept, not an inferred species synonym. The later paper's conflicting genus wording, described below, does not authorize changing the NCBI-based label or ancestry.

## Evidence

The sole attestation correctly carries source `NCBITAXON`, source ID `NCBITaxon:1035595`, exact label, count 1, unit `NAME`, and snapshot note. It counts a name rather than a strain or genome. The backbone has no direct children. The seven primary inventories for BacDive, LPSN, GTDB mappings, GOLD, MediaDive, Madin and BactoTraits contained no exact target rows.

Nuccore UID `333494190` resolves to `JF345182.1`, a 1,505-nt partial 16S rRNA sequence. Its source explicitly names strain PG16, organism Stenotrophomonas sp. PG16 and taxon 1035595. The full metadata contains no culture-collection, assembly, BioSample, BioProject, host or isolation-source qualifier. It was submitted on 17 February 2011, created on 15 August and updated on 29 August. Its bibliography links the 2011 paper; the sequence is not a genome. [GenBank JF345182.1](https://www.ncbi.nlm.nih.gov/nuccore/JF345182.1)

The inspected 2011 Table 2 pairs PG16 with JF345182 and a nearest-neighbor Stenotrophomonas rhizophila sequence GU186108.1: `PMID:21840210`, `DOI:10.1016/j.biortech.2011.07.064`. The comparator is not PG16's own accession or proof of species equivalence. Its seven-isolate plant experiment does not establish PG16-alone effects. [2011 primary article](https://www.academia.edu/22554591/Arsenic_resistant_bacteria_solubilized_arsenic_in_the_growth_media_and_increased_growth_of_arsenic_hyperaccumulator_Pteris_vittata_L)

The phosphorus study, `PMID:25880602`, `DOI:10.1016/j.chemosphere.2015.03.048`, explicitly includes PG16, but section 2.1 calls the whole group Pseudomonas. This conflicts with the exact GenBank identity and earlier comparator; preserve the disagreement, not a reassignment. Section 3.1 reports no phosphate-rock solubilization for PG16 under its assay, narrower than the collective abstract wording. Tomato experiments select PG6 and PG12, not PG16. Spent-medium observations do not establish a specific gene or enzyme identity. [2015 primary article](https://www.academia.edu/22554621/Phosphorus_solubilization_and_plant_growth_enhancement_by_arsenic_resistant_bacteria)

The primary abstract of `PMID:25576133`, `DOI:10.1016/j.chemosphere.2014.12.046`, includes PG16 in a comparative arsenate-reduction group. Its ranges are not individual PG16 measurements. `PMID:26547029`, `DOI:10.1016/j.chemosphere.2015.10.096`, does not resolve PG16-specific plant effects in the inspected abstract. Their full methods were not inspected, and no quantitative phenotype is inferred. [Arsenic-transformation abstract](https://pubmed.ncbi.nlm.nih.gov/25576133/), [Plant-study abstract](https://pubmed.ncbi.nlm.nih.gov/26547029/)

All four primary abstracts and DOI/PMID metadata were read during this review session, alongside the relevant 2011/2015 article passages. Applying them here rests on the independent PG16 sequence linkage and explicit PG16 text, not on another record's verdict.

The fresh structured iModulonDB listing had 28 dataset rows and no exact PG16 match. It is not applicable; that absence is not evidence against any phenotype. No module or gene was borrowed from another organism.

## Completeness

The zero BacDive strain count and omitted source-specific sections agree with the inspected inventories. PG16 in a taxon label is not a registered deposit. Neither a marker nor a repeated short designation establishes a strain-to-genome link. Literature evidence is optional for seeded records, so the absent phenotype narrative and optional discussion are not record defects.

Two ignored-independent searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using `rg --no-ignore --hidden -n -z -i`, including compressed files. All five excluded `SOURCE.json` files were separately parsed in full; history filenames were independently traversed.

The identity stage searched taxid 1035595, exact label, slug and PG16 separator variants associated with either Stenotrophomonas or Pseudomonas. Including both genera tested the observed literature wording without accepting it as an alias. Five lines matched: three exact backbone/name/scope rows and these two fully inspected rejected candidates:

| Candidate | Identity boundary |
| --- | --- |
| `data/gold/organisms.jsonl.gz:162606`, `Go0224450` | Pseudomonas syringae Dye PG16, taxid 317, empty culture ID; not this Stenotrophomonas concept. |
| `data/straininfo/records.jsonl.gz:13794`, SI-ID 13794 | Dye PG16 among source designations, strain-level taxon Pseudomonas amygdali pv. lachrymans, taxid 53707. Eleven retained Pseudomonas deposits include LMG 2205, ICMP 534, ICMP 541 and NCPPB 541; neither the designation nor the group supplies a link to taxid 1035595. |

The accession stage searched JF345182 with optional version and all four cited DOI/PMID pairs; no matches were found. Neither stage found matching metadata values or history paths. These are bounded local absence results, not proof of absence from all databases or publications.

No supported missing assembly or culture-deposit relationship was established. The exact-taxid Assembly zero retains its phrase-not-found warning and is not a universal no-genome claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current YAML. The external paper's conflicting genus wording is preserved in this report, but the YAML correctly follows the pinned and live NCBI concept and does not assert the problematic literature claims.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` lifecycle status. This report is not human approval.

Any future literature enrichment must keep the genus conflict visible and verify exact strain and treatment identity. Any proposed deposit/genome mapping needs explicit own-strain evidence. Maintained seeder/source inputs with tests own future TaxonMech changes; phenotype and growth-context curation belongs in the appropriate sibling corpus.

## Follow-up Checks

- Before numerical or mechanism curation, inspect original article PDFs and strain-specific methods/results. Resolve the genus wording without silently reclassifying the taxon or equating strains by PG16 alone.
- Do not transfer consortium or other-strain plant outcomes to this record. Keep marker accessions distinct from genomes and deposits.
- After an authorized maintained-input change, rerun the two single-record validators, then `just verify-corpus` and `just qc`. Those full-corpus gates were not run here.

## Additional Notes

The NCBI browser HTML fetch failed; primary taxonomy APIs succeeded. The arsenic-transformation publisher page returned HTTP 403, so only its primary PubMed abstract was used. The 2011/2015 passages were inspected as author-associated full-text HTML extraction, not visually checked PDFs. No exhaustive supplementary-material or numerical-table verification is claimed.

The seed event wording agrees with the exact scope reason and attestation. Its timestamp `2026-09-13T17:54:04Z` follows the newest raw/ATB/StrainInfo manifest timestamp under `src/taxonmech/seed.py:_seed_timestamp`, not the review date.

The entire target was reread unchanged before report creation. Only this new report is written; no YAML, source inventory, generated page, prior report, history record, lifecycle status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.

