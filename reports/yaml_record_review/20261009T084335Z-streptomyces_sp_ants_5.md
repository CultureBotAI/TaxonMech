# YAML Record Review: Streptomyces sp. ANTS-5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_ants_5.yaml`
- Started UTC: 2026-10-09T08:39:04Z
- Finished UTC: 2026-10-09T08:43:35Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036665`, Streptomyces sp. ANTS-5. It asserts species rank, Bacteria, parent 2593676, ten root-first ancestors, code 11, `EXACT` grounding, `SEEDED` mapping status, zero represented BacDive strains and one NCBITAXON name attestation. Its seed event is dated 2026-09-13T17:54:04Z.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` uniquely resolved this YAML and found no prior target report. Synonyms, nomenclature, mappings, deposits, genomes, phenotypes, discussion and graphs are unasserted. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptomyces_sp_ants_5.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/streptomyces_sp_ants_5.yaml --out /private/tmp/taxonmech-streptomyces-ants5-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched own identity, every ancestor, PATHS, scope reason, attestation and seed wording. Exact scans covered seven supplemental raw inventories, type material, merged IDs and dropped taxa.
- Own-marker annotation consistency passed: declared and actual length 477, rRNA transcription identical to DNA, no non-ACGT symbols. This is not independent alignment or species identification.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Focused comparisons do not prove corpus reproduction. Embedded history was read; ignored-inclusive content and filename searches found no separate target history artifact within the stated roots. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036665&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036665) responses agree with label, species rank and lineage. EFetch confirms parent 2593676 and code 11; Datasets includes root. Ancestors are root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces.

Live taxonomy has no other names; pinned synonym fields are empty. No own type-material, merged-ID or dropped-taxon row, or backbone child, was found. Species rank does not establish formal nomenclatural standing or a particular named Streptomyces species. ANTS-1 is not an alias for ANTS-5. The strain code does not imply an insect association.

## Evidence

Complete own rows inspected: `data/raw/ncbitaxon_taxa.tsv:222569`, `data/catalog/ncbi_names-0005.jsonl.gz:32113`, `data/taxa/PATHS.tsv:15086` and `curation/seed_scope.tsv:322816`. Snapshot 2026-09-13, one-name unit and admission reason support the attestation and seed event. Exact target scans found no row in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits raw inventories. A name count is not a genome or experiment count.

