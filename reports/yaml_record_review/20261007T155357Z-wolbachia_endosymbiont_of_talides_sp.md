# YAML Record Review: Wolbachia endosymbiont of Talides sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_talides_sp.yaml`
- Started UTC: 2026-10-07T15:51:14Z
- Finished UTC: 2026-10-07T15:53:57Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035981`,
Wolbachia endosymbiont of Talides sp. It asserts species rank,
bacterial domain, parent 2640676, code 11, 11 root-first ancestors,
`EXACT` grounding, `SEEDED` lifecycle, zero inventoried BacDive strains,
one NCBITAXON name attestation, and one inline seed event.
No synonyms, nomenclature, mappings, strain/genome objects, citations,
phenotypes, or causal graph are asserted. Seeded fields are read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_talides_sp.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_talides_sp.yaml --out /private/tmp/wol-talides-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed comparisons passed for the full backbone row, every ancestor label/rank/parent link, empty synonym columns, unique scope/path rows, attestation, and seed wording. These bounded checks do not reproduce the corpus.
- Live NCBI EFetch XML and Datasets JSON were read for the target and both neighboring taxa. Exact Assembly/Nuccore and broader Talides Nuccore queries were inspected. Both nucleotide objects' metadata/features/references were read completely, excluding sequence/translation payloads.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxonomy IDs and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- The NCBI taxonomy browser was unavailable through the web tool; authoritative EFetch and Datasets responses were available.
- Not checked: independent BOLD/protein objects, sequence alignment, historical accession reassignment, or the related primary paper's Table S2.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035981&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035981)
confirm the active exact taxid, label, species rank, bacterial lineage,
and parent `NCBITaxon:2640676`, unclassified Wolbachia. EFetch confirms
code 11. This denotes the bacterium, not a Talides host; NCBI species
rank does not establish formal nomenclatural status for this name.

Complete pinned rows agree at `data/raw/ncbitaxon_taxa.tsv:222240`,
`data/catalog/ncbi_names-0005.jsonl.gz:31753`,
`data/taxa/PATHS.tsv:14738`, and `curation/seed_scope.tsv:322497`.
The native row is a scientific name with empty unique name. Backbone
synonym columns and live alternate-name fields are empty, consistent
with YAML omission. Snapshot date is 2026-09-13; `retired_into` is empty.

Every ancestor ID, label, rank, and parent link agrees with the pinned
root-first chain. Datasets includes root; EFetch supplies the remaining
labeled chain through Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Rickettsiales, Anaplasmataceae, Wolbachieae, Wolbachia, and unclassified
Wolbachia. Parsed inventories contain no target child, type-material,
merged-ID, or dropped row. `EXACT` grounding does not promote `SEEDED` lifecycle.

Separate EFetch and Datasets responses confirm active neighboring species:
[NCBITaxon:1094265, Talides Burns01](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1094265),
and [NCBITaxon:1035982, Talides sinois](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035982).
They share the parent and code 11 but are not established aliases of
the reviewed taxid. Host naming and current date fields alone do not
prove equivalence or historical sequence reassignment.

## Evidence

The NCBITAXON attestation counts one `NAME`, not specimens, infections,
cultures, sequences, or genomes. Exact-target scans of raw BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories found
no applicable rows. With no backbone descendants, zero inventoried
BacDive strains agrees with the inputs without implying biological
absence of strains or infections.

Inline seed wording matches the scope row and attestation. Its
`2026-09-13T17:54:04Z` timestamp equals the latest inspected raw, ATB,
and StrainInfo extraction timestamp, following
`src/taxonmech/seed.py::_seed_timestamp`.

Exact Assembly and Nuccore queries `txid1035981[Organism:noexp]`
each returned zero with phrase-not-found/no-items diagnostics.
These bounded index results do not prove global or historical absence.
The broader query `Wolbachia[Organism] AND Talides[All Fields]` returned
two partial COI objects, neither assigned to taxid 1035981:

| Accession | Bacterial taxid / label suffix | Host qualifier | Length | Specimen voucher | GenBank-reported BOLD cross-reference |
| --- | --- | --- | --- | --- | --- |
| [JF902248.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902248.1) | 1094265 / Talides Burns01 | Talides sp. | 614 nt | `BIOUG<CAN>:CSRII486-04.w` | `ASLEP010-10.COI-5P` |
| [JF902249.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902249.1) | 1035982 / Talides sinois | Talides sinois | 646 nt | `BIOUG<CAN>:MHAHL310-07.w` | `ASLEP064-10.COI-5P` |

Both use codon start 1 and translation table 11. Protein qualifiers
are AEG78069.1 and AEG78070.1 respectively. JF902248.1 reports collection
on 7 March 2002 by Harry Ramirez at Sendero Circular, Sector Cacao,
Area de Conservacion Guanacaste, Guanacaste, Costa Rica, coordinates
10.927 N, 85.467 W. JF902249.1 reports only Costa Rica, without a
collection date or finer locality. Primer and identification qualifiers
were also inspected. Independent BOLD/protein objects were not retrieved.

The Talides sp. host qualifier on JF902248.1 does not override its
explicit bacterial taxid 1094265. Neither specimen, sequence, locality,
protein, or putative phenotype is transferred to the reviewed taxon.
Markers are not genome assemblies, and vouchers are not culture deposits.

Both GenBank objects retain a Smith unpublished manuscript reference
and direct submission dated 1 May 2011 at the University of Guelph.
The related
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, describes Wolbachia COI recovered
during insect barcoding, `.w` sample IDs, and accessions in Table S2.
The main text did not match Talides; Table S2 was not inspected.
This provides methodological context, not an inspected exact-target
allele, prevalence, or reproductive-phenotype assignment. GenBank's
unpublished labels are not evidence that no related publication exists.

## Completeness

Complete enough for its generated NCBI-only identity purpose.
Optional nomenclature, mappings, strain/genome objects, and causal
claims are appropriately unasserted on the inspected evidence.

Ignored-independent search used `rg --no-ignore --hidden -n -z -i`
across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`, including ignored, hidden, and compressed
content. Patterns covered taxid, label, slug, broader Wolbachia/Talides
combinations, JF902248/JF902249, CSRII486-04/MHAHL310-07, and
ASLEP010-10/ASLEP064-10.

