# YAML Record Review: Gordonia alkanivorans NBRC 16433

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/gordonia_alkanivorans_nbrc_16433.yaml`
- Started UTC: 2026-10-03T11:18:55Z
- Finished UTC: 2026-10-03T11:22:08Z
- Verdict: needs curation

## Target

Generated `TaxonRecord` for `NCBITaxon:1027371`, Gordonia alkanivorans
NBRC 16433, rank STRAIN, domain BACTERIA, parent `NCBITaxon:84096`.
The entire 953-line YAML was read. It has EXACT grounding, SEEDED mapping
status, one GTDB mapping, five exact synonyms, one BacDive strain, nine
culture identifiers, nine assembly assertions, six genome-record
assertions, 45 related-record assertions, six source attestations and an
embedded seed event. There is no own nomenclature object or type flag.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/gordonia_alkanivorans_nbrc_16433.yaml` | PASS; no issues found, exit 0. |
| `just validate-strict data/taxa/bacteria/gordonia_alkanivorans_nbrc_16433.yaml` | PASS; one file, zero ERROR rows, exit 0. |
| `just verify-corpus` | Not run: full-corpus reproduction check without a focused record selector. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs. |
| `just validate-history` | Not run: ignored-inclusive identifier, label and slug search of `history/` found no target entry. Strict validation covered the embedded event. |

All ten lineage entries matched the complete pinned taxonomy inventory.
Full subtree traversal found the target alone; the complete BacDive
inventory has exactly one classified strain here, 10585. Its nine culture
IDs match the YAML. Exact assertion-multiset checks passed for all
9 assemblies, 6 genome records and 45 related records. All 57
whole-culture-accession checks passed the pinned CAFI rules. Native
StrainInfo checks passed for all 21 assertions, including seven sequences.
Those checks do not validate the species-to-strain equivalence below.

## Identity and Grounding

Raw taxonomy row 218795 supplies the target ID, label, parent, STRAIN rank,
code 11, four NCBI names and six source labels. The inspected
[NCBI target page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1027371)
confirms the identifier, label, lineage, code and equivalent NBRC name
forms. Its live rank is no rank, unlike the snapshot's STRAIN. The live
browser labels the CIP 106363 and DSM 44369 names heterotypic synonyms,
whereas the inspected native name catalog uses generic synonym for them.
The YAML's exact placement reproduces the native categories through
`src/taxonmech/ncbi_taxdump.py:90`. These source-version differences remain
unresolved pending hash-verified original-taxdump replay.

The NCBI lineage passes through Gordoniaceae; native GTDB uses
Mycobacteriaceae. Keeping the NCBI parent chain is correct under the
repository's non-reconciliation rule. A GTDB species-cluster name is not,
however, an exact synonym of a single strain, even when that strain
supplies the representative genome.

## Evidence

**GTDB mapping and membership.** An ignored-inclusive decompressed search
of all native GTDB genome shards, followed by exact terminal-species
filtering, found 23 members of `s__Gordonia alkanivorans` with eight taxids:

| NCBI taxid | Members | Native scope |
| --- | --- | --- |
| 84096 | 15 | Species-classified Gordonia alkanivorans genomes. |
| 1027371 | 1 | NBRC 16433, RS_GCF_000225505.1, representative. |
| 2676309 | 1 | Gordonia sp. 135, RS_GCF_009720185.1. |
| 1883427 | 2 | Actinomycetes bacterium, GB_GCA_023387895.1 and GB_GCA_023460655.1. |
| 1095773 | 1 | Strain s104, RS_GCF_000529675.1. |
| 1423140 | 1 | CGMCC 6845, RS_GCF_000503935.1. |
| 3029399 | 1 | Gordonia sp. Swx-4, RS_GCF_030316175.1. |
| 1904963 | 1 | Gordonia sp. CNJ-863, RS_GCF_001942325.1. |

The sole target-taxid member explicitly names NBRC 16433,
GCA_000225505.1, SAMD00041830 and PRJNA224116. Raw mapping row 1211
nevertheless gives the whole cluster a closeMatch to this strain; other
rows map the same cluster to the parent and other taxa. Twenty-three is
the reproduced cluster size, not the number of genomes for NBRC 16433.
The GTDB web endpoint was inaccessible; the inspected native census
establishes the scope defect independently.

