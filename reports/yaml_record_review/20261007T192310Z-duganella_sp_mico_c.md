# YAML Record Review: Duganella sp. MICO-C

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/duganella_sp_mico_c.yaml`
- Started UTC: 2026-10-07T19:19:01Z
- Finished UTC: 2026-10-07T19:23:10Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1036122`, label Duganella sp. MICO-C, rank `SPECIES`, domain `BACTERIA`. The complete YAML was read independently. It carries eleven ancestors, genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, one NCBI name attestation and `strain_count: 0`. The count describes inventoried BacDive strains, not whether the named isolate has been cultivated experimentally.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/duganella_sp_mico_c.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/duganella_sp_mico_c.yaml --out /private/tmp/dmicoc-strict.tsv`: exit 0; one file, zero errors; the diagnostic TSV contains only its header and was read.
- Complete structured source comparisons verified identity, rank, parent, code, every ancestor, source attestation, scope reason and unique path mapping. No target descendants occur in the pinned backbone. Exact type-material, merged-ID and dropped-ID checks returned no target rows. These bounded checks do not establish corpus reproduction.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. No target graph or standalone history record was found within the bounded searches; their specialized checks have no target here. No focused replacement for a full-corpus gate was invented.

## Identity and Grounding

Live NCBI Taxonomy EFetch matches the identifier, exact name, species rank, genetic code 11 and parent `NCBITaxon:2636909` unclassified Duganella. Datasets confirms all eleven ancestor IDs, including root. Pinned and live lineage names/ranks agree: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Oxalobacteraceae, Telluria group, Duganella and unclassified Duganella. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036122), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036122).

The native name catalog supplies only the scientific name. Empty synonyms, nomenclature and mappings agree with the inventories. Species rank does not establish formal nomenclatural standing. MICO-C must not be merged with the similarly named MICO-M or MICO-M2, nor identified with another isolate solely through sequence similarity.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:222263` matches all backbone fields, empty synonym fields, sole NCBI source and 2026-09-13 snapshot. The native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31778`.
- `data/taxa/PATHS.tsv:14764` uniquely maps the identifier to this slug. `curation/seed_scope.tsv:322519` provides the one-source attested inclusion reason and 2026-09-13 date.
- Exact-taxonomy Nucleotide search returned three records. All non-sequence/non-translation metadata were inspected: [HQ616151.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616151.1), a 1,365-base partial 16S rRNA sequence; [HQ616158.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616158.1), a 1,110-base partial gyrB CDS; and [HQ616165.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616165.1), an 895-base partial vioA CDS. Each names MICO-C, taxon 1036122 and olive rhizosphere as the isolation source. These are marker fragments, not genome assemblies. Their metadata supply no culture, BioSample or BioProject accession.
- All three markers cite Aranda, Montes-Borrego and Landa's 2011 Microbial Ecology article, `PMID:21424823`, `DOI:10.1007/s00248-011-9840-9`, and the IAS-CSIC direct submission dated 14 November 2010. PubMed EFetch and publisher metadata/abstract were inspected during this review run; the complete EFetch result was reread for MICO-C. The paper establishes the seven-isolate context, while GenBank supplies the explicit marker-to-isolate chain. No quantitative phenotype was inferred simply from cohort membership. [PubMed](https://pubmed.ncbi.nlm.nih.gov/21424823/), [primary article](https://link.springer.com/article/10.1007/s00248-011-9840-9).
- The inspected Spanish patent description distinguishes MICO-C from MICO-M: both originated from cultivated Arbequina olives, but MICO-C came from the non-inoculated condition and MICO-M from the mycorrhizal-inoculated condition. The patent's CECT 7781 designation belongs to MICO-M, not MICO-C; CECT 7779 and 7780 likewise belong to other isolates. [Primary patent description](https://patents.google.com/patent/WO2012062951A1/es).
- Bajaj, Schmidt and Winter's 2012 study mentions MICO-C as a 16S sequence comparison for isolates C 1 and C 4. Its actual selenium experiments concern those other isolates, not MICO-C. The inspected primary results do not justify transferring selenite reduction, nanoparticle production or their accessions to this record. [Primary article](https://link.springer.com/article/10.1186/1475-2859-11-64).
- Exact-taxonomy Assembly search returned zero items with phrase-not-found/no-items warnings. This is a bounded query result, not proof of universal genome absence.
- The seed event matches the inventories and scope reason. Its `2026-09-13T17:54:04Z` timestamp is the latest raw/ATB/StrainInfo extraction timestamp, consistent with `src/taxonmech/seed.py:139`. It documents seeding, not human review.

## Completeness

The exact BacDive inventory is empty and there are no backbone descendants, supporting zero inventoried strains. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits source comparisons also returned no target row. Experimental cultivation does not imply a BacDive entry, and another isolate's CECT accession is not a valid enrichment for MICO-C.

The gitignore-independent search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It covered digit-bounded 1036122, MICO-C spelling variants matching the label and slug, all three nucleotide accessions, both associated protein accessions, PMID 21424823 and the 2011 article DOI. All four candidate rows/objects were inspected completely. Five SOURCE.json files were parsed separately and history filenames checked independently. No supported target culture/genome link, additional curation overlay or standalone history record was found within those roots.

Marker and literature enrichment remains optional; no consequential required representation was demonstrated missing. No gene-function, regulator, transcriptomic, mechanism or dataset claim appears in the YAML. iModulonDB is not applicable, and absence from it is not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The identity, lineage, source attestation, source-specific strain count and seeded provenance are supported. The distinct-isolate literature checks reveal no unsupported claim in the current YAML.

## Recommended Edits

None required. Preserve the generated record and seed event. Optional enrichment belongs in maintained extractor/seeder inputs or a suitable durable curator representation. Do not borrow MICO-M's deposit or C 1/C 4's selenium phenotypes and sequence identifiers.

## Follow-up Checks

Any future strain/genome enrichment needs an explicit primary identifier-to-MICO-C chain, not shared taxonomy, paper membership or a similar marker sequence. A later maintained-input change should be tested by schema/strict validation and the documented corpus/provenance gates. Do not patch the generated YAML directly.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The YAML was byte-identical before report creation. Existing worktrees and the closed parallel session's work were left untouched.
- The fourth local candidate is AllTheBacteria row 2144407: Streptococcus suis sample SAMN21424823, run SRR15886619 and analysis ERZ26421993. It matches the PMID digits in another namespace, not MICO-C. Its previously retrieved complete row was reread for this target.
- The original 2011 publisher article requires subscription access; its metadata and abstract were inspected, not the full experimental tables. The 2012 PMC endpoint showed an access challenge; the openly accessible publisher article supplied the inspected metadata, abstract and relevant results instead. No challenge was bypassed.
- No full experimental-table audit, sequence alignment, current culture-collection availability verification or taxonomic reassignment was performed. Patent evidence was used for explicit isolate distinctions and origin, not legal status or quantitative efficacy. Search snippets alone were not used to establish claims.
- Only this new report was written for the target. No YAML, source inventory, history/lifecycle or GitHub state was changed.
