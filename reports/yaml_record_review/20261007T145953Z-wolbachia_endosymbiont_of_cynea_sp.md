# YAML Record Review: Wolbachia endosymbiont of Cynea sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_cynea_sp.yaml`
- Started UTC: 2026-10-07T14:56:56Z
- Finished UTC: 2026-10-07T14:59:53Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for
`NCBITaxon:1035969`, Wolbachia endosymbiont of Cynea sp.
It asserts species rank, bacterial domain, code 11,
11 root-first ancestors, `EXACT` grounding, `SEEDED` lifecycle,
zero inventoried BacDive strains, one NCBITAXON name
attestation, and one inline seed event. It asserts no
synonyms, nomenclature, mappings, strain/genome objects,
citations, phenotypes, or causal graph.
Seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_cynea_sp.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_cynea_sp.yaml --out /private/tmp/wol-cynea-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Bounded parsed source checks passed for identity, every ancestor label/rank/link, empty synonym columns, attestation, unique scope/path rows, and seed wording. These checks are not corpus reproduction.
- Live NCBI EFetch/Datasets taxonomy was inspected for the target and distinct Cynea Burns07 node. Exact Assembly/Nuccore searches and a broader name search were inspected; full metadata/features/references of its three sequence candidates were read, excluding sequence/translation payloads.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxonomy terms were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- The target NCBI browser page was unavailable through the web tool; authoritative EFetch XML and Datasets JSON were available.
- Not checked: historical sequence reassignment, independent BOLD/protein objects, alignments, or the primary paper's Table S2.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035969&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035969)
confirm the active exact taxid, label, species rank, bacterial
lineage, and parent `NCBITaxon:2640676`
(unclassified Wolbachia). EFetch confirms code 11.
The species rank belongs to this NCBI bacterial node;
it neither resolves the host's unspecified species nor
asserts a formally established nomenclatural name.

Complete source rows agree at
`data/raw/ncbitaxon_taxa.tsv:222228`,
`data/catalog/ncbi_names-0005.jsonl.gz:31740`,
`data/taxa/PATHS.tsv:14726`, and
`curation/seed_scope.tsv:322485`.
The native name is a scientific name; pinned synonym
columns and live alternate-name fields supply no synonym.

Every ancestor ID, label, rank, and parent link agrees with
the pinned root-first chain. Datasets includes root;
EFetch supplies the remaining labeled chain through
Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Rickettsiales, Anaplasmataceae, Wolbachieae, and Wolbachia.
The snapshot is dated 2026-09-13 and `retired_into` is empty.
Parsed inventories contain no target child, type-material,
merged-ID, or dropped row.

A separate active species node,
[NCBITaxon:1094255](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1094255&retmode=xml),
is Wolbachia endosymbiont of Cynea Burns07.
Full EFetch/Datasets responses and pinned rows
`data/raw/ncbitaxon_taxa.tsv:235301`,
`curation/seed_scope.tsv:333614`, and
`data/catalog/ncbi_names-0005.jsonl.gz:47530`
confirm that distinct identity under the same parent.
Shared host-name text or parentage does not establish
equivalence. No merge or synonym relationship is asserted.

## Evidence

The attestation counts one NCBITAXON `NAME`, not a
sequence, specimen, culture, genome, or infection.
Exact-target scans of raw BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin, and BactoTraits inventories found no
applicable rows. With no backbone descendants, zero
inventoried BacDive strains agrees with the pinned inputs.

The inline seed wording matches scope and inventories.
Its timestamp `2026-09-13T17:54:04Z` equals the latest
extraction timestamp in the fully read raw, ATB, and
StrainInfo manifests, following
`src/taxonmech/seed.py::_seed_timestamp`.
`EXACT` grounding does not promote the `SEEDED` lifecycle.

Both exact queries `txid1035969[Organism:noexp]`
returned zero, in Assembly and Nuccore, with
phrase-not-found/no-items diagnostics.
These are bounded indexing results, not proof of global
or historical sequence/genome absence or taxon invalidity.

Broader Nuccore search
`Wolbachia[Organism] AND Cynea[All Fields]`
returned three partial COI records. Full inspection shows
that all carry organism Wolbachia endosymbiont of Cynea
Burns07 and `taxon:1094255`, although their host qualifier
is Cynea sp. They are not exact-target sequence evidence.

