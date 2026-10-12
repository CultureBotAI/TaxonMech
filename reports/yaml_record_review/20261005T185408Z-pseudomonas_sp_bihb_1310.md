# YAML Record Review: Pseudomonas sp. BIHB 1310

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_bihb_1310.yaml`
- Started UTC: 2026-10-05T18:51:31Z
- Finished UTC: 2026-10-05T18:54:08Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. The target is
`NCBITaxon:1034637`, Pseudomonas sp. BIHB 1310: rank `SPECIES`,
domain `BACTERIA`, parent `NCBITaxon:196821`, genetic code 11,
`EXACT` grounding, `SEEDED` status, and `strain_count: 0`.
A taxon record is not itself a culture deposit or genome.

Source and scope rows are `data/raw/ncbitaxon_taxa.tsv:221674`
and `curation/seed_scope.tsv:321985`.
`data/taxa/PATHS.tsv:14140` agrees in identifier and slug.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_bihb_1310.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_bihb_1310.yaml --out /private/tmp/bihb1310-strict-20261005.tsv`: exit 0; one file, zero error files and zero error rows. The TSV contains only its header.
- Structured checks compared the full backbone row and ten ancestors, PATHS, scope, attestation, and seed event. Seven raw source inventories and exact type-material, merged-ID, and dropped-record tables were checked.
- `rg --no-ignore --hidden -n -z -i` searched the ID, full label, slug, and BIHB 1310 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Hidden, ignored, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All three candidate rows were read completely with TSV headers or JSON decoding.
- Separate marker scanning across those roots found no JF766688 row. Ignored-inclusive content and filename searches under `reports` and `history`, including the marker, found no prior target report or separate target history artifact before this report.
- Live NCBI Taxonomy EFetch/Datasets, exact nonexpanded Assembly/Nuccore searches, full sequence metadata, and three PubMed queries completed. Exact-name, marker, strain/topic, and specific article searches were run. The primary RSC article was inspected; its supplement could not be retrieved and was not accepted as inspected evidence.
- Not checked: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused checks do not establish corpus reproduction.
- iModulonDB and curator-added graph ID/label checks are inapplicable because the record makes no gene, regulator, protein, phenotype, transcriptomic, or graph assertion. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

Live NCBI Taxonomy EFetch and Datasets agree on ID 1034637, exact
label, species rank, parent 196821, Bacteria division, and code 11.
The full root-first lineage matches:
`1 > 131567 > 2 > 3379134 > 1224 > 1236 > 72274 > 135621 > 286 > 196821`.
Its ten labeled ancestors are root, cellular organisms, Bacteria,
Pseudomonadati, Pseudomonadota, Gammaproteobacteria,
Pseudomonadales, Pseudomonadaceae, Pseudomonas, and unclassified
Pseudomonas. Normalized ranks also agree.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034637);
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034637).

