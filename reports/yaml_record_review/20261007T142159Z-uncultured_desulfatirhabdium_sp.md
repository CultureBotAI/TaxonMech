# YAML Record Review: uncultured Desulfatirhabdium sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_desulfatirhabdium_sp.yaml`
- Started UTC: 2026-10-07T14:18:25Z
- Finished UTC: 2026-10-07T14:21:59Z
- Verdict: pass with minor issues

## Target

The entire generated `TaxonRecord` for `NCBITaxon:1035937`,
uncultured Desulfatirhabdium sp., was read. It is a species-rank
environmental NCBI node in BACTERIA, with `EXACT` grounding,
`SEEDED` lifecycle, code 11, 10 root-first ancestors, two GTDB
`skos:broadMatch` mappings, zero inventoried BacDive strains,
NCBITAXON and GTDB attestations, and one inline seed event.
It asserts no synonyms, nomenclature, xrefs, strain/genome
objects, literature citations, phenotypes, or graph.
All seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/uncultured_desulfatirhabdium_sp.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/uncultured_desulfatirhabdium_sp.yaml --out /private/tmp/unc-desulfat-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed identity, lineage, synonym, NCBITAXON attestation, path/scope, and seed-wording checks passed. GTDB mappings, counts, ordering, and attestation were separately compared with complete raw/native rows and seeder/schema semantics.
- Live NCBI EFetch/Datasets and complete Assembly ESummary objects for all three exact-taxid assemblies were inspected.
- `just validate-products`: not applicable; there is no curator-added causal graph. Taxon labels were checked at NCBI; source-native GTDB metadata supports the pinned mapping IDs.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Live GTDB tree pages were unavailable through the web tool. Original GTDB KGX nodes/edges were not present at the exact configured upstream paths; direct filesystem checks bypassed gitignore. Upstream extraction was not reproduced.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite. Bounded checks are not corpus-wide acceptance.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035937&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035937)
confirm the active ID, exact label, species rank, parent
`NCBITaxon:1035936` (environmental samples), genetic code 11,
and bacterial lineage. EFetch's Environmental samples division
does not contradict the Bacteria domain in its lineage.
Species rank here does not establish one isolated biological species.

All 10 ancestor labels/ranks/links match the pinned backbone,
including Thermodesulfobacteriota, Desulfobacteria,
Desulfobacterales, Desulfatirhabdiaceae, and Desulfatirhabdium.
Datasets supplies root and EFetch the rest of the labeled chain.
GTDB's Desulfobacterota phylum label is retained as source context,
not silently substituted into the NCBI lineage.

Complete rows agree at `data/raw/ncbitaxon_taxa.tsv:222220`,
`data/catalog/ncbi_names-0005.jsonl.gz:31728`,
`data/taxa/PATHS.tsv:14718`, and
`curation/seed_scope.tsv:66008`.
Synonym columns and `retired_into` are empty; the snapshot
is 2026-09-13. Parsed backbone/status inventories contain no
target child, type-material, merged-ID, or dropped row.

## Evidence

Raw GTDB species rows 54943 and 54944 report two genomes for
`GTDB:s__Desulfatirhabdium_sp040755275` and one for
`GTDB:s__Desulfatirhabdium_sp964549995`.
Raw mapping rows 1447 and 1448 map these to the target by
`skos:broadMatch`; row 173683 also maps the first species to
`NCBITaxon:2202153`. Complete native metadata confirms:

| GTDB species | Assembly | NCBI taxid | Representative |
| --- | --- | --- | --- |
| sp040755275 | GCA_040755275.1, MAG156 | 2202153 | yes |
| sp040755275 | GCA_964646175.1, binchicken_co135_181 | 1035937 | no |
| sp964549995 | GCA_964549995.1, binchicken_co135_1 | 1035937 | yes |

The full metadata rows are in
`data/catalog/gtdb_genomes-0002.jsonl.gz:21504`,
`data/catalog/gtdb_genomes-0001.jsonl.gz:34914`, and
`data/catalog/gtdb_genomes-0002.jsonl.gz:39552`.
The two counts describe complete GTDB species pools, not counts
restricted to assemblies bearing NCBI taxid 1035937.
`TaxonomyMapping.genome_count` explicitly has this source-taxon
scope. `extract.py:751` copies the source species total.

Both broad mappings are defensible as the repository's documented
pooling signal: this NCBI node spans genomes assigned to multiple
GTDB species. They are not exact equivalence and do not become
xrefs or synonyms. The first species has the larger count, so
the seeder selects it for the GTDB attestation, which correctly
reports two `GENOME` records and points to the additional pool.
NCBITAXON counts one `NAME`; units are not added.
The second mapping's explanatory note overstates the mapping
cardinality, as detailed under Findings.

[Exact-taxid NCBI assemblies](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=assembly&id=26325311,26294151,26197131&retmode=json)
number three, all scaffold-level metagenome-derived submissions
under `PRJEB82487`:

| Assembly | Isolate | BioSample | Contigs / scaffolds |
| --- | --- | --- | --- |
| GCA_964444655.1 | SRP272421_co1_689 | SAMEA117374202 | 1514 / 1056 |
| GCA_964549995.1 | binchicken_co135_1 | SAMEA117392849 | 270 / 265 |
| GCA_964646175.1 | binchicken_co135_181 | SAMEA117382973 | 675 / 572 |

Full current Assembly objects agree with complete local GenBank
rows at `ncbi_genbank-0063.jsonl.gz:19015`, `:29511`,
and `:39094`. The first is flagged as fragmented and has an
inconclusive taxonomy check; the second has a RefSeq annotation
failure and an OK taxonomy check; the third has an inconclusive
taxonomy check. None supplies a RefSeq accession or type-material
claim. Their availability is not evidence for a cultured strain.

