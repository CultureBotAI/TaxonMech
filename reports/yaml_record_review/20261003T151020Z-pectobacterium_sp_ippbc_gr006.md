# YAML Record Review: Pectobacterium sp. IPPBC GR006

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pectobacterium_sp_ippbc_gr006.yaml`
- Started UTC: 2026-10-03T15:09:28Z
- Finished UTC: 2026-10-03T15:10:20Z
- Verdict: pass

## Target

Read the complete generated YAML before judgement. This `TaxonRecord`
denotes `NCBITaxon:1303726`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:2627739`, genetic code 11. Grounding is `EXACT`, mapping
status `SEEDED`, and strain count zero. The record has one NCBI name
attestation and one embedded seed event, with no synonyms, nomenclature,
mappings, strains, genome links, experimental evidence or causal graph.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pectobacterium_sp_ippbc_gr006.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pectobacterium_sp_ippbc_gr006.yaml`:
  PASS; one file scanned, zero errors. Standard diagnostic:
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison confirms identity, rank,
  parent, code and all ten lineage entries. There are no target children
  in the pinned backbone.
- Complete exact-field inventory scans find no direct target BacDive,
  LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits rows.
  Empty BacDive membership and the singleton subtree support count zero.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Global provenance, generated pages, exports
  and downloaded sequences were not audited.
- Ignored-inclusive ID, label and slug searches of `history/` found no
  target entry. Standalone history validation had no target; strict
  validation checked the embedded event. Graph/product gates do not apply.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308126` supports the scientific name,
species rank, parent 2627739, genetic code 11 and empty synonym fields.
The complete native name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30674` records the same identifier
and scientific name, with no unique-name qualifier.

The NCBI browser URL was inaccessible through the web tool. Inspected
[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303726&retmode=xml)
confirms identifier, label, species rank, Bacteria division, parent,
code and lineage, with no alternate names in the response.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303726)
independently confirms species rank and all ten ancestor IDs, including root.

The immediate parent is the unranked unclassified Pectobacterium node,
not directly genus Pectobacterium. IPPBC GR006 is part of this exact
NCBI label; it does not authorize inventing a culture-collection record,
changing rank to strain, or assigning a named Pectobacterium species.
Exact grounding is to this NCBI concept, not formal species nomenclature.

## Evidence

The sole attestation is `NCBITAXON`, source ID 1303726, count 1, unit
`NAME`, snapshot date 2026-09-13. It agrees with the raw taxonomy row
and native name object. `curation/seed_scope.tsv:393088` explicitly
admits the taxon on 2026-09-13 with the one-source NCBI reason.
The 2026-09-13T17:54:04Z seed event preserves that reason without
claiming human review. Its generic input-directory wording does not
claim evidence from every named inventory.

Every lineage ID, label and rank matches the pinned chain: root,
cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota,
Gammaproteobacteria, Enterobacterales, Pectobacteriaceae, Pectobacterium
and unclassified Pectobacterium. Both live NCBI responses corroborate
the same hierarchy. No alternative hierarchy is inferred locally.

Ignored-inclusive compressed searches of all 156 selected native JSONL
catalogs in `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/straininfo/` and `data/seqcode/` used the target ID, full label
and slug. Only the NCBI scientific-name object matched. This establishes
bounded pinned-source coverage, not absence of biological data elsewhere.

## Completeness

- Complete structured inventory reads support zero listed BacDive strains
  and explain the omitted nomenclature, mappings and non-NCBI counts.
- Ignored-inclusive compressed searches of `data/atb/` and the complete
  `data/catalog/allthebacteria.tsv.xz` found no target ID, label or slug.
  No culture or BioSample key was supplied for a further evidence-backed
  strain-genome join. This does not establish that no culture or sequence
  exists outside the searched pinned sources.
- No gene, locus, regulator, pathway, phenotype or transcriptomic dataset
  is asserted, so the structured iModulonDB workflow is not applicable.
- No DOI, PMID, publication or experimental evidence object is cited.
  Optional record-level evidence, nomenclature, type flag and causal
  graph need not be invented for this NCBI-only identity record.
- Genus membership supplies no evidence for a particular phenotype or
  genome relationship. None has been inferred in the YAML or this review.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

The record agrees with inspected maintained inputs and current NCBI identity.

## Recommended Edits

None required. Do not hand-edit generated YAML, shorten the identifying
designation, infer culture/genome links, substitute a named species,
or promote an automated review to human `REVIEWED` status.
Future source corrections belong in the authoritative source and
maintained extraction workflow, followed by `src/taxonmech/seed.py`.
Scope is owned by `curation/seed_scope.tsv`; no owner change is proposed.

## Follow-up Checks

No corrective edit needs verification. After a future authorized source
refresh, repeat the focused validators and explicit lineage/source
membership comparisons. New culture/genome associations require their
own source evidence, not a matching genus or a similar isolate designation.
Run `just verify-corpus` in the full-corpus regeneration workflow;
this focused review does not claim corpus-wide reproducibility.

## Additional Notes

Absence checks include ignored files through complete structured reads
or `rg --no-ignore --hidden`, with `-z` for compressed sources. Prior
report absence was checked with `find`. The only manual write is this
report; strict validation wrote its standard diagnostic. No taxon YAML,
prior report, source, history or status was edited. No refresh, generator,
paid research, GitHub mutation or cross-repository write occurred.
Eukaryota was not re-reviewed.
