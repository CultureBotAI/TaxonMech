# YAML Record Review: Pseudomonas sp. DAT14

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_dat14.yaml`
- Started UTC: 2026-10-07T08:09:00Z
- Finished UTC: 2026-10-07T08:12:42Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035621`, Pseudomonas sp. DAT14, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`, ten root-first ancestors and genetic code 11. It carries `EXACT` grounding, `SEEDED` mapping status, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, culture deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graphs are asserted. DAT14 is an isolate designation, not a verified culture accession. Generated YAML is read-only. Maintained source/extraction inputs and `src/taxonmech/seed.py` own future fixes, with scope and slug ownership in `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudomonas_sp_dat14.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_dat14.yaml --out /private/tmp/dat14-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/dat14-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, complete lineage, seven source inventories, path, scope and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and complete ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not prove byte-for-byte corpus reproduction.

`just validate-products` was not run: configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded. There are no literature/internal evidence references in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content/path searches found no target history artifact; none is created here.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222149` agrees on ID, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31629` agrees. Unique path and scope rows are `data/taxa/PATHS.tsv:14649` and `curation/seed_scope.tsv:322416`.

All ten ancestors match the committed parent chain in identifier, label, rank and order. Live EFetch confirms species rank, parent 196821, code 11, no alternate names and nine non-root ancestors; Datasets confirms the same chain including root. Gammaproteobacteria/Pseudomonadales/Pseudomonadaceae/Pseudomonas and the unclassified Pseudomonas parent agree. No retirement or replacement was found in the inspected lifecycle sources. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035621&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035621)

`EXACT` grounds this NCBI concept, not a validly published species binomial, strain-deposit equivalence or a new identification inferred from a marker.

## Evidence

The sole `NCBITAXON` attestation agrees on exact ID and label, count 1, unit `NAME` and snapshot note. It is not a count of strains or genomes. The complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore UID 333952288 resolves to `JF799915.1`, a 1,403-nt partial 16S rRNA marker. Complete GenBank metadata explicitly identifies Pseudomonas sp. DAT14, strain DAT14 and `taxon:1035621`. Its source is the active layer in permafrost, with a China/Qinghai-Tibet locality. The rRNA feature is partial at both ends. No culture-collection, BioSample, BioProject or assembly link is supplied. The metadata were read completely, excluding only sequence strings and translation/transcription payloads. [GenBank JF799915.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799915.1)

The marker cites an unpublished study of bacterial diversity in active-layer permafrost along the Qinghai-Tibet highway and a direct submission by Li, Xu and Zhang. Submission was 11 April 2011; creation/update were 30 May 2011. No DOI or PMID is linked. This is submission provenance, not independent published species confirmation. Locality and genus do not establish cold-growth or plant-growth-promoting phenotypes. The marker is not a genome.

Ten additional catalog hits were read completely and excluded as numeric-field or identifier-substring collisions:

| Native rows | Actual identity and reason for exclusion |
| --- | --- |
| `data/catalog/ncbi_genbank-0059.jsonl.gz:2529`; `data/catalog/gtdb_genomes-0017.jsonl.gz:39860` | GCA_937906985.1 and its GTDB row, uncultured Candidatus Nitrosopelagicus sp., NCBI taxid/species_taxid 1896163. Total and ungapped lengths are 1035621. This is an archaeal MAG, not DAT14. |
| `data/catalog/ncbi_genbank-0001.jsonl.gz:41772`; `data/catalog/ncbi_refseq-0001.jsonl.gz:24984`; `data/catalog/gtdb_genomes-0005.jsonl.gz:29144` | GCA_002291145.1, GCF_002291145.1 and the GTDB row, Streptomyces sp. SA15, taxid/species_taxid 934019. Ungapped length 10356218 contains the search digits. NCBI explicitly pairs the assemblies as identical; that relation remains confined to SA15. |
| `data/catalog/ncbi_genbank-0049.jsonl.gz:23446`; `data/catalog/ncbi_refseq_historical-0001.jsonl.gz:42466` | GCA_053539865.1 and GCF_053539865.1, Mycobacterium avium subsp. hominissuis Jc1476, taxid 439334/species_taxid 1764. BioSample SAMN21035621 contains the digits. The historical RefSeq record is suppressed, not-live date 2025-11-23. |
| `data/gold/analyses.jsonl.gz:437380` | Ga0653406, Salmonella enterica enterica sv. Stockholm 130377, project Gp0811390, GCA_007223555.1. IMG identifier 8103562174 contains the digits and is not an NCBI taxid. |
| `data/catalog/allthebacteria.tsv.xz:66266` | Staphylococcus aureus, sample SAMEA1035621, run ERR083794, ENA analysis ERZ3070808. Sample digits are not taxonomy; assembly/HQ filters are META_FAIL, independently preventing an eligible ATB link. |
| `data/catalog/allthebacteria.tsv.xz:3092483` | Salmonella enterica subsp. enterica, sample SAMN44339249, run SRR31035621, ENA analysis ERZ27111874. The match is within a run accession, not taxonomy. |

