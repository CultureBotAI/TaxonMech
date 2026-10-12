# YAML Record Review: Wolbachia endosymbiont of Blastophaga sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_blastophaga_sp.yaml`
- Started UTC: 2026-10-09T16:17:16Z
- Finished UTC: 2026-10-09T16:21:34Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036837` was read. It denotes Wolbachia endosymbiont of Blastophaga sp., rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), genetic code 11, grounding `EXACT` and status `SEEDED`. It contains zero inventoried strains, one NCBITAXON name attestation and one seeding event.

An ignored-inclusive filename inventory resolved this YAML and no prior own report. Its SHA-256 is `88452b52c1bab528db4abdae49fb4db670e2c1205396b4297bb3b422716a66e9`. Other organism rows were inspected only to distinguish source matches, not as additional review targets.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` with the existing environment.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_blastophaga_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_blastophaga_sp.yaml --workers 1 --out /private/tmp/taxonmech-blastophaga-20261009-validation.tsv`: passed, one file and zero errors; the inspected output TSV has only its header.
- `uv run --offline python scripts/validate_history.py history`: passed earlier in this review turn, 17 valid records and zero invalid links; history was not changed.
- Structured own-row checks passed for identity, every ancestor, source attestation, PATHS/scope entries and generated event wording.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift were not rerun for this individual review. The documented `just verify-corpus` gate has no record selector. Focused comparisons do not certify corpus reproduction.
- Not applicable: OAK curator-added graph checks and iModulonDB gene/component checks. This YAML contains no causal graph, gene, regulator, pathway, trait or transcriptomics assertion. External identity-marker checks do not add these claims to the YAML.
- Live NCBI taxonomy, exact-taxon nucleotide search and genome search were inspected independently. All 63 returned GenBank records were fetched; source qualifiers, marker annotations, bibliographic metadata and sequence-length/alphabet checks were inspected across the complete set, with common fields grouped and differing values preserved. Amino-acid strings were reduced to length/hash checks for inspection; no protein-function or sequence-alignment validation is claimed.
- Not checked: the contextual Smith paper's supplementary Table S2 specimen mapping. The existing environment lacks the legacy XLS `xlrd` reader; no dependency was installed. Its publisher text and PubMed metadata were inspected in this turn. BOLD identifiers below were read as GenBank cross-references, not independently resolved at BOLD.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222631` and `data/catalog/ncbi_names-0005.jsonl.gz:32225` support the exact identifier, label and scientific-name status. The backbone supports species rank, parent, genetic code, NCBI-only attestation and 2026-09-13 snapshot. It supplies no exact, related or broad synonyms.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036837&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036837) agree. All eleven lineage entries match the local backbone and live authority: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676. Labels and ranks are consistent.

The record denotes the bacterial endosymbiont, not its Blastophaga host. NCBI species rank does not establish a formally named species or cultured type strain. Host identity, marker similarity or a study-wide supergroup result does not justify replacing the carried lineage.

## Evidence

The attestation counts one NCBI name, not 63 sequences, cultures or strains. Its source ID, label, count, unit and snapshot date match the own inventory. `strain_count: 0` concerns inventoried BacDive coverage, not biological absence.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036837%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned 63 IDs, all retrieved. Their accessions span [JF902315.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902315.1) through [JF902377.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902377.1), with every intermediate accession present. All carry the exact organism and `taxon:1036837`, a `BIOUG<CAN>:` specimen voucher ending in .w, a BOLD COI-5P cross-reference, partial COI gene/CDS annotation and translation table 11. They are marker sequences, not assemblies or culture deposits.

Declared and actual nucleotide lengths agree for all 63. Lengths range from 436 to 642 bases. Only five sequences have the A/C/G/T-only alphabet; the others include N and, in some cases, additional ambiguity codes R, W or Y. No complete-genome, full-length-gene, sequence-equivalence or functional inference is made from these markers.

