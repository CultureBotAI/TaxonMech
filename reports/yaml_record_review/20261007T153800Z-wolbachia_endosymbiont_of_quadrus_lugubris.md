# YAML Record Review: Wolbachia endosymbiont of Quadrus lugubris

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_quadrus_lugubris.yaml`
- Started UTC: 2026-10-07T15:36:04Z
- Finished UTC: 2026-10-07T15:38:00Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035978`,
Wolbachia endosymbiont of Quadrus lugubris. It asserts species rank,
bacterial domain, code 11, 11 root-first ancestors, `EXACT` grounding,
`SEEDED` lifecycle, zero inventoried BacDive strains, one NCBITAXON
name attestation, and one inline seed event. No synonyms, nomenclature,
mappings, strain/genome objects, citations, phenotypes, or causal
graph are asserted. Seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_quadrus_lugubris.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_quadrus_lugubris.yaml --out /private/tmp/wol-quadrus-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed source checks passed for the complete backbone row, every ancestor label/rank/parent link, empty synonym columns, unique scope/path rows, attestation, and seed wording. These bounded checks are not corpus reproduction.
- Live NCBI EFetch XML and Datasets JSON and exact Assembly/Nuccore queries were inspected. All seven nucleotide objects' metadata/features/references were read completely, excluding sequence/translation payloads.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxonomy identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- The NCBI taxonomy browser was unavailable through the web tool; authoritative EFetch and Datasets responses were available.
- Not checked: independent BOLD/protein objects, sequence alignment, or the related primary paper's Table S2.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035978&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035978)
confirm the active exact taxid, label, species rank, bacterial lineage,
and parent `NCBITaxon:2640676` (unclassified Wolbachia).
EFetch confirms code 11. This record denotes the bacterium, not its
Quadrus host. NCBI species rank does not establish formal nomenclatural
status for the host-qualified bacterial name.

Complete pinned rows agree at `data/raw/ncbitaxon_taxa.tsv:222237`,
`data/catalog/ncbi_names-0005.jsonl.gz:31750`,
`data/taxa/PATHS.tsv:14735`, and `curation/seed_scope.tsv:322494`.
The native row is a scientific name. All pinned synonym columns are
empty, consistent with live alternate-name fields and YAML omission.
Snapshot date is 2026-09-13 and `retired_into` is empty.

Every ancestor ID, label, rank, and parent link agrees with the pinned
root-first chain. Datasets includes root; EFetch supplies the remaining
labeled chain through Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Rickettsiales, Anaplasmataceae, Wolbachieae, and Wolbachia.
Parsed inventories contain no target child, type-material, merged-ID,
or dropped row. `EXACT` grounding does not promote `SEEDED` lifecycle.

## Evidence

The NCBITAXON attestation counts one `NAME`, not specimens, sequences,
infections, cultures, or genomes. Exact-target scans of raw BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories found
no applicable rows. With no backbone descendants, zero inventoried
BacDive strains agrees with the source inputs without implying
absence of biological strains or infections.

Inline seed wording matches the scope row and attestation.
The `2026-09-13T17:54:04Z` timestamp equals the latest inspected raw,
ATB, and StrainInfo extraction timestamp, following
`src/taxonmech/seed.py::_seed_timestamp`.

Exact Nuccore query `txid1035978[Organism:noexp]` returned seven
partial COI records. Each explicitly identifies `taxon:1035978`,
the target bacterial organism, and host Quadrus lugubris.
All are 657 nt, use codon start 1 and translation table 11,
and report collections in Area de Conservacion Guanacaste,
Guanacaste, Costa Rica:

| Accession | Specimen voucher | GenBank-reported BOLD cross-reference | Collection date | Locality |
| --- | --- | --- | --- | --- |
| [JF902230.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902230.1) | `BIOUG<CAN>:MHAHD355-05.w` | `ASLEP024-10.COI-5P` | 10-Jan-2004 | Cafetal, Sector Santa Rosa |
| [JF902231.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902231.1) | `BIOUG<CAN>:MHAHD356-05.w` | `ASLEP025-10.COI-5P` | 07-Apr-2004 | Cuesta Caimito, Sector Cacao |
| [JF902232.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902232.1) | `BIOUG<CAN>:MHAHD359-05.w` | `ASLEP026-10.COI-5P` | 16-Apr-2004 | Gongora Bananal, Sector Cacao |
| [JF902233.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902233.1) | `BIOUG<CAN>:MHAHD360-05.w` | `ASLEP027-10.COI-5P` | 25-Apr-2004 | Estacion Cacao, Sector Cacao |
| [JF902234.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902234.1) | `BIOUG<CAN>:MHAHD361-05.w` | `ASLEP028-10.COI-5P` | 19-Aug-2004 | Gongora Bananal, Sector Cacao |
| [JF902235.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902235.1) | `BIOUG<CAN>:MHAHD362-05.w` | `ASLEP029-10.COI-5P` | 07-Jun-2004 | Estacion Gongora, Sector Cacao |
| [JF902236.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902236.1) | `BIOUG<CAN>:MHAHF763-06.w` | `ASLEP043-10.COI-5P` | 30-Jan-2006 | Quebrada Trigal, Sector Del Oro |

