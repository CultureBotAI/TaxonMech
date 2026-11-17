# YAML Record Review: Staphylococcus sp. CIFRI P-TSB-31

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_cifri_p_tsb_31.yaml`
- Started UTC: 2026-10-06T13:00:38Z
- Finished UTC: 2026-10-06T13:03:09Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035175`, Staphylococcus sp. CIFRI P-TSB-31. It has SPECIES rank, BACTERIA domain, parent 91994, ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, external taxonomy mappings, genome links, phenotype assertions or causal graphs are present.

The target was resolved by its exact CURIE and pinned path. The punctuation-neighbor CIFRI PTSB-31, taxon 1035177, was checked only to disambiguate evidence; this is not a completed review or verdict for that second record.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_sp_cifri_p_tsb_31.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_sp_cifri_p_tsb_31.yaml --out /private/tmp/sp31-validation.tsv`: passed, one file and zero errors. The TSV was read and contains only its header.
- Structured comparisons inspected the complete backbone row, ancestor chain, seven other imported taxon tables, PATHS/scope, synonyms, attestation and seed event.
- Exact-ID reads found no target entry in the type-material, merged-ID or dropped tables.
- Live NCBI Taxonomy XML, Datasets, exact non-descendant Assembly/Nuccore searches and complete marker metadata were inspected. The similarly named taxon and the paper's alternative accession were also checked at NCBI.
- `just validate-products` is inapplicable because no curator-added graph nodes are present. No undocumented focused term/reference validator was invented.
- Ignored-inclusive history filename and content searches found no target artifact. The inline seed event was checked; no history validator was run against a nonexistent target file.
- Full-corpus reproduction, validation, tests, history validation, provenance/site checks and `just qc` were not run. Focused checks are not corpus-wide certification.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221903` supports the exact label, rank, parent, genetic code, empty synonyms and NCBI-only provenance. The native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31343`. `data/taxa/PATHS.tsv:14394` resolves this file, and `curation/seed_scope.tsv:322190` supplies its 2026-09-13 NCBI-only scope rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035175&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035175) agree on the species-level concept and all ten ancestor IDs: 1, 131567, 2, 1783272, 1239, 91061, 1385, 90964, 1279 and 91994. The immediate parent is unclassified Staphylococcus, NO_RANK. All ancestor labels and ranks agree with the backbone.

The provisional source label is not a validly published binomial. A strain qualifier in nucleotide metadata does not justify changing NCBI's SPECIES rank to STRAIN. EXACT grounding means agreement with this NCBI concept, not proof that it represents a biologically distinct isolate from every similarly named submission.

## Evidence

The NCBITAXON attestation counts one NAME from snapshot 2026-09-13. The 2026-09-13T17:54:04Z SEEDED_FROM_SOURCES event by seed_from_sources agrees with the inventory and scope rationale. It does not claim human-reviewed status or a count of distinct biological isolates.

The exact Nuccore search returned only UID 333973499. Complete [JF784039.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF784039.1) identify Staphylococcus sp. CIFRI P-TSB-31, strain CIFRI P-TSB-31 and taxon 1035175. It is a 1,362-base partial 16S rRNA gene, partial at both ends, not a genome assembly. Source qualifiers describe marine water from Puri, India, collected by Bijay Kumar Behera. These are submission details for the isolate, not general Staphylococcus habitat assertions.

The marker was created and updated on 30 May 2011. Its direct submission is dated 5 April 2011 and names Behera, Sharma, Das, Chanda and Patra at the Central Inland Fisheries Research Institute. Its other reference is marked unpublished and concerns identification of salt-tolerant bacteria from India's east coast. The title alone cannot establish a measured salt-growth limit or mechanism.

The exact Assembly search returned zero items and reported the taxid query phrase as not found. This is bounded to the exact NCBI concept, not proof that no genome exists elsewhere or under another classification. Datasets' dsDNA designation is not an assembly accession.

The Behera et al. primary paper, [DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), was inspected through its [author-uploaded text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis). Table 2 labels an isolate P-TSB-31, with 1,362 bases and a nearest-strain comparison to Staphylococcus hominis, but explicitly cites JF784031, not this target's JF784039. The extracted text search found no JF784039. The similar designation and equal sequence length therefore do not establish that the paper's experimental results belong to taxon 1035175.

Complete [JF784031.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF784031.1) identify CIFRI PTSB-31 and taxon 1035177, with nucleotide UID 333973491. They likewise describe a 1,362-base partial 16S marker and Puri marine water, but include Sahoo in the submission authors. Live [taxonomy 1035177](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035177&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035177) retain that separate identifier and spelling. The two submissions might concern the same biological isolate, but no inspected authority equates or merges them. This review neither asserts their biological independence nor transfers the paper's S. hominis association to the target.

## Completeness

Initial `rg --no-ignore --hidden -n -z` searches covered taxid, full label/slug and CIFRI P-TSB-31/PTSB-31/TSB31 variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored and compressed files were included.

All 25 candidate rows were read in full: eight TSV rows and seventeen native JSONL rows. Lossless common-field reconstruction and exact address reconciliation were checked. Expanded searches for JF784039, nucleotide UID 333973499, comparator JF784031 and DOI 10.1007/s40011-014-0440-6 returned no matches in those roots. All five SOURCE.json files were separately fully traversed for both patterns, with no hit. No target report or history filename was found before writing this report.

All seven other imported taxon evidence tables have no exact target row, and the backbone has no direct children. Zero BacDive strains and empty nomenclature/mapping/genome fields agree with the checked inputs. Neither marker supplies an eligible culture-deposit identity chain or assembly.

The separate local comparator rows are `data/raw/ncbitaxon_taxa.tsv:221905`, `data/catalog/ncbi_names-0005.jsonl.gz:31345` and `curation/seed_scope.tsv:322192`. They support a separate source concept, not an established synonym of this target. Omitting an inferred synonym or unverified literature association is appropriate.

Record-level literature evidence is optional for this seeded record. Phenotype, medium and habitat enrichment requires the appropriate sibling-model scope and evidence. iModulonDB is inapplicable because this YAML names no functional gene, regulator, pathway or expression module.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's identity, provenance, lineage, counts or status. The unresolved biological relationship between NCBI concepts 1035175 and 1035177 is an upstream identity question, not evidence that this generated record violates its source contract. No publication claim currently in the YAML is contradicted by the accession mismatch.

## Recommended Edits

None required. Do not hand-edit the generated YAML, normalize the punctuation into a synonym, infer S. hominis identity from the other accession, merge the NCBI concepts locally, or count either marker as a genome.

Any later authority-supported identity correction belongs upstream in NCBI and the pinned inventory/extraction pipeline. Representation changes belong in `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, followed by validated regeneration. Optional literature enrichment needs an explicit accession/identity chain.

