# YAML Record Review: Sulfitobacter sp. KU27D4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sulfitobacter_sp_ku27d4.yaml`
- Started UTC: 2026-10-10T00:55:38Z
- Finished UTC: 2026-10-10T00:57:13Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. `NCBITaxon:1037361` denotes Sulfitobacter sp. KU27D4, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196795` (unclassified Sulfitobacter), genetic code 11, grounding `EXACT`, status `SEEDED`.

It carries ten ancestors, no synonym list, zero inventoried BacDive strains, one NCBITAXON name attestation and one seed event. The strain-like designation does not override NCBI's species rank.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/sulfitobacter_sp_ku27d4.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/sulfitobacter_sp_ku27d4.yaml --out /private/tmp/taxonmech-ku27d4-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured scans matched identity, full lineage, code, empty source synonyms, own attestation, index/scope entries and seed-event text. Complete backbone scanning found no direct child; exact own-ID type-material, merged-ID and dropped scans found none.
- The own native NCBI name row, complete live taxonomy responses and primary nucleotide metadata were inspected. The complete linked PubMed abstract and identifiers were read during this review run; its strain connection was independently verified in KU27D4's marker entry.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. Focused agreement is not corpus reproduction. No causal graph is asserted, so `just validate-products` has no applicable nodes.
- The complete experimental paper, strain-level assay tables, independent phylogeny and genome comparisons were not audited. Web-search taxonomy trees supplied leads, not substitutes for the exact authority responses.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222727` agrees with [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037361&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037361): Sulfitobacter sp. KU27D4, species rank, parent 196795 and code 11.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Rhodobacterales, Roseobacteraceae, Sulfitobacter and unclassified Sulfitobacter. Every stored ancestor ID, label and rank matches the pinned backbone. EFetch confirms the chain below root; Datasets includes root 1.

`data/catalog/ncbi_names-0005.jsonl.gz:32341` is the scientific-name row. The pinned exact/related/broad synonym columns are empty and live EFetch supplies no synonym. Exact grounding denotes this NCBI concept, not formal nomenclatural validity or equivalence to a named neighboring species.

## Evidence

The sole NCBITAXON attestation has exact own ID/label, count 1, unit `NAME`, snapshot 2026-09-13. It is not a count of genomes, culture deposits or experiments.

A live NCBI nucleotide query for `txid1037361[Organism:exp]` returned one entry. Complete [AB636138 metadata](https://www.ncbi.nlm.nih.gov/nuccore/AB636138) identifies AB636138.1, a 1,354-base partial 16S rRNA sequence with partial feature endpoints, explicitly organism Sulfitobacter sp. KU27D4, strain KU27D4 and `taxon:1037361`. Its source qualifier gives Japan:Nagasaki. The sequence includes ambiguous N bases. This is a marker, not a genome or culture-collection accession, and is not currently asserted as a YAML sequence link. The query is not a global sequence census.

The marker bibliography explicitly links [Iwaki, Nishimura and Hasegawa, PMID 22805854](https://pubmed.ncbi.nlm.nih.gov/22805854/), DOI 10.1007/s11274-011-0925-x, World Journal of Microbiology and Biotechnology 28:1321-1325 (2012). The inspected abstract describes eleven Japanese seawater isolates, phthalate utilization and assay/PCR observations. It does not name KU27D4 individually; the marker bibliography supplies the identity connection.

The YAML asserts taxonomy and provenance only. Study-level context and a partial marker do not establish a complete genome, a named-species reassignment, or a strain-specific enzymatic mechanism. No phthalate, growth, gene, habitat or causal claim was added or inferred as an existing YAML field.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 1037361, KU27D4 with optional space/hyphen/underscore separators, and the slug. Its three matching lines were the own backbone, native name and scope rows; all were inspected.

A follow-up ignored/compressed-inclusive AB636138 search over the same roots returned no matches. Five SOURCE.json files were separately parsed without a target match. Gitignore-independent filename enumeration under the taxon corpus and report directory found only the target YAML and no prior report. History filename inspection found no target-specific filename. These are bounded repository checks, not global absence claims.

Complete structured own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. No immediate backbone child supplies descendant inventory. Zero correctly counts inventoried BacDive strains, not whether an isolate was studied. No repository-supported deposit/genome identity chain was established.

Optional definition, nomenclature, mappings, record-level evidence and causal graphs need not be invented. iModulonDB was not applicable to the taxonomy-only YAML: contextual assay/PCR language in the abstract does not create a gene or transcriptomics assertion. No adapter run or global dataset absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, rank, lineage, provenance, source-count semantics and seeded status are supported. Skipped corpus checks and uninspected strain-level experimental detail remain limitations.

## Recommended Edits

None required. Preserve the authority species rank, unclassified placement and zero BacDive count. Do not treat AB636138 as a genome or infer a species reassignment or full pathway from the marker and study abstract.

Any future authorized correction belongs in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. No supported defect requires a change here; generated YAML must not be hand-edited.

## Follow-up Checks

Before phthalate-related enrichment, inspect the full paper and strain-specific assay evidence; keep computational/sequence support distinct from phenotype or causal mechanism. New genome/deposit links require an explicit source-supported identity chain and whole culture accessions.

After an authorized source refresh, rerun schema/strict/history validation and documented full-corpus reproduction/QC gates. Focused matching does not replace those checks.

## Additional Notes

- YAML SHA-256: `d4f2e23c4803102f604924522993902c0f30160a7c6d9a49ad0940660b076120`.
- `data/taxa/PATHS.tsv:15275` and `curation/seed_scope.tsv:322953` uniquely resolve the target. The seed retains 2026-09-13T17:54:04Z and the exact one-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
