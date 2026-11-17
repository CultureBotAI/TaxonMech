# YAML Record Review: Alteromonas sp. KU27F1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alteromonas_sp_ku27f1.yaml`
- Started UTC: 2026-10-10T01:18:17Z
- Finished UTC: 2026-10-10T01:21:16Z
- Verdict: pass

## Target

The complete 57-line generated `TaxonRecord` was read. `NCBITaxon:1037366` denotes Alteromonas sp. KU27F1, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2614992` (unclassified Alteromonas), genetic code 11, grounding `EXACT`, status `SEEDED`.

It carries eleven ancestors, no synonym list, zero inventoried BacDive strains, one NCBITAXON name attestation and one seed event. The isolate-style designation does not override NCBI's species rank.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alteromonas_sp_ku27f1.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/alteromonas_sp_ku27f1.yaml --out /private/tmp/taxonmech-ku27f1-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured source comparisons verified own identity, every ancestor, code, empty synonym columns, attestation, index/scope entries and seed reason. Complete backbone scanning found no direct child. Exact own-ID type-material, merged-ID and dropped scans found none.
- The native name row, complete live taxonomy responses, marker annotations and complete linked PubMed abstract were inspected. A later primary paper's phylogenetic methods, accession section and Table 2 were inspected at the publisher; PMC returned a browser check.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. No causal graph is asserted, so `just validate-products` has no applicable nodes. Focused source agreement is not corpus reproduction.
- The complete phthalate paper, strain-level assays, independent phylogeny and genome comparisons were not audited. Additional search hits, including a 2020 journal PDF and a thesis, were not inspected and are not used as evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222732`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037366&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037366) agree on the exact scientific name, species rank, parent and code.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Alteromonadales, Alteromonadaceae, Alteromonas/Salinimonas group, Alteromonas and unclassified Alteromonas. Every stored ancestor ID, label and rank matches the pinned backbone. EFetch confirms the chain below root; Datasets includes root 1. The group at `NCBITaxon:2903219` is explicitly unranked, not a second genus or an inferred alternative placement.

`data/catalog/ncbi_names-0005.jsonl.gz:32351` is the exact own scientific-name row. Pinned synonym columns are empty and live EFetch supplies no synonym. Exact grounding concerns this NCBI concept, not formal nomenclatural validity or assignment to a named neighboring species.

## Evidence

The sole NCBITAXON attestation has exact own ID/label, count 1, unit `NAME`, snapshot 2026-09-13. It counts a name assertion, not genomes, deposits or phenotypes.

A live exact nucleotide query, `txid1037366[Organism:exp]`, returned one entry. Complete [AB636144 metadata](https://www.ncbi.nlm.nih.gov/nuccore/AB636144) identifies AB636144.1, a 1,493-base partial 16S rRNA sequence with partial feature endpoints, organism Alteromonas sp. KU27F1, strain KU27F1 and `taxon:1037366`. Its source qualifier gives Japan:Fukui. Sequence length agrees with the annotation; ambiguous Y bases are present. This marker is not a genome or culture accession, and the query is not a global sequence census.

The marker explicitly cites [Iwaki, Nishimura and Hasegawa, PMID 22805854](https://pubmed.ncbi.nlm.nih.gov/22805854/), DOI 10.1007/s11274-011-0925-x, World Journal of Microbiology and Biotechnology 28:1321-1325 (2012). The inspected abstract describes eleven Japanese seawater isolates, phthalate utilization and assay/PCR observations. It does not name KU27F1 individually; the marker bibliography supplies that connection. This study context does not establish a complete genome or a fully resolved strain-specific pathway.

The later [2016 protist-bacteria study, DOI 10.3389/fmicb.2016.00498](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2016.00498/full), distinguishes newly obtained sequences from database references. Table 2 lists KU27F1/AB636144 as the closest match for OTU3 from Diophrys scutum, with 99% coverage and 98% identity. It does not identify OTU3 as the same isolate. Neither digestion resistance nor host association can be transferred to KU27F1 from that match.

The YAML asserts taxonomy and provenance only. No phthalate, growth, gene, habitat, host-association or causal claim was added or inferred as an existing field.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 1037366, KU27F1 with optional space/hyphen/underscore separators, and the slug. All three matching lines were inspected: own backbone, native name and scope rows.

A follow-up ignored/compressed-inclusive AB636144 search over the same roots returned no matches. Five SOURCE.json files were separately parsed without a target match. Gitignore-independent filename enumeration under the taxon corpus and report directory found only this YAML and no prior report. History filename inspection found no target-specific filename. These are bounded repository checks, not global absence claims.

Complete structured own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. No immediate backbone child supplies descendant inventory. Zero correctly counts inventoried BacDive strains, not whether an isolate was studied. No repository-supported deposit/genome chain was established.

Optional definitions, nomenclature, mappings, record-level evidence and causal graphs need not be invented. iModulonDB was not applicable to the taxonomy-only YAML; contextual assay/PCR language and reference-sequence use do not create record gene or transcriptomics assertions. No adapter run or global dataset absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, rank, lineage, provenance, source-count semantics and seeded status are supported. Skipped corpus checks and uninspected experimental detail remain limitations.

## Recommended Edits

None required. Preserve the authority rank, unclassified placement, unranked Alteromonas/Salinimonas group and zero BacDive count. Do not treat AB636144 as a genome or equate the later study's OTU3 with this isolate.

Future authorized corrections belong in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. No supported defect requires a change here; generated YAML must not be hand-edited.

## Follow-up Checks

Before phenotype or mechanism enrichment, inspect the complete primary study and target-specific assays. A closest sequence match is not experimental-strain equivalence. New deposit/genome links require an explicit source-supported identity chain and whole culture accessions.

After an authorized source refresh, rerun schema/strict/history validation and documented full-corpus reproduction/QC gates. Focused matching does not replace those checks.

## Additional Notes

- YAML SHA-256: `642a07c7fad733e21793e809f83494b05abc94863c84dfefd5db8db7128e104f`.
- `data/taxa/PATHS.tsv:15280` and `curation/seed_scope.tsv:322957` uniquely resolve the target. The seed retains 2026-09-13T17:54:04Z and the exact one-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
