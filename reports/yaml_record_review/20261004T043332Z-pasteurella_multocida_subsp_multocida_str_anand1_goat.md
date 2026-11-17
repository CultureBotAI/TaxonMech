# YAML Record Review: Pasteurella multocida subsp. multocida str. Anand1_goat

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pasteurella_multocida_subsp_multocida_str_anand1_goat.yaml`
- Started UTC: 2026-10-04T04:32:04Z
- Finished UTC: 2026-10-04T04:33:32Z
- Verdict: needs curation

## Target

The full generated `TaxonRecord` identifies `NCBITaxon:1032869`, Pasteurella multocida subsp. multocida str. Anand1_goat, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:44283`. It carries eleven root-first ancestors, code 11, `EXACT` grounding, `SEEDED` status, zero BacDive strains and NCBITAXON/GTDB/GOLD/MADIN attestations. Its seed event is dated 2026-09-13T17:54:04Z.

Future fixes belong to maintained upstream mapping transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py`, associated tests/documentation and, only for changed inclusion, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pasteurella_multocida_subsp_multocida_str_anand1_goat.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pasteurella_multocida_subsp_multocida_str_anand1_goat.yaml`: passed, one file and zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched complete backbone identity/lineage/code, own NCBI names, scope/PATHS registration, source inventory counts and seed text. Native and live evidence checks do not substitute for corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone row `data/raw/ncbitaxon_taxa.tsv:220931`, name-catalog shard 0005 rows 30245-30246, PATHS row 13332 and scope row 26081 agree on the exact strain. Current NCBI EFetch and Datasets confirm its label, strain rank, parent 44283, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 135625, 712, 745, 747, 44283. The retained NCBI equivalent-name synonym is supported. [NCBI Taxonomy API](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032869&retmode=xml)

Current XML additionally includes Anand1goat as a misspelling, absent from the pinned name catalog. This is a bounded source-version/name-coverage difference; a refresh should preserve its non-exact class. It is not evidence that the preferred identifier or label is wrong.

The other Anand1 taxa are distinct: poultry 1032866, cattle 1032867 and buffalo 1032868. Poultry has subsp. gallicida parent 123812 rather than this target's subsp. multocida parent. The broad GTDB species association is supported, but its promotion to exact strain identity is not; see M1.

## Evidence

| Assertion | Inspected support and scope |
| --- | --- |
| NCBITAXON, 1 NAME | Pinned backbone/name catalog and live taxonomy agree; the 2026-09-13 snapshot date matches the attestation. |
| GTDB, 683 GENOME | `data/raw/gtdb_mappings.tsv:1354` and `gtdb_species.tsv:137724` reproduce the cluster mapping/count. A complete scan of 901,341 native metadata rows found 683 distinct cluster accessions across 30 NCBI taxon IDs, one assigned to this target. |
| GOLD, 1 ORGANISM | `data/raw/gold_organisms.tsv:430` and `data/gold/organisms.jsonl.gz:10177` identify Go0011581, taxid 1032869, strain Anand1_goat. The culture-collection field is empty. |
| MADIN, 1 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:619` supports the aggregate count. Original transformed trait edges are unavailable in the configured upstream checkout, so no individual phenotype assertion was independently reconstructed or imported. |

The full target GTDB row at `data/catalog/gtdb_genomes-0002.jsonl.gz:1235` is GB_GCA_000219335.2, taxid 1032869, species taxid 747, strain Anand1_goat, BioProject PRJNA66363 and BioSample SAMN02469636. Its strain-identifiers field contains only the bare designation. GTDB's cluster includes other strains and subspecies, including Anand1_poultry. All 30 raw cluster mappings were inspected: 29 closeMatch entries and one broadMatch to NCBI species 747. These predicates do not establish one-to-one strain/species identity. GTDB uses Enterobacterales while NCBI uses Pasteurellales; the YAML properly preserves NCBI lineage rather than reconciling the hierarchies.

Native GOLD project row 10031 connects Gp0011581 to Go0011581, PRJNA66363 and SAMN02469636. Analysis row 7689 identifies Ga0014097 and connects through that project, supplying unversioned GCA_000219335, WGS AFRS00000000 and IMG 2529293056. Its direct organism field is empty; the explicit project chain is consistent. The unversioned accession must not acquire an invented version. GOLD Go/Gp/Ga identifiers are not genome assemblies.

The full BV-BRC row `data/bvbrc/bvbrc-0000.jsonl.gz:3183` identifies 1032869.4, GCA_000219335.2 and the same exact strain/taxid/project/sample, but supplies no culture_collection field. Neither its bare strain name nor GTDB's creates a registered-deposit join.

The full current GenBank row `data/catalog/ncbi_genbank-0000.jsonl.gz:3729` and live Datasets agree on GCA_000219335.2/ASM21933v2, current and contig-level, with 349 contigs and 2,285,382 bp. Paired GCF_000219335.1 is suppressed. Exact-taxid Assembly ESearch returned two entries, both inspected by ESummary: UID 467888 represents the current GenBank/suppressed RefSeq pair; UID 292568 represents suppressed earlier GCA_000219335.1, with .2 as latest. These are not two independent current genomes. [NCBI assembly](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000219335.2/)

Historical GenBank shard 0000 row 1092 retains the .1 scaffold assembly and 2012-01-29 non-live date. Historical RefSeq shard 0000 row 1066 retains GCF_000219335.1 and 2020-07-29 non-live date; its PRJNA224116 differs from GenBank PRJNA66363. Native/live sources preserve annotation-completeness and frameshifted-protein exclusion notes. These quality limitations are not evidence of a changed taxon identity and are not imported as phenotype claims. The YAML cites no DOI/PMID or marker sequence; bulk WGS contigs were not fetched for this taxonomy-scope judgement.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, MediaDive or BactoTraits inventory row, no direct backbone child, and no own-ID type-material, merged-ID or dropped-ID row. Zero strain_count agrees with the BacDive-subtree definition and does not claim genome absence. The inspected native sources lack an eligible registered culture key, so missing optional deposit links are not filled from a bare designation or neighboring type strain.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` for bounded 1032869, Anand1 and the target stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 58 matched lines and structured contexts were inspected; SOURCE.json files were separately scanned. No target-specific BacDive/StrainInfo deposit or separate history reference was found within those bounds. Legacy target-page registration row 785 exists.

