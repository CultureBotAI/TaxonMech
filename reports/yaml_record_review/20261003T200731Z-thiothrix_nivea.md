# YAML Record Review: Thiothrix nivea

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/thiothrix_nivea.yaml`
- Started UTC: 2026-10-03T20:01:48Z
- Finished UTC: 2026-10-03T20:07:31Z
- Verdict: needs curation

## Target

Reviewed all 739 lines of this generated `TaxonRecord`: `NCBITaxon:1031`,
Thiothrix nivea, rank `SPECIES`, domain `BACTERIA`, grounding `EXACT`, mapping
status `SEEDED`. The record has one BacDive strain, ten assembly assertions,
seven genome-record assertions and 31 related-record assertions. These are
source assertions, not counts of distinct assemblies or biological strains.

The maintained inputs are the source inventories and transforms, notably
`src/taxonmech/seed.py`; this review does not authorize patching the generated
YAML. The species is distinct from its child strain taxon `NCBITaxon:870187`.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/thiothrix_nivea.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/thiothrix_nivea.yaml` | Passed; one file, zero ERROR rows. Standard diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured source comparisons | Exact backbone/lineage and seed-history comparison; complete field-multiset equality for all 10/7/31 strain assertions against raw inventories and the StrainInfo overlay. |
| StrainInfo evidence | All ten assertions checked against the native record, eligible culture identifiers, deposit status, nonerroneous relations, DOI and explicit same-deposit sequence membership. |
| Embedded history | Covered by strict validation; seed event matches the source inventory and seed-scope reason. |
| Standalone history | Not applicable: identifier, label and slug searches including ignored/hidden files found no target history under `history/`. |
| Causal graph and ontology-product gates | Not applicable: the entire YAML contains no causal graph. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
rendered-page freshness, exports and full test suite. These are not replaced by
the focused comparisons above. No generator, history writer or curation-status
promotion was run. Structural validators do not detect the semantic finding
below.

## Identity and Grounding

The identity, parent `NCBITaxon:1030`, genetic code 11, three NCBI synonym or
authority strings and complete nine-entry root-first lineage match
`data/raw/ncbitaxon_taxa.tsv:801`. Live [NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1031,870187)
and taxonomy EFetch independently confirm the species and its strain child.
A complete traversal of the local backbone finds only that child. An
ignored-inclusive anchored identifier search across `data/taxa/**/*.yaml`
finds exactly this species record. `PATHS.tsv:12881` and
`curation/seed_scope.tsv:20756` agree with its identity and slug.

