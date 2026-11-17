# YAML Record Review: bromate-reducing bacterium WC21

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bromate_reducing_bacterium_wc21.yaml`
- Started UTC: 2026-10-06T12:41:50Z
- Finished UTC: 2026-10-06T12:43:42Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035158`, bromate-reducing bacterium WC21. It has SPECIES rank, BACTERIA domain, parent 49928, four root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. It asserts no synonym, external nomenclature/mapping, genome link, causal graph or explicit phenotype beyond carrying the source's descriptive label.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bromate_reducing_bacterium_wc21.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/bromate_reducing_bacterium_wc21.yaml --out /private/tmp/wc21-validation.tsv`: passed, one file and zero errors. The TSV was read and contains only its header.
- Structured comparisons inspected the full backbone row, ancestor chain, seven other imported taxon tables, PATHS/scope, synonyms, attestation and seed provenance.
- Exact-ID reads found no target entry in the type-material, merged-ID or dropped tables.
- Live NCBI Taxonomy XML, Datasets, exact non-descendant Assembly/Nuccore searches, complete marker metadata and the primary publication's complete PubMed abstract were read.
- `just validate-products` is inapplicable because there are no curator-added graph nodes. No undocumented focused term/reference validator was invented.
- Ignored-inclusive history content and filename searches found no separate target artifact. The inline seed event was checked; no history validator was run against a nonexistent file.
- Full-corpus reproduction, validation, tests, history validation, provenance/site checks and `just qc` were not run. Focused checks are not corpus-wide certification.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221898` supports the exact descriptive label, species rank, parent, genetic code, empty synonyms and NCBI-only provenance. `data/catalog/ncbi_names-0005.jsonl.gz:31338` is the complete native scientific-name row. `data/taxa/PATHS.tsv:14389` resolves the file, and `curation/seed_scope.tsv:322185` supplies its 2026-09-13 scope rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035158&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035158) agree with the record's identity and four ancestors: root 1, cellular organisms 131567, Bacteria 2 and unclassified Bacteria 49928. The final ancestor is NO_RANK. The short lineage is NCBI's source placement, not a missing TaxonMech inference.

SPECIES is the NCBI rank of this provisional concept, not proof of a validly published binomial. EXACT grounding denotes agreement with that concept, not independent demonstration of a reduction mechanism. No closer genus or species assignment is justified by the inspected record evidence.

## Evidence

The NCBITAXON attestation counts one NAME from snapshot 2026-09-13. The seed event at 2026-09-13T17:54:04Z by seed_from_sources matches the inventory and scope rationale. It does not claim human-reviewed status.

The exact Nuccore search returned only UID 333697131. Complete [JN002283.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JN002283.1) identify this taxid, strain WC21 and Waller Creek water as the source. This is a 1,303-base partial 16S rRNA gene with both ends partial, not an assembly. The source reports create/update dates of 25 June 2012 and a direct submission dated 16 May 2011. A submitter comment reports chimera screening with Pintail; this review did not independently repeat that analysis.

The nucleotide reference explicitly cites [PMID 21943884](https://pubmed.ncbi.nlm.nih.gov/21943884/) and DOI 10.1016/j.watres.2011.09.001. The inspected PubMed metadata confirm Davidson, Chee-Sanford, Lai, Ho, Klenzendorf and Kirisits, Water Research 45(18):6051-6062, published 15 November 2011 with an earlier online date. Thus the marker-to-publication link is explicit, not inferred from a similar paper title.

The complete abstract describes fifteen bromate-reducing isolates spanning several broad taxonomic groups. It discusses unresolved mechanisms and subset-level experiments; it does not identify WC21 as belonging to a particular mechanistic subset. Those results cannot be promoted into a WC21-specific pathway or into a lineage change. The source label can be retained without treating every abstract observation as a claim made by this YAML.

The exact Assembly search returned zero items and reported the taxid query phrase as not found. This bounds what was found at NCBI under the exact taxid; it does not prove that no genome exists under another classification or elsewhere.

## Completeness

Initial `rg --no-ignore --hidden -n -z` searches covered the taxid, label/slug and WC21/WC_21/WC-21 variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored and compressed files were included.

All seventeen candidate rows were read in full: three TSV rows and fourteen native JSONL rows. Lossless common-field reconstruction and exact address reconciliation were checked. Expanded searches for JN002283, nucleotide UID 333697131, PMID 21943884 and DOI 10.1016/j.watres.2011.09.001 returned no matches in those roots. The five SOURCE.json files were separately fully traversed for the identity pattern with no hit. No target report or history filename was found before writing this report.

All seven other imported taxon evidence tables have no exact target row, and the backbone has no direct children. Zero BacDive strains and absent culture-deposit/genome links therefore match the checked inputs. The marker does not establish a genome identifier or an eligible deposit join.

The descriptive name is not a functional gene, locus, regulator or expression-module assertion. No covered organism/dataset identity for an iModulonDB query was established for this unclassified concept, so iModulonDB was not applicable to the identity review. No mechanistic conclusion was based on its absence.

No material missing representation was established. Optional literature, phenotype or graph enrichment needs appropriately scoped evidence and a maintained input; it is not required to make this seeded identity record complete.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed identity, lineage, counts, provenance or status. The unclassified placement and uninspected full experimental paper are explicit limits, not demonstrated record defects.

## Recommended Edits

None required. Do not hand-edit the generated YAML, infer a higher-resolution lineage, count JN002283.1 as a genome, or import cohort-level mechanism claims without WC21-specific evidence.

Any later upstream taxonomy refresh belongs in the pinned inventory/extraction pipeline. Representation changes belong in `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, followed by validated regeneration. A future strain-genome association needs an explicit supported identity chain.

## Follow-up Checks

For a source refresh, recheck taxon 1035158, parent 49928 and JN002283.1. Read the full paper and relevant WC21-specific results before importing any mechanism, phenotype or refined biological placement.

Run both focused validators on any regenerated record and corpus reproduction/full QC before release. Preserve the distinction between source classification and experimental interpretation.

## Additional Notes

The similarly named WC_21 genome is Candidatus Peribacterales bacterium, taxid 2711152, GCA_020058865.1, BioSample SAMN18076683 and WGS JAGVDG000000000.1. Its native NCBI entry is metagenome-derived and fragmented, and its several BV-BRC versions do not identify the Waller Creek WC21 marker. A designation-only match would be erroneous.

Numeric near-matches include Butyricimonas virosa with SAMN41035158 and GCA/GCF_040926625.1, Mycobacterium tuberculosis run ERR1035158, Campylobacter jejuni assembly GCA_010351585.1, and a Verrucomicrobiota MAG whose contig N50 is 1,035,158. None is target identity evidence.

The DOI resolver page was inaccessible through the browser tool; the DOI and bibliographic identity were nevertheless verified in NCBI's nucleotide reference and PubMed. Full experimental text, independent sequence analysis and release-wide certification were not performed.

Only this new report was written for this target. No YAML, source, code, generated page, history, status or older report was changed. Eukaryotic reviews were not reopened.
