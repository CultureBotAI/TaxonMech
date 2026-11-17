# YAML Record Review: Arthrobacter sp. BAT8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_bat8.yaml`
- Started UTC: 2026-10-07T07:53:17Z
- Finished UTC: 2026-10-07T07:55:43Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035618`, Arthrobacter sp. BAT8, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:235627`, ten root-first ancestors and genetic code 11. It carries `EXACT` grounding, `SEEDED` mapping status, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, culture deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graphs are asserted. BAT8 is an isolate designation, not a verified culture accession. Generated YAML is read-only; maintained source/extraction inputs and `src/taxonmech/seed.py` own future fixes. Scope and slug ownership are in `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/arthrobacter_sp_bat8.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/arthrobacter_sp_bat8.yaml --out /private/tmp/bat-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/bat-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, complete lineage, seven source inventories, path, scope and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and complete ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not prove byte-for-byte corpus reproduction.

`just validate-products` was not run: configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded. There are no literature/internal evidence references in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content/path searches found no target history artifact; none is created here.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222146` agrees on ID, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31626` agrees. Unique path and scope rows are `data/taxa/PATHS.tsv:14646` and `curation/seed_scope.tsv:322413`.

All ten ancestors match the committed parent chain in identifier, label, rank and order. Live EFetch confirms species rank, parent 235627, code 11, no alternate names and nine non-root ancestors; Datasets confirms the same chain including root. Bacillati/Actinomycetota/Actinomycetes/Micrococcales/Micrococcaceae/Arthrobacter and the unclassified Arthrobacter parent agree. No retirement or replacement was found in the inspected lifecycle sources. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035618&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035618)

`EXACT` grounds this NCBI concept, not a validly published species binomial or a new species identification inferred from a marker. The NCBI genus is carried, not replaced with a plausible modern genus without exact-target evidence.

## Evidence

The sole `NCBITAXON` attestation agrees on ID, exact label, count 1, unit `NAME` and snapshot note. It is not a count of cultured strains or genome assemblies. The complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore UID 333952285 resolves to `JF799912.1`, a 1,378-nt partial 16S rRNA marker. Complete GenBank metadata explicitly identifies Arthrobacter sp. BAT8, strain BAT8 and `taxon:1035618`. Its source is the active layer in permafrost, with a China/Qinghai-Tibet locality. The rRNA feature is partial at both ends. No culture-collection, BioSample, BioProject or assembly link is supplied. The metadata were inspected in full, excluding only sequence strings and translation/transcription payloads. [GenBank JF799912.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799912.1)

The marker cites an unpublished study of bacterial diversity in active-layer permafrost along the Qinghai-Tibet highway and a direct submission by Li, Xu and Zhang. Submission was 11 April 2011; creation/update were 30 May 2011. No DOI or PMID is linked. This establishes submission provenance, not independent publication-based taxonomic confirmation. A permafrost isolation source alone establishes neither cold-growth performance nor another physiological phenotype. The marker is not a genome.

No gene, regulator, pathway, stress-response or transcriptomics assertion in this YAML requires an iModulonDB lookup. The adapter is not applicable; its absence is not negative biological evidence.

## Completeness

Zero BacDive strains and the optional omissions agree with inspected source scope. A marker's strain qualifier does not establish a missing BacDive deposit. Record-level literature evidence is optional for seeded records. No required gap was found.

Both local search stages included ignored/hidden files and compressed catalogs with `rg --no-ignore --hidden -n -z -i`. Roots were `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full per stage; history filenames were independently traversed.

The identity stage used taxid 1035618, exact label, slug and BAT8 with case/separator variants. Three lines matched: backbone, scope and native name; all were read completely. The accession stage searched JF799912 with optional .1 and found no lines. Neither stage found matching source-metadata values or history paths. These negative findings include ignored files and are bounded to those roots and terms.

Web searches used the exact label, BAT8 with Arthrobacter/16S and JF799912. They supplied no inspected exact-target publication or supported culture-deposit/genome chain. Broad enzyme-database search results were not evidence for this isolate and supplied no imported protein or phenotype claim. The exact-taxid Assembly zero carries a phrase-not-found warning and does not exclude assemblies filed under another identity. Exhaustive literature retrieval, sequence similarity and genome-equivalence analysis were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, complete lineage, source provenance, zero strain count and seed history agree. The marker supports the taxon's use without establishing an omitted culture deposit or genome.

## Recommended Edits

None required. Do not patch generated YAML, treat BAT8 as a culture accession, count JF799912.1 as a genome, infer a genus reassignment from neighboring taxa, or promote `SEEDED` to `REVIEWED`.

A later authorized taxonomy-source refresh belongs in `conf/ncbi_taxdump.yaml` and `scripts/extract_source_inventory.py`, followed by guarded seeding. Optional literature annotations require maintained-input support merged by `src/taxonmech/seed.py` with tests under `docs/CURATION.md`. Habitat and phenotype assertions belong in the corresponding sibling corpora with claim-specific evidence.

## Follow-up Checks

- Require an exact culture-deposit and genome-source chain before adding strain/genome identifiers.
- Preserve source-supplied marker identity without treating it as a genome or a species-equivalence claim.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`; validate any new history artifact. Full-corpus gates remain skipped here.

## Additional Notes

Primary NCBI taxonomy, Datasets, sequence-index and nucleotide metadata reads succeeded. All returned exact-taxid nucleotide records were inspected; this does not imply complete coverage of sequences under other taxids.

Seed wording agrees with scope and attestation. Timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date. All three timestamps and the selection code were inspected earlier in this turn.

The entire target was reread unchanged before report creation. An ignored-independent filename search found no previous report for this stem. Only this new repository report is added for this review; no record, inventory, page, old report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
