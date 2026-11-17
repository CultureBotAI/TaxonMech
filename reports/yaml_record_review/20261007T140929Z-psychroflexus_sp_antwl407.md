# YAML Record Review: Psychroflexus sp. antwl407

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/psychroflexus_sp_antwl407.yaml`
- Started UTC: 2026-10-07T14:05:08Z
- Finished UTC: 2026-10-07T14:09:29Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` for `NCBITaxon:1035917` was read.
Psychroflexus sp. antwl407 is a species-rank bacterial node with
`EXACT` identity, `SEEDED` lifecycle, genetic code 11, 12 root-first
ancestors, zero inventoried BacDive strains, one NCBITAXON name
attestation, and one inline seed event. It asserts no synonyms,
nomenclature, taxonomy mappings, strain/genome objects, citations,
phenotypes, or graph. Seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/psychroflexus_sp_antwl407.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/psychroflexus_sp_antwl407.yaml --out /private/tmp/psy-antwl407-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed source comparisons passed for identity, every ancestor label/rank/link, synonyms, attestation, path/scope uniqueness, and seed-event wording. They do not replace corpus reproduction.
- Live NCBI taxonomy EFetch/Datasets and all metadata/features/references for the sole exact-taxid Nuccore hit were inspected.
- `just validate-products`: not applicable; no curator-added causal graph grounding/label pairs. Taxon identifiers were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite. No corpus-wide acceptance claim is made.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035917&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035917)
agree on the active ID, exact lowercase antwl407 label, species
rank, parent `NCBITaxon:196864` (unclassified Psychroflexus),
bacterial placement, genetic code, and lineage.

All 12 local ancestors match the pinned backbone, including
Pseudomonadati, FCB group, Bacteroidota/Chlorobiota group,
Bacteroidota, Flavobacteriia, Flavobacteriales, Flavobacteriaceae,
and Psychroflexus. Datasets supplies root; EFetch supplies the
remaining labeled chain. A strain-like suffix does not change
the rank assigned to this NCBI node.

Full source rows agree at `data/raw/ncbitaxon_taxa.tsv:222216`,
`data/catalog/ncbi_names-0005.jsonl.gz:31724`,
`data/taxa/PATHS.tsv:14715`, and
`curation/seed_scope.tsv:322475`. Synonym columns and
`retired_into` are empty. The snapshot is 2026-09-13.
Parsed backbone/status inventories contain no target child,
type-material, merged-ID, or dropped row.

## Evidence

The NCBITAXON attestation counts one `NAME`, not one genome or
culture deposit. Exact-target scans of raw BacDive, LPSN, GTDB,
GOLD, MediaDive, Madin, and BactoTraits found no applicable rows.
With no backbone descendants, zero inventoried BacDive strains
agrees with the inputs.

The seed wording matches the parsed scope/inventories.
The event timestamp `2026-09-13T17:54:04Z` matches the newest
extraction timestamp across the actual YAML manifests in
`data/raw/`, `data/atb/`, and `data/straininfo/`,
as specified by `src/taxonmech/seed.py::_seed_timestamp`.

Exact Assembly search `txid1035917[Organism:noexp]` returned
zero with phrase-not-found/no-items warnings. This is a bounded
index result, not proof of global genome absence. Exact Nuccore
search returned UID 334690414; its entire metadata, feature,
and reference structure was read, excluding sequence payloads.

[JF811035.1](https://www.ncbi.nlm.nih.gov/nuccore/JF811035.1)
is a 1,394-nt partial 16S rRNA gene annotated with strain antwl407,
`taxon:1035917`, and isolation source sea ice. This is
isolate-scoped submission metadata, not a whole-genome assembly,
culture-deposit link, taxon-wide habitat assertion, or measured
cold-adaptation phenotype. No geographic qualifier is supplied.
The references list an unpublished S. Xiong study and a
14-April-2011 direct submission from Zhejiang Wanli University.

A similarly titled [2005 Greenland study](https://pubmed.ncbi.nlm.nih.gov/16332755/)
has different authors, locality, and publication date; its
bibliographic metadata and abstract were inspected. It is not
substituted for Xiong's unpublished Antarctic submission.

Other exact-name/accession web results were discovery leads only.
A CiteSeer PDF fetch returned HTTP 403; direct access to a
[Psychroflexus torquis study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3914696/)
returned a browser challenge. Their figures and full source
context were not verified, and no identity, genome, or phenotype
claim is transferred from those search excerpts. The YAML
asserts no literature claim requiring either optional source.

## Completeness

Complete enough for an NCBI-only generated identity record.
Optional fields are appropriately empty without applicable
supported objects. `strain_count: 0` describes the BacDive
inventory, not every isolate ever sequenced.

Initial and accession-expanded searches used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
Ignored, hidden, and compressed content was included.
Patterns covered taxid, exact label/slug, antwl407, and JF811035.
Both searches returned the same 16 candidate rows, all read
completely, including nested native objects.

Three rows describe the target backbone, scope, and scientific
name. Twelve others describe Campylobacter jejuni samples
`SAMN10359177`, `SAMN10359178`, and `SAMN10359179`:
numeric BioSample substrings in GOLD projects, BV-BRC, GenBank,
and AllTheBacteria are not Psychroflexus evidence.
The remaining GenBank row at
`data/catalog/ncbi_genbank-0066.jsonl.gz:47195` describes
uncultured bacterium `GCA_983742175.1`, taxid 77133;
its ungapped genome size happens to be 1035917.

Five native `SOURCE.json` files were parsed completely;
history filenames were searched independently.
No additional applicable source assertion, deposit,
strain-genome link, or standalone history artifact was found
within these bounded local sources. Global absence is not claimed.

iModulonDB is not applicable: there is no regulatory,
transcriptomic, or mechanistic gene claim. An optional 16S marker
does not identify an expression dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, count units, optional omissions,
and seed provenance are supported.

## Recommended Edits

None required. Keep generated YAML and `mapping_status: SEEDED`
unchanged; a read-only review does not authorize an audit event
or human-review status.

Future source corrections belong to maintained upstream inputs
and `src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope corrections belong to `curation/seed_scope.tsv`.
Optional enrichment needs authoritative strain/deposit/assembly
links, not a marker match or another Psychroflexus species' biology.

## Follow-up Checks

No corrective follow-up is required. Before optional literature
enrichment, obtain full primary source context and establish the
exact isolate link. Preserve unpublished-submission status and
distinguish sea-ice metadata from experimentally demonstrated traits.

After future authorized input changes, rerun appropriate
extraction/seeding, schema, strict, reproduction, provenance,
and QC gates. Validate products/history if introduced.

## Additional Notes

- Baseline: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`.
- The complete YAML was reread byte-identical before report creation.
- An initial manifest lookup used the wrong JSON extension; ignored-independent filename discovery found the actual YAML manifests, which were then checked. This was a lookup error, not missing provenance.
- Only this new report is created. No YAML, history, generated product, GitHub object, branch, or worktree is changed.
- Eukaryota is already fully covered and was not re-reviewed.
