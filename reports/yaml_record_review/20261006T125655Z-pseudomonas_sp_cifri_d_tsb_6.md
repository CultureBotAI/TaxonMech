# YAML Record Review: Pseudomonas sp. CIFRI D-TSB-6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_cifri_d_tsb_6.yaml`
- Started UTC: 2026-10-06T12:54:15Z
- Finished UTC: 2026-10-06T12:56:55Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035172`, Pseudomonas sp. CIFRI D-TSB-6. It has SPECIES rank, BACTERIA domain, parent 196821, ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, external taxonomy mappings, genome links, phenotype assertions or causal graphs are present.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_cifri_d_tsb_6.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_cifri_d_tsb_6.yaml --out /private/tmp/pdtsb6-validation.tsv`: passed, one file and zero errors. The TSV was read and contains only its header.
- Structured comparisons inspected the complete backbone row, ancestors, seven other imported taxon tables, PATHS/scope, synonyms, attestation and seed event.
- Exact-ID reads found no target entry in the type-material, merged-ID or dropped tables.
- Live NCBI Taxonomy XML, Datasets, exact non-descendant Assembly/Nuccore searches and complete marker metadata were inspected.
- `just validate-products` is inapplicable because no curator-added graph nodes are present. No undocumented focused term/reference validator was invented.
- Ignored-inclusive history filename and content searches found no target artifact. The inline seed event was checked; no history validator was run against a nonexistent target file.
- Full-corpus reproduction, validation, tests, history validation, provenance/site checks and `just qc` were not run. Focused checks are not corpus-wide certification.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221901` supports the exact label, rank, parent, genetic code, empty synonyms and NCBI-only provenance. The native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31341`. `data/taxa/PATHS.tsv:14392` resolves this file, and `curation/seed_scope.tsv:322188` supplies its 2026-09-13 NCBI-only scope rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035172&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035172) agree on the species-level concept and all ten ancestor IDs: 1, 131567, 2, 3379134, 1224, 1236, 72274, 135621, 286 and 196821. The immediate parent is unclassified Pseudomonas, NO_RANK. All ancestor labels and ranks agree with the backbone.

The provisional source label is not a validly published binomial. A strain qualifier in nucleotide metadata does not justify changing NCBI's SPECIES rank to STRAIN. EXACT grounding means agreement with the NCBI concept, not independent validation of a species boundary or experimental trait.

## Evidence

The NCBITAXON attestation counts one NAME from snapshot 2026-09-13. The 2026-09-13T17:54:04Z SEEDED_FROM_SOURCES event by seed_from_sources agrees with the inventory and scope rationale. It does not claim human-reviewed status.

The exact Nuccore search returned only UID 333973481. Complete [JF784021.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF784021.1) identify Pseudomonas sp. CIFRI D-TSB-6, strain CIFRI D-TSB-6 and taxon 1035172. It is a 1,422-base partial 16S rRNA gene, partial at both ends, not a genome assembly. Source qualifiers describe marine water from Digha, India, collected by Bijay Kumar Behera. This is isolate-specific submission context, not a genus-wide habitat assertion.

The sequence record was created and updated on 30 May 2011. Its direct submission is dated 5 April 2011 and names Behera, Sharma, Das, Chanda and Patra at the Central Inland Fisheries Research Institute. Its other reference is marked unpublished; a salt-tolerant-bacteria study title alone cannot establish a quantitative phenotype.

The exact Assembly search returned zero items and reported the taxid query phrase as not found. This is bounded to the exact NCBI concept, not proof that no genome exists elsewhere or under another classification. Datasets' dsDNA designation does not identify an assembly.

