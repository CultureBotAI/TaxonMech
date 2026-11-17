# YAML Record Review: Wolbachia endosymbiont of Burmoniscus meeusei

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_burmoniscus_meeusei.yaml`
- Started UTC: 2026-10-08T00:00:01Z
- Finished UTC: 2026-10-08T00:05:45Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1036169`, Wolbachia endosymbiont of Burmoniscus meeusei, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read. It asserts eleven ancestors, code 11, exact grounding, seeded status, one NCBI name attestation and zero inventory strains. It asserts no synonyms, nomenclature, mappings, listed strains, evidence objects, graph, discussion or dataset. This is a bacterial record, not its eukaryotic host's record.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_burmoniscus_meeusei.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_burmoniscus_meeusei.yaml --out /private/tmp/wbm-strict.tsv`: exit 0, one file, zero errors; diagnostic TSV read, header-only.
- Structured comparisons passed for backbone fields, all eleven ancestors, attestation, path and seed-scope history. Exact pinned type-material, merged-ID and dropped-ID checks returned no target rows. No classified children occur in the backbone.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs, product and vendored gates. These bounded checks do not prove corpus reproducibility. Graph and standalone history validation have no asserted target in this review; the ignored-inclusive history search is described below.

## Identity and Grounding

Live Taxonomy EFetch agrees with the ID, name, species rank, bacterial division, genetic code 11 and parent `NCBITaxon:2640676`, unclassified Wolbachia. Datasets agrees with all eleven ancestor IDs including root. Ancestor labels and ranks match through cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Rickettsiales, Anaplasmataceae, Wolbachieae, Wolbachia and the unclassified parent. Wolbachieae is correctly carried as a tribe. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036169), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036169).

Exact grounding identifies the source taxonomy node. Neither its species rank nor its host-associated label establishes a formally named species, exclusive host range, registered culture or one clonal lineage shared by every sample.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:222295` matches the identity, parent, rank, genetic code, empty synonyms, sole source and 2026-09-13 snapshot. The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31813` agrees.
- `data/taxa/PATHS.tsv:14799` uniquely maps the ID and slug; `curation/seed_scope.tsv:322549` agrees with the seed date and one-source inclusion reason.
- Exact-taxonomy Nucleotide search returned three records; all complete non-sequence GenBank metadata were inspected. [JF799949.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799949.1) is an 860-base partial 16S rRNA marker, isolate wBur, clone B, explicitly assigned to taxon 1036169 and host Burmoniscus meeusei. Its Porto Alegre, Brazil, collection date is 11 January 2010. It cites PMID 24031883 and DOI `10.1590/S1517-83822012000200036`.
- [KJ814208.1](https://www.ncbi.nlm.nih.gov/nuccore/KJ814208.1) is an 827-base partial 16S marker. [KJ814224.1](https://www.ncbi.nlm.nih.gov/nuccore/KJ814224.1) is a 378-base partial dnaA coding sequence, with protein AIG17932.1 and translation table 11. Both name clone J, the same taxon, Porto Alegre and collection on 16 July 2009. Their host qualifier embeds voucher UFRGS 50010; that is not a bacterial culture accession. The forest-soil qualifier is not proof of a free-living isolate. Both cite PMID 25764472 and DOI `10.1093/femsec/fiv025`.
- The linked 2012 primary paper was inspected through SciELO; its PubMed citation and abstract were reread from the prior EFetch result. It reports detection from host tissue in two B. meeusei females, includes JF799949 in its accession list and calls the associated marker wMee. This differs from GenBank's wBur designation. Preserve both source labels without inventing a synonym or inferring an extra culture. General Wolbachia reproductive effects discussed in the introduction are not experiments on this particular record. [Primary 2012 study](https://new.scielo.br/j/bjm/a/3tMnDg5R75sMMvwLQ8TQSpS/?ilang=pt_BR&lang=en), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24031883/).
- The 2015 publisher HTML was inspected for the host-specific table rows, headers and surrounding Results/Discussion; the PubMed abstract was reread. Table 1 describes two tested females, both positive, not a species-wide prevalence estimate. Table 2 reports Porto Alegre material as ST 414; phylogenetic results place it in supergroup A. The discussion says its transmission source is unresolved. These are study-level observations, not a genome accession, culture deposit or demonstrated transmission mechanism. The YAML makes no competing supergroup assertion. The current PubMLST entry and supplementary analyses were not independently audited. [Primary 2015 study](https://academic.oup.com/femsec/article/91/4/fiv025/598436), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25764472/).
- The three metadata records contain no BioSample, BioProject, assembly or bacterial culture-deposit link. Exact-taxonomy Assembly search returned zero with phrase-not-found/no-items warnings; this does not prove that no genome exists under another identifier. Partial markers and a protein accession must not be counted as genomes.
- The attestation counts one NCBI `NAME`, not three sequences or two host individuals. Seed timestamp `2026-09-13T17:54:04Z` agrees with the latest extracted-at value among the raw, ATB and StrainInfo manifests, selected by `src/taxonmech/seed.py:139`; those unchanged inputs and implementation were inspected during this review sequence.

## Completeness

Exact BacDive comparison and the lack of classified descendants support `strain_count: 0` as an inventory count, not a claim about cultivability. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits comparisons found no target rows. No required representation was demonstrated missing.

Resolution used an ignored-inclusive search of `data/taxa`, `reports`, `curation` and `history`. Source discovery used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included digit-bounded 1036169, host label/slug forms, the three marker accessions, UFRGS 50010, wBur and wMee. All three candidate rows/objects were read completely: native name, backbone and scope. Five SOURCE.json files were separately parsed and history filenames independently checked.

No supported additional culture/genome link, curation overlay or standalone history record was found in these bounded roots, including ignored files. Optional literature enrichment is not a required field. iModulonDB is not applicable to this identity-only record; an incidental external dnaA marker does not create a functional or transcriptomic assertion in the YAML.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found against the current YAML. Source identity, lineage, inventory count and seeded provenance are supported. The external wBur/wMee naming discrepancy is preserved; the YAML asserts neither designation nor a phenotype or genome link derived from it.

## Recommended Edits

None required. Preserve generated YAML and its seed event. A supported source-taxonomy correction belongs upstream at NCBI; a harmonization defect belongs in `src/taxonmech/seed.py` with a test. Source extraction changes belong in maintained inputs and `scripts/extract_source_inventory.py`; scope changes belong in `curation/seed_scope.tsv`. No such correction is justified here. Durable curator overlays need the implementation described in `docs/CURATION.md`; do not hand-edit generated records. Optional host-interaction or phenotype enrichment belongs to the appropriate sibling repository.

## Follow-up Checks

Before optional strain-level enrichment, reconcile wBur/wMee using primary accession provenance and retain the distinct collection dates and clone labels. A shared host or partial marker does not prove a single strain. Audit the current typing record and relevant supplements before extending the study's typing assertions. Proposed culture/genome links require their own explicit source chain. Future maintained-input changes should be regenerated and checked with focused schema/strict validation plus corpus/provenance gates.

## Additional Notes

- HEAD remained `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the YAML was byte-identical before report creation. Existing branches and worktrees were preserved.
- The publisher's public redirected CDN supplied the 2015 primary text. A first oversized context extraction was truncated; a focused reread returned the complete relevant target passages. No source was relied on solely through a search snippet.
- No sequence alignment, culture-availability assessment, host reclassification, paid research or outreach was performed. Only this new report was written; no YAML, source inventory, history/lifecycle or GitHub state changed. Eukaryota remained untouched.