All 21 candidate rows were fully read:

- Three describe the target backbone, scope, and native scientific name.
- Six concern the two distinct neighboring taxa: Talides sinois at backbone line 222241, scope line 322498, native-name line 31754; Talides Burns01 at backbone line 235311, scope line 333624, native-name line 47540. Both native names are in `ncbi_names-0005.jsonl.gz`. These rows do not establish target synonyms.
- Ten ATB rows at lines 143629-143638 describe Escherichia coli samples SAMEA110359810 through SAMEA110359819. Sample digits cause the matches.
- One ATB row at line 549319 describes Klebsiella pneumoniae sample SAMEA3357198, assembly ERZ3256718, and run ERR1035981. The run ID is a numeric collision.
- One ATB row at line 1072957 describes Salmonella enterica sample SAMN03289431, assembly ERZ4099026, and run SRR1996157. Its SeqKit sum contains the taxid digits; it is not target taxonomy or strain evidence.

Expanded marker/voucher/BOLD search added no rows. Five native
`SOURCE.json` files were parsed completely and history filenames
searched independently. No additional applicable local assertion,
culture deposit, strain-genome link, or standalone target history
artifact was found within these bounded roots. No global absence is claimed.

iModulonDB is not applicable: no regulator, expression module, or
transcriptomic dataset is asserted. Neighboring COI barcoding objects
do not establish an expression-module claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, empty synonym fields, one-name attestation,
inventoried strain count, optional omissions, and seed provenance are
supported. Broader sequence candidates resolve to separate bacterial
taxids and do not establish missing target genome links.

## Recommended Edits

None required. Preserve generated YAML and `mapping_status: SEEDED`.
No status promotion or curation-history event is authorized by this review.
Future source corrections belong to maintained upstream inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`; scope changes belong
to `curation/seed_scope.tsv`. Do not patch generated YAML/pages.

## Follow-up Checks

No corrective follow-up is required. A proposed linkage to Talides
Burns01 or Talides sinois requires explicit authority or accession-level
evidence, not shared host wording. Optional marker enrichment should
inspect Table S2 without importing neighboring-taxon claims.
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
