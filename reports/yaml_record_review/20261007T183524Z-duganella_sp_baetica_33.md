# YAML Record Review: Duganella sp. BAETICA.33

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/duganella_sp_baetica_33.yaml`
- Started UTC: 2026-10-07T18:30:20Z
- Finished UTC: 2026-10-07T18:35:24Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1036118`, label Duganella sp. BAETICA.33, rank `SPECIES`, domain `BACTERIA`. The whole YAML was read. It contains eleven ancestors, genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, zero inventoried strains and one NCBI name attestation. The isolate designation in a species-rank NCBI name does not imply a formally described species or a BacDive deposit.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/duganella_sp_baetica_33.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/duganella_sp_baetica_33.yaml --out /private/tmp/db33-strict.tsv`: exit 0; one file, zero errors; diagnostic TSV is header-only.
- Complete pinned-source comparisons verified identity fields, genetic code, the full lineage, scope reason, path mapping and the NCBI attestation. No direct descendants were found in the backbone. These bounded checks do not replace corpus reproduction.
- Exact status-row checks found no target type-material, merged-ID or dropped-ID entry.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored checks. No target graph or standalone history record was found in the bounded searches; their specialized validators therefore have no target here. No undocumented focused substitute was used.

## Identity and Grounding

Live NCBI Taxonomy EFetch matches taxon 1036118, the exact name, species rank, genetic code 11 and parent `NCBITaxon:2636909` unclassified Duganella. Datasets independently confirms the identifier, name, rank and all ancestor IDs, including root. The pinned chain and live named/ranked ancestors agree: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Oxalobacteraceae, Telluria group, Duganella and unclassified Duganella. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036118), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036118).

The native name catalog contains the scientific name only. Empty synonyms, nomenclature and taxonomy mappings are consistent with the inventories. `EXACT` applies to the NCBI concept, not to equivalence with a named Duganella species or another olive isolate.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:222259` supplies the complete backbone row, including empty synonym fields, NCBI-only scope and the 2026-09-13 snapshot date. `data/catalog/ncbi_names-0005.jsonl.gz:31774` preserves its scientific-name row.
- `data/taxa/PATHS.tsv:14759` uniquely pins the slug to this identifier. `curation/seed_scope.tsv:322515` records the attested-rule inclusion with one source.
- Exact-taxonomy Nucleotide search returned three records. Complete metadata, excluding nucleotide/translation payloads, were inspected: [HQ616149.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616149.1), a 1,384-base partial 16S rRNA sequence; [HQ616156.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616156.1), a 1,110-base partial gyrB CDS; and [HQ616163.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616163.1), a 961-base partial vioA CDS. Each names BAETICA.33, taxon 1036118 and olive rhizosphere as the isolation source. None supplies a culture accession, BioSample, BioProject or assembled genome. Genomic DNA as the molecule source does not make these fragments genome assemblies.
- All three sequences cite Aranda, Montes-Borrego and Landa's 2011 study, `PMID:21424823`, `DOI:10.1007/s00248-011-9840-9`, and a direct submission dated 14 November 2010 from IAS-CSIC, Cordoba. PubMed and the publisher confirm the publication metadata and describe seven olive-associated Duganella isolates studied using 16S, gyrB and vioA. The abstract supports cohort context, while GenBank supplies the exact sequence-to-isolate link. Quantitative phenotype results were not generalized to the YAML. [PubMed](https://pubmed.ncbi.nlm.nih.gov/21424823/), [primary article](https://link.springer.com/article/10.1007/s00248-011-9840-9).
- The inspected description of patent WO2012062951A1 distinguishes Baetica-33 from the deposited isolates: CECT 7779 is LO-22, CECT 7780 is CICYT-60 and CECT 7781 is Mico-M. Those deposits must not be transferred to BAETICA.33 through shared study membership. This is a biological provenance check, not a patent-validity assessment. [Patent description](https://patents.google.com/patent/WO2012062951A1/en).
- Exact-taxonomy Assembly search returned zero items with phrase-not-found/no-items warnings. This is a bounded query result, not proof that no related genome exists.
- The seed event agrees with the source attestation and scope reason. Its `2026-09-13T17:54:04Z` timestamp is the latest of the raw, ATB and StrainInfo extraction timestamps, matching `src/taxonmech/seed.py:139`. `SEEDED` does not claim human review.

## Completeness

The exact-taxon BacDive inventory is empty and the backbone contains no descendants, supporting `strain_count: 0` as an inventory count. It does not mean the isolate was never cultivated. No target LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion was found in the exact pinned-source comparisons. Empty optional slots are appropriate; record-level literature citations are not required in addition to the existing NCBI provenance.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It included the digit-bounded taxon identifier and BAETICA.33 spelling variants, then the three nucleotide accessions, two associated protein accessions, PMID and DOI. All four resulting source rows/objects were read completely. Five SOURCE.json manifests were parsed separately, and history filenames were checked independently. No exact-target culture/genome link, additional curation overlay or standalone history record was found within these roots. These findings are bounded to the inspected inventories.

No gene-function, regulatory, transcriptomic or mechanism claim is present in the YAML, so iModulonDB is not applicable. Discovering gene-fragment accessions during identity review does not require adding such claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source scope, strain count and lifecycle provenance are supported.

## Recommended Edits

None required. Do not alter the generated YAML or append a curation event for this read-only review. Optional marker or literature enrichment requires a maintained representation that survives seeding, not a direct record edit.

## Follow-up Checks

For future strain/genome additions, require an explicit BAETICA.33 accession or registered-deposit chain. Do not infer identity from shared olive origin, pigment production, nearby phylogenetic placement or another study isolate's CECT accession. Route source corrections through the maintained extractor/seeder inputs, then rerun schema/strict checks and the documented corpus/provenance gates.

## Additional Notes

- HEAD remained `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The target was byte-identical before report creation. Existing worktrees were inspected and preserved; the other session is closed.
- The fourth local candidate was `data/catalog/allthebacteria.tsv.xz:2144407`: Streptococcus suis BioSample SAMN21424823, run SRR15886619, ENA analysis ERZ26421993. Its digits match the PMID, not the taxon or publication namespace; it provides no BAETICA.33 genome evidence.
- The publisher exposed metadata and abstract but required subscription access for the full article. No full experimental-table audit, sequence alignment or independent biochemical interpretation was performed. The patent's explicit isolate/deposit paragraph was inspected without relying on its broader claims as established phenotypes.
- Only this new report was written. No generated record, source inventory, history/lifecycle or GitHub state was changed.
