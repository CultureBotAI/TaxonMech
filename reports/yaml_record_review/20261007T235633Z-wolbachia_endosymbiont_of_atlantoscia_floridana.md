# YAML Record Review: Wolbachia endosymbiont of Atlantoscia floridana

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_atlantoscia_floridana.yaml`
- Started UTC: 2026-10-07T23:46:27Z
- Finished UTC: 2026-10-07T23:56:33Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1036168`, Wolbachia endosymbiont of Atlantoscia floridana, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read independently. It contains eleven ancestors, genetic code 11, exact grounding, seeded status, one NCBI name attestation and `strain_count: 0`. There are no asserted synonyms, nomenclature, taxonomy mappings, listed strains, evidence objects, causal graph, discussion or dataset. The eukaryotic host's name does not make this a eukaryotic record.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_atlantoscia_floridana.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_atlantoscia_floridana.yaml --out /private/tmp/waf-strict.tsv`: exit 0, one file, zero errors. The diagnostic TSV was read and is header-only.
- Structured comparisons passed for backbone fields, all eleven ancestors, attestation, unique path and scope reason. Exact pinned type-material, merged-ID and dropped-ID searches returned no target rows. The backbone has no target children.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs, product and vendored gates. Bounded source comparisons do not establish corpus reproducibility. No graph is asserted; the ignored-inclusive bounded search found no standalone target history record, so specialized graph/history validation had no target.

## Identity and Grounding

Live NCBI Taxonomy EFetch agrees on the identifier, label, species rank, bacterial division, genetic code 11 and parent `NCBITaxon:2640676`, unclassified Wolbachia. Datasets confirms all eleven ancestor IDs including root. Labels and ranks match through cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Rickettsiales, Anaplasmataceae, Wolbachieae, Wolbachia and the unclassified parent. The tribe `NCBITaxon:952` is source-supported, not an extra invented lineage level. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036168), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036168).

