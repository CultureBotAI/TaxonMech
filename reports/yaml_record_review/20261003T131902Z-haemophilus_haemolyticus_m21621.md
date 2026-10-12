# YAML Record Review: Haemophilus haemolyticus M21621

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/haemophilus_haemolyticus_m21621.yaml`
- Started UTC: 2026-10-03T13:18:02Z
- Finished UTC: 2026-10-03T13:19:02Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1028805`, Haemophilus haemolyticus
M21621, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:726`.
Grounding is `EXACT`; mapping status remains `SEEDED`.

Read all 66 YAML lines: ten ancestors, two NCBI synonyms, code 11, zero
BacDive strains, two source attestations and one embedded seed event. No
GTDB mapping, identity xref, nomenclature, genome accession, publication
or causal graph is asserted in the target.

Read-only review: only this report was manually written. No source,
generated YAML, history, status or page was changed. Eukaryota was excluded.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/haemophilus_haemolyticus_m21621.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/haemophilus_haemolyticus_m21621.yaml` | PASS; one file, zero errors. |
| Complete identity, lineage and synonym comparison | PASS; all ten ancestors, label, rank, parent, code and both synonyms match the raw inventory. |
| Complete BacDive subtree membership | PASS; target is its only subtree member; zero classified strains agrees with the YAML. |
| Source counts and selection | PASS; one NCBI scientific-name attestation and one Madin assertion; no raw GTDB, GOLD or LPSN target row. |
| Native genome context | Current GenBank, historical GenBank/RefSeq, BV-BRC and the relevant GOLD chain were read; current RefSeq/GTDB searches found no target match. |
| `just verify-corpus` | Not run: full-corpus reproduction check; focused checks do not substitute for it. |
| `just validate-history` | Not run: ignored-inclusive identifier/name/slug search found no standalone target history. Strict validation checked the embedded event. |
| Graph and generated products | No graph asserted; graph grounding not applicable. Generated pages and exports were not audited. |

Live NCBI Taxonomy, BioSample and BioProject metadata were inspected.
No publication body or sequence payload was reassessed. The reviewed
record asserts neither a publication claim nor a sequence-derived trait.

## Identity and Grounding

