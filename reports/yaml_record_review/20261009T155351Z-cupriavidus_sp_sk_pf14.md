# YAML Record Review: Cupriavidus sp. SK PF14

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/cupriavidus_sp_sk_pf14.yaml`
- Started UTC: 2026-10-09T15:51:45Z
- Finished UTC: 2026-10-09T15:53:51Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036801` was read. It denotes Cupriavidus sp. SK PF14, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640874` (unclassified Cupriavidus), genetic code 11, grounding `EXACT` and status `SEEDED`. It contains zero inventoried strains, one NCBITAXON name attestation and one seeding event.

An ignored-inclusive filename inventory resolved only this YAML and no prior own report. SHA-256: `0937826a5ea9dc266b6512dea1946318d5634e90c8c739ecbc491c92fbb85d4b`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` with the existing environment.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/cupriavidus_sp_sk_pf14.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/cupriavidus_sp_sk_pf14.yaml --workers 1 --out /private/tmp/taxonmech-skpf14-20261009-validation.tsv`: passed, one file, zero errors; the inspected TSV has only its header.
- `uv run --offline python scripts/validate_history.py history`: passed, 17 valid records and zero invalid links.
- Structured own-row checks passed for identity, the full ancestor chain, attestation, PATHS/scope entries and generated event wording.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift were not rerun for this individual review. The documented `just verify-corpus` gate has no record selector. Focused comparisons do not certify corpus reproduction.
- Not applicable: OAK curator-added graph checks and iModulonDB gene/component checks. The YAML contains no causal graph, gene, regulator, pathway, trait or transcriptomics assertion.
- Live NCBI EFetch and Datasets responses were inspected successfully. The Taxonomy browser page was inaccessible through the web tool; that access failure was not treated as biological evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222628` supports the exact identifier, label, rank, parent, genetic code, NCBI-only attestation and 2026-09-13 snapshot. `data/catalog/ncbi_names-0005.jsonl.gz:32222` supplies the scientific name. The own inventory has no exact, related or broad synonyms requiring representation.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036801&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036801) confirm the identity, species rank, parent and genetic code. All ten lineage entries match the local backbone and live authority: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Cupriavidus 106589; unclassified Cupriavidus 2640874. Labels and ranks agree.

The strain-like suffix does not override the authority's species rank or establish a formally published species or type strain. `EXACT` concerns grounding to this source concept, not an independent species-delimitation result. The unresolved designation is faithfully retained.

## Evidence

The sole attestation counts one NCBI name, not a culture or genome. Its identifier, label, count, unit and snapshot date match the own inventory. `strain_count: 0` concerns BacDive coverage, not whether the source organism has a strain designation.

An exact non-expanded nucleotide query for `txid1036801[Organism:noexp]` returned one ID, 334546870. Complete [GenBank JF827024.1](https://www.ncbi.nlm.nih.gov/nuccore/JF827024.1) metadata, features and references identify a 224-base partial 16S rRNA sequence with the same organism and taxon ID, strain SK PF14 and isolate C. Collection is recorded in India on 2009-07-27 at 28.47 N, 77.03 E. Actual and declared lengths agree. The sequence alphabet includes N; the transcription qualifier contains four N bases.

This short, partly ambiguous marker corroborates the source-record association, not a definitive species-level identification. Its sole reference is a direct submission dated 2011-04-15, and its submitter-reported chimera screening does not establish an independent phenotype or complete genome. No culture deposit, type designation or assembly relationship is supplied by this record.

The live [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036801/dataset_report) returned an empty object. This supplies no positive assembly evidence through that query, not proof of universal genome absence.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches used the bounded numeric ID, current label/slug-compatible spelling and SK PF14 separator variants. All five candidate rows were read in full: own backbone, scope and native scientific name, plus two unrelated assemblies. All five source `SOURCE.json` files were parsed and supplied no target match. A further ignored-inclusive search for JF827024 found no local match in these roots.

`data/catalog/ncbi_genbank-0066.jsonl.gz:36255` is GCA_982779475.1, Flavobacteriales bacterium, taxon 2021391, with an ungapped genome length of 1036801. `data/catalog/ncbi_genbank-0061.jsonl.gz:7111` is GCA_949072075.1, Lactobacillus johnsonii MGBC106074, taxon 33959, with total genome length 1036801. Neither row identifies SK PF14; a matching sequence-length value cannot supply a taxon or strain link.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. The broader inspection supplied no eligible own culture, deposit, sample-to-genome or assembly chain. These are bounded snapshot findings, not universal absence claims.

Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty. The external partial marker does not demonstrate a missing required genome relationship.

`data/taxa/PATHS.tsv:15158` agrees with the filename. `curation/seed_scope.tsv:322861` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the source/scope-generated wording. Ignored-inclusive history filename and content searches found no target-specific external history entry. No human review status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete record and inspected evidence. The limited external marker does not invalidate the accurately represented NCBI source concept.

## Recommended Edits

None required. Preserve the unresolved source-taxonomy designation and do not infer a named species, culture deposit or genome from the partial marker or bare strain name.

Any later authorized correction belongs in maintained upstream extraction inputs, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, followed by regeneration, not a hand edit to this generated YAML.

## Follow-up Checks

No defect-specific repair is required. A future biological reassignment would need stronger target-specific evidence than this short marker. Before any later authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No record, source, scope/history entry, generated page, branch, worktree or GitHub item was changed. Eukaryota remains outside the active review queue. No paid research was performed.

