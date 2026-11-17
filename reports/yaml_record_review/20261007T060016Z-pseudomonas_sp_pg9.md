# YAML Record Review: Pseudomonas sp. PG9

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_pg9.yaml`
- Started UTC: 2026-10-07T05:58:13Z
- Finished UTC: 2026-10-07T06:00:16Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read before judging it: `NCBITaxon:1035593`, `Pseudomonas sp. PG9`, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`, genetic code 11. It carries ten lineage entries, `grounding_status: EXACT`, `mapping_status: SEEDED`, zero BacDive strains, one NCBI name attestation, and one seed event.

No synonyms, nomenclature, taxonomy mappings, strains, genome links, record-level evidence, definition, discussion, dataset, replacement, or causal graph is asserted. PG9 is part of this NCBI placeholder label; it is not itself a registered culture-collection accession. All seeded YAML remains read-only.

Future corrections belong to maintained source/extraction inputs, `src/taxonmech/seed.py` with tests, `curation/seed_scope.tsv` for membership, or `data/taxa/PATHS.tsv` for the pinned slug. None requires changing for the findings below.

## Validation

The uv commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` with offline dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudomonas_sp_pg9.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_pg9.yaml --out /private/tmp/p9-strict.tsv` | Exit 0; one file scanned, zero ERROR rows. |
| `cat /private/tmp/p9-strict.tsv` | Actual TSV read; header only, no findings. |
| Structured full-row comparison with NCBI inventory, lineage, scope, path lock and attestation | Passed; this is a bounded comparison, not regeneration. |
| Exact-token primary-source and status scans | No target rows in seven non-NCBI primary inventories, type material, merged IDs, or dropped records. |
| Live Taxonomy EFetch XML and Datasets JSON | Exact ID, label, rank, parent and ancestry agree. |
| Exact-taxid Assembly / nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, whose complete metadata was read. |
| Structured iModulonDB dataset listing | Successful; no exact PG9 dataset, so not applicable. |

Not checked: `just verify-corpus`, `just qc`, full-corpus validation, tests, provenance hashing, generated-site drift, documentation statistics, and vendored checks. No narrow custom check is represented as a substitute for a full-corpus gate.

`just validate-products` was not run: the configured gate checks curator-added graph nodes, and this YAML has none. It is not the NCBI lineage validator. No optional literature or internal evidence references are asserted in the YAML. The existing seed event was checked, but `just validate-history` was not run: ignored-independent content and path searches found no corresponding separate history artifact, and no history write is authorized by this review.

## Identity and Grounding

The full row at `data/raw/ncbitaxon_taxa.tsv:222121` supports taxid, label, rank, parent, genetic code, empty synonyms, and snapshot `2026-09-13`. The complete native name row at `data/catalog/ncbi_names-0005.jsonl.gz:31600` is an exact scientific-name match. The path lock at `data/taxa/PATHS.tsv:14623` and scope at `curation/seed_scope.tsv:322391` identify this target without ambiguity.

The complete root-first ancestor chain agrees with the committed backbone. NCBI EFetch independently agrees on all nine non-root ancestors; Datasets supplies root and the same ten-ID chain. The direct parent is unclassified Pseudomonas, not Pseudomonas putida. The live name, species rank, Bacteria placement and code 11 agree. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035593&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035593)

`EXACT` correctly describes this source concept; it does not imply a formally established species name, isolate equivalence with another PG designation, or a taxonomic reassignment based on marker similarity.

## Evidence

The one NCBI attestation has the correct source ID, source label, count 1, unit `NAME`, and snapshot note. It is not a count of strains or genomes. The backbone has no direct children for this taxon. Exact target searches in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, and `bactotraits_taxa.tsv` returned no rows.

