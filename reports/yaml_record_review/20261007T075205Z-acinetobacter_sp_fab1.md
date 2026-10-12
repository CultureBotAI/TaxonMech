# YAML Record Review: Acinetobacter sp. FAB1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acinetobacter_sp_fab1.yaml`
- Started UTC: 2026-10-07T07:49:05Z
- Finished UTC: 2026-10-07T07:52:05Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035617`, Acinetobacter sp. FAB1, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196816`, ten root-first ancestors and genetic code 11. It carries `EXACT` grounding, `SEEDED` mapping status, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, culture deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graphs are asserted. FAB1 is an isolate designation, not a verified culture-collection accession. Generated YAML is read-only. Maintained source/extraction inputs and `src/taxonmech/seed.py` own future fixes, with scope and slug ownership in `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/acinetobacter_sp_fab1.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/acinetobacter_sp_fab1.yaml --out /private/tmp/fab-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/fab-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, complete lineage, seven source inventories, path, scope and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and complete ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not prove byte-for-byte corpus reproduction.

`just validate-products` was not run: configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded. There are no literature/internal evidence references in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content/path searches found no target history artifact; none is created here.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222145` agrees on ID, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31625` agrees. Unique path and scope rows are `data/taxa/PATHS.tsv:14645` and `curation/seed_scope.tsv:322412`.

All ten ancestors match the committed parent chain in identifier, label, rank and order. Live EFetch confirms species rank, parent 196816, code 11, no alternate names and nine non-root ancestors; Datasets confirms the same chain including root. Moraxellales/Moraxellaceae/Acinetobacter and the unclassified Acinetobacter parent agree. No retirement or replacement was found in the inspected lifecycle sources. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035617&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035617)

`EXACT` grounds this NCBI concept, not a validly published species binomial or equivalence to another organism sharing FAB1 in its designation.

## Evidence

The sole `NCBITAXON` attestation agrees on ID, exact label, count 1, unit `NAME` and snapshot note. It is not a count of strains or genomes. The complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore UID 333952291 resolves to `JF799918.1`, a 1,425-nt partial 16S rRNA marker. Complete GenBank metadata explicitly identifies Acinetobacter sp. FAB1, strain FAB1 and `taxon:1035617`. Its source is the active layer in permafrost, with a China/Qinghai-Tibet locality. The feature is partial at both ends. No culture-collection, BioSample, BioProject or assembly link is supplied. An unpublished bacterial-diversity study and direct submission by Li, Xu and Zhang are cited without DOI or PMID; submission was 11 April 2011 and creation/update 30 May 2011. This marker is not a genome and its locality does not establish a physiological phenotype. [GenBank JF799918.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799918.1)

Four additional native catalog rows were read completely and excluded as designation-substring matches to a different organism:

| Native row | Explicit identity |
| --- | --- |
| `data/bvbrc/bvbrc-0002.jsonl.gz:35241` | Genome 1352.19582, Enterococcus faecium TATVAM-FAB1, taxid 1352. |
| `data/catalog/ncbi_genbank-0042.jsonl.gz:43547` | GCA_046537615.1, Enterococcus faecium, strain TATVAM-FAB1, taxid/species_taxid 1352. |
| `data/catalog/ncbi_refseq-0007.jsonl.gz:2031` | GCF_046537615.1, same Enterococcus strain, with an explicit identical GenBank counterpart. |
| `data/catalog/gtdb_genomes-0016.jsonl.gz:10871` | RS_GCF_046537615.1, GTDB Enterococcus_B faecium; NCBI taxid/species_taxid 1352 and TATVAM-FAB1 identifiers. |

These rows carry BioSample SAMN38138613 and WGS JAYDZD metadata. None denotes the Acinetobacter target. A suffix matching FAB1 cannot transfer their assembly, sample or GTDB classification here.

A web literature candidate, `PMID:31372943` / `DOI:10.1007/s10482-019-01306-3`, was read through the primary PubMed XML. Its 2019 abstract names several rhizobacterial genera and isolate labels, including FAB1, but supplies no JF799918 or exact-taxid connection. A later primary article, `PMCID:PMC10193011`, `PMID:37213696`, `DOI:10.1016/j.sjbs.2023.103664`, was checked via its full-text XML metadata and complete section 2.1. It explicitly identifies the FAB1 carried forward from the 2019 study as Bacillus subtilis. This is a different organism, not evidence to rename this record or import plant-growth/biofilm traits. Only the identity methods section, not the later article's full experimental results, was used. [2019 PubMed record](https://pubmed.ncbi.nlm.nih.gov/31372943/), [2023 primary article XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10193011/fullTextXML)

The YAML asserts no gene, regulator, pathway, stress response or transcriptomics dataset requiring iModulonDB. FAB1 is a strain designation here, not the similarly spelled gene name. The adapter is not applicable, and its absence is not negative phenotype evidence.

## Completeness

Zero BacDive strains and the optional omissions agree with inspected source scope. A marker's strain qualifier does not establish a missing BacDive deposit. Record-level literature evidence is optional for seeded records. No required gap was found.

Both local search stages included ignored/hidden files and compressed catalogs with `rg --no-ignore --hidden -n -z -i`. Roots were `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full per stage; history filenames were independently traversed.

The identity stage used taxid 1035617, label, slug and FAB1 with case/separator variants. Seven lines matched: backbone, scope, native name and the four Enterococcus rows. Every matching row was read completely. The accession stage searched JF799918 with optional .1 and found no lines. Neither stage found matching source-metadata values or history paths. These negative findings include ignored files and are bounded to those roots and terms.

Web searches used the exact label, FAB1 with Acinetobacter/16S, JF799918, and the unpublished study title. No supported culture-deposit/genome chain was established. The exact-taxid Assembly zero carries a phrase-not-found warning and does not exclude genomes under another identity. An accession-bearing PDF search hit was not inspected or used as evidence; this was not an exhaustive literature review.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, complete lineage, source provenance, counts and seed history agree. Enterococcus TATVAM-FAB1 and the Bacillus subtilis FAB1 literature must remain distinct from this target.

## Recommended Edits

None required. Do not patch generated YAML, join designation substrings, count JF799918.1 as a genome, import another FAB1 isolate's experimental traits, or promote `SEEDED` to `REVIEWED`.

A later authorized taxonomy-source refresh belongs in `conf/ncbi_taxdump.yaml` and `scripts/extract_source_inventory.py`, followed by guarded seeding. Optional literature annotations require maintained-input support merged by `src/taxonmech/seed.py` with tests under `docs/CURATION.md`. Traits and habitats belong in the corresponding sibling corpora with claim-specific evidence.

## Follow-up Checks

- Require an exact culture-deposit and genome-source chain before adding strain/genome identifiers.
- Check accession, organism, source provenance and full designation together when literature or catalogs reuse FAB1.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`; validate any new history artifact. Full-corpus gates remain skipped here.

## Additional Notes

Primary NCBI taxonomy, nucleotide and PubMed API reads succeeded. The PubMed web page returned only boilerplate and the PMC page presented a browser check; primary PubMed XML and Europe PMC full-text XML supplied the inspected literature evidence instead.

Seed wording agrees with scope and attestation. Timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date. The manifest timestamps and selection code were inspected earlier in this turn.

The entire target was reread unchanged before report creation. An ignored-independent filename search found no previous report for this stem. Only this new repository report is added for this review; no record, inventory, page, old report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
