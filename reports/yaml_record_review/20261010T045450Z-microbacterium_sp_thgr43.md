# YAML Record Review: Microbacterium sp. THGR43

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microbacterium_sp_thgr43.yaml`
- Started UTC: 2026-10-10T04:52:45Z
- Finished UTC: 2026-10-10T04:54:50Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:1037507` denotes Microbacterium sp. THGR43, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2609290`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`. It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. No synonym, formal nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph is asserted.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/microbacterium_sp_thgr43.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/microbacterium_sp_thgr43.yaml --out /private/tmp/taxonmech-thgr43-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, code, complete lineage, empty source synonyms, seven inventories, unique index/scope resolution, attestation and exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- Both matching native catalog rows were read completely. Live NCBI EFetch/Datasets taxonomy, nucleotide search and complete marker annotations were inspected. The web reader failed on the taxonomy-browser URL; direct public retrieval succeeded, and all 74 parsed HTML text lines were read.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`. Focused passes do not establish corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222779` agrees with the directly read [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037507&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037507&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037507). Parent 2609290, species rank and code 11 agree; Datasets includes root 1.

The root-first lineage matches completely: root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Microbacteriaceae, Microbacterium and unclassified Microbacterium. The direct parent is correctly `NO_RANK`.

`data/catalog/ncbi_names-0005.jsonl.gz:32417` contains the exact scientific name with an empty unique-name qualifier. Neither backbone nor EFetch supplies alternate names. NCBI's species-ranked placeholder and the sequence strain qualifier are compatible metadata layers, not a rank conflict. Exact grounding does not establish formal species nomenclature or type status. Preserve THGR43 as the complete designation; a shared genus or THGR prefix is not an identity join.

## Evidence

The one-NAME NCBITAXON assertion and 2026-09-13 snapshot note match the pinned source. No additional own source-count inventory row was found.

The exact nucleotide query returns one entry, UID 334361436: [JF799804.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799804.1), a 770-base partial 16S rRNA gene with both ends marked partial. The source explicitly links Microbacterium sp. THGR43, strain THGR43, `taxon:1037507` and wetland soil. Declared and observed lengths agree, with alphabet `acgt`. This supports a marker-to-taxon relationship, not a genome or culture-deposit association.

Its sole reference is a direct submission dated 10-Apr-2011 by Liu, Shao, Li and Sun at Hebei University. No DOI, PMID, collection country, coordinates or collection date is supplied. The institutional address and submission date are not sampling metadata. Shared submitters or isolation-source wording cannot transfer another isolate's biological claims to THGR43.

The fully read native row at `data/catalog/ncbi_genbank-0009.jsonl.gz:7564` identifies GCA_010375075.1, Francisella tularensis subsp. holarctica, taxon 119857, species taxon 263, strain 17T1184, BioSample SAMN12576385 and BioProject PRJNA560345. The numeric search matched assembly name ASM1037507v1 and its FTP path, not the target taxon. This unrelated assembly-name collision is not a THGR43 genome.

Datasets omits an assembly-count field rather than explicitly returning zero. No target genome was established from the inspected evidence. Exact name/accession searches supplied taxonomy pages but no direct experimental publication; the NCBI-excluded name query was empty. These bounded searches do not rule out additional literature.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The bounded taxon-ID/slug/designation search and its expansion with JF799804 each found four lines: own backbone, native name and scope, plus the inspected off-target assembly row.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence statements are restricted to the inspected repository surfaces.

Zero strain count describes represented culture inventory, not isolate existence or culturability. Empty optional slots are appropriate without exact supporting joins. A partial marker is optional context, not a missing required genome or phenotype field. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, full lineage, source count and seed audit are supported. The unrelated assembly-name match does not justify a missing-association finding.

## Recommended Edits

No generated-record correction is justified. Retain THGR43, species rank, the full Microbacterium lineage, `SEEDED` status and existing history. Do not import the unrelated assembly, treat the marker as a genome or infer sampling locality from an institutional address.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not a direct generated-YAML edit. Optional marker enrichment needs a supported taxon-level representation rather than an invented culture-strain container.

## Follow-up Checks

For authorized enrichment, reconfirm exact THGR43 linkage and retain JF799804.1's version. Require explicit assembly and organism/strain evidence before adding a genome, and direct isolate-linked evidence for any functional claim. After maintained-source changes, run the documented seed canary, schema/strict/history checks, corpus reproduction and QC.

## Additional Notes

- YAML SHA-256: `6367376565faeb9b789c6267bf69dc36527233a347e5c4e7c4e330a4d6ef6a8d`.
- JF799804.1 lowercase sequence SHA-256: `b83540d8f34d02a863a79d9dcb9559fac3cf1255f7d206519a1896d01b49a39c`.
- `data/taxa/PATHS.tsv:15332` and `curation/seed_scope.tsv:322996` uniquely resolve this target. Scope addition is 2026-09-13; the seed event preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened, curation event appended or review status promoted.