No culture-deposit/genome chain for DAT14 is supplied by those rows. NCBI/GTDB classification differences on unrelated genomes were not reconciled or imported.

A literature search hit was checked in the publisher's primary text. Figure 3 of DOI 10.1038/s41598-025-14065-1 concerns Pseudomonas sp. A-2 and defines DAT as days after treatment; its DAT14 measurements are not evidence about the strain named DAT14. No phenotypes or genomes from that paper are transferred. [Primary article, Figure 3](https://www.nature.com/articles/s41598-025-14065-1)

No gene, regulator, pathway, stress-response or transcriptomics assertion in this YAML requires an iModulonDB lookup. The adapter is not applicable; its absence is not negative biological evidence.

## Completeness

Zero BacDive strains and the optional omissions agree with inspected source scope. A marker's strain qualifier is not a culture deposit. Record-level literature evidence is optional for seeded records. No required gap was found.

Both local search stages included ignored/hidden files and compressed catalogs with `rg --no-ignore --hidden -n -z -i`. Roots were `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full per stage; history filenames were independently traversed.

The identity stage searched taxid 1035621, exact label, slug and DAT14 with case/separator variants. Thirteen lines matched: backbone, scope, native name and ten incidental catalog hits; all were read completely. The accession stage searched JF799915 with optional .1 and found no lines. Neither stage found matching source-metadata values or history paths. These negative findings include ignored files and are bounded to the specified roots and terms.

Web searches used Pseudomonas with DAT14 and JF799915. The accession search returned no results. No inspected exact-target publication or supported culture-deposit/genome chain was established. The exact-taxid Assembly zero carries a phrase-not-found warning and does not exclude assemblies filed under another identity. Exhaustive literature retrieval and sequence similarity were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, complete lineage, source provenance, zero strain count and seed history agree. Numeric coincidences and an experimental time-point abbreviation do not justify new biological links.

## Recommended Edits

None required. Do not patch generated YAML, join a taxid to lengths or substrings of sample/run/IMG identifiers, count JF799915.1 as a genome, import A-2 phenotypes, or promote `SEEDED` to `REVIEWED`.

A later authorized taxonomy-source refresh belongs in `conf/ncbi_taxdump.yaml` and `scripts/extract_source_inventory.py`, followed by guarded seeding. Optional literature annotations require maintained-input support merged by `src/taxonmech/seed.py` with tests under `docs/CURATION.md`. Habitat and phenotype assertions belong in the corresponding sibling corpora with claim-specific evidence.

## Follow-up Checks

- Require an exact culture-deposit and genome-source chain before adding strain/genome identifiers.
- Preserve marker accessions separately from assemblies and validate matches within the appropriate whole-identifier field.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`; validate any new history artifact. Full-corpus gates remain skipped here.

## Additional Notes

Primary NCBI taxonomy, Datasets, sequence-index and nucleotide reads succeeded. PMC access returned a browser challenge for the literature lead; the publisher's article supplied the inspected primary text instead.

Seed wording agrees with scope and attestation. Timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date. All three timestamps and the selection code were inspected.

The entire target was reread unchanged before report creation. An ignored-independent filename search found no previous report for this stem. Only this new repository report is added for this review; no record, inventory, page, old report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
