# YAML Record Review: Streptomyces sp. KLBMP 03533

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03533.yaml`
- Started UTC: 2026-10-08T22:36:29Z
- Finished UTC: 2026-10-08T22:39:56Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036482`, Streptomyces sp. KLBMP 03533. It asserts species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero BacDive strain records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, strain/genome links and causal graphs are unasserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03533.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03533.yaml --out /private/tmp/klbmp03533-strict.tsv`: passed, one file and zero errors. The complete TSV was header-only.
- Structured comparisons checked the complete backbone row, all ten ancestors, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and complete type-material, merged-ID and dropped tables were scanned.
- Complete nucleotide XML parsing confirmed declared versus actual length, equality with the submitted rRNA transcription and absence of non-ACGT symbols. This is annotation consistency, not independent alignment or species identification.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. The embedded event was inspected; bounded searches found no separate target history artifact. Graph product validation is not applicable without graph nodes. No focused substitute for a corpus-wide gate was invented.

## Identity and Grounding

The complete [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036482&retmode=xml) agrees with the ID, label, species rank, parent 2593676 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036482) confirms all ten root-first ancestor IDs. Ancestor labels and ranks match the pinned lineage through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

Species rank is the authority's rank for this unnamed strain-associated taxon, not evidence of a formally described species. Exact grounding denotes this precise NCBI identity, not equivalence with a named congener. Live EFetch supplies no other names; pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete native source rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222484`: identity, rank, parent, code, empty synonyms, attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32028`: exact scientific-name object, empty unique-name field.
- `data/taxa/PATHS.tsv:14991`: ID and slug.
- `curation/seed_scope.tsv:322731`: date and one-source admission reason matching the seed event.

The attestation unit is `NAME`, not strain, assembly or experiment. Full exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema and seeder contract, `strain_count: 0` means zero represented BacDive records, not a denial that a named strain exists.

Two additional native catalog matches were read completely and excluded. `data/catalog/ncbi_genbank-0052.jsonl.gz:3124` is `GCA_056325265.1`, sample `SAMN55001201`, project `PRJNA1417612`; `data/catalog/ncbi_genbank-0066.jsonl.gz:6209` is `GCA_982294615.1`, sample `SAMEA121961347`, project `PRJEB109305`. Both classify Candidatus Marisimplicoccus sp. under taxid 3101254, with isolate S2022_10_D_bin.34. Their matching value is `genome_size: 1036482`, not the target taxon ID; their ungapped size is 1030382. These numeric collisions supply no strain, genome, sample or project link for KLBMP 03533. No equivalence between the two assemblies is inferred.

Exact non-expanded Nuccore query `txid1036482[Organism:noexp]` returned one record, UID 334303286. The complete [JF803762.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF803762.1) identifies this taxon and strain KLBMP 03533. It is a 707-base partial 16S rRNA sequence, with both ends marked partial, from rhizosphere associated with Pinus massoniana in China: Panzhihua. No culture-deposit qualifier or assembly cross-reference is supplied. Source and rRNA features were read fully; there is no CDS feature. Actual sequence length and submitted transcription agree, without ambiguous nucleotide symbols.

The sequence cites an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin, plus a direct submission dated 11-APR-2011, without a study PMID or DOI. The title does not demonstrate successful disease control by this strain. A partial ribosomal marker is not a genome, functional assay or basis for reassignment to a named species. No phenotype was inferred from the genus.

Spaced and compact strain-designation web searches returned broad NCBI taxonomy listings and a biofertilizer literature discovery hit. The complete primary taxonomy response, not those snippets, supports the identity assessment. Subsequent unrestricted queries for JF803762 and JF803762.1, and a genus plus complete strain-designation query excluding NCBI, returned no results. The optional literature access limits are detailed below. These bounded searches do not establish literature absence.

## Completeness

Complete enough for its supported taxonomy-seed scope. Optional nomenclature, synonyms, mappings, deposits, genomes and graphs appropriately remain empty without an explicit identity chain. The external strain designation and ribosomal sequence do not require inventing a BacDive entry or adding a genome link.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain-designation variants and JF803762 with optional version. Five rows matched: three target name/taxonomy/scope rows and the two excluded assembly metrics described above. All were read completely. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence statements are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. The PubMed query `"KLBMP 03533"[All Fields] OR "JF803762"[All Fields]` returned zero with quoted-phrase warnings. These are bounded query outcomes, not universal genome or literature absence. No strain-genome chain or strain-specific published functional study was verified.

iModulonDB was not run: the YAML asserts no gene, regulator or expression claim and no covered strain/dataset was identified. The external ribosomal marker does not establish such coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. Limited external characterization and inaccessible optional literature do not invalidate this NCBI-grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not infer strain equivalence from the KLBMP prefix, assign a formal species from the partial marker, or promote the unpublished study title into a biocontrol phenotype. Numeric catalog collisions and genus-level traits cannot supply strain-specific assertions.

Future taxonomy corrections belong first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional sequence or source-context enrichment requires maintained input and suitable model/seeder handling, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Before optional enrichment, inspect primary evidence explicitly linking this strain to a proposed deposit, genome or experiment, keeping sequence, sample, project and genome identifiers distinct. Any further literature work must verify the complete strain designation in accessible primary text rather than adopting a shared prefix from a search result.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036482`, inspect the emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

The optional discovery hit was [an OUCI listing](https://ouci.dntb.gov.ua/en/works/9ZPYAvZO/) for *Four Decades of Bacillus Biofertilizers: Advances and Future Prospects in Agriculture*. Its search snippet names a different strain, Bacillus flexus KLBMP 4941. A title search located [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11767708/) and [the publisher](https://www.mdpi.com/2076-2607/13/1/187). PMC returned a browser challenge and the publisher returned HTTP 429. Find operations against those responses do not establish absence. Full text was not inspected; the lead was excluded from the biological verdict, without claiming an exhaustive literature search or a verified full-text mismatch.

The single-record skill and checklist governed the review, with unchanged local ownership guidance and documented validators. Own source rows and accession were inspected independently. Before/after YAML SHA-256 was `985586385e33933d27adbee0dca7cf0d118fcc5f586532f5ceacf87b62c1ba16`.

Only this new timestamped report was written for the target. No record, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
