# YAML Record Review: Pseudomonas sp. IAB15

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_iab15.yaml`
- Started UTC: 2026-10-07T08:19:36Z
- Finished UTC: 2026-10-07T08:22:19Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035623`, Pseudomonas sp. IAB15, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`, ten root-first ancestors and genetic code 11. It carries `EXACT` grounding, `SEEDED` mapping status, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, culture deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graphs are asserted. IAB15 is an isolate designation, not a verified culture accession. Generated YAML is read-only. Maintained source/extraction inputs and `src/taxonmech/seed.py` own future fixes, with scope and slug ownership in `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudomonas_sp_iab15.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_iab15.yaml --out /private/tmp/iab15-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/iab15-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, complete lineage, seven source inventories, path, scope and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and complete ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not prove byte-for-byte corpus reproduction.

`just validate-products` was not run: configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded. There are no literature/internal evidence references in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content/path searches found no target history artifact; none is created here.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222151` agrees on ID, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31631` agrees. Unique path and scope rows are `data/taxa/PATHS.tsv:14651` and `curation/seed_scope.tsv:322418`.

All ten ancestors match the committed parent chain in identifier, label, rank and order. Live EFetch confirms species rank, parent 196821, code 11, no alternate names and nine non-root ancestors; Datasets confirms the same chain including root. Gammaproteobacteria/Pseudomonadales/Pseudomonadaceae/Pseudomonas and the unclassified Pseudomonas parent agree. No retirement or replacement was found in the inspected lifecycle sources. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035623&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035623)

`EXACT` grounds this NCBI concept, not a validly published species binomial, strain-deposit equivalence or a new identification inferred from a marker.

## Evidence

The sole `NCBITAXON` attestation agrees on exact ID and label, count 1, unit `NAME` and snapshot note. It is not a count of strains or genomes. The complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore UID 333952301 resolves to `JF799928.1`, a 1,404-nt partial 16S rRNA marker. Complete GenBank metadata explicitly identifies Pseudomonas sp. IAB15, strain IAB15 and `taxon:1035623`. Its source is the active layer in permafrost, with a China/Qinghai-Tibet locality. The rRNA feature is partial at both ends. No culture-collection, BioSample, BioProject or assembly link is supplied. The metadata were read completely, excluding only sequence strings and translation/transcription payloads. [GenBank JF799928.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799928.1)

The marker cites an unpublished study of bacterial diversity in active-layer permafrost along the Qinghai-Tibet highway and a direct submission by Li, Xu and Zhang. Submission was 11 April 2011; creation/update were 30 May 2011. No DOI or PMID is linked. This is submission provenance, not independent published species confirmation. Locality and genus do not establish cold-growth or other phenotypes. The marker is not a genome.

Thirty-three additional catalog hits were read completely and excluded as numeric-field or identifier-substring collisions:

- Eight Thermus thermophilus N-1 rows: `data/bvbrc/bvbrc-0015.jsonl.gz`, lines 20072, 20079, 20086, 20093 and 20100; `data/catalog/ncbi_genbank-0018.jsonl.gz:13855`; `data/catalog/ncbi_refseq-0003.jsonl.gz:39802`; `data/catalog/gtdb_genomes-0014.jsonl.gz:47420`. These have taxid 274, sample SAMN21035623 and GCA_019884805.1/GCF_019884805.1. BV-BRC 274.49 is Complete; 274.56, 274.68, 274.75 and 274.82 are Deprecated. Sample digits do not identify IAB15.
- Two GOLD project rows: `data/gold/projects.jsonl.gz`, lines 267475 and 267476, Salmonella enterica PNUSAS059640/PNUSAS059638, projects Gp0379896/Gp0379897, organisms Go0495842/Go0495843, samples SAMN10356233/SAMN10356235.
- Six BV-BRC Salmonella rows: `data/bvbrc/bvbrc-0017.jsonl.gz`, lines 10749, 10772, 10806, 10871, 11184 and 11216, genomes 28901.5288, 28901.5311, 28901.5345, 28901.5410, 28901.5724 and 28901.5756, all taxid 28901.
- Six NCBI Salmonella rows: `data/catalog/ncbi_genbank-0002.jsonl.gz`, lines 48244, 48277, 48327, 48421, 48922 and 48963. Assemblies GCA_003758355.1, GCA_003759025.1, GCA_003760025.1, GCA_003761905.1, GCA_003772065.1 and GCA_003772885.1 all have taxid/species_taxid 28901. Samples SAMN10356230 through SAMN10356235 explain these and the preceding Salmonella matches.
- One GOLD analysis row: `data/gold/analyses.jsonl.gz:459326`, Ga0699210, Bacteroidales bacterium 3300072073_s21, organism Go0725129, IMG identifier 8151035623. It is a metagenome-assembled-genome analysis with an empty GenBank list; IMG digits are not an NCBI taxid.
- One GTDB row: `data/catalog/gtdb_genomes-0016.jsonl.gz:33833`, RS_GCF_048500235.1, Candidatus Kuenenia sp. AMX1, NCBI taxid/species_taxid 2499824. `ncbi_contig_n50: 1035623` explains the match; GTDB classifies it as Kuenenia stuttgartiensis_A, not Pseudomonas.
- Two E. coli rows: `data/catalog/ncbi_refseq-0009.jsonl.gz:2088` and `data/catalog/ncbi_genbank-0054.jsonl.gz:28409`, GCF_058934645.1/GCA_058934645.1, isolate B19-2, taxid/species_taxid 562, sample SAMN61035623.
- Seven ATB rows in `data/catalog/allthebacteria.tsv.xz`: line 66268 is Staphylococcus aureus, SAMEA1035623, ERZ3070807, ERR083854, with META_FAIL assembly/HQ filters; lines 1503867 through 1503872 are six Salmonella enterica samples SAMN10356230 through SAMN10356235, with ENA analyses ERZ9093346, ERZ9093350, ERZ9093351, ERZ9093352, ERZ9093360 and ERZ9093353.

