# YAML Record Review: Staphylococcus sp. CIFRI PTSB-31

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_cifri_ptsb_31.yaml`
- Started UTC: 2026-10-06T13:08:28Z
- Finished UTC: 2026-10-06T13:12:45Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035177`, Staphylococcus sp. CIFRI PTSB-31. It has SPECIES rank, BACTERIA domain, parent 91994, ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, external taxonomy mappings, genome links, phenotype assertions or causal graphs are present.

This target is not the separately represented NCBI concept 1035175, Staphylococcus sp. CIFRI P-TSB-31. Similar names warrant an identity check, not automatic synonymy or an assumption of biological independence.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_sp_cifri_ptsb_31.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_sp_cifri_ptsb_31.yaml --out /private/tmp/spt31-validation.tsv`: passed, one file and zero errors. The TSV was read and contains only its header.
- Structured comparisons inspected the complete backbone row, ancestor chain, seven other imported taxon tables, PATHS/scope, synonyms, attestation and seed event.
- Exact-ID reads found no target entry in the type-material, merged-ID or dropped tables.
- Live NCBI Taxonomy XML, Datasets, exact non-descendant Assembly/Nuccore searches and complete marker metadata were inspected.
- `just validate-products` is inapplicable because no curator-added graph nodes are present. No undocumented focused term/reference validator was invented.
- Ignored-inclusive history filename and content searches found no target artifact. The inline seed event was checked; no history validator was run against a nonexistent target file.
- Full-corpus reproduction, validation, tests, history validation, provenance/site checks and `just qc` were not run. Focused checks are not corpus-wide certification.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221905` supports the exact label, rank, parent, genetic code, empty synonyms and NCBI-only provenance. The native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31345`. `data/taxa/PATHS.tsv:14396` resolves this file, and `curation/seed_scope.tsv:322192` supplies its 2026-09-13 NCBI-only scope rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035177&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035177) agree on the species-level concept and all ten ancestor IDs: 1, 131567, 2, 1783272, 1239, 91061, 1385, 90964, 1279 and 91994. The immediate parent is unclassified Staphylococcus, NO_RANK. All ancestor labels and ranks agree with the backbone.

The provisional source label is not a validly published binomial. A strain qualifier in nucleotide metadata does not justify replacing NCBI's SPECIES rank with STRAIN. EXACT grounding means agreement with this NCBI concept, not independent validation of a species boundary or phenotype.

## Evidence

The NCBITAXON attestation counts one NAME from snapshot 2026-09-13. The 2026-09-13T17:54:04Z SEEDED_FROM_SOURCES event by seed_from_sources agrees with the inventory and scope rationale. It does not claim human-reviewed status.

The exact Nuccore search returned only UID 333973491. Complete [JF784031.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF784031.1) identify Staphylococcus sp. CIFRI PTSB-31, strain CIFRI PTSB-31 and taxon 1035177. It is a 1,362-base partial 16S rRNA gene, partial at both ends, not a genome assembly. Source qualifiers describe marine water from Puri, India, collected by Bijay Kumar Behera. These are isolate-specific submission details, not genus-wide habitat assertions.

The marker was created and updated on 30 May 2011. Its direct submission is dated 5 April 2011 and names Behera, Sharma, Sahoo, Das, Chanda and Patra at the Central Inland Fisheries Research Institute. Its other reference remains marked unpublished. A manuscript title about salt-tolerant bacteria alone cannot establish a numerical growth limit or mechanism.

The exact Assembly search returned zero items and reported the taxid query phrase as not found. This is bounded to the exact NCBI concept, not proof that no genome exists elsewhere or under another classification. Datasets' dsDNA designation is not an assembly accession.

The Behera et al. primary paper, [DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), was inspected through its [author-uploaded text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis). Table 2 connects P-TSB-31, 1,362 bases and JF784031, with Staphylococcus hominis as the nearest-strain comparison and 99.93 alignment identity. Table 1 places P-TSB-31 in the Puri-water salt-screening cohort. The exact accession connects this paper entry to taxon 1035177 despite the paper's hyphenation resembling the other NCBI name. This is not authority for merging taxa or replacing the carried NCBI classification with S. hominis. No numerical salt-growth limit is inferred from extraction-corrupted symbols.

The inspected [NCBI concept 1035175](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035175&retmode=xml) instead owns [JF784039.1](https://www.ncbi.nlm.nih.gov/nuccore/JF784039.1). That marker is also 1,362 bases and has similar Puri source metadata, but its taxon cross-reference and accession are different. Its author list lacks Sahoo. Neither inspected authority establishes that the two concepts denote distinct biological isolates or that they are equivalent. Preserve this unresolved upstream identity question; the reviewed YAML asserts neither equivalence nor independence.

## Completeness

Initial `rg --no-ignore --hidden -n -z` searches covered taxid, full label/slug and CIFRI PTSB-31/P-TSB-31/TSB31 variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored and compressed files were included.

All fifteen candidate rows were read in full: seven TSV rows and eight native JSONL rows. Lossless common-field reconstruction and exact address reconciliation were checked. Expanded searches for JF784031, nucleotide UID 333973491, comparator JF784039 and the inspected DOI returned no matches in those roots. All five SOURCE.json files were separately fully traversed for both patterns, with no hit. Ignored-inclusive filename searches found no prior report for this exact record or target history artifact before writing this report.

All seven other imported taxon evidence tables have no exact target row, and the backbone has no direct children. Zero BacDive strains and empty nomenclature/mapping/genome fields agree with the checked inputs. No eligible culture-deposit identity chain or target assembly was established.

Record-level literature enrichment is optional for this seeded record. Phenotype, medium and habitat details need the appropriate sibling-model scope and claim-specific evidence. iModulonDB is inapplicable because this YAML names no functional gene, regulator, pathway or expression module.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's identity, provenance, lineage, counts or status. The unresolved relationship to taxon 1035175 is an upstream identity question, not an unsupported equivalence assertion in this YAML.

## Recommended Edits

None required. Do not hand-edit this generated YAML, merge similarly spelled NCBI concepts, infer S. hominis identity from a partial-marker comparison, or count JF784031.1 as a genome.

Any later authority-supported identity correction belongs in the pinned inventory/extraction pipeline. Representation changes belong in `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, followed by validated regeneration. Literature enrichment needs a supported maintained input and explicit claim scope.

