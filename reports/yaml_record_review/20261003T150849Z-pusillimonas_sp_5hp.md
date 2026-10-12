# YAML Record Review: Pusillimonas sp. 5HP

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pusillimonas_sp_5hp.yaml`
- Started UTC: 2026-10-03T15:07:52Z
- Finished UTC: 2026-10-03T15:08:49Z
- Verdict: pass

## Target

Read the complete generated YAML before judgement. This `TaxonRecord`
denotes `NCBITaxon:1303724`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:2640016`, code 11. Grounding is `EXACT`, mapping status
`SEEDED`, and strain count zero. One NCBI name attestation and one seed
event are present; no synonyms, nomenclature, mappings, strains, genomes,
experimental evidence or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pusillimonas_sp_5hp.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pusillimonas_sp_5hp.yaml`:
  PASS; one file scanned, zero errors. Standard diagnostic:
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison confirms identity, rank,
  parent, code and all ten lineage entries. There are no target children
  in the pinned backbone.
- Complete exact-field inventory scans find no direct target BacDive,
  LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits rows.
  The empty BacDive membership and singleton subtree support count zero.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Global provenance, generated pages, exports
  and downloaded sequences were not audited.
- Ignored-inclusive ID, label and slug searches of `history/` found no
  entry. Standalone history validation had no target; strict validation
  checked the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308125` supports the exact name, species
rank, parent 2640016, code 11 and empty synonym fields. The full native
name object at `data/catalog/ncbi_names-0007.jsonl.gz:30673` assigns
the same scientific name and identifier, with no unique-name qualifier.

The web tool could not access the Datasets URL. Read-only public API
requests succeeded: inspected
[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303724&retmode=xml)
confirms name, species rank, Bacteria division, parent, code and lineage,
with no alternate names in the response.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303724)
independently supplies all ten ancestor IDs, including root, and species rank.

The authoritative immediate parent is unclassified Pusillimonas, not
directly genus Pusillimonas. The isolate-like 5HP suffix does not justify
changing the rank to strain or assigning a registered culture accession.
Exact grounding means this NCBI concept, not formal species nomenclature
or equivalence to a named Pusillimonas species.

## Evidence

The NCBI attestation has source ID 1303724, count 1, unit `NAME`, and
snapshot date 2026-09-13. It agrees with the raw row and native name
object. `curation/seed_scope.tsv:393087` explicitly admits this taxon
on 2026-09-13 with the one-source NCBI reason. The embedded event at
2026-09-13T17:54:04Z preserves that reason without claiming human review.
Its generic input-directory wording does not claim strain or genome
evidence from every mentioned inventory.

All lineage IDs, labels and ranks match the pinned parent chain: root,
cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota,
Betaproteobacteria, Burkholderiales, Alcaligenaceae, Pusillimonas and
unclassified Pusillimonas. Both live NCBI responses corroborate the chain.

Ignored-inclusive compressed searches of all 156 selected native JSONL
catalogs in `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/straininfo/` and `data/seqcode/` used the taxon ID, full label and
slug. Only the target NCBI scientific-name object matched. This is
bounded source coverage, not an inference about uncataloged biological data.

## Completeness

- Complete structured inventory reads explain zero listed BacDive strains
  and the omitted nomenclature, taxonomic mappings and non-NCBI counts.
- Ignored-inclusive compressed searches of `data/atb/` and the complete
  `data/catalog/allthebacteria.tsv.xz` found no target ID, label or slug.
  No culture or BioSample key was supplied for a further strain-genome
  join. This does not prove that no culture or sequence exists elsewhere.
- No gene, locus, regulator, pathway, phenotype or transcriptomics dataset
  is asserted, so the structured iModulonDB workflow is not applicable.
- No DOI, PMID, publication or experimental evidence object is cited.
  Optional nomenclature, evidence and graph fields need not be invented
  to complete a source-grounded identity record.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

The record agrees with maintained inputs and live NCBI identity.

## Recommended Edits

None required. Do not hand-edit generated YAML, infer a culture identifier
from 5HP, substitute a named species, or promote this automated review to
human `REVIEWED` status. Future source corrections belong in the
authoritative source and maintained extraction workflow, then
`src/taxonmech/seed.py`; scope is owned by `curation/seed_scope.tsv`.

## Follow-up Checks

No corrective edit needs verification. After a future authorized refresh,
repeat the focused validators and explicit lineage/source-membership
checks. New culture or genome links require their own source evidence.
Run `just verify-corpus` in the full-corpus regeneration workflow; this
review does not claim global reproducibility.

## Additional Notes

Absence checks include ignored files via complete structured reads or
`rg --no-ignore --hidden`, with `-z` for compression. Prior report absence
was checked with `find`. The only manual write is this report; strict
validation wrote its standard diagnostic. No YAML, prior report, source,
history or status was edited. No refresh, generator, paid research,
GitHub mutation or cross-repository write occurred. Eukaryota was not
re-reviewed.
