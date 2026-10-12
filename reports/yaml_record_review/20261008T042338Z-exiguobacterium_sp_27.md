# YAML Record Review: Exiguobacterium sp. 27

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/exiguobacterium_sp_27.yaml`
- Started UTC: 2026-10-08T04:17:25Z
- Finished UTC: 2026-10-08T04:23:38Z
- Verdict: pass

## Target

One generated `TaxonRecord`: `NCBITaxon:1036308`, Exiguobacterium sp. 27, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2644629` (unclassified Exiguobacterium), genetic code 11, grounding `EXACT`, mapping status `SEEDED`. All 57 YAML lines were read before judgement.

`data/taxa/PATHS.tsv:14821` and `curation/seed_scope.tsv:322561` resolve this exact record. The scope row was added on 2026-09-13 under the one-source NCBI attestation rule. This is the NCBI taxon with isolate designation 27, not any strain with that number or a formally named Exiguobacterium species. The YAML has no synonyms, nomenclature, mappings, strain blocks, genome links, experimental evidence, or causal graph.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/exiguobacterium_sp_27.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/exiguobacterium_sp_27.yaml --out /private/tmp/ex27-strict.tsv` | Pass; one file, zero errors; output TSV read and contains only its header. |
| Structured pinned-source comparison | Identity, parent, rank, genetic code, all eleven ancestors, empty synonym columns, attestation, scope/index membership, and seed explanation agree. |
| Exact identifier status | No target row in the pinned type-material, merged-ID, or dropped-ID inventories; the backbone does not mark the node retired. |
| Ignored-inclusive source checks | All three matching rows/objects read completely; five source-metadata JSON files and history filenames separately checked. |
| Current authority and primary evidence | NCBI Taxonomy XML, Datasets taxonomy, exact sequence/assembly queries, full marker source/reference metadata, and relevant primary-paper passages inspected. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. The bounded comparisons are diagnostics, not substitutes for corpus reproduction. There is no documented focused reference validator for this record. `just validate-products` is not applicable to this graph-free record. Ignored-inclusive content and filename searches found no target-specific separate history artifact; the embedded seed event was checked directly. No history entry or review-status promotion was made.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222314` agrees with live NCBI Taxonomy XML on identifier 1036308, scientific name, species rank, parent 2644629, bacterial division, and genetic code 11. Datasets supplies the same identifier, name, rank, and root-inclusive ancestry. Species rank is the authority's rank for this isolate-associated node; the label does not justify substituting a new formal species name or a different rank. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036308&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036308).

All eleven ancestors match the pinned parent chain: root; cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Caryophanales; Caryophanales incertae sedis; Caryophanales Family XII. Incertae Sedis; Exiguobacterium; unclassified Exiguobacterium. Both incertae-sedis nodes correctly retain `NO_RANK`. The word Family in a source label does not establish a formal family rank. The full backbone scan found no immediate children.

