# YAML Record Review: Wolbachia endosymbiont of Epipyropidae sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_epipyropidae_sp.yaml`
- Started UTC: 2026-10-09T08:46:35Z
- Finished UTC: 2026-10-09T08:57:58Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036667`, Wolbachia endosymbiont of Epipyropidae sp. It asserts species rank, Bacteria, parent 2640676, eleven root-first ancestors, code 11, `EXACT` grounding, `SEEDED` mapping status, zero represented BacDive strains and one NCBITAXON name attestation. The seed event is dated 2026-09-13T17:54:04Z.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` uniquely resolved this YAML and found no prior target report. Synonyms, nomenclature, mappings, deposits, genomes, phenotypes, discussion and graphs are unasserted. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_epipyropidae_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_epipyropidae_sp.yaml --out /private/tmp/taxonmech-wolbachia-epipy-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched own identity, every ancestor, PATHS, scope reason, attestation and seed wording. Exact scans covered seven supplemental raw inventories, type material, merged IDs and dropped taxa.
- Length/alphabet checks passed for seven contextual JF902205-JF902211 markers. JF902205.1 has two N bases at positions 628 and 629; the other six have only ACGT. This is not CDS translation verification, alignment or an identity test for the reviewed taxon. The two JN markers received complete XML reads, not this separate consistency check.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Focused comparisons do not prove corpus reproduction. Embedded history was read; ignored-inclusive content and filename searches found no separate target history artifact within the stated roots. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036667&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036667) responses agree with the label, species rank and lineage. EFetch confirms parent 2640676 and code 11; Datasets includes root. Ancestors are root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Rickettsiales, Anaplasmataceae, Wolbachieae, Wolbachia and unclassified Wolbachia.

Live taxonomy supplies no other names. Pinned synonym fields are empty, and no own type-material, merged-ID or dropped-taxon row, or backbone child, was found. Species rank is an NCBI classification, not evidence of formal nomenclatural standing. The label is source-supported; a broad host-family label does not make more specifically named Wolbachia records its descendants or aliases.

Complete live EFetch and Datasets responses for 1084950 and 1085674 establish separate sibling taxa under 2640676: Wolbachia endosymbiont of epipaJanzen01 Janzen01 and Wolbachia endosymbiont of epipaBioLep01 BioLep01. Their corresponding Wolbachia sp. names are synonyms of those siblings, not of 1036667. No inspected authority explicitly merges these identities.

## Evidence

Complete own rows inspected: `data/raw/ncbitaxon_taxa.tsv:222570`, `data/catalog/ncbi_names-0005.jsonl.gz:32114`, `data/taxa/PATHS.tsv:15087` and `curation/seed_scope.tsv:322817`. Snapshot 2026-09-13, one-name unit and admission reason support the attestation and seed event. Exact target scans found no row in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits raw inventories. A name count is not a genome or experiment count.

The host-family Nuccore search returned seven records. All seven ESummary objects and complete GenBank XML records, including references, source qualifiers, gene/CDS features and sequences, were read. They are partial bacterial COI markers, not assemblies:

| Accession | UID | Taxon | Bases | Specimen voucher suffix | BOLD process |
| --- | --- | --- | --- | --- | --- |
| [JF902205.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902205.1) | 334360767 | 1085674 | 657 | BLPBE410-07.w | ASLEP002-10 |
| [JF902206.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902206.1) | 334360769 | 1085674 | 657 | BLPBE412-07.w | ASLEP003-10 |
| [JF902207.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902207.1) | 334360771 | 1085674 | 657 | BLPCF769-08.w | ASLEP004-10 |
| [JF902208.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902208.1) | 334360773 | 1085674 | 657 | BLPCJ868-08.w | ASLEP005-10 |
| [JF902209.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902209.1) | 334360775 | 1084950 | 624 | MHMXI846-07.w | ASLEP067-10 |
| [JF902210.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902210.1) | 334360777 | 1084950 | 657 | MHMYD740-09.w | ASLEP091-10 |
| [JF902211.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902211.1) | 334360779 | 1084950 | 657 | MHMYD741-09.w | ASLEP092-10 |

All seven source annotations name host Epipyropidae sp. and Costa Rica, with BIOUG<CAN> specimen-voucher prefixes and COI-5P BOLD cross-references. They use code 11 and codon start 1, with both CDS ends partial. All have creation/update date 30-APR-2012, an unpublished Smith and colleagues barcoding reference, and direct submission dated 01-MAY-2011 from the University of Guelph. JF902209 supplies less collection metadata than the other six. These vouchers identify sampled specimens, not cultured bacterial deposits; none is assigned to the reviewed taxon.

The primary [Smith et al. 2012 PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514), DOI 10.1371/journal.pone.0036514, PMID 22567162 and PMCID PMC3342236, concerns Wolbachia in insect barcoding. Its PubMed abstract and bibliographic identifiers, and selected primary HTML sections including Methods and supporting-table descriptions, were inspected. Methods explain the host-extract identifier plus .w convention. The paper supports study context, not exact equivalence between the reviewed taxon and the two sibling taxa. The entire paper and figure images were not inspected.

