# YAML Record Review: Streptomyces sp. KLBMP 03661

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03661.yaml`
- Started UTC: 2026-10-08T23:26:05Z
- Finished UTC: 2026-10-08T23:31:20Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036492`, Streptomyces sp. KLBMP 03661. Stored claims are species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero BacDive strain records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, strain/genome links and causal graphs are unasserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03661.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03661.yaml --out /private/tmp/klbmp03661-strict.tsv`: passed, one file and zero errors; the complete TSV was header-only.
- Structured comparisons checked the complete backbone row, all ten ancestors, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and complete type-material, merged-ID and dropped tables were scanned.
- Complete nucleotide XML parsing confirmed declared versus actual length, equality with the submitted rRNA transcription and absence of non-ACGT symbols. This checks annotation consistency, not independent alignment or species identification.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. The embedded event was inspected; bounded searches found no separate target history artifact. Graph product validation is not applicable without graph nodes. No focused substitute for a corpus-wide gate was invented.

## Identity and Grounding

The complete [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036492&retmode=xml) agrees with the ID, label, species rank, parent 2593676 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036492) confirms all ten root-first ancestor IDs. Ancestor labels and ranks match the pinned lineage through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

Species rank is the authority's rank for this unnamed strain-associated taxon, not evidence of a formally described species. Exact grounding denotes this precise NCBI identity, not equivalence with a named congener. Live EFetch supplies no other names; pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete native source rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222494`: identity, rank, parent, code, empty synonyms, attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32038`: exact scientific-name object, empty unique-name field.
- `data/taxa/PATHS.tsv:15001`: ID and slug.
- `curation/seed_scope.tsv:322741`: date and one-source admission reason matching the seed event.

The attestation unit is `NAME`, not strain, assembly or experiment. Full exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema and seeder contract, `strain_count: 0` means zero represented BacDive records, not a denial that a named strain exists.

Exact non-expanded Nuccore query `txid1036492[Organism:noexp]` returned one record, UID 334303274. The complete [JF803750.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF803750.1) identifies this taxon and strain KLBMP 03661. It is a 689-base partial 16S rRNA sequence, with both ends marked partial. Its own isolation-source qualifier is stem, with host Pinus massoniana and location China: Panzhihua. No culture-deposit qualifier or assembly cross-reference is supplied. Source and rRNA features were read fully; there is no CDS feature. Actual sequence length and submitted transcription agree, without ambiguous nucleotide symbols.

The sequence cites an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin, plus a direct submission dated 11-APR-2011, without a study PMID or DOI. The title does not demonstrate successful disease control by this strain. A partial ribosomal marker is not a genome, functional assay or basis for reassignment to a named species. Stem isolation is this accession's collection context, not evidence for every Streptomyces or KLBMP strain.

Four additional local catalog candidates were read completely and excluded:

- `data/bvbrc/bvbrc-0000.jsonl.gz:44393` is Staphylococcus aureus taxid 1280, strain 48-001, BV-BRC genome 1280.25760, with GCA_010364925.1, SAMN13948069 and PRJNA604020.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:7070` and `data/catalog/ncbi_refseq-0002.jsonl.gz:41239` both explicitly identify Staphylococcus aureus taxid 1280 and strain 48-001. They name GCA_010364925.1 and GCF_010364925.1, respectively, assembly ASM1036492v1, sample SAMN13948069 and WGS JAAFMA000000000.1. Their project IDs are PRJNA604020 and PRJNA224116, respectively. Both are latest contig-level assemblies for that other organism.
- `data/catalog/gtdb_genomes-0012.jsonl.gz:35065` is RS_GCF_010364925.1, also Staphylococcus aureus taxid 1280, strain 48-001 and ASM1036492v1. Its respiratory isolation and USA: Texas metadata belong to that Staphylococcus record, not to KLBMP 03661.

The matching digits are embedded in assembly accessions/names, not exact target taxon IDs. These four rows do not support a target genome, sample, project, deposit or phenotype link. Shared metadata within that unrelated assembly group does not establish identity with this Streptomyces.

Spaced and compact strain-name web searches returned broad NCBI taxonomy listings. Subsequent queries for `"JF803750" OR "JF803750.1"` and `"Streptomyces" "KLBMP 03661"` excluding NCBI domains returned no results. Search snippets supplied no biological verdict evidence; the primary taxonomy and complete nucleotide responses were inspected directly.

## Completeness

Complete enough for its supported taxonomy-seed scope. Optional nomenclature, synonyms, mappings, deposits, genomes and graphs appropriately remain empty without an explicit identity chain. The external strain designation and ribosomal sequence do not require inventing a BacDive entry or adding a genome link. Unasserted source-context details are not a required taxonomic seed field.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain-designation variants, JF803750 (also matching its versioned form) and nucleotide UID 334303274. Initial and expanded searches each returned the same seven rows: three own name/taxonomy/scope rows and four unrelated candidates. All were read completely. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence statements are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. The PubMed query `"KLBMP 03661"[All Fields] OR "JF803750"[All Fields]` returned zero with quoted-phrase warnings. These are bounded query outcomes, not universal genome or literature absence; exact PubMed searches can miss mentions confined to figures or supplements. No strain-genome chain was established.

iModulonDB was not run: the YAML asserts no gene, regulator or expression claim and no covered strain/dataset was identified. The external ribosomal marker does not establish such coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. Limited external characterization and unrelated native catalog hits do not invalidate this NCBI-grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join on numeric substrings, infer identity from a KLBMP prefix, assign a formal species from the partial marker, or transfer Staphylococcus assembly metadata. Isolation metadata and unpublished study titles must retain their original scope.

Future taxonomy corrections belong first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional sequence or source-context enrichment requires maintained input and suitable model/seeder handling, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Before optional enrichment, inspect primary evidence explicitly linking this strain to a proposed deposit, genome or experiment, keeping sequence, sample, project and genome identifiers distinct. Preserve this accession's own stem-isolation qualifier and its narrow scope.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036492`, inspect the emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

The single-record skill and checklist governed the review, with unchanged local ownership guidance and documented validators. Own source rows and accession were inspected independently. Before/after YAML SHA-256 was `4161519e7d833d5a7d453b56d9c2b415ba68fc9523d98498166eed29c65f7108`.

Only this new timestamped report was written for the target. No record, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