An additional ignored-inclusive compressed search in `data/atb` and `data/catalog/allthebacteria.tsv.xz` found no SAMN02469636 or PRJNA66363 match. SAMEA1032869 instead belongs to Streptococcus equi EQUI0055, taxid 148942, GCA/GCF_001176905.1, BV-BRC 148942.103 and ATB ERR064435/ERZ3067724. A genome-size value of 1032869 in Thermoplasmata assembly GCA_007130065.1 is also not a taxon-ID match. Neighboring Anand1 assemblies were kept separate.

No gene, resistance, pathway, expression-module or causal-graph assertion is present. Empty functional fields are appropriate and iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **M1 - Major: species-cluster membership is promoted to exact strain identity.** YAML lines 49-52 call Pasteurella multocida an `EXACT_SYNONYM` of Anand1_goat, and lines 56-57 add the GTDB species as an identity xref. The full cluster has 683 genomes across 30 NCBI taxa, with one genome belonging to this strain. `src/taxonmech/seed.py:451` treats any closeMatch as identity, and lines 466-469 emit both assertions, although its one-to-one assumption does not hold here. The source mapping/count are faithfully copied, but the synonym/xref overstate their meaning. Owners: upstream GTDB-NCBI mapping generation, `src/taxonmech/extract.py`, identity-promotion logic in `src/taxonmech/seed.py`, and mapping tests/documentation. The preferred NCBI strain identity remains correct, so this is major rather than a wrong-target blocker.

## Recommended Edits

1. Correct the maintained identity rule so a source closeMatch alone cannot make a species cluster an exact synonym/xref of a strain. Preserve supported membership/classification context and provenance. Inspect predicate direction and cardinality before changing upstream relations; do not mechanically substitute a different predicate.
2. Regenerate after the maintained fix, removing the unsupported exact species synonym and identity-only xref while retaining the supported NCBI synonym, lineage and qualified GTDB association. The 683 count belongs to the cluster, not the strain; do not silently replace it with one.
3. Future genome enrichment must preserve GOLD's unversioned accession, distinguish current GenBank from suppressed RefSeq/older GenBank and retain distinct BioProjects. Do not invent deposits from strain labels or transfer sibling metadata.

## Follow-up Checks

Add a focused regression proving no exact species synonym/xref arises from cluster membership, while the qualified GTDB association/count and exact NCBI strain identity remain. Include a supported species-level identity control. After an authorized fix, run `just seed-canary NCBITaxon:1032869 --force`, inspect the YAML and repeat both focused validators. No canary ran here.

Recheck source assembly statuses and the extra live misspelling during refresh. Restore pinned transformed GTDB/Madin inputs before independently reproducing their edge derivations, and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the GTDB tree or this NCBI browser page. Direct public NCBI EFetch, Datasets and ESummary succeeded, and the complete pinned GTDB catalog/mappings support M1. The configured upstream checkout was inventoried with ignored files included and contains only two NLP files, not the original transformed edges; raw aggregate agreement does not imply independent reconstruction.

No clinical, host-range, virulence or phenotype inference was made from the strain name or source genome metadata. No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written, with prior reports preserved.
