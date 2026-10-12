# YAML Record Review: Desert rose witches'-broom phytoplasma

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/desert_rose_witches_broom_phytoplasma.yaml`
- Started UTC: 2026-10-08T03:53:04Z
- Finished UTC: 2026-10-08T03:58:44Z
- Verdict: pass

## Target

One generated `TaxonRecord`: `NCBITaxon:1036299`, Desert rose witches'-broom phytoplasma, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:85621` (16SrII (Peanut WB group)), genetic code 11, grounding `EXACT`, mapping status `SEEDED`. All 54 YAML lines were read before judgement.

`data/taxa/PATHS.tsv:14817` and `curation/seed_scope.tsv:322557` resolve this record. The scope row was added on 2026-09-13 under the one-source NCBI attestation rule; the embedded seed event is dated `2026-09-13T17:54:04Z`. This is a bacterial taxonomic record, not the desert rose host plant, a disease entity, or a general record for every phytoplasma associated with that host.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/desert_rose_witches_broom_phytoplasma.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/desert_rose_witches_broom_phytoplasma.yaml --out /private/tmp/drwb-strict.tsv` | Pass; one file, zero errors; the output TSV contains only its header. |
| Structured pinned-source comparison | Identity, rank, parent, genetic code, all ten ancestors, source attestation, scope row, and embedded seed explanation agree. |
| Exact identifier status | No target row in the pinned type-material, merged-ID, or dropped-ID inventories. The backbone does not mark the target retired. |
| Ignored-inclusive source checks | All three candidate rows/objects read in full: backbone, scope, and native scientific-name object. Five source-metadata JSON files were separately parsed. |
| Live authority and publication checks | NCBI Taxonomy XML, NCBI Datasets taxonomy, exact-taxonomy sequence search, sequence source/reference metadata, and the primary publisher's abstract and article metadata inspected. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. The bounded diagnostics do not replace corpus reproduction. There is no documented focused reference validator for this record. `just validate-products` addresses curator-added causal-node labels and is not applicable to this graph-free record. No target-specific separate history artifact was found within the ignored-inclusive searches; the embedded seed event was checked directly. No history event or review-status promotion was made.

## Identity and Grounding

The complete backbone row `data/raw/ncbitaxon_taxa.tsv:222310` matches current NCBI Taxonomy XML on identifier 1036299, scientific name, species rank, parent 85621, bacterial division, and genetic code 11. NCBI Datasets independently returns the same identifier, name, species rank, and ancestry. The code is taken from this exact source record, not inferred from a generalization about Mollicutes. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036299&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036299).

The root-first lineage is root, cellular organisms, Bacteria, Bacillati, Mycoplasmatota, Mollicutes, Acholeplasmatales, Acholeplasmataceae, Candidatus Phytoplasma, and 16SrII (Peanut WB group). All ten identifiers, labels, ranks, and parent-chain relationships agree with the pinned backbone. Datasets includes root; the XML lineage begins with cellular organisms. The parent is a species group, while the target is the separately identified species-rank leaf. No immediate children were found in a full backbone scan.

The complete native name object at `data/catalog/ncbi_names-0005.jsonl.gz:31851` supplies exactly this scientific name for `NCBITaxon:1036299`, with an empty unique-name field. The backbone's synonym columns are empty, and the live XML does not provide other names. These checks support the narrow `EXACT` NCBI grounding without inventing an exact mapping to a different named phytoplasma.

## Evidence

**Source attestation and provenance.** The sole attestation is one `NAME` from `NCBITAXON`, carrying the exact identifier and label and the 2026-09-13 snapshot date. The backbone, native name object, scope reason, and seed explanation agree. This attests a taxonomic name, not a culture deposit, assembled genome, experimental phenotype, or disease mechanism. Exact-ID scans of the seven other raw source inventories found no target rows: BacDive, LPSN, GTDB mappings, GOLD, MediaDive, Madin, and BactoTraits.

**Sequence context.** An exact-taxonomy Nuccore search, `txid1036299[Organism:noexp]`, returned one record, UID 334291878. Its inspected metadata identifies `AB634851.1`, a 1,819-bp ribosomal-region sequence, with organism and taxon cross-reference matching 1036299. The source is a desert rose plant collected in Myanmar in March 2011. The source block does not name a culture deposit or genome assembly. Complete top-level, source-feature, and reference metadata were inspected; sequence bases and non-source feature annotations were not evaluated. This marker is not evidence for an assembly or an eligible BacDive strain. [NCBI sequence record](https://www.ncbi.nlm.nih.gov/nuccore/AB634851.1).

**Primary publication context.** The sequence bibliography identifies Win, Back, Kim, and Jung's disease note in Journal of General Plant Pathology 78:73-76 (2012). The publisher confirms DOI `10.1007/s10327-011-0348-4`, online publication on 8 November 2011, and the January 2012 issue. Its abstract describes symptomatic Adenium obesum in Myanmar and molecular placement with the peanut witches'-broom group and Candidatus Phytoplasma aurantifolia. This supports the bounded study context, but does not replace the current NCBI identifier or authorize an unqualified exact synonym. Only the abstract and publication metadata were read; subscription full text was not inspected. [Primary disease note](https://link.springer.com/article/10.1007/s10327-011-0348-4).

The YAML makes no publication-specific phenotype, host, location, sequence, or causal claim, so no citation or quoted-snippet mismatch was found. Optional literature enrichment is distinct from correcting a required field. The inspected study does not warrant changing this generated record's NCBI-owned identity.

## Completeness

No consequential gap was established under the current source-owned model. `strain_count: 0` and absent strain blocks agree with the eligible pinned inventory. Empty optional synonyms, nomenclature, mappings, cross-references, genome links, experimental evidence, discussion, and causal graphs are not errors merely because a marker sequence and disease note exist elsewhere. iModulonDB is not applicable because the YAML has no gene, regulator, transcriptomic, or causal claims.

Resolution searched identifier, label, and slug including ignored files under `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`; it resolved one target and found no prior target review or separate history artifact. Source searches used `rg --no-ignore --hidden -z` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Exactly three candidate rows/objects matched the target identity and were fully read. Expanded searches for `AB634851`, `334291878`, the publication DOI, and the bounded alias `DrWB` found no additional rows in those roots. All five `SOURCE.json` files were separately parsed, and history filenames were independently searched without ignoring files.

The live exact-taxonomy Assembly query returned zero records but also a phrase-not-found warning. That result is not treated as proof that no assembly exists anywhere. The local ignored-inclusive searches establish bounded pinned-source coverage, not exhaustive online absence or a claim that the organism has never been studied.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The identity, lineage, genetic code, single-source name attestation, zero eligible strains, and seeded history are supported within the inspected scope. The host-associated name and publication context were not promoted into unsupported genome, nomenclatural-equivalence, or mechanistic assertions.

## Recommended Edits

None required. Do not hand-edit generated YAML, relabel the record from the publication title, or append an unearned review event.

Any future taxonomy correction belongs in the maintained NCBI snapshot configuration and importer, including `conf/ncbi_taxdump.yaml`, with materialization owned by `src/taxonmech/seed.py`. Scope changes belong in `curation/seed_scope.tsv`; new source support belongs in the responsible source configuration and adapter, not a generated catalog, YAML, or page. No such correction is requested by this verdict.

## Follow-up Checks

- After an authorized source refresh, compare exact taxon 1036299, parent 85621, all ten ancestors, genetic code 11, native names, and identifier lifecycle before a one-record seed canary.
- Any future culture or genome enrichment must establish the exact source-owned identity and an eligible strain relationship; a host name or ribosomal marker alone is insufficient.
- Rerun schema and strict validation after authorized regeneration, followed by corpus, provenance, rendering, documentation, and QC gates before publication. Validate separate append-only history only if later curation creates an event.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report target SHA-256: `64c8329c2c6683f683a34c4184e2caf7a97204bb99b40ff7c3dd5109c2350bcc`. No YAML, source, scope, lifecycle, or history change was made. Existing reports and all seven worktrees were preserved. Eukaryota was neither re-reviewed nor edited. No paid research, outreach, GitHub mutation, or source refresh occurred.

The NCBI browser page was unavailable through the web tool; successful public Taxonomy XML and Datasets responses supplied the current identity checks. Publisher full text was not inspected. No independent sequence analysis, experimental replication, genome-quality assessment, or broad host-range inference was performed. The verdict does not confer human `REVIEWED` status.
