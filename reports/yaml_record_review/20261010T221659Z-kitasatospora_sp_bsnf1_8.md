# YAML Record Review: Kitasatospora sp. BSNF1(8)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/kitasatospora_sp_bsnf1_8.yaml`
- Started UTC: 2026-10-10T22:15:02Z
- Finished UTC: 2026-10-10T22:16:59Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Kitasatospora sp. BSNF1(8), `NCBITaxon:1037649`. Species rank, bacterial domain, parent `NCBITaxon:2633591`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event are recorded. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/kitasatospora_sp_bsnf1_8.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/kitasatospora_sp_bsnf1_8.yaml --out /private/tmp/taxonmech-kitasatosporabsnf18-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, full lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. These are not corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222864` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1 (no rank); cellular organisms 131567 (cellular root); Bacteria 2 (domain); Bacillati 1783272 (kingdom); Actinomycetota 201174 (phylum); Actinomycetes 1760 (class); Kitasatosporales 85011 (order); Streptomycetaceae 2062 (family); Kitasatospora 2063 (genus); unclassified Kitasatospora 2633591 (no rank).

Complete live [EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037649&retmode=xml), [Datasets taxonomy JSON](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037649), and all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037649) lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes this NCBI placeholder, not nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32500` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15419` uniquely resolves ID/slug; `curation/seed_scope.tsv:323079` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037649[Organism:exp]` returned one UID, 345019051. Complete [GenBank annotation JF779800.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779800.1) explicitly joins organism, strain BSNF1(8), and taxon 1037649. The 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `b21486f332d0a40e10ab0d722a7efc6a23330c1a27505e1ef99f22addc1bf5ec`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), freshly read earlier this turn for BSNF1(1)'s shared study, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate study compares mineral-amended and control forest plots. Its cohort results do not establish BSNF1(8)-specific weathering, iron-release, chitin-degradation, or plant-growth phenotypes. Full text and isolate-level assay tables were not inspected. This marker's own qualifiers establish its isolation context.

All 15 non-target native matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7634`: Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 12T0055, GCA_010376495.1, PRJNA560345, SAMN12576314, JAAGHL000000000.1. Assembly name ASM1037649v1 supplies the match.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:20450`: Salmonella Virchow, taxid 48409/species 28901, strain 1037649, GCA_015873675.1, PRJNA248792, SAMN16972218, AAXRQE000000000.1, assembly PDT000901538.1. The bare strain number is not this NCBI taxon ID.
- `data/catalog/ncbi_genbank-0017.jsonl.gz:17814`: Salmonella Typhimurium, taxid 90371/species 28901, strain FSIS32105091, GCA_018934775.1, PRJNA242847, SAMN19222433, ABAWNG000000000.1. Assembly name PDT001037649.1 supplies the match. These three assemblies are excluded from RefSeq as parts of large multi-isolate projects.
- `data/catalog/gtdb_genomes-0017.jsonl.gz:21974` and `data/catalog/ncbi_genbank-0058.jsonl.gz:8392` describe GCA_903835715.1, uncultured Actinomycetes bacterium taxid/species 152507, isolate AM-2014-D2_bin-537, PRJEB38681, SAMEA6946740, CAILOE000000000.1. The 1,037,649-base genome length supplies the match. This lake-water MAG is GTDB PALSA-747 sp903897155, not Kitasatospora BSNF1(8); its GTDB representative and type-species-of-genus source flags are both false. Those flags are not independent nomenclature conclusions. GenBank reports exclusion from RefSeq for metagenomic origin and undefined genus. These are two source rows for one unrelated assembly, not target attestations.
- Ten AllTheBacteria rows have scientific name/current and prior Sylph E. coli, dataset r0.2, available FASTA, and passing assembly/Sylph filters. They match run-accession substrings. Nine pass HQ and have true prior HQ membership. Row 993051 instead has HQ `CHECKM2_MAX_CONTAM,MAX_CONTIG_NUM` and false prior HQ membership. Complete checksum, filter, and download fields were inspected; none was transferred to the target.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992798 | SAMEA9850004 | ERR10376491 | ERZ25465062 |
| 992799 | SAMEA9850005 | ERR10376493 | ERZ25465070 |
| 992800 | SAMEA9850006 | ERR10376495 | ERZ25465077 |
| 992892 | SAMEA9850144 | ERR10376490 | ERZ25465573 |
| 992893 | SAMEA9850145 | ERR10376492 | ERZ25465577 |
| 992894 | SAMEA9850146 | ERR10376496 | ERZ25465579 |
| 992896 | SAMEA9850148 | ERR10376494 | ERZ25465589 |
| 992933 | SAMEA9850288 | ERR10376497 | ERZ25576638 |
| 992934 | SAMEA9850289 | ERR10376499 | ERZ25576646 |
| 993051 | SAMEA9850633 | ERR10376498 | ERZ25466764 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779800, the DOI, and S003807171100280X. Both returned the same 18 lines: own backbone, scope, scientific name, and 15 unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism/16S web search returned taxonomy-tree leads; snippets were not treated as evidence, and the dedicated NCBI primary page was independently inspected.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support recorded taxonomy/name claims. Unchecked full text and isolate-specific assays constrain enrichment research without contradicting those claims.

## Recommended Edits

None required. Preserve BSNF1(8)/JF779800.1 identity and non-fertilized bulk-soil context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Inspect the primary article and isolate-level table before adding BSNF1(8)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

All requested NCBI taxonomy/marker responses succeeded. Marker annotation and native rows were inspected for this target; shared HAL requested metadata and complete abstract were read earlier this turn. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those routes were not retried. No login, payment, contact, or full-text reading occurred.

YAML SHA-256: `848fc92fcbb4eff65af953ff50a306cf3b12580c88f534575cb5a42fa6ff9f35`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged by this review.
