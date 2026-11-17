# YAML Record Review: Streptomyces banglaensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_banglaensis.yaml`
- Started UTC: 2026-10-09T13:31:08Z
- Finished UTC: 2026-10-09T13:37:05Z
- Verdict: pass

## Target

All 58 lines of the generated `TaxonRecord` for `NCBITaxon:1036731` were independently read. The target is Streptomyces banglaensis, an NCBI species-rank taxon with ANTS-1-related names, not the similarly named Streptomyces bangladeshensis. It carries `BACTERIA`, parent `NCBITaxon:1883`, code 11, `EXACT` grounding, `SEEDED` status, two related synonyms, zero inventoried strains, one NCBI name attestation and an embedded seed event.

Committed inventories and `curation/seed_scope.tsv` own the inputs. `src/taxonmech/seed.py`, called through `scripts/seed_from_sources.py`, owns generated representation. No neighboring record supplied this verdict.

## Validation

Both documented focused validators passed, exit zero:

```bash
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptomyces_banglaensis.yaml
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline python scripts/validate_strict.py data/taxa/bacteria/streptomyces_banglaensis.yaml --out /private/tmp/taxonmech-sbang-review-strict.tsv
```

Schema validation found no issues. Strict validation scanned one file with zero errors; its full TSV was header-only. Read-only source comparisons verified the own backbone, nine ancestors, synonyms, attestation, scope/index and embedded event. Exact-field status scans found two own type-material rows, no merged/dropped-ID row and no immediate children in the pinned backbone.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-history`, provenance, documentation and rendered-site drift gates. No focused substitute for a corpus-only check was invented. OAK `validate-products` was not run because the YAML has no curator-added graph nodes. No literature identifier is asserted in the YAML; no separate history file matched the searches below. Bounded comparisons do not certify corpus reproduction.

## Identity and Grounding

The complete backbone at `data/raw/ncbitaxon_taxa.tsv:222613`, native NCBI names at `data/catalog/ncbi_names-0005.jsonl.gz:32168`, `:32169` and `:32170`, scope at `curation/seed_scope.tsv:322853` and index at `data/taxa/PATHS.tsv:15136` support the exact identity and slug.

Full [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036731&retmode=xml) and [Datasets JSON](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036731) confirm identity, species rank, parent, bacterial placement and code. They agree with the pinned root-first chain:

`1 root (NO_RANK) -> 131567 cellular organisms (CELLULAR_ROOT) -> 2 Bacteria (DOMAIN) -> 1783272 Bacillati (KINGDOM) -> 201174 Actinomycetota (PHYLUM) -> 1760 Actinomycetes (CLASS) -> 85011 Kitasatosporales (ORDER) -> 2062 Streptomycetaceae (FAMILY) -> 1883 Streptomyces (GENUS)`.

The quoted Sharmin et al. 2017 name is NCBI's authority entry; Streptomyces sp. ANTS-1 is its includes entry. Neither is incorrectly promoted to `EXACT_SYNONYM`: `src/taxonmech/ncbi_taxdump.py:91` deliberately projects these name classes as related, and `src/taxonmech/seed.py:381` carries that scope. The authority string preserves its quotation marks. `EXACT` supports NCBI identity grounding, not nomenclatural validity or equivalence to another species.

## Evidence

One `NCBITAXON` `NAME` at the 2026-09-13 snapshot supports the own attestation; it is not a strain/genome count. The 2026-09-13T17:54:04Z seed event matches the source and scope reason and does not imply human review.

Native `data/raw/ncbi_type_material.tsv:1915` and `:1916` retain `personal::ANTS-1` and `strain ANTS-1` as type-strain annotations, consistent with live NCBI. These are not registered culture-collection accessions. The inspected seeder's BacDive-based strain construction and `strain_count` at `src/taxonmech/seed.py:543` explain zero inventoried strains without asserting that no laboratory isolate exists.

Exact non-expanded nuccore lookup returned two entries. Both complete [GenBank XML records](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=2363080489,334546879&rettype=gb&retmode=xml) were read: `JF812169.1` and RefSeq `NR_178485.1`, each 564 bases, partial 16S rRNA, taxon `1036731`, strain ANTS-1 and a type-material qualifier. Metadata specify Bangladesh soil collected in November 2010. RefSeq explicitly derives from JF812169.1 positions 1-564. Both stored sequences and transcription qualifiers were checked: lengths agree, all characters are A/C/G/T, and the two sequences are identical. They are not independent genomes. `PRJNA33175` is a project reference, not an assembly. No independent phylogenetic analysis was performed.

The 2017 primary paper explicitly links ANTS-1 and JF812169 and proposes the name. Its methods describe 568 bases, versus the current records' 564; its tree uses 561 aligned positions. The discrepancy remains unresolved. Figure 2 places ANTS-1 beside S. griseoplanus; the text briefly suggests that identity, then argues for a distinct species. This is not a basis to merge NCBI taxa. Paper text was read in full, with printed pages 33, 34 and 37 visually checked. The paper's type-strain assertion does not establish a registered deposit or validated nomenclatural status. [Sharmin et al., 2017](https://sciarena.com/storage/models/article/wHP2t2pl21PpAHr39VmFvLKbyo1cD4A7q8J2wQMoyLGH3khnNSOl1btpKxEx/streptomyces-banglaensis-spnov-isolated-from-soils-of-rajshahi-bangladesh-producing-actinomycin-d.pdf).

The 2013 primary paper also explicitly links ANTS-1 to JF812169 and identifies an isolated component as actinomycin D. Its biological assays concern a crude extract; the authors state that separated compounds were not biologically tested. Accordingly, extract activity must not become a pure-compound potency claim or a clinical-efficacy claim. All five pages were read as text; printed pages 16, 18 and 19 were visually checked, including table headers and limitations. No trait was added to this species record. [Sharmin et al., 2013, Bangladesh Pharmaceutical Journal 16(1):15-19](https://www.banglajol.info/index.php/BPJ/article/download/14485/10287).

The complete native name-discovery row at `data/seqcode/names.jsonl.gz:34923` points to SeqCode `36810`. Its full [live API response](https://api.seqco.de/v1/names/36810.json) says Automated discovery, with no priority date, unknown nomenclatural type and unresolved description/publication metadata. Its higher-level Streptomycetales classification differs from NCBI's Kitasatosporales. Per `docs/SOURCE_COVERAGE.md`, a native discovery hit is not an inferred taxon equivalence; per `CLAUDE.md`, NCBI lineage is carried, not reconciled. Neither the name hit nor valid-status labels on SeqCode ancestors establish species-name validity.

## Completeness

Exact taxon-field scans found no own rows in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. Optional nomenclature, mapping, collection-strain, genome, literature and graph slots may remain empty. The type-material and name-discovery evidence is retained in native inventories, not lost merely because it does not produce an admitted strain or nomenclature assertion here.

The [exact assembly query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=assembly&term=txid1036731%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned zero items with phrase-not-found/no-items warnings. This is not proof of global genome absence under other IDs. Name/accession web searches yielded the primary papers and secondary leads; only inspected primary material supports the biological discussion. No unverified thesis, book or ResearchGate DOI was adopted. iModulonDB was not applicable because the YAML contains no gene, regulator, pathway, module or transcriptomic claim.

LPSN's species URL was unavailable to the web reader; a site-restricted name search did not establish a resolvable entry. This is an access/search limitation, not evidence proving global LPSN absence or invalid publication. Nomenclatural validity is not independently certified by this review and is not asserted by the YAML.

## Findings

None found in the reviewed YAML. The sequence-length discrepancy and differing source classifications are retained as source-level cautions, not silently resolved or counted as claims the record makes.

Counts: 0 blocker, 0 major, 0 minor.

## Recommended Edits

None required for the current seeded identity record. Preserve the quoted authority name, related scope, NCBI-carried lineage and `SEEDED` status. Do not invent a culture accession, name-validity flag or genome link.

Optional future enrichment belongs in maintained inventories or supported overlays, with claim-level source scope and the paper/sequence discrepancy preserved. Harmonization changes belong in `src/taxonmech/seed.py` or the relevant extractor with tests; regenerate via `scripts/seed_from_sources.py`. Scope and slug ownership remain `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Follow-up Checks

