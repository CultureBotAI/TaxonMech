# YAML Record Review: Wolbachia endosymbiont of Anacrusis nephrodes

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_anacrusis_nephrodes.yaml`
- Started UTC: 2026-10-07T14:38:04Z
- Finished UTC: 2026-10-07T14:40:48Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035965`,
Wolbachia endosymbiont of Anacrusis nephrodes.
This is a species-rank bacterial node with `EXACT` grounding,
`SEEDED` lifecycle, genetic code 11, 11 root-first ancestors,
one NCBI synonym, zero inventoried BacDive strains, one
NCBITAXON name attestation, and one inline seed event.
No nomenclature, mapping, strain/genome, citation, phenotype,
or causal-graph objects are asserted. Seeded fields are
generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_anacrusis_nephrodes.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_anacrusis_nephrodes.yaml --out /private/tmp/wol-aneph-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed source checks passed for identity, every ancestor label/rank/link, synonym, attestation, unique path/scope rows, and seed wording. These bounded checks do not substitute for corpus reproduction.
- Live NCBI taxonomy, exact Assembly/Nuccore indexes, and all 16 returned Nuccore records' metadata/features/references were inspected. Sequence and translation payloads were excluded.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxon identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- NCBI's browser page was unavailable through the web tool; authoritative EFetch XML and Datasets JSON were available.
- Not checked: independent BOLD/protein records, sequence alignment, or supplementary Table S2 of the contextual primary publication.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035965&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035965)
agree on the active taxid, exact label, species rank, bacterial
lineage, and parent `NCBITaxon:2640676`
(unclassified Wolbachia). EFetch confirms genetic code 11
and synonym Wolbachia sp. Anacrusis nephrodes.

Complete local rows agree at
`data/raw/ncbitaxon_taxa.tsv:222224`,
`data/catalog/ncbi_names-0005.jsonl.gz:31734` and line 31735,
`data/taxa/PATHS.tsv:14722`, and `curation/seed_scope.tsv:322481`.
The native name class is `synonym`, mapped to
`EXACT_SYNONYM` by `src/taxonmech/ncbi_taxdump.py:91`.
This is a bacterial-name synonym, not equivalence to the host.

Every ancestor's ID, label, rank, and parent link agrees with
the pinned root-first chain. Datasets supplies root and
EFetch the remaining labeled chain, including Pseudomonadota,
Alphaproteobacteria, Rickettsiales, Anaplasmataceae, Wolbachieae,
and Wolbachia. Snapshot date is 2026-09-13.
Related/broad synonym columns and `retired_into` are empty.
Parsed inventories contain no target child, type-material,
merged-ID, or dropped row.

The nearby
[Anacrusis nephrodesDHJ05 endosymbiont](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1084939&retmode=xml)
is a separate active species node, `NCBITaxon:1084939`.
Live EFetch/Datasets and full pinned backbone, scope, and
native-name rows agree. Shared parent and overlapping
host-name text do not justify merging them or transferring
their sequence evidence.

## Evidence

The attestation counts one `NAME`, not 16 marker records,
infections, strains, or genomes. Exact-target raw BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits scans
found no applicable rows. With no backbone descendants,
zero inventoried BacDive strains agrees with the inputs.

The seed wording matches scope/inventories. The inline
timestamp `2026-09-13T17:54:04Z` equals the latest inspected
extraction timestamp from the raw, ATB, and StrainInfo manifests,
as required by `src/taxonmech/seed.py::_seed_timestamp`.

Exact Nuccore query `txid1035965[Organism:noexp]`
returned 16 records. All are partial bacterial COI markers
with explicit `taxon:1035965` source cross-references,
Anacrusis nephrodes host features, Costa Rica locality
features, and translation table 11:

| Accession | Length (nt) | Specimen voucher | GenBank-reported BOLD cross-reference |
| --- | --- | --- | --- |
| [JF902165.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902165.1) | 646 | `BIOUG<CAN>:MHMXF059-07.w` | `ASLEP068-10.COI-5P` |
| [JN674095.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674095.1) | 469 | `MHMYD211-09.w` | `ASWLP035-11.COI-5P` |
| [JN674096.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674096.1) | 658 | `MHMYD206-09.w` | `ASWLP034-11.COI-5P` |
| [JN674097.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674097.1) | 614 | `MHMYD204-09.w` | `ASWLP033-11.COI-5P` |
| [JN674098.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674098.1) | 614 | `MHMYD202-09.w` | `ASWLP032-11.COI-5P` |
| [JN674099.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674099.1) | 614 | `MHMYD201-09.w` | `ASWLP031-11.COI-5P` |
| [JN674100.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674100.1) | 658 | `MHMYD196-09.w` | `ASWLP030-11.COI-5P` |
| [JN674101.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674101.1) | 658 | `MHMYD192-09.w` | `ASWLP029-11.COI-5P` |
| [JN674102.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674102.1) | 658 | `MHMYD191-09.w` | `ASWLP028-11.COI-5P` |
| [JN674103.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674103.1) | 658 | `MHMXZ2174-09.w` | `ASWLP024-11.COI-5P` |
| [JN674104.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674104.1) | 658 | `MHMXZ2162-09.w` | `ASWLP023-11.COI-5P` |
| [JN674105.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674105.1) | 626 | `MHMXZ2150-09.w` | `ASWLP022-11.COI-5P` |
| [JN674106.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674106.1) | 614 | `MHMXZ2127-09.w` | `ASWLP021-11.COI-5P` |
| [JN674107.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674107.1) | 658 | `MHMXZ2112-09.w` | `ASWLP020-11.COI-5P` |
| [JN674108.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674108.1) | 589 | `MHMXF061-07.w` | `ASWLP018-11.COI-5P` |
| [JN674109.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674109.1) | 454 | `MHMXF046-07.w` | `ASWLP017-11.COI-5P` |

