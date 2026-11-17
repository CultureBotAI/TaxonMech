# YAML Record Review: Bacillus sp. MAYA

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_maya.yaml`
- Started UTC: 2026-10-08T04:26:24Z
- Finished UTC: 2026-10-08T04:31:35Z
- Verdict: pass

## Target

One generated `TaxonRecord`: `NCBITaxon:1036310`, Bacillus sp. MAYA, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:185979` (unclassified Bacillus (in: firmicutes)), genetic code 11, grounding `EXACT`, mapping status `SEEDED`. All 53 YAML lines were read before judgement.

`data/taxa/PATHS.tsv:14822` and `curation/seed_scope.tsv:322562` resolve this exact target. The scope row was added on 2026-09-13 under the one-source NCBI attestation rule. The file represents the NCBI taxon bearing the MAYA isolate designation, not an arbitrary Bacillus strain, a formally named species inferred from sequence similarity, or a culture deposit. There are no synonyms, nomenclature, taxonomy mappings, strain blocks, genome links, experimental evidence, or causal graphs in the record.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/bacillus_sp_maya.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/bacillus_sp_maya.yaml --out /private/tmp/bmaya-strict.tsv` | Pass; one file, zero errors; TSV read and contains only its header. |
| Structured pinned-source comparison | Identity, rank, parent, genetic code, all ten ancestors, empty synonym columns, source attestation, scope/index membership, and seed explanation agree. |
| Exact identifier status | No target row in pinned type-material, merged-ID, or dropped-ID inventories; the backbone does not mark this node retired. |
| Ignored-inclusive source checks | All three matching rows/objects read completely. Five source-metadata JSON files and history filenames separately checked. |
| Current authority and primary evidence | NCBI Taxonomy XML, Datasets taxonomy, exact sequence/assembly queries, full marker source/reference metadata, and the journal-hosted primary-paper abstract inspected. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. Bounded source comparisons are diagnostics, not proof of corpus reproduction. No documented focused reference validator applies to this record. `just validate-products` is not applicable to the graph-free YAML. Ignored-inclusive content and filename searches found no target-specific separate history artifact; the embedded seed event was checked directly. No history entry or status promotion was made.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222315` agrees with current NCBI Taxonomy XML on identifier 1036310, scientific name, species rank, parent 185979, bacterial division, and genetic code 11. Datasets independently supplies the same identifier, label, rank, and root-inclusive ancestry. NCBI's species rank is preserved even though the label contains an isolate designation; no formal binomial or strain-rank assertion was invented. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036310&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036310).

All ten ancestors match the pinned parent chain: root; cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Caryophanales; Bacillaceae; Bacillus; unclassified Bacillus (in: firmicutes). The final parent correctly retains `NO_RANK`. The full backbone scan found no immediate children.

