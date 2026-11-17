# YAML Record Review: Stenotrophomonas sp. bB23(2011)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/stenotrophomonas_sp_bb23_2011.yaml`
- Started UTC: 2026-10-05T18:01:24Z
- Finished UTC: 2026-10-05T18:04:10Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. It denotes
`NCBITaxon:1034556`, Stenotrophomonas sp. bB23(2011), with species
rank, `BACTERIA`, parent `NCBITaxon:196198`, genetic code 11,
`EXACT` grounding, `SEEDED` status, and `strain_count: 0`.
It identifies a taxon, not a culture deposit or genome.

Owning inputs are `data/raw/ncbitaxon_taxa.tsv:221665` and
`curation/seed_scope.tsv:321976`; `data/taxa/PATHS.tsv:14131`
agrees in identifier and slug. No generated YAML was edited.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/stenotrophomonas_sp_bb23_2011.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/stenotrophomonas_sp_bb23_2011.yaml --out /private/tmp/sbb23-strict-20261005.tsv`: exit 0; one file, zero files with errors and zero error rows.
- Structured checks read the complete backbone row and ten ancestors, PATHS, scope, attestation, and seed event. Exact-ID checks covered seven raw source inventories, type material, merged IDs, and dropped records.
- `rg --no-ignore --hidden -n -z -i` searched the numeric ID, complete label, slug, and BB23 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All 18 matches were read in full with TSV headers or JSON decoding and reconciled against their addresses: six raw/scope, three name, two BV-BRC, one StrainInfo, four assembly, and two GTDB rows.
- A separate marker search across those roots returned no JF772544 rows. Ignored-inclusive filename and content searches under `reports` and `history` for ID, full label, slug, and marker found no prior target report or separate history artifact before this report.
- Live NCBI Taxonomy EFetch/Datasets, exact nonexpanded Assembly/Nuccore searches, complete marker metadata, and bounded PubMed queries completed. Relevant primary thesis pages were read and visually checked to exclude a literature name collision.
- Not checked: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused agreement does not prove corpus reproduction.
- iModulonDB and the curator-added graph ID/label gate were not applicable: the record asserts no gene, regulator, protein, phenotype, transcriptomic, or causal-graph claim. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

NCBI EFetch agrees on exact label, species rank, parent 196198, Bacteria
division, genetic code 11, and the ancestor labels/ranks. Datasets confirms
the complete root-first chain:
`1 > 131567 > 2 > 3379134 > 1224 > 1236 > 135614 > 32033 > 40323 > 196198`.
This is root, cellular organisms, Bacteria, Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Lysobacterales, Lysobacteraceae,
Stenotrophomonas, and unclassified Stenotrophomonas.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034556);
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034556).

The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31053`. The backbone has no
synonyms, retirement target, or direct children. Exact type-material,
merged-ID, and dropped-record scans found no target rows.
A provisional NCBI species rank is not valid nomenclatural publication.
`EXACT` grounds the taxon identifier, not genomic species equivalence.

## Evidence

The sole NCBITAXON attestation matches the source ID, label, count 1,
unit `NAME`, and snapshot 2026-09-13. This is a name assertion, not
a strain or genome count. Scope and the 2026-09-13T17:54:04Z
`seed_from_sources` / `SEEDED_FROM_SOURCES` event agree.

