# YAML Record Review: Streptomyces sp. KLBMP 03695

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03695.yaml`
- Started UTC: 2026-10-08T23:54:41Z
- Finished UTC: 2026-10-08T23:56:45Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036498`. Stored assertions are species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, code 11, `EXACT` grounding, `SEEDED` mapping status, zero BacDive records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, genome links and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved exactly one YAML and no prior report for this stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03695.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03695.yaml --out /private/tmp/klbmp03695-strict.tsv`: passed, one file and zero errors; full TSV was header-only.
- Structured comparisons verified complete backbone/ancestor rows, lineage, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and full type-material, merged-ID and dropped tables were scanned.
- Complete nucleotide XML parsing verified declared/actual length, equality with submitted rRNA transcription and no non-ACGT symbols. This is annotation consistency, not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. The embedded event was inspected; stated ignored-inclusive searches found no separate target history artifact. Graph product validation is inapplicable without graph nodes. No invented focused substitute for a corpus gate was used.

## Identity and Grounding

Full [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036498&retmode=xml) agrees with the identifier, label, rank, parent and code. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036498) confirms all ten root-first ancestor IDs. Pinned labels/ranks agree with the live lineage through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root in its displayed lineage while Datasets includes it; this is not a taxonomic conflict.

Species rank for this unnamed strain-associated NCBI taxon is not evidence of a formally described species or synonymy with a congener. Exact grounding denotes this specific NCBI identity. Live EFetch has no other names; pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete target source rows were read:

- `data/raw/ncbitaxon_taxa.tsv:222500`: identity, parent, rank, code, empty synonyms, attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32044`: exact scientific-name object.
- `data/taxa/PATHS.tsv:15007`: identifier/slug.
- `curation/seed_scope.tsv:322747`: admission date and one-source reason matching the embedded event.

One `NAME` is counted, not a genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. The schema/seeder defines `strain_count: 0` as zero represented BacDive records, not denial that the source strain designation exists.

Exact non-expanded Nuccore query `txid1036498[Organism:noexp]` returned UID 334303295. The complete [JF803771.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF803771.1), including references, source/rRNA features and sequence, explicitly identifies this taxon and KLBMP 03695. It supplies a 682-base partial 16S marker with both ends partial. Its own source is rhizosphere, host Pinus massoniana, location China: Panzhihua. No culture-deposit qualifier, assembly cross-reference or CDS is supplied. Declared length, actual sequence and submitted rRNA transcription agree without ambiguous symbols.

References name an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin and a direct submission dated 11-APR-2011, without a study PMID or DOI. The title does not demonstrate successful disease control by this strain. A partial ribosomal marker is not a genome, functional assay or basis for a formal species reassignment. Rhizosphere isolation is this accession's collection context.

Four additional catalog rows were read completely and excluded:

- `data/bvbrc/bvbrc-0000.jsonl.gz:44400` describes Staphylococcus aureus taxid 1280, strain 49-079, genome 1280.25767, GCA_010364985.1, sample SAMN13948074 and project PRJNA604020.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:7073` and `data/catalog/ncbi_refseq-0002.jsonl.gz:41242` describe that Staphylococcus strain and respectively GCA_010364985.1/GCF_010364985.1, assembly ASM1036498v1, sample SAMN13948074 and WGS JAAFLV000000000.1. Both are latest contig-level records; projects are PRJNA604020 and PRJNA224116, respectively.
- `data/catalog/gtdb_genomes-0003.jsonl.gz:35299` is RS_GCF_010364985.1, likewise Staphylococcus aureus taxid 1280, strain 49-079. Its Bone/Joint source and USA: Texas location belong to that organism, not KLBMP 03695.

Matching digits occur within assembly accessions/names and do not establish an exact target taxon identity. No target genome, sample, project, deposit or phenotype chain follows from these rows.

Spaced/compact strain-name web searches returned broad NCBI taxonomy listings. Queries for `"JF803771" OR "JF803771.1"` and the full strain with Streptomyces excluding NCBI domains returned no results. Search snippets supplied no biological verdict evidence.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, other mappings, deposits, genomes and graphs should remain unasserted without explicit evidence. The external marker/source metadata do not require an invented BacDive entry or genome link.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain variants, JF803771 (including versioned matches) and UID 334303295. Initial and expanded searches returned the same seven rows: three own taxonomy/name/scope rows and four unrelated candidates. All were read completely. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence statements are bounded to these roots/expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. PubMed query `"KLBMP 03695"[All Fields] OR "JF803771"[All Fields]` returned zero with quoted-phrase warnings. These are bounded outcomes, not universal genome/literature absence; indexed queries may miss figure or supplement mentions.

iModulonDB was not run: there is no asserted gene, regulator or expression claim and no covered strain/dataset was identified. A ribosomal marker does not establish such coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Sparse characterization and excluded numeric catalog matches do not invalidate the grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join numeric substrings, equate KLBMP-prefix strains, transfer Staphylococcus metadata or infer formal species/phenotype from a partial marker or study title.

Future taxonomic corrections belong first at NCBI, then in pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional source-context/sequence enrichment requires maintained inputs and model/seeder support, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Any later enrichment needs inspected primary evidence explicitly linking this strain to a proposed deposit, genome or experiment. Keep sequence, sample, project and genome identities distinct; preserve this accession's own rhizosphere source and narrow evidence scope.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036498`, inspect the result, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

The local single-record skill, checklist and ownership guidance governed this review. Own source rows and accession were independently inspected. Before/after YAML SHA-256 was `559fc1738381dad43c4d7cea7216cebdba5b3bef4758c5cf2f7b97a663c504e0`.

Only this new timestamped report was written for the target. No YAML, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
