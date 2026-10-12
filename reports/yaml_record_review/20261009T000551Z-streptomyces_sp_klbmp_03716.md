# YAML Record Review: Streptomyces sp. KLBMP 03716

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03716.yaml`
- Started UTC: 2026-10-09T00:03:13Z
- Finished UTC: 2026-10-09T00:05:51Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036500`. It asserts species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero BacDive records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, genome links and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03716.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03716.yaml --out /private/tmp/klbmp03716-strict.tsv`: passed, one file and zero errors; full TSV was header-only.
- Structured comparisons verified complete backbone/ancestor rows, lineage, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and full type-material, merged-ID and dropped tables were scanned.
- Complete nucleotide XML parsing verified actual/declared length, equality with submitted rRNA transcription and no non-ACGT symbols. This is annotation consistency, not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Bounded individual checks do not prove corpus reproduction. The embedded event was read; stated ignored-inclusive searches found no separate target history artifact. Graph product validation is inapplicable without graph nodes. No focused substitute for a corpus gate was invented.

## Identity and Grounding

Full [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036500&retmode=xml) agrees with the identifier, label, rank, parent and code. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036500) confirms all ten root-first ancestor IDs. Pinned labels/ranks agree with the live chain through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

NCBI species rank for this unnamed strain-associated taxon does not establish a formally described species or synonymy with a congener. Exact grounding denotes this specific NCBI identity. Live EFetch has no other names; pinned synonyms are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete target source rows were read:

- `data/raw/ncbitaxon_taxa.tsv:222502`: identity, parent, rank, code, empty synonyms, source and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32046`: exact scientific-name object.
- `data/taxa/PATHS.tsv:15009`: identifier/slug.
- `curation/seed_scope.tsv:322749`: date and one-source admission reason matching the seed event.

The attestation counts one `NAME`, not a genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema/seeder contract, `strain_count: 0` counts represented BacDive records and does not deny the source strain designation.

Exact non-expanded Nuccore query `txid1036500[Organism:noexp]` returned UID 334303279. The complete [JF803755.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF803755.1), including references, source/rRNA features and sequence, explicitly identifies this taxon and KLBMP 03716. It supplies a 693-base 16S marker with both ends partial. Its own source is stem, host Pinus massoniana, location China: Panzhihua. There is no culture-deposit qualifier, assembly cross-reference or CDS. Declared length, actual sequence and submitted transcription agree without ambiguous symbols.

References name an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin and direct submission on 11-APR-2011, without a study PMID or DOI. The title does not establish successful disease control by this strain. A partial ribosomal marker is not a genome, functional assay or formal species reassignment. Collection context applies to this accession.

Three additional native candidates were read completely and excluded:

- `data/catalog/gtdb_genomes-0017.jsonl.gz:4582` describes Thiomonas sp. Sup16B3, NCBI taxid 2493109, with GTDB species label Thiomonas arsenitoxydans. Its genome is RS_GCF_900634585.1/GCA_900634585.1, sample SAMEA5160197 and project PRJNA224116. The matching value 1036500 is its contig N50. These source-specific classifications were preserved; neither classification denotes the target Streptomyces.
- `data/catalog/ncbi_genbank-0059.jsonl.gz:10833` is GCA_943332175.1, Singulisphaera sp. GP187 taxid 1882752, isolate HRS-HS6-bin-74, sample SAMEA14435024, project PRJEB52406 and WGS CALQOK000000000.1. Its total and ungapped genome lengths are 1036500. The source flags it as a fragmented metagenome-derived assembly. A genome length is not a target taxon identifier.
- `data/catalog/allthebacteria.tsv.xz:1752000` names Clostridioides difficile, sample SAMN13638954, run SRR10869638 and analysis ERZ25694401. The matching digits are inside SeqKit sum `seqkit.v0.1_DLS_k0_a3c5cb31036500da397c1569b04f7f0e`. All three source filters pass, but neither the checksum nor its download URL establishes a target identity chain. SeqKit sum is not an MD5 identifier.

These rows supply no target strain-genome, sample, project, deposit or phenotype link.

Spaced/compact strain-name web searches returned broad NCBI listings. Queries for `"JF803755" OR "JF803755.1"` and the full strain with Streptomyces excluding NCBI domains returned no results. Snippets supplied no biological verdict evidence.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, other mappings, deposits, genomes and graphs should remain empty without explicit identity chains. The external marker/source context do not require an invented BacDive entry or genome link.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain variants, JF803755 (including versioned matches) and UID 334303279. Initial and expanded searches returned the same six rows: three own taxonomy/name/scope rows and three unrelated candidates. All were read fully. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence statements are bounded to those roots/expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. PubMed query `"KLBMP 03716"[All Fields] OR "JF803755"[All Fields]` returned zero with quoted-phrase warnings. These are bounded outcomes, not universal genome or literature absence; figure/supplement mentions may escape indexed queries.

iModulonDB was not run: there is no asserted gene, regulator or expression claim and no covered strain/dataset was identified. The marker does not establish coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Sparse characterization and unrelated numerical matches do not invalidate the grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join on numeric metrics or checksum substrings, equate strains by KLBMP prefix, transfer another organism's metadata or infer formal species/phenotype from the partial marker or study title.

Future taxonomy corrections belong first at NCBI, then in pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional sequence/source-context enrichment needs maintained inputs and model/seeder support, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Future enrichment must explicitly link this strain to any proposed deposit, genome or experiment. Keep strain, sequence, sample, project and genome identities distinct and preserve this accession's own stem source and narrow evidence scope.

After an authorized input/seeder correction, run a focused regression test, `just seed-canary NCBITaxon:1036500`, inspect its output, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

The local single-record skill, checklist and ownership guidance governed the review. Own source rows and accession were independently inspected. Before/after YAML SHA-256 was `dc58430d4cc9a6a49e25e965ea84d56b47fcf6a8fdfbb8fdbf79c2ca331772a3`.

Only this new timestamped report was written for the target. No YAML, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
