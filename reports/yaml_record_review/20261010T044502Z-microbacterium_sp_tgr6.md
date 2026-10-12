# YAML Record Review: Microbacterium sp. TGR6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microbacterium_sp_tgr6.yaml`
- Started UTC: 2026-10-10T04:41:16Z
- Finished UTC: 2026-10-10T04:45:02Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:1037504` denotes Microbacterium sp. TGR6, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2609290`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`. Ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event are represented. The record asserts no synonym, formal nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/microbacterium_sp_tgr6.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/microbacterium_sp_tgr6.yaml --out /private/tmp/taxonmech-tgr6-20261010-validation.tsv --workers 1`: one file, zero errors; output TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons checked identity, code, every ancestor, source synonyms, seven inventories, unique index/scope resolution, the NCBITAXON attestation and exact seed reason. No immediate child, own type-material, merged-ID or dropped-record row was found.
- Complete matching native catalog rows, live NCBI EFetch/Datasets taxonomy, nucleotide search and full marker annotations were inspected. The web reader failed on the taxonomy-browser URL; a direct public HTML read succeeded, and all 74 parsed text lines were inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`. Focused checks are not a claim that these full-corpus gates passed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222776` matches the directly inspected [NCBI taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037504&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037504&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037504). Parent 2609290, species rank and code 11 agree; Datasets includes root 1.

The root-first chain agrees in full: root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Microbacteriaceae, Microbacterium and unclassified Microbacterium. The final parent is correctly `NO_RANK`; it is not an alternate species identity.

`data/catalog/ncbi_names-0005.jsonl.gz:32414` contains the exact scientific name, with an empty unique-name qualifier. Neither the backbone nor EFetch supplies alternate names. NCBI's species-ranked placeholder and a sequence's strain qualifier are compatible metadata layers. Exact grounding does not imply formally established species nomenclature or a type culture. Similar designations such as TG6, or other Microbacterium isolates, must not be merged with TGR6 without explicit identity evidence.

## Evidence

The one-NAME NCBITAXON assertion and 2026-09-13 snapshot note match the pinned backbone. No additional own source-count inventory row was found.

The exact taxon nucleotide query returns one entry, UID 334361470: [JF799838.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799838.1), a 790-base partial 16S rRNA gene with both ends marked partial. Its source explicitly links Microbacterium sp. TGR6, strain TGR6, `taxon:1037504` and wetland soil. Declared and observed lengths agree, with alphabet `acgt`. This is marker-to-taxon support, not a genome or culture-deposit accession.

The marker has one direct-submission reference, dated 10-Apr-2011, by Li, Liu, Shao and Sun at Hebei University. No DOI, PMID, collection country, coordinates or collection date is supplied. The submitters' address and submission date do not establish sampling locality or time. Shared submitters or habitat wording would not justify transferring another isolate's claims.

The other native catalog hit, `data/catalog/ncbi_genbank-0009.jsonl.gz:7561`, matches the assembly name ASM1037504v1 and its FTP path, not taxon 1037504. The full row identifies GCA_010375045.1, Francisella tularensis subsp. holarctica, taxon 119857, species taxon 263, strain 17T1202, BioSample SAMN12576387 and BioProject PRJNA560345. This is an unrelated assembly-name collision, not a TGR6 genome association.

Datasets omits an assembly-count field rather than explicitly returning zero. No target genome was established by the inspected sources. Exact genus/designation web searching returned taxonomy-tree listings; separate accession and NCBI-excluded name searches returned no results. No direct experimental publication was established by these bounded searches, which do not exclude other literature.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Bounded taxon ID, slug and designation searches, then an expanded search including JF799838, each found four lines: own backbone, native name and scope, plus the fully inspected unrelated assembly row.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence statements are restricted to the inspected repository surfaces.

Zero strain count describes the represented culture inventory, not isolate existence or culturability. Empty optional slots are appropriate without exact supporting joins. The partial marker is optional context, not a missing required genome or phenotype field. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, complete lineage, source count and seed audit are supported. The unrelated assembly-name hit does not justify a missing-association finding.

## Recommended Edits

No generated-record correction is justified. Preserve TGR6, species rank, the complete Microbacterium lineage, `SEEDED` status and existing history. Do not import the unrelated assembly, treat the marker as a genome, or infer a collection locality from the submitter's address.

Any separately authorized correction belongs in maintained upstream evidence and the extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not a direct generated-YAML edit. Optional marker enrichment requires a supported taxon-level representation, not an invented culture-strain container.

## Follow-up Checks

For authorized enrichment, verify the exact TGR6 linkage and retain JF799838.1's version. Require explicit assembly and organism/strain evidence before adding a genome, and direct isolate-linked evidence before adding a functional claim. After maintained-source changes, run the documented seed canary, schema/strict/history checks, corpus reproduction and QC.

## Additional Notes

- YAML SHA-256: `180cde7e149e447e0ea60e5c1033f35a846311a8aa185ee7b0cdaf5a7678bf17`.
- JF799838.1 lowercase sequence SHA-256: `3df7e280aef65d2f885a93dacf91e372eafed5265bc7f890a8908df0806a376b`.
- `data/taxa/PATHS.tsv:15329` and `curation/seed_scope.tsv:322993` uniquely resolve the target. Scope addition is 2026-09-13; the seed event preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened, curation event appended or review status promoted.
