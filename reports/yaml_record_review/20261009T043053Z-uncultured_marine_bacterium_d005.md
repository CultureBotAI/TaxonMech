# YAML Record Review: uncultured marine bacterium D005

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d005.yaml`
- Started UTC: 2026-10-09T04:27:00Z
- Finished UTC: 2026-10-09T04:30:53Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:103662`: species rank, Bacteria, parent `NCBITaxon:150608`, five root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It has zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior target report. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d005.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d005.yaml --out /private/tmp/taxonmech-d005-review-strict.tsv`: passed, one file and zero errors; full TSV was header-only.
- Structured comparisons matched backbone, all ancestors, attestation, PATHS, scope and seed wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Marker annotation consistency passed: declared/actual length 559, submitted rRNA transcription equals DNA and no non-ACGT symbols. This does not independently validate alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. Embedded history was inspected; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103662&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103662) agree with identifier, name, rank and ancestor chain. EFetch additionally verifies parent and genetic code; Datasets includes root in its five ancestor IDs.

The lineage is root, cellular organisms, Bacteria, environmental samples and marine bacteria D ensemble. This sparse classification is carried from NCBI, not a seeder omission to repair by inference. EFetch supplies no other names; pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children. Species rank for this environmental concept does not establish formal nomenclatural standing, a cultured strain or a complete genome. The separate Tateyamaria sp. D005 entry must not be joined by its bare strain label.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:18527`: identity, rank, parent, genetic code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0000.jsonl.gz:38543`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15051`: identifier/slug.
- `curation/seed_scope.tsv:144171`: admission date/reason matching the seed event.

One `NAME` attestation counts a source name, not an experiment or genome. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` counts represented BacDive entries, not environmental clone labels.

Exact Nuccore query `txid103662[Organism:noexp]` returned only UID 5882264. Complete [AF177549.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177549.1) XML was read, including references, all features and sequence. It is a 559-base partial 16S marker with both feature ends partial. Six source qualifiers identify the organism, genomic DNA, taxon 103662, clone D005, environmental sampling and surface-associated marine origin. No strain, culture-deposit, host, geographic or genome qualifier is supplied. References name Dang and Lovell's 2000 paper and a 13-AUG-1999 direct submission from the University of South Carolina; the submission address is not collection locality.

[PMID 10653705](https://pubmed.ncbi.nlm.nih.gov/10653705/) was verified through full abstract/metadata, including DOI 10.1128/AEM.66.2.467-475.2000 and PMC91850. Inspected [publisher methods and Table 1](https://journals.asm.org/doi/10.1128/AEM.66.2.467-475.2000) report D005 on five surfaces at 24 hours and six at 72 hours in Clam Bank Creek, South Carolina. These cultivation-independent clone frequencies are not growth rates.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, deposits, genome links and graphs are appropriately unasserted without explicit identity/evidence chains. The clone-level publication is an optional enrichment opportunity, not a missing required slot.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms included word-bounded taxid 103662, label/slug and D005 with optional hyphen, space or underscore. Expansion added AF177549 and word-bounded UID 5882264. Both searches returned the same 28 rows: three own taxonomy/name/scope rows and 25 exclusions. Every candidate row was read completely in native structured form, including common fields and lossless per-row differences. Five SOURCE.json files were fully parsed for both term sets; history filenames were independently inventoried.

Excluded local candidates comprised:

- Backbone, scope and scientific-name rows for Tateyamaria sp. D005 (943938), whose source parent is unclassified Tateyamaria (2645127), rather than marine bacteria D ensemble.
- BacDive 103662, Rhodococcus sp. ST030058 (194249), in raw and native records. SOURCE.json requested IDs/URLs use the BacDive namespace, not NCBI taxids.
- CIP 103662, Aggregatibacter aphrophilus (732), represented by BacDive 135329, StrainInfo SI-ID 42322 / SI-DP 151559 and GOLD Go0263274. Native records retain ATCC 49146 / SI-DP 113839 and ACM 4762 / SI-DP 667100 under Haemophilus paraphrophilus wording, with aliases AmMS115 and NZRM3417. The explicit deposit/taxon chain, culture and related-record projections concern that strain, not the marine clone. Inspected native BacDive and StrainInfo records provide no sequence entries.
- GenBank/RefSeq GCA/GCF_901521635.1 and its GTDB row, Klebsiella variicola isolate k_variicola_3 (244366), assembly name KLP-ELB-HUB-103662, BioSample SAMEA5605370.
- GCA_009576945.1, Salmonella enterica serovar Corvallis strain 103662 (593905), not the environmental clone.
- Six GTDB rows where 103662 is a contig/scaffold N50: GCF_013868335.1, Staphylococcus aureus (1280); GCF_002134155.1, Escherichia coli (562); GCA_043421755.1, Xylella fastidiosa subsp. multiplex (644357); GCA_017470485.1, Synergistaceae bacterium (2053624); and GCA_948831505.1 / GCA_948629255.1, uncultured Muribaculaceae bacterium (2301481). These statistics do not establish target identity.

The Tateyamaria near match was checked beyond local naming. Exact `txid943938[Organism:noexp]` Nuccore search returned one entry, UID 317408448. Complete [HQ336493.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ336493.1) XML identifies a 1,381-base partial 16S sequence, strain D005 and taxon 943938. Its Lee/Lee/Lee submission is dated 09-SEP-2010, from POSTECH in Korea, with an unpublished study title concerning Ullungdo and Dokdo. This differs from the reviewed clone's 1999 Dang/Lovell submission and AF177549 accession; no explicit identity chain links them. No sequence-alignment or species-equivalence conclusion was drawn.

`D005[All Fields] AND txid150608[Organism]` returned only the own marker. Its translation stack reports 358 unfiltered D005 matches; that cross-organism set was not exhaustively audited. Exact non-expanded Assembly search returned zero with missing-phrase/no-items diagnostics. PubMed `D005[All Fields] AND bacterium[All Fields]` returned zero. `AF177549[All Fields]` also returned zero with a missing-phrase diagnostic, despite the explicit GenBank PMID and inspected primary paper. These index misses are not evidence that literature is absent or the sequence citation is invalid.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence. Absence statements are bounded to the stated roots, terms and indexes.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. The record does not conflate an environmental clone, a later similarly named strain, culture deposits, provider IDs or genome statistics. PubMed indexing limitations do not alter the supported seed claims.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Never join on a bare D005 label or unnamespaced 103662.

## Follow-up Checks

No corrective follow-up is needed for current claims. Optional enrichment should preserve clone-level provenance, retain the direct GenBank-to-PMID chain despite index misses and distinguish deployment conditions from culture properties. Finer taxonomic placement requires upstream review, not hand-editing lineage. No independent alignment, full experimental reanalysis, genome comparison or PDF/figure visual verification is claimed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:103662`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and checklist governed this independent review. Complete YAML, own source rows, all local candidates, live taxonomy, both specified marker records, primary publisher methods/table text and full own PubMed abstract/metadata were inspected. No neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `5c1859bd2b4e533f6dd08ba7f4814417a2003bf528b0ae6a00d6640f421b2a58`. Only this new report was written for the target. This review did not modify YAML, sources, history, status, pages, GitHub objects, Eukaryota or worktrees.
