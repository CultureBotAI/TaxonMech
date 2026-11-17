# YAML Record Review: Shewanella sp. HdiPB02

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/shewanella_sp_hdipb02.yaml`
- Started UTC: 2026-10-10T00:35:06Z
- Finished UTC: 2026-10-10T00:36:44Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:1037356` denotes Shewanella sp. HdiPB02, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196818` (unclassified Shewanella), genetic code 11, grounding `EXACT`, status `SEEDED`.

It carries ten ancestors, no synonym list, zero inventoried BacDive strains, one NCBITAXON name attestation and a seed event. The laboratory designation does not justify changing the NCBI species rank.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/shewanella_sp_hdipb02.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/shewanella_sp_hdipb02.yaml --out /private/tmp/taxonmech-hdipb02-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons matched pinned identity, every ancestor, code, empty synonym columns, own attestation, PATHS/scope rows and seed text. Complete backbone scanning found no direct child; exact own-ID type-material, merged-ID and dropped scans found none.
- Native candidate rows, live taxonomy responses and primary marker metadata were read completely. The nucleotide query resolved the marker's explicit taxon/strain identity.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. Focused source agreement is not corpus reproduction. No causal graph is asserted, so `just validate-products` has no applicable nodes.
- Exact-name web searches returned no results; this is not a claim that no publication exists. No experimental manuscript, infection assay, genome comparison or independent taxonomic reconstruction was audited.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:222722` agrees with [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037356&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037356): exact name Shewanella sp. HdiPB02, species rank, parent 196818 and code 11.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Alteromonadales, Shewanellaceae, Shewanella and unclassified Shewanella. Each stored ID, label and rank matches the pinned backbone. EFetch confirms the chain below root; Datasets includes root 1.

`data/catalog/ncbi_names-0005.jsonl.gz:32336` contains the scientific name. The pinned exact/related/broad synonym columns are empty and live EFetch supplies no synonym. An omitted synonym list is supported by these inspected sources. Exact grounding identifies this NCBI concept; it does not assert a validated binomial, identity with a named Shewanella species or disease causation.

## Evidence

The sole NCBITAXON attestation has exact own ID/label, count 1, unit `NAME`, snapshot 2026-09-13. The count describes one source name assertion, not a genome or cultured-deposit count.

The live NCBI nucleotide query `txid1037356[Organism:exp]` returned one entry. The complete [JF781122 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF781122) identifies JF781122.1, a 600-base partial 16S rRNA marker with partial feature endpoints, explicitly Shewanella sp. HdiPB02, strain HdiPB02 and `taxon:1037356`. It is not a genome assembly or culture-collection accession and is not currently an asserted YAML link. The query result is a dated observation from one database, not a global sequence census.

The primary submission records host Haliotis diversicolor supertexta. Its bibliography labels the Li and Ke study as unpublished and includes a 2011 direct submission. The study title concerns isolation/identification of bacteria from diseased hosts, but a title and host qualifier are not proof that this isolate causes disease. No experimental causal or virulence claim is inferred, and no PMID or DOI is invented.

The record itself asserts taxonomy and provenance only: no host, pathogenicity, resistance, gene, transcriptomics or mechanism claim. The contextual marker evidence does not expand those assertions.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 1037356, HdiPB02 with optional space/hyphen/underscore separators, and the slug. Five matches comprised the own backbone/name/scope rows and two unrelated native assembly rows; all were inspected.

The GTDB and GenBank entries for `GCA_964355835.1` concern isolate ERP119705_co13_204, NCBI taxon 86473, not HdiPB02. Their genome-length value is 1037356. Matching that statistic does not establish taxon identity or a missing genome link. The separate NCBI/GTDB classifications on this unrelated assembly were not reconciled or transferred.

A follow-up ignored/compressed-inclusive JF781122 search over the same roots returned no matches. Five SOURCE.json files were separately parsed without a target match. Gitignore-independent filename enumeration under the taxon corpus and report directory found the single target YAML and no prior report; history filename inspection found no target-specific filename. These are bounded repository checks, not global absence claims.

Complete structured own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. With no direct backbone child, there is no descendant inventory to aggregate. Zero correctly counts inventoried BacDive entries, not the existence of a research isolate. No repository-supported deposit/genome identity chain was established.

Optional definition, nomenclature, mappings, record-level evidence and causal graphs need not be invented. iModulonDB was not applicable because the YAML asserts no gene, regulator, pathway or transcriptomics result. The host/submission-title context is not a module claim; no adapter execution or global dataset absence is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, rank, lineage, provenance, count semantics and seed status are supported. Skipped corpus checks and unverified experimental pathogenicity remain explicit limitations.

## Recommended Edits

None required. Preserve the authority species rank, unclassified placement and zero BacDive count. Do not attach the unrelated assembly based on matching length, infer a genome from JF781122, or promote host association into disease causation.

Future authorized corrections belong in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. No supported defect requires such a change here; do not hand-edit generated YAML.

## Follow-up Checks

Any future host or pathogenicity enrichment needs isolate-specific primary experimental evidence and appropriately narrow claim placement. New genome/deposit links require an explicit source-supported identity chain.

After an authorized source refresh, rerun schema/strict/history validation and the documented full-corpus reproduction/QC gates. The focused checks do not replace those gates.

## Additional Notes

- YAML SHA-256: `00566be2acb31b41afd783750546d516342164ad718d7b816cc485042f5be127`.
- `data/taxa/PATHS.tsv:15269` and `curation/seed_scope.tsv:322948` uniquely resolve the target. The seed retains 2026-09-13T17:54:04Z and its matching one-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
