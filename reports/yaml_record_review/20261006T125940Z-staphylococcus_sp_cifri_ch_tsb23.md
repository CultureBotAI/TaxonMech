# YAML Record Review: Staphylococcus sp. CIFRI CH-TSB23

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_cifri_ch_tsb23.yaml`
- Started UTC: 2026-10-06T12:57:55Z
- Finished UTC: 2026-10-06T12:59:40Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035174`, Staphylococcus sp. CIFRI CH-TSB23. It has SPECIES rank, BACTERIA domain, parent 91994, ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, external taxonomy mappings, genome links, phenotype assertions or causal graphs are present.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_sp_cifri_ch_tsb23.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_sp_cifri_ch_tsb23.yaml --out /private/tmp/sch23-validation.tsv`: passed, one file and zero errors. The TSV was read and contains only its header.
- Structured comparisons inspected the complete backbone row, ancestor chain, seven other imported taxon tables, PATHS/scope, synonyms, attestation and seed event.
- Exact-ID reads found no target entry in the type-material, merged-ID or dropped tables.
- Live NCBI Taxonomy XML, Datasets, exact non-descendant Assembly/Nuccore searches and complete marker metadata were inspected.
- `just validate-products` is inapplicable because no curator-added graph nodes are present. No undocumented focused term/reference validator was invented.
- Ignored-inclusive history filename and content searches found no target artifact. The inline seed event was checked; no history validator was run against a nonexistent target file.
- Full-corpus reproduction, validation, tests, history validation, provenance/site checks and `just qc` were not run. Focused checks are not corpus-wide certification.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221902` supports the exact label, rank, parent, genetic code, empty synonyms and NCBI-only provenance. The native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31342`. `data/taxa/PATHS.tsv:14393` resolves this file, and `curation/seed_scope.tsv:322189` supplies its 2026-09-13 NCBI-only scope rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035174&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035174) agree on the species-level concept and all ten ancestor IDs: 1, 131567, 2, 1783272, 1239, 91061, 1385, 90964, 1279 and 91994. The immediate parent is unclassified Staphylococcus, NO_RANK. All ancestor labels and ranks agree with the backbone.

The provisional source label is not a validly published binomial. A strain qualifier in nucleotide metadata does not justify changing NCBI's SPECIES rank to STRAIN. EXACT grounding means agreement with this NCBI concept, not independent validation of a named Staphylococcus species or salt-tolerance phenotype.

## Evidence

The NCBITAXON attestation counts one NAME from snapshot 2026-09-13. The 2026-09-13T17:54:04Z SEEDED_FROM_SOURCES event by seed_from_sources agrees with the inventory and scope rationale. It does not claim human-reviewed status.

The exact Nuccore search returned only UID 333973507. Complete [JF784047.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF784047.1) identify Staphylococcus sp. CIFRI CH-TSB23, strain CIFRI CH-TSB23 and taxon 1035174. It is a 1,441-base partial 16S rRNA gene, partial at both ends, not a genome assembly. Source qualifiers describe marine soil sediment from Chandipur, India, collected by Bijay Kumar Behera. These are isolate-specific submission details, not a broader Staphylococcus habitat claim.

The marker was created and updated on 30 May 2011. Its direct submission is dated 5 April 2011 and names Behera, Sharma, Sahoo, Das, Chanda and Patra at the Central Inland Fisheries Research Institute. Its other reference is marked unpublished and concerns identification of salt-tolerant bacteria from India's east coast. The title alone cannot establish a measured salt-growth limit or mechanism.

The exact Assembly search returned zero items and reported the taxid query phrase as not found. This is bounded to the exact NCBI concept, not proof that no genome exists elsewhere or under another classification. Datasets' dsDNA designation is not an assembly accession.

The related Behera et al. primary paper, [DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), was examined through its [author-uploaded text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis). The inspected isolate tables list other Chandipur designations, but do not establish CH-TSB23 or JF784047 as one of their isolates. Searches within the extracted text for JF784047, TSB23 and TSB-23 found no match. This is a bounded text/table check, not proof of absence from every supplementary or unpublished source. Shared authors, institution and locality are insufficient to transfer another isolate's species assignment or phenotype. The paper remains an unconfirmed optional lead for this target.

## Completeness

Initial `rg --no-ignore --hidden -n -z` searches covered taxid, full label/slug and CIFRI CH-TSB23/CH-TSB-23/TSB23 variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored and compressed files were included.

All nine candidate rows were read in full: three TSV rows and six native JSONL rows. Lossless common-field reconstruction and exact address reconciliation were checked. Expanded searches for JF784047, nucleotide UID 333973507 and DOI 10.1007/s40011-014-0440-6 returned no matches in those roots. All five SOURCE.json files were separately fully traversed for both patterns, with no hit. No target report or history filename was found before writing this report.

All seven other imported taxon evidence tables have no exact target row, and the backbone has no direct children. Zero BacDive strains and empty nomenclature/mapping/genome fields agree with the checked inputs. No eligible culture-deposit identity chain or target assembly was established.

Record-level literature evidence is optional for this seeded record. An unpublished marker reference is not a mandatory missing representation when the YAML makes no experimental claim. Phenotype, medium and habitat enrichment requires appropriate sibling-model scope and evidence. iModulonDB is inapplicable because this YAML names no functional gene, regulator, pathway or expression module.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed identity, provenance, lineage, counts or status. Unconfirmed literature leads and unrun full-corpus gates are limitations, not demonstrated YAML errors.

## Recommended Edits

None required. Do not hand-edit this generated YAML, infer a named Staphylococcus species from neighboring isolates, count JF784047.1 as a genome, or turn a manuscript title into phenotype evidence.

Any later NCBI identity refresh belongs in the pinned inventory/extraction pipeline. Representation changes belong in `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, followed by validated regeneration. Optional literature enrichment needs a supported maintained input and an explicit accession or full-designation match.

## Follow-up Checks

For a source refresh, recheck taxon 1035174, its complete parent chain and JF784047.1. Before importing results from a CIFRI publication, establish the target's identity in the primary text and inspect the relevant isolate-specific evidence.

Run both focused validators on a regenerated record and corpus reproduction/full QC before release. Any future genome association requires explicit provenance and an eligible strain identity chain.

## Additional Notes

Numeric candidate matches concern Mycobacterium tuberculosis run ERR1035174 and Collinsella aerofaciens with SAMN41035174 and GCA/GCF_040926305.1. The latter's GTDB classification as Collinsella sp937965595 belongs to that assembly; neither that mapping nor the ATB tuberculosis assembly supplies evidence for CIFRI CH-TSB23.

The related paper was inspected as extracted primary text, not a rendered PDF. No supplementary-material census, independent sequence analysis, experimental replication assessment or release-wide certification was performed. Broad web searches are discovery checks, not exhaustive evidence that no publication exists.

Only this new report was written for this target. No YAML, source, code, generated page, history, status or older report was changed. Eukaryotic reviews were not reopened.
