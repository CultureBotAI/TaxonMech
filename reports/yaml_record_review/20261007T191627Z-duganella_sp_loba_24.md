# YAML Record Review: Duganella sp. LOBA-24

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/duganella_sp_loba_24.yaml`
- Started UTC: 2026-10-07T19:11:07Z
- Finished UTC: 2026-10-07T19:16:27Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1036121`, label Duganella sp. LOBA-24, rank `SPECIES`, domain `BACTERIA`. The whole YAML was read independently. It carries eleven ancestors, genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, one NCBI name attestation and `strain_count: 0`. This count concerns inventoried BacDive strains, not whether the isolate was cultured experimentally.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/duganella_sp_loba_24.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/duganella_sp_loba_24.yaml --out /private/tmp/dloba24-strict.tsv`: exit 0; one file, zero errors; diagnostic TSV read and contains only its header.
- Structured source comparisons verified identity, rank, code, parent, every lineage entry, source attestation, scope reason and unique path mapping. No descendants occur in the pinned backbone. Exact type-material, merged-ID and dropped-ID checks returned no target rows. These are bounded checks, not full corpus reproduction.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. No target graph or standalone history record was found in the bounded searches; their specialized checks have no target here. No focused replacement for a full-corpus gate was invented.

## Identity and Grounding

Live NCBI Taxonomy EFetch agrees with the identifier, exact label, species rank, genetic code 11 and parent `NCBITaxon:2636909` unclassified Duganella. Datasets confirms all eleven ancestor IDs, including root. The pinned lineage and live names/ranks agree: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Oxalobacteraceae, Telluria group, Duganella and unclassified Duganella. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036121), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036121).

The native catalog supplies only the scientific name. Empty synonyms, nomenclature and mappings agree with the inventories. Species rank does not confer formal nomenclatural standing. LOBA-24 remains distinct from LO-22, the other olive isolates and Duganella violaceinigra.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:222262` is the complete matching backbone row, with empty synonym fields, sole NCBI source and 2026-09-13 snapshot. `data/catalog/ncbi_names-0005.jsonl.gz:31777` is the scientific-name record.
- `data/taxa/PATHS.tsv:14763` uniquely maps the identifier to this slug. `curation/seed_scope.tsv:322518` supplies the one-source attested inclusion reason and 2026-09-13 date.
- Exact-taxonomy Nucleotide search returned three records. All non-sequence/non-translation metadata were inspected: [HQ616150.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616150.1), a 1,346-base partial 16S rRNA sequence; [HQ616157.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616157.1), a 1,119-base partial gyrB CDS; and [HQ616164.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616164.1), a 903-base partial vioA CDS. Each explicitly names LOBA-24, taxon 1036121 and olive rhizosphere as the isolation source. These are marker fragments, not genome assemblies; their metadata supply no culture, BioSample or BioProject accession.
- All three markers cite Aranda, Montes-Borrego and Landa's 2011 Microbial Ecology article, `PMID:21424823`, `DOI:10.1007/s00248-011-9840-9`, and the IAS-CSIC direct submission of 14 November 2010. PubMed EFetch and publisher metadata/abstract were inspected. They establish the article and seven-isolate context, while the exact marker-to-isolate links come from GenBank. Cohort-level quantitative phenotypes were not transferred into the record. [PubMed](https://pubmed.ncbi.nlm.nih.gov/21424823/), [primary article](https://link.springer.com/article/10.1007/s00248-011-9840-9).
- The inspected Spanish patent description separately names LOBA-24 among wild-olive isolates. Its CECT 7779, 7780 and 7781 designations are explicitly attached to LO-22, CICYT-60 and Mico-M respectively, not LOBA-24. The shared study does not transfer those deposits or establish species equivalence. [Primary patent description](https://patents.google.com/patent/WO2012062951A1/es).
- Exact-taxonomy Assembly search returned zero items with phrase-not-found/no-items warnings. This is a bounded result, not a universal genome-absence claim.
- The seed event's source and scope reason match the inventories. Its `2026-09-13T17:54:04Z` timestamp is the latest raw/ATB/StrainInfo extraction timestamp, consistent with `src/taxonmech/seed.py:139`. The event records seeding, not human review.

## Completeness

The exact BacDive inventory is empty and there are no pinned backbone descendants, supporting zero inventoried strains. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits comparisons also returned no target row. Optional marker or literature enrichment is possible, but no consequential required representation was demonstrated missing.

The gitignore-independent search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It covered digit-bounded 1036121, LOBA-24 spelling variants matching the label and slug, all three nucleotide accessions, both associated protein accessions, PMID and DOI. All five candidate rows/objects were inspected completely. Five SOURCE.json files were parsed separately and history filenames checked independently. No supported target culture/genome link, additional curation overlay or standalone history record was found within those roots.

No gene-function, regulator, transcriptomic, mechanism or dataset claim appears in the YAML. iModulonDB is not applicable; its absence was not used as negative biological evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, complete lineage, source attestation, source-specific strain count and seeded lifecycle provenance are supported.

## Recommended Edits

None required. Preserve the generated YAML and seed event. Optional enrichment belongs in maintained extractor/seeder inputs or an appropriate durable curator representation. Do not assign another isolate's CECT accession or a gene fragment as a genome.

## Follow-up Checks

Any future culture or genome link needs an explicit primary identifier-to-LOBA-24 chain. Shared taxonomy, study membership or matching numeric metadata is insufficient. Validate a later maintained-input change with schema/strict checks and the documented corpus/provenance gates; do not hand-edit the generated record.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The YAML remained byte-identical before report creation. Existing worktrees and the closed parallel session's work were left untouched.
- The fourth candidate is `data/catalog/ncbi_genbank-0067.jsonl.gz:2631`: uncultured bacterium taxon 77133, assembly GCA_984587405.1, isolate KIMD21-1_SAMN19716612_MAG_00000105, sample SAMEA122266198 and project PRJEB73018. Its 1,036,121-base genome size matches the target's numeric identifier, but it is not LOBA-24 evidence.
- The fifth candidate is AllTheBacteria row 2144407: Streptococcus suis sample SAMN21424823, run SRR15886619 and analysis ERZ26421993. This is a PMID-digit collision. Its previously retrieved complete row was reread for this target.
- The publisher's full article requires subscription access. A later browser retrieval of PubMed was incomplete, so its complete citation and abstract were verified through public EFetch. No full experimental-table audit, sequence alignment, current culture-collection availability check or taxonomic reassignment was performed. Search snippets were treated only as leads; patent use was limited to explicit isolate distinctions and source context, not legal status or quantitative efficacy.
- Only this new report was written for the target. No YAML, source inventory, history/lifecycle or GitHub state was changed.
