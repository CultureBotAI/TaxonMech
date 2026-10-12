# YAML Record Review: Sphingomonas sp. T19

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sphingomonas_sp_t19.yaml`
- Started UTC: 2026-10-04T03:08:42Z
- Finished UTC: 2026-10-04T03:09:57Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032727`, Sphingomonas sp. T19. It carries SPECIES rank, BACTERIA domain, parent unclassified Sphingomonas (196159), ten lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No phenotype, host-interaction, gene-function, causal-graph or genome-equivalence assertion is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/sphingomonas_sp_t19.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/sphingomonas_sp_t19.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked the full lineage, source inventories, attestation, path, scope and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220911` and `data/catalog/ncbi_names-0005.jsonl.gz:30217` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032727&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032727) confirm exact label, species rank, parent, code 11, bacterial domain and all ten root-first lineage IDs. Labels and ranks through Alphaproteobacteria, Sphingomonadales and Sphingomonadaceae agree with the carried hierarchy.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this NCBI placeholder, not a formally named species or every Sphingomonas strain designated T19.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13298` and `curation/seed_scope.tsv:321282` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without claiming human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HQ647266.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ647266.1) is a 1,368-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain T19 and explicit taxon 1032727. Source qualifiers identify rhizosphere, host wild rice and China: Dongxiang, Jiangxi. References comprise an unpublished study by Fei and a direct submission on 2010-11-21; no PMID or DOI is supplied.

The marker does not establish a scientific host-species grounding or a strain-specific phenotype. Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than proof of universal genome absence. Both structured taxonomy requests and GenBank XML retrieval succeeded.

A same-genus T19 candidate required separate investigation. Full BacDive 169342 and StrainInfo 401525 records associate T19 with DSM 103178, not with the target taxon. The inspected [DSMZ catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-103178) describes a cleanroom wipe isolate from Turin, Italy, sampled in September 2013, with a European Space Agency / Moissl-Eichinger deposit history. This differs from the Chinese rhizosphere source and predates neither the target's 2010 submission nor its source context. The evidence supports keeping the records separate, not adding DSM 103178 to this YAML.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` as an upstream count. The broader-classified DSM 103178 candidate does not invalidate that count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the numeric target identifier with digit boundaries, full label, slug and Sphingomonas co-occurring with bounded T19 separator variants in either order across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 12 matching lines were inspected. This was not a census of every bare T19 alias. A second ignored-inclusive search covered DSM 103178, BacDive 169342, SI-ID 401525 and SI-DP 908468; all 30 matching lines were inspected in structured context.

Recursive SOURCE.json traversal included ignored files. The target query had no metadata matches; the candidate query found six request/URL contexts for BacDive 169342 and StrainInfo IDs 169342 and 401525. Those document retrieval, not identity equivalence. Within these bounded surfaces, no independently supported target deposit, genome association, extra source mapping or separate history record was found. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only YAML; marker context is not a functional assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The investigated same-name culture candidate is not a supported missing strain association.

## Recommended Edits

None required. Preserve generated ownership, source-carried taxonomy and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Do not join DSM 103178 through the bare T19 designation. Require explicit provenance and identity evidence before any future culture or genome association.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032727 --force`, inspect its YAML and rerun both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

The candidate occurs at `data/raw/bacdive_strains.tsv:91575` and `data/bacdive/records.jsonl.gz:91574`, classified to NCBITaxon:28214, with an empty native Sequence information object. StrainInfo at `records.jsonl.gz:299414` gives both the group 401525 and own deposit 908468 the genus classification Sphingomonas (13687), LPSN 516629, DOI 10.60712/SI-ID401525.2 and no sequence list. The source's group and deposit identities remain distinct. No sequence can be transferred through this grouping.

The BacDive browser page was unavailable through the web tool; its native local JSON was inspected completely. The DSMZ page's main record is Sphingomonas, while a peripheral BacDive-link caption says Moraxella osloensis. This external caption inconsistency was not treated as a taxonomic synonym or used to alter either source identity. It does not affect the target's supported NCBI grounding.

SAMEA1032727 belongs to Streptococcus pneumoniae R34-3127 (1313), including GCA_001126525.1/.2, GCF_001126525.1 and ATB run ERR068027. Candidate-ID collisions also include Paracoccus sp. AG06 taxon 401525; Nakamurella multipartita's SI-DP 169342; Myxococcus fulvus SI-DP 401525; Chrysosporium merdarium SI-ID 169342; Aeromonas marker AY169342; Salmonella CP169342 and PNUSAS401525; Escherichia run DRR401525; assembly statistics and an ATB SeqKit checksum. None supplies target evidence.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
