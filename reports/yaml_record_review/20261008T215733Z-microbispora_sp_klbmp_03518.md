# YAML Record Review: Microbispora sp. KLBMP 03518

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microbispora_sp_klbmp_03518.yaml`
- Started UTC: 2026-10-08T21:54:47Z
- Finished UTC: 2026-10-08T21:57:33Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036474`, Microbispora sp. KLBMP 03518. Stored claims are species rank, Bacteria domain, parent `NCBITaxon:2614687`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero BacDive strain records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, strain/genome links and causal graphs are unasserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/microbispora_sp_klbmp_03518.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/microbispora_sp_klbmp_03518.yaml --out /private/tmp/klbmp03518-strict.tsv`: passed, one file and zero errors. Complete diagnostic TSV was header-only.
- Structured comparisons checked the complete backbone row, all ten ancestors, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and complete type-material, merged-ID and dropped tables were scanned.
- Complete nucleotide XML parsing confirmed declared versus actual sequence length, equality with its submitted rRNA transcription annotation and absence of non-ACGT symbols. This is annotation consistency, not independent alignment or species identification.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. The embedded event was inspected; bounded searches found no separate target history artifact. Graph product validation is not applicable without graph nodes. No focused replacement was invented for a corpus-wide gate.

## Identity and Grounding

The complete [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036474&retmode=xml) agrees with the ID, label, species rank, parent 2614687 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036474) confirms all ten root-first ancestor IDs. Ancestor labels and ranks match the pinned lineage through Bacillati, Actinomycetota, Actinomycetes, Streptosporangiales, Streptosporangiaceae, Microbispora and unclassified Microbispora. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

Species rank is the authority's rank for this unnamed strain-associated taxon, not evidence of a formally described species. Exact grounding means this precise NCBI identity, not equivalence with a named congener. Live EFetch supplies no other names; pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

An inspected [TogoGenome lineage table](https://togogenome.org/stanza/lineage_information?tax_id=2614687) pairs this label with 1036474, but labels ancestor 1783272 as Terrabacteria group rather than Bacillati. That external display difference is retained here; the record agrees with both pinned and current primary NCBI data. It is not a reason to replace the carried lineage or infer a reconciled classification.

## Evidence

Complete native source rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222476`: identity, rank, parent, code, empty synonyms, attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32020`: exact scientific-name object, empty unique-name field.
- `data/taxa/PATHS.tsv:14983`: ID and slug.
- `curation/seed_scope.tsv:322723`: date and one-source admission reason matching the seed event.

The attestation unit is `NAME`, not strain, assembly or experiment. Full exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema and seeder contract, `strain_count: 0` means zero represented BacDive records, not a denial that a named strain exists.

Exact non-expanded Nuccore query `txid1036474[Organism:noexp]` returned one record, UID 334303283. The complete [JF803759.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF803759.1) identifies this taxon and strain KLBMP 03518. It is a 681-base partial 16S rRNA sequence, with both ends marked partial, from rhizosphere associated with Pinus massoniana in China: Panzhihua. No culture-deposit qualifier or assembly cross-reference is supplied. Source and rRNA features were read fully; there is no CDS feature. Actual sequence length and submitted transcription agree, without ambiguous nucleotide symbols.

The sequence cites an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin, plus a direct submission dated 11-APR-2011, without a study PMID or DOI. The title does not demonstrate successful disease control by this strain. A partial ribosomal marker is not a genome, functional assay or basis for reassignment to a named species.

Spaced/compact strain-label web searches surfaced NCBI taxonomy listings and taxonomy summaries, including the inspected TogoGenome table. Unrestricted JF803759 and JF803759.1 searches returned no results, as did a genus/strain-number query excluding NCBI, Genome.jp and TogoGenome. Those bounded searches do not establish literature absence; no independent phenotype or culture-deposit claim was adopted.

## Completeness

Complete enough for its supported taxonomy-seed scope. Optional nomenclature, synonyms, mappings, deposits, genomes and graphs appropriately remain empty without an explicit identity chain. The external strain designation and ribosomal sequence do not require inventing a BacDive entry or adding a genome link.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain-designation variants and JF803759 with optional version. Only the three name/taxonomy/scope rows matched, and all were read completely. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence statements are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. The PubMed query `"KLBMP 03518"[All Fields] OR "JF803759"[All Fields]` returned zero with quoted-phrase warnings. These are bounded query outcomes, not universal genome or literature absence. No strain-genome chain was established.

iModulonDB was not run: the YAML asserts no gene, regulator or expression claim and no covered strain/dataset was identified. The external ribosomal marker does not establish such coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. Limited external characterization and the secondary lineage-label difference do not invalidate this NCBI-grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not infer strain equivalence from the KLBMP prefix, assign a formal species from the partial marker, or promote the unpublished study title into a biocontrol phenotype.

Future taxonomy corrections belong first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional sequence or source-context enrichment requires maintained input and suitable model/seeder handling, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Before optional enrichment, inspect primary evidence explicitly linking this strain to a proposed deposit, genome or experiment, keeping sequence, sample, project and genome identifiers distinct.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036474`, inspect the emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

The single-record skill and checklist governed the review, with unchanged local ownership guidance and documented validators. Own source rows and accession were inspected independently. Before/after YAML SHA-256 was `a7253b86e6ef2214a8475261d2806cdf852a071379bf67d32e9ad1574ae9254c`.

Only this new timestamped report was written for the target. No record, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
