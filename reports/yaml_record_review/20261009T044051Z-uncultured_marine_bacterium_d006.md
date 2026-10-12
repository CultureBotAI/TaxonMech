# YAML Record Review: uncultured marine bacterium D006

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d006.yaml`
- Started UTC: 2026-10-09T04:35:43Z
- Finished UTC: 2026-10-09T04:40:51Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:103663`: species rank, Bacteria, parent `NCBITaxon:150608`, five root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It has zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior target report. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d006.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d006.yaml --out /private/tmp/taxonmech-d006-review-strict.tsv`: passed, one file and zero errors; full TSV was header-only.
- Structured comparisons matched backbone, all ancestors, attestation, PATHS, scope and seed wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Marker annotation consistency passed: declared/actual length 559, submitted rRNA transcription equals DNA and no non-ACGT symbols. This is not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. Embedded history was inspected; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103663&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103663) agree with identifier, name, rank and ancestor chain. EFetch additionally verifies parent and genetic code; Datasets includes root in its five ancestor IDs.

The lineage is root, cellular organisms, Bacteria, environmental samples and marine bacteria D ensemble. Its sparse classification is carried from NCBI, not a seeder omission to repair by inference. EFetch supplies no other names; pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children. Species rank for this environmental concept does not establish formal nomenclatural standing, a cultured strain or a complete genome. The separate uncultured bacterium D006 and Borreliella sp. D006 entries must not be joined by their bare labels.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:18528`: identity, rank, parent, genetic code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0000.jsonl.gz:38544`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15052`: identifier/slug.
- `curation/seed_scope.tsv:144172`: admission date/reason matching the seed event.

