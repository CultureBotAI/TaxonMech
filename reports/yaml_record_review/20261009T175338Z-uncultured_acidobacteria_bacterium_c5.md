# YAML Record Review: uncultured Acidobacteria bacterium C5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_acidobacteria_bacterium_c5.yaml`
- Started UTC: 2026-10-09T17:51:40Z
- Finished UTC: 2026-10-09T17:53:38Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036856` was read. It denotes uncultured Acidobacteria bacterium C5, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:57727`, genetic code 11, grounding `EXACT`, status `SEEDED`. It contains six lineage entries, no synonyms, zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this YAML and no prior own report. Target SHA-256: `92422b90757f7eb186ac46f0d8f6444ddab7cdf4e947d99f42b9b901c3e04e3e`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_acidobacteria_bacterium_c5.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_acidobacteria_bacterium_c5.yaml --workers 1 --out /private/tmp/taxonmech-acidobacteria-c5-20261009-validation.tsv`: passed, one file and zero errors; inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed earlier this turn, 17 valid records and zero invalid links; history remained unchanged.
- Own-row comparisons passed for identity, all ancestors, source attestation, PATHS/scope entries and generated event wording. All five local source candidates were read completely.
- Live NCBI taxonomy, exact-taxon nucleotide and genome responses were inspected. Complete GenBank metadata, features/source qualifiers and references were read; protein translations were represented by length/SHA-256. Nucleotide length/alphabet/hash checks passed. No functional or phylogenetic reanalysis is claimed.
- The own GenBank citation matches the exact PMID/DOI and live PubMed metadata/abstract inspected earlier this turn.
- Not checked: fresh primary publisher full text and supporting figures. The same article's web retrieval failed earlier this turn and a direct request returned HTTP 403. Search snippets are not experimental evidence.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and generated-site drift. `just verify-corpus` has no record selector; focused comparisons do not certify reproduction.
- Not applicable: curator-added OAK graph and iModulonDB checks; the YAML asserts no graph, gene, pathway, regulator, phenotype or transcriptomic result.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222650` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:32249` agree with the ID, label, rank, parent, code and 2026-09-13 snapshot. Neither supplies an own synonym or retirement.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036856&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036856) agree with this identity. The six root-first ancestors match the local backbone: root 1 (`NO_RANK`), cellular organisms 131567 (`CELLULAR_ROOT`), Bacteria 2 (`DOMAIN`), Pseudomonadati 3379134 (`KINGDOM`), Acidobacteriota 57723 (`PHYLUM`) and environmental samples 57727 (`NO_RANK`). EFetch supplies the ancestors after root; Datasets includes root 1.

Environmental samples is NCBI's division and the immediate parent label; neither conflicts with the bacterial domain. The organism's Acidobacteria wording and phylum Acidobacteriota are both authority-supplied. Species rank denotes an NCBI environmental taxon, not a formal nomenclatural or cultured-species assertion. A shared study or matching clone abbreviation cannot establish equivalence with another taxon.

## Evidence

The single NCBITAXON name assertion agrees with the own source ID, label, count, `NAME` unit and snapshot note. This is not a count of cultured isolates, genomes or genes. `strain_count: 0` records BacDive inventory coverage rather than universal unculturability.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036856%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned one entry, [JF342593.1](https://www.ncbi.nlm.nih.gov/nuccore/JF342593.1). Its source carries the exact organism, `taxon:1036856`, `clone: fosmid C5` and an environmental-sample qualifier. The stated isolation source is a soil core at 10-50 cm depth from Hancock Agricultural Research Station, Central Sands, Hancock, Wisconsin, USA.

JF342593.1 is a partial fosmid sequence, not a whole-genome assembly or culture-deposit identifier. Declared and actual length agree at 37,660 nucleotides, alphabet A/C/G/T, SHA-256 `f367304ade7b4cbc35133b347aa492f4563e5873345a06ad585b64cdc096e630`. Complete annotation inspection found seven CDS and two miscellaneous features; all CDS use translation table 11. The first CDS is partial and uses `codon_start: 2`; that reading-frame qualifier does not contradict genetic code 11.

Two polyketide-synthase CDS annotations, AEH26538.1 and AEH26539.1, occur at 6441..17237 and 17247..28496. A beta-lactamase-domain similarity at `complement(1777..3111)` is a miscellaneous feature, not a translated CDS or a measured antibiotic-resistance phenotype. These sequence annotations are not experimentally verified taxon-wide functions, and the YAML asserts none of them.

The own sequence cites PMID [21539584](https://pubmed.ncbi.nlm.nih.gov/21539584/) and DOI `10.1111/j.1574-6941.2011.01122.x`. They match PubMed's 2011 FEMS Microbiology Ecology 78(1):176-187 article concerning soil Acidobacteria metagenomic polyketide-synthase pathways. The citation establishes bibliographic provenance, not that every reported cultured-isolate experiment or functional result belongs to C5. No clone-specific PCR outcome or compound-production phenotype is inferred from the abstract.

Two native catalog candidates are unrelated numeric matches:

- `data/catalog/ncbi_genbank-0063.jsonl.gz:16536` is assembly `GCA_964419835.1`, uncultured Candidatus Saccharibacteria bacterium, taxon 179883, isolate SRP192927_co1_1036. Its ungapped genome length, not its taxon ID, is `1036856`.
- `data/catalog/gtdb_genomes-0003.jsonl.gz:6759` is the same assembly, `GB_GCA_964419835.1`, with explicit NCBI taxon 179883 and the same ungapped length. Its GTDB species is CAYQPT01 sp964419835, not the reviewed environmental taxon.

Neither provides a C5 mapping, strain or genome link. The [own genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036856/dataset_report) returned an empty object, supplying no positive assembly evidence rather than proving universal genome absence. No inspected source establishes an eligible explicit culture-deposit-to-genome chain.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded numeric ID and complete label/slug spelling. All five candidates were read in full: three native JSON rows and two backbone/scope TSV rows. Explicit catalog identity fields resolved the numeric false matches.

All five source `SOURCE.json` files were parsed without a target match. Further ignored-inclusive compressed searches for JF342593, PMID 21539584 and the exact DOI found no local match in those roots. These negatives concern the inspected snapshots and identifiers, not all external evidence.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. Optional synonyms, nomenclature, mappings, strain/genome lists, experimental evidence and graphs are appropriately empty for this supported taxonomy seed. The external fosmid/publication is potential later typed provenance enrichment, not a required whole-genome link.

`data/taxa/PATHS.tsv:15182` agrees with the filename. `curation/seed_scope.tsv:322883` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external entry. Human-reviewed status is not asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. All asserted taxonomy/provenance fields are supported. Unrelated genome-length matches do not establish omitted mappings, and a domain-similarity annotation does not establish a missing resistance phenotype.

## Recommended Edits

None required. Preserve the distinction between the environmental taxon, fosmid C5, a culture deposit and a genome assembly. Do not join on an unrelated numerical measurement or promote sequence annotations into measured phenotypes.

Any later authorized correction belongs in maintained extraction inputs, `src/taxonmech/ncbi_taxdump.py`, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, as appropriate, followed by regeneration. Do not hand-edit generated YAML. A future clone/publication cross-reference must retain its non-genome type and exact accession provenance.

## Follow-up Checks

No defect-specific repair is needed. Inspect C5-specific primary experimental evidence and supporting figures before functional enrichment. Genome links require an explicit eligible culture-deposit chain, not a genome-size match. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No YAML, source, scope/history entry, generated page, branch, worktree or GitHub item changed. Other study targets and catalog taxa were disambiguation context only; no Eukaryota record was reviewed. No paid research was performed.
