# YAML Record Review: Wolbachia endosymbiont of Macrosoma cascaria

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_macrosoma_cascaria.yaml`
- Started UTC: 2026-10-07T15:09:55Z
- Finished UTC: 2026-10-07T15:11:41Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for
`NCBITaxon:1035972`, Wolbachia endosymbiont of Macrosoma cascaria.
It asserts species rank, bacterial domain, code 11,
11 root-first ancestors, `EXACT` grounding, `SEEDED` lifecycle,
zero inventoried BacDive strains, one NCBITAXON name
attestation, and one inline seed event.
No synonyms, nomenclature, mappings, strain/genome objects,
citations, phenotypes, or causal graph are asserted.
Seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_macrosoma_cascaria.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_macrosoma_cascaria.yaml --out /private/tmp/wol-mcasc-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Bounded parsed source checks passed for identity, each ancestor label/rank/link, empty synonym columns, attestation, unique scope/path rows, and seed wording. These checks are not corpus reproduction.
- Live NCBI EFetch/Datasets taxonomy, exact Assembly/Nuccore searches, and full metadata/features/references of the sole returned nucleotide object were inspected. Sequence/translation payloads were excluded.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxonomy identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- The NCBI taxonomy browser was unavailable through the web tool; authoritative EFetch XML and Datasets JSON were available.
- Not checked: independent BOLD/protein objects, sequence alignment, or the related primary paper's Table S2.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035972&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035972)
confirm the active exact taxid, label, species rank,
bacterial lineage, and parent `NCBITaxon:2640676`
(unclassified Wolbachia). EFetch confirms code 11.
This is the bacterial taxon associated with the named host,
not the host organism or an asserted equivalent of another
host-qualified Wolbachia node.

Complete source rows agree at
`data/raw/ncbitaxon_taxa.tsv:222231`,
`data/catalog/ncbi_names-0005.jsonl.gz:31743`,
`data/taxa/PATHS.tsv:14729`, and
`curation/seed_scope.tsv:322488`.
The native scientific name, empty pinned synonym columns,
and live alternate-name fields support omission of synonyms.

Every ancestor ID, label, rank, and parent link agrees with
the pinned root-first chain. Datasets includes root;
EFetch supplies the remaining labeled chain, including
Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Rickettsiales, Anaplasmataceae, Wolbachieae, and Wolbachia.
Snapshot date is 2026-09-13 and `retired_into` is empty.
Parsed inventories contain no target child, type-material,
merged-ID, or dropped row.

## Evidence

The attestation counts one `NAME`, not a specimen,
infection, culture, sequence, or genome. Exact-target
scans of raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin,
and BactoTraits inventories found no applicable rows.
With no backbone descendants, zero inventoried BacDive
strains agrees with the source inputs.

The inline seed wording matches scope and attestation.
Its timestamp `2026-09-13T17:54:04Z` is the latest
inspected raw, ATB, and StrainInfo extraction timestamp,
following `src/taxonmech/seed.py::_seed_timestamp`.
It is not manual review or biological observation time.
`EXACT` grounding remains distinct from `SEEDED` lifecycle.

Exact Nuccore query `txid1035972[Organism:noexp]`
returned [JF902212.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902212.1),
a 644-nt partial COI record explicitly assigned to
`taxon:1035972`, with host Macrosoma cascaria.
It gives voucher `BIOUG<CAN>:MHMYA441-09.w`,
BOLD cross-reference `ASLEP072-10.COI-5P`, and
collection on 3 December 2007 at Roca Verde,
Sector Cacao, Guanacaste, Costa Rica.

The gene and CDS are partial at both ends.
CDS qualifiers specify codon start 1, translation table 11,
and protein ID AEG78033.1.
Full non-payload metadata, primer qualifiers, references,
and collection features were inspected.
The record retains a Smith barcoding-manuscript reference
labeled unpublished and direct submission dated
1 May 2011 at the University of Guelph.
BOLD/protein cross-references were read as GenBank values,
not independently retrieved objects or experimental
functional evidence.

[Smith et al.'s related primary paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514)
provides barcoding context; its main text does not match
Macrosoma. Table S2 was not inspected.
No accession-specific literature claim, allele identity,
prevalence, or reproductive phenotype is inferred.
The stored unpublished label is not proof of publication absence.

The voucher is not a culture deposit and the partial marker
is not a genome assembly. Neither contradicts
`strain_count: 0` or the one-name attestation.
Exact Assembly query `txid1035972[Organism:noexp]`
returned zero with phrase-not-found/no-items diagnostics.
This bounded indexing result is not global genome absence.

## Completeness

Complete enough for its generated NCBI-only identity purpose.
Optional fields are appropriately empty without applicable
supported objects; the external marker does not require
inventing a culture or genome relationship.

Ignored-independent search used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
It included ignored, hidden, and compressed content.
Patterns covered taxid, host-qualified label, slug,
JF902212, MHMYA441-09, and ASLEP072-10.

All 15 candidate rows were read completely:

- Three describe the target backbone, scope, and native scientific name.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6812` describes Campylobacter jejuni PNUSAC009941, taxid 197, assembly GCA_010359725.1. Its accession digits are a collision.
- `data/catalog/ncbi_genbank-0065.jsonl.gz:16014` describes an uncultured bacterium, taxid 77133, isolate MarMAG_015220, assembly GCA_977675845.1. The match 1035972 is its ungapped genome size, not the target taxid.
- Ten ATB rows at lines 143539-143548 describe Escherichia coli samples SAMEA110359720 through SAMEA110359729. Matching digits are not taxonomic evidence.

The expanded marker/voucher/BOLD search returned no new rows.
Five native `SOURCE.json` files were parsed completely and
history filenames searched independently.
No additional applicable local assertion, culture deposit,
strain-genome link, or standalone history artifact was found
within these bounded roots. No global absence is claimed.

iModulonDB is not applicable: no regulator, expression
module, or transcriptomic dataset is asserted.
Optional COI barcoding context is not expression evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, empty synonym fields,
attestation unit, inventory count, optional omissions,
and seed provenance are supported.

## Recommended Edits

None required. Preserve generated YAML and
`mapping_status: SEEDED`; this review does not authorize
lifecycle promotion or a curation-history event.

Future source corrections belong to maintained upstream
inputs and `src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope changes belong to `curation/seed_scope.tsv`.
Do not patch generated YAML/pages.
Optional enrichment must retain exact taxid, accession
version, and voucher scope without inventing culture
or genome equivalence.

## Follow-up Checks

No corrective follow-up is required.
Before optional literature enrichment, inspect Table S2
and reconcile its accession with current taxonomy.
Independently resolve BOLD/protein objects when a proposed
claim relies on them; align sequences before allele claims.

After separately authorized maintained-input changes,
rerun the owning generator, per-file schema/strict checks,
and applicable full-corpus acceptance gates.
New curated history requires `just validate-history`;
new graph terms/evidence require `just validate-products`.

## Additional Notes

The complete YAML was reread and remained byte-identical
before report creation. All bounded local reads and public
retrievals reached terminal results.
No YAML, source inventory, lifecycle, standalone history,
generated page, GitHub state, branch, or worktree was changed.
Eukaryota records were not re-reviewed.
Only this new timestamped report was written for this target.

