# YAML Record Review: Streptomyces sp. AJ8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_aj8.yaml`
- Started UTC: 2026-10-03T15:23:11Z
- Finished UTC: 2026-10-03T15:24:43Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. The target is
`NCBITaxon:1303767`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:2593676`, genetic code 11. Grounding is `EXACT`, mapping
status `SEEDED`, and strain count zero. One NCBI name attestation and
one embedded seed event are present. No synonyms, nomenclature,
mappings, strains, genome links, experimental claims or causal graph
are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_sp_aj8.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/streptomyces_sp_aj8.yaml`:
  PASS; one file scanned, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison confirms identity, rank,
  parent, genetic code and all ten root-first lineage entries. No
  target children occur in the pinned backbone.
- Complete exact-field scans found no target BacDive, LPSN, GTDB mapping,
  GOLD, MediaDive, Madin or BactoTraits inventory rows. Empty BacDive
  membership and the singleton subtree support strain count zero.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Global source provenance, rendered products,
  exports and downloaded genome sequences were not audited.
- Ignored-inclusive ID, label and slug searches found no target standalone
  history entry. History validation had no target; strict validation
  checked the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308131` supplies the exact label, species
rank, parent, code and empty synonym fields. The complete native name
object at `data/catalog/ncbi_names-0007.jsonl.gz:30679` agrees, without
a unique-name qualifier. The PATHS index contains one target row with
this slug.

The NCBI browser URL was inaccessible through the web tool, and initial
sandboxed API calls failed DNS resolution. Subsequent read-only public
API requests succeeded with network escalation. Inspected
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303767&retmode=xml)
confirms the ID, exact name, species rank, Bacteria division, parent,
code and non-root lineage, with no alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303767)
confirms the name, species rank and all ten ancestor IDs including root.

The immediate parent is unclassified Streptomyces, not directly the
genus. AJ8 is part of the exact NCBI label, not an established culture
accession or permission to change the rank to strain. Exact grounding
to this NCBI concept is not a formal nomenclatural assertion.

## Evidence

The sole `NCBITAXON` attestation has the correct source ID and label,
count 1, unit `NAME`, snapshot 2026-09-13. The scope row at
`curation/seed_scope.tsv:393092` admits the taxon on 2026-09-13 with
the one-source NCBI reason. The 2026-09-13T17:54:04Z seed event
preserves that reason without claiming human review. Its generic
input-directory wording is not evidence from every named inventory.

Every lineage ID, label and rank agrees with the complete pinned chain:
root, cellular organisms, Bacteria, Bacillati, Actinomycetota,
Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and
unclassified Streptomyces. Current NCBI responses corroborate that chain.

Ignored-inclusive compressed searches by target ID, full label and slug
covered every `*.jsonl.gz` file under `data/catalog/`, `data/bacdive/`,
`data/bvbrc/`, `data/gold/`, `data/straininfo/` and `data/seqcode/`.
Only the NCBI scientific-name object matched. This establishes bounded
pinned-source coverage, not an absence of biological data elsewhere.

## Completeness

Empty exact-ID memberships in the taxon inventories explain omitted
nomenclature, mappings, strains and non-NCBI attestations. The zero
strain count is a BacDive membership count, not a genome-absence claim.

Ignored-inclusive compressed searches of `data/atb/` and the full
`data/catalog/allthebacteria.tsv.xz` found no target ID, full label or
slug. No culture-deposit or BioSample key was supplied for a further
evidence-backed strain-genome join. Neither a similar designation nor
genus membership justifies inventing an association.

No gene, locus, regulator, pathway, phenotype or transcriptomic dataset
is asserted, so iModulonDB is not applicable. No DOI, PMID or literature
object is cited. Optional record-level evidence, nomenclature, type
flags and causal graphs need not be populated for this identity record.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Keep generated YAML and review status unchanged. Future
source corrections belong in the authoritative source and maintained
extraction workflow, followed by `src/taxonmech/seed.py`; scope changes
belong in `curation/seed_scope.tsv`. No owner change is proposed here.

## Follow-up Checks

No corrective edit needs verification. After an authorized source
refresh, repeat both focused validators and explicit lineage/source
comparisons. Run `just verify-corpus` in the full regeneration workflow;
this focused review does not establish corpus-wide reproducibility.

## Additional Notes

Absence checks included ignored files through complete structured reads,
`find`, or `rg --no-ignore --hidden` with `-z` for compressed sources.
The only manual write is this report; strict validation produced its
standard diagnostic. No target YAML, prior report, source, history or
status was changed. No generator, refresh, paid research, GitHub mutation
or cross-repository write occurred. Eukaryota was not re-reviewed.
