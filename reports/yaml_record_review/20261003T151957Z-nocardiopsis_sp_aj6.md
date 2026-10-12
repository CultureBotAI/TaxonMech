# YAML Record Review: Nocardiopsis sp. AJ6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_aj6.yaml`
- Started UTC: 2026-10-03T15:18:58Z
- Finished UTC: 2026-10-03T15:19:57Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. Identity is
`NCBITaxon:1303765`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:2649073`, genetic code 11. Grounding is `EXACT`, mapping
status `SEEDED`, strain count zero. One NCBI name attestation and one
embedded seed event are present. No synonyms, nomenclature, mappings,
strains, genome links, experimental claims or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/nocardiopsis_sp_aj6.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/nocardiopsis_sp_aj6.yaml`:
  PASS; one file scanned, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone read confirms identity, rank, parent, code
  and all ten root-first lineage entries. No target children occur in
  the pinned backbone, so its subtree is a singleton.
- Complete exact-field inventory scans find no direct BacDive, LPSN,
  GTDB mapping, GOLD, MediaDive, Madin or BactoTraits rows for this ID.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Global source provenance, generated products,
  exports and genome sequences were not audited.
- Ignored-inclusive history searches found no target ID, label or slug.
  Standalone history validation had no target; strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308129` supplies the exact label, species
rank, parent, code and empty synonym fields. The complete native name
object at `data/catalog/ncbi_names-0007.jsonl.gz:30677` agrees and has
no unique-name qualifier. The PATHS index has one target row with this slug.

The NCBI browser URL was inaccessible through the web tool. Read-only
public API requests succeeded with network escalation after sandbox DNS
failure had been established earlier in the review session. Inspected
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303765&retmode=xml)
confirms the identifier, scientific name, species rank, Bacteria division,
parent 2649073, code 11 and complete non-root lineage, with no alternate
names. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303765)
also confirms species rank and all ten ancestor IDs including root.

The immediate parent is unclassified Nocardiopsis, not directly genus
Nocardiopsis. AJ6 is part of the exact source label, not evidence for a
registered culture accession or permission to change the rank to strain.
Exact grounding to this NCBI concept is not formal species nomenclature.

## Evidence

The sole `NCBITAXON` attestation uses the correct source ID and label,
count 1, unit `NAME`, snapshot 2026-09-13. The scope row at
`curation/seed_scope.tsv:393090` admits this taxon on 2026-09-13 with
the one-source NCBI reason. The embedded 2026-09-13T17:54:04Z seed event
preserves that reason and makes no human-review claim. Its generic
input-directory wording is not a claim of evidence from every inventory.

Every lineage identifier, label and rank matches the complete pinned
chain: root, cellular organisms, Bacteria, Bacillati, Actinomycetota,
Actinomycetes, Streptosporangiales, Nocardiopsidaceae, Nocardiopsis and
unclassified Nocardiopsis. Current NCBI responses agree with the chain.

Ignored-inclusive compressed ID, full-label and slug searches covered all
`*.jsonl.gz` files in `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/straininfo/` and `data/seqcode/`. The relevant result
was the scientific-name object. Three additional objects were fully read
and excluded: `gtdb_genomes-0013.jsonl.gz:1559`,
`ncbi_genbank-0016.jsonl.gz:19528` and
`ncbi_refseq-0003.jsonl.gz:26727`. They describe the
GCA/GCF_017911785.1 assembly family, Borreliella garinii strain IPT176,
taxon 29519. The number 1303765 is a sequence-length value, not their
taxon ID. They supply no genome or GTDB mapping evidence for AJ6.

## Completeness

The singleton subtree and empty BacDive membership support strain count
zero. Empty exact-ID memberships in the other taxon inventories explain
the omitted nomenclature, mappings and non-NCBI counts. This is bounded
pinned-source coverage, not proof of biological or genome absence.

Ignored-inclusive compressed searches of `data/atb/` and the complete
`data/catalog/allthebacteria.tsv.xz` found no target ID, full label or
slug. No culture-deposit or BioSample key was supplied for a further
supported strain-genome join. Optional fields must not be filled from
genus membership, a similar designation or unrelated numeric matches.

No gene, locus, regulator, pathway, phenotype or transcriptomic dataset
is asserted, so iModulonDB is not applicable. There are no cited DOI,
PMID or literature objects to resolve. Optional record-level evidence,
nomenclature, type flags and causal graphs need not be invented.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Keep the generated YAML and review status unchanged.
Future source corrections belong in the authoritative source and
maintained extraction workflow, followed by `src/taxonmech/seed.py`;
scope changes belong in `curation/seed_scope.tsv`. No owner change is
proposed for this record.

## Follow-up Checks

No corrective edit needs verification. After an authorized source refresh,
repeat both focused validators and explicit lineage/source comparisons.
Run `just verify-corpus` in the full regeneration workflow. This focused
review does not prove corpus-wide reproducibility.

## Additional Notes

Absence checks included ignored files using full structured reads,
`find`, or `rg --no-ignore --hidden` with `-z` for compressed sources.
The only manual write is this report; strict validation produced its
standard diagnostic. No YAML, source, prior report, history or status
was edited. No generator, refresh, paid research, GitHub mutation or
cross-repository write occurred. Eukaryota was not re-reviewed.
