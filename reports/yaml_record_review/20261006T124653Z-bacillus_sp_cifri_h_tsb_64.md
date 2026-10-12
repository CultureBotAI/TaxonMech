# YAML Record Review: Bacillus sp. CIFRI H-TSB-64

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_cifri_h_tsb_64.yaml`
- Started UTC: 2026-10-06T12:44:39Z
- Finished UTC: 2026-10-06T12:46:53Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035170`, Bacillus sp. CIFRI H-TSB-64. It has SPECIES rank, BACTERIA domain, parent 185979, ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. There are no synonyms, nomenclature entries, external taxonomy mappings, genome links, phenotype assertions or causal graphs.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bacillus_sp_cifri_h_tsb_64.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/bacillus_sp_cifri_h_tsb_64.yaml --out /private/tmp/cifri64-validation.tsv`: passed, one file and zero errors. The TSV was read and contains only its header.
- Structured comparisons inspected the full backbone row, ancestor chain, seven other imported taxon tables, PATHS/scope, synonyms, attestation and seed provenance.
- Exact-ID reads found no target entry in the type-material, merged-ID or dropped tables.
- Live NCBI Taxonomy XML, Datasets, exact non-descendant Assembly/Nuccore searches and complete marker metadata were inspected.
- `just validate-products` is inapplicable because no curator-added graph nodes are present. No undocumented focused term/reference validator was invented.
- Ignored-inclusive history filename and content searches found no target artifact. The inline seed event was checked; no history validator was run against a nonexistent target file.
- Full-corpus reproduction, validation, tests, history validation, provenance/site checks and `just qc` were not run. Focused checks are not corpus-wide certification.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221899` supports the exact label, rank, parent, genetic code, empty synonyms and NCBI-only provenance. The native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31339`. `data/taxa/PATHS.tsv:14390` resolves this file, and `curation/seed_scope.tsv:322186` supplies its 2026-09-13 NCBI-only scope rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035170&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035170) agree on this species-level concept and its ten ancestors: 1, 131567, 2, 1783272, 1239, 91061, 1385, 186817, 1386 and 185979. The immediate parent is unclassified Bacillus (in: firmicutes), NO_RANK.

The provisional source label is not a validly published binomial. Its occurrence as a strain designation in nucleotide metadata does not justify changing NCBI's SPECIES rank to STRAIN. EXACT grounding means agreement with the NCBI concept, not independent validation of a species boundary, salt-tolerance phenotype or genome identity.

## Evidence

The NCBITAXON attestation counts one NAME from snapshot 2026-09-13. The 2026-09-13T17:54:04Z SEEDED_FROM_SOURCES event by seed_from_sources agrees with the inventory and scope rationale. It does not claim human-reviewed status.

The exact Nuccore search returned only UID 333973477. Complete [JF784017.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF784017.1) identify Bacillus sp. CIFRI H-TSB-64, strain CIFRI H-TSB-64 and taxon 1035170. It is a 933-base partial 16S rRNA gene, partial at both ends, not a genome assembly. The source qualifiers describe marine water from Haldia, India. This is isolate-specific submission context, not a broader Bacillus habitat claim.

The sequence record was created and updated on 30 May 2011. Its direct submission is dated 5 April 2011 and names Behera, Sharma, Das, Chanda and Patra at the Central Inland Fisheries Research Institute. Its other reference is marked unpublished and concerns identification of salt-tolerant bacteria from India's east coast. A manuscript title alone cannot validate a quantitative salt-tolerance claim.

The exact Assembly search returned zero items and reported the taxid query phrase as not found. This is a bounded search under the exact NCBI concept, not proof that no genome exists elsewhere or under another classification.

Literature searching found a related [2014-online/2015-issue primary paper](https://link.springer.com/article/10.1007/s40011-014-0440-6), DOI 10.1007/s40011-014-0440-6. Its publisher abstract and bibliographic metadata were inspected, but the full article requires subscription access. The inspected abstract describes an isolate cohort and does not identify this taxid, accession or full strain designation.

A related [2019 primary paper abstract](https://pubmed.ncbi.nlm.nih.gov/31245639/), PMID 31245639 and DOI 10.1016/j.heliyon.2019.e01869, was likewise inspected. It does not establish that its reported selected-isolate results apply to CIFRI H-TSB-64. Similar authors, locality and study topic are insufficient identity evidence. Neither optional lead was treated as a verified replacement for the marker's unpublished citation.

## Completeness

Initial `rg --no-ignore --hidden -n -z` searches covered the taxid, full label/slug and CIFRI H-TSB-64/H-TSB-64/TSB-64 variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored and compressed files were included.

All thirteen candidate rows were read in full: three TSV rows and ten native JSONL rows. Lossless common-field reconstruction and exact address reconciliation were checked. Expanded searches for JF784017 and nucleotide UID 333973477 returned no matches in those roots. The five SOURCE.json files were separately fully traversed for the identity pattern, with no hit. No target report or history filename was found before writing this report.

All seven other imported taxon evidence tables have no exact target row, and the backbone has no direct children. Zero BacDive strains and empty external nomenclature/mapping/genome fields agree with the checked inputs. The marker supplies no culture-deposit identity or genome assembly, and numeric near-matches do not establish missing associations.

Optional literature and phenotype enrichment may be useful only after the isolate identity and relevant experimental evidence are verified. Their absence is not a mandatory missing representation. iModulonDB is inapplicable because this YAML names no functional gene, regulator, pathway or expression module; an unrelated transcriptomics paper does not create such an assertion here.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed identity, source provenance, lineage, counts or status. Unconfirmed literature leads and unrun full-corpus gates are limitations, not demonstrated YAML errors.

## Recommended Edits

None required. Do not hand-edit this generated YAML, infer a named Bacillus species, count JF784017.1 as a genome, or promote an unpublished study title into a phenotype assertion.

Any later NCBI identity refresh belongs in the pinned inventory/extraction pipeline. Representation changes belong in `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, followed by validated regeneration. Literature enrichment needs a supported maintained input and claim-specific evidence.

## Follow-up Checks

For a source refresh, recheck taxon 1035170, its complete parent chain and JF784017.1. Before importing a result from a later CIFRI study, establish an explicit accession or full-designation match and inspect the relevant isolate-specific results.

Run both focused validators on a regenerated record and corpus reproduction/full QC before release. A future genome link requires explicit provenance and an eligible strain identity chain.

## Additional Notes

The candidate reads distinguish this taxon from [Clostridium] symbiosum with SAMN41035170 and GCA/GCF_040926465.1, Mycobacterium tuberculosis run ERR1035170, Campylobacter jejuni assembly GCA_010351705.1, and Corallococcus terminator CA054A with a genome length of 10,351,705 bases. The Corallococcus type-material and reference-genome annotations concern that organism, not CIFRI H-TSB-64.

The 2015 paper was available only as a publisher preview. PMC requests for the 2019 paper and a related Staphylococcus P-TSB-70 transcriptomics lead returned browser verification pages; their full texts were not inspected. The 2011 conference abstract-book search result remained a lead and supplied no finding. No independent sequence analysis, experimental replication assessment or release-wide certification was performed.

Only this new report was written for this target. No YAML, source, code, generated page, history, status or older report was changed. Eukaryotic reviews were not reopened.