The 15 JN records were submitted on 13 September 2011;
JF902165.1 was submitted on 1 May 2011, all through Smith
at the University of Guelph. They retain an unpublished
barcoding-manuscript reference. JN-record locality details
include named sites in Area de Conservacion Guanacaste;
JF902165.1 gives Costa Rica. Collection dates are not present
in every object, and none are inferred from voucher suffixes.

These are specimen-associated sequence submissions, not
culture deposits or genome assemblies. Sixteen markers do
not prove 16 distinct cultured Wolbachia strains, and the
host-qualified taxonomy name does not establish host-wide
infection prevalence. BOLD cross-references and CDS protein
identifiers were inspected as GenBank feature values, not
independently retrieved or experimentally validated objects.

The matching-title
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, provides contextual
methods for bacterial COI recovered during insect barcoding.
The inspected methods explain the .w specimen suffix and
place accession details in supplementary Table S2.
The main-text search did not find Anacrusis; Table S2 was
not inspected. No accession-specific allele, reproductive
phenotype, or prevalence conclusion is transferred to this
record. GenBank's unpublished metadata is preserved as stored,
not treated as proof that no relevant paper exists.

Exact Assembly query `txid1035965[Organism:noexp]`
returned zero with phrase-not-found/no-items diagnostics.
This is a bounded index result, not proof of global or
historical genome absence.

## Completeness

Complete enough for the generated NCBI-only identity purpose.
Optional fields are appropriately empty without applicable
supported objects. External marker evidence does not
contradict the BacDive inventory count.

Ignored-independent search used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
Ignored, hidden, and compressed content was included.
Patterns covered the taxid, host-qualified label, slug,
all 16 marker accessions, voucher stems, and BOLD stems.

All 30 candidate rows were read completely:

- Four describe the target backbone, scope, scientific name, and synonym.
- Three describe the distinct DHJ05 node: backbone, scope, and scientific name.
- GOLD analysis `Ga0653413` describes Salmonella enterica enterica sv. Kirkee 265723; IMG taxon `8103596533` is a numeric collision.
- GenBank `GCA_041035965.1` describes Klebsiella pneumoniae zj01149, taxid 573.
- GenBank `GCA_021035965.1` describes Escherichia coli PP379, taxid 562.
- GenBank `GCA_051035965.1` and historical RefSeq `GCF_051035965.1` describe Vibrio parahaemolyticus VP19192, taxid 670. The inspected RefSeq row is suppressed; neither accession concerns Wolbachia.
- Ten ATB rows at lines 143469-143478 describe Escherichia coli samples SAMEA110359650 through SAMEA110359659.
- Seven ATB rows at lines 401081-401087 describe Enterococcus cecorum samples SAMEA12751060 through SAMEA12751066; their run IDs contain the numeric substring.
- ATB line 990911 describes Acinetobacter baumannii sample `SAMEA9800634`, run `ERR10471773`, assembly `ERZ25455382`; the match occurs in a sequence checksum.

The expanded marker/voucher/BOLD search returned no new rows.
Five native `SOURCE.json` files were parsed completely and
history filenames were searched independently.
No additional applicable local assertion, culture deposit,
strain-genome link, or standalone history artifact was found
within these bounded roots. No global absence claim is made.

iModulonDB is not applicable: the identity record has no
regulator, expression module, or transcriptomic dataset;
COI barcoding context is not expression-module evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, synonym class/source, lineage,
attestation unit, zero BacDive inventory count, optional
omissions, and seed provenance are supported.

## Recommended Edits

None required. Preserve generated YAML and `mapping_status: SEEDED`.
This review does not authorize status promotion or a
curation-history event.

Future source corrections belong to maintained inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
taxonomy name-class handling belongs to
`src/taxonmech/ncbi_taxdump.py`, and scope changes to
`curation/seed_scope.tsv`. Do not patch generated YAML/pages.
Any optional enrichment must preserve the target/DHJ05
distinction and exact specimen/accession scope.

## Follow-up Checks

No corrective follow-up is required. For optional publication
enrichment, inspect exact accession/voucher rows in Table S2
and authoritative BOLD objects. Do not derive culture counts,
genome counts, or host-wide effects from these markers.

After separately authorized maintained-input changes, rerun
the owning generator, per-file schema/strict validation, and
applicable full-corpus acceptance gates. New curated history
requires `just validate-history`; new graph terms/evidence
require `just validate-products`.

## Additional Notes

The complete YAML was reread and remained byte-identical
before report creation. All bounded source reads and public
retrievals reached terminal results. No YAML, source inventory,
lifecycle, standalone history, generated page, GitHub state,
branch, or worktree was changed. Eukaryota records were not
re-reviewed. Only this new timestamped report is authorized.
