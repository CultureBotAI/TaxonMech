# YAML Record Review: uncultured Treponema clone HsPySp1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_treponema_clone_hspysp1.yaml`
- Started UTC: 2026-10-07T18:14:45Z
- Finished UTC: 2026-10-07T18:25:12Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:103611`, label uncultured Treponema clone HsPySp1, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read. It contains ten ancestors, genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, zero inventoried strains and one NCBI name attestation. Its species rank is a taxonomy assignment, not evidence of formal nomenclature, a cultured strain or an assembled genome.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/uncultured_treponema_clone_hspysp1.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/uncultured_treponema_clone_hspysp1.yaml --out /private/tmp/hsp1-strict.tsv`: exit 0; one file, zero error rows; diagnostic TSV contains only its header.
- Complete source-row comparisons support identity, lineage, genetic code, source scope, attestation and path mapping. The pinned backbone has no descendants for the target. These manual comparisons do not replace corpus reproduction.
- Ignored-inclusive status checks found no target type-material, merged-ID or dropped-ID row.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, render/docs/vendored checks and tests. Bounded searches found no target causal graph or standalone history record, so graph term/label and standalone history validation have no target here. No substitute focused validator was invented.

## Identity and Grounding

Live NCBI Taxonomy EFetch and Datasets match the clone name, species rank and parent `NCBITaxon:77353` environmental samples. Genetic code 11 and the full pinned lineage agree: root, cellular organisms, Bacteria, Pseudomonadati, Spirochaetota, Spirochaetia, Treponematales, Treponemataceae, Treponema and environmental samples. Datasets includes the root; EFetch verifies the other ancestor identifiers, names and ranks. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103611), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103611).

The native name row contains the scientific name only. Empty synonym, nomenclature and mapping slots are consistent with the source. `EXACT` describes agreement with the NCBI concept; it does not assert a formally described species or equivalence to a nearby clone.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18513` supports the label, rank, parent, code, empty synonym fields and NCBI-only source scope. `data/catalog/ncbi_names-0000.jsonl.gz:38521` preserves the complete native scientific-name row.
- `data/taxa/PATHS.tsv:14758` uniquely connects the slug and taxon identifier. `curation/seed_scope.tsv:144159` records its 2026-09-13 attested-rule inclusion with one source.
- Exact-taxonomy Nucleotide search returned one sequence, UID 7209328. Complete non-sequence GenBank metadata identify `AB032003.1`, a 1,471-base partial 16S rRNA gene, clone HsPySp1, taxon 103611 and an environmental sample from host Hodotermopsis sjoestedti. The source note describes a PCR-amplified clone from an isolated protist. The direct submission is dated 29 August 1999; the record was created 29 February 2000 and updated 16 December 2008. No BioSample, BioProject, culture accession or assembly is supplied by that metadata. [GenBank](https://www.ncbi.nlm.nih.gov/nuccore/AB032003.1).
- GenBank cites Iida, Ohkuma, Ohtoko and Kudo's original study, `PMID:11053732`, `DOI:10.1111/j.1574-6941.2000.tb00750.x`. PubMed metadata/abstract and the publisher's abstract/methods were inspected. The study used micromanipulation, SSU-rDNA analysis and in situ hybridization to investigate uncultivated protist-associated spirochetes. Its cohort results are not automatically exact-clone phenotypes. [PubMed](https://pubmed.ncbi.nlm.nih.gov/11053732/), [original article](https://academic.oup.com/femsec/article/34/1/17/617207).
- Noda and colleagues' 2003 follow-up, `DOI:10.1128/AEM.69.1.625-633.2003`, explicitly discusses RsDiSp9 and HsPySp1 as related ectosymbiotic phylotypes associated with different protists and termite hosts. The inspected discussion supports distinguishing the clones, not treating them as synonyms. [Primary follow-up](https://journals.asm.org/doi/10.1128/AEM.69.1.625-633.2003).
- A public Yuki/Ohkuma poster was read and visually inspected. HsPySp1 is a separate terminal label in the Cluster IIB phylogeny, alongside HsPySp20 and Pyr2-C9. The genome table assigns its Cluster IIB genome to Pyr2-C9, not HsPySp1. This is a related-genome lead, not an explicit exact-clone assembly link; its metabolic predictions were not transferred to the YAML. [Research poster](https://www.ifo.or.jp/rc_pdf/yuki.pdf).
- Exact-taxonomy Assembly search returned zero items with phrase-not-found/no-items warnings. This reports that query's result, not universal absence of related genomes.
- The sole curation event agrees with the scope reason and NCBI label. Its `2026-09-13T17:54:04Z` timestamp equals the latest of the three extraction-manifest timestamps, consistent with `src/taxonmech/seed.py:139`. It records seeding, not completed human curation.

## Completeness

The exact-taxon BacDive inventory is empty and the pinned backbone has no descendants, supporting the zero inventoried-strain count. Exact source-row checks also found no target LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion in the pinned inventories. Optional culture, nomenclature, genome, phenotype, mapping and graph slots may remain empty. A clone's marker sequence is not an assembly or BacDive strain. Additional literature evidence is optional for this explicitly sourced seeded record.

The gitignore-independent search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It searched the digit-bounded taxon number and clone spelling, then expanded to AB032003, PMID 11053732 and the two inspected article DOIs. All 38 resulting rows/objects were read completely using lossless common-field grouping. Five source manifests were parsed separately; history filenames were also checked independently. No exact-target culture/genome association, additional curation overlay or standalone history record was found within those roots. These are bounded inventory findings, not a claim that all literature has been exhausted.

No gene-function, transcriptomic, regulator, MIC or mechanism claim is asserted, so iModulonDB is not applicable.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The identity, lineage, source scope, strain count and lifecycle provenance are supported.

## Recommended Edits

None required. Preserve the generated record and its seed event. Optional marker/literature enrichment would need a maintained representation that survives seeding, not an ad hoc YAML change.

## Follow-up Checks

Any future culture or genome proposal must explicitly connect its accession to HsPySp1/AB032003.1. Similarity to RsDiSp9, membership in Cluster IIB or proximity to Pyr2-C9 is insufficient by itself. Source or harmonization fixes belong in maintained extractor/seeder inputs, followed by schema/strict validation and the documented corpus/provenance gates.

## Additional Notes

- HEAD remained `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. Target bytes were unchanged before report creation. Existing worktrees were preserved; the other session is closed.
- Numeric counterexamples included BacDive 103611 (Rhodococcus ST031444), CIP 103611 (Lactobacillus gallinarum, BacDive 6565, StrainInfo 3188), Enterobacter cloacae sequence CP103611/GCA_024917615.1, unrelated Allobaculum MGBC103611 and MarMAG_103611 assemblies, Salmonella strain numbers, Pseudomonas assembly name ASM103611v1 and unrelated genome statistics. The AllTheBacteria matches were E. coli run DRR103611 and Mycobacterium sample SAMN11053732, not this taxon or its cited PMID.
- The original publisher page exposed its abstract and methods, but subsequent full-text/in-page retrieval attempts failed. The 2003 ASM article's relevant discussion was accessible. The poster screenshot calls returned no usable image; a downloaded copy was successfully rendered with macOS Quick Look and inspected. An initial sandboxed rendering attempt failed; the approved retry succeeded. These access/tool limitations are not record findings.
- No sequence alignment or complete original-study result-table audit was performed. Related-genome and later-paper leads are explicitly bounded rather than asserted as exact-clone identifications.
- Only this new report was written for the target. No generated YAML, source snapshot, lifecycle/history or GitHub state was changed.
