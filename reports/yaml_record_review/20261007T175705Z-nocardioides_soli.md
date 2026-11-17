# YAML Record Review: Nocardioides soli

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardioides_soli.yaml`
- Started UTC: 2026-10-07T17:40:56Z
- Finished UTC: 2026-10-07T17:57:05Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1036020`, Nocardioides soli, rank `SPECIES`, domain `BACTERIA`, mapping status `EXACT`, curation status `SEEDED`. The entire YAML was read. Its single strain is mbc-2 (`kgmicrobe.strain:bacdive_140067`), with four culture deposits, ten assembly assertions, seven genome-record assertions and 26 related-record assertions. These are source relationships, not 43 distinct genomes.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/nocardioides_soli.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/nocardioides_soli.yaml --out /private/tmp/nsol-strict.tsv`: exit 0; one file, zero error rows. The diagnostic TSV contains only its header.
- Structured read-only comparisons confirmed backbone, nomenclature, mapping and source-count values against complete raw rows. All nine raw assembly, seven raw genome and 24 raw related-record assertions match the YAML field for field. The StrainInfo assembly and two related-record assertions match their overlay rows, including decoded nested evidence.
- Every deposit-based match passes the repository's CAFI full-accession normalization. The StrainInfo assembly names the same deposit as its strain match.
- Source-status checks found the active taxon and nine type-material spellings, with no matching merged/deleted status. Ignored files and compressed source projections were included.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-products`, render/docs checks and tests. Manual source comparisons are not replacements for these gates. No graph grounding or standalone history entry was present in the bounded ignored-inclusive searches, so graph term checks and standalone history validation have no target here. No focused substitute validator was invented.

## Identity and Grounding

NCBI Taxonomy EFetch confirms the exact species identity, parent `NCBITaxon:1839` Nocardioides, genetic code 11 and all nine root-first ancestors: root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Propionibacteriales, Nocardioidaceae and Nocardioides. The authority and former mbc-2 name are conservatively retained as `RELATED` synonyms. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036020).

The LPSN record is Sun et al. 2014, `lpsn:791880`, a legitimate, validly published correct name, with marker JF937914. This is not the homonymous Srinivasan et al. 2014 name: that name has type strain SR-1, JCM 19684/KEMC 9004-134, marker KF955611 and correct name Nocardioides montaniterrae. The YAML's authority, identifier and mbc-2 strain distinguish them. [Target LPSN record](https://lpsn.dsmz.de/species/nocardioides-soli), [homonym](https://lpsn.dsmz.de/species/nocardioides-soli-1).

