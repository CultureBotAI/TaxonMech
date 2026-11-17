# YAML Record Review: Duganella sp. MICO-M

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/duganella_sp_mico_m.yaml`
- Started UTC: 2026-10-07T19:28:39Z
- Finished UTC: 2026-10-07T19:36:36Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1036123`, label Duganella sp. MICO-M, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read independently. It contains eleven ancestors, genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, one NCBI name attestation and `strain_count: 0`. This count denotes inventoried BacDive strains, not cultivation status or the number of deposits reported elsewhere.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/duganella_sp_mico_m.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/duganella_sp_mico_m.yaml --out /private/tmp/dmicom-strict.tsv`: exit 0; one file, zero errors. The diagnostic TSV was read and contains only its header.
- Structured source comparisons verified every backbone field, all eleven ancestors, the attestation, scope entry and unique path mapping. The pinned backbone has no descendants for this taxon. Exact type-material, merged-ID and dropped-ID searches returned no target rows. These bounded comparisons are not full-corpus reproduction.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. No target graph or standalone history record occurs in the bounded checks, so their specialized checks have no target. No focused substitute for a full-corpus gate was invented.

## Identity and Grounding

Live NCBI Taxonomy EFetch agrees on identifier, exact name, species rank, bacterial division, code 11 and parent `NCBITaxon:2636909`, unclassified Duganella. Datasets confirms all eleven ancestor IDs, including root. Pinned and live lineage names/ranks agree: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Oxalobacteraceae, Telluria group, Duganella and unclassified Duganella. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036123), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036123).

The native name catalog contains the scientific name. Empty synonyms, nomenclature and mappings agree with the available inventories. Species rank does not establish formal nomenclatural standing. MICO-M must remain distinct from MICO-C and MICO-M2; shared prefix or article membership does not establish identity.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:222264` matches identity, rank, parent, code, empty synonym fields, sole NCBI source and snapshot 2026-09-13. The native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31779`.
- `data/taxa/PATHS.tsv:14765` uniquely maps the identifier to this slug. `curation/seed_scope.tsv:322520` gives the one-source attested inclusion reason and date 2026-09-13.
- Exact-taxonomy Nucleotide search returned three entries. All non-sequence/non-translation metadata were inspected: [HQ616148.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616148.1), 1,372 bases of partial 16S rRNA; [HQ616155.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616155.1), a 1,062-base partial gyrB CDS; and [HQ616162.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616162.1), a 942-base partial vioA CDS. Each explicitly names MICO-M, taxon 1036123 and olive rhizosphere as isolation source. These marker fragments are not assemblies. Their metadata give no culture, BioSample or BioProject accession.
- The two CDS entries identify proteins AEJ88325.1 and AEH95317.1 respectively, both with codon start 1 and translation table 11. All markers cite Aranda, Montes-Borrego and Landa's 2011 Microbial Ecology article, `PMID:21424823`, `DOI:10.1007/s00248-011-9840-9`, and an IAS-CSIC direct submission dated 14 November 2010. The publisher metadata and abstract were inspected, and the complete PubMed EFetch citation/abstract retrieved earlier in this review run was reread for MICO-M. The paper supplies seven-isolate context; GenBank supplies the explicit marker-to-isolate chain. No quantitative phenotype was inferred merely from cohort membership. [PubMed](https://pubmed.ncbi.nlm.nih.gov/21424823/), [primary article](https://link.springer.com/article/10.1007/s00248-011-9840-9).
- The primary patent description explicitly assigns Mico-M to CECT 7781, deposited on 13 October 2010, and places it among cultivated-olive isolates. CECT 7779 and CECT 7780 instead belong to LO-22 and CICYT-60. This supports a bounded optional deposit enrichment lead; it does not create a BacDive record or verify current culture availability. [Primary patent description](https://patents.google.com/patent/WO2012062951A1/es).
- Exact-taxonomy Assembly search returned zero items with phrase-not-found/no-items warnings. This is only the result of that exact query, not proof that no genome exists under any identifier.
- The seed event agrees with the scope and source inventories. Its `2026-09-13T17:54:04Z` timestamp is the latest raw/ATB/StrainInfo extraction timestamp, consistent with `src/taxonmech/seed.py:139`. It represents seeding, not human review.

## Completeness

Exact BacDive comparison returned no target row, and the pinned backbone has no descendants, supporting the zero inventoried strain count. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits comparisons also returned no target row. The patent's explicit CECT deposit does not contradict the BacDive-specific count.

The gitignore-independent search used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Patterns covered digit-bounded 1036123, MICO-M variants matching the label and slug, CECT 7781 spacing/URL variants, the three nucleotide accessions, both protein accessions, PMID 21424823 and the article DOI. All six candidate rows/objects were inspected completely; the previously retrieved complete AllTheBacteria collision row was reread for this target. Five SOURCE.json files were parsed separately and history filenames checked independently. No supported target culture/genome link, additional curation overlay or standalone history record was found within those roots. The patent deposit evidence is external to those inventories.

Optional literature, marker or deposit enrichment is not a missing required representation under the local checklist. The YAML makes no gene-function, regulator, transcriptomic, mechanism or dataset claim. iModulonDB is not applicable; absence from it is not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, attestation, source-specific strain count and seeded provenance are supported. The external deposit lead and namespace collisions do not reveal an unsupported assertion in the current YAML.

## Recommended Edits

None required. Preserve the generated YAML and seed event. Optional CECT 7781 or marker enrichment belongs in maintained source/extractor inputs or an appropriate durable curator representation, retaining the explicit identifier-to-MICO-M evidence. Do not inflate BacDive counts or borrow another isolate's deposit.

## Follow-up Checks

Before any future deposit enrichment, verify the primary CECT catalog or deposit documentation against MICO-M and retain the evidence separately from BacDive provenance. Any later maintained-input change should be followed by schema/strict validation and the documented corpus/provenance gates. Do not patch generated output directly.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The YAML was byte-identical before report creation. Existing worktrees and the closed parallel session's work were left intact.
- GenBank catalog `data/catalog/ncbi_genbank-0031.jsonl.gz:15605` and BV-BRC `data/bvbrc/bvbrc-0018.jsonl.gz:45686` concern Corynebacterium sp. SFY-K9, taxon 3092263, assembly GCA_033598475.1 and sample SAMN38113680. The matching digits are in BioProject PRJNA1036123, not this taxon identifier. Both complete native objects were read.
- AllTheBacteria row 2144407 is Streptococcus suis sample SAMN21424823, run SRR15886619, analysis ERZ26421993. Its sample accession matches the PMID digits in a different namespace, not MICO-M.
- The original publisher article requires subscription access; metadata and abstract were inspected, not its full experimental tables. The browser PubMed view was incomplete; the inspected structured EFetch result supplied citation and abstract. No access restriction was bypassed.
- No complete experimental-table audit, sequence alignment, current culture availability check or taxonomic reassignment was performed. Patent text was used for explicit deposit identity and origin, not legal status or quantitative efficacy. Search snippets alone were not used to support claims.
- Only this new report was written for the target. No YAML, source inventory, history/lifecycle or GitHub state was changed.