Nuccore UID `333494187` resolves to `JF345179.1`, a 1,498-nt partial 16S rRNA sequence, with source strain PG9 and explicit `taxon:1035593`. Its full metadata contains no culture-collection, assembly, BioSample, BioProject, host, or isolation-source qualifier. Submission was 17 February 2011; creation and update dates are 15 and 29 August 2011. This is a nucleotide marker, not an assembly. [GenBank JF345179.1](https://www.ncbi.nlm.nih.gov/nuccore/JF345179.1)

The GenBank bibliography and inspected 2011 article Table 2 link PG9 to JF345179: `PMID:21840210`, `DOI:10.1016/j.biortech.2011.07.064`. AM411059.1 is its nearest-neighbor comparator, not PG9's own sequence. The seven-strain plant treatment does not establish PG9-alone plant effects. [2011 primary article](https://www.academia.edu/22554591/Arsenic_resistant_bacteria_solubilized_arsenic_in_the_growth_media_and_increased_growth_of_arsenic_hyperaccumulator_Pteris_vittata_L)

The inspected phosphorus paper includes PG9 in its spent-medium assays, but its tomato experiments select PG6 and PG12, not PG9: `PMID:25880602`, `DOI:10.1016/j.chemosphere.2015.03.048`. No plant benefit or enzyme identity is transferred to PG9. [2015 primary article](https://www.academia.edu/22554621/Phosphorus_solubilization_and_plant_growth_enhancement_by_arsenic_resistant_bacteria)

The primary abstract of `PMID:25576133`, `DOI:10.1016/j.chemosphere.2014.12.046`, explicitly includes PG9 in its comparative arsenate-reduction group, but the reported group ranges do not specify an individual PG9 measurement. The primary abstract of `PMID:26547029`, `DOI:10.1016/j.chemosphere.2015.10.096`, does not resolve PG9-specific plant effects. These are bounded literature leads, not support for adding a genome, gene, or quantitative phenotype to this YAML. [Arsenic-transformation abstract](https://pubmed.ncbi.nlm.nih.gov/25576133/), [Plant-study abstract](https://pubmed.ncbi.nlm.nih.gov/26547029/)

The common papers' primary abstracts, DOI/PMID metadata, and relevant 2011/2015 full-text passages were inspected during this review session; their use for PG9 rests on its independently inspected GenBank linkage and the explicit PG9 text, not another taxon's report. Full methods for the last two papers and visually rendered PDFs were not inspected.

The fresh structured iModulonDB listing returned 28 dataset rows, including other Pseudomonas species but no PG9 match. No component search was applicable. Absence from that listing is not negative biological evidence.

## Completeness

Zero BacDive strains and the omitted source-specific sections are consistent with the inspected inventories. A strain-designated taxon and its marker sequence do not establish a deposit match or a strain-to-genome relationship. Literature evidence is optional for seeded records, so omission of a phenotype narrative is not a record defect.

Ignored-independent searches included `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, using `rg --no-ignore --hidden -n -z -i`. Compressed catalogs were searched. The five `SOURCE.json` files were excluded from text output but separately parsed in full; history filenames were independently traversed.

The identity stage searched taxid 1035593, full label, slug, and genus-associated PG9 separator variants. It returned only the three backbone, native-name, and scope rows, all read in full. The accession stage searched JF345179 with optional version and all four DOI/PMID pairs above; no rows matched. Both stages found no matching source metadata value or history path. These results establish bounded local absence under the named roots, not global database or publication absence.

The exact-taxid Assembly count 0 carried a phrase-not-found warning. No missing assembly was established, but that query is not evidence that an assembly could never exist under another source identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record's identity, ancestry, source count, grounding and lifecycle fields are supported. No claim in the YAML improperly generalizes a consortium, neighboring strain, marker comparator, or plant treatment.

## Recommended Edits

None required. Keep the YAML generated and its status `SEEDED`; an automated review report is not human sign-off.

Future literature enrichment must preserve exact strain and experiment scope. Future genome enrichment requires a supported culture-deposit or other explicit source identity chain. Route any authorized TaxonMech change through maintained inputs and the seeder, with tests; phenotype and growth-context work belongs in the appropriate sibling corpus.

## Follow-up Checks

- Before numerical curation, inspect the original article PDFs and strain-specific methods/results. Do not infer PG9 plant effects from treatments of PG6, PG12, or a mixed inoculum.
- Keep JF345179.1 typed as a marker sequence; do not treat AM411059.1 or a matching short label as an equivalent strain or assembly.
- After any authorized upstream correction, rerun the two single-record validators, then `just verify-corpus` and `just qc`. Those full-corpus checks were skipped here.

## Additional Notes

The NCBI browser HTML request failed; primary EFetch and Datasets reads succeeded. Broader search leads were not promoted to evidence where the primary text could not be inspected or an exact identity link was missing. In particular, search-only PG9 labels do not establish an alias. No unsupported absence claim relies on search-engine results.

The source papers were read as primary abstracts and author-associated HTML full-text extraction, not visually checked PDF pages. No claim of exhaustive literature, supplementary-material, or quantitative-table verification is made.

The seed event's wording agrees exactly with the scope reason and attestation. Its timestamp `2026-09-13T17:54:04Z` follows the newest of the raw, ATB, and StrainInfo manifest timestamps under `src/taxonmech/seed.py:_seed_timestamp`. That timestamp is not this review's date.

The target was reread unchanged before writing this report. Only this new report is added: no taxon, inventory, source artifact, prior report, generated page, history event, lifecycle state, GitHub object, or cross-repository file is changed. No paid research or outbound contact was used.

