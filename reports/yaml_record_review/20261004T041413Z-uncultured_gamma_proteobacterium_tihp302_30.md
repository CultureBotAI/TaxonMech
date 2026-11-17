# YAML Record Review: uncultured gamma proteobacterium TIHP302-30

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_30.yaml`
- Started UTC: 2026-10-04T04:13:31Z
- Finished UTC: 2026-10-04T04:14:13Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` reviewed: `NCBITaxon:103285`, uncultured gamma proteobacterium TIHP302-30, `SPECIES`, `BACTERIA`, parent `NCBITaxon:50423`. It has seven root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero listed strains and one NCBITAXON name attestation. There are no synonym, nomenclature, external mapping or causal-graph claims. Its sole seed event is dated 2026-09-13T17:54:04Z.

Maintained owners for any future correction are source inventories/extraction in `src/taxonmech/extract.py`, generation in `src/taxonmech/seed.py`, and inclusion in `curation/seed_scope.tsv`; this generated YAML is not a manual-edit target.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_30.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_30.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured source checks verified the entire local lineage, rank/label/parent/code, names, exact-ID source inventories, scope/PATHS entries, seed text and attestation. These evidence checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or site rendering. No focused substitute was invented, and no regeneration was run.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18394`, `data/catalog/ncbi_names-0000.jsonl.gz:38412`, `data/taxa/PATHS.tsv:13326` and `curation/seed_scope.tsv:144054` agree on the target. Live NCBI Taxonomy XML and Datasets independently agree on the identifier, scientific name, species rank, parent, code and the seven-ID chain: 1, 131567, 2, 3379134, 1224, 1236, 50423. NCBI XML omits the root from its displayed lineage; Datasets and the local backbone include it. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103285)

This is an environmental clone taxon under Gammaproteobacteria/environmental samples, not a cultured isolate or formally named species. The species rank is NCBI's rank, not a claim of nomenclatural standing. No more specific classification is inferred.

## Evidence

The local backbone has no synonyms, retirement target or additional source attestation for this ID. Its 2026-09-13 snapshot supports the single `NAME` attestation. The scope reason and seed-history source list match exactly.

Exact-taxid Nuccore search returned one result; its full source feature and references were inspected. `AB031616.1` is a 710-base partial 16S rRNA sequence with explicit `taxon:103285`, clone TIHP302-30, an environmental-sample qualifier and coastal marine sediment as isolation source. It is not an assembly, strain deposit or trait measurement. [GenBank AB031616.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031616.1)

The sequence cites an unpublished Urakawa, Yoshida, Nishimura and Ohwada coastal-community study using 16S/quinone profiling, plus Urakawa's direct submission dated 1999-08-25. No PMID or DOI is supplied in those sequence references. The community-study title does not establish a clone-specific metabolic phenotype. No literature identifier, quotation, trait or culture claim has been added to the YAML.

Exact-taxid Assembly search returned zero results with NCBI's phrase-not-found/no-items warning. This is a bounded retrieval result, not proof that no assembly exists anywhere.

## Completeness

Complete structured scans found no exact target row in BacDive, LPSN, GTDB mappings, GOLD, MediaDive, Madin or BactoTraits inventories; no direct child in the backbone; and no own-ID type-material, merged-ID or dropped-ID row. Together with the clone evidence, these support leaving optional culture, genome, mapping and nomenclature fields empty.

The absence search included ignored files: `rg --no-ignore --hidden -n -z -i` searched `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history` for bounded 103285, TIHP302-30 spelling variants and the file stem. All 41 matched lines and their structured contexts were inspected. SOURCE.json manifests in the source roots were scanned separately; their two BacDive matches are requests for BacDive ID 103285, not NCBI taxon evidence. No target-specific deposit, assembly or separate history reference was found within these bounds.

Important collisions were explicitly excluded:

- CIP 103285 is Pasteurella multocida subsp. gallicida, taxid 123812, BacDive 11737, StrainInfo SI-ID43125/own SI-DP141207. Its GOLD Go0289381 species-level context and partial sodA accession AY702501 do not concern the clone or supply a clone assembly.
- BacDive 103285 is Agromyces ST000943, taxid 51513. SI-DP103285 is ATCC 23846, Escherichia coli taxid 562; DSM 103285 is Escherichia phage vB_EcoS_HdH2, taxid 2508174, own SI-DP913873.
- Limosilactobacillus fermentum SRCM103285, Listeria FLAG-103285, Muribaculaceae MGBC103285 and Dactylosporangium NAICONS 103285 have their own labels/taxids. Their assemblies, including GCA/GCF_004063515.1 and GCA_948696655.1, are not target evidence.
- CP103285 belongs to Bacteroides thetaiotaomicron BFG-119; ATB run DRR103285 belongs to an E. coli sample SAMD00077693. Contig statistics and a checksum containing 103285 are not identity links.

iModulonDB is not applicable: the record makes no gene, regulator, expression-module, pathway, resistance or functional claim. No causal graph or additional required representation is missing.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed identity, provenance and completeness scope.

## Recommended Edits

None. Preserve the source-defined environmental identity and empty optional fields. Any future source-backed enrichment belongs in maintained extraction/seeding inputs, not a handwritten change to the generated record.

## Follow-up Checks

After a future authorized source refresh, recheck the exact taxid and AB031616.1, inspect `just seed-canary NCBITaxon:103285 --force` output, and repeat the two focused validators. The canary was not run during this review. Run documented corpus-wide gates before a broader publication or regeneration change.

## Additional Notes

This report does not equate record completeness with biological completeness: the assembly miss and sparse source coverage are bounded by the inspected snapshot and current NCBI query. No curation event, status promotion, source regeneration, site update or GitHub mutation was performed. Only this new report was manually written; existing reports and the YAML were left unchanged.
