# YAML Record Review: Stenotrophomonas sp. bC64(2011)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/stenotrophomonas_sp_bc64_2011.yaml`
- Started UTC: 2026-10-05T17:53:08Z
- Finished UTC: 2026-10-05T17:55:48Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes
`NCBITaxon:1034555`, Stenotrophomonas sp. bC64(2011), with species
rank, `BACTERIA`, parent `NCBITaxon:196198`, genetic code 11,
`EXACT` grounding, `SEEDED` status, and `strain_count: 0`.
It is neither a culture deposit nor a genome.

Owning inputs are `data/raw/ncbitaxon_taxa.tsv:221664` and
`curation/seed_scope.tsv:321975`; `data/taxa/PATHS.tsv:14130`
agrees with the identifier and slug. No generated YAML was edited.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/stenotrophomonas_sp_bc64_2011.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/stenotrophomonas_sp_bc64_2011.yaml --out /private/tmp/sbc64-strict-20261005.tsv`: exit 0; one file, zero files with errors and zero error rows.
- Structured checks read the complete backbone row, all ten ancestors, PATHS, scope, attestation, and seed event. Exact-ID checks covered seven raw source inventories, type material, merged IDs, and dropped records.
- `rg --no-ignore --hidden -n -z -i` searched the numeric ID, full label, slug, and BC64 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All 14 matches were read in full with TSV headers or JSON decoding and reconciled with search addresses: four raw/scope, two name, five assembly, and three GTDB rows.
- A separate marker search across those roots returned no JF772543 rows. Ignored-inclusive filename and content searches under `reports` and `history` for ID, full label, slug, and marker found no prior target report or separate history artifact before this report.
- Live NCBI Taxonomy EFetch/Datasets, exact nonexpanded Assembly/Nuccore searches, complete marker metadata, and bounded PubMed queries completed. Primary identity text was read for the literature and plasmid collisions described below.
- Not checked: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused agreement is not corpus reproduction; `--max-diffs` is not a one-record scope option.
- iModulonDB and the curator-added graph ID/label gate were not applicable: the record makes no gene, regulator, protein, phenotype, transcriptomic, or causal-graph assertion. No separate applicable focused term/reference validator was available beyond the schema and authority checks performed.

## Identity and Grounding

NCBI EFetch agrees on exact label, species rank, parent 196198, Bacteria
division, and genetic code 11. Datasets confirms all ten root-first
ancestor IDs:
`1 > 131567 > 2 > 3379134 > 1224 > 1236 > 135614 > 32033 > 40323 > 196198`.
Labels and ranks agree for root, cellular organisms, Bacteria,
Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Lysobacterales,
Lysobacteraceae, Stenotrophomonas, and unclassified Stenotrophomonas.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034555);
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034555).

The pinned backbone has empty synonym/retirement fields and no direct
children. Exact type-material, merged-ID, and dropped scans found no
target rows. The scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31052`.
A provisional NCBI species rank is not valid nomenclatural publication;
`EXACT` grounds the taxon identifier, not genomic species equivalence.

## Evidence

The sole NCBITAXON attestation agrees in ID, label, count 1, unit
`NAME`, and snapshot 2026-09-13. The count is not a strain or genome
count. The 2026-09-13T17:54:04Z seed event, curator
`seed_from_sources`, action `SEEDED_FROM_SOURCES`, and scope text
agree with the inputs.

