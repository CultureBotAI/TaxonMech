# YAML Record Review: Acinetobacter sp. K7SC-8A

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acinetobacter_sp_k7sc_8a.yaml`
- Started UTC: 2026-10-07T06:16:19Z
- Finished UTC: 2026-10-07T06:18:51Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035597`, `Acinetobacter sp. K7SC-8A`, rank `SPECIES`, domain `BACTERIA`. It has parent `NCBITaxon:196816`, genetic code 11, ten root-first lineage entries, `grounding_status: EXACT`, `mapping_status: SEEDED`, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, strains, genome links, definition, literature evidence, discussion, datasets, replacement or causal graph is asserted. This isolate-labelled NCBI concept is not a culture-collection accession and is distinct from K7SC-11A.

The YAML is generated and read-only. Future corrections belong to maintained extraction/source inputs or `src/taxonmech/seed.py` with tests; scope and locked-slug changes belong to `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`. No correction is required here.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` with offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/acinetobacter_sp_k7sc_8a.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/acinetobacter_sp_k7sc_8a.yaml --out /private/tmp/a8-strict.tsv` | Exit 0; one file scanned, zero ERROR rows. |
| `cat /private/tmp/a8-strict.tsv` | Actual TSV inspected; header only. |
| Structured comparison of backbone, full lineage, scope, path lock, source inventories and attestation | All bounded comparisons passed. |
| Exact scans of type material, merged IDs and dropped records | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |
| Structured iModulonDB dataset listing | Initial sandbox DNS failure; permitted network retry succeeded. No exact target dataset. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not establish byte-for-byte corpus reproduction.

