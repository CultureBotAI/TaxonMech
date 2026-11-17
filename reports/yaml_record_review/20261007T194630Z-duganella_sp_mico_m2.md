# YAML Record Review: Duganella sp. MICO-M2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/duganella_sp_mico_m2.yaml`
- Started UTC: 2026-10-07T19:40:48Z
- Finished UTC: 2026-10-07T19:46:30Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1036124`, Duganella sp. MICO-M2, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read independently. It carries eleven ancestors, code 11, exact grounding, seeded mapping status, one NCBI name attestation and zero inventoried BacDive strains. It has no additional synonyms, nomenclature, mappings, strains, evidence objects, graph or discussion.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/duganella_sp_mico_m2.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/duganella_sp_mico_m2.yaml --out /private/tmp/dmicom2-strict.tsv`: exit 0, one file and zero errors. The output TSV was read and contains only its header.
- Structured comparisons checked every backbone field, all ancestors, the source attestation, scope reason and unique path entry. Exact type-material, merged-ID and dropped-ID checks found no target rows. There are no descendants in the pinned backbone.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. The bounded source comparisons do not replace these gates. No target graph or standalone history record was found within the stated searches; no specialized graph/history validation target was present.

## Identity and Grounding

Live Taxonomy EFetch confirms identifier, exact label, species rank, bacterial division, code 11 and parent `NCBITaxon:2636909`, unclassified Duganella. Datasets confirms all eleven ancestor IDs, including root. Pinned and live lineage names/ranks agree: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Oxalobacteraceae, Telluria group, Duganella and unclassified Duganella. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036124), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036124).

The native name row contains the scientific name only. Species rank does not imply formal nomenclatural standing. MICO-M2 is not interchangeable with MICO-M or MICO-C; isolate names and explicit accession chains must be preserved.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:222265` supports the complete backbone, empty synonym fields, sole NCBI attestation and snapshot 2026-09-13. `data/catalog/ncbi_names-0005.jsonl.gz:31780` is the complete native scientific-name object.
- `data/taxa/PATHS.tsv:14766` uniquely maps the identifier and slug. `curation/seed_scope.tsv:322521` supplies the one-source attested inclusion reason and date 2026-09-13.
- Exact-taxonomy Nucleotide search returned three entries. Complete metadata, excluding nucleotide strings and translations, were inspected: [HQ616152.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616152.1), 1,391 bases of partial 16S rRNA; [HQ616159.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616159.1), a 1,110-base partial gyrB CDS; and [HQ616166.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616166.1), an 896-base partial vioA CDS. Each explicitly names MICO-M2, taxon 1036124 and olive rhizosphere as isolation source. These are marker fragments, not assemblies; their metadata contain no culture, BioSample or BioProject accession.
- The CDS entries identify AEJ88329.1 and AEH95321.1 respectively, with codon start 1 and translation table 11. All markers cite Aranda, Montes-Borrego and Landa's 2011 Microbial Ecology article, `PMID:21424823`, `DOI:10.1007/s00248-011-9840-9`, and the IAS-CSIC submission dated 14 November 2010. Fresh PubMed EFetch and publisher metadata/abstract were inspected. The article supplies seven-isolate context, while GenBank supplies the exact isolate-to-marker chain. No quantitative phenotype was transferred merely through cohort membership. [PubMed](https://pubmed.ncbi.nlm.nih.gov/21424823/), [primary article](https://link.springer.com/article/10.1007/s00248-011-9840-9).
- The inspected patent description distinguishes MICO-M2, isolated from four-year-old mycorrhizal-inoculated Arbequina olives at another commercial field, from MICO-M/MICO-C at the five-year-old planting. Its CECT 7781 deposit belongs to MICO-M; CECT 7779 and 7780 belong to LO-22 and CICYT-60. Those deposits must not be reassigned to MICO-M2. [Primary patent description](https://patents.google.com/patent/WO2012062951A1/es).
- Exact-taxonomy Assembly search returned zero items with phrase-not-found/no-items warnings. This is a bounded query result, not proof of genome absence under every possible identifier.
- The seed event matches the scope and source inventory. Its timestamp, `2026-09-13T17:54:04Z`, is the latest extraction timestamp across raw, ATB and StrainInfo manifests, as specified by `src/taxonmech/seed.py:139`. It represents seeding, not human review.

## Completeness

Exact BacDive comparison found no target row, and the backbone has no descendants, supporting zero inventoried strains. This count does not deny experimental cultivation. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits comparisons likewise found no target rows.

The gitignore-independent search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It included digit-bounded 1036124, MICO-M2 variants matching the label and slug, all three nucleotide accessions, both protein accessions, PMID 21424823 and the DOI. All four candidate rows/objects were read completely. Five SOURCE.json files were parsed separately and history filenames checked independently. No supported target culture/genome link, additional curation overlay or standalone history record was found within those roots.

Empty optional literature, marker and deposit fields are not consequential required omissions under the local checklist. The YAML has no gene-function, regulator, transcriptomic, mechanism or dataset claim. iModulonDB is not applicable and its absence supplies no negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, name attestation, source-specific strain count and seeded provenance are supported. The inspected isolate distinctions reveal no unsupported assertion in the current YAML.

## Recommended Edits

None required. Leave the generated YAML and seed event intact. Optional enrichment belongs in maintained source/extractor inputs or an appropriate durable curator representation, retaining explicit MICO-M2 evidence. Do not borrow a similarly named isolate's deposit or phenotype.

## Follow-up Checks

Future strain/genome enrichment requires an explicit primary identifier-to-MICO-M2 chain, not shared taxonomy, sequence similarity or publication membership. Any later maintained-input change should pass schema/strict validation and the documented corpus/provenance gates after regeneration.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The complete target remained byte-identical before report creation. Existing branches and worktrees were preserved.
- The fourth local candidate, `data/catalog/allthebacteria.tsv.xz:2144407`, was read as a complete row. It is Streptococcus suis sample SAMN21424823, run SRR15886619 and analysis ERZ26421993. The PMID digits occur in a different identifier namespace; this is not MICO-M2 evidence.
- The 2011 publisher article requires subscription access; its metadata and abstract, not full experimental tables, were inspected. No access restriction was bypassed. Additional web search results remained leads and were not used as evidence without source inspection.
- No sequence alignment, complete experimental-table audit, current collection-availability check or taxonomic reassignment was performed. Patent text was used for isolate distinctions and origin, not legal status or quantitative efficacy.
- Only this new report was written. No taxon YAML, source inventory, history/lifecycle or GitHub state changed.
