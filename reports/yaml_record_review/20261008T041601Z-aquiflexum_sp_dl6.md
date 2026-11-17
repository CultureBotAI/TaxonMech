# YAML Record Review: Aquiflexum sp. DL6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/aquiflexum_sp_dl6.yaml`
- Started UTC: 2026-10-08T04:13:13Z
- Finished UTC: 2026-10-08T04:16:01Z
- Verdict: pass

## Target

One generated `TaxonRecord`: `NCBITaxon:1036307`, Aquiflexum sp. DL6, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2644351` (unclassified Aquiflexum), genetic code 11, grounding `EXACT`, mapping status `SEEDED`. All 59 YAML lines were read before judgement.

`data/taxa/PATHS.tsv:14820` and `curation/seed_scope.tsv:322560` resolve the exact record. The scope row was added on 2026-09-13 under the one-source NCBI attestation rule. This is the NCBI taxon bearing the DL6 isolate designation, not an arbitrary Aquiflexum species or a deposited microbial culture. The record has no synonyms, nomenclature, mappings, strain blocks, genome links, experimental evidence, or causal graph.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/aquiflexum_sp_dl6.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/aquiflexum_sp_dl6.yaml --out /private/tmp/adl6-strict.tsv` | Pass; one file, zero errors; the TSV was read and contains only its header. |
| Structured pinned-source comparison | Identity, rank, parent, genetic code, all twelve ancestors, empty synonym columns, attestation, scope/index membership, and seed explanation agree. |
| Exact identifier status | No target row in the pinned type-material, merged-ID, or dropped-ID inventories; the backbone does not mark the node retired. |
| Ignored-inclusive source checks | All three candidate rows/objects read completely. Five source-metadata JSON files and history filenames were separately checked. |
| Current authority and publication checks | NCBI Taxonomy XML, Datasets taxonomy, exact sequence/assembly queries, full marker source/reference metadata, and primary publication abstracts/metadata inspected. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. The bounded comparisons are diagnostics, not substitutes for corpus reproduction. There is no documented focused reference validator for this record. `just validate-products` is not applicable to this graph-free record. Ignored-inclusive content and filename searches found no target-specific separate history artifact; the embedded seed event was checked directly. No history entry or review-status promotion was made.

## Identity and Grounding

The full backbone row `data/raw/ncbitaxon_taxa.tsv:222313` agrees with live NCBI Taxonomy XML on taxon 1036307, label, species rank, parent 2644351, bacterial division, and genetic code 11. Datasets independently supplies the same identifier, name, rank, and root-inclusive ancestry. Species rank is NCBI's rank for this node; a strain designation in its name is not grounds for inventing a different rank or a formal species epithet. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036307&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036307).

All twelve ancestors match the pinned parent chain: root; cellular organisms; Bacteria; Pseudomonadati; FCB group; Bacteroidota/Chlorobiota group; Bacteroidota; Cytophagia; Cytophagales; Cyclobacteriaceae; Aquiflexum; unclassified Aquiflexum. Both intermediate clades and the unranked direct parent are preserved correctly. The full backbone scan found no immediate children.

The complete native object at `data/catalog/ncbi_names-0005.jsonl.gz:31857` identifies the same scientific name and taxon, with an empty unique-name field. All three backbone synonym columns are empty, and live Taxonomy XML supplies no other names. `EXACT` grounding to this NCBI node is supported; it is not an exact mapping to some named neighboring species.

## Evidence

**Attestation and history.** The sole attestation correctly records `NCBITAXON`, the exact identifier and label, count 1, unit `NAME`, and the 2026-09-13 snapshot. The full backbone and native scientific-name object support it. This counts a taxonomic name, not a strain deposit or enzyme assay. The scope reason and embedded seed explanation agree; the seed timestamp is `2026-09-13T17:54:04Z`. Neither the seed event nor this report implies human promotion to `REVIEWED`.