The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31859` agrees with this taxon and label and has an empty unique-name field. All three backbone synonym columns are empty, and current Taxonomy XML supplies no other names. `EXACT` grounding is supported for this NCBI node, not for a similar Bacillus sequence or species.

## Evidence

**Attestation and seed history.** The sole attestation names `NCBITAXON`, the exact identifier and label, count 1, unit `NAME`, and the 2026-09-13 snapshot. The full backbone and native name object support it. A name assertion is not a strain-deposit or experimental count. The scope reason and seed explanation agree, including the embedded timestamp `2026-09-13T17:54:04Z`; neither implies human `REVIEWED` status.

**Primary sequence context.** The exact Nuccore query `txid1036310[Organism:noexp]` returned one record, UID 334302960. Its complete top-level, source-feature, and reference metadata identifies `JF799093.1`, a 936-bp partial 16S rRNA sequence. The source block explicitly names Bacillus sp. MAYA, strain MAYA, taxon 1036310, ocean water, and South Africa: Algoa Bay, Eastern Cape Province. It supplies no culture-deposit accession or genome assembly. The sole reference is a direct submission dated 10 April 2011 by Okoh, Olaniran, Cosa, and Mabinya; the sequence was created and last updated on 5 June 2011. Sequence bases and non-source feature annotations were not evaluated. [JF799093.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799093.1).

**Primary publication context.** The journal-hosted abstract for Ugbenyen and Okoh's 2013 bioflocculant paper, Chemical and Biochemical Engineering Quarterly 27(4):511-518, explicitly identifies Bacillus sp. MAYA with accession JF799093. That accession connects the study to the nucleotide record and reviewed taxon without a name-only join. Its reported sequence similarity to Bacillus sp. A-5A does not make the isolates equivalent. Only the abstract and bibliographic metadata were inspected directly; the full PDF could not be retrieved, and assay details and sample-context reconciliation were not audited. No experimental performance or genus-wide phenotype was imported into the review verdict. [Primary article and abstract](https://hrcak.srce.hr/clanak/165841).

Searches also led to a later mixed-culture publication, but its publisher page was inaccessible and it was not used as verified evidence. Consortium-level results would require their own scope assessment before any attribution to MAYA. The sequence submission does not cite the 2013 article; these remain distinct bibliographic observations.

The YAML asserts no bioflocculation performance, habitat, growth condition, gene function, or mechanism. Literature existence is therefore not evidence of a missing required trait or causal graph. iModulonDB is not applicable because no gene, locus, regulator, expression-module, or functional claim is present. Search snippets and secondary pages were leads only.

## Completeness

No consequential gap was established under the current source-owned model. Exact target scans found no rows in the seven raw BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin, or BactoTraits inventories. With no descendants or eligible BacDive entries found, `strain_count: 0` agrees with the pinned inventory. It does not deny that the MAYA isolate exists or was studied. A bare isolate designation is not a registered culture accession, and a partial ribosomal marker is not a genome assembly.

Identifier, label, and slug resolution included ignored files under `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`; it resolved one target and found no prior target review or separate history artifact. Source searches used `rg --no-ignore --hidden -z` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. All three candidates, comprising backbone, scope, and native scientific name, were fully read. Expanded searches for JF799093 and Bacillus MAYA naming variants found only those same three rows. A separate search for JF799093 and the later-publication DOI lead found zero matches in those roots. All five `SOURCE.json` files and history filenames were separately checked without ignoring files.

The exact-taxonomy Assembly query returned zero entries with a phrase-not-found warning. This is a bounded result, not proof that no assembly exists elsewhere. The local scans establish pinned-source coverage, not exhaustive online absence. Optional synonyms, nomenclature, mappings, genome links, literature evidence, discussions, and graphs may correctly remain empty under the documented model.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the record's identity, lineage, genetic code, empty synonym fields, strain count, attestation, or seed-history assertions. The marker and primary abstract supply isolate context without establishing a required missing culture or genome relationship. Inaccessible optional literature does not invalidate the independently verified YAML identity claims.

## Recommended Edits

None required for this generated record. Do not substitute a similar sequence's organism, treat a marker as an assembly, or add phenotype claims without authorized evidence-backed curation.

Future taxonomy corrections belong upstream at NCBI and in the pinned ingestion governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Supported enrichment or emission changes belong in the responsible maintained adapter and `src/taxonmech/seed.py`, with focused tests; scope decisions belong in `curation/seed_scope.tsv`. Generated YAML, catalogs, and pages are not independent correction surfaces.

## Follow-up Checks

- Before optional literature enrichment, retrieve and inspect the full primary paper, reconcile any sample-context differences with the sequence submission, and distinguish single-isolate from consortium experiments. Verify any proposed culture or genome identifier directly.
- After an authorized source refresh, compare exact taxon 1036310, all ten ancestors, genetic code, names, lifecycle rows, and eligible strain evidence before a one-record seed canary.
- Rerun schema and strict validation after authorized regeneration, then corpus, provenance, rendering, documentation, and QC gates before publication. Validate separate append-only history only if later curation creates an event.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report SHA-256: `6e416a4bf3cc68befe794bdabd636e6b630f556f5095048926937e440f1f7e75`. Only this new report was written for the target. No YAML, source, scope, lifecycle, history, generated page, prior report, GitHub item, or worktree was modified. Eukaryota was neither re-reviewed nor edited. No paid research, outreach, source refresh, independent sequence analysis, or experimental replication was performed. The verdict does not confer human `REVIEWED` status.

The primary PDF at `https://hrcak.srce.hr/file/165841` returned HTTP 418 through direct retrieval; an alternate publisher PDF route also failed. The journal's HTML abstract was successfully opened. The later-publication search lead `10.2166/washdev.2014.181` was not independently resolved: the IWA page returned HTTP 403 and DOI opening failed. Its search-index excerpt is not treated as inspected primary text, and it is not a citation asserted by the YAML. No PDF rendering or full-paper review is claimed.
