# YAML Record Review: Microscilla marina

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microscilla_marina.yaml`
- Started UTC: 2026-10-03T10:48:05Z
- Finished UTC: 2026-10-03T10:50:33Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1027`, Microscilla marina, rank
SPECIES, domain BACTERIA, parent `NCBITaxon:1023`. The complete 690-line
YAML was read before judgment. It has EXACT grounding, SEEDED mapping
status, one LPSN nomenclature entry, one retained BacDive strain, five
source attestations and an embedded seed event.

The review concerns this species record only. Its descendant strain and
native source records were inspected as provenance, not independently
assigned record-level review verdicts.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/microscilla_marina.yaml` | PASS; no issues found, exit 0. |
| `just validate-strict data/taxa/bacteria/microscilla_marina.yaml` | PASS; one file, zero ERROR rows, exit 0. |
| `just verify-corpus` | Not run: full-corpus reproduction comparison; no focused record selector. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs. |
| `just validate-history` | Not run: ignored-inclusive identifier, label and slug search of `history/` found no target history entry. Strict validation covered the embedded event. |

Additional read-only checks passed:

- All eleven ancestor labels/ranks and the parent chain match the pinned
  taxonomy table. Descendant traversal yields only this species and strain
  313606, Microscilla marina ATCC 23134.
- Complete BacDive inventory membership for that subtree is exactly the
  retained BacDive 3813 entry.
- Exact assertion-multiset comparisons reproduce all ten assemblies, eight
  genome records and thirty related records from the raw/StrainInfo tables.
- All 44 assertions carrying a matched culture ID reference an existing
  deposit of this strain and pass the repository CAFI culture-key recognition.
- All seven StrainInfo assertions match their native deposit, status,
  classification, record-version DOI and BacDive reference. The assembly
  accession is explicitly attached to the same matched deposit.

These diagnostics verify provenance and shape, not sequence identity,
experimental properties or full-corpus reproducibility.

## Identity and Grounding

Raw taxonomy row 798 agrees with the species identity, parent, code 11,
related authority strings and taxonomy snapshot. The inspected
[NCBI species detail page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1027&lvl=&mode=node)
confirms species rank, code 11, the name, type-culture identifiers and the
lineage through Cytophagia, Cytophagales and Microscillaceae. The separate
tree view places ATCC 23134 beneath the species.

[LPSN 778233](https://lpsn.dsmz.de/species/microscilla-marina) supports the
current name, Approved Lists standing, the listed 1969/2016 emendations,
five type-strain designations and AB078080. The YAML's authority string
includes emendations that the source page presents separately; this does
not change the taxon identity.

The two NCBI related synonyms are source authority strings, not new exact
taxon equivalences. Their placement agrees with the native names catalog.
The GTDB species xref is supported by the LPSN raw mapping and the native
type-genome classification. It is not a strain-level identity inflation.

## Evidence

**Taxonomy, names and scope.** Native NCBI names contain the scientific name
and the two authority-class entries retained as RELATED_SYNONYM. Raw row
64062 confirms that taxid 313606 is the species' child. Type-material rows
1361-1371 corroborate ATCC 23134, DSM 4236, IFO 16560, LMG 18923 and NBRC
16560 with source syntax variants.

The scope entry, `curation/seed_scope.tsv` row 23281, describes four direct
attesting sources. The YAML adds the descendant-derived BacDive attestation,
so the five-source embedded seed-event list is not an unexplained count
discrepancy. Mapping status correctly remains SEEDED.

**Bibliography and sequence accession.** Raw LPSN row 18339 supplies both
DOIs, PMID 14824478 and AB078080. The publisher's
[Approved Lists page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-30-1-225)
resolves the 1980 reference. The publisher's
[1951 Pringsheim article page](https://www.microbiologyresearch.org/content/journal/micro/10.1099/00221287-5-1-124)
resolves the second DOI and supports the historical description context.
The original article PDFs were not inspected.

PubMed returned a browser challenge and its alternate format request
failed, so PMID metadata could not be independently verified there.
AB078080 appears on the inspected LPSN page and in both native BacDive and
StrainInfo records as the IFO 16560 16S sequence. NCBI nucleotide and ENA
fetches failed; no claim is made to have inspected its sequence bases.

**BacDive identity.** The exact native BacDive 3813 object and the retrieved
[BacDive strain page](https://bacdive.dsmz.de/strain/3813) agree on SIO-8,
DSM 4236, ATCC 23134 and NCMB 1400. The source lists species 1027 and strain
313606; using the more specific strain taxid for `classified_as` is supported.
The type flag also follows the overlap with LPSN's type designations.

The web page is an older source rendering than the native 2026 record;
matching identity fields were used as corroboration, not evidence that all
page content is current. Neither the page's phenotypes nor its computational
pathway predictions were imported into the taxon review as biological claims.

**Assembly and genome assertions.** Nine raw assembly assertions plus one
StrainInfo assertion account for the ten listed assemblies. The accession
forms are GCA_000169175, GCA_000169175.1 and GCF_000169175.1. Distinct source
and match-field assertions are retained instead of counted as unique genomes.

Native NCBI GenBank and RefSeq objects identify the paired versioned
assemblies as type-material contig assemblies, under ATCC 23134 and taxid
313606, with BioSample SAMN02436130. GenBank carries PRJNA13411; RefSeq
carries PRJNA224116. The YAML preserves the different project references.

Native BV-BRC 313606.3 independently supplies its ATCC culture and strain
fields, GCA_000169175.1, SAMN02436130 and PRJNA13411. The native BacDive
genome section supplies IMG 2636416090 and BV-BRC 313606.3 with the assembly,
plus a separate IMG 640196209 entry marked complete. The latter is retained
with its own source-provided level, not converted into an NCBI assembly or
asserted equivalent to every other identifier on the strain.

**GOLD provenance.** The native chain is Go0001596 -> Gp0001596 ->
Ga0097828. It explicitly supports ATCC 23134, the NCBI assembly, IMG
2636416090, PRJNA13411 and SAMN02436130. Culture-collection and strain-field
matches are separate retained assertions. Native Go0620367 supplies NCMB
1400 and Go0620368 supplies DSM 4236, both directly classified under 1027.

A complete native-organism scan found three objects directly under 1027:
Go0620366, Go0620367 and Go0620368. This agrees with the raw GOLD count of
three. Go0620366 has the bare designation SIO-8 but no culture accession;
its omission from strain-linked related records is correct under the
culture-identifier matching contract. Go0001596 is classified under 313606
and is not included in the direct-species count.

**GTDB representation.** The exact native cluster contains one genome,
RS_GCF_000169175.1, with ATCC 23134, taxid 313606 and species taxid 1027.
It supplies the retained strain genome, both assembly identifiers, BioSample
and RefSeq project references. Its GTDB class is Bacteroidia, while the
carried NCBI lineage uses Cytophagia; classifications are not reconciled here.

`data/raw/gtdb_species.tsv` row 121730 contains this species and count 1.
The crosswalk row 263342 targets strain 313606, not species 1027. Therefore
the species YAML's GTDB xref comes from the LPSN mapping, while no direct
GTDB taxonomy-mapping row or attestation is emitted. That is consistent
with the inspected inputs, not evidence that the GTDB taxon is absent.
The live GTDB page could not be retrieved.

**StrainInfo.** Native SI-ID 10158.3, DOI 10.60712/SI-ID10158.3, is published
online and references BacDive 3813. All three retained deposits are available
and classified under species 1027:

| Deposit | Designation | Retained sequence |
| --- | --- | --- |
| 39951 | ATCC 23134 | Unversioned GCA_000169175, explicitly linked to this deposit. |
| 39952 | DSM 4236 | None attached to this deposit in the native object. |
| 158710 | NCMB 1400 | None attached to this deposit in the native object. |

The six related assertions are the deposit and strain-record references for
those three matches. AB078080 belongs to IFO deposit 278490; AB681071 belongs
to NBRC deposit 487807. Neither was transferred onto a different matched
deposit. Dead LMG 13022 and additional live deposits in the group were not
automatically added to BacDive's culture list. NCMB was not rewritten to
NCIMB. These are correct source boundaries, not missing-genome findings.

**AllTheBacteria and other counts.** Ignored-inclusive searches found no
SAMN02436130 entry in `data/atb/` or the complete compressed
`data/catalog/allthebacteria.tsv.xz`. No ATB genome is asserted. This absence
is limited to the inspected local snapshot, not every future ATB release.
Madin's two trait assertions match its raw inventory count; no phenotype
is inferred from that number. The raw BacDive medium count is zero and the
YAML does not invent a positive count from the retrieved page.

## Completeness

The entire BacDive-classified subtree is represented by the single retained
strain. All raw and overlay assertion multisets match the YAML. Counts are
source-specific and are not summed as if they were unique biological objects.

Definition, causal graph, discussion and record-level evidence are optional
for this seeded record. No unsupported mechanism or phenotype was added to
fill those slots. iModulonDB is not applicable to the identity/provenance
claims being reviewed; no expression-module claim is present.

Absence searches included ignored files: target ID, label and slug in the
raw inventories, curation and history; exact report stems; compressed native
catalogs; and the full local ATB XZ for the known sample. There was no prior
exact-stem report or target history entry in the searched locations.
Unavailable live endpoints and original article full texts are verification
limits, not evidence that those references do not exist.

## Findings

None found. Counts: 0 blocker, 0 major, 0 minor.

The pass is bounded to the inspected record, source inventories, native
objects and accessible authority pages. It is not a full-corpus gate, a
sequence-content audit, or experimental validation of strain properties.

## Recommended Edits

None required by this review. Do not manually edit the generated taxon,
inflate the culture list from StrainInfo grouping, replace NCMB with NCIMB,
or collapse source-specific genome and project assertions.

Any future source correction belongs in its maintained extractor, seeder
or upstream authority, followed by regeneration, not in this generated YAML.

## Follow-up Checks

- Retry PubMed 14824478, the AB078080 sequence authority and live GTDB when
  accessible; preserve snapshot and accession-version distinctions.
- Run `just verify-corpus` for a future full-corpus reproducibility claim.
- After any authorized source refresh, rerun both record validators and
  check the same deposit-level sequence associations and GOLD source chains.

## Additional Notes

No source, record, history, mapping status or GitHub state was changed.
The strict validator writes its standard validation TSV under `reports/`.
This timestamped Markdown report is the only manually authored artifact
from this record review. Eukaryota was not reopened.
