# YAML Record Review: uncultured Treponema clone HsPySp4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_treponema_clone_hspysp4.yaml`
- Started UTC: 2026-10-07T21:46:46Z
- Finished UTC: 2026-10-07T21:52:45Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:103615`, uncultured Treponema clone HsPySp4, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read. It has ten ancestors, genetic code 11, exact grounding, seeded status, one NCBI name attestation and `strain_count: 0`. It asserts no synonyms, nomenclature, mappings, strains, evidence objects, graph, discussion or dataset.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/uncultured_treponema_clone_hspysp4.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/uncultured_treponema_clone_hspysp4.yaml --out /private/tmp/hspy4-strict.tsv`: exit 0, one file, zero errors. The diagnostic TSV was read and contains only its header.
- Structured comparisons checked all backbone fields, ten ancestors, source attestation, unique path and scope reason. Exact pinned type-material, merged-ID and dropped-ID checks returned no target rows; the backbone has no target descendants.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. Bounded comparisons do not reproduce the corpus. No graph is asserted; no standalone target history record was found within the bounded search, so specialized graph/history checks had no target.

## Identity and Grounding

Live Taxonomy EFetch agrees on the ID, label, species rank, genetic code 11 and parent `NCBITaxon:77353`, environmental samples. Datasets confirms all ten ancestor IDs including root. Ancestor labels and ranks agree with the pinned lineage through cellular organisms, Bacteria, Pseudomonadati, Spirochaetota, Spirochaetia, Treponematales, Treponemataceae and Treponema. EFetch's division is Environmental samples; the bacterial domain is established by ancestor `NCBITaxon:2`, not by treating that division as Bacteria. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103615), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103615).

