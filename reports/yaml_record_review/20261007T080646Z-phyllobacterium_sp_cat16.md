# YAML Record Review: Phyllobacterium sp. CAT16

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/phyllobacterium_sp_cat16.yaml`
- Started UTC: 2026-10-07T08:02:10Z
- Finished UTC: 2026-10-07T08:06:46Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035620`, Phyllobacterium sp. CAT16, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2638441`, ten root-first ancestors and genetic code 11. It carries `EXACT` grounding, `SEEDED` mapping status, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, culture deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graphs are asserted. CAT16 is an isolate designation, not a verified culture accession. Generated YAML is read-only. Maintained source/extraction inputs and `src/taxonmech/seed.py` own future fixes, with scope and slug ownership in `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/phyllobacterium_sp_cat16.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/phyllobacterium_sp_cat16.yaml --out /private/tmp/cat16-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/cat16-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, complete lineage, seven source inventories, path, scope and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and complete ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not prove byte-for-byte corpus reproduction.

`just validate-products` was not run: configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded. There are no literature/internal evidence references in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content/path searches found no target history artifact; none is created here.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222148` agrees on ID, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31628` agrees. Unique path and scope rows are `data/taxa/PATHS.tsv:14648` and `curation/seed_scope.tsv:322415`.

All ten ancestors match the committed parent chain in identifier, label, rank and order. Live EFetch confirms species rank, parent 2638441, code 11, no alternate names and nine non-root ancestors; Datasets confirms the same chain including root. Alphaproteobacteria/Hyphomicrobiales/Phyllobacteriaceae/Phyllobacterium and the unclassified Phyllobacterium parent agree. No retirement or replacement was found in the inspected lifecycle sources. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035620&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035620)

`EXACT` grounds this NCBI concept, not a validly published species binomial, strain-deposit equivalence or a new identification inferred from a marker.

## Evidence

The sole `NCBITAXON` attestation agrees on exact ID and label, count 1, unit `NAME` and snapshot note. It is not a count of strains or genomes. The complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore UID 333952296 resolves to `JF799923.1`, a 1,355-nt partial 16S rRNA marker. Complete GenBank metadata explicitly identifies Phyllobacterium sp. CAT16, strain CAT16 and `taxon:1035620`. The source is the active layer in permafrost, with a China/Qinghai-Tibet locality. The rRNA feature is partial at both ends. No culture-collection, BioSample, BioProject or assembly link is supplied. The metadata were read completely, excluding only sequence strings and translation/transcription payloads. [GenBank JF799923.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799923.1)

The marker cites an unpublished study of bacterial diversity in active-layer permafrost along the Qinghai-Tibet highway and a direct submission by Li, Xu and Zhang. Submission was 11 April 2011; creation/update were 30 May 2011. No DOI or PMID is linked. This is submission provenance, not independent published species confirmation. Locality and genus do not establish cold-growth, plant association or nitrogen-fixation phenotypes. The marker is not a genome.

Four additional catalog hits were read completely and excluded:

| Native row | Actual identity and reason for exclusion |
| --- | --- |
| `data/bvbrc/bvbrc-0023.jsonl.gz:48262` | BV-BRC 562.67550, Escherichia coli strain Cat16, taxid 562; linked GCA_015624625.1, SAMN16063145 and PRJNA661559. The bare strain label is a homonym, not a target link. |
| `data/catalog/ncbi_genbank-0014.jsonl.gz:8265` | GCA_015624625.1, E. coli strain Cat16, taxid/species_taxid 562; same sample/project. The source explicitly pairs it with GCF_015624625.1 as identical, but neither denotes this Phyllobacterium isolate. |
| `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:33791` | GCF_015624625.1, E. coli strain Cat16, taxid/species_taxid 562, same BioSample; status suppressed, not-live date 2020-11-25. This historical row is not evidence of a current target assembly. |
| `data/catalog/ncbi_genbank-0054.jsonl.gz:8657` | GCA_058537585.1, Bathyarchaeaceae archaeon (SeqCode), taxid/species_taxid 3107053; both genome-length fields equal 1035620. The matching number is a length, not a taxon identifier. |

Source-declared assembly pairing for the unrelated E. coli rows was preserved without transferring it to CAT16. The archaeal metagenome-derived assembly, its sample and its project likewise supply no target relationship.

No gene, regulator, pathway, stress-response or transcriptomics assertion in this YAML requires an iModulonDB lookup. The adapter is not applicable; its absence is not negative biological evidence.

## Completeness

Zero BacDive strains and the optional omissions agree with inspected source scope. A marker's strain qualifier is not a culture deposit. Record-level literature evidence is optional for seeded records. No required gap was found.

Both local search stages included ignored/hidden files and compressed catalogs with `rg --no-ignore --hidden -n -z -i`. Roots were `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full per stage; history filenames were independently traversed.

The identity stage used taxid 1035620, exact label, slug and CAT16 with case/separator variants. Seven lines matched: backbone, scope, native name and the four catalog hits above; all were read completely. The accession stage searched JF799923 with optional .1 and found no lines. Neither stage found matching source-metadata values or history paths. These negative findings include ignored files and are bounded to the specified roots and terms.

A web search used Phyllobacterium with CAT16. Search snippets were treated only as leads and did not establish an exact-target publication. No supported culture-deposit/genome chain or inspected exact-target publication was established. The exact-taxid Assembly zero carries a phrase-not-found warning and does not exclude assemblies filed under another identity. Exhaustive literature retrieval and sequence similarity were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, complete lineage, source provenance, zero strain count and seed history agree. Bare strain-label homonyms and numeric-field coincidences do not justify genome links.

## Recommended Edits

None required. Do not patch generated YAML, join bare Cat16 strain names across genera, match a taxid to a genome-length field, count JF799923.1 as a genome, infer genus-wide phenotypes, or promote `SEEDED` to `REVIEWED`.

A later authorized taxonomy-source refresh belongs in `conf/ncbi_taxdump.yaml` and `scripts/extract_source_inventory.py`, followed by guarded seeding. Optional literature annotations require maintained-input support merged by `src/taxonmech/seed.py` with tests under `docs/CURATION.md`. Habitat and phenotype assertions belong in the corresponding sibling corpora with claim-specific evidence.

## Follow-up Checks

- Require an exact culture-deposit and genome-source chain before adding strain/genome identifiers.
- Preserve marker accessions separately from assemblies; distinguish current and historical assembly states, and restrict matching to the relevant structured identifier field.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`; validate any new history artifact. Full-corpus gates remain skipped here.

## Additional Notes

Primary NCBI taxonomy, Datasets, sequence-index and nucleotide reads succeeded. The target's own assertions were checked independently of nearby records from the same submission series.

Seed wording agrees with scope and attestation. Timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date. All three timestamps and the selection code were inspected.

The entire target was reread unchanged before report creation. An ignored-independent filename search found no previous report for this stem. Only this new repository report is added for this review; no record, inventory, page, old report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
