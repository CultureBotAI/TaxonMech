# YAML Record Review: Streptomyces sp. KLBMP 03519

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03519.yaml`
- Started UTC: 2026-10-08T22:26:20Z
- Finished UTC: 2026-10-08T22:29:46Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036480`, Streptomyces sp. KLBMP 03519. It asserts species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero BacDive strain records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, strain/genome links and causal graphs are unasserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03519.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03519.yaml --out /private/tmp/klbmp03519-strict.tsv`: passed, one file and zero errors. The complete TSV was header-only.
- Structured comparisons checked the complete backbone row, all ten ancestors, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and complete type-material, merged-ID and dropped tables were scanned.
- Complete nucleotide XML parsing confirmed declared versus actual length, equality with the submitted rRNA transcription and absence of non-ACGT symbols. This is annotation consistency, not independent alignment or species identification.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. The embedded event was inspected; bounded searches found no separate target history artifact. Graph product validation is not applicable without graph nodes. No focused substitute for a corpus-wide gate was invented.

## Identity and Grounding

The complete [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036480&retmode=xml) agrees with the ID, label, species rank, parent 2593676 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036480) confirms all ten root-first ancestor IDs. Ancestor labels and ranks match the pinned lineage through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

Species rank is the authority's rank for this unnamed strain-associated taxon, not evidence of a formally described species. Exact grounding denotes this precise NCBI identity, not equivalence with a named congener. Live EFetch supplies no other names; pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete native source rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222482`: identity, rank, parent, code, empty synonyms, attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32026`: exact scientific-name object, empty unique-name field.
- `data/taxa/PATHS.tsv:14989`: ID and slug.
- `curation/seed_scope.tsv:322729`: date and one-source admission reason matching the seed event.

The attestation unit is `NAME`, not strain, assembly or experiment. Full exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema and seeder contract, `strain_count: 0` means zero represented BacDive records, not a denial that a named strain exists.

Exact non-expanded Nuccore query `txid1036480[Organism:noexp]` returned one record, UID 334303284. The complete [JF803760.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF803760.1) identifies this taxon and strain KLBMP 03519. It is a 687-base partial 16S rRNA sequence, with both ends marked partial, from rhizosphere associated with Pinus massoniana in China: Panzhihua. No culture-deposit qualifier or assembly cross-reference is supplied. Source and rRNA features were read fully; there is no CDS feature. Actual sequence length and submitted transcription agree, without ambiguous nucleotide symbols.

The sequence cites an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin, plus a direct submission dated 11-APR-2011, without a study PMID or DOI. The title does not demonstrate successful disease control by this strain. A partial ribosomal marker is not a genome, functional assay or basis for reassignment to a named species. No phenotype was inferred from the genus.

Spaced and compact strain-designation web searches returned broad NCBI taxonomy listings and a root-exudate literature discovery hit. The complete primary taxonomy response, not those snippets, supports the identity assessment. A refined exact strain query excluding NCBI still returned the root-exudate hit; those searches were not empty. A separate exact-accession OR query for JF803760 and JF803760.1 returned no results. The ambiguous literature lead and access limits are detailed below; no biological assertion was adopted from it.

## Completeness

Complete enough for its supported taxonomy-seed scope. Optional nomenclature, synonyms, mappings, deposits, genomes and graphs appropriately remain empty without an explicit identity chain. The external strain designation and ribosomal sequence do not require inventing a BacDive entry or adding a genome link.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain-designation variants and JF803760 with optional version. Only the three name/taxonomy/scope rows matched; all were read completely. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence statements are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. The PubMed query `"KLBMP 03519"[All Fields] OR "JF803760"[All Fields]` returned zero with quoted-phrase warnings. These are bounded query outcomes, not universal genome or literature absence. No strain-genome chain or strain-specific published functional study was verified.

iModulonDB was not run: the YAML asserts no gene, regulator or expression claim and no covered strain/dataset was identified. The external ribosomal marker does not establish such coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. Limited external characterization and inaccessible optional literature do not invalidate this NCBI-grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not infer strain equivalence from the KLBMP prefix, assign a formal species from the partial marker, or promote the unpublished study title into a biocontrol phenotype. Shared search tokens and genus-level traits cannot supply strain-specific assertions.

Future taxonomy corrections belong first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional sequence or source-context enrichment requires maintained input and suitable model/seeder handling, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Before optional enrichment, inspect primary evidence explicitly linking this strain to a proposed deposit, genome or experiment, keeping sequence, sample, project and genome identifiers distinct. If pursuing the root-exudate lead, obtain accessible full text and verify the complete strain designation; the current search output cannot establish a match.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036480`, inspect the emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

The root-exudate discovery hit was [an OUCI listing](https://ouci.dntb.gov.ua/works/7XwwVrp9/) for *Root exudates, the warrior of plant life: Revolution below the ground*. Its search output included a reference DOI ending `03519-w` and a different designation, Bacillus flexus KLBMP 4941. This suggests a token collision, not demonstrated evidence about KLBMP 03519. The OUCI page returned HTTP 502 through web fetch and HTTP 403 through a direct native request. The [publisher page](https://www.sciencedirect.com/science/article/pii/S0254629923007305) returned HTTP 403. Find operations on failed fetches do not establish absence. Full text was not inspected; the lead was excluded from the biological verdict rather than silently treated as a verified mismatch or empty search.

The single-record skill and checklist governed the review, with unchanged local ownership guidance and documented validators. Own source rows and accession were inspected independently. Before/after YAML SHA-256 was `cf4c71ce4c595d37175d0d05c5166f262352bbacb20a8b83f4bed409d7f6649a`.

Only this new timestamped report was written for the target. No record, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
