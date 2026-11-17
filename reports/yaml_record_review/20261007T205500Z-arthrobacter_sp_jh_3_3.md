# YAML Record Review: Arthrobacter sp. JH-3-3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_jh_3_3.yaml`
- Started UTC: 2026-10-07T20:49:32Z
- Finished UTC: 2026-10-07T20:55:00Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1036142`, Arthrobacter sp. JH-3-3, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read independently. It carries ten ancestors, code 11, exact grounding, seeded status, one NCBI name attestation and `strain_count: 0`. No synonyms, nomenclature, mappings, strains, evidence objects, graph, discussion or dataset are asserted.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/arthrobacter_sp_jh_3_3.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/arthrobacter_sp_jh_3_3.yaml --out /private/tmp/jh33-strict.tsv`: exit 0, one file, zero errors. The diagnostic TSV contains only its header.
- Structured comparisons checked all backbone fields, the full ten-ancestor chain, sole attestation, path and scope reason. Exact pinned type-material, merged-ID and dropped-ID searches returned no target rows; the backbone contains no target descendants.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. Bounded comparisons do not reproduce the corpus. There is no graph, and the stated search found no standalone target history record; specialized graph/history validation had no target.

## Identity and Grounding

Live Taxonomy EFetch agrees on identifier, exact label, species rank, bacterial division, code 11 and parent `NCBITaxon:235627`, unclassified Arthrobacter. Datasets confirms all ten ancestor IDs including root. The pinned names and ranks agree: root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Micrococcaceae, Arthrobacter and unclassified Arthrobacter. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036142), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036142).

JH-3-3 is a source strain designation, not a registered culture-deposit accession. Exact grounding is to this NCBI node. The species rank does not assert a formally named species or an LPSN nomenclatural status. Similar designations in other genera do not establish identity.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:222270` matches every backbone field, empty synonym fields, sole source and the 2026-09-13 snapshot. The complete native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31788`.
- `data/taxa/PATHS.tsv:14772` uniquely maps the identifier and slug. `curation/seed_scope.tsv:322524` matches the one-source inclusion reason and date.
- Exact-taxonomy Nucleotide search returned one record, [JF820100.1](https://www.ncbi.nlm.nih.gov/nuccore/JF820100.1). Its complete non-sequence metadata describe a 1,403-base partial 16S rRNA sequence and explicitly link strain JH-3-3 and taxon 1036142. The submitter gives Jianghan oil-field soil in China as the isolation source. Direct submission was 14 April 2011 by Zhang, Li, Yang, Wang and Yuan at China Agricultural University; the accession was created and updated on 7 June 2011. No culture deposit, BioSample, BioProject, protein or assembly accession appears in the inspected metadata. This marker is not a genome.
- The sequence's first reference is an unpublished study titled Diversity of Culturable Butane-oxidizing Bacteria in Oil and Gas Field Soil. A fresh PubMed read verifies a 2012 article with the matching title and corresponding author names, PMID 22452226, Huan Jing Ke Xue 33(1):299-304. Its abstract reports an isolation survey including Arthrobacter from two fields, but does not name JH-3-3 or provide its individual assay results. Association with the submission is a bibliographic inference from title and authors, not an explicit PMID link in the sequence. No strain-specific butane-oxidation rate, gene or phenotype is inferred. [Primary abstract in PubMed](https://pubmed.ncbi.nlm.nih.gov/22452226/).
- Exact-taxonomy Assembly search returned zero, with phrase-not-found/no-items warnings. This bounded result does not establish genome absence under every identifier.
- The sole attestation correctly counts one NCBI name, not one culture or genome. The seed event reproduces the inventory and scope reason. Its `2026-09-13T17:54:04Z` timestamp matches the newest extraction time among raw, ATB and StrainInfo manifests, as selected by `src/taxonmech/seed.py:139`.

## Completeness

The exact BacDive inventory search found no target strain and the pinned backbone has no descendants, supporting the source-specific zero count. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits searches also returned no target rows. The schema defines this count as BacDive records classified in the taxon subtree; it does not contradict isolation of a strain outside that inventory.

The gitignore-independent search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It covered digit-bounded 1036142, JH-3-3 label/slug variants and JF820100. All 40 candidate rows were inspected completely: 22 catalog/BV-BRC objects, four BacDive/GOLD objects and 14 TSV rows. Five SOURCE.json files were parsed separately, and history filenames were checked independently.

Three candidate rows describe this target: backbone, native name and scope. The other 37 concern different taxa or designations. No supported additional target culture/genome association, curation overlay or standalone history record was found within these roots. The subsequently identified PMID was checked as literature, not included in the local candidate search count.

Optional fields are appropriately empty for the present seeded claims. The marker and publication offer optional context, not a demonstrated missing required field. No gene, regulator, transcriptomic or dataset claim is made; iModulonDB is not applicable.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, attestation, source-specific strain count and seeding provenance are supported. No claim in the YAML depends on an unverified phenotype or inferred culture/genome join.

## Recommended Edits

None required. Preserve the generated YAML and seed event. Optional marker enrichment belongs in maintained source/extractor inputs or a durable curator representation, not a hand-edited generated record. Phenotype or isolation-context curation belongs with the appropriate sibling repository under `docs/CURATION.md`; retain explicit strain-level evidence. Do not manufacture a culture deposit from the bare designation.

## Follow-up Checks

Before adding any strain-specific phenotype, inspect the primary article's relevant methods, tables and strain assignments and verify the link to JF820100.1. Before adding a genome or deposit, require an explicit source identity link rather than a similar designation. Future maintained-input changes should be regenerated through the documented pipeline, then checked with focused schema/strict validation and corpus/provenance gates.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the YAML was byte-identical before report creation. Existing branches and worktrees were preserved.
- Campylobacter sp. JH33 is taxon 2798510 with GCA/GCF_017846555.1 and BV-BRC 2798510.3. Micromonospora sp. JH33, Streptomyces sp. JH33 and Staphylococcus sp. ljh-33 likewise have distinct NCBI identities. None is this Arthrobacter strain.
- Maribellus mangrovi FJH33 is taxon 3133146, BacDive 175545, deposits KCTC 102210 and MCCC 1H01459, and marker PP485723. Its GOLD Go0703756/Gp0828710/Ga0674327 chain, IMG 8124686520, GCA/GCF_037646455.1 and BV-BRC 3133146.3 are unrelated to the target; full matching source objects were read.
- Other matches concern Salmonella NMSU_WWLCJH33X, Pseudomonas aeruginosa WTJH33, Bacteroides fragilis BJH_33 and Klebsiella variicola JH_33. Historical suppressed RefSeq rows for the Pseudomonas and Bacteroides assemblies were retained as source context, not target links.
- The publication abstract was read via fresh PubMed XML. PubMed supplied no DOI in the inspected identifier list. The OALib discovery page led to an AllJournals full-text endpoint that timed out; primary full-text strain tables were not inspected. Search snippets and later hydrocarbon studies were not used as evidence for JH-3-3.
- No sequence alignment, exhaustive literature review, deposit-availability assessment or taxonomic reassignment was performed. The full-corpus goal remains incomplete.
- Only this new report was written for this target. No YAML, inventory, history/lifecycle or GitHub state changed.
