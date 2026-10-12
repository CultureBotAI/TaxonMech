# YAML Record Review: Wolbachia endosymbiont of Mesopolobus verditer

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_mesopolobus_verditer.yaml`
- Started UTC: 2026-10-09T15:25:08Z
- Finished UTC: 2026-10-09T15:27:35Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036784` was read. It denotes Wolbachia endosymbiont of Mesopolobus verditer, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), genetic code 11, grounding `EXACT` and status `SEEDED`. It has zero inventoried strains, one NCBITAXON name attestation and one seeding event.

An ignored-inclusive filename inventory resolved only this YAML and no prior own report. SHA-256: `b1e5c7c148444128a924b64c4d1cbc45685a78d2e6c3dd2b4b86391533e331e6`. The bacterial endosymbiont, not its eukaryotic host, is the single target.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` with the existing environment.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_mesopolobus_verditer.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_mesopolobus_verditer.yaml --workers 1 --out /private/tmp/taxonmech-wmes-20261009-validation.tsv`: passed, one file, zero errors. The inspected TSV has only its header.
- `uv run --offline python scripts/validate_history.py history`: passed, 17 valid records and zero invalid links.
- Own-row structured checks passed for the complete ancestor chain, identity fields, source attestation, PATHS/scope entries and generated event wording.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift were not rerun for this individual review. The documented `just verify-corpus` command has no record selector. These bounded checks do not certify corpus reproduction.
- Not applicable: OAK curator-added graph checks and iModulonDB gene/component checks. This YAML contains no causal graph, gene, regulator, pathway, trait or transcriptomics claim.
- Direct live NCBI taxonomy EFetch and Datasets responses were inspected successfully. The Taxonomy browser page was inaccessible through the web tool; that access failure is not evidence against the identity.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222624` supports every own identity field, the 2026-09-13 snapshot and NCBI-only attestation. `data/catalog/ncbi_names-0005.jsonl.gz:32218` contains the scientific name and no own synonym requiring representation.

Live [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036784&retmode=xml) confirms taxon 1036784, the exact label, species rank, parent 2640676 and genetic code 11. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036784) independently agrees.

The complete 11-entry chain matches the own backbone and live taxonomy: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676. The tribe and unranked group are retained correctly.

The source's `SPECIES` rank does not establish a formally published bacterial binomial or a type strain. The host name in the label does not identify the bacterial record as an animal or demonstrate equivalence to all Wolbachia associated with that host. No such over-scoped claim is present.

## Evidence

The source attestation is exactly one NCBI name, not one culture or genome. Its identifier, label, count, unit and snapshot date match the own inventory row. Zero inventoried strains is consistent with the absence of an own BacDive row, not an assertion that the bacterium lacks biological strains.

An exact non-expanded nucleotide query for `txid1036784[Organism:noexp]` returned one ID, 334360652. The complete [GenBank JF952019.1](https://www.ncbi.nlm.nih.gov/nuccore/JF952019.1) metadata, references and features were inspected. It is a 622-base partial COI coding sequence with the same organism and taxon ID, host Mesopolobus verditer, voucher `BIOUG<CAN>:ASSPP927-08.w` and additional sequence ID `uoguelph|ASNBW001-09.COI-5P`. The source records collection on 1986-07-22 at Acadia Research Forest, New Brunswick, Canada, and CDS translation table 11. Actual and declared lengths match; the sequence contains A/C/G/T only.

That record directly corroborates the source-specific host-associated organism label. It is specimen/marker evidence, not a culture accession, type designation, genome assembly or tested biological mechanism. Its first reference remains marked unpublished and its second is a direct submission; neither is used to invent a target-specific phenotype or curation status.

The live [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036784/dataset_report) returned an empty object. This supplies no positive assembly evidence through that query, not proof that no genome can exist elsewhere. The YAML correctly contains no inferred genome or strain relationship.

## Completeness

Gitignore-independent searches included hidden and compressed source files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches used the bounded taxon ID, current label and host name. All three matches were read: backbone, scope and native scientific name. All five source `SOURCE.json` files were parsed for target matches. A further ignored-inclusive content search for JF952019, ASSPP927 and ASNBW001 returned no local candidates in these roots.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. The broader source search supplied no eligible own culture/genome/sample/deposit evidence. These are bounded snapshot findings, not claims of universal absence.

Empty synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are therefore appropriate. The external COI discovery does not demonstrate a missing required culture-to-genome relationship.

`data/taxa/PATHS.tsv:15152` agrees with the filename. `curation/seed_scope.tsv:322857` records the 2026-09-13 one-source inclusion. The sole YAML event at 2026-09-13T17:54:04Z exactly matches the source/scope-generated text. Ignored-inclusive history filename and content searches found no target-specific external history entry. No human review status is implied.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete record and inspected evidence.

## Recommended Edits

None required. Do not turn the specimen voucher into a culture deposit or the partial marker into a genome. Preserve the source-taxonomy scope and generated status.

Future authorized changes belong in maintained source extraction/seeding inputs or scope, followed by regeneration, not hand edits to this generated YAML.

## Follow-up Checks

No defect-specific repair is required. Before any later authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates. Additional genome or phenotype claims would require their own explicit source evidence.

## Additional Notes

This independent report is the only repository write for the target. No record, source, scope/history entry, generated page, branch, worktree or GitHub item was changed. Eukaryota remains outside the active queue. No paid research was performed.

