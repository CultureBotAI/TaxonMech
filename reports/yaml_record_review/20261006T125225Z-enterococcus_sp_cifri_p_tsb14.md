# YAML Record Review: Enterococcus sp. CIFRI P-TSB14

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterococcus_sp_cifri_p_tsb14.yaml`
- Started UTC: 2026-10-06T12:48:33Z
- Finished UTC: 2026-10-06T12:52:25Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035171`, Enterococcus sp. CIFRI P-TSB14. It has SPECIES rank, BACTERIA domain, parent 2608891, ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature entries, external taxonomy mappings, genome links, phenotype assertions or causal graphs are present.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/enterococcus_sp_cifri_p_tsb14.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/enterococcus_sp_cifri_p_tsb14.yaml --out /private/tmp/etsb14-validation.tsv`: passed, one file and zero errors. The TSV was read and contains only its header.
- Structured comparisons inspected the complete backbone row, ancestor chain, seven other imported taxon tables, PATHS/scope, synonyms, attestation and seed provenance.
- Exact-ID reads found no target entry in the type-material, merged-ID or dropped tables.
- Live NCBI Taxonomy XML, Datasets, exact non-descendant Assembly/Nuccore searches and complete marker metadata were inspected.
- `just validate-products` is inapplicable because no curator-added graph nodes are present. No undocumented focused term/reference validator was invented.
- Ignored-inclusive history filename and content searches found no target artifact. The inline seed event was checked; no history validator was run against a nonexistent target file.
- Full-corpus reproduction, validation, tests, history validation, provenance/site checks and `just qc` were not run. Focused checks are not corpus-wide certification.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221900` supports the exact label, rank, parent, genetic code, empty synonyms and NCBI-only provenance. The native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31340`. `data/taxa/PATHS.tsv:14391` resolves this file, and `curation/seed_scope.tsv:322187` supplies its 2026-09-13 NCBI-only scope rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035171&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035171) agree on the species-level concept and all ten ancestor IDs: 1, 131567, 2, 1783272, 1239, 91061, 186826, 81852, 1350 and 2608891. The immediate parent is unclassified Enterococcus, NO_RANK.

The provisional source label is not a validly published binomial. A strain qualifier in nucleotide metadata does not justify changing NCBI's SPECIES rank to STRAIN. EXACT grounding means agreement with this NCBI concept, not independent validation of a species boundary or phenotype.

## Evidence

The NCBITAXON attestation counts one NAME from snapshot 2026-09-13. The 2026-09-13T17:54:04Z SEEDED_FROM_SOURCES event by seed_from_sources agrees with the inventory and scope rationale. It does not claim human-reviewed status.

The exact Nuccore search returned only UID 333973488. Complete [JF784028.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF784028.1) identify Enterococcus sp. CIFRI P-TSB14, strain CIFRI P-TSB14 and taxon 1035171. It is a 1,449-base partial 16S rRNA gene, partial at both ends, not a genome assembly. Source qualifiers describe marine water from Puri, India, collected by Bijay Kumar Behera. These are isolate-specific submission details, not general Enterococcus habitat assertions.

The sequence record was created and updated on 30 May 2011. Its direct submission is dated 5 April 2011 and names Behera, Sharma, Das, Chanda, Patra and Jana at the Central Inland Fisheries Research Institute. The other reference remains marked unpublished. Its salt-tolerant-bacteria study title alone cannot establish a quantitative phenotype.

The exact Assembly search returned zero items and reported the taxid query phrase as not found. This bounds the result to the exact NCBI concept; it does not prove that no genome exists elsewhere or under another classification. Datasets' dsDNA designation is not an assembly accession.

The [publisher record](https://link.springer.com/article/10.1007/s40011-014-0440-6) verifies the later Behera et al. paper, DOI 10.1007/s40011-014-0440-6, published online in 2014 and in the 2015 issue. Its publicly accessible [author-uploaded primary text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis) was inspected for methods and relevant tables. Table 2 explicitly connects P-TSB-14, 1,449 bases and JF784028; its nearest-strain comparison names Enterococcus faecalis with 99.93 alignment identity. Table 1 places P-TSB-14 in the Puri-water isolation and salt-screening cohort. This is a verified literature connection, unlike a match based only on authors or locality.

The paper's sequence-based association with E. faecalis and NCBI's retained unclassified Enterococcus placement have different resolution. Preserve that distinction: the paper does not establish a current NCBI merge or authorize overwriting the carried lineage. No quantitative salt-growth result or species-wide phenotype is imported into this review verdict.

## Completeness

Initial `rg --no-ignore --hidden -n -z` searches covered the taxid, full label/slug and CIFRI P-TSB14/P-TSB-14/TSB14 variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored and compressed files were included.

All thirteen candidate rows were read in full: five TSV rows and eight native JSONL rows. Lossless common-field reconstruction and exact address reconciliation were checked. Expanded searches for JF784028, nucleotide UID 333973488 and DOI 10.1007/s40011-014-0440-6 returned no matches in those roots. All five SOURCE.json files were separately fully traversed for both the identity and expanded patterns, with no hit. No target report or history filename was found before writing this report.

All seven other imported taxon evidence tables have no exact target row, and the backbone has no direct children. Zero BacDive strains and empty nomenclature/mapping/genome fields agree with the checked inputs. The marker and paper supply no verified culture-deposit identity chain or assembly.

Literature enrichment is optional, not a mandatory missing representation. Any future experimental assertion needs its own supported scope and maintained representation. iModulonDB is inapplicable because this YAML names no functional gene, regulator, pathway or expression module; an external salt-screening paper does not create such an assertion here.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed identity, provenance, lineage, counts or status. Literature resolution differences and unrun full-corpus gates are retained as limitations, not demonstrated YAML errors.

## Recommended Edits

None required. Do not hand-edit this generated YAML, equate it with E. faecalis solely from a partial-marker comparison, count JF784028.1 as a genome, or turn a study title into phenotype evidence.

Any later NCBI identity refresh belongs in the pinned inventory/extraction pipeline. Representation changes belong in `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, followed by validated regeneration. Optional literature enrichment needs a supported maintained input and claim-specific evidence.

## Follow-up Checks

For a source refresh, recheck taxon 1035171, its complete parent chain and JF784028.1. Before adding salt-growth claims, visually verify the original table's concentration columns and symbols, reconcile them with the methods, and preserve isolate and assay scope.

Run both focused validators on a regenerated record and corpus reproduction/full QC before release. Any future genome link requires explicit provenance and an eligible strain identity chain.

## Additional Notes

The candidate rows distinguish this record from Burkholderia sp. TSB14 (taxon 1184138), Clostridium tertium with SAMN41035171 and GCA/GCF_040926385.1, Mycobacterium tuberculosis run ERR1035171, and metagenomic bacterium JPNA_maxbin.263 (taxon 1869227, GCA_029555535.1). The latter matches through a genome size of 1,035,171 bases, not the target taxid. None supplies a target genome or culture deposit.

The author-uploaded paper was inspected as extracted primary text, not as a rendered PDF. Its salt-table symbols are extraction-corrupted, so no numerical growth limit is asserted. No independent sequence reanalysis, phylogram interpretation, experimental replication assessment or release-wide certification was performed.

Only this new report was written for this target. No YAML, source, code, generated page, history, status or older report was changed. Eukaryotic reviews were not reopened.
