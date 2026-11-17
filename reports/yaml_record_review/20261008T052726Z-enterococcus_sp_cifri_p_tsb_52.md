# YAML Record Review: Enterococcus sp. CIFRI P-TSB-52

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterococcus_sp_cifri_p_tsb_52.yaml`
- Started UTC: 2026-10-08T05:23:55Z
- Finished UTC: 2026-10-08T05:27:26Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1036318`, Enterococcus sp. CIFRI P-TSB-52. All 54 YAML lines were read before judgement. It is a bacterial `SPECIES` node under `NCBITaxon:2608891` (unclassified Enterococcus), genetic code 11, grounding `EXACT`, mapping status `SEEDED`, with zero listed strains and one NCBI name attestation.

The target resolves at `data/taxa/PATHS.tsv:14830` and `curation/seed_scope.tsv:322570`. No synonyms, nomenclature, taxonomy mappings, genome links, record-level literature assertions, discussions, or causal graphs are present. The designation identifies this source node, not a registered collection accession or a formal species assignment.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/enterococcus_sp_cifri_p_tsb_52.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/enterococcus_sp_cifri_p_tsb_52.yaml --out /private/tmp/ep52-strict.tsv` | Pass; one file, zero errors; TSV read and contains only its header. |
| Structured source comparison | Identity, rank, parent, genetic code, all ten ancestors, empty synonym columns, attestation, scope/index membership, and seed explanation agree. |
| Identifier status | No target rows in pinned type-material, merged-ID, or dropped-ID inventories; backbone retirement field empty. |
| Ignored-inclusive source checks | All three matching rows/objects read completely; five source-metadata JSON files parsed and history filenames checked. |
| Current authority and literature | NCBI Taxonomy XML, Datasets taxonomy, exact sequence/assembly queries, marker source/reference metadata, and accession-linked primary publication passages inspected. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. Bounded source comparisons do not prove corpus reproduction. No documented focused reference validator applies. `just validate-products` is inapplicable to this graph-free record. Ignored-inclusive content and filename searches found no target-specific separate history artifact; the embedded seed event was checked directly. No history or review-status mutation was made.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222323` agrees with live NCBI Taxonomy XML on identifier 1036318, exact label, species rank, parent 2608891, bacterial division, and genetic code 11. Datasets confirms the same taxon, name, rank, and root-inclusive ancestry. Taxonomy XML supplies no other names. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036318&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036318).

The ten source ancestors are root; cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Enterococcaceae; Enterococcus; unclassified Enterococcus. Every identifier, label, rank, and position agrees with the pinned chain and current authority. The direct parent correctly retains `NO_RANK`. The full backbone scan found no immediate children.