The exact query `txid1034556[Organism:noexp]` returned zero Assembly
items with missing-phrase/no-items diagnostics and one Nuccore item,
UID 333981238. Complete metadata and source/rRNA features identify
`JF772544.1`, a 1,504-base partial 16S rRNA sequence, strain bB23,
taxon 1034556, isolation source rhizosphere. Huang J.'s direct
submission is dated 1 April 2011. Its weathering-related reference is
unpublished. Neither that title nor the submitter address establishes a
measured weathering trait, host, isolation locality, or culture deposit.
The marker is not a whole-genome accession.
[GenBank JF772544.1](https://www.ncbi.nlm.nih.gov/nuccore/JF772544.1).

Complete native rows distinguish the following unrelated identities:

- Uncultured bacterium BB23 is `NCBITaxon:94759`, parent 48479, not the target. Its backbone, scope, and scientific-name rows are `data/raw/ncbitaxon_taxa.tsv:15717`, `curation/seed_scope.tsv:141815`, and `data/catalog/ncbi_names-0000.jsonl.gz:35329`.
- Jannaschia sp. BB23 is `NCBITaxon:888410`, parent 2645469. Its corresponding rows are backbone 189195, scope 292779, and `data/catalog/ncbi_names-0004.jsonl.gz:44140`. The shared short designation does not establish a synonym or reclassification.
- Winogradskyella sp. BB23 is taxon 1883156. Identical latest scaffold assemblies `GCA_016744625.1` and `GCF_016744625.1` have 190 contigs and 159 scaffolds, BioSample `SAMN16086349`, WGS `JADGDZ000000000.1`, and the metagenome-derived flag. GenBank project `PRJNA606180` differs from RefSeq project `PRJNA224116`. Full assembly rows are `data/catalog/ncbi_genbank-0015.jsonl.gz:13084` and `data/catalog/ncbi_refseq-0003.jsonl.gz:19636`. BV-BRC genome `1883156.16` explicitly names the GenBank assembly and sample, retaining unversioned `JADGDZ000000000` (`data/bvbrc/bvbrc-0007.jsonl.gz:30991`). Representative GTDB `RS_GCF_016744625.1` names Winogradskyella sp016744625 under Bacteroidia, while its NCBI classification retains Flavobacteriia (`data/catalog/gtdb_genomes-0002.jsonl.gz:39425`). Preserve both source classifications; none belongs to Stenotrophomonas.
- Bifidobacterium adolescentis BB23 is taxon 1680. Latest complete-genome `GCF_000817995.1` explicitly pairs with `GCA_000817995.1`, with sample `SAMN03273368`, project `PRJNA224116`, and no WGS master (`data/catalog/ncbi_refseq-0000.jsonl.gz:26794`). BV-BRC `1680.5` uses genome-name designation BBMN23 but strain field BB23, the same explicit RefSeq accession and sample, project `PRJNA271241`, and nucleotide accessions `CP010437` / `NZ_CP010437.1` (`data/bvbrc/bvbrc-0005.jsonl.gz:13302`). Nonrepresentative GTDB `RS_GCF_000817995.1` preserves BB23, the sample, and explicit GenBank assembly, while using Actinomycetales rather than NCBI Bifidobacteriales (`data/catalog/gtdb_genomes-0009.jsonl.gz:36915`). These are source-specific assertions, not a license to transfer a genome or reconcile classifications.
- Staphylococcus aureus BB23-I1-E1 is taxon 1280, latest contig assembly `GCA_026826395.1`, sample `SAMN17579954`, project `PRJNA514245`, WGS `DAKWEO000000000.1`, no RefSeq pair, and a large-multi-isolate-project exclusion (`data/catalog/ncbi_genbank-0024.jsonl.gz:45473`). A designation substring is not identity evidence.
- StrainInfo `SI-ID186715`, record-version DOI `10.60712/SI-ID186715.1`, is Aspergillus ruber, taxon 396024, published offline. Its available deposit `SI-DP466481` is `IMI 094154`; source aliases include UC 4257 and LSHB BB23 (`data/straininfo/records.jsonl.gz:138578`). The row supplies no sequence. Its strain/deposit/version identities cannot be transferred through the BB23 substring. This incidental native-source collision did not reopen a Eukaryota YAML review.

PubMed returned zero items for `JF772544[All Fields]`,
`"bB23"[All Fields] AND Stenotrophomonas[All Fields]`, and the exact
weathering-reference title. Web searches for the exact marker and
Stenotrophomonas/bB23 did not establish a target-specific publication
bridge. These bounded negatives do not establish that no literature exists.

A relevant search collision was Silvia Carlo's thesis
*Nanobiotechnologies to improve plant protection* (academic year
2022-2023). Complete printed pages 25-26, including Figure 2.1 and its
caption, were extracted and visually read. Its BB23/Tad is named
Ranhella aquatilis in consortia MC_B/MC_C; the separately listed
Stenotrophomonas is S. rhizophila Sp952 in MC_D. That co-occurrence
does not connect either strain to bB23(2011) or JF772544.1. No plant,
medium, or experimental phenotype was transferred.
[Primary thesis](https://air.unipr.it/retrieve/420363be-ee25-4fb7-a0bd-7e374f15d176/Silvia.Carlo_PhD_thesis.pdf).

## Completeness

The seven source inventories contain no exact target row for BacDive,
LPSN, GTDB mapping, GOLD, MediaDive, Madin, or BactoTraits, and the
backbone has no descendants to supply BacDive strains. The record's zero
strain count means zero represented BacDive entries, not absence of a
biological isolate. Bounded ignored-inclusive native searches found no
supported culture-deposit/genome chain for this target.

Empty optional synonyms, nomenclature, mappings, strains, record-level
literature, and causal graphs are therefore defensible. The marker
establishes sequence provenance but does not by itself require a new
BacDive strain or genome entry. No consequential missing assertion was
established by the inspected evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record is supported within its limited taxonomic scope.
This pass does not certify biological properties, genomic species
boundaries, or complete worldwide evidence coverage.

## Recommended Edits

None for this record. Retain the generated YAML and lifecycle status.
Future verified source corrections belong in
`scripts/extract_source_inventory.py` / `src/taxonmech/extract.py`,
harmonization fixes in `scripts/seed_from_sources.py`, and scope
decisions in `curation/seed_scope.tsv`. Do not patch generated YAML,
pages, or this immutable report to represent later evidence.

## Follow-up Checks

Revisit only if an explicit marker, registered deposit, BioSample, or
assembly chain identifies this same isolate. Read full native evidence
and retain source classifications, accession versions, and identifier
types. A bare BB23 match is insufficient.

For a later authorized maintained-input change, rerun focused schema and
strict validation, then corpus reproduction and the applicable provenance,
history, rendering, and QC gates. Run no generator for this read-only review.

## Additional Notes

The verdict concerns this generated taxon record at the inspected
snapshot; it does not promote `SEEDED` to `REVIEWED`. No history,
YAML, inventory, scope, code, page, commit, GitHub item, or paid research
was changed or created. Only this timestamped report is added.
