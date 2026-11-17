# YAML Record Review: uncultured marine bacterium D002

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d002.yaml`
- Started UTC: 2026-10-09T04:05:53Z
- Finished UTC: 2026-10-09T04:12:37Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:103659`: species rank, Bacteria, parent `NCBITaxon:150608`, five root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It represents zero BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior target report. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d002.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d002.yaml --out /private/tmp/taxonmech-d002-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched backbone, all ancestors, attestation, PATHS, scope and seed wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Own marker consistency passed: declared/actual length 559, submitted rRNA transcription equals DNA and no non-ACGT symbols. This is an annotation check, not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. Embedded history was inspected; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103659&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103659) agree with identifier, name, rank and ancestor chain. EFetch additionally verifies parent and genetic code; Datasets includes root in its five ancestor IDs.

The lineage is root, cellular organisms, Bacteria, environmental samples and marine bacteria D ensemble. This sparse classification is upstream NCBI placement, not a seeder omission to repair by inference. EFetch supplies no other names; pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children. Species rank for this uncultured concept does not establish formal nomenclatural standing, a pure culture or a complete genome.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:18524`: identity, rank, parent, genetic code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0000.jsonl.gz:38540`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15048`: identifier/slug.
- `curation/seed_scope.tsv:144168`: admission date/reason matching the seed event.

One `NAME` attestation counts a source name, not an experiment or genome. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` counts represented BacDive entries, not environmental clone labels.

Exact Nuccore query `txid103659[Organism:noexp]` returned only UID 5882261. Complete [AF177546.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177546.1) XML was read, including references, all features and sequence. It is a 559-base partial 16S marker with both feature ends partial. Six source qualifiers identify the organism, genomic DNA, taxon 103659, clone D002, environmental sampling and surface-associated marine origin. There is no strain, culture-deposit, host, geographic or genome qualifier. References name Dang and Lovell's 2000 paper and a 13-AUG-1999 direct submission from the University of South Carolina. The submission address is not collection locality.

[PMID 10653705](https://pubmed.ncbi.nlm.nih.gov/10653705/) was verified through full abstract/metadata, including DOI 10.1128/AEM.66.2.467-475.2000 and PMC91850. The inspected [publisher methods and Table 1](https://journals.asm.org/doi/10.1128/AEM.66.2.467-475.2000) describe a cultivation-independent survey at Clam Bank Creek, North Inlet, South Carolina. D002 occurs on all six test-surface types after both 24 and 72 hours. Its clone frequencies on short-chain PEG surfaces were 3.1% and 38.1%, respectively. These are proportions of cloned rRNA genes with the same restriction pattern, not absolute cell counts or pure-culture growth rates. The paper's accession range includes AF177546. Experimental observations and phylogenetic interpretations do not authorize replacing the record's carried NCBI lineage or inferring a genome identity.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, culture deposits, genome links and graphs are appropriately unasserted without explicit identity/evidence chains. The clone-level publication is an optional enrichment opportunity, not a missing required slot.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms included word-bounded taxid 103659, label/slug and D002 with optional hyphen, space or underscore. Expansion added AF177546 and word-bounded UID 5882261. Both searches returned the same 24 candidate rows: three own taxonomy/name/scope rows and 21 exclusions. Every candidate row was read completely in native structured form, including common fields and lossless per-row differences. Five SOURCE.json files were fully parsed for both term sets; history filenames were independently inventoried.

Excluded candidates comprised:

- Backbone, scope and name rows for Flavobacteriales endosymbiont of Parlatoria camelliae D002 (404110) and Borreliella sp. D002 (3448910), each a distinct taxon with its own parent.
- BacDive 103659, explicitly Rhodococcus sp. ST029967 (194249), in raw and complete native records. Matching SOURCE.json requested IDs/URLs are BacDive identifiers, not NCBI taxids.
- CIP 103659, a Klebsiella aerogenes deposit (548), represented by BacDive 139664 and StrainInfo SI-ID 42497 / SI-DP 150487. The related ATCC 49469 / SI-DP 114360 entry retains Enterobacter aerogenes wording; aliases include AmMS244. Raw culture/strain links, related rows and complete native records support this separate culture-deposit chain, not the marine clone.
- StrainInfo SI-ID 38358 / SI-DP 103659, Leucothrix mucor ATCC 25110 (45248), a provider deposit identifier rather than the target taxid.
- GCA_048561585.1, Candidatus Thiodubiliella endoseptemdiera (2738886), isolate J21407_BXC-D_002-Thio, with PRJNA1159215 and SAMN43832077. Its explicit isolate identity and metagenome-derived assembly are not D002 evidence.
- GCA_008833785.1, Salmonella enterica serovar Typhimurium strain 103659 (90371), not the environmental clone.
- Three GTDB rows where 103659 is a contig/scaffold statistic: GCF_943369415.1, Polaromonas sp. YR568 (1855301); GCA_949483375.1, uncultured Clostridia bacterium (244328); and GCF_001866135.1, Microbacterium sp. LCT-H2 (1914306). None supplies target identity evidence.

`D002[All Fields] AND txid150608[Organism]` returned only the own marker. Its translation stack reports 969 unfiltered D002 matches; that cross-organism set was not exhaustively audited. Exact non-expanded Assembly search returned zero with missing-phrase/no-items diagnostics. PubMed `D002[All Fields] AND bacterium[All Fields]` returned zero, but `AF177546[All Fields]` returned the independently verified own paper. The label-query miss is therefore not a literature-absence claim.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence. All absence statements are bounded to the stated roots, terms and indexes.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. The record does not confuse clone evidence, culture deposits, provider identifiers, unrelated D002 labels or assembly statistics.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Never join on a bare D002 label or unnamespaced 103659.

## Follow-up Checks

No corrective follow-up is needed for current claims. Optional enrichment should retain clone-level provenance and distinguish deployment conditions from culture properties. Finer taxonomic placement requires upstream review, not a hand-edited lineage. No independent alignment, full experimental reanalysis, genome comparison or PDF/figure visual verification is claimed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:103659`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and checklist governed this independent review. Complete YAML, own source rows, all local candidates, live taxonomy, the own marker, primary publisher methods/table text and full own PubMed abstract/metadata were inspected. No neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `5dbfc3c25c720558f2fd31afe9aa5a12fb7b07a1d46f9829c46db4a3caac3194`. Only this new report was written for the target. This review did not modify YAML, sources, history, status, pages, GitHub objects, Eukaryota or worktrees.
