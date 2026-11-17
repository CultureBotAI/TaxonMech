# YAML Record Review: Streptomyces sp. JAT10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_jat10.yaml`
- Started UTC: 2026-10-07T08:34:49Z
- Finished UTC: 2026-10-07T08:36:45Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035626`, Streptomyces sp. JAT10, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status and `strain_count: 0`. It has one NCBI name attestation and one seed event.

There are no synonyms, nomenclature, taxonomy mappings, culture deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graphs in the YAML. JAT10 is an isolate designation, not a verified culture accession. Generated records remain read-only; maintained source/extraction inputs and `src/taxonmech/seed.py` own future fixes, with scope and slug ownership in `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/streptomyces_sp_jat10.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/streptomyces_sp_jat10.yaml --out /private/tmp/jat10-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/jat10-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, complete lineage, seven inventories, path, scope and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Identity and complete ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons are not byte-for-byte corpus reproduction.

`just validate-products` was not run: configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded. No literature/internal evidence references occur in this YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content/path searches found no target history artifact.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222154` agrees on ID, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31634` agrees. Unique path and scope rows are `data/taxa/PATHS.tsv:14654` and `curation/seed_scope.tsv:322421`.

All ten ancestors match the committed parent chain in identifier, label, rank and order. Live EFetch confirms species rank, parent 2593676, code 11, no alternate names and nine non-root ancestors; Datasets confirms the chain including root. The Bacillati/Actinomycetota/Actinomycetes/Kitasatosporales/Streptomycetaceae/Streptomyces hierarchy and unclassified Streptomyces parent agree. No retirement or replacement was found in inspected lifecycle sources. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035626&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035626)

`EXACT` grounds this NCBI concept, not a validly published species binomial, culture-deposit equivalence or marker-based reidentification.

## Evidence

The sole `NCBITAXON` attestation agrees on exact ID and label, count 1, unit `NAME` and snapshot note. It does not count strains or genomes. A complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore UID 333952302 resolves to `JF799929.1`, a 1,387-nt partial 16S rRNA marker. Complete GenBank metadata names Streptomyces sp. JAT10, strain JAT10 and `taxon:1035626`. Source qualifiers describe active-layer permafrost in China/Qinghai-Tibet. The rRNA feature is partial at both ends. No culture-collection, BioSample, BioProject or assembly link is supplied. All metadata were inspected, excluding only sequence strings and translation/transcription payloads. [GenBank JF799929.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799929.1)

The marker cites an unpublished permafrost bacterial-diversity study and a direct submission by Li, Xu and Zhang. Submission was 11 April 2011; creation/update were 30 May 2011. No DOI or PMID is linked. This is submission provenance, not independent published species confirmation. Neither genus nor locality establishes cold-growth, antimicrobial production or other phenotypes. The marker is not a genome.

Both additional catalog hits were read completely and excluded:

| Native row | Actual identity and reason for exclusion |
| --- | --- |
| `data/catalog/allthebacteria.tsv.xz:66271` | Staphylococcus aureus, sample SAMEA1035626, run ERR083751, ENA analysis ERZ3070812. Matching sample digits are not taxonomy; META_FAIL assembly/HQ filters also preclude an eligible ATB link. |
| `data/catalog/allthebacteria.tsv.xz:551209` | Escherichia coli, sample SAMEA3375244, ENA analysis ERZ3259020. Matching digits occur in run ERR1035626, not a taxon field. |

No YAML gene, regulator, pathway, stress-response or transcriptomics assertion requires iModulonDB. The adapter is not applicable; this is not negative biological evidence.

## Completeness

Zero BacDive strains and optional omissions agree with inspected source scope. A marker strain qualifier is not a culture deposit. Literature evidence is optional for seeded records. No required gap was found.

Both local search stages included ignored/hidden files and compressed catalogs with `rg --no-ignore --hidden -n -z -i`. Roots: `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full per stage; history filenames were independently traversed.

Identity searches used taxid 1035626 as a complete digit run, exact label/slug and JAT10 with case/separator variants. Numeric boundaries exclude substrings within longer numbers; returned rows were checked structurally. Five lines matched: backbone, scope, native name and the two incidental ATB rows; all were read completely. The accession stage searched JF799929 with optional .1 and found no lines. Neither stage found matching source-metadata values or history paths. Negative local findings include ignored files and are bounded to these roots and terms.

Web searches for Streptomyces with JAT10 and for JF799929 returned no results. No inspected exact-target publication or supported culture-deposit/genome chain was established. The exact-taxid Assembly zero includes a phrase-not-found warning and does not exclude assemblies under another identity. Exhaustive literature retrieval and sequence similarity were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, full lineage, source provenance, zero strain count and seed history agree. Numeric coincidences do not establish biological links.

## Recommended Edits

None required. Do not patch generated YAML, join taxids to sample/run accession digits, count JF799929.1 as a genome, infer phenotypes from locality or promote `SEEDED` to `REVIEWED`.

An authorized taxonomy-source refresh belongs in `conf/ncbi_taxdump.yaml` and `scripts/extract_source_inventory.py`, followed by guarded seeding. Optional literature annotations need maintained-input support merged by `src/taxonmech/seed.py` with tests under `docs/CURATION.md`. Habitat and phenotype assertions belong in the corresponding sibling corpora with claim-specific evidence.

## Follow-up Checks

- Require an exact culture-deposit and genome-source chain before adding strain/genome identifiers.
- Keep marker accessions separate from assemblies; establish matching provenance for any same-label literature evidence.
- After authorized maintained-input changes, rerun both single-record validators, then `just verify-corpus` and `just qc`; validate any new history artifact. Full-corpus gates remain skipped here.

## Additional Notes

Primary NCBI taxonomy, Datasets, sequence-index and nucleotide reads succeeded. No exact-target publication was inspected; the marker's unpublished reference remains submission provenance only.

Seed wording agrees with scope and attestation. Timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date. The selection code and all three timestamps were inspected.

The entire YAML was reread unchanged before this report. An ignored-independent filename search found no previous report for this stem. Only this new report is added; no record, inventory, page, old report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
