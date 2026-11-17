# YAML Record Review: Endozoicomonas montiporae

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/endozoicomonas_montiporae.yaml`
- Started UTC: 2026-10-03T10:59:13Z
- Finished UTC: 2026-10-03T11:01:57Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1027273`, Endozoicomonas montiporae,
rank SPECIES, domain BACTERIA, parent `NCBITaxon:305899`. The entire
586-line YAML was read before judgment. It has EXACT grounding, SEEDED
mapping status, one LPSN name, one GTDB species mapping, one BacDive strain,
six source attestations and an embedded seed event.

The strain carries ten assembly assertions, eight genome-record assertions
and 22 related-record assertions. These source-bearing counts are not
counts of distinct biological genomes. CL-33's descendant taxon was
inspected as provenance, not assigned a separate review verdict here.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/endozoicomonas_montiporae.yaml` | PASS; no issues found, exit 0. |
| `just validate-strict data/taxa/bacteria/endozoicomonas_montiporae.yaml` | PASS; one file, zero ERROR rows, exit 0. |
| `just verify-corpus` | Not run: full-corpus reproduction check without a focused record selector. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs. |
| `just validate-history` | Not run: ignored-inclusive identifier, label and slug search of `history/` found no target entry. Strict validation covered the embedded event. |

Additional read-only checks passed:

- Nine ancestor labels/ranks and the parent chain match the pinned taxonomy
  table. Its complete target subtree consists of this species and strain
  `NCBITaxon:570277`, Endozoicomonas montiporae CL-33.
- Complete BacDive inventory membership for that subtree is exactly the
  retained BacDive 133557 record, classified at the species itself.
- Exact assertion-multiset comparisons reproduce ten assemblies, eight
  genome records and 22 related records from raw and StrainInfo inventories.
- All 34 assertions carrying a matched culture ID reference a listed
  deposit and pass the repository's whole-accession CAFI recognition.
- All five StrainInfo assertions agree with the native deposit identity,
  availability, classification, BacDive cross-reference and record-version
  DOI. The assembly names the same deposit in its native sequence object.

Initial ad hoc taxonomy/inventory checks used incorrect column names and
stopped. They were corrected against the actual TSV headers and rerun;
only the successful checks above support the verdict. They are not a
substitute for the skipped full-corpus reproduction gate.

## Identity and Grounding

Raw taxonomy row 218782 and the inspected
[NCBI species detail page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1027273&keep=1&lin=f&lvl=3&mode=Info&srchmode=1&unlock=)
agree on the species identity, rank, code 11, lineage and type-strain
designations. The browser tree and raw taxonomy row 134436 place CL-33
beneath the species. A genome assertion bearing taxid 570277 is therefore
not automatically evidence of a foreign species or incorrect record ID.

[LPSN 788550](https://lpsn.dsmz.de/species/endozoicomonas-montiporae)
supports the Yang et al. 2010 name, valid publication, correct-name status,
LMG 24815/BCRC 17933/CL-33 type identity and FJ347758. The raw LPSN row
supplies the legitimate flag. The retrieved LPSN page is an older cached
view, so it is corroboration, not proof of a live October 2026 update.

The native NCBI names catalog has a scientific-name entry and an authority
entry for this taxid. The latter is correctly retained as RELATED_SYNONYM.
The separate GTDB exact synonym is source-marked text derived from the
GTDB species identifier; it does not assert a new validly published name.

## Evidence

**GTDB scope.** The complete native GTDB catalog search finds exactly two
members of `s__Endozoicomonas_A montiporae`:

| Native genome | NCBI taxid | Native strain field |
| --- | --- | --- |
| RS_GCF_000722565.1 | 1027273 | LMG 24815 |
| RS_GCF_001583435.1 | 570277 | CL-33 |

Both have NCBI species taxid 1027273 and type-material designation. The
second is the GTDB representative. Thus the species-level closeMatch and
genome count two are supported even though only LMG 24815 supplies a
recognized whole culture-deposit match for a GTDB strain-genome link.
The bare CL-33 field must not be treated as a collection accession.

GTDB places this species in Pseudomonadales and Endozoicomonas_A; NCBI
places it in Oceanospirillales and Endozoicomonas. The record preserves
NCBI lineage while identifying the GTDB mapping separately. The GTDB
website did not resolve during this review; native metadata provide the
cluster evidence above.

**Type identity and literature.** The inspected
[primary species description](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.014357-0)
explicitly equates CL-33, LMG 24815 and BCRC 17933 as the type strain.
The [PubMed record](https://pubmed.ncbi.nlm.nih.gov/19666790/), reached
through NCBI's reference link after an initial challenge, confirms PMID
19666790, the DOI and associated accession FJ347758.

DOI `10.1099/ijs.0.026617-0` is supplied by the raw LPSN row; the inspected
LPSN page identifies the corresponding notification for volume 60, part 5.
Publisher retries timed out and DOI/Crossref requests were inaccessible.
That DOI's live resolution remains unverified, not established as broken.
NCBI and ENA nucleotide requests also failed; FJ347758's attribution is
supported by LPSN, PubMed and the native BacDive sequence object, not by
an independently inspected nucleotide record or sequence analysis.

**BacDive and assembly classification.** Raw BacDive row 55868, the
inspected [BacDive 133557 page](https://bacdive.dsmz.de/strain/133557), and
its native object agree on CL-33's type-strain identity and species
classification. Native genome reference 66792 supplies two explicit
groups of linked identifiers:

- LMG 24815: unversioned GCA_000722565, IMG 2574179789 and PATRIC
  1027273.5, scaffold level, taxon 1027273.
- CL-33: unversioned GCA_001583435, IMG 2687453173 and PATRIC 570277.3,
  chromosome level, taxon 570277.

Both groups are directly attached to this native BacDive record; they
were not joined merely through a shared species name. The YAML retains
their different accession strings, taxids and source evidence. Native
reference 29499 identifies FJ347758 as a partial 16S sequence of CL-33.

**NCBI and BV-BRC.** Native GenBank/RefSeq entries support the versioned
GCA/GCF_000722565.1 pair, LMG 24815, SAMN02851611 and scaffold level.
GenBank supplies PRJNA252578; RefSeq supplies PRJNA224116. Native BV-BRC
1027273.5 supplies GCA_000722565.1, LMG 24815, SAMN02851611 and
PRJNA252578, matching its retained assertions.

The separately inspected CL-33 primary entries support GCA/GCF_001583435.1,
sample SAMN04155633 and taxid 570277. Native BV-BRC 570277.3 likewise
uses CL-33 without a culture collection field. These confirm the BacDive
identifiers, but their bare strain names do not authorize additional
collection-based joins or transfer of the child sample into this record.

**GOLD.** The complete native organism scan for taxid 1027273 finds
Go0095339, explicitly naming LMG 24815. Project Gp0095339 identifies that
organism, PRJNA252578 and SAMN02851611. Analysis Ga0048311 links to that
project and supplies GCA_000722565.1 and IMG 2574179789. Its own organism
field is blank, but the explicit project chain resolves unambiguously.
The two independent culture/strain fields explain repeated provenance
assertions; they are not extra organisms or biological genomes.

**StrainInfo.** Native SI-ID 359550.3 is published online and references
BacDive 133557. It has two own available deposits: LMG 24815 at SI-DP
834936 and BCRC 17933 at SI-DP 854956, both type strains classified as
1027273 with LPSN 788550. The sole sequence object supplies unversioned
GCA_000722565 and explicitly names only SI-DP 834936. The YAML correctly
keeps that assembly attached to LMG 24815, while retaining two typed
deposit and two strain-record assertions with DOI
`10.60712/SI-ID359550.3`. It neither appends `.1` nor transfers the assembly
to the BCRC deposit simply because both share one source strain record.

**Attestations and history.** Raw inventories support NCBI/LPSN one NAME
each, GTDB two GENOME records, BacDive one STRAIN, GOLD one ORGANISM and
Madin 22 TRAIT_ASSERTION records. GOLD and Madin are explicitly direct-
taxon counts, not descendant totals. Scope row 10780 and the seed event
name the same six sources. Status remains SEEDED; this report does not
promote it to human-reviewed status.

## Completeness

No consequential gap was established. The full target subtree's BacDive
membership is represented without a cap. The raw LPSN type list contains
LMG 24815 only, but both recognized deposits and the CL-33 designation
are present on the correctly flagged type strain elsewhere in the YAML.

Ignored-inclusive searches of `data/atb/` found no target strain, retained
sample or species-name match. A separate ignored-inclusive decompressed
search of the complete `data/catalog/allthebacteria.tsv.xz` found no
SAMN02851611 row. No eligible ATB omission is established for the sample
actually linked in this record; this is not a claim that the species has
never appeared in any other ATB release.

Ignored-inclusive target identifier, label and slug searches of `history/`
found no separate entry. The same filename-independent policy was used
to confirm that no report already existed for this exact stem.

Empty optional definition, graph, discussion and curator-evidence fields
are appropriate for this seeded identity record. iModulonDB was not
applicable: no gene, regulator, pathway or expression-module assertion is
made by the YAML. BacDive pathway predictions were not imported or treated
as species-level experimental evidence.

## Findings

None found: 0 blocker, 0 major and 0 minor findings. Unavailable endpoints
and the skipped corpus-wide gate bound the verdict as described above.

## Recommended Edits

None required by the inspected evidence. Preserve the species/descendant
distinction, whole-deposit matching, source-scoped BioProjects and
unversioned BacDive/StrainInfo accessions. Do not hand-edit generated YAML
to add guessed collection-based links for CL-33.

If future authority evidence changes the LPSN projection or GTDB mapping,
the owner is the upstream transform feeding `data/raw/lpsn_names.tsv` or
`data/raw/gtdb_mappings.tsv`, respectively; a generated-record patch is
not the maintained fix.

## Follow-up Checks

1. Retry the GTDB species page, notification DOI and nucleotide authority
   record when accessible. The failed requests do not invalidate the
   independently inspected native and bibliographic evidence.
2. Run `just verify-corpus` before claiming corpus-wide reproducibility.
   Focused schema and inventory checks do not prove that broader property.
3. Any later source refresh should retain both distinct assembly groups
   and rerun focused validators plus deposit-specific StrainInfo checks.

## Additional Notes

This review created only its new report as a manual edit. No taxon YAML,
maintained inventory, scope, curation event, history entry or GitHub item
was changed. The strict validator emitted its normal diagnostic TSV.
Eukaryota was outside the review target.
