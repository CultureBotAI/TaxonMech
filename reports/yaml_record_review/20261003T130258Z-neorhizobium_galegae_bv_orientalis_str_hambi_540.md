# YAML Record Review: Neorhizobium galegae bv. orientalis str. HAMBI 540

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/neorhizobium_galegae_bv_orientalis_str_hambi_540.yaml`
- Started UTC: 2026-10-03T12:58:43Z
- Finished UTC: 2026-10-03T13:02:58Z
- Verdict: needs curation

## Target

Generated `TaxonRecord` for `NCBITaxon:1028800`, Neorhizobium galegae bv.
orientalis str. HAMBI 540, rank `STRAIN`, domain `BACTERIA`, parent
`NCBITaxon:323655`. Grounding is `EXACT`; mapping status remains `SEEDED`.

Read the entire 95-line YAML. It contains 12 lineage entries, one GTDB
mapping, three synonyms, one xref, zero BacDive strain entries, four source
attestations and an embedded seed event. No publication, sequence accession
or genome link is asserted in this target record.

This is a read-only review. No source, YAML, history, status or generated
page was changed; only this report was manually written. The parent species
was inspected for relevant culture/genome presence, not fully reviewed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/neorhizobium_galegae_bv_orientalis_str_hambi_540.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/neorhizobium_galegae_bv_orientalis_str_hambi_540.yaml` | PASS; one file, zero errors. |
| Complete raw identity and lineage comparison | PASS; identity, parent, rank, code and all 12 ancestor objects agree with the pinned inventory. |
| Complete BacDive subtree membership | PASS; the raw subtree contains only taxon 1028800 and no classified BacDive entries. |
| Complete native GTDB species census | PASS for count: four genomes, three NCBI taxids, only one target-strain genome. All four objects were read. |
| Complete raw GTDB mapping-target comparison | PASS for inventory fidelity: three target rows for the species; only taxon 1028800 has closeMatch. This does not validate identity equivalence. |
| Parent culture/genome presence | PASS; BacDive 13626 and HAMBI 540 are retained on `data/taxa/bacteria/neorhizobium_galegae.yaml`, including GCA_000731315.1. |
| `just verify-corpus` | Not run: full-corpus reproduction check; no focused substitute is exposed. |
| `just validate-history` | Not run: ignored-inclusive identifier/name/slug search found no standalone target history. Strict validation checked the embedded event. |
| Causal graph and generated products | Not applicable to asserted graph content; no graph is present. Generated pages and exports were not audited. |

Live GTDB, direct NCBI BioSample and BioProject fetches did not yield usable
source text. Their native structured records were inspected instead. The
configured KG-Microbe GOLD edge file was unavailable, limiting independent
reconstruction of the GOLD attestation. No sequence payload or publication
body was reassessed.

## Identity and Grounding

The [NCBI Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1028800)
confirms the target identifier, scientific name, biovar parent and code 11.
Its served page says `no rank` and labels the older Rhizobium strain name a
heterotypic synonym. The pinned taxonomy instead supplies rank `STRAIN` and
a generic synonym class. These are explicit source differences, not grounds
to silently rewrite one source from the other.

`data/raw/ncbitaxon_taxa.tsv:219205` matches the record. All three target
native name objects at `data/catalog/ncbi_names-0005.jsonl.gz:28255` onward
were read: scientific name, equivalent name with `strain HAMBI 540`, and
generic synonym with `Rhizobium ... str. HAMBI 540`. The inspected
`src/taxonmech/ncbi_taxdump.py` copies native ranks rather than inferring a
strain rank from the label, and maps generic synonyms/equivalent names to
exact synonyms. Thus the YAML is faithful to the pinned NCBI inputs; live
rank/name-class reconciliation remains a follow-up, not a confirmed second
record defect.

