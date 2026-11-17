# YAML Record Review: Wolbachia endosymbiont of Myrmicinae sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_myrmicinae_sp.yaml`
- Started UTC: 2026-10-08T04:01:48Z
- Finished UTC: 2026-10-08T04:05:29Z
- Verdict: pass

## Target

One generated `TaxonRecord`: `NCBITaxon:1036300`, Wolbachia endosymbiont of Myrmicinae sp., rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), genetic code 11, grounding `EXACT`, mapping status `SEEDED`. All 67 YAML lines were read before judgement, including the three synonyms, sole source attestation, and seed event.

`data/taxa/PATHS.tsv:14818` and `curation/seed_scope.tsv:322558` resolve this exact record. The scope row was added on 2026-09-13 under the one-source NCBI attestation rule. The record denotes the bacterial taxonomic node, not its host, every Myrmicinae-associated Wolbachia, a microbial culture deposit, or one barcode specimen.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/wolbachia_endosymbiont_of_myrmicinae_sp.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_myrmicinae_sp.yaml --out /private/tmp/wmyr-strict.tsv` | Pass; one file, zero errors; the output TSV was read and contains only its header. |
| Structured pinned-source comparison | Identity, parent, rank, genetic code, all eleven ancestors, synonym scope, attestation, scope/index membership, and embedded seed explanation agree. |
| Exact identifier status | No target row in the pinned type-material, merged-ID, or dropped-ID inventories; the backbone does not mark the node retired. |
| Ignored-inclusive source checks | Twelve unique candidate rows/objects read in full, including the separate neighboring identities. All five source-metadata JSON files were separately parsed. |
| Live authority checks | NCBI Taxonomy XML and Datasets confirm the target and separately resolve 1035888. All three sequence records returned by the exact target query had their complete top-level, source-feature, and reference metadata inspected. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. These bounded diagnostics are not a substitute for corpus reproduction. There is no documented focused reference validator for this record. `just validate-products` is not applicable to this graph-free record. Ignored-inclusive content and filename searches found no target-specific separate history artifact; the embedded seed event was checked directly. No history entry or review-status promotion was made.

## Identity and Grounding

The full backbone row `data/raw/ncbitaxon_taxa.tsv:222311` agrees with current NCBI Taxonomy XML on taxon 1036300, its label, species rank, parent 2640676, bacterial division, genetic code 11, and all names. Datasets independently confirms the identifier, name, rank, and root-inclusive ancestry. Species rank is the source node's rank; it is not an assertion of a formally described bacterial species. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036300&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036300).

All eleven ancestors match the pinned parent chain: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria; Rickettsiales; Anaplasmataceae; Wolbachieae; Wolbachia; unclassified Wolbachia. The tribe and unranked direct parent are preserved. The full backbone scan found no immediate children.

The four complete native name objects at `data/catalog/ncbi_names-0005.jsonl.gz:31852` through row 31855 agree with both YAML and live XML:

| Native name class | Name | YAML representation |
| --- | --- | --- |
| scientific name | Wolbachia endosymbiont of Myrmicinae sp. | Main label |
| synonym | Wolbachia endosymbiont of Myrmicinae | `EXACT_SYNONYM`, source NCBITaxon |
| includes | Wolbachia sp. Myrmicinae_ACGAN331-09 | `RELATED_SYNONYM`, source NCBITaxon |
| includes | Wolbachia sp. Myrmicinae_ACGAN556-09 | `RELATED_SYNONYM`, source NCBITaxon |

`src/taxonmech/ncbi_taxdump.py:91` maps native synonym/equivalent-name classes to exact synonyms and other alternate-name classes to related synonyms; `src/taxonmech/seed.py:381` preserves those columns. Neither includes name is incorrectly promoted to exact equivalence or a cultured-strain entry.

## Evidence

**Attestation and history.** The sole attestation correctly carries `NCBITAXON`, the exact source identifier and label, count 1, unit `NAME`, and the 2026-09-13 snapshot. The seed explanation reproduces the scope reason. The embedded timestamp `2026-09-13T17:54:04Z` is the newest extraction time among the raw, ATB, and StrainInfo manifests, following `_seed_timestamp` in `src/taxonmech/seed.py:139`. This is source provenance, not a human review claim. The three alternate names do not become three additional biological strains or attestations.

**Explicit sequence context.** The current exact-taxonomy query `txid1036300[Organism:noexp]` returned three Nuccore records, and all three were inspected. Their source blocks explicitly name taxon 1036300 and Myrmicinae hosts. They are partial COI coding sequences, not genome assemblies.

| Accession | Length | Source voucher | Source BOLD reference |
| --- | --- | --- | --- |
| JN625824.1 | 578 bp | ACGAN331-09.w | ASWSB001-11.COI-5P |
| JN625825.1 | 658 bp | ACGAN556-09.w | ASWSB002-11.COI-5P |
| JF960138.1 | 409 bp | `BIOUG<CAN>:ACGAB271-09.w` | ASWAN001-10.COI-5P |

The first two connect the distinguishing ACGAN codes to source specimen vouchers, consistent with their related-name scope. All three source blocks describe Costa Rican collections; they supply no registered microbial culture deposit or assembled genome. BOLD identifiers above were inspected as GenBank cross-references, not independently through BOLD. Sequence bases, translations, and non-source feature annotations were not evaluated. [JN625824.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625824.1), [JN625825.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625825.1), [JF960138.1](https://www.ncbi.nlm.nih.gov/nuccore/JF960138.1).

**Distinct source nodes and unresolved correspondence.** The JF960138.1 voucher resembles the label of `NCBITaxon:1035888`, Wolbachia sp. ACGAB271-09.w. That node still resolves separately under the same parent in both live NCBI endpoints. Its full pinned backbone, scope, and native scientific-name rows were read; the target's synonyms do not include this label. The sequence's explicit taxon is 1036300. These facts support its sequence assignment here, but do not establish a taxonomic merger or prove distinct biological species. The external voucher/taxonomy correspondence remains unresolved and is not a demonstrated defect in this YAML. [Separate NCBI node 1035888](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035888).

The broader name search also found the separate node `NCBITaxon:1418527`, Wolbachia endosymbiont of Myrmicinae gen. 16 sp. MG07. Its full backbone, scope, and native scientific-name objects were inspected. Shared host wording does not make that node an alias of 1036300. Neither neighboring record was assigned a new review verdict here.

**Primary publication context.** The sequence bibliographies name Smith's barcoding study, retaining an unpublished status in their source metadata. The inspected publisher article is Smith et al. (2012), DOI `10.1371/journal.pone.0036514`. Its abstract and relevant methods/discussion distinguish Wolbachia COI from host barcodes; the methods explain that the `.w` suffix denotes a bacterial sample associated with a host BOLD process ID. This supports treating the codes as specimen context, not microbial culture accessions. No general reproductive effect, host-range claim, or allele-group assignment was transferred to this YAML. [Primary article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514).

The publisher's Table S2 supplies specimen/accession correspondence, but the web tool could not retrieve the XLS. A suitable local XLS reader was unavailable, and the full supplementary rows were not inspected. No conclusion here relies on uninspected table cells or search snippets. iModulonDB is not applicable because the YAML asserts identity and name provenance, not a gene, regulator, expression module, or mechanism.

## Completeness

No consequential gap was established under the current source-owned model. Exact target scans found no rows in the seven raw BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin, or BactoTraits inventories. With no descendants or eligible BacDive entries found, zero `strain_count` is a supported inventory count, not a claim that no specimens exist. The three barcode records do not require genome links or strain blocks. Optional nomenclature, mappings, cross-references, literature evidence, discussion, and causal graphs need not be invented.

Identifier, label, and slug resolution included ignored files under `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`. An existing report for 1035888 mentions this target, but is not a prior review of this record. Source searches used `rg --no-ignore --hidden -z` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. The initial search found nine candidate rows/objects; expansion through specimen codes, the three accessions, BOLD codes, and the DOI added three new candidates. All twelve were read fully. They consist of six TSV rows and six native name objects spanning the three distinct NCBI identities discussed above. No accession-specific local enrichment chain was found within those roots. Five `SOURCE.json` files and history filenames were separately checked without ignoring files.

The live exact-taxonomy Assembly search returned zero entries with a phrase-not-found warning. This is a bounded query result, not proof that no assembly exists anywhere. These searches and comparisons establish local pinned-source coverage, not exhaustive online absence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current identity, lineage, synonym scope, source count, attestation, or seed-history claims. The unresolved external voucher correspondence and supplementary-table access limit do not demonstrate a missing required representation. This pass does not authorize merging separately resolving taxa or certify their biological distinctness.

## Recommended Edits

None required for this generated record. Preserve the two related synonyms as related, not exact, and do not infer culture deposits from barcode vouchers.

Any future taxonomy correction belongs upstream at NCBI and in the pinned refresh governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. An emission-rule correction belongs in `src/taxonmech/seed.py` with a focused test; a scope change belongs in `curation/seed_scope.tsv`. Do not hand-edit generated YAML, append an unearned review event, or use a shared voucher label as an identity override.

## Follow-up Checks

- Before future specimen-level enrichment, inspect the complete publisher Table S2 rows with an XLS-capable reader and verify the BOLD records independently. Obtain explicit accession/taxon-history evidence before treating 1035888 and 1036300 as equivalent.
- After an authorized source refresh, compare exact taxon 1036300, all eleven ancestors, genetic code, four native name classes, lifecycle rows, and eligible strain evidence before a one-record seed canary.
- Rerun schema and strict validation after authorized regeneration, then the corpus, provenance, rendering, documentation, and QC gates before publication. Validate separate append-only history only if later curation creates an event.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report SHA-256: `072445acf340fdb30081ee3e8d4582862bcc34f15cb1610b51ac2b7552895b13`. Only this new review report was written for this target. No YAML, source, scope, lifecycle, history, generated page, prior report, GitHub item, or worktree was modified. Eukaryota was neither re-reviewed nor edited. No paid research, outreach, source refresh, independent sequence analysis, or phenotypic inference was performed. The verdict does not confer human `REVIEWED` status.
