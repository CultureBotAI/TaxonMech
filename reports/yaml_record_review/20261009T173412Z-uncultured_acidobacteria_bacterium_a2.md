# YAML Record Review: uncultured Acidobacteria bacterium A2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_acidobacteria_bacterium_a2.yaml`
- Started UTC: 2026-10-09T17:30:18Z
- Finished UTC: 2026-10-09T17:34:12Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036852` was read. It denotes uncultured Acidobacteria bacterium A2, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:57727` (environmental samples under Acidobacteriota), code 11, grounding `EXACT`, status `SEEDED`. It contains no synonyms, zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this YAML and no prior own report. Target SHA-256: `254037ffa551f03ad7ded3d2f35eb34f839a233f44dfe8e6c768c7228b572826`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_acidobacteria_bacterium_a2.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_acidobacteria_bacterium_a2.yaml --workers 1 --out /private/tmp/taxonmech-acidobacteria-a2-20261009-validation.tsv`: passed, one file and zero errors; inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed earlier this turn, 17 valid records and zero invalid links; history was unchanged.
- Own-row comparisons passed for identity, every ancestor, source attestation, PATHS/scope entries and event wording. All three local source candidates were read in full.
- Live NCBI taxonomy and exact-taxon nucleotide/genome responses were inspected. Complete GenBank metadata, source qualifiers, feature annotations and references were read. An initially truncated display was recovered with an annotation-preserving read that represented protein translations by length/SHA-256. Nucleotide length/alphabet/hash checks passed; no alignment, protein-function validation or phylogenetic reanalysis is claimed.
- GenBank's PMID/DOI were cross-checked against PubMed metadata/abstract and the primary publisher article's relevant methods/results. The direct DOI web open failed and the PubMed browser page presented a challenge; public NCBI EFetch and the publisher's accessible article supplied the evidence instead.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift. `just verify-corpus` has no record selector; focused comparisons do not certify corpus reproduction.
- Not applicable: curator-added OAK graph and iModulonDB checks; the YAML itself asserts no graph, gene, regulator, pathway, trait or transcriptomic result.
- Not checked: supplementary figure S1 or experimental revalidation of predicted protein functions. The report makes no gene-level functional or compound-production finding from those uninspected materials.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222646` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:32245` agree with the exact ID, label, species rank, parent, code and 2026-09-13 snapshot. No own synonym or retirement is supplied.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036852&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036852) agree with the identity. All six root-first lineage entries match the local backbone: root 1 (`NO_RANK`), cellular organisms 131567 (`CELLULAR_ROOT`), Bacteria 2 (`DOMAIN`), Pseudomonadati 3379134 (`KINGDOM`), Acidobacteriota 57723 (`PHYLUM`) and environmental samples 57727 (`NO_RANK`). EFetch supplies the five ancestors after root; Datasets also supplies root 1.

The source's Environmental samples division is not a contradiction of domain `BACTERIA`: its parent chain explicitly includes Bacteria. The label retains Acidobacteria while the current phylum is Acidobacteriota, exactly as NCBI supplies them. No inferred nomenclatural update is needed. `SPECIES` is the authority's rank for this environmental taxon concept, not a claim of a formally named, cultured species.

## Evidence

The NCBITAXON source ID, label, count, unit and snapshot note match the own inventory. One `NAME` assertion is not a count of sequences, fosmid inserts, genes or biological abundance. `strain_count: 0` describes BacDive inventory coverage, not proof that the organism is universally unculturable.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036852%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned one entry, [JF342589.1](https://www.ncbi.nlm.nih.gov/nuccore/JF342589.1). Its source explicitly carries `taxon:1036852`, the own organism name, `clone: fosmid A2` and an environmental-sample qualifier. The source is a soil core at 10-50 cm depth from Hancock Agricultural Research Station, Central Sands, Hancock, Wisconsin, USA.

JF342589.1 is a partial fosmid sequence, not a 16S marker, whole-genome assembly or culture-deposit identifier. Its declared and actual lengths are 39,771 nucleotides, alphabet A/C/G/T, SHA-256 `58ae61f8c5d6414f4abfd77c0541140d755981bd0b216f981e61cc3a7eb459e8`. The inspected annotation contains 23 CDS and two miscellaneous features; all CDS translation tables are 11. Named products include fatty-acid-related enzymes and multiple hypothetical proteins. These source annotations are not experimental validation of those activities and are not asserted as taxon-wide functions in the YAML.

GenBank links the sequence to [Parsley et al., FEMS Microbiology Ecology 78:176-187 (2011)](https://academic.oup.com/femsec/article/78/1/176/521179), PMID [21539584](https://pubmed.ncbi.nlm.nih.gov/21539584/), DOI `10.1111/j.1574-6941.2011.01122.x`; these identifiers and the title agree with PubMed. The publisher's insert-sequencing methods explicitly map A2 to JF342589. Its results identify A2 as PCR-negative in the KS-screening context and point to supplemental S1 for predicted ORFs. The detailed MtaD analysis concerns A12 and separately screened cultured isolates, not A2. Those findings must not be transferred to A2, nor does the paper's title establish antibiotic or polyketide production by this taxon. The accession mapping supports the environmental-clone provenance, not a culture identity or proven metabolic phenotype.

The [own NCBI genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036852/dataset_report) returned an empty object. It supplies no positive assembly evidence rather than proving universal genome absence. The fosmid sequence provides no eligible explicit culture-to-genome chain.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded numeric ID and complete label/slug spelling. All three candidates were read in full: the native name JSON row and two backbone/scope TSV rows.

All five source `SOURCE.json` files were parsed without a target match. A further ignored-inclusive compressed search for JF342589, PMID 21539584 and the exact DOI found no local match in those roots. These negatives concern the inspected snapshots and identifiers, not all external evidence.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. No inspected source establishes an eligible own culture-to-genome link. Optional synonyms, nomenclature, mappings, strain/genome lists, experimental evidence and graphs are appropriately empty for the supported seeded claims. The external fosmid/publication is a possible later provenance enrichment, not a required genome link or a defect in this taxonomy-only seed.

`data/taxa/PATHS.tsv:15178` agrees with the filename. `curation/seed_scope.tsv:322879` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external entry. No human-reviewed status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. The environmental taxon identity is source-backed; neither the fosmid accession nor the study's other clones and isolates establish a missing cultured-strain or functional assertion.

## Recommended Edits

None required. Preserve the authority's environmental taxon label/rank and distinguish fosmid A2 from a cultured strain, a genome assembly and the paper's other targets.

Any later authorized correction belongs in maintained upstream extraction inputs, `src/taxonmech/ncbi_taxdump.py`, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, as appropriate, followed by regeneration. A future clone/publication cross-reference must retain its non-genome type and exact accession provenance. Do not hand-edit this generated YAML.

## Follow-up Checks

No defect-specific repair is needed. Any later functional enrichment requires inspection of the A2-specific supplementary annotations and primary experimental evidence, without transferring A12 or cultured-isolate results. Genome links require explicit eligible culture-deposit chains. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No YAML, source, scope/history entry, generated page, branch, worktree or GitHub item changed. Other study targets were disambiguation context only; no Eukaryota record was reviewed. No paid research was performed.
