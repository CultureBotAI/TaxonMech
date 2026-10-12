# YAML Record Review: Streptomyces sp. KLBMP 03671

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03671.yaml`
- Started UTC: 2026-10-08T23:48:19Z
- Finished UTC: 2026-10-08T23:50:20Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036496`. It asserts species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, code 11, `EXACT` grounding, `SEEDED` status, zero BacDive records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, genome links and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no previous report for this stem. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03671.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03671.yaml --out /private/tmp/klbmp03671-strict.tsv`: passed, one file, zero errors; the full TSV was header-only.
- Complete backbone/ancestor comparisons verified lineage, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and complete type-material, merged-ID and dropped tables were scanned.
- Full nucleotide XML parsing verified actual/declared length, equality with submitted rRNA transcription and no non-ACGT symbols. This is annotation consistency, not independent alignment or species inference.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Bounded individual checks do not establish corpus reproduction. The embedded event was read; stated ignored-inclusive searches found no separate target history artifact. Graph product validation is inapplicable without graph nodes. No focused substitute for a corpus gate was invented.

## Identity and Grounding

Full [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036496&retmode=xml) agrees with the identifier, label, rank, parent and code. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036496) confirms all ten root-first ancestor IDs. The pinned labels/ranks agree with the live chain through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

NCBI species rank for this unnamed strain-associated taxon does not establish a formally described species or synonymy with a congener. Exact grounding denotes this specific NCBI identity. Live EFetch has no other names; pinned synonyms are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete target source rows were read:

- `data/raw/ncbitaxon_taxa.tsv:222498`: identity, parent, rank, code, empty synonyms, source and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32042`: exact scientific-name object.
- `data/taxa/PATHS.tsv:15005`: identifier/slug.
- `curation/seed_scope.tsv:322745`: date and one-source admission reason matching the seed event.

The attestation counts one `NAME`, not a genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. The schema/seeder defines `strain_count: 0` as zero represented BacDive records, not denial of a source strain designation.

Exact non-expanded Nuccore query `txid1036496[Organism:noexp]` returned UID 334303294. The complete [JF803770.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF803770.1), including references, source/rRNA features and sequence, explicitly identifies this taxon and KLBMP 03671. It supplies a 684-base 16S marker with both ends partial. Its own source is rhizosphere, host Pinus massoniana, location China: Panzhihua. There is no culture-deposit qualifier, assembly cross-reference or CDS. Declared length, actual sequence and submitted transcription agree without ambiguous symbols.

Its references name an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin and direct submission on 11-APR-2011, without a study PMID or DOI. The title does not demonstrate disease control by this strain. This partial marker is not a genome, functional assay or formal species assignment; collection context applies to this accession.

Four additional catalog rows were read completely and excluded:

- `data/bvbrc/bvbrc-0000.jsonl.gz:44397` identifies Staphylococcus aureus taxid 1280, strain 46-023, genome 1280.25764, GCA_010364965.1, sample SAMN13948066 and project PRJNA604020.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:7072` and `data/catalog/ncbi_refseq-0002.jsonl.gz:41241` identify the same Staphylococcus strain, GCA_010364965.1 and GCF_010364965.1, assembly ASM1036496v1, sample SAMN13948066 and WGS JAAFMD000000000.1. They are latest contig-level records; projects are PRJNA604020 and PRJNA224116, respectively.
- `data/catalog/gtdb_genomes-0013.jsonl.gz:42156` is RS_GCF_010364965.1 for Staphylococcus aureus taxid 1280, strain 46-023. Its Bone/Joint isolation source and USA: Texas location do not describe KLBMP 03671.

Matching digits occur inside assembly accessions/names, not exact target taxon identifiers. No target strain-genome, sample, project, deposit or phenotype chain follows from these four rows.

Spaced/compact strain-name web searches returned the target NCBI browser entry and broad taxonomy listings. Subsequent queries for `"JF803770" OR "JF803770.1"` and the full strain with Streptomyces excluding NCBI domains returned no results. Snippets were discovery leads, not biological verdict evidence.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, mappings, deposits, genome links and graphs correctly remain unasserted without explicit evidence. The external marker/source metadata do not require inventing a BacDive record or genome link.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain variants, JF803770 (including versioned matches) and UID 334303294. Initial and expanded searches returned the same seven rows: three own taxonomy/name/scope rows and four unrelated candidates. All were read fully. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence claims are bounded to these roots/expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. PubMed query `"KLBMP 03671"[All Fields] OR "JF803770"[All Fields]` returned zero with quoted-phrase warnings. These are bounded outcomes, not universal absence of genomes or literature; figure/supplement mentions may escape indexed queries.

iModulonDB was not run: the YAML asserts no gene, regulator or expression claim and no covered strain/dataset was identified. The marker does not establish such coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Sparse characterization and excluded numeric catalog matches do not invalidate the grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join numeric substrings, equate KLBMP-prefix strains, transfer Staphylococcus metadata or infer a species/phenotype from a partial marker or study title.

Future taxonomy corrections belong at NCBI, then in pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional source-context/sequence enrichment needs maintained input and model/seeder support, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Any later enrichment must explicitly link this strain to a proposed deposit, genome or experiment and distinguish sample, project, sequence and genome identities. Preserve this accession's own rhizosphere qualifier and evidence scope.

After an authorized input/seeder correction, run a focused regression test, `just seed-canary NCBITaxon:1036496`, inspect the emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

The local single-record skill, checklist and ownership guidance governed this review. Own source rows and accession were independently inspected. Before/after YAML SHA-256 was `70e93690c4918c8ae9daa1e45f4a4c9d6b644d869e50bcee67cd247adce24652`.

Only this new timestamped report was written for the target. No YAML, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
