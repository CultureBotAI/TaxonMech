# YAML Record Review: Aliarcobacter butzleri 7h1h

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/aliarcobacter_butzleri_7h1h.yaml`
- Started UTC: 2026-10-08T00:56:36Z
- Finished UTC: 2026-10-08T01:03:35Z
- Verdict: needs curation

## Target

The complete 87-line generated `TaxonRecord` was read. Its identifier is `NCBITaxon:1036172`, label `Aliarcobacter butzleri 7h1h`, rank `STRAIN`, domain `BACTERIA`, and parent `NCBITaxon:28197`. It is `EXACT`/`SEEDED`, with ten ancestors, four synonyms, one GTDB mapping/xref, genetic code 11, zero listed BacDive strains, three source attestations and one seed event.

This is one strain review, not a review of the species or of similarly matching source accessions. No generated YAML was edited.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/aliarcobacter_butzleri_7h1h.yaml` | Passed; no LinkML issues. |
| `just validate-strict data/taxa/bacteria/aliarcobacter_butzleri_7h1h.yaml --out /private/tmp/ab7-strict.tsv` | Passed; one file, zero errors; TSV header only. |
| Pinned backbone and lineage comparison | ID, label, rank, parent, code, all ten ancestors and all three NCBI synonyms agree. |
| Source, scope and path-index comparison | GTDB mapping/count, Madin count, scope admission and identifier-to-slug entry agree with their exact inventory rows. |
| Exact status checks | No merged, dropped or type-material row for this strain ID. No descendants in the pinned backbone. |
| Public NCBI Taxonomy and Datasets | Current identity, rank, parent and lineage agree; the strain has one assembly in Datasets. |
| Public assembly metadata | GCA_000215345.3 is current and paired with GCF_000215345.2; strain, sample and project metadata were inspected. |

These were bounded read-only checks, not a substitute for whole-corpus reproduction. Not run: `just verify-corpus`, full QC, source-provenance gates, product-label checks, rendering or documentation checks. No separate target history artifact was found in the ignored-inclusive search, so no external history file was submitted to its validator; the inline event was checked structurally. The record has no curator-added ontology graph requiring a separate focused term check.

The live GTDB genome and taxon pages were inaccessible through the web tool. Its current live species census was not verified. The pinned GTDB inventory and native genome object were inspected, and the report does not claim that 341 is a current-release count.

## Identity and Grounding

NCBI resolves 1036172 to strain 7h1h under species 28197. The three older `Arcobacter` name forms all retain 7h1h and are present in the pinned names and live taxonomy metadata. They do not collapse the strain into the species. The lineage is correctly carried from NCBI rather than replaced with GTDB's class label. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036172)

By contrast, `GTDB:s__Aliarcobacter_butzleri` is a species concept. Its presence as an `EXACT_SYNONYM` of this strain is an over-scoped identity assertion. The matching native GTDB genome `RS_GCF_000215345.2` classifies 7h1h in that species; membership does not make the entire species identical to 7h1h.

LPSN currently prefers the species combination `Arcobacter butzleri` and treats `Aliarcobacter butzleri` as a validly published homotypic synonym, with a qualification about recognition of the separate genus. That nomenclatural difference is retained here as context, not silently resolved by renaming the NCBI record. LPSN's type strain is represented by designations including ATCC 49616, DSM 8739 and RM 4018, not 7h1h. No species nomenclature or type status should be inherited into this strain merely from its parent. [LPSN species entry](https://lpsn.dsmz.de/species/aliarcobacter-butzleri)

## Evidence

The pinned backbone row at `data/raw/ncbitaxon_taxa.tsv:222298` supports the identity, aliases, code and source list. The matching raw GTDB row is `data/raw/gtdb_mappings.tsv:1452`, with `skos:closeMatch` and 341 genomes; Madin row `data/raw/madin_taxa.tsv:682` supplies five trait assertions. The YAML accurately copies those inventory values, but the GTDB identity interpretation still needs correction.

The three attestations have distinct units: NCBI 1 NAME, GTDB 341 GENOME, and Madin 5 TRAIT_ASSERTION. The extractor counts assemblies belonging to the GTDB species, not assemblies independently demonstrated to be 7h1h. The five Madin assertions are a coverage count, not five specified phenotypes in this YAML. There are no cited experimental passages or causal edges to verify.

Native source records independently retain this strain's genome context:

| Source | Inspected identity and linkage |
| --- | --- |
| NCBI current catalogs | GCA_000215345.3 and GCF_000215345.2, strain 7h1h, BioSample SAMN02604193. |
| NCBI historical catalogs | GCA_000215345.1 is suppressed; GCA_000215345.2 and GCF_000215345.1 are replaced. These are not additional current strain genomes. |
| GTDB | RS_GCF_000215345.2, species Aliarcobacter butzleri, explicit strain field 7h1h, not the species representative. |
| BV-BRC | Genome 1036172.3 links to GCA_000215345.3, PRJNA67167 and SAMN02604193; the source retains the older Arcobacter label. |
| GOLD | Go0011272 -> Gp0011272 -> Ga0016973; project sample SAMN02604193, project PRJNA67167, analysis GCA_000215345/CP006615 and IMG 2541046991. |