`GTDB:s__Nocardioides_soli` is appropriately a `skos:closeMatch`, not exact species equivalence. The pinned GTDB catalog contains two members: representative DSM 105498 (`RS_GCF_014191495.1`) and LMS-CY (`RS_GCF_018732145.1`, NCBI taxon 2840457). The raw mapping and species inventory both count two. The public GTDB tree rendered only its loading interface, so this is snapshot verification, not a newly retrieved live count. [GTDB tree](https://gtdb.ecogenomic.org/tree?r=s__Nocardioides+soli).

## Evidence

- `data/raw/lpsn_names.tsv:28672` supports the nomenclature fields, two DOI references, PMID and sequence accession. The original publisher abstract and PubMed entry identify mbc-2 as the proposed species' type, with KACC 17152 and CCTCC AB 2012934. `PMID:24651303` resolves to `DOI:10.1099/ijs.0.057935-0`. The other DOI resolves to Oren and Garrity's September 2014 notification for volume 64 part 6. Publisher metadata and its general abstract were inspected, but the notification's individual-name table was not retrieved; LPSN supplies the target-specific association. [Original paper](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.057935-0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24651303/), [notification](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.068510-0).
- GenBank metadata for `JF937914.1` identifies a 1,485-base partial 16S rRNA sequence from mbc-2, taxon 1036020, with the original DOI/PMID and explicit type-material annotation. It is a marker, not an assembly. [GenBank](https://www.ncbi.nlm.nih.gov/nuccore/JF937914.1).
- BacDive 140067 and the directly fetched JCM 32088 catalog support mbc-2, all four deposits and type status. JCM records the KACC-to-JCM transfer and the same assembly accessions. The generated type flag traces to the intersection of the raw LPSN JCM-32088 designation and BacDive's deposit set. [BacDive](https://bacdive.dsmz.de/strain/140067), [JCM](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=32088).
- NCBI Datasets confirms current paired assemblies `GCA_014191495.1` and `GCF_014191495.1`, DSM 105498, assembly name ASM1419149v1, contig level, BioSample `SAMN12025574` and project `PRJNA546943`. BioSample independently gives DSM:105498, target species and type material. The YAML preserves unversioned accessions supplied by BacDive/StrainInfo and versioned accessions supplied by other sources. [Assembly](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_014191495.1/), [BioSample](https://www.ncbi.nlm.nih.gov/biosample/SAMN12025574).
- The inspected GOLD native chain is `Go0456191` -> `Gp0325188` -> `Ga0310458`, connecting DSM 105498 to the same assembly, sample/project and IMG `2824233761`. `Go0621432` and `Go0621433` separately name KACC 17152 and CCTCC AB 2012934. A fourth organism record, `Go0621431`, names mbc-2 without a collection accession; it supports the organism count but not a deposit join. GOLD public organism/analysis pages returned HTTP 403. Native snapshot objects and BacDive's independent IMG assertion were inspected; the IMG detail page was unavailable.
- The complete pinned BV-BRC object `1036020.3` supports the assembly, sample and project via both `strain=DSM 105498` and `culture_collection=DSM:105498`. These separate source-field assertions are intentional. The live BV-BRC API failed DNS resolution; current availability was not established.
- `PRJNA224116` resolves to NCBI's multispecies RefSeq annotation project, whereas `PRJNA546943` is the DSM 105498 sequencing project. Retaining both as source-qualified links is correct; the former is not an isolate-specific sequencing experiment. [RefSeq project](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA224116), [sequencing project](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA546943).
- Live StrainInfo API data agree with native `SI-ID402049`, DOI version `10.60712/SI-ID402049.3`, published-online status and available DSM 105498 deposit `SI-DP909025`. Its genome sequence explicitly names deposit 909025, matching the nested YAML evidence. No sequence was borrowed from an unrelated deposit. [StrainInfo API](https://api.straininfo.dsmz.de/v2/data/strain/max/402049).
- The six attestations preserve their units: NCBI one name, LPSN one name, GTDB two genomes, BacDive one strain, MediaDive three media and GOLD four organism records. A directly fetched MediaDive page confirms media 535, 92 and J26, matching `data/raw/mediadive_taxa.tsv:126`. Counts were not summed or interpreted as species-wide phenotype evidence. [MediaDive](https://mediadive.dsmz.de/taxonomy?item=Nocardioides+soli&level=species).

## Completeness

The record is complete enough for its seeded identity and strain-link scope. Live NCBI Datasets and the pinned Assembly catalog also contain DR6 assemblies `GCA_060053545.1`/`GCF_060053545.1` with BioSample `SAMN53301518`. DR6 is not a documented synonym of mbc-2 or one of its culture deposits and must not be attached to the listed strain. GTDB's LMS-CY member likewise contributes to the species-cluster count without becoming an mbc-2 genome link.

LPSN's public page lists CCTCC AB 2012934, KACC 17152 and mbc-2 in addition to JCM 32088. The frozen nomenclature projection contains only JCM-32088, but this designation is correct, the type flag is present and all culture deposits are retained in the strain. This is optional upstream enrichment, not a missing type strain or unsupported assertion. Expansion belongs to the KG-Microbe LPSN transform inputs consumed by `src/taxonmech/extract.py:420`, followed by normal extraction/seeding, not a direct YAML patch.

The ignored-inclusive compressed search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the taxon/name, mbc-2, deposits, marker, assembly/sample, GOLD, StrainInfo, IMG and citation identifiers. All 205 candidate rows/objects were read completely with lossless common-field grouping. Five source manifests and history filenames were checked separately. No additional target history or causal overlay was found within these roots. No target Madin/BactoTraits row was found in the inspected inventories; no absence across all literature is claimed.

The original study describes strain phenotypes, but the YAML makes no corresponding gene, mechanism, trait, MIC or transcriptomic claim. Optional graph/evidence/trait slots need not be invented. iModulonDB is not applicable to these identity and source-link assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record. Public-service access limits and optional enrichment are documented separately; neither establishes a broken stored reference.

## Recommended Edits

None required. Do not edit the generated YAML, promote its review status or append a curation event as part of this review. Optional enrichment should preserve source boundaries, supplied accession versions and full culture-accession matching.

## Follow-up Checks

On an authorized future source refresh, recheck the GTDB cluster and unavailable GOLD/BV-BRC/IMG public resources. Before adding DR6 or LMS-CY to any strain, obtain an explicit deposit relationship rather than matching a species label. For optional LPSN designation enrichment, fix the maintained upstream transform, run the documented inventory/seed workflow, validate the regenerated target, then run full provenance/corpus/QC gates.

## Additional Notes

- Reviewed at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; target bytes remained unchanged.
- The seed event timestamp `2026-09-13T17:54:04Z` agrees with the latest inspected source-manifest timestamp. Its source list and `SEEDED` status are consistent; no human review is implied.
- Counterexamples included the montaniterrae homonym, Pseudomonas MBC2/08XMBC-2 names, Campylobacter mbc2, pig metagenomes whose BioSample IDs contain the taxon digits, a Chlamydia genome with ungapped length 1036020, and an AllTheBacteria Bacteroides row whose run accession contains PMID digits. None was transferred to this record. The 70 LPSN hits largely share the notification DOI; they are not 70 identity matches.
- Direct fetching recovered JCM and MediaDive after web-fetch errors. DOI redirects and the notification full-text endpoint were unavailable; primary landing pages, PubMed, LPSN and marker metadata provided the bounded citation checks above.
- The other Codex session is closed. Existing branches/worktrees, source snapshots, records, lifecycle/history and GitHub state were left untouched. Only this new report was written for this target.
