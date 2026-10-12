# YAML Record Review: Erwinia amylovora ACW56400

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/erwinia_amylovora_acw56400.yaml`
- Started UTC: 2026-10-03T11:29:43Z
- Finished UTC: 2026-10-03T11:33:39Z
- Verdict: needs curation

## Target

Generated `TaxonRecord` for `NCBITaxon:1027397`, Erwinia amylovora
ACW56400, rank STRAIN, domain BACTERIA, parent `NCBITaxon:552`.
The entire 84-line YAML was read. It has EXACT grounding, SEEDED mapping
status, one GTDB mapping, three exact synonyms, one GTDB xref, zero
listed BacDive strains, three source attestations and an embedded seed event.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/erwinia_amylovora_acw56400.yaml` | PASS; no issues found, exit 0. |
| `just validate-strict data/taxa/bacteria/erwinia_amylovora_acw56400.yaml` | PASS; one file, zero ERROR rows, exit 0. |
| `just verify-corpus` | Not run: full-corpus reproduction check without a focused record selector. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs. |
| `just validate-history` | Not run: ignored-inclusive identifier, label and slug searches found no target history entry. Strict validation covered the embedded event. |

All ten lineage entries matched the complete pinned taxonomy table.
Full subtree traversal found only the target; complete BacDive inventory
inspection found no strain classified within that subtree. These checks
support the inventory count, not species/strain equivalence.

## Identity and Grounding

Raw taxonomy row 218808 supports the identifier, label, STRAIN rank,
parent, code 11 and two expanded ACW56400 names. The inspected
[NCBI target page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1027397&keep=1&log_op=modifier_toggle&lvl=3&mod=1&mode=Info&srchmode=1&unlock=)
confirms ID, name, equivalent forms, code and lineage. The web tool
returned an older cached page with rank no rank, unlike the snapshot's
STRAIN. This is a bounded source-version disagreement, not proof of
a current importer defect. The NCBI Datasets page returned no usable
record body. Original-source replay is unavailable: an ignored-inclusive
filename search under `data/` found neither the pinned taxdump archive
nor `nodes.dmp`.

Native NCBI names contain the scientific name and the two equivalent
str./strain forms, supporting the YAML's NCBI synonyms. The GTDB species
name is not an equivalent name for ACW56400 alone. Native GTDB places
the cluster in Enterobacteriaceae; the NCBI lineage uses Erwiniaceae.
Those source-specific classifications are not merged in this review.

## Evidence

**Full GTDB cluster.** Ignored-inclusive decompressed search across all
native GTDB genome shards, followed by exact terminal-species filtering,
found 313 members of `s__Erwinia amylovora` across 15 NCBI taxids.
Of those, 298 bear species taxid 552, one bears target taxid 1027397,
and 14 bear other taxids. Representative RS_GCF_017161565.1 is ATCC 15580,
taxid 552, not ACW56400. It names GCA_017161565.1 and SAMN17141014.

The sole target-taxid member, RS_GCF_000240705.2, is a nonrepresentative
ACW56400 genome and names GCA_000240705.2, SAMN02469387 and PRJNA224116.
Raw mapping row 1215 supplies the closeMatch and count of 313 used in
the YAML. The count reproduces species-cluster membership, not ACW56400
genome coverage. The GTDB web endpoint was inaccessible; the complete
native cluster still disproves exact species/strain identity.

**Native NCBI genome context.** Current and historical GenBank/RefSeq
taxid searches retained the paired GCA/GCF_000240705.2 contig assembly
ASM24070v2, explicitly `strain=ACW56400`, taxid 1027397, species taxid 552
and BioSample SAMN02469387. Projects are PRJNA66419 and PRJNA224116
respectively. The objects retain AFHN00000000.1 and PMID 22174857;
the direct PubMed request returned no inspectable text, so no article
claim is used here. Assembly version .2 is preserved, not replaced by .1.

**GOLD chain and join boundary.** Native Go0011941 names ACW56400 and
target taxid 1027397 with an empty culture-collection field. Gp0011941
explicitly names that organism and supplies PRJNA66419 and SAMN02469387.
Gp0042359 also names it, but supplies PRJEB603 and no sample. These
project identities are retained separately.

Ga0248271 names Gp0011941 and IMG 2843814981. Its three GenBank source
entries cite AFHN01000023, AFHN00000000 and CP002951, all against
GCA_000240705.2; these are not three different assemblies. The analysis
object's empty organism field does not erase the explicit project chain.
The NCBI page's Go0011941 and IMG linkouts agree with this native context.