HsPySp4 is an environmental sequence-clone designation. Exact grounding means this particular NCBI node, not a cultured isolate, formal species publication or equivalence to another Treponema phylotype. The environmental parent and its no-rank classification are preserved verbatim.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18517` matches the identity, empty synonym fields, sole source and 2026-09-13 snapshot. The complete native scientific-name object is `data/catalog/ncbi_names-0000.jsonl.gz:38525`.
- `data/taxa/PATHS.tsv:14780` uniquely maps the identifier and slug. `curation/seed_scope.tsv:144163` matches the date and one-source inclusion reason.
- Exact-taxonomy Nucleotide search returned one record, [AB032007.1](https://www.ncbi.nlm.nih.gov/nuccore/AB032007.1). Its complete non-sequence metadata identify a 1,459-base partial 16S rRNA sequence, clone HsPySp4, taxon 103615 and an environmental sample. The source names Hodotermopsis sjoestedti as host and describes PCR amplification from an isolated termite protist. Direct submission was 29 August 1999; the accession was created 29 February 2000 and updated 16 December 2008. No strain qualifier, culture deposit, BioSample, BioProject, assembly or protein accession appears in the inspected metadata. This marker is not a genome.
- The accession explicitly cites Iida, Ohkuma, Ohtoko and Kudo's 2000 FEMS Microbiology Ecology article, PMID 11053732. Primary PubMed XML confirms the citation and DOI `10.1111/j.1574-6941.2000.tb00750.x`. Its abstract describes cultivation-independent investigation of spirochetes associated with isolated oxymonad protists, including Pyrsonympha and Dinenympha in H. sjoestedti. The abstract alone does not resolve every clone-specific assay. [Primary citation and abstract](https://pubmed.ncbi.nlm.nih.gov/11053732/).
- The inspected 2003 follow-up's methods, results and discussion distinguish newly studied N. koshunensis phylotypes from HsPySp4. Its discussion places HsPySp4 in termite Treponema cluster I and identifies HsPySp4/HsDiSp320 as representatives of a shared phylotype recovered from Pyrsonympha/Dinenympha in H. sjoestedti. It describes HsPySp4's distribution across the protist surface. These observations do not make the two clone identifiers synonymous or establish acetogenesis, nitrogen fixation or another metabolic function for this record. Figure 1 uses cluster-level probes; the NkS-specific assays concern other phylotypes. [Noda et al., 2003](https://journals.asm.org/doi/10.1128/AEM.69.1.625-633.2003).
- Exact-taxonomy Assembly search returned zero with phrase-not-found/no-items warnings. This is not proof of genome absence under all identifiers.
- The sole attestation counts one NCBI `NAME`, not a culture or genome. The seed event matches the scope reason and source inventory. Its timestamp, `2026-09-13T17:54:04Z`, is the latest extracted-at value among the raw, ATB and StrainInfo manifests, selected by `src/taxonmech/seed.py:139`.

## Completeness

The exact BacDive comparison and lack of classified descendants support the source-specific zero strain count. The count is not an independent biological assertion about cultivability. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits comparisons also found no target rows. Optional fields are appropriately empty for this seeded identity record; the literature context does not make phenotype or interaction enrichment mandatory.

Resolution included an ignored-inclusive search of `data/taxa`, `reports`, `curation` and `history`. The subsequent source search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It covered digit-bounded 103615, HsPySp4 label/slug variants and AB032007. All 32 candidates were read completely: 20 native JSON objects and 12 TSV rows. Five SOURCE.json files were parsed separately, and history filenames were checked independently.

Three candidates are target backbone, native name and scope records. The other 29 concern different taxa or incidental identifiers. No supported additional target culture/genome association, maintained curation overlay or standalone history record was found within these bounded roots. This does not establish absence from every database or publication. No required representation was demonstrated missing. iModulonDB is not applicable: the record has no gene, regulator, functional, transcriptomic or dataset claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, name attestation, inventory-specific count and seeded provenance are supported. The YAML makes no unsupported cultivation, genome, phenotype or causal assertion.

## Recommended Edits

None required. Preserve the generated YAML and seed event. Optional marker or identity enrichment belongs in maintained source/extractor inputs or a durable curator representation, not a direct generated-file edit. Ecological interactions and functional observations should follow the sibling-repository ownership rules in `docs/CURATION.md` and retain clone, protist and termite scope. Do not join by a bare numeric identifier or infer clone synonymy from phylotype grouping.

## Follow-up Checks

Before adding detailed ecological claims, inspect the original 2000 article's full clone-specific methods and results alongside the follow-up's probe specificity. Before adding a culture or genome, require a direct source link to HsPySp4/AB032007.1/taxon 103615. Regenerate future maintained-input changes through the documented pipeline, then run focused schema/strict validation and corpus/provenance gates.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the YAML was byte-identical before report creation. Existing branches and worktrees were preserved.
- BacDive 103615 is Rhodococcus sp. ST017678(HKI)/BI 08828/CIBAID40628, taxon 194249, not NCBITaxon:103615. Its source metadata request also contains that BacDive number.
- CIP 103615 is Lactobacillus gasseri, taxon 1596, with VPI 6322/VA 24061, BacDive 135314, StrainInfo 69023/deposit 152086 and GOLD Go0238865. Its complete own-deposit object and associated normalized links identify that organism, not this clone.
- StrainInfo 63022 is Jianyunia sakaguchii, taxon 109612; KY103615 is one of its sequence accessions. Reading this unrelated source candidate did not review or modify its Eukaryota YAML.
- Remaining numeric collisions include MarMAG_103615 (taxon 77133, GCA_977617435.1), MGBC103615 (taxon 2301481, GCA_948869815.1), Klebsiella pneumoniae 3571 (taxon 573, CP103615 among its sequences), Rhodoferax PELAGICS-MAG-m2-bin103615 (taxon 50421), three Salmonella strain names, and Pseudomonas aeruginosa Pae_CF67.11e (taxon 287, assembly name ASM103615v1). Complete BV-BRC, GOLD, GenBank/RefSeq and GTDB candidates provide no target identity link.
- ATB row 6211 is Escherichia coli O26:H11, SAMD00075958/DRR103615/ERZ25075589. ATB row 2092750 is Vibrio parahaemolyticus, SAMN20168534/SRR15099784/ERZ25972046; 103615 occurs inside its checksum. Neither is target evidence.
- The original 2000 article's OUP page and DOI routes were inaccessible; its primary PubMed abstract and explicit sequence citation were inspected. PMC/Europe PMC follow-up routes returned a browser check or errors, but the ASM publisher text was accessible and inspected. A 2006 comparison-paper search lead was not followed or used as evidence. No exhaustive literature-absence claim is made.
- No sequence alignment, contemporary culture-availability assessment or taxonomic reassignment was performed. Only this new report was written for the target; no YAML, source inventory, history/lifecycle or GitHub state changed.
