# YAML Record Review: Burkholderia sp. THGR19-3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_thgr19_3.yaml`
- Started UTC: 2026-10-10T04:25:27Z
- Finished UTC: 2026-10-10T04:27:37Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. `NCBITaxon:1037500` denotes Burkholderia sp. THGR19-3, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2613784`, genetic code 11, grounding `EXACT`, mapping status `SEEDED`. It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. No synonym, nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph is asserted. Preserve the full THGR19-3 designation.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_thgr19_3.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_thgr19_3.yaml --out /private/tmp/taxonmech-thgr19-3-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, genetic code, every ancestor, empty source synonyms, seven inventories, unique index/scope resolution and exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- Full native name row, live NCBI EFetch/Datasets taxonomy, nucleotide search and complete marker annotations were inspected. Marker length and hash were checked. The web reader failed on two taxonomy-browser URLs; a direct public HTML read then succeeded and all 74 parsed text lines were inspected. This was an access-path failure, not an unresolved identity conflict.
- No DOI or PMID is cited by the YAML or marker submission. Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222772` agrees with the directly read [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037500&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037500&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037500). EFetch confirms parent 2613784 and code 11; Datasets includes root 1.

The complete root-first chain matches: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Burkholderiaceae, Burkholderia and unclassified Burkholderia. Preserve the distinct kingdom Pseudomonadati (3379134) and phylum Pseudomonadota (1224), the genus Burkholderia (32008), and the unranked parent 2613784. No evidence supports replacing this with another genus or a named Burkholderia species.

`data/catalog/ncbi_names-0005.jsonl.gz:32410` is the exact scientific name with an empty unique-name qualifier. Neither backbone nor EFetch supplies alternate names. The species-ranked NCBI placeholder and sequence strain qualifier are different metadata layers. Exact grounding does not establish formal nomenclature, type status or a phenotype. THGR19-3 must not be reduced to THGR19 or conflated with another isolate.

## Evidence

The one-NAME NCBITAXON assertion and 2026-09-13 snapshot note match the pinned source. No additional own source-count inventory row was found.

The nucleotide query returns one entry, UID 334361450, [JF799818.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799818.1), a 769-base partial 16S rRNA gene with both ends marked partial. The source explicitly links Burkholderia sp. THGR19-3, strain THGR19-3, `taxon:1037500` and wetland soil. Declared and observed lengths agree, with alphabet `acgt`. This is marker-to-taxon evidence, not a complete genome or culture-deposit accession.

The sole sequence reference is a direct submission dated 10-Apr-2011 by Li, Liu, Shao and Sun at Hebei University. It supplies no DOI, PMID, collection country, coordinates or collection date. The institutional address and submission date are not sampling metadata. No Hetao locality is present in this marker's source qualifiers; a locality supplied for a different isolate cannot be transferred here.

Bounded exact-name web search returned NCBI taxonomy-tree pages, not a target research paper; accession search returned no results. This does not establish that no target publication exists. Taxonomy-tree co-membership and the browser's general database citation do not establish shared strain identity or target experimental evidence.

Datasets omits an assembly-count field rather than explicitly returning zero. No target genome was established from the inspected evidence. Shared submitters or wetland-soil wording does not justify importing a genome, culture deposit or phenotype from another isolate.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded taxon ID, slug and designation. The expanded search added JF799818. Both found exactly three lines: own backbone, native name and scope.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence statements are bounded to inspected repository surfaces, not all external evidence.

Zero strain count refers to represented culture inventory, not isolate existence or culturability. Empty optional slots are appropriate without exact supporting joins. The partial marker is optional taxon context, not a missing required genome. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, complete lineage, source count and seed audit are supported. The browser access issue was resolved by direct HTML inspection.

## Recommended Edits

No generated-record correction is justified. Preserve THGR19-3, species rank, the independently verified Burkholderia lineage, `SEEDED` status and history. Do not add the partial marker as a genome, infer a collection locality, or transfer biological claims from another isolate.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not a direct generated-YAML edit. Optional marker/citation enrichment needs a supported taxon-level representation rather than an invented strain container.

## Follow-up Checks

For authorized enrichment, confirm exact THGR19-3 linkage and retain JF799818.1's version. Require explicit assembly and organism/strain evidence before adding a genome. After source changes, run the documented seed canary, schema/strict/history checks, corpus reproduction and QC. A future primary paper needs an independent claim-level review.

## Additional Notes

- YAML SHA-256: `6fd001582cce1f0eb92f23a0911e4490b0c117f337f4a3ffba2f3ebe29b13048`.
- JF799818.1 lowercase sequence SHA-256: `9475765f6886b6cdf51508dbe8f932816e2d40a16fc22e539b0ebb9a8935d8ec`.
- `data/taxa/PATHS.tsv:15325` and `curation/seed_scope.tsv:322989` uniquely resolve the target. Scope addition is 2026-09-13; the seed event preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was written for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened or review status promoted.
