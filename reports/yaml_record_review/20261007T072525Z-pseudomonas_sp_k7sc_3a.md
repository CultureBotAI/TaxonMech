# YAML Record Review: Pseudomonas sp. K7SC-3A

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_k7sc_3a.yaml`
- Started UTC: 2026-10-07T07:20:23Z
- Finished UTC: 2026-10-07T07:25:25Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035611`, Pseudomonas sp. K7SC-3A, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`, ten root-first ancestors and genetic code 11. It carries `EXACT` grounding, `SEEDED` mapping status, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, culture deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graphs are asserted. The suffix is an isolate designation, not a verified culture accession. Generated YAML is read-only. Maintained source/extraction inputs and `src/taxonmech/seed.py` own future corrections, with scope and slug ownership in `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudomonas_sp_k7sc_3a.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_k7sc_3a.yaml --out /private/tmp/ps3a-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/ps3a-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, complete lineage, seven source inventories, path, scope and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and complete ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not prove byte-for-byte reproduction.

`just validate-products` was not run: `conf/id_label_targets.yaml` covers curator-added graph nodes, absent here, and excludes NCBI taxonomy from OAK. There are no literature/internal evidence references in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content/path searches found no target history artifact; none is created here.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222139` agrees on ID, label, rank, parent, code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31618` agrees. Path and scope are unique at `data/taxa/PATHS.tsv:14641` and `curation/seed_scope.tsv:322409`.

All ten ancestors match the committed parent chain in identifier, label, rank and order. Live EFetch confirms species rank, parent 196821, code 11 and nine non-root ancestors; Datasets confirms the same chain including root. Pseudomonadaceae/Pseudomonas and direct parent unclassified Pseudomonas agree. No retirement or replacement was found in the inspected lifecycle sources. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035611&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035611)

`EXACT` grounds this NCBI concept, not a formal species determination or equivalence to Pseudomonas lutea. Keep K7SC-3A distinct from Bacillus/Lysinibacillus isolate K7SC-3b.

## Evidence

The sole `NCBITAXON` attestation agrees on source ID, exact label, count 1, unit `NAME` and snapshot note. Unlike units are not summed. The complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Nuccore UID `334361513` resolves to `JF799954.1`, a 1,512-nt partial 16S rRNA marker. Complete GenBank metadata explicitly identifies the target organism, strain K7SC-3A and `taxon:1035611`, with soil isolation and India: Kafni Glacier. No culture-collection, assembly, BioSample or BioProject link is supplied. Its references are an unpublished Kafni study and direct submission, without DOI or PMID. Submission is dated 11 April 2011; creation/update are 6 June 2011. The rRNA feature is partial at both ends. It is not a genome. [GenBank JF799954.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799954.1)

Primary PubMed metadata verifies the Kafni paper as `PMID:21918795`, `DOI:10.1007/s00792-011-0398-8`. Table 3 row 10 gives Pseudomonas lutea OK2T, AY364537, as K7Sc-3a's nearest neighbor at 98.5% 16S similarity. The column is a comparison, not an isolate accession/deposit assertion. Enzyme signs in the HTML extraction are unreliable and are not interpreted. [Primary article text](https://www.researchgate.net/publication/51644024_Comparison_of_bacterial_diversity_in_proglacial_soil_from_Kafni_Glacier_Himalayan_Mountain_ranges_India_with_the_bacterial_diversity_of_other_glaciers_in_the_world), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21918795/)

