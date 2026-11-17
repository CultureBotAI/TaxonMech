# YAML Record Review: Microcystis aeruginosa NIER 10024

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microcystis_aeruginosa_nier_10024.yaml`
- Started UTC: 2026-10-04T17:03:41Z
- Finished UTC: 2026-10-04T17:05:24Z
- Verdict: pass with minor issues

## Target

Read the entire generated TaxonRecord for NCBITaxon:1033666, Microcystis aeruginosa NIER 10024. It is a STRAIN in BACTERIA, parent NCBITaxon:1126, genetic code 11, EXACT grounding and SEEDED status. It has zero inventoried BacDive strains, one NCBITAXON NAME attestation and the 2026-09-13T17:54:04Z seed event. The strain-level taxon and BacDive strain count have different meanings; zero is not internally contradictory. No YAML, history or status was changed.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/microcystis_aeruginosa_nier_10024.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/microcystis_aeruginosa_nier_10024.yaml`: one file, zero ERROR rows.
- Ignored-inclusive exact identifier search across `data/taxa` resolved only this YAML; ignored-inclusive report filename search found no previous review for its stem.
- Structured comparisons passed for the full backbone chain, seven source inventories, PATHS, scope reason, NCBI attestation and seed text. Exact type-material, merged-ID and dropped scans were completed.
- Inspected the name-class parser, native-name catalog builder and synonym emission code to assess the live-name discrepancy below.
- Not checked: full-corpus `just qc`, `just verify-corpus`, tests, provenance, global term/reference and history/product gates, or rendering. Bounded source comparisons are not corpus reproduction. No curator-added graph nodes or external record-level evidence references require an additional product check.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221280` agrees on identity, rank, parent, code and snapshot 2026-09-13. Its synonym and retirement fields are empty. The twelve ancestors were checked in full: root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Bacillati 1783272 (KINGDOM), Cyanobacteriota/Melainabacteria group 1798711 (CLADE), Cyanobacteriota 1117 (PHYLUM), Cyanophyceae 3028117 (CLASS), Oscillatoriophycideae 1301283 (SUBCLASS), Chroococcales 1118 (ORDER), Microcystaceae 1890449 (FAMILY), Microcystis 1125 (GENUS), Microcystis aeruginosa 1126 (SPECIES). PATHS row 13733 and `curation/seed_scope.tsv:321632` confirm slug and reason. The full native name object at `data/catalog/ncbi_names-0005.jsonl.gz:30588` contains only the scientific name.

Live [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033666&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033666) agree on identity, STRAIN rank and ancestry; EFetch confirms parent and code, and Datasets includes root. The Taxonomy Browser was inaccessible through the web tool, so successful structured authority responses supplied verification. The bacterial placement is explicit; a cyanobacterial name does not make this an eukaryotic record.

EFetch additionally identifies Microcystis aeruginosa NIER-10024 with name class `misspelling`. That spelling must not be promoted to a correct name or exact synonym. Its absence from the pinned local sources is the minor finding below, not evidence that the taxon identity or parent is wrong.

## Evidence

The attestation correctly counts one NAME, not a genome or culture. Complete scans found no direct children or exact matching BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory rows. Exact type-material, merged-ID and dropped scans also returned no target entry. Parent-species nomenclature or another Microcystis strain's properties must not be copied onto NIER 10024.

Live exact-organism queries returned zero Assembly results with phrase-not-found/no-items warnings and one Nuccore result, UID 333362439. [HM991458.1](https://www.ncbi.nlm.nih.gov/nuccore/HM991458.1) is a 938 bp partial RNA-polymerase beta-subunit coding sequence, not 16S or an assembly. Source qualifiers explicitly identify NIER 10024, taxon:1033666 and genomic DNA, with South Korea: Hapcheon Reservoir context. Its sole reference is Ki J.-S.'s direct submission dated 2010-07-27 from Sangmyung University in Seoul, without DOI, PMID or a named research article. No microcystin production, toxicity, bloom behavior or other phenotype is established by this marker or by the species name.

## Completeness

Ignored-inclusive compressed-file search covered taxon-number boundaries, NIER 10024/NIER-10024/NIER_10024 variants, label and filename slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Four rows matched: target backbone, scope, native scientific name and one unrelated ATB row. Recursive structured SOURCE.json inspection found no additional match. Thus the live misspelling is absent from the inspected local name sources, including ignored files.

`data/catalog/allthebacteria.tsv.xz:65025` identifies SAMEA1033666, ERR068216 and ERZ3069101. Using the previously inspected native header, scientific name and both Sylph fields are Streptococcus pneumoniae, FASTA is available, assembly/Sylph/HQ filters are PASS and prior-HQ is T. Only the BioSample suffix and its download URL match the taxon number. No target-linked strain/deposit/sample chain supports a link. Sharing a sample would not establish genome equivalence; SeqKit is not MD5 and the AWS URL is mutable.

No supported omitted target strain/deposit/genome association was found in the bounded searches; worldwide absence is not claimed. Optional mechanisms, record-level literature evidence, mappings and strain-specific nomenclature are appropriately empty. The spelling-coverage issue is separate. Zero BacDive entries does not mean the named strain was never cultivated. iModulonDB is not applicable to this taxonomy-only record: the supplementary marker lookup is not an expression-module or phenotype assertion.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

1. Minor: current-authority spelling coverage differs from the pinned local record and name catalog. Live EFetch explicitly retains Microcystis aeruginosa NIER-10024 as a misspelling, while the local scientific-name object and inventory contain no related synonym. `src/taxonmech/ncbi_taxdump.py:90` maps non-scientific names other than synonym/equivalent name to RELATED_SYNONYM; `scripts/build_source_catalog.py:92` retains every prokaryotic name class; `src/taxonmech/seed.py:381` emits related synonyms supplied by the inventory. This can reduce discoverability by the source spelling but does not change identity. The inspected code does not establish a generator bug: the difference may originate in snapshot contents or source refresh. An ignored-inclusive repository filename search found no local taxdump archive/names.dmp, and the configured `data/source_snapshots` directory is unavailable, so the pinned source row could not be independently checked. EFetch's update date is not proof of when that particular name entered the dump. Maintained owners: `conf/ncbi_taxdump.yaml`, the pinned upstream source snapshot and `src/taxonmech/ncbi_taxdump.py`; regeneration flows through `src/taxonmech/extract.py` and `src/taxonmech/seed.py`.

## Recommended Edits

Investigate the pinned names.dmp row before making a change. If an authorized source refresh establishes the misspelling, retain its original source class in the native catalog and emit it as an NCBITaxon RELATED_SYNONYM through the maintained importer. Do not replace the canonical label, assert EXACT_SYNONYM, hand-edit the YAML or silently alter the pinned catalog. If the pinned row is absent, record the difference as a source-version delta and update the source pin only through the normal refresh workflow. No genus, parent, rank or genome edit is supported.

## Follow-up Checks

Resolve the exact NCBI names.dmp entries for 1033666 in the pinned and proposed source versions, compare original name classes, and verify the importer preserves the class-to-scope rule. If authorized to refresh, run extraction and seed dry-run, then `just seed-canary NCBITaxon:1033666 --force`; inspect the resulting RELATED_SYNONYM, retained scientific label and lineage. Rerun both focused validators, relevant name-class tests, provenance checking, `just verify-corpus` and `just qc`. No refresh, canary, regeneration or curation event was performed during this review.

## Additional Notes

The local single-record skill and checklist governed this read-only review. No human-reviewed promotion, generated-page edit or GitHub mutation was made. The minor spelling discrepancy remains unresolved for later source maintenance; Eukaryota coverage was not reopened.
