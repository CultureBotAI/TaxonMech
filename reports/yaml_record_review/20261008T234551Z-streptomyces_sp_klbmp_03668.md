# YAML Record Review: Streptomyces sp. KLBMP 03668

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03668.yaml`
- Started UTC: 2026-10-08T23:43:33Z
- Finished UTC: 2026-10-08T23:45:51Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036495`, Streptomyces sp. KLBMP 03668. Assertions are species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero represented BacDive strains, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, genome links and causal graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. The generated file is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03668.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03668.yaml --out /private/tmp/klbmp03668-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons verified the complete backbone row, ten ancestors, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and full type-material, merged-ID and dropped tables were scanned.
- Complete nucleotide XML parsing confirmed declared/actual length, equality with submitted rRNA transcription and absence of non-ACGT symbols. This verifies annotation consistency, not an independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. The embedded event was inspected; bounded ignored-inclusive searches found no separate target history artifact. Graph product validation is inapplicable without graph nodes. No invented focused substitute for a corpus gate was used.

## Identity and Grounding

Full [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036495&retmode=xml) agrees with the ID, label, species rank, parent and code. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036495) confirms all ten root-first ancestor IDs. The pinned labels/ranks agree with the live lineage through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage; Datasets includes it. This is not a taxonomic conflict.

This unnamed strain-associated taxon has NCBI species rank, which does not establish a formally described species or synonymy with a congener. Exact grounding denotes this specific NCBI identity. Live EFetch supplies no other names; pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete target source rows were read:

- `data/raw/ncbitaxon_taxa.tsv:222497`: identity, parent, rank, code, empty synonyms, source attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32041`: exact scientific-name object.
- `data/taxa/PATHS.tsv:15004`: identifier/slug.
- `curation/seed_scope.tsv:322744`: date and one-source admission reason matching the embedded event.

The attestation counts one `NAME`, not a strain, genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories found no rows. Under the schema/seeder contract, `strain_count: 0` counts represented BacDive records, not the existence of a strain designation.

Exact non-expanded Nuccore query `txid1036495[Organism:noexp]` returned UID 334303276. The complete [JF803752.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF803752.1), including references, source/rRNA features and sequence, explicitly identifies KLBMP 03668 and taxon 1036495. This is a 685-base 16S marker with both ends marked partial. Its own isolation source is leaf, host Pinus massoniana, location China: Panzhihua. No culture-deposit qualifier, assembly cross-reference or CDS is supplied. Actual/declared length and submitted rRNA transcription agree, with no ambiguous nucleotide symbols.

References name an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin and direct submission on 11-APR-2011, without a study PMID or DOI. The study title does not establish successful biocontrol by this strain. A ribosomal marker is not a genome, functional assay or basis for formal species reassignment. Leaf isolation is this accession's own collection context, not a genus-wide or KLBMP-wide property.

Ten additional native rows were read fully and excluded:

- `data/bvbrc/bvbrc-0016.jsonl.gz:22213`, `data/catalog/ncbi_genbank-0000.jsonl.gz:36103`, `data/catalog/ncbi_refseq-0000.jsonl.gz:30505` and `data/catalog/gtdb_genomes-0006.jsonl.gz:37045` identify Pseudomonas aeruginosa taxid 287, strain Pae_CF67.12d. Their genome identifiers are BV-BRC 287.1676, GCA_001036495.1, GCF_001036495.1 and RS_GCF_001036495.1, with assembly ASM103649v1, sample SAMN03566447 and WGS LEJP00000000.1. Projects are PRJNA282164 for GenBank/BV-BRC and PRJNA224116 for RefSeq/GTDB. GTDB sputum/Canada: Toronto metadata belongs to that Pseudomonas, not this target.
- `data/gold/analyses.jsonl.gz:101385` is Ga0158606, explicitly named Pseudomonas aeruginosa Pae_CF67.12d, with project Gp0189856 and GCA_001036495.1/LEJP00000000. Its direct organism GOLD ID and IMG taxon ID are blank. This is not a target organism-project-analysis chain or a culture-deposit match; neither the GOLD ID nor its referenced project is a genome identifier for KLBMP 03668.
- `data/catalog/ncbi_genbank_historical-0001.jsonl.gz:21309` and `:21310`, plus `data/catalog/ncbi_genbank-0028.jsonl.gz:43513`, concern Klebsiella aerogenes taxid 548, isolate 2000313, sample SAMN34998479 and project PRJNA288601. GCA_031036495.1 and GCA_031036495.2 are replaced historical versions; GCA_031036495.3 is latest. Their WGS versions are ABLWJL000000000.1, .2 and .3, respectively. No version is a Streptomyces link.
- `data/catalog/ncbi_genbank-0056.jsonl.gz:27351` and `data/catalog/ncbi_refseq-0009.jsonl.gz:19515` identify Komagataeibacter piraceti taxid 3229897, strain Hr1, sample SAMN41991991, assembly ASM6103649v1, GCA_061036495.1 and GCF_061036495.1. Projects are PRJNA1127035 and PRJNA224116, respectively. Both are latest complete-genome records; the supplied paired-assembly comparison is `different`, so even within this unrelated group no identical-sequence claim was inferred.

Matching taxid digits embedded in these assembly accessions do not establish identity. Native versions, statuses and identity-chain gaps were preserved. None of these ten rows supports a target genome, deposit, project, phenotype or source-context link.

Spaced/compact strain-name web searches returned broad NCBI listings. Queries for `"JF803752" OR "JF803752.1"` and the full strain with Streptomyces excluding NCBI domains returned no results. Search snippets supplied no biological verdict evidence.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, other mappings, deposits, genomes and graphs should remain empty without explicit source links. The external ribosomal sequence and collection metadata do not require an invented BacDive record or genome link.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain-designation variants, JF803752 (including versioned matches) and UID 334303276. Initial and expanded searches returned the same thirteen rows: three own taxonomy/name/scope rows and ten unrelated candidates. All were read completely. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence statements are bounded to those roots/expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. PubMed query `"KLBMP 03668"[All Fields] OR "JF803752"[All Fields]` returned zero with quoted-phrase warnings. These do not prove universal absence of genomes or publications; indexed searches may miss figure/supplement mentions.

iModulonDB was not run: there is no asserted gene, regulator or expression claim and no covered strain/dataset was identified. The marker does not establish such coverage; this is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Sparse external characterization and excluded numeric catalog matches do not invalidate this NCBI-grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join assembly substrings to taxon IDs, infer strain identity from KLBMP prefixes, transfer another organism's metadata, assign formal species from the partial marker or treat a study title as a phenotype result.

Future taxonomy corrections belong first at NCBI, then in pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional sequence/source-context enrichment requires maintained input and model/seeder support, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Future enrichment needs inspected primary evidence explicitly linking this strain to any proposed deposit, genome or experiment. Keep strain, sequence, sample, project, GOLD and genome identifiers distinct; preserve this accession's leaf-isolation qualifier and narrow evidence scope.

After authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036495`, inspect the emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran in this review.

## Additional Notes

The local single-record skill, checklist and ownership guidance governed this review. Own source rows and nucleotide accession were independently inspected. Before/after YAML SHA-256 was `22fc8be482db0caa18d12be4c88d308968a7151bade314e77b54cd0a670d3f4e`.

Only this new timestamped report was written for the target. No YAML, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota were untouched.
