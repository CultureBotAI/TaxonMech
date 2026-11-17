# YAML Record Review: Wolbachia endosymbiont of Ceratosolen grandii

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_ceratosolen_grandii.yaml`
- Started UTC: 2026-10-09T16:39:18Z
- Finished UTC: 2026-10-09T16:41:55Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036840` was read. It denotes Wolbachia endosymbiont of Ceratosolen grandii, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), code 11, grounding `EXACT` and status `SEEDED`. It contains zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this exact YAML and no prior own report. Its SHA-256 is `0223bd55eef3134564465336bc60189a241c9ff7ebe40a6c4795ff73cacf4e87`. Non-target source records were inspected only to distinguish candidate matches.

## Validation

Commands used the existing environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_ceratosolen_grandii.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_ceratosolen_grandii.yaml --workers 1 --out /private/tmp/taxonmech-ceratosolen-grandii-20261009-validation.tsv`: passed, one file and zero errors; inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed earlier this turn, 17 valid records and zero invalid links; history was unchanged.
- Structured own-row checks passed for identity, every ancestor, all attestation fields, PATHS/scope entries and generated event wording.
- A fresh exact-target comparison against the checksum-verified 2026-10-09 NCBI dump passed for the own identity and complete lineage. Full names, nodes, merged, deleted and citation members were scanned with the repository's `taxonmech.ncbi_taxdump.fields` parser.
- All thirteen exact-taxon GenBank candidates were fetched. Complete source qualifiers, annotations and references were inspected through common/variant field grouping. Nucleotide lengths/alphabets were checked; amino-acid strings were reduced to length/hash checks. No sequence-alignment or protein-function validation is claimed.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift. The documented `just verify-corpus` gate has no record selector. Focused source comparisons do not certify corpus reproduction.
- Not applicable: OAK curator-added graph and iModulonDB gene/component checks. No graph, gene, regulator, pathway, trait or transcriptomics assertion occurs in the YAML.
- External limitations: taxonomy EFetch/Datasets responses disagree with the positive primary dump and ESummary/name-search evidence. BOLD cross-references and publication-level specimen mappings were not independently resolved; no such claims are made in the YAML or inferred here.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222634` and `data/catalog/ncbi_names-0005.jsonl.gz:32228` support the exact identifier, scientific name, rank, parent, code and 2026-09-13 snapshot. Source exact, related and broad synonyms are empty.

All eleven lineage entries match the local backbone and the current primary dump: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676. Each label, rank and parent link agrees. The record denotes a bacterial endosymbiont, not its Ceratosolen host. NCBI species rank does not establish formal nomenclatural standing or a cultured type strain.

[Taxonomy ESummary](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=taxonomy&id=1036840&retmode=json) identifies this exact name and ID as active, species rank, bacterial GenBank division. [Exact scientific-name search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=taxonomy&term=%22Wolbachia%20endosymbiont%20of%20Ceratosolen%20grandii%22%5BScientific%20Name%5D&retmode=json&retmax=100) returns this one ID.

In contrast, [taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036840&retmode=xml) returned an empty TaxaSet, and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036840) returned an unrecognized-ID error. Their cause is unknown. These responses are not silently discarded, but do not establish a retirement or merger.

The independently downloaded [2026-10-09 NCBI primary dump](https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz) contains the exact taxon at `nodes.dmp:835858` and its scientific name at `names.dmp:1634206`; the own fields and every ancestor match the record. Full merged/deleted member scans have no own match. The current primary source therefore supports the seeded taxonomy despite the interface discrepancy.

## Evidence

The NCBITAXON attestation counts one name. Its source ID, label, count, unit and snapshot date agree with the own inventory. It does not count thirteen sequences, cultures or strains. `strain_count: 0` is an inventory count, not biological absence.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036840%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) and [broader host-name plus Wolbachia query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=%22Ceratosolen%20grandii%22%5BAll%20Fields%5D%20AND%20Wolbachia%5BAll%20Fields%5D&retmode=json&retmax=100) returned the same thirteen IDs. Every accession from [JF902403.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902403.1) through [JF902415.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902415.1), inclusive, was inspected. All carry the exact organism and `taxon:1036840`.