One `NAME` attestation counts a source name, not an experiment or genome. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` counts represented BacDive entries, not environmental clone labels.

Exact Nuccore query `txid103663[Organism:noexp]` returned only UID 5882265. Complete [AF177550.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177550.1) XML was read, including references, all features and sequence. It is a 559-base partial 16S marker with both feature ends partial. Six source qualifiers identify the organism, genomic DNA, taxon 103663, clone D006, environmental sampling and surface-associated marine origin. No strain, culture-deposit, host, geographic or genome qualifier is supplied. References name Dang and Lovell's 2000 paper and a 13-AUG-1999 direct submission from the University of South Carolina; the submission address is not collection locality.

[PMID 10653705](https://pubmed.ncbi.nlm.nih.gov/10653705/) was verified through full abstract/metadata, including DOI 10.1128/AEM.66.2.467-475.2000 and PMC91850. Inspected [publisher methods and Table 1](https://journals.asm.org/doi/10.1128/AEM.66.2.467-475.2000) report D006 in three surface libraries at each sampling time, with different surface combinations, at Clam Bank Creek, South Carolina. These cultivation-independent clone frequencies are not growth rates.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, deposits, genome links and graphs are appropriately unasserted without explicit identity/evidence chains. The clone-level publication is an optional enrichment opportunity, not a missing required slot.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms included word-bounded taxid 103663, label/slug and D006 with optional hyphen, space or underscore. Expansion added AF177550 and word-bounded UID 5882265. Initial search returned 28 rows; expansion returned 29: three own taxonomy/name/scope rows and 26 exclusions. Every candidate row was read completely in native structured form, including common fields and lossless per-row differences. Five SOURCE.json files were fully parsed for both term sets; history filenames were independently inventoried.

Excluded local candidates comprised:

- Backbone, scope and scientific-name rows for uncultured bacterium D006 (90430), parent 48479, and Borreliella sp. D006 (3448911), parent 2645750. Neither source asserts equivalence to taxon 103663.
- BacDive 103663, Rhodococcus sp. ST030062 (194249), in raw and native records. SOURCE.json requested IDs/URLs use the BacDive namespace, not NCBI taxids.
- CIP 103663, Klebsiella oxytoca (571), represented by BacDive 135330, StrainInfo SI-ID 46104 / SI-DP 151760 and GOLD Go0285541. Native records also name ATCC 49473 / SI-DP 124998 and alias AmMS247. StrainInfo assigns EU623143 through EU623153 specifically to ATCC 49473; these are rRNA-region/tRNA records, not marine-clone or genome evidence. Culture and related-record projections retain that separate strain chain.
- StrainInfo SI-ID 38361 / SI-DP 103663, ATCC 25113, classified as Mycobacterium terrae (1788). The grouped CT1969-01686 / SI-DP 51505 deposit is classified as Mycobacterium sinense (875328). That source-level classification difference is preserved, but neither deposit supplies target evidence.
- GenBank/RefSeq GCA/GCF_901521575.1 and its GTDB row, Klebsiella variicola isolate k_variicola_4 (244366), assembly name KLP-ELB-HUB-103663, BioSample SAMEA5605371.
- GCA_009216145.1 and BV-BRC 90370.4508, Salmonella enterica serovar Typhi strain 103663 (90370). Shared naming does not independently establish equivalence between those two genome records, and neither concerns the marine clone.
- GTDB GCF_037784115.1, Acinetobacter baumannii SUD-CH-P1 (470), where 103663 is contig/scaffold N50.
- Expanded-search GCA_045902075.1, Klebsiella pneumoniae strain 2024CE-CRO_12_02_001 (573), where 5882265 is genome length rather than the target marker UID.

The uncultured bacterium D006 near match was checked beyond local naming. Exact `txid90430[Organism:noexp]` Nuccore search returned UID 4530525. Complete [AF125201.1](https://www.ncbi.nlm.nih.gov/nuccore/AF125201.1) XML identifies a 1,475-base 16S sequence and an environmental clone from the oral cavity, taxon 90430. It names Paster and Dewhirst, an unpublished oral-cavity study and a 02-FEB-1999 Forsyth Dental Center submission. This is not the reviewed marine clone's Dang/Lovell accession or provenance. No alignment or species-equivalence conclusion was drawn.

`D006[All Fields] AND txid150608[Organism]` returned only the own marker. Its translation stack reports 233 unfiltered D006 matches; that cross-organism set was not exhaustively audited. Exact non-expanded Assembly search returned zero with missing-phrase/no-items diagnostics. PubMed `AF177550[All Fields]` returned zero with a missing-phrase diagnostic despite the explicit GenBank PMID and inspected primary paper; the index miss is not literature-absence evidence.

PubMed `D006[All Fields] AND bacterium[All Fields]` returned [PMID 40770677](https://pubmed.ncbi.nlm.nih.gov/40770677/). Full abstract/metadata describes a clinical catheter-infection study, not this clone. Independently inspected PubMed GrantList contains `2023CSJ-3-D006`, explaining the name fragment without an organism identity chain. The full-text PMC request encountered a browser challenge and the DOI web request was inaccessible; no full-text absence finding is claimed.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence. Absence statements are bounded to the stated roots, terms and indexes.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. The record does not conflate marine and oral clones, unrelated taxa, culture deposits, provider identifiers, assembly statistics or funding identifiers.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Never join on a bare D006 label or unnamespaced 103663.

## Follow-up Checks

No corrective follow-up is needed for current claims. Optional enrichment should preserve clone-level provenance, retain the direct GenBank-to-PMID chain despite index misses and distinguish deployment conditions from culture properties. Finer taxonomic placement requires upstream review, not hand-editing lineage. No independent alignment, full experimental reanalysis, genome comparison or PDF/figure visual verification is claimed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:103663`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and checklist governed this independent review. Complete YAML, own source rows, all local candidates, live taxonomy, both specified marker records, primary publisher methods/table text, both PubMed abstracts/metadata and the clinical paper's funding metadata were inspected. No neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `ed9f8b53f09b47a7f1be719305be284c120f5d590f03b7c9612df1ecb1bf68ad`. Only this new report was written for the target. This review did not modify YAML, sources, history, status, pages, GitHub objects, Eukaryota or worktrees.
