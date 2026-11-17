# YAML Record Review: Wolbachia endosymbiont of Neosycophila omeomorpha

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_neosycophila_omeomorpha.yaml`
- Started UTC: 2026-10-09T16:57:53Z
- Finished UTC: 2026-10-09T17:02:14Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036844` was read. It denotes Wolbachia endosymbiont of Neosycophila omeomorpha, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), genetic code 11, grounding `EXACT` and mapping status `SEEDED`. It contains no synonyms, zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this YAML and two separately identified suffixed concepts, but no prior own report. The target SHA-256 is `39e5fa104f314eb85ee2a594867881f88c8803e51a523fccc284915b85c47b63`. Other taxa were inspected only as disambiguation context.

## Validation

Commands used the existing environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_neosycophila_omeomorpha.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_neosycophila_omeomorpha.yaml --workers 1 --out /private/tmp/taxonmech-neosycophila-omeomorpha-20261009-validation.tsv`: passed, one file and zero errors; the inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed earlier this turn, 17 valid records and zero invalid links; history was unchanged.
- Own-row comparisons passed for identity, every ancestor, attestation fields, PATHS/scope entries and generated event wording. Native scientific-name rows and similarly named candidate rows were read in full.
- Live NCBI taxonomy and exact-taxon nucleotide/genome responses were inspected. All five broader nucleotide candidates were fetched, and their complete metadata, source qualifiers, annotations and references were read with nucleotide length/alphabet checks. No sequence alignment or protein-function validation is claimed.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift. The documented `just verify-corpus` gate has no record selector. Focused comparisons do not certify corpus reproduction.
- Not applicable: OAK curator-added graph and iModulonDB gene/component checks. The YAML asserts no graph, gene, regulator, pathway, trait or transcriptomics result.
- Not checked: independent BOLD resolution or external publication/supplementary specimen mapping. The YAML cites no experimental paper, and the candidate markers belong to other taxon IDs.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222638` and the native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:32233` support the exact identifier, scientific name, species rank, parent, genetic code and 2026-09-13 snapshot. No own synonym is asserted by the inspected local rows.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036844&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036844) agree with the identity. All eleven root-first lineage entries match the local backbone. EFetch matches the ten named ancestors after root; Datasets also supplies root ID 1: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676.

This is the bacterial taxon concept, not the host species or every Wolbachia associated with that host. The similarly prefixed omeomorpha-TIN endosymbiont is `NCBITaxon:1094260`; omeomorpha-TIN.F is `NCBITaxon:1094261`. Their backbone rows are 235306 and 235307, native name rows 47535 and 47536, and scope rows 333619 and 333620. They share the same parent but are neither own children nor declared synonyms. Similar spelling does not justify merging their evidence into this target.

## Evidence

The NCBITAXON attestation's source ID, label, count, unit and snapshot date match the own inventory. Its one `NAME` assertion is not a sequence, specimen, strain or biological abundance count. `strain_count: 0` describes classified BacDive inventory coverage, not biological absence.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036844%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned zero entries with a phrase-not-found warning. This is bounded lack of positive evidence from that query, not proof that no sequence exists for the target. A [broader name query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=%22Neosycophila%20omeomorpha%22%5BAll%20Fields%5D%20AND%20Wolbachia%5BAll%20Fields%5D&retmode=json&retmax=100) returned five entries, all explicitly assigned to the two different IDs:

| Accession | Explicit source taxon | Bases | BIOUG voucher suffix | BOLD cross-reference |
| --- | --- | --- | --- | --- |
| [JF902485.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902485.1) | `1094260`, omeomorpha-TIN | 608 | `YLCFX519-08.w` | `ASWFW090-10.COI-5P` |
| [JF902484.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902484.1) | `1094260`, omeomorpha-TIN | 642 | `YLCFX517-08.w` | `ASWFW089-10.COI-5P` |
| [JF902483.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902483.1) | `1094261`, omeomorpha-TIN.F | 642 | `YLCFX528-08.w` | `ASWFW094-10.COI-5P` |
| [JF902482.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902482.1) | `1094261`, omeomorpha-TIN.F | 612 | `YLCFX524-08.w` | `ASWFW093-10.COI-5P` |
| [JF902481.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902481.1) | `1094261`, omeomorpha-TIN.F | 612 | `YLCFX523-08.w` | `ASWFW092-10.COI-5P` |

All five annotate partial COI gene/CDS with translation table 11; their declared and actual nucleotide lengths agree and all contain N ambiguity. The TIN specimens have 05-Apr-2007 collection qualifiers from Nada, Taoyuancun, Hainan, China; the TIN.F specimens have 15-Apr-2007 qualifiers from Nada, Hainan. These are candidate-specific specimen details, not evidence for the target's own distribution, phenotype, cultured strains or genome assemblies.

The five entries retain an unpublished Smith study reference and a 01-May-2011 direct submission. No independent publication or BOLD specimen mapping was established. Neither shared submission context nor similar labels establish taxonomic equivalence. No supergroup, reproductive phenotype, prevalence or protein-function claim is transferred to this YAML.

The [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036844/dataset_report) returned an empty object. It supplies no positive own assembly evidence, not proof of universal genome absence. None of the five marker vouchers establishes an eligible own culture-to-genome chain.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches used the bounded numeric ID and full label/slug spelling. All nine candidates were read in full: three native name JSON rows and six backbone/scope TSV rows, describing this target and the two separately identified suffixed concepts.

All five source `SOURCE.json` files were parsed without a target match. Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. These negative findings concern the inspected local snapshots and identifiers, not all external evidence. The inspected sources supply no eligible own culture-to-genome link.

Optional synonyms, nomenclature, additional mappings/xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty for the supported seeded claims. Distinct-ID marker candidates are not missing own links.

`data/taxa/PATHS.tsv:15170` agrees with the filename. `curation/seed_scope.tsv:322871` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external history entry. No human-reviewed mapping status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. The nucleotide query limitation remains explicit; all broader candidates were resolved to different taxon IDs and are not silently treated as target evidence.

## Recommended Edits

None required. Preserve this concept separately from the TIN and TIN.F concepts unless an authoritative identifier-level change supports a later update. Keep specimen markers distinct from culture and genome assertions.

Any later authorized correction belongs in maintained upstream extraction inputs, `src/taxonmech/ncbi_taxdump.py`, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, as appropriate, followed by regeneration. Do not hand-edit this generated YAML.

## Follow-up Checks

No defect-specific repair is required. Future enrichment should repeat an exact-ID lookup and verify candidate taxon IDs rather than rely on host-name similarity. Experimental additions need independently inspected publication/specimen mappings; genome links require explicit eligible culture-deposit chains. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No record, source, scope/history entry, generated page, branch, worktree or GitHub item changed. The two other taxon concepts were disambiguation context only; no host or Eukaryota record was reviewed. No paid research was performed.
