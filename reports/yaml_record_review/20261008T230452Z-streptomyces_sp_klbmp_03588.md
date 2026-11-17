# YAML Record Review: Streptomyces sp. KLBMP 03588

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03588.yaml`
- Started UTC: 2026-10-08T23:01:39Z
- Finished UTC: 2026-10-08T23:04:52Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036487`, Streptomyces sp. KLBMP 03588. It asserts species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero BacDive strain records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, strain/genome links and causal graphs are unasserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03588.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03588.yaml --out /private/tmp/klbmp03588-strict.tsv`: passed, one file and zero errors. The complete TSV was header-only.
- Structured comparisons checked the complete backbone row, all ten ancestors, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and complete type-material, merged-ID and dropped tables were scanned.
- Complete nucleotide XML parsing confirmed declared versus actual length, equality with the submitted rRNA transcription and absence of non-ACGT symbols. This is annotation consistency, not independent alignment or species identification.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. The embedded event was inspected; bounded searches found no separate target history artifact. Graph product validation is not applicable without graph nodes. No focused substitute for a corpus-wide gate was invented.

## Identity and Grounding

The complete [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036487&retmode=xml) agrees with the ID, label, species rank, parent 2593676 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036487) confirms all ten root-first ancestor IDs. Ancestor labels and ranks match the pinned lineage through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

Species rank is the authority's rank for this unnamed strain-associated taxon, not evidence of a formally described species. Exact grounding denotes this precise NCBI identity, not equivalence with a named congener. Live EFetch supplies no other names; pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete native source rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222489`: identity, rank, parent, code, empty synonyms, attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32033`: exact scientific-name object, empty unique-name field.
- `data/taxa/PATHS.tsv:14996`: ID and slug.
- `curation/seed_scope.tsv:322736`: date and one-source admission reason matching the seed event.

The attestation unit is `NAME`, not strain, assembly or experiment. Full exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under `src/taxonmech/schema/taxonmech.yaml` and the inspected BacDive construction in `src/taxonmech/seed.py`, `strain_count: 0` means zero represented BacDive records, not a denial that a named strain exists.

Exact non-expanded Nuccore query `txid1036487[Organism:noexp]` returned one record, UID 334303270. The complete [JF803746.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF803746.1) identifies this taxon and strain KLBMP 03588. It is a 706-base partial 16S rRNA sequence, with both ends marked partial. Its own isolation-source qualifier is leaf, with host Pinus massoniana and location China: Panzhihua. No culture-deposit qualifier or assembly cross-reference is supplied. Source and rRNA features were read fully; there is no CDS feature. Actual sequence length and submitted transcription agree, without ambiguous nucleotide symbols.

The sequence cites an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin, plus a direct submission dated 11-APR-2011, without a study PMID or DOI. The title does not demonstrate successful disease control by this strain. A partial ribosomal marker is not a genome, functional assay or basis for reassignment to a named species. Leaf isolation is this source record's collection context, not evidence for every Streptomyces or KLBMP strain, and it must not be replaced by neighboring records' stem or rhizosphere metadata.

All twenty additional local candidate rows were read completely, including full JSON objects and TSV headers/rows, and excluded as numeric near matches:

- Five `data/catalog/ncbi_genbank-0003.jsonl.gz` rows, at 32471, 32474, 32475, 32476 and 32478, concern Listeria monocytogenes taxid 1639 with FDA1036487-prefixed strain designations. Their assemblies are GCA_004631415.1, GCA_004631475.1, GCA_004631495.1, GCA_004631515.1 and GCA_004631555.1. The embedded numeric string does not identify this Streptomyces.
- `data/bvbrc/bvbrc-0000.jsonl.gz:44391`, `data/catalog/ncbi_genbank-0009.jsonl.gz:7068`, `data/catalog/ncbi_refseq-0002.jsonl.gz:41237` and `data/catalog/gtdb_genomes-0014.jsonl.gz:6869` concern Staphylococcus aureus taxid 1280, strain 49-069. GCA_010364875.1, GCF_010364875.1, RS_GCF_010364875.1, BV-BRC 1280.25758 and assembly name ASM1036487v1 are not target identities. Their SAMN13948073 and project references likewise supply no link to KLBMP 03588.
- `data/catalog/ncbi_genbank-0065.jsonl.gz:33522` concerns an uncultured bacterium, taxid 77133, isolate HUMAGS_000094, assembly GCA_978049185.1. Its sample SAMEA121036487 contains the search digits but is not this taxon identifier.
- Ten `data/catalog/allthebacteria.tsv.xz` rows, at 1635018, 1635019, 1716559, 1716560, 1716561, 1716564, 1716567, 1716568, 1716569 and 1716570, match run accessions SRR10364870 through SRR10364879. Nine name Salmonella enterica and one names Escherichia coli. These runs, samples, ENA analysis accessions, FASTA URLs and SeqKit sums establish no identity chain to the target.

Spaced and compact strain-designation web searches returned this taxon's NCBI browser entry and broad Streptomyces taxonomy listings. Discovery snippets were not used as independent evidence; this taxon's complete primary taxonomy response was inspected directly. Subsequent unrestricted queries for JF803746 and JF803746.1, and a genus plus complete strain-designation query excluding NCBI, returned no results. These bounded searches do not establish literature absence.

## Completeness

Complete enough for its supported taxonomy-seed scope. Optional nomenclature, synonyms, mappings, deposits, genomes and graphs appropriately remain empty without an explicit identity chain. The external strain designation and ribosomal sequence do not require inventing a BacDive entry or adding a genome link. Unasserted source-context details are not a required taxonomic seed field.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain-designation variants, JF803746 with optional version and nucleotide UID 334303270. Initial and expanded searches each returned the same 23 rows: three own name/taxonomy/scope rows and twenty unrelated numeric matches. All were read completely. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence statements are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. The PubMed query `"KLBMP 03588"[All Fields] OR "JF803746"[All Fields]` returned zero with quoted-phrase warnings. These are bounded query outcomes, not universal genome or literature absence. No strain-genome chain was established.

iModulonDB was not run: the YAML asserts no gene, regulator or expression claim and no covered strain/dataset was identified. The external ribosomal marker does not establish such coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. Limited external characterization and unrelated catalog search hits do not invalidate this NCBI-grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not infer strain equivalence from the KLBMP prefix, assign a formal species from the partial marker, transfer isolation-source metadata between records, join on numeric substrings, or promote the unpublished study title into a biocontrol phenotype. Genus-level traits cannot supply strain-specific assertions.

Future taxonomy corrections belong first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional sequence or source-context enrichment requires maintained input and suitable model/seeder handling, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Before optional enrichment, inspect primary evidence explicitly linking this strain to a proposed deposit, genome or experiment, keeping sequence, sample, project and genome identifiers distinct. Preserve this accession's own leaf-isolation qualifier and its narrow scope.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036487`, inspect the emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

The single-record skill, checklist, ownership guidance and documented validators governed the review. Own source rows and accession were inspected independently. Before/after YAML SHA-256 was `29c2d68c28fbf267bf29f80e6c968af7e756e0083a8cc440e389123df998d9bf`.

Only this new timestamped report was written for the target. No record, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