The [current NCBI summary](https://www.ncbi.nlm.nih.gov/taxonomy/1028805)
identifies M21621 as a strain. The inspected
[legacy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1028805&lvl=3&mode=node)
confirms the identifier, scientific name, equivalent strain names, parent
lineage and code 11, but says `no rank`. The current summary and pinned
taxonomy support `STRAIN`; this source-version discrepancy is preserved
rather than used to rewrite the record.

`data/raw/ncbitaxon_taxa.tsv:219210` matches the target. Read all three
native name objects at `data/catalog/ncbi_names-0005.jsonl.gz:28270` onward:
one scientific name and two equivalent names explicitly containing
M21621. Both exact synonyms retain strain scope. No species name is
promoted to an exact strain alias.

## Evidence

**Counts and audit.** `data/raw/madin_taxa.tsv:537` supplies one trait
assertion; the YAML does not turn this count into an unspecified phenotype.
The NCBI count is one scientific-name attestation, not the number of
synonym strings. `curation/seed_scope.tsv:57228` agrees with the two-source
selection and embedded seed event dated 2026-09-13T17:54:04Z. The NCBI
attestation states the pinned 2026-09-13 taxonomy snapshot.

**Genome evidence is present but not linked through a local strain row.**
Complete native objects read:

| Source object | Checked evidence |
| --- | --- |
| `data/catalog/ncbi_genbank-0000.jsonl.gz:3844` | GCA_000222065.2, latest in the snapshot, contig level with 28 contigs, strain M21621, taxid 1028805/species 726, SAMN02952886 and PRJNA66577. |
| `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:1160` | GCA_000222065.1 is suppressed; source not-live date 2012-01-21. Keep accession versions separate. |
| `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:1095` | GCF_000222065.1 is suppressed, not-live date 2016-01-21, paired to GCA_000222065.2, project PRJNA71473. Source exclusion reason is low quality sequence. |
| `data/bvbrc/bvbrc-0000.jsonl.gz:2994` | Genome 1028805.3, WGS, M21621, GCA_000222065.2, PRJNA66577, SAMN02952886 and AFQQ00000000. |
| `data/gold/organisms.jsonl.gz:10576` | Go0012009, taxid 1028805 and M21621; culture-collection field empty. |
| `data/gold/projects.jsonl.gz:10434` | Gp0012009 explicitly links Go0012009 to PRJNA66577 and SAMN02952886. |
| `data/gold/analyses.jsonl.gz:4279` | Ga0009498 joins Gp0012009, IMG 2512047059 and unversioned GCA_000222065. Do not infer a source accession version. |

The current GenBank record also carries the low-quality RefSeq exclusion
flag. Its paired historical RefSeq identifier is not evidence that the
RefSeq assembly is current. Ignored-inclusive, decompressed searches of
every current `ncbi_refseq-*.jsonl.gz` and `gtdb_genomes-*.jsonl.gz` shard,
using exact taxid, strain token, sample and assembly stem, found no target
match. This is a bounded snapshot result. The reason for GTDB noncoverage
was not inferred from the RefSeq flag.

The [BioSample authority page](https://www.ncbi.nlm.nih.gov/biosample/SAMN02952886)
confirms M21621, AFQQ00000000.1 and PRJNA66577. The
[BioProject authority page](https://www.ncbi.nlm.nih.gov/bioproject/66577)
explicitly connects GCA_000222065.2 at contig level to the sample and
target taxid. Its generic project background was not converted into a
strain-specific clinical claim.

The project names the genome study identified by PMID 21952546 in native
GenBank metadata. The article body was not used as evidence for additional
traits, mechanisms or genome quality; no publication is directly cited in
the reviewed YAML.

**GOLD has two distinct provenance routes.** The native workbook chain
exists, but the raw KGX-derived taxon-count inventory has no target row.
`docs/HARMONIZATION.md` and `conf/sources.yaml` distinguish these routes.
The missing GOLD attestation therefore matches the maintained input. The
empty native culture-collection field and bare M21621 designation do not
establish a supported deposit join for importing the genome chain.

## Completeness

No consequential required-field omission was found. Identity, lineage,
code, strain-specific aliases and seed audit are complete for this record.
Zero BacDive strains means no classified BacDive entry in the target
subtree, not that the strain has never been cultured or sequenced.

Under the current model, genome links attach to supported BacDive/deposit
identities. The positive source-native genome evidence above cannot by
itself authorize a new BacDive row, a bare-name join or inferred collection
accession. Likewise, the parent species' GTDB or nomenclature evidence
must not be transferred to M21621 without a target-specific assertion.

Ignored-inclusive identifier, scientific-name, slug, strain-token, sample
and assembly-stem searches covered `history/`, `data/raw/`,
`data/bacdive/`, `data/straininfo/` and `data/atb/`, including compressed
files where present. No target standalone history, native BacDive record,
StrainInfo match or ATB match was found in those bounded locations. No raw
GTDB mapping or LPSN target row was found. This is not a worldwide source
absence claim.

No explicit phenotype, gene, regulator, transcriptomic dataset or causal
graph is asserted. iModulonDB and graph checks are not applicable, rather
than evidence against any biological property.

## Findings

None found. Blocker: 0. Major: 0. Minor: 0.

The pass covers this record under its present model and pinned sources,
subject to the skipped full-corpus check. It does not certify complete
exposure of every native source or other records' review quality.

## Recommended Edits

None required. Preserve the generated YAML unchanged.

A separately authorized expansion to expose non-BacDive genome evidence
or native GOLD taxon coverage would belong in maintained extraction,
seeding, schema and harmonization policy with tests. It must preserve
accession versions, suppression flags and source-specific attestation
semantics rather than patch this generated record.

## Follow-up Checks

Run full `just verify-corpus` before making a corpus-wide reproduction
claim. For any authorized future refresh affecting this target, check the
current/historical assembly status, exact strain/sample matches and
deposit eligibility; run both focused validators and inspect a dry-run
and canary before accepting regenerated output.

The suppressed RefSeq record and low-quality metadata must remain visible
if genome links are later represented. Retrieve the publication body only
if later curation needs evidence beyond the identity metadata reviewed here.

## Additional Notes

The complete target was inspected without sampling. It remains `SEEDED`;
no human-review status, curation event or standalone history was added.
Report presence is counted separately from full-corpus review completion.