BV-BRC `1035937.3`, `1035937.4`, and `1035937.5` have
matching isolate, BioSample, project, and WGS prefixes
`CAYUIP`, `CAZJXF`, and `CAZYCZ`, respectively.
The complete local BV-BRC rows omit an assembly accession.
Assembly associations here are corroborated by NCBI metadata,
not inferred solely from a shared BioSample.

The first NCBI assembly was not found in the bounded native GTDB
catalog search. Thus the three NCBI assemblies and three genomes
across the two GTDB pools are different sets: the GTDB total
includes MAG156 under another NCBI taxid. No equality is inferred
from their coincidentally equal counts.

Exact Nuccore search enumerated 67 IDs. Their individual metadata
and cited literature were not audited; the YAML asserts none of
those accessions or claims. This review does not claim exhaustive
sequence-level or literature characterization of the catch-all node.

Raw BacDive, LPSN, GOLD, MediaDive, Madin, and BactoTraits exact-target
scans found no applicable rows. No descendants contribute BacDive
strains. The seed wording agrees with the inventories and scope;
`2026-09-13T17:54:04Z` matches the latest inspected raw/ATB/StrainInfo
manifest extraction timestamp under `_seed_timestamp`.

## Completeness

Complete enough for an NCBI identity record with qualified GTDB
pooling context, apart from the minor wording finding.
`strain_count: 0` counts inventoried BacDive strains, not MAGs
or nucleotide entries. The inspected genomes lack explicit
culture-deposit links; creating cultured `StrainEntry` objects
or type-strain claims would not be justified.

Ignored-independent searches used
`rg --no-ignore --hidden -n -z -i` over `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
Ignored, hidden, and compressed content was included.
Patterns covered taxid, label/slug, both GTDB species, and then
the discovered assemblies, samples, WGS prefixes, and bounded
isolate identifiers. Initial search returned 43 rows; final
qualified expansion returned 45. Every one of these 45 rows
was read completely, including nested source objects.

An intermediate unbounded isolate-prefix search returned 99
addresses because binchicken_co135_1 also matched longer numbers.
Those extra prefix matches were not fully inspected or used as
evidence. The final boundary-qualified search replaced it for
all completeness conclusions.

Nineteen final rows are the target identity/scope, GTDB species
and mappings, and relevant genome context including MAG156.
The other 26 are numeric collisions: 24 Salmonella rows match
BioSamples `SAMN10359370` through `SAMN10359377`;
two Alcaligenes nematophilus EBU-23 rows match `PRJNA1035937`
and describe `GCA_034258645.1`, taxid 2994643.

Five native `SOURCE.json` files were parsed completely, and
history filenames were independently searched. No applicable
culture deposit, standalone target history, or extra source
attestation was found within these bounded roots.
No global absence claim is made.

iModulonDB is not applicable: no expression module, regulator,
transcriptomic dataset, or mechanistic gene claim is asserted.
MAG existence does not supply such a dataset.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

1. **Minor: generated pooled-mapping note overstates cross-NCBI membership.**
   At YAML line 52, the sp964549995 note says the GTDB species
   also maps to other NCBI taxa. The full raw mapping scan has
   only its row to 1035937, and its sole native genome carries
   that taxid. The source supports this NCBI node spanning two
   GTDB species, not this particular GTDB species spanning
   multiple NCBI nodes. The first species does span two NCBI
   nodes, so the identical note happens to fit that first entry.
   This is a non-blocking explanatory-text defect; identifiers,
   predicates, counts, and qualified identity remain supported.
   Maintained owner: `src/taxonmech/seed.py:462`.
   Regression coverage belongs in `tests/test_seed.py`,
   whose current pooled-note assertion checks only the word Pooled.

## Recommended Edits

1. Correct the seeder's generic broadMatch note to describe
   pooling without asserting unverified reverse cardinality.
   For example: this NCBI taxon contains genomes assigned to
   multiple GTDB species; the mapping is not an equivalence.
   If other-NCBI membership is stated, derive it from explicit
   mapping membership rather than the broadMatch predicate alone.
2. Add a seeder regression case with two GTDB species mapping to
   one NCBI node, where one species has no other NCBI mapping.
   Retain the existing primary-pool count and no-xref/no-synonym
   behavior. Do not change correct counts to taxid-restricted
   numbers or sum the two pools.
3. Regenerate through the normal maintained-input workflow after
   authorized implementation. Do not hand-edit YAML or pages.
   Keep `mapping_status: SEEDED`; this review does not authorize
   a status promotion or history event.

No identity, strain-count, or scope change is recommended.
If future source mappings themselves change, their owner is the
kg-microbe transform plus `src/taxonmech/extract.py`.

## Follow-up Checks

Run the focused seeder tests after the wording change, then
regenerate and run schema, strict, `just verify-corpus`,
provenance, and QC gates. Verify that sp964549995 no longer
claims another NCBI mapping, both predicates remain broadMatch,
the primary attestation stays two genomes, and neither mapping
becomes an exact synonym or xref.

For an external refresh, recheck both live GTDB species and
the original KGX mapping edges when available. Preserve the
distinction between source-wide GTDB counts, target-taxid
assemblies, MAG labels, and culture-deposit identity.

## Additional Notes

- Baseline: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`.
- The complete YAML was reread byte-identical before report creation.
- Configuration is `conf/sources.yaml`; an initial lookup under config was corrected using ignored-independent filename discovery.
- Only this new report is written; no YAML, source, history, generated product, GitHub object, branch, or worktree is changed.
- Eukaryota remains fully covered and was not re-reviewed.
