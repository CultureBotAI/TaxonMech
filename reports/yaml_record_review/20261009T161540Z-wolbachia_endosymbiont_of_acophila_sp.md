# YAML Record Review: Wolbachia endosymbiont of Acophila sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_acophila_sp.yaml`
- Started UTC: 2026-10-09T16:13:14Z
- Finished UTC: 2026-10-09T16:15:40Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` for `NCBITaxon:1036836` was read. It denotes Wolbachia endosymbiont of Acophila sp., rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), genetic code 11, grounding `EXACT` and status `SEEDED`. It has zero inventoried strains, one NCBITAXON name attestation and one seeding event.

The ignored-inclusive filename inventory also found `wolbachia_endosymbiont_of_acophila_sp_1.yaml`. Its source identity is taxon 1248005, labeled Wolbachia endosymbiont of Acophila sp. 1. The exact identifier and PATHS row uniquely resolve the present target; the other record was not reviewed. No prior report for this target was found. Target SHA-256: `26c51c2b3bc369b3dd3b5385ec56f56d9234029b5019ff59eeb1380fea4573ab`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` with the existing environment.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_acophila_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_acophila_sp.yaml --workers 1 --out /private/tmp/taxonmech-acophila-20261009-validation.tsv`: passed, one file and zero errors; the inspected output TSV contains only its header.
- `uv run --offline python scripts/validate_history.py history`: passed earlier in this review turn, 17 valid records and zero invalid links; history was not changed.
- Structured own-row checks passed for identity, every ancestor, source attestation, PATHS/scope entries and generated event wording.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift were not rerun for this individual review. The documented `just verify-corpus` gate has no record selector. Focused comparisons do not certify corpus reproduction.
- Not applicable: OAK curator-added graph checks and iModulonDB gene/component checks. The YAML has no causal graph, gene, regulator, pathway, trait or transcriptomics assertion. External identity-marker checks do not add these claims to the record.
- Live NCBI EFetch/Datasets taxonomy and exact-taxon nucleotide/genome queries were inspected independently for this target, followed by all nine GenBank records. The contextual Smith paper's publisher text and PubMed metadata were inspected during this same turn.
- Not checked: the contextual paper's supplementary Table S2 specimen mapping. The existing environment lacks the legacy XLS `xlrd` reader; no dependency was installed. GenBank's own qualifiers supply the specimen details used here. BOLD cross-references were not independently resolved at BOLD.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222630` and `data/catalog/ncbi_names-0005.jsonl.gz:32224` support the exact identifier and scientific name. The backbone supports species rank, direct parent, genetic code, NCBI-only attestation and the 2026-09-13 snapshot. It has no exact, related or broad synonyms requiring representation.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036836&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036836) agree. All eleven ancestor entries match the local backbone and live authority: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676. Labels and ranks are consistent.

This is the bacterial endosymbiont concept, not its Acophila host. NCBI species rank does not establish a formally named species or cultured type strain. The carried unclassified-Wolbachia placement is not replaced by a supergroup inference or host classification.

## Evidence

The attestation counts one NCBI name, not nine specimens or nine bacterial strains. Its source ID, label, count, unit and snapshot date match the own inventory. `strain_count: 0` concerns inventoried BacDive coverage, not biological absence.

The exact non-expanded query `txid1036836[Organism:noexp]` returned nine nucleotide IDs. Complete metadata, source/gene/CDS features, references and actual-versus-declared sequence lengths were inspected for every returned record. All are partial COI sequences with the exact organism, `taxon:1036836` and translation table 11:

| Accession | Length, bases | `BIOUG<CAN>` voucher suffix | BOLD cross-reference |
|---|---:|---|---|
| [JF902306.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902306.1) | 612 | YLCFW576-08.w | ASWFW009-10.COI-5P |
| [JF902307.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902307.1) | 612 | YLCFW577-08.w | ASWFW010-10.COI-5P |
| [JF902308.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902308.1) | 612 | YLCFW578-08.w | ASWFW011-10.COI-5P |
| [JF902309.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902309.1) | 612 | YLCFW579-08.w | ASWFW012-10.COI-5P |
| [JF902310.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902310.1) | 612 | YLCFW580-08.w | ASWFW013-10.COI-5P |
| [JF902311.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902311.1) | 642 | YLCFW261-08.w | ASWFW005-10.COI-5P |
| [JF902312.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902312.1) | 599 | YLCFW262-08.w | ASWFW006-10.COI-5P |
| [JF902313.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902313.1) | 640 | YLCFW263-08.w | ASWFW007-10.COI-5P |
| [JF902314.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902314.1) | 642 | YLCFW264-08.w | ASWFW008-10.COI-5P |

