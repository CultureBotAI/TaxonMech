# YAML Record Review: Pseudomonas sp. PG6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_pg6.yaml`
- Started UTC: 2026-10-07T05:53:26Z
- Finished UTC: 2026-10-07T05:56:51Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035592`, label `Pseudomonas sp. PG6`, rank `SPECIES`, domain `BACTERIA`. The record has parent `NCBITaxon:196821`, ten root-first ancestors, genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, `strain_count: 0`, one NCBI name attestation, and one seed event.

No synonyms, nomenclature, taxonomy mappings, strains, genome links, literature evidence, definitions, discussions, datasets, replacements, or causal graphs are asserted. This is an NCBI species-rank placeholder carrying an isolate designation, not a culture-collection deposit or a formally named species. The YAML is generated and must not be hand-edited.

Maintained owners of any future correction are `src/taxonmech/seed.py`, the extraction/source pipeline and its inventories, `curation/seed_scope.tsv`, or `data/taxa/PATHS.tsv` for slug ownership. This review changes none of those inputs.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudomonas_sp_pg6.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_pg6.yaml --out /private/tmp/p6-strict.tsv` | Exit 0; one file scanned, zero ERROR rows. |
| `cat /private/tmp/p6-strict.tsv` | Read the actual output: header only, `file category detail path message`. |
| Structured comparison with committed NCBI backbone, ancestors, scope, path index, seven source inventories and attestation | All bounded assertions passed. |
| Exact-token scans of `ncbi_type_material.tsv`, `ncbi_merged_ids.tsv`, and `dropped.tsv` | No target rows. |
| Live NCBI Taxonomy EFetch XML and Datasets JSON | Both resolved the exact target; identity and lineage agree. |
| Exact-taxid NCBI Assembly and nuccore searches | Assembly count 0, with a phrase-not-found warning; nuccore count 1. All returned nucleotide metadata inspected. |
| Structured iModulonDB dataset listing | Successful; no exact PG6 organism/dataset match. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, site drift, documentation statistics, and vendored checks. The source comparison is not a byte-for-byte regeneration or a substitute for these gates.

`just validate-products` was not run: `conf/id_label_targets.yaml` targets curator-added graph nodes and does not validate this record's NCBI lineage through OAK; this YAML contains no such nodes. No literature citation or internal evidence reference exists in the YAML to resolve. The seed event's shape, wording, and timestamp were checked, but `just validate-history` was not run because the ignored-independent history search found no target artifact and this read-only review creates no history entry.

## Identity and Grounding

