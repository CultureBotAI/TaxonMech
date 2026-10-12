# YAML Record Review: Proteus penneri

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/proteus_penneri.yaml`
- Started UTC: 2026-10-03T12:00:13Z
- Finished UTC: 2026-10-03T12:07:29Z
- Verdict: pass with minor issues

## Target

Generated `TaxonRecord` for `NCBITaxon:102862`, Proteus penneri, rank
`SPECIES`, domain `BACTERIA`, parent `NCBITaxon:583` (Proteus).
Grounding is `EXACT`; mapping status remains `SEEDED`.

Read all 2,412 lines' parsed content: all root fields, all strain scalars,
and every assembly, genome and related-record object. Long repeated lists
were inspected as lossless common-field/column tables, with reconstruction
assertions confirming that no field or row was omitted. This was not sampling.
There are 16 BacDive strains, 18 assembly assertions, 15 genome assertions
and 118 related-record assertions. Repeated accessions preserve distinct
source and matching-field provenance; these are not counts of unique genomes.

The record is generated from raw inventories and the ATB/StrainInfo overlays.
No record, source, history, mapping status or generated page was changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/proteus_penneri.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/proteus_penneri.yaml` | PASS; one file, zero errors. |
| Full lineage and BacDive subtree comparison | PASS; nine ancestors and all 16 strain rows agree with the local inventories. |
| Raw strain-link equality | PASS; 16 assemblies, 14 genomes and 59 related records match their complete raw objects. |
| StrainInfo overlay equality | PASS; two assemblies and 59 related records match the overlay objects. |
| ATB overlay comparison | PASS; all assembly metadata, release/identifier fields and both complete BioSample evidence links match. |
| `just verify-corpus` | Not run: documented full-corpus reproduction check, not a focused single-record validator. Source-object comparisons above do not replace it. |
| `just validate-history` | Not run: ignored-inclusive identifier/label/slug search found no target-specific standalone history entry. Embedded seed history was checked by strict validation. |
| Graph and generated-product checks | Not run: no causal graph is asserted; pages and other generated products were outside this record review. |

Schema and strict validation are not substitutes for external reference
verification. Authority pages and source snapshots were inspected as below;
not every accession or deposit DOI was independently fetched from a live resolver.

## Identity and Grounding

The inspected [NCBI Taxonomy detail page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=102862&lvl=&mode=node)
agrees on species identity, genetic code 11, parent and lineage. The local
subtree contains this taxon and child `NCBITaxon:471881` (ATCC 35198).
The record does not confuse that child with the type strain ATCC 33519.

