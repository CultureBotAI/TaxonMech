# YAML Record Review: Salinivibrio sp. CMST-7

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/salinivibrio_sp_cmst_7.yaml`
- Started UTC: 2026-10-03T15:20:34Z
- Finished UTC: 2026-10-03T15:21:37Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303766`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:2636825`, genetic code 11. Grounding is `EXACT`, mapping
status `SEEDED`, strain count zero. One NCBI name attestation and one
seed event are present; synonyms, nomenclature, mappings, strains,
genome links and causal graphs are not asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/salinivibrio_sp_cmst_7.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/salinivibrio_sp_cmst_7.yaml`:
  PASS; one file scanned, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone read confirms ID, label, rank, parent,
  code and all ten lineage entries. There are no target children in the
  pinned backbone, making its subtree a singleton.
- Complete exact-field scans of BacDive, LPSN, GTDB mappings, GOLD,
  MediaDive, Madin and BactoTraits inventories find no direct target rows.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Global provenance, generated products,
  exports and downloaded sequences were not audited.
- Ignored-inclusive ID, label and slug searches found no target history
  entry. Standalone history validation had no target; strict validation
  checked the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

The raw taxonomy row at `data/raw/ncbitaxon_taxa.tsv:308130` supplies
the exact identity, species rank, parent, genetic code and empty synonym
fields. The complete scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30678` agrees. The PATHS index
contains exactly one target row with this slug.

The NCBI browser URL was inaccessible through the web tool. Current
public API responses were inspected through a read-only escalated
request after sandbox DNS failure had been established in this session.
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303766&retmode=xml)
confirms identifier, scientific name, species rank, Bacteria division,
parent 2636825, code 11 and the non-root lineage without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303766)
confirms species rank and all ten ancestor IDs, including root.

The immediate parent is unclassified Salinivibrio, not directly the
genus. CMST-7 is part of the exact label, not a source-supported culture
accession. Do not infer strain rank or assign a named Salinivibrio
species. Exact grounding is to the NCBI concept, not formal nomenclature.

## Evidence

The sole `NCBITAXON` attestation uses the correct ID and label, count 1,
unit `NAME`, snapshot 2026-09-13. `curation/seed_scope.tsv:393091`
admits this taxon on 2026-09-13 with the one-source NCBI reason.
The embedded 2026-09-13T17:54:04Z event preserves that reason and does
not claim human review. Its generic inventory-directory wording does
not attribute evidence to sources absent from the attestation list.

Every lineage ID, label and rank matches the pinned root-first chain:
root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota,
Gammaproteobacteria, Vibrionales, Vibrionaceae, Salinivibrio and
unclassified Salinivibrio. Current NCBI responses corroborate the chain.

Ignored-inclusive compressed searches using target ID, full label and
slug covered all `*.jsonl.gz` files in `data/catalog/`, `data/bacdive/`,
`data/bvbrc/`, `data/gold/`, `data/straininfo/` and `data/seqcode/`.
The relevant hit was the NCBI scientific-name object. Two unrelated
objects were read and excluded: `ncbi_genbank-0063.jsonl.gz:9702` and
`gtdb_genomes-0009.jsonl.gz:38667` describe GCA_964343565.1, an
uncultured Actinomycetes bacterium, taxon 152507, isolate
ERP107066_co1_340. The number 1303766 is its ungapped sequence length.
Neither object supplies a genome or GTDB association for CMST-7.

## Completeness

The singleton subtree and empty BacDive membership support count zero.
Empty target memberships in other taxon inventories explain omitted
nomenclature, taxonomy mappings and non-NCBI attestations. These findings
are bounded to pinned source coverage, not biological absence.

Ignored-inclusive compressed searches of `data/atb/` and the full
`data/catalog/allthebacteria.tsv.xz` found no target ID, full label or
slug. No culture or BioSample key was supplied for a further supported
strain-genome join. Similar names, genus membership and numeric
coincidences do not justify populating those optional fields.

No DOI, PMID, literature evidence, gene, locus, regulator, pathway,
phenotype or transcriptomic dataset is asserted. iModulonDB is not
applicable. Optional evidence, nomenclature, type flags and causal
graphs need not be invented for this NCBI-only identity record.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Leave generated YAML and review status unchanged.
Future source corrections belong in the authoritative source and
maintained extraction workflow, followed by `src/taxonmech/seed.py`;
scope changes belong in `curation/seed_scope.tsv`. No owner change is
proposed here.

## Follow-up Checks

No corrective edit needs verification. Following an authorized source
refresh, repeat both focused validators and explicit lineage/source
comparisons. Run `just verify-corpus` in the full regeneration workflow;
this focused review does not establish corpus-wide reproduction.

## Additional Notes

Absence checks included ignored files through complete structured reads,
`find`, or `rg --no-ignore --hidden` with `-z` for compressed sources.
The only manual write is this report; strict validation produced its
standard diagnostic. No YAML, source, prior report, history or status
was edited. No generator, refresh, paid research, GitHub mutation or
cross-repository write occurred. Eukaryota was not re-reviewed.
