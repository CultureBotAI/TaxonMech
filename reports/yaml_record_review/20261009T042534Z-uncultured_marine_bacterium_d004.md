# YAML Record Review: uncultured marine bacterium D004

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d004.yaml`
- Started UTC: 2026-10-09T04:22:03Z
- Finished UTC: 2026-10-09T04:25:34Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:103661`: species rank, Bacteria, parent `NCBITaxon:150608`, five root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It has zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior target report. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d004.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d004.yaml --out /private/tmp/taxonmech-d004-review-strict.tsv`: passed, one file and zero errors; full TSV was header-only.
- Structured comparisons matched backbone, all ancestors, attestation, PATHS, scope and seed wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Marker annotation consistency passed: declared/actual length 559, submitted rRNA transcription equals DNA and no non-ACGT symbols. This does not independently validate alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. Embedded history was inspected; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103661&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103661) agree with identifier, name, rank and ancestor chain. EFetch additionally verifies parent and genetic code; Datasets includes root in its five ancestor IDs.

The lineage is root, cellular organisms, Bacteria, environmental samples and marine bacteria D ensemble. This sparse classification is carried from NCBI, not a seeder omission to repair by inference. EFetch supplies no other names; pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children. Species rank for this environmental concept does not establish formal nomenclatural standing, a cultured strain or a complete genome. Oxynema aestuarii AP17, whose synonyms include BDU D004, is a separate taxon, not an alternate identity for this record.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:18526`: identity, rank, parent, genetic code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0000.jsonl.gz:38542`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15050`: identifier/slug.
- `curation/seed_scope.tsv:144170`: admission date/reason matching the seed event.

One `NAME` attestation counts a source name, not an experiment or genome. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` counts represented BacDive entries, not environmental clone labels.

Exact Nuccore query `txid103661[Organism:noexp]` returned only UID 5882263. Complete [AF177548.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177548.1) XML was read, including references, all features and sequence. It is a 559-base partial 16S marker with both feature ends partial. Six source qualifiers identify the organism, genomic DNA, taxon 103661, clone D004, environmental sampling and surface-associated marine origin. No strain, culture-deposit, host, geographic or genome qualifier is supplied. References name Dang and Lovell's 2000 paper and a 13-AUG-1999 direct submission from the University of South Carolina; that submission address is not collection locality.

[PMID 10653705](https://pubmed.ncbi.nlm.nih.gov/10653705/) was verified through full abstract/metadata, including DOI 10.1128/AEM.66.2.467-475.2000 and PMC91850. Inspected [publisher methods and Table 1](https://journals.asm.org/doi/10.1128/AEM.66.2.467-475.2000) report D004 on five surfaces at 24 hours and six at 72 hours in Clam Bank Creek, South Carolina. These cultivation-independent clone frequencies are not growth rates.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, deposits, genome links and graphs are appropriately unasserted without explicit identity/evidence chains. The clone-level publication is an optional enrichment opportunity, not a missing required slot.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms included word-bounded taxid 103661, label/slug and D004 with optional hyphen, space or underscore. Expansion added AF177548 and word-bounded UID 5882263. Both searches returned the same 27 rows: three own taxonomy/name/scope rows and 24 exclusions. All candidate rows were read completely in native structured form, including common fields and lossless per-row differences. Five SOURCE.json files were fully parsed for both term sets; history filenames were independently inventoried.

Excluded candidates comprised:

- BacDive 103661, Rhodococcus sp. ST029982 (194249), in raw and native records. SOURCE.json requested IDs/URLs use the BacDive namespace, not NCBI taxids.
- CIP 103661, Haemophilus influenzae (727), represented by BacDive 137251, StrainInfo SI-ID 42320 / SI-DP 151457 and GOLD Go0244793. Native records name ATCC 49144 / SI-DP 113835 and ACM 4761 / SI-DP 667091 as other deposits; aliases include AmMS120 and NZRM3416. Culture, GOLD and StrainInfo projections retain that explicit strain chain, not a link to D004. The inspected native BacDive and StrainInfo records supply no sequence entries.
- StrainInfo SI-ID 38360 / SI-DP 103661, Leucothrix mucor ATCC 25112 (45248), a provider deposit identifier rather than the target taxid.
- StrainInfo SI-ID 106368, designation FP 103661-S, with KCTC 6665 / SI-DP 316694 and ATCC 42463 / SI-DP 316695. Its native record has no taxon assignment or sequences, so no organism identity is inferred from the shared numeral.
- Backbone and equivalent-name rows for Oxynema aestuarii AP17 (2064643), including Oscillatoria sp. BDU D004, plus four NFMC BDU D004 spelling variants in reference-strain rows for Oxynema aestuarii (2874213). These explicitly belong to the cyanobacterial taxon, not NCBITaxon:103661.
- GenBank/RefSeq GCA/GCF_901521565.1 and its GTDB row, Klebsiella variicola isolate k_variicola_2 (244366), assembly name KLP-ELB-HUB-103661, BioSample SAMEA5605369.
- GCA_007609695.1, Salmonella enterica serovar Braenderup strain 103661 (149391), not the environmental clone.

`D004[All Fields] AND txid150608[Organism]` returned only the own marker. Its translation stack reports 288 unfiltered D004 matches; that cross-organism set was not exhaustively audited. Exact non-expanded Assembly search returned zero with missing-phrase/no-items diagnostics. PubMed `D004[All Fields] AND bacterium[All Fields]` returned zero, while `AF177548[All Fields]` returned the verified own paper. The label-query miss is not a literature-absence claim.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence. Absence statements are bounded to the stated roots, terms and indexes.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. The record does not conflate the environmental clone with similarly named cyanobacteria, culture deposits, provider IDs, unclassified source records or unrelated assemblies.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Never join on a bare D004 label or unnamespaced 103661.

## Follow-up Checks

No corrective follow-up is needed for current claims. Optional enrichment should preserve clone-level provenance and distinguish deployment conditions from culture properties. Finer taxonomic placement requires upstream review, not hand-editing lineage. No independent alignment, full experimental reanalysis, genome comparison or PDF/figure visual verification is claimed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:103661`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and checklist governed this independent review. Complete YAML, own source rows, all local candidates, live taxonomy, the own marker, primary publisher methods/table text and full own PubMed abstract/metadata were inspected. No neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `e8e7a888bf084c4c3b0a16821927c071281c6f9f96e53631a9277fbe0331dcb1`. Only this new report was written for the target. This review did not modify YAML, sources, history, status, pages, GitHub objects, Eukaryota or worktrees.