Exact Nuccore taxon query returned UID 334546887 alone. Complete [JF812170.1](https://www.ncbi.nlm.nih.gov/nuccore/JF812170.1) XML, references, features and sequence were read. This 477-base partial 16S marker is incomplete at both ends. Its nine source qualifiers identify Streptomyces sp. ANTS-5, genomic DNA, strain ANTS-5, soil, taxon 1036665, Bangladesh, Nov-2010 collection, collector Tahmida Sharmin and the submitted PCR primers. No deposit, type-material or genome qualifier is supplied.

The marker cites an unpublished isolation/characterization submission by Islam, Sharmin, Rahman, Anisuzzaman and colleagues, plus a 16-APR-2011 direct submission from the Department of Pharmacy, Rajshahi University. Creation/update dates are both 06-JUN-2011. No PMID or DOI is supplied in that marker. The submission establishes source-reported provenance, not a formal species description or an experimentally validated metabolic mechanism.

The [publisher article page](https://www.banglajol.info/index.php/BPJ/article/view/14485) verifies Sharmin and colleagues' 2013 paper and DOI 10.3329/bpj.v16i1.14485. Its [five-page PDF](https://www.banglajol.info/index.php/BPJ/article/download/14485/10287) was fully read as text and visually inspected. It includes ANTS-5 among five Rajshahi soil isolates and labels it in Figure 2. Figure 3 presents screening photographs, not an isolate-by-isolate quantitative ANTS-5 dataset. Methods and Results select ANTS-1 for detailed work; Table 2 explicitly names ANTS-1. The antimicrobial, cytotoxicity and actinomycin findings cannot transfer to ANTS-5. Matching laboratory, collector and strain code support a provenance-context inference, but the paper does not explicitly cite JF812170. The PDF instead identifies ANTS-1 with JF812169. These are bounded context observations, not new YAML claims.

Complete [JF812169.1](https://www.ncbi.nlm.nih.gov/nuccore/JF812169.1) XML confirms the paper's separate ANTS-1 accession: 564 bases, UID 334546879, current organism Streptomyces banglaensis, taxon 1036731, and a type-strain qualifier. Its older definition still says Streptomyces sp. ANTS-1. The shared collection provenance does not collapse the two strain identities or transfer the type-material assertion.

## Completeness

Complete enough for supported taxonomy-seed claims. Zero represented BacDive strains does not deny the cultured isolate's existence. No additional target deposit or genome link was established within the inspected evidence. The publication is an optional enrichment lead, not evidence that the present taxonomy-only seed is materially incomplete.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms were word-bounded 1036665, the exact slug and ANTS5 with an optional space, hyphen or underscore. Expansion added word-bounded JF812170 with optional .1 and UID 334546887. Both searches returned the same three own rows: backbone, name catalog and scope. All were read completely in native form, two TSV and one JSON row, with lossless common fields and differences.

Five SOURCE.json files were separately parsed in full for both term sets, with no matching keys or values; history filenames were independently inventoried. This covers the stated local roots, not every external source or spelling.

The all-genus Nuccore query `ANTS5[All Fields] OR "ANTS-5"[All Fields] OR "ANTS 5"[All Fields]` returned two records, with all three terms effective. Both received complete XML reads. Besides the own marker, [LT703220.1](https://www.ncbi.nlm.nih.gov/nuccore/LT703220.1), UID 1336499596, is a 674-base mitochondrial COI sequence from Austruca annulipes, taxon 196277, isolate Tanga-Mpirani ANTS5, Tanzania, collected 07-Aug-2015. Its title uses the older Uca annulipes name. This is a non-bacterial name collision, not a target genome or a reason to reopen any Eukaryota corpus review.

Exact Assembly taxon query returned zero with missing-phrase/no-items diagnostics, not proof of global genome absence. Exact JF812170 PubMed search returned zero with a quoted-phrase-not-found diagnostic. The genus/code PubMed search returned 13 IDs only after rejecting ANTS5 and both quoted separator variants, translating the code into ants plus 5. Those 13 abstracts were not individually adjudicated and do not constitute an exact-strain literature census.

Web searches for the exact genus/code, accession and isolation/characterization title plus Sharmin supplied the primary paper lead above. Other search snippets were not used as evidence. No claim of absent literature is made from PubMed's indexing misses, and no exhaustive full-text literature census was performed.

iModulonDB was not run: no gene, regulator or expression claim is asserted, and no applicable target strain/dataset was established. Optional empty fields are not automatic defects; absence conclusions remain bounded to the stated roots, terms and indexes.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, source attestation and admission agree with pinned and live authorities. ANTS-1's accession, type-material assertion and experiments do not establish missing claims for ANTS-5.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; admission changes belong in `curation/seed_scope.tsv`. Do not merge records based on the ANTS prefix, shared authors or adjacent accessions.

## Follow-up Checks

Optional enrichment needs an explicit ANTS-5/JF812170 provenance link and isolate-specific evidence; culture-deposit and genome links require their own source chain. Keep inferred literature context separate from exact accession evidence. No independent sequence alignment, genome comparison or experimental reanalysis was performed.

After an authorized maintained-input change, run focused tests, `just seed-canary NCBITaxon:1036665`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

Independent review followed the local skill/checklist; no neighboring verdict was inherited. Entire YAML, own source rows, all three local candidates, live taxonomy, own marker, the non-bacterial near-name marker, ANTS-1 marker and the primary paper's complete text and five page images were inspected.

The DOI web endpoint was inaccessible, while the publisher landing page and direct PDF were accessible. Web PDF screenshots timed out. Poppler was unavailable on PATH; a temporary `uv run --no-project` environment with pypdfium2 and Pillow extracted and rendered all five pages successfully, without changing repository dependencies. Downloaded PDF SHA-256: `aca0aaa1715e20d11c52c4a7ecf633740d0a47af3e7637238cc4d5ad49cc0dfa`. Temporary PDF/images are review working files, not published corpus products.

Before/after YAML SHA-256: `763cc71cd828926c2ee50eb3bf065ffc7ad14ad25d618132153964a872423119`. Only this new report was written in the repository for the target. YAML, sources, status, history, pages, Eukaryota, GitHub objects and worktrees were unchanged.