The [LPSN species entry](https://lpsn.dsmz.de/species/neorhizobium-galegae)
is record 792476, the validly published correct name Neorhizobium galegae.
It names Rhizobium galegae as its basonym and homotypic synonym and includes
HAMBI 540 among the type-strain deposits. This supports parent-species name
context and the culture identity; it does not make the entire species an
exact synonym of this individual strain.

## Evidence

**Raw values and provenance.** `data/raw/gtdb_mappings.tsv:1239` supplies
closeMatch and four genomes. `data/raw/gold_organisms.tsv:353` supplies two
organisms; `data/raw/madin_taxa.tsv:532` supplies five trait assertions.
`curation/seed_scope.tsv:26052` records the four-source selection. The seed
event and NCBI snapshot date are consistent with this provenance. These
counts describe upstream records; no specific phenotype is asserted and
different units must not be summed.

**GTDB scope is broader than HAMBI 540.** A structured scan of every native
GTDB genome shard found exactly four members of `s__Neorhizobium galegae`:

| Genome | Native strain identifier | NCBI taxid |
| --- | --- | --- |
| RS_GCF_000731315.1 | HAMBI 540 | 1028800 |
| RS_GCF_000986035.1 | HAMBI 2427 | 323655 |
| RS_GCF_008806425.1 | NG_87_Ori | 399 |
| RS_GCF_024384645.1 | Ng77_Ori | 399 |

The complete HAMBI 540 object is at
`data/catalog/gtdb_genomes-0007.jsonl.gz:2177`: representative and type
material, species taxid 399, target taxid 1028800, GCA_000731315.1,
SAMEA3139073 and PRJNA224116. Representative/type status does not confer
identity between the strain and the species. Native GTDB uses Rhizobiales
where the NCBI lineage uses Hyphomicrobiales; each classification remains
source-scoped.

The same GTDB species has raw broadMatch rows to taxa 323655 and 399 at
`data/raw/gtdb_mappings.tsv:268511` and `:286198`. The four-genome count is
correct for the cluster, not a count of four HAMBI 540 genomes. The target's
closeMatch must not be promoted to exact biological identity (M1).

**The culture and genome evidence is retained at the species level.**
`data/raw/bacdive_strains.tsv:13462` classifies BacDive 13626 under taxon
399, with 12 culture identifiers including HAMBI 540. Read its complete
native object at `data/bacdive/records.jsonl.gz:13461`. The inspected
[BacDive page](https://bacdive.dsmz.de/strain/13626) corroborates the species
assignment, culture identity and associated genome references.

The target taxon's descendants do not include its ancestors. Consequently
the model's subtree gathering does not bring a strain classified under 399
down into 1028800. The parent YAML retains BacDive 13626, HAMBI 540 and
10 assembly-link assertions, seven genome-record assertions and 86 related
record assertions. These are link counts, not counts of independent genomes.
Relevant GCA_000731315.1 presence was checked, not every parent assertion.

Complete native genome/context objects inspected for this target include:

| Source | Evidence |
| --- | --- |
| GenBank | `data/catalog/ncbi_genbank-0000.jsonl.gz:27123`: GCA_000731315.1, HAMBI 540, taxid 1028800, species 399, SAMEA3139073, PRJEB1950, complete type-material assembly. |
| RefSeq | `data/catalog/ncbi_refseq-0000.jsonl.gz:23559`: paired GCF_000731315.1, same strain/sample, project PRJNA224116; the paired GenBank assembly is explicitly identical. |
| BV-BRC | `data/bvbrc/bvbrc-0000.jsonl.gz:2986` and `:2987`: 1028800.16 is a plasmid record for HG938354; 1028800.3 is the complete record with HG938353.1 and HG938354.1. Do not collapse those record types. |
| GOLD | `data/gold/organisms.jsonl.gz:48377`, `projects.jsonl.gz:47595`, `analyses.jsonl.gz:35728`: Go0081455 -> Gp0081455 -> Ga0056506, HAMBI 540/taxid 1028800, SAMEA3139073/PRJEB1950, GCA_000731315.1 and IMG 2585427634. |
| StrainInfo | `data/straininfo/records.jsonl.gz:4763` and `assemblies.tsv:2915`: strain 4763, HAMBI deposit 20768 and unversioned GCA_000731315, classified under species 399. Preserve the unversioned source accession. |

The StrainInfo object contains other deposit contexts; only the explicit
HAMBI deposit-to-assembly chain informs this target review. Marker sequences
in BacDive and StrainInfo are not promoted into whole-genome evidence.

**GOLD count limitation.** The target has two organisms in the raw KGX-derived
inventory, but the inspected native GOLD workbook catalog has one matching
organism, Go0081455. `docs/HARMONIZATION.md` distinguishes these provenance
routes. The configured `kg-microbe/data/transformed/gold/edges.tsv` could
not be opened; an ignored-inclusive filename search of that configured
checkout, excluding Git internals, found no replacement GOLD edge file.
`data/raw/MANIFEST.yaml:60` pins the unavailable edge input with SHA-256
`b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12`.
The raw count matches the YAML, but the two underlying organisms were not
independently resolved. This is a documented limitation, not proof that
the YAML count must be changed to one.

## Completeness

The NCBI lineage, parent, genetic code and seed provenance are complete for
the asserted identity. `strain_count: 0` is correct under the present
BacDive classification/subtree contract, not a claim that HAMBI 540 lacks
a culture deposit or genome. Parent-filed evidence should not be moved into
this target merely because its genome has the target taxid.

Empty nomenclature, strain and genome sections are not independently
confirmed omissions under this model. The target has no phenotype, gene,
regulator, transcriptomic or causal-graph assertion requiring iModulonDB
or graph evaluation; iModulonDB is not applicable, not negative evidence.

Ignored-inclusive searches covered target identifier, scientific name and
slug in `history/`, `data/atb/` and `data/straininfo/`, including compressed
files. No standalone target history or ATB match was found in those bounded
locations. StrainInfo yielded the parent-classified HAMBI chain described
above. These searches do not establish worldwide source absence.

## Findings

Blocker: 0. Major: 1. Minor: 0.

**M1 (major): a species is promoted to an exact strain synonym and identity
xref.** Target lines 52-55 declare bare Neorhizobium galegae an
`EXACT_SYNONYM` of HAMBI 540; lines 62-63 also promote that GTDB species to
an identity xref. The complete native membership includes three other
genomes assigned to different strain/taxon contexts. The target's own
lineage separately identifies species 399 and biovar 323655. A source
closeMatch and representative status do not erase these scope differences.

Maintained owner: `src/taxonmech/seed.py:451` treats every GTDB closeMatch
as identity without a rank/scope guard; lines 467-469 then emit the xref and
exact synonym. `src/taxonmech/extract.py` preserves upstream mapping
predicates. `docs/HARMONIZATION.md` describes the identity-promotion policy.
The generated YAML and raw inventories are not manual-fix owners.

## Recommended Edits

1. In a separately authorized change, make GTDB identity promotion in
   `src/taxonmech/seed.py` rank- and scope-aware. Do not emit the species as
   this strain's exact synonym or identity xref. Preserve the NCBI-specific
   strain aliases and source classification context.
2. Retain four as a clearly source-cluster count; do not relabel it as four
   HAMBI 540 genomes. Review the imported predicate policy before choosing
   a replacement relation, rather than guessing its direction in generated
   YAML. Update the corresponding harmonization guidance.
3. Add regression coverage in `tests/test_seed.py` for strain, subspecies
   and unranked below-species targets receiving species closeMatch rows,
   alongside a valid same-scope species case. Regenerate only through the
   documented dry-run/canary workflow after authorization.

## Follow-up Checks

Run the focused seed tests, both target validation commands above, a dry
seed and `just seed-canary NCBITaxon:1028800` after the maintained fix.
Verify that the target-specific NCBI aliases remain, the broader exact
synonym/xref is gone, source-cluster provenance remains, and the parent
culture/genome chain is not moved or lost. Run full `just verify-corpus`
before accepting regenerated corpus-wide changes.

For unresolved source reconciliation, inspect a current NCBI summary and
the pinned native taxdump for rank/name classes; keep differences explicit.
Resolve the GOLD count only against the manifest-matching KGX input or a
separately documented refreshed snapshot. Repeat live GTDB and NCBI
sample/project authority checks when accessible. None is a reason to
silently change pinned source data in this read-only review.

## Additional Notes

The finding is biological scope inflation, not failed schema validation.
The record remains `SEEDED`; no review status or history event was added.
Eukaryota was outside this individual review and its existing reports were
left untouched. Report filename coverage is tracked separately from review
quality and does not by itself certify the full corpus.