Bare ACW56400 is not recognized as a culture-deposit accession. The
target has no listed BacDive strain. Ignored-inclusive searches of raw
strain-link inventories and the GOLD taxon-count inventory for the
target ID, ACW56400, assembly/sample identifiers and Go0011941 found
no target assertion there. The native GOLD organism is not absent;
the KGX-derived count inventory and native catalog are separate inputs.
No deposit or genome link is inferred through a bare-name match.

**Nomenclature and audit.** Raw LPSN row 16957 and the inspected
[LPSN species page](https://lpsn.dsmz.de/species/erwinia-amylovora)
concern parent taxid 552, name 776008. Type deposits include ATCC 15580,
CIP 82.82, DSM 30165, LMG 2024 and NBRC 12687. They are not evidence
that ACW56400 is the species type. The NCBI page labels its BacDive
4386 linkout as a species type-strain link; that label alone cannot
support an ACW56400 deposit association. No such link is added here.

Madin row 515 supplies one TRAIT_ASSERTION; NCBI supplies one NAME,
and GTDB supplies the cluster-sized GENOME count above. Scope row
36098 and the seed event name the same three sources. Distinct count
units are not summed or turned into strain phenotype assertions.

## Completeness

The zero-strain listing follows the complete source-classified subtree.
It does not mean ACW56400 lacks a genome: native NCBI, GTDB and GOLD
objects explicitly retain its genome context. The target has no supported
listed-strain BioSample assertion from which an ATB join could be derived.
An expanded source-identity model would need explicit provenance and
tests, not an ad hoc link through shared names or species type material.

Ignored-inclusive identifier, label and slug searches covered raw inputs,
curation and history. There was no target history entry or earlier
report. Absence claims are confined to those inspected inputs; native
catalog presence and raw-inventory absence are distinguished above.
The original taxdump absence search covered all filenames under `data/`,
including ignored files.

Optional definition, discussion, curator evidence and graph slots are
appropriately empty. iModulonDB was not applicable: this YAML asserts
no gene, regulator, pathway or transcriptomic dataset. External genome
publication metadata do not introduce such an assertion into the record.

## Findings

**Major M1: a GTDB species cluster becomes exact strain identity.** The
313-member, 15-taxid cluster becomes an EXACT_SYNONYM and an equivalence
xref on ACW56400, although only one native member bears the target taxid.
The species and the narrower strain are not interchangeable. The GENOME
attestation also must not be interpreted as strain-specific coverage.

Maintained owners: the upstream kg-microbe GTDB mapping transform feeding
`data/raw/gtdb_mappings.tsv`, and `src/taxonmech/seed.py:438`. The condition
at line 451 accepts closeMatch as identity without a rank/scope guard;
xref and exact-synonym emission follow from line 467. Editing only the
generated YAML would leave the behavior reproducible.

Finding counts: 0 blocker, 1 major, 0 minor. Cached-page rank disagreement,
inaccessible publication text and unjoined native genome context remain
bounded limitations, not additional demonstrated defects.

## Recommended Edits

1. Make GTDB identity promotion rank- and scope-aware in the maintained
   seeder. Retain species-cluster context without presenting it as an
   exact name or equivalent identifier for ACW56400.
2. Correct upstream mapping semantics and explicitly retain cluster scope
   on counts. Add this target and its 313-member cluster as a regression
   fixture, with a valid species-level positive control.
3. Resolve the rank difference through hash-verified pinned-taxdump replay
   before a separate taxonomy-inventory correction. Do not create a culture
   accession or copy species type material onto this strain.

## Follow-up Checks

1. Confirm removal of unsupported species equivalence while retaining
   the target's supported NCBI identity, equivalent names and lineage.
2. After maintained fixes, run the documented dry-run/canary workflow,
   both focused validators and `just verify-corpus`. Confirm native
   genome context remains available without unsupported deposit joins.
3. Inspect PMID 22174857 only if literature-backed characterization is
   proposed; its uninspected text was not needed for the scope finding.

## Additional Notes

Only this new report was manually written. No YAML, source inventory,
scope, status or history event changed. Strict validation emitted its
normal diagnostic TSV. No paid research or GitHub mutation was performed.
Species/type-strain context is not a separate record review. Eukaryota
was outside the target.
