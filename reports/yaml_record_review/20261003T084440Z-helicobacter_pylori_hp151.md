# YAML Record Review: Helicobacter pylori HP151

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_hp151.yaml`
- Started UTC: 2026-10-03T08:43:30Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T08:44:40Z
- Verdict: pass with minor issues

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:103172` denotes
Helicobacter pylori HP151 beneath species `NCBITaxon:210`. It declares
`STRAIN`, `BACTERIA`, `EXACT` grounding and `SEEDED` mapping status, with ten
ancestors, genetic code 11, zero attached strains, one NCBI name attestation
and one seed event. No synonyms, nomenclature, GTDB mappings, genome links
or causal-graph claims are present. It is indexed at `data/taxa/PATHS.tsv:13126`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_hp151.yaml`: passed,
  no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_hp151.yaml`:
  passed, one file scanned and zero errors.
- Structured YAML/TSV checks confirmed identifier, label, stored rank, parent,
  genetic code and every ancestor ID, label, rank and parent link. A complete
  taxonomy-inventory scan found zero direct children.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_hp151.yaml`
  passed. No generated record or maintained source was edited.
- `just verify-corpus` was not rerun: it is full-corpus-only. Focused checks
  are not a new reproduction pass. Full source hashes/censuses and rendered
  pages were not checked.
- `just validate-products` is not applicable without causal-graph nodes.
  `just validate-history` was not run: the ignored-file-inclusive target
  search found no separate history artifact. The embedded seed event was
  inspected and covered by strict validation.

## Identity and Grounding

The pinned taxonomy inventory and native NCBI name catalog agree on the
identifier and HP151 label. The stored parent is the species H. pylori, not
a similarly numbered strain, and the carried lineage is internally consistent.
The label has not been expanded into a species-wide equivalence claim.

The [NCBI browser target](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103172)
could not be retrieved. Alternate parameter order, name lookup and the
[NCBI Datasets target](https://www.ncbi.nlm.nih.gov/datasets/taxonomy/103172/)
also failed. These links document attempted checks, not inspected authority
content. Current external rank/name confirmation therefore remains incomplete;
no live rank discrepancy is asserted for HP151.

## Evidence

| Claim group | Inspected source and conclusion |
| --- | --- |
| Identifier, name, rank and parent | `data/raw/ncbitaxon_taxa.tsv:18339` records 103172, HP151, STRAIN, parent 210 and code 11. All ten ancestor rows were separately checked. |
| Native name | `data/catalog/ncbi_names-0000.jsonl.gz:38352` has the scientific name Helicobacter pylori HP151 for 103172. This supports identity within the retained source snapshot. |
| Source attestation | The taxonomy inventory's attested source is NCBI, matching the one NAME assertion and the 2026-09-13 snapshot note. This is not a phenotype or genome count. |
| Scope and history | `curation/seed_scope.tsv:144000` supplies the 2026-09-13 one-source rationale, preserved in the seed event. SEEDED status does not imply human review. |

There are no cited papers, LPSN identifiers, ontology graph nodes or genome
accessions in the target requiring claim-specific verification. iModulonDB
is not applicable: no gene, regulator, trait or expression-module claim is
made. Absence from that resource would not constitute negative evidence.

## Completeness

The identifier, exact name and slug were searched with
`rg --no-ignore --hidden` in review reports, history, curation, raw, ATB and
StrainInfo uncompressed inventories. Only the taxonomy and scope rows matched
before this report; no prior target report or separate history artifact was
found in those surfaces. A standalone HP151 search in the BacDive and
culture-collection inventories returned no match, including ignored files.

A decompressed, ignored-file-inclusive search of JSONL.GZ/TSV.GZ catalogs
under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/` and
`data/straininfo/` checked exact taxonomy fields, name, slug and standalone
HP151. Its only match was the native NCBI scientific-name row. This is a
bounded finding, not proof that this strain has never been sequenced or
deposited anywhere. The compressed ATB full TSV.XZ was not scanned.

Zero attached strains and empty optional source/phenotype slots are
consistent with the inspected evidence. Do not borrow a species type strain,
genome, deposit or phenotype solely because it belongs to H. pylori.

## Findings

- **Blocker:** None found in the inspected file or pinned evidence.
- **Major:** None found.
- **Minor (1): Live authority verification remains unavailable.** The local
  identity and stored lineage are supported, but repeated authority requests
  failed, so present-day identity/rank correspondence was not independently
  checked. This is a review-evidence limitation, not an observed YAML defect.
  A future discrepancy would belong to `conf/ncbi_taxdump.yaml` and
  `src/taxonmech/ncbi_taxdump.py`, followed by regenerated inventory/records,
  not a direct YAML patch.

## Recommended Edits

No evidence-backed record edit is recommended now. Retry the exact NCBI
authority lookup and inspect the hash-verified pinned taxdump if a discrepancy
appears. The importer normalizes the supplied rank; it does not establish a
new rank from the organism label. Preserve the source-based empty optional
slots and current SEEDED status.

## Follow-up Checks

- Retry the NCBI browser or Datasets endpoint for 103172 and compare label,
  rank and parent with the snapshot. Do not infer this record's rank from
  another HP-numbered taxon.
- If needed, recover the source pinned in `conf/ncbi_taxdump.yaml`, SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`,
  and inspect the exact `nodes.dmp`/`names.dmp` rows.
- After any separately authorized source correction, use the normal refresh,
  `just seed-canary NCBITaxon:103172`, both target validators and the full
  `just verify-corpus`.

## Additional Notes

No external page content was used to fabricate a successful live check.
The ignored-file-inclusive taxdump filename search in this session found no
archive or `nodes.dmp` in the checkout; copies elsewhere were not assessed.
No full catalog hashes, external sequence payloads or rendered pages were
verified. No paid research, outbound messages, GitHub mutation, history
addition or review-status promotion occurred.