`just validate-products` was not run: the configured OAK gate checks curator-added graph nodes, and this record has none. The NCBI lineage is not resolved through that gate. No literature or internal evidence references occur in the YAML. The seed event was checked; `just validate-history` was not run because ignored-independent content/path searches found no target history artifact and this review creates none.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222125` agrees on identifier, label, rank, parent, code, empty synonyms and snapshot `2026-09-13`. The complete native name row at `data/catalog/ncbi_names-0005.jsonl.gz:31604` agrees. The unique path and scope rows are `data/taxa/PATHS.tsv:14627` and `curation/seed_scope.tsv:322395`.

Every ancestor identifier, label, rank and position agrees with the committed parent chain. Live EFetch confirms nine non-root ancestors; Datasets confirms the same chain including root. Both resolve taxid 1035597 as Acinetobacter sp. K7SC-8A at species rank, and EFetch confirms parent 196816 and code 11. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035597&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035597)

The parent remains unclassified Acinetobacter. `EXACT` means exact grounding to this source concept, not species identification from sequence similarity or equivalence to a similarly designated isolate.

## Evidence

The sole `NCBITAXON` attestation agrees on source ID, exact label, count 1, unit `NAME` and snapshot note. Units are not summed across sources. No direct children were found in the backbone. Exact scans found no target rows in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Nuccore UID `334361519` is `JF799960.1`, a 1,529-nt partial 16S rRNA sequence. The source explicitly names strain K7SC-8A and `taxon:1035597`, with soil isolation and India: Kafni Glacier as the geographic qualifier. Complete metadata contains no culture-collection, assembly, BioSample or BioProject link. The submission is dated 11 April 2011; creation and update are 6 June 2011. Its bibliography lists an unpublished Kafni culturable-diversity study and direct submission, without a DOI or PMID. The marker is not a genome. [GenBank JF799960.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799960.1)

The 2011 Kafni study, `PMID:21918795`, `DOI:10.1007/s00792-011-0398-8`, was inspected through publisher metadata/abstract and the primary article's extracted text on ResearchGate. Methods distinguish cultured isolates from clone libraries; Table 3 explicitly lists K7Sc-8a. Its A. lwoffii DSM 2403 / X81665 entry is the nearest phylogenetic neighbor, not the target's deposit or accession. No equivalence, synonym, type-strain status or genome link follows. The extracted enzyme signs are corrupted into question marks, so individual enzyme results are not inferred from that extraction. No numerical phenotype is curated. [Publisher record](https://link.springer.com/article/10.1007/s00792-011-0398-8), [Primary article text](https://www.researchgate.net/publication/51644024_Comparison_of_bacterial_diversity_in_proglacial_soil_from_Kafni_Glacier_Himalayan_Mountain_ranges_India_with_the_bacterial_diversity_of_other_glaciers_in_the_world), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21918795/)

The 2022 pork-storage article, `DOI:10.1590/fst.80321`, names K7SC-8A in community results. Its methods use V4 16S amplicons, 97% OTU clustering and SILVA annotation; plate counts are total viable counts. These methods and results do not establish recovery or testing of the original glacier isolate. The community label therefore does not support strain-specific pork growth, spoilage causation, pathogenicity or a deposit/genome association. [Primary article, methods 2.4-2.5 and results 3.4](https://new.scielo.br/j/cta/a/5hmZkpPXtt9TvKZKFRHpLwq/?lang=en)

The fresh iModulonDB listing contained 28 dataset rows. Its Acinetobacter dataset is `a_baumannii/precise139`, not this target. It is not applicable and provides no negative phenotype evidence.

## Completeness

The zero BacDive strain count and optional-field omissions agree with the inspected inventories. A GenBank strain designation is not an omitted BacDive row, and literature is optional for this seeded record.

Two ignored-independent search stages covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using `rg --no-ignore --hidden -n -z -i`, including compressed catalogs. All five excluded `SOURCE.json` files were separately parsed in full for each stage, and history filenames independently traversed.

The identity stage searched taxid 1035597, full label, slug and K7SC-8A separator/case variants. Five lines matched: the three exact identity/name/scope rows above and two unrelated native genome rows, each read in full:

| Candidate | Reason rejected |
| --- | --- |
| `data/catalog/gtdb_genomes-0014.jsonl.gz:38042`, `GB_GCA_002315915.1` | UBA1737, Bacillales bacterium, taxid 1950247; 1035597 is total sequence length. |
| `data/catalog/ncbi_genbank-0001.jsonl.gz:42991`, `GCA_002315915.1` | UBA1737, Caryophanales bacterium, taxid 3700542; 1035597 is genome size. |

The source snapshots use different classifications for that unrelated MAG; neither identifies the target. Those records supply no target genome, sample or project link.

The accession/citation stage searched JF799960 with optional version, PMID 21918795 and both inspected DOI strings. No matches were found. Neither stage found matching metadata values or history paths. Absence claims apply only to the stated roots and terms.

The Assembly zero with its phrase-not-found warning is a bounded exact-taxid result, not proof that no genome exists under another identity. No supported missing strain-genome relationship, required attestation or required taxonomy field was identified.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. Identity, lineage, attestation, source count, lifecycle and optional-field omissions are supported within the inspected scope. Numeric collisions and literature sequence-classification labels do not justify new record assertions.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status; this report is not human sign-off.

Future enrichment must establish an explicit source chain before joining deposits or genomes. Phenotype and growth-context evidence belongs in the appropriate sibling corpus. Any authorized TaxonMech addition requires maintained input/seeder support with tests, not hand-edited YAML.

## Follow-up Checks

- Before phenotype curation, visually inspect the original 2011 table and supplementary material, including enzyme signs and the exact strain-to-accession association.
- Preserve the 2022 study's amplicon/community scope; require isolate-specific evidence before assigning effects to K7SC-8A.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`. Full-corpus gates remain skipped here.

## Additional Notes

Primary taxonomy and nucleotide APIs succeeded. The 2011 article was inspected as HTML-extracted text, not a visually checked PDF; publisher full text is subscription content. The 2022 publisher-hosted article methods and relevant results were inspected. No claim of complete numerical or supplementary-material verification is made.

The seed event wording agrees with the source attestation and scope. Its timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date.

The complete target was reread unchanged before report creation. An ignored-independent filename search found no prior report for this stem. Only this new report is added; no generated record, inventory, page, previous report, history, lifecycle status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
