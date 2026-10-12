# YAML Record Review: Staphylococcus sp. CIFRI PTSB-29

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_cifri_ptsb_29.yaml`
- Started UTC: 2026-10-06T13:05:03Z
- Finished UTC: 2026-10-06T13:07:31Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035176`, Staphylococcus sp. CIFRI PTSB-29. It has SPECIES rank, BACTERIA domain, parent 91994, ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, external taxonomy mappings, genome links, phenotype assertions or causal graphs are present.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_sp_cifri_ptsb_29.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_sp_cifri_ptsb_29.yaml --out /private/tmp/spt29-validation.tsv`: passed, one file and zero errors. The TSV was read and contains only its header.
- Structured comparisons inspected the complete backbone row, ancestor chain, seven other imported taxon tables, PATHS/scope, synonyms, attestation and seed event.
- Exact-ID reads found no target entry in the type-material, merged-ID or dropped tables.
- Live NCBI Taxonomy XML, Datasets, exact non-descendant Assembly/Nuccore searches and complete marker metadata were inspected.
- `just validate-products` is inapplicable because no curator-added graph nodes are present. No undocumented focused term/reference validator was invented.
- Ignored-inclusive history filename and content searches found no target artifact. The inline seed event was checked; no history validator was run against a nonexistent target file.
- Full-corpus reproduction, validation, tests, history validation, provenance/site checks and `just qc` were not run. Focused checks are not corpus-wide certification.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221904` supports the exact label, rank, parent, genetic code, empty synonyms and NCBI-only provenance. The native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31344`. `data/taxa/PATHS.tsv:14395` resolves this file, and `curation/seed_scope.tsv:322191` supplies its 2026-09-13 NCBI-only scope rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035176&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035176) agree on the species-level concept and all ten ancestor IDs: 1, 131567, 2, 1783272, 1239, 91061, 1385, 90964, 1279 and 91994. The immediate parent is unclassified Staphylococcus, NO_RANK. All ancestor labels and ranks agree with the backbone.

The provisional source label is not a validly published binomial. A strain qualifier in nucleotide metadata does not justify changing NCBI's SPECIES rank to STRAIN. EXACT grounding means agreement with this NCBI concept, not independent validation of a species boundary or experimental phenotype.

## Evidence

The NCBITAXON attestation counts one NAME from snapshot 2026-09-13. The 2026-09-13T17:54:04Z SEEDED_FROM_SOURCES event by seed_from_sources agrees with the inventory and scope rationale. It does not claim human-reviewed status.

The exact Nuccore search returned only UID 333973497. Complete [JF784037.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF784037.1) identify Staphylococcus sp. CIFRI PTSB-29, strain CIFRI PTSB-29 and taxon 1035176. It is a 1,433-base partial 16S rRNA gene, partial at both ends, not a genome assembly. Source qualifiers describe marine water from Puri, India, collected by Bijay Kumar Behera. These are isolate-specific submission details, not genus-wide habitat assertions.

The marker was created and updated on 30 May 2011. Its direct submission is dated 5 April 2011 and names Behera, Sharma, Dsa, Chanda, Sahoo and Patra at the Central Inland Fisheries Research Institute. Dsa is the spelling in the inspected metadata; it was not silently normalized. Its other reference remains marked unpublished. A manuscript title about salt-tolerant bacteria alone cannot establish a numerical growth limit or mechanism.

The exact Assembly search returned zero items and reported the taxid query phrase as not found. This is bounded to the exact NCBI concept, not proof that no genome exists elsewhere or under another classification. Datasets' dsDNA designation is not an assembly accession.

The Behera et al. primary paper, [DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), was inspected through its [author-uploaded text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis). Table 2 connects P-TSB-29, 1,433 bases and JF784037, with Staphylococcus hominis as the nearest-strain comparison and 99.93 alignment identity. Table 1 places P-TSB-29 in the Puri-water salt-screening cohort. The accession establishes this literature connection despite punctuation differences. The paper's sequence-based species association does not establish a current NCBI merge or justify overwriting the carried unclassified Staphylococcus placement. No numerical salt-growth limit is inferred from extraction-corrupted symbols.

Sevim and Sevim's [2022 primary paper](https://dergipark.org.tr/en/download/article-file/2348465), DOI 10.28979/jarnas.1097397, was also inspected for its abstract, methods and Table 1. The target row on printed page 646 was visually verified from the PDF: JF784037 and CIFRI PTSB-29 are a GenBank comparison hit for isolate KT5.4, with 100% query coverage and 99.72% similarity. They are not the paper's newly isolated bacterium. The methods assign that study's sequences to MT537942-MT537963. Consequently, the larval-host and Turkish collection context cannot be transferred to this marine-water CIFRI isolate.

## Completeness

Initial `rg --no-ignore --hidden -n -z` searches covered taxid, full label/slug and CIFRI PTSB-29/P-TSB-29/TSB29 variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored and compressed files were included.

All eleven candidate rows were read in full: three TSV rows and eight native JSONL rows. Lossless common-field reconstruction and exact address reconciliation were checked. Expanded searches for JF784037, nucleotide UID 333973497 and both inspected DOIs returned no matches in those roots. All five SOURCE.json files were separately fully traversed for both patterns, with no hit. No target report or history filename was found before writing this report.

All seven other imported taxon evidence tables have no exact target row, and the backbone has no direct children. Zero BacDive strains and empty nomenclature/mapping/genome fields agree with the checked inputs. No eligible culture-deposit identity chain or target assembly was established.

Record-level literature enrichment is optional for this seeded record. Phenotype, medium and habitat details need the appropriate sibling-model scope and claim-specific evidence. A database-reference occurrence in another study is not a missing host association. iModulonDB is inapplicable because this YAML names no functional gene, regulator, pathway or expression module.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's identity, provenance, lineage, counts or status. The inspected literature supports bounded context, not an obligatory change to the record's carried classification.

## Recommended Edits

None required. Do not hand-edit this generated YAML, infer S. hominis identity from a partial-marker comparison, count JF784037.1 as a genome, or attach KT5.4's host or location to this taxon.

Any later authority-supported identity correction belongs in the pinned inventory/extraction pipeline. Representation changes belong in `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, followed by validated regeneration. Literature enrichment needs a supported maintained input and explicit claim scope.

