# YAML Record Review: Comamonas sp. CNB 8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/comamonas_sp_cnb_8.yaml`
- Started UTC: 2026-10-04T19:56:20Z
- Finished UTC: 2026-10-04T19:57:24Z
- Verdict: pass

## Target

Read the full generated `TaxonRecord` for `NCBITaxon:1033887`,
Comamonas sp. CNB 8: SPECIES, BACTERIA, parent `NCBITaxon:2638500`,
`grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code 11.
It contains ten root-first lineage entries, zero inventoried BacDive
strains, one NCBITAXON name attestation and one seed event. It asserts
no external name mapping, culture deposit, genome or mechanism.

The review concerns this exact CNB 8 concept, not other CNB isolates.
No generated record, input, code or curation-history entry was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/comamonas_sp_cnb_8.yaml`.
  Output: `No issues found`.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/comamonas_sp_cnb_8.yaml`.
  One file scanned, zero files with errors and zero error rows. This is
  the implementation of `just validate-strict` and emits its standard
  `reports/instance_validation_failures.tsv` diagnostic.
- Passed bounded source comparisons of identity, the full ancestor chain,
  direct inventory matches, filename lock, scope and seed wording. A
  complete backbone scan found no children of this taxon.
- The existing CAFI-backed `normalize_culture_identifier('CNB 8')`
  returned an empty string, not an eligible culture-deposit join key.
- Not run: `just verify-corpus`. Its inspected implementation is a
  full-corpus byte-comparison gate; `--max-diffs` limits diagnostics only.
  The bounded comparisons here are not a focused replacement.
- Not applicable: `just validate-products`, because there are no
  curator-added graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline event was inspected.
  Full-corpus QC, provenance, rendering and test-suite gates were not run.

## Identity and Grounding

The complete backbone row `data/raw/ncbitaxon_taxa.tsv:221323`, native
name object `data/catalog/ncbi_names-0005.jsonl.gz:30663` and inspected
[NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033887&retmode=xml)
agree on the taxon identifier, scientific name, species rank, parent,
bacterial domain and genetic code. The
[Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033887)
confirms all ten lineage IDs, including root 1. Expanded live lineage
labels and ranks agree with the pinned parent chain.

The direct parent is unclassified Comamonas, beneath genus Comamonas;
the carried family, order and class are Comamonadaceae, Burkholderiales
and Betaproteobacteria. The SPECIES rank is NCBI's rank for this
placeholder concept, not a formal nomenclatural assertion. The CNB 8
laboratory designation does not imply STRAIN rank or an MTCC accession.

The native name object has only the scientific name, and the backbone's
three synonym fields are empty. Complete exact-ID scans of type-material,
merged-ID and dropped-taxon tables found no matching row. The live
response gives no replacement or synonym requiring a lifecycle change.

## Evidence

The NCBITAXON attestation exactly reproduces the backbone's identifier
and label, one NAME assertion and snapshot `2026-09-13`. Complete
directly mapped BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits
inventory scans returned no target rows. With no descendants, zero
listed BacDive strains is also the complete subtree count.

The exact-taxonomy nuccore search returned one entry, whose metadata,
reference and feature qualifiers were inspected in the
[NCBI sequence response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF775508.1&rettype=gb&retmode=xml).
`JF775508.1` is a 1,405-base partial 16S rRNA sequence with explicit
taxon 1033887 and strain CNB 8 qualifiers. The source records pesticide
contaminated soil in Chhattisgarh, India. Its reference is a 2011 direct
submission, not a cited species-description paper.

The submitting institution's Microbial Type Culture Collection and Gene
Bank affiliation is an address, not an explicit culture accession for
CNB 8. Neither that affiliation nor the laboratory name supplies a
deposit-backed strain-genome join. The marker also does not establish
a genome assembly or a pesticide-degradation phenotype. No such claim
is present in the YAML, and none was added from the isolation context.

The exact-taxonomy Assembly search returned zero entries with a
`phrasesnotfound` warning for `txid1033887[Organism:noexp]`. This is a
bounded query result, not proof of global genome absence. The Taxonomy
Browser HTML was inaccessible to the web tool, but NCBI's direct public
taxonomy and sequence APIs provided the evidence above. No DOI or PMID
is cited by the record or the inspected marker submission.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i` over
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. The taxon, full name, slug and
CNB-8/CNB 8/CNB_8 spelling variants yielded four matching lines, all
inspected. The name object was subsequently read in full.

Three matches were the backbone, scope and native name. The fourth,
AllTheBacteria sample `SAMEA1033887`, is classified as Streptococcus
pneumoniae and is a numeric collision, not identity evidence. A second
ignored-inclusive search for `JF775508` completed with zero matches.
No native deposit or eligible strain-genome assertion for CNB 8 was
found within that searched scope.

The zero strain count means zero inventoried BacDive strains, not that
no biological isolate exists. The newly inspected marker is bounded
source context; without an eligible strain association, its absence from
the YAML is not a required missing genome link. Empty optional
nomenclature, taxonomy mappings, definition, record-level evidence and
mechanism sections are appropriate for this NCBI-only seeded record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and source scope. The identifier,
rank, lineage, name attestation, strain count, status and inline
provenance are supported. Similar designations and isolation context
were not promoted into additional biological claims.

## Recommended Edits

None. Preserve the generated YAML. Future evidence-backed source or
identity corrections belong in the maintained inventory pipeline and,
where required, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`.
Scope changes belong in `curation/seed_scope.tsv`. The present evidence
does not justify a scope change, manual patch or status promotion.

## Follow-up Checks

On future source refreshes, search the exact taxon and CNB 8 designation
for an explicit registered deposit or primary genome assertion. Do not
derive a culture accession from a submitter's affiliation or transfer
evidence from another CNB isolate. Keep `JF775508.1` a nucleotide marker.
After an authorized change, rerun focused validators and the complete
`just verify-corpus` gate after regeneration. No unresolved blocker
prevents the present verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13779` locks the slug.
`curation/seed_scope.tsv:321653` records the September 13, 2026 addition
and one-source reason. The `2026-09-13T17:54:04Z` seed event reproduces
the NCBITAXON source list and scope reason exactly. This read-only
review neither promotes SEEDED to REVIEWED nor appends a curation event.

Ignored-inclusive report/history/curation filename searches found no
earlier target report or target-specific history artifact before this
report was created. iModulonDB is not applicable to a record without
gene, regulator or expression-module claims. No paid research, outside
contact, GitHub mutation or generator run occurred.
