# YAML Record Review: Arthrobacter sp. PG-3-2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_pg_3_2.yaml`
- Started UTC: 2026-10-07T20:56:01Z
- Finished UTC: 2026-10-07T21:01:31Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1036143`, Arthrobacter sp. PG-3-2, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read independently. It contains ten ancestors, genetic code 11, exact grounding, seeded status, one NCBI name attestation and `strain_count: 0`. No synonyms, nomenclature, taxonomy mappings, strains, evidence objects, graph, discussion or dataset are asserted.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/arthrobacter_sp_pg_3_2.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/arthrobacter_sp_pg_3_2.yaml --out /private/tmp/pg32-strict.tsv`: exit 0, one file, zero errors. The diagnostic TSV contains only its header.
- Structured comparisons checked every backbone field, all ten ancestors, attestation, unique path and scope reason. Exact pinned type-material, merged-ID and dropped-ID searches returned no target rows; the backbone has no target descendants.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. Bounded comparisons are not a corpus reproduction. There is no graph; no standalone target history record was found in the stated search, so specialized graph/history checks had no target.

## Identity and Grounding

Live Taxonomy EFetch agrees on identifier, label, species rank, bacterial division, genetic code 11 and parent `NCBITaxon:235627`, unclassified Arthrobacter. Datasets confirms all ten ancestor IDs including root. Pinned labels and ranks match: root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Micrococcaceae, Arthrobacter and unclassified Arthrobacter. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036143), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036143).

