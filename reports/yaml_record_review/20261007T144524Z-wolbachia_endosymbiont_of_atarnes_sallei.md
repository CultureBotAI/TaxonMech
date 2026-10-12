# YAML Record Review: Wolbachia endosymbiont of Atarnes sallei

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_atarnes_sallei.yaml`
- Started UTC: 2026-10-07T14:43:12Z
- Finished UTC: 2026-10-07T14:45:24Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035966`,
Wolbachia endosymbiont of Atarnes sallei.
It is a species-rank bacterial NCBI node with `EXACT` grounding,
`SEEDED` lifecycle, genetic code 11, 11 root-first ancestors,
zero inventoried BacDive strains, one NCBITAXON name attestation,
and one inline seed event. No synonyms, nomenclature, mappings,
strain/genome links, citations, phenotypes, or causal graph are
asserted. Seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_atarnes_sallei.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_atarnes_sallei.yaml --out /private/tmp/wol-asall-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed source checks passed for identity, every ancestor label/rank/link, empty synonyms, attestation, unique path/scope rows, and seed wording. These bounded checks are not corpus reproduction.
- Live NCBI EFetch/Datasets and exact Assembly/Nuccore queries were inspected. Complete metadata/features/references for all four returned Nuccore objects were read, excluding sequence and translation payloads.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxon IDs and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- NCBI's browser page was unavailable through the web tool; authoritative EFetch XML and Datasets JSON were available.
- Not checked: independent BOLD/protein records, sequence alignment, or the contextual primary paper's supplementary Table S2.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035966&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035966)
agree on the active taxid, exact label, species rank, bacterial
lineage, and parent `NCBITaxon:2640676`
(unclassified Wolbachia). EFetch confirms code 11 and lists
no other names.

Complete local rows agree at
`data/raw/ncbitaxon_taxa.tsv:222225`,
`data/catalog/ncbi_names-0005.jsonl.gz:31736`,
`data/taxa/PATHS.tsv:14723`, and `curation/seed_scope.tsv:322482`.
All synonym columns and `retired_into` are empty.
Snapshot date is 2026-09-13. Parsed inventories contain
no target child, type-material, merged-ID, or dropped row.

All 11 ancestor IDs, labels, ranks, and links match the pinned
root-first chain. Datasets supplies root and EFetch the remaining
labeled chain, including Pseudomonadota, Alphaproteobacteria,
Rickettsiales, Anaplasmataceae, Wolbachieae, and Wolbachia.

The record denotes a host-qualified bacterial node, not the
Atarnes sallei host itself, a culture deposit, or a statement
that all members of that host species carry the same infection.

## Evidence

The attestation counts one `NAME`, not specimens, infections,
sequences, or genomes. Exact-target raw BacDive, LPSN, GTDB,
GOLD, MediaDive, Madin, and BactoTraits scans found no applicable
rows. With no backbone descendants, zero inventoried BacDive
strains agrees with the inputs.

The inline seed wording matches scope/inventories.
Its timestamp `2026-09-13T17:54:04Z` is the latest inspected
extraction timestamp among the raw, ATB, and StrainInfo manifests,
as used by `src/taxonmech/seed.py::_seed_timestamp`.

Exact Nuccore query `txid1035966[Organism:noexp]`
returned four partial COI records, all 657 nt, explicitly
linked to `taxon:1035966`, with host Atarnes sallei,
translation table 11, and codon start 1:

| Accession | Specimen voucher | GenBank-reported BOLD cross-reference | Collection date |
| --- | --- | --- | --- |
| [JF902166.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902166.1) | `BIOUG<CAN>:MHAHD837-05.w` | `ASLEP030-10.COI-5P` | 12 April 2004 |
| [JF902167.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902167.1) | `BIOUG<CAN>:MHAHD839-05.w` | `ASLEP031-10.COI-5P` | 26 September 2004 |
| [JF902168.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902168.1) | `BIOUG<CAN>:MHAHD842-05.w` | `ASLEP032-10.COI-5P` | 19 January 2005 |
| [JF902169.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902169.1) | `BIOUG<CAN>:MHAHE374-05.w` | `ASLEP036-10.COI-5P` | 7 July 2005 |

The locality features name sites in Area de Conservacion
Guanacaste, Costa Rica: Cuesta Caimito, Casa Potrero Grande,
Rio Azufrado, and Vado Zanja Tapada respectively.
All retain Smith's unpublished barcoding-manuscript reference
and direct-submission metadata dated 1 May 2011,
University of Guelph. The CDS protein IDs AEG77987.1 through
AEG77990.1 correspond in ascending accession order.
These are inspected GenBank feature values, not independently
validated protein functions or retrieved BOLD objects.

Specimen vouchers are not culture deposits, and four marker
submissions do not imply four distinct cultured strains or
four genome assemblies. Their presence does not contradict
the BacDive inventory count.

The closely matching-title
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, supplies study context.
Its inspected methods describe bacterial COI recovered during
insect barcoding, .w identifiers, and accession details in
Table S2. The main-text search did not find Atarnes, and
Table S2 was not inspected. No accession-specific allele,
reproductive phenotype, or host-wide prevalence is inferred.
The unpublished label is reported as GenBank metadata,
not treated as proof that no relevant publication exists.

Exact Assembly query `txid1035966[Organism:noexp]`
returned zero with phrase-not-found/no-items diagnostics.
This is a bounded indexing result, not proof of global or
historical genome absence.

## Completeness

Complete enough for an NCBI-only generated identity record.
Optional slots are appropriately empty without supported
applicable objects; `strain_count: 0` is an inventory count.

Ignored-independent search used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
Ignored, hidden, and compressed content was included.
Patterns covered the taxid, host-qualified label, slug,
all four Nuccore accessions, voucher stems, and BOLD stems.

All 20 candidate rows were read completely:

- Three describe the target backbone, scope, and native scientific name.
- GenBank `GCA_010359665.1` describes Campylobacter jejuni FSIS12027782, taxid 197; overlapping assembly digits are a collision.
- Ten ATB rows at lines 143479-143488 describe Escherichia coli samples SAMEA110359660 through SAMEA110359669.
- Six ATB rows at lines 401088-401093 describe Enterococcus cecorum samples SAMEA12751067 through SAMEA12751072; their run IDs contain the numeric substring.

The expanded marker/voucher/BOLD search returned no new rows.
Five native `SOURCE.json` files were parsed completely and
history filenames were searched independently.
No additional applicable local source assertion, culture deposit,
strain-genome link, or standalone history artifact was found
within these bounded roots. No global absence claim is made.

iModulonDB is not applicable: no regulator, expression module,
or transcriptomic dataset is asserted. COI barcode context
does not constitute expression-module evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, attestation unit, zero inventoried
BacDive strains, empty optional fields, and seed provenance
are supported.

## Recommended Edits

None required. Keep generated YAML and `mapping_status: SEEDED`
unchanged. A read-only review does not authorize status promotion
or a curation-history event.

Future source corrections belong to maintained inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope changes belong to `curation/seed_scope.tsv`.
Do not patch generated YAML/pages. Any optional enrichment
must retain exact accession and specimen scope.

## Follow-up Checks

No corrective follow-up is required. For optional publication
enrichment, inspect exact accession/voucher rows in Table S2
and authoritative BOLD records. Do not derive culture counts,
genome counts, or taxon-wide effects from these markers.

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
