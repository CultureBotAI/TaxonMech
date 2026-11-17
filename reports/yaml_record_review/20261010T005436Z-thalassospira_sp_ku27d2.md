# YAML Record Review: Thalassospira sp. KU27D2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/thalassospira_sp_ku27d2.yaml`
- Started UTC: 2026-10-10T00:52:28Z
- Finished UTC: 2026-10-10T00:54:36Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. `NCBITaxon:1037360` denotes Thalassospira sp. KU27D2, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2648997` (unclassified Thalassospira), genetic code 11, grounding `EXACT`, status `SEEDED`.

It carries ten ancestors, no synonym list, zero inventoried BacDive strains, one NCBITAXON name attestation and one seed event. The strain-like designation does not override NCBI's species rank.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/thalassospira_sp_ku27d2.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/thalassospira_sp_ku27d2.yaml --out /private/tmp/taxonmech-ku27d2-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured scans matched identity, full lineage, code, empty source synonyms, own attestation, index/scope entries and seed-event text. Complete backbone scanning found no direct child; exact own-ID type-material, merged-ID and dropped scans found none.
- The own native NCBI name row, complete live taxonomy responses, primary nucleotide metadata and complete linked PubMed abstract/identifiers were inspected. A separate primary paper's identification text and nearest-match table were checked to resolve an apparent strain hit.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. Focused agreement is not corpus reproduction. No causal graph is asserted, so `just validate-products` has no applicable nodes.
- The complete phthalate paper and its strain-level assay tables, all experimental results of the separate co-culture paper, independent phylogeny and genome comparisons were not audited.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222726` agrees with [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037360&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037360): Thalassospira sp. KU27D2, species rank, parent 2648997 and code 11.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Rhodospirillales, Thalassospiraceae, Thalassospira and unclassified Thalassospira. Every stored ancestor ID, label and rank matches the pinned backbone. EFetch confirms the chain below root; Datasets includes root 1.

`data/catalog/ncbi_names-0005.jsonl.gz:32340` is the scientific-name row. The pinned exact/related/broad synonym columns are empty and live EFetch supplies no synonym. Exact grounding denotes this NCBI concept, not formal nomenclatural validity or equivalence to a named neighboring species.

## Evidence

The sole NCBITAXON attestation has exact own ID/label, count 1, unit `NAME`, snapshot 2026-09-13. It is not a count of genomes, culture deposits or experiments.

A live NCBI nucleotide query for `txid1037360[Organism:exp]` returned one entry. Complete [AB636137 metadata](https://www.ncbi.nlm.nih.gov/nuccore/AB636137) identifies AB636137.1, a 1,378-base partial 16S rRNA sequence with partial feature endpoints, explicitly organism Thalassospira sp. KU27D2, strain KU27D2 and `taxon:1037360`. It is a marker, not a genome or culture-collection accession, and is not currently asserted as a YAML sequence link. The query is not a global sequence census.

The marker bibliography explicitly links [Iwaki, Nishimura and Hasegawa, PMID 22805854](https://pubmed.ncbi.nlm.nih.gov/22805854/), DOI 10.1007/s11274-011-0925-x, World Journal of Microbiology and Biotechnology 28:1321-1325 (2012). The inspected abstract describes eleven Japanese seawater isolates, phthalate utilization and assay/PCR observations. It does not name KU27D2 individually; the marker bibliography supplies the identity connection. Full strain-specific experiments were not inspected, and no pathway or phenotype was added to the taxonomy-only YAML.

The separate [2018 co-culture paper, section 2.1 and Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC6071102/#sec2dot1-toxins-10-00257), identifies experimental isolates by nearest 16S BLAST matches. Its fourth row names KU27D2 with 99% identity. This is sequence-comparison context, not proof that the tested isolate was KU27D2. Consequently, its AHL-production, algal-growth or toxin-related results were not attributed to the target. Neither numerical similarity nor the displayed reference name supplies strain identity.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 1037360, KU27D2 with optional space/hyphen/underscore separators, and the slug. Its three matching lines were the own backbone, native name and scope rows; all were inspected.

A follow-up ignored/compressed-inclusive AB636137 search over the same roots returned no matches. Five SOURCE.json files were separately parsed without a target match. Gitignore-independent filename enumeration under the taxon corpus and report directory found only the target YAML and no prior report. History filename inspection found no target-specific filename. These are bounded repository checks, not global absence claims.

Complete structured own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. No immediate backbone child supplies descendant inventory. Zero correctly counts inventoried BacDive strains, not whether an isolate was studied. No repository-supported deposit/genome identity chain was established.

Optional definition, nomenclature, mappings, record-level evidence and causal graphs need not be invented. iModulonDB was not applicable to this taxonomy-only YAML: contextual pathway/PCR and quorum-sensing language does not create a record gene or transcriptomics assertion. No adapter run or global dataset absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, rank, lineage, provenance, source-count semantics and seeded status are supported. The nearest-match paper presents a potential evidence-transfer trap, not an existing YAML defect. Skipped corpus checks and uninspected strain-level experimental detail remain limitations.

## Recommended Edits

None required. Preserve the authority species rank, unclassified placement and zero BacDive count. Do not treat AB636137 as a genome or equate the later paper's 99%-matching experimental isolate with KU27D2.

Any future authorized correction belongs in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. No supported defect requires a change here; generated YAML must not be hand-edited.

## Follow-up Checks

Before phthalate-related enrichment, inspect the full linked paper and strain-specific assay evidence; keep computational/sequence support distinct from phenotype or causal mechanism. New genome/deposit links require an explicit source-supported identity chain.

After an authorized source refresh, rerun schema/strict/history validation and documented full-corpus reproduction/QC gates. Focused matching does not replace those checks.

## Additional Notes

- YAML SHA-256: `2dfddeecc24e5ad62d8d101dedf51351c21b84882cf2d161be843814c836fea8`.
- `data/taxa/PATHS.tsv:15274` and `curation/seed_scope.tsv:322952` uniquely resolve the target. The seed retains 2026-09-13T17:54:04Z and the exact one-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
