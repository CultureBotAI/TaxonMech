# YAML Record Review: Streptomyces sp. KLBMP 03660

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03660.yaml`
- Started UTC: 2026-10-08T23:22:05Z
- Finished UTC: 2026-10-08T23:24:45Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036491`, Streptomyces sp. KLBMP 03660. Stored claims are species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero BacDive strain records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, strain/genome links and causal graphs are unasserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03660.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03660.yaml --out /private/tmp/klbmp03660-strict.tsv`: passed, one file and zero errors; the complete TSV was header-only.
- Structured comparisons checked the complete backbone row, all ten ancestors, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and complete type-material, merged-ID and dropped tables were scanned.
- Complete nucleotide XML parsing confirmed declared versus actual length, equality with the submitted rRNA transcription and absence of non-ACGT symbols. This checks annotation consistency, not independent alignment or species identification.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. The embedded event was inspected; bounded searches found no separate target history artifact. Graph product validation is not applicable without graph nodes. No focused substitute for a corpus-wide gate was invented.

## Identity and Grounding

The complete [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036491&retmode=xml) agrees with the ID, label, species rank, parent 2593676 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036491) confirms all ten root-first ancestor IDs. Ancestor labels and ranks match the pinned lineage through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

Species rank is the authority's rank for this unnamed strain-associated taxon, not evidence of a formally described species. Exact grounding denotes this precise NCBI identity, not equivalence with a named congener. Live EFetch supplies no other names; pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete native source rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222493`: identity, rank, parent, code, empty synonyms, attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32037`: exact scientific-name object, empty unique-name field.
- `data/taxa/PATHS.tsv:15000`: ID and slug.
- `curation/seed_scope.tsv:322740`: date and one-source admission reason matching the seed event.

The attestation unit is `NAME`, not strain, assembly or experiment. Full exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema and seeder contract, `strain_count: 0` means zero represented BacDive records, not a denial that a named strain exists.

Exact non-expanded Nuccore query `txid1036491[Organism:noexp]` returned one record, UID 334303273. The complete [JF803749.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF803749.1) identifies this taxon and strain KLBMP 03660. It is a 685-base partial 16S rRNA sequence, with both ends marked partial. Its own isolation-source qualifier is stem, with host Pinus massoniana and location China: Panzhihua. No culture-deposit qualifier or assembly cross-reference is supplied. Source and rRNA features were read fully; there is no CDS feature. Actual sequence length and submitted transcription agree, without ambiguous nucleotide symbols.

The sequence cites an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin, plus a direct submission dated 11-APR-2011, without a study PMID or DOI. The title does not demonstrate successful disease control by this strain. A partial ribosomal marker is not a genome, functional assay or basis for reassignment to a named species. Stem isolation is this accession's collection context, not evidence for every Streptomyces or KLBMP strain.

Eleven additional local candidate rows were read completely and excluded:

- `data/gold/organisms.jsonl.gz:243120`, `data/gold/projects.jsonl.gz:104273` and `data/gold/analyses.jsonl.gz:86771` and `:156134` concern Salmonella enterica serovar Typhi strain 1036491, not NCBI taxon 1036491. The organism is taxid 90370, GOLD Go0314455; the project is Gp0162930 with SAMEA2160515 and PRJEB3215. Analyses Ga0142644 and Ga0248258 name that Salmonella and Gp0162930, with blank direct organism-ID fields, IMG IDs 8114897698 and 8030485420, and GCA_001367555.2/LT904885. No culture-deposit match to KLBMP 03660 exists in these rows. The GOLD IDs and project/sample references are not target genome identifiers.
- `data/bvbrc/bvbrc-0027.jsonl.gz:47907` is Salmonella taxid 90370, genome 90370.1569, strain 1036491 and GCF_001367555.1. `data/catalog/gtdb_genomes-0012.jsonl.gz:13398` is GB_GCA_001367555.2 for that same Salmonella designation. These are not Streptomyces links.
- `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:11208`, `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:7228` and `:7229`, and `data/catalog/ncbi_genbank-0001.jsonl.gz:1954` all name Salmonella taxid 90370, strain 1036491. Their respective accessions/statuses are GCF_001367555.1 suppressed, GCA_001367555.1 replaced, GCA_001367555.2 replaced and GCA_001367555.3 latest. Versions and statuses were preserved rather than collapsed or transferred to the target.
- `data/catalog/allthebacteria.tsv.xz:1716571` names Campylobacter jejuni, sample SAMN13159399, run SRR10364917 and analysis ERZ25665714. Its matching digits occur inside the run accession. Its FASTA URL, passing filters and SeqKit sum do not establish a target identity chain.

Spaced and compact strain-name searches returned the target's NCBI browser entry and broad taxonomy listings. Subsequent accession/full-strain queries were not collectively empty: broader search hits included exopolysaccharide and maize-rhizosphere literature. In the accessible [Wiley article](https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/1758-2229.70296), the inspected reference contexts name Glutamicibacter halophytocota KLBMP 5180 and separately contain DOI 10.1007/s11274-023-03660-x. Exact searches of its parsed HTML found neither JF803749 nor KLBMP 03660. This supports a bibliographic-token near match, not a target phenotype. A separate accession-only query for JF803749 or JF803749.1 returned no results.

## Completeness

Complete enough for its supported taxonomy-seed scope. Optional nomenclature, synonyms, mappings, deposits, genomes and graphs appropriately remain empty without an explicit identity chain. The external strain designation and ribosomal sequence do not require inventing a BacDive entry or adding a genome link. Unasserted source-context details are not a required taxonomic seed field.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain-designation variants, JF803749 with optional version and nucleotide UID 334303273. Initial and expanded searches each returned the same fourteen rows: three own name/taxonomy/scope rows and eleven unrelated candidates. All were read completely. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence statements are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. The PubMed query `"KLBMP 03660"[All Fields] OR "JF803749"[All Fields]` returned zero with quoted-phrase warnings. These are bounded query outcomes, not universal genome or literature absence. No strain-genome chain was established.

iModulonDB was not run: the YAML asserts no gene, regulator or expression claim and no covered strain/dataset was identified. The external ribosomal marker does not establish such coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. Limited external characterization, unrelated native catalog hits and unverified discovery leads do not invalidate this NCBI-grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not confuse a numeric Salmonella strain designation with this NCBI taxon, join on numeric substrings, infer equivalence from a KLBMP prefix, assign a formal species from the partial marker, or transfer another organism's phenotype. Isolation metadata and unpublished study titles must retain their original scope.

Future taxonomy corrections belong first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional sequence or source-context enrichment requires maintained input and suitable model/seeder handling, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Before optional enrichment, inspect primary evidence explicitly linking this strain to a proposed deposit, genome or experiment, keeping sequence, sample, project and genome identifiers distinct. Preserve this accession's own stem-isolation qualifier and its narrow scope.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036491`, inspect the emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

The single-record skill and checklist governed the review, with unchanged local ownership guidance and documented validators. Own source rows and accession were inspected independently. Before/after YAML SHA-256 was `a36a0f7970fc430b70c945f0332c45a5a49fc6c52bb064faa17137afa6e677c5`.

The [SciEngine PDF lead](https://www.sciengine.com/cfs/files/pdfs/view/2095-2341/1D06B9DAAB1F42AC91922BDA2210B10A.pdf) and [OUCI maize-rhizosphere lead](https://ouci.dntb.gov.ua/en/works/7np8wMbl/) returned open errors. Their snippets suggest different KLBMP strains and DOI-suffix matches, but their full text was not inspected; they remain unverified leads and supply no biological verdict evidence. The Wiley identity check covered parsed main HTML and reference contexts, not every image or supplement. Access failures were not treated as no-match results.

Only this new timestamped report was written for the target. No record, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
