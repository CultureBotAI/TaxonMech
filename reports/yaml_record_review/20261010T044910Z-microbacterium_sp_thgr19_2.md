# YAML Record Review: Microbacterium sp. THGR19-2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microbacterium_sp_thgr19_2.yaml`
- Started UTC: 2026-10-10T04:46:50Z
- Finished UTC: 2026-10-10T04:49:10Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. `NCBITaxon:1037505` denotes Microbacterium sp. THGR19-2, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2609290`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`. It represents ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. No synonym, nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph is asserted.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/microbacterium_sp_thgr19_2.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/microbacterium_sp_thgr19_2.yaml --out /private/tmp/taxonmech-thgr19-2-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured source comparisons verified identity, genetic code, complete lineage, empty source synonyms, seven inventories, unique index/scope resolution, attestation and exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- Both matching native catalog rows were read in full. Live NCBI EFetch/Datasets taxonomy, nucleotide search and complete marker annotations were inspected. After the web reader failed on the taxonomy-browser URL, direct HTML retrieval succeeded; all 74 parsed text lines were read.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`. Focused passes do not establish corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222777` agrees with the directly read [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037505&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037505&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037505). Parent 2609290, species rank and code 11 match; Datasets includes root 1.

The root-first chain matches completely: root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Microbacteriaceae, Microbacterium and unclassified Microbacterium. The direct parent is correctly `NO_RANK`.

`data/catalog/ncbi_names-0005.jsonl.gz:32415` is the exact scientific name, with an empty unique-name qualifier. Neither backbone nor EFetch supplies alternate names. A species-ranked NCBI placeholder and a sequence strain qualifier are compatible metadata layers, not a rank conflict. Exact grounding does not establish formal nomenclature or type status. Preserve the complete THGR19-2 designation; other Microbacterium isolates cannot supply its identity or functional evidence merely by sharing a genus or similar designation.

## Evidence

The one-NAME NCBITAXON assertion and 2026-09-13 snapshot note match the pinned source. No additional own source-count inventory row was found.

The exact nucleotide query returns one entry, UID 334361437: [JF799805.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799805.1), a 771-base partial 16S rRNA gene with both ends marked partial. The source explicitly links Microbacterium sp. THGR19-2, strain THGR19-2, `taxon:1037505` and wetland soil. Declared and observed lengths agree, with alphabet `acgt`. The accession is a marker, not a genome or culture-deposit identifier.

The sole reference is a direct submission dated 10-Apr-2011, by Liu, Shao, Li and Sun at Hebei University. No DOI, PMID, collection country, coordinates or collection date is supplied. The institutional address and submission date are not sampling metadata. Neither shared submitters nor a shared isolation-source phrase transfers another isolate's biological claims.

The full row at `data/catalog/ncbi_genbank-0009.jsonl.gz:7562` identifies GCA_010375055.1, Francisella tularensis subsp. holarctica, taxon 119857, species taxon 263, strain 17T1429, BioSample SAMN12576388 and BioProject PRJNA560345. The search matched assembly name ASM1037505v1 and its FTP path, not the target taxon. This unrelated assembly-name collision is not a THGR19-2 genome association.

Datasets omits an assembly-count field rather than returning an explicit zero. No target genome was established by the inspected sources. Exact name searches returned taxonomy-tree listings, while the NCBI-excluded name query returned no result; the accession search supplied no additional direct source. No experimental publication was established by these bounded searches, which do not exclude additional literature.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Bounded taxon ID, slug and designation, including separator variants, were searched, then JF799805 was added. Both searches found four lines: own backbone, native name and scope, plus the inspected unrelated assembly row.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence statements are bounded to the inspected repository surfaces.

Zero strain count describes represented culture inventory, not isolate existence or culturability. Empty optional fields are appropriate without exact supporting joins. The partial marker is optional context, not a missing required genome or phenotype field. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, full lineage, source count and seed audit are supported. The unrelated assembly hit is not a missing association.

## Recommended Edits

No generated-record correction is justified. Retain THGR19-2, species rank, the full Microbacterium lineage, `SEEDED` status and existing history. Do not import the unrelated assembly, represent the marker as a genome, or infer a collection locality from the submitters' address.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not a direct YAML edit. Optional marker enrichment needs a supported taxon-level representation rather than an invented culture-strain container.

## Follow-up Checks

For authorized enrichment, reconfirm exact THGR19-2 linkage and retain JF799805.1's version. Require explicit assembly and organism/strain evidence for a genome, and direct isolate-linked evidence for a functional claim. After maintained-source changes, run the documented seed canary, schema/strict/history checks, corpus reproduction and QC.

## Additional Notes

- YAML SHA-256: `9ad62586ff49220057cdb1e5c160e56aeb084077d5efcdacfba4cca386462225`.
- JF799805.1 lowercase sequence SHA-256: `301a05de603127ad1d24ceb508705e17e2e8256e4a0ff9327f23a39305ddabc9`.
- `data/taxa/PATHS.tsv:15330` and `curation/seed_scope.tsv:322994` uniquely resolve this target. Scope addition is 2026-09-13; the seed event preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened, curation event appended or review status promoted.
