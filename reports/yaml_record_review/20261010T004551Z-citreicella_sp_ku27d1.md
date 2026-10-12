# YAML Record Review: Citreicella sp. KU27D1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/citreicella_sp_ku27d1.yaml`
- Started UTC: 2026-10-10T00:44:06Z
- Finished UTC: 2026-10-10T00:45:51Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. `NCBITaxon:1037359` denotes Citreicella sp. KU27D1, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2649625` (unclassified Citreicella), genetic code 11, grounding `EXACT`, status `SEEDED`.

It carries ten ancestors, no synonym list, zero inventoried BacDive strains, one NCBITAXON name attestation and one seed event. Its strain-like designation does not override NCBI's species rank.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/citreicella_sp_ku27d1.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/citreicella_sp_ku27d1.yaml --out /private/tmp/taxonmech-ku27d1-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured scans matched identity, full lineage, code, empty source synonyms, own attestation, index/scope entries and seed-event text. Complete backbone scanning found no direct child; exact own-ID type-material, merged-ID and dropped scans found none.
- Every native candidate row was read completely. Live taxonomy responses, primary nucleotide metadata and the complete linked PubMed abstract/identifiers were inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. Focused agreement is not corpus reproduction. No causal graph is asserted, so `just validate-products` has no applicable nodes.
- The complete experimental paper, strain-specific assay tables, independent phylogeny and genome comparisons were not audited. Taxonomy search pages supplied leads, not substitutes for exact authority responses.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222725` agrees with [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037359&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037359): Citreicella sp. KU27D1, species rank, parent 2649625 and code 11.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Rhodobacterales, Roseobacteraceae, Citreicella and unclassified Citreicella. Every stored ID, label and rank matches the pinned backbone. EFetch confirms the chain below root; Datasets includes root 1.

`data/catalog/ncbi_names-0005.jsonl.gz:32339` is the scientific-name row. The pinned exact/related/broad synonym columns are empty and live EFetch supplies no synonym. Exact grounding identifies this NCBI concept, not formal nomenclatural validity or equivalence to a named neighboring species.

## Evidence

The sole NCBITAXON attestation has exact own ID/label, count 1, unit `NAME`, snapshot 2026-09-13. It is not a count of genomes or cultured deposits.

A live NCBI nucleotide query for `txid1037359[Organism:exp]` returned one entry. Complete [AB636136 metadata](https://www.ncbi.nlm.nih.gov/nuccore/AB636136) identifies AB636136.1, a 1,422-base partial 16S rRNA sequence with partial feature endpoints, explicitly organism Citreicella sp. KU27D1, strain KU27D1 and `taxon:1037359`. The source qualifier gives Japan:Nagasaki. It is a marker, not a genome or culture-collection accession, and is not currently asserted as a YAML link. The query is not a global sequence census.

The sequence display definition spells the genus Citricella, while its structured organism/source fields and NCBI taxonomy use Citreicella. Preserve this discrepancy as an external display-title issue; it does not justify renaming the taxon or adding an unsupported exact synonym.

The marker bibliography explicitly links [Iwaki, Nishimura and Hasegawa, PMID 22805854](https://pubmed.ncbi.nlm.nih.gov/22805854/), DOI 10.1007/s11274-011-0925-x, World Journal of Microbiology and Biotechnology 28:1321-1325 (2012). The inspected abstract describes eleven Japanese seawater isolates, their phthalate utilization and supporting assay/PCR observations. It does not name KU27D1 individually; the sequence bibliography supplies the identity link. The abstract is supplementary study context, not a substitute for full strain-level experimental evidence.

The YAML asserts taxonomy and provenance only. No phthalate pathway, gene, enzymatic mechanism, growth or environmental claim was added or inferred as an existing record field.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 1037359, KU27D1 with optional space/hyphen/underscore separators, and the slug. Five matching lines were the own backbone/name/scope rows and two unrelated assembly rows; all were inspected.

The GTDB and GenBank rows for `GCA_018671295.1` describe Candidatus Woesearchaeota archaeon SI037_bin49, NCBI taxon 2026803, not this bacterial isolate. Their total and ungapped genome lengths are 1037359. Numerical length identity cannot supply a taxon or genome link, and the unrelated source's taxonomy/publication was not transferred.

A follow-up ignored/compressed-inclusive AB636136 search over the same roots returned no matches. Five SOURCE.json files were separately parsed without a target match. Gitignore-independent filename enumeration under the taxon corpus and report directory found only the target YAML and no prior report; history filename inspection found no target-specific filename. These are bounded repository checks, not global absence claims.

Complete structured own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. No immediate backbone child supplies descendant inventory. Zero correctly counts inventoried BacDive strains, not whether an isolate was studied. No repository-supported deposit/genome identity chain was established.

Optional definition, nomenclature, mappings, record-level evidence and causal graphs need not be invented. iModulonDB was not applicable to the taxonomy-only YAML: contextual pathway/PCR language in the abstract does not create a gene or transcriptomics assertion. No adapter run or global dataset absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, rank, lineage, provenance, source-count semantics and seeded status are supported. The external sequence-title spelling discrepancy is not present in the YAML. Skipped corpus checks and uninspected strain-level experimental detail remain limitations.

## Recommended Edits

None required. Preserve Citreicella, the authority species rank, unclassified placement and zero BacDive count. Do not import the archaeal assembly based on its length, treat AB636136 as a genome, or convert the sequence-title typo into a taxonomic synonym.

Any future authorized correction belongs in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. No supported defect requires a change here; generated YAML must not be hand-edited.

## Follow-up Checks

Before phthalate-related enrichment, inspect the full paper and strain-specific assay evidence; keep computational/sequence support distinct from phenotype and causal mechanism. New genome/deposit links require an explicit source-supported identity chain.

After an authorized source refresh, rerun schema/strict/history validation and documented full-corpus reproduction/QC gates. Focused matching does not replace those checks.

## Additional Notes

- YAML SHA-256: `9ec6f9b6431b64f652b65d8d6dfaf280963e5521a8e8c4bea6a35e9a4b56d806`.
- `data/taxa/PATHS.tsv:15272` and `curation/seed_scope.tsv:322951` uniquely resolve the target. The seed retains 2026-09-13T17:54:04Z and the exact one-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