## Follow-up Checks

Before merging identities or attaching the paper to this target, establish whether JF784039.1 and JF784031.1 are duplicate submissions, distinct isolates, or a citation error using authoritative accession history or an explicit primary-source clarification. Equal marker lengths and near-identical labels are insufficient. A sequence comparison alone would not prove strain identity.

For a source refresh, recheck taxon 1035175, its complete parent chain, current merge status and JF784039.1. Run both focused validators on any regenerated record and corpus reproduction/full QC before release. Any future genome association requires explicit provenance and an eligible strain identity chain.

## Additional Notes

Other candidates concern Streptomyces sp. TSB31 (1184156), Pseudomonas aeruginosa Pae_CF67.08p with GCA/GCF_001035175.1 and GOLD Ga0158539, Collinsella aerofaciens with SAMN41035175 and GCA/GCF_040926325.1, Mycobacterium tuberculosis run ERR1035175, Klebsiella pneumoniae GCA_031035175 versions 1 through 3, and Mediterraneibacter faecis GCA_061035175.1. An ATB Enterobacter cloacae row matches a numeric substring in its SeqKit sum. These are not target taxon or strain links.

The paper was inspected as extracted primary text, not a rendered PDF. No numerical salt-growth limit, phylogram interpretation, independent sequence analysis or experimental replication assessment is asserted. No release-wide certification was performed. The comparator checks do not count as a second record review.

Only this new report was written for this target. No YAML, source, code, generated page, history, status or older report was changed. Eukaryotic reviews were not reopened.
