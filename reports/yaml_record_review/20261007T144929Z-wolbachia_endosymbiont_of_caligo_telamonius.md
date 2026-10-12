# YAML Record Review: Wolbachia endosymbiont of Caligo telamonius

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_caligo_telamonius.yaml`
- Started UTC: 2026-10-07T14:46:32Z
- Finished UTC: 2026-10-07T14:49:29Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035967`,
Wolbachia endosymbiont of Caligo telamonius.
This species-rank bacterial node has `EXACT` grounding,
`SEEDED` lifecycle, genetic code 11, 11 root-first ancestors,
one NCBI synonym, zero inventoried BacDive strains,
one NCBITAXON name attestation, and one inline seed event.
No nomenclature, mapping, strain/genome, citation, phenotype,
or causal-graph objects are asserted. Seeded fields are
generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_caligo_telamonius.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_caligo_telamonius.yaml --out /private/tmp/wol-ctel-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed source checks passed for identity, every ancestor label/rank/link, synonym, attestation, unique path/scope rows, and seed wording. These bounded checks are not corpus reproduction.
- Live NCBI EFetch/Datasets confirmed the target and two distinct DHJ nodes. Exact Assembly/Nuccore queries and complete metadata/features/references for all 18 returned Nuccore objects were inspected, excluding sequence and translation payloads.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxon IDs and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- NCBI's browser page was unavailable through the web tool; authoritative EFetch XML and Datasets JSON were available.
- Not checked: independent BOLD/protein objects, sequence alignment, the primary paper's Table S2, or exact accession reconciliation of its historical count against current taxonomy.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035967&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035967)
agree on the active taxid, exact label, species rank, bacterial
lineage, and parent `NCBITaxon:2640676`
(unclassified Wolbachia). EFetch confirms code 11 and
synonym Wolbachia sp. Caligo telamonius.

Complete source rows agree at
`data/raw/ncbitaxon_taxa.tsv:222226`,
`data/catalog/ncbi_names-0005.jsonl.gz:31737` and line 31738,
`data/taxa/PATHS.tsv:14724`, and `curation/seed_scope.tsv:322483`.
The native name class `synonym` maps to `EXACT_SYNONYM`
under `src/taxonmech/ncbi_taxdump.py:91`.
This bacterial synonym does not make the host a synonym.

Every ancestor's ID, label, rank, and parent link agrees with
the pinned root-first chain. Datasets supplies root and EFetch
the remaining labeled chain, including Pseudomonadota,
Alphaproteobacteria, Rickettsiales, Anaplasmataceae,
Wolbachieae, and Wolbachia. Snapshot date is 2026-09-13.
Related/broad synonym columns and `retired_into` are empty.
Parsed inventories contain no target child, type-material,
merged-ID, or dropped row.

Two similarly named bacterial nodes remain separate:

- [NCBITaxon:1084940](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1084940&retmode=xml): Wolbachia endosymbiont of Caligo telamoniusDHJ02, with the corresponding Wolbachia sp. synonym.
- [NCBITaxon:1084941](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1084941&retmode=xml): Wolbachia endosymbiont of Caligo telamoniusDHJ03, with the corresponding Wolbachia sp. synonym.

Live EFetch/Datasets and full pinned backbone, scope, and
native-name rows confirm both active species nodes.
Their shared parent and overlapping host-name text do not
establish equivalence with the target. No DHJ sequence is
transferred into the target's exact-taxid evidence set.

## Evidence

The attestation counts one `NAME`, not 18 markers, specimens,
infections, cultures, or genomes. Exact-target raw BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits scans
found no applicable rows. With no backbone descendants,
zero inventoried BacDive strains agrees with the inputs.

The inline seed wording matches scope/inventories.
Its timestamp `2026-09-13T17:54:04Z` is the latest inspected
raw, ATB, and StrainInfo extraction timestamp, as used by
`src/taxonmech/seed.py::_seed_timestamp`.

Exact Nuccore query `txid1035967[Organism:noexp]`
returned 18 partial COI records. Each explicitly carries
`taxon:1035967`, a Caligo telamonius host feature,
Costa Rica locality, and translation table 11:

| Accession | Length (nt) | Specimen voucher | GenBank-reported BOLD cross-reference |
| --- | --- | --- | --- |
| [JF902173.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902173.1) | 657 | `BIOUG<CAN>:MHAAB047-05.w` | `ASLEP012-10.COI-5P` |
| [JF902174.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902174.1) | 657 | `BIOUG<CAN>:MHAAB387-05.w` | `ASLEP015-10.COI-5P` |
| [JF902175.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902175.1) | 561 | `BIOUG<CAN>:MHAAB669-05.w` | `ASLEP016-10.COI-5P` |
| [JF902176.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902176.1) | 657 | `BIOUG<CAN>:MHAAB843-05.w` | `ASLEP017-10.COI-5P` |
| [JF902177.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902177.1) | 657 | `BIOUG<CAN>:MHMYB048-09.w` | `ASLEP075-10.COI-5P` |
| [JF902178.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902178.1) | 657 | `BIOUG<CAN>:MHMYB054-09.w` | `ASLEP076-10.COI-5P` |
| [JF902179.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902179.1) | 657 | `BIOUG<CAN>:MHMYB055-09.w` | `ASLEP077-10.COI-5P` |
| [JF902180.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902180.1) | 657 | `BIOUG<CAN>:MHMYB057-09.w` | `ASLEP078-10.COI-5P` |
| [JF902181.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902181.1) | 657 | `BIOUG<CAN>:MHMYB062-09.w` | `ASLEP079-10.COI-5P` |
| [JF902182.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902182.1) | 626 | `BIOUG<CAN>:MHMYB064-09.w` | `ASLEP080-10.COI-5P` |
| [JF902183.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902183.1) | 657 | `BIOUG<CAN>:MHMYB068-09.w` | `ASLEP081-10.COI-5P` |
| [JF902184.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902184.1) | 623 | `BIOUG<CAN>:MHMYB070-09.w` | `ASLEP082-10.COI-5P` |
| [JF902185.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902185.1) | 657 | `BIOUG<CAN>:MHMYB071-09.w` | `ASLEP083-10.COI-5P` |
| [JF902186.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902186.1) | 657 | `BIOUG<CAN>:MHMYB076-09.w` | `ASLEP084-10.COI-5P` |
| [JF902187.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902187.1) | 657 | `BIOUG<CAN>:MHMYB080-09.w` | `ASLEP085-10.COI-5P` |
| [JF902188.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902188.1) | 657 | `BIOUG<CAN>:MHMYB083-09.w` | `ASLEP086-10.COI-5P` |
| [JF902189.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902189.1) | 657 | `BIOUG<CAN>:MHMYC1259-09.w` | `ASLEP090-10.COI-5P` |
| [JN674110.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674110.1) | 658 | `MHMYG2711-10.w` | `ASWLP044-11.COI-5P` |

