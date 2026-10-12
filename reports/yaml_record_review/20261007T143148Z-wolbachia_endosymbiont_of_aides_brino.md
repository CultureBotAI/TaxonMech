# YAML Record Review: Wolbachia endosymbiont of Aides brino

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_aides_brino.yaml`
- Started UTC: 2026-10-07T14:27:29Z
- Finished UTC: 2026-10-07T14:31:48Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035963`,
Wolbachia endosymbiont of Aides brino.
This is a species-rank bacterial node with `EXACT` grounding,
`SEEDED` lifecycle, genetic code 11, 11 root-first ancestors,
one NCBI synonym, zero inventoried BacDive strains,
one NCBITAXON name attestation, and one inline seed event.
No nomenclature, mapping, strain/genome, citation, phenotype,
or causal-graph objects are asserted. Seeded fields are generated
and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_aides_brino.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_aides_brino.yaml --out /private/tmp/wol-abrino-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed source comparisons passed for identity, every ancestor label/rank/link, synonym, attestation, unique path/scope rows, and seed wording. These bounded checks do not substitute for corpus reproduction.
- Live NCBI EFetch/Datasets identity and exact Assembly/Nuccore queries were inspected. All three returned Nuccore records' metadata, features, and references were read; sequence and translation payloads were excluded.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxon identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- Not checked: independent BOLD object retrieval, sequence alignment, and the primary paper's supplementary Table S2. No claim of accession-specific experimental results from that supplement is made.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035963&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035963)
agree on the active taxid, exact label, species rank, bacterial
lineage, and parent `NCBITaxon:2640676` (unclassified Wolbachia).
EFetch confirms genetic code 11 and synonym
Wolbachia sp. Aides brino.

Complete source rows agree at `data/raw/ncbitaxon_taxa.tsv:222222`,
`data/catalog/ncbi_names-0005.jsonl.gz:31730` and line 31731,
`data/taxa/PATHS.tsv:14720`, and `curation/seed_scope.tsv:322479`.
The native names row uses the NCBI class `synonym`;
`src/taxonmech/ncbi_taxdump.py:91` maps that class to
`EXACT_SYNONYM`. This is an alternative name for the same
bacterial node, not an assertion that the host species is a
synonym of Wolbachia.

All 11 ancestor IDs, labels, ranks, and parent links match
the pinned backbone; Datasets supplies root and EFetch the
remaining labeled chain. The lineage includes Pseudomonadota,
Alphaproteobacteria, Rickettsiales, Anaplasmataceae, Wolbachieae,
and Wolbachia. The snapshot is 2026-09-13 and
`retired_into` is empty. Parsed inventories contain no
target child, type-material, merged-ID, or dropped row.

The record denotes a host-qualified NCBI bacterial node,
not the insect itself, a cultured strain, or a declaration
that every member of the host species carries the same infection.

## Evidence

The attestation counts one `NAME`, not three sequences,
three strains, infections, or genomes. Exact-target raw BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits scans
found no applicable rows. With no backbone descendants,
zero inventoried BacDive strains agrees with the inputs.
The inline seed wording matches the source inventory and scope.
Its timestamp agrees with the latest inspected extraction manifest
timestamp, `2026-09-13T17:54:04Z`, used by
`src/taxonmech/seed.py::_seed_timestamp`.

Exact Nuccore query `txid1035963[Organism:noexp]`
returned three partial bacterial COI records, all explicitly
linked to `taxon:1035963`:

| Accession | Length | Voucher | GenBank-reported BOLD cross-reference |
| --- | --- | --- | --- |
| [JN674092.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674092.1) | 383 nt | MHAHE164-05.w | ASWLP012-11.COI-5P |
| [JF902163.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902163.1) | 596 nt | `BIOUG<CAN>:MHAHE163-05.w` | ASLEP035-10.COI-5P |
| [JF902162.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902162.1) | 623 nt | `BIOUG<CAN>:MHAHE161-05.w` | ASLEP034-10.COI-5P |

