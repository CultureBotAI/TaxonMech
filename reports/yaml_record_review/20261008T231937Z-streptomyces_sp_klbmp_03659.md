# YAML Record Review: Streptomyces sp. KLBMP 03659

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03659.yaml`
- Started UTC: 2026-10-08T23:15:29Z
- Finished UTC: 2026-10-08T23:19:37Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036490`, Streptomyces sp. KLBMP 03659. Stored claims are species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero BacDive strain records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, strain/genome links and causal graphs are unasserted.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03659.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03659.yaml --out /private/tmp/klbmp03659-strict.tsv`: passed, one file and zero errors; the complete TSV was header-only.
- Structured comparisons checked the complete backbone row, all ten ancestors, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and complete type-material, merged-ID and dropped tables were scanned.
- Complete nucleotide XML parsing confirmed declared versus actual length, equality with the submitted rRNA transcription and absence of non-ACGT symbols. This checks annotation consistency, not independent alignment or species identification.
- The primary paper's complete relevant PDF pages were read, the target's figure was rendered and visually inspected, and bibliographic identifiers were verified through PubMed EFetch. The distinct experimental-strain accession was read completely.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. The embedded event was inspected; bounded searches found no separate target history artifact. Graph product validation is not applicable without graph nodes. No focused substitute for a corpus-wide gate was invented.

## Identity and Grounding

The complete [NCBI EFetch taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036490&retmode=xml) agrees with the ID, label, species rank, parent 2593676 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036490) confirms all ten root-first ancestor IDs. Ancestor labels and ranks match the pinned lineage through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

Species rank is the authority's rank for this unnamed strain-associated taxon, not evidence of a formally described species. Exact grounding denotes this precise NCBI identity, not equivalence with a named congener. Live EFetch supplies no other names; pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete native source rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222492`: identity, rank, parent, code, empty synonyms, attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32036`: exact scientific-name object, empty unique-name field.
- `data/taxa/PATHS.tsv:14999`: ID and slug.
- `curation/seed_scope.tsv:322739`: date and one-source admission reason matching the seed event.

The attestation unit is `NAME`, not strain, assembly or experiment. Full exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema and seeder contract, `strain_count: 0` means zero represented BacDive records, not a denial that a named strain exists.

Exact non-expanded Nuccore query `txid1036490[Organism:noexp]` returned one record, UID 334303272. The complete [JF803748.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF803748.1) identifies this taxon and strain KLBMP 03659. It is a 683-base partial 16S rRNA sequence, with both ends marked partial. Its own isolation-source qualifier is leaf, with host Pinus massoniana and location China: Panzhihua. No culture-deposit qualifier or assembly cross-reference is supplied. Source and rRNA features were read fully; there is no CDS feature. Actual sequence length and submitted transcription agree, without ambiguous nucleotide symbols.

The sequence cites an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin, plus a direct submission dated 11-APR-2011, without a study PMID or DOI. That title does not demonstrate successful disease control by this strain. A partial ribosomal marker is not a genome, functional assay or basis for reassignment to a named species. Leaf isolation is this source record's collection context and must not be generalized to other KLBMP records.

A genuine literature mention was inspected in [Almuhayawi et al. (2021), Plants 10:2745](https://mdpi-res.com/d_attachment/plants/plants-10-02745/article_deploy/plants-10-02745-v2.pdf): Figure 1 on page 6 labels JF803748.1 and KLBMP 03659 as a comparison sequence, separately from JSA11/MZ489115. Sections 2.2-2.4 and 3.1 identify Endo 2/JSA11 as the studied isolate. The figure therefore supports reference-sequence use, not transfer of its experimental phenotypes to KLBMP 03659. PubMed EFetch independently verified PMID 34961218, PMC8704246, DOI 10.3390/plants10122745 and the 13-DEC-2021 publication date.

The complete [MZ489115.1 record](https://www.ncbi.nlm.nih.gov/nuccore/MZ489115.1) confirms strain JSA11, a separate 1097-base partial 16S sequence filed under taxon 1931 (Streptomyces sp.), not taxon 1036490. Shared genus or placement near the target in a tree does not establish strain identity. No JSA11 phenotype, isolation protocol or genome link was transferred.

Two additional local candidates were read completely and excluded as numeric near matches:

- `data/catalog/ncbi_genbank-0012.jsonl.gz:28886` is GCA_013938005.1, Shigella flexneri taxid 623, strain PNUSAE019771, sample SAMN10364909, project PRJNA218110 and WGS master AAUXVH000000000.1.
- `data/catalog/allthebacteria.tsv.xz:1505321` names Shigella flexneri and the same sample, run SRR8144975 and analysis ERZ9093828. Its assembly pipeline is PASS, with HQ and sylph filters SYLPH_RESULTS_FAIL, current sylph species unknown and prior sylph species Escherichia coli. These source details were preserved, not reconciled or used as target evidence.

Both hits contain the search digits within SAMN10364909; this is not the target's taxon ID. No sample, analysis, assembly, run, FASTA URL or SeqKit sum from either row establishes a link to KLBMP 03659. Shared sample also does not by itself prove that those two assemblies are equivalent.

Spaced/compact strain-name searches and later accession/full-strain queries returned the primary paper, copies of it and NCBI taxonomy results. They were not empty searches. Publisher PDF content and primary NCBI responses, not discovery snippets or mirror authority, support the conclusions above.

## Completeness

Complete enough for its supported taxonomy-seed scope. Optional nomenclature, synonyms, mappings, deposits, genomes and graphs appropriately remain empty without an explicit identity chain. The external strain designation and ribosomal sequence do not require inventing a BacDive entry or adding a genome link. Optional reference-sequence literature context is not a missing required field or direct functional characterization of this taxon.

Expanded `rg --no-ignore --hidden -n -z -i` searches included ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain-designation variants, JF803748 with optional version and nucleotide UID 334303272. Initial and expanded searches each returned the same five rows: three own name/taxonomy/scope rows and two unrelated sample matches. All were read completely. Five source `SOURCE.json` files were separately parsed without a target identity match; history filenames were independently inventoried. Absence statements are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. The PubMed query `"KLBMP 03659"[All Fields] OR "JF803748"[All Fields]` returned zero with quoted-phrase warnings, despite the independently verified figure mention in PMID 34961218. This explicitly demonstrates why a bounded query miss cannot establish literature absence. No strain-genome chain was established.

iModulonDB was not run: the YAML asserts no gene, regulator or expression claim and no covered strain/dataset was identified. Neither the external ribosomal marker nor another strain's plant experiments establishes such coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored claims. The external reference-sequence use, distinct experimental strain and unrelated catalog hits do not invalidate this NCBI-grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not infer strain equivalence from a KLBMP prefix, numeric substring, related sequence or tree position. Do not assign a formal species from the partial marker, transfer isolation-source metadata, or promote either an unpublished screening title or another strain's experiments into a target phenotype.

Future taxonomy corrections belong first at NCBI, then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection defects belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional sequence/literature enrichment requires maintained input and suitable model/seeder handling, not direct generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Before optional enrichment, inspect primary evidence explicitly linking this strain to a proposed deposit, genome or experiment, keeping sequence, sample, project and genome identifiers distinct. Retain the narrow reference-sequence role of the literature mention.

After an authorized input/seeder correction, run its focused regression test, `just seed-canary NCBITaxon:1036490`, inspect the emitted YAML, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

The single-record skill and checklist governed the review, with unchanged local ownership guidance and documented validators. Before/after YAML SHA-256 was `f5b53ded443dd1ae032828ce1cbd834bc2f4462acd840aa23f1ec3e2fe8089b1`.

The publisher PDF has 25 pages. Complete pages 1, 5, 6, 17 and 18 were read; exact target text was searched across all 25 pages and occurred on page 6. Page 6 was rendered locally and visually inspected. The figure caption describes neighbor joining and approximately 950-base sequences, while methods describe maximum likelihood and 683 final positions. These statements were not silently reconciled, nor was an exact target similarity calculated. This external methods ambiguity is not a stored YAML claim.

PubMed and PMC HTML opens encountered browser challenges. The accessible publisher PDF and PubMed EFetch resolved the relevant evidence; the failed HTML access was not treated as an absence result. The web screenshot call returned no usable image to this session, so local PDF rendering supplied the visual check. Only relevant paper pages were read in full, not an exhaustive audit of all experiments or supplements.

Only this new timestamped report was written in the repository for the target. Temporary PDF/render files remained outside the repository. No record, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
