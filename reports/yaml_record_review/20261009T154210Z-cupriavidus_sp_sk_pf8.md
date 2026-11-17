# YAML Record Review: Cupriavidus sp. SK PF8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/cupriavidus_sp_sk_pf8.yaml`
- Started UTC: 2026-10-09T15:40:20Z
- Finished UTC: 2026-10-09T15:42:10Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036799` was read. It denotes Cupriavidus sp. SK PF8, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640874` (unclassified Cupriavidus), genetic code 11, grounding `EXACT` and status `SEEDED`. It has zero inventoried strains, one NCBITAXON name attestation and one seeding event.

An ignored-inclusive filename inventory resolved only this YAML and no prior own report. SHA-256: `8a2c20b664f300cef1f9b8749308ef79c76f9fc72e4762427c12685181862020`. Unrelated source-search hits were inspected only to resolve identity, not reviewed as additional targets.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` with the existing environment.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/cupriavidus_sp_sk_pf8.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/cupriavidus_sp_sk_pf8.yaml --workers 1 --out /private/tmp/taxonmech-skpf8-20261009-validation.tsv`: passed, one file, zero errors; the inspected TSV has only its header.
- `uv run --offline python scripts/validate_history.py history`: passed earlier in this review turn, 17 valid records and zero invalid links; history was not changed.
- Structured own-row checks passed for the complete ancestor chain, identity, source attestation, PATHS/scope entries and generated event wording.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift were not rerun for this individual review. The documented `just verify-corpus` gate has no record selector. These focused checks do not certify corpus reproduction.
- Not applicable: OAK curator-added graph checks and iModulonDB gene/component checks. This YAML contains no causal graph, gene, regulator, pathway, trait or transcriptomics assertion.
- Direct NCBI EFetch and Datasets responses were inspected successfully. The Taxonomy browser page was inaccessible through the web tool; this access failure is not evidence against the identity.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222626` supports the identifier, exact label, rank, parent, genetic code, NCBI-only attestation and 2026-09-13 snapshot. `data/catalog/ncbi_names-0005.jsonl.gz:32220` contains the scientific name. The own inventory has no exact, related or broad synonyms requiring representation.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036799&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036799) confirm the exact label, species rank, parent and genetic code. All ten lineage entries match the local backbone and live authority: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Cupriavidus 106589; unclassified Cupriavidus 2640874. Labels and ranks agree.

The strain-like label does not override the source's species rank or establish a validly published binomial or type strain. The record correctly preserves an unresolved Cupriavidus species designation.

## Evidence

The source attestation is one NCBI name, not one culture, genome or experiment. Its identifier, label, count, unit and snapshot date match the own inventory. Zero inventoried strains concerns BacDive coverage, not the number of biological strains suggested by the label.

An exact non-expanded nucleotide query for `txid1036799[Organism:noexp]` returned one ID, 334546868. Complete [GenBank JF827022.1](https://www.ncbi.nlm.nih.gov/nuccore/JF827022.1) metadata, features and references identify a 408-base partial 16S rRNA sequence with the same organism and taxon ID, strain SK PF8 and isolate A. Collection is recorded in India on 2009-07-27 at 28.47 N, 77.03 E. Actual and declared lengths agree; the sequence contains A/C/G/T only.

Its sole reference is a direct submission dated 2011-04-15. The submitter's chimera-screening comment does not establish a biological phenotype. The marker independently corroborates the source-specific identity but supplies no registered culture deposit, type designation or genome assembly.

The live [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036799/dataset_report) returned an empty object. This is no positive assembly evidence through that query, not a claim that no genome could exist elsewhere.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches used the bounded numeric ID, current label/slug-compatible spelling and SK PF8 separator variants. All five candidate rows were read in full: own backbone, scope and native scientific name, plus two unrelated genome records. All five source `SOURCE.json` files were parsed and supplied no target match. A further ignored-inclusive search for JF827022 found no local match in these roots.

`data/bvbrc/bvbrc-0004.jsonl.gz:30200` and `data/catalog/ncbi_genbank-0034.jsonl.gz:58` match `PRJNA1036799`, a BioProject accession, not this NCBI taxon. Both concern Listeria monocytogenes AUF-2, taxon 1639, assembly GCA_036348275.1 and BioSample SAMN38150782; the BV-BRC genome ID is 1639.14045. Full row inspection excludes them as SK PF8 evidence. A shared numeric suffix across identifier namespaces is not an identity link.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. The broader source inspection supplied no eligible own culture, deposit, sample-to-genome or assembly chain. These are bounded snapshot findings, not universal absence claims.

Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty. The external marker does not demonstrate a missing required genome relationship.

`data/taxa/PATHS.tsv:15155` agrees with the filename. `curation/seed_scope.tsv:322859` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the source/scope-generated text. Ignored-inclusive history filename and content searches found no target-specific external history entry. No human review status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete record and inspected evidence.

## Recommended Edits

None required. Preserve the source-taxonomy designation. Do not promote the partial 16S sequence into a genome or join the unrelated BioProject using its numeric suffix.

Any later authorized correction belongs in maintained upstream extraction inputs, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, followed by regeneration, not a hand edit to this generated YAML.

## Follow-up Checks

No defect-specific repair is required. Before any later authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates. New strain/genome associations require a complete, namespace-aware source chain supporting this target.

## Additional Notes

This independent report is the only repository write for the target. No record, source, scope/history entry, generated page, branch, worktree or GitHub item was changed. Eukaryota remains outside the active review queue. No paid research was performed.