Primer, collector, identifier, coordinate, and protein qualifiers
were also inspected as GenBank data. Protein cross-references run
from `AEG78051.1` through `AEG78057.1` in accession order.
Independent BOLD/protein objects were not retrieved. Shared marker
length, host, or taxid does not prove sequence, strain, or genome
equivalence among these specimens.

All seven retain an unpublished Smith manuscript reference and a
direct submission dated 1 May 2011 at the University of Guelph.
The related
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, describes Wolbachia COI recovered
during insect barcoding, bacterial `.w` sample IDs, and accession
details in Table S2. Main-text search did not match Quadrus; the
supplement was not inspected. The paper supplies methodological
context, not an inspected exact-target allele, prevalence, or
reproductive-phenotype assignment. GenBank's unpublished labels are
retained as stored, not interpreted as absence of a relevant publication.

Exact Assembly query `txid1035978[Organism:noexp]` returned zero
with phrase-not-found/no-items diagnostics. This bounded index result
does not prove global or historical genome absence.
The COI markers are not seven cultured strains or assemblies;
specimen vouchers are not culture deposits. They establish neither
a missing strain-genome link nor a contradictory inventoried strain count.

## Completeness

Complete enough for its generated NCBI-only identity purpose.
Optional nomenclature, mappings, strain/genome objects, and causal
claims are appropriately unasserted on the inspected evidence.

Ignored-independent search used `rg --no-ignore --hidden -n -z -i`
across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`, including ignored, hidden, and compressed
content. Patterns covered taxid, label, slug, and all seven marker,
specimen-voucher, and BOLD stems listed above.

All 15 candidate rows were fully read:

- Three describe the target backbone, scope, and native scientific name.
- One describes Campylobacter jejuni PNUSAC014845, taxid 197, GCA_010359785.1, at `data/catalog/ncbi_genbank-0009.jsonl.gz:6815`. Accession digits cause the match, not taxonomic identity.
- Ten ATB rows at lines 143599-143608 describe Escherichia coli samples SAMEA110359780 through SAMEA110359789. Their sample digits cause false matches.
- One ATB row at line 1716049 describes Salmonella enterica sample SAMN13152860, assembly ERZ25671887, and run SRR10359785. The run digits cause the match. None of these foreign objects supports target taxonomic or strain-link evidence.

Expanded marker/voucher/BOLD search added no rows. Five native
`SOURCE.json` files were parsed completely and history filenames
searched independently. No additional applicable local assertion,
culture deposit, strain-genome link, or standalone history artifact
was found within these bounded roots. No global absence is claimed.

iModulonDB is not applicable: no regulator, expression module, or
transcriptomic dataset is asserted. Optional COI barcoding evidence
does not establish an expression-module claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, empty synonym fields, one-name
attestation, inventoried strain count, optional omissions, and seed
provenance are supported. Additional exact-taxid markers are compatible
with the generated record without establishing missing genome links.

## Recommended Edits

None required. Preserve generated YAML and `mapping_status: SEEDED`.
No status promotion or curation-history event is authorized by this review.
Future source corrections belong to maintained upstream inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`; scope changes belong
to `curation/seed_scope.tsv`. Do not patch generated YAML/pages.

## Follow-up Checks

No corrective follow-up is required. Before optional marker enrichment,
inspect Table S2 and exact accession-level primary evidence, keeping
specimen, marker, strain, and assembly identities separate.
After separately authorized maintained-input changes, rerun the owning
generator, per-file schema/strict validation, and applicable full-corpus
acceptance gates. New curated history requires `just validate-history`;
new graph terms/evidence require `just validate-products`.

## Additional Notes

The entire YAML was reread and remained byte-identical before report
creation. All bounded local reads and public retrievals reached terminal
results. No YAML, source inventory, lifecycle, standalone history,
generated page, GitHub state, branch, or worktree was changed.
Eukaryota records were not re-reviewed. Only this new timestamped
report was written for this target.
