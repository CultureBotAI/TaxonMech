# YAML Record Review: Stenotrophomonas sp. bB21(2011)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/stenotrophomonas_sp_bb21_2011.yaml`
- Started UTC: 2026-10-05T18:12:44Z
- Finished UTC: 2026-10-05T18:14:49Z
- Verdict: pass

## Target

The full 54-line generated `TaxonRecord` was read. It denotes
`NCBITaxon:1034558`, Stenotrophomonas sp. bB21(2011), with
`SPECIES` rank, `BACTERIA` domain, parent
`NCBITaxon:196198`, genetic code 11, `EXACT` grounding,
`SEEDED` status, and `strain_count: 0`. It identifies a taxon,
not a deposit or genome.

Owning inputs are `data/raw/ncbitaxon_taxa.tsv:221667` and
`curation/seed_scope.tsv:321978`.
`data/taxa/PATHS.tsv:14133` agrees in identifier and slug.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/stenotrophomonas_sp_bb21_2011.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/stenotrophomonas_sp_bb21_2011.yaml --out /private/tmp/sbb21-strict-20261005.tsv`: exit 0; one file, zero files with errors and zero error rows.
- Structured checks read the complete backbone row and ten ancestors, PATHS, scope, attestation, and seed event. Exact-ID checks covered seven raw source inventories, type material, merged IDs, and dropped records.
- `rg --no-ignore --hidden -n -z -i` searched the numeric ID, full label, slug, and BB21 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All 13 matches were read in full with TSV headers or JSON decoding and reconciled with their addresses: four raw/scope, two name, two BV-BRC, three assembly, and two GTDB rows.
- Separate marker scanning across those roots found no JF772546 rows. Ignored-inclusive filename/content searches under `reports` and `history` for target ID, label, slug, and marker found no prior target report or separate history artifact before this report.
- Live NCBI Taxonomy EFetch/Datasets, exact nonexpanded Assembly/Nuccore searches, full marker metadata, and bounded PubMed queries completed. Relevant primary thesis text was read, with the BB21-containing page also visually checked.
- Not checked in this focused review: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused source agreement does not prove corpus reproduction.
- iModulonDB and the curator-added graph ID/label gate are not applicable because the record makes no gene, regulator, protein, phenotype, transcriptomic, or causal-graph assertion. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

NCBI EFetch agrees on exact label, species rank, parent 196198,
Bacteria division, code 11, and ancestor labels/ranks. Datasets confirms
the entire root-first chain:
`1 > 131567 > 2 > 3379134 > 1224 > 1236 > 135614 > 32033 > 40323 > 196198`.
These are root, cellular organisms, Bacteria, Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Lysobacterales, Lysobacteraceae,
Stenotrophomonas, and unclassified Stenotrophomonas.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034558);
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034558).

The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31055`.
The backbone has no synonyms, retirement target, or direct children.
Exact type-material, merged-ID, and dropped-record scans found no
target rows. The provisional NCBI species rank is not valid
nomenclatural publication. `EXACT` grounds the taxon identifier,
not genomic species equivalence.

## Evidence

The sole NCBITAXON attestation matches source ID, label, count 1,
unit `NAME`, and snapshot 2026-09-13. It counts a name assertion,
not a strain or genome. Scope and the 2026-09-13T17:54:04Z
`seed_from_sources` / `SEEDED_FROM_SOURCES` event agree.