LPSN `782776`, name, status, type-deposit identifiers, publication and sequence
accession match `data/raw/lpsn_names.tsv:21125`. The inspected
[LPSN species page](https://lpsn.dsmz.de/species/thiothrix-nivea) supports the
correct-name status, ATCC 35100, DSM 5205, JP2 and AH001799, and documents the
1983 emendation. JP2 is retained as a strain designation, not invented as a
registered culture-collection CURIE. The local NCBI type-material rows
1499-1504 independently corroborate these designations.

Source taxonomies disagree at higher ranks: NCBI uses Thiotrichales and
Thiotrichaceae, while the LPSN-derived classification in BacDive uses
Beggiatoales and Leucotrichaceae. Keeping the explicitly NCBI lineage is
appropriate; this difference is not a reason to rewrite it. The GTDB species
identity conflict is more consequential and is Finding M1.

## Evidence

- **BacDive strain:** `data/raw/bacdive_strains.tsv:16893`, native
  `data/bacdive/records.jsonl.gz:16892`, and the inspected
  [BacDive record](https://bacdive.dsmz.de/strain/17079) agree on JP2, the two
  registered deposits, type-strain status and child taxon 870187. Genome
  reference 66792 explicitly supplies unversioned GCA_000260135, PATRIC
  870187.4 and IMG 2506520049. Those source-specific versions and identifiers
  are preserved, not silently upgraded or conflated.
- **Genome and project provenance:** Raw assembly rows 93665-93673,
  genome-record rows 75567-75573 and related-record rows 273169-273190 match
  the YAML exactly. Native BV-BRC `bvbrc-0027.jsonl.gz:41302` has both explicit
  DSM 5205 fields. Native GOLD organism 2835, project 2892 and analysis 15779
  supply the Go0003219 -> Gp0003219 -> Ga0024915 chain, GCA_000260135.1,
  IMG 2506520049, PRJNA51139 and SAMN02256515. GOLD organism 453374 separately
  supports Go0622755 for ATCC 35100 at species scope.
- **NCBI/GTDB genome records:** Native GenBank `ncbi_genbank-0000.jsonl.gz:5421`,
  RefSeq `ncbi_refseq-0000.jsonl.gz:4576` and GTDB
  `gtdb_genomes-0010.jsonl.gz:9653` support DSM 5205 and the paired
  GCA/GCF_000260135.1 accessions. The RefSeq/GTDB project PRJNA224116 and the
  GenBank project PRJNA51139 remain separate source assertions. Live
  [NCBI genome metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000260135.1/dataset_report)
  confirms the current GenBank assembly, RefSeq pair, type material,
  scaffold level and BioSample identity.
- **StrainInfo:** Native `data/straininfo/records.jsonl.gz:35807` and the live
  [SI-ID 47903 API record](https://api.straininfo.dsmz.de/v2/data/strain/max/47903)
  support DOI `10.60712/SI-ID47903.3`, BacDive 17079, published status, DSM
  deposit 159092 and ATCC deposit 159093. The two matches are reproduced in
  `strain_links.tsv:72861` and the following row. All six sequence associations
  explicitly point to DSM deposit 159092; none transfers through group
  membership alone. Assembly row 6569 and related rows 172669-172677 exactly
  reproduce all ten overlay assertions.
- **Sequence identities:** NCBI nuccore EFetch source features confirm
  [AH001799.2](https://www.ncbi.nlm.nih.gov/nuccore/AH001799.2) as JP2/ATCC
  35100, and [EF618600.1](https://www.ncbi.nlm.nih.gov/nuccore/EF618600.1),
  [EF641919.1](https://www.ncbi.nlm.nih.gov/nuccore/EF641919.1),
  [EU155048.1](https://www.ncbi.nlm.nih.gov/nuccore/EU155048.1),
  [HQ823668.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ823668.1) and
  [HQ823672.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ823672.1) as DSM 5205,
  taxon 870187. Their annotations support the cited soxB, aprBA, dsrAB,
  16S and gyrB descriptions. Source-unversioned identifiers remain
  unversioned in the YAML. Sequence strings were not aligned or reannotated.
- **Publication:** [Crossref metadata for the Approved Lists DOI](https://api.crossref.org/works/10.1099/00207713-30-1-225)
  verifies title, year 1980, volume 30, issue 1 and pages 225-420. The full
  article was not read; nomenclatural interpretation uses inspected LPSN
  text, not bibliographic metadata alone.
- **Attestations:** Complete structured inventory scans verify NCBI NAME 1,
  LPSN NAME 1, directly mapped GTDB GENOME 1, gathered BacDive STRAIN 1,
  direct GOLD ORGANISM 1 and direct MADIN TRAIT_ASSERTION 2. The child's
  GOLD 1, MediaDive medium 573 and MADIN 6 are not added to species-level
  direct counts. These counts make no phenotype claim.
- **iModulonDB:** The resolved `culturebotai-claw/.venv/bin/kg-microbe-sources
  imodulondb datasets` adapter returned 28 dataset keys, none covering
  Thiothrix. No organism-matched query applies; this is not negative
  evidence about the sequence annotations or metabolism.

## Completeness

The BacDive listing is complete for the local species subtree, not capped.
Ignored-inclusive compressed searches covered the native catalog, BacDive,
BV-BRC, GOLD, SeqCode and StrainInfo snapshots using full names, synonyms,
deposits and exact typed taxon fields. Complete structured scans additionally
covered the raw taxon/source inventories, retired IDs and dropped rows.
No extra eligible deposit-backed strain was identified in those boundaries.
Initial DSM-prefix hits such as DSM 52050-52059 belong to Myxococcus and do
not match the whole DSM 5205 culture identifier.

BV-BRC candidates DOLJORAL78_51_81 and RT are not JP2 and do not provide a
matching eligible culture deposit. GTDB's ABC2.126 member is an independently
classified metagenome, not evidence for another DSM 5205 genome association.
SeqCode name 21890 corroborates the name; the type-genome hit for Thiothrix
phosphatis arises from its genus ancestry and is not this species' type.

AllTheBacteria is correctly absent from `genome_records`. The full ignored
catalog `data/catalog/allthebacteria.tsv.xz:1018142` contains SAMN02256515 as
`NOT_PROCESSED`, assembly availability 0, with no assembly or download
accessions. The committed overlap row `data/atb/assemblies.tsv:2513` agrees,
and `data/atb/exclusions.tsv:1646` records `assembly_unavailable`.
Ignored-inclusive sample/strain searches find no target strain or genome
crosslink in `data/atb/`. The full-catalog genus scan returns only other
species plus this unavailable sample. No FASTA/download replay is warranted.

StrainInfo also lists ATCC 31500 in the same group, but that designation is
not in the BacDive culture identifiers used for joins. LPSN explicitly
describes ATCC 31500 as a historical abstract error. Its omission here is
correct, not a missing deposit. Optional biological mechanisms or causal
graphs are not required by these identity and provenance assertions.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - Major: a non-type genome mapping is promoted to an unsupported exact
species synonym and identity cross-reference.** YAML line 70 introduces
`Thiolinea nivea A` as `EXACT_SYNONYM`, and line 78 includes
`GTDB:s__Thiolinea_nivea_A` among identity xrefs. The upstream
`data/raw/gtdb_mappings.tsv:1298` genuinely supplies `skos:closeMatch` and
genome count 1, but that source row alone does not establish species identity.

Native `data/catalog/gtdb_genomes-0014.jsonl.gz:36283` identifies its supporting
genome as GCA_002746895.1, isolate DOLJORAL78_51_81, a metagenome with no type
material. The corresponding native GenBank row at
`ncbi_genbank-0002.jsonl.gz:8938` additionally flags its source organism as
unverified. Conversely, the actual DSM 5205 type genome is assigned to GTDB
`s__Thiothrix nivea` in `gtdb_genomes-0010.jsonl.gz:9653`, consistent with
the LPSN-linked GTDB identifier already retained in the YAML. Its local GTDB
mapping is filed under child taxon 870187 (`gtdb_mappings.tsv:316025`), not
the species ID. Thus direct-ID mapping cardinality conceals the conflict
between a non-type metagenome and the name-bearing type lineage.

This is unsupported equivalence, not proof that the record's NCBI identity
is wrong. Preserve the observed source classification, but do not present
the Thiolinea cluster as an exact alternate species identity.

Maintained owner: `src/taxonmech/seed.py:451` treats every `skos:closeMatch`
as identity regardless of conflicting LPSN/type-genome evidence, then adds
the xref and exact synonym at lines 467-469. `docs/HARMONIZATION.md:124`
documents the same assumption. The source inventory is faithfully copied;
changing generated YAML or relabeling the source predicate without evidence
would not address this transform-level problem.

## Recommended Edits

1. In a later curation change, guard GTDB identity promotion in
   `src/taxonmech/seed.py` against conflicting LPSN-linked/type-strain
   classifications across the species and its strain descendants. For this
   record, remove the Thiolinea exact synonym and identity xref while retaining
   the observed mapping, predicate, source ID and count with an explicit
   classification-conflict note. Preserve the supported Thiothrix GTDB xref.
2. Add a targeted regression in `tests/test_seed.py` covering a species-level
   non-type `closeMatch` that conflicts with the LPSN identity and a child
   type-genome classification. Keep ordinary supported mappings and pooled
   mappings covered. Update the ownership explanation in
   `docs/HARMONIZATION.md`; do not infer new genome counts or silently move
   child assertions to species scope.
3. After approval and tests, regenerate through the documented seed workflow
   and review the resulting diff. No such edits or regeneration occurred in
   this review.

## Follow-up Checks

- Run focused `tests/test_seed.py` regressions for conflicting and supported
  mappings, including unchanged counts, source predicates and strain links.
- Use the documented seed dry run, then an authorized
  `just seed-canary NCBITaxon:1031`; inspect the diff before any broader write.
- Rerun both target validators. Confirm the unsupported exact synonym and
  xref are gone, the bounded source mapping remains explicit, and all
  deposit/genome evidence still matches its source.
- A shared seeder change also needs full tests, corpus reproduction,
  provenance and rendered-product checks in its own coordinated curation
  workflow. This report does not establish a corpus-wide finding count.
- Recheck the GTDB authority page when accessible. The browser request failed;
  the finding rests on inspected pinned native GTDB records, LPSN identity
  evidence and NCBI metadata, not an uninspected live GTDB result.

## Additional Notes

The difference between the SI species taxon 1031 and the genome/sequence
strain taxon 870187 is retained as source scope, not treated as a mismatch.
AH001799.2 includes segmented rRNA features and gaps; the YAML does not
assert sequence length or contiguity. No functional phenotype or mechanism
is inferred from partial-gene descriptions or source-record counts.

All absence statements are bounded to the named complete structured reads
or ignored-inclusive searches. Live taxonomy, genome, StrainInfo and sequence
metadata were read without authentication or paid research. One report was
created; the target, previous reports, source code, curation history and
statuses were not edited. Eukaryota records were left untouched.
