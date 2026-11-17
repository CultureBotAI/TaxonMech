# YAML Record Review: Haloplasma contractile SSD-17B

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/haloplasma_contractile_ssd_17b.yaml`
- Started UTC: 2026-10-04T19:17:10Z
- Finished UTC: 2026-10-04T19:18:41Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1033810`, rank
`STRAIN`, domain `BACTERIA`, parent species `NCBITaxon:471825`. It has
`EXACT` grounding, `SEEDED` mapping status, ten root-first ancestors,
genetic code 11, one GTDB mapping, three exact synonyms, one GTDB xref,
zero inventoried BacDive strains and three source attestations. Its seed
event is dated 2026-09-13T17:54:04Z.

The parent species YAML was read in full for source/classification context,
not given a second review verdict. Source extraction, scope/path inputs
and `src/taxonmech/seed.py` own future fixes; neither generated record
was edited.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/haloplasma_contractile_ssd_17b.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/haloplasma_contractile_ssd_17b.yaml`: exit 0, one file, zero errors; normal diagnostic TSV under `reports/`.
- Bounded structured checks compared identity, all ancestors, synonyms, direct source inventories, path lock, scope and seed-event wording. These checks are not a focused corpus reproduction gate.
- `just verify-corpus` was skipped because it rebuilds the full corpus without a target-record selector; `--max-diffs` limits diagnostics only.
- `just validate-products` was not applicable: no curator-grounded graph nodes are present. NCBI identity was checked directly.
- Ignored-inclusive searches found no separate target history artifact. Full-history validation, full `just qc`, corpus tests, all-record validation, provenance hashing and rendering checks were skipped. No history or status was changed.

## Identity and Grounding

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033810&retmode=xml)
confirms the identifier, exact label, strain rank, species parent,
bacterial division, genetic code 11 and both equivalent names:
`Haloplasma contractile str. SSD-17B` and
`Haloplasma contractile strain SSD-17B`.
[Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033810)
corroborates the complete ancestor ID chain including root. These agree
with backbone row `data/raw/ncbitaxon_taxa.tsv:221312` and all ten emitted
ancestor IDs, labels and ranks. The full native names at
`data/catalog/ncbi_names-0005.jsonl.gz:30642`, line 30643 and line 30644
support the scientific name and the two exact NCBI synonyms.

Genetic code 11 is explicitly supported; it must not be replaced by a
code inferred from membership in Mollicutes. GTDB's Bacillota_I /
Bacilli_A placement differs from NCBI's Mycoplasmatota / Mollicutes
placement. The repository carries the NCBI lineage and does not reconcile
these classifications. Complete relevant inventories contain no child,
direct type-material, merged-ID or dropped-ID row for the strain taxon.

The NCBI identity and `EXACT` grounding are sound. The unsupported identity
claim is the additional equivalence to the whole GTDB species.

## Evidence

| Emitted assertion | Inspected support and scope |
|---|---|
| NCBI name attestation, count 1 | Full backbone/native names and public taxonomy APIs agree; snapshot date 2026-09-13. This is not a culture or assembly count. |
| GTDB mapping and attestation, count 1 | `data/raw/gtdb_mappings.tsv:1374` and `data/raw/gtdb_species.tsv:73147` reproduce the predicate and whole species-cluster count. |
| Madin trait-assertion attestation, count 2 | `data/raw/madin_taxa.tsv:634` supplies this taxon/count. No individual phenotype or experimental condition is asserted. |
| Scope and seed event | `data/taxa/PATHS.tsv:13767` fixes the slug. `curation/seed_scope.tsv:36152` supplies the three-source inclusion reason reproduced by the seed event. |

The complete scan of 901,341 GTDB genome objects found exactly one unique
member of `s__Haloplasma contractile`: `RS_GCF_000215935.2`. Its full
native object at `data/catalog/gtdb_genomes-0006.jsonl.gz:13606` identifies
SSD-17B, NCBI strain taxon 1033810, NCBI species taxon 471825,
`GCA_000215935.3`, `SAMN02472186`, translation table 11 and type-material
status. It is the representative genome.

The singleton cluster supports species membership and a count of one.
It does not make a species identifier equivalent to an individual strain
identifier. No second genome or second mapped NCBI taxon was found in this
cluster, and no such conflict is asserted here.

A separate native hit, `GB_GCA_016841945.1` at
`data/catalog/gtdb_genomes-0000.jsonl.gz:17979`, is a metagenome-derived
B5_bin.1 assembly classified by NCBI under species 471825 but by GTDB
under `s__JAENYC01 sp016841945`. That full object was inspected and
excluded from the target cluster count. Its presence under the NCBI
species is not evidence for a second SSD-17B genome or for identity to
SSD-17B. The parent species' separate mapping requires its own review.

[NCBI Datasets assembly](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000215935.3/dataset_report)
confirms current `GCA_000215935.3` paired with current
`GCF_000215935.2`, contig-level HLPCO_V2, taxon 1033810, type-material
status, `SAMN02472186` and `PRJNA66977`. The BioSample explicitly names
DSM 18853. Full native current objects at
`data/catalog/ncbi_genbank-0000.jsonl.gz:3580` and
`data/catalog/ncbi_refseq-0000.jsonl.gz:3090` agree. The different
GenBank/RefSeq version suffixes are the supported pairing, not an error.

The exact-taxonomy Assembly query returned three entries, all inspected:
the current paired assembly, suppressed `GCA_000215935.1`, and replaced
`GCA_000215935.2` / `GCF_000215935.1`. Native historical objects at
`data/catalog/ncbi_genbank_historical-0000.jsonl.gz:953`, line 954 and
`data/catalog/ncbi_refseq_historical-0000.jsonl.gz:1015` corroborate these
statuses. This is not three current assemblies or three isolates.

Current status is not a genome-quality endorsement: the live report also
carries a CheckM contamination estimate of 10.95. No purity or assembly
quality claim is emitted by the target, and no new quality verdict or
taxonomic reassignment was inferred from that estimate.

## Completeness

Complete direct inventories have no target BacDive, LPSN, GOLD,
MediaDive or BactoTraits row. This is an inventory-scope statement,
not absence of SSD-17B from the native sources.

The gitignore-independent compressed-content search
(`rg --no-ignore --hidden -z`) covered the taxon ID, full species name
and SSD-17B spelling variants under `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`. It returned
58 matching lines. Numeric substrings in unrelated sample, run and
assembly identifiers were excluded; SAMEA1033810 is not this taxon's
BioSample.

Full native BacDive object `data/bacdive/records.jsonl.gz:17483` and
[BacDive 17673](https://bacdive.dsmz.de/strain/17673) identify SSD-17B,
DSM 18853 and JCM 14575, classified under parent species 471825. Sequence
metadata separately names strain taxon 1033810. The parent YAML already
retains that culture and its assembly, IMG, PATRIC, sample and project
assertions. The seeder gathers strains from the target and descendants,
not ancestors, so `strain_count: 0` on this child is consistent with
source classification. It does not mean there is no deposited culture.

[LPSN](https://lpsn.dsmz.de/species/haloplasma-contractile) supports
the species name and type designations. Pinned LPSN row
`data/raw/lpsn_names.tsv:24811` maps name 787613 to parent species
471825 and the GTDB species, not to strain taxon 1033810. A type strain
anchors a species name; that does not equate the two taxonomic ranks.

Full native GOLD objects retain the DSM 18853 chain through organism
`Go0011313` (`data/gold/organisms.jsonl.gz:9937`), project `Gp0011313`
(`data/gold/projects.jsonl.gz:9798`) and analysis `Ga0024145`
(`data/gold/analyses.jsonl.gz:15120`). The project supplies the same
sample/project, and the analysis explicitly supplies assembly/IMG IDs.
These assertions already appear on the parent's classified culture.
This native evidence is distinct from the KGX-derived GOLD
taxon-attestation inventory; an absent attestation is not absence from GOLD.

The full BV-BRC object `data/bvbrc/bvbrc-0000.jsonl.gz:3222` identifies
genome 1033810.11, the same strain/assembly/sample/project and explicit
`culture_collection: DSM:18853`. Its supported culture-linked assertions
also appear on the parent. Preserve the versioned BV-BRC assembly link
and the unversioned BacDive/GOLD `GCA_000215935` assertions independently;
do not append a version to the latter from another source.

Optional record-level citations, definitions and causal graphs can remain
empty. The target contains no DOI, PMID or verbatim evidence snippet.
Parent-species literature and source genome publications were not
audited as though they were citations asserted by this strain record.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a GTDB species is asserted as equivalent to strain SSD-17B.**
   Its species identifier appears in `xrefs`, and the strain-free
   species label appears as an exact synonym. Neither a singleton
   cluster nor representative/type-material status establishes that
   species and strain denote the same taxonomic concept. This conflicts
   with the schema's true-equivalence restriction on `xrefs`.
   `src/taxonmech/seed.py:451` treats all `skos:closeMatch` rows as identity
   without a rank check, and lines 467-469 emit both claims. The raw
   predicate and count are faithfully retained but do not justify that
   promotion. This is one scope error with two emitted manifestations.

## Recommended Edits

1. Make GTDB identity promotion rank-aware in `src/taxonmech/seed.py`.
   Do not emit a species xref or exact synonym for an infraspecific
   taxon solely from `skos:closeMatch`, even when the cluster has one
   genome. Preserve both NCBI synonyms, identity, parent, lineage and
   genetic code 11.
2. Retain source mapping and singleton count with a scope note while
   the upstream kg-microbe predicate is investigated separately. Any
   source correction belongs upstream and in maintained extraction
   (`scripts/extract_source_inventory.py` / `src/taxonmech/extract.py`),
   not a hand-edited raw row or generated YAML override.
3. Add a singleton strain/species regression in `tests/test_seed.py`,
   alongside legitimate species-level equivalence cases. A singleton
   must not bypass the rank guard. Regenerate through
   `scripts/seed_from_sources.py` only after an authorized change.

## Follow-up Checks

- After the future seeder fix, run `uv run pytest tests/test_seed.py` and both target validators. Confirm only unsupported GTDB equivalence claims change, with source mapping/count and exact NCBI names preserved.
- Compare regenerated strain and parent records without merging their distinct mapping contexts or altering existing culture/genome evidence. Run full `just verify-corpus` and applicable `just qc` gates after authorized regeneration.
- Recheck GTDB membership and assembly statuses on refresh. Keep B5_bin.1's different GTDB cluster, historical assembly versions and genome-quality metadata separate from this record's strain identity.

## Additional Notes

The GTDB taxon page was inaccessible through the web reader; full pinned
native objects and complete membership scanning supplied its evidence.
Current GTDB web membership was not verified. NCBI APIs and BacDive were
accessible. The returned LPSN page was a cached rendition printed
2026-06-04; it agrees with the pinned name/type data but was not a fresh
LPSN snapshot.

iModulonDB was not applicable: no gene, regulator, pathway or transcriptomic
assertion is present. This review does not infer phenotype, culture
availability or a reconciled higher taxonomy.

Only this new report was added apart from the validator's normal
diagnostic output. No generated record, source inventory, generator,
history, status or prior report was edited. No paid research, external
contact or GitHub mutation was performed.