No unresolved blocker to the existing representation. Before optional enrichment, independently verify nomenclatural standing and any collection deposition, resolve the paper/sequence length discrepancy, and distinguish crude-extract assays from isolated-component assays. Run focused validators after regeneration and documented corpus reproduction/QC gates before publication; none of those broader gates is certified here.

## Additional Notes

Ignored-inclusive filename enumeration under `data/taxa`, `reports/yaml_record_review` and `history`, with `1036731|streptomyces_banglaensis`, found only this target YAML. Content searches used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including supported compressed catalogs. The final pattern was:

```text
\b1036731\b|\bStreptomyces[ _-]+banglaensis\b|streptomyces_banglaensis\b|\bANTS[ _-]1\b|\b(?:JF812169|NR_178485)(?:\.1)?\b|seqcode:36810\b|seqco\.de/i:36810\b
```

Initial and expanded searches each returned the same eight complete rows, all independently read: own backbone/scope, three native NCBI names, two type-material rows, and the SeqCode discovery row, at the addresses above. No extra accession-linked local candidate appeared within these roots/terms. This is not a census of every remote resource or possible spelling.

Ignored-inclusive discovery under `data`, `curation` and `history` found five `SOURCE.json` files in `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode` and `data/straininfo`; all were fully parsed for both patterns, without matching values. Ignored-independent recursive history filename checks found no match; history contents were also searched.

NCBI and SeqCode web-reader page failures were covered by successful full public API reads. Both publisher PDFs were downloaded to a unique temporary directory; the 2013 PDF succeeded after web-reader timeouts. With Poppler unavailable on PATH, macOS PDFKit extracted all text and rendered the PDFs for the visual checks described above. No failure response was treated as evidence absence.

Target SHA-256 stayed `7e933992695e4ad60627ce0398625a2ffdf2a83b0e78d15f39aad71c9495b8e6` before and after inspection. This review wrote only this new repository report and left records, inventories, scope, history, generated pages, branches, worktrees and GitHub state unchanged. Eukaryota and unrelated work were preserved.
