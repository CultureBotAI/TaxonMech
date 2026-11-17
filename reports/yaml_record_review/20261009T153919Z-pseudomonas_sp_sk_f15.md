# YAML Record Review: Pseudomonas sp. SK F15

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_sk_f15.yaml`
- Started UTC: 2026-10-09T15:37:11Z
- Finished UTC: 2026-10-09T15:39:19Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036798` was read. It denotes Pseudomonas sp. SK F15, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821` (unclassified Pseudomonas), genetic code 11, grounding `EXACT` and status `SEEDED`. It contains zero inventoried strains, one NCBITAXON name attestation and one seeding event.

An ignored-inclusive filename inventory resolved only this YAML and no prior own report. SHA-256: `ae345b67aa5cb6eab9e70395689a401feec4e71d1f961b724b2fc2e592c6be3b`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` with the existing environment.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_sk_f15.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_sk_f15.yaml --workers 1 --out /private/tmp/taxonmech-skf15-20261009-validation.tsv`: passed, one file, zero errors; the inspected TSV has only its header.
- `uv run --offline python scripts/validate_history.py history`: passed, 17 valid records and zero invalid links.
- Structured own-row checks passed for identity, all ancestors, the source attestation, PATHS/scope entries and generated event wording.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift were not rerun for this individual review. The documented `just verify-corpus` gate has no record selector. Focused comparisons do not certify corpus reproduction.
- Not applicable: OAK curator-added graph checks and iModulonDB gene/component checks. The YAML contains no causal graph, gene, regulator, pathway, trait or transcriptomics assertion.
- Live NCBI EFetch and Datasets records were inspected successfully. The Taxonomy browser page was inaccessible through the web tool; this access failure was not treated as biological evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222625` supports the identifier, exact label, rank, parent, genetic code, NCBI-only attestation and 2026-09-13 snapshot. `data/catalog/ncbi_names-0005.jsonl.gz:32219` contains the scientific name. The own inventory has no exact, related or broad synonyms requiring representation.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036798&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036798) confirm the same label, species rank, parent and genetic code. The complete ten-entry chain matches the local backbone and live authority: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Gammaproteobacteria 1236; Pseudomonadales 72274; Pseudomonadaceae 135621; Pseudomonas 286; unclassified Pseudomonas 196821. Labels and ranks agree.

The strain-like suffix does not change NCBI's `SPECIES` rank or establish a formally named species or type strain. The record preserves the authority's unresolved species designation without assigning it to a nearby named species.

## Evidence

The sole source attestation counts one NCBI name. Its source ID, label, count, unit and snapshot date agree with the own inventory. `strain_count: 0` counts BacDive records under this taxon, not the number of biological strains implied by its label.

An exact non-expanded nucleotide query for `txid1036798[Organism:noexp]` returned one ID, 334546867. Complete [GenBank JF827021.1](https://www.ncbi.nlm.nih.gov/nuccore/JF827021.1) metadata, features and references identify a 403-base partial 16S rRNA sequence with the same organism and taxon ID, strain SK F15 and isolate F. The source records collection in India on 2009-07-27 at 28.47 N, 77.03 E. Declared and actual sequence lengths agree; the sequence contains A/C/G/T only.

The sequence's sole reference is a direct submission dated 2011-04-15. Its submitter-reported chimera screening is not independent evidence of a phenotype or a genome. This marker corroborates the source-specific identity but does not establish a registered culture deposit, type designation, assembly or strain-to-genome relationship.

The live [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036798/dataset_report) returned an empty object. That query supplies no positive assembly evidence; it is not proof of universal genome absence.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches used the bounded numeric ID, current label/slug-compatible spelling and SK F15 separator variants. All three matches were read: backbone, scope and native scientific name. All five source `SOURCE.json` files were parsed and supplied no target match. A further ignored-inclusive search for JF827021 found no local match in these roots.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. The broader search supplied no eligible own culture, deposit, sample-to-genome or assembly evidence. These are bounded snapshot findings, not claims that such evidence cannot exist elsewhere.

Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty. The external marker does not establish a missing required genome relationship.

`data/taxa/PATHS.tsv:15154` agrees with the filename. `curation/seed_scope.tsv:322858` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z exactly matches the source/scope-generated wording. Ignored-inclusive history filename and content searches found no target-specific external history entry. No human review status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete record and inspected evidence.

## Recommended Edits

None required. Preserve the unresolved source-taxonomy designation. Do not treat the bare strain name as a registered deposit or the partial 16S sequence as a genome.

Any later authorized correction belongs in maintained upstream extraction inputs, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, followed by regeneration, not a hand edit to this generated YAML.

## Follow-up Checks

No defect-specific repair is required. Before any later authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates. New culture, assembly or phenotype links require their own explicit target-specific evidence.

## Additional Notes

This independent report is the only repository write for the target. No record, source, scope/history entry, generated page, branch, worktree or GitHub item was changed. Eukaryota remains outside the active review queue. No paid research was performed.

