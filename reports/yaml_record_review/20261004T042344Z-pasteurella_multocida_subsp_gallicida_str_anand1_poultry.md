# YAML Record Review: Pasteurella multocida subsp. gallicida str. Anand1_poultry

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pasteurella_multocida_subsp_gallicida_str_anand1_poultry.yaml`
- Started UTC: 2026-10-04T04:21:47Z
- Finished UTC: 2026-10-04T04:23:44Z
- Verdict: needs curation

## Target

The full generated `TaxonRecord` identifies `NCBITaxon:1032866`, Pasteurella multocida subsp. gallicida str. Anand1_poultry, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:123812`. It has eleven root-first ancestors, code 11, `EXACT` grounding, `SEEDED` status and zero BacDive strains. Attestations are NCBITAXON, GTDB, GOLD and MADIN. Its seed event is dated 2026-09-13T17:54:04Z.

Future correction owners are maintained upstream source transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py`, associated tests/documentation and, only if inclusion changes, `curation/seed_scope.tsv`. The generated record remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pasteurella_multocida_subsp_gallicida_str_anand1_poultry.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pasteurella_multocida_subsp_gallicida_str_anand1_poultry.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched the complete backbone lineage, identity/code, own names, scope/PATHS registration, seed text and NCBI attestation. Source inventories, native genome/organism records and current NCBI metadata were inspected as evidence, not as substitutes for corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220928`, `data/catalog/ncbi_names-0005.jsonl.gz:30239-30240`, PATHS row 13329 and scope row 26080 agree on this strain. Live NCBI Taxonomy XML/Datasets agree on its label, rank, parent, genetic code and all eleven lineage IDs: 1, 131567, 2, 3379134, 1224, 1236, 135625, 712, 745, 747, 123812. The equivalent-name synonym retaining Anand1_poultry is supported. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032866)

The current XML additionally lists an Anand1poultry spelling as a misspelling. That alias is not present in the pinned name projection; this is a bounded source-version/name-coverage difference, not evidence that the retained identifier or preferred label is wrong. Any refresh should preserve its non-exact source class.

Anand1_cattle (1032867), Anand1_buffalo (1032868) and Anand1_goat (1032869) are distinct strain taxa, under subsp. multocida 44283 rather than this target's subsp. gallicida parent. The shared Anand1 prefix is not an identity key. The GTDB species association is supported, but its promotion to exact strain identity is not; see M1.

## Evidence

| Assertion | Inspected support and scope |
| --- | --- |
| NCBITAXON, 1 NAME | Backbone/name catalog and live taxonomy agree; snapshot date 2026-09-13 matches the attestation. |
| GTDB, 683 GENOME | `data/raw/gtdb_mappings.tsv:1353` and `gtdb_species.tsv:137724` reproduce the source mapping and cluster count. A complete structured metadata-catalog scan found 683 cluster members across 30 NCBI taxon IDs, with exactly one member assigned to 1032866. |
| GOLD, 1 ORGANISM | `gold_organisms.tsv:427` and native `data/gold/organisms.jsonl.gz:10139` identify Go0011541, taxid 1032866, strain Anand1_poultry. Its culture-collection field is empty. |
| MADIN, 3 TRAIT_ASSERTION | `madin_taxa.tsv:616` supports the aggregate count. Original transformed trait edges were unavailable in the configured upstream checkout, so their individual meanings were not independently audited or imported. |

The full GTDB target row at `data/catalog/gtdb_genomes-0014.jsonl.gz:18342` identifies GB_GCA_000219315.2, strain Anand1_poultry, taxid 1032866, species taxid 747, BioProject PRJNA66361 and BioSample SAMN02469635. The cluster also includes Anand1_goat and many other strains, subspecies and unclassified source taxa. A complete raw-mapping scan found 30 mappings for this cluster, including 29 closeMatch entries and a broadMatch entry for NCBI species 747. These predicates are not evidence of a one-to-one strain/species identity. GTDB places the cluster under Enterobacterales while NCBI uses Pasteurellales; the YAML properly carries NCBI's lineage without resolving that source hierarchy difference.

Native GOLD project row 9993 connects Gp0011541 to Go0011541, PRJNA66361 and SAMN02469635. Analysis row 7690 connects Ga0014098 through that project to unversioned GCA_000219315, WGS accession AFRR00000000 and IMG 2529293057. These corroborate taxon/genome context but do not supply a registered culture-deposit match. GOLD organism/project/analysis identifiers are not assemblies.

Native BV-BRC row `data/bvbrc/bvbrc-0000.jsonl.gz:3180` identifies 1032866.4, GCA_000219315.2, the same taxid, strain, BioProject and BioSample, but has no culture_collection field. The raw strain name alone is insufficient to create a culture-identifier join.

