# YAML Record Review: uncultured gamma proteobacterium TIHP302-31

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_31.yaml`
- Started UTC: 2026-10-04T04:20:32Z
- Finished UTC: 2026-10-04T04:21:00Z
- Verdict: pass

## Target

Full generated `TaxonRecord` reviewed: `NCBITaxon:103286`, uncultured gamma proteobacterium TIHP302-31, `SPECIES`, `BACTERIA`, parent `NCBITaxon:50423`. The record has seven ancestors, code 11, `EXACT` grounding, `SEEDED` status, zero strains and one NCBITAXON `NAME` attestation. Synonym, nomenclature, external mapping, genome and causal-graph fields are empty. The seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong in maintained source/extraction inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, not in this generated YAML.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_31.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_31.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured evidence checks matched the complete backbone lineage, identity/code, names, scope/PATHS registration, attestation and seed text. No custom focused substitute for corpus reproduction was used.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendered pages. No canary or regeneration ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18395`, `data/catalog/ncbi_names-0000.jsonl.gz:38413`, PATHS row 13328 and scope row 144055 agree. Live NCBI Taxonomy XML and Datasets confirm the name, species rank, parent, code and seven ancestor IDs: 1, 131567, 2, 3379134, 1224, 1236, 50423. Datasets and the local backbone include root 1, which the XML's displayed lineage omits. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103286)

This denotes a Gammaproteobacteria environmental clone, not a formally described cultured species or collection deposit. The NCBI rank is faithfully retained without inferring nomenclatural standing or a more specific placement.

## Evidence

The pinned backbone supplies no synonym, retirement target or non-NCBI attestation. The 2026-09-13 snapshot date, count of one name and seed-history source list are reproduced exactly; the scope reason also matches.

The exact-taxid Nuccore query returned one record, fetched with its source feature and references. AB031617.1 is a 656-base partial 16S rRNA sequence with explicit taxon 103286, clone TIHP302-31, environmental-sample status and coastal marine sediment as the isolation source. This supports the clone identity, not a whole-genome assembly or metabolic phenotype. [GenBank AB031617.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031617.1)

Its references identify an unpublished Urakawa/Yoshida/Nishimura/Ohwada coastal-community 16S/quinone study and Urakawa's direct submission dated 1999-08-25. Neither supplies a PMID or DOI in the inspected sequence record. No published citation or clone-specific functional inference was invented from the community-study title.

The exact-taxid Assembly query returned zero with phrase-not-found/no-items diagnostics. This is a bounded current retrieval result, not a universal assembly-absence claim.

## Completeness

Complete exact-ID scans of the seven BacDive/LPSN/GTDB/GOLD/MediaDive/Madin/BactoTraits inventories returned no target rows. The backbone has no direct child, and complete own-ID scans of type-material, merged-ID and dropped-ID tables returned no row. Empty optional fields are consistent with the evidence.

The search included ignored files: `rg --no-ignore --hidden -n -z -i` covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history` for bounded 103286, TIHP302-31 variants and the file stem. All 33 matched lines and structured contexts were inspected. Separate SOURCE.json scans found two BacDive request contexts for BacDive ID 103286, not support for this NCBI taxon. No target-specific culture, assembly or separate history reference was found within those bounds.

Excluded collisions include:

- CIP 103286 is Pasteurella multocida subsp. multocida W-9217, BacDive 11729, represented under taxids 44283/747. Its own StrainInfo deposit is SI-DP141223 in SI-ID3815. AY702502 and GU594189 are its partial sodA/23S sequences, not clone genomes.
- BacDive 103286 is Agromyces ST000825, taxid 51513. DSM 103286 is Escherichia phage vB_EcoM_HdK5, taxid 2508197, own SI-DP904084.
- MGBC103286 is a Bacteroidales genome GCA_948674985.1, taxid 194843; FLAG-103286 is Listeria GCA_050884965.1. CP103286 belongs to Parabacteroides distasonis BFG-574/GCA_024760285.1.
- ATB DRR103286 belongs to E. coli sample SAMD00077694. Numeric contig/scaffold statistics from other taxa do not establish identity.

iModulonDB is not applicable because no gene, regulator, expression-module or functional assertion is made. No causal graph or other required representation is missing.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed identity, provenance and completeness scope.

## Recommended Edits

None. Retain the environmental clone identity, NCBI-defined rank and empty unsupported fields. Any later evidence-backed enrichment must enter through maintained inputs and the generator.

## Follow-up Checks

After a future authorized source refresh, recheck taxid 103286/AB031617.1, inspect output from `just seed-canary NCBITaxon:103286 --force`, and repeat both focused validators. The canary was not run here. Corpus-wide gates remain required for broader regeneration/publication.

## Additional Notes

The assembly miss and source-inventory misses are bounded by the searched roots, snapshot and current query. No YAML, source input, curation event, status, separate history, generated page or GitHub item changed. Only this new report was manually written; earlier reports remain untouched.
