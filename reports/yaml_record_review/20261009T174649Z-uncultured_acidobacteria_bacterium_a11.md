# YAML Record Review: uncultured Acidobacteria bacterium A11

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_acidobacteria_bacterium_a11.yaml`
- Started UTC: 2026-10-09T17:43:44Z
- Finished UTC: 2026-10-09T17:46:49Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036854` was read. It denotes uncultured Acidobacteria bacterium A11, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:57727`, genetic code 11, grounding `EXACT`, status `SEEDED`. It has six lineage entries, no synonyms, zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this YAML and no prior own report. Target SHA-256: `e96bfd3fe55eb8d5e0ca9ccb9e5b0e30ecbe55eb9e1d63e6ac985f1705f81428`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_acidobacteria_bacterium_a11.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_acidobacteria_bacterium_a11.yaml --workers 1 --out /private/tmp/taxonmech-acidobacteria-a11-20261009-validation.tsv`: passed, one file and zero errors; the output TSV was inspected and is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed this turn, 17 valid records and zero invalid links.
- Own-row comparisons passed for identity, each ancestor, source attestation, PATHS/scope entries and event wording. All three local source candidates were read in full.
- Live NCBI taxonomy, nucleotide and genome responses were inspected. Complete GenBank metadata, source qualifiers, feature annotations and references were read; protein translations were represented by length/SHA-256. Nucleotide length/alphabet/hash checks passed. No alignment or protein-function validation is claimed.
- The linked PMID/DOI were verified through live PubMed metadata and abstract.
- Not checked: fresh publisher full-text inspection, because attempts to open the article and its redirect failed. Search-result text was not used to establish clone-specific experimental claims. Supplementary figures were not inspected.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and generated-site drift. `just verify-corpus` has no record selector; focused comparisons do not certify reproduction.
- Not applicable: curator-added OAK graph and iModulonDB checks. The YAML asserts no graph, gene, pathway, regulator, phenotype or transcriptomic result.

## Identity and Grounding

The own backbone row at `data/raw/ncbitaxon_taxa.tsv:222648` and scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32247` agree with the exact ID, name, rank, parent, code and 2026-09-13 snapshot. No own synonym or retirement is supplied.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036854&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036854) confirm this identity. The six root-first ancestors agree with the local backbone: root 1 (`NO_RANK`), cellular organisms 131567 (`CELLULAR_ROOT`), Bacteria 2 (`DOMAIN`), Pseudomonadati 3379134 (`KINGDOM`), Acidobacteriota 57723 (`PHYLUM`) and environmental samples 57727 (`NO_RANK`). EFetch supplies the five ancestors after root; Datasets also supplies root 1.

The Environmental samples division does not contradict the bacterial domain. Acidobacteria in the organism label and Acidobacteriota in the lineage are the authority's supplied fields, not an inconsistency to reconcile locally. The species rank denotes an NCBI environmental taxon, not validly published nomenclature or proof of a cultured species. A11 is not interchangeable with another clone from the same study.

## Evidence

The single NCBITAXON `NAME` assertion, exact source ID/label, count and snapshot note match the inventory. The count does not enumerate cultures, fosmids or genes. `strain_count: 0` records BacDive inventory coverage rather than a universal claim that the organism cannot be cultured.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036854%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned one entry, [JF342591.1](https://www.ncbi.nlm.nih.gov/nuccore/JF342591.1). Its source explicitly identifies `taxon:1036854`, the own organism, `clone: fosmid A11` and an environmental sample. The isolation source is a soil core at 10-50 cm depth from Hancock Agricultural Research Station, Central Sands, Hancock, Wisconsin, USA.

This is a partial fosmid sequence, not a whole-genome assembly or culture-deposit identifier. Declared and actual length agree at 39,783 nucleotides, alphabet A/C/G/T, SHA-256 `5229ced7cd4d6ad05ddc0bd843c0949e4defaf9ff7026c81dc65d7e70e3bfe4d`. Complete annotation inspection found 21 CDS and four miscellaneous features; all CDS use translation table 11. The polyketide-synthase CDS at 31634..39274 has protein accession AEH26521.1. Predicted efflux proteins and a metal-efflux-pump annotation do not themselves establish a measured resistance phenotype. None of these functional annotations is asserted in the YAML.

GenBank cites PMID [21539584](https://pubmed.ncbi.nlm.nih.gov/21539584/) and DOI `10.1111/j.1574-6941.2011.01122.x`. Live PubMed confirms the matching article, "Polyketide synthase pathways identified from a metagenomic library are derived from soil Acidobacteria," FEMS Microbiology Ecology 78(1):176-187 (2011). The citation supports the provenance of the sequence study; the abstract alone does not assign every reported experiment to A11. No clone-specific PCR result, compound-production phenotype or cultured-isolate equivalence is inferred here.

The [own genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036854/dataset_report) returned an empty object. This supplies no positive assembly evidence, not proof of universal genome absence. Neither the inspected fosmid nor the local inventories supplies an eligible explicit culture-deposit-to-genome chain.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded numeric ID and complete label/slug spelling. All three candidates were read completely: the scientific-name JSON row and backbone/scope TSV rows. All five source `SOURCE.json` files were parsed without a target match. A further ignored-inclusive compressed search for JF342591, PMID 21539584 and the exact DOI found no local match in those roots. These negatives are bounded to the inspected snapshots and identifiers.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. Optional nomenclature, mappings, strain/genome lists, experimental evidence and graphs are appropriately empty for the supported seeded claims. The external fosmid/publication could support later typed provenance enrichment, but is not a required genome link.

`data/taxa/PATHS.tsv:15180` agrees with the filename. `curation/seed_scope.tsv:322881` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external entry. The YAML does not assert human-reviewed status.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. All asserted taxonomy and provenance fields are supported. Unchecked experimental details concern potential enrichment, not an unsupported claim already in this record.

## Recommended Edits

None required. Preserve the distinction between the environmental taxon, fosmid A11, a cultured strain and an assembly. Do not promote sequence similarity annotations to measured phenotypes.

Any later authorized correction belongs in maintained extraction inputs, `src/taxonmech/ncbi_taxdump.py`, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, as appropriate, followed by regeneration. Do not hand-edit the generated YAML. A later clone/publication cross-reference must retain its exact accession provenance and non-genome type.

## Follow-up Checks

No defect-specific repair is needed. Reopen the primary article and inspect A11-specific experimental details and supporting figures before functional enrichment. Genome enrichment requires an explicit eligible culture-deposit chain. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No YAML, source, scope/history entry, generated page, branch, worktree or GitHub item changed. Other study targets were disambiguation context only; no Eukaryota record was reviewed. No paid research was performed.
