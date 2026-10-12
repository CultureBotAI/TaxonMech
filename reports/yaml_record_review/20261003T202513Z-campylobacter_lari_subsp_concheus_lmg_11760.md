# YAML Record Review: Campylobacter lari subsp. concheus LMG 11760

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_lari_subsp_concheus_lmg_11760.yaml`
- Started UTC: 2026-10-03T20:19:03Z
- Finished UTC: 2026-10-03T20:25:13Z
- Verdict: needs curation

## Target

Reviewed all 613 lines of this generated `TaxonRecord`: `NCBITaxon:1031536`,
Campylobacter lari subsp. concheus LMG 11760, rank `STRAIN`, domain `BACTERIA`,
grounding `EXACT`, mapping status `SEEDED`. It contains one BacDive strain,
seven assembly assertions, five genome-record assertions and 26 related-record
assertions. These are provenance-bearing assertions, not distinct biological
genome counts.

Maintained owners include `src/taxonmech/seed.py`, `src/taxonmech/extract.py`
and the source inventories. This read-only review does not authorize edits to
those inputs or to generated YAML. The strain is distinct from its parent
subspecies, `NCBITaxon:488545`, and species ancestor, `NCBITaxon:201`.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/campylobacter_lari_subsp_concheus_lmg_11760.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/campylobacter_lari_subsp_concheus_lmg_11760.yaml` | Passed; one file, zero ERROR rows. Standard diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured source comparisons | Backbone, complete lineage, seed reason and direct source inventories checked; exact full-field multiset equality for all 7/5/26 strain assertions against raw inventories and the StrainInfo overlay. |
| StrainInfo evidence | All ten assertions checked against native deposit eligibility, statuses, DOI, source taxonomy and explicit same-deposit sequence membership; live record corroborates them. |
| Embedded history | Covered by strict validation; source inventory and seed-scope reason agree with the seed event. |
| Standalone history | Not applicable: identifier, label and slug searches including ignored/hidden files found no target history under `history/`. |
| Causal graph and ontology-product gates | Not applicable: the complete YAML contains no causal graph. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
rendered-page freshness, exports, FASTA replay and full test suite. Focused
comparisons do not substitute for those checks. No generator, curation-status
promotion or history writer was run. Structural validity does not resolve
the semantic scope problem below.

## Identity and Grounding

The identifier, label, strain rank, parent, genetic code 11, two NCBI equivalent
names and all eleven root-first lineage entries match
`data/raw/ncbitaxon_taxa.tsv:220741`. Live taxonomy EFetch and
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1031536)
confirm that identity. A complete backbone scan finds no child taxa.
`data/taxa/PATHS.tsv:13067` and `curation/seed_scope.tsv:14828` agree with the
identifier and slug. Native name rows in
`data/catalog/ncbi_names-0005.jsonl.gz:29898` and the next two rows support
the scientific name and both strain-specific equivalent names.