The entries annotate partial COI gene/CDS sequences with translation table 11. Declared and actual lengths agree: eight are 642 bases, four 612 bases and JF902410.1 is 641 bases. Four accessions (JF902403.1, JF902407.1, JF902409.1 and JF902411.1) include N ambiguity; the other nine have A/C/G/T-only alphabets. These are marker sequences, not genome assemblies or full-length-gene/function evidence.

Source qualifiers specify Yunnan, China, location Xtbg, 11-May-2004, with collector Zhenwenquan. Vouchers are BIOUG<CAN>:YLCFX645-08.w, YLCFX646-08.w and YLCFX648-08.w through YLCFX658-08.w; YLCFX647 is not in this returned set. BOLD cross-references run from ASWFW109-10.COI-5P through ASWFW121-10.COI-5P. These support source-specific specimen context, not eligible culture deposits.

The GenBank entries retain an unpublished Smith study reference and a 01-May-2011 direct submission. They supply no inspected publication-level taxon-specific phenotype, supergroup assignment or reproductive mechanism, and none is inferred. BOLD identifiers were read as GenBank cross-references, not independently resolved.

The [genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036840/dataset_report) returned an empty object. This is no positive assembly evidence, not proof of universal absence, especially given the taxonomy service limitation above.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded ID 1036840 and label/slug-compatible spelling. All five candidates were read in full: three native JSON and two TSV rows. All five source `SOURCE.json` files were parsed without a target match. A further ignored-inclusive compressed search covering all thirteen accessions and their voucher/BOLD patterns found no local match in those roots. These negative results are bounded to the inspected snapshot and identifiers.

The two non-target native matches are Salmonella enterica, taxon 28901: FDA1036840-C003-001/GCA_006200755.1/SAMN08390758 and FDA1036840-C005-001/GCA_005535035.1/SAMN08390749. Both are contig assemblies in PRJNA186035, excluded from RefSeq as a large multi-isolate project. Their strain-name numeric substring is not a taxonomic or culture relationship to this Wolbachia record.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, local type-material row, merged-ID row, dropped row or child. No inspected source supplies an eligible own culture-to-genome chain. Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty. The external marker specimens do not establish a missing required strain/genome link.

`data/taxa/PATHS.tsv:15166` agrees with the filename. `curation/seed_scope.tsv:322867` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external history entry. No human-reviewed mapping status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete record and inspected evidence. The live service inconsistency does not establish a record defect because the current primary dump independently verifies the asserted taxonomy fields.

## Recommended Edits

None required. Keep specimen-marker evidence distinct from culture and genome assertions. Do not import the Salmonella assemblies through a numeric substring match.

Any later authorized taxonomy correction belongs in the snapshot pinned by `conf/ncbi_taxdump.yaml`, its extraction through `src/taxonmech/ncbi_taxdump.py` and maintained inventory-generation code, or the seeding/scope inputs as appropriate, followed by regeneration. Do not hand-edit this generated YAML or replace the pinned source with a diagnostic download during review.

## Follow-up Checks

Recheck EFetch/Datasets before relying on those services during an authorized refresh. Preserve dated primary-source checksums and inspect nodes/names/merged/deleted evidence before inferring retirement. A later literature enrichment should independently resolve publication and BOLD specimen mappings before asserting experimental traits; genome links require eligible culture-deposit source chains. Run the documented corpus reproduction, provenance, schema, tests and publication gates before authorized regeneration.

## Additional Notes

The diagnostic dump at `/private/tmp/taxonmech-ncbi-taxdump-20261009.tar.gz` is 79,794,570 bytes. Its MD5 `8fa90f979abdf24614da0f4e2ac39dfb` matches the [published checksum](https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz.md5), and SHA-256 is `26505b54d0cffe428eb70aecea005c18bce0ac5d7a51fa55fb7cf805e1fa2290`. This archive was downloaded earlier in the turn; its checksum and exact target/lineage rows were checked again for this record. Archive members were streamed, not extracted into the repository. Its citation member contains no exact-target entry.

This new report is the only repository write for the target. No record, source, history/scope entry, generated page, branch, worktree or GitHub item changed. Other organisms were disambiguation context only; no Eukaryota record was reviewed. No paid research was performed.
