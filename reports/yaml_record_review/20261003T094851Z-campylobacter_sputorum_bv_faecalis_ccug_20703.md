# YAML Record Review: Campylobacter sputorum bv. faecalis CCUG 20703

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_sputorum_bv_faecalis_ccug_20703.yaml`
- Started UTC: 2026-10-03T09:44:37Z
- Finished UTC: 2026-10-03T09:48:51Z
- Verdict: needs curation

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1031920` denotes
Campylobacter sputorum bv. faecalis CCUG 20703, stored as `STRAIN` under
biovar 1031919 in `BACTERIA`. It has eleven ancestors, code 11, `EXACT`
grounding, `SEEDED` mapping status, one GTDB mapping/synonym/xref, zero
attached BacDive strains, three source attestations and one seed event.
The index entry is `data/taxa/PATHS.tsv:13150`.

## Validation

- `just validate data/taxa/bacteria/campylobacter_sputorum_bv_faecalis_ccug_20703.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/campylobacter_sputorum_bv_faecalis_ccug_20703.yaml`:
  passed, one file and zero errors.
- Structured inventory checks matched ID, label, stored rank, parent,
  genetic code and all eleven ancestor IDs/labels/ranks/parent links.
  The target has no direct children in the pinned taxonomy.
- `just straininfo-query --strain SI-ID13604 --evidence --limit 20`
  passed during this biovar/child review sequence, with three deposit
  matches. It checks source/configuration and hashes with
  `reproduce=False`; it is not full source replay. Native JSON and
  deposit-specific committed rows were also inspected.
- `git diff --exit-code -- data/taxa/bacteria/campylobacter_sputorum_bv_faecalis_ccug_20703.yaml data/taxa/bacteria/campylobacter_sputorum_biovar_fecalis.yaml`:
  passed. No taxon or maintained input changed.
- `just verify-corpus` was skipped because it is full-corpus-only.
  Full source reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped after the ignored-inclusive target
  search found no separate history artifact. The embedded event was read
  and included in strict validation.

## Identity and Grounding

The successfully inspected [NCBI node page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1031920&lvl=&mode=node)
agrees on identity, name, biovar parent, code and ancestry, but currently
reports no rank rather than the pinned `STRAIN`. This is a source-version
discrepancy, not proof that the taxon denotes the wrong culture. A later
request to the same page failed; the earlier successful read is the basis
for this comparison.

