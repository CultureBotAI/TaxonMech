# YAML Record Review: Arthrobacter sp. THGR17

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_thgr17.yaml`
- Started UTC: 2026-10-10T03:39:38Z
- Finished UTC: 2026-10-10T03:41:41Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:1037486` denotes Arthrobacter sp. THGR17, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:235627`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`.

It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. No synonyms, formal nomenclature, GTDB mappings, culture deposits, genomes, phenotypes or causal graph are asserted. THGR17 must not be conflated with other TGR/THGR isolates or named Arthrobacter species.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/arthrobacter_sp_thgr17.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/arthrobacter_sp_thgr17.yaml --out /private/tmp/taxonmech-thgr17-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Complete structured source comparisons verified identity, genetic code, every ancestor, empty synonyms, seven source inventories, unique index/scope resolution and the exact seed reason. The backbone contains no immediate child. Own type-material, merged-ID and dropped-record inventories have no rows.
- The complete native name and three assembly-catalog search hits were read. Live EFetch/Datasets taxonomy, nucleotide search and complete marker annotations were inspected; marker length and hash were checked.
- Not available: both attempted NCBI taxonomy browser URLs failed in the web reader. The two structured taxonomy endpoints succeeded. No DOI or PMID is cited by the YAML or the marker submission.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222758` agrees with [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037486&retmode=xml) on the exact name, species rank, parent 235627 and genetic code 11. [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037486) confirms the lineage including root 1.

The root-first chain is root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Micrococcaceae, Arthrobacter and unclassified Arthrobacter. Every label, rank and identifier matches the pinned backbone. The final grouping retains `NO_RANK`; no assignment to a named species is justified.

`data/catalog/ncbi_names-0005.jsonl.gz:32396` supplies the exact scientific name and an empty unique-name qualifier. Neither the backbone nor EFetch supplies an alternate name. The species-ranked NCBI placeholder and a sequence strain qualifier describe different metadata layers, not contradictory ranks. Exact grounding does not establish nomenclatural status, type material or phenotype. The broad BLAST category is not a strain-specific Gram-stain or GC-content measurement.

## Evidence

The one-NAME NCBITAXON attestation and 2026-09-13 snapshot note match the pinned source. No additional own source-count inventory row was found.

The NCBI nucleotide query returns one entry, UID 334361434, [JF799802.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799802.1). This is a 760-base partial 16S rRNA sequence, with both ends marked partial. Its source explicitly names Arthrobacter sp. THGR17, strain THGR17, `taxon:1037486` and wetland soil. Declared and observed lengths agree and the sequence alphabet is `acgt`. The marker supports the exact sequence-to-taxon relationship, not a whole genome or culture deposit.

The sole reference is a direct submission dated 10-Apr-2011 by Liu, Shao, Li and Sun at Hebei University. No DOI, PMID, collection country, coordinates or collection date is supplied. The submitter's institutional address and submission date must not become sampling metadata. Bounded exact-name and accession web searches returned no results; this does not prove that no publication exists.

Three assembly-catalog hits belong to Escherichia coli ATCC 11230, NCBI taxon 562, not THGR17:

- `data/catalog/gtdb_genomes-0003.jsonl.gz:24637`: `RS_GCF_010374865.1`, GTDB classification `s__Escherichia coli`.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:7553`: `GCA_010374865.1`.
- `data/catalog/ncbi_refseq-0002.jsonl.gz:41290`: paired identical `GCF_010374865.1`.

The matching string is assembly name `ASM1037486v1`, not the taxon field. None supports a target genome, GTDB mapping or ATCC association. The unrelated assembly's PMID 32021174 was not treated as a THGR17 citation and was not resolved for this review. Datasets omits an assembly-count field rather than explicitly returning zero; no target assembly was established from the inspected evidence.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded taxon ID, slug and designation. The expanded search added JF799802. Both returned six lines: own backbone/name/scope and the three unrelated assembly rows.

Complete source-inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were fully parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence statements apply to the inspected repository surfaces, not the entire literature.

Zero inventoried strains does not mean the isolate does not exist or cannot be cultured. Empty optional mappings, nomenclature, deposits, genomes and graph are appropriate without exact supporting joins. The partial marker is optional taxon context, not a missing required genome. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, lineage, source count and seed audit are supported. The apparent genome hits are demonstrably non-target entries.

## Recommended Edits

No generated-record correction is justified. Preserve the exact THGR17 name, species rank, NCBI lineage, `SEEDED` status and history. Do not turn the partial marker into a genome, import the E. coli deposit, or transfer biological claims from another Arthrobacter isolate.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not a direct generated-YAML edit. Optional marker enrichment needs a supported taxon-level representation rather than an invented strain container.

## Follow-up Checks

For authorized enrichment, confirm exact THGR17 linkage and preserve JF799802.1's accession version. Use typed taxon fields rather than assembly-name digit matches. A genome assertion needs an explicit assembly and organism/strain link.

After an authorized source change, run the documented seed canary, schema/strict/history checks, corpus reproduction and QC. A future primary paper would require independent claim-level assessment. The browser can be retried if needed; identity was checked through structured NCBI sources.

## Additional Notes

- YAML SHA-256: `1177d66855f9f7a04a2f92038f31ecf89922f6d6583d5fb384f11445c80faf13`.
- JF799802.1 lowercase sequence SHA-256: `38473b9c9c00ed817ec564c425129b951b5d3da1a5e76e69315952356969cc5f`.
- `data/taxa/PATHS.tsv:15311` and `curation/seed_scope.tsv:322975` uniquely resolve the target. Scope addition is 2026-09-13; the seed event preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was written for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed; no Eukaryota YAML was opened or review status promoted.