The later Behera et al. primary paper, [DOI 10.1007/s40011-014-0440-6](https://link.springer.com/article/10.1007/s40011-014-0440-6), was inspected through its publicly accessible [author-uploaded text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis). Table 2 explicitly connects D-TSB-6, 1,422 bases and JF784021; its nearest-strain comparison names Pseudomonas aeruginosa with 99.86 alignment identity. Table 1 identifies Digha water as the isolation context. The relevant methods describe isolate screening and partial-marker comparisons.

The paper's sequence-based association with P. aeruginosa and NCBI's unclassified Pseudomonas placement differ in resolution. Retain that distinction: this paper does not establish a current taxonomic merge or authorize rewriting the carried lineage. No numerical salt-growth limit is asserted from extraction-corrupted table symbols.

## Completeness

Initial `rg --no-ignore --hidden -n -z` searches covered taxid, full label/slug and CIFRI D-TSB-6/D-TSB-6/TSB6 variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored and compressed files were included.

All 66 candidate rows were read in full: 17 TSV rows and 49 native JSONL rows. Lossless common-field reconstruction and exact address reconciliation were checked. Expanded searches for JF784021, nucleotide UID 333973481 and DOI 10.1007/s40011-014-0440-6 returned no matches in those roots. All five SOURCE.json files were separately fully traversed for both patterns, with no hit. No target report or history filename was found before writing this report.

All seven other imported taxon evidence tables have no exact target row, and the backbone has no direct children. Zero BacDive strains and empty nomenclature/mapping/genome fields agree with the checked inputs. No eligible culture-deposit identity chain was established by the marker or the candidate rows.

An important near-match is P. aeruginosa TSB 6, GCA/GCF_001375255.1, in BV-BRC, GTDB and NCBI assembly catalogs. Full [SAMEA3296572 metadata](https://www.ebi.ac.uk/biosamples/samples/SAMEA3296572) identify sample RW73, isolate TSB 6, Cardiff University and an industrial-isolate whole-genome project, with SRA sample ERS679811. They do not name CIFRI D-TSB-6 or JF784021. Shared name fragments and a species suggested by the marker paper are insufficient to join these records. The checked evidence supplies no target assembly link; no claim of demonstrated genome equivalence is made.

Optional literature enrichment is not a required representation. Experimental phenotype, medium and habitat details belong in the appropriate sibling models, with their own evidence. iModulonDB is inapplicable because this YAML names no functional gene, regulator, pathway or expression module.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed identity, provenance, lineage, counts or status. A same-fragment genome candidate without an identity chain is not a demonstrated missing link.

## Recommended Edits

None required. Do not hand-edit this generated YAML, infer P. aeruginosa identity from the partial-marker comparison, count JF784021.1 as a genome, or join the Cardiff TSB 6 assembly by its abbreviated designation.

Any later NCBI identity refresh belongs in the pinned inventory/extraction pipeline. Representation changes belong in `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, followed by validated regeneration. Literature enrichment needs a supported maintained input and claim-specific evidence.

## Follow-up Checks

For a source refresh, recheck taxon 1035172, its complete parent chain and JF784021.1. Any future assembly association requires an explicit source-supported strain identity chain. Before adding salt-growth claims elsewhere, inspect the original table visually and reconcile its symbols and concentrations with the methods.

Run both focused validators on a regenerated record and corpus reproduction/full QC before release.

## Additional Notes

Other candidates concern Anoxybacillus sp. TSB-6 (413100), Staphylococcus sp. CIFRI H-TSB-6-HA (1036323), Pseudomonas groundwater isolates GW456-12-1-14-TSB6 (2751350), GW456-12-10-14-TSB6 (2751351), GW460-12-1-14-TSB6 (2751362), and Sphingomonadaceae bacterium GW460-11-11-14-TSB6 (3693101). Their GOLD, BV-BRC, GTDB, NCBI and ATB entries retain distinct full designations and identifiers; they are not evidence for this CIFRI marine-water isolate.

Numeric false positives include Clostridium tertium with SAMN41035172 and GCA/GCF_040926365.1, Mycobacterium tuberculosis run ERR1035172, and Campylobacter jejuni assembly GCA_010351725.1. No evidence or counts were transferred from these rows.

The BioSamples browser request failed, but the public JSON endpoint was successfully read in full. The primary paper was inspected as extracted text, not a rendered PDF; no phylogram inference, independent sequence analysis, experimental replication assessment or release-wide certification was performed.

Only this new report was written for this target. No YAML, source, code, generated page, history, status or older report was changed. Eukaryotic reviews were not reopened.
