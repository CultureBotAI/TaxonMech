# YAML Record Review: Desulfovibrio sp. HS4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/desulfovibrio_sp_hs4.yaml`
- Started UTC: 2026-10-06T12:04:38Z
- Finished UTC: 2026-10-06T12:08:59Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035114`, Desulfovibrio sp. HS4. The record retains SPECIES rank, BACTERIA domain, parent unclassified Desulfovibrio (2593640), ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME assertion and one inline seed event. It asserts no habitat, corrosion phenotype, culture deposit, genome association or causal graph.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/desulfovibrio_sp_hs4.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/desulfovibrio_sp_hs4.yaml --out /private/tmp/deshs4-validation.tsv`: passed, one file and zero errors. Read the output TSV; it contains only the header.
- Structured comparisons of the complete backbone row, all ancestors, synonyms, seven other imported taxon tables, PATHS/scope, source attestation and seed provenance passed.
- Exact-ID checks of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Read live NCBI Taxonomy XML/Datasets, exact non-expanded Assembly/Nuccore results and all marker metadata, references and feature qualifiers. Inspected relevant thesis text and rendered figures.
- `just validate-products` is inapplicable: no curator-added graph nodes are present. Taxonomy identifiers were checked at their authority; no undocumented focused term/reference validator was invented.
- Ignored-inclusive history content and filename searches found no separate target artifact. Checked the inline seed event; no validator was run against a nonexistent separate history file.
- Full-corpus reproduction, validation, tests, history, provenance/site checks and `just qc` were not run. Focused checks do not certify the full corpus.

## Identity and Grounding

The backbone row at `data/raw/ncbitaxon_taxa.tsv:221891` agrees with the complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31326`. `data/taxa/PATHS.tsv:14378` resolves the slug, and `curation/seed_scope.tsv:322181` supports its one-source seed rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035114&retmode=xml) confirms the name, rank, parent and genetic code. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035114) confirms all ten ancestor IDs: 1, 131567, 2, 3379134, 200940, 3031449, 213115, 194924, 872 and 2593640.

Thermodesulfobacteriota / Desulfovibrionia is the carried NCBI chain, not a reconciliation with other classifications. EXACT refers to this NCBI concept. SPECIES is its authority rank, not a claim that HS4 is a validly published species binomial. The bare strain label alone is not a unique identity.

## Evidence

The attestation counts one NAME in the 2026-09-13 snapshot, not a culture, genome or experiment. The inline event at 2026-09-13T17:54:04Z agrees with the source and scope.

The exact Nuccore search returned [HQ188931.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ188931.1), a 1,445-base partial 16S rRNA sequence. Its source feature explicitly identifies Desulfovibrio sp. HS4, strain HS4, taxon 1035114 and marine sediment as isolation source. This is submitter-level habitat evidence, not a whole genome.

Dinh, Enning, Kuever and Widdel submitted the marker on 2010-08-26. Its unpublished reference discusses Desulfopila corrodens and Desulfovibrio ferrophilus, but the sequence feature identifies HS4. A reference title does not rename this isolate or identify it as IS4 or IS5. No DOI or PMID is attached to that sequence reference.

Dennis R. Enning's 2012 University of Bremen dissertation, [Bioelectrical corrosion of iron by lithotrophic sulfate-reducing bacteria](https://pure.mpg.de/rest/items/item_2484670_2/component/file_3253088/content), describes HS4 and HS5 isolated from iron-corroding enrichments (printed pages 36 and 60). Read these pages and supplements S1/S2; visually inspected printed pages 36, 87 and 88. HS4 is a hydrogen-scavenging control, distinct from strongly corrosive IS4/IS5. Figure S1 uses 2.4 square centimeters of iron in 1.4 liters of artificial seawater and warns that sulfate-derived sulfide values are imprecise. Figure S2 shows 1.57% weight loss for HS4 after 21 weeks, versus 0.96% and 0.77% for sterile controls; its caption allows occasional slight stimulation by hydrogenotrophs. Do not turn this into an absolute inability to affect corrosion.

The dissertation-to-marker association is plausible from the organism name and shared investigator, but remains an inference. Its searchable text yielded no HQ188931 match. Before formal phenotype enrichment, verify an explicit isolate-to-accession bridge. A dissertation is not automatically a peer-reviewed article.

## Completeness

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the ID, full label, slug, Desulfovibrio-associated variants and bounded HS4 tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.

Read all 78 initial candidate rows: thirteen TSV, eighteen GOLD and forty-seven other native JSONL rows. Common fields and per-row differences were losslessly factored with reconstruction assertions. The combined addresses reconcile exactly with discovery. Only the target backbone, native name and scope entries support this taxon; other matches are short-label or numeric collisions.

Expanded searches for HQ188931 and sequence UID 333973172 found no rows in those roots, including ignored and compressed files. All five SOURCE.json files were separately discovered without ignore filtering and completely traversed for the initial identity pattern; none matched. History content and filenames contained no separate target artifact.

The backbone has no synonyms or direct children. Seven other imported taxon tables have no exact target row. Zero BacDive strains is consistent with this pinned subtree, not proof that the named isolate does not exist. The exact Assembly query returned zero items with a phrases-not-found warning, not proof of global genome absence.

Empty optional nomenclature, mapping, habitat, phenotype and graph slots are acceptable for this seed. iModulonDB is inapplicable to this identity-only YAML, which names no functional gene, regulator or expression module. The 16S marker is not a genome.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the retained assertions. Optional literature or habitat enrichment is not a missing required representation.

## Recommended Edits

None required. Do not hand-edit the generated YAML, promote its status, append a review history event or infer corrosion activity from genus membership or a reference title.

Any accepted later enrichment belongs in maintained inventory handling and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`, with source-qualified identity tests. A bare HS4 label cannot establish a culture-deposit or genome join.

