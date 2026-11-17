# YAML Record Review: Pedosphaera parvula

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pedosphaera_parvula.yaml`
- Started UTC: 2026-10-04T01:04:23Z
- Finished UTC: 2026-10-04T01:09:16Z
- Verdict: pass

## Target

Read all 67 lines of this generated TaxonRecord. It denotes species `NCBITaxon:1032527`, Pedosphaera parvula, in BACTERIA, with EXACT grounding and SEEDED mapping status. It is not the separate Ellin514 child taxon `NCBITaxon:320771`. The record contains ten lineage entries, two NCBI authority-name related synonyms, genetic code 11, zero listed strains, two source attestations and one seed event. No phenotype, genome equivalence or causal graph is asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pedosphaera_parvula.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pedosphaera_parvula.yaml`: passed, one file, zero errors. The validator refreshed `reports/instance_validation_failures.tsv`.
- Structured comparisons checked all carried lineage entries, authority synonyms, exact taxon source inventories, scope, path index, complete descendant closure and BacDive strain inventory. These are read-only comparisons, not a substitute for corpus reproduction.
- Not checked: `just verify-corpus`, `just qc`, full tests, global provenance/history/product gates and rendering. They were not run as part of this focused review; no undocumented focused replacement was claimed. The record has no curator-added graph identifiers or external history references requiring a record-specific term/reference gate.
- Public NCBI taxonomy XML and Datasets responses were inspected. PubMed and PMC browser requests returned a browser challenge; the publisher full-text URL was inaccessible. Europe PMC bibliographic metadata and the SeqCode JSON API were accessible. Full publication text was not verified and was not used to assert phenotype or genome equivalence.

## Identity and Grounding

The pinned backbone row at `data/raw/ncbitaxon_taxa.tsv:220867` and live NCBI EFetch/Datasets agree on ID, species label, parent `NCBITaxon:1032526` (Pedosphaera), bacterial domain, genetic code 11 and all ten root-first ancestors. The chain includes Pseudomonadati, PVC group, Verrucomicrobiota, Pedosphaerae, Pedosphaerales and Pedosphaeraceae. The [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032527) also displays the lineage and Ellin514 child.

Native NCBI names in `data/catalog/ncbi_names-0005.jsonl.gz:30157` through 30159 distinguish the scientific name from the Kant et al. 2011 and Ozyurt 2008 authority strings. Both quoted authority strings are retained as RELATED_SYNONYM, not formal exact-name equivalence or a claim of valid publication. Live taxonomy agrees. Exact structured checks found no own-ID row in `ncbi_merged_ids.tsv` or `dropped.tsv`.

