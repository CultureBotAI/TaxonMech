# YAML Record Review: Pseudomonas sp. BIHB 1312

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_bihb_1312.yaml`
- Started UTC: 2026-10-05T18:55:15Z
- Finished UTC: 2026-10-05T18:57:16Z
- Verdict: pass

## Target

The full 54-line generated `TaxonRecord` was read. It denotes
`NCBITaxon:1034638`, Pseudomonas sp. BIHB 1312, rank `SPECIES`,
domain `BACTERIA`, parent `NCBITaxon:196821`, genetic code 11,
`EXACT` grounding, `SEEDED` status, and `strain_count: 0`.
The taxon is not itself a culture deposit or genome.

Owning source and scope rows are `data/raw/ncbitaxon_taxa.tsv:221675`
and `curation/seed_scope.tsv:321986`.
`data/taxa/PATHS.tsv:14141` agrees in identifier and slug.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_bihb_1312.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_bihb_1312.yaml --out /private/tmp/bihb1312-strict-20261005.tsv`: exit 0; one file, zero files with errors and zero error rows. The TSV contains only its header.
- Structured comparisons read the full backbone row and ten ancestors, PATHS, scope, attestation, and seed event. Seven raw source inventories and exact type-material, merged-ID, and dropped-record tables were checked.
- `rg --no-ignore --hidden -n -z -i` searched the target ID, full label, slug, and BIHB 1312 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All eight candidate rows were read completely with TSV headers or JSON decoding.
- Separate marker scanning in those roots found no JF766689 row. Ignored-inclusive content and filename searches under `reports` and `history`, including marker searches, found no prior target report or separate target history artifact before this report.
- Live NCBI Taxonomy EFetch/Datasets, exact nonexpanded Assembly/Nuccore searches, full sequence metadata, and three PubMed queries completed. Exact-name, marker, compact-strain-name, and strain/topic web searches were performed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused source agreement does not prove corpus reproduction.
- iModulonDB and curator-added graph ID/label checks are inapplicable: the record asserts no gene, regulator, protein, phenotype, transcriptomic result, or graph. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

Live NCBI Taxonomy EFetch and Datasets agree on taxon 1034638,
exact label, species rank, parent 196821, Bacteria division, and
genetic code 11. The full root-first lineage matches:
`1 > 131567 > 2 > 3379134 > 1224 > 1236 > 72274 > 135621 > 286 > 196821`.
All ten ancestors have the correct labels and normalized ranks:
root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota,
Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae,
Pseudomonas, and unclassified Pseudomonas.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034638);
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034638).