Source-declared GCA/GCF pairing and shared sample relationships among these unrelated rows remain confined to their own organisms. No IAB15 culture-deposit/genome chain is supplied. NCBI/GTDB classification differences on the unrelated Thermus and Kuenenia genomes were not reconciled or imported.

No gene, regulator, pathway, stress-response or transcriptomics assertion in this YAML requires an iModulonDB lookup. The adapter is not applicable; its absence is not negative biological evidence.

## Completeness

Zero BacDive strains and the optional omissions agree with inspected source scope. A marker's strain qualifier is not a culture deposit. Record-level literature evidence is optional for seeded records. No required gap was found.

Both local search stages included ignored/hidden files and compressed catalogs with `rg --no-ignore --hidden -n -z -i`. Roots were `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full per stage; history filenames were independently traversed.

The identity stage searched taxid 1035623, exact label, slug and IAB15 with case/separator variants. Thirty-six lines matched: backbone, scope, native name and the 33 incidental catalog hits; all were read completely. The accession stage searched JF799928 with optional .1 and found no lines. Neither stage found matching source-metadata values or history paths. These negative findings include ignored files and are bounded to the specified roots and terms.

Web searches used Pseudomonas with IAB15 and JF799928. A broader taxonomy-browser result was only a search lead; the accession search returned no results. No inspected exact-target publication or supported culture-deposit/genome chain was established. The exact-taxid Assembly zero carries a phrase-not-found warning and does not exclude assemblies filed under another identity. Exhaustive literature retrieval and sequence similarity were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, complete lineage, source provenance, zero strain count and seed history agree. Numeric coincidences do not justify genome or strain links.

## Recommended Edits

None required. Do not patch generated YAML, match taxids to sample/IMG substrings or assembly statistics, count JF799928.1 as a genome, infer genus-wide phenotypes, or promote `SEEDED` to `REVIEWED`.

A later authorized taxonomy-source refresh belongs in `conf/ncbi_taxdump.yaml` and `scripts/extract_source_inventory.py`, followed by guarded seeding. Optional literature annotations require maintained-input support merged by `src/taxonmech/seed.py` with tests under `docs/CURATION.md`. Habitat and phenotype assertions belong in the corresponding sibling corpora with claim-specific evidence.

## Follow-up Checks

- Require an exact culture-deposit and genome-source chain before adding strain/genome identifiers.
- Keep marker accessions, assembly statistics and each database's whole identifier fields distinct; preserve deprecated-source statuses without transferring their links.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`; validate any new history artifact. Full-corpus gates remain skipped here.

## Additional Notes

Primary NCBI taxonomy, Datasets, sequence-index and nucleotide reads succeeded. The target's own assertions were checked independently of nearby records from the same submission series.

Seed wording agrees with scope and attestation. Timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date. All three timestamps and the selection code were inspected.

The entire target was reread unchanged before report creation. An ignored-independent filename search found no previous report for this stem. Only this new repository report is added for this review; no record, inventory, page, old report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
