# YAML Record Review: Lysobacter sp. TGR23

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lysobacter_sp_tgr23.yaml`
- Started UTC: 2026-10-10T04:29:26Z
- Finished UTC: 2026-10-10T04:31:32Z
- Verdict: pass

## Target

The complete 53-line generated `TaxonRecord` was read. `NCBITaxon:1037501` denotes Lysobacter sp. TGR23, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2635362`, genetic code 11, grounding `EXACT`, mapping status `SEEDED`. It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. No synonym, nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph is asserted.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/lysobacter_sp_tgr23.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/lysobacter_sp_tgr23.yaml --out /private/tmp/taxonmech-tgr23-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, genetic code, every ancestor, empty source synonyms, seven inventories, unique index/scope resolution and exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- Full native name row, live NCBI EFetch/Datasets taxonomy, nucleotide search and complete marker annotations were inspected. Marker length and hash were checked. After the web reader failed on the taxonomy-browser URL, a direct public HTML read succeeded; all 74 parsed text lines were inspected.
- No DOI or PMID is cited by the YAML or marker submission. Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222773` agrees with the directly read [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037501&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037501&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037501). EFetch confirms parent 2635362 and code 11; Datasets includes root 1.

The complete root-first chain matches: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Lysobacterales, Lysobacteraceae, Lysobacter and unclassified Lysobacter. Preserve Lysobacterales (135614), Lysobacteraceae (32033), genus Lysobacter (68), and the `NO_RANK` parent 2635362. The inspected authorities support these labels; no alternative placement is inferred.

`data/catalog/ncbi_names-0005.jsonl.gz:32411` is the exact scientific name with an empty unique-name qualifier. Neither backbone nor EFetch supplies alternate names. The species-ranked NCBI placeholder and sequence strain qualifier are different metadata layers. Exact grounding does not establish formal nomenclature, type status or a phenotype. TGR23 must not be conflated with another isolate.

## Evidence

The one-NAME NCBITAXON assertion and 2026-09-13 snapshot note match the pinned source. No additional own source-count inventory row was found.

The nucleotide query returns one entry, UID 334361457, [JF799825.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799825.1), a 770-base partial 16S rRNA gene with both ends marked partial. The source explicitly links Lysobacter sp. TGR23, strain TGR23, `taxon:1037501` and wetland soil. Declared and observed lengths agree, with alphabet `acgt`. This is marker-to-taxon evidence, not a complete genome or culture-deposit accession.

The sole reference is a direct submission dated 10-Apr-2011 by Li, Liu, Shao and Sun at Hebei University. It supplies no DOI, PMID, collection country, coordinates or collection date. The institutional address and submission date are not sampling metadata. A locality supplied for another isolate cannot be transferred here.

Bounded exact-name web search returned NCBI taxonomy-tree and Genome.jp taxonomy-summary leads, not a target research paper; accession search returned no results. These leads were not treated as independent experimental or strain-genome evidence. The browser's general database citation is not a primary study of TGR23. The bounded searches do not prove that no target publication exists.

Datasets omits an assembly-count field rather than explicitly returning zero. No target genome was established from the inspected evidence. Shared genus, submitters or wetland-soil wording does not justify importing a genome, culture deposit or phenotype from another isolate.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded taxon ID, slug and designation. The expanded search added JF799825. Both found exactly three lines: own backbone, native name and scope.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence statements are bounded to inspected repository surfaces, not all external evidence.

Zero strain count refers to represented culture inventory, not isolate existence or culturability. Empty optional slots are appropriate without exact supporting joins. The partial marker is optional taxon context, not a missing required genome. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, complete lineage, source count and seed audit are supported. The browser access issue was resolved by direct HTML inspection.

## Recommended Edits

No generated-record correction is justified. Preserve TGR23, species rank, the independently verified Lysobacter lineage, `SEEDED` status and history. Do not add the partial marker as a genome or transfer biological claims from another isolate.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not a direct generated-YAML edit. Optional marker/citation enrichment needs a supported taxon-level representation rather than an invented strain container.

## Follow-up Checks

For authorized enrichment, confirm exact TGR23 linkage and retain JF799825.1's version. Require explicit assembly and organism/strain evidence before adding a genome. After source changes, run the documented seed canary, schema/strict/history checks, corpus reproduction and QC. A future primary paper needs an independent claim-level review.

## Additional Notes

- YAML SHA-256: `26a0a5ccfc92bff8975b241032436dbc59a34be399fdf21fc6d0a13ecc381de1`.
- JF799825.1 lowercase sequence SHA-256: `781bcc645f1173414d9d6e27edd014d8bee66f3d76965100338938732928e218`.
- `data/taxa/PATHS.tsv:15326` and `curation/seed_scope.tsv:322990` uniquely resolve the target. Scope addition is 2026-09-13; the seed event preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was written for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened or review status promoted.