The complete source row at `data/raw/ncbitaxon_taxa.tsv:222120` agrees with the identifier, label, species rank, parent, genetic code, empty synonym fields, and 2026-09-13 snapshot. The full native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31599` agrees. `data/taxa/PATHS.tsv:14622` resolves the exact slug; `curation/seed_scope.tsv:322390` supplies the NCBI-attested inclusion reason.

All ten ancestor identifiers, labels, ranks, and ordering match the committed parent chain. Live EFetch supplies the same nine non-root ancestors; Datasets includes root 1 and the same complete identifier chain. Thus Bacteria and Pseudomonas placement are supported, and no lineage reconciliation is needed. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035592&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035592)

`EXACT` denotes agreement with this NCBI concept, not definitive identification as Pseudomonas putida. The literature's nearest-neighbor marker comparison does not establish a species synonym, culture-deposit equivalence, or genome identity.

## Evidence

The sole attestation is supported: source `NCBITAXON`, source ID `NCBITaxon:1035592`, exact label, count 1, unit `NAME`, and snapshot note. This counts a source name, not a strain or genome. The complete backbone scan found no direct children, and the seven primary inventories contained no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin, or BactoTraits row.

NCBI nuccore UID `333494186` resolves to `JF345178.1`, a 1,498-nt partial 16S rRNA sequence. The source feature explicitly names strain PG6 and taxon 1035592. It carries no culture-collection, BioSample, BioProject, assembly, host, or isolation-source qualifier. The record was submitted on 17 February 2011, created on 15 August, and updated on 29 August. It is a marker sequence, not a genome. Its bibliography explicitly links the 2011 article below. [GenBank JF345178.1](https://www.ncbi.nlm.nih.gov/nuccore/JF345178.1)

Ghosh, Rathinasabapathi and Ma (2011), `PMID:21840210`, `DOI:10.1016/j.biortech.2011.07.064`: inspected the primary abstract and extracted full article text. Table 2 pairs PG6 with JF345178 and compares it with P. putida marker GU248219; the latter is a comparator, not PG6's accession. Isolation methods describe arsenate-selected bacteria from Pteris vittata rhizosphere soils near Gainesville, Florida, but do not assign PG6 to one precise collection site. Section 2.4.1 explicitly mixes seven isolates in equal proportions for the plant experiment. Its consortium-level arsenic mobilization and plant responses cannot be attributed to PG6 alone. [PubMed](https://pubmed.ncbi.nlm.nih.gov/21840210/), [primary article text](https://www.academia.edu/22554591/Arsenic_resistant_bacteria_solubilized_arsenic_in_the_growth_media_and_increased_growth_of_arsenic_hyperaccumulator_Pteris_vittata_L)

Ghosh, Rathinasabapathi and Ma (2015), `PMID:25880602`, `DOI:10.1016/j.chemosphere.2015.03.048`: the primary abstract and extracted article text specifically discuss PG6 spent-medium phytate solubilization and tomato responses. Preserve the cell-free treatment and conditions; these are not generic inoculation or field-performance results. Section 3.1 explicitly reports no phosphate-rock solubilization by PG6 under that assay, narrower than the abstract's collective wording. Section 3.2 states that direct phytase determination was unsuccessful because of medium interference, so substrate release is not a verified PG6 enzyme identity. The extracted section 2.3 appears to interchange the PG6/PG12 treatment assignments, and numerical phytate values differ between its table and narrative; retain these as unresolved source-text caveats pending PDF inspection. No quantitative table values were curated. [PubMed](https://pubmed.ncbi.nlm.nih.gov/25880602/), [primary article text](https://www.academia.edu/22554621/Phosphorus_solubilization_and_plant_growth_enhancement_by_arsenic_resistant_bacteria)

Two further primary abstracts were inspected with their DOI/PMID metadata. `PMID:25576133`, `DOI:10.1016/j.chemosphere.2014.12.046`, explicitly includes PG6 in the comparative arsenate-reduction group; its group ranges are not exact PG6 measurements. `PMID:26547029`, `DOI:10.1016/j.chemosphere.2015.10.096`, reports plant experiments with multiple bacteria but its abstract does not identify PG6's individual treatment. Full methods were not inspected for either article; no individual quantitative or gene-mechanism claim is inferred. [2015 arsenic-transformation abstract](https://pubmed.ncbi.nlm.nih.gov/25576133/), [2016 plant-study abstract](https://pubmed.ncbi.nlm.nih.gov/26547029/)

The structured iModulonDB listing contained 28 dataset rows, including other Pseudomonas species but no exact PG6 dataset. It is not applicable; this is not negative phenotype evidence. No gene, regulator, or module identity was borrowed from another strain.

## Completeness

The empty optional fields and zero BacDive strain count are consistent with the inspected source inventory. A published isolate designation does not itself provide a registered culture deposit, a BacDive identity, or a supported strain-to-genome chain. Record-level literature evidence is optional for seeded records; the absence of a phenotype narrative is not a defect in this taxonomic record.

Two ignored-independent search stages covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Each used `rg --no-ignore --hidden -n -z -i`, including compressed catalogs. The excluded `SOURCE.json` files were separately parsed in full across all five source directories, and history paths were independently traversed.

The first stage searched taxid 1035592, the full label, slug, and genus-associated PG6 separator variants. It returned only three identity/scope/name rows, all fully inspected. The second searched JF345178 with optional version, and the 2011 and phosphorus-paper DOI/PMID pairs; it returned zero rows. Both metadata and history-path stages returned no target matches. This supports absence only within those local roots and terms, not a universal claim that no source, genome, or publication exists. The two later follow-up papers were not part of the local DOI search.

No supported missing assembly or deposit relationship was established. The Assembly zero is a bounded exact-taxid result with the warning reported above, not proof of global genome absence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current YAML. The external literature caveats concern possible future evidence extraction; no corresponding over-scoped claim is present in this record. The current taxonomy, source attestation, count, lifecycle status, and optional-field omissions are supported within the review scope.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status; this report is not human approval.

If literature evidence is later requested, first resolve the noted primary-text inconsistencies and keep marker, strain, consortium, spent-medium, and plant-treatment identities distinct. Phenotype and growth-context curation belongs in the appropriate sibling corpus. Any future TaxonMech representation must have a maintained seeder/source input and tests, rather than a manual edit to this YAML.

## Follow-up Checks

- Before numerical or mechanism curation, inspect the original phosphorus-paper PDF, especially methods 2.3, Table 1, and sections 3.2-3.3. Verify treatment assignments and distinguish measured substrate release from inferred enzyme activity.
- Read full methods and strain-specific results for the two follow-up abstracts before assigning their group results to PG6.
- Any future deposit/genome enrichment must establish an explicit own-strain source chain; JF345178.1 and the nearest-neighbor accession are not assemblies.
- After an authorized maintained-input change, rerun the two single-record validators, then `just verify-corpus` and `just qc`. These gates remain unrun in this review.

## Additional Notes

The NCBI browser HTML fetch failed; primary Taxonomy EFetch and Datasets APIs succeeded. The phosphorus-paper publisher page also failed to open. Primary article text was inspected through an author-associated full-text HTML extraction, not visually verified PDF pages. No claim of complete supplementary-material or numerical-table verification is made.

A search collision was resolved at the primary PDB source: `5YB6` is a protein structure from Pseudomonas sp. AIU 813, and `PG6` is a small-molecule ligand code there, not this strain. No protein or biosynthetic pathway was transferred. Other uninspected search hits were not used as evidence. [RCSB 5YB6](https://www.rcsb.org/structure/5YB6)

The seed event wording matches the scope and attestation. Its timestamp `2026-09-13T17:54:04Z` matches the newest of the raw, ATB, and StrainInfo manifests under `src/taxonmech/seed.py:_seed_timestamp`; it is not a review date. No seed event, lifecycle promotion, or separate history artifact was added. The target was reread and verified unchanged before report creation.

Only this new report is written. No inventories, YAML records, generated pages, prior reports, GitHub objects, or cross-repository artifacts are changed; no paid research or outbound contact was used.

