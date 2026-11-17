# YAML Record Review: Thalassobius sp. KU27E3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/thalassobius_sp_ku27e3.yaml`
- Started UTC: 2026-10-10T01:06:21Z
- Finished UTC: 2026-10-10T01:09:40Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. `NCBITaxon:1037363` denotes Thalassobius sp. KU27E3, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2619711` (unclassified Thalassovita), genetic code 11, grounding `EXACT`, status `SEEDED`.

It contains ten ancestors, zero inventoried BacDive strains, one NCBITAXON name attestation and one seed event. Its strain-like designation does not override the authority species rank.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/thalassobius_sp_ku27e3.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/thalassobius_sp_ku27e3.yaml --out /private/tmp/taxonmech-ku27e3-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured source comparisons verified identity, every ancestor, code, empty synonym columns, attestation, index/scope entries and seed reason. Complete backbone scanning found no direct child; exact own-ID type-material, merged-ID and dropped scans found none.
- Native name and candidate assembly rows, full live NCBI taxonomy responses, marker annotations and the complete linked PubMed abstract were inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, source replay, rendering and publication gates. Focused agreement is not corpus reproduction. No causal graph is asserted, so `just validate-products` has no applicable nodes.
- The complete experimental paper, strain-level assay tables, independent phylogeny and genome comparisons were not audited. Search results supplied leads only. The LPSN genus page was opened but its relevant text was not inspected and is not used as evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222729`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037363&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037363) agree on the exact name, ID, species rank, parent and code.

The full root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Rhodobacterales, Roseobacteraceae, Thalassovita and unclassified Thalassovita. All ancestor IDs, labels and ranks match the pinned backbone. EFetch confirms the chain below root; Datasets includes root 1.

The target name retains Thalassobius while its genus and unclassified parent use Thalassovita. This combination occurs in both the pinned authority inventory and live NCBI responses. It is an inherited source-level naming tension, not evidence that TaxonMech selected the wrong concept. Local rules retain NCBI lineage verbatim; neither a replacement target name nor assignment to a named species is justified here.

`data/catalog/ncbi_names-0005.jsonl.gz:32348` is the exact own scientific-name row. The pinned synonym columns are empty and live EFetch supplies no synonym. `EXACT` concerns the NCBI concept, not formal nomenclatural validity.

## Evidence

The sole attestation is NCBITAXON, exact own ID/label, count 1, unit `NAME`, snapshot 2026-09-13. It is not a phenotype, genome or culture count.

A live exact nucleotide query, `txid1037363[Organism:exp]`, returned one entry. Complete [AB636141 metadata](https://www.ncbi.nlm.nih.gov/nuccore/AB636141) identifies AB636141.1, a 1,426-base partial 16S rRNA sequence with partial feature endpoints, organism Thalassobius sp. KU27E3, strain KU27E3 and `taxon:1037363`. Its source qualifier gives Japan:Okinawa. Sequence length agrees with the annotation and its alphabet is A/C/G/T. This is a marker, not a genome or culture accession; the query is not a global sequence census.

The marker explicitly cites [Iwaki, Nishimura and Hasegawa, PMID 22805854](https://pubmed.ncbi.nlm.nih.gov/22805854/), DOI 10.1007/s11274-011-0925-x, World Journal of Microbiology and Biotechnology 28:1321-1325 (2012). The inspected abstract describes eleven Japanese seawater isolates, phthalate utilization and assay/PCR observations. It does not identify KU27E3 individually; the marker bibliography provides that connection.

These sources provide bounded identity and study context. They do not establish a complete genome, a species reassignment or a fully resolved strain-specific pathway. The YAML asserts no phthalate, growth, gene, habitat or causal claim requiring that stronger evidence.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 1037363, KU27E3 with optional space/hyphen/underscore separators, and the slug. All four matching lines were inspected: own backbone, name and scope rows, plus one unrelated assembly row.

The candidate `data/catalog/ncbi_genbank-0051.jsonl.gz:36896` contains 1037363 as genome length, not taxon ID. Its complete row denotes GCA_055987205.1, Pseudomonadota bacterium taxon 1977087, isolate JZ-2_201808_bins_187, BioSample SAMN40882281, project PRJNA544494. This numeric collision provides no target genome evidence.

A follow-up ignored/compressed-inclusive AB636141 search over the same roots returned no matches. Five SOURCE.json files were separately parsed without a target match. Gitignore-independent filename enumeration under the taxon corpus and review directory found only this YAML and no prior report. History filename inspection found no target-specific filename. These are bounded repository findings, not global absence claims.

Complete structured own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. No immediate backbone child supplies descendant inventory. Zero correctly means no inventoried BacDive strain, not that no isolate exists. No source-supported deposit/genome identity chain was established.

Optional definitions, nomenclature, mappings, record-level evidence and causal graphs need not be invented. iModulonDB was not applicable to this taxonomy-only YAML; contextual assay/PCR language is not a record gene or transcriptomics assertion. No adapter run or global dataset absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, lineage, rank, provenance and source-count semantics are supported. The inherited name/lineage tension, skipped corpus checks and uninspected experimental details remain explicit limitations.

## Recommended Edits

None required. Preserve the authority name and Thalassovita lineage together until an authoritative refresh changes them. Do not treat AB636141 as a genome or transfer an unrelated assembly based on a numeric match.

Any later authorized correction belongs in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. Generated YAML must not be hand-edited.

## Follow-up Checks

On a future authority refresh, recheck both target scientific name and full lineage without independently inferring a name change. Before phenotype or mechanism enrichment, inspect the complete paper and strain-specific assays. New deposit/genome links require an explicit source-supported identity chain and whole culture accessions.

After an authorized source refresh, rerun schema/strict/history validation and documented full-corpus reproduction/QC gates. Focused agreement does not replace those checks.

## Additional Notes

- YAML SHA-256: `b3a830d91251c251734b37ee0daa16e8d21317faf05cddfaad346dc97390fc15`.
- `data/taxa/PATHS.tsv:15277` and `curation/seed_scope.tsv:322954` uniquely resolve the target. The seed retains 2026-09-13T17:54:04Z and its exact one-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