## Follow-up Checks

Before attaching an experimental phenotype, verify the accession bridge and preserve the experimental conditions and comparator results. Require an explicit source chain for any culture or genome association.

Run both focused validators for an accepted change, and corpus reproduction plus full QC before release.

## Additional Notes

The BacDive 12528 / StrainInfo SI-ID 40988 records use HS4 for Hoylesella/Prevotella buccalis, with NCBI species 28127 and strain 679190. Their ATCC 35310, DSM 20616, CCUG 15557, JCM 12246 and other deposits, marker sequences and GCA_000177075 / GCA_025151385 genomes do not belong to this Desulfovibrio.

Other name collisions include Vibrio enrichment clone HS4 (717089), Bacillus sp. Hs4 (1036646), Arthrobacter HS4-1/HS4-2 (1395626/1395627), Helicobacter suis HS4 (GCA_900196935.1; GOLD Go0496595 / Gp0380658 / Ga0347064), Pseudomonas aeruginosa HS4 (GCA_013522575.1), Escherichia coli HS4 and HS4-1, Cutibacterium avidum HS4, Virgibacillus oceani HS4 and Bacillus safensis HS4-2. Desulfovibrio Hs463_bin8 and Hs463_bin41 are distinct metagenomic strain designations, not HS4.

Numeric overlaps include Staphylococcus haemolyticus 94759 (SAMEA1035114; GCA/GCF_001231825.1; ATB ERZ3070571), Mycobacterium tuberculosis ERR1035114 (SAMEA3558647; ATB ERZ3502042), Bifidobacterium bifidum with SAMN41035114, and Campylobacter jejuni GCA_010351145.1. GOLD also matches the separate Pseudoalteromonas phage PSA-HS4 chain, a Hainan soil HS4 community and SAMN10351140-49 community projects. None supplies a target strain-genome association.

Browser extraction of the institutional PDF failed. The public download succeeded, and PDFKit provided text and rendered pages. PDFKit logged a generic CoreGraphics warning, but the relevant rendered pages were legible and the figures/captions were visually checked.

Only this new report was written in the repository for this individual review. No record, source, code, page, history or older report was changed. Eukaryotic reviews were not reopened.