**BacDive and culture identity.** Raw row 10446 and native BacDive 10585
agree on designation 2102-488 and select strain taxid 1027371 over the
also-listed species taxid 84096. The inspected
[BacDive page](https://bacdive.dsmz.de/strain/10585) confirms the identity,
type status and collection context. The native metadata retain DOI
10.13145/bacdive10585.20260601.11; this was inspected as source provenance,
not independently resolved through the DOI service. Native reference
67770 explicitly supplies GCA_000225505, IMG 2512047058 and PATRIC
1027371.3, all at target taxid 1027371. Source-supplied unversioned assembly
syntax is preserved. DQ020577 and Y18054 occur in native 16S context;
only the first is an owned StrainInfo sequence in the reviewed object.

The inspected
[NBRC 16433 catalog](https://www.nite.go.jp/nbrc/catalogue/NBRCCatalogueDetailServlet?CAT=00016433&ID=NBRC)
independently confirms type status, deposit equivalents, the IFO-to-DSM
history, BACI00000000, SAMD00041830 and PRJNA66367. The inspected
[JCM 10677 catalog](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=10677)
confirms the same deposit history and culture equivalents, plus the
assembly pair and three gene accessions. These catalog crosslinks do
not authorize transferring StrainInfo sequence ownership among deposits.

**Genome and related source chains.** Counts by source are:

| Assertion kind | Source counts |
| --- | --- |
| Assemblies, 9 | BACDIVE 1; BV-BRC 1; GOLD 2; GTDB 2; NCBI 2; STRAININFO 1. |
| Genome records, 6 | BACDIVE 2; BV-BRC 1; GOLD 2; GTDB 1. |
| Related records, 45 | BV-BRC 2; GOLD 17; GTDB 2; NCBI 4; STRAININFO 20. |

Native GenBank/RefSeq objects verify GCA/GCF_000225505.1, contig assembly
ASM22550v1, `strain=NBRC 16433`, sample SAMD00041830, type-material status,
and projects PRJNA66367/PRJNA224116 respectively. BV-BRC 1027371.3 verifies
the GenBank assembly, sample, PRJNA66367 and BACI00000000. Accession
versions and project provenance are retained separately.

Five GOLD organisms were inspected. Go0012003 explicitly names NBRC 16433
in both culture and strain fields; Gp0012003 connects that organism to
SAMD00041830 and PRJNA66367; Ga0009497 names the project and supplies
GCA_000225505.1 and IMG 2512047058. Its empty organism field does not
conflict with the explicit project chain. Go0606374 through Go0606377
support DSM 44369, HKI 0136, IFO 16433 and JCM 10677 respectively. HKI
has only a strain-field assertion; the other three retain both source
fields. These repeated provenance assertions are not distinct genomes.

**StrainInfo.** The full native object 50595.3 is published online,
references BacDive 10585 and carries DOI 10.60712/SI-ID50595.3 with its
version history. Its seven own available deposits all have type status
true: CIP 106363 (DP151275), DSM 44369 (DP151276), IFO 16433 (DP169546),
JCM 10677 (DP169547), KCTC 9951 (DP322036), NBRC 16433 (DP336542) and
NCIMB 13615 (DP565408). The seven sequences have explicit ownership:

| Owner | Native sequences retained |
| --- | --- |
| CIP 106363, DP151275 | DQ020577, rRNA operon reference. |
| DSM 44369, DP151276 | AB075553 and AB438179, gyrB; AB437906, secA1; EU871790, catA; GU130258, putative alkB. |
| NBRC 16433, DP336542 | GCA_000225505, unversioned contig assembly. |

Every generated assertion matches its native ID, status, taxon, source
description, record DOI and own-deposit sequence relationship. Six
nucleotide references remain outside genome counts. Direct requests for
AB075553, AB437906 and AB438179 returned browser challenges; DQ020577,
EU871790 and GU130258 were inaccessible. Native provenance and the
inspected JCM links support the retained references, but current sequence
content was not independently validated.

The NCBI browser also links SI-ID 125946. Its inspected native object
instead concerns BacDive 10586 and deposits including DSM 44499,
CIP 106722 and NBRC 102012, associated with the Gordonia nitida type
context. None is one of this target's nine deposits. Its AY972054 and
EU871791 sequences must not be imported through a species-level linkout.
Likewise, HKI 0136 and IFM 10352 are aliases in 50595, not extra owned
deposit objects.

**Nomenclature, type flag and attestations.** Raw LPSN row 17241 and the
inspected [LPSN species page](https://lpsn.dsmz.de/species/gordonia-alkanivorans)
identify name 776578, parent taxid 84096, and type-deposit equivalents.
There is no separately mapped LPSN name on this child. The omitted
`is_type_strain` follows the documented same-taxon LPSN derivation in
`docs/HARMONIZATION.md:176` and the schema slot at line 477; it is not an
assertion of false type status. Any broader type-evidence representation
requires an explicit maintained-model change.

Raw MediaDive row 83 supplies two medium IDs, 535 and J57; Madin row 510
supplies one trait assertion; BactoTraits row 60 supplies six. They agree
with the six-source scope row 10781 and embedded seed event. The raw GOLD
taxon-count table has 22 organisms at the parent only, so native GOLD
genome links do not imply an additional child GOLD attestation. Attestation
units remain distinct and are not phenotype claims.

## Completeness

The one-strain listing is complete relative to the full inventoried
subtree. All source-backed assembly, genome and related assertions in
the raw and StrainInfo link inventories are retained. SAMD00041830 was
not found in an ignored-inclusive search of `data/atb/` or the full
decompressed native `data/catalog/allthebacteria.tsv.xz`; no omitted
eligible ATB link was established. Y18054 is native BacDive/LPSN context,
not an owned sequence of SI-ID 50595, and does not establish an omitted
StrainInfo row.

Ignored-inclusive identifier, label and slug searches covered raw
identity/count inputs, curation inputs and history. There was no target
history entry or prior report. The original pinned NCBI taxdump archive
and `nodes.dmp` were absent from the ignored-inclusive filename search
under `data/`; taxonomy rank and name-class replay remain unavailable.

Optional definition, discussion, curator evidence and graph slots may
remain empty. Gene names occur only in source accession descriptions.
The installed `kg-microbe-sources` runner was unavailable; ignored-inclusive
runner discovery in the Mechs subtree found staging scripts but no usable
claw checkout. The iModulonDB page exposed no inspectable dataset content,
and targeted Gordonia search returned no hit. That is not proof of source
absence and supplies no expression-module evidence or inferred function.

## Findings

**Major M1: GTDB species identity is promoted onto NBRC 16433.** The exact
species synonym and GTDB equivalence xref conflate this single strain
with a 23-genome cluster spanning eight taxids. Representative-genome and
type-strain status do not make those identities equal. The 23-GENOME
attestation must remain explicitly cluster-scoped rather than being read
as strain-specific coverage.

Maintained owners: the upstream kg-microbe GTDB mapping transform feeding
`data/raw/gtdb_mappings.tsv`, and `src/taxonmech/seed.py:438`. The condition
at line 451 accepts closeMatch as identity without rank/scope checks;
xref and exact-synonym emission follow from line 467. A generated-record
patch would not correct either source of the behavior.

Finding counts: 0 blocker, 1 major, 0 minor. The documented type-flag
boundary, native/live taxonomy differences and inaccessible nucleotide
endpoints are explicit limitations, not additional proven defects.

## Recommended Edits

1. Make GTDB identity promotion rank- and scope-aware in
   `src/taxonmech/seed.py`. Preserve the supported NBRC 16433 genome,
   sample and deposit links while suppressing exact species equivalence
   on this narrower strain.
2. Correct the upstream mapping semantics and explicitly retain the
   species scope of cluster counts. Add NBRC 16433 and the 23-member
   cluster as a regression fixture, with a valid species-level positive
   control. Do not transfer SI-ID 125946 links.
3. Resolve rank/name-class differences using the hash-verified pinned
   taxonomy before proposing a separate inventory correction. Any expanded
   type-evidence rule belongs in maintained schema/seed logic, not YAML.

## Follow-up Checks

1. Confirm that removing unsupported species equivalence leaves all
   valid native genome/deposit evidence intact and does not change NCBI
   lineage to GTDB's family assignment.
2. After maintained fixes, use the documented dry-run/canary workflow,
   both focused validators and `just verify-corpus`. Repeat assertion
   multiset, full-accession and own-deposit sequence checks.
3. Retry the six nucleotide endpoints if sequence-level confirmation is
   required. Keep function descriptions as source descriptions, not new
   mechanistic or expression claims.

## Additional Notes

Only this new report was manually written. No YAML, inventory, scope,
status or history event changed. Strict validation emitted its normal
diagnostic TSV. No paid research or GitHub mutation was used. The parent
and SI-ID 125946 context does not constitute a separate record review.
Eukaryota was untouched.