The inspected [CCUG culture page](https://www.ccug.se/strain?id=20703)
confirms CCUG 20703, Bolton A3, LMG 8532 and CIP 105558 and the biovar
fecalis designation. Its link from BacDive succeeded; a subsequent direct
retry failed. Native and live BacDive classify the culture at species 206,
while its genome metadata identifies the more specific NCBI taxon 1031920.
These are different source scopes, not interchangeable classifications.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:220789` and native scientific-name row
  `data/catalog/ncbi_names-0005.jsonl.gz:29992` support the pinned identity
  and one NAME attestation. `curation/seed_scope.tsv:36138` supports the
  three-source seed rationale.
- `data/raw/gtdb_mappings.tsv:1322` supports the stored closeMatch row and
  count 11. A complete native cluster selection recovered eleven genomes
  across six NCBI IDs: 206 (four), 32024 (three), and one each at 1032066,
  1031920, 1031754 and 32023. The target genome RS_GCF_002220735.1 is
  not the representative; RS_GCF_008245005.1, taxon 32024, is.
  Membership in this species cluster does not establish identity between
  the species and this individual strain.
- `data/catalog/gtdb_genomes-0004.jsonl.gz:33531` preserves native genus
  Campylobacter_F and species Campylobacter_F sputorum. The YAML synonym
  Campylobacter F sputorum also loses the meaningful underscore suffix.
- `data/raw/madin_taxa.tsv:593` supports one TRAIT_ASSERTION count, not a
  specific phenotype. `data/raw/MANIFEST.yaml` identifies the transformed
  Madin input and SHA256
  `3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f`.
  The configured upstream `data/transformed/madin_etal/edges.tsv` could
  not be opened at the path resolved from `conf/sources.yaml`; its
  individual edge was not independently verified. No phenotype is inferred.
- Native [BacDive 134440](https://bacdive.dsmz.de/strain/134440), at
  `data/bacdive/records.jsonl.gz:56745`, agrees with the inspected live
  page on the culture deposits and genome identifiers. Its native type
  flag is no. The unversioned BacDive GCA_002220735 and BV-BRC 1031920.3
  are separate source assertions, not two biological genomes.
- Native BV-BRC `bvbrc-0000.jsonl.gz:3102` identifies CCUG 20703,
  GCA_002220735.1, CP019683, SAMN03737989 and PRJNA66805. Native GenBank
  `ncbi_genbank-0001.jsonl.gz:38544` and RefSeq
  `ncbi_refseq-0001.jsonl.gz:22392` supply the paired versioned assemblies,
  the same BioSample and target taxon. Their project scopes differ:
  PRJNA66805 versus PRJNA224116. Preserve the source-specific values.
- Native GOLD `projects.jsonl.gz:8150` and `organisms.jsonl.gz:8285`
  corroborate Gp0009294 / Go0009294 and the target culture. These
  organism/project identifiers are not assembly accessions.
- Full native SI-ID13604 at `data/straininfo/records.jsonl.gz:13604`
  supplies DOI 10.60712/SI-ID13604.2 and three own deposits: CCUG 20703 /
  SI-DP52020, LMG 8532 / SI-DP52018, and CIP 105558 / SI-DP149640.
  Only CCUG 20703 explicitly supplies unversioned GCA_002220735.
  CCUG and LMG deposits name biovar taxon 1031919; CIP has no explicit
  deposit taxon. Neither the shared group nor CIP's origin relation
  permits sequence transfer or invented deposit-level classification.
- The corresponding BacDive strain on
  `data/taxa/bacteria/campylobacter_sputorum.yaml` retains seven assembly,
  three genome-record and 24 related assertions across these sources.
  This was a focused context check, not a verdict on the whole species
  record. The evidence is not globally lost from TaxonMech.

iModulonDB is not applicable to this taxon/count record, which asserts no
gene, pathway or transcriptomic function. Sequence descriptions were used
only for identity and source-type checks.

## Completeness

Ignored-inclusive ID/name/slug searches covered reports, history, curation,
raw, ATB and StrainInfo inventories. No prior target report or separate
history artifact was found. Decompressed native searches covered JSONL.GZ
and TSV.GZ under catalog, BacDive, BV-BRC, GOLD and StrainInfo, including
ignored files. The cluster count was independently recomputed from the
complete native GTDB cluster, not inferred from a search snippet.

The zero strain count follows BacDive classification and the seeder's
NCBI-subtree rule. It does not mean the culture or its genomes are absent.
The model does not surface the parent species' culture evidence here.
Missing LPSN/type-strain or phenotype slots are not mandatory-field defects.

The full ATB TSV.XZ and all live auxiliary accession/DOI pages were not
audited. Both live GTDB taxon and genome requests failed. The live NCBI
assembly page supplied a matching title but a JavaScript body, and the
live StrainInfo page was also a shell; neither substituted for native
metadata verification. A PubMed request for the contextual assembly
reference returned only a footer, so its publication was not used to
support a finding. No global absence or current-release GTDB confirmation
is claimed.

## Findings

- **Blocker:** None found; the NCBI and culture identity is sound.
- **Major (1): Species-cluster membership is promoted to strain identity.**
  The eleven-genome GTDB species is emitted as an EXACT_SYNONYM and
  identity-style xref for a single strain. The same path flattens
  Campylobacter_F to Campylobacter F. The maintained owner is
  `src/taxonmech/seed.py:451` and its synonym emission, which treats every
  closeMatch as identity without a rank/scope guard. Review the upstream
  kg-microbe GTDB mapping semantics consumed by `src/taxonmech/extract.py`
  and add focused coverage in `tests/test_seed.py`.
- **Minor (1): Rank-source discrepancy.** Live NCBI says no rank while
  the pinned inventory/YAML say STRAIN. The owners are
  `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. The importer
  directly normalizes native rank; inspect the pinned archive before
  diagnosing an importer bug or refreshing the source.
- **Minor (2): Culture/genome evidence is not discoverable on this node.**
  The exact culture is represented on species 206 but this child record
  exposes only zero attached strains. This is a non-blocking representation
  limitation, not an incorrect stored count. A source-labeled navigation
  improvement belongs in the seeder/templates and harmonization guidance;
  it must retain BacDive, StrainInfo and genome classification separately.

## Recommended Edits

Do not patch the generated YAML. In a separately authorized curation
change, make GTDB identity promotion rank/scope-aware and preserve native
suffixes. Retain useful cluster membership and its count 11; do not change
the cluster count to one or mechanically reverse a SKOS predicate.
Investigate the pinned rank separately. Any culture-link improvement must
preserve the own-deposit sequence rule and source-specific taxon IDs.

## Follow-up Checks

- Inspect the rank in the NCBI archive pinned by SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
  An ignored-inclusive checkout filename search did not locate it or
  `nodes.dmp`; no absence outside the checkout is claimed.
- Retry live GTDB and source-specific accession verification, and recover
  the manifest-pinned Madin edge before adding any phenotype claim.
- Test species-versus-strain closeMatch behavior, suffix preservation,
  unchanged cluster counts and deposit-specific sequence attribution.
  After authorized input changes, use the normal refresh, run
  `just seed-canary NCBITaxon:1031920`, both target validators and full
  `just verify-corpus`; inspect pages if presentation changes.

## Additional Notes

Some source queries returned truncated output; structured native JSON/CSV
reads recovered the relevant rows. Initial guessed configuration/manifest
filenames failed and were corrected to `conf/sources.yaml` and
`data/raw/MANIFEST.yaml`. No paid research, outbound messages, GitHub
mutation, history addition or review-status promotion occurred.
