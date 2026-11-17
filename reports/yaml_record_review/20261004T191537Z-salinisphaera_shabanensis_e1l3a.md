# YAML Record Review: Salinisphaera shabanensis E1L3A

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/salinisphaera_shabanensis_e1l3a.yaml`
- Started UTC: 2026-10-04T19:13:56Z
- Finished UTC: 2026-10-04T19:15:37Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1033802`, rank
`STRAIN`, domain `BACTERIA`, parent species `NCBITaxon:180542`. It has
`EXACT` grounding, `SEEDED` mapping status, ten root-first ancestors,
genetic code 11, one GTDB mapping, three exact synonyms, one GTDB xref,
zero inventoried BacDive strains and three source attestations. The seed
event is dated 2026-09-13T17:54:04Z.

The parent species YAML was read in full for classification and source
scope comparison, not reviewed as a second target. Future changes belong
in maintained source extraction, scope/path inputs or `src/taxonmech/seed.py`;
generated records were not edited.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/salinisphaera_shabanensis_e1l3a.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/salinisphaera_shabanensis_e1l3a.yaml`: exit 0, one file, zero errors; normal diagnostic TSV under `reports/`.
- Bounded structured checks compared identity, the complete lineage, synonyms, direct source inventories, path lock, scope and seed-event wording. These are not a focused corpus reproduction gate.
- `just verify-corpus` was skipped: it rebuilds the full corpus and has no target-record selector; `--max-diffs` limits diagnostics only.
- `just validate-products` was not applicable: no curator-grounded graph nodes are present. NCBI identity was checked directly.
- Ignored-inclusive target searches found no separate target history artifact. Full-history validation, full `just qc`, corpus tests, all-record validation, provenance hashing and rendering checks were skipped. No history or status was changed.

## Identity and Grounding

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033802&retmode=xml)
confirms the identifier, exact label, strain rank, species parent,
bacterial division, genetic code 11 and both equivalent-name variants:
`Salinisphaera shabanensis str. E1L3A` and
`Salinisphaera shabanensis strain E1L3A`.
[Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033802)
confirms the complete ancestor ID chain, including root. These agree
with the pinned backbone at `data/raw/ncbitaxon_taxa.tsv:221310` and all
ten emitted ancestors. Native scientific/equivalent-name objects at
`data/catalog/ncbi_names-0005.jsonl.gz:30635`, line 30636 and line 30637
were read in full and support the NCBI synonyms' exact scope.

Complete relevant tables contain no child, direct type-material,
merged-ID or dropped-ID row for this strain taxon. The NCBI identity
and `EXACT` grounding are sound. The unsupported equivalence is the
additional GTDB species xref and strain-free exact synonym.

GTDB uses order Nevskiales while the NCBI lineage uses Salinisphaerales.
That difference is preserved as source classification, not repaired by
replacing NCBI's carried lineage.

## Evidence

| Emitted assertion | Inspected support and scope |
|---|---|
| NCBI name attestation, count 1 | Full backbone/native name objects and public NCBI taxonomy agree; snapshot date 2026-09-13. This is not an isolate or assembly count. |
| GTDB mapping and attestation, count 2 | `data/raw/gtdb_mappings.tsv:1372` and `data/raw/gtdb_species.tsv:163055` reproduce the predicate and whole species-cluster count. |
| Madin trait-assertion attestation, count 2 | `data/raw/madin_taxa.tsv:632` supplies this taxon/count. No individual phenotype or experimental condition is asserted in the target. |
| Scope and audit | `data/taxa/PATHS.tsv:13765` fixes the slug; `curation/seed_scope.tsv:36151` supplies the three-source inclusion reason reproduced by the seed event. |

A complete scan of 901,341 GTDB genome objects found exactly two unique
members of `s__Salinisphaera shabanensis`; both full native objects were read:

| Genome | Native source object | NCBI strain taxon | GenBank assembly / BioSample |
|---|---|---|---|
| `RS_GCF_000215955.2` | `data/catalog/gtdb_genomes-0011.jsonl.gz:41330` | 1033802, E1L3A | `GCA_000215955.3` / `SAMN02472183` |
| `RS_GCF_040361315.1` | `data/catalog/gtdb_genomes-0002.jsonl.gz:7365` | 1304276, T35B1 | `GCA_040361315.1` / `SAMN03015570` |

Both have NCBI species taxon 180542. E1L3A is the representative and is
marked as type material; T35B1 is not. Raw mapping row 17495 also maps
the species cluster to the sibling strain. The count of two is therefore
correct as source-cluster volume, not as two genomes assigned to E1L3A.
The complete cluster evidence does not establish strain equivalence.

[NCBI Datasets assembly](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000215955.3/dataset_report)
confirms current `GCA_000215955.3` paired with current
`GCF_000215955.2`, contig-level assembly SSPSH_V2, taxon 1033802,
type-material status, `SAMN02472183` and `PRJNA66981`. Its BioSample
also explicitly identifies DSM 14853. Full native current rows at
`data/catalog/ncbi_genbank-0000.jsonl.gz:3581` and
`data/catalog/ncbi_refseq-0000.jsonl.gz:3091` agree. Different GenBank and
RefSeq version suffixes are supported by the actual pairing, not a typo.

The exact-taxonomy Assembly query returned three entries, all inspected:
the current paired assembly, suppressed `GCA_000215955.1`, and replaced
`GCA_000215955.2` / `GCF_000215955.1`. Native historical objects at
`data/catalog/ncbi_genbank_historical-0000.jsonl.gz:955`, line 956 and
`data/catalog/ncbi_refseq_historical-0000.jsonl.gz:1016` corroborate these
statuses. This is one current assembly pair plus historical versions,
not three current assemblies or three biological isolates.

## Completeness

Complete direct inventories have no target BacDive, LPSN, GOLD,
MediaDive or BactoTraits row. This does not mean the native catalogs
lack E1L3A: both BacDive and GOLD retain relevant culture/genome evidence.

The gitignore-independent compressed-content search
(`rg --no-ignore --hidden -z`) covered the taxon ID, full species name
and E1L3A under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`
and `history`, returning 70 matched lines. Numeric substrings in unrelated
sample, run and assembly identifiers were excluded. The similarly
numbered BioSample SAMEA1033802 is not this taxon or its sample.