The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31867` agrees and has an empty unique-name field. All three backbone synonym columns are empty. `EXACT` grounds the record to this NCBI node; it does not assert a more resolved species classification. Literature identifications must not silently replace the carried NCBI lineage.

## Evidence

**Attestation and seed history.** The sole attestation correctly names `NCBITAXON`, the exact target identifier and label, count 1, unit `NAME`, and the 2026-09-13 snapshot. It is not a culture, genome, or experiment count. The scope date/reason and embedded seed explanation agree, including timestamp `2026-09-13T17:54:04Z`. An external review does not promote `SEEDED` to human `REVIEWED` status.

**Primary sequence.** Exact Nuccore query `txid1036318[Organism:noexp]` returned UID 334303332. Complete top-level, source-feature, and reference metadata identifies `JF799894.1`, a 1,442-bp partial 16S rRNA sequence, organism Enterococcus sp. CIFRI P-TSB-52, strain CIFRI P-TSB-52, and taxon 1036318. Its isolation source is marine water and its location is supplied as `India: W.B.`. The source feature supplies no culture-deposit or assembly accession. Its references comprise an unpublished salt-tolerant-bacteria study and an 11 April 2011 direct submission by Behera, Sharma, Das, Chanda, and Patra. Creation and update dates are both 5 June 2011. Sequence bases and non-source feature annotations were not audited. [JF799894.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799894.1).

**Accession-linked publication.** The Behera primary text pairs P-TSB-52 with JF799894 and Enterococcus casseliflavus in Table 2; Table 1 gives Puri water. The exact accession supports the study link, not automatic species reassignment. The supplied locality descriptions are retained separately rather than silently reconciled. [Primary text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis). Publisher metadata confirms DOI `10.1007/s40011-014-0440-6`, online publication in 2014 and volume 85, pages 957-964 (2015). [Publisher](https://link.springer.com/article/10.1007/s40011-014-0440-6).

The YAML makes no isolation-locality, medium, salt-tolerance, resistance, gene-function, or mechanism claim. Optional study context was not converted into required missing fields or transferred between CIFRI isolates. No exact synonym, deposit, or genome relationship follows from a nearest-strain identification. iModulonDB is not applicable because no gene, locus, regulator, expression-module, or functional assertion is present. Search snippets and unrelated results were not used as evidence.

## Completeness

No consequential source-owned gap was established. Exact target scans found no entries in the seven raw BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin, or BactoTraits inventories. With no descendants or eligible BacDive entries found, `strain_count: 0` agrees with the pinned inventory. This does not deny the sequenced isolate's existence. A laboratory designation is not a registered culture deposit, and a partial marker is not a genome assembly.

Identifier, label, and slug resolution included ignored files under `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`, resolving one record with no prior target report. Source scans used `rg --no-ignore --hidden -z` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. All three candidates, backbone, scope, and native name, were fully read. Expanded searches for JF799894, the publication DOI, and CIFRI P-TSB-52/P-TSB-52 designation variants returned only the same three target-name rows. Five `SOURCE.json` files and history filenames were separately checked without ignoring files.

The live exact-taxonomy Assembly query returned zero results with a phrase-not-found warning. This is a bounded result, not proof that no assembly exists elsewhere. Optional nomenclature, synonyms, mappings, genomes, literature, and graphs can remain empty under the present model.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the record's asserted identity, lineage, genetic code, empty synonyms, strain count, attestation, or seed history. No required missing strain/genome relationship was established. External classification and locality details are preserved in Evidence without treating them as facts asserted by this YAML or automatically reconciling them into the record.

## Recommended Edits

None required for the generated record. Do not rename it from a marker-based identification, infer a collection accession, attach a genome through a shared CIFRI prefix, or import other isolates' phenotypes.

Any accepted taxonomy correction belongs upstream at NCBI and then in pinned ingestion through `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Supported enrichment or emission changes belong in the maintained adapter and `src/taxonmech/seed.py`, with focused tests; scope decisions belong in `curation/seed_scope.tsv`. Generated YAML, catalogs, and pages are not independent correction surfaces.

## Follow-up Checks

- Before optional enrichment, verify exact isolate/deposit links and reconcile source locality metadata. Inspect original table layouts and assay evidence before adding quantitative phenotypes; none was validated here.
- Following an authorized source refresh, recheck taxon 1036318, all ten ancestors, names, lifecycle status, and eligible strain evidence before a one-record seed canary.
- Rerun schema and strict validation after authorized regeneration, then corpus, provenance, rendering, documentation, and QC gates before publication. Validate separate append-only history if later curation creates an event.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report SHA-256: `9de4b6f5909b31d6380fcc1bd75ed996add17335b51c0ba433e999e18813253e`. Only this new report was written for the target. No YAML, source, scope, lifecycle, history, generated page, prior report, GitHub item, or worktree was changed. Eukaryota was not re-reviewed or edited. No paid research, outreach, source refresh, independent sequence analysis, or experimental replication was performed.

Publisher metadata/abstract and relevant author-uploaded primary text were inspected. Subscription full-text access was not purchased. Garbled growth symbols in the transcription were not interpreted as numeric tolerance values, and no figure was visually inspected for this target. These bounded identity reads are not a full-paper, figure, or assay-reproducibility audit. The source-specific locality metadata would need clarification before any habitat enrichment, but the present YAML does not assert a location.
