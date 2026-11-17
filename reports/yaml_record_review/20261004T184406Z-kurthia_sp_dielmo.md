# YAML Record Review: Kurthia sp. Dielmo

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/kurthia_sp_dielmo.yaml`
- Started UTC: 2026-10-04T18:37:39Z
- Finished UTC: 2026-10-04T18:44:06Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1033738`, label
`Kurthia sp. Dielmo`, rank `SPECIES`, domain `BACTERIA`. Its grounding is
`EXACT`, mapping status is `SEEDED`, and its one seed event is dated
2026-09-13T17:54:04Z. This is a species-level NCBI concept despite its
isolate-like label, not a separately ranked strain record.

The maintained inputs are `data/raw/`, `curation/seed_scope.tsv` and the
path lockfile; `src/taxonmech/seed.py` owns their projection. The reviewed
YAML, context records, inventories, status and history were not edited.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/kurthia_sp_dielmo.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/kurthia_sp_dielmo.yaml`: exit 0, one file, zero errors. The validator writes its normal diagnostic TSV under `reports/`.
- Structured read-only comparisons verified the identity, all ten root-first lineage entries, code 11, path lock, scope reason, source counts and seed-event wording against the inventories. These are source comparisons, not a substitute for the reproduction gate.
- `just verify-corpus` was skipped: its implementation rebuilds the full corpus and has no target-record selector; `--max-diffs` only limits printed differences. No focused reproduction validator was invented.
- `just validate-products` was not run: the record has no curator-grounded graph nodes. Its configured OAK targets do not validate these NCBI identity or lineage fields; those were checked directly instead.
- No target-specific external history artifact was found in the bounded, ignored-inclusive searches. No history was added, and full-history validation was skipped. Full `just qc`, corpus tests, provenance hashing, render checks and all-record schema validation were not run for this read-only review.

## Identity and Grounding

Current [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033738&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033738)
confirm the name, species rank, parent `NCBITaxon:2644826` (unclassified
Kurthia), bacterial placement and lineage. EFetch confirms genetic code 11
and supplies no alternate names. The pinned backbone agrees at
`data/raw/ncbitaxon_taxa.tsv:221303`; its subtree scan found no children.
Exact-value scans of the complete type-material, merged-ID and dropped
tables found no row for this identifier.

The source-specific GTDB assignment is defensible. The full pinned genome
catalog scan found 16 unique members of `s__Kurthia populi`, including
`RS_GCF_000307285.2` classified by NCBI as this target, and the representative
`RS_GCF_042686175.1`, the KCTC 33522 type-strain genome of Kurthia populi.
`data/raw/gtdb_mappings.tsv:1365` supplies the recorded `skos:closeMatch`.
The GTDB-labelled synonym and xref retain that source attribution; they do
not change the NCBI identifier or assert that NCBI has formally renamed it.

[LPSN Kurthia populi](https://lpsn.dsmz.de/species/kurthia-populi), record
793489, identifies the validly published correct name and type strain
10y-14 = CFCC 11600 = KCTC 33522. The local LPSN row maps that name to
`NCBITaxon:1562132`, not this target. Its nomenclature and type designation
must not be copied here merely because GTDB groups the genomes together.

## Evidence

- **NCBI attestation:** one `NAME`, matching the 2026-09-13 backbone snapshot and its source identifier. `data/raw/MANIFEST.yaml` pins the taxonomy dump and the kg-microbe extraction.
- **GTDB attestation:** 16 `GENOME` assertions, matching the mapping, species inventory and complete native cluster. This is the source cluster's size, not 16 Dielmo genomes. Native NCBI classifications comprise one target genome, one Kurthia populi genome, eight Candidatus Kurthia intestinigallinarum genomes, four individually named UBA taxa, one Caryophanaceae bacterium and one uncultured Kurthia sp. The different NCBI placements remain source context.
- **Madin attestation:** `data/raw/madin_taxa.tsv:627` supports one `TRAIT_ASSERTION`. No phenotype value is asserted by this YAML, and the count is not promoted into experimental evidence.
- **Dielmo assembly context:** [NCBI Datasets GCA_000307285.2](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000307285.2/dataset_report) confirms the current scaffold assembly, paired `GCF_000307285.2`, sample `SAMEA2272405` and project `PRJEA70549`. Current and historical native assembly objects were read. Versions `.1` are suppressed, whereas `.2` is current; an unversioned BacDive accession must remain unversioned.
- **Culture classification conflict:** [BacDive 160806](https://bacdive.dsmz.de/strain/160806) identifies Dielmo / DSM 24643 but classifies the culture under `NCBITaxon:1963358` (Kurthia sp.). Its sequence assertion, reference 66792, instead carries target taxon 1033738, `GCA_000307285`, IMG 2548876794 and BV-BRC 1033738.3. The full pinned BacDive object explicitly has `type strain: no`. This is a strain-classification versus genome-metadata distinction, not evidence that the taxon identifiers are interchangeable.
- **Deposit corroboration:** [DSMZ DSM 24643](https://www.dsmz.de/collection/catalogue/details/culture/DSM-24643) confirms designation Dielmo and its human-stool origin in Senegal. Native StrainInfo record `data/straininfo/records.jsonl.gz:299107` links SI-ID 401218, SI-DP 908134 and DOI `10.60712/SI-ID401218.2` to that own deposit, classifies it only at genus Kurthia, and sets `typeStrain` false. It provides no sequence object to transfer to this target.

## Completeness

`strain_count: 0` is correct under the documented BacDive-subtree rule.
The Dielmo culture is already preserved, with its three BacDive genome
assertions and StrainInfo identifiers, on
`data/taxa/bacteria/kurthia_sp.yaml`. That sibling is not a descendant of
the target. Its complete contents were read as context, not reviewed as a
second target. Genome metadata cannot override its BacDive classification.

The native BV-BRC record 1033738.3 links the historical `.1` assembly and
sample but has no culture-collection identifier. GOLD's explicit chain is
Go0017279 -> Gp0017279 -> Ga0020298, with that same sample, historical
assembly and IMG accession; its organism culture-collection field is also
empty. GTDB supplies bare `Dielmo`, and NCBI supplies a strain-description
string rather than DSM 24643. These are not eligible whole-deposit joins
under the repository's matching rules. No extra strain links are required
from those records.

Ignored-inclusive, compressed-content searches covered `data/raw`,
`data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`, using the target ID
and name, GTDB name, then DSM 24643, BacDive 160806, SI-ID/SI-DP values and
the complete BioSample accession. Numeric collisions were inspected and
excluded. No matching ATB row surfaced within those searched artifacts;
this is not a claim about every remote assembly or an unsearched external
cache. Exact direct inventory joins found no BacDive, LPSN, GOLD, MediaDive
or BactoTraits taxon-level attestation for this target. Native GOLD context
does not by itself require a KGX-derived GOLD attestation.

Optional record-level evidence, graphs, discussions and nomenclature may
remain empty. The three source attestations provide the seeded provenance.
The seed status and event correctly remain unchanged by this review.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record. Source-classification differences and
historical accession versions are preserved as context rather than treated
as errors or silently reconciled. This verdict does not certify whole-corpus
reproduction or resolve formal taxonomic synonymy.

## Recommended Edits

None required. Do not manually add DSM 24643, transplant LPSN nomenclature,
rename the record, infer a type-strain flag, or append assembly versions.
If an authority later revises a classification, its upstream source and
inventory extraction own the correction; any projection change belongs in
`src/taxonmech/seed.py` with a regression test, followed by documented
regeneration rather than editing generated YAML.

## Follow-up Checks

- On a source refresh, recheck NCBI taxon 1033738, BacDive 160806's general classification and sequence taxon separately, and DSM 24643 / SI-DP 908134.
- Preserve current versus suppressed assembly versions, source-cluster versus target-specific genome counts, and type-strain evidence boundaries.
- For any future curation change, rerun both target validators, then the documented full `just verify-corpus` and applicable `just qc` gates. Do not label these skipped gates as passed.

## Additional Notes

The GTDB taxon page and live StrainInfo page were inaccessible through the
web reader. Their pinned native records were inspected instead; GTDB
release RS232 is identified in `data/catalog/MANIFEST.json`. The full GTDB
scan covered 901,341 rows and all 16 objects in the relevant cluster.

Current NCBI ANI metadata reports a genus-level match and a best hit to
GCA_019114605.1, Candidatus Kurthia intestinigallinarum, at 98.72% ANI with
66.83% assembly coverage. That genome is also in the inspected GTDB cluster.
This contextual result neither supplies a formal rename nor overrides
NCBI's retained species concept. The assembly's text containing `type
strain: Dielmo` is not a nomenclatural type-material assertion.

iModulonDB was not applicable: this record has no gene, regulator, pathway,
stress-response or expression-module claim. No paid research, external
contact, GitHub mutation, new curation event, or status promotion occurred.