All cells across the four sheets of [Table S2](https://journals.plos.org/plosone/article/file?id=10.1371%2Fjournal.pone.0036514.s003&type=supplementary) were searched for the target/context identifiers; headers and nine matching rows were read in full, preserving duplicate column names. In sheet Wolbachia CO1, rows 163-166, 226 and 250-251 map the seven accessions to their specimen identifiers. Rows 483 and 510 supply two further specimens whose accessions were pending at publication. Other nonmatching rows were not individually adjudicated. No matching rows occurred in the new insect CO1, new wsp or existing wsp sheets.

Follow-up voucher searches resolved the two pending rows to current records, both read as complete XML. [JN674121.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674121.1), UID 350996231, is 658 bases, taxon 1085674, specimen BLPDT1439-10.w and BOLD ASWLP009-11.COI-5P, collected 12-Jun-2010 at Manta Mona, Costa Rica. [JN674122.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674122.1), UID 350996233, is 658 bases, taxon 1084950, specimen MHMYD374-09.w and BOLD ASWLP036-11.COI-5P, collected 03-Nov-2008 at Manguera, Costa Rica. Matching vouchers and process identifiers support these supplement-to-accession links. Both annotate code 11, codon start 2, partial CDS ends and host specimen names rather than a host family; neither is an own-taxon genome.

Preserved source conflicts: all nine matching supplement rows have Pyralidae in Extra Info, whereas the seven JF source records say Epipyropidae sp. Their bacterial Family column retains historical Rickettsiaceae rather than current Anaplasmataceae. The workbook also labels itself Table S1 although the publisher calls this attachment Table S2. These discrepancies remain source-context cautions. They do not independently establish that the reviewed NCBI label or current lineage is wrong, and they must not be silently resolved during future enrichment.

## Completeness

Complete enough for supported taxonomy-seed claims. Zero represented BacDive strains does not assert biological absence. No inspected source establishes a deposit, genome or explicit identity link connecting the nine contextual markers to 1036667. The separate sibling accessions are not required missing claims for this seed.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms began with word-bounded 1036667, the exact slug and Epipyropidae. Expansions added all nine accessions with optional .1, their nine UIDs, sibling taxon IDs, epipaJanzen01 and epipaBioLep01, and all nine voucher and BOLD process codes listed above. The final ignored-inclusive search returned eleven rows, all previously read in full native form: six TSV and five JSON rows. No additional row appeared when JN674121/JN674122 and their UIDs were added.

Besides the three own rows, contextual addresses were `data/raw/ncbitaxon_taxa.tsv:233138` and `:233291`, `curation/seed_scope.tsv:331684` and `:331809`, and `data/catalog/ncbi_names-0005.jsonl.gz:44953`, `:44954`, `:45154` and `:45155`. These represent the two sibling taxa and their names. Five SOURCE.json files were separately parsed in full for the expanded terms, with no matching keys or values; history filenames were independently inventoried. Search completeness is limited to the stated local roots and terms.

Exact Nuccore and Assembly queries `txid1036667[Organism:exp]` each returned zero with missing-phrase/no-items diagnostics. This is not proof of global sequence or genome absence. `Wolbachia[Organism] AND Epipyropidae[All Fields]` returned seven, with the host-family term expanded to Organism OR All Fields while retaining the Wolbachia intersection. The two additional voucher hits arose from a four-term OR query: BLPDT1439-10 and MHMYD374-09 were effective; the ASWLP009-11 and ASWLP036-11 terms were rejected as quoted phrases not found.

PubMed Wolbachia AND Epipyropidae returned zero after genus MeSH/all-fields expansion, without rejecting the family term. Exact ID/name and submission-title web searches supplied leads to the inspected primary paper. Neither the PubMed miss nor the selected HTML reading is an exhaustive full-text literature census. Search snippets were not used as independent evidence.

iModulonDB was not run: no gene, regulator or expression claim is asserted, and no applicable target strain/dataset was established. Optional empty fields are not automatic defects.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, source attestation and admission agree with pinned and live authorities. The unresolved host-family discrepancy concerns contextual sibling-marker sources, not a demonstrated contradiction in this record's assertions.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; admission changes belong in `curation/seed_scope.tsv`. Do not merge the three Wolbachia identities or transfer sibling marker evidence based only on host-family wording.

## Follow-up Checks

Optional enrichment requires an explicit source chain from 1036667 to a specimen/accession and resolution of the Pyralidae/Epipyropidae discrepancy through primary specimen/BOLD/submission provenance. Keep historical bacterial family names separate from current taxonomic placement. No independent sequence alignment, CDS translation verification, genome comparison or experimental reanalysis was performed.

After an authorized maintained-input change, run focused tests, `just seed-canary NCBITaxon:1036667`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

Independent review followed the local skill/checklist; no neighboring verdict was inherited. Entire YAML, own source rows, all eleven local candidate rows, own and sibling live taxonomy, and nine contextual marker XML records were inspected. The supplement search covered all cell values, not independent assessment of every specimen in the study.

The browser supplement download failed at a signed redirect; a direct public download succeeded. A temporary `uv run --no-project --with xlrd` environment read the old-format XLS without repository dependency changes. Workbook SHA-256: `8df12e221a835a4504e4ce0a30e5aed17a4e906c9bc2e1bffcd4113adf0f0a1e`. Temporary downloads and validator outputs are working files, not published corpus products.

Before/after YAML SHA-256: `11ccbfadcb5cb8f68224667e7f442b458a57fade8a09e6c62447d9476d058f1e`. Only this new report was written in the repository for the target. YAML, sources, status, history, pages, Eukaryota, GitHub objects and worktrees were unchanged.
