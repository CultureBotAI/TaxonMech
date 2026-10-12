# YAML Record Review: Desulfovibrio sp. HS3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/desulfovibrio_sp_hs3.yaml`
- Started UTC: 2026-10-06T11:59:32Z
- Finished UTC: 2026-10-06T12:02:56Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035113`, Desulfovibrio sp. HS3. It retains SPECIES rank, BACTERIA domain, parent unclassified Desulfovibrio (2593640), ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME assertion and one inline seed event. It asserts no habitat, corrosion phenotype, culture deposit, genome association or causal graph.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/desulfovibrio_sp_hs3.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/desulfovibrio_sp_hs3.yaml --out /private/tmp/deshs3-validation.tsv`: passed, one file and zero errors. Read the TSV; it contains only the header.
- Structured comparisons of the complete backbone row, ancestors, synonyms, seven other imported taxon tables, PATHS/scope, attestation and inline seed event passed.
- Exact-ID checks of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Read live NCBI Taxonomy XML/Datasets, exact non-expanded Assembly/Nuccore results, complete marker metadata and relevant primary-paper results/methods pages.
- `just validate-products` is inapplicable: no curator-added graph nodes are present. Taxonomy identifiers were checked at their authority; no undocumented focused term/reference validator was invented.
- Ignored-inclusive history content and filename searches found no separate target artifact. Checked the inline event; no validator was run against a nonexistent separate history file.
- Full-corpus reproduction, validation, tests, history, provenance/site checks and `just qc` were not run. Focused checks do not certify the full corpus.

## Identity and Grounding

The backbone row at `data/raw/ncbitaxon_taxa.tsv:221890` agrees with the complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31325`. `data/taxa/PATHS.tsv:14377` resolves the slug, and `curation/seed_scope.tsv:322180` supports the one-source seeding rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035113&retmode=xml) confirms the name, rank, parent and genetic code. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035113) confirms all ten ancestor IDs: 1, 131567, 2, 3379134, 200940, 3031449, 213115, 194924, 872 and 2593640.

Thermodesulfobacteriota / Desulfovibrionia is the carried NCBI chain, not a reconciliation with another classification. EXACT refers to this NCBI concept; SPECIES is its authority rank, not a claim that HS3 is a validly published species binomial. Other organisms with the short label HS3 do not disambiguate this taxon without the genus and identifier.

## Evidence

The attestation counts one NAME in the 2026-09-13 snapshot, not a culture, genome or experiment. The inline event at 2026-09-13T17:54:04Z agrees with source provenance and scope.

The exact Nuccore search returned [HQ188932.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ188932.1), a 1,452-base partial 16S rRNA sequence. Read all metadata, references and feature qualifiers. It explicitly identifies Desulfovibrio sp. HS3, strain HS3, taxon 1035113 and marine sediment as isolation source. This is submitter-level habitat evidence, not a whole-genome record.

Dinh, Enning, Kuever and Widdel submitted the marker on 2010-08-26. Its unpublished reference names Desulfopila corrodens and Desulfovibrio ferrophilus in its title, but the source feature identifies HS3. The reference title does not rename this isolate or make it one of those species. No DOI or PMID is attached to the sequence reference.

A relevant primary study is Enning et al. (2012), DOI:10.1111/j.1462-2920.2012.02778.x, PMID:22616633. Read its results and cultivation methods and visually inspected printed pages 1774 and 1783 (PDF indices 2 and 11) in the [institutional paper](https://www.mpi-bremen.de/Binaries/Binary2709/emi0014-1772.pdf). The study's Desulfovibrio HS3 was isolated from marine sediment under hydrogen-limited enrichment and used as a hydrogenotrophic control. It did not accelerate iron corrosion relative to sterile controls under the reported conditions. Strong corrosion by IS4 and IS5 must not be assigned to HS3.

The shared strain designation, source and overlapping authors make this a plausible literature association, but that link remains an inference: the searchable main-paper text contains no HQ188932 or accession statement. Supplementary files were not inspected. A formal phenotype addition should verify the isolate-to-accession chain and retain experimental conditions; the control result is not a claim of universal inability to corrode iron.

## Completeness

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the ID, full label, slug, Desulfovibrio-associated variants and bounded HS3 tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.

All 247 initial candidate addresses were accounted for. Read twelve complete TSV rows and nineteen complete GOLD rows. For 216 other native JSONL candidates, inspected every row's organism/taxon identity, source identifiers and matching fields with lossless factoring of that projection; the target name row was retained and read in full. The other 215 native rows were not full annotation reviews. The combined address set reconciles exactly with discovery.

Only the native scientific-name row identifies this Desulfovibrio taxon. Other HS3 names, HRS-HS3-bin identifiers and numeric overlaps belong to other recorded taxa or environmental projects. They do not establish a target strain-deposit or genome association.

Expanded searches for HQ188932, sequence UID 333973173, PMID 22616633 and the primary paper's DOI found no rows in those roots, including ignored and compressed files. All five SOURCE.json files were separately discovered without ignore filtering and traversed completely for the initial identity pattern; none matched. History content and filenames contained no separate target artifact.

The backbone has no synonyms or direct children. Seven other imported taxon tables have no exact target row. Zero BacDive strains agrees with the pinned subtree, not a claim that no isolate exists. The exact Assembly query returned zero items with a phrases-not-found warning, not proof of global genome absence.

Optional habitat, phenotype and graph slots may remain empty in this seed. iModulonDB is inapplicable to the identity-only YAML, which names no functional gene, regulator or expression module. The marker is not a genome.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the retained assertions. Optional literature or habitat enrichment is not a missing required representation.

## Recommended Edits

None required. Do not hand-edit the generated YAML, promote its status, append a review history event or infer iron-corrosion activity from genus membership or a paper title.

Any later accepted enrichment belongs in maintained inventory handling and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`, with source-qualified identity tests. Keep bare-label matches separate from supported strain identity.

