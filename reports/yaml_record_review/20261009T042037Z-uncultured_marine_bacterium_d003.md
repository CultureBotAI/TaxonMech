# YAML Record Review: uncultured marine bacterium D003

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d003.yaml`
- Started UTC: 2026-10-09T04:15:57Z
- Finished UTC: 2026-10-09T04:20:37Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:103660`: species rank, Bacteria, parent `NCBITaxon:150608`, five root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It has zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior target report. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d003.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d003.yaml --out /private/tmp/taxonmech-d003-review-strict.tsv`: passed, one file and zero errors; full TSV was header-only.
- Structured comparisons matched backbone, all ancestors, attestation, PATHS, scope and seed wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Marker annotation consistency passed: declared/actual length 559, submitted rRNA transcription equals DNA and no non-ACGT symbols. This is not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. Embedded history was inspected; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103660&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103660) agree with identifier, name, rank and ancestor chain. EFetch additionally verifies parent and genetic code; Datasets includes root in its five ancestor IDs.

The lineage is root, cellular organisms, Bacteria, environmental samples and marine bacteria D ensemble. Its sparse classification is carried from NCBI, not a seeder omission to repair by inference. EFetch supplies no other names; pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children. Species rank for this environmental concept does not establish formal nomenclatural standing, a cultured strain or a complete genome.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:18525`: identity, rank, parent, genetic code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0000.jsonl.gz:38541`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15049`: identifier/slug.
- `curation/seed_scope.tsv:144169`: admission date/reason matching the seed event.

One `NAME` attestation counts a source name, not an experiment or genome. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` counts represented BacDive entries, not environmental clone labels.

Exact Nuccore query `txid103660[Organism:noexp]` returned only UID 5882262. Complete [AF177547.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177547.1) XML was read, including references, all features and sequence. It is a 559-base partial 16S marker with both feature ends partial. Six source qualifiers identify the organism, genomic DNA, taxon 103660, clone D003, environmental sampling and surface-associated marine origin. No strain, culture-deposit, host, geographic or genome qualifier is supplied. References name Dang and Lovell's 2000 paper and a 13-AUG-1999 direct submission from the University of South Carolina; the submission address is not collection locality.

[PMID 10653705](https://pubmed.ncbi.nlm.nih.gov/10653705/) was verified through full abstract/metadata, including DOI 10.1128/AEM.66.2.467-475.2000 and PMC91850. Inspected [publisher methods and Table 1](https://journals.asm.org/doi/10.1128/AEM.66.2.467-475.2000) report D003 on six surfaces at 24 hours and three at 72 hours in Clam Bank Creek, South Carolina. These cultivation-independent clone frequencies are not growth rates.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, deposits, genome links and graphs are appropriately unasserted without explicit identity/evidence chains. The clone-level publication is an optional enrichment opportunity, not a missing required slot.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms included word-bounded taxid 103660, label/slug and D003 with optional hyphen, space or underscore. Expansion added AF177547 and word-bounded UID 5882262. Initial search returned 26 rows; expansion returned 29: three own taxonomy/name/scope rows and 26 exclusions. All candidate rows were read completely in native structured form, including common fields and lossless per-row differences. Five SOURCE.json files were fully parsed for both term sets; history filenames were independently inventoried.

Excluded candidates comprised:

- BacDive 103660, Rhodococcus sp. ST029981 (194249), in raw and native records. SOURCE.json requested IDs/URLs use the BacDive namespace, not NCBI taxids.
- CIP 103660, Gardnerella vaginalis (2702), represented by BacDive 135327, StrainInfo SI-ID 42321 / SI-DP 151234 and GOLD Go0287262. Native records name ATCC 49145 and ACM 4765 as other deposits; related strain aliases include AmMS117. StrainInfo explicitly links JQ354969, GCA_003034925 and GCA_001913835 to ATCC 49145 / SI-DP 113837, not to the target clone. BacDive's associated IMG/BV-BRC identifiers and the projected culture/GOLD/StrainInfo rows remain part of that separate strain chain.
- StrainInfo SI-ID 38359 / SI-DP 103660, Leucothrix mucor ATCC 25111 (45248), a provider deposit ID rather than the target taxid. A separate SOURCE.json match is a response byte count of 103660, not an identity assertion.
- GOLD Go0702537 / Gp0825833, Panicum virgatum D003.C (38727), a plant resequencing project, not this environmental bacterium.
- GenBank/RefSeq GCA/GCF_901521535.1 and its GTDB row, Klebsiella variicola isolate k_variicola_1 (244366), assembly name KLP-ELB-HUB-103660; and GCA_009531115.1, Salmonella enterica serovar Heidelberg strain 103660 (611).
- Four GTDB rows where 103660 is a contig/scaffold statistic: GCA_021158125.1, Candidatus Bathyarchaeota archaeon (2026714); GCA_052270635.1, Candidatus Cryptobacteroides bacterium (3085639); GCF_000154885.1, Streptomyces sp. Mg1 (465541); and GCF_009893025.1, Enterococcus mundtii (53346).
- Three expanded-search rows for GCA/GCF_004794015.1, Pseudomonas fluorescens LoriBL (294), including the suppressed historical RefSeq record and GTDB classification as Aquipseudomonas rhodesiae. Here 5882262 is genome length, not the target marker UID. The upstream classification discrepancy is unrelated to D003.

`D003[All Fields] AND txid150608[Organism]` returned only the own marker. Its translation stack reports 291 unfiltered D003 matches; that cross-organism set was not exhaustively audited. Exact non-expanded Assembly search returned zero with missing-phrase/no-items diagnostics. PubMed `AF177547[All Fields]` returned the verified own paper.

PubMed `D003[All Fields] AND bacterium[All Fields]` returned one other candidate. Full abstract/metadata for [PMID 11948628](https://pubmed.ncbi.nlm.nih.gov/11948628/) identifies D-003 as a mixture of long-chain fatty acids from sugar-cane wax tested in cytotoxicity/genotoxicity assays, not a marine clone. It supplies no target identity chain. This exclusion is not an exhaustive literature-absence claim.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence. Absence statements are bounded to the stated roots, terms and indexes.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. The record does not conflate clone evidence, culture deposits, provider identifiers, plant samples, assembly statistics or an unrelated chemical-mixture name.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Never join on a bare D003 label or unnamespaced 103660.

## Follow-up Checks

No corrective follow-up is needed for current claims. Optional enrichment should preserve clone-level provenance and distinguish deployment conditions from culture properties. Finer taxonomic placement requires upstream review, not hand-editing lineage. No independent alignment, full experimental reanalysis, genome comparison or PDF/figure visual verification is claimed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:103660`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and checklist governed this independent review. Complete YAML, own source rows, all local candidates, live taxonomy, the own marker, primary publisher methods/table text and both stated PubMed abstracts/metadata were inspected. No neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `8fbe5fca6ef26893eb724f64e529625b35eae742fa05a6301e5c4716ae7fc3b8`. Only this new report was written for the target. This review did not modify YAML, sources, history, status, pages, GitHub objects, Eukaryota or worktrees.
