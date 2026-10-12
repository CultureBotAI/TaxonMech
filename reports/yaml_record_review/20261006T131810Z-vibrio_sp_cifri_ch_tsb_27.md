# YAML Record Review: Vibrio sp. CIFRI CH-TSB-27

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/vibrio_sp_cifri_ch_tsb_27.yaml`
- Started UTC: 2026-10-06T13:14:51Z
- Finished UTC: 2026-10-06T13:18:10Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035178`, Vibrio sp. CIFRI CH-TSB-27. It has SPECIES rank, BACTERIA domain, parent 2614977, ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, taxonomy mappings, genome links, phenotype claims or causal graphs are present.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/vibrio_sp_cifri_ch_tsb_27.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/vibrio_sp_cifri_ch_tsb_27.yaml --out /private/tmp/vch27-validation.tsv`: passed, one file and zero errors. The TSV was read and contains only its header.
- Structured comparisons inspected the complete backbone row, ancestor chain, seven other imported taxon tables, PATHS/scope, synonyms, attestation and seed event.
- Exact-ID reads found no target entry in the type-material, merged-ID or dropped tables.
- Live NCBI Taxonomy XML, Datasets, exact non-descendant Assembly/Nuccore searches and complete marker metadata were inspected.
- `just validate-products` is inapplicable because no curator-added graph nodes are present. No undocumented focused term/reference validator was invented.
- Ignored-inclusive history filename and content searches found no target artifact. The inline seed event was checked; no history validator was run against a nonexistent target file.
- Full-corpus reproduction, validation, tests, history validation, provenance/site checks and `just qc` were not run. Focused checks are not corpus-wide certification.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221906` supports the exact label, rank, parent, genetic code, empty synonyms and NCBI-only provenance. The native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31346`. `data/taxa/PATHS.tsv:14397` resolves this file, and `curation/seed_scope.tsv:322193` supplies its 2026-09-13 NCBI-only scope rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035178&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035178) agree on the species-level concept and all ten ancestor IDs: 1, 131567, 2, 3379134, 1224, 1236, 135623, 641, 662 and 2614977. The immediate parent is unclassified Vibrio, NO_RANK. All ancestor labels and ranks agree with the backbone.

The provisional label is not a validly published binomial. A strain qualifier in nucleotide metadata does not justify replacing NCBI's SPECIES rank with STRAIN. EXACT grounding means agreement with this NCBI concept, not independent validation of a species boundary or phenotype.

## Evidence

The NCBITAXON attestation counts one NAME from snapshot 2026-09-13. The 2026-09-13T17:54:04Z SEEDED_FROM_SOURCES event by seed_from_sources agrees with the inventory and scope rationale. It does not claim human-reviewed status.

The exact Nuccore search returned only UID 333973504. Complete [JF784044.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF784044.1) identify Vibrio sp. CIFRI CH-TSB-27, strain CIFRI CH-TSB-27 and taxon 1035178. This is a 1,439-base partial 16S rRNA gene, partial at both ends, not a genome assembly. Source qualifiers describe marine soil sediment from Chandipur, India, collected by Bijay Kumar Behera. These are isolate-specific submission details.

The marker was created and updated on 30 May 2011. Its direct submission is dated 5 April 2011 and names Behera, Sharma, Sahoo, Das, Chanda and Patra at the Central Inland Fisheries Research Institute. Its other reference remains marked unpublished. A manuscript title about salt-tolerant bacteria alone cannot establish a numerical growth limit or mechanism.

The exact Assembly search returned zero items and reported the taxid query phrase as not found. This is bounded to the exact NCBI concept, not proof that no genome exists elsewhere or under another classification. Datasets' dsDNA designation is not an assembly accession.

The Behera et al. primary paper, [DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), was inspected through its [author-uploaded text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis). Table 2 connects CH-TSB-27-TSA, 1,439 bases and JF784044, with Vibrio parahaemolyticus as the nearest-strain comparison and 100.00 alignment identity. Table 1 associates that designation with Chandipur soil. The separate CH-TSB-27 entry has JF784041 and a Staphylococcus aureus comparison; its water origin must not be transferred to this target. The accession resolves the designation difference. Neither the partial-marker comparison nor the paper's naming establishes a current NCBI reclassification. No numerical salt-growth limit is inferred from extraction-corrupted symbols.

Muh. Aris's [2011 IPB dissertation](https://www.marineagronomy.org/sites/default/files/IDENTIFIKASI,%20PATOGENISITAS%20BAKTERI%20DAN%20PEMANFAATAN%20GEN%2016S-rRNA%20UNTUK%20DETEKSI%20PENYAKIT%20ICE-ICE%20PADA%20BUDIDAYA%20RUMPUT%20LAUT%20%28Kappaphycus%20alvarezii%29.pdf) was checked through its title page, abstract and Appendix 16. PDF pages 142-144 were rendered and visually inspected. The appendix identifies PNGK 1 as the query isolate and lists JF784044.1/CIFRI CH-TSB-27 among database hits. The displayed 99% column is query coverage, not an identity estimate. The dissertation's seaweed and disease experiments cannot be assigned to this CIFRI taxon merely because its sequence is a comparison hit.

The [publisher abstract for Lan et al. (2020)](https://yykxjz.ijournals.cn/yykxjz/article/abstract/20190128001?st=search), DOI 10.19663/j.issn2095-9869.20190128001, was inspected and describes a distinct flatfish-isolate cohort. Search snippets suggest JF784044 occurs in its GenBank comparison column, but the full table could not be retrieved. That remains an unverified literature lead, not evidence of a host, virulence or identity claim for this target.

## Completeness

Initial `rg --no-ignore --hidden -n -z` searches covered taxid, full label/slug and CIFRI CH-TSB-27/CH-TSB27/TSB27 variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored and compressed files were included.

All seventeen candidate rows were read in full: three TSV rows and fourteen native JSONL rows. Lossless common-field reconstruction and exact address reconciliation were checked. Expanded searches for JF784044, nucleotide UID 333973504, CH-TSB-27-TSA and both inspected DOIs returned no matches in those roots. All five SOURCE.json files were separately fully traversed for the initial and final expanded patterns, with no hit. Ignored-inclusive filename searches found no prior report for this exact record or target history artifact before writing this report.

All seven other imported taxon evidence tables have no exact target row, and the backbone has no direct children. Zero BacDive strains and empty nomenclature/mapping/genome fields agree with the checked inputs. No eligible culture-deposit identity chain or target assembly was established.

Record-level literature enrichment is optional for this seeded record. Phenotype, medium and habitat details need the appropriate sibling-model scope and claim-specific evidence. iModulonDB is inapplicable because this YAML names no functional gene, regulator, pathway or expression module.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's identity, provenance, lineage, counts or status. The inaccessible literature table does not contradict a claim made by this seeded record.

## Recommended Edits

None required. Do not hand-edit this generated YAML, infer V. parahaemolyticus identity from a partial-marker comparison, count JF784044.1 as a genome or transfer PNGK 1's experiments to this taxon.

Any later authority-supported identity correction belongs in the pinned inventory/extraction pipeline. Representation changes belong in `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, followed by validated regeneration. Literature enrichment needs a supported maintained input and explicit claim scope.

