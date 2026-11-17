# YAML Record Review: Duganella sp. CICYT-60

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/duganella_sp_cicyt_60.yaml`
- Started UTC: 2026-10-07T18:38:52Z
- Finished UTC: 2026-10-07T18:42:16Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1036119`, label Duganella sp. CICYT-60, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read independently. It carries eleven ancestors, genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, one NCBI name attestation and `strain_count: 0`. The count measures classified BacDive records, not whether the named isolate has been cultured or deposited elsewhere.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/duganella_sp_cicyt_60.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/duganella_sp_cicyt_60.yaml --out /private/tmp/dc60-strict.tsv`: exit 0; one file, zero error rows; diagnostic TSV contains only its header.
- Complete source-row comparisons verified identifier, label, rank, code, parent, full lineage, source attestation, scope reason and path mapping. No target descendants were found in the pinned backbone. These are bounded manual checks, not corpus reproduction.
- Exact type-material, merged-ID and dropped-ID checks returned no target rows.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. No target graph or standalone history record was found in the bounded searches, so their specialized validators have no target here. No focused replacement for a full-corpus gate was invented.

## Identity and Grounding

Live NCBI Taxonomy EFetch matches the identifier, exact name, species rank, genetic code 11 and parent `NCBITaxon:2636909` unclassified Duganella. NCBI Datasets confirms the identity and all eleven ancestor IDs, including root. The complete pinned lineage and live names/ranks agree: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Oxalobacteraceae, Telluria group, Duganella and unclassified Duganella. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036119), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036119).

The native name catalog supplies only the scientific name. Empty synonyms, nomenclature and mappings agree with the inventories. Species rank does not establish formal nomenclatural standing, and exact NCBI grounding does not assert identity with another olive isolate or a formally named Duganella species.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:222260` is the complete matching backbone row, including empty synonym fields, sole NCBI source and snapshot date 2026-09-13. The native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31775`.
- `data/taxa/PATHS.tsv:14760` uniquely maps the identifier to this slug. `curation/seed_scope.tsv:322516` supplies the attested-rule inclusion reason, one source and inclusion date 2026-09-13.
- Exact-taxonomy Nucleotide search found three records. All non-sequence/non-translation metadata were inspected: [HQ616146.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616146.1), a 1,374-base partial 16S rRNA sequence; [HQ616153.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616153.1), a 1,122-base partial gyrB CDS; and [HQ616160.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616160.1), an 879-base partial vioA CDS. Each names CICYT-60, taxon 1036119 and olive rhizosphere as the isolation source. These are gene fragments, not genome assemblies, and their metadata do not supply culture, BioSample or BioProject accessions.
- All three cite Aranda, Montes-Borrego and Landa's 2011 study, `PMID:21424823`, `DOI:10.1007/s00248-011-9840-9`, and the IAS-CSIC direct submission of 14 November 2010. Inspected PubMed and publisher metadata/abstract confirm the paper's identity and seven-isolate context. The exact strain-to-sequence linkage comes from GenBank; no quantitative phenotype or species equivalence was inferred from the cohort abstract. [PubMed](https://pubmed.ncbi.nlm.nih.gov/21424823/), [primary article](https://link.springer.com/article/10.1007/s00248-011-9840-9).
- The inspected Spanish description of patent WO2012062951A1 explicitly links CICYT-60 to CECT 7780, deposited on 14 September 2010. CECT 7779 and CECT 7781 refer to other isolates. This supplies a historical culture-identity lead, not proof of present availability, a BacDive identifier, a type strain or a genome accession. [Patent description](https://patents.google.com/patent/WO2012062951A1/es).
- Exact-taxonomy Assembly search returned zero items, with phrase-not-found/no-items warnings. This is a bounded query result; no universal genome-absence claim is made.
- The seed event matches the source and scope reason. Its `2026-09-13T17:54:04Z` timestamp equals the latest of the raw, ATB and StrainInfo extraction timestamps, as required by `src/taxonmech/seed.py:139`. It records seeding, not human review.

## Completeness

The exact-taxon BacDive inventory is empty and there are no backbone descendants, supporting zero inventoried strains. Exact source comparisons likewise found no target LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. The CECT deposit documented in the patent does not contradict this source-specific count or authorize inventing a BacDive strain identifier.

The gitignore-independent search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It covered the digit-bounded taxon number, CICYT-60 spelling variants, CECT 7780 separators including percent-encoded space, three nucleotide accessions, two associated protein accessions, PMID and DOI. All four resulting rows/objects were read completely. Five SOURCE.json files were parsed separately, and history filenames checked independently. Within these roots, no matching CECT 7780 source entry, supported target genome link, additional curation overlay or standalone history record was found.

Optional literature, culture and marker enrichment remains possible, but none is required to make this seeded record internally complete. No gene-function, regulator, transcriptomic or mechanism claim appears in the YAML, so iModulonDB is not applicable.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source scope, strain count and lifecycle provenance are supported. The external deposit lead is not a demonstrated error in the generated record.

## Recommended Edits

None required. Preserve the generated YAML and seed event. Optional enrichment should retain the explicit CICYT-60/CECT 7780 provenance in a maintained source or durable curator representation, rather than changing the BacDive count or inserting an unsupported strain entry.

## Follow-up Checks

Before adding CECT 7780, verify a current primary collection or supported source record and preserve its identifier namespace and exact isolate association. Any genome link additionally needs an explicit accession-to-deposit chain; neither patent membership nor shared taxonomy is sufficient. Source changes belong in the maintained extractor/seeder inputs, followed by schema/strict validation and the documented corpus/provenance gates.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The YAML remained byte-identical before report creation. Existing worktrees and the closed parallel session's work were left untouched.
- The expanded local search's fourth candidate was AllTheBacteria row 2144407: Streptococcus suis sample SAMN21424823, run SRR15886619 and ENA analysis ERZ26421993. This is a PMID-digit collision in a different namespace, not CICYT-60 evidence.
- The publisher's full article required subscription access; metadata and abstract were inspected. No complete experimental-table audit, sequence alignment or present-day CECT availability verification was performed. The patent was used for its explicit deposit provenance, not as a legal-status or independently verified quantitative phenotype source.
- Only this new report was written for the target. No YAML, source inventory, history/lifecycle or GitHub state was changed.
