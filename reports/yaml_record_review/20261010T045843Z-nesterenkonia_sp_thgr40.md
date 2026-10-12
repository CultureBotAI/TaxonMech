# YAML Record Review: Nesterenkonia sp. THGR40

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nesterenkonia_sp_thgr40.yaml`
- Started UTC: 2026-10-10T04:56:34Z
- Finished UTC: 2026-10-10T04:58:43Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. `NCBITaxon:1037508` denotes Nesterenkonia sp. THGR40, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2629769`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`. It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. No synonym, formal nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph is asserted.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/nesterenkonia_sp_thgr40.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/nesterenkonia_sp_thgr40.yaml --out /private/tmp/taxonmech-thgr40-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, code, every ancestor, empty source synonyms, seven inventories, unique index/scope resolution, attestation and exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- Both matching native catalog rows were read completely. Live NCBI EFetch/Datasets taxonomy, nucleotide search and complete marker annotations were inspected. The web reader failed on the taxonomy-browser URL; direct retrieval succeeded, and all 74 parsed HTML text lines were inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`. Focused passes do not establish corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222780` agrees with the directly inspected [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037508&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037508&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037508). Parent 2629769, species rank and code 11 agree; Datasets includes root 1.

The complete root-first lineage matches: root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Micrococcaceae, Nesterenkonia and unclassified Nesterenkonia. Family Micrococcaceae (1268) and genus Nesterenkonia (57494) are correct; do not substitute the Microbacteriaceae lineage of nearby records. The direct parent is correctly `NO_RANK`.

`data/catalog/ncbi_names-0005.jsonl.gz:32418` contains the exact scientific name with an empty unique-name qualifier. Neither backbone nor EFetch supplies alternate names. The NCBI species-ranked placeholder and sequence strain qualifier are compatible metadata layers. Exact grounding does not establish formal species nomenclature or type status. Other THGR-designated isolates are not interchangeable with THGR40.

## Evidence

The one-NAME NCBITAXON assertion and 2026-09-13 snapshot note match the pinned source. No additional own source-count inventory row was found.

The exact nucleotide query returns one entry, UID 334361438: [JF799806.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799806.1), a 779-base partial 16S rRNA gene with both ends marked partial. Its source explicitly links Nesterenkonia sp. THGR40, strain THGR40, `taxon:1037508` and wetland soil. Declared and observed lengths agree, with alphabet `acgt`. This supports a marker-to-taxon link, not a genome or culture-deposit association.

The sole reference is a direct submission dated 10-Apr-2011 by Liu, Shao, Li and Sun at Hebei University. No DOI, PMID, collection country, coordinates or collection date is supplied. The institutional address and submission date are not sampling metadata. Shared submitters or habitat wording does not transfer another isolate's biological claims.

The fully read row at `data/catalog/ncbi_genbank-0066.jsonl.gz:37334` identifies GCA_982811275.1, uncultured bacterium, taxon 77133, isolate FORT21-1_SAMEA101260168_MAG_00000016, BioSample SAMEA122255188 and BioProject PRJEB72992. The numeric search matched `genome_size: 1037508`, not a taxon identifier. The row describes a metagenome-derived assembly with undefined genus and does not establish any THGR40 association. It must not be imported as a target genome merely because its size equals the target taxon number.

Datasets omits an assembly-count field rather than explicitly returning zero. No target genome was established from the inspected evidence. Exact name/accession searches supplied a taxonomy-tree listing but no direct experimental publication; the NCBI-excluded name query was empty. These bounded searches do not rule out additional literature.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The bounded taxon-ID/slug/designation search and its expansion with JF799806 each found four lines: own backbone, native name and scope, plus the inspected unrelated assembly row.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence statements apply only to the inspected repository surfaces.

Zero strain count describes represented culture inventory, not isolate existence or culturability. Empty optional slots are appropriate without exact supporting joins. The partial marker is optional context, not a missing required genome or phenotype field. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, full lineage, source count and seed audit are supported. The unrelated genome-size collision does not establish a missing association.

## Recommended Edits

No generated-record correction is justified. Preserve THGR40, species rank, the complete Nesterenkonia lineage, `SEEDED` status and existing history. Do not import the unrelated metagenome assembly, promote the marker to a genome or infer sampling locality from an institutional address.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not a direct generated-YAML edit. Optional marker enrichment needs a supported taxon-level representation rather than an invented culture-strain container.

## Follow-up Checks

For authorized enrichment, reconfirm exact THGR40 linkage and retain JF799806.1's version. Require explicit assembly and organism/strain evidence for a genome, and direct isolate-linked evidence for a functional claim. After maintained-source changes, run the documented seed canary, schema/strict/history checks, corpus reproduction and QC.

## Additional Notes

- YAML SHA-256: `772881d753eb738530400ede760bfb3455e45c0b6a2071c2f8f6b63d437e8020`.
- JF799806.1 lowercase sequence SHA-256: `3b3af79eca840e0f3645db06fb3418a8ca399e811c5218a4a25cb2ae33557579`.
- `data/taxa/PATHS.tsv:15333` and `curation/seed_scope.tsv:322997` uniquely resolve this target. Scope addition is 2026-09-13; the seed event preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened, curation event appended or review status promoted.