Exact grounding denotes the NCBI node. It does not establish a formally named bacterial species, a single clonal isolate, an exclusive host range or equivalence of all samples filed under this host-associated label. The record appropriately makes none of those stronger assertions.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:222294` agrees with identity, rank, parent, genetic code, empty synonyms, sole source and snapshot date 2026-09-13. The complete native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31812`.
- `data/taxa/PATHS.tsv:14798` uniquely maps ID to slug. `curation/seed_scope.tsv:322548` agrees on date and the one-source inclusion reason.
- Exact-taxonomy Nucleotide search returned three records. Complete non-sequence GenBank metadata were read for each. [JF799948.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799948.1) is an 856-base partial 16S rRNA marker, isolate wFlo, clone A, from the named host collected in Porto Alegre, Brazil, on 20 November 2009. It explicitly cites PMID 24031883 and DOI `10.1590/S1517-83822012000200036`.
- [KJ814201.1](https://www.ncbi.nlm.nih.gov/nuccore/KJ814201.1) is a 773-base partial 16S marker; [KJ814218.1](https://www.ncbi.nlm.nih.gov/nuccore/KJ814218.1) is a 411-base partial dnaA coding sequence with protein accession AIG17926.1 and translation table 11. Both identify clone C, collection in Corupa, Brazil, on 16 April 2012, and taxon 1036168. Their host qualifier embeds `specimen_voucher = UFRGS 50003`; this is not evidence of a bacterial culture deposit. Their forest-soil qualifier does not demonstrate a free-living bacterial isolate. Both cite PMID 25764472 and DOI `10.1093/femsec/fiv025`.
- The 2012 primary article was inspected through SciELO, alongside its PubMed citation/abstract. It reports sequence-based detection in host tissue, including a Porto Alegre sample called A. floridana and the designation wFlo, and explicitly lists JF799948 among its accessions. Its background discussion of Wolbachia reproductive effects does not establish those effects for this record. [Primary 2012 study](https://new.scielo.br/j/bjm/a/3tMnDg5R75sMMvwLQ8TQSpS/?ilang=pt_BR&lang=en), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24031883/).
- For the 2015 study, the complete PubMed abstract and relevant publisher HTML were inspected. Table 2 separates A. floridana from Corupa from A. petronioi from Porto Alegre. Its Results call the A. floridana detection a first report, whereas the 2012 article used the same host name. That literature-level inconsistency is not silently reconciled. The distinct sample, locality and marker metadata must remain attached to their own accessions. The study does not justify combining the 2009 and 2012 samples into one genome or culture. [Primary 2015 study](https://academic.oup.com/femsec/article/91/4/fiv025/598436), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25764472/).
- A later primary article's author-uploaded text was inspected, including host-identification methods and the relevant Results/Discussion. It reports infection in A. petronioi, not the sampled A. floridana or A. inflata, and explicitly compares its Wolbachia 16S sequence with JF799948. This preserves an important host/sample caveat; matching a partial marker is not independently established whole-strain identity or proof that the original host was misidentified. Its reproductive findings cannot be assigned wholesale to this host-labelled NCBI node. [Primary 2018 study, DOI 10.1139/cjz-2018-0086](https://www.researchgate.net/publication/326382678_How_coexistence_may_influence_life_history_the_reproductive_strategies_of_sympatric_congeneric_terrestrial_isopods_Crustacea_Oniscidea).
- None of the three complete GenBank metadata records supplies a BioSample, BioProject, assembled genome or bacterial collection-deposit link. Exact-taxonomy Assembly search returned zero with phrase-not-found/no-items warnings. This is bounded negative evidence, not a claim that no genome exists anywhere.
- The sole attestation counts one NCBI `NAME`, not samples, sequences or cultures. Seed event and scope reason agree. The timestamp is the latest extracted-at value among the raw, ATB and StrainInfo manifests, as implemented by `src/taxonmech/seed.py:139`.

## Completeness

The exact BacDive comparison and absence of classified descendants support the inventory-specific zero strain count. It is not a claim about cultivability or biological strain diversity. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits comparisons found no target rows. Empty optional slots are appropriate for this seeded identity record.

Resolution searched ignored files in `data/taxa`, `reports`, `curation` and `history`. Source discovery used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Queries covered digit-bounded 1036168, host label/slug forms, all three nucleotide accessions, wFlo and UFRGS 50003. All three matching source objects/rows were read completely: native scientific name, backbone and scope. Five SOURCE.json files were separately parsed; history filenames were independently checked.

No additional supported target culture/genome link, curation overlay or standalone history record was found within those bounded roots, including ignored files. No required representation was demonstrated missing. iModulonDB is not applicable: the YAML asserts no gene, regulator, functional, transcriptomic or dataset claim. The incidental dnaA marker in external sequence metadata does not create a record-level functional claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found against the current YAML. Its identity, lineage, inventory count and seeded provenance are supported. The literature caveats concern optional sample-level enrichment; the YAML does not import phenotype, exclusive-host, clonal-equivalence or culture/genome assertions that would overstate that evidence.

## Recommended Edits

None required. Preserve the generated YAML and seed event. Supported source taxonomy corrections belong upstream at NCBI; a demonstrated harmonization defect belongs in `src/taxonmech/seed.py` with a test. Source extraction changes belong in maintained extractor inputs, including `scripts/extract_source_inventory.py`. A scope correction would belong in `curation/seed_scope.tsv`, but none is justified here. Durable curator overlays require the implementation described in `docs/CURATION.md`; do not invent an existing overlay or hand-edit generated records. Host-interaction and phenotype enrichment belongs to the relevant sibling repository.

## Follow-up Checks

Before any sample-level enrichment, resolve host identification and accession provenance separately for the Porto Alegre and Corupa material. Inspect the 2015 supplements and host vouchers if those distinctions become material. No sequence alignment or whole-genome comparison was performed; the 2018 paper's partial-marker comparison alone is not a strain-equivalence assertion. Any proposed collection or genome link needs its own primary chain. Retain the source discrepancy rather than relabelling the NCBI node from inference. Future maintained-input changes require the documented regeneration pipeline, focused schema/strict validation and corpus/provenance gates.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the target YAML was byte-identical before report creation. Existing branches and worktrees were preserved.
- Direct PMC/PubMed HTML access sometimes returned a browser-check interstitial. Public EFetch supplied PubMed metadata; SciELO supplied the 2012 primary text. The 2015 publisher page was successfully read from its publicly redirected CDN after the web reader failed on the redirect. No challenge or access control was bypassed.
- The 2018 mirror PDF could not be retrieved because of a TLS certificate error. Its author-uploaded primary text was instead inspected on ResearchGate. No inaccessible supplement, unread PDF figure/table or search snippet was treated as verified evidence.
- No culture-availability assessment, taxonomic reassignment, paid research or outreach was performed. Only this new report was written for this review; no YAML, source inventory, curation history/lifecycle or GitHub state changed. Eukaryota remained untouched.
