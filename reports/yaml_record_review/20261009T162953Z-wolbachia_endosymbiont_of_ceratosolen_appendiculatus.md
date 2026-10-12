# YAML Record Review: Wolbachia endosymbiont of Ceratosolen appendiculatus

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_ceratosolen_appendiculatus.yaml`
- Started UTC: 2026-10-09T16:24:51Z
- Finished UTC: 2026-10-09T16:29:53Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036838` was read. It denotes Wolbachia endosymbiont of Ceratosolen appendiculatus, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), genetic code 11, grounding `EXACT` and status `SEEDED`. It contains zero inventoried strains, one NCBITAXON name attestation and one seeding event.

An ignored-inclusive filename inventory resolved this YAML and the separately identified appendiculatus-VAR sibling; no prior own report was found. The target SHA-256 is `4ac2ca5062af83b36e00fae1522f112804e74269d83c233b5645f7049929ebf4`. Sibling source rows and sequences were inspected only for disambiguation, not as a second review target.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` with the existing environment.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_ceratosolen_appendiculatus.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_ceratosolen_appendiculatus.yaml --workers 1 --out /private/tmp/taxonmech-ceratosolen-appendiculatus-20261009-validation.tsv`: passed, one file and zero errors; the inspected TSV contains only its header.
- `uv run --offline python scripts/validate_history.py history`: passed in this review turn, 17 valid records and zero invalid links.
- Structured comparisons passed for the own backbone row, all lineage entries, attestation fields, PATHS/scope entries and generated event wording.
- Live NCBI taxonomy, exact-taxon and name-based nucleotide searches, genome search and all nine broader-search GenBank candidates were inspected. Candidate metadata, source qualifiers, references, annotations and sequence-length/alphabet checks were read; no sequence-alignment or protein-function validation is claimed.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift were not rerun for this individual review. The documented `just verify-corpus` gate has no record selector. Focused source comparisons do not certify corpus reproduction.
- Not applicable: OAK curator-added graph checks and iModulonDB gene/component checks. The YAML asserts no causal graph, gene, regulator, pathway, trait or transcriptomics evidence. Markers assigned to another taxon do not add such claims to this record.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222632` and `data/catalog/ncbi_names-0005.jsonl.gz:32226` support the exact identifier, label and scientific-name status. The backbone supports species rank, parent, genetic code, NCBI-only attestation and 2026-09-13 snapshot. Its exact, related and broad synonym fields are empty.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036838&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036838) agree with the identity. All eleven carried lineage entries agree with the local backbone; the live EFetch lineage agrees on the ten named ancestors after root, and Datasets includes root ID 1 as well: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676.

The record denotes the bacterial endosymbiont, not its Ceratosolen host. Species rank in NCBI does not establish formal nomenclatural standing or a cultured type strain. The live record has creation date 2011-05-27, update date 2020-07-08 and publication date 2026-05-06; those dates alone do not establish retirement or merger.

The near match is explicitly distinct in the local backbone and name catalog: `NCBITaxon:1094252`, Wolbachia endosymbiont of Ceratosolen appendiculatus-VAR, in `data/taxa/bacteria/wolbachia_endosymbiont_of_ceratosolen_appendiculatus_var.yaml`. Its backbone row is 235298, catalog row 47527 and scope row 333611. Sharing a parent and name prefix does not make the records duplicates or synonyms.

## Evidence

The attestation counts one NCBI name, not cultures, specimens or nucleotide records. Its source ID, label, count, unit and snapshot date match the own inventory. `strain_count: 0` describes inventoried BacDive coverage, not biological absence.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036838%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned zero IDs with a phrase-not-found diagnostic. The [full organism-name query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=%22Wolbachia%20endosymbiont%20of%20Ceratosolen%20appendiculatus%22%5BOrganism%5D&retmode=json&retmax=100) also returned zero IDs, with an incorrect-translation/quoted-phrase warning. These are bounded query results, not proof that no sequence for this organism exists.

The [broader host-name plus Wolbachia search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=%22Ceratosolen%20appendiculatus%22%5BAll%20Fields%5D%20AND%20Wolbachia%5BAll%20Fields%5D&retmode=json&retmax=100) returned nine entries. Every candidate was fetched: JF902378.1, JF902379.1, JF902380.1, JF902381.1, JF902382.1, JF902383.1, JF902384.1, JF902385.1 and JF902386.1. All nine carry the organism name ending in appendiculatus-VAR and `taxon:1094252`, not the target ID. For example, [JF902378.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902378.1) and [JF902386.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902386.1) delimit this completely inspected accession set.

The candidates annotate partial COI gene/CDS sequences with genetic code 11, specimen vouchers and BOLD cross-references. They concern specimens collected in Diaoluoshan, Hainan, China on 19-Apr-2007. Their declared and actual lengths agree: eight are 642 bases and JF902386.1 is 637 bases. JF902385.1 and JF902386.1 include N ambiguity; the other seven have A/C/G/T-only alphabets. These details are sibling-specific source context, not target evidence or culture/assembly relationships.

The sibling entries cite an unpublished Smith study and a 01-May-2011 direct submission. No publication-level phenotype, supergroup assignment or specimen mapping is attributed to the target. BOLD cross-references were read in GenBank, not independently resolved. A publication or supplementary-table investigation was not needed to establish the observed taxon-ID mismatch and was not used to infer target traits.

The live [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036838/dataset_report) returned an empty object. It supplies no positive assembly evidence; it does not prove universal genome absence.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The query used bounded numeric ID 1036838 and label/slug-compatible spelling. All six candidate rows were read in full: two native name JSON rows and four backbone/scope TSV rows. They describe only the own and appendiculatus-VAR concepts. All five source `SOURCE.json` files were parsed and had no target match. Absence findings are limited to these inspected snapshots and search roots.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. No inspected source supplies an eligible own culture-to-genome chain. Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty. The nine sibling markers do not demonstrate a missing required relationship in this target.

`data/taxa/PATHS.tsv:15164` agrees with the filename. `curation/seed_scope.tsv:322865` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z agrees with the source/scope-generated wording. Ignored-inclusive history filename and content searches found no target-specific external history entry. No human-reviewed mapping status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete record and inspected evidence. Search warnings and sibling marker matches do not contradict the independently verified target taxonomy or demonstrate a required missing field.

## Recommended Edits

None required. Preserve the target's own identity. Do not merge it with appendiculatus-VAR or import that sibling's sequence, specimen, study or genome assertions merely because the label prefix matches.

Any later authorized correction belongs in maintained upstream extraction inputs, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, followed by regeneration, not a hand edit to this generated YAML.

## Follow-up Checks

No defect-specific repair is required. A later sequence-enrichment task should resolve exact target accession-to-taxonomy associations independently, because the current exact queries carry warnings. Any future culture/genome link needs an explicit eligible source chain. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for this target. Temporary validator output is outside the repository. No record, source, scope/history entry, generated page, branch, worktree or GitHub item was changed. The sibling was disambiguation context only; no host or Eukaryota record was reviewed. No paid research was performed.
