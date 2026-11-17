# YAML Record Review: Pseudomonas sp. HAT5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_hat5.yaml`
- Started UTC: 2026-10-07T08:13:57Z
- Finished UTC: 2026-10-07T08:18:04Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035622`, Pseudomonas sp. HAT5, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`, ten root-first ancestors and genetic code 11. It carries `EXACT` grounding, `SEEDED` mapping status, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, culture deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graphs are asserted. HAT5 is an isolate designation, not a verified culture accession. Generated YAML is read-only. Maintained source/extraction inputs and `src/taxonmech/seed.py` own future fixes, with scope and slug ownership in `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudomonas_sp_hat5.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_hat5.yaml --out /private/tmp/hat5-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/hat5-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, complete lineage, seven source inventories, path, scope and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and complete ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not prove byte-for-byte corpus reproduction.

`just validate-products` was not run: configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded. There are no literature/internal evidence references in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content/path searches found no target history artifact; none is created here.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222150` agrees on ID, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31630` agrees. Unique path and scope rows are `data/taxa/PATHS.tsv:14650` and `curation/seed_scope.tsv:322417`.

All ten ancestors match the committed parent chain in identifier, label, rank and order. Live EFetch confirms species rank, parent 196821, code 11, no alternate names and nine non-root ancestors; Datasets confirms the same chain including root. Gammaproteobacteria/Pseudomonadales/Pseudomonadaceae/Pseudomonas and the unclassified Pseudomonas parent agree. No retirement or replacement was found in the inspected lifecycle sources. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035622&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035622)

`EXACT` grounds this NCBI concept, not a validly published species binomial, strain-deposit equivalence or a new identification inferred from a marker.

## Evidence

The sole `NCBITAXON` attestation agrees on exact ID and label, count 1, unit `NAME` and snapshot note. It is not a count of strains or genomes. The complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore UID 333952305 resolves to `JF799932.1`, a 1,428-nt partial 16S rRNA marker. Complete GenBank metadata explicitly identifies Pseudomonas sp. HAT5, strain HAT5 and `taxon:1035622`. Its source is the active layer in permafrost, with a China/Qinghai-Tibet locality. The rRNA feature is partial at both ends. No culture-collection, BioSample, BioProject or assembly link is supplied. The metadata were read completely, excluding only sequence strings and translation/transcription payloads. [GenBank JF799932.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799932.1)

The marker cites an unpublished study of bacterial diversity in active-layer permafrost along the Qinghai-Tibet highway and a direct submission by Li, Xu and Zhang. Submission was 11 April 2011; creation/update were 30 May 2011. No DOI or PMID is linked in the nucleotide record. This is submission provenance, not independent published species confirmation. Locality and genus do not establish cold-growth or other phenotypes. The marker is not a genome.

Thirty-four additional catalog hits were read completely and excluded as identifier-substring collisions. The groups below account for every row:

- Five IOP_13 rows: `data/bvbrc/bvbrc-0000.jsonl.gz:30045` and line 30046; `data/catalog/ncbi_genbank-0019.jsonl.gz:18332`; `data/catalog/ncbi_refseq-0003.jsonl.gz:47579`; `data/catalog/gtdb_genomes-0000.jsonl.gz:7636`. These concern Stutzerimonas kunmingensis, taxid 1211807, sample SAMN21035622, GCA/GCF_021021335.1 and BV-BRC 1211807.16/1211807.17. BV-BRC retains the older Pseudomonas kunmingensis label and marks 1211807.17 Deprecated. Neither that old genus name nor sample digits identify HAT5.
- Two GOLD project rows: `data/gold/projects.jsonl.gz:267474` and line 267768, Salmonella enterica PNUSAS059646 and PNUSAS058007, projects Gp0379895/Gp0380189, organisms Go0495841/Go0496135, samples SAMN10356226/SAMN10356229. The numbers occur within sample accessions.
- Six BV-BRC Salmonella rows: `data/bvbrc/bvbrc-0017.jsonl.gz`, lines 10705, 10710, 10808, 11179, 11183 and 11204. Genomes 28901.5244, 28901.5249, 28901.5347, 28901.5719, 28901.5723 and 28901.5744 have taxid 28901, not 1035622.
- Eight NCBI Salmonella assembly rows: `data/catalog/ncbi_genbank-0002.jsonl.gz`, lines 48178, 48185, 48329, 48911, 48919 and 48944, plus `data/catalog/ncbi_genbank-0014.jsonl.gz`, lines 40899 and 40901. These are GCA_003757045.1, GCA_003757185.1, GCA_003760065.1, GCA_003771845.1, GCA_003772005.1, GCA_003772505.1, GCA_016289455.1 and GCA_016289495.1. All have taxid/species_taxid 28901; samples SAMN10356222 through SAMN10356229 explain the matches.
- One Campylobacter row: `data/catalog/ncbi_genbank-0009.jsonl.gz:6642`, GCA_010356225.1, Campylobacter jejuni PNUSAC014607, taxid/species_taxid 197. The digits occur within the assembly accession.
- Two E. coli rows: `data/catalog/ncbi_refseq-0009.jsonl.gz:2084` and `data/catalog/ncbi_genbank-0054.jsonl.gz:28399`, GCF/GCA_058934445.1, isolate A9-2, taxid/species_taxid 562. BioSample SAMN61035622 explains the matches.
- Ten ATB rows in `data/catalog/allthebacteria.tsv.xz`: line 66267 is Staphylococcus aureus, SAMEA1035622, ERZ3070806, ERR083787, with META_FAIL assembly/HQ filters; lines 1503859 through 1503866 are eight Salmonella enterica samples SAMN10356222 through SAMN10356229; line 3092484 is Salmonella enterica subsp. enterica serovar Infantis, SAMN44339250, ERZ27111884, with matching digits in run SRR31035622.

Source-declared GCA/GCF pairing and shared sample relationships among these unrelated rows remain confined to their own organisms. No HAT5 culture-deposit/genome chain is supplied.

A primary paper does use the HAT5 marker as a comparison sequence. Urtubia et al., DOI 10.3856/vol42-issue1-fulltext-7, Table 4 and its continuation, distinguishes experimental isolate BACT-18 (`JQ861996`) from related reference sequence `JF799932`. The reported comparison is 353/359 identities (98%) with 3/359 gaps. BACT-18's larval origin, R2A culture and morphology are not HAT5 observations. This supports a bounded citation to the reference marker, not strain equivalence, a HAT5 host association, pathogenicity or a genome link. Primary HTML methods, publisher metadata and the relevant PDF table text were inspected. [Primary article](https://www.lajar.cl/index.php/rlajar/article/view/vol42-issue1-fulltext-7), [SciELO full text](https://www.scielo.cl/scielo.php?lng=en&nrm=iso&pid=S0718-560X2014000100007&script=sci_arttext)

No gene, regulator, pathway, stress-response or transcriptomics assertion in this YAML requires an iModulonDB lookup. The adapter is not applicable; its absence is not negative biological evidence.

## Completeness

Zero BacDive strains and the optional omissions agree with inspected source scope. A marker's strain qualifier is not a culture deposit. Record-level literature evidence is optional for seeded records. The comparison citation does not create a required missing claim. No required gap was found.

Both local search stages included ignored/hidden files and compressed catalogs with `rg --no-ignore --hidden -n -z -i`. Roots were `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full per stage; history filenames were independently traversed.

