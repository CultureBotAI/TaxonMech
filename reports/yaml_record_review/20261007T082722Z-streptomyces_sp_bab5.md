# YAML Record Review: Streptomyces sp. BAB5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_bab5.yaml`
- Started UTC: 2026-10-07T08:24:43Z
- Finished UTC: 2026-10-07T08:27:22Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035624`, Streptomyces sp. BAB5, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2593676`, ten root-first ancestors and genetic code 11. It carries `EXACT` grounding, `SEEDED` mapping status, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, culture deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graphs are asserted. BAB5 is an isolate designation, not a verified culture accession. Generated YAML is read-only. Maintained source/extraction inputs and `src/taxonmech/seed.py` own future fixes, with scope and slug ownership in `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/streptomyces_sp_bab5.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/streptomyces_sp_bab5.yaml --out /private/tmp/bab5-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/bab5-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, complete lineage, seven source inventories, path, scope and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and complete ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not prove byte-for-byte corpus reproduction.

`just validate-products` was not run: configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded. There are no literature/internal evidence references in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content/path searches found no target history artifact; none is created here.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222152` agrees on ID, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31632` agrees. Unique path and scope rows are `data/taxa/PATHS.tsv:14652` and `curation/seed_scope.tsv:322419`.

All ten ancestors match the committed parent chain in identifier, label, rank and order. Live EFetch confirms species rank, parent 2593676, code 11, no alternate names and nine non-root ancestors; Datasets confirms the same chain including root. Bacillati/Actinomycetota/Actinomycetes/Kitasatosporales/Streptomycetaceae/Streptomyces and the unclassified Streptomyces parent agree. No retirement or replacement was found in the inspected lifecycle sources. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035624&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035624)

`EXACT` grounds this NCBI concept, not a validly published species binomial, strain-deposit equivalence or a new identification inferred from a marker.

## Evidence

The sole `NCBITAXON` attestation agrees on exact ID and label, count 1, unit `NAME` and snapshot note. It is not a count of strains or genomes. The complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore UID 333952286 resolves to `JF799913.1`, a 1,443-nt partial 16S rRNA marker. Complete GenBank metadata explicitly identifies Streptomyces sp. BAB5, strain BAB5 and `taxon:1035624`. Its source is the active layer in permafrost, with a China/Qinghai-Tibet locality. The rRNA feature is partial at both ends. No culture-collection, BioSample, BioProject or assembly link is supplied. The metadata were read completely, excluding only sequence strings and translation/transcription payloads. [GenBank JF799913.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799913.1)

The marker cites an unpublished study of bacterial diversity in active-layer permafrost along the Qinghai-Tibet highway and a direct submission by Li, Xu and Zhang. Submission was 11 April 2011; creation/update were 30 May 2011. No DOI or PMID is linked. This is submission provenance, not independent published species confirmation. Locality and genus do not establish cold-growth, antimicrobial production or other phenotypes. The marker is not a genome.

Three additional catalog hits were read completely and excluded:

| Native row | Actual identity and reason for exclusion |
| --- | --- |
| `data/catalog/ncbi_genbank-0051.jsonl.gz:19545` | GCA_055615715.1, Streptococcus pneumoniae, taxid/species_taxid 1313, SAMEA120831644. The field `isolate: 1035624` is an isolate label, not the target taxid. Its PMID 30286803 pointer belongs to that unrelated row and was not used as target evidence. |
| `data/catalog/allthebacteria.tsv.xz:66269` | Staphylococcus aureus, sample SAMEA1035624, run ERR083735, ENA analysis ERZ3070805. Matching sample digits are not taxonomy; META_FAIL assembly/HQ filters also preclude an eligible ATB link. |
| `data/catalog/allthebacteria.tsv.xz:551207` | Escherichia coli, SAMEA3375242, ENA analysis ERZ3259019. The matching digits occur in run accession ERR1035624, not a taxon field. |

A same-designation literature lead was inspected in its institutional abstract. Bassam Qasim Mohammed's 2017 M.Sc. thesis describes an Iraqi soil-isolate collection containing Bab5. That provenance does not establish identity with the 2011 Qinghai-Tibet BAB5 submission. The abstract's detailed metabolite work concerns Bag3, so it cannot support those claims for this target even by matching Bab5's label. No antimicrobial or antitumor findings are transferred. The full thesis was not inspected. [Al-Nahrain University thesis abstract](https://nahrainuniv.edu.iq/ar/node/5391)

No gene, regulator, pathway, stress-response or transcriptomics assertion in this YAML requires an iModulonDB lookup. The adapter is not applicable; its absence is not negative biological evidence.

## Completeness

Zero BacDive strains and the optional omissions agree with inspected source scope. A marker's strain qualifier is not a culture deposit. Record-level literature evidence is optional for seeded records. No required gap was found.

Both local search stages included ignored/hidden files and compressed catalogs with `rg --no-ignore --hidden -n -z -i`. Roots were `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full per stage; history filenames were independently traversed.

The identity stage searched taxid 1035624 as a complete digit run, exact label, slug and BAB5 with case/separator variants. Numeric boundaries exclude substrings within longer numbers; every returned row was still checked against its structured identity fields. Six lines matched: backbone, scope, native name and the three incidental catalog hits; all were read completely. The accession stage searched JF799913 with optional .1 and found no lines. Neither stage found matching source-metadata values or history paths. These negative findings include ignored files and are bounded to the specified roots and terms.

Web searches used Streptomyces with BAB5 and JF799913. The accession search returned no results. Broader taxonomy and thesis search results were leads; only the institutional abstract above was used for the homonym assessment. No inspected exact-target publication or supported culture-deposit/genome chain was established. The exact-taxid Assembly zero carries a phrase-not-found warning and does not exclude assemblies filed under another identity. Exhaustive literature retrieval and sequence similarity were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, complete lineage, source provenance, zero strain count and seed history agree. Numeric coincidences and a reused isolate designation do not justify new biological links.

## Recommended Edits

None required. Do not patch generated YAML, join taxids to isolate labels or sample/run accession digits, count JF799913.1 as a genome, transfer the Iraqi study's observations, or promote `SEEDED` to `REVIEWED`.

A later authorized taxonomy-source refresh belongs in `conf/ncbi_taxdump.yaml` and `scripts/extract_source_inventory.py`, followed by guarded seeding. Optional literature annotations require maintained-input support merged by `src/taxonmech/seed.py` with tests under `docs/CURATION.md`. Habitat and phenotype assertions belong in the corresponding sibling corpora with claim-specific evidence.

## Follow-up Checks

- Require an exact culture-deposit and genome-source chain before adding strain/genome identifiers.
- Preserve marker accessions separately from assemblies; any further same-label literature review must establish matching provenance rather than infer equivalence.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`; validate any new history artifact. Full-corpus gates remain skipped here.

## Additional Notes

Primary NCBI taxonomy, Datasets, sequence-index and nucleotide reads succeeded. The institutional thesis abstract was inspected as primary source context, not used as a source for BAB5 phenotypes.

Seed wording agrees with scope and attestation. Timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date. All three timestamps and the selection code were inspected.

The entire target was reread unchanged before report creation. An ignored-independent filename search found no previous report for this stem. Only this new repository report is added for this review; no record, inventory, page, old report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
