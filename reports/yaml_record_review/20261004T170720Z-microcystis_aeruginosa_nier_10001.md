# YAML Record Review: Microcystis aeruginosa NIER 10001

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microcystis_aeruginosa_nier_10001.yaml`
- Started UTC: 2026-10-04T17:06:21Z
- Finished UTC: 2026-10-04T17:07:20Z
- Verdict: pass with minor issues

## Target

Read the entire generated TaxonRecord, NCBITaxon:1033667, Microcystis aeruginosa NIER 10001. It is a STRAIN in BACTERIA, with parent NCBITaxon:1126, genetic code 11, EXACT grounding and SEEDED status. It carries zero inventoried BacDive strains, one NCBITAXON NAME attestation and the 2026-09-13T17:54:04Z seed event. Strain-level taxon rank and BacDive strain count denote different things, so zero is not contradictory. No YAML, history or status was changed.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/microcystis_aeruginosa_nier_10001.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/microcystis_aeruginosa_nier_10001.yaml`: one file, zero ERROR rows.
- Ignored-inclusive exact identifier search across `data/taxa` resolved one file. Ignored-inclusive report filename search found no previous review for the stem.
- Structured comparisons passed for full backbone ancestry, seven source inventories, PATHS, scope, NCBI attestation and seed text. Exact type-material, merged-ID and dropped scans were completed.
- Name-class parser, native catalog builder and synonym-emission policy were inspected in this review session; the target-specific native name object was read in full.
- Not checked: full-corpus `just qc`, `just verify-corpus`, tests, provenance, global term/reference and history/product gates, or rendering. Bounded source comparisons do not prove corpus reproduction. No curator-added graph nodes or external record-level evidence references require an additional product check here.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221281` agrees on label, rank, parent, code and snapshot 2026-09-13, with empty synonym and retirement fields. All twelve ancestors agree: root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Bacillati 1783272 (KINGDOM), Cyanobacteriota/Melainabacteria group 1798711 (CLADE), Cyanobacteriota 1117 (PHYLUM), Cyanophyceae 3028117 (CLASS), Oscillatoriophycideae 1301283 (SUBCLASS), Chroococcales 1118 (ORDER), Microcystaceae 1890449 (FAMILY), Microcystis 1125 (GENUS), Microcystis aeruginosa 1126 (SPECIES). PATHS row 13734 and `curation/seed_scope.tsv:321633` match the slug and reason. The complete native name object at `data/catalog/ncbi_names-0005.jsonl.gz:30589` contains the scientific name only.

Live [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033667&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033667) were read and confirm identity, STRAIN rank and ancestry; EFetch confirms parent and genetic code, and Datasets includes root. The Taxonomy Browser was inaccessible through the web tool, so structured authority responses supplied verification. BACTERIA is correct despite the cyanobacterial terminology.

EFetch additionally names Microcystis aeruginosa NIER-10001 with class `misspelling`. That name is not an alternative correct name or an exact synonym. Its local omission is a minor source-coverage discrepancy, not a wrong taxon identity or placement.

## Evidence

The sole attestation correctly counts one NAME, not a genome. Complete scans found no direct children or exact target matches in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventories. Type-material, merged-ID and dropped inventories also had no target row. Parent-species nomenclature and another strain's properties cannot be transferred here.

Live exact-organism searches returned zero Assembly results with phrase-not-found/no-items warnings and one Nuccore result, UID 333362441. [HM991459.1](https://www.ncbi.nlm.nih.gov/nuccore/HM991459.1) is a 938 bp partial RNA-polymerase beta-subunit coding sequence, not 16S or an assembly. Inspected source qualifiers explicitly name NIER 10001, taxon:1033667 and genomic DNA, with South Korea: Daechung Reservoir context. The sole reference is Ki J.-S.'s direct submission dated 2010-07-27 from Sangmyung University in Seoul, without DOI, PMID or named article. Neither this marker nor the species name establishes microcystin production, toxicity or bloom behavior. The source was checked independently; shared length and submission date do not make this sequence identical to another NIER strain's marker.

## Completeness

Ignored-inclusive compressed-file search covered taxon-number boundaries, NIER 10001/NIER-10001/NIER_10001 variants, label and filename slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Four rows matched: target backbone, scope, native scientific name and one unrelated ATB row. Recursive structured SOURCE.json inspection found no additional match. Thus the hyphenated live misspelling is absent from the searched local name sources, including ignored files.

`data/catalog/allthebacteria.tsv.xz:65026` identifies SAMEA1033667, ERR064634/ERR085893 and ERZ3069102. Using the previously inspected native header, scientific name and both Sylph fields are Streptococcus pneumoniae, FASTA is available, assembly/Sylph/HQ filters are PASS and prior-HQ is T. Only the numeric BioSample suffix and its download URL match. No target-linked strain/deposit/sample chain supports an association. Sharing a sample would not establish assembly equivalence; SeqKit is not MD5 and the AWS URL is mutable.

No supported omitted target strain/deposit/genome association was found in these bounded searches; worldwide absence is not claimed. Optional mechanisms, strain-specific nomenclature, mappings and literature evidence are appropriately empty apart from the separate spelling issue. Zero BacDive entries does not mean the named strain was never cultivated. iModulonDB is not applicable: the YAML is taxonomy-only, and the supplementary marker lookup is not a transcriptomic or mechanistic assertion.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

1. Minor: live NCBI retains Microcystis aeruginosa NIER-10001 as a misspelling, but the pinned inventory, native catalog and generated record omit that source spelling. This may reduce discoverability without changing identity. The inspected `src/taxonmech/ncbi_taxdump.py:90` maps non-scientific names other than synonym/equivalent name to RELATED_SYNONYM; `scripts/build_source_catalog.py:92` retains all prokaryotic name classes; `src/taxonmech/seed.py:381` emits inventory-provided related synonyms. The discrepancy is not proof of a generator defect or a particular introduction date. The configured source-snapshot directory is unavailable; an ignored-inclusive repository filename search in this session found no taxdump archive/names.dmp, so the pinned original name row was not inspected. EFetch's update date does not date individual name additions. Maintained owners: `conf/ncbi_taxdump.yaml`, the pinned upstream source, `src/taxonmech/ncbi_taxdump.py`, then `src/taxonmech/extract.py` and `src/taxonmech/seed.py` for regeneration.

## Recommended Edits

First compare exact target name rows in the pinned and proposed NCBI dumps. If authorized source maintenance establishes the misspelling, retain its native class and emit it as an NCBITaxon RELATED_SYNONYM through the importer. Do not replace the scientific label, assert EXACT_SYNONYM, hand-edit YAML or silently patch the pinned catalog. If the pinned dump lacks the row, document a source-version delta and use the normal authorized refresh process. No identity, rank, parent or genome change is supported.

## Follow-up Checks

Inspect names.dmp entries for 1033667 and verify source class-to-synonym-scope handling. For an authorized refresh, run extraction and seed dry-run, then `just seed-canary NCBITaxon:1033667 --force`; inspect the related synonym, unchanged canonical label and lineage. Rerun both focused validators, relevant name-class tests, provenance checking, `just verify-corpus` and `just qc`. No refresh, canary, regeneration or curation event was performed here.

## Additional Notes

The local single-record review skill and checklist governed this report. No human-reviewed promotion, generated-page edit or GitHub mutation was made. The minor source-spelling discrepancy remains a maintenance follow-up. Eukaryota coverage was not reopened.
