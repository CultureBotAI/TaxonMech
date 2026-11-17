# YAML Record Review: Wolbachia endosymbiont of Wiebesia flava

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_wiebesia_flava.yaml`
- Started UTC: 2026-10-09T17:07:59Z
- Finished UTC: 2026-10-09T17:09:41Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036846` was read. It denotes Wolbachia endosymbiont of Wiebesia flava, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), code 11, grounding `EXACT`, status `SEEDED`. It has no synonyms, zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this record and the separate flava-SAG concept, but no prior own report. Target SHA-256: `026f5ae34e5f158f544361a09107a371ba3e1161d82c33b34de39999e94f4cd4`. The SAG concept was disambiguation context only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_wiebesia_flava.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_wiebesia_flava.yaml --workers 1 --out /private/tmp/taxonmech-wiebesia-flava-20261009-validation.tsv`: passed, one file and zero errors; the inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed earlier this turn, 17 valid records and zero invalid links; history was unchanged.
- Own-row comparisons passed for identity, all ancestors, source attestation, PATHS/scope entries and generated event wording. All six local source candidates were read in full.
- Live NCBI taxonomy, nucleotide and genome responses were inspected. Complete metadata, source qualifiers, annotations and references for the single broader nucleotide candidate were read, with nucleotide length/alphabet checks. No sequence alignment or protein-function validation is claimed.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift. `just verify-corpus` has no record selector; focused comparisons do not certify corpus reproduction.
- Not applicable: curator-added OAK graph or iModulonDB checks; the record asserts no graph, gene, regulator, pathway, trait or transcriptomic result.
- Not checked: independent BOLD resolution or external publication/supplementary specimen mapping. The YAML cites no experimental paper, and the inspected marker belongs to another taxon ID.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222640` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:32235` agree with the exact identifier, label, species rank, parent, code and 2026-09-13 snapshot. The inspected own rows supply no synonyms or retirement.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036846&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036846) support the identity. All eleven root-first lineage entries match the local backbone. EFetch supplies the ten named ancestors after root; Datasets also supplies root 1: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676. Ancestor ranks agree with the YAML.

The record denotes a bacterial taxon, not the Wiebesia host species or all its endosymbionts. Wolbachia endosymbiont of Wiebesia flava-SAG is a separate species concept, `NCBITaxon:1094266`, in backbone row 235312, native name row 47541 of the same name shard, and scope row 333625. It shares the parent but is not an own child or declared synonym. No equivalence follows from the common name prefix.

## Evidence

The own NCBITAXON source ID, label, count, unit and snapshot note match the inventory. One `NAME` assertion is not a sequence, specimen or biological abundance count. `strain_count: 0` describes BacDive inventory coverage, not biological absence.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036846%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned zero entries with a phrase-not-found warning. This supplies no positive own sequence evidence, not proof that no own sequence exists. The [broader name query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=%22Wiebesia%20flava%22%5BAll%20Fields%5D%20AND%20Wolbachia%5BAll%20Fields%5D&retmode=json&retmax=100) returned one entry, [JF902518.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902518.1).

JF902518.1 explicitly names Wolbachia endosymbiont of Wiebesia flava-SAG and `taxon:1094266`, with voucher `BIOUG<CAN>:YLCFX388-08.w` and BOLD cross-reference `ASWFW067-10.COI-5P`. It annotates partial COI gene/CDS, translation table 11 and protein AEG77978.1. Declared/actual length is 642 bases with N ambiguity. Source qualifiers specify Diaoluoshan, Hainan, China, 19-Apr-2007, collected by Fenggui, Liwei, Huhaoyuan and Niuliming and identified by Alex Smith. These are SAG-specific specimen annotations, not own distribution, phenotype, cultured-strain or assembly evidence.

The candidate retains an unpublished Smith study reference and a 01-May-2011 direct submission. Neither a shared study nor a similar label supplies identifier-level equivalence. No independent BOLD or publication-level specimen mapping was established, and no biological claim from this candidate is transferred to the target.

The [own NCBI genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036846/dataset_report) returned an empty object. This is bounded lack of positive assembly evidence, not universal genome absence. A partial marker and specimen voucher would not establish an eligible culture-to-genome chain even for their own taxon.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded numeric ID and full label/slug spelling. All six candidates were read in full: two native name JSON rows and four backbone/scope TSV rows, describing this target and the separate SAG concept.

All five source `SOURCE.json` files were parsed without a target match. Complete own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. These negatives concern the inspected snapshots and identifiers, not all external evidence. No inspected source establishes an eligible own culture-to-genome link.

Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty for the supported seeded claims. The distinct-ID SAG marker is not a missing own link.

`data/taxa/PATHS.tsv:15172` agrees with the filename. `curation/seed_scope.tsv:322873` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external entry. No human-reviewed status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. The exact nucleotide query's warning is retained as a limitation; the broader candidate was resolved to another explicit taxon ID and is not treated as target evidence.

## Recommended Edits

None required. Keep flava and flava-SAG concepts separate unless an authoritative identifier-level change supports a future update. Do not infer synonymy, a genome or a culture deposit from the suffix or marker.

Any later authorized correction belongs in maintained upstream extraction inputs, `src/taxonmech/ncbi_taxdump.py`, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, as appropriate, followed by regeneration. Do not hand-edit this generated YAML.

## Follow-up Checks

No defect-specific repair is needed. Future enrichment should resolve the exact taxon ID and independently inspect publication/specimen mappings before adding experimental claims. Genome links require eligible explicit culture-deposit chains. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No YAML, source, scope/history entry, generated page, branch, worktree or GitHub item changed. The other taxon was disambiguation context only; no host or Eukaryota record was reviewed. No paid research was performed.
