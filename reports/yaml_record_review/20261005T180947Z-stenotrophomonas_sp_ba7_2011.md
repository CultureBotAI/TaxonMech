# YAML Record Review: Stenotrophomonas sp. bA7(2011)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/stenotrophomonas_sp_ba7_2011.yaml`
- Started UTC: 2026-10-05T18:05:44Z
- Finished UTC: 2026-10-05T18:09:47Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. It identifies
`NCBITaxon:1034557`, Stenotrophomonas sp. bA7(2011), a species-ranked
bacterial taxon under `NCBITaxon:196198`, not a deposit or genome.
It has genetic code 11, `EXACT` grounding, `SEEDED` lifecycle
status, and `strain_count: 0`.

Owning inputs are `data/raw/ncbitaxon_taxa.tsv:221666` and
`curation/seed_scope.tsv:321977`.
`data/taxa/PATHS.tsv:14132` agrees in identifier and slug.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/stenotrophomonas_sp_ba7_2011.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/stenotrophomonas_sp_ba7_2011.yaml --out /private/tmp/sba7-strict-20261005.tsv`: exit 0; one file, zero files with errors and zero error rows.
- Structured checks read the complete backbone row and ten ancestors, PATHS, scope, attestation, and seed event. Exact-ID checks covered seven raw source inventories, type material, merged IDs, and dropped records.
- `rg --no-ignore --hidden -n -z -i` searched the numeric ID, full label, slug, and BA7 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All 49 matched rows were read completely with TSV headers or JSON decoding and reconciled with their addresses: 18 raw/scope/type-material, eight names, six BV-BRC, one BacDive, one GOLD, ten assemblies, and five GTDB rows.
- Separate marker scanning across those roots found no JF772545 rows. Ignored-inclusive filename/content searches under `reports` and `history` for target ID, label, slug, and marker found no prior target report or separate history artifact before this report.
- Live NCBI Taxonomy EFetch/Datasets, exact nonexpanded Assembly/Nuccore searches, complete marker metadata, bounded PubMed searches, the single PubMed hit's full abstract, primary article tables, and relevant thesis pages were checked.
- Not checked in this focused review: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused agreement is not a corpus-reproduction result.
- iModulonDB and the curator-added graph ID/label gate are not applicable to a record with no gene, regulator, protein, phenotype, transcriptomic, or causal-graph assertion. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

NCBI EFetch agrees on label, species rank, parent 196198, Bacteria
division, genetic code 11, and ancestor labels/ranks. Datasets agrees
with all ten root-first IDs:
`1 > 131567 > 2 > 3379134 > 1224 > 1236 > 135614 > 32033 > 40323 > 196198`.
These are root, cellular organisms, Bacteria, Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Lysobacterales, Lysobacteraceae,
Stenotrophomonas, and unclassified Stenotrophomonas.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034557);
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034557).

The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31054`.
The backbone has no synonym, retirement target, or direct child, and
exact type-material, merged-ID, and dropped-record scans found no
target rows. The provisional species rank is not proof of valid
nomenclatural publication. `EXACT` identifies the taxon concept,
not genomic species equivalence.

## Evidence

The single NCBITAXON attestation matches the ID, label, count 1, unit
`NAME`, and 2026-09-13 snapshot. The count is not a strain/genome
count. Scope and the `seed_from_sources` /
`SEEDED_FROM_SOURCES` event dated 2026-09-13T17:54:04Z agree.

