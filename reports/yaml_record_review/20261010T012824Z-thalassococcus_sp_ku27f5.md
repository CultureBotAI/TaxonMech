# YAML Record Review: Thalassococcus sp. KU27F5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/thalassococcus_sp_ku27f5.yaml`
- Started UTC: 2026-10-10T01:25:28Z
- Finished UTC: 2026-10-10T01:28:24Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. `NCBITaxon:1037368` denotes Thalassococcus sp. KU27F5, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2633072` (unclassified Thalassococcus), genetic code 11, grounding `EXACT`, status `SEEDED`.

It carries ten ancestors, no synonym list, zero inventoried BacDive strains, one NCBITAXON name attestation and one seed event. The isolate-style designation does not override NCBI's species rank.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/thalassococcus_sp_ku27f5.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/thalassococcus_sp_ku27f5.yaml --out /private/tmp/taxonmech-ku27f5-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links, run earlier this turn; history was not changed.
- Structured comparisons verified own identity, every ancestor, code, empty synonym columns, attestation, index/scope entries and seed reason. Complete backbone scanning found no direct child. Exact own-ID type-material, merged-ID and dropped scans found none.
- The complete native name row, live taxonomy responses and primary marker annotations were inspected. The linked PubMed abstract and identifiers were read this turn; the target's bibliography was independently verified in its own marker entry. A later paper's Table 2 header, target row, footnotes and surrounding results were inspected at the publisher.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. No causal graph is asserted, so `just validate-products` has no applicable nodes. Focused source agreement is not corpus reproduction.
- The complete phthalate paper, strain-level assays, independent phylogeny and genome comparisons were not audited. The later paper's underlying clone sequences and complete experimental dataset were not independently reanalyzed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222734`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037368&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037368) agree on the exact scientific name, species rank, parent and code.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Rhodobacterales, Roseobacteraceae, Thalassococcus and unclassified Thalassococcus. Every stored ancestor ID, label and rank matches the pinned backbone. EFetch confirms the chain below root; Datasets includes root 1.

`data/catalog/ncbi_names-0005.jsonl.gz:32353` is the exact own scientific-name row. Pinned synonym columns are empty and live EFetch supplies no synonym. Exact grounding concerns this NCBI concept, not formal nomenclatural validity or assignment to a named neighboring species.

## Evidence

The sole NCBITAXON attestation has exact own ID/label, count 1, unit `NAME`, snapshot 2026-09-13. It counts a name assertion, not genomes, deposits or phenotypes.

A live exact nucleotide query, `txid1037368[Organism:exp]`, returned one entry. Complete [AB636146 metadata](https://www.ncbi.nlm.nih.gov/nuccore/AB636146) identifies AB636146.1, a 1,421-base partial 16S rRNA sequence with partial feature endpoints, organism Thalassococcus sp. KU27F5, strain KU27F5 and `taxon:1037368`. Its source qualifier gives Japan:Fukui. Sequence length agrees with the annotation and its alphabet is A/C/G/T. This is a marker, not a genome or culture accession; the query is not a global sequence census.

The marker explicitly cites [Iwaki, Nishimura and Hasegawa, PMID 22805854](https://pubmed.ncbi.nlm.nih.gov/22805854/), DOI 10.1007/s11274-011-0925-x, World Journal of Microbiology and Biotechnology 28:1321-1325 (2012). The inspected abstract describes eleven Japanese seawater isolates, phthalate utilization and assay/PCR observations. It does not name KU27F5 individually; the marker bibliography supplies that connection. This study context does not establish a complete genome or a fully resolved strain-specific pathway.

The later [2020 environmental-stress and protist study, DOI 10.3389/fmars.2020.00659](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2020.00659/full), Table 2, separates OTU46's accession MH556716 from its closest match KU27F5/AB636146. It reports 100% coverage and 99% identity, with treatment OTC1 and ciliate code E. The footnotes identify E as Euplotes vannus and OTC1 as 1 mg/L oxytetracycline. This is not an assertion that OTU46 is KU27F5. No digestion-resistance, host association or antibiotic phenotype can be transferred to the target from that match. The paper's older Rhodobacteraceae label also does not override the current NCBI lineage.

The YAML asserts taxonomy and provenance only. No phthalate, growth, gene, habitat, host-association or causal claim was added or inferred as an existing field.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 1037368, KU27F5 with optional space/hyphen/underscore separators, and the slug. All three matching lines were inspected: own backbone, native name and scope rows.

A follow-up ignored/compressed-inclusive AB636146 search over the same roots returned no matches. Five SOURCE.json files were separately parsed without a target match. Gitignore-independent filename enumeration under the taxon corpus and report directory found only this YAML and no prior report. History filename inspection found no target-specific filename. These are bounded repository checks, not global absence claims.

Complete structured own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. No immediate backbone child supplies descendant inventory. Zero correctly counts inventoried BacDive strains, not whether an isolate was studied. No repository-supported deposit/genome chain was established.

Optional definitions, nomenclature, mappings, record-level evidence and causal graphs need not be invented. iModulonDB was not applicable to the taxonomy-only YAML; contextual assay/PCR language and reference-sequence use do not create record gene or transcriptomics assertions. No adapter run or global dataset absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, rank, lineage, provenance, source-count semantics and seeded status are supported. Skipped corpus checks and uninspected experimental detail remain limitations.

## Recommended Edits

None required. Preserve authority rank, unclassified placement, Roseobacteraceae lineage and zero BacDive count. Do not treat AB636146 as a genome or equate the later study's OTU46/MH556716 with this isolate.

Future authorized corrections belong in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. No supported defect requires a change here; generated YAML must not be hand-edited.

## Follow-up Checks

Before phenotype or mechanism enrichment, inspect complete primary studies and target-specific assays. A closest sequence match or detection under an antibiotic treatment is not a target-strain susceptibility result. New deposit/genome links require an explicit source-supported identity chain and whole culture accessions.

After an authorized source refresh, rerun schema/strict/history validation and documented full-corpus reproduction/QC gates. Focused matching does not replace those checks.

## Additional Notes

- YAML SHA-256: `7571130c1795103e69e04871f18409b0ee3e2e78c3755fd24fa387ee2aff9171`.
- `data/taxa/PATHS.tsv:15282` and `curation/seed_scope.tsv:322959` uniquely resolve the target. The seed retains 2026-09-13T17:54:04Z and the exact one-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