Full native BacDive object `data/bacdive/records.jsonl.gz:17596` and the
[BacDive 17786 page](https://bacdive.dsmz.de/strain/17786) identify E1L3A,
DSM 14853 and JCM 11575, classified at parent species 180542. Its sequence
assertions separately name strain taxon 1033802. The parent YAML already
retains the culture and its assembly, IMG and PATRIC links. The seeder
gathers strains from the target and descendants, not ancestors, so zero
listed BacDive strains on this child is consistent with source classification.
It does not mean no deposited culture exists.

[LPSN's species page](https://lpsn.dsmz.de/species/salinisphaera-shabanensis)
supports the species name and type designations. Pinned LPSN row
`data/raw/lpsn_names.tsv:19729` links name 780730 to parent species
180542 and the GTDB species, not to strain taxon 1033802. That
species-level link does not establish a strain-level GTDB equivalence.

Full native GOLD objects preserve the chain from organism `Go0011162`
(`data/gold/organisms.jsonl.gz:9808`, DSM 14853, taxon 1033802) to
project `Gp0011162` (`data/gold/projects.jsonl.gz:9672`, the same organism,
sample and project) to analysis `Ga0024146`
(`data/gold/analyses.jsonl.gz:15121`, that project and assembly/IMG IDs).
These culture-linked assertions are already retained on the parent
record's BacDive strain. Their presence is distinct from the separate
KGX-derived GOLD taxon-attestation inventory; an absent attestation must
not be described as absence from GOLD.

The full BV-BRC object at `data/bvbrc/bvbrc-0000.jsonl.gz:3218` identifies
genome 1033802.3 and the same E1L3A assembly/sample/project. Its bare
strain designation is not a new registered-culture join key. The
unversioned `GCA_000215955` supplied by BacDive and GOLD on the parent
must remain unversioned as source evidence, not be silently rewritten
to the version found in live NCBI metadata.

Optional record-level citations, definitions and causal graphs may remain
empty. The target asserts no DOI, PMID or verbatim evidence snippet;
the parent species' literature was not audited as a second record.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: the GTDB species is promoted to equivalence with strain E1L3A.**
   Its identifier is in `xrefs`, and `Salinisphaera shabanensis` is an
   exact synonym despite denoting the species rather than this strain.
   Complete GTDB membership includes the sibling T35B1 strain. This
   violates the schema's true-equivalence restriction for `xrefs`.
   `src/taxonmech/seed.py:451` treats every `skos:closeMatch` as identity
   without checking rank; lines 467-469 emit both unsupported claims.
   The raw predicate is faithfully reproduced but cannot justify that
   promotion. These are two manifestations of one scope error.

## Recommended Edits

1. Make GTDB identity promotion rank-aware in `src/taxonmech/seed.py`.
   A species mapping must not supply an infraspecific taxon's equivalent
   xref or exact synonym solely because it carries `skos:closeMatch`.
   Preserve both exact NCBI synonyms, NCBI identity, parent and lineage.
2. Keep source mapping and whole-cluster count traceable, with a scope
   note distinguishing species membership from strain identity. Review
   the upstream kg-microbe mapping predicate independently. Any source
   correction belongs upstream and in maintained extraction
   (`scripts/extract_source_inventory.py` / `src/taxonmech/extract.py`),
   not a hand-edited raw row or YAML override.
3. Add a regression in `tests/test_seed.py` for two sibling strain taxa
   mapped to one GTDB species. Preserve legitimate species-level
   equivalences, source counts and the separate culture/genome evidence.
   Regenerate through `scripts/seed_from_sources.py` only after an
   authorized implementation change.

## Follow-up Checks

- After the future seeder change, run `uv run pytest tests/test_seed.py` and both target validators. Confirm only unsupported GTDB identity claims are removed and source mappings remain auditable.
- Compare the regenerated strain and parent species, preserving source accession versions and the classified culture's links. Run full `just verify-corpus` and applicable `just qc` gates after authorized regeneration.
- At refresh time, recheck cluster membership and exact-taxonomy assembly status. Keep historical versions separate from current assemblies, and do not infer strain identity from a shared GTDB species.

## Additional Notes

The GTDB taxon page was inaccessible through the web reader. Complete
pinned native objects and the full membership scan supplied its source
evidence; current GTDB web membership was not verified. NCBI APIs and
BacDive were accessible. The LPSN page returned by the web reader was
an older cached rendition printed 2025-11-10; its name/type information
agrees with the pinned inventory, but this was not a fresh LPSN snapshot.

iModulonDB was not applicable: no gene, regulator, pathway or transcriptomic
assertion is present. No phenotype, culture-availability or genome-quality
conclusion was inferred from the supporting source metadata.

Only this new report was added apart from the validator's normal
diagnostic output. No generated record, inventory, generator, history,
status or earlier report was edited. No paid research, external contact
or GitHub mutation was performed.