The source features identify Aides brino hosts and Costa Rican
collection sites in Area de Conservacion Guanacaste.
JN674092.1 was collected on 6 April 2004 at Pasmompa;
JF902163.1 on 3 January 2005 at Sendero Rincon;
JF902162.1 on 5 October 2004 at Sendero Laguna.
All annotate translation table 11.
The corresponding CDS protein identifiers are AEQ36756.1,
AEG77984.1, and AEG77983.1 respectively.
These identifiers are inspected GenBank feature values,
not independent protein-function validation or culture deposits.

GenBank retains an unpublished Smith barcoding manuscript
reference and direct-submission metadata: 13 September 2011
for JN674092.1 and 1 May 2011 for the JF accessions.
A matching-title primary publication was verified through
[PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514)
and [PubMed PMID 22567162](https://pubmed.ncbi.nlm.nih.gov/22567162/):
Smith et al. (2012), DOI `10.1371/journal.pone.0036514`.
Its methods describe bacterial COI recovered during insect
barcoding, use of a .w specimen suffix, and accession details
in Table S2. The inspected main text does not name Aides brino;
Table S2 was not inspected. Thus the publication is relevant
study context, not verified accession-level evidence for a
particular allele, reproductive effect, or host-wide prevalence.
The GenBank manuscript status is reported as stored, not silently
rewritten or treated as proof that no publication exists.

Exact Assembly query `txid1035963[Organism:noexp]`
returned zero with phrase-not-found/no-items diagnostics.
This is a bounded indexing result, not proof that no genome
exists globally or historically. The three marker records
do not imply three cultured strains or three genome assemblies.

## Completeness

Complete enough for this generated NCBI-only identity record.
Optional slots are appropriately empty without applicable
supported objects. The external marker evidence does not
make `strain_count: 0` inconsistent: that slot counts the
inventoried BacDive strain set.

Ignored-independent search used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
Ignored, hidden, and compressed content was included.
Patterns covered the taxid, host-qualified label, slug,
all three Nuccore accessions, voucher stems, and BOLD stems.

All 15 returned candidate rows were read completely.
Four are the target backbone, scope, scientific name, and synonym.
Ten AllTheBacteria rows at lines 143449-143458 concern
Escherichia coli samples SAMEA110359630 through SAMEA110359639;
their overlapping digits are not taxonomic matches.
Line 322257 concerns Escherichia coli sample SAMEA115626259,
run ERR13115243 and assembly ERZ26446615; the numeric match
occurs only in a sequence checksum.
The expanded marker/voucher/BOLD search produced no new rows.

Five native `SOURCE.json` files were parsed completely and
history filenames were searched independently.
No additional applicable local source assertion, culture deposit,
strain-genome link, or standalone history artifact was found
within these bounded roots. No global absence claim is made.

iModulonDB is not applicable: this identity record has no
regulator, expression module, or transcriptomic dataset.
Optional COI barcoding context is not expression-module evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, synonym source/class, attestation
units, zero inventoried BacDive strains, optional omissions,
and seed provenance are supported.

## Recommended Edits

None required. Keep generated YAML and `mapping_status: SEEDED`
unchanged. This read-only review does not authorize a curation
event, history artifact, or lifecycle promotion.

Future source corrections belong to maintained inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
taxonomy name-class handling belongs to
`src/taxonmech/ncbi_taxdump.py`, and scope corrections to
`curation/seed_scope.tsv`. Do not patch generated YAML or pages.
Optional publication enrichment should first resolve the exact
accessions against the primary supplementary data.

## Follow-up Checks

No corrective follow-up is required. For optional enrichment,
inspect Table S2 and authoritative BOLD records, retain
accession versions and voucher scope, and distinguish markers,
cultures, genomes, host taxa, and infection prevalence.
Do not transfer cohort-level biological conclusions to this node.

After any separately authorized maintained-input change, rerun
the owning generator, per-file schema/strict validation, and
the repository's applicable full-corpus acceptance gates.
For a new curated history artifact, run `just validate-history`;
for new graph terms/evidence, run `just validate-products`.

## Additional Notes

The complete YAML was reread and remained byte-identical before
report creation. All bounded source commands and public data
retrievals reached terminal results. No YAML, source inventory,
curation status, standalone history, generated page, GitHub state,
branch, or worktree was changed. Eukaryota records were not
re-reviewed. Only this new timestamped report is authorized.
