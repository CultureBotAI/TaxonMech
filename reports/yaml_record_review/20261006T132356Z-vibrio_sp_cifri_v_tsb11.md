# YAML Record Review: Vibrio sp. CIFRI V-TSB11

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/vibrio_sp_cifri_v_tsb11.yaml`
- Started UTC: 2026-10-06T13:21:49Z
- Finished UTC: 2026-10-06T13:23:56Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035180`, Vibrio sp. CIFRI V-TSB11. It has SPECIES rank, BACTERIA domain, parent 2614977, ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, taxonomy mappings, genome links, phenotype assertions or causal graphs are present.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/vibrio_sp_cifri_v_tsb11.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/vibrio_sp_cifri_v_tsb11.yaml --out /private/tmp/vv11-validation.tsv`: passed, one file and zero errors. The TSV was read and contains only its header.
- Structured comparisons inspected the complete backbone row, ancestor chain, seven other imported taxon tables, PATHS/scope, synonyms, attestation and seed event.
- Exact-ID reads found no target entry in the type-material, merged-ID or dropped tables.
- Live NCBI Taxonomy XML, Datasets, exact non-descendant Assembly/Nuccore searches, complete target marker metadata and comparator metadata were inspected.
- `just validate-products` is inapplicable because no curator-added graph nodes are present. No undocumented focused term/reference validator was invented.
- Ignored-inclusive history filename and content searches found no target artifact. The inline seed event was checked; no history validator was run against a nonexistent target file.
- Full-corpus reproduction, validation, tests, history validation, provenance/site checks and `just qc` were not run. Focused checks are not corpus-wide certification.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221908` supports the exact label, rank, parent, genetic code, empty synonyms and NCBI-only provenance. The native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31348`. `data/taxa/PATHS.tsv:14399` resolves this file, and `curation/seed_scope.tsv:322195` supplies its 2026-09-13 NCBI-only scope rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035180&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035180) agree on the species-level concept and all ten ancestor IDs: 1, 131567, 2, 3379134, 1224, 1236, 135623, 641, 662 and 2614977. The immediate parent is unclassified Vibrio, NO_RANK. All ancestor labels and ranks agree with the backbone.

The provisional label is not a validly published binomial. A strain qualifier in nucleotide metadata does not justify replacing NCBI's SPECIES rank with STRAIN. EXACT grounding means agreement with this NCBI concept, not independent validation of a species boundary or phenotype.

## Evidence

The NCBITAXON attestation counts one NAME from snapshot 2026-09-13. The 2026-09-13T17:54:04Z SEEDED_FROM_SOURCES event by seed_from_sources agrees with the inventory and scope rationale. It does not claim human-reviewed status.

The exact Nuccore search returned only UID 333973472. Complete [JF784012.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF784012.1) identify Vibrio sp. CIFRI V-TSB11, strain CIFRI V-TSB11 and taxon 1035180. This is a 981-base partial 16S rRNA gene, partial at both ends, not a genome assembly. Source qualifiers describe marine water from Vizag, India, collected by Bijay Kumar Behera. These are isolate-specific submission details.

The marker was created and updated on 30 May 2011. Its direct submission is dated 5 April 2011 and names Behera, Sharma, Das, Chanda and Patra at the Central Inland Fisheries Research Institute. Its other reference remains marked unpublished. A manuscript title about salt-tolerant bacteria alone cannot establish a numerical growth limit or mechanism.

The exact Assembly search returned zero items and reported the taxid query phrase as not found. This is bounded to the exact NCBI concept, not proof that no genome exists elsewhere or under another classification. Datasets' dsDNA designation is not an assembly accession.

The inspected [Behera et al. paper, DOI 10.1007/s40011-014-0440-6](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis) connects V-TSB-11 to JF784012 and V-TSB-1 to JF784015. Similarity comparisons do not establish a current taxonomic merge.

Complete comparator [JF784015.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF784015.1) instead identify Vibrio alginolyticus, taxon 663, strain CIFRI V-TSB1. That partial 16S record has 1,448 bases and a source qualifier naming marine water from Yanam. Its accession, taxon cross-reference and strain designation differ from the reviewed target. These source records do not justify transferring the comparator's classification or other literature associations to V-TSB11. No equivalence was inferred from the nearly identical labels.

## Completeness

Initial `rg --no-ignore --hidden -n -z` searches covered taxid, full label/slug and CIFRI V-TSB11/V-TSB-11/TSB11 variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored and compressed files were included.

All sixteen candidate rows were read in full: seven TSV rows and nine native JSONL rows. Lossless common-field reconstruction and exact address reconciliation were checked. Expanded searches for JF784012, nucleotide UID 333973472, comparator JF784015 and the inspected DOI returned no matches in those roots. All five SOURCE.json files were separately fully traversed for both patterns, with no hit. Ignored-inclusive filename searches found no prior report for this exact record or target history artifact before writing this report.

All seven other imported taxon evidence tables have no exact target row, and the backbone has no direct children. Zero BacDive strains and empty nomenclature/mapping/genome fields agree with the checked inputs. No eligible culture-deposit identity chain or target assembly was established.

Record-level literature enrichment is optional for this seeded record. Phenotype, medium and habitat details need the appropriate sibling-model scope and claim-specific evidence. iModulonDB is inapplicable because this YAML names no functional gene, regulator, pathway or expression module.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's identity, provenance, lineage, counts or status. The comparator was kept separate and supplies no missing representation for this record.

## Recommended Edits

None required. Do not hand-edit this generated YAML, conflate V-TSB11 with V-TSB1, infer species-level equivalence from a partial-marker comparison or count JF784012.1 as a genome.

Any later authority-supported identity correction belongs in the pinned inventory/extraction pipeline. Representation changes belong in `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, followed by validated regeneration. Literature enrichment needs a supported maintained input and explicit claim scope.

## Follow-up Checks

For a source refresh, recheck taxon 1035180, its complete parent chain and JF784012.1. Any proposed identity link to V-TSB1 requires explicit authority or depositor provenance. Before adding salt-growth claims elsewhere, visually verify the original table symbols and concentration columns against the methods; none were interpreted quantitatively here.

Run both focused validators on a regenerated record and corpus reproduction/full QC before release. Any future genome association requires explicit provenance and an eligible strain identity chain.

## Additional Notes

Short-designation matches identify Anoxybacillus sp. TSB-11, taxon 413095, and Lactococcus sp. TSB11, taxon 1224416. Numeric matches concern Collinsella aerofaciens SAMN41035180, GCA/GCF_040926205.1, whose GTDB name is Collinsella aerofaciens_BC; Campylobacter jejuni GCA_010351805.1; Streptococcus pneumoniae isolate 1035180, GCA_058711665.1; and Mycobacterium tuberculosis ERR1035180 with ATB ERZ3502366/SAMEA3558713. None identifies this Vibrio taxon.

The primary paper was inspected as extracted text only. No visual salt-table verification, independent sequence alignment, phylogram interpretation, experimental replication assessment or release-wide certification was performed. Comparator metadata were used only for identity discrimination, not a second record review. Only this new report was written in the repository for this target. No YAML, source, code, generated page, history, status or older report was changed. Eukaryotic reviews were not reopened.