## Follow-up Checks

For a source refresh, recheck taxon 1035177, its complete parent chain and JF784031.1. Resolve any proposed equivalence with taxon 1035175 and JF784039.1 through explicit authority or depositor provenance, not spelling similarity, equal marker length or shared location. Keep the paper's accession-specific connection separate from its isolate-name punctuation.

Before adding growth claims elsewhere, inspect the original salt-table symbols and concentration columns visually and reconcile them with the methods. Run both focused validators on a regenerated record and corpus reproduction/full QC before release. Any future genome association requires explicit provenance and an eligible strain identity chain.

## Additional Notes

The short designation TSB31 also identifies Streptomyces sp. TSB31, taxon 1184156; it is not this Staphylococcus concept. Numeric matches concern Mycobacterium tuberculosis run ERR1035177 and its AllTheBacteria assembly ERZ3502368/SAMEA3558710, and Collinsella aerofaciens with SAMN41035177 and GCA/GCF_040926345.1. The Collinsella GTDB name is Collinsella aerofaciens_BB. Those genomes and mappings are not target attestations.

The primary paper was inspected as extracted text only. No visual salt-table verification, independent sequence alignment, phylogram interpretation, experimental replication assessment or release-wide certification was performed. Comparator metadata were inspected for identity discrimination, not a second review of the already reported record.

Only this new report was written in the repository for this target. No YAML, source, code, generated page, history, status or older report was changed. Eukaryotic reviews were not reopened.
