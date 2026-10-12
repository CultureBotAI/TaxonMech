# YAML Record Review: uncultured Treponema clone HsPySp20

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_treponema_clone_hspysp20.yaml`
- Started UTC: 2026-10-07T18:47:45Z
- Finished UTC: 2026-10-07T18:58:23Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:103612`, label uncultured Treponema clone HsPySp20, rank `SPECIES`, domain `BACTERIA`. The complete YAML was read independently. It contains ten ancestors, genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, one NCBI name attestation and `strain_count: 0`. That count measures inventoried BacDive strains, not a universal claim about cultivation.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/uncultured_treponema_clone_hspysp20.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/uncultured_treponema_clone_hspysp20.yaml --out /private/tmp/hsp20-strict.tsv`: exit 0; one file, zero error rows; the diagnostic TSV contains only its header.
- Complete structured source comparisons verified identity, rank, parent, code, every ancestor, source attestation, scope reason and path mapping. No children occur in the pinned backbone. Exact type-material, merged-ID and dropped-ID checks returned no target rows. These bounded checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. No target graph or standalone history record was found in the bounded searches. No focused substitute for a full-corpus gate was invented.

## Identity and Grounding

Live NCBI Taxonomy EFetch agrees with the exact name, identifier, species rank, genetic code 11 and parent `NCBITaxon:77353` environmental samples. Datasets confirms all ten ancestor IDs including root. The complete pinned and live lineage agrees: root, cellular organisms, Bacteria, Pseudomonadati, Spirochaetota, Spirochaetia, Treponematales, Treponemataceae, Treponema and environmental samples. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103612), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103612).

The native name catalog provides only the scientific name; empty synonyms and nomenclature agree with the inventories. Species rank and exact grounding identify this environmental clone; they do not confer formal nomenclatural standing or establish equivalence with another Treponema clone, cultured strain or genome.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18514` matches all backbone fields, empty synonym fields, sole NCBI source and the 2026-09-13 snapshot. `data/catalog/ncbi_names-0000.jsonl.gz:38522` supplies the scientific-name record.
- `data/taxa/PATHS.tsv:14761` uniquely maps the ID to this slug. `curation/seed_scope.tsv:144160` provides the one-source attested inclusion reason and 2026-09-13 date.
- Exact-taxonomy Nucleotide search returned one record, [AB032004.1](https://www.ncbi.nlm.nih.gov/nuccore/AB032004.1), UID 7209352. Its complete non-sequence/non-translation metadata identify a 1,507-base partial 16S rRNA sequence, clone HsPySp20 and taxon 103612. The source has the environmental-sample flag, names Hodotermopsis sjoestedti as host and describes PCR amplification from an isolated termite protist. No culture, BioSample, BioProject or assembly accession appears in this metadata.
- The sequence cites Iida, Ohkuma, Ohtoko and Kudo's 2000 FEMS Microbiology Ecology article, `PMID:11053732`, `DOI:10.1111/j.1574-6941.2000.tb00750.x`, and a RIKEN direct submission dated 29 August 1999. Inspected PubMed metadata/abstract confirm the article and its protist-associated spirochete context. The exact clone-to-marker and host links come from GenBank; cohort-level microscopy findings were not assigned indiscriminately to this clone. [Primary article metadata and abstract](https://pubmed.ncbi.nlm.nih.gov/11053732/).
- Figure 2's inspected caption in the 2006 Spirochaeta coccoides paper explicitly includes HsPySp20/AB032004 in termite Treponema cluster II. The paper's experimental organism SPN1 is different; its cultivation and physiological results do not belong to HsPySp20. [Primary article](https://journals.asm.org/doi/10.1128/aem.72.1.392-397.2006).
- A visually inspected public Yuki/Ohkuma poster places HsPySp20 and HsPySp1 as distinct tree tips near Treponema sp. Pyr2-C9. Its genome table names Pyr2-C9, not HsPySp20; neither that genome nor its inferred metabolism was transferred to the target. [Primary poster](https://www.ifo.or.jp/rc_pdf/yuki.pdf).
- Exact-taxonomy Assembly search returned zero items with phrase-not-found/no-items warnings. This bounded result does not prove universal genome absence.
- The seed event's source and scope reason agree with the inventories. Its `2026-09-13T17:54:04Z` timestamp is the latest raw/ATB/StrainInfo extraction timestamp, matching `src/taxonmech/seed.py:139`. It documents seeding, not human review.

## Completeness

Exact BacDive inventory and backbone-descendant checks support zero inventoried strains. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits comparisons also returned no target row. Optional literature and marker enrichment is possible, but no required seeded representation was demonstrated missing.

The bounded gitignore-independent search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It covered digit-bounded 103612, HsPySp20 spelling variants matching the label and slug, AB032004, PMID 11053732 and the original article DOI. All 46 resulting rows/objects were inspected completely. Five SOURCE.json files were parsed separately, and history filenames checked independently. No supported target culture/genome link, additional curation overlay or standalone history record was found within those roots.

No gene-function, regulator, transcriptomic, mechanism or dataset claim appears in the YAML. iModulonDB is not applicable; its absence was not used as biological evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The clone identity, lineage, source attestation, source-specific strain count and seeded lifecycle provenance are supported.

## Recommended Edits

None required. Preserve the generated record and seed history. Optional marker/literature enrichment should retain the explicit HsPySp20 identity in maintained source or durable curator inputs. Do not insert neighboring genomes, SPN1 physiology or arbitrary BacDive identifiers into this record.

## Follow-up Checks

Any future genome or strain enrichment needs an explicit primary accession-to-clone chain. A shared tree cluster, termite host or numeric identifier is insufficient. Changes would belong in maintained extractor/seeder inputs or an appropriate durable curation representation, followed by schema/strict validation and the documented corpus/provenance gates.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The YAML was byte-identical before report creation. Existing worktrees and the closed parallel session's work were left untouched.
- The BacDive SOURCE.json match requests BacDive 103612, a Rhodococcus sp. record for taxon 194249, not NCBITaxon:103612. BacDive 136233 and related GOLD/StrainInfo rows instead describe Lactobacillus gallinarum CIP 103612, taxon 52242. StrainInfo deposit SI-DP 103612 belongs to Pseudomonas aeruginosa ATCC 25010.
- Other fully inspected numeric collisions include Wenling narna-like virus 7 WLJQ 103612; Bacillus subtilis SRCM103612; Enterobacter cloacae 3143 accession CP103612; Duncaniella muris MGBC103612; Salmonella and Shigella isolate/run names; uncultured bacterium MarMAG103612; and unrelated GTDB assembly statistics. These different namespaces do not ground the target.
- AllTheBacteria row 6208 is Escherichia coli O26:H11 run DRR103612, sample SAMD00075955. Row 1559824 is Mycobacterium tuberculosis sample SAMN11053732, run SRR8692806 and analysis ERZ25547831, a PMID-digit collision. Neither is target genome evidence.
- The original 2000 article's full publisher text was not retrieved; the inspected abstract and sequence metadata bound the claims here. The poster was inspected from the previously downloaded public PDF render because the current web-tool refetch failed. No clone-specific experimental-table audit, sequence alignment or taxonomic reassignment was performed.
- Only this new report was written for the target. No YAML, source inventory, history/lifecycle or GitHub state was changed.
