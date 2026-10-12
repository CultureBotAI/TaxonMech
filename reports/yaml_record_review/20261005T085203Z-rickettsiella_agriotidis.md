# YAML Record Review: Rickettsiella agriotidis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rickettsiella_agriotidis.yaml`
- Started UTC: 2026-10-05T08:48:41Z
- Finished UTC: 2026-10-05T08:52:03Z
- Verdict: pass

## Target

The complete 58-line `TaxonRecord` was read before judgment. It denotes `NCBITaxon:1034385`, Rickettsiella agriotidis, rank `SPECIES`, domain `BACTERIA`, with `grounding_status: EXACT` and `mapping_status: SEEDED`. This is a generated NCBI-backed record, not a manually maintained organism description. Future changes belong to the responsible source capture/transform, `src/taxonmech/extract.py`, `src/taxonmech/seed.py`, or `curation/seed_scope.tsv`, not direct edits to the YAML.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/rickettsiella_agriotidis.yaml`: exit 0, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/rickettsiella_agriotidis.yaml --out /private/tmp/agriotidis-strict-20261005.tsv`: exit 0; one file scanned, zero error rows.
- Read-only full-table comparisons checked identity, complete lineage, synonyms, direct inventory rows, attestation, PATHS/scope uniqueness, and the inline seed event. Full backbone/status scans found no children, no target type-material row, no merged-ID row involving the target, and no dropped row.
- `just verify-corpus`: not run because it is a full-corpus reproduction gate, not a single-record validator. Its `--max-diffs` option caps diagnostics, not scope. The comparisons above are not a substitute for full reproduction.
- `validate-products`: not applicable; no curator-added causal graph. `validate-history`: not run; ignored-inclusive filename and content searches found no target history artifact. The inline event was checked separately. No undocumented focused term/reference validator was invented.

## Identity and Grounding

The pinned backbone row at `data/raw/ncbitaxon_taxa.tsv:221583`, live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034385&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034385), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034385&mode=Info) agree on the identity, species rank, parent Rickettsiella (`NCBITaxon:59195`), and bacterial placement. EFetch/browser confirm genetic code 11.

Every root-first ancestor matches the pinned backbone: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Legionellales, Coxiellaceae, Rickettsiella. Datasets provides the same ancestor IDs. The Leclerque et al. 2011 authority and host-associated name Rickettsiella symbiont of Agriotes sp. are correctly related synonyms. Complete native objects at `data/catalog/ncbi_names-0005.jsonl.gz:30959` through line 30961 classify them as `authority` and `includes`, respectively; EFetch confirms this. Neither is incorrectly promoted to an exact synonym.