Source qualifiers cover collection sites in Yunnan, Fujian and Hainan, China, with dates from 2002 through 2007. For example, JF902377.1 is voucher YLCFY114-08.w/BOLD ASWFW168-10.COI-5P, Yunnan, 20-May-2002; JF902315.1 is YLCFY265-08.w/ASWFW198-10.COI-5P, Yunnan, 04-May-2004. The complete inspected set retains its differing specimen identifiers, coordinates, collection dates, collectors where supplied, and primer combinations. These details support source-specific specimen context, not culture eligibility.

All entries retain an unpublished Smith study reference and the 01-May-2011 direct submission. The related [Smith et al. 2012 publication, DOI 10.1371/journal.pone.0036514](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514), and [PubMed 22567162](https://pubmed.ncbi.nlm.nih.gov/22567162/) were inspected as context. Its methods describe bacterial COI recovery from host extracts and the .w naming convention. The supplementary accession mapping was not verified. Study-wide prevalence, supergroup assignments and reproductive effects are not assigned to this taxon.

The live [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036837/dataset_report) returned an empty object. That query supplies no positive assembly evidence, not proof of universal absence.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches used the bounded numeric identifier and label/slug-compatible spelling. All 36 candidates were read in full: 34 native JSON rows and two TSV rows. All five source `SOURCE.json` files were parsed and had no target match. A follow-up ignored-inclusive compressed-source search covering all 63 accessions and their voucher/BOLD patterns found no local match in those roots. These absence findings concern the inspected snapshot only.

All 33 non-target native matches share BioProject PRJNA1036837, whose numeric suffix is not an NCBI taxonomic association. Their complete metadata identify other organisms:

- Six Enterococcus faecalis records, taxon 1351: En2-SB, En2-EF, En2-AC, En1-EF, En1-SB and En1-AC; GCA_051295875.1, GCA_051295895.1, GCA_051295935.1, GCA_051295955.1, GCA_051295975.1 and GCA_051295995.1, with corresponding BV-BRC records. The last three also have GTDB catalog rows under Enterococcus faecalis_A. Their NCBI exclusion flags are retained as source context, not evidence about Wolbachia.
- Enterococcus gilvus En4, taxon 160453, GCA_051295915.1 and BV-BRC 160453.29.
- Proteus mirabilis Pr2-AC and Pr1-SB, taxon 584, GCA_051296015.1/GCA_051296035.1 and BV-BRC 584.4729/584.4730.
- Serratia marcescens Se1-AC and Se2-AC, taxon 615, GCA_051296065.1/GCA_051296095.1 and BV-BRC 615.4314/615.4315.
- Yokenella regensburgei Yo1-SB, Yo2-SB, Yo1-EF and Yo1-AC, taxon 158877, GCA_051295825.1, GCA_051296055.1, GCA_051296115.1 and GCA_051296125.1, with BV-BRC 158877.30 through 158877.33. Their BioSamples, WGS accessions and available paired RefSeq IDs concern those organisms.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. No inspected source supplies an eligible own culture-to-genome chain. Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty. External specimen markers do not demonstrate a missing required strain/genome relationship.

`data/taxa/PATHS.tsv:15163` agrees with the filename. `curation/seed_scope.tsv:322864` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z agrees with the source/scope-generated wording. Ignored-inclusive history filename and content searches found no target-specific external history entry. No human-reviewed status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete record and inspected evidence. The optional supplementary-literature limitation does not leave an asserted YAML claim unsupported.

## Recommended Edits

None required. Preserve the bacterial identity and distinguish it from the host, specimens, partial markers and unrelated genome projects. Do not import culture/genome links by matching a project-number suffix.

Any later authorized correction belongs in maintained upstream extraction inputs, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, followed by regeneration, not a hand edit to this generated YAML.

## Follow-up Checks

No defect-specific repair is required. A later literature-enrichment task should inspect Table S2 before asserting specimen-level publication mappings and resolve BOLD cross-references before making current BOLD claims. Additional strain/genome relationships require explicit eligible source chains. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target; temporary validation and marker-comparison output was kept outside the repository. No record, source, scope/history entry, generated page, branch, worktree or GitHub item was changed. Other organisms were source context only; no host or Eukaryota record was reviewed. No paid research was performed.

