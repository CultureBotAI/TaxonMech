# YAML Record Review: Vibrio sp. CIFRI P-TSB-17

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/vibrio_sp_cifri_p_tsb_17.yaml`
- Started UTC: 2026-10-06T13:19:10Z
- Finished UTC: 2026-10-06T13:20:55Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035179`, Vibrio sp. CIFRI P-TSB-17. It has SPECIES rank, BACTERIA domain, parent 2614977, ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, taxonomy mappings, genome links, phenotype assertions or causal graphs are present.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/vibrio_sp_cifri_p_tsb_17.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/vibrio_sp_cifri_p_tsb_17.yaml --out /private/tmp/vp17-validation.tsv`: passed, one file and zero errors. The TSV was read and contains only its header.
- Structured comparisons inspected the complete backbone row, ancestor chain, seven other imported taxon tables, PATHS/scope, synonyms, attestation and seed event.
- Exact-ID reads found no target entry in the type-material, merged-ID or dropped tables.
- Live NCBI Taxonomy XML, Datasets, exact non-descendant Assembly/Nuccore searches and complete marker metadata were inspected.
- `just validate-products` is inapplicable because no curator-added graph nodes are present. No undocumented focused term/reference validator was invented.
- Ignored-inclusive history filename and content searches found no target artifact. The inline seed event was checked; no history validator was run against a nonexistent target file.
- Full-corpus reproduction, validation, tests, history validation, provenance/site checks and `just qc` were not run. Focused checks are not corpus-wide certification.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221907` supports the exact label, rank, parent, genetic code, empty synonyms and NCBI-only provenance. The native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31347`. `data/taxa/PATHS.tsv:14398` resolves this file, and `curation/seed_scope.tsv:322194` supplies its 2026-09-13 NCBI-only scope rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035179&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035179) agree on the species-level concept and all ten ancestor IDs: 1, 131567, 2, 3379134, 1224, 1236, 135623, 641, 662 and 2614977. The immediate parent is unclassified Vibrio, NO_RANK. All ancestor labels and ranks agree with the backbone.

The provisional label is not a validly published binomial. A strain qualifier in nucleotide metadata does not justify replacing NCBI's SPECIES rank with STRAIN. EXACT grounding means agreement with this NCBI concept, not independent validation of a species boundary or phenotype.

## Evidence

The NCBITAXON attestation counts one NAME from snapshot 2026-09-13. The 2026-09-13T17:54:04Z SEEDED_FROM_SOURCES event by seed_from_sources agrees with the inventory and scope rationale. It does not claim human-reviewed status.

The exact Nuccore search returned only UID 333973486. Complete [JF784026.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF784026.1) identify Vibrio sp. CIFRI P-TSB-17, strain CIFRI P-TSB-17 and taxon 1035179. This is a 1,415-base partial 16S rRNA gene, partial at both ends, not a genome assembly. Source qualifiers describe marine water from Puri, India, collected by Bijay Kumar Behera. These are isolate-specific submission details.

The marker was created and updated on 30 May 2011. Its direct submission is dated 5 April 2011 and names Behera, Sharma, Das, Chanda and Patra at the Central Inland Fisheries Research Institute. Its other reference remains marked unpublished. A manuscript title about salt-tolerant bacteria alone cannot establish a numerical growth limit or mechanism.

The exact Assembly search returned zero items and reported the taxid query phrase as not found. This is bounded to the exact NCBI concept, not proof that no genome exists elsewhere or under another classification. Datasets' dsDNA designation is not an assembly accession.

Behera et al., [DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), was inspected via [author-uploaded primary text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis). Table 2 links P-TSB-17 to JF784026 and a V. parahaemolyticus comparison; Table 1 gives Puri water. The accession supports the literature connection, not a current taxonomic merge. Extraction-corrupted growth symbols were not interpreted quantitatively.

## Completeness

Initial `rg --no-ignore --hidden -n -z` searches covered taxid, full label/slug and CIFRI P-TSB-17/P-TSB17/TSB17 variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored and compressed files were included.

All nine candidate rows were read in full: three TSV rows and six native JSONL rows. Lossless common-field reconstruction and exact address reconciliation were checked. Expanded searches for JF784026, nucleotide UID 333973486 and the inspected DOI returned no matches in those roots. All five SOURCE.json files were separately fully traversed for both patterns, with no hit. Ignored-inclusive filename searches found no prior report for this exact record or target history artifact before writing this report.

All seven other imported taxon evidence tables have no exact target row, and the backbone has no direct children. Zero BacDive strains and empty nomenclature/mapping/genome fields agree with the checked inputs. No eligible culture-deposit identity chain or target assembly was established.

Record-level literature enrichment is optional for this seeded record. Phenotype, medium and habitat details need the appropriate sibling-model scope and claim-specific evidence. iModulonDB is inapplicable because this YAML names no functional gene, regulator, pathway or expression module.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's identity, provenance, lineage, counts or status. The inspected literature does not establish an obligatory change to its carried classification.

## Recommended Edits

None required. Do not hand-edit this generated YAML, infer species-level equivalence from a partial-marker comparison or count JF784026.1 as a genome.

Any later authority-supported identity correction belongs in the pinned inventory/extraction pipeline. Representation changes belong in `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, followed by validated regeneration. Literature enrichment needs a supported maintained input and explicit claim scope.

## Follow-up Checks

For a source refresh, recheck taxon 1035179, its complete parent chain and JF784026.1. Before adding salt-growth claims elsewhere, visually verify the original table symbols and concentration columns against the methods. Keep strain-specific observations distinct from genus-level claims.

Run both focused validators on a regenerated record and corpus reproduction/full QC before release. Any future genome association requires explicit provenance and an eligible strain identity chain.

## Additional Notes

Numeric matches concern Mycobacterium tuberculosis run ERR1035179 and ATB assembly ERZ3502364/SAMEA3558712, and Collinsella aerofaciens with SAMN41035179 and GCA/GCF_040926235.1. The Collinsella GTDB assignment is Collinsella aerofaciens_BH. These do not identify the target or supply its missing genome links.

The primary paper was inspected as extracted text only. No visual salt-table verification, independent sequence analysis, phylogram interpretation, experimental replication assessment or release-wide certification was performed. Only this new report was written in the repository for this target. No YAML, source, code, generated page, history, status or older report was changed. Eukaryotic reviews were not reopened.