| Candidate accession | Length (nt) | Specimen voucher | GenBank-reported BOLD cross-reference |
| --- | --- | --- | --- |
| [JF902192.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902192.1) | 625 | `BIOUG<CAN>:MHAHE600-06.w` | `ASLEP037-10.COI-5P` |
| [JF902193.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902193.1) | 536 | `BIOUG<CAN>:MHAHE601-06.w` | `ASLEP038-10.COI-5P` |
| [JF902194.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902194.1) | 596 | `BIOUG<CAN>:MHAHE687-06.w` | `ASLEP040-10.COI-5P` |

The candidate metadata gives Costa Rican collections,
translation table 11, codon start 1, a Smith manuscript
reference labeled unpublished, and direct submission on
1 May 2011 at the University of Guelph.
These are inspected candidate values, not claims about
the target. BOLD/protein cross-references were not
independently retrieved. A host qualifier is not a
taxonomic synonym; a voucher is not a culture deposit;
a partial marker is not a genome assembly.

The related
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, supplies methodological
context for bacterial COI recovered during insect barcoding
and refers accession details to Table S2.
The main text did not match Cynea, and the supplement was
not inspected. No exact-target allele, prevalence,
reproductive phenotype, or historical reassignment is
inferred. GenBank's unpublished label is retained as stored,
not interpreted as absence of a relevant publication.

## Completeness

Complete enough for its generated NCBI-only identity purpose.
The empty sequence query is not a reason to invent
strain/genome links or delete an active taxonomy record.
No consequential missing required object was found.

Ignored-independent search used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
It included hidden, ignored, and compressed content.
Initial patterns covered taxid, label, and slug; expansion
covered Cynea generally and all three candidate nucleotide,
voucher, and BOLD stems.

All 17 candidate rows were fully read:

- Three describe the target backbone, scope, and scientific name.
- Three describe the distinct Cynea Burns07 backbone, scope, and scientific name.
- Ten ATB rows at lines 143509-143518 describe Escherichia coli samples SAMEA110359690 through SAMEA110359699; matching digits are not taxonomic evidence.
- ATB line 2502931 describes Salmonella enterica, sample SAMN32471709, run SRR22927493, assembly ERZ26248064. The match is inside its seqkit checksum, not its taxonomic identity.

The accession/voucher/BOLD expansion returned no additional
rows. Five native `SOURCE.json` files were parsed completely,
and history filenames were searched independently.
No additional applicable local assertion, culture deposit,
strain-genome link, or standalone history artifact was found
within the bounded roots. No global absence is claimed.

iModulonDB is not applicable: no regulator, expression
module, or transcriptomic dataset is asserted. Candidate
COI barcoding evidence is not expression-module evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, rank/domain, lineage, empty synonym
fields, one-name attestation, inventory count, optional
omissions, and seed provenance are supported.
The broader sequence hits belong to a distinct taxon and
do not establish a missing target linkage.

## Recommended Edits

None required. Preserve generated YAML and
`mapping_status: SEEDED`; do not append a curation event
or promote status as part of this read-only review.

Future source corrections belong to maintained upstream
inputs and `src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope changes belong to `curation/seed_scope.tsv`.
Do not patch generated YAML/pages.
Any proposed equivalence with Cynea Burns07 requires
explicit authority evidence, not just matching host text.

## Follow-up Checks

No corrective follow-up is required.
Before optional enrichment, resolve exact organism taxids
and inspect accession-level primary evidence.
Historical accession/taxonomy records and Table S2 would be
needed before claiming a reassignment or linking the two
Cynea-qualified nodes. The current checks establish only
their present separate identities.

After separately authorized maintained-input changes, rerun
the owning generator, per-file schema/strict validation,
and applicable full-corpus acceptance gates.
New curated history requires `just validate-history`;
new graph terms/evidence require `just validate-products`.

## Additional Notes

The complete YAML was reread and remained byte-identical
before report creation. All bounded local reads and public
retrievals reached terminal results.
No YAML, source inventory, lifecycle, standalone history,
generated page, GitHub state, branch, or worktree was
changed. Eukaryota records were not re-reviewed.
Only this new timestamped report was written for this target.

