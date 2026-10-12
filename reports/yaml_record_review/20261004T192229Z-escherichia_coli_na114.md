# YAML Record Review: Escherichia coli NA114

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/escherichia_coli_na114.yaml`
- Started UTC: 2026-10-04T19:20:21Z
- Finished UTC: 2026-10-04T19:22:29Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1033813`, rank
`STRAIN`, domain `BACTERIA`, parent species `NCBITaxon:562`. It has
`EXACT` grounding, `SEEDED` mapping status, ten root-first ancestors,
genetic code 11, one GTDB mapping, three exact synonyms, one GTDB xref,
zero inventoried BacDive strains and three source attestations. Its seed
event is dated 2026-09-13T17:54:04Z.

Only NA114 is the review target. No verdict on the much broader E. coli
species record or other cluster members is implied. Maintained source
extraction, scope/path inputs and `src/taxonmech/seed.py` own future
changes; generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/escherichia_coli_na114.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/escherichia_coli_na114.yaml`: exit 0, one file, zero errors; normal diagnostic TSV under `reports/`.
- Bounded structured checks compared identity, all ten ancestors, synonyms, direct source inventories, path lock, scope and seed-event wording. These are not a focused corpus reproduction gate.
- `just verify-corpus` was skipped because it rebuilds the full corpus without a target-record selector; `--max-diffs` limits diagnostics only.
- `just validate-products` was not applicable: there are no curator-grounded graph nodes. NCBI identity was checked directly.
- Ignored-inclusive searches found no separate target history artifact. Full-history validation, full `just qc`, corpus tests, all-record validation, provenance hashing and rendering checks were skipped. No history or status was changed.

## Identity and Grounding

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033813&retmode=xml)
confirms the identifier, exact label, strain rank, species parent,
bacterial division, genetic code 11 and both equivalent names:
`Escherichia coli str. NA114` and `Escherichia coli strain NA114`.
[Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033813)
corroborates the full ancestor ID chain including root. The pinned
backbone at `data/raw/ncbitaxon_taxa.tsv:221313` and all ten emitted
ancestor IDs, labels and ranks agree.

Full native scientific/equivalent-name objects at
`data/catalog/ncbi_names-0005.jsonl.gz:30645`, line 30646 and line 30647
support the two exact NCBI synonyms. Complete relevant tables contain
no child, direct type-material, merged-ID or dropped-ID row for the
target. Its NCBI identity and `EXACT` grounding are sound; the unsupported
equivalence is the additional GTDB species identity claim.

## Evidence

| Emitted assertion | Inspected support and scope |
|---|---|
| NCBI name attestation, count 1 | Full backbone/native names and public taxonomy APIs agree; snapshot date 2026-09-13. This is not an isolate count. |
| GTDB mapping and attestation, count 36,408 | `data/raw/gtdb_mappings.tsv:1375` and `data/raw/gtdb_species.tsv:59219` supply this source-cluster volume and predicate. The number is not a count of NA114 genomes. |
| Madin trait-assertion attestation, count 5 | `data/raw/madin_taxa.tsv:635` supplies the exact taxon/count. No individual phenotype or experimental condition is asserted by this YAML. |
| Scope and seed event | `data/taxa/PATHS.tsv:13768` fixes the slug. `curation/seed_scope.tsv:36153` supplies the three-source inclusion reason reproduced by the seed event. |

A structured scan of all 901,341 native GTDB genome objects counted
36,408 distinct accessions in `s__Escherichia coli`, spanning 2,002
NCBI taxon IDs. Exactly one member has `ncbi_taxid: 1033813`; 31,765
have the parent species taxon 562 directly. The complete mapping table
contains 2,002 rows for the cluster. This verifies count and scope, not
the biological correctness of every other member's classification.

Two full native objects were inspected in detail:

- `data/catalog/gtdb_genomes-0009.jsonl.gz:29789`: `RS_GCF_000214765.2`, NA114, strain taxon 1033813, species taxon 562, `GCA_000214765.3`, `SAMN02603711`, not the representative and not marked type material.
- `data/catalog/gtdb_genomes-0015.jsonl.gz:39806`: representative `RS_GCF_003697165.2`, NCBI taxon 866789, E. coli DSM 30083 = JCM 1649 = ATCC 11775, designated neotype; this is not NA114.

The raw mapping to parent species 562 at
`data/raw/gtdb_mappings.tsv:296603` has `skos:broadMatch`, whereas the
NA114 row has `skos:closeMatch`. These are source predicates, not proof
that a whole species is identical to one of its strains. The source
count of 36,408 should not be changed to one merely to disguise the
scope mismatch.

[NCBI Datasets assembly](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000214765.3/dataset_report)
confirms current `GCA_000214765.3` paired with current
`GCF_000214765.2`, contig-level ASM21476v3, taxon 1033813,
`SAMN02603711` and `PRJNA66975`. The current assembly has 105 contigs.
Its source comment states that it replaced CP002797 at the submitter's
request following newer sequencing technology. Full native current
objects at `data/catalog/ncbi_genbank-0000.jsonl.gz:3534` and
`data/catalog/ncbi_refseq-0000.jsonl.gz:3051` agree.

The exact-taxonomy Assembly query returned three entries, all inspected:
the current pair, replaced `GCA_000214765.2` / `GCF_000214765.1`, and
replaced `GCA_000214765.1`. Native historical objects at
`data/catalog/ncbi_genbank_historical-0000.jsonl.gz:911`, line 912 and
`data/catalog/ncbi_refseq_historical-0000.jsonl.gz:999` corroborate this.
The older versions were labeled Complete Genome. That historical label
must not be transferred to the current contig assembly or treated as
three currently independent genomes.

Full native BV-BRC object `data/bvbrc/bvbrc-0000.jsonl.gz:3223` links
genome 1033813.3 to the older `GCA_000214765.2` and CP002797, with the
same sample/project. GOLD's full objects at
`data/gold/organisms.jsonl.gz:9911`,
`data/gold/projects.jsonl.gz:9775` and
`data/gold/analyses.jsonl.gz:19150` preserve organism `Go0011285`,
project `Gp0011285` and analysis `Ga0028749`. The analysis names
unversioned `GCA_000214765`, CP002797 and IMG 651053022. Those native
assertions must not be silently rewritten as the latest assembly.

## Completeness

Complete direct inventories have no target BacDive, LPSN, GOLD,
MediaDive or BactoTraits row. Native GOLD does contain NA114, as detailed
above. The separate KGX taxon-attestation inventory and native genome
catalog are different source pipelines, not contradictory absence claims.

The gitignore-independent compressed-content search
(`rg --no-ignore --hidden -z`) covered taxon 1033813, the full slug and
token-bounded NA114 under `data/raw`, `data/catalog`, `data/bacdive`,
`data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`, returning 25 matched lines. Arthrobacter sp.
NA114, a freshwater-community sample named NA114, and numeric substrings
in unrelated accessions were excluded. The earlier unrestricted NA114
substring search was too noisy and its truncated output was not used
to establish completeness; the token-bounded search completed untruncated.

A second ignored-inclusive compressed search used the exact BioSample,
assembly stems, CP002797 and WGS master stem. It found the native genome
records above and unrelated WGS-prefix substrings, but no eligible
BacDive/deposit crosswalk, StrainInfo link or ATB sample row for this
target. The full native GOLD organism has an empty culture-collection
field; BV-BRC, GTDB and the inspected NCBI BioSample give the bare NA114
designation without a registered deposit identifier.

Thus zero listed BacDive strains is consistent with the inspected
inventory and join rules, not a claim that NA114 lacks a genome or that
no laboratory holds it. Shared species identity or an isolate name
cannot create a culture-deposit match. Do not import the GTDB
representative's ATCC/JCM/DSM identifiers into NA114. Genome assertions
remain independently searchable in their native catalogs.

Optional nomenclature, record-level literature evidence, definitions and
causal graphs can remain empty. No DOI, PMID or verbatim evidence snippet
is asserted by the target. Publication identifiers in external genome
metadata were not treated as mandatory record citations or used to
infer phenotypes, mechanisms or experimental findings.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: the E. coli GTDB species is promoted to equivalence with NA114.**
   The species identifier is emitted in `xrefs`, and `Escherichia coli`
   is an exact synonym of the strain. The full cluster scan and the
   distinct representative demonstrate broader species scope; only one
   member is assigned specifically to NA114. This violates the schema's
   true-equivalence restriction on `xrefs`. At
   `src/taxonmech/seed.py:451`, every `skos:closeMatch` becomes identity
   without checking rank; lines 467-469 emit both claims. Faithful
   copying of the source predicate does not justify identity promotion.
   These are two manifestations of one scope error, not two findings.

## Recommended Edits

1. Make GTDB identity promotion rank-aware in `src/taxonmech/seed.py`.
   Do not emit a species xref or exact synonym for an infraspecific
   taxon solely from source `skos:closeMatch`. Preserve NCBI identity,
   both exact NCBI synonyms, parent, lineage and genetic code.
2. Retain the source mapping and 36,408-member source count with an
   explicit scope note. Investigate the upstream kg-microbe predicate
   separately; source corrections belong upstream and in maintained
   extraction (`scripts/extract_source_inventory.py` /
   `src/taxonmech/extract.py`), not a hand-edited raw row or YAML override.
3. Add a regression in `tests/test_seed.py` covering an individual strain
   inside a large GTDB species cluster, with a distinct representative.
   Preserve legitimate species-level equivalences and source counts.
   Regenerate through `scripts/seed_from_sources.py` only after an
   authorized implementation change.

## Follow-up Checks

- After the future seeder fix, run `uv run pytest tests/test_seed.py` and both target validators. Confirm only unsupported GTDB identity claims change, while the source mapping/count and exact NCBI names remain traceable.
- Run full `just verify-corpus` and applicable `just qc` gates after authorized regeneration; a shared seeder fix requires broader coverage than this read-only review.
- On refresh, recheck any newly supplied registered culture accession and the native assembly statuses. Preserve source-specific versions, keep historical complete assemblies separate from the current contig assembly, and do not transfer the representative's culture identity to NA114.

## Additional Notes

The GTDB web taxon page was inaccessible. Pinned native metadata,
complete cluster aggregation and the inspected target/representative
objects supplied its evidence; current GTDB web membership was not
verified. The other 36,406 cluster members were counted structurally,
not individually reviewed. Public NCBI taxonomy and assembly APIs were
accessible. No LPSN or BacDive identifier is asserted by the target,
and unrelated species pages were not used as substitute strain evidence.

iModulonDB was not applicable: no gene, regulator, pathway or transcriptomic
assertion is present. Only this new report was added apart from the
validator's normal diagnostic output. No generated record, source
inventory, generator, history, status or earlier report was edited.
No paid research, external contact or GitHub mutation was performed.
