# YAML Record Review: Candidatus Paraburkholderia petitii

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/candidatus_paraburkholderia_petitii.yaml`
- Started UTC: 2026-10-05T07:58:39Z
- Finished UTC: 2026-10-05T08:04:10Z
- Verdict: pass

## Target

Read the complete 71-line generated `TaxonRecord` for `NCBITaxon:1034319`. It denotes Candidatus Paraburkholderia petitii at `SPECIES` rank in `BACTERIA`, parent `NCBITaxon:1822464`, genetic code 11, `EXACT` grounding, and `SEEDED` mapping status. Six NCBI synonyms and zero inventoried strains are represented. The sole source attestation counts one NCBITAXON `NAME` from snapshot 2026-09-13, not seven native name rows or two isolates.

Maintained owners are `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, `src/taxonmech/ncbi_taxdump.py`, and `src/taxonmech/seed.py` through `scripts/seed_from_sources.py`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/candidatus_paraburkholderia_petitii.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/candidatus_paraburkholderia_petitii.yaml --out /private/tmp/petitii-strict-20261005.tsv`: exit 0; one file scanned, zero error files or rows.
- Structured source comparisons passed identity, all lineage entries, source attestation, unique path-index entry, scope, and inline-event checks. A separate exact-set assertion verified all six synonym text/type/source tuples without duplicates.
- `just verify-corpus`: not run; the documented check is full-corpus-only. Its `--max-diffs` parameter limits diagnostics, not record scope.
- `just validate-products`: not applicable without curator-added graph/product-label assertions.
- `just validate-history`: not run; ignored-inclusive target/alias searches found no separate history artifact. The inline event was inspected.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221577` supports the identity and synonyms. All seven complete native name objects at `data/catalog/ncbi_names-0005.jsonl.gz` lines 30934-30940 were inspected, including their empty unique-name fields.

Complete live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034319&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034319) responses confirm the current identity and classification. The browser taxonomy page was inaccessible through the web tool; the structured responses supplied the check.

All nine root-first ancestors and their ranks match the pinned backbone: 1 root, 131567 cellular organisms, 2 Bacteria, 3379134 Pseudomonadati, 1224 Pseudomonadota, 28216 Betaproteobacteria, 80840 Burkholderiales, 119060 Burkholderiaceae, and 1822464 Paraburkholderia. Taxonomy EFetch also confirms code 11.

Three exact synonyms derive from NCBI's synonym/equivalent-name classes: the historical Burkholderia petitii and corrected Burkholderia sericanthae names, plus Paraburkholderia petitii. The authority string and the `includes` names Burkholderia sp. OL658 and Burkholderia sp. SD1512 remain related synonyms. This follows `ncbi_taxdump.py:91` and `seed.py:381`, without promoting individual isolate names to exact species equivalences.

`data/raw/ncbi_merged_ids.tsv:1004` redirects `NCBITaxon:1034317` into this current taxon. The target is not the retired source ID. Exact-field scans found no target dropped or type-material row.

## Evidence

`data/taxa/PATHS.tsv:14041` uniquely supplies the slug. `curation/seed_scope.tsv:321892` agrees with the exact reason in the inline `SEEDED_FROM_SOURCES` event dated 2026-09-13T17:54:04Z. Full mapped-inventory scans returned no target entries in BacDive, LPSN, GTDB, GOLD organisms, MediaDive, Madin, or BactoTraits; the backbone has no target children.

