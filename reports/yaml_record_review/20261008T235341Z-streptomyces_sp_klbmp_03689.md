# YAML Record Review: Streptomyces sp. KLBMP 03689

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03689.yaml`
- Started UTC: 2026-10-08T23:51:42Z
- Finished UTC: 2026-10-08T23:53:41Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036497`. Assertions are species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero BacDive records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, genome links and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03689.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03689.yaml --out /private/tmp/klbmp03689-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons verified the complete backbone row, all ten ancestors, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and full type-material, merged-ID and dropped tables were scanned.
- Complete nucleotide XML parsing verified actual/declared length, equality with submitted rRNA transcription and no non-ACGT symbols. This is annotation consistency, not independent alignment or species inference.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not establish corpus reproduction. The embedded event was inspected; stated ignored-inclusive searches found no separate target history artifact. Graph product validation is inapplicable without graph nodes. No focused substitute for a corpus gate was invented.

## Identity and Grounding

Full [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036497&retmode=xml) agrees with the identifier, label, rank, parent and code. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036497) confirms all ten root-first ancestor IDs. Pinned labels/ranks agree with the live chain through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root in its displayed lineage while Datasets includes it; this is not a conflict.

This unnamed strain-associated taxon has NCBI species rank, not demonstrated status as a formally described species or synonym of a named congener. Exact grounding denotes this specific NCBI identity. Live EFetch supplies no other names; pinned synonyms are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete target source rows were read:

- `data/raw/ncbitaxon_taxa.tsv:222499`: identity, parent, rank, code, empty synonyms, attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32043`: exact scientific-name object.
- `data/taxa/PATHS.tsv:15006`: identifier/slug.
- `curation/seed_scope.tsv:322746`: date and one-source admission reason matching the seed event.

The source counts one `NAME`, not a genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories found no rows. Under the schema/seeder contract, `strain_count: 0` counts represented BacDive records, not existence of a source strain designation.

Exact non-expanded Nuccore query `txid1036497[Organism:noexp]` returned UID 334303277. The complete [JF803753.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF803753.1), including references, source/rRNA features and sequence, explicitly identifies this taxon and KLBMP 03689. It supplies a 558-base partial 16S marker, with both ends partial. Its own isolation source is stem, host Pinus massoniana, location China: Panzhihua. No culture-deposit qualifier, assembly cross-reference or CDS is supplied. Declared length, actual sequence and submitted transcription agree without ambiguous symbols.

References name an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin and direct submission dated 11-APR-2011, without a study PMID or DOI. The title does not establish successful disease control by this strain. This short marker is not a genome, functional assay or formal species reassignment. Stem isolation is this accession's collection context, not evidence for every KLBMP strain or Streptomyces.

Spaced/compact strain-name web searches returned broad NCBI taxonomy listings. Queries for `"JF803753" OR "JF803753.1"` and the full strain with Streptomyces excluding NCBI domains returned no results. Search snippets supplied no biological verdict evidence.

## Completeness

Complete enough for its supported taxonomy-seed scope. Optional nomenclature, other mappings, deposits, genomes and graphs should remain unasserted without explicit identity chains. An external ribosomal marker and source metadata do not require inventing a BacDive record or adding a genome link.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain variants, JF803753 (including versioned matches) and UID 334303277. Initial and expanded searches returned the same three own taxonomy/name/scope rows, all read completely; no additional native candidates were found in those roots. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence claims are bounded to these roots/expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. PubMed query `"KLBMP 03689"[All Fields] OR "JF803753"[All Fields]` returned zero with quoted-phrase warnings. Neither outcome proves universal absence of genomes or literature; figure/supplement mentions can escape indexed queries.

iModulonDB was not run: there is no asserted gene, regulator or expression claim and no covered strain/dataset was identified. The ribosomal marker does not establish database coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Limited external characterization does not invalidate the exact NCBI seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not infer identity from a shared KLBMP prefix, species equivalence from a short marker or phenotype from an unpublished study title.

Future taxonomic corrections belong first at NCBI, then in pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional source-context/sequence enrichment needs maintained input and model/seeder support, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Before enrichment, inspect primary evidence explicitly linking this exact strain to any proposed deposit, genome or experiment. Keep sequence, sample, project and genome identifiers distinct, and preserve this accession's own stem source and narrow evidence scope.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036497`, inspect the output, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

The local single-record skill, checklist and ownership guidance governed this review. Own source rows and accession were independently inspected. Before/after YAML SHA-256 was `25207d76d51e684d55121c4a6cc64ec23f930b99e3845db254aa229d9793bbb8`.

Only this new timestamped report was written for the target. No YAML, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
