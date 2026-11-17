# YAML Record Review: Pseudomonas sp. THGR16

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_thgr16.yaml`
- Started UTC: 2026-10-10T05:24:56Z
- Finished UTC: 2026-10-10T05:27:04Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:1037514` denotes Pseudomonas sp. THGR16, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`. It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. No synonym, formal nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph is asserted.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_thgr16.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_thgr16.yaml --out /private/tmp/taxonmech-thgr16-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, genetic code, full lineage, empty source synonyms, seven inventories, unique index/scope resolution, attestation and exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- Complete native name and additional assembly-candidate rows were read. Live NCBI EFetch/Datasets taxonomy, exact nucleotide search and full marker annotations were inspected. The taxonomy-browser web reader failed; direct HTML retrieval succeeded and all 74 parsed text lines were read.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`. Focused checks do not establish corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222786` agrees with the directly inspected [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037514&lvl=3&mode=node), [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037514&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037514). Parent 196821, species rank and code 11 agree; Datasets includes root 1.

The complete root-first lineage agrees: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae, Pseudomonas and unclassified Pseudomonas. The immediate parent is correctly `NO_RANK`.

`data/catalog/ncbi_names-0005.jsonl.gz:32424` contains the exact scientific name with an empty unique-name qualifier. Neither backbone nor EFetch supplies alternate names. The species-ranked placeholder and a sequence strain qualifier are compatible metadata layers. Exact grounding does not establish formal nomenclature or type status.

## Evidence

The one-NAME NCBITAXON assertion and 2026-09-13 snapshot note match the pinned source. No additional own source-count row was found.

The exact nucleotide query returns one entry, UID 334361446: [JF799814.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799814.1), a 770-base partial 16S rRNA gene with both ends partial. The source explicitly names Pseudomonas sp. THGR16, strain THGR16, `taxon:1037514` and wetland soil. Declared and actual lengths agree, with alphabet `acgt`. This supports marker-to-taxon linkage, not a genome or culture-deposit association.

The marker's sole reference is a direct submission dated 10-Apr-2011 by Li, Liu, Shao and Sun at Hebei University. It supplies no DOI, PMID, collection country, collection date or coordinates. Institutional address and submission date are not sampling metadata. Shared submitters or habitat wording cannot transfer another isolate's traits or location.

The additional native hit, `data/catalog/ncbi_genbank-0009.jsonl.gz:7566`, was fully read. It describes `GCA_010375145.1`, assembly name `ASM1037514v1`, strain 16T0026, BioSample `SAMN12576380` and BioProject `PRJNA560345`. Its organism is Francisella tularensis subsp. holarctica, taxon 119857, species taxon 263. The target numeral occurs inside an assembly name, not a matching organism taxon. This row supplies no missing THGR16 assembly link.

Exact-name, spaced-designation and JF799814 web queries established no directly joined experimental publication. Search snippets and broad taxonomy-tree co-membership were treated only as leads; no neighboring taxon or unrelated paper supplied a phenotype. Datasets omits an assembly-count field rather than explicitly returning zero. These bounded searches do not exclude additional genomes or publications.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Bounded taxon ID, slug and designation were searched, followed by JF799814 and spaced/hyphenated THGR 16 variants. Both searches returned four lines: own backbone, name and scope, plus the unrelated assembly-name collision inspected above.

Complete inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. Absence statements apply only to those inspected repository surfaces.

Zero strain count describes represented culture inventory, not isolate existence or culturability. Empty optional slots are appropriate without exact supporting joins. A partial marker and an unrelated assembly-name hit do not establish a missing required genome field. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, complete lineage, attestation and seed audit are supported. The off-target assembly hit does not establish a missing association.

## Recommended Edits

No generated-record correction is justified. Preserve THGR16, species rank, full lineage, `SEEDED` status and existing history. Do not join taxa through assembly-name numerals, treat the partial marker as a genome or infer collection locality from an institutional address.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not direct generated-YAML edits. Optional marker enrichment requires a supported taxon-level representation rather than an invented culture-strain container.

## Follow-up Checks

For authorized enrichment, reconfirm exact organism linkage and retain JF799814.1's version. Require typed identifiers and explicit organism/strain evidence before adding an assembly, and directly joined experimental evidence before assigning a phenotype. After maintained-source changes, run the documented seed canary, schema/strict/history validation, corpus reproduction and QC.

## Additional Notes

- YAML SHA-256: `e07f659cbd68a78a482e077ebcc3f1eb17f2aeb92555e187fb58237fe7247087`.
- JF799814.1 lowercase sequence SHA-256: `3b4a8e36d1813b84500581bba8ec5af08a7a24b87ab039d465fcf8ac14a9c91d`.
- `data/taxa/PATHS.tsv:15339` and `curation/seed_scope.tsv:323003` uniquely resolve the target. Scope addition is 2026-09-13; the seed event preserves 2026-09-13T17:54:04Z and its exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this report was added for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened, curation event appended or review status promoted.
