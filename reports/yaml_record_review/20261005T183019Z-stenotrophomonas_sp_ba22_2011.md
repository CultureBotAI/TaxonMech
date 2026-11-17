# YAML Record Review: Stenotrophomonas sp. bA22(2011)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/stenotrophomonas_sp_ba22_2011.yaml`
- Started UTC: 2026-10-05T18:27:13Z
- Finished UTC: 2026-10-05T18:30:19Z
- Verdict: pass

## Target

The full 54-line generated `TaxonRecord` was read. It denotes
`NCBITaxon:1034560`, Stenotrophomonas sp. bA22(2011):
`SPECIES` rank, `BACTERIA` domain, parent
`NCBITaxon:196198`, genetic code 11, `EXACT` grounding,
`SEEDED` status, and `strain_count: 0`. It is a taxon record,
not a culture deposit or genome.

Owning source and scope rows are
`data/raw/ncbitaxon_taxa.tsv:221669` and
`curation/seed_scope.tsv:321980`.
`data/taxa/PATHS.tsv:14135` agrees in identifier and slug.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/stenotrophomonas_sp_ba22_2011.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/stenotrophomonas_sp_ba22_2011.yaml --out /private/tmp/sba22-strict-20261005.tsv`: exit 0; one file, zero files with errors and zero error rows.
- Structured reads checked the full backbone row and ten ancestors, PATHS, scope, source attestation, and seed event. Exact-ID checks covered seven raw source inventories plus type material, merged IDs, and dropped records.
- `rg --no-ignore --hidden -n -z -i` searched the target ID, full label, slug, and BA22 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All 25 matches were read in full using TSV headers or JSON decoding and reconciled by source address: ten raw/scope, five name, one GOLD, one BV-BRC, one StrainInfo, five assembly, and two GTDB rows.
- Separate marker scanning across those roots found no JF772548 row. Ignored-inclusive filename and content searches under `reports` and `history` found no prior target report or separate target history artifact, including marker searches, before this report.
- Live NCBI Taxonomy EFetch/Datasets, exact nonexpanded Assembly/Nuccore searches, complete marker metadata, and three PubMed queries completed. Two primary papers were inspected from publisher PDFs; their identity-bearing pages were also visually checked. The SciELO HTML view timed out, but the publisher PDF was readable.
- Not checked in this focused review: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused source agreement does not prove corpus reproduction.
- iModulonDB and curator-added graph ID/label checks are not applicable: the record asserts no gene, regulator, protein, phenotype, transcriptomic result, or causal graph. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

NCBI Taxonomy EFetch and Datasets agree on taxon 1034560, exact label,
species rank, parent 196198, Bacteria division, and code 11.
The complete root-first chain agrees:
`1 > 131567 > 2 > 3379134 > 1224 > 1236 > 135614 > 32033 > 40323 > 196198`.
These are root, cellular organisms, Bacteria, Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Lysobacterales, Lysobacteraceae,
Stenotrophomonas, and unclassified Stenotrophomonas.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034560);
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034560).

The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31057`.
The backbone supplies no synonyms, retirement target, or direct children.
Exact type-material, merged-ID, and dropped-record scans found no target
rows. The provisional species rank does not imply valid nomenclatural
publication. `EXACT` grounds a taxon identifier, not genomic species
equivalence or identity with every BA22 isolate.

## Evidence

The sole NCBITAXON attestation matches source ID, label, count 1,
unit `NAME`, and snapshot 2026-09-13. It counts a source-name
assertion, not a strain or genome. Scope and the
2026-09-13T17:54:04Z `seed_from_sources` /
`SEEDED_FROM_SOURCES` event agree.