The identity stage searched taxid 1035622, exact label, slug and HAT5 with case/separator variants. Thirty-seven lines matched: backbone, scope, native name and the 34 incidental catalog hits; all were read completely. The accession stage searched JF799932 with optional .1 and found no lines. Neither stage found matching source-metadata values or history paths. These negative findings include ignored files and are bounded to the specified roots and terms.

Web searches used Pseudomonas with HAT5 and JF799932. An institutional thesis lead could not be inspected: the web fetch failed and direct download returned HTTP 403. Its search snippet remains a lead, not evidence. A separate agricultural-paper PDF lead also failed to fetch and is not used for identity or phenotype conclusions. [Uninspected thesis landing page](https://www.colibri.udelar.edu.uy/jspui/handle/20.500.12008/3921)

No supported culture-deposit/genome chain was established. The exact-taxid Assembly zero carries a phrase-not-found warning and does not exclude assemblies filed under another identity. Exhaustive literature retrieval and sequence similarity were not performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, complete lineage, source provenance, zero strain count and seed history agree. Catalog substrings and a partial-marker comparison do not justify new strain/genome or phenotype links. The inaccessible literature leads remain bounded follow-up uncertainty, not demonstrated record defects.

## Recommended Edits

None required. Do not patch generated YAML, match taxids to substrings of sample/run/assembly identifiers, conflate HAT5 with BACT-18, count JF799932.1 as a genome, or promote `SEEDED` to `REVIEWED`.

A later authorized taxonomy-source refresh belongs in `conf/ncbi_taxdump.yaml` and `scripts/extract_source_inventory.py`, followed by guarded seeding. Optional literature annotations require maintained-input support merged by `src/taxonmech/seed.py` with tests under `docs/CURATION.md`. Habitat and phenotype assertions belong in the corresponding sibling corpora with claim-specific evidence.

## Follow-up Checks

- Revisit the thesis and agricultural-paper leads when primary text is accessible; preserve the distinction between the target, a sequence comparator and a similarly named isolate.
- Require an exact culture-deposit and genome-source chain before adding strain/genome identifiers. Keep marker comparisons separate from identity assertions.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`; validate any new history artifact. Full-corpus gates remain skipped here.

## Additional Notes

Primary NCBI taxonomy, Datasets, sequence-index and nucleotide reads succeeded. The aquatic-research paper was available through the publisher and SciELO. PDF screenshot calls returned references but no inspectable image payload; table interpretation above rests on the complete relevant extracted table text and column headings, not a claimed visual verification.

Seed wording agrees with scope and attestation. Timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date. All three timestamps and the selection code were inspected.

The entire target was reread unchanged before report creation. An ignored-independent filename search found no previous report for this stem. Only this new repository report is added for this review; no record, inventory, page, old report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