## Follow-up Checks

Before attaching an experimental phenotype, inspect the study supplements or another primary source that explicitly connects the experiment's HS3 with HQ188932.1. Preserve its role as the control, distinguishing it from IS4 and IS5. Before adding culture or genome links, require an explicit source chain for this taxon.

Run both focused validators for an accepted change, and corpus reproduction plus full QC before release.

## Additional Notes

Bare-label collisions include Rhodococcus sp. HS3 (216855), Vibrio sp. HS3 (484436), Pseudovibrio sp. Hs3 (989452) and Bacillus sp. Hs3 (1036645), each with separate backbone, name and scope rows. Genome candidates include Helicobacter suis HS3 (GCA_900196865.1, BV-BRC 104628.27, GOLD Go0496596 / Gp0380659 / Ga0347075), Pseudomonas aeruginosa HS3 (GCA_013522595.1, BV-BRC 287.11892), Staphylococcus aureus HS3 (GCA_056621595.1), Escherichia coli HS3-104 / HS3-1 and Lactiplantibacillus pentosus HS3-L1 through HS3-L6. None is Desulfovibrio HS3.

Numerical matches include Staphylococcus haemolyticus 7589 (SAMEA1035113, paired GCA/GCF_001239725.1, BV-BRC 1283.205, GOLD Gp0140424, ATB ERZ3070576), Bifidobacterium bifidum RTP21002st1_F3_RTP21002_201210 (SAMN41035113, paired GCA/GCF_040927585.1, BV-BRC 1681.1551) and Mycobacterium tuberculosis ERR1035113 / SAMEA3558646 / ATB ERZ3502041. GOLD's SAMN10351130-39 entries are unrelated freshwater community projects. HRS-HS3-bin names occur across many other taxon assignments and accession versions; their shared token is not organism equivalence.

PMC initially exposed the article but later returned a browser challenge. Browser PDF screenshots timed out. The public institutional PDF download succeeded, and local PDFKit rendering allowed visual verification. An initial Swift cache-path failure was resolved by explicitly selecting a writable module cache; it did not affect record validation. A separate Syntrophy Portal search lead returned 404 and was not used as evidence.

Only this new report was written in the repository for this individual review. No record, source, code, page, history or older report was changed. Eukaryotic reviews were not reopened.