The 17 JF records retain Smith's direct submission dated
1 May 2011; JN674110.1 retains 13 September 2011, all at
the University of Guelph. All retain an unpublished
barcoding-manuscript reference. JN674110.1 has codon start 2;
the JF records have codon start 1.
JF902175.1 and JF902176.1 give Margarita collections on
8 and 9 June 2005; JF902189.1 gives Puente Sabalo,
24 December 2008. Other returned records give Costa Rica
without a collection-date feature; dates are not inferred
from voucher suffixes.

BOLD cross-references and CDS protein IDs were read as
GenBank feature values, not independently retrieved objects
or experimentally validated functions. The source contains
different primer combinations and some primer text in notes;
no uniform assay beyond the inspected metadata is assumed.

The relevant
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, reports 23
Caligo telamonius-associated bacterial sequences, comprising
12% of that reported bacterial-sequence set. That percentage
is not host infection prevalence. Its methods describe
insect-barcoding recovery of bacterial COI and refer accession
details to Table S2. The supplement was not inspected.
The paper's historical host-associated count and today's
18 exact-taxid records are not established as the same set.
No missing-five claim, DHJ reassignment, allele identity,
or reproductive phenotype is inferred.

Specimen vouchers are not culture deposits, and partial
markers are not genome assemblies. Neither these markers
nor the paper's count contradict `strain_count: 0` or
the one-name NCBITAXON attestation.
GenBank's unpublished label is preserved as stored, not
taken as proof that no relevant publication exists.

Exact Assembly query `txid1035967[Organism:noexp]`
returned zero with phrase-not-found/no-items diagnostics.
This bounded indexing result is not proof of global or
historical genome absence.

## Completeness

Complete enough for the generated NCBI-only identity purpose.
Optional fields are appropriately empty without applicable
supported objects; externally observed markers do not require
inventing culture or genome relationships.

Ignored-independent search used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
Ignored, hidden, and compressed content was included.
Patterns covered the taxid, host-qualified label, slug,
all 18 Nuccore accessions, voucher stems, and BOLD stems.

All 24 candidate rows were read completely:

- Four describe the target backbone, scope, scientific name, and synonym.
- Eight describe the two distinct DHJ nodes: one backbone, scope, scientific name, and synonym row for each.
- Ten ATB rows at lines 143489-143498 describe Escherichia coli samples SAMEA110359670 through SAMEA110359679; the overlapping digits are not taxonomic matches.
- Two ATB rows at lines 401094-401095 describe Enterococcus cecorum samples SAMEA12751073 and SAMEA12751074; run IDs ERR10359670 and ERR10359671 are numeric collisions.

The expanded marker/voucher/BOLD search returned no new rows.
Five native `SOURCE.json` files were parsed completely and
history filenames were searched independently.
No additional applicable local assertion, culture deposit,
strain-genome link, or standalone history artifact was found
within these bounded roots. No global absence claim is made.

iModulonDB is not applicable: no regulator, expression module,
or transcriptomic dataset is asserted. COI barcoding context
is not expression-module evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, synonym class/source, lineage,
attestation unit, zero BacDive inventory count, optional
omissions, and seed provenance are supported.

## Recommended Edits

None required. Preserve generated YAML and `mapping_status: SEEDED`.
This review does not authorize lifecycle promotion or a
curation-history event.

Future source corrections belong to maintained inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
name-class handling belongs to `src/taxonmech/ncbi_taxdump.py`,
and scope changes to `curation/seed_scope.tsv`.
Do not patch generated YAML/pages. Optional enrichment must
preserve exact taxid, accession version, voucher scope, and
the separation from the two DHJ nodes.

## Follow-up Checks

No corrective follow-up is required. Before optional literature
enrichment, inspect Table S2 and resolve its individual
accessions against current taxonomy. Keep the historical paper
count, current exact-taxid marker count, source-name attestation,
and culture/genome counts separate.

After separately authorized maintained-input changes, rerun the
owning generator, per-file schema/strict validation, and applicable
full-corpus acceptance gates. New curated history requires
`just validate-history`; new graph terms/evidence require
`just validate-products`.

## Additional Notes

The complete YAML was reread and remained byte-identical before
report creation. All bounded source reads and public retrievals
reached terminal results. No YAML, source inventory, lifecycle,
standalone history, generated page, GitHub state, branch, or
worktree was changed. Eukaryota records were not re-reviewed.
Only this new timestamped report is authorized.