[LPSN record 779878](https://lpsn.dsmz.de/species/proteus-penneri)
supports the name, 1983 authority, correct-name status and marker FJ971869.
All six listed registered collection designations agree. One additional
source designation is missing from the nomenclature list; see finding M1.

The GTDB mapping remains `skos:closeMatch`, not identity of strain or tree.
All 42 native `s__Proteus_penneri` members were inspected: 25 have NCBI taxid
102862, one has 471881, and 16 have other NCBI taxids. The representative is
`RS_GCF_003144535.1`, ATCC 33519. The count is species-cluster scoped and
correctly differs from the number of matching strain records. GTDB's
Enterobacteriaceae placement does not replace NCBI's Morganellaceae lineage.

All four exact synonyms trace to the NCBI inventory; the authority-bearing
name is retained as related. The original description also supports the
historical biogroup/indole-negative names. No phenotype was inferred from a
synonym or generalized from a strain to the species.

## Evidence

**Nomenclature and publications.** The inspected
[original publisher page](https://journals.asm.org/doi/10.1128/jcm.15.6.1097-1102.1982)
confirms the paper, DOI, PMID 7050147 and type designation 1808-73 = ATCC 33519.
The [Validation List 10 publisher page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-33-2-438)
confirms its citation metadata. The 1982 description and 1983 authority are
not contradictory: LPSN explains that a subsequent correction treated the
name as validly published in List 10. List 11 itself was not independently read.

**BacDive.** Inspected all 16 native identity, culture-collection, literature
and sequence objects. IDs are 5065, 136383, 136384, 143745, 143746, 144519,
144790, 147312, 149549, 156147, 174548, 174549, 174550, 174551, 174552 and
174553. Their deposited culture identifiers and source taxids agree with
the YAML. The [BacDive 5065 identity section](https://bacdive.dsmz.de/strain/5065)
independently supports the type strain, designation and deposit list, and
lists the same 15 other strains. Individual live pages for those 15 were
not opened. Only 5065 has native sequence objects; this is not a claim that
the others lack genomes elsewhere.

**Assembly chains.** Native BacDive, BV-BRC, GOLD, NCBI and GTDB objects
support the assertions at their stated source fields. Key chains are:

| Deposit | Assembly/sample | Supporting source chain |
| --- | --- | --- |
| ATCC 33519 | GCA_003144535.1; SAMN07977613 | BV-BRC 102862.7; GOLD Go0033079 / Gp0370147 / Ga0336153; NCBI; GTDB representative. |
| NCTC 12737 | GCA_900455015.1; SAMEA2548146 | BV-BRC 102862.13; GOLD Go0622210 / Gp0818768 / Ga0668063; BacDive and StrainInfo. |
| DSM 4544 | GCA_016028675.1; SAMN13450404 | BV-BRC 102862.20; GOLD Go0575814 / Gp0550543 / Ga0490977; BacDive. |

Read six native NCBI GenBank/RefSeq objects, including paired accessions,
BioSamples, project IDs, assembly levels and source strain strings.
The NCTC compact string and FDAARGOS_874 do not pass the current whole-culture
identifier parser; the YAML correctly relies on explicit matched deposits
from other sources instead of manufacturing those NCBI/GTDB strain joins.
Unversioned BacDive and StrainInfo assembly accessions remain source-faithful.

**GOLD.** Read all 19 referenced native objects (13 organisms, three projects,
three analyses). All 54 GOLD assertions pass field, taxid and chain checks.
Organism links for the analysis rows resolve through their projects.
IMG identifiers 2858358578 and 8117433022 are supported; the FDAARGOS_874
chain has no native IMG identifier and the record does not invent one.

**StrainInfo.** Read all 16 rich source records and checked all 61 assertions
against their own matched deposit, sequence, status, DOI and taxid fields.
Type-strain record 10834.3 supplies ten matching deposits, five nucleotide
records and two assemblies. The five nucleotide records are DQ836272,
AY370857, FJ971869, LN809884 and DQ885258; their rpoB, gyrB or 16S descriptions
are retained as sequence metadata, not as inferred functional observations.
StrainInfo 108253.2 classifies CCUG 25463 only as Proteus, taxid 583. The
YAML preserves that source taxid alongside BacDive/GOLD's species-level
classification; it does not silently promote the StrainInfo assignment.
ATCC 35198 in source record 40916.2 and ATCC 35197 in 40915.2 are not matching
local culture identifiers. Group membership alone does not justify importing
their assemblies into the CCUG/CIP strain entries.

**AllTheBacteria.** The full compressed native table supports
`atb.assembly:202505.SAMN13450404`, dataset r0.2, run SRR12047298, analysis
ERZ25690845, checksum, PASS filters and exact archive/download locations.
Both BioSample links match the raw BV-BRC/GOLD related-record objects and
the committed ATB crosswalk. SAMEA2548146 is present as NOT_PROCESSED;
SAMN07977613 was not found in that full native table. Neither warrants
an additional ATB assembly assertion. Archive payloads were not downloaded.

**Attestations.** Raw inventory rows support counts of one NCBI name, one
LPSN name, 42 GTDB genomes, 16 BacDive strains, four MediaDive media,
41 GOLD organisms and five MADIN trait assertions. MediaDive IDs are 1,
693, 92 and J12. The last three source counts explicitly exclude descendant
taxa. These heterogeneous units are not summed or promoted into detailed
growth/trait claims; the GOLD count is the KGX inventory count, not the
number of native GOLD objects joined to the included deposits.

## Completeness

All 16 BacDive strains are included, without a hidden cap. The sole material
gap found is the bounded nomenclature-provenance issue M1. Optional trait,
mechanism and causal-graph slots are appropriately unfilled for this seed.

Identifier, label and slug searches included ignored and hidden files in
raw inventories, curation and history. Native compressed files were searched
with decompression or fully scanned with structured parsers. No standalone
target history or existing review report was found; the scope and legacy-path
rows do exist. These searches do not establish absence from external databases.

## Findings

Counts: **0 blocker, 0 major, 1 minor**.

**M1 - Minor: one source type designation is missing from nomenclature.**
`nomenclature[0].type_strain_designations` at YAML lines 50-56 has six entries
but omits CDC 1808-73, which the inspected LPSN page lists. NCBI's local
`data/raw/ncbi_type_material.tsv:1418` independently retains it. The BacDive
section already carries `kgmicrobe.strain:CDC%201808-73` at YAML line 98,
so the strain identity and true type-strain flag are not in doubt.

The omission is already present in `data/raw/lpsn_names.tsv:19187`.
`src/taxonmech/seed.py:405` faithfully projects that list. Future ownership
is the upstream KG-Microbe LPSN transform supplying type-designation edges,
consumed by `src/taxonmech/extract.py:445`; the exact upstream loss stage
was not established from the available inputs. This finding does not authorize
treating CDC as a newly approved culture registry or widening genome joins.

## Recommended Edits

1. In a separate curation change, inspect the maintained upstream LPSN
   transform and its source row for 779878. Preserve the omitted source
   designation, or document an intentional restriction on the represented
   list. If the current collection-ID model cannot express it faithfully,
   choose a provenance-preserving representation before changing normalization.
2. After an authorized upstream correction, use `just extract-inventory`
   with the configured source checkout, then dry-run `just seed` and run
   `just seed-canary NCBITaxon:102862`. Do not hand-edit the generated YAML
   or raw inventory to conceal the discrepancy. Leave unrelated joins and
   source-specific taxonomic differences unchanged.

## Follow-up Checks

- Compare the revised LPSN row and generated type-designation list with the
  authority page, preserving all six existing registered deposits.
- Add a focused regression at the maintained transform/extraction boundary;
  verify that preserving this designation does not relax culture matching.
- Rerun both exact record validators above. Before merging a curation change,
  run `just verify-corpus` and the appropriate source/provenance tests.
- Retry unavailable live endpoints only to resolve remaining access limits,
  not as grounds to infer that a referenced record does not exist.

## Additional Notes

The structured iModulonDB datasets command was attempted through the installed
`kg-microbe-sources` runner because gene names occur in sequence descriptions.
It failed with DNS access to the datasets endpoint. A direct API attempt also
failed and targeted site search yielded no usable coverage result. No claim
of iModulonDB absence or functional support follows from those failures.

The GTDB taxon page, live FJ971869 nucleotide page and live StrainInfo 108253
page were unavailable. Native snapshots supplied the bounded checks above.
The original PubMed page did not provide usable article text; the inspected
publisher page supplied publication metadata and abstract instead. The
configured archived NCBI taxdump was unavailable locally; lineage comparison
used the inventory plus the live NCBI page, not a re-extraction of that archive.

Native checks used `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/straininfo/` and `data/atb/`, without rebuilding indexes
or refreshing source snapshots. The review does not certify unrelated source
records, the entire corpus or the published site. Review status was not promoted.