[LPSN record 2496](https://lpsn.dsmz.de/species/rickettsiella-agriotidis) identifies an effectively used but not validly published name, preferred rather than correct, with nomenclatural type JKI_E1959/09D and marker HQ640943. The NCBI browser independently notes the lack of valid publication. These qualifications are compatible with exact grounding to the NCBI concept; the YAML does not assert valid publication or resolve the literature's species-boundary question.

## Evidence

- The sole `NCBITAXON` attestation matches the source row in ID, label, one `NAME`, and 2026-09-13 snapshot. Its count refers to the source concept, not independent strains, experiments, or genomes.
- Complete direct inventory scans found no target row in BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin, or BactoTraits. An additional whole-table LPSN scan found neither `lpsn:2496` nor agriotidis. No already imported mapped nomenclature row was therefore omitted by the seeder. The live LPSN entry is a bounded enrichment lead.
- The [2011 original study](https://link.springer.com/article/10.1007/s00284-011-9958-5) and PubMed XML for [PMID 21638041](https://pubmed.ncbi.nlm.nih.gov/21638041/) agree on DOI `10.1007/s00284-011-9958-5`, authors, and Current Microbiology 63(2):158-163. The abstract places the studied organism in Rickettsiella using microscopy and 16S/ftsY evidence, proposes the agriotidis pathotype, and suggests a likely relationship to R. popilliae under the classification then accepted. PubMed's accession list explicitly names HQ640942 and HQ640943. No phenotype or host-range claim is generalized beyond that study.
- The [MLSA follow-up](https://link.springer.com/article/10.1007/s00284-012-0219-z) and PubMed XML for [PMID 23007524](https://pubmed.ncbi.nlm.nih.gov/23007524/) verify DOI `10.1007/s00284-012-0219-z`, Schuster and colleagues, Current Microbiology 66(1):1-9 (2013), first published online in September 2012. Its abstract supports proximity to the melolonthae/tipulae pathotype complex and argues against assignment to R. grylli. Crucially, the proposed R. popilliae assignment was not directly corroborated because type-strain genetic data were unavailable to that study. This historical limitation is not a claim about current data availability and does not establish present-day exact synonymy or genome equivalence. Both papers were reviewed at abstract/bibliographic level, not full text.
- The exact NCBI Assembly query `txid1034385[Organism:noexp]` returned zero items with a phrases-not-found warning. This is a bounded query result, not proof that no genome exists. The corresponding Nuccore query returned seven IDs; all seven records' metadata, source qualifiers, references, and feature annotations were inspected, with bases and translations omitted.
- The original-study pair retains strain spelling JKI_E1959/09D: [HQ640943.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ640943.1), 1,357 bp partial 16S, and [HQ640942.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ640942.1), 996 bp complete ftsY CDS. Both name taxon 1034385, host Agriotes sp., and PMID 21638041. LPSN's designation and 16S accession match these records.
- Five other marker records retain the different spelling JKI E1959/09-D, again with taxon 1034385 and host Agriotes sp.: [JN565687.1](https://www.ncbi.nlm.nih.gov/nuccore/JN565687.1), 787 bp partial gidA; [JN565688.1](https://www.ncbi.nlm.nih.gov/nuccore/JN565688.1), 891 bp partial sucB; [JN695773.1](https://www.ncbi.nlm.nih.gov/nuccore/JN695773.1), 894 bp partial rpsA; [JF519845.1](https://www.ncbi.nlm.nih.gov/nuccore/JF519845.1), 931 bp partial 23S; and [JF708245.1](https://www.ncbi.nlm.nih.gov/nuccore/JF708245.1), 256 bp partial 23S with an intervening sequence. The three protein-marker records cite the MLSA paper as online/in press in 2012, consistent with its 2013 issue date. The 23S records retain an unpublished reference and direct submission. Their source spellings/references are not silently rewritten into one assertion. None of these seven markers is an assembly, including the complete ftsY CDS.
- The complete SeqCode object at `data/seqcode/names.jsonl.gz:34916` supplies ID 36803, matching name, and resource/API URLs only. It establishes a native name-catalog lead, not an explicit NCBI mapping, valid-publication status, or type-genome association.

## Completeness

The zero BacDive strain count matches the complete direct inventory; the target has no descendant taxa from which additional strains could be gathered. Source strain designations and marker sequences do not justify inventing a BacDive entry or an eligible culture-deposit join. No supported strain-genome link missing from this record was identified.

Gitignore-independent, compressed-aware searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. They covered ID, scientific name, host-associated name, stem, LPSN ID, both strain-designation forms, and all seven marker accessions. The primary search returned six contexts; the taxon/type-marker search seven. Neither supplied a target-specific LPSN inventory row, GTDB mapping/genome, BacDive strain, GOLD/BV-BRC genome chain, StrainInfo deposit, ATB sample chain, or history artifact.

A broad E1959 substring search returned 134 contexts. Structured inspection of all match fields classified them as unrelated BacDive DOI substrings, PNUSAE isolate prefixes, other strain/isolate names, or ATB SeqKit-sum substrings. A subsequent bounded search for the complete E1959...09D designation pattern and exact marker accessions returned zero matches across the same ignored-inclusive roots. BioSample SAMEA1034385 in the numeric-ID search belongs to Streptococcus equi subsp. zooepidemicus; sharing taxonomy-ID digits does not make it a target sample.

Optional evidence, phenotype, definition, and causal-graph slots need not be filled. The live LPSN name absent from the pinned inventory is a source-enrichment opportunity, not evidence that this YAML dropped a supplied mapping. This review does not claim exhaustive external literature or genome discovery.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record. The NCBI concept, synonym scope, lineage, source count, strain count, and seed history are supported. Nomenclatural qualifications, historical taxonomic uncertainty, and source strain spellings are preserved in this report. A pass verdict is not human sign-off or promotion to `REVIEWED`.

## Recommended Edits

None required for the current generated record. Optional nomenclature enrichment belongs upstream in the kg-microbe LPSN/LPSN-API capture and mapping for name 2496. The local importer is `src/taxonmech/extract.py:420`, feeding derived `data/raw/lpsn_names.tsv`; `src/taxonmech/seed.py:386` emits mapped nomenclature. Establish an explicit source mapping, preserve non-valid/preferred status, and retain the source designation and marker accession. The missing original transformed inputs prevent diagnosing why the name is absent from the inventory.

Do not merge this NCBI record with R. popilliae, turn the host-associated name into an exact synonym, normalize strain punctuation as a genome-join rule, or count gene records as assemblies.

## Follow-up Checks

For a separately authorized refresh, inspect the native LPSN name/status and mapping, compare the resulting inventory row, verify status parsing and marker provenance, and rerun both focused validators. Use `just verify-corpus` after authorized regeneration to prove full reproduction. Any later genome association needs explicit source/deposit/sample provenance rather than inferred taxonomy or punctuation equivalence. No additional action is necessary to accept this bounded review.

## Additional Notes

- `data/taxa/PATHS.tsv:14047` uniquely maps the target to this stem. `curation/seed_scope.tsv:321895` supplies the 2026-09-13 one-source scope reason. The 2026-09-13T17:54:04Z inline seed event correctly names NCBITAXON and that reason.
- Ignored-inclusive filename searches found no prior target report or history path; history content was searched too. The previous two Rickettsiella reviews did not substitute for this record's source checks.
- The previously read review skill, CLAUDE guidance, curation skill/checklist, justfile, curation/harmonization/schema/history documentation, and schema had no current tracked changes.
- The initial NCBI browser URL failed; its Info view later resolved and was inspected. EFetch/Datasets and both publisher abstracts resolved. Full paper bodies remained subscription content and were not purchased or claimed as read.
- An ignored-inclusive filename search throughout the configured kg-microbe checkout found no `nodes.tsv` or `edges.tsv`; original transformed LPSN inputs were unavailable there. Committed inventories were read without claiming a fresh extraction.
- iModulonDB is not applicable: the YAML makes no gene, regulator, pathway, stress-response, or transcriptomic assertion. Marker annotations were examined only to verify identity and the gene/genome boundary.
- Tracked and staged diffs were empty before report creation. No taxon YAML, source data, code, page, lifecycle status, curation event, prior report, or history entry was edited. No paid research, external contact, or GitHub mutation was performed.

