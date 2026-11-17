# YAML Record Review: Paenibacillus sp. BSF1(8)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_sp_bsf1_8.yaml`
- Started UTC: 2026-10-10T22:21:39Z
- Finished UTC: 2026-10-10T22:23:22Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Paenibacillus sp. BSF1(8), `NCBITaxon:1037651`. Species rank, bacterial domain, parent `NCBITaxon:185978`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event are recorded. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/paenibacillus_sp_bsf1_8.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/paenibacillus_sp_bsf1_8.yaml --out /private/tmp/taxonmech-paenibacillusbsf18-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, full lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. These are not corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222866` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1 (no rank); cellular organisms 131567 (cellular root); Bacteria 2 (domain); Bacillati 1783272 (kingdom); Bacillota 1239 (phylum); Bacilli 91061 (class); Caryophanales 1385 (order); Paenibacillaceae 186822 (family); Paenibacillus 44249 (genus); unclassified Paenibacillus 185978 (no rank).

Complete live [EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037651&retmode=xml), [Datasets taxonomy JSON](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037651), and all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037651) lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes this NCBI placeholder, not nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32502` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15421` uniquely resolves ID/slug; `curation/seed_scope.tsv:323081` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037651[Organism:exp]` returned one UID, 345019003. Complete [GenBank annotation JF779752.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779752.1) explicitly joins organism, strain BSF1(8), and taxon 1037651. The 450-base 16S rRNA marker is partial at both ends and annotated from fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `a94388c2707da9776ba4c927e7efe842c35b18bb9d4c68632f6acb16d5992776`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), freshly read earlier this turn for Micrococcus BSF2(15)'s shared study, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate study compares mineral-amended and control forest plots. Its cohort results do not establish BSF1(8)-specific weathering, iron-release, chitin-degradation, or plant-growth phenotypes. Full text and isolate-level assay tables were not inspected. This marker's own qualifiers establish its isolation context.

All 15 non-target native matches were read completely:

- `data/bvbrc/bvbrc-0012.jsonl.gz:4627` and `:4646`, and `data/catalog/ncbi_genbank-0019.jsonl.gz:22548`: Desulfobacterales bacterium SMBSF18, taxid 2044940, GCA_021108135.1, PRJNA758896, SAMN21083246. BV-BRC genome 2044940.159 has status WGS; 2044940.176 is Deprecated. GenBank WGS is JAIORM000000000.1; BV-BRC stores the unversioned prefix. GenBank identifies a metagenomic assembly excluded from RefSeq for metagenomic origin, fragmentation, and undefined genus. SMBSF18 is not Paenibacillus BSF1(8); three source rows are not three target isolates or genomes.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:7635`: Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 12T0057, GCA_010376515.1, PRJNA560345, SAMN12576315, JAAGHM000000000.1. Assembly name ASM1037651v1 supplies the match.
- `data/catalog/ncbi_genbank-0016.jsonl.gz:41786`: Salmonella Kentucky, taxid 192955/species 28901, strain FSIS32105090, GCA_018385965.1, PRJNA242847, SAMN19222434, ABAMAB000000000.1. Assembly name PDT001037651.1 supplies the match. Both these assemblies are excluded from RefSeq as parts of large multi-isolate projects.
- Ten AllTheBacteria rows have scientific name/current and prior Sylph E. coli, dataset r0.2, available FASTA, and passing assembly/Sylph filters. They match run-accession substrings. Seven pass HQ and have true prior HQ membership. Rows 992801 and 992941 instead have HQ `CHECKM2_MAX_CONTAM,MAX_CONTIG_NUM,MIN_N50`; row 992895 has `CHECKM2_MAX_CONTAM,MAX_CONTIG_NUM`. Those three have false prior HQ membership. Complete checksum, filter, and download fields were inspected; none was transferred to the target.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992801 | SAMEA9850007 | ERR10376513 | ERZ25465089 |
| 992802 | SAMEA9850008 | ERR10376515 | ERZ25465096 |
| 992835 | SAMEA9850057 | ERR10376519 | ERZ25465320 |
| 992837 | SAMEA9850059 | ERR10376517 | ERZ25465329 |
| 992895 | SAMEA9850147 | ERR10376514 | ERZ25465584 |
| 992897 | SAMEA9850151 | ERR10376516 | ERZ25465592 |
| 992898 | SAMEA9850152 | ERR10376518 | ERZ25465601 |
| 992941 | SAMEA9850296 | ERR10376511 | ERZ25466064 |
| 993058 | SAMEA9850640 | ERR10376510 | ERZ25466803 |
| 993059 | SAMEA9850641 | ERR10376512 | ERZ25466806 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779752, the DOI, and S003807171100280X. Both returned the same 18 lines: own backbone, scope, scientific name, and 15 unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism/16S web search returned taxonomy-tree and other terminology leads; snippets were not treated as target evidence. The dedicated NCBI primary page was independently inspected.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support recorded taxonomy/name claims. Unchecked full text and isolate-specific assays constrain enrichment research without contradicting those claims.

## Recommended Edits

None required. Preserve BSF1(8)/JF779752.1 identity and fertilized bulk-soil context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Inspect the primary article and isolate-level table before adding BSF1(8)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

All requested NCBI taxonomy/marker responses succeeded. Marker annotation and native rows were inspected for this target; shared HAL requested metadata and complete abstract were read earlier this turn. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those routes were not retried. No login, payment, contact, or full-text reading occurred.

YAML SHA-256: `37d2dbb1f23b85df3080a776323bf3830c5bc704f082ef931a6327a0049d4d57`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged by this review.