[LPSN name 1108](https://lpsn.dsmz.de/species/pedosphaera-parvula) identifies the Kant et al. name as not validly published and preferred rather than a correct name, with Ellin514 as nomenclatural type. NCBI type-material rows 1623-1624 independently retain `personal::Ellin514` and `strain Ellin514`. The YAML does not contradict that status: EXACT refers to its NCBI identity, not nomenclatural validity.

## Evidence

The NCBITAXON attestation is one NAME from the 2026-09-13 snapshot. `data/raw/madin_taxa.tsv:612` supplies exactly two directly filed TRAIT_ASSERTION records. This count is not two experimentally validated phenotypes and does not gather descendant assertions. No exact target row was found in the structured BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive or BactoTraits inventories.

`data/taxa/PATHS.tsv:13241`, `curation/seed_scope.tsv:57232` and `curation/legacy_page_paths.tsv:777` agree on the target and slug. The scope date is 2026-09-12; the 2026-09-13 seed event correctly names the two attesting sources. SEEDED is retained and is not represented as human REVIEWED.

[Europe PMC metadata for PMID 21460084](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:21460084%20AND%20SRC:MED&format=json) resolves the Kant et al. 2011 genome paper, DOI `10.1128/jb.00299-11`, and PMCID `PMC3133123`. This confirms bibliographic context for the authority string. It does not justify applying Ellin514-specific experimental observations to every genome filed under this species. The Ozyurt authority was verified as an NCBI name assertion, not independently authenticated as a publication.

The cataloged Ellin514 isolate assembly is `GCA_000172555.1` with explicitly identical paired RefSeq `GCF_000172555.1`, taxon 320771, BioSample `SAMN00000631`, 7,414,222 bp and 102 contigs. Native GenBank/RefSeq rows are `ncbi_genbank-0000.jsonl.gz:2265` and `ncbi_refseq-0000.jsonl.gz:2001`. GOLD preserves the explicit `Go0001332 -> Gp0001332 -> Ga0031580` chain to that GenBank assembly and IMG `645058870`; the organism culture-collection field is empty. BV-BRC `320771.20` and deprecated `320771.5` retain separate source statuses. These are catalog facts, not deposit-backed links carried by this YAML.

## Completeness

The complete pinned descendant closure is exactly this species plus Ellin514 (320771). A full structured scan of `bacdive_strains.tsv` found no classified strain for either. Thus `strain_count: 0` is correct for the maintained BacDive representation; it does not deny the existence of the cultured isolate or its genome. The maintained CAFI matcher rejects the bare Ellin514 name and both NCBI type-designation strings as collection join keys.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifiers, label, slug and Ellin514 context across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. A recursive structured SOURCE.json search also included ignored files. Exact structured checks disambiguated numeric collisions and source namespaces. No target-specific standalone history record or native BacDive/StrainInfo deposit was found on these searched surfaces.

A complete structured LPSN inventory scan found neither exact `lpsn:1108` nor a Pedosphaera name. This is a bounded live-source enrichment opportunity, not proof that the pinned transform was incompletely reproduced: `docs/SOURCE_COVERAGE.md` promises every name in that transform, not a live LPSN mirror. A future supported addition belongs upstream in the kg-microbe LPSN transform and its explicit taxon mapping, then `src/taxonmech/extract.py::extract_lpsn` and the generated inventories. Do not hand-add nomenclature to this YAML.

The native SeqCode census retains name 36798 at `data/seqcode/names.jsonl.gz:34911`. Its [live API record](https://api.seqco.de/v1/names/36798.json) reports Automated discovery, no defined nomenclatural type and warnings for missing description, type and proposing publication. It is not evidence of SeqCode validation or a type genome. Its Verrucomicrobiia/Limisphaerales classification differs from NCBI; source classifications must remain distinct.

No carried GTDB mapping, cultured-deposit genome link, causal graph or general phenotype assertion requires completion by inference. Native GTDB coverage is described below; a descendant's source metadata must not be silently promoted into a parent mapping.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the claims carried by this record. The LPSN enrichment opportunity and external genome-classification conflicts are explicitly bounded above and below; neither establishes an incorrect value or a missing required representation in this generated YAML.

## Recommended Edits

None required for the reviewed record. Preserve the generated-file boundary and SEEDED status. Any optional LPSN refresh must preserve the invalidly published/preferred-name status and source-supported type designation. Its owner is the maintained upstream transform and extractor, not this report or generated YAML.

Do not create culture links from Ellin514, taxonomy IDs, sample co-occurrence or the GOLD chain alone. A future deposit-backed link requires an eligible complete collection accession and the source-specific evidence chain defined in `docs/STRAIN_GENOMES.md`.

## Follow-up Checks

For an authorized source refresh, inspect the new LPSN source node and explicit NCBI mapping, re-extract the inventory, preview seeding, generate a single canary with `just seed-canary NCBITaxon:1032527 --force`, inspect its emitted fields, and rerun both focused validators. Before publishing regenerated products, run the documented full provenance, reproduction, history, tests and `just qc` gates.

Any future use of the MAGs below requires assembly-specific classification review. Neither NCBI nor GTDB taxonomy alone establishes identity with the cultured Ellin514 isolate. iModulonDB is not applicable: this record has no gene, regulator, locus, pathway or transcriptomic claim.

## Additional Notes

A full structured scan of all 901,341 pinned GTDB genome rows found nine rows for species 1032527, all filed under child taxon 320771. `RS_GCF_000172555.1` at `gtdb_genomes-0008.jsonl.gz:32481` is the representative of `s__Pedosphaera sp000172555`, with strain identifier Ellin514 and genome category none. This differs from NCBI's species name and class/order. It was not absent from the catalog; a compact reread recovered it after an earlier text search output was truncated.

The remaining eight rows are explicitly metagenomic, despite carrying the NCBI organism name Pedosphaera parvula Ellin514. GTDB places `GCA_943322435.2` in Fibrobacterota, `s__UBA11236 sp947482115`, and `GCA_943329295.2` in Cyanobacteriota, `s__Cyanobium sp943324725`. The other six (`943331745.1`, `943332515.1`, `943333225.1`, `943333805.2`, `945866295.1`, `945872975.1`, all GCA accessions) belong to `s__JADJPG01 sp943332515`; `GCA_943332515.1` is that cluster's representative. These native conflicts are preserved as context, not resolved by relabeling this NCBI lineage or treating the MAGs as Ellin514 cultures.

The species-filed `GCA_016191705.1` is another metagenomic assembly (BioSample `SAMN15435427`, isolate NC_groundwater_788_Ag_S2p5_62_4; 1,510,391 bp, 1,038 contigs), without a paired RefSeq or eligible collection identifier. BV-BRC `1032527.4` is corresponding source context, not evidence of Ellin514 equivalence. Historical assembly versions and differing source sample assertions were not silently collapsed. An isolate value 1032527 on unrelated Streptococcus pneumoniae `GCA_058712165.1` is a numeric collision, not the target taxon.

Only this new review report was manually written. No taxon, source inventory, code, scope, audit status, history entry, GitHub item or generated page was changed.

