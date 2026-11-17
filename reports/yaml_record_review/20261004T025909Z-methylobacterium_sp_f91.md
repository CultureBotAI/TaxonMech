# YAML Record Review: Methylobacterium sp. F91

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_f91.yaml`
- Started UTC: 2026-10-04T02:58:27Z
- Finished UTC: 2026-10-04T02:59:09Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1032721`, Methylobacterium sp. F91. It has SPECIES rank, BACTERIA domain, parent unclassified Methylobacterium (2615210), ten lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No phenotype, host-interaction, gene-function, causal-graph or genome-equivalence claim is asserted.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/methylobacterium_sp_f91.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/methylobacterium_sp_f91.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks compared the full lineage, source inventories, attestation, path, scope and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220905` and `data/catalog/ncbi_names-0005.jsonl.gz:30211` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032721&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032721) confirm the exact label, species rank, parent, code 11, bacterial domain and all ten root-first lineage IDs. The hierarchy through Alphaproteobacteria, Hyphomicrobiales and Methylobacteriaceae is source-carried, not inferred from metabolism.

Complete structured scans found no backbone synonym or direct child and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this NCBI placeholder, not every strain called F91 or a formally named species.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13292` and `curation/seed_scope.tsv:321276` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event matches that reason without claiming human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HQ680432.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ680432.1) is a 1,450-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain F91 and explicit taxon 1032721. Its source qualifiers identify rhizosphere, host wild rice and China: Dongxiang, Jiangxi.

The unpublished study title describes endophytic bacteria from Dongxiang wild rice, while the source qualifier says rhizosphere. These different scopes are preserved; the title alone does not establish internal plant colonization by this strain. Fei's direct submission is dated 2010-12-02; no PMID or DOI is supplied. The marker does not ground the host to a scientific species or establish a metabolic function, and the genus name is not phenotype evidence.

Exact Assembly search returned zero with a phrase-not-found warning. This bounded result is not proof of universal genome absence, and the partial marker is not an assembly. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` as an upstream record count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the numeric identifier with digit boundaries, full label, slug and bounded F91 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 76 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. F91 alone is not a culture-collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to the taxonomy-only YAML; an external marker is not a functional assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The external title/source-qualifier distinction is not a contradictory YAML assertion.

## Recommended Edits

None required. Preserve source-carried taxonomy, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Resolve the experimental source context before any future host-localization claim, and require explicit identity crosswalks before attaching culture or genome identifiers.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032721 --force`, inspect its YAML and rerun both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Chryseobacterium nakagawai F91 is taxon 1241982, BacDive 134064, StrainInfo strain 410528, with CCUG 60563 and NCTC 13529 among its source designations. Myxococcus fulvus Mx f91 is taxon 33, BacDive 9786 and StrainInfo 215788. Neither identity transfers through the shared alias. StrainInfo also has unrelated F91 designations under Malbranchea conjugata and Terrisporobacter glycolicus; VKM F-91 is the own deposit 450587 of Botrytis galanthina strain 72690.

Malaciobacter molluscorum F91 (1032072), also carried as Arcobacter molluscorum in BV-BRC, has GCA_004116685.1 / GCF_004116685.1. Other excluded genomes include Neisseria gonorrhoeae F91 GCA_007655285.1 and historical GCF_007655285.1; Listeria monocytogenes LM-F-91 GCA_003188385.1 / GCF_003188385.1; Pantoea stewartii F91 GCA_056712175.1 / GCF_056712175.1; and unrelated Escherichia coli, Campylobacter and Vibrio F91-prefixed isolates. GOLD environmental-community projects labeled F91 do not classify this isolate.

Other excluded taxon labels include Brevundimonas sp. Muzt-F91 (269839), actinobacterium MS-F-91 (579320), Burkholderia clone F91_06b_B (661006), Desulfovibrio sp. oral taxon F91 (712260), Psychrobacillus sp. F91 (1224321) and Exiguobacterium sp. F-91 (1664559). SAMEA1032721 belongs to Streptococcus pneumoniae R34-3150 (1313), including GCA_001105605.1/.2, GCF_001105605.1 and ATB run ERR068042. None is target-specific evidence.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