## Follow-up Checks

For a source refresh, recheck taxon 1035178, its complete parent chain and JF784044.1. Before using the flatfish paper, obtain and inspect its complete Table 1 and distinguish study accessions from GenBank comparison sequences. Before adding salt-growth claims elsewhere, visually check the original table symbols and concentration columns against the methods.

Run both focused validators on a regenerated record and corpus reproduction/full QC before release. Any future genome association requires explicit provenance and an eligible strain identity chain.

## Additional Notes

False candidate matches concern Bacteroides uniformis AM100_PB_TSB_27, GCA/GCF_027661385.1; Mycobacterium tuberculosis ERR1035178, with ATB ERZ3502365/SAMEA3558711; Collinsella aerofaciens SAMN41035178, GCA/GCF_040926265.1; Campylobacter jejuni GCA_010351785.1; and unrelated genomes whose length is 1035178 bases, GCA_902511385.1 and GCA_947589105.1. Their GTDB mappings and genome links are not target attestations.

The dissertation's text extraction omitted the relevant rasterized table. Browser screenshots failed or did not provide an inspectable image; a public download and macOS PDFKit rendering succeeded. A generic virtualization warning did not prevent readable images. The flatfish CDN hostname failed to resolve, an alternate PDF endpoint returned HTTP 429, publisher full-text links failed, and the whole-issue PDF exceeded the web tool's size limit. Those failures were not treated as proof of source absence.

The earlier CIFRI paper was inspected as extracted text only. No independent sequence alignment, phylogram interpretation, experimental replication assessment or release-wide certification was performed. Only this new report was written in the repository for this target; PDF inspection files were temporary and outside the repository. No YAML, source, code, generated page, history, status or older report was changed. Eukaryotic reviews were not reopened.