PG-3-2 is a source strain designation, not an identified culture-collection deposit. Exact grounding is to the NCBI node; species rank does not establish a formally published species name. The neighboring Arthrobacter sp. JH-3-3 and similarly spelled PG32 strains are not treated as equivalent.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:222271` matches every backbone field, empty synonym fields, sole source and the 2026-09-13 snapshot. The complete native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31789`.
- `data/taxa/PATHS.tsv:14773` uniquely maps identifier and slug. `curation/seed_scope.tsv:322525` matches the one-source inclusion reason and date.
- Exact-taxonomy Nucleotide search returned two records; complete non-sequence metadata for both were read. [JF820099.1](https://www.ncbi.nlm.nih.gov/nuccore/JF820099.1) is a 1,410-base partial 16S rRNA sequence explicitly naming PG-3-2 and taxon 1036143. Its submitters report Puguang gas-field soil in China. Direct submission was 14 April 2011 by Zhang, Li, Yang, Wang and Yuan at China Agricultural University; the accession was created and updated on 7 June 2011.
- [JN207847.1](https://www.ncbi.nlm.nih.gov/nuccore/JN207847.1) is a 419-base partial coding sequence annotated as putative butane monooxygenase alpha subunit, gene `bmoX`, with strain PG-3-2, taxon 1036143, code 11 and protein AEM44627.1. It was submitted by Zhang on 4 July 2011; its study reference remains unpublished in the accession. The independently retrieved [protein record AEM44627.1](https://www.ncbi.nlm.nih.gov/protein/AEM44627.1) confirms a 139-residue partial protein, the same strain/taxon and the explicit coding link to JN207847.1. Annotation is not itself a biochemical validation or a complete genome.
- Neither nucleotide record provides a culture deposit, BioSample, BioProject or assembly accession. Exact-taxonomy Assembly search returned zero with phrase-not-found/no-items warnings; this bounded result is not proof of genome absence under every identifier.
- The 16S submission's survey title and author names correspond to PMID 22452226, Huan Jing Ke Xue 33(1):299-304 (2012), whose metadata and abstract were freshly inspected during this turn. The association is bibliographic, not an explicit PMID link in the accession. The abstract does not identify PG-3-2's individual results. [Survey abstract](https://pubmed.ncbi.nlm.nih.gov/22452226/).
- A separate primary article specifically addresses PG-3-2: Zhang and colleagues, Geomicrobiology Journal 30(2):85-92 (2013), DOI 10.1080/01490451.2011.653086. Publisher-deposited Crossref metadata verify the title, six authors and citation. Its abstract, inspected on ResearchGate, reports growth using butane and amplification of a `bmoX` fragment. It calls the source location Puguang oilfield, whereas the 16S submission says gas field. Neither wording is asserted in the YAML. Full methods and accession tables were unavailable, so the report does not equate sequence homology with direct enzyme proof or infer an assembly from DNA amplification. [DOI registry metadata](https://api.crossref.org/works/10.1080%2F01490451.2011.653086), [Primary article abstract](https://www.researchgate.net/publication/262954103_Identification_and_Characterization_of_the_Butane-Utilizing_Bacterium_Arthrobacter_sp_PG-3-2_Harboring_a_Novel_bmoX_Gene).
- The sole `NAME` attestation counts one NCBI name, not one culture or genome. The seed event reproduces the inventory and scope reason. Its `2026-09-13T17:54:04Z` timestamp is the newest of the raw, ATB and StrainInfo manifest extraction times, as selected by `src/taxonmech/seed.py:139`.

## Completeness

Exact BacDive comparison found no target strain; the pinned backbone has no descendants. These support the source-specific zero count, which does not mean that the strain was never cultured. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventory comparisons also returned no target rows. Optional slots are appropriate for the present seeded claims.

The gitignore-independent search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It covered digit-bounded 1036143, PG-3-2 label/slug variants, JF820099, JN207847 and AEM44627. All 31 candidates were inspected completely: 17 catalog/BV-BRC objects, ten GOLD objects and four TSV rows. Five SOURCE.json files were parsed separately and history filenames checked independently.

Three candidates describe the target: backbone, native name and scope. The other 28 are unrelated numeric or designation matches. No supported additional target culture/genome association, curation overlay or standalone history record was found within those roots. The publication identifiers were checked separately as literature, not included in this candidate count.

The marker, partial gene and article provide optional enrichment context, not a missing required representation. The YAML names no gene, regulator, transcriptomic dataset or functional mechanism; iModulonDB is not applicable to the asserted record fields. Expression-module evidence would not validate the enzyme annotation or strain phenotype in any case.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, full lineage, source-specific strain count, attestation and seeded provenance are supported. The YAML makes no functional claim requiring stronger evidence than was inspected.

## Recommended Edits

None required. Preserve the generated YAML and seed event. Optional sequence enrichment belongs in maintained source/extractor inputs or a durable curator representation, not a direct YAML patch. Preserve marker, partial gene, protein and genome identifier types. Phenotype or mechanism curation should follow the ownership and evidence rules in `docs/CURATION.md`, including direct strain-specific evidence; do not infer a collection deposit from PG-3-2.

## Follow-up Checks

Before curating quantitative growth or enzyme-function claims, inspect the primary article's methods and results and verify explicit accession assignments. Preserve the sequence annotation's putative and partial qualifiers. Before adding a deposit or assembly, require an explicit source identity link to this strain/taxon rather than a name substring. Future maintained-input changes should be regenerated, then checked by focused schema/strict validation and corpus/provenance gates.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the YAML was byte-identical before report creation. Existing branches and worktrees were preserved.
- Salmonella enterica serovar Typhi strain 1036143 is taxon 90370, GOLD Go0314454/Gp0162929/Ga0142762, BV-BRC 90370.631 and GCA_001144345.1. Its historical GCF_001144345.1 row is suppressed. Its numeric strain designation does not identify this Arthrobacter taxon.
- Serratia liquefaciens IPG32 is taxon 614 with GCA/GCF_028620835.1 and BV-BRC 614.162. Pseudomonas viridiflava MPG32, Xanthomonas euvesicatoria DAPP_PG32 and Allobosea sp. RIT-PG3_2 likewise have separate identities. Their complete matching source objects were inspected; none provides a target link.
- GOLD Panicum virgatum FPG-32-4/FPG-32-8 records and soil-community CPg_3-2/CPg_3-2b projects are distinct sample/organism contexts, including taxonless project objects; they are not PG-3-2 strain associations. Their source rows were read without reviewing or changing any Eukaryota record.
- The DOI and Taylor & Francis abstract endpoints were inaccessible through the web tool. Crossref citation metadata and the article's public abstract on ResearchGate were inspected; ResearchGate offered no full text. No author contact, paid retrieval or access-control bypass was attempted. The 2012 survey's full-text route had timed out earlier in this turn.
- No sequence alignment, exhaustive literature review, protein-function experiment, deposit-availability assessment or taxonomic reassignment was performed. Later co-culture studies and other butane-utilizing Arthrobacter strains were not treated as equivalent evidence.
- Only this new report was written for this target. No YAML, inventory, history/lifecycle or GitHub state changed.