The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31062`.
No synonyms, retirement target, or direct children occur in the
backbone. Exact type-material, merged-ID, and dropped-record checks
found no target row. Provisional species rank does not establish
valid nomenclatural publication; `EXACT` does not assert genomic
species equivalence or identity with other BIHB isolates.

## Evidence

The sole NCBITAXON attestation matches the native ID and label,
count 1, unit `NAME`, and snapshot 2026-09-13. A name assertion
is not a strain or genome count. The scope row and the
2026-09-13T17:54:04Z `seed_from_sources` /
`SEEDED_FROM_SOURCES` event agree exactly.

The query `txid1034637[Organism:noexp]` returned zero Assembly
items with missing-phrase/no-items diagnostics and one Nuccore
item, UID 333496466. The complete metadata identifies
`JF766688.1`, a 1,485-base partial 16S rRNA sequence. Source
features explicitly connect BIHB 1310 to taxon 1034637 and record
rhizosphere, host pea, and country India. Those are submitted
provenance, not measured phenotypes, precise coordinates, deposit
identifiers, or a genome.
[GenBank JF766688.1](https://www.ncbi.nlm.nih.gov/nuccore/JF766688.1).

Gulati A., Rahi P., and Sharma N. directly submitted the sequence
on 1 April 2011. Its associated pea-rhizosphere phosphate-solubilizing
genotypes study is marked unpublished in the inspected sequence
record. A title alone does not establish this isolate's functional
results, and the submitter's institutional address is not its
sampling location.

PubMed searches for `JF766688[All Fields]`,
`"BIHB 1310"[All Fields] AND Pseudomonas[All Fields]`, and the
full sequence-reference title returned zero items. Query translations
and diagnostics were inspected. This bounded result is not proof
that no publication mentions the marker.

The inspected 2016 RSC article by Sathiyanarayanan and colleagues,
DOI 10.1039/C6RA17450G, explicitly studies Arctic isolate
AS-06/29, deposited as PAMC 28620, with marker KT445272.
Its methods and identification results distinguish that study isolate
from its comparison sequences. Its EPS production, metal-removal,
and temperature results therefore cannot be assigned to BIHB 1310.
[RSC primary article](https://pubs.rsc.org/en/content/articlehtml/2016/ra/c6ra17450g).

An indexed exact-name/accession hit points to the article's
supplement, but retrieval failed. The purported BIHB 1310 comparison
placement remains unverified here; search snippets are not source
evidence. No functional claim is accepted from that lead.

## Completeness

No exact target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or
BacTraits row was found in the seven parsed inventories. The wider
native search found only backbone, scope, and NCBI name rows, not
an exact deposit, assembly, type-material, or GTDB mapping.
`strain_count: 0` is inventory coverage, not a denial that the
GenBank isolate exists. Empty optional nomenclature, synonyms,
mappings, strains, traits, and graphs are appropriate here.

The exact marker and its explicit submitted source qualifiers are
optional enrichment leads under the local checklist. No missing
required representation was demonstrated. Target-specific assay
results, eventual publication of the submitted study, and the
inaccessible supplement remain unresolved; the YAML's existing
taxonomy assertions do not depend on them.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record. This is a focused assessment,
not a full-corpus reproduction result or endorsement of uninspected
experimental claims.

## Recommended Edits

No required edit is demonstrated. Preserve generated values and
`SEEDED` status.

Separately authorized sequence enrichment should define and test
the exact `taxon:1034637` / BIHB 1310 / `JF766688.1`
relationship in maintained extraction inputs and logic
(`scripts/extract_source_inventory.py`, `src/taxonmech/extract.py`),
with `scripts/seed_from_sources.py` adjusted only if needed.
`curation/seed_scope.tsv` owns scope, not inferred isolate identity.
Do not directly patch generated YAML/pages, label a marker as a
genome, or transfer PAMC 28620's traits to this taxon.

## Follow-up Checks

For optional enrichment, re-read the versioned source features,
retain host/country/source as submitted provenance, and test that
PAMC 28620 and other BIHB strains remain excluded. Regenerate by
the maintained pipeline, then rerun focused schema and strict checks.

Resolve the RSC supplement only if pursuing its comparison lead;
even a confirmed phylogenetic reference does not prove experimental
identity. Functional enrichment needs inspected primary results and
an exact target bridge. Before publishing regenerated products, run
the documented corpus reproduction, QC, tests, strict validation,
provenance, history, and site gates.

## Additional Notes

The indexed RSC supplement URL returned 404 through both web and
direct-download tools; the publications-host variant returned 403.
The main article was readable. No statement about a specific
supplementary figure or its topology is presented as verified.

All three native candidates were inspected. Search misses include
ignored files within the stated roots and remain bounded to those
sources and queries, not global absence claims. No paid research,
outbound contact, GitHub mutation, record/inventory/scope/history
edit, status promotion, regeneration, or Eukaryota review occurred.
