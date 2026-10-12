# YAML Record Review: Stenotrophomonas sp. bB9(2011)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/stenotrophomonas_sp_bb9_2011.yaml`
- Started UTC: 2026-10-05T17:47:44Z
- Finished UTC: 2026-10-05T17:51:12Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes
`NCBITaxon:1034554`, Stenotrophomonas sp. bB9(2011), with species rank,
`BACTERIA`, parent `NCBITaxon:196198`, genetic code 11, `EXACT`
grounding, `SEEDED` status, and `strain_count: 0`. It is not a
culture deposit, genome, or all organisms designated BB9.

Inputs are `data/raw/ncbitaxon_taxa.tsv:221663` and
`curation/seed_scope.tsv:321974`; PATHS line 14129 agrees with the slug.
No generated record was changed.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/stenotrophomonas_sp_bb9_2011.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/stenotrophomonas_sp_bb9_2011.yaml --out /private/tmp/sbb9-strict-20261005.tsv`: exit 0; one file, zero files with errors, zero error rows.
- Structured checks read the backbone, all ten ancestors, PATHS, scope, attestation, and seed event. Exact-ID scans covered seven raw source inventories, type material, merged IDs, and dropped records.
- `rg --no-ignore --hidden -n -z -i` searched ID, full label, slug, and BB9 separator variants in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All 55 matches were read as complete native rows and reconciled with search addresses: 16 raw/scope, nine GOLD, three BV-BRC, eight NCBI names, fifteen assembly, three GTDB, and one ATB.
- A separate marker search across those roots returned no JF772542 rows. Ignored-inclusive report/history filename and content searches for target ID, label, slug, and marker found no prior target report or separate history artifact before this report.
- Live NCBI EFetch/Datasets, exact Assembly/Nuccore searches, complete marker metadata, and bounded PubMed queries completed. Relevant primary literature identity text and tables were inspected.
- Not checked: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused source agreement is not corpus reproduction; `--max-diffs` is not a one-record scope option.
- iModulonDB and the curator-added graph ID/label gate were not applicable: the record asserts no genes, regulators, proteins, phenotypes, transcriptomics, or causal graphs. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

NCBI EFetch agrees on exact name, species rank, parent 196198, Bacteria
division, and genetic code 11. Datasets confirms the complete root-first chain:
`1 > 131567 > 2 > 3379134 > 1224 > 1236 > 135614 > 32033 > 40323 > 196198`.
Labels and ranks agree for root, cellular organisms, Bacteria,
Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Lysobacterales,
Lysobacteraceae, Stenotrophomonas, and unclassified Stenotrophomonas.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034554);
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034554).

The backbone has empty synonym and retirement fields and no direct children.
Exact type-material, merged-ID, and dropped checks found no target rows.
The full native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31051`.
The provisional species rank is not nomenclatural publication;
`EXACT` denotes identifier grounding, not genome-delimited equivalence.

## Evidence

The sole NCBITAXON attestation agrees in ID, label, count 1, unit
`NAME`, and snapshot 2026-09-13. This is a source-name count, not a
strain or genome count. The embedded seed event at
2026-09-13T17:54:04Z, curator `seed_from_sources`, action
`SEEDED_FROM_SOURCES`, and scope text agree with the inputs.

