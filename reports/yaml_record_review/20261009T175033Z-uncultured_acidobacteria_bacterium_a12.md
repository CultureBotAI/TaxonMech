# YAML Record Review: uncultured Acidobacteria bacterium A12

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_acidobacteria_bacterium_a12.yaml`
- Started UTC: 2026-10-09T17:47:53Z
- Finished UTC: 2026-10-09T17:50:33Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036855` was read. It denotes uncultured Acidobacteria bacterium A12, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:57727`, genetic code 11, grounding `EXACT`, status `SEEDED`. Its six-entry lineage is accompanied by no synonyms, zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this YAML and no prior own report. Target SHA-256: `ef65c7086f3363bd098d3fa1c93319e5fba39af7af1fd6e58dc75df2d514b56e`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_acidobacteria_bacterium_a12.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_acidobacteria_bacterium_a12.yaml --workers 1 --out /private/tmp/taxonmech-acidobacteria-a12-20261009-validation.tsv`: passed, one file and zero errors; inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed earlier this turn, 17 valid records and zero invalid links; history remained unchanged.
- Own-row comparisons passed for identity, every ancestor, attestation fields, PATHS/scope entries and generated event wording. All three local source candidates were read in full.
- Live NCBI taxonomy, nucleotide and genome responses were inspected. Complete GenBank metadata, feature/source qualifiers and references were read, with protein translations represented by length/SHA-256. Nucleotide length, alphabet, hash and annotated gap bases were checked. No functional or phylogenetic reanalysis is claimed.
- The own GenBank citation agrees with the exact PMID/DOI and PubMed metadata/abstract fetched earlier this turn.
- Not checked: fresh publisher full text and supporting figures. Direct publisher retrieval returned HTTP 403 after web-tool redirect failures earlier this turn. Search snippets are not used as experimental evidence.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and generated-site drift. `just verify-corpus` has no record selector; own-row comparisons are not a substitute.
- Not applicable: curator-added OAK graph and iModulonDB checks. The YAML asserts no graph, gene, regulator, pathway, phenotype or transcriptomic result.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222649` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:32248` agree with the exact ID, label, species rank, parent, code and 2026-09-13 snapshot. Neither supplies an own synonym or retirement.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036855&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036855) agree with the identity and ancestry. The full root-first chain matches the local backbone: root 1 (`NO_RANK`), cellular organisms 131567 (`CELLULAR_ROOT`), Bacteria 2 (`DOMAIN`), Pseudomonadati 3379134 (`KINGDOM`), Acidobacteriota 57723 (`PHYLUM`) and environmental samples 57727 (`NO_RANK`). EFetch supplies the ancestors after root and Datasets includes root 1.

NCBI's Environmental samples division and the bacterial domain are different fields, not conflicting classifications. The organism label's Acidobacteria wording and the Acidobacteriota phylum are both source-supplied. The species rank identifies an environmental taxon; it does not assert validly published nomenclature or a cultured strain. A12 remains distinct from other clone concepts even when their sources or publications coincide.

## Evidence

The source ID, source label, count, `NAME` unit and snapshot note agree with the NCBITAXON inventory. One name assertion is not a count of cultures or genes. `strain_count: 0` describes BacDive coverage, not an experimentally established inability to culture the organism.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036855%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned one entry, [JF342592.1](https://www.ncbi.nlm.nih.gov/nuccore/JF342592.1). It carries the own organism, `taxon:1036855`, `clone: fosmid A12` and an environmental-sample qualifier. Its stated isolation source is a soil core at 10-50 cm depth from Hancock Agricultural Research Station, Central Sands, Hancock, Wisconsin, USA. It is a partial fosmid sequence, not a whole-genome assembly or culture-deposit identifier.

Declared and actual length agree at 31,095 nucleotides, alphabet A/C/G/N/T, SHA-256 `220ab761ddd9b82fed47a1efa9f195dec7e0e635b98151618de9c281f5f46c21`. Complete annotation inspection found 12 CDS, three miscellaneous features and one gap; all CDS use translation table 11. The 100 Ns occur at the annotated gap, 30323..30422. Its `estimated_length: unknown` qualifier means those placeholder bases do not establish the physical gap length.

The MtaD CDS is partial at `complement(<30423..30869)`, protein AEH26534.1, with 149 translated amino acids. The supplied myxothiazol-synthesis note is an annotation, not direct proof that the source organism produces that compound. A nearby ATPase similarity is a miscellaneous feature rather than a translated CDS. The YAML correctly makes no pathway, resistance or compound-production assertion based on these annotations.

The own GenBank entry cites PMID [21539584](https://pubmed.ncbi.nlm.nih.gov/21539584/) and DOI `10.1111/j.1574-6941.2011.01122.x`, matching PubMed's 2011 FEMS Microbiology Ecology 78(1):176-187 article on soil Acidobacteria metagenomic polyketide-synthase pathways. Bibliographic agreement does not transfer every experiment or cultured-isolate result to this taxon; clone-specific functional conclusions were not independently established in this review.

The [own genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036855/dataset_report) returned an empty object, supplying no positive assembly evidence rather than proving universal genome absence. No inspected source provides an eligible explicit culture-deposit-to-genome chain.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded numeric ID and complete label/slug spelling. All three candidates were read completely: one scientific-name JSON row and the backbone/scope TSV rows. All five source `SOURCE.json` files were parsed without a target match. Further ignored-inclusive compressed searches for JF342592, PMID 21539584 and the exact DOI found no local match in these roots. These negatives are bounded to the inspected snapshots and identifiers.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. Empty optional nomenclature, mappings, strain/genome lists, experimental evidence and graphs are appropriate for this taxonomy-only seed. The external clone and article could support later typed provenance enrichment, not a required assembly link.

`data/taxa/PATHS.tsv:15181` agrees with the filename. `curation/seed_scope.tsv:322882` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external entry. No human-reviewed status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. All asserted taxonomy/provenance fields are supported. The gapped fosmid and partial protein annotations are not mislabeled as complete genomes or experimental phenotypes in the YAML.

## Recommended Edits

None required. Preserve the distinction between an environmental taxon, fosmid A12, a culture deposit and an assembly. Do not convert the partial MtaD annotation into a demonstrated biosynthetic phenotype.

Any later authorized correction belongs in maintained extraction inputs, `src/taxonmech/ncbi_taxdump.py`, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, as appropriate, followed by regeneration. Do not hand-edit generated YAML. Future clone/publication enrichment must retain its non-genome type and exact accession provenance.

## Follow-up Checks

No defect-specific repair is needed. Before functional enrichment, inspect the primary article and A12-specific supporting data, including the distinction between clone homology and experiments on cultured isolates. Before adding genome links, establish an explicit eligible culture-deposit chain. Run the documented corpus reproduction, provenance, strict-schema, tests and publication gates before authorized regeneration.

## Additional Notes

This independent report is the only repository write for the target. No YAML, source, scope/history entry, generated page, branch, worktree or GitHub item changed. Other clones were disambiguation context only; no Eukaryota record was reviewed. No paid research was performed.