The full voucher prefix is `BIOUG<CAN>:`. JF902306-JF902310 record Yunnan, China, 16-May-2004; JF902311-JF902314 record Danzhou, Hainan, China, 19-Apr-2005. Length checks passed for all nine. JF902309 and JF902312 include ambiguous N bases; the remaining seven contain A/C/G/T only. These are source-associated specimen markers, not culture deposits or genome assemblies. Identical short marker sequences do not establish identical bacterial taxa or strains.

Each GenBank record retains an unpublished Smith reference titled "Wolbachia and Barcoding Insects: Patterns, Potential and Problems." The related [Smith et al. 2012 publication, DOI 10.1371/journal.pone.0036514](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514), and [PubMed 22567162](https://pubmed.ncbi.nlm.nih.gov/22567162/) were checked as context. The methods describe bacterial COI recovery from host extracts and the .w naming convention. Without inspecting supplementary Table S2, this review does not claim a verified paper-to-specimen mapping. Study-wide prevalence, reproductive effects and supergroup assignments are not asserted for this record.

The live [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036836/dataset_report) returned an empty object. This provides no positive assembly evidence through that query, not proof of universal absence.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches used the bounded numeric identifier and label/slug-compatible spelling. All 19 candidates were read in full: 15 native JSON rows and four TSV rows. All five source `SOURCE.json` files were parsed and had no target match. A further ignored-inclusive compressed-source search for all nine accessions and their voucher/BOLD identifiers found no match in those roots. These absence findings are snapshot-bounded.

The non-target candidates resolve as follows:

- Taxon 1248005 has the separate Acophila sp. 1 endosymbiont name, with its own backbone, scientific-name and scope rows. No inspected source equates it with taxon 1036836.
- BioProject PRJNA1036836 identifies three unrelated bacterial sequencing records, not this taxon. Acutalibacter caecimuris M00118 is taxon 3093657, GCA/GCF_034335085.1, SAMN38153120, BV-BRC 3093657.3, GOLD Go0716461/Gp0879794. Neglectibacter caecimuris M00184 is taxon 3093658, GCA/GCF_034335015.1, SAMN38153121, BV-BRC 3093658.3, GOLD Go0716462/Gp0879795. Acutalibacter intestini M00204 is taxon 3093659, GCA/GCF_034334985.1, SAMN38153122, BV-BRC 3093659.3, GOLD Go0716463/Gp0879796. Their type-material and reference-genome flags do not support any Wolbachia linkage.
- GCA_964511175.1/SAMEA117291213 has NCBI taxon 332614, uncultured Pseudomonadales bacterium, and a different GTDB placement under Patescibacteriota. That source disagreement remains attached to its own assembly. Its ungapped length, not its identity, matches 1036836.
- GCA_900557205.1/SAMEA4892602 is uncultured Eubacteriales bacterium, taxon 172733; GCA_982747085.1/SAMEA122251129 is Bacteroidota bacterium, taxon 1898104. Their genome-size values likewise match the numeric search without identifying this target.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. No inspected source supplies an eligible own culture-to-genome chain. Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty. The external markers do not demonstrate a missing required genome relationship.

`data/taxa/PATHS.tsv:15162` agrees with the filename. `curation/seed_scope.tsv:322863` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z agrees with the source/scope-generated wording. Ignored-inclusive history filename and content searches found no target-specific external history entry. No human-reviewed status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete record and inspected evidence. The bounded supplementary-literature limitation does not leave an asserted YAML claim unsupported.

## Recommended Edits

None required. Preserve the bacterial identity and separate it from the host, specimen vouchers, marker sequences and similarly named taxon. Do not join other sources on a project-number suffix or genome-size statistic.

Any later authorized correction belongs in maintained upstream extraction inputs, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, followed by regeneration, not a hand edit to this generated YAML.

## Follow-up Checks

No defect-specific repair is required. A later literature-enrichment task should inspect Table S2 before asserting specimen-level publication mappings and resolve BOLD cross-references before making current BOLD claims. Further strain/genome claims require explicit eligible source chains. Before authorized regeneration, run documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No record, source, scope/history entry, generated page, branch, worktree or GitHub item was changed. Other organisms were source context only; no host or Eukaryota record was reviewed. No paid research was performed.
