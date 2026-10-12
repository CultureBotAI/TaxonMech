# YAML Record Review: Streptomyces sp. KLBMP 03665

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03665.yaml`
- Started UTC: 2026-10-08T23:39:44Z
- Finished UTC: 2026-10-08T23:42:16Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036494`, Streptomyces sp. KLBMP 03665. Stored assertions are species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero represented BacDive strains, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, genome links and causal graphs are unasserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved exactly one YAML and no previous report for this stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03665.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03665.yaml --out /private/tmp/klbmp03665-strict.tsv`: passed, one file and zero errors; the entire TSV was header-only.
- Structured comparisons checked the complete backbone row, all ten ancestors, source attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and complete type-material, merged-ID and dropped tables were scanned.
- Full nucleotide XML parsing confirmed actual/declared length, equality of sequence and submitted rRNA transcription, and absence of non-ACGT symbols. This is annotation consistency, not an independent sequence alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not establish corpus reproduction. The embedded event was read; bounded searches found no separate target history artifact. Graph product validation is not applicable without graph nodes. No focused substitute for a corpus-wide gate was invented.

## Identity and Grounding

Full [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036494&retmode=xml) agrees with the identifier, label, species rank, parent 2593676 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036494) confirms all ten root-first ancestor IDs. The pinned lineage labels/ranks agree with the live chain through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root in its displayed lineage; Datasets includes it. This is a presentation difference, not a conflict.

Species rank does not make this unnamed strain-associated taxon a formally described species. Exact grounding denotes this specific NCBI identity, not a named congener or other KLBMP strain. Live EFetch supplies no other names; pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped entry and no backbone children.

## Evidence

Complete source rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222496`: identity, rank, parent, genetic code, empty synonyms, attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32040`: exact scientific-name object.
- `data/taxa/PATHS.tsv:15003`: identifier/slug.
- `curation/seed_scope.tsv:322743`: date and one-source admission reason matching the embedded seed event.

One `NAME` is counted, not a strain, genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema/seeder definition, `strain_count: 0` counts represented BacDive records and does not deny the source strain designation.

Exact non-expanded Nuccore query `txid1036494[Organism:noexp]` returned UID 334303293. The complete [JF803769.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF803769.1) identifies this taxon and KLBMP 03665. Its 720-base partial 16S sequence has both ends marked partial. Its own isolation source is rhizosphere, with host Pinus massoniana and location China: Panzhihua. The complete source/rRNA features, references and sequence were read; no culture-deposit qualifier, assembly cross-reference or CDS is supplied. Sequence length and submitted rRNA transcription agree, without ambiguous nucleotide symbols.

The references name an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin and a direct submission dated 11-APR-2011, without a study PMID or DOI. A study title is not evidence that this particular strain controlled disease. The partial marker is not a genome or functional assay. Rhizosphere is this accession's source context; another strain's stem or leaf metadata must not be substituted.

Three additional local candidates were fully read and excluded:

- `data/catalog/gtdb_genomes-0007.jsonl.gz:26319` is Pseudomonas aeruginosa taxid 287, strain BTP034, RS_GCF_001086755.1/GCA_001086755.1, assembly ASM108675v1, sample SAMN03787335 and project PRJNA224116. The matching value 1036494 is its contig N50, not a taxon ID. Its associated-infection and USA: Rochester; Minnesota metadata belong to that Pseudomonas.
- `data/catalog/allthebacteria.tsv.xz:1505324` names Pedobacter cryoconitis, sample SAMN10364940, run SRR8156494 and analysis ERZ25501340. Its assembly pipeline passes; HQ/sylph filters record SYLPH_RESULTS_FAIL, current sylph species is unknown and prior sylph label is Pedobacter cryoconitis_C. The digits match a substring of the sample accession.
- `data/catalog/allthebacteria.tsv.xz:2702747` names Campylobacter coli, sample SAMN37598639, run SRR26215415 and analysis ERZ27010920. All three filters pass; sylph label is Campylobacter_D coli. The matching digits are in SeqKit sum `seqkit.v0.1_DLS_k0_21de87380b9021c5176729ba11036494`, not in a taxon/strain identifier.

The ATB download URLs, source statuses and sums were inspected without treating them as identity evidence. A metric, sample substring or checksum substring cannot establish a target genome link. SeqKit sums are not MD5 identifiers.

Spaced and compact strain-name web searches returned broad NCBI listings. Queries for `"JF803769" OR "JF803769.1"` and the full strain with Streptomyces excluding NCBI domains returned no results. Search snippets supplied no biological verdict evidence.

## Completeness

Complete enough for the record's supported taxonomy-seed scope. Optional nomenclature, other mappings, deposits, genomes and graphs should remain unasserted without a source identity chain. The external ribosomal sequence and source context do not require an invented BacDive record or genome link.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files within `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions included taxid, slug, spaced/compact strain variants, JF803769 (including versioned matches) and UID 334303293. Initial and expanded scans returned the same six rows: three own taxonomy/name/scope rows and three unrelated candidates. All were read completely. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence findings are limited to those roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. PubMed query `"KLBMP 03665"[All Fields] OR "JF803769"[All Fields]` returned zero with quoted-phrase warnings. These are bounded query results, not universal absence of genomes or literature; indexed searches can miss figure or supplement mentions.

iModulonDB was not run: the YAML asserts no gene, regulator or expression claim, and no covered strain/dataset was identified. A ribosomal marker does not establish coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Sparse external characterization and unrelated native candidates do not invalidate this taxonomic seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join numerical substrings, equate strains by KLBMP prefix, reassign species from the partial marker or transfer phenotypes from the study title or unrelated catalog records.

Future taxonomy corrections belong first at NCBI, then in pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Seeder defects belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Any optional sequence/source-context enrichment requires maintained input and model/seeder support, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Before enrichment, obtain inspected primary evidence explicitly linking this strain to any proposed deposit, genome or experiment. Preserve separate sample, project, sequence and genome identities and this accession's own rhizosphere source.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036494`, inspect the result, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

Single-record guidance, ownership rules and checklist governed the review. Own source rows and accession were independently inspected. Before/after YAML SHA-256 was `c6468206f53e81265fc562b164e02d265f484525f8ec06221336f91e65259707`.

Only this timestamped report was written for the target. No YAML, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
