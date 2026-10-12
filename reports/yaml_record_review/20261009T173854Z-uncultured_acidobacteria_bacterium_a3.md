# YAML Record Review: uncultured Acidobacteria bacterium A3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_acidobacteria_bacterium_a3.yaml`
- Started UTC: 2026-10-09T17:36:20Z
- Finished UTC: 2026-10-09T17:38:54Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036853` was read. It denotes uncultured Acidobacteria bacterium A3, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:57727` (environmental samples under Acidobacteriota), genetic code 11, grounding `EXACT`, status `SEEDED`. It contains no synonyms, zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this YAML and no prior own report. Target SHA-256: `fa64e2e8633c3a9e0487eec0344a6359921b48f61da2ab4cc7ab0d3b2d741081`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_acidobacteria_bacterium_a3.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_acidobacteria_bacterium_a3.yaml --workers 1 --out /private/tmp/taxonmech-acidobacteria-a3-20261009-validation.tsv`: passed, one file and zero errors; inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed earlier this turn, 17 valid records and zero invalid links; history was unchanged.
- Own-row comparisons passed for identity, every ancestor, attestation fields, PATHS/scope entries and generated event wording. All six local source candidates were read in full.
- Live NCBI taxonomy and exact-taxon nucleotide/genome responses were inspected. Complete GenBank metadata, source qualifiers, feature annotations and references were read, with protein translations represented by length/SHA-256. Nucleotide length/alphabet/hash checks passed; no alignment, protein-function validation or phylogenetic reanalysis is claimed.
- The linked PMID/DOI were checked against the PubMed metadata/abstract and primary publisher methods/results inspected this turn; the article's own A3 accession mapping was checked independently of the A2 mapping.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift. `just verify-corpus` has no record selector; focused comparisons do not certify corpus reproduction.
- Not applicable: curator-added OAK graph and iModulonDB checks; the YAML itself asserts no graph, gene, regulator, pathway, trait or transcriptomic result.
- Not checked: independent inspection of figure 3's image, supplementary figures or experimental revalidation of predicted protein functions. The report does not claim to reproduce the paper's functional analysis.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222647` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:32246` agree with the exact ID, label, species rank, parent, code and 2026-09-13 snapshot. No own synonym or retirement is supplied.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036853&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036853) agree with the identity. All six root-first lineage entries match the local backbone: root 1 (`NO_RANK`), cellular organisms 131567 (`CELLULAR_ROOT`), Bacteria 2 (`DOMAIN`), Pseudomonadati 3379134 (`KINGDOM`), Acidobacteriota 57723 (`PHYLUM`) and environmental samples 57727 (`NO_RANK`). EFetch supplies the five ancestors after root; Datasets also supplies root 1.

NCBI's Environmental samples division does not contradict domain `BACTERIA`, which follows the parent chain. The label's Acidobacteria wording and phylum Acidobacteriota match the authority and need no inferred reconciliation. `SPECIES` is the authority's environmental taxon rank, not a claim of formal nomenclature or a cultured species. A3 remains distinct from similarly named clone concepts; a shared study or sample source does not establish taxon equivalence.

## Evidence

The NCBITAXON source ID, label, count, unit and snapshot note match the own inventory. One `NAME` assertion is not a count of fosmid inserts, genes, cultures or biological abundance. `strain_count: 0` describes BacDive inventory coverage, not universal unculturability.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036853%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned one entry, [JF342590.1](https://www.ncbi.nlm.nih.gov/nuccore/JF342590.1). It explicitly carries `taxon:1036853`, the own organism, `clone: fosmid A3` and an environmental-sample qualifier. Its source is a soil core at 10-50 cm depth from Hancock Agricultural Research Station, Central Sands, Hancock, Wisconsin, USA.

JF342590.1 is a partial fosmid sequence, not a 16S marker, whole-genome assembly or culture-deposit identifier. Declared/actual length is 41,375 nucleotides, alphabet A/C/G/T, SHA-256 `166644dacbe6a555704270e3a0e9f3f55a3f4c105194aa1a8bfde1299b93dc02`. The complete annotation contains 21 CDS and five miscellaneous features; all CDS translation tables are 11. In particular, the beta-ketoacyl-synthase similarity at 18094..24813 is a `misc_feature`, not a translated CDS annotation. A macrolide-specific note on a transporter-related CDS is not a measured antibiotic-resistance phenotype. These annotations are not experimental validation of gene function and are not asserted as taxon-wide functions in the YAML.

GenBank's linked PMID [21539584](https://pubmed.ncbi.nlm.nih.gov/21539584/) and DOI `10.1111/j.1574-6941.2011.01122.x` agree with PubMed. The [primary article](https://academic.oup.com/femsec/article/78/1/176/521179) maps A3 to JF342590, identifies A3 as PCR-positive and describes a predicted hybrid PKS/NRPS region. That interpretation is not a demonstrated compound-production phenotype, and results for A12 or cultured isolates cannot identify A3. The YAML makes none of these functional claims.

Three local native genome candidates are unrelated numeric matches:

- `data/bvbrc/bvbrc-0017.jsonl.gz:34036` is genome `29430.140`, Acinetobacter haemolyticus JS-1us, taxon 29430, assembly `GCA_034047135.1`; it matches through BioProject `PRJNA1036853`.
- `data/catalog/ncbi_genbank-0031.jsonl.gz:37042` is the same assembly with Acinetobacter haemolyticus taxon 29430 and strain text JS-1. Its matching BioProject suffix is not this taxon ID, and the source-specific strain text is not transferred to A3.
- `data/catalog/ncbi_genbank-0065.jsonl.gz:9544` is `GCA_977609215.1`, Candidatus Nitrosopelagicus brevis, an archaeal taxon 1410606. Its genome size alone is `1036853`.

None supplies an own strain or genome link. The [own NCBI genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036853/dataset_report) returned an empty object, which supplies no positive assembly evidence rather than proving universal genome absence. The fosmid itself provides no eligible explicit culture-to-genome chain.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded numeric ID and complete label/slug spelling. All six candidates were read completely: four native JSON rows and two backbone/scope TSV rows. The unrelated catalog rows were resolved using their explicit identity fields.

All five source `SOURCE.json` files were parsed without a target match. A further ignored-inclusive compressed search for JF342590, PMID 21539584 and the exact DOI found no local match in those roots. These negatives concern the inspected snapshots and identifiers, not all external evidence.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. No inspected source establishes an eligible own culture-to-genome link. Optional synonyms, nomenclature, mappings, strain/genome lists, experimental evidence and graphs are appropriately empty for the supported seeded claims. The external fosmid/publication is possible later provenance enrichment, not a required genome link or a defect in this taxonomy-only seed.

`data/taxa/PATHS.tsv:15179` agrees with the filename. `curation/seed_scope.tsv:322880` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external entry. No human-reviewed status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. The environmental taxon identity is source-backed. A fosmid annotation, project-number collision or unrelated genome length does not establish a missing cultured-strain or functional assertion.

## Recommended Edits

None required. Preserve the authority's environmental label/rank and the distinction between fosmid A3, a cultured strain and a genome assembly. Do not promote similarity annotations to experimental phenotypes.

Any later authorized correction belongs in maintained upstream extraction inputs, `src/taxonmech/ncbi_taxdump.py`, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, as appropriate, followed by regeneration. A future clone/publication cross-reference must retain its non-genome type and exact accession provenance. Do not hand-edit this generated YAML.

## Follow-up Checks

No defect-specific repair is needed. Later functional enrichment requires A3-specific primary evidence and independent annotation review. Genome links require explicit eligible culture-deposit chains, not a BioProject's numeric suffix or assembly-size match. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No YAML, source, scope/history entry, generated page, branch, worktree or GitHub item changed. Other study targets and catalog taxa were disambiguation context only; no Eukaryota record was reviewed. No paid research was performed.