The complete scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31063`.
The backbone contains no synonyms, retirement target, or direct
children. Exact type-material, merged-ID, and dropped-record
checks found no target row. Provisional species rank does not imply
valid nomenclatural publication. `EXACT` grounds this identifier,
not a genome-defined species or equivalence with adjacent BIHB
isolate numbers.

## Evidence

The NCBITAXON attestation matches identifier, label, count 1, unit
`NAME`, and snapshot 2026-09-13. This counts a name assertion,
not genomes or biological isolates. Scope and the
2026-09-13T17:54:04Z `seed_from_sources` /
`SEEDED_FROM_SOURCES` event agree exactly.

The query `txid1034638[Organism:noexp]` returned zero Assembly
items with missing-phrase/no-items diagnostics and one Nuccore
item, UID 333496467. Full metadata and source/rRNA features identify
`JF766689.1`, a 1,483-base partial 16S rRNA sequence, with strain
BIHB 1312 and `taxon:1034638`. The explicit source qualifiers
are rhizosphere, host pea, and country India. They support submitted
provenance, not measured phenotypes, precise sampling coordinates,
deposit equivalence, or a whole genome.
[GenBank JF766689.1](https://www.ncbi.nlm.nih.gov/nuccore/JF766689.1).

Gulati A., Rahi P., and Sharma N. submitted this marker on
1 April 2011. The associated pea-rhizosphere phosphate-solubilizing
genotypes study is marked unpublished in the inspected sequence
record. Its title does not establish BIHB 1312-specific assay
results, and its institutional address is not a sampling locality.

PubMed queries for `JF766689[All Fields]`,
`"BIHB 1312"[All Fields] AND Pseudomonas[All Fields]`, and the
full sequence-reference title returned zero items. Query translations
and no-items diagnostics were inspected. Exact marker and compact-name
web searches returned no results; the broader bounded searches did
not establish a primary target-specific experimental publication.
No functional claim is inferred from generic Pseudomonas literature,
the submitted study title, or other BIHB strains.

## Completeness

Seven parsed raw inventories contain no exact target BacDive, LPSN,
GTDB, GOLD, MediaDive, Madin, or BacTraits row. The wider native
search found the three target backbone/scope/name rows and five
unrelated numeric collisions detailed below. It did not establish
an exact deposit, type material, assembly, or GTDB mapping.

Empty optional nomenclature, synonyms, mappings, strains, traits,
and graphs are appropriate under the local checklist.
`strain_count: 0` is inventory coverage, not a claim that the
GenBank isolate does not exist. The marker and its explicit source
qualifiers are optional enrichment leads. No missing required
representation was demonstrated. Eventual publication of the
submitted study and target-specific functional results remain
unresolved; the current YAML makes no claim depending on them.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record. Full-corpus reproduction and
uninspected experimental claims are not established by this review.

## Recommended Edits

No required edit is demonstrated. Preserve generated fields and
`SEEDED` status.

If optional sequence enrichment is separately authorized, define
and test the exact `taxon:1034638` / BIHB 1312 / `JF766689.1`
relation in maintained extraction inputs and logic
(`scripts/extract_source_inventory.py`, `src/taxonmech/extract.py`),
then adjust `scripts/seed_from_sources.py` only if needed.
`curation/seed_scope.tsv` owns scope, not inferred isolate identity.
Do not patch generated YAML/pages, label a marker as a genome, or
interpret genome-length matches as taxon mappings.

## Follow-up Checks

For optional enrichment, re-read the versioned GenBank features,
preserve their submitted-provenance scope, and test exclusion of
unrelated BIHB isolates and the numeric collisions below.
Regenerate through the maintained pipeline and rerun focused schema
and strict validation.

Functional claims require inspected primary target-specific
methods/results and an exact identity bridge. Before publication
of regenerated products, run the documented corpus reproduction,
QC, tests, strict validation, provenance, history, and site gates.
This report does not supply those results or promote status.

## Additional Notes

All five additional candidates match the number 1034638 in a length
field, not in a target taxon or strain field. Their full native rows
were read and rejected as target evidence:

| Native row | Assembly | Actual identity | Matching field |
| --- | --- | --- | --- |
| `data/catalog/ncbi_genbank-0064.jsonl.gz:38174` | `GCA_977194695.1` | Uncultured archaeon, taxid 115547, isolate MarMAG_004785 | `genome_size` |
| `data/catalog/ncbi_genbank-0033.jsonl.gz:723` | `GCA_035348055.1` | Anaerolineaceae bacterium, taxid 2024896, isolate AMR_MDS_1523 | `genome_size` |
| `data/catalog/ncbi_genbank-0043.jsonl.gz:17293` | `GCA_047025295.1` | Lactobacillus iners, taxid 147802, isolate C043_06 | `genome_size` |
| `data/catalog/gtdb_genomes-0005.jsonl.gz:35350` | `GB_GCA_047025295.1` | The same L. iners assembly, GTDB L. iners, NCBI taxid 147802 | `ncbi_total_length` |
| `data/catalog/ncbi_genbank-0066.jsonl.gz:18582` | `GCA_982445555.1` | Oscillospiraceae bacterium, taxid 2485925, isolate DRR171933_bin_39008 | `genome_size`, `genome_size_ungapped` |

Search misses include ignored files within the stated roots and
remain bounded to those sources and queries, not global absence
claims. No paid research, outbound contact, GitHub mutation,
record/inventory/scope/history edit, status promotion, regeneration,
or Eukaryota review occurred.