The full rendered Supplementary Fig. S3 on PDF page 4 was visually inspected for this target. It explicitly links Pseudomonas isolate K7SC-3a to JF799954, agreeing with the exact-taxid sequence result; no genus conflict is established. [Publisher supplementary figures](https://media.springernature.com/original/springer-static/esm/art:10.1007%2Fs00792-011-0398-8/MediaObjects/792_2011_398_MOESM2_ESM.pdf)

Complete primary metadata identifies comparator `AY364537.1` as a separate 1,531-nt partial 16S marker from Pseudomonas lutea OK2, taxon 243924, with explicit type-material status. Its linked `PMID:15143034` resolves to the 2004 species-description paper, `DOI:10.1099/ijs.0.02966-0`; the abstract names OK2T = LMG 21974T = CECT 5822T from Spanish grass rhizosphere soil. None of these deposits, type status or phenotypes transfers to K7SC-3A. [GenBank AY364537.1](https://www.ncbi.nlm.nih.gov/nuccore/AY364537.1), [Comparator publication](https://pubmed.ncbi.nlm.nih.gov/15143034/)

A Tyumen Scientific Centre catalog was downloaded after web retrieval timed out. Complete text was read, and rendered pages 1 and 5 were visually checked. Its introduction describes GenBank-based 16S screening of Siberian permafrost cultures. Row 61 lists culture 1/07 against multiple reference sequences; JF799954.1 has score 673 and 100% maximum identity. This is similarity evidence, not deposit equivalence or proof that the Himalayan isolate was collected in Siberia. No link is imported. [Institutional catalog](https://www.tmnsc.ru/wp-content/uploads/2014/08/%D0%9A%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3.pdf)

The successful 28-dataset iModulonDB listing from this session was fully re-inspected, not re-fetched. Its Pseudomonas entries cover other species, not K7SC-3A. With no target gene/regulator/omics claim, the adapter is not applicable. Absence is not negative phenotype evidence.

## Completeness

Zero BacDive strains and optional omissions agree with the inspected inventories. The marker's strain qualifier and the catalog's similarity hit do not establish missing deposits. Record-level literature evidence is optional for seeded records; no required gap was found.

Both local search stages included ignored/hidden files and compressed catalogs with `rg --no-ignore --hidden -n -z -i`. Roots were `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full per stage; history filenames were independently traversed.

Identity terms were taxid 1035611, exact label, slug and K7SC-3A case/separator variants. Exactly three lines matched: backbone, scope and native scientific-name rows above. Citation terms were JF799954 with optional version, PMID 21918795 and its DOI; no lines matched. Neither stage found matching metadata values or history paths. These negative findings include ignored files and are bounded to those roots and terms.

Web searches used the exact label and K7SC-3A with JF799954. No supported deposit/genome chain was established. Exact-taxid Assembly zero has a phrase-not-found warning and does not exclude genomes indexed under another identity. The main paper was read as HTML extraction, not a visually checked PDF; its supplementary DOC tables were not inspected.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, name provenance, source counts and seed history are supported. Nearest-neighbor and reference-sequence hits do not justify merging this record with another strain or species.

## Recommended Edits

None required. Do not patch generated YAML, import comparator deposits, promote `SEEDED` to `REVIEWED`, or count the marker as a genome.

Any later authorized source refresh belongs in `conf/ncbi_taxdump.yaml` and `scripts/extract_source_inventory.py`, followed by guarded seeding. Optional literature annotations require maintained-input support merged by `src/taxonmech/seed.py` with regression tests under `docs/CURATION.md`; no annotation is added by this review. Experimental traits and habitat claims belong to the corresponding sibling corpora.

## Follow-up Checks

- Require exact culture-deposit and genome-source chains before adding strain/genome identifiers; sequence similarity alone is insufficient.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`; validate any new history artifact.
- Preserve the distinction between K7SC-3A, K7SC-3b, comparator OK2 and catalog culture 1/07 in future searches.

## Additional Notes

Primary NCBI and PubMed API reads succeeded. The catalog web timeout was resolved by direct download; macOS PDFKit supplied extraction and rendering in scratch storage. The publisher supplement was rendered earlier in this session and re-inspected here. Its page-1 caption is visibly unfinished; no missing methodology is reconstructed.

Seed wording agrees with scope and attestation. Timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date.

The whole target was reread unchanged before report creation. An ignored-independent filename search found no previous report for this stem. Only this new repository report is added; no record, inventory, page, old report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
