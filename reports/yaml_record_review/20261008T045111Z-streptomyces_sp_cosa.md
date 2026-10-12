# YAML Record Review: Streptomyces sp. Cosa

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_cosa.yaml`
- Started UTC: 2026-10-08T04:47:08Z
- Finished UTC: 2026-10-08T04:51:11Z
- Verdict: pass

## Target

One generated `TaxonRecord`: `NCBITaxon:1036313`, Streptomyces sp. Cosa, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2593676` (unclassified Streptomyces), genetic code 11, grounding `EXACT`, mapping status `SEEDED`. All 54 YAML lines were read before judgement.

`data/taxa/PATHS.tsv:14825` and `curation/seed_scope.tsv:322565` resolve the exact target. Its scope row was added on 2026-09-13 under the one-source NCBI attestation rule. The record denotes the NCBI taxon bearing the Cosa isolate designation, not a similarly named organism, a publication author, a formally named Streptomyces species, or a culture deposit. There are no synonyms, nomenclature, mappings, strain blocks, genome links, experimental evidence, or causal graphs in this YAML.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/streptomyces_sp_cosa.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/streptomyces_sp_cosa.yaml --out /private/tmp/scosa-strict.tsv` | Pass; one file, zero errors; TSV read and contains only its header. |
| Structured pinned-source comparison | Identity, rank, parent, genetic code, all ten ancestors, empty synonym columns, attestation, scope/index membership, and seed explanation agree. |
| Exact identifier status | No target row in pinned type-material, merged-ID, or dropped-ID inventories; the backbone does not mark the node retired. |
| Ignored-inclusive source checks | All five matching rows/objects read completely, including two unrelated numerical hits. Five source-metadata JSON files and history filenames separately checked. |
| Current authority checks | NCBI Taxonomy XML, Datasets taxonomy, exact sequence/assembly queries, and complete marker top-level/source/reference metadata inspected. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. Bounded comparisons are diagnostics, not substitutes for corpus reproduction. There is no documented focused reference validator for this record. `just validate-products` is not applicable to the graph-free YAML. Ignored-inclusive content and filename searches found no target-specific separate history artifact; the embedded seed event was checked directly. No history entry or status promotion was made.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222318` agrees with current NCBI Taxonomy XML on identifier 1036313, scientific name, species rank, parent 2593676, bacterial division, and genetic code 11. Datasets independently supplies the same identifier, label, rank, and root-inclusive ancestry. NCBI's species rank is preserved for this isolate-associated node; the label does not justify a different rank or an invented formal species epithet. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036313&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036313).

All ten ancestors match the pinned parent chain: root; cellular organisms; Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales; Streptomycetaceae; Streptomyces; unclassified Streptomyces. In particular, the carried order is Kitasatosporales, as both pinned and current NCBI sources state. No alternate hierarchy was inferred. The direct parent correctly retains `NO_RANK`, and the full backbone scan found no immediate children.

