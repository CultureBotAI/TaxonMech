# YAML Record Review: Peptoniphilus senegalensis JC140

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/peptoniphilus_senegalensis_jc140.yaml`
- Started UTC: 2026-10-04T19:10:13Z
- Finished UTC: 2026-10-04T19:12:21Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1033744`, rank
`STRAIN`, domain `BACTERIA`, parent species `NCBITaxon:1465757`. It has
`EXACT` grounding, `SEEDED` mapping status, ten root-first ancestors,
genetic code 11, one GTDB mapping, two exact synonyms, one GTDB xref,
zero inventoried BacDive strains and three source attestations. Its seed
event is dated 2026-09-13T17:54:04Z.

The entire parent species YAML was also read to distinguish source
classification from strain identity, not to give that second record a
review verdict. Source extraction, `curation/seed_scope.tsv`,
`data/taxa/PATHS.tsv` and `src/taxonmech/seed.py` own future changes;
generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/peptoniphilus_senegalensis_jc140.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/peptoniphilus_senegalensis_jc140.yaml`: exit 0, one file, zero errors; normal diagnostic TSV under `reports/`.
- Bounded structured comparisons checked the full backbone identity, all ten ancestors, synonyms, direct source rows, path lock, scope and seed-event wording. These are evidence checks, not a focused corpus reproduction gate.
- `just verify-corpus` was skipped because it rebuilds the full corpus and offers no target-record selector; `--max-diffs` limits diagnostics only.
- `just validate-products` was not applicable: there are no curator-grounded graph nodes. NCBI identity and lineage were checked directly.
- Ignored-inclusive searches found no separate target history artifact. Full-history validation, full `just qc`, corpus tests, all-record validation, provenance hashing and rendering checks were skipped. No history entry or status promotion was made.

## Identity and Grounding

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033744&retmode=xml)
confirms the exact label, strain rank, bacterial division, parent species,
genetic code and synonym `Peptoniphilus sp. JC140`.
[Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033744)
independently gives the complete ancestor ID chain, including root.
Both agree with the record and pinned backbone at
`data/raw/ncbitaxon_taxa.tsv:221309`. Full native name objects at
`data/catalog/ncbi_names-0005.jsonl.gz:30633` and line 30634 support the
scientific name and NCBI synonym. Complete relevant tables contain no
child, direct type-material, merged-ID or dropped-ID row for this taxon.

NCBI's strain identity is not in doubt. The unsupported identity claim
is the added GTDB species equivalence. `EXACT` describes grounding to
NCBI; it does not establish equivalence to every mapped source concept.

[LPSN](https://lpsn.dsmz.de/species/peptoniphilus-senegalensis) treats
P. senegalensis as a validly published heterotypic synonym of
P. tyrrelliae. The pinned parent-species record preserves this status
and the related name. This source disagreement does not authorize
renaming the NCBI strain or replacing its lineage. In particular,
LPSN/GTDB's class Clostridia must not overwrite NCBI's Tissierellia.

## Evidence

| Emitted assertion | Inspected support and scope |
|---|---|
| NCBI name attestation, count 1 | Full backbone and native names agree with live NCBI; the snapshot date is 2026-09-13. This is not an isolate count. |
| GTDB mapping and attestation, count 8 | `data/raw/gtdb_mappings.tsv:1371` and `data/raw/gtdb_species.tsv:139766` reproduce the source predicate and species-cluster count. They do not establish eight JC140 genomes. |
| Madin trait-assertion attestation, count 4 | `data/raw/madin_taxa.tsv:631` supplies this exact taxon/count. No individual phenotype or experimental condition is asserted in the YAML. |
| Scope and seed event | `data/taxa/PATHS.tsv:13762` fixes the slug. `curation/seed_scope.tsv:36150` supplies the three-source inclusion reason reproduced by the seed event. |

The full scan of 901,341 GTDB genome objects found eight unique members
of `s__Peptoniphilus_A senegalensis`; every matching native object was read:

| Genome | Native catalog object | NCBI taxon | Source designation |
|---|---|---|---|
| `GB_GCA_047032335.1` | `gtdb_genomes-0000.jsonl.gz:37530` | 1465757 | C039_13, metagenome-derived |
| `RS_GCF_040096825.1` | `gtdb_genomes-0001.jsonl.gz:37719` | 1465757 | CLA-SR-H019 |
| `GB_GCA_910592365.1` | `gtdb_genomes-0002.jsonl.gz:20411` | 755171 | P. tyrrelliae, isolate 261-21 |
| `RS_GCF_000321025.1` | `gtdb_genomes-0008.jsonl.gz:14158` | 1033744 | JC140, representative and type material |
| `RS_GCF_902374975.1` | `gtdb_genomes-0008.jsonl.gz:44569` | 1465757 | MGYG-HGUT-01425 |
| `RS_GCF_047026745.1` | `gtdb_genomes-0009.jsonl.gz:13795` | 1465757 | C040_42, metagenome-derived |
| `GB_GCA_937997845.1` | `gtdb_genomes-0010.jsonl.gz:23569` | 1465757 | ERR209782_bin.1_CONCOCT_v1.1_MAG |
| `GB_GCA_023409115.1` | `gtdb_genomes-0015.jsonl.gz:23350` | 1879010 | Bacillota bacterium, OH_HFB_367 |

Catalog paths in this table are relative to `data/catalog/`. Thus five
members are filed under the parent species, one under JC140, one under
P. tyrrelliae and one under Bacillota bacterium. Raw mapping rows 31610,
306108 and 74509 retain the other three NCBI targets. Species membership
does not make these genomes instances of the same individual strain.

[NCBI Datasets assembly](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000321025.1/dataset_report)
confirms current `GCA_000321025.1` and paired `GCF_000321025.1`, scaffold
level, type-material status, `SAMEA2272315` and `PRJEA70541`. An exact
Assembly query for taxon 1033744 returned one paired assembly record.
Full native current rows at `data/catalog/ncbi_genbank-0000.jsonl.gz:8133`
and `data/catalog/ncbi_refseq-0000.jsonl.gz:6983` agree.

The MGYG member is retained in pinned GTDB but marked suppressed, with
non-live date 2026-04-03, in the full historical NCBI objects at
`data/catalog/ncbi_genbank_historical-0001.jsonl.gz:41301` and
`data/catalog/ncbi_refseq_historical-0002.jsonl.gz:4065`. This is not a
reason to silently decrement the pinned GTDB source count. No suppression
reason or equivalence between JC140 and MGYG-HGUT-01425 was inferred.

## Completeness

The complete direct inventories have no target row for BacDive, LPSN,
GOLD, MediaDive or BactoTraits. This statement concerns those inventories,
not the complete native catalogs: native GOLD does contain JC140.

The ignored-inclusive compressed-content search
(`rg --no-ignore --hidden -z`) covered the target ID, full name, GTDB
spelling and JC140 under `data/raw`, `data/catalog`, `data/bacdive`,
`data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`. It returned 137 matching lines. Unrelated
Pseudorhizobium endolithicum JC140, taxon 1191678, and numeric substrings
in run/sample/assembly identifiers were excluded rather than joined.

Full native BacDive object `data/bacdive/records.jsonl.gz:23254` and the
live [BacDive 23453 page](https://bacdive.dsmz.de/strain/23453) identify
JC140, DSM 25694, CSUR P154 and KCTC 15414, classified at parent species
1465757. Sequence metadata separately names strain taxon 1033744.
The parent YAML already contains this culture and its supported assembly,
IMG and PATRIC links. Since the seeder gathers BacDive records from the
target and descendants, not ancestors, `strain_count: 0` is consistent
with source classification. It does not mean there is no culture.

Full native GOLD objects preserve a supported chain:
`data/gold/organisms.jsonl.gz:14769`, `Go0017277`, names DSM 25694 and
taxon 1033744; `data/gold/projects.jsonl.gz:14300`, `Gp0017277`, names
that organism and the sample/project; `data/gold/analyses.jsonl.gz:11782`,
`Ga0019633`, names that project and assembly/IMG identifiers. Those
assertions already occur on the parent record's classified BacDive
strain. The absence of a separate KGX-derived GOLD taxon attestation
does not erase this native evidence or require copying the parent
culture down to the child. `docs/HARMONIZATION.md` distinguishes these
two source pipelines.

The full native BV-BRC object at
`data/bvbrc/bvbrc-0000.jsonl.gz:3217` independently identifies genome
1033744.3, JC140 and the same assembly/sample/project. Its bare strain
designation is not a new culture-deposit join key.

Optional record-level literature evidence, definitions and causal graphs
can remain empty. This target asserts no DOI, PMID or verbatim evidence
snippet. Literature on the parent species was not treated as a mandatory
strain-level citation or imported wholesale.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: the GTDB species is asserted as equivalent to strain JC140.**
   The species-level GTDB identifier appears in `xrefs`, and its name
   without JC140 appears as an exact synonym. The complete cluster
   evidence supports a species membership relation, not identity to this
   individual strain. This violates the schema's true-equivalence
   restriction on `xrefs`. `src/taxonmech/seed.py:451` promotes any
   `skos:closeMatch` to identity without a rank check, and lines 467-469
   emit both claims. The faithfully retained raw predicate does not
   justify this promotion. These are manifestations of one scope error.

## Recommended Edits

1. Make GTDB identity promotion rank-aware in `src/taxonmech/seed.py`.
   Do not emit a species xref or exact synonym for an infraspecific taxon
   solely from source `skos:closeMatch`. Keep NCBI identity, synonym,
   parent, lineage and genetic code unchanged.
2. Keep the source mapping and species-cluster count traceable, with a
   scope note explaining that they do not assert JC140 identity for all
   members. Investigate the upstream kg-microbe predicate separately.
   Any source correction belongs upstream and in maintained extraction
   (`scripts/extract_source_inventory.py` / `src/taxonmech/extract.py`),
   not a hand-edited raw row or YAML override.
3. Add regression coverage in `tests/test_seed.py` for a strain, parent
   species and other species sharing a GTDB cluster. Preserve legitimate
   species-level identity mappings and source counts. Regenerate through
   `scripts/seed_from_sources.py` only after an authorized implementation
   change; do not rewrite the record as part of this review.

## Follow-up Checks

- After the future fix, run `uv run pytest tests/test_seed.py` and both target validators. Confirm that the strain loses only unsupported GTDB equivalence claims and that source mappings remain auditable.
- Compare the regenerated strain and parent species, including culture/genome links and LPSN synonym status. Then run full `just verify-corpus` and applicable `just qc` gates.
- On a source refresh, recheck GTDB membership, source predicates and exact-taxonomy assembly scope. Preserve the NCBI/LPSN distinction; do not infer a new reconciled taxonomy or merge strains from a shared species cluster.

## Additional Notes

The GTDB web taxon page was inaccessible through the web reader. Full
pinned native objects and a complete cluster scan supplied the source
evidence; current GTDB web membership was not verified. Public NCBI
taxonomy/assembly APIs, LPSN and BacDive were accessible.

iModulonDB was not applicable: no gene, regulator, pathway or
transcriptomic assertion is present. This is not a genome-quality,
phenotype or culture-availability review. The parent species' whole
evidence was not audited as a second target.

Only this new review report was added apart from the validator's normal
diagnostic output. No generated record, source inventory, generator,
history, status or previous report was edited. No paid research,
external contact or GitHub mutation was performed.
