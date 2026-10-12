# YAML Record Review: Streptomyces sp. TGR24

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_tgr24.yaml`
- Started UTC: 2026-10-10T05:42:24Z
- Finished UTC: 2026-10-10T05:44:26Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:1037519` denotes Streptomyces sp. TGR24, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2593676`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`. It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. No synonym, formal nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph is asserted.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptomyces_sp_tgr24.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/streptomyces_sp_tgr24.yaml --out /private/tmp/taxonmech-tgr24-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, code, full lineage, empty source synonyms, seven inventories, unique index/scope resolution, attestation and exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- The complete native name and all 40 additional catalog rows were read through a lossless common-field/differing-field representation. Live NCBI EFetch/Datasets taxonomy, exact nucleotide search and full marker annotations were inspected. The taxonomy-browser web reader failed; direct retrieval succeeded and all 74 parsed HTML text lines were read.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`. Focused checks do not establish corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222791` agrees with the directly inspected [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037519&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037519&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037519). Species rank, parent 2593676 and genetic code 11 agree; Datasets includes root 1.

The complete root-first lineage agrees: root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. Kingdom 1783272, phylum 201174, class 1760, order 85011, family 2062 and genus 1883 are correctly carried from NCBI; the immediate parent is `NO_RANK`.

`data/catalog/ncbi_names-0005.jsonl.gz:32429` supplies the exact scientific name and empty unique-name qualifier. Neither backbone nor EFetch supplies alternate names. The species-ranked placeholder and marker strain qualifier are compatible metadata layers. Exact grounding does not establish formal nomenclature or type status.

## Evidence

The one-NAME NCBITAXON assertion and 2026-09-13 snapshot note match the pinned inventory. No additional own source-count row was found.

The exact nucleotide query returns one entry, UID 334361469: [JF799837.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799837.1), a 761-base partial 16S rRNA gene with both ends partial. Its source explicitly names Streptomyces sp. TGR24, strain TGR24, `taxon:1037519` and wetland soil. Declared and observed lengths agree, with alphabet `acgt`. This supports marker-to-taxon linkage, not an assembly or culture-deposit association.

The marker's sole reference is a direct submission dated 10-Apr-2011 by Li, Liu, Shao and Sun at Hebei University. It supplies no DOI, PMID, collection country, collection date or coordinates. Institutional address and submission date are not sampling metadata; shared authors or habitat wording cannot transfer another isolate's traits.

All 40 additional native rows match BioProject `PRJNA1037519`, not the target taxon ID. They comprise 20 BV-BRC records and their 20 GenBank assembly counterparts: 11 Streptococcus suis assemblies, taxon 1307, and nine Streptococcus agalactiae assemblies, taxon 1311. Every row was inspected, including its own organism, strain, assembly and sample fields. None names Streptomyces sp. TGR24.

For example, `data/bvbrc/bvbrc-0001.jsonl.gz:27827` and `data/catalog/ncbi_genbank-0031.jsonl.gz:25662` identify S. suis Ss_100, `GCA_033803125.1`, `SAMN38182236`; the BV-BRC ID is `1307.7371`. The pair at BV-BRC line 32802 and GenBank line 25651 identifies S. agalactiae Sa_82, `GCA_033802905.1`, `SAMN38182247`, with BV-BRC ID `1311.6151`. The numeric cross-namespace collision supplies no missing TGR24 genome link.

Exact-name, spaced-designation, wetland and JF799837 web queries established no directly joined experimental publication; the additional accession/name query returned no results. Datasets omits an assembly-count field rather than explicitly returning zero. These bounded checks do not exclude additional genomes or publications, and no trait was inferred from genus membership.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Bounded ID, slug and designation were searched, then JF799837 and spaced/hyphenated TGR 24 variants were added. Both searches returned 43 lines: three own backbone/name/scope rows and the 40 BioProject-number collisions, all individually read and excluded.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence statements apply only to inspected repository surfaces.

Zero strain count describes represented culture inventory, not isolate existence or culturability. Optional fields are appropriately empty without exact supporting joins. Neither a partial marker nor off-target catalog matches establish a missing required genome field. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, full Kitasatosporales lineage, attestation and seed audit are supported. Numeric BioProject matches do not establish missing associations.

## Recommended Edits

No generated-record correction is justified. Preserve Streptomyces sp. TGR24, species rank, full lineage, `SEEDED` status and existing history. Do not join BioProject numerals to taxon IDs, promote the partial marker to a genome or infer locality from an institutional address.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not direct generated-YAML edits. Optional marker enrichment requires a supported taxon-level representation rather than an invented culture-strain container.

## Follow-up Checks

For authorized enrichment, reconfirm exact organism linkage and retain JF799837.1's version. Require typed identifiers and explicit organism/strain evidence before adding an assembly, and directly joined experimental evidence before assigning a phenotype. After maintained-source changes, run the seed canary, schema/strict/history validation, corpus reproduction and QC.

## Additional Notes

- YAML SHA-256: `82aba079259251fe14136b400332d3dc20ad2e6a8aa0d49edfb06e341ed3d7ee`.
- JF799837.1 lowercase sequence SHA-256: `92dbc67fa0c4495b16d41572c7a840433967a5c28d840dcc6908b2017cca1a51`.
- The 40 extra complete rows were inspected in `data/bvbrc/bvbrc-0001.jsonl.gz` and `data/catalog/ncbi_genbank-0031.jsonl.gz`; their source fields, not search excerpts or genus resemblance, determined exclusion.
- `data/taxa/PATHS.tsv:15344` and `curation/seed_scope.tsv:323008` uniquely resolve the target. Scope addition is 2026-09-13; the seed preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this report was added for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened, curation event appended or review status promoted.
