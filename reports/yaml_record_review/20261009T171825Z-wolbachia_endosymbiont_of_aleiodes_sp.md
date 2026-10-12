# YAML Record Review: Wolbachia endosymbiont of Aleiodes sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_aleiodes_sp.yaml`
- Started UTC: 2026-10-09T17:15:57Z
- Finished UTC: 2026-10-09T17:18:25Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036848` was read: Wolbachia endosymbiont of Aleiodes sp., rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), code 11, grounding `EXACT`, status `SEEDED`. It has one exact synonym, zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this YAML and no prior own report. Target SHA-256: `59fbfdd1bdc2ea580cde4a213fd0e91b9542dffb6fb313a4a160b7583cdbbb59`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_aleiodes_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_aleiodes_sp.yaml --workers 1 --out /private/tmp/taxonmech-aleiodes-sp-20261009-validation.tsv`: passed, one file and zero errors; inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed, 17 valid records and zero invalid links.
- Own-row comparisons passed for identity, every ancestor, source attestation, PATHS/scope entries and event wording. The exact synonym was checked against its native name class, live authority and repository mapping. All nine local source candidates were read in full.
- Live NCBI taxonomy and exact-taxon nucleotide/genome responses were inspected. Complete metadata, source qualifiers, annotations and references for both nucleotide hits were read, with length/alphabet checks. No sequence alignment or protein-function validation is claimed.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift. `just verify-corpus` has no record selector; focused comparisons do not certify corpus reproduction.
- Not applicable: curator-added OAK graph and iModulonDB checks; the YAML asserts no graph, gene, regulator, pathway, trait or transcriptomic result.
- Not checked: independent BOLD resolution or external publication/supplementary specimen mapping. No experimental paper is cited by the YAML.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222642` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:32238` agree with the exact ID, label, species rank, parent, code and 2026-09-13 snapshot. The shorter form Wolbachia endosymbiont of Aleiodes is explicitly classed as `synonym` at native row 32239 and appears in the backbone's exact-synonym field.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036848&retmode=xml) lists the shorter form under `OtherNames/Synonym`. Its `EXACT_SYNONYM` placement agrees with `src/taxonmech/ncbi_taxdump.py`, which maps native synonym/equivalent-name classes to exact synonyms and other name classes to related synonyms. It is not a host-genus-wide equivalence inferred from spelling.

EFetch and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036848) support the own identity. All eleven root-first lineage entries match the local backbone. EFetch supplies the ten named ancestors after root; Datasets also supplies root 1: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676. Ancestor ranks agree with the YAML.

The record denotes this bacterial taxon, not the Aleiodes host grouping or all its endosymbionts. The exact synonym does not broaden that scope.

## Evidence

The NCBITAXON source ID, label, count, unit and snapshot note match the inventory. One `NAME` assertion is not a count of all aliases, specimens, sequences or biological abundance. `strain_count: 0` describes BacDive inventory coverage, not biological absence.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036848%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned two entries, both explicitly carrying the own organism and `taxon:1036848`:

| Accession | Bases | BIOUG voucher suffix | BOLD cross-reference |
| --- | --- | --- | --- |
| [JF960243.1](https://www.ncbi.nlm.nih.gov/nuccore/JF960243.1) | 657 | `ASQSQ719-10.w` | `ASEND159-10.COI-5P` |
| [JF960242.1](https://www.ncbi.nlm.nih.gov/nuccore/JF960242.1) | 378 | `ASQSQ062-09.w` | `ASEND078-09.COI-5P` |

Both annotate partial COI gene/CDS, translation table 11 and `codon_start: 1`; declared and actual lengths agree. JF960243.1 has only A/C/G/T nucleotides and a BARCODE keyword; JF960242.1 includes N ambiguity. The former gives United Kingdom and collector Mark Shaw, without a collection date; the latter gives Khao Kho National Park, Phetchabun, Thailand, 01-Jan-2003, and collectors Somchai Chachumnan and Saink Singtong. Both identify Alex Smith. These are source-specific specimen annotations, not culture-deposit or assembly evidence.

Both entries retain an unpublished Smith study reference and a 01-May-2011 direct submission. No independent BOLD or publication-level specimen mapping was established. The markers do not justify taxon-wide prevalence, reproductive phenotype, supergroup assignment or experimentally established full-length protein function.

Five other local catalog rows are non-identity numeric matches:

- `data/bvbrc/bvbrc-0012.jsonl.gz:6354`, `data/catalog/ncbi_genbank-0031.jsonl.gz:33932` and `data/catalog/gtdb_genomes-0016.jsonl.gz:19025` refer to assembly `GCA_033977065.1` and BioProject `PRJNA1036848`. BV-BRC calls it Chlamydiales bacterium Cla049, taxon 2047757; the NCBI/GTDB rows call it Candidatus Algichlamydia australiensis, NCBI taxon 3341976. Those source-specific names/IDs are retained as context; neither identifies this Wolbachia, and the BioProject suffix is not a taxon ID.
- `data/catalog/ncbi_genbank-0066.jsonl.gz:28406` is `GCA_982676465.1`, Alphaproteobacteria bacterium, taxon 1913988. Its genome size alone is `1036848`.
- `data/catalog/allthebacteria.tsv.xz:1512397` concerns Pseudomonas aeruginosa sample `SAMN10436337`, run `SRR8198960`, assembly `ERZ25506541`. Only its SeqKit checksum contains the numeric substring. This is not a taxon, deposit or sequence-identity match.

The [own NCBI genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036848/dataset_report) returned an empty object. It supplies no positive assembly evidence rather than proving universal genome absence. None of the inspected markers or catalog candidates supplies an eligible own culture-to-genome chain.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded numeric ID and the complete shorter synonym/label/slug prefix. All nine candidates were read completely: six native JSON rows and three TSV rows, including the compressed ATB row.

All five source `SOURCE.json` files were parsed without a target match. A further ignored-inclusive compressed search for JF960242/JF960243, ASQSQ719-10/ASQSQ062-09 and ASEND159-10/ASEND078-09 found no local match in those roots. These negatives concern the inspected snapshots and identifiers, not all external evidence.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. The source-backed exact synonym is present. Optional additional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and graphs are appropriately empty for the seeded claims.

`data/taxa/PATHS.tsv:15174` agrees with the filename. `curation/seed_scope.tsv:322875` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external entry. No human-reviewed mapping status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. The exact synonym is source-backed; project suffix, genome length and checksum collisions are not treated as own links.

## Recommended Edits

None required. Preserve the exact synonym without broadening the taxon to every Aleiodes-associated endosymbiont. Keep marker specimens, culture deposits, BioProjects and genome identifiers distinct.

Any later authorized correction belongs in maintained upstream extraction inputs, the name-class mapping in `src/taxonmech/ncbi_taxdump.py`, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, as appropriate, followed by regeneration. Do not hand-edit this generated YAML.

## Follow-up Checks

No defect-specific repair is needed. Future name refreshes should retain native name classes and exact taxon IDs. Experimental additions need independently inspected publication/specimen mappings; genome links require explicit eligible culture-deposit chains, not numeric substrings. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No YAML, source, scope/history entry, generated page, branch, worktree or GitHub item changed. Unrelated catalog rows were disambiguation context only; no host or Eukaryota record was reviewed. No paid research was performed.