The live [LPSN Paraburkholderia petitii page](https://lpsn.dsmz.de/species/paraburkholderia-petitii), record 22383, recognizes the Candidatus combination, the Lemaire/Sawana authority attribution, and the corrected Burkholderia sericanthae basonym. It distinguishes not-validly-published status from pro-validly-published/pro-correct status. Its type field combines absence of a designated type strain with SD 1512 and SD 1512 (BR), and it links 16S accession JF916923. Those fields do not establish an authenticated culture deposit.

The [historical Burkholderia petitii page](https://lpsn.dsmz.de/species/burkholderia-petitii), record 800197, treats that spelling as inaccurate and points to the correction. The [Burkholderia sericanthae page](https://lpsn.dsmz.de/species/burkholderia-sericanthae), record 800452, identifies a homotypic relationship with the current Paraburkholderia name and attributes the spelling correction to Oren (2017). Both historical pages also give SD 1512 and JF916923. These are name-specific external nomenclatural statements, not an instruction to replace the NCBI-sourced label or to assert valid publication.

Exact-taxid Nuccore search returned six records. Every returned record's full metadata, references, and features were inspected, omitting raw bases and protein translations. All six carry taxon 1034319 and the respective strain qualifier:

| Isolate | Partial 16S rRNA | Partial recA | Partial gyrB |
| --- | --- | --- | --- |
| SD1512 | [JF916923.1](https://www.ncbi.nlm.nih.gov/nuccore/JF916923.1), 1144 bp | [JF916916.1](https://www.ncbi.nlm.nih.gov/nuccore/JF916916.1), 549 bp | [JF916911.1](https://www.ncbi.nlm.nih.gov/nuccore/JF916911.1), 588 bp |
| OL658 | [JF916922.1](https://www.ncbi.nlm.nih.gov/nuccore/JF916922.1), 1144 bp | [JF916917.1](https://www.ncbi.nlm.nih.gov/nuccore/JF916917.1), 549 bp | [JF916910.1](https://www.ncbi.nlm.nih.gov/nuccore/JF916910.1), 588 bp |

These are marker records, not genomes or collection-deposit accessions. Exact-taxid Assembly search returned zero IDs with phrase-not-found/no-items diagnostics; this is a bounded query result, not proof of global genome absence.

All six records cite Lemaire et al. (2011), [PMID 22203556](https://pubmed.ncbi.nlm.nih.gov/22203556/), [DOI 10.1007/s12275-011-1163-5](https://link.springer.com/article/10.1007/s12275-011-1163-5). The complete primary PubMed metadata and abstract fetched during the immediately preceding review were reread here. The paper proposes two Sericanthe-associated Candidatus species using 16S, recA, and gyrB evidence. Its publisher abstract was inspected in the preceding review; the subscription-only main text was not read. Plant chloroplast markers mentioned in the abstract are not bacterial gene evidence.

The public [supplementary PDF](https://static-content.springer.com/esm/art%3A10.1007%2Fs12275-011-1163-5/MediaObjects/12275_2011_1163_MOESM1_ESM.pdf) had been downloaded and text-inspected in the preceding review. The rendered Figure S1 panels A-C on PDF pages 3-5 were visually re-inspected for this target. All three label petitii as OL658 and **SD1592**, whereas NCBI taxonomy, the three SD-series nucleotide records, and the inspected LPSN pages use **SD1512**. This is an unresolved source-label discrepancy. No inspected source explicitly equates those two designations; neither a typographical correction nor an isolate-identity merge is assumed. The YAML preserves the NCBI designation and does not assert SD1592 equivalence.

## Completeness

The identity seed's represented fields are supported. Optional nomenclature enrichment is available externally, but no corresponding target LPSN input or mapping was found locally. That optional gap does not make the NCBI identity invalid.

Ignored-inclusive content searches covered hidden and compressed data under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding generic `SOURCE.json` descriptors. Boundary-aware identity/name/alias searches included both SD1512 and SD1592 and returned ten contexts: the backbone, scope row, redirect, and seven native names. A separate whole retired-ID search returned only the redirect. Exact nucleotide-accession/original-paper and prefixed LPSN-record-ID/record-DOI searches returned no matches. These bounds do not claim all external sources or every possible bare numerical identifier were searched.

Ignored-inclusive report/history filename searches and history-content searches found no prior target report or separate history artifact before this report was added.

`seed.py:483` onward counts inventoried BacDive entries, not NCBI aliases or marker sequences, so `strain_count: 0` is consistent. No authenticated collection identifier or explicit genome source chain was established. iModulonDB is not applicable: no expression-module or regulatory assertion is represented.

## Findings

None found in the represented YAML claims.

Counts: 0 blocker, 0 major, 0 minor.

The external SD1512/SD1592 discrepancy is retained as unresolved evidence context, not a demonstrated YAML defect: the record attributes its actual alias to NCBI and makes no cross-designation identity assertion.

## Recommended Edits

No required edits. Retain the current NCBI identity and scoped synonyms; do not rename SD1512 from a figure label, add SD1592 as an equivalent isolate, or convert six markers into genome or culture-strain entries.

Optional nomenclature enrichment belongs in the maintained LPSN source/mapping pipeline (`src/taxonmech/extract.py` and upstream kg-microbe inputs). Preserve name-specific source identifiers and Candidatus status distinctions. Before any isolate-level enrichment, resolve the SD1512/SD1592 conflict through an explicit primary specimen/accession mapping or authoritative correction. Do not patch generated YAML or promote review/curation status.

## Follow-up Checks

For optional enrichment, inspect the complete original description and any explicit specimen-to-accession table or correction, preserving the unresolved designation difference until supported. Confirm a source-backed NCBI mapping for each nomenclatural row. Require whole eligible collection identifiers and explicit provenance for genome joins. After an authorized maintained-input change, regenerate through the validated writer and run focused schema/strict checks plus full corpus reproduction.

## Additional Notes

All invoked review command sessions terminated. The original main text remains unread, and the source-label discrepancy remains unresolved. Cached public primary evidence was explicitly distinguished from fresh taxonomy and nucleotide reads.

No taxon, source, generated page, earlier report, curation history, or status changed. This review adds only this new repository report; diagnostic and inspection artifacts are under `/private/tmp`.
