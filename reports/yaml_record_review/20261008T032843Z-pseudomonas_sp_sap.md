# YAML Record Review: Pseudomonas sp. SAP

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_sap.yaml`
- Started UTC: 2026-10-08T03:22:15Z
- Finished UTC: 2026-10-08T03:28:43Z
- Verdict: pass

## Target

One generated `TaxonRecord`: `NCBITaxon:1036184`, Pseudomonas sp. SAP, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821` (unclassified Pseudomonas), genetic code 11, grounding `EXACT`, mapping status `SEEDED`. All 53 YAML lines were read before judgement.

`data/taxa/PATHS.tsv:14815` and `curation/seed_scope.tsv:322556` agree on this identifier and slug. The scope row was added on 2026-09-13 under the one-source attested rule; the embedded seed event is dated `2026-09-13T17:54:04Z`. The record is an NCBI species-rank placeholder, not a claim of a validly published species name or a deposited type strain.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudomonas_sp_sap.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_sap.yaml --out /private/tmp/psap-strict.tsv` | Pass; one file, zero errors; TSV contains only its header. |
| Structured backbone and lineage comparison | Identity, rank, parent, genetic code, all ten ancestors, empty synonym inventory, and sole NCBI attestation agree. |
| Source inventory, scope, and index checks | Exact-ID searches across the seven other source inventories returned no target rows; scope and index each have one exact target. |
| Native catalog and live authority checks | All seven source-search candidate rows/objects were read in full; live NCBI taxonomy, exact-taxon sequence search, and the resulting marker metadata were inspected. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. The bounded comparisons are diagnostics, not a substitute for corpus reproduction. There is no documented focused reference validator for this record. `just validate-products` targets curator-added causal-node labels and is not applicable to this graph-free record. Ignored-inclusive searches found no target-specific separate history artifact for `just validate-history`; the embedded seed event was checked directly. No new history event is authorized by this read-only review.

## Identity and Grounding

The complete pinned backbone row `data/raw/ncbitaxon_taxa.tsv:222309` and complete native name object `data/catalog/ncbi_names-0005.jsonl.gz:31850` resolve the exact taxon to Pseudomonas sp. SAP. Live NCBI Taxonomy XML independently confirms taxon 1036184, the species rank, parent 196821, and genetic code 11. Datasets agrees and supplies the complete root-first lineage. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036184&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036184).

The ten ancestors are root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae, Pseudomonas, and unclassified Pseudomonas. Each identifier, label, and rank matches the pinned parent chain; live NCBI supports the same chain. The XML omits root from its lineage, whereas Datasets includes taxon 1. The unranked direct parent is not a reason to change the child's explicitly supplied species rank. No children occur in the complete pinned backbone comparison.

The initial broad name search also found longer SAP-prefixed labels. A second ignored-inclusive search with exact taxon and terminal name/slug boundaries resolved only this YAML plus its index and scope rows. Evidence from SAP705_1, SAP02_2, and other longer labels was not transferred to this target.

## Evidence

| Claim or candidate | Evidence and assessment |
| --- | --- |
| NCBI identity and sole attestation | The full backbone and native scientific-name row agree with `source: NCBITAXON`, `source_id: NCBITaxon:1036184`, the exact label, count 1, unit NAME, and snapshot 2026-09-13. This is a count of source names, not genomes, deposits, or experiments. |
| No listed BacDive strains | The full exact-ID scan of `data/raw/bacdive_strains.tsv` returned no row, and the backbone contains no descendants from which strains could be gathered. The native-source search found no supported BacDive/deposit object. `strain_count: 0` describes the available BacDive classification inventory; it does not mean that the isolate never existed. |
| Other source fields | Exact-ID scans returned no LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventory row. Compressed ignored-inclusive searches across the full named native-catalog roots found no exact target entry in those sources, StrainInfo, or SeqCode. Empty nomenclature, mappings, type-material, and deposit-linked genome slots are not filled by guessing. |
| Status and history | Exact-ID scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` found no matching rows. The seed event's source list and scope reason match the maintained scope and inventory. No separate curation event or status promotion was made. |
| Rejected GenBank matches | Full `data/catalog/ncbi_genbank-0042.jsonl.gz:26557` is GCA_046125715.1, Klebsiella michiganensis, taxon 1134687; its sample SAMN41036184 contains the search digits. Full `data/catalog/ncbi_genbank-0066.jsonl.gz:39385` is GCA_982844945.1, Flavobacteriaceae bacterium, taxon 1871037; its ungapped genome length is 1036184. Neither is evidence for this Pseudomonas record. |
| Rejected ATB matches | Full `data/catalog/allthebacteria.tsv.xz:2291220` describes Salmonella enterica sample SAMN27620242; the digit match is in its SeqKit sum. Row 2876809 describes sample SAMN41036184 with unknown name and NO_RUNS status. Neither supports a target sample or strain link. |
| Live unpublished name | NCBI's taxonomy response additionally supplies Pseudomonas tyrosinaticus with name class `unpublished name`. It is absent from the pinned scientific-name object and backbone synonyms. This is a live-interface versus pinned-catalog difference, not proof that the YAML miscopied its source, nor evidence of valid publication. No exact-synonym or LPSN status was inferred. |
| Live marker candidate | Exact-taxon Nuccore search returned one UID, 334361613. Complete source/reference metadata identifies JF838195.1 as a 1,437-bp partial 16S rRNA sequence from strain SAP with `taxon:1036184`; it has no culture-deposit identifier or genome assembly. Its source metadata and unpublished submission title provide context, not peer-reviewed proof of a phenotype. The sequence is not represented as a genome. [Marker record](https://www.ncbi.nlm.nih.gov/nuccore/JF838195.1). |

There are no DOI, PMID, phenotype, gene-function, pathway, habitat, or causal-edge assertions in the YAML. iModulonDB is not applicable. The marker's unpublished title concerning L-DOPA production was not promoted to experimental evidence or used to populate a causal graph. Bases and non-source sequence features were not reanalyzed.

## Completeness

No consequential gap was established under the current source-owned model. The record is complete for its sole pinned NCBI attestation. Optional literature evidence, nomenclature, mappings, discussions, strain lists, and causal graphs need not be invented for an unclassified NCBI entry. No eligible culture-deposit relationship supports adding the live marker to a StrainInfo or BacDive strain block.

The exact record-resolution search included ignored files across `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`. It found no prior target report or target-specific history artifact. Source searches used `rg --no-ignore --hidden -z` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. The seven candidate addresses were fully read: backbone and scope rows, one genuine scientific-name object, and four unrelated numeric matches. All five `SOURCE.json` files were separately parsed and history filenames independently inspected.

Additional ignored-inclusive searches over those same ten roots found no occurrence of Pseudomonas tyrosinaticus, JF838195, or marker UID 334361613. These are bounded statements about the pinned sources, not proof of global online absence. Live exact-taxon NCBI Assembly search returned zero items together with a `phrasesnotfound` warning; it is recorded as that query result, not used as proof that no assembly exists anywhere.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, rank, domain, sole source attestation, zero classified-strain count, and seeded provenance are supported within the inspected scope. The extra live unpublished name is a documented source-surface difference, not a demonstrated generator defect. No finding is inferred from unrelated records or an unsuccessful web search.

## Recommended Edits

None required for the reviewed record. Do not hand-edit its generated YAML, invent a type strain, or join genomes by the bare SAP designation.

At a normal authorized NCBI source refresh, compare the source name classes with the live unpublished-name entry. `conf/ncbi_taxdump.yaml` owns the pinned primary snapshot; `src/taxonmech/ncbi_taxdump.py:84` through 93 parses names and assigns non-synonym/non-equivalent classes to related scope. If the new pinned dump actually supplies this alias, retain that scope through extraction and seeding rather than presenting it as a published correct name. This is an optional source-refresh check, not an instruction to patch the existing inventory or create a nomenclatural record.

## Follow-up Checks

- If maintained source inputs change, recheck exact taxon 1036184, parent 196821, all ten ancestors, genetic code 11, and the source name class before an authorized one-record seed canary.
- Rerun the one-record schema and strict commands after any authorized regeneration. Recheck that counts and source units still agree with the refreshed inventories.
- Require an explicit eligible culture-deposit/source relationship before importing a strain-linked assembly or marker. A matching SAP substring, taxon number embedded in another field, or generic genus similarity is insufficient.
- Run corpus reproduction, provenance, rendering, documentation, and QC gates before publishing maintained-input changes. Validate a new append-only history event only if later curation actually creates one.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report target SHA-256: `259d72fe40a0887fc71f737d0f8b4a7b4a42845670d01a2aedbbffc0b9c02f8b`. No YAML, source, scope, lifecycle, or history change was made. Existing reports and worktrees were preserved; Eukaryota was neither re-reviewed nor edited. No paid research, outreach, or GitHub mutation occurred.

The web-tool NCBI browser page was unavailable; successful primary Taxonomy XML and Datasets responses supplied the authority check. General exact-name web searches produced broader unrelated material and were not used as supporting evidence. No archive was downloaded, no source snapshot was refreshed, and no whole-corpus validation pass is claimed. The review verdict does not imply human `REVIEWED` status.
