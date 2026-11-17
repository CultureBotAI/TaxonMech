# YAML Record Review: Paenibacillus sp. THGR15

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_sp_thgr15.yaml`
- Started UTC: 2026-10-10T04:59:28Z
- Finished UTC: 2026-10-10T05:02:18Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:1037509` denotes Paenibacillus sp. THGR15, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:185978`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`. Ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event are represented. No synonym, formal nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph is asserted.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/paenibacillus_sp_thgr15.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/paenibacillus_sp_thgr15.yaml --out /private/tmp/taxonmech-thgr15-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, code, complete lineage, empty source synonyms, seven inventories, unique index/scope resolution, attestation and exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- Both matching native catalog rows were read completely. Live NCBI EFetch/Datasets taxonomy, nucleotide search and complete marker annotations were inspected. The web reader failed on the taxonomy-browser URL; direct retrieval succeeded, and all 74 parsed HTML text lines were inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`. Focused passes do not establish corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222781` agrees with the directly read [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037509&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037509&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037509). Parent 185978, species rank and code 11 agree; Datasets includes root 1.

The complete root-first chain is supported: root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Paenibacillaceae, Paenibacillus and unclassified Paenibacillus. Retain Caryophanales (1385) as the order and Paenibacillaceae (186822) as the family; these match the inspected authority. The direct parent is correctly `NO_RANK`.

`data/catalog/ncbi_names-0005.jsonl.gz:32419` supplies the exact scientific name with an empty unique-name qualifier. Neither backbone nor EFetch supplies alternate names. The NCBI species-ranked placeholder and a sequence strain qualifier are compatible metadata layers, not a rank conflict. Exact grounding does not establish formal species nomenclature or type status. Other THGR-designated isolates cannot supply THGR15's identity or functional evidence.

## Evidence

The one-NAME NCBITAXON assertion and 2026-09-13 snapshot note match the pinned source. No additional own source-count inventory row was found.

The exact nucleotide query returns one entry, UID 334361444: [JF799812.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799812.1), a 750-base partial 16S rRNA gene with both ends marked partial. Its source explicitly links Paenibacillus sp. THGR15, strain THGR15, `taxon:1037509` and wetland soil. Declared and observed lengths agree, with alphabet `acgt`. This is marker-to-taxon evidence, not a genome or culture-deposit association.

The sole reference is a direct submission dated 10-Apr-2011 by Li, Liu, Shao and Sun at Hebei University. No DOI, PMID, collection country, coordinates or collection date is supplied. The institutional address and submission date are not sampling metadata. Shared authors or isolation-source wording does not transfer another isolate's biological claims.

The fully read native row at `data/catalog/ncbi_genbank-0009.jsonl.gz:7565` identifies GCA_010375095.1, Francisella tularensis subsp. holarctica, taxon 119857, species taxon 263, strain 17T1201, BioSample SAMN12576386 and BioProject PRJNA560345. The numeric search matched assembly name ASM1037509v1 and its FTP path, not this taxon. This unrelated assembly-name collision is not a THGR15 genome.

Datasets omits an assembly-count field rather than returning an explicit zero. No target genome was established from the inspected evidence. Exact name/accession searches supplied taxonomy-tree listings but no direct experimental publication; the NCBI-excluded name query was empty. These bounded searches do not rule out additional literature.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The bounded taxon-ID/slug/designation search and its expansion with JF799812 each found four lines: own backbone, native name and scope, plus the fully inspected off-target assembly row.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence statements apply only to the inspected repository surfaces.

Zero strain count describes represented culture inventory, not isolate existence or culturability. Empty optional slots are appropriate without exact supporting joins. The partial marker is optional context, not a missing required genome or phenotype field. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, complete lineage, source count and seed audit are supported. The unrelated assembly-name collision does not justify a missing-association finding.

## Recommended Edits

No generated-record correction is justified. Preserve THGR15, species rank, the complete Paenibacillus lineage, `SEEDED` status and existing history. Do not import the unrelated assembly, promote the marker to a genome or infer sampling locality from an institutional address.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not a direct generated-YAML edit. Optional marker enrichment needs a supported taxon-level representation rather than an invented culture-strain container.

## Follow-up Checks

For authorized enrichment, reconfirm exact THGR15 linkage and retain JF799812.1's version. Require explicit assembly and organism/strain evidence before adding a genome, and direct isolate-linked evidence for a functional claim. After maintained-source changes, run the documented seed canary, schema/strict/history checks, corpus reproduction and QC.

## Additional Notes

- YAML SHA-256: `b9464e596965d81cd8b7a9549ec8d2636e5b8f2ba771298e6c95a14539e2fec5`.
- JF799812.1 lowercase sequence SHA-256: `564707147306591768137dceab17a1006edffb6b11cedd4eecd6da65d97ff7dc`.
- `data/taxa/PATHS.tsv:15334` and `curation/seed_scope.tsv:322998` uniquely resolve this target. Scope addition is 2026-09-13; the seed event preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened, curation event appended or review status promoted.
