# YAML Record Review: Microbacterium sp. THGR30

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microbacterium_sp_thgr30.yaml`
- Started UTC: 2026-10-10T04:49:55Z
- Finished UTC: 2026-10-10T04:52:04Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:1037506` denotes Microbacterium sp. THGR30, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2609290`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`. Ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event are represented. The record asserts no synonym, formal nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/microbacterium_sp_thgr30.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/microbacterium_sp_thgr30.yaml --out /private/tmp/taxonmech-thgr30-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, code, complete lineage, empty source synonyms, seven inventories, unique index/scope resolution, attestation and exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- Both matching native catalog rows were read completely. Live NCBI EFetch/Datasets taxonomy, nucleotide search and complete marker annotations were inspected. The web reader could not open the taxonomy-browser URL; direct retrieval succeeded, and all 74 parsed HTML text lines were inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`. Focused checks do not establish full-corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222778` agrees with the directly inspected [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037506&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037506&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037506). Parent 2609290, rank and code 11 agree; Datasets includes root 1.

The complete root-first lineage is correct: root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Microbacteriaceae, Microbacterium and unclassified Microbacterium. The direct parent is `NO_RANK`.

`data/catalog/ncbi_names-0005.jsonl.gz:32416` supplies the exact scientific name and an empty unique-name qualifier. Neither backbone nor EFetch provides an alternate name. The species-ranked NCBI placeholder and sequence strain qualifier are compatible metadata layers. Exact grounding does not imply formal species nomenclature or type-culture status. Other THGR-designated isolates are not interchangeable with THGR30.

## Evidence

The one-NAME NCBITAXON assertion and 2026-09-13 snapshot note match the pinned source. No additional own source-count inventory row was found.

The exact nucleotide query returns one entry, UID 334361435: [JF799803.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799803.1), a 771-base partial 16S rRNA gene with both ends marked partial. The source explicitly names Microbacterium sp. THGR30, strain THGR30, `taxon:1037506` and wetland soil. Declared and observed lengths agree, with alphabet `acgt`. This accession supports a marker-to-taxon link, not a genome or culture-deposit association.

Its sole reference is a direct submission dated 10-Apr-2011 by Liu, Shao, Li and Sun at Hebei University. No DOI, PMID, collection country, coordinates or collection date is supplied. The institutional address and submission date are not sampling metadata. Shared authors, genus or habitat wording does not transfer evidence from a different isolate.

The full native row at `data/catalog/ncbi_genbank-0009.jsonl.gz:7563` identifies GCA_010375065.1, Francisella tularensis subsp. holarctica, taxon 119857, species taxon 263, strain 17T1131, BioSample SAMN12576384 and BioProject PRJNA560345. The numeric search matched assembly name ASM1037506v1 and its FTP path, not this taxon. This off-target assembly is not a THGR30 genome.

Datasets omits an assembly-count field instead of returning an explicit zero. No target genome was established from the inspected evidence. Exact name/accession searches supplied taxonomy pages but no direct experimental publication; the NCBI-excluded name query was empty. This bounded search does not prove that no additional literature exists.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Both the bounded taxon-ID/slug/designation search and the expanded search adding JF799803 found four lines: own backbone, native name and scope, plus the inspected unrelated assembly row.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence findings apply only to the inspected repository surfaces.

Zero strain count means zero represented culture-inventory entries, not no isolate or no culturability. Empty optional slots are appropriate without exact supporting joins. A partial marker is optional context, not a missing required genome or phenotype field. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, full lineage, source count and seed audit are supported. The unrelated assembly-name collision does not establish a missing association.

## Recommended Edits

No generated-record correction is justified. Preserve THGR30, species rank, the full Microbacterium lineage, `SEEDED` status and existing history. Do not import the unrelated assembly, promote the marker to a genome or infer a collection locality from an institutional address.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not a direct generated-YAML edit. Optional marker enrichment requires a supported taxon-level representation, not an invented culture-strain container.

## Follow-up Checks

For authorized enrichment, reconfirm exact THGR30 linkage and retain JF799803.1's version. Require explicit assembly and organism/strain evidence before adding a genome, and direct isolate-linked evidence for a functional claim. After maintained-source changes, run the documented seed canary, schema/strict/history checks, corpus reproduction and QC.

## Additional Notes

- YAML SHA-256: `8e56a1648aee1dad177b9d7c5d22897df860944d25462c242dec3ae8cfb8698d`.
- JF799803.1 lowercase sequence SHA-256: `2659ccda12d36a7886f5e7310ac271503855804c52b7d698b8d16418a8afc92c`.
- `data/taxa/PATHS.tsv:15331` and `curation/seed_scope.tsv:322995` uniquely resolve this record. Scope addition is 2026-09-13; the seed event preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened, curation event appended or review status promoted.