The parent subspecies is not interchangeable with LMG 11760. The inspected
[LPSN subspecies page](https://lpsn.dsmz.de/subspecies/campylobacter-lari-concheus)
identifies its type as LMG 21009 = CCUG 55786, not LMG 11760 = CCUG 55789.
The parent-name row `data/raw/lpsn_names.tsv:25024` is contextual evidence,
not a direct nomenclatural assertion for this strain. Keeping the strain's
own nomenclature slot empty and not declaring it a type strain is correct.

NCBI's class Epsilonproteobacteria and the native GTDB class Campylobacteria
are source-specific classifications. They do not justify rewriting the NCBI
lineage. The GTDB species-level exact synonym and identity xref, however,
overstate the strain's identity and are Finding M1.

## Evidence

- **BacDive identity:** `data/raw/bacdive_strains.tsv:77180`, native
  `data/bacdive/records.jsonl.gz:77179` and the inspected
  [BacDive record](https://bacdive.dsmz.de/strain/154937) support BacDive 154937,
  LMG 11760 and CCUG 55789. The native record explicitly says this is not a
  type strain. Reference 66792 supplies unversioned GCA_000816225,
  IMG 2636415659 and PATRIC 1031536.3. The reference belongs to those genome
  assertions, not to every assertion in the taxon record.
- **Inventory fidelity:** `data/raw/strain_assemblies.tsv:61997` and the next
  six rows, `data/raw/strain_genome_records.tsv:47894` and the next four rows,
  and `data/raw/strain_related_records.tsv:197090` and the next fifteen rows
  exactly reproduce the raw-source assertions. Two-field GOLD matches are
  retained as separate provenance, not counted as distinct assemblies.
- **GOLD:** Native organism row 9790, project row 9654 and analysis row 43655
  support the Go0011144 -> Gp0011144 -> Ga0069343 chain. Both eligible
  organism fields explicitly name LMG 11760. The linked analysis/project
  supply GCA_000816225.1, IMG 2636415659, PRJNA66781 and SAMN03248542.
- **NCBI and GTDB genomes:** Native GenBank
  `data/catalog/ncbi_genbank-0000.jsonl.gz:30779`, RefSeq
  `data/catalog/ncbi_refseq-0000.jsonl.gz:26741` and GTDB
  `data/catalog/gtdb_genomes-0008.jsonl.gz:32308` agree on the strain and
  GCA/GCF_000816225.1 pair. Live
  [NCBI genome metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000816225.1/dataset_report)
  corroborates the current complete assembly ASM81622v1, strain taxon and
  BioSample. GenBank/GOLD PRJNA66781 and RefSeq/GTDB PRJNA224116 remain
  distinct source assertions. Versioned accessions are not substituted for
  the unversioned BacDive accession.
- **StrainInfo:** Native `data/straininfo/records.jsonl.gz:9851` and the live
  [SI-ID 9851 API record](https://api.straininfo.dsmz.de/v2/data/strain/max/9851)
  support DOI `10.60712/SI-ID9851.2`, BacDive 154937, published status,
  available LMG deposit 38718 and CCUG deposit 923364, with no deprecated or
  erroneous match. `data/straininfo/strain_links.tsv:51996` and the following
  row match both eligible culture identifiers. Related rows 123359-123368
  exactly reproduce all ten assertions. There is no StrainInfo assembly
  assertion for this target.
- **Own-deposit sequences:** All six StrainInfo sequence associations
  explicitly identify LMG deposit 38718. They are not transferred to CCUG
  through shared group membership. Inspected NCBI nuccore EFetch metadata
  confirm strain LMG 11760 and taxon 1031536 for
  [AF550633.1](https://www.ncbi.nlm.nih.gov/nuccore/AF550633.1),
  [AM924139.1](https://www.ncbi.nlm.nih.gov/nuccore/AM924139.1),
  [KF855248.1](https://www.ncbi.nlm.nih.gov/nuccore/KF855248.1),
  [KF855257.1](https://www.ncbi.nlm.nih.gov/nuccore/KF855257.1),
  [KF855266.1](https://www.ncbi.nlm.nih.gov/nuccore/KF855266.1) and
  [KF855291.1](https://www.ncbi.nlm.nih.gov/nuccore/KF855291.1). Definitions and
  features support the partial 16S and hsp60 annotations and complete-CDS
  descriptions for phosphoramidate cytidylyltransferase, type I glutamine
  amidotransferase, phosphate kinase and atpA. No alignment or functional
  reannotation was performed.
- **Attestations:** Structured scans verify NCBI NAME 1, BacDive STRAIN 1,
  GOLD ORGANISM 1 and MADIN TRAIT_ASSERTION 4. The raw GTDB count of 30 is
  faithfully copied but describes the whole species cluster, not thirty
  genomes identified as this strain; see M1. Counts alone are not phenotype
  evidence. No direct MediaDive or BactoTraits row was found in complete
  target-ID scans of those inventories.
- **iModulonDB:** The resolved `culturebotai-claw/.venv/bin/kg-microbe-sources
  imodulondb datasets` adapter returned 28 dataset keys, none covering
  Campylobacter. No organism-matched gene query applies; this absence is not
  negative evidence about the record's gene annotations.

## Completeness

Ignored-inclusive compressed searches covered native catalog, BacDive,
BV-BRC, GOLD, SeqCode and StrainInfo data using the full target name, typed
taxon identifier, whole LMG 11760 and CCUG 55789 designations and the GTDB
species identifier. Additional searches checked the StrainInfo alias
LCDC 90-12273. Complete structured scans covered the raw source inventories,
NCBI type material, merged IDs and dropped rows. No extra eligible
deposit-backed genome association was identified within those boundaries.

Native BV-BRC `data/catalog/bvbrc-0000.jsonl.gz:3060` identifies genome
1031536.3, the same assembly/sample/project, and source strings `LMG11760`
and `LMG culture`. The current culture normalizer accepts neither string;
it does accept the spaced LMG 11760 designation. Missing BV-BRC-derived
assertions therefore follow the guarded whole-culture join policy. BacDive
independently supports the PATRIC identifier already present. Taxonomy or a
similar genome name is not used to bypass the join guard.

The LCDC alias finds GOLD organism Go0214059 at native organism row 152235,
classified at species taxon 201. No matching project, analysis or genome
record was found in the searched native catalogs. That alias is not an
eligible culture identifier on the BacDive strain, so the StrainInfo group
alias is not treated as authorization for another GOLD join.

Searches including ignored files covered `data/atb/` and the complete
compressed `data/catalog/allthebacteria.tsv.xz`, using both culture
designations, LCDC alias, SAMN03248542, BacDive identity, target identifier
and full slug. No target ATB match was found within those sources. This is
not a claim that no additional genome exists elsewhere. Standalone history
searches were likewise ignored-inclusive. Optional phenotype and mechanism
slots need not be invented for an identity/provenance record.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - Major: a species-cluster mapping is promoted to exact strain identity,
with an unqualified cluster-wide genome count.** YAML line 49 introduces
`Campylobacter D concheus` as an `EXACT_SYNONYM` of the strain, and line 60
places `GTDB:s__Campylobacter_D_concheus` in identity `xrefs`. The mapping at
line 43 and GTDB attestation at line 586 carry count 30. The upstream
`data/raw/gtdb_mappings.tsv:1302` genuinely supplies the source predicate
`skos:closeMatch` and count 30, but this does not make a species identical
to an individual strain taxon.

An ignored-inclusive scan followed by structured inspection of every exact
cluster-member identity finds 30 unique GTDB genome records: thirteen under
NCBI species 201, sixteen under subspecies 488545 and only one under strain
1031536. That one is RS_GCF_000816225.1, LMG 11760. Other members explicitly
include LMG 21009 (`data/catalog/gtdb_genomes-0008.jsonl.gz:28033`),
CCUG 55786 (the same file, row 3019) and MRC_CL1
(`data/catalog/gtdb_genomes-0017.jsonl.gz:26188`). These member identity
checks establish the cluster's broader scope; they are not reviews of those
other TaxonMech records.

The count 30 is valid as a species-cluster total. It must not be interpreted
as thirty genomes of LMG 11760. Schema identity xrefs are reserved for true
equivalence (`src/taxonmech/schema/taxonmech.yaml:180`), so the exact synonym
and xref are unsupported even though the NCBI identity and own genome links
remain correct. There is no identity blocker for the whole record.

Maintained owners: `src/taxonmech/seed.py:451` treats every `skos:closeMatch`
as identity without a rank guard and adds the xref/exact synonym at lines
467-469. `src/taxonmech/extract.py:501` counts all genome members per GTDB
species, then line 755 writes that cluster total to each mapping row.
`docs/HARMONIZATION.md:124` describes the identity-promotion assumption.
The YAML faithfully reflects these transforms. Neither patching generated
YAML nor silently inventing a replacement source predicate fixes ownership.

## Recommended Edits

1. In a later curation change, make GTDB identity promotion rank-aware in
   `src/taxonmech/seed.py`. For this strain, suppress the species exact
   synonym and identity xref while retaining the observed source mapping,
   identifier and predicate with explicit membership/scope context. Preserve
   both supported NCBI strain synonyms and every own-deposit genome link.
2. Make the cluster scope of `genome_count` and the associated attestation
   explicit in the maintained extraction/seeding contract and
   `docs/HARMONIZATION.md`. If taxon-specific membership counts are added,
   derive them independently from inspected native member identities rather
   than relabeling the cluster total or guessing a replacement predicate.
3. Add a focused `tests/test_seed.py` regression for a strain with a
   species-level `closeMatch` and a cluster containing other strains. Cover
   retained provenance, suppressed identity promotion and count scope.
   Regenerate only through the documented workflow after an authorized
   implementation and regression tests; no such edits occurred here.

## Follow-up Checks

- Run the focused seeder regression and existing supported species-mapping
  tests. Add extraction tests if the count representation changes.
- Inspect `just seed --only NCBITaxon:1031536`, then, in an authorized
  curation change, run `just seed-canary NCBITaxon:1031536` and inspect the
  diff. Do not use this review as authorization for a bulk seed.
- Rerun both target validators and exact source comparisons. Confirm the
  species label is no longer an exact strain synonym or identity xref, the
  source mapping remains available, and the seven/five/26 source assertions
  retain their identifiers, versions, source taxonomy and deposit provenance.
- A shared transform change needs full tests, corpus reproduction,
  provenance and rendered-product checks in its own curation workflow.
- Recheck the live GTDB species page when accessible. Its browser request
  failed; M1 rests on inspected pinned native GTDB members and the maintained
  extraction/seeding logic, not an unread live page.

## Additional Notes

StrainInfo classifies its group at subspecies 488545, while NCBI genome and
sequence records use strain 1031536. Retaining the source-specific taxon is
appropriate; neither scope is silently rewritten. Live StrainInfo confirms
both deposits are non-types. Parent LPSN publication identifiers are context,
not citations attached to this strain's YAML. The DOI actually asserted in
the record is the inspected StrainInfo version DOI.

The AM924139 source feature uses its own translation-table annotation; this
review does not turn that feature metadata into a change to the NCBI taxon's
genetic code or a functional claim. Sequence names and MADIN counts do not
establish phenotype, pathway activity or expression evidence.

All absence statements are bounded to the named complete structured scans
or ignored-inclusive searches. One new report was written. The record,
source code, previous reports, curation status and history were not edited.
Eukaryota records were left untouched. The other session is closed; the
existing single worktree and branch were retained without a checkout or merge.
