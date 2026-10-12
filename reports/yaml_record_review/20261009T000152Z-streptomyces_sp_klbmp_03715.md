# YAML Record Review: Streptomyces sp. KLBMP 03715

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03715.yaml`
- Started UTC: 2026-10-08T23:59:07Z
- Finished UTC: 2026-10-09T00:01:52Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036499`. It asserts species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, code 11, `EXACT` grounding, `SEEDED` mapping status, zero represented BacDive records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, genome links and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03715.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03715.yaml --out /private/tmp/klbmp03715-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons verified complete backbone/ancestor rows, lineage, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and full type-material, merged-ID and dropped tables were scanned.
- Complete nucleotide XML parsing verified declared/actual length, equality with submitted rRNA transcription and no non-ACGT symbols. This is annotation consistency, not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not establish corpus reproduction. The embedded event was inspected; stated ignored-inclusive searches found no separate target history artifact. Graph product validation is inapplicable without graph nodes. No focused substitute for a corpus gate was invented.

## Identity and Grounding

Full [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036499&retmode=xml) agrees with the identifier, label, rank, parent and code. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036499) confirms all ten root-first ancestor IDs. Pinned labels/ranks agree with the live chain through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

NCBI species rank for this unnamed strain-associated taxon does not establish a formally described species or synonymy with a congener. Exact grounding denotes this particular NCBI identity. Live EFetch supplies no other names; pinned synonyms are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete target source rows were read:

- `data/raw/ncbitaxon_taxa.tsv:222501`: identity, parent, rank, code, empty synonyms, source and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32045`: exact scientific-name object.
- `data/taxa/PATHS.tsv:15008`: identifier/slug.
- `curation/seed_scope.tsv:322748`: date and one-source admission reason matching the seed event.

The attestation counts one `NAME`, not a genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema/seeder contract, `strain_count: 0` counts represented BacDive records and does not deny the source strain designation.

Exact non-expanded Nuccore query `txid1036499[Organism:noexp]` returned UID 334303278. The complete [JF803754.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF803754.1), including references, source/rRNA features and sequence, explicitly identifies this taxon and KLBMP 03715. It supplies a 678-base 16S marker with both ends partial. Its own source is stem, host Pinus massoniana, location China: Panzhihua. No culture-deposit qualifier, assembly cross-reference or CDS is supplied. Declared length, actual sequence and submitted rRNA transcription agree without ambiguous symbols.

References name an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin and direct submission on 11-APR-2011, without a study PMID or DOI. The study title does not demonstrate disease control by this strain. This partial marker is not a genome, functional assay or formal species assignment; collection context applies to this accession.

Four additional native catalog rows were read completely and excluded:

- `data/bvbrc/bvbrc-0000.jsonl.gz:44399` describes Staphylococcus aureus taxid 1280, strain 47-087, genome 1280.25766, GCA_010364995.1, sample SAMN13948068 and project PRJNA604020.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:7074` and `data/catalog/ncbi_refseq-0002.jsonl.gz:41243` describe that Staphylococcus strain and respectively GCA_010364995.1/GCF_010364995.1, assembly ASM1036499v1, sample SAMN13948068 and WGS JAAFMB000000000.1. Both are latest contig-level records; projects are PRJNA604020 and PRJNA224116, respectively.
- `data/catalog/gtdb_genomes-0005.jsonl.gz:43548` is RS_GCF_010364995.1 for Staphylococcus aureus taxid 1280, strain 47-087. Its blood isolation source and USA: Texas location do not concern KLBMP 03715.

The target's digits occur inside unrelated assembly accessions/names. These are not exact target taxon identifiers and establish no target genome, sample, project, deposit or phenotype chain.

Spaced/compact strain-name web searches returned broad NCBI taxonomy listings. Queries for `"JF803754" OR "JF803754.1"` and the full strain with Streptomyces excluding NCBI domains returned no results. Search snippets supplied no biological verdict evidence.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, other mappings, deposits, genomes and graphs should remain unasserted without explicit evidence. The external ribosomal marker and source context do not require inventing a BacDive entry or genome link.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain variants, JF803754 (including versioned matches) and UID 334303278. Initial and expanded searches returned the same seven rows: three own taxonomy/name/scope rows and four unrelated candidates. All were read fully. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence statements are bounded to these roots/expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. PubMed query `"KLBMP 03715"[All Fields] OR "JF803754"[All Fields]` returned zero with quoted-phrase warnings. Neither outcome proves universal genome or literature absence; indexed queries may miss figure or supplement mentions.

iModulonDB was not run: the YAML asserts no gene, regulator or expression claim and no covered strain/dataset was identified. The marker does not establish database coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Sparse characterization and excluded numerical matches do not invalidate the grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join numeric substrings, equate strains by KLBMP prefix, transfer Staphylococcus metadata or infer formal species/phenotype from a partial marker or study title.

Future taxonomy corrections belong at NCBI, then in pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional sequence/source-context enrichment requires maintained input and model/seeder support, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Any later enrichment needs inspected primary evidence explicitly linking this strain to a proposed deposit, genome or experiment. Keep strain, sequence, sample, project and genome identities distinct; preserve this accession's own stem source and narrow evidence scope.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036499`, inspect the result, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

The local single-record skill, checklist and ownership guidance governed the review. Own source rows and accession were independently inspected. Before/after YAML SHA-256 was `9f7d1d867244b00b3dbb7a908e00e1424703a61f59d88d8ebe6cc987f37b8590`.

Only this new timestamped report was written for the target. No YAML, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
