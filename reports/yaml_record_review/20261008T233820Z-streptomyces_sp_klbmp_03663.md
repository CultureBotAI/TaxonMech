# YAML Record Review: Streptomyces sp. KLBMP 03663

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03663.yaml`
- Started UTC: 2026-10-08T23:34:23Z
- Finished UTC: 2026-10-08T23:38:20Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036493`. It asserts species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero BacDive records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, strain/genome links and graphs are unasserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. The generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03663.yaml`: passed with no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03663.yaml --out /private/tmp/klbmp03663-strict.tsv`: one file, zero errors; the full TSV was header-only.
- Structured comparisons verified the complete backbone row, all ten ancestors, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and type-material, merged-ID and dropped tables were scanned.
- Full nucleotide XML parsing verified declared/actual length, equality with the submitted rRNA transcription and absence of non-ACGT symbols. This is annotation consistency, not independent phylogenetic analysis.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Bounded individual checks do not prove corpus reproduction. The embedded event was inspected; ignored-inclusive searches found no separate target history artifact in the stated roots. Graph product validation is inapplicable without graph nodes. No invented focused substitute for a corpus gate was used.

## Identity and Grounding

Full [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036493&retmode=xml) agrees with the ID, label, rank, parent and genetic code. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036493) confirms all ten root-first ancestor IDs. The pinned ancestor labels/ranks agree with the live chain through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

This is an unnamed strain-associated taxon assigned species rank by NCBI, not a formally described species or a demonstrated synonym of a named congener. Exact grounding denotes this NCBI identity. Live EFetch has no other names; pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped entry and no backbone children.

## Evidence

Complete target source rows were read:

- `data/raw/ncbitaxon_taxa.tsv:222495`: identity, parent, rank, code, empty synonyms, source and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32039`: exact scientific-name object.
- `data/taxa/PATHS.tsv:15002`: ID/slug.
- `curation/seed_scope.tsv:322742`: admission date and one-source reason matching the seed event.

The attestation counts one `NAME`, not a genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories found no rows. Under the schema/seeder contract, `strain_count: 0` counts represented BacDive records and does not deny the existence of a strain designation.

Exact non-expanded Nuccore query `txid1036493[Organism:noexp]` returned UID 334303275. The complete [JF803751.1 record](https://www.ncbi.nlm.nih.gov/nuccore/JF803751.1), including references, source/rRNA features and sequence, was inspected. It explicitly identifies KLBMP 03663 and taxon 1036493 and supplies a 680-base 16S marker with both ends partial. Its own source is stem, host Pinus massoniana, location China: Panzhihua. There is no culture-deposit qualifier, assembly cross-reference or CDS. Declared length, actual sequence and submitted rRNA transcription agree without ambiguous symbols.

References identify an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin and direct submission on 11-APR-2011, without a study PMID or DOI. The title does not prove successful biocontrol by this strain. The marker supports submitted identity, not a genome, functional mechanism or formal species reassignment. Collection context is specific to this accession.

Six additional native candidates were read completely and excluded:

- `data/bvbrc/bvbrc-0000.jsonl.gz:44398`, `data/catalog/ncbi_genbank-0009.jsonl.gz:7071`, `data/catalog/ncbi_refseq-0002.jsonl.gz:41240` and `data/catalog/gtdb_genomes-0000.jsonl.gz:38112` all describe Staphylococcus aureus taxid 1280, strain 51-045. Their identifiers are BV-BRC 1280.25765, GCA_010364935.1, GCF_010364935.1 and RS_GCF_010364935.1, with assembly name ASM1036493v1, sample SAMN13948077 and WGS JAAFLS000000000.1. GenBank/BV-BRC project PRJNA604020 and RefSeq/GTDB project PRJNA224116 are not target projects. The GTDB respiratory/USA: Texas context belongs to that Staphylococcus.
- `data/catalog/allthebacteria.tsv.xz:1505322` concerns Ensifer adhaerens, sample SAMN10364938, run SRR8156493 and analysis ERZ25501324. Assembly pipeline and sylph filters pass; HQ records CHECKM2_MAX_CONTAM and CHECKM2_MIN_COMPL. Its sylph label is Ensifer sp000799055.
- `data/catalog/allthebacteria.tsv.xz:1505323` concerns Flavobacterium succinicans, sample SAMN10364939, run SRR8156492 and analysis ERZ25501332. Assembly pipeline passes, while HQ/sylph report NO_SYLPH_RESULTS and sylph species is unknown.

ATB URLs, source filters and SeqKit sums were retained in the inspected native records; neither sample identifies KLBMP 03663. Their matching digits occur inside sample accessions. Numeric substrings in assemblies or samples are not taxon identity chains, and source-quality flags do not overcome this mismatch.

Spaced/compact strain-name web queries returned the target NCBI browser entry and broad taxonomy listings. Queries for `"JF803751" OR "JF803751.1"` and the full strain with Streptomyces excluding NCBI domains returned no results. Search snippets supplied no phenotype evidence.

## Completeness

Complete enough for supported taxonomy-seed claims. Empty optional nomenclature, mappings, deposits, genomes and graphs should not be filled without explicit evidence. The marker and source metadata do not create a BacDive record or require a genome link.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, spaced/compact strain variants, JF803751 (including versioned matches) and UID 334303275. Initial and expanded scans returned the same nine rows: three own taxonomy/name/scope rows and six unrelated candidates. All were read fully. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence statements are bounded to these roots/expressions.

Exact Assembly search returned zero with a phrase-not-found warning. PubMed query `"KLBMP 03663"[All Fields] OR "JF803751"[All Fields]` returned zero with quoted-phrase warnings. Neither proves universal genome or literature absence; figure/supplement mentions may escape indexed searches.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no covered strain/dataset was identified. A ribosomal marker does not establish database coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Sparse characterization and excluded numeric catalog matches do not invalidate the grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join numeric substrings, equate KLBMP-prefix strains, transfer another organism's metadata or infer a formal species/phenotype from this marker or study title.

Future taxonomic corrections belong at NCBI and then in the pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional source-context/sequence enrichment needs maintained inputs and suitable model/seeder support, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Any later enrichment must explicitly connect this exact strain to a deposit, genome or experiment and keep sample/project/sequence/genome identities distinct. Preserve this accession's own stem source and narrow evidence scope.

After an authorized input/seeder correction, run a focused regression test, `just seed-canary NCBITaxon:1036493`, inspect the generated result, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran in this review.

## Additional Notes

Local single-record guidance, ownership rules and checklist governed this review. Own source rows and accession were independently inspected. Before/after YAML SHA-256 was `66920ddd7b8c496488e502aff035ebba1a0d608659ec24954d775b0c638e6486`.

Only this new timestamped report was written for the target. No YAML, source, history, review status, generated page or GitHub object changed. Existing worktrees and Eukaryota were untouched.