The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31862` agrees with the exact identifier and label and has an empty unique-name field. All three backbone synonym columns are empty, and current Taxonomy XML supplies no other names. `EXACT` grounding is supported for this node, not for another Streptomyces isolate or a nearby sequence submission.

## Evidence

**Attestation and seed history.** The sole attestation names `NCBITAXON`, the exact identifier and label, count 1, unit `NAME`, and the 2026-09-13 snapshot. The complete backbone and native name object support it. A name assertion does not count biological isolates, culture deposits, genomes, or experiments. The scope reason and embedded seed explanation agree, including timestamp `2026-09-13T17:54:04Z`; neither implies human `REVIEWED` status.

**Primary sequence context.** The exact Nuccore query `txid1036313[Organism:noexp]` returned one record, UID 334302956. Its complete top-level, source-feature, and reference metadata identifies `JF799089.1`, an 863-bp partial 16S rRNA sequence. The source explicitly names Streptomyces sp. Cosa, strain Cosa, taxon 1036313, ocean water, and South Africa: Algoa Bay, Eastern Cape Province. It names no culture-deposit accession or genome assembly. The sole reference is a direct submission dated 10 April 2011 by Okoh, Olaniran, Cosa, and Mabinya; creation and last update are both 5 June 2011. The source provides a direct sequence-to-taxon identity link, not a functional assay or genome relationship. Sequence bases and non-source feature annotations were not evaluated. [JF799089.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799089.1).

**Literature boundary.** Bounded web searches for the exact taxon label, JF799089, and Streptomyces/Cosa/Algoa combinations did not establish an accession-linked primary publication. Results about other Streptomyces isolates, general marine-actinomycete surveys, or papers with an author named Cosa were not treated as evidence for this isolate. The sequence reference inspected here is a direct submission, not a journal citation. This is a limitation of the search, not proof that no relevant paper exists. No independent publication or full-paper review is claimed.

The YAML makes no bioflocculation, antimicrobial, habitat, growth-condition, gene-function, or mechanism assertion. Such properties were not inferred from the genus, submitter, geography, neighboring accession, or other reviewed records. iModulonDB is not applicable because no gene, locus, regulator, expression-module, or functional assertion is present. Search-index excerpts and secondary summaries were leads only.

## Completeness

No consequential gap was established under the current source-owned model. Exact target scans found no rows in the seven raw BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin, or BactoTraits inventories. With no descendants or eligible BacDive entries found, `strain_count: 0` agrees with the pinned inventory. It does not deny the existence of the isolate represented by the sequence. A bare strain designation is not a registered culture accession, and a partial ribosomal marker is not a genome assembly.

Identifier, label, and slug resolution included ignored files under `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`; it resolved one target and found no prior target review or separate history artifact. Source searches used `rg --no-ignore --hidden -z` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. All five candidates were fully read. Three are the target's backbone, scope, and native name rows. The other two are:

- `data/catalog/gtdb_genomes-0004.jsonl.gz:20949`: `GB_GCA_018655505.1`, Candidatus Peribacteria bacterium, NCBI taxon 2053688, isolate SI054_bin27. Its length fields equal 1036313.
- `data/catalog/ncbi_genbank-0017.jsonl.gz:4126`: the same assembly accession and unrelated taxon, again with genome-size fields equal to 1036313.

Those length matches are numerical coincidences, not Cosa genome links. Expanded searches for JF799089 and Streptomyces Cosa naming variants returned only the same three target-name rows within those ten roots. All five `SOURCE.json` files and history filenames were separately checked without ignoring files.

The live exact-taxonomy Assembly query returned zero entries with a phrase-not-found warning. That is a bounded query result, not proof that no assembly exists elsewhere. Local scans establish pinned-source coverage, not exhaustive online absence. Optional synonyms, nomenclature, mappings, genome links, literature evidence, discussions, and graphs may correctly remain empty under the documented model.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current identity, lineage, genetic code, empty synonym fields, strain count, source attestation, or seed-history assertions. The ribosomal marker and unrelated numerical assembly hits do not demonstrate a missing required culture or genome relationship. Failure to establish a primary paper is not a defect in this independently supported identity-only record.

## Recommended Edits

None required for the generated record. Do not treat genome-size matches as taxonomy matches, transfer properties from other Streptomyces studies, or substitute a formal species name without authority evidence.

Future taxonomy corrections belong upstream at NCBI and in the pinned ingestion governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Supported enrichment or emission changes belong in the responsible maintained adapter and `src/taxonmech/seed.py`, with focused tests; scope decisions belong in `curation/seed_scope.tsv`. Generated YAML, catalogs, and pages are not independent correction surfaces.

## Follow-up Checks

- Before optional literature enrichment, establish an explicit identifier connection to this isolate and inspect the complete primary source. Preserve sample, assay, and strain scope; verify any proposed culture or genome identifier directly.
- After an authorized source refresh, compare exact taxon 1036313, all ten ancestors, genetic code, names, lifecycle rows, and eligible strain evidence before a one-record seed canary.
- Rerun schema and strict validation after authorized regeneration, then corpus, provenance, rendering, documentation, and QC gates before publication. Validate separate append-only history only if later curation creates an event.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report SHA-256: `807027a66ea9f577ec5a423bbdd406c3c93d95187a00be15582616d708db6287`. Only this new report was written for the target. No YAML, source, scope, lifecycle, history, generated page, prior report, GitHub item, or worktree was modified. Eukaryota was neither re-reviewed nor edited. No paid research, outreach, source refresh, independent sequence analysis, experimental replication, or full-paper review was performed. The verdict does not confer human `REVIEWED` status.
