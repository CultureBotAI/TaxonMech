# YAML Record Review: Brevibacillus sp. THGR18

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/brevibacillus_sp_thgr18.yaml`
- Started UTC: 2026-10-10T04:22:32Z
- Finished UTC: 2026-10-10T04:24:23Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. `NCBITaxon:1037499` denotes Brevibacillus sp. THGR18, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2684853`, genetic code 11, grounding `EXACT`, mapping status `SEEDED`. It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. No synonym, nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph is asserted.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/brevibacillus_sp_thgr18.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/brevibacillus_sp_thgr18.yaml --out /private/tmp/taxonmech-thgr18-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, genetic code, every ancestor, empty source synonyms, seven inventories, unique index/scope resolution and exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- Full native name row, live NCBI browser/EFetch/Datasets taxonomy, nucleotide search and complete marker annotations were inspected. Marker length and hash were checked. No DOI or PMID is cited by the YAML or marker submission.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222771` agrees with the [NCBI browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037499&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037499&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037499). EFetch confirms parent 2684853 and code 11; Datasets includes root 1.

The complete root-first chain matches: root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Paenibacillaceae, Brevibacillus and unclassified Brevibacillus. The final parent is `NO_RANK`, not the genus itself. Retain Paenibacillaceae (186822), Brevibacillus (55080) and parent 2684853; adjacent Bacillus records do not supply this record's lineage. Caryophanales is supported by the inspected source.

`data/catalog/ncbi_names-0005.jsonl.gz:32409` is the exact scientific name with an empty unique-name qualifier. Neither backbone nor EFetch supplies alternate names. The species-ranked NCBI placeholder and sequence strain qualifier are different metadata layers. Exact grounding does not establish formal nomenclature, type status or a phenotype. THGR18 must not be conflated with another isolate.

## Evidence

The one-NAME NCBITAXON assertion and 2026-09-13 snapshot note match the pinned source. No additional own source-count inventory row was found.

The nucleotide query returns one entry, UID 334361443, [JF799811.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799811.1), a 772-base partial 16S rRNA gene with both ends marked partial. The source explicitly links Brevibacillus sp. THGR18, strain THGR18 and `taxon:1037499`. Declared and observed lengths agree, with alphabet `acgt`. This is marker-to-taxon evidence, not a complete genome or culture-deposit accession.

Its source qualifiers explicitly give wetland soil and `geo_loc_name: China: Inner Mongolia Hetao`. This is source-backed isolation context for THGR18, not a location inferred from an institution or shared with other isolates. No coordinates or collection date are supplied. The sole reference is a direct submission dated 10-Apr-2011 by Li, Liu, Shao and Sun at Hebei University, with no DOI or PMID. The institutional address and submission date remain distinct from collection metadata.

Bounded exact-name web search returned NCBI taxonomy-tree pages, not a target research paper; accession search returned no results. This does not establish that no target publication exists. Taxonomy-tree co-membership and the browser's general database citation do not establish shared strain identity or target experimental evidence.

Datasets omits an assembly-count field rather than explicitly returning zero. No target genome was established from the inspected evidence. Shared submitters or wetland-soil wording does not justify importing a genome, culture deposit or phenotype from another isolate.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded taxon ID, slug and designation. The expanded search added JF799811. Both found exactly three lines: own backbone, native name and scope.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence statements are bounded to inspected repository surfaces, not all external evidence.

Zero strain count refers to represented culture inventory, not isolate existence or culturability. Empty optional slots are appropriate without exact supporting joins. The partial marker and its locality are optional source context, not missing required genome or phenotype fields. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, complete lineage, source count and seed audit are supported.

## Recommended Edits

No generated-record correction is justified. Preserve THGR18, species rank, the independently verified Brevibacillus lineage, `SEEDED` status and history. Do not add the partial marker as a genome or transfer biological claims from another isolate.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not a direct generated-YAML edit. Optional marker/citation enrichment needs a supported taxon-level representation rather than an invented strain container. Isolation-context curation must follow the repository ownership rules for habitat/strain claims and preserve the exact source qualifier.

## Follow-up Checks

For authorized enrichment, confirm exact THGR18 linkage and retain JF799811.1's version. Require explicit assembly and organism/strain evidence before adding a genome. Keep the explicit Hetao locality distinct from the submitter's address and do not infer coordinates. After source changes, run the documented seed canary, schema/strict/history checks, corpus reproduction and QC. A future primary paper needs an independent claim-level review.

## Additional Notes

- YAML SHA-256: `b2100fcc7f2ece4a5b25985a0d3d17994030f02da09d51bc84c34e4234d19e1e`.
- JF799811.1 lowercase sequence SHA-256: `303bd70823e003b62ffc0bdddef7a1d7e74ca12a00713739a399e31c04e8c244`.
- `data/taxa/PATHS.tsv:15324` and `curation/seed_scope.tsv:322988` uniquely resolve the target. Scope addition is 2026-09-13; the seed event preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was written for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened or review status promoted.
