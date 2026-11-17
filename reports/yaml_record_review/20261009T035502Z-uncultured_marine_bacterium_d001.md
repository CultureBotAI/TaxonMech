# YAML Record Review: uncultured marine bacterium D001

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d001.yaml`
- Started UTC: 2026-10-09T03:49:28Z
- Finished UTC: 2026-10-09T03:55:02Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:103658`: species rank, Bacteria, parent `NCBITaxon:150608`, five root-first ancestors, code 11, `EXACT` grounding and `SEEDED` status. It has zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior target report. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d001.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d001.yaml --out /private/tmp/taxonmech-d001-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched backbone, all ancestors, attestation, PATHS, scope and seed wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Own marker consistency passed: declared/actual length 559, submitted rRNA transcription equals DNA and no non-ACGT symbols. This checks annotation, not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. Embedded history was inspected; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103658&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103658) agree with identifier, label, rank, parent, code and lineage. Datasets confirms all five root-first ancestor IDs; EFetch supplies matching labels/ranks while omitting root from its displayed chain.

The supplied lineage is root, cellular organisms, Bacteria, environmental samples and marine bacteria D ensemble. Its sparse classification is upstream NCBI placement, not a seeder omission to repair by inference. EFetch has no other names; pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children. Species rank for this uncultured concept does not imply formal nomenclatural standing, a pure culture or a complete genome.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:18523`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0000.jsonl.gz:38539`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15046`: identifier/slug.
- `curation/seed_scope.tsv:144167`: admission date/reason matching the seed event.

One `NAME` attestation counts a source name, not an experiment or genome. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` counts represented BacDive entries, not all environmental clone labels.

Exact Nuccore query `txid103658[Organism:noexp]` returned only UID 5882260. Complete [AF177545.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177545.1) XML was read, including references, every feature and sequence. This is a 559-base partial 16S marker with both feature-end partial flags. Six source qualifiers identify the organism, genomic DNA, taxon 103658, clone D001, environmental sampling and surface-associated marine origin. There is no strain, deposit, genome, host or geographic qualifier. The record cites Dang and Lovell's 2000 paper and a 13-AUG-1999 direct submission from the University of South Carolina. The submission address is not a collection locality.

[PMID 10653705](https://pubmed.ncbi.nlm.nih.gov/10653705/) was verified through complete PubMed abstract/metadata, including DOI 10.1128/AEM.66.2.467-475.2000. The inspected [publisher methods, results and Table 1](https://journals.asm.org/doi/10.1128/AEM.66.2.467-475.2000) establish a cultivation-independent survey of test surfaces deployed at Clam Bank Creek, South Carolina. D001 was recovered after 24 hours and remained represented in several libraries after 72 hours. The accession range includes AF177545. Table frequencies describe cloned rRNA genes, not absolute cell counts or strain growth rates; the discussion explicitly notes PCR and rRNA-copy biases. The paper's phylogenetic interpretation is additional research context, not authorization to replace NCBI's carried lineage. No pure-culture phenotype, genome equivalence or causal graph is inferred.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, deposits, genome links and graphs are appropriately unasserted without explicit identity/evidence chains. The available clone-level publication is an optional enrichment opportunity, not a missing required slot.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms included word-bounded taxid 103658, label/slug and D001 with optional hyphen, space or underscore. Expansion added AF177545 and word-bounded UID 5882260. The initial search returned 123 rows; expansion returned 125: three own taxonomy/name/scope rows and 122 excluded candidates. Every candidate row was read completely in native structured form, including common fields and lossless per-row differences. Five SOURCE.json files were fully parsed for each term set; history filenames were independently inventoried.

Excluded candidates comprised:

- Backbone, name and scope rows for Flavobacteriales endosymbiont of Dynaspidiotus degeneratus D001 (404084), a different environmental concept.
- Cohnella lubricantis DSM 103658 (2163172): BacDive 133071, StrainInfo SI-ID 399652 / SI-DP 906457, culture/type-material entries, NCBI/GTDB/BV-BRC metadata and projected genome/related rows. Its GCA/GCF_014212015.1 and GCA/GCF_017874835.1 assemblies, IMG IDs 8118970613/2913573228, samples and projects belong to that explicit culture-deposit chain. GOLD Go0552709 links via Gp0818926/Gp0505777 to Ga0668220/Ga0454156; these are not D001 links.
- CIP 103658, a Paeniclostridium/Clostridium sordellii deposit: BacDive 2666, species taxid 1505 and strain taxid 1292036, StrainInfo SI-ID 92518 / SI-DP 33772, LPSN names and related raw entries. Neither the nomenclatural variants nor different source classification levels make it taxon 103658.
- BacDive 103658, explicitly Rhodococcus sp. ST029915 (194249). Matching SOURCE.json requested IDs/URLs are BacDive identifiers, not NCBI taxids.
- StrainInfo SI-ID 38357 / SI-DP 103658, Leucothrix mucor ATCC 25109 (45248), and SI-ID 181893, Fusicolla aquaeductuum / Fusarium aquaeductuum IMI 103658 (1053102). These are different source namespaces and organisms.
- GCA_009511665.1, Salmonella enterica serovar Typhimurium strain 103658 (90371), not the marine clone.
- Six GTDB rows where 103658 is an N50/N75 statistic: GCA_949081685.1, GCF_018786045.1, GCA_948568525.1, GCA_948617815.1, GCA_948959455.1 and GCA_949091365.1. Native classification is Bacteroides faecis or uncultured Muribaculaceae, not D001.
- Expanded-search GCA/GCF_036216705.1 rows, Bacillus thuringiensis B-59759 (1428), where 5882260 is genome length rather than the target marker UID. The historical RefSeq row is suppressed; neither row supplies target evidence.

`D001[All Fields] AND txid150608[Organism]` returned only the own marker. Unfiltered `D001[All Fields]` returned 887 Nuccore hits, with 100 UIDs retrieved; these cross-organism results were not exhaustively audited. Exact non-expanded Assembly search returned zero with missing-phrase/no-items diagnostics. PubMed `AF177545[All Fields]` returned the verified own paper.

PubMed `D001[All Fields] AND bacterium[All Fields]` returned four other candidates, all inspected through complete abstracts/metadata: PMIDs 42750456 and 40859739 concern Weissella confusa WIKIM51, marketed as Wilac D001; PMID 38930801 concerns Lactobacillus plantarum and encapsulated lactoferrin; PMID 27770918 concerns a clay-gentamicin material tested against Escherichia coli, with d(001) crystallographic notation. None provides an identity chain to this marine clone. These exclusions are not an exhaustive literature absence claim.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence. All absence statements are bounded to the stated roots, terms and indexes.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. The record does not confuse environmental clone evidence, culture-collection numbers, provider IDs, genome statistics or probiotic product names.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Never join on a bare D001 label or unnamespaced 103658.

## Follow-up Checks

No corrective follow-up is needed for current claims. Optional enrichment should retain clone-level provenance and distinguish experimental deployment conditions from pure-culture properties. Any finer taxonomic placement requires upstream review rather than a hand-edited lineage. No independent alignment, complete experiment audit, genome comparison or PDF/figure visual verification is claimed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:103658`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and checklist governed this independent review. Complete YAML, own source rows, all local candidates, live taxonomy, the own marker, primary publisher text and the stated PubMed abstracts/metadata were inspected. No neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `e74880687f37a4089099bcb742190fb2e1e7683d513e9b54ddedaadb6efd4cf3`. Only this new report was written for the target. This review did not modify YAML, sources, history, status, pages, GitHub objects, Eukaryota or worktrees.