The exact query `txid1034558[Organism:noexp]` returned zero Assembly
items with missing-phrase/no-items diagnostics and one Nuccore item,
UID 333981240. Complete metadata and source/rRNA features identify
`JF772546.1`, a 1,511-base partial 16S rRNA sequence, strain bB21,
taxon 1034558, isolation source rhizosphere. Huang J.'s direct
submission is dated 1 April 2011. The weathering-related reference
is unpublished. Neither that title nor the submitter address proves
a measured weathering phenotype, host, isolation locality, or deposit.
A marker sequence is not a whole-genome accession.
[GenBank JF772546.1](https://www.ncbi.nlm.nih.gov/nuccore/JF772546.1).

Complete native rows distinguish these unrelated identities:

- Rhodospirillaceae bacterium BB21 is taxon 888408, parent 41296. Its rows are `data/raw/ncbitaxon_taxa.tsv:189193`, `curation/seed_scope.tsv:292777`, and `data/catalog/ncbi_names-0004.jsonl.gz:44138`. A shared BB21 designation is not synonymy or reclassification evidence.
- Desulfuromusa sp. BB21 is taxon 2614228, latest scaffold assembly `GCA_016744675.1`, with 186 contigs, 166 scaffolds, sample `SAMN16086347`, project `PRJNA606180`, WGS `JADGDX000000000.1`, no RefSeq pair, and a metagenome-derived flag (`data/catalog/ncbi_genbank-0015.jsonl.gz:13086`). BV-BRC genome `2614228.5` explicitly names this assembly/sample chain and retains unversioned WGS `JADGDX000000000` (`data/bvbrc/bvbrc-0015.jsonl.gz:1884`). Representative GTDB `GB_GCA_016744675.1` names Desulfuromusa sp016744675 under Desulfobacterota while its NCBI fields retain Thermodesulfobacteriota (`data/catalog/gtdb_genomes-0007.jsonl.gz:33465`). Preserve both classifications.
- UUID `6b50408d-bb21-410b-bf53-c761b53f873e` is the isolate designation of Chloroflexota bacterium, taxon 2026724, not a BB21 alias. Latest complete-genome assembly `GCA_965116855.1` has one contig, sample `SAMEA114659190`, project `PRJEB72585`, no WGS master or RefSeq pair, and metagenome-derived/genus-undefined exclusions (`data/catalog/ncbi_genbank-0064.jsonl.gz:4925`). BV-BRC `2026724.3582` preserves the sample/project and unversioned nucleotide accession `OZ220726`, but no assembly-accession field (`data/bvbrc/bvbrc-0011.jsonl.gz:692`). Nonrepresentative GTDB `GB_GCA_965116855.1` supplies the explicit assembly and sample and names VXOZ01 sp965220045 under Chloroflexota/UBA11872 (`data/catalog/gtdb_genomes-0010.jsonl.gz:9810`). A UUID substring or shared sample does not establish target identity or cross-database assembly equivalence.
- Staphylococcus aureus BB21-I1-E1 is taxon 1280, latest contig assembly `GCA_026831085.1`, sample `SAMN17580149`, project `PRJNA514245`, WGS `DAKWNM000000000.1`, no RefSeq pair, with a large-multi-isolate-project exclusion (`data/catalog/ncbi_genbank-0024.jsonl.gz:45706`). The designation substring does not connect it to Stenotrophomonas.

PubMed returned zero items for `JF772546[All Fields]`,
`"bB21"[All Fields] AND Stenotrophomonas[All Fields]`, and the exact
weathering-reference title. Web searches for the exact marker and
Stenotrophomonas/bB21 supplied no inspected publication with an explicit
target accession bridge. These are bounded negatives, not a claim that
no literature exists.

A primary 2025 thesis document by Eva-Boglarka Vincze, *The role of
plant growth-promoting bacteria in plant stress response induced by
heavy metals*, lists S. rhizophila BB21. PDF pages 4 and 6 were read
completely, covering sections 3.1 and 4.1; page 6 was also visually
checked. The study describes its own regional strain collection and
lists BB21 among agricultural-soil strains. The inspected sections
supply no JF772546 or NCBITaxon:1034558 bridge. Treat it as an unlinked
name lead, not a demonstrated synonym, re-identification, or target
phenotype source. No heavy-metal result was transferred.
[Primary thesis document](https://pea.lib.pte.hu/server/api/core/bitstreams/07fe0d54-f89d-44b9-8bd5-07b31d935204/content).

## Completeness

The seven raw source inventories have no exact target row for BacDive,
LPSN, GTDB mapping, GOLD, MediaDive, Madin, or BactoTraits, and there
are no backbone descendants to supply BacDive entries. Ignored-inclusive
native searches found no supported target culture-deposit/genome chain.

The zero strain count means zero represented BacDive records, not
absence of a biological isolate. Empty optional synonyms, nomenclature,
mappings, strains, record-level citations, and causal graphs are
defensible. The marker and unlinked literature name do not require an
invented deposit, assembly, or phenotype. No consequential missing
assertion was established within the inspected evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record is supported within its limited taxonomic scope.
This pass does not certify biological properties, genomic species
boundaries, unexamined literature, or corpus-wide reproducibility.

## Recommended Edits

None. Retain the generated YAML and `SEEDED` status.
Future verified source corrections belong in
`scripts/extract_source_inventory.py` / `src/taxonmech/extract.py`,
harmonization fixes in `scripts/seed_from_sources.py`, and scope
decisions in `curation/seed_scope.tsv`. Do not patch generated YAML,
pages, or this immutable report to represent later evidence.

## Follow-up Checks

Before attaching the thesis or another BB21 source, require an explicit
marker, registered deposit, sample, or assembly chain to this isolate.
Preserve supplied versions, source classifications, and identifier
types; a shared short name or genus is insufficient.

For a later authorized maintained-input correction, rerun focused schema
and strict validation, then corpus reproduction and the applicable
provenance, history, rendering, and QC gates. Run no generator for this
read-only review.

## Additional Notes

Only this timestamped report is added. No YAML, history, inventory,
scope, code, page, commit, GitHub item, or paid research was changed
or created. There is no human-review status promotion. Eukaryota
YAML records were not reopened.