**Primary sequence context.** The exact Nuccore query `txid1036307[Organism:noexp]` returned one record, UID 334192418. Its complete top-level, source-feature, and reference metadata identifies `JF812063.1`, a 1,390-bp partial 16S rRNA sequence. The source block explicitly states strain DL6, taxon 1036307, deep sediment, India: Lonar Lake, and collection on 19 October 2008. The reference is a direct submission by Lingojwar and colleagues dated 16 April 2011. These fields support the exact isolate-associated identity; the source block does not name a registered culture deposit or genome assembly. Sequence bases and non-source feature annotations were not evaluated. [JF812063.1](https://www.ncbi.nlm.nih.gov/nuccore/JF812063.1).

**Primary literature context.** Two enzyme-study titles explicitly name Aquiflexum sp. DL6. They are useful evidence that the isolate was studied, not grounds for importing an unasserted functional graph or claiming a genome relationship:

- Misal, Lingojwar, and Gawai's azoreductase study is DOI `10.1007/s10930-013-9522-1`, PMID `24186471`. The publisher's abstract explicitly describes isolation and 16S identification of DL6 and purification of an NAD(P)H-dependent azoreductase. Publisher metadata and the PubMed abstract were inspected; full subscription text was not. [Azoreductase study](https://link.springer.com/article/10.1007/s10930-013-9522-1), [PubMed record](https://pubmed.ncbi.nlm.nih.gov/24186471/).
- The publisher's nitroreductase article is DOI `10.1134/S0003683813030125`, Applied Biochemistry and Microbiology 49:227-232 (2013). Its inspected abstract names DL6 and reports enzyme purification after nitro-aromatic acclimatization. PMID `23882943` is indexed under Prikladnaia biokhimiia i mikrobiologiia and reports a different DOI, `10.7868/s0555109913030124`. These distinct bibliographic identifiers were retained as source metadata rather than silently collapsed. The latter DOI was read from PubMed, not independently resolved; neither complete paper was inspected. [Publisher nitroreductase article](https://link.springer.com/article/10.1134/S0003683813030125), [PubMed entry](https://pubmed.ncbi.nlm.nih.gov/23882943/).

The YAML asserts no enzyme activity, substrate specificity, habitat, assay condition, or causal mechanism, so the existence of these studies does not establish an unsupported claim or a missing required field. Search snippets and secondary reviews were used only as leads. No phenotype was generalized to the genus or substituted for direct identity evidence. iModulonDB is not applicable because the reviewed YAML has no gene, locus, regulator, expression-module, or mechanistic claim.

## Completeness

No consequential gap was established under the current source-owned model. Exact target scans found no rows in the seven raw BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin, or BactoTraits inventories. With no descendants or eligible BacDive entries found, `strain_count: 0` is correct as a source inventory count. It does not deny the existence of the biological isolate studied in the papers. DL6 alone is a strain designation, not a registered culture-deposit accession; a ribosomal marker is not a genome assembly.

Identifier, label, and slug resolution included ignored files under `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`; it resolved one target and found no prior target review or separate history artifact. Source searches used `rg --no-ignore --hidden -z` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. All three matching rows/objects, comprising backbone, scope, and native scientific name, were fully read. Expanded searches for JF812063, both PMIDs, and the two publisher DOIs found no further rows within those roots. All five `SOURCE.json` files and history filenames were separately checked without ignoring files.

The live exact-taxonomy Assembly query returned zero entries with a phrase-not-found warning. That is a bounded query result, not proof that no assembly exists anywhere. These local checks establish pinned-source coverage, not exhaustive online absence. Optional synonyms, nomenclature, mappings, genome links, literature evidence, discussions, and causal graphs may correctly remain empty under the documented model.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current identity, lineage, genetic code, empty synonym fields, source count, attestation, or seed-history assertions. The marker and enzyme studies do not demonstrate a missing required genome or culture representation. Bibliographic differences in external sources do not affect any citation asserted by this YAML.

## Recommended Edits

None required for the generated record. Do not change its rank from the isolate wording, invent a culture accession, or add enzyme/habitat claims without an authorized evidence-backed curation workflow.

Future taxonomy corrections belong upstream at NCBI and in the pinned ingestion governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Supported enrichment or emission changes belong in the responsible maintained adapter and `src/taxonmech/seed.py`, with focused tests; scope decisions belong in `curation/seed_scope.tsv`. Generated YAML, catalogs, and pages are not independent correction surfaces.

## Follow-up Checks

- Before optional literature enrichment, read the complete primary papers and reconcile citation versions. Preserve assay-specific scope and verify any proposed culture or genome identifier directly.
- After an authorized source refresh, compare exact taxon 1036307, all twelve ancestors, genetic code, names, lifecycle rows, and eligible strain evidence before a one-record seed canary.
- Rerun schema and strict validation after authorized regeneration, then corpus, provenance, rendering, documentation, and QC gates before publication. Validate separate append-only history only if later curation creates an event.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report SHA-256: `1936f02deecdac49ac603d208375eae1d50fe2bac860d6e0c17e63ff119b6167`. Only this new report was written for the target. No YAML, source, scope, lifecycle, history, generated page, prior report, GitHub item, or worktree was modified. Eukaryota was neither re-reviewed nor edited. No paid research, outreach, source refresh, independent sequence analysis, or experimental replication was performed. The verdict does not confer human `REVIEWED` status.