Live NCBI Datasets confirms GCA_000219315.2/ASM21931v2 as a current contig-level GenBank assembly of this exact strain, with 489 contigs and the same project/sample. Its paired GCF_000219315.1 is suppressed. Assembly ESearch returned two entries; both ESummary records were inspected: UID 467868 represents the current GenBank/ suppressed RefSeq pair, while UID 292548 is the suppressed earlier GCA_000219315.1 and points to .2 as latest. Thus two search results do not mean two independent current genomes. [NCBI assembly](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000219315.2/)

The current GenBank catalog row is `ncbi_genbank-0000.jsonl.gz:3728`; historical GenBank/RefSeq rows are respectively shard 0000 rows 1091 and 1065. They preserve the suppressed statuses. RefSeq exclusion notes concern annotation completeness and frameshifted proteins, not a replacement taxonomic identity. No assembly quality or functional claim is added to this YAML. The record itself cites no DOI/PMID or marker sequence requiring literature verification; bulk WGS contigs were not fetched for this taxonomy-scope judgement.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, MediaDive or BactoTraits inventory entry, no direct backbone child, and no own-ID type-material, merged-ID or dropped-ID row. Zero strain_count is therefore consistent with the documented BacDive-subtree count. It does not imply that the taxon lacks a sequenced genome. The inspected GOLD/BV-BRC/GTDB records lack an eligible culture-collection key, so this review does not invent a deposit or attach sibling cultures.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, covering bounded 1032866, Anand1 and the full target stem. All 52 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned. No target-specific BacDive/StrainInfo deposit or separate history reference was found within these bounds.

An additional ignored-inclusive compressed search of `data/atb` and `data/catalog/allthebacteria.tsv.xz` found no SAMN02469635 or PRJNA66361 match. The numeric collision SAMEA1032866 instead belongs to an ATB Streptococcus equi record with run ERR045920 and is not this strain's BioSample. Other Anand1 assemblies, projects and taxa were kept separate.

Empty nomenclature and functional fields are appropriate for the present strain record. No graph, gene, expression-module, resistance or pathway assertion is made, so iModulonDB is not applicable and no functional representation is required.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **M1 - Major: species-cluster membership is represented as an exact strain synonym.** YAML lines 49-52 label `Pasteurella multocida` an `EXACT_SYNONYM` of Anand1_poultry and lines 56-57 add the GTDB species to identity xrefs. The source cluster spans 683 genomes/30 NCBI taxon IDs; only one member belongs to this strain. `src/taxonmech/seed.py` treats every closeMatch as identity and emits both assertions, relying on a one-to-one assumption not satisfied here. The mapping/count are source-faithful, but the exact identity claim is over-scoped. Maintained owners: upstream GTDB-NCBI mapping generation, `src/taxonmech/extract.py`, identity-promotion logic in `src/taxonmech/seed.py`, and mapping documentation/tests. The preferred NCBI strain identity is sound, so this is major rather than a wrong-target blocker.

## Recommended Edits

1. Correct the maintained identity-promotion rule: source closeMatch alone must not make a broader GTDB species an exact synonym/xref of an NCBI strain. Preserve supported membership/classification context and provenance. Inspect upstream mapping direction/cardinality before choosing a different predicate; do not mechanically replace closeMatch with another relation.
2. Regenerate after the maintained fix, removing the unsupported exact species synonym and identity-only xref while retaining the supported NCBI equivalent name and qualified GTDB association. Explain that 683 is the source cluster's genome count, not Anand1_poultry's genome count; do not silently change the defined count to one.
3. Any future genome enrichment must preserve the supplied GOLD accession without inventing a version, distinguish current GenBank from suppressed RefSeq/older GenBank entries, and avoid transferring metadata from the other Anand1 strains. No deposit should be inferred from a bare strain name.

## Follow-up Checks

Add a focused generator regression for this strain: no exact species synonym from cluster membership, supported GTDB association retained, cluster count scope explicit, and the NCBI strain synonym/lineage unchanged. Include a supported species-level identity control.

After an authorized maintained-input fix, run `just seed-canary NCBITaxon:1032866 --force`, inspect the written YAML, and repeat both focused validators. No canary ran here. Recheck the live name-class difference and source assembly statuses during refresh. Restore the pinned Madin/GTDB transformed inputs before independently reproducing those edge derivations, and run corpus-wide gates before a broader release.

## Additional Notes

The live GTDB tree could not be retrieved by the web tool; the complete pinned metadata and mapping inventories support the bounded cluster finding. The configured upstream checkout lacks the transformed input files, as confirmed by an ignored-inclusive inventory during this review session. Aggregate inventory matches do not claim independent validation of the unavailable Madin trait edges.

No clinical, host-range, virulence or phenotype inference was made from the strain name or genome source metadata. No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written, and previous reports were preserved.