The native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31858` was read completely and agrees with the exact taxon and label; its unique-name field is empty. All three backbone synonym columns are empty, and current Taxonomy XML supplies no other names. Grounding is exact to this NCBI node, not to a neighboring named species.

## Evidence

**Attestation and history.** The sole attestation correctly records `NCBITAXON`, the exact identifier and label, count 1, unit `NAME`, and the 2026-09-13 snapshot. The complete backbone and native name object support that taxonomic-name assertion. It is not an experimental or culture-deposit count. The scope reason and embedded seed explanation agree, including seed timestamp `2026-09-13T17:54:04Z`; neither implies a human `REVIEWED` status.

**Primary sequence context.** The exact Nuccore query `txid1036308[Organism:noexp]` returned one record, UID 334725195. Its complete top-level, source-feature, and reference metadata identifies `JF909557.1`, a 621-bp partial 16S rRNA sequence. Its source block explicitly names Exiguobacterium sp. 27, strain 27, taxon 1036308, Mariout lake water behind ANRPC petroleum company, and Egypt: Alexandria. The source block names no culture-deposit accession or genome assembly. Sequence bases and non-source feature annotations were not evaluated. [JF909557.1](https://www.ncbi.nlm.nih.gov/nuccore/JF909557.1).

The sequence's references list an unpublished heavy-metal-removal manuscript and a direct submission by Saad, Ghozlan, and Sabry dated 19 April 2011. These references were preserved as submitted metadata, not silently replaced with a later paper having different bibliographic details. The nucleotide record's creation and update dates are 8 June 2011. [Sequence metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF909557.1).

**Primary publication context.** Amer, Hassan, Ghozlan, and Sabry's 2013 nickel-biosorption study names Exiguobacterium sp. 27 in its title (Life Science Journal 10(4):1338-1347). Its methods on page 1340 explicitly associate isolate H27 with accession JF909557; the identification results on page 1342 repeat that accession. Together with the nucleotide source taxon, this supports an accession-based connection between H27 and the reviewed node. JX625999 belongs to the compared isolate EdyKol Es20, not H27. The abstract, relevant methods, and identification passages were read, and pages 1338, 1340, and 1342 were visually inspected. The full ten-page paper and assay reproducibility were not audited. The article does not supply a verified culture-deposit or genome link for this review. Its experimental observations were not imported as taxon-wide traits or evidence of a formal new species name. [Primary paper](https://www.lifesciencesite.com/lsj/life1004/177_21413life1004_1338_1347.pdf).

The YAML asserts no nickel-biosorption performance, metal tolerance, habitat, assay condition, gene function, or causal mechanism. Optional literature context therefore does not reveal an unsupported YAML claim or a missing required mechanism representation. iModulonDB is not applicable to this identity-only record: no gene, locus, regulator, transcriptomic module, or functional assertion requires that adapter. Other search hits were leads, not inspected evidence.

## Completeness

No consequential gap was established under the current source-owned model. Exact target scans found no rows in the seven raw BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin, or BactoTraits inventories. With no descendants or eligible BacDive entries found, `strain_count: 0` agrees with the pinned source inventory. It does not deny that isolate 27 was studied. Neither 27 nor the paper's H27 designation alone is a registered culture accession, and a partial ribosomal marker is not a genome assembly. A publication-local designation need not be invented as an NCBI synonym.

Identifier, label, and slug resolution included ignored files under `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`; it found one target and no prior target report or separate history artifact. Source searches used `rg --no-ignore --hidden -z` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. All three candidates, comprising backbone, scope, and native scientific name, were fully read. Expanded searches for JF909557 and Exiguobacterium H27 naming variants returned no further matches in those roots. All five `SOURCE.json` files and history filenames were separately checked without ignoring files.

The live exact-taxonomy Assembly query returned zero entries with a phrase-not-found warning. This is a bounded result, not proof that no assembly exists elsewhere. Local searches establish pinned-source coverage, not exhaustive online absence. Optional synonyms, nomenclature, mappings, genome links, literature evidence, discussions, and graphs may remain empty under the documented model.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current identity, lineage, genetic code, empty synonym fields, source count, attestation, or seed-history assertions. The marker and inspected paper passages establish isolate context without demonstrating a missing required genome, culture, or functional representation.

## Recommended Edits

None required for the generated record. Do not infer a formal family rank from an ancestor label, turn a marker into a genome link, or add assay claims without an authorized evidence-backed curation workflow.

Future taxonomy corrections belong upstream at NCBI and in the pinned ingestion governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Supported enrichment or emission changes belong in the responsible maintained adapter and `src/taxonmech/seed.py`, with focused tests; scope decisions belong in `curation/seed_scope.tsv`. Generated YAML, catalogs, and pages are not independent correction surfaces.

## Follow-up Checks

- Before optional literature enrichment, inspect the complete paper and assay-specific conditions; retain the JF909557 identity link and do not transfer the comparator's accession. Verify any proposed culture or genome identifier directly.
- After an authorized source refresh, compare exact taxon 1036308, all eleven ancestors, genetic code, names, lifecycle rows, and eligible strain evidence before a one-record seed canary.
- Rerun schema and strict validation after authorized regeneration, then corpus, provenance, rendering, documentation, and QC gates before publication. Validate separate append-only history only if later curation creates an event.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report SHA-256: `def9317f8c866c0ea47cfa9d3ab653bb24a60018940a98cf65bdf1d0af04e555`. Only this new report was written for the target. No YAML, source, scope, lifecycle, history, generated page, prior report, GitHub item, or worktree was modified. Eukaryota was neither re-reviewed nor edited. No paid research, outreach, source refresh, independent sequence analysis, or experimental replication was performed. The verdict does not confer human `REVIEWED` status.

PDF retrieval initially encountered a web-tool parsing error, but the primary PDF was subsequently retrieved successfully. Poppler and common Python PDF libraries were unavailable locally; installed macOS PDFKit rendered the three inspected pages into temporary PNGs. The temporary PDF and images are reading aids outside the repository, not generated repository products or new dependencies.