The exact query `txid1034560[Organism:noexp]` returned zero Assembly
items with missing-phrase/no-items diagnostics and one Nuccore item,
UID 333981242. Full metadata and source/rRNA features identify
`JF772548.1`, a 1,451-base partial 16S rRNA sequence, strain bA22,
taxon 1034560, isolation source rhizosphere. Huang J.'s direct submission
is dated 1 April 2011; the weathering-related reference is unpublished.
That title and the submitter's institutional address do not demonstrate
a measured weathering phenotype, host, isolation locality, or deposit.
The marker is not a whole-genome accession.
[GenBank JF772548.1](https://www.ncbi.nlm.nih.gov/nuccore/JF772548.1).

PubMed searches for `JF772548[All Fields]`,
`"bA22"[All Fields] AND Stenotrophomonas[All Fields]`, and the
complete weathering-reference title returned zero items, with query
translations and diagnostics inspected. These are bounded index misses,
not proof of no literature.

Exact-name and strain/genus web searches found a genuine citation of
the marker in Criollo, Obando, Sanchez M., and Bonilla (2012), on
plant-growth-promoting bacteria associated with Pennisetum clandestinum,
Revista Corpoica 13(2):189-195. Full PDF pages 189-192 were read and
page 191 visually checked. The paper's experimental isolate 4K has
98% reported sequence identity to bA22 `JF772548.1`; bA22 is the
comparison sequence, not the inoculated isolate. The nitrogen-fixation,
indole, phosphate, and plant-growth results concern 4K and 5B. They
must not be assigned to bA22 or used to make 4K its synonym.
[Primary 2012 paper](https://revistacta.agrosavia.co/index.php/revista/article/download/254/257).

Ayala-Torres et al. (2023), DOI `10.18781/R.MEX.FIT.2208-2`,
is a separate bare-BA22 collision. Full relevant methods/results
pages 150-152 and Table 3 were read, with page 152 visually checked.
Its BA22 from Toluca is identified as Bacillus sp., with
`MF510169.1` in the comparison-sequence column and 99.48% identity.
The column is not proof that MF510169.1 is the study isolate's own
submission. Neither its identification nor its antagonism/metabolite
results support this Stenotrophomonas record.
[Primary 2023 paper](https://www.smf.org.mx/rmf/historicoRMF/pub_anticipadas/RMF2208-2.pdf).

## Completeness

The seven raw-source checks found no exact target BacDive, LPSN, GTDB,
GOLD, MediaDive, Madin, or BacTraits row. The broader native search did
not establish a target culture deposit, type material, assembly, or
GTDB mapping. Optional nomenclature, synonyms, mappings, strains,
traits, and graphs are appropriately empty for the seeded record.
`strain_count: 0` measures classified inventory coverage, not the
nonexistence of the isolate documented by GenBank.

The exact marker is a bounded optional enrichment lead. It does not
create a required whole-genome/deposit slot under the local checklist,
and it must not be inserted by hand into generated YAML. The 2012
literature citation establishes comparison use, not experimental
phenotype evidence for bA22. No consequential missing required
representation was demonstrated.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record. The native and literature collisions
below are excluded candidates, not unsupported claims in this YAML.
Full-corpus reproducibility remains untested.

## Recommended Edits

No required edit is demonstrated. Preserve generated fields and
`SEEDED` status.

For a separately authorized marker-enrichment task, define and test the
exact `taxon:1034560` / bA22 / `JF772548.1` association in
maintained extraction inputs and logic
(`scripts/extract_source_inventory.py`, `src/taxonmech/extract.py`),
then adjust `scripts/seed_from_sources.py` only if needed.
`curation/seed_scope.tsv` owns scope, not inferred isolate identity.
Do not transfer the 4K or Bacillus BA22 phenotypes, and do not patch
generated YAML or pages.

## Follow-up Checks

Any future marker enrichment should re-read the versioned GenBank
features and test that reference-sequence comparisons and same-name
foreign isolates remain excluded. Regenerate through the documented
maintained pipeline, then rerun focused schema and strict validation.

Before publication of regenerated products, run the documented
full-corpus reproduction, QC, tests, strict validation, provenance,
history, and site gates. This read-only review supplies no such
full-corpus result and does not promote status.

## Additional Notes

All 25 native search matches were read in full, including these
non-target identities:

- Diazotroph str. BA22 is taxon 100017, parent 83494: backbone line 17117, scope line 142946, native names shard 0000 line 36957.
- Agrococcus sp. BA22(2011) is taxon 942131, parent 2615065: backbone line 201258, scope line 303437, native names shard 0005 line 8045.
- Aeromonas sp. BA-22 is taxon 1296437, parent 257493: backbone line 305432, scope line 390754, native names shard 0007 line 27640.
- Pseudomonas sp. BA-22-09 is taxon 1296515, parent 196821: backbone line 305510, scope line 390832, native names shard 0007 line 27718.
- StrainInfo `data/straininfo/records.jsonl.gz:28234` is SI-ID 39930, DOI `10.60712/SI-ID39930.1`, published online, classified as Bacillus (NCBI 1386; LPSN 515217). BA-22 / FERM-P 3358 are designations. Available non-type SI-DP 107836 is ATCC 31185; there is no sequence or target bridge in that row. Strain and deposit IDs are distinct.

The archaeal BA_22 is Candidatus Bathyarchaeota archaeon, taxon 2026714:
`GCA_005888755.1`, `SAMN11380322`, `PRJNA449266`,
`VBBQ00000000.1`, latest scaffold with 67 contigs / 48 scaffolds,
no paired RefSeq, and metagenome/genus-undefined flags.
The full GenBank row is
`data/catalog/ncbi_genbank-0004.jsonl.gz:43278`.
BV-BRC 2026714.121
(`data/bvbrc/bvbrc-0010.jsonl.gz:45369`) explicitly links that
assembly/sample/project and unversioned VBBQ00000000.
GOLD Go0528219 (`data/gold/organisms.jsonl.gz:373013`) agrees on
archaeal label, taxon, and BA_22, with an empty culture field; it does
not supply an assembly/sample link.
GTDB `GB_GCA_005888755.1`
(`data/catalog/gtdb_genomes-0017.jsonl.gz:40799`) is representative
`40CM-2-53-6 sp005888755`, Thermoproteota/Bathyarchaeia,
whereas its NCBI fields use Candidatus Bathyarchaeota.
No classifier or genome association is transferred to the target.

The UUID component ba22 belongs to a Dehalococcoidia bacterium
(taxon 2026734), isolate `34552985-5af6-4851-ba22-5fcde49cff9b`:
`GCA_965207775.1`, `SAMEA115807662`, `PRJEB85492`,
`CBDBNR000000000.1`, latest chromosome-level assembly with three
contigs / three scaffolds, no paired RefSeq, and
metagenome/genus-undefined flags.
The full GenBank row is
`data/catalog/ncbi_genbank-0064.jsonl.gz:8397`.
GTDB `GB_GCA_965207775.1`
(`data/catalog/gtdb_genomes-0006.jsonl.gz:9363`) is
nonrepresentative `VXMT01 sp009837285`, Chloroflexota /
Dehalococcoidia / UBA2979. It is not a BA22 culture synonym.

Heyndrickxia oleronia BA22-01-12, taxon 38875, has the explicitly
identical pair `GCA_057895545.1` / `GCF_057895545.1`,
`SAMN60396242`, `JBYQTX000000000.1`, latest scaffold assemblies
with 54 contigs / 32 scaffolds. GenBank project is `PRJNA1470082`;
RefSeq uses umbrella `PRJNA224116`. Native rows are GenBank shard
0053 line 27131 and RefSeq shard 0008 line 45983. Their different
annotation gene counts are database annotations, not evidence that
either denotes Stenotrophomonas.

Finally, numeric 1034560 is a Salmonella strain name, not the taxon
ID, in `data/catalog/ncbi_genbank-0014.jsonl.gz:11672`:
Salmonella enterica subsp. enterica serovar Enteritidis, taxon 149539 /
species 28901, `GCA_015695005.1`, `SAMN16952249`,
`PRJNA248792`, `AAXLWG000000000.1`, latest contig assembly
with 35 contigs, no paired RefSeq, and large multi-isolate exclusion.

No paid research, outbound contact, GitHub mutation,
YAML/inventory/scope/history edit, status promotion, regeneration,
or Eukaryota-record review occurred.