The exact query `txid1034557[Organism:noexp]` returned zero Assembly
items with missing-phrase/no-items diagnostics and one Nuccore item,
UID 333981239. Complete metadata and source/rRNA features identify
`JF772545.1`, a 1,516-base partial 16S rRNA sequence, strain bA7,
taxon 1034557, isolation source rhizosphere. Huang J.'s direct
submission is dated 1 April 2011. Its weathering-related reference is
unpublished. That title and the submitter address do not prove a
measured weathering phenotype, host, isolation locality, or deposit.
The marker is not a whole genome.
[GenBank JF772545.1](https://www.ncbi.nlm.nih.gov/nuccore/JF772545.1).

The full native rows distinguish unrelated BA7 names and source chains:

- Uncultured bacterium BA7 (taxon 102930), Pseudomonas sp. BA-7-09 (1296506), Nocardiopsis sp. BA7-1-1 (1337873), Ochrobactrum sp. BA7 (1365802), Curtobacterium sp. Ba7 (1636653), and Psychrobacter sp. BA7 (1685601) each have their own backbone, scope, and scientific-name rows. Respective backbone lines are 18185, 305501, 320543, 334733, 426503, and 440368. The full short-name matches do not establish identity or synonymy with this Stenotrophomonas taxon.
- W-BA7 is a Polaribacter name, retained as an `includes` name under taxon 985043, Polaribacter sejongensis (`data/catalog/ncbi_names-0005.jsonl.gz:12765`; backbone 205305). Type-material rows 276301-276302 retain Polaribacter undariae and W-BA7 designations. BacDive 167508 (`data/bacdive/records.jsonl.gz:89740`; raw strain row 89741) distinguishes its P. undariae species name from the nested LPSN P. sejongensis name/synonym context. Deposits are KCTC 42175 and CECT 8670. It supplies marker `MT760307`, unversioned assembly `GCA_024918935`, BV-BRC `1574269.7`, and IMG `8047691767`, with sequence taxon 1574269 versus General taxon 985043. Preserve those source fields and accession syntax; neither the naming conflict nor the BA7 substring links it to the target.
- Lacticaseibacillus rhamnosus BA7, taxon 47715, has identical latest contig assemblies `GCA_054074985.1` / `GCF_054074985.1`, BioSample `SAMN21401156`, WGS `JAIQXL000000000.1`, GenBank project `PRJNA762683`, and RefSeq project `PRJNA224116`. Full rows: `data/catalog/ncbi_genbank-0049.jsonl.gz:49143` and `data/catalog/ncbi_refseq-0008.jsonl.gz:12123`. BV-BRC `47715.2273` retains the sample, GenBank project, and unversioned WGS `JAIQXL000000000`, but no assembly-accession field (`data/bvbrc/bvbrc-0020.jsonl.gz:45857`). Sample association does not create assembly equivalence.
- Ralstonia solanacearum BA7, taxon 305, has identical latest chromosome-level assemblies `GCA_029220005.1` / `GCF_029220005.1`, sample `SAMN32543033`, GenBank project `PRJNA917596`, RefSeq project `PRJNA224116`, and no WGS master. Full rows: `data/catalog/ncbi_genbank-0027.jsonl.gz:10588` and `data/catalog/ncbi_refseq-0004.jsonl.gz:47231`. BV-BRC `305.1358` explicitly names the GenBank assembly, sample, and unversioned nucleotide accessions `CP115949,CP115950,CP115951`, with source status Complete (`data/bvbrc/bvbrc-0018.jsonl.gz:35446`). Nonrepresentative GTDB `RS_GCF_029220005.1` retains Gammaproteobacteria versus NCBI Betaproteobacteria (`data/catalog/gtdb_genomes-0004.jsonl.gz:12876`). These classifications and assembly descriptions remain source-specific.
- Ignavibacteria bacterium BA7, taxon 2053306, is latest contig assembly `GCA_014879455.1`, sample `SAMN12995742`, project `PRJNA576469`, WGS `JACSRZ000000000.1`, no RefSeq pair, with metagenome-derived/genus-undefined exclusions (`data/catalog/ncbi_genbank-0013.jsonl.gz:23494`). BV-BRC `2053306.68` explicitly preserves this assembly/sample chain and unversioned WGS (`data/bvbrc/bvbrc-0012.jsonl.gz:22218`). Nonrepresentative GTDB `GB_GCA_014879455.1` places it in UBA9002 sp003519545 under Bacteroidota, versus NCBI Ignavibacteriota (`data/catalog/gtdb_genomes-0006.jsonl.gz:40517`).
- Candidatus Bathyarchaeota archaeon BA_7 is taxon 2026714, latest scaffold assembly `GCA_005882955.1`, sample `SAMN11380307`, project `PRJNA449266`, WGS `VBBB00000000.1`, no RefSeq pair, and metagenome-derived/genus-undefined exclusions (`data/catalog/ncbi_genbank-0004.jsonl.gz:42988`). BV-BRC `2026714.102` explicitly names that assembly/sample and unversioned WGS (`data/bvbrc/bvbrc-0010.jsonl.gz:45305`). Representative GTDB `GB_GCA_005882955.1` calls it 40CM-2-53-6 sp005882955 under Thermoproteota/Bathyarchaeia, retaining the separate NCBI Bathyarchaeota classification (`data/catalog/gtdb_genomes-0017.jsonl.gz:32719`). GOLD `Go0528230` is an organism record with the BA_7 name and taxon, no culture identifier, not a genome (`data/gold/organisms.jsonl.gz:373024`).
- Two Borreliella afzelii BA_7 chains, both taxon 29518, must remain separate. Identical latest scaffold pair `GCA_964213285.1` / `GCF_964213285.1` uses sample `SAMEA115904565`, GenBank project `PRJEB78704`, WGS `CAXOVT000000000.1`, and BV-BRC `29518.315`. Identical latest contig pair `GCA_965177955.1` / `GCF_965177955.1` instead uses `SAMEA117759218`, `PRJEB86142`, `CBCXTO000000000.1`, and BV-BRC `29518.466`. Both RefSeq projects are `PRJNA224116`; both BV-BRC rows omit an assembly-accession field and preserve unversioned WGS values. Assembly rows are GenBank 0063:3214 and 0064:6715, RefSeq 0010:18179 and 0010:20903; BV-BRC rows are 0017:37671 and 0017:37679. Nonrepresentative GTDB rows 0013:4368 and 0015:36956 retain `RS_GCF_964213285.1` and `RS_GCF_965177955.1`, respectively, with Borreliales versus NCBI Spirochaetales. A shared BA_7 label establishes neither identical samples/assemblies nor any target link.

PubMed returned zero items for `JF772545[All Fields]` and the exact
weathering-reference title. The bA7/Stenotrophomonas query returned
one item, PMID 37727857. The full abstract and primary section 3.3 /
Table 4 identify its BA-7 as Pseudomonas fragi, 1,405-base accession
`OP978162`, with comparison accession `FJ972529`; its
Stenotrophomonas humi is SA-5, `OP978163`. These table roles,
including the comparison sequence, are not target identity evidence.
No wheat-growth result was transferred.
[Asghar et al. 2023, DOI 10.3389/fpls.2023.1232271](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2023.1232271/full).

The primary 2017 sugarcane study's complete Table 4 gives Pseudomonas
sp. BA7 its own accession `KY460984`, length 1,486, with a 99%
match to comparison accession `LC093430`. It does not identify
bA7(2011)/JF772545.1; neither accession is a genome.
[Primary study, DOI 10.3389/fmicb.2017.01268](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2017.01268/full).

Ayala-Torres et al. (2023), DOI 10.18781/r.mex.fit.2208-2,
Table 3 on printed page 152 was read completely, including headers,
22 rows, footnotes, and visual layout. It labels BA7 from Atlacomulco
as Pseudomonas geniculata, with 99.44% identity and `JX042457.1`
in the species-reference accession column. The comparison accession
must not be relabeled as this study isolate's own accession.
Stenotrophomonas entries BA4 and BA9 are separate rows. No stable
identifier bridge to the target or transferable phenotype is supplied.
The PDF was used after intermittent HTML reader failures.
[Primary article PDF](https://www.scielo.org.mx/pdf/rmfi/v41n2/2007-8080-rmfi-41-02-143-es.pdf).

Cason's 2015 thesis, *Pathways for anaerobic hydrocarbon degradation
in a nitrate reducing consortium*, contains a more relevant bA7
label. Printed page 60 explains the community-sequence/reference
comparison; complete Table 3.17 on page 63 and Figure 3.10 /
Table 3.18 on page 65 were read, with pages 63 and 65 also visually
checked. The tree lists Stenotrophomonas sp. bA7 as a reference label
separate from study sequences DLQ01-DLQ04. Table 3.17 instead gives
DLQ03 a closest relative DB-17 (99%) and DLQ04 I28-J6NNFC6A2
(100%). The inspected pages provide no accession for the bA7
reference, so its exact linkage to JF772545.1 remains unresolved.
Neither a reference-tree label nor the adjacent genus-level table
proves hydrocarbon degradation by this isolate.
[Primary thesis](https://scholar.ufs.ac.za/bitstreams/2de86e16-2509-47a6-9746-76e0866a36d5/download).

## Completeness

Exact source-inventory checks found no target BacDive, LPSN, GTDB
mapping, GOLD, MediaDive, Madin, or BactoTraits row; there are no
backbone descendants to supply BacDive entries. Ignored-inclusive
native scans established no supported target culture-deposit/genome
chain. These are bounded searches, not proof that no further evidence
exists anywhere.

The zero strain count means zero represented BacDive records, not
absence of an isolate. Empty optional nomenclature, mappings,
strains, record-level citations, and causal graphs are defensible.
A partial marker and an accession-unresolved thesis reference do not
require creation of a deposit, assembly, or phenotype claim. No
consequential missing assertion was established.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The limited taxonomic record is supported. The pass does
not certify genomic species boundaries, biological properties,
unexamined literature, or corpus-wide reproducibility.

## Recommended Edits

None. Keep the generated record and `SEEDED` status unchanged.
Any later verified source correction belongs in
`scripts/extract_source_inventory.py` / `src/taxonmech/extract.py`;
harmonization fixes belong in `scripts/seed_from_sources.py`, and
scope changes in `curation/seed_scope.tsv`. Do not edit generated
YAML/pages or amend this immutable review.

## Follow-up Checks

An optional literature follow-up would recover the thesis's exact
RDP/GenBank reference identifier before asserting that its bA7 is
this marker. Even a match would support use as a reference sequence,
not a measured phenotype.

For a future explicit culture-deposit, sample, or assembly chain,
read complete source rows and preserve identifier types, versions,
classifications, and separate sample identities. After any later
authorized maintained-input fix, rerun focused schema/strict
validation and the applicable corpus reproduction, provenance,
history, rendering, and QC gates. Run no generator for this review.

## Additional Notes

No record, history, inventory, scope, code, page, commit, GitHub item,
or paid research was changed or created. Only this timestamped report
is added; there is no human-review status promotion. Eukaryota YAML
records were not reopened.