## Follow-up Checks

For a source refresh, recheck taxon 1035176, its complete parent chain and JF784037.1. Before adding growth claims elsewhere, inspect the original salt-table symbols and concentration columns visually and reconcile them with the methods. Distinguish experimental isolates from database-reference rows in later papers.

Run both focused validators on a regenerated record and corpus reproduction/full QC before release. Any future genome association requires explicit provenance and an eligible strain identity chain.

## Additional Notes

Numeric matches concern GOLD analysis Ga0493203 for Alphaproteobacteria bacterium AG-909-K09, whose IMG ID is 8031035176; Mycobacterium tuberculosis run ERR1035176; Collinsella aerofaciens with SAMN41035176 and GCA/GCF_040926285.1; and Campylobacter jejuni GCA_010351765.1. These do not identify this target. The GOLD row's unscreened single-cell analysis and the Collinsella GTDB mapping are not target attestations.

The PDF browser screenshot failed twice. The public PDF was downloaded to temporary storage and page 6 was rendered successfully with macOS PDFKit because pdftoppm was unavailable; the target row was visually inspected. PDFKit emitted a generic CoreGraphics warning, but the rendered page was legible. The earlier CIFRI paper was inspected as extracted primary text only. No independent sequence analysis, phylogram inference, experimental replication assessment or release-wide certification was performed.

Only this new report was written in the repository for this target. Temporary PDF inspection files were outside the repo. No YAML, source, code, generated page, history, status or older report was changed. Eukaryotic reviews were not reopened.