The GOLD organism's culture-collection field is empty and the relevant source strain fields contain only 7h1h. Such native catalog associations are useful, but do not supply a missing eligible BacDive/culture-deposit join. GOLD's taxon attestation is explicitly KGX-derived, whereas the primary workbook supports separate strain/project relationships; a native GOLD object does not automatically create a raw attestation row under the current documented pipeline.

Live NCBI confirms the current complete assembly, the versioned RefSeq pair, the BioSample and PRJNA67167 association. Its source identifies 7h1h as collected in the United Kingdom in 2007 from healthy dairy-cattle feces. The public metadata supplies no culture-collection identifier; those source details are not additional YAML habitat, host or phenotype assertions. No genome sequence or annotation-content audit was performed. [NCBI assembly](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000215345.3/)

## Completeness

`strain_count: 0` means zero supported BacDive entries in this record's classified subtree, not that strain 7h1h or its genome does not exist. Exact inventory checks and native-catalog searches found no BacDive entry or eligible deposit link for the target. No strains are hidden by a listing cap. Do not fabricate a BacDive ID or turn the bare laboratory designation into a collection accession to populate the nested genome slots.

Ignored-inclusive, compressed-input searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. They used the taxon ID, 7h1h/name/slug, then discovered assembly, chromosome, sample, project and GOLD/IMG identifiers. All 35 candidate addresses were inspected: 19 target-context rows and 16 unrelated longer WGS-accession substring matches. No candidate was accepted on substring similarity.

Resolution across `data/taxa`, `curation`, `history` and `reports` found one target YAML, its scope/index/legacy-path references and no prior target report. The five source metadata JSON files and history filenames were also checked. These are bounded repository searches, not a claim of universal absence from every public resource.

The record asserts no strain-specific LPSN nomenclature, mechanism, expression module or causal graph, so their empty optional slots are not independent defects. iModulonDB was not applicable to this identity-only record; its absence was not used as negative evidence.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: the broader GTDB species is promoted to strain identity.** YAML line 43 carries `skos:closeMatch`; lines 46-49 make the species name an exact synonym, and line 60 supplies the associated xref. The GTDB attestation at lines 70-75 repeats the species-wide count without clarifying this rank mismatch. The primary NCBI identifier and label are correct, so this is a scope-inflation finding rather than a wrong-record blocker. The source inventory supplies the mapping, but `src/taxonmech/seed.py:451` treats every close match as identity and line 468 emits the exact synonym without checking rank. Maintained owners: the identity/mapping handling in `src/taxonmech/seed.py`, the extraction contract at `src/taxonmech/extract.py:501`, and the upstream kg-microbe GTDB mapping transform identified by `conf/sources.yaml`. Do not patch the generated TSV/YAML or invent a replacement count.

## Recommended Edits

1. Make GTDB identity promotion rank-aware in the seeder. Preserve the source species-membership evidence while removing the unsupported exact species synonym and unqualified identity xref from this strain. Review the mapping and its attestation together.
2. Review the upstream species-to-strain mapping semantics before changing the predicate. Do not blindly substitute `broadMatch`: this repository uses it for an upstream pooling condition, so any revised relation needs an explicit tested contract.
3. Add a strain-versus-species regression fixture in `tests/test_seed.py`, preserving valid species-level identity cases. Keep the supported NCBI aliases and exact source counts scoped to their inventories. A future representation for genomes without BacDive deposits would be a separate model change, not justification to manufacture a deposit now.

## Follow-up Checks

After an authorized change to maintained code/input, run the focused seed tests and dry-run seed, then the documented `just seed-canary NCBITaxon:1036172` workflow. Inspect the regenerated biological diff and rerun both focused validators above. Assert that species membership no longer produces an exact strain synonym or unqualified identity xref, and that the attestation does not imply 341 strain-specific genomes.

Test ordinary species identity mappings, pooling cases and strain records with no eligible deposits before broader regeneration. Before publication, run the full documented corpus, QC, product, rendering, documentation and provenance gates. Retry live GTDB verification when accessible without rewriting a pinned count from an unrelated release.

## Additional Notes

The single seed event remains `2026-09-13T17:54:04Z`; scope admission is `2026-09-12`. No lifecycle promotion, curation event, external history record, source refresh, generated product or GitHub mutation was performed. Eukaryota was not reviewed again.

Reviewed HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The YAML retained SHA256 `2977b96c33db1d7b00ace8eeb70127bf8a6cde12f8beb24685d89f8555899e8a` before report creation. Only this new report was written for this review.