The exact query `txid1034555[Organism:noexp]` returned no Assembly
items with missing-phrase/no-items diagnostics and one Nuccore item,
UID 333981237. Complete metadata, references, and source/rRNA features
identify `JF772543.1`, a 1,450-base partial 16S rRNA sequence, strain
bC64, taxon 1034555, isolation source rhizosphere. Huang J.'s direct
submission is dated 1 April 2011. The weathering-related reference is
unpublished; its title and the submitter address do not prove a measured
weathering trait, host plant, isolation locality, or culture deposit.
The marker is not a whole-genome accession.
[GenBank JF772543.1](https://www.ncbi.nlm.nih.gov/nuccore/JF772543.1).

The 14 native rows exclude these other identities:

- Bacillus cereus group sp. BC64 is taxon 3445279, parent 2750818, in `data/raw/ncbitaxon_taxa.tsv:633693`, `curation/seed_scope.tsv:134170`, and `data/catalog/ncbi_names-0015.jsonl.gz:13551`. Identical latest contig assemblies `GCA_051782225.1`/`GCF_051782225.1` have 79 contigs, sample `SAMN48908380`, WGS `JBPWKV000000000.1`, GenBank project `PRJNA1272304`, and RefSeq project `PRJNA224116`. Full assembly rows are `data/catalog/ncbi_genbank-0047.jsonl.gz:40494` and `data/catalog/ncbi_refseq-0007.jsonl.gz:40044`. Nonrepresentative GTDB `RS_GCF_051782225.1` names Bacillus_A anthracis under Bacillaceae_G, while its NCBI fields retain Bacillus cereus group sp. BC64/Bacillaceae (`data/catalog/gtdb_genomes-0004.jsonl.gz:40985`). This classification difference is preserved without reconciling it or transferring it to Stenotrophomonas.
- Bacillus mobilis BC64 is taxon 2026190. Identical latest contig assemblies `GCA_057589115.1`/`GCF_057589115.1` have 74 contigs, sample `SAMN54318582`, WGS `JBYDJV000000000.1`, GenBank project `PRJNA1394226`, and RefSeq project `PRJNA224116`. Full rows are `data/catalog/ncbi_genbank-0053.jsonl.gz:12621` and `data/catalog/ncbi_refseq-0008.jsonl.gz:43162`. The sample and genome are distinct from the preceding Bacillus BC64 chain as well as from the target.
- The UUID `47fa77e8-325c-4f7d-bc64-5822249aad55` is the isolate designation of Terriglobia bacterium, taxon 2081523, not the strain bC64. Its latest contig assembly `GCA_965238295.1` uses sample `SAMEA117789109`, project `PRJEB86565`, and WGS `CBDEHL000000000.1`; no RefSeq pair is supplied and exclusions are metagenome-derived/genus undefined. Nonrepresentative GTDB `GB_GCA_965238295.1` is JAJEDW01 sp965262675 under Acidobacteriota/Terriglobia. Full rows: `data/catalog/ncbi_genbank-0064.jsonl.gz:10951` and `data/catalog/gtdb_genomes-0007.jsonl.gz:20801`. A UUID substring is not an isolate alias.
- Number 1034555 is the contig N50, not taxon ID, in the full GTDB row `data/catalog/gtdb_genomes-0005.jsonl.gz:49684`. That row is nonrepresentative `RS_GCF_002532375.1`, explicit GenBank accession `GCA_002532375.1`, Cronobacter sakazakii MOD1_KW1, taxon 28141, sample `SAMN07205645`, project `PRJNA224116`, and WGS `NITI00000000.1`. Its scaffold-level assembly metric does not provide target identity evidence.

Schmid et al. 2021, DOI 10.3389/fmicb.2021.698974, studies Bacillus
cereus-group packaging isolates. The inspected primary Results and
Figure 2 caption explicitly include BC64 in that Bacillus isolate set.
This is an identity exclusion, not evidence for target packaging
association or toxicity; the study's phenotype results were not imported.
[Frontiers, Results and Figure 2 caption](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.698974/full).

Coburn et al. 2023, DOI 10.3389/fcimb.2023.1304677, uses Bc64 for a
Bacillus cereus ocular isolate. Its primary strain-source section and
complete Table 1, including headers and source-abbreviation footnotes,
were read. The Bc64 row is PTE with source COML, defined as the Campbell
Ophthalmic Microbiology Laboratory. Neither that clinical isolate nor
its gene-profile assertions establish a bridge to Stenotrophomonas
JF772543.1. No disease or virulence claim was transferred.
[Frontiers, section 2.1 and Table 1](https://www.frontiersin.org/journals/cellular-and-infection-microbiology/articles/10.3389/fcimb.2023.1304677/full).

Addgene 202905 is explicitly Salsa-BC64-P1F4, a barcoded reporter plasmid
with synthetic EGFP/BC64 insert, not a taxon or culture deposit. The
primary catalog's identity, purpose, backbone, and insert fields were
read; a BC64 barcode does not denote target bC64.
[Addgene 202905](https://www.addgene.org/202905/).

## Completeness

Exact-ID scans found no target rows in raw BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin, or BactoTraits inventories. The ignored-inclusive native
searches supplied no supported target culture-deposit, assembly, BV-BRC,
GOLD, SeqCode, StrainInfo, or ATB chain. These are bounded source/search
negatives, not proof that no external evidence exists.

Empty optional synonyms, nomenclature, mappings, strains, genomes, and
graph are not demonstrated omissions. `strain_count: 0` counts
represented inventory strains, not the absence of a sequenced isolate.
A marker alone does not establish an eligible culture-deposit association.

PubMed returned zero results for JF772543, bC64 with Stenotrophomonas,
and the exact unpublished title, with missing-phrase/no-items diagnostics.
Exact-marker web searches returned no results. Broader short-name leads
required the exclusions above; they did not provide an inspected target
identity bridge. This was not a complete literature census.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Retained identity, lineage, attestation, inventory count,
source status, and seed history are supported within the reviewed scope.

## Recommended Edits

None. Leave the generated YAML, `SEEDED` status, and history unchanged.
Do not attach Bacillus genomes or literature, UUID matches, numeric
assembly metrics, or barcode plasmids to the target.

Future verified enrichment belongs in maintained source inputs and
extraction through `scripts/extract_source_inventory.py` and
`src/taxonmech/extract.py`. Representation changes belong in
`scripts/seed_from_sources.py`; scope changes belong in
`curation/seed_scope.tsv`. Preserve accession versions, source-specific
classifications, and distinct strain/sample/genome identifiers.

## Follow-up Checks

After a separately authorized upstream change, repeat focused schema
and strict checks, inspect the full generated record and its evidence,
then run full corpus reproduction and QC. Any proposed genome
association must resolve at its authority and show an explicit
strain/deposit/sample/assembly chain.

## Additional Notes

The existing review branch and HEAD
`b6a6508faca1388b88feb5740b1095e9f64cfdb8` remained unchanged.

The PMC readers for the packaging and baby-wipe leads returned browser
challenges. The packaging paper was inspected at Frontiers instead.
The separate baby-wipe paper, DOI 10.3390/microorganisms10091779,
also failed at its MDPI reader and was not used as primary full-text
evidence; that failed access is not an absence finding. No claim of
visually inspecting the Frontiers figures is made: the relevant caption,
identity text, and HTML table were the inspected evidence.

No Eukaryota YAML was reopened. Only this new report was added for the
record; taxon YAMLs, source inventories, generators, scope, statuses,
history, site products, and GitHub were not modified.