The exact query `txid1034554[Organism:noexp]` returned no Assembly items
with missing-phrase/no-items diagnostics and one Nuccore item, UID
333981236. Full metadata, references, and source/rRNA features identify
`JF772542.1`, a 1,512-base partial 16S rRNA sequence, strain bB9,
taxon 1034554, isolation source rhizosphere. Huang J.'s direct submission
is dated 1 April 2011. Its weathering-related reference is unpublished;
neither its title nor the submitter address proves a measured weathering
trait, host plant, locality, or culture deposit. The marker is not a genome.
[GenBank JF772542.1](https://www.ncbi.nlm.nih.gov/nuccore/JF772542.1).

Native short-name matches were excluded as follows:

- Seven other scientific-name/backbone/scope chains identify Halomonas sp. BB9 (888333), Lactobacillus sp. BB9 (1264892), Comamonas sp. BB9 (1317671), Bacillus sp. OUCC BB9(1) (1674070), Bacillus sp. OUCC BB9(2) (1674071), Campylobacter sp. JWC-BB9 (2512010), and Ruegeria sp. BB9 (3437555). Their backbone lines are 189118, 293257, 313792, 436747, 436748, 528813, and 632648. Each has its own parent, source name, and scope row; none is an alias for target 1034554. The two OUCC suffixes remain distinct.
- ATB's Campylobacter sp. JWC-BB9 row at `data/catalog/allthebacteria.tsv.xz:1543709` supplies `ERZ25535722`, sample `SAMN10869150`, run `SRR8526916`, available FASTA, PASS assembly/HQ/Sylph filters, and Campylobacter_D jejuni classification. Its SeqKit sum and download/archive fields were read; none creates a target identity link. A separate Campylobacter jejuni JWC-BB9 assembly, taxon 197, is latest contig `GCA_019297915.1`, sample `SAMN20331737`, project `PRJNA327813`, WGS `ABBKJC000000000.1`, with no RefSeq pair and a large-multi-isolate-project exclusion (`data/catalog/ncbi_genbank-0017.jsonl.gz:35369`). The different BioSamples prohibit inferring assembly equivalence from the shared strain label.
- Ruegeria sp. BB9, taxon 3437555, has identical latest contig assemblies `GCA_056539345.1`/`GCF_056539345.1`, sample `SAMN48980581`, WGS `JBQFUU000000000.1`, GenBank project `PRJNA1264799`, and RefSeq project `PRJNA224116`. Full rows: `data/catalog/ncbi_genbank-0052.jsonl.gz:13558` and `data/catalog/ncbi_refseq-0008.jsonl.gz:32444`.
- Staphylococcus aureus UKST63/485, isolate BB9, taxon 1280, has identical latest contig `GCA_001351355.1`/`GCF_001351355.1`, sample `SAMEA1569626`, WGS `CVGX00000000.1`, GenBank project `PRJEB2812`, and RefSeq project `PRJNA224116`. GOLD `Go0501954`/`Gp0386180`/`Ga0363985` follows this organism/project/assembly chain; the analysis's organism-ID field is empty but the project link is explicit. Nonrepresentative GTDB `RS_GCF_001351355.1` retains Staphylococcales separately from NCBI Bacillales. Full rows include `data/catalog/ncbi_genbank-0001.jsonl.gz:1145`, `data/catalog/ncbi_refseq-0000.jsonl.gz:43096`, and `data/gold/projects.jsonl.gz:273654`. Another S. aureus isolate, BB9-I1-E1, is latest contig `GCA_026835715.1`, `SAMN17577097`, `PRJNA514245`, `DAKXDG000000000.1`, with no RefSeq pair and a large-multi-isolate-project exclusion (`data/catalog/ncbi_genbank-0024.jsonl.gz:45936`). These isolate/sample chains are not interchangeable.
- Brucella melitensis bv. 1 BB9 is taxon 644337, species taxon 29459: identical latest contig `GCA_003993855.1`/`GCF_003993855.1`, `SAMN03381105`, `JZHE00000000.1`, GenBank project `PRJNA266058`, RefSeq project `PRJNA224116`. BV-BRC `644337.8`, GOLD `Go0546015`/`Gp0496950`/`Ga0445891`, IMG `2978314846`, and nonrepresentative GTDB `RS_GCF_003993855.1` all concern that foreign identity. GOLD analysis-to-project linkage is explicit despite an empty analysis organism-ID field. GTDB Rhizobiales/Rhizobiaceae and NCBI Hyphomicrobiales/Brucellaceae remain source-specific. Full rows include `data/catalog/ncbi_genbank-0003.jsonl.gz:7409`, `data/catalog/ncbi_refseq-0002.jsonl.gz:10274`, `data/bvbrc/bvbrc-0026.jsonl.gz:6909`, and `data/gold/projects.jsonl.gz:357042`.
- Sulfurovum sp. BB9, taxon 1969726, has identical latest scaffold `GCA_016744875.1`/`GCF_016744875.1`, `SAMN16086335`, `JADGDL000000000.1`, GenBank project `PRJNA606180`, RefSeq project `PRJNA224116`, and a metagenome-derived flag. It has 159 contigs in 137 scaffolds. BV-BRC `1969726.39` explicitly names the GenBank assembly; representative GTDB `RS_GCF_016744875.1` is Sulfurovum sp016744875, with GTDB Campylobacteria versus NCBI Epsilonproteobacteria preserved. Full rows include `data/catalog/ncbi_genbank-0015.jsonl.gz:13096`, `data/catalog/ncbi_refseq-0003.jsonl.gz:19638`, and `data/catalog/gtdb_genomes-0003.jsonl.gz:39603`. This MAG is not a target culture deposit.
- Mycoplasmopsis bovis BB-9 is taxon 28903. Latest GenBank contig `GCA_018594475.1` uses `SAMN11487526`, `PRJNA534329`, and `SVZP00000000.1`. Its identical paired RefSeq `GCF_018594475.1` is suppressed since 2021-06-01, with project `PRJNA224116`; exclusion is a large multi-isolate project. BV-BRC `28903.476` retains older Mycoplasma wording, sample/project, and unversioned WGS, but no assembly field. Do not attribute the assembly link directly to that BV-BRC row or treat suppressed RefSeq as live. Full rows: `data/catalog/ncbi_genbank-0017.jsonl.gz:1163`, `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:40352`, and `data/bvbrc/bvbrc-0017.jsonl.gz:15226`.
- Xanthomonas oryzae 131GD-BB9-1, taxon 347, has identical latest complete genomes `GCA_056503085.1`/`GCF_056503085.1`, sample `SAMN32105322`, GenBank project `PRJNA909919`, and RefSeq project `PRJNA224116`. Full rows: `data/catalog/ncbi_genbank-0052.jsonl.gz:11872` and `data/catalog/ncbi_refseq-0008.jsonl.gz:31745`. The substring BB9 does not identify this Stenotrophomonas.
- Numeric strain label 1034554 belongs to Salmonella enterica subsp. enterica serovar Virchow, taxon 48409, species taxon 28901: `GCA_015882725.1`, `SAMN16942825`, `PRJNA248792`, and `AAXSEG000000000.1`. It is a latest contig assembly without a RefSeq pair, excluded as a large multi-isolate project (`data/catalog/ncbi_genbank-0014.jsonl.gz:20901`). A numeric strain string is not the same identifier namespace as NCBITaxon.
- GOLD's Bb9 soil-fungal-community metatranscriptome is `Gp0291437`, `PRJNA468863`, sample `SAMN09094242`, analyses `Ga0247632` and `Ga0247977`, and IMG field `3300030533` on the first analysis. These are metatranscriptome analysis and self-mapping records, with empty organism IDs and GenBank lists, not isolate-genome evidence. Full rows: `data/gold/projects.jsonl.gz:194825` and `data/gold/analyses.jsonl.gz:155787` and line 156011. This incidental source-native collision did not reopen an Eukaryota YAML.

Heindl et al. 2012, DOI 10.2436/20.1501.01.155, identifies BB9 as
Halomonas phylotype 7 in Table 1. The full table, all continuations,
headers, and footnotes on printed pages 20-22 were read; its rendered
pages had also been visually inspected. The shared short name does not
support transferring its host association or activity to this taxon.
[Publisher PDF, Table 1](https://revistes.iec.cat/index.php/IM/article/view/60577/pdf_273).

Donkersley's 2014 Lancaster thesis Table 4.2, pages 138-140, uses BB9
for a bee-bread DGGE OTU at gel position b2. Its closest homologue is
uncultured bacterium clone BIGH1473, identity score 95, frequency 1.48%
in n=472, with accession KF881808. The complete table and continuations
were read and the relevant row visually checked. This is not an asserted
alias for target bB9 or JF772542.1.
[Lancaster thesis, Table 4.2](https://eprints.lancs.ac.uk/id/eprint/88132/1/2014donkersleyphd.pdf).

The primary Experimental/Reagents section of Zhang et al.,
DOI 10.1093/jaoacint/qsac109, explicitly uses BLX-BB9 as the catalog
number of a phosphate buffer. Co-occurrence with Stenotrophomonas in that
assay paper does not make the reagent a strain or establish target evidence.
[Oxford Academic, Apparatus and Reagents](https://academic.oup.com/jaoac/article/106/1/171/6709336).

## Completeness

Exact-ID scans returned no target rows in raw BacDive, LPSN, GTDB,
GOLD, MediaDive, Madin, or BactoTraits inventories. Ignored-inclusive
native searches supplied no supported target culture-deposit, assembly,
BV-BRC, GOLD, SeqCode, StrainInfo, or ATB chain. These are bounded
negatives, not a global claim that external evidence cannot exist.

Empty optional synonyms, nomenclature, mappings, strains, genomes, and
graph are not demonstrated omissions. `strain_count: 0` concerns
represented inventory strains, not absence of a sequenced isolate.
The marker alone does not establish an eligible culture-deposit link.

PubMed returned zero results for JF772542, bB9 with Stenotrophomonas,
and the exact unpublished title. Exact-marker and broader web searches
supplied no inspected target-specific publication or deposit bridge;
short-label literature collisions were excluded above. This was not a
complete literature census.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Retained identity, lineage, attestation, inventory count,
source status, and seed history are supported in the reviewed scope.

## Recommended Edits

None. Leave the generated YAML, `SEEDED` status, and history unchanged.
Do not add foreign BB9 genome, culture, sample, or phenotype associations.

Future verified enrichment belongs in maintained source inputs and
extraction through `scripts/extract_source_inventory.py` and
`src/taxonmech/extract.py`. Representation changes belong in
`scripts/seed_from_sources.py`; scope changes belong in
`curation/seed_scope.tsv`. Preserve identifiers, versions, native
classification conflicts, assembly status, and explicit source chains.

## Follow-up Checks

After a separately authorized upstream change, repeat focused schema and
strict validation, inspect the full record and supporting source rows,
then run corpus reproduction and QC. Any proposed genome link must
resolve at its authority and have an explicit strain/deposit/sample chain.

## Additional Notes

The existing review branch and HEAD
`b6a6508faca1388b88feb5740b1095e9f64cfdb8` remained unchanged.
No Eukaryota YAML was reopened. The local PDFs were read with MuPDF;
the Oxford publisher page supplied the reagent text despite a separate
PMC browser challenge. Access failures were not treated as evidence absence.

Only this new report was added for the target. Taxon YAMLs, source inputs,
generators, scope, review statuses, history, site products, and GitHub
were not modified.
